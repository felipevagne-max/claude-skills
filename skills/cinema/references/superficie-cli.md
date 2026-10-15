# Superfície real da CLI — medido em 30/08/2026

Conta `seu-email@exemplo.com`, plano **plus**. Tudo aqui foi verificado no terminal,
não lido em documentação.

---

## A armadilha central: catálogo ≠ executor

Três superfícies diferentes, com listas diferentes:

| comando | o que responde | inclui Cinema Studio? |
|---|---|---|
| `higgsfield workflow list` | catálogo (19 workflows) | ✅ sim |
| `higgsfield generate cost <x>` | preço | ✅ sim, preça tudo |
| `higgsfield generate workflow <x>` | **execução** | ❌ **não** |
| `higgsfield model list` | modelos executáveis | ❌ nem lista |

`generate workflow` aceita exatamente quatro nomes — `reframe`, `draw_to_video`,
`dubbing`, `voice_change`. Qualquer outro devolve `Unknown workflow`.

```
$ higgsfield generate workflow cinematic_studio_video_4_0 --prompt "..." --wait
Error: Unknown workflow "cinematic_studio_video_4_0".
$ higgsfield generate cost cinematic_studio_video_4_0 --duration 5 --resolution 480p
12.5 credits          ← preça alegremente um workflow que não roda
```

🔑 **A cotação não prova execução.** É o mesmo formato do gate de plano que já
mordeu antes: `generate cost` responde sobre o `job_type`, não sobre o seu direito
nem sobre o runner. Prova de execução é o job voltando `completed`.

**Catálogo-only (não rodam pela CLI):** `cinematic_studio_video_4_0`,
`cinematic_studio_3_0`, `cinematic_studio_video_3_5`, `cinematic_studio_video`,
`cinematic_studio_video_v2`, `kling3_0_motion_control`, `marketing_studio_video`.

---

## O que Cinema Studio 4.0 exporia, se rodasse

Vale conhecer porque é o que existe **na web** — e explica por que a web dá um
resultado que o terminal não dá. A cinematografia lá é **campo estruturado**, não prosa:

`camera_model_id` (corpo) · `camera_lens_id` (lente) · `camera_aperture_id` (abertura) ·
`era_id` (época) · `genre_id` · `pacing_id` (ritmo) · `light` + `light_id` + `light_custom` ·
`color_palette` · `bitrate_mode` · modos `t2v / omni_reference / video_edit / video_extension`.

⚠️ Os `*_id` são strings opacas **sem enum na CLI** e sem endpoint de descoberta —
o próprio binário nunca os consulta. Não há como adivinhá-los pelo terminal.

`cinematic_studio_3_0` adiciona `multi_shots` + `multi_prompt` + `multi_shot_mode`,
`speedramp` (auto/linear/slowmo/speedup/fast_to_slowmo/slowmo_to_fast/super_slowmo/impact),
`genre`, `preset_id`, 4k — e tem `prompt_language` com default **`zh`**.

---

## Modelos que EXECUTAM — params exatos

### `kling3_0` — o padrão daqui
`aspect_ratio` 16:9/9:16/1:1 · `duration` int · `mode` **std/pro/4k** ·
`sound` on/off · `start_image` · `end_image` · `prompt` (obrigatório)
→ Sem `image_references`. Sem `resolution` (a qualidade vem pelo `mode`).

### `kling3_0_turbo` — rascunho
`aspect_ratio` · `duration` · `resolution` **720p/1080p** · `start_image` · `prompt`
→ Sem `end_image`, sem som.

### `seedance_2_0` — o único com referência
`aspect_ratio` (7 opções, inclui 21:9) · `mode` std/fast · `resolution` 480p/720p/1080p/4k ·
`genre` auto/action/horror/comedy/noir/drama/epic · `generate_audio` ·
`bitrate_mode` · `image_references[]` · `video_references[]` · `audio_references[]` ·
`start_image` · `end_image`

Limites: **9 imagens** (contando start/end), **3 vídeos**, **3 áudios**, **12 no total**.
`audio_references` exige pelo menos uma imagem ou vídeo junto.
`mode=fast` só vai até 720p — 1080p/4k exigem `mode=std`.

### `veo3_1` — quando tem gente falando
`aspect_ratio` 16:9/9:16 · `duration` **só 4, 6 ou 8** · `quality` basic/high/ultra ·
`variant` veo-3-1-preview / veo-3-1-fast · `start_image`
→ Sem referências, sem 9:16 fora do par.

---

## Matriz de custo — medida, 5s e 10s

| modelo | opção | 5s | 10s |
|---|---|---|---|
| `kling3_0_turbo` | 720p | **7,5** | 15 |
| `kling3_0_turbo` | 1080p | **10** | 20 |
| `kling3_0` | mode=std | 10 | 20 |
| `kling3_0` | mode=pro | **12,5** | 25 |
| `kling3_0` | mode=4k | **30** | 60 |
| `seedance_2_0` | 480p | 15 | 30 |
| `seedance_2_0` | 720p | 22,5 | 45 |
| `seedance_2_0` | 1080p | 45 | 90 |
| `seedance_2_0` | 4k | **110** | 220 |
| `veo3_1` | basic 8s | — | **22** |
| `veo3_1` | high 8s | — | **22** |
| `veo3_1` | ultra 8s | — | 48 |

O custo é **estritamente linear na duração** em todos eles — 10s custa exatamente 2× 5s.
Não existe desconto por clipe longo; um clipe de 10s e dois de 5s custam igual, e dois
de 5s dão duas chances de acerto.

**Três leituras que mudam decisão:**
1. `veo3_1` **basic = high = 22cr**. Pedir basic é jogar qualidade fora de graça.
2. `kling3_0` 4k a 30cr contra `seedance_2_0` 4k a 110cr — **3,7×**.
3. `kling3_0` pro (12,5cr) sai **mais barato** que Seedance no 480p (15cr).
   Seedance só se paga quando a referência é necessária.

---

## Comandos que custam ZERO

```bash
higgsfield account status                      # saldo e plano
higgsfield generate cost <modelo> [params]     # preço exato
higgsfield model get <modelo>                  # params e constraints
higgsfield workflow list / get <w>             # catálogo (cuidado: ≠ executor)
higgsfield generate list --size 50 --json      # auditoria do que foi gasto
higgsfield preset list video-explainer|animation-action
higgsfield product-photoshoot create --enhance-only   # enriquece prompt de graça
```

## Auditar gasto (nunca por delta de saldo)

Várias sessões rodam na mesma conta em paralelo. Para saber o que **este** trabalho
custou, listar os jobs e somar os seus:

```bash
higgsfield generate list --size 50 --json | jq -r '.[] | "\(.created_at) \(.job_type) \(.status)"'
```

## Ler a superfície de verdade de um modelo

`model get` desatualiza. O `params` do JSON de um job **executado** mostra campos que o
schema não lista (foi assim que apareceram `multi_shots`, `speedramp`, `reference_elements`,
`prompt_language`). Depois de um render que interessa:

```bash
higgsfield generate get <job_id> --json | jq '.params'
```

---

## `reframe` — o único workflow útil que EXECUTA

Muda a proporção de um vídeo que já existe. Serve para reaproveitar material antigo
(um 16:9 virando 9:16 para Reels), **não** para economizar na geração — proporção não
muda o preço, então material novo se gera nativo.

```
PARAM              obrigatório?
aspect_ratio       ✅ sim — 21:9,16:9,4:3,1:1,3:4,9:16
video_references   ✅ exatamente UM
resolution         480p,720p,1080p (default 720p)
duration           opcional
start_image        opcional
image_references   opcional
```

```bash
higgsfield generate workflow reframe --video ./clipe16x9.mp4 \
  --aspect-ratio 9:16 --resolution 1080p --wait
```

⚠️ O `generate cost` do reframe **exige `aspect_ratio`** e o create exige
`exactly one video_references entry`. Cotar antes com os dois params preenchidos.

Os outros três executáveis: `draw_to_video` (rabisco sobre um frame vira movimento —
exige `--timestamp`), `dubbing`, `voice_change`.

---

## Redes sociais — o que a CLI serve nativo

**Proporção não altera o custo** (16:9 = 9:16 = 1:1, medido). Gerar sempre no formato
de destino.

| modelo | proporções nativas | 1080p? |
|---|---|---|
| `kling3_0_turbo` | 16:9 · 9:16 · 1:1 | ✅ `--resolution 1080p` |
| `kling3_0` | 16:9 · 9:16 · 1:1 | via `--mode` (ver nota abaixo) |
| `seedance_2_0` | auto · 16:9 · 9:16 · 4:3 · 3:4 · 1:1 · 21:9 | ✅ `--resolution 1080p` |
| `veo3_1` | 16:9 · 9:16 apenas | sem controle de resolução |

**4:5 (feed do Instagram) não existe como parâmetro** em nenhum deles — gerar 1:1 ou
9:16 e cortar no ffmpeg:

```bash
ffmpeg -i in.mp4 -vf "crop=ih*4/5:ih" -c:a copy out45.mp4
```
