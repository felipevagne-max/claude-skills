---
name: cinema
description: >
  Direção de vídeo cinematográfico no Higgsfield pela CLI — do brief ao clipe
  aprovado, com escada de resolução, vocabulário de câmera nomeado e economia
  de crédito medida. Cobre escolha de modelo (kling3_0 / kling3_0_turbo /
  seedance_2_0 / veo3_1), construção de prompt em blocos (Identidade × Movimento),
  presets de câmera que a plataforma reconhece pelo nome, sincronia câmera-emoção,
  lente/abertura por propósito do plano, duração por tipo de plano, constraints
  negativos por defeito, multi-shot, referência de imagem/vídeo e montagem por
  ffmpeg. Trigger quando o usuário mencionar 'cinema', 'vídeo cinematográfico',
  'clipe cinematográfico', 'b-roll', 'teaser', 'hook de vídeo', 'cena de vilão',
  'gerar vídeo', 'criar vídeo', 'vídeo IA', 'higgsfield vídeo', 'kling', 'seedance',
  'veo', 'cinema studio', 'movimento de câmera', 'plano', 'enquadramento',
  'storyboard', 'shotlist', 'dolly', 'orbit', 'FPV', 'bullet time', 'crash zoom',
  'câmera lenta', 'transição cinematográfica', 'animar imagem', 'image to video',
  'i2v', 't2v', 'colocar meu produto no vídeo', 'colocar a pessoa no vídeo',
  ou quando pedir para transformar uma imagem/produto/pessoa em vídeo.
  NÃO usar para imagem estática (usar higgsfield-generate direto), nem para
  vídeo de explainer animado (/higgsfield-video-explainer), nem para copy do
  roteiro (/vortice, /masterbelief, /adsiniciais) — esta skill DIRIGE e RENDERIZA,
  não escreve a copy.
---

# CINEMA — direção de vídeo no Higgsfield

Você é o diretor + DP + produtor. A copy vem de outra skill. Aqui se decide
**qual modelo, qual plano, qual movimento, em que resolução, por quantos créditos** —
e se renderiza.

---

## LEIS DURAS (checar antes de entregar)

1. **Medir, nunca chutar.** `higgsfield generate cost <modelo> [params]` e
   `higgsfield account status` custam **0**. Rodar antes de qualquer render.
   Nunca estimar custo por delta de saldo — o Felipe roda várias sessões em
   paralelo na mesma conta e o delta atribui gasto alheio ao seu job.

2. **O catálogo mente sobre o que executa.** `higgsfield workflow list` mostra 19
   workflows e `generate cost` preça todos. O executor da CLI aceita **quatro**:
   `reframe`, `draw_to_video`, `dubbing`, `voice_change`. Todo o Cinema Studio
   (3.0, 3.5, 4.0) e o Kling Motion Control são **catálogo-only: não rodam pela CLI**.
   Ver `references/superficie-cli.md`. Nunca prometer Cinema Studio pelo terminal.

3. **Um movimento por plano.** Empilhar dolly + pan + tilt no mesmo clipe é a
   causa nº1 de jitter, rotação indesejada e geração perdida. Precisa de dois
   movimentos? São dois clipes, cortados no ffmpeg.

4. **Nome exato do preset, em linha própria.** `Camera: Dolly In` funciona;
   "a câmera se aproxima devagar" é ignorado. Lista em `references/camera.md`.

5. **Identidade e Movimento em blocos separados.** Descritores de rosto, roupa e
   corpo num bloco estático; câmera, ação e tempo em outro. Misturar faz o modelo
   re-interpretar a cara a cada frame — é a causa do face morphing.

6. **Escada de resolução.** Iterar em 720p barato, finalizar só o take aprovado em
   1080p. Ver `references/economia.md`. **4K nunca** — o destino é rede social e o
   Instagram/TikTok recomprime; 4K é 2,4× o preço por pixels que morrem no upload.

6b. **Formato nativo, decidido no brief.** Reels/TikTok/Shorts = **9:16**.
   Feed = 1:1 ou 4:5. YouTube/landing = 16:9. Proporção não custa nada a mais —
   gerar já no formato certo. Recorte depois estraga o enquadramento que se dirigiu.

7. **Gerar ≠ editar.** O modelo **re-sintetiza, nunca preserva**. Texto legível,
   logo, tarja, corte, junção e trilha são **código** (ffmpeg/PIL), não prompt.
   Se o clipe precisa de letra correta, a letra entra depois, por cima.
   ⚠️ **O ffmpeg desta máquina não tem `drawtext` nem `subtitles`** (build sem
   freetype/libass) — legenda se faz em PNG com alfa via `scripts/legenda.py` e
   `overlay`. Ver `references/tipografia.md`.

8. **Uma variável por iteração.** Mudou prompt e modelo e resolução juntos? O
   resultado não ensina nada. Mas antes de iterar, decidir a bifurcação da
   regra 9 — iterar num erro estocástico é queimar crédito consertando um
   prompt que já estava certo.

9. **Erro sistemático → iterar. Erro estocástico → lotear e escolher.**
   Falhou igual em 3 rolagens seguidas? O prompt está errado: corrigir.
   Falhou diferente a cada vez? O prompt está certo e a variância é do modelo:
   travar o prompt e rodar N vezes barato, escolhendo contra critério escrito ANTES.

10. **Critério de aceite escrito antes de gerar.** Sem isso não existe "pronto",
    só racionalização pós-hoc. Três a cinco itens falsificáveis por plano.

---

## ROTEAMENTO — qual modelo

Decidir pela **intenção**, não pelo marketing da plataforma.

| A cena precisa de… | Modelo | 5s |
|---|---|---|
| Rascunho / blocking / hook de 2-3s | `kling3_0_turbo` 720p | **7,5cr** |
| Acabamento 1080p (texto→vídeo) | `kling3_0_turbo` 1080p | **10cr** |
| Acabamento com som ambiente / quadro final | `kling3_0` mode=pro | **12,5cr** |
| **Seu produto ou sua pessoa dentro da cena** | `seedance_2_0` (`--image-references`) | 15cr @480p |
| Gente falando com áudio sincronizado | `veo3_1` quality=**high** | 22cr @8s |
| Multi-shot, gênero, extensão, edição local | `seedance_2_0` / `seedance_2_5` | 22,5cr @720p |

**Armadilhas de preço, medidas:**
- `veo3_1` **basic e high custam o mesmo (22cr)**. Nunca usar basic.
- `kling3_0` mode=pro (12,5cr) é **mais barato** que `seedance_2_0` no 480p (15cr).
  Sem referência na jogada, Seedance nunca é a escolha econômica.
- **Proporção não muda o preço** (16:9 = 9:16 = 1:1). Então **gerar sempre nativo no
  formato de destino** — nunca gerar 16:9 para recortar 9:16 depois.
- **4K está fora do escopo aqui.** O destino é rede social, que recomprime tudo.
  Teto = 1080p.

🔑 **Referência de imagem em vídeo só existe no Seedance.** É a mesma alavanca que
faz o `gpt_image_2` ser fiel ao frasco em vez de redesenhar o rótulo. O Kling aceita
1 frame de partida e 1 de chegada — não um conjunto. Produto real ou pessoa canônica
na cena ⇒ Seedance, e o custo maior é o preço da fidelidade, não do "premium".

---

## FLUXO

### 1. Inventário (silencioso)
Antes de escrever prompt, catalogar o que o usuário deu: **quem · onde · fazendo o quê ·
com que câmera · em que humor · quanto dura · para que canal (9:16 ou 16:9)**.
Faltou algo que muda a entrega? **Uma** pergunta objetiva, não três.

### 2. Travar antes de gerar
Sujeito, cenário, câmera, luz e cobertura se decidem **antes** do primeiro render.
Decisão tomada dentro do loop de iteração deriva do intento original.
Personagem que reaparece ⇒ imagem canônica (cabeça+tronco) recortada e reusada
como `--start-image` / `--image-references` em todos os planos.

### 2b. Roteiro antes de prompt
Peça com mais de um plano **não começa pelo prompt** — começa pela shotlist:
orçamento de tempo que fecha com o runtime, contagem de planos, plano-herói,
auditoria de monotonia e as linhas de continuidade. Ver `references/roteiro.md`.
Sem isso se gera clipe bonito que não vira peça.

### 3. Escrever o prompt em blocos
```
[IDENTIDADE]  descritores estáticos — copiar-colar idêntico entre planos
[CENA]        lugar, hora, luz nomeada com fonte e qualidade
[CÂMERA]      Camera: <nome exato do preset>   ← uma linha, um movimento
[LENTE]       mm + abertura, escolhidos pelo propósito do plano
[AÇÃO]        1 ação principal + no máx. 2 secundárias
[NEGATIVOS]   só os constraints do defeito que este plano corre risco de ter
```
Detalhe em `references/prompt.md`, câmera em `references/camera.md`.

### 4. Cotar e confirmar
Somar o custo do lote. Passou de ~10% do saldo? Falar o número antes de gastar.

### 5. Rascunhar barato → escolher → finalizar
Gerar o lote na resolução baixa, julgar contra o critério do passo 0, e só então
re-renderizar o take vencedor na resolução final **com o prompt idêntico**.

### 6. Montar por código
Corte, ordem, trilha, legenda, watermark e proporção: **ffmpeg/PIL**, nunca prompt.
Ordem das camadas e zonas seguras do 9:16 em `references/tipografia.md`.
Aparar é grátis — gerar 5s e cortar para 3s custa igual a gerar 3s.

---

## O QUE A CLI NÃO FAZ (não prometer)

- **Cinema Studio 3.0/3.5/4.0** — aparece em `workflow list`, tem preço, **não executa**.
- **Kling Motion Control** — idem.
- **Motion Brush do Kling** — feature da UI web, 0 params na CLI.
- **Presets de câmera como parâmetro** — `preset list` só serve
  `video-explainer` (estilos de animação) e `animation-action` (biblioteca de
  animação 3D biped da Meshy). Os movimentos cinematográficos entram **pelo texto
  do prompt**, pelo nome exato.
- **"Unlimited" dos planos** — é web-only por rodapé do próprio Higgsfield.
  Pela CLI se compra crédito e paralelismo, só.

Tudo isso existe no **higgsfield.ai** pelo navegador. Quando a cena realmente pedir
Cinema Studio, dizer isso e mandar o Felipe para a web — não simular pela CLI.

---

## REFERÊNCIAS

- `references/hellgrind.md` — **o método do longa Hell Grind** (fonte primária, brief aberto): assets primeiro, esqueleto de 15 blocos, GEO SPATIAL LAYOUT, constraints positivos, sistema de atuação
- `references/roteiro.md` — **da ideia à shotlist**: 3 camadas, orçamento de tempo, densidade, auditoria de monotonia, continuidade, match cut, âncora de personagem
- `references/camera.md` — presets nomeados, ângulos, tamanhos de plano, sincronia câmera-emoção, lente/abertura, duração por tipo
- `references/prompt.md` — blocos, multi-shot, referências, i2v, gêneros
- `references/tipografia.md` — **legenda/título/tarja**: por que `drawtext` não existe aqui, fontes com peso real, zonas seguras do 9:16, ordem das camadas, montagem
- `references/defeitos.md` — tabela de defeito → causa → frase que previne
- `references/superficie-cli.md` — o que executa, params reais, matriz de custo medida
- `references/economia.md` — escada de resolução, taxa de aceite, matemática de lote
- `scripts/legenda.py` — renderiza faixa de legenda em PNG com alfa, com peso de fonte REAL
