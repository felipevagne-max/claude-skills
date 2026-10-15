#!/bin/sh
set -eu

replace_failed=0
if [ "${1-}" = "--replace-failed" ]; then
  replace_failed=1
  shift
fi

if [ "$#" -lt 1 ] || [ "$#" -gt 2 ]; then
  echo "Usage: render_docx.sh [--replace-failed] INPUT.md [OUTPUT.docx]" >&2
  exit 64
fi

input=$1
if [ "$#" -eq 2 ]; then
  output=$2
else
  output=${input%.md}.docx
fi

if [ ! -f "$input" ]; then
  echo "Input file not found: $input" >&2
  exit 66
fi

output_dir=$(dirname "$output")
output_name=$(basename "$output")
if [ ! -d "$output_dir" ]; then
  echo "Output directory not found: $output_dir" >&2
  exit 73
fi

if [ "$replace_failed" -eq 0 ]; then
  if [ -e "$output" ] || [ -L "$output" ]; then
    echo "Refusing to overwrite existing output: $output" >&2
    exit 73
  fi
elif [ ! -f "$output" ] || [ -L "$output" ]; then
  echo "--replace-failed requires an existing regular, non-symlink output: $output" >&2
  exit 73
fi

if ! command -v pandoc >/dev/null 2>&1; then
  echo "pandoc is required" >&2
  exit 69
fi

if ! command -v python3 >/dev/null 2>&1; then
  echo "python3 is required to validate and promote DOCX output" >&2
  exit 69
fi

attempt=$(mktemp "$output_dir/.${output_name}.attempt.XXXXXX")
cleanup() {
  if [ -n "${attempt-}" ] && [ -e "$attempt" ]; then
    rm -f "$attempt"
  fi
}
trap cleanup EXIT HUP INT TERM

pandoc "$input" --from=gfm --to=docx --standalone --output="$attempt"

python3 - "$attempt" "$output" "$replace_failed" <<'PY'
import os
from pathlib import Path
import sys
import zipfile


attempt = Path(sys.argv[1])
output = Path(sys.argv[2])
replace_failed = sys.argv[3] == "1"

if not attempt.is_file() or attempt.stat().st_size == 0:
    raise SystemExit("Rendered DOCX is empty")

try:
    with zipfile.ZipFile(attempt) as archive:
        names = set(archive.namelist())
        required = {"[Content_Types].xml", "word/document.xml"}
        missing = sorted(required - names)
        if missing:
            raise SystemExit(
                "Rendered DOCX is missing required entries: " + ", ".join(missing)
            )
        damaged = archive.testzip()
        if damaged is not None:
            raise SystemExit(f"Rendered DOCX contains a damaged member: {damaged}")
except zipfile.BadZipFile as exc:
    raise SystemExit(f"Rendered output is not a valid DOCX archive: {exc}")

if not replace_failed:
    try:
        os.link(attempt, output)
    except FileExistsError:
        raise SystemExit(f"Refusing to overwrite existing output: {output}")
    os.unlink(attempt)
else:
    if output.is_symlink() or not output.is_file():
        raise SystemExit(
            f"--replace-failed requires an existing regular, non-symlink output: {output}"
        )
    suffix = 1
    while True:
        backup = output.with_name(f"{output.name}.failed.{os.getpid()}.{suffix}")
        try:
            os.link(output, backup)
            break
        except FileExistsError:
            suffix += 1
    try:
        os.replace(attempt, output)
    except OSError:
        backup.unlink(missing_ok=True)
        raise
    print(f"Preserved failed output: {backup}", file=sys.stderr)
PY

echo "$output"
