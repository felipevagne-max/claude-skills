#!/usr/bin/env python3
"""Validate the artifacts produced by a Black Copy Chief run."""

import argparse
from datetime import datetime
import hashlib
import json
import os
from pathlib import Path
import re
import sys
import tempfile
import zipfile


REQUIRED_BIBLE_FIELDS = (
    "piece_type",
    "audience",
    "emotional_state",
    "awareness",
    "sophistication",
    "current_belief",
    "target_belief",
    "one_belief",
    "accepted_premise",
    "single_villain",
    "root_cause",
    "broken_process",
    "solution_mechanism",
    "central_promise",
    "promise_boundary",
    "dominant_emotion",
    "argument_chain",
    "proof_ledger",
    "objections",
    "known_facts",
    "assumptions",
    "open_gaps",
)

STAGE_FILES = {
    "argument": (
        "01-intake.md",
        "02-prospect-mind-map.md",
        "03-argument-bible.md",
    ),
    "routes": (
        "01-intake.md",
        "02-prospect-mind-map.md",
        "03-argument-bible.md",
        "04-creative-routes.md",
    ),
    "draft": (
        "01-intake.md",
        "02-prospect-mind-map.md",
        "03-argument-bible.md",
        "04-creative-routes.md",
        "05-draft-1.md",
    ),
    "review": (
        "01-intake.md",
        "02-prospect-mind-map.md",
        "03-argument-bible.md",
        "04-creative-routes.md",
        "05-draft-1.md",
        "06-kill-room.md",
    ),
    "final": (
        "01-intake.md",
        "02-prospect-mind-map.md",
        "03-argument-bible.md",
        "04-creative-routes.md",
        "05-draft-1.md",
        "06-kill-room.md",
        "07-final.md",
        "manifest.json",
    ),
}

REQUIRED_MANIFEST_KEYS = (
    "project",
    "piece_type",
    "mode",
    "status",
    "artifacts",
)

MANIFEST_STATUSES = ("provisional", "publish-ready")

ACTIVE_STAGE_FILES = {
    "argument": ("03-argument-bible.md",),
    "routes": ("04-creative-routes.md",),
    "draft": ("05-draft-1.md",),
    "review": ("06-kill-room.md",),
    "final": ("03-argument-bible.md", "07-final.md"),
}

CANONICAL_MODES = ("CREATE", "MODEL", "REWRITE", "KILL ROOM", "ROUTES")

MODE_STAGE_FILES = {
    "CREATE": STAGE_FILES,
    "MODEL": STAGE_FILES,
    "ROUTES": {
        "argument": STAGE_FILES["argument"],
        "routes": (*STAGE_FILES["routes"], "manifest.json"),
    },
    "REWRITE": {
        "draft": (
            "01-intake.md",
            "02-prospect-mind-map.md",
            "03-argument-bible.md",
            "05-draft-1.md",
        ),
        "review": (
            "01-intake.md",
            "02-prospect-mind-map.md",
            "03-argument-bible.md",
            "05-draft-1.md",
            "06-kill-room.md",
        ),
        "final": (
            "01-intake.md",
            "02-prospect-mind-map.md",
            "03-argument-bible.md",
            "05-draft-1.md",
            "06-kill-room.md",
            "07-final.md",
            "manifest.json",
        ),
    },
    "KILL ROOM": {
        "review": (
            "01-intake.md",
            "03-argument-bible.md",
            "05-draft-1.md",
            "06-kill-room.md",
            "manifest.json",
        ),
    },
}

PLACEHOLDER_PATTERN = re.compile(
    r"(?i:\[PROVA NECESSÁRIA\]|\[INSERIR[^\]]*\]|\[EXPERT:[^\]]*\])"
    r"|\b(?:TBD|TODO)\b",
)

BIBLE_VERSION_PATTERN = re.compile(r"^version\s*:\s*['\"]?([1-9]\d*)['\"]?\s*$", re.MULTILINE)
BIBLE_CREATED_AT_PATTERN = re.compile(
    r"^created_at\s*:\s*['\"]?"
    r"(\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}(?:Z|[+-]\d{2}:\d{2}))"
    r"['\"]?\s*$",
    re.MULTILINE,
)
BIBLE_APPROVAL_PATTERN = re.compile(
    r"^approved_by_chief\s*:\s*true\s*$",
    re.IGNORECASE | re.MULTILINE,
)
PUBLISH_READY_HASH_KEYS = ("argument_bible", "final_markdown", "final_docx")
FROZEN_INPUT_CANONICAL_PATHS = {
    "argument_bible": "03-argument-bible.md",
    "draft_1": "05-draft-1.md",
    "final_markdown": "07-final.md",
    "final_docx": "07-final.docx",
}
DOCX_REQUIRED_ENTRIES = {"[Content_Types].xml", "word/document.xml"}


def _normalize_mode(mode):
    if not isinstance(mode, str):
        return None

    normalized = re.sub(r"[\s_-]+", " ", mode.strip().upper())
    if normalized in CANONICAL_MODES:
        return normalized
    return None


def _read_text(path, errors):
    try:
        return path.read_text(encoding="utf-8")
    except (OSError, UnicodeError) as exc:
        message = f"Unable to read {path}: {exc}"
        if message not in errors:
            errors.append(message)
        return None


def _validate_bible(path, errors):
    if not path.is_file():
        return

    text = _read_text(path, errors)
    if text is None:
        return

    for field in REQUIRED_BIBLE_FIELDS:
        if not re.search(rf"^{re.escape(field)}\s*:", text, re.MULTILINE):
            errors.append(f"Argument Bible missing required field: {field}")

    if not BIBLE_VERSION_PATTERN.search(text):
        errors.append("Argument Bible missing valid positive integer version")
    created_at_match = BIBLE_CREATED_AT_PATTERN.search(text)
    if not created_at_match:
        errors.append("Argument Bible missing valid ISO 8601 created_at")
    else:
        try:
            datetime.fromisoformat(created_at_match.group(1).replace("Z", "+00:00"))
        except ValueError:
            errors.append("Argument Bible missing valid ISO 8601 created_at")
    if not BIBLE_APPROVAL_PATTERN.search(text):
        errors.append("Argument Bible missing approved_by_chief: true")


def _sha256(path):
    digest = hashlib.sha256()
    with path.open("rb") as artifact_file:
        for chunk in iter(lambda: artifact_file.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def _validate_docx(path, errors):
    if not path.is_file() or path.is_symlink():
        errors.append("Missing required artifact: 07-final.docx")
        return

    try:
        with zipfile.ZipFile(path) as archive:
            names = set(archive.namelist())
            missing = sorted(DOCX_REQUIRED_ENTRIES - names)
            if missing:
                errors.append(
                    "07-final.docx is not a valid DOCX; missing entries: "
                    + ", ".join(missing)
                )
                return
            damaged = archive.testzip()
            if damaged is not None:
                errors.append(
                    f"07-final.docx is not a valid DOCX; damaged entry: {damaged}"
                )
    except (OSError, zipfile.BadZipFile) as exc:
        errors.append(f"07-final.docx is not a valid DOCX archive: {exc}")


def _validate_frozen_inputs(manifest, run_path, artifacts, errors):
    frozen_inputs = manifest.get("frozen_inputs")
    publish_ready = manifest.get("status") == "publish-ready"

    if frozen_inputs is None:
        if publish_ready:
            errors.append("Publish-ready manifest missing frozen_inputs checksums")
        return
    if not isinstance(frozen_inputs, dict):
        errors.append("Manifest frozen_inputs must be an object")
        return

    if publish_ready:
        for key in PUBLISH_READY_HASH_KEYS:
            if key not in frozen_inputs:
                errors.append(f"Publish-ready manifest missing frozen_inputs.{key}")

    for key, record in frozen_inputs.items():
        if not isinstance(record, dict):
            errors.append(f"Manifest frozen_inputs.{key} must be an object")
            continue
        artifact = record.get("path")
        expected = record.get("sha256")
        canonical_path = FROZEN_INPUT_CANONICAL_PATHS.get(key)
        if canonical_path is not None and artifact != canonical_path:
            errors.append(
                f"Manifest frozen_inputs.{key}.path must use canonical path "
                f"{canonical_path}"
            )
        artifact_path, containment_error = _contained_artifact_path(run_path, artifact)
        if containment_error:
            errors.append(
                f"Manifest frozen_inputs.{key}.path: {containment_error}"
            )
            continue
        if artifact not in artifacts:
            errors.append(
                f"Manifest frozen_inputs.{key}.path is not listed in artifacts: {artifact}"
            )
        if not artifact_path.is_file() or artifact_path.is_symlink():
            errors.append(f"Manifest frozen_inputs.{key} points to a missing artifact")
            continue
        if not isinstance(expected, str) or not re.fullmatch(r"[0-9a-f]{64}", expected):
            errors.append(f"Manifest frozen_inputs.{key}.sha256 must be 64 lowercase hex characters")
            continue
        actual = _sha256(artifact_path)
        if actual != expected:
            errors.append(
                f"Manifest frozen_inputs.{key} checksum mismatch for {artifact}"
            )


def _contained_artifact_path(run_path, artifact):
    """Return a safe artifact path contained by run_path, or an error string."""
    if not isinstance(artifact, str) or not artifact:
        return None, "Artifact must be a non-empty relative path inside the run directory"

    relative = Path(artifact)
    if relative.is_absolute() or artifact in (".", "..") or ".." in relative.parts:
        return None, "Artifact must be a safe relative path inside the run directory"

    artifact_path = run_path / relative
    try:
        artifact_path.resolve().relative_to(run_path.resolve())
    except (OSError, ValueError):
        return None, "Artifact must resolve inside the run directory"
    return artifact_path, None


def _validate_manifest(
    path,
    run_path,
    errors,
    required_files,
    selected_mode,
    require_docx,
    provisional_only=False,
):
    if not path.is_file():
        return None

    text = _read_text(path, errors)
    if text is None:
        return None

    try:
        manifest = json.loads(text)
    except json.JSONDecodeError as exc:
        errors.append(f"Invalid manifest.json: {exc}")
        return None

    if not isinstance(manifest, dict):
        errors.append("Invalid manifest.json: root must be an object")
        return None

    for key in REQUIRED_MANIFEST_KEYS:
        if key not in manifest:
            errors.append(f"Manifest missing required key: {key}")

    if "status" in manifest and manifest["status"] not in MANIFEST_STATUSES:
        errors.append(
            "Manifest status must be exactly provisional or publish-ready"
        )
    elif provisional_only and manifest.get("status") != "provisional":
        errors.append("Manifest status must be provisional before final delivery")

    if manifest.get("status") == "publish-ready":
        bible_version = manifest.get("bible_version")
        if not isinstance(bible_version, int) or isinstance(bible_version, bool) or bible_version < 1:
            errors.append("Publish-ready manifest requires positive integer bible_version")
        else:
            bible_text = _read_text(run_path / "03-argument-bible.md", errors)
            bible_match = BIBLE_VERSION_PATTERN.search(bible_text or "")
            if bible_match and int(bible_match.group(1)) != bible_version:
                errors.append("Manifest bible_version does not match Argument Bible version")

    if "mode" in manifest:
        manifest_mode = _normalize_mode(manifest["mode"])
        if manifest_mode is None:
            errors.append(
                "Manifest mode must be one of: " + ", ".join(CANONICAL_MODES)
            )
        elif manifest_mode != selected_mode:
            errors.append(
                f"Manifest mode {manifest_mode} does not match selected mode "
                f"{selected_mode}"
            )

    if "artifacts" not in manifest:
        return manifest

    artifacts = manifest["artifacts"]
    if not isinstance(artifacts, list) or not artifacts:
        errors.append("Manifest artifacts must be a non-empty list of strings")
        return manifest

    if not all(isinstance(artifact, str) for artifact in artifacts):
        errors.append("Manifest artifacts must be a non-empty list of strings")
        return manifest

    required_inventory = tuple(
        filename
        for filename in required_files
        if filename != "manifest.json"
    )
    docx_required = require_docx or manifest.get("status") == "publish-ready"
    if docx_required:
        required_inventory += ("07-final.docx",)

    for filename in required_inventory:
        if filename not in artifacts:
            errors.append(f"Manifest artifacts missing required entry: {filename}")

    for artifact in artifacts:
        artifact_path, containment_error = _contained_artifact_path(run_path, artifact)
        if containment_error:
            errors.append(f"Manifest artifact {artifact!r}: {containment_error}")
        elif not artifact_path.is_file():
            errors.append(f"Manifest lists nonexistent artifact: {artifact}")

    _validate_frozen_inputs(manifest, run_path, artifacts, errors)

    return manifest


def record_artifact(run_dir, artifact):
    """Atomically append an existing safe relative artifact to manifest.json."""
    errors = []
    warnings = []
    run_path = Path(run_dir)
    artifact_path, containment_error = _contained_artifact_path(run_path, artifact)
    if containment_error:
        errors.append(containment_error)
        return {"valid": False, "errors": errors, "warnings": warnings}
    if not artifact_path.is_file():
        errors.append(f"Artifact does not exist: {artifact}")
        return {"valid": False, "errors": errors, "warnings": warnings}

    manifest_path = run_path / "manifest.json"
    text = _read_text(manifest_path, errors)
    if text is None:
        return {"valid": False, "errors": errors, "warnings": warnings}

    try:
        manifest = json.loads(text)
    except json.JSONDecodeError as exc:
        errors.append(f"Invalid manifest.json: {exc}")
        return {"valid": False, "errors": errors, "warnings": warnings}

    if not isinstance(manifest, dict):
        errors.append("Invalid manifest.json: root must be an object")
    artifacts = manifest.get("artifacts") if isinstance(manifest, dict) else None
    if not isinstance(artifacts, list) or not all(
        isinstance(item, str) for item in artifacts
    ):
        errors.append("Manifest artifacts must be a list of strings")
    if errors:
        return {"valid": False, "errors": errors, "warnings": warnings}

    changed = False
    if artifact not in artifacts:
        manifest["artifacts"] = [*artifacts, artifact]
        changed = True

    if artifact == "07-final.docx":
        frozen_inputs = manifest.get("frozen_inputs")
        if frozen_inputs is None:
            frozen_inputs = {}
            manifest["frozen_inputs"] = frozen_inputs
        elif not isinstance(frozen_inputs, dict):
            errors.append("Manifest frozen_inputs must be an object")
            return {"valid": False, "errors": errors, "warnings": warnings}
        final_docx = {
            "path": artifact,
            "sha256": _sha256(artifact_path),
        }
        if frozen_inputs.get("final_docx") != final_docx:
            frozen_inputs["final_docx"] = final_docx
            changed = True

    if not changed:
        return {"valid": True, "errors": [], "warnings": []}

    temporary_path = None
    try:
        with tempfile.NamedTemporaryFile(
            mode="w",
            encoding="utf-8",
            dir=run_path,
            prefix=".manifest.json.",
            suffix=".tmp",
            delete=False,
        ) as temporary:
            temporary_path = Path(temporary.name)
            json.dump(manifest, temporary, ensure_ascii=False, indent=2)
            temporary.write("\n")
            temporary.flush()
            os.fsync(temporary.fileno())
        os.replace(temporary_path, manifest_path)
    except OSError as exc:
        errors.append(f"Unable to update manifest.json atomically: {exc}")
    finally:
        if temporary_path is not None and temporary_path.exists():
            try:
                temporary_path.unlink()
            except OSError:
                pass

    return {"valid": not errors, "errors": errors, "warnings": warnings}


def _validate_placeholders(run_path, filenames, destination, errors):
    for filename in filenames:
        path = run_path / filename
        if path.suffix != ".md" or not path.is_file():
            continue

        text = _read_text(path, errors)
        if text is None:
            continue

        for match in PLACEHOLDER_PATTERN.finditer(text):
            destination.append(
                f"Unresolved placeholder in {filename}: {match.group(0)}"
            )


def validate_mode(
    run_dir,
    mode,
    stage="final",
    allow_placeholders=False,
    require_docx=False,
):
    """Return {'valid': bool, 'errors': list[str], 'warnings': list[str]}."""
    errors = []
    warnings = []
    run_path = Path(run_dir)

    selected_mode = _normalize_mode(mode)
    if selected_mode is None:
        errors.append("Unknown mode; expected one of: " + ", ".join(CANONICAL_MODES))
        return {"valid": False, "errors": errors, "warnings": warnings}

    if stage not in STAGE_FILES:
        errors.append(f"Unknown stage: {stage}")
        return {"valid": False, "errors": errors, "warnings": warnings}

    mode_stages = MODE_STAGE_FILES[selected_mode]
    if stage not in mode_stages:
        errors.append(f"Stage {stage} is not supported for mode {selected_mode}")
        return {"valid": False, "errors": errors, "warnings": warnings}

    required_files = mode_stages[stage]
    for filename in required_files:
        if not (run_path / filename).is_file():
            errors.append(f"Missing required artifact: {filename}")

    _validate_bible(run_path / "03-argument-bible.md", errors)

    manifest = None
    manifest_required = stage == "final" or (
        (selected_mode == "ROUTES" and stage == "routes")
        or (selected_mode == "KILL ROOM" and stage == "review")
    )
    if manifest_required:
        manifest = _validate_manifest(
            run_path / "manifest.json",
            run_path,
            errors,
            required_files,
            selected_mode,
            require_docx,
            provisional_only=stage != "final",
        )

    placeholders_are_warnings = (
        allow_placeholders
        and (
            stage != "final"
            or (
                manifest is not None
                and manifest.get("status") == "provisional"
            )
        )
    )
    placeholder_messages = warnings if placeholders_are_warnings else errors
    _validate_placeholders(
        run_path,
        ACTIVE_STAGE_FILES[stage],
        placeholder_messages,
        errors,
    )

    docx_required = require_docx or (
        manifest is not None and manifest.get("status") == "publish-ready"
    )
    if docx_required:
        _validate_docx(run_path / "07-final.docx", errors)

    return {"valid": not errors, "errors": errors, "warnings": warnings}


def validate(run_dir, stage="final", allow_placeholders=False, require_docx=False):
    """Validate a default CREATE run with the full pipeline contract."""
    return validate_mode(
        run_dir,
        "CREATE",
        stage=stage,
        allow_placeholders=allow_placeholders,
        require_docx=require_docx,
    )


def _infer_manifest_mode(run_path):
    path = run_path / "manifest.json"
    if not path.is_file():
        return None

    try:
        manifest = json.loads(path.read_text(encoding="utf-8"))
    except (OSError, UnicodeError, json.JSONDecodeError):
        return None

    if not isinstance(manifest, dict):
        return None
    return _normalize_mode(manifest.get("mode"))


def main():
    parser = argparse.ArgumentParser(
        description="Validate artifacts produced by a Black Copy Chief run."
    )
    parser.add_argument("run_dir")
    parser.add_argument("--stage", choices=tuple(STAGE_FILES), default="final")
    parser.add_argument("--mode")
    parser.add_argument("--allow-placeholders", action="store_true")
    parser.add_argument("--require-docx", action="store_true")
    parser.add_argument("--record-artifact")
    args = parser.parse_args()

    if args.record_artifact:
        result = record_artifact(args.run_dir, args.record_artifact)
        output = json.dumps(result, ensure_ascii=False, indent=2) + "\n"
        sys.stdout.buffer.write(output.encode("utf-8"))
        return 0 if result["valid"] else 1

    mode = args.mode
    if mode is None and args.stage == "final":
        mode = _infer_manifest_mode(Path(args.run_dir))
    if mode is None:
        mode = "CREATE"

    result = validate_mode(
        args.run_dir,
        mode,
        stage=args.stage,
        allow_placeholders=args.allow_placeholders,
        require_docx=args.require_docx,
    )
    output = json.dumps(result, ensure_ascii=False, indent=2) + "\n"
    sys.stdout.buffer.write(output.encode("utf-8"))
    return 0 if result["valid"] else 1


if __name__ == "__main__":
    raise SystemExit(main())
