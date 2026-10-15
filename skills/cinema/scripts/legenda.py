#!/usr/bin/env python3
"""
Gera uma faixa de legenda/título em PNG com alfa, para sobrepor no vídeo via ffmpeg overlay.

Existe porque o ffmpeg desta máquina NÃO tem drawtext/subtitles (build sem freetype/libass).
E porque renderizar por arquivo de fonte é o único jeito de garantir peso REAL —
pedir "bold" a uma fonte que só tem Regular devolve falso-negrito sintético.

Uso:
  python3 legenda.py --text "SUA LINHA AQUI" --out legenda.png \
      --width 1080 --size 72 --weight bold --align center --stroke 6
"""
import argparse, os, sys
from PIL import Image, ImageDraw, ImageFont

FONTES = {
    "bold":    ["/System/Library/Fonts/Supplemental/Arial Bold.ttf"],
    "regular": ["/System/Library/Fonts/Supplemental/Arial.ttf"],
    "impact":  ["/System/Library/Fonts/Supplemental/Impact.ttf"],
}

def carregar(weight, size, font_path=None):
    caminhos = [font_path] if font_path else FONTES.get(weight, FONTES["bold"])
    for p in caminhos:
        if p and os.path.exists(p):
            f = ImageFont.truetype(p, size)
            nome, estilo = f.getname()
            print(f"fonte: {nome} {estilo}  ({os.path.basename(p)})", file=sys.stderr)
            return f
    sys.exit(f"ERRO: nenhuma fonte encontrada em {caminhos}")

def quebrar(texto, fonte, largura_max, draw):
    linhas, atual = [], ""
    for palavra in texto.split():
        teste = (atual + " " + palavra).strip()
        if draw.textlength(teste, font=fonte) <= largura_max:
            atual = teste
        else:
            if atual: linhas.append(atual)
            atual = palavra
    if atual: linhas.append(atual)
    return linhas

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--text", required=True)
    ap.add_argument("--out", required=True)
    ap.add_argument("--width", type=int, default=1080, help="largura do vídeo de destino")
    ap.add_argument("--size", type=int, default=72)
    ap.add_argument("--weight", default="bold", choices=list(FONTES))
    ap.add_argument("--font", default=None, help="caminho explícito de .ttf")
    ap.add_argument("--color", default="#FFFFFF")
    ap.add_argument("--stroke", type=int, default=6, help="contorno preto; 0 desliga")
    ap.add_argument("--stroke-color", default="#000000")
    ap.add_argument("--align", default="center", choices=["left", "center", "right"])
    ap.add_argument("--margin", type=int, default=None, help="margem lateral; default 8%% da largura")
    ap.add_argument("--line-spacing", type=float, default=1.18)
    a = ap.parse_args()

    margem = a.margin if a.margin is not None else int(a.width * 0.08)
    largura_texto = a.width - 2 * margem

    fonte = carregar(a.weight, a.size, a.font)
    tmp = Image.new("RGBA", (10, 10)); d = ImageDraw.Draw(tmp)
    linhas = quebrar(a.text, fonte, largura_texto, d)

    asc, desc = fonte.getmetrics()
    alt_linha = int((asc + desc) * a.line_spacing)
    altura = alt_linha * len(linhas) + 2 * a.stroke + 8

    img = Image.new("RGBA", (a.width, altura), (0, 0, 0, 0))
    d = ImageDraw.Draw(img)
    for i, linha in enumerate(linhas):
        w = d.textlength(linha, font=fonte)
        x = margem if a.align == "left" else (a.width - w - margem if a.align == "right" else (a.width - w) / 2)
        y = i * alt_linha + a.stroke
        d.text((x, y), linha, font=fonte, fill=a.color,
               stroke_width=a.stroke, stroke_fill=a.stroke_color)

    img.save(a.out)
    print(f"{a.out}  {a.width}x{altura}  {len(linhas)} linha(s)")

if __name__ == "__main__":
    main()
