# Tipografia — legenda, título e tarja

O modelo **re-sintetiza, nunca preserva**: texto pedido no prompt sai borrado, com letra
trocada ou em inglês macarrônico. Tipografia é **camada por cima, feita por código**.

---

## ⚠️ O ffmpeg desta máquina NÃO renderiza texto

Verificado em 30/08/2026, ffmpeg 8.1.1 (Homebrew):

```
$ ffmpeg -h filter=drawtext   → Unknown filter 'drawtext'
$ ffmpeg -h filter=subtitles  → Unknown filter 'subtitles'
$ ffmpeg -buildconf | grep -E "freetype|libass|fontconfig"   → (nada)
```

O build veio **sem freetype, sem libass, sem fontconfig**. Todo tutorial de
`drawtext=...` e de `.srt` queimado **falha aqui**. Não é erro de sintaxe — o filtro
não existe.

**O caminho que funciona:** renderizar o texto em **PNG com alfa (PIL)** e compor com
`overlay`, que existe. É melhor mesmo assim — dá controle sobre o **arquivo** de fonte,
que é o único jeito de garantir peso real.

🔑 **Peso pedido ≠ peso carregado.** Pedir "bold" a uma fonte que só tem Regular devolve
**falso-negrito sintético** — engorda o traço por algoritmo e fica sujo em movimento.
Carregar o arquivo do peso: `Arial Bold.ttf`, não `Arial.ttf` com flag.

Fontes com peso real confirmadas nesta máquina:

| Uso | Arquivo | getname() |
|---|---|---|
| Legenda / título padrão | `/System/Library/Fonts/Supplemental/Arial Bold.ttf` | ('Arial', 'Bold') |
| Corpo / secundário | `/System/Library/Fonts/Supplemental/Arial.ttf` | ('Arial', 'Regular') |
| Impacto / manchete | `/System/Library/Fonts/Supplemental/Impact.ttf` | ('Impact', 'Regular') |
| Alternativa neutra | `/System/Library/Fonts/HelveticaNeue.ttc` **índice 1** | ('Helvetica Neue', 'Bold') |

`.ttc` é coleção — precisa do `index=` para pegar o peso certo.

---

## A ferramenta

`scripts/legenda.py` (nesta skill) gera a faixa em PNG com quebra de linha automática,
contorno e alinhamento.

```bash
python3 ~/.claude/skills/cinema/scripts/legenda.py \
  --text "ELE NUNCA CONTOU ISSO PRA NINGUÉM" \
  --out leg.png --width 1080 --size 72 --weight bold --stroke 6
# → fonte: Arial Bold (Arial Bold.ttf)
# → leg.png  1080x212  2 linha(s)
```

Ele **imprime a fonte que realmente carregou** — se sair "Regular" onde se pediu bold,
o falso-negrito foi pego antes de ir para o vídeo.

Compor com janela de tempo:

```bash
ffmpeg -i plano.mp4 -i leg.png \
  -filter_complex "overlay=0:H-h-420:enable='between(t,0.5,4.5)'" \
  -c:a copy saida.mp4
```

`enable='between(t,início,fim)'` é o que faz a legenda entrar e sair na hora certa.
Sem isso ela fica o clipe inteiro.

---

## Zonas seguras do 9:16 (1080×1920)

A UI do app cobre as bordas. Texto fora da zona segura **fica escondido atrás do
botão de curtir, do @ do perfil ou da legenda do post**.

| Região | Pixels (de 1920) | O que ocupa |
|---|---|---|
| Topo perigoso | 0–220 | relógio, barra de status, botão de fechar |
| **Zona segura** | **220–1500** | aqui vai o texto |
| Base perigosa | 1500–1920 | @perfil, legenda, som, botões laterais |

Lateral: manter **8% de margem** de cada lado (86px em 1080) — a coluna de botões do
Reels/TikTok come a direita.

**Posição padrão de legenda queimada:** centralizada horizontalmente, base do bloco em
~`H-420` (dentro da zona segura, acima da UI). É o `overlay=0:H-h-420` do exemplo.

**Título de abertura (hook):** terço superior, dentro de 220–700.

---

## Tamanhos que leem no celular

Base 1080 de largura, texto lido em tela de ~6":

| Papel | Tamanho | Linhas máx. |
|---|---|---|
| Hook / manchete de abertura | 84–96px | 2 |
| Legenda queimada (fala) | 64–72px | 2 |
| Crédito / rodapé / disclaimer | 36–42px | 1 |

**Contorno preto de 5–8px é obrigatório** em legenda sobre vídeo. Sem ele o texto
some quando o fundo clareia — e o fundo sempre clareia em algum frame.

Duas linhas é o teto de legenda queimada. Três linhas viram parágrafo e o espectador
para de ver o vídeo para ler.

---

## Ordem das camadas

```
1. clipes gerados          (Higgsfield)
2. corte e ordem           (ffmpeg concat)
3. correção de cor         (ffmpeg, se necessário)
4. legenda / título        (PIL → overlay)
5. logo / marca d'água     (PIL ou PNG pronto → overlay)
6. trilha e mixagem        (ffmpeg)
7. proporção final / crop  (ffmpeg)
```

Texto **depois** do corte. Legenda queimada antes de cortar vira legenda cortada no meio.

---

## Montagem da sequência

```bash
# emendar planos na ordem
printf "file '%s'\n" plano01.mp4 plano02.mp4 plano03.mp4 > lista.txt
ffmpeg -f concat -safe 0 -i lista.txt -c copy sequencia.mp4

# aparar um plano de 5s para 3s (aparar é grátis; gerar curto não é mais barato)
ffmpeg -i plano.mp4 -ss 0.8 -t 3.0 -c:v libx264 -pix_fmt yuv420p plano_aparado.mp4

# 1:1 ou 9:16 → 4:5 (feed do Instagram, que não existe como parâmetro em modelo nenhum)
ffmpeg -i in.mp4 -vf "crop=ih*4/5:ih" -c:a copy out45.mp4
```

⚠️ `-c copy` no concat exige que todos os clipes tenham **mesmo codec, resolução e fps**.
Gerou tudo no mesmo modelo e proporção? Funciona. Misturou Kling com Seedance, ou 720p
com 1080p? Re-encodar antes, ou o concat sai com áudio dessincronizado e frames pulados.

---

## Se quiser o `drawtext` de verdade

O build do Homebrew pode ser trocado por um com as libs de texto:

```bash
brew tap homebrew-ffmpeg/ffmpeg
brew install homebrew-ffmpeg/ffmpeg/ffmpeg --with-libass --with-freetype --with-fontconfig
```

Não é necessário — o caminho PIL→overlay cobre tudo que legenda de rede social precisa,
com mais controle de fonte. Só vale se aparecer necessidade de `.srt`/`.ass` com
karaokê ou centenas de falas cronometradas.
