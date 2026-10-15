#!/usr/bin/env python3
"""Mede um roteiro de /adstube em markdown: palavras e duração por bloco + limites da ficha Demand Gen.

Uso: python3 medir.py arquivo.md [--wpm 165]

Blocos reconhecidos: linhas de título que começam com GANCHO, CORPO, CTA (com ou sem #).
Fala = texto entre aspas "…" ou “…”. Marcações entre [colchetes] são ignoradas.
Ficha: linhas "Títulos (≤40):", "Título longo (≤90):", "Descrições (≤90):", "Nome da empresa (≤25):"
com itens numerados "1) … 2) …" ou separados por " | ".
Sai com código 1 se algum limite estourar ou peça ficar abaixo de 10s (não roda in-stream).
"""
import re
import sys

LIMITES = {
    "títulos": 40, "titulos": 40,
    "título longo": 90, "titulo longo": 90,
    "descrições": 90, "descricoes": 90,
    "nome da empresa": 25,
}


def fala(texto):
    texto = re.sub(r"\[[^\]]*\]", " ", texto)
    trechos = re.findall(r"[\"“]([^\"”]+)[\"”]", texto)
    return " ".join(trechos)


def itens(valor):
    partes = re.split(r"\s*\d\)\s*", valor)
    partes = [p.strip() for p in partes if p.strip()]
    if len(partes) <= 1 and " | " in valor:
        partes = [p.strip() for p in valor.split(" | ") if p.strip()]
    return partes


def main():
    if len(sys.argv) < 2:
        print(__doc__)
        sys.exit(2)
    wpm = 165
    if "--wpm" in sys.argv:
        wpm = int(sys.argv[sys.argv.index("--wpm") + 1])
    linhas = open(sys.argv[1], encoding="utf-8").read().splitlines()

    blocos, atual = [], None
    for ln in linhas:
        cab = re.match(r"^#*\s*(GANCHO[^\n]*|CORPO[^\n]*|CTA[^\n]*)$", ln.strip())
        if cab:
            atual = [cab.group(1).strip(), []]
            blocos.append(atual)
        elif re.match(r"^#*\s*FICHA", ln.strip()):
            atual = None
        elif atual:
            atual[1].append(ln)

    erro = False
    corpo_cta = 0
    ganchos = []
    print(f"{'BLOCO':45} {'PALAVRAS':>8} {'SEG':>6}")
    for nome, conteudo in blocos:
        n = len(fala("\n".join(conteudo)).split())
        seg = n / wpm * 60
        print(f"{nome[:45]:45} {n:8d} {seg:6.1f}")
        if nome.upper().startswith("GANCHO"):
            ganchos.append((nome, seg))
        else:
            corpo_cta += seg
    for nome, seg in ganchos:
        total = seg + corpo_cta
        aviso = "  ⛔ <10s não roda in-stream" if total < 10 else ""
        erro |= total < 10
        print(f"PEÇA com {nome[:30]:30} ≈ {total:5.1f}s{aviso}")
    if not ganchos and corpo_cta:
        print(f"PEÇA ≈ {corpo_cta:5.1f}s")

    for ln in linhas:
        m = re.match(r"^\s*[-*]?\s*([A-Za-zçãéíõ ]+?)\s*\(≤\d+\)\s*:\s*(.*)$", ln)
        if not m:
            continue
        chave = m.group(1).strip().lower()
        lim = LIMITES.get(chave)
        if not lim:
            continue
        for i, item in enumerate(itens(m.group(2)), 1):
            c = len(item)
            ok = "ok" if c <= lim else f"⛔ ESTOUROU {c - lim}"
            erro |= c > lim
            print(f"{chave[:16]:16} #{i} {c:3d}/{lim} {ok}  {item}")

    sys.exit(1 if erro else 0)


if __name__ == "__main__":
    main()
