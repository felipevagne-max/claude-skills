# Economia — o que dá para fazer com o saldo que existe

Plano **Plus**: 1.000 créditos/mês, **não acumulam** (na virada, zera).
6 vídeos / 8 imagens em paralelo. Crédito parado vale zero.

---

## A conta que muda a estratégia

A produção da Higgsfield que rodou o longa "Hell Grind" (90 min, 14 dias, 15 pessoas)
publicou os números: **108.859 gerações**, 9,54 milhões de créditos, ~US$400 mil.
Taxa de aceite confirmada em quatro fontes independentes: **~1,0% imagem, ~1,5% vídeo**.

1,5% significa **~67 tentativas por clipe aprovado**.

A 7,5cr o rascunho mais barato, um clipe naquele padrão custa **~500 créditos**.
Com 1.000/mês isso dá **dois clipes por mês**. Não é um regime operável aqui.

🔑 **A conclusão não é "gerar mais barato" — é que a disciplina de prompt tem que
fazer o trabalho que o orçamento de iteração não pode fazer.** Quem tem 10 milhões de
créditos compra o acerto na força bruta. Com 1.000, o acerto vem de travar sujeito,
luz, câmera e critério **antes** do primeiro render.

O regime realista aqui é **1 em 8**, não 1 em 67 — e o que compra essa diferença é
o bloco de identidade travado, um movimento por plano e o nome exato do preset.

---

## Escada de resolução — teto 1080p

O destino é **rede social**: Instagram, TikTok, YouTube Shorts. Todos recomprimem
pesado no upload. **4K está fora de escopo** — é 2,4× o preço por pixels que morrem
antes de chegar no espectador.

Nunca iterar em alta. Composição, enquadramento, movimento e atuação já se julgam em
720p; resolução só decide o acabamento.

| Etapa | Modelo | 5s |
|---|---|---|
| **Rascunho** — bloqueio, movimento, ritmo | `kling3_0_turbo` 720p | **7,5cr** |
| **Acabamento 1080p** | `kling3_0_turbo` 1080p | **10cr** |
| Acabamento com som ambiente ou quadro final travado | `kling3_0` mode=pro | 12,5cr |
| Rascunho **com referência** | `seedance_2_0` 480p | 15cr |
| Acabamento com referência | `seedance_2_0` 1080p | 45cr |

Re-renderizar o vencedor com o **prompt idêntico** — mudar resolução e texto junto
joga fora a informação do rascunho.

**Só sair do turbo quando ele não dá o que a cena pede.** `kling3_0_turbo` não tem
`end_image` nem `sound` — precisa travar o quadro final, ou quer som ambiente do
modelo, aí sim `kling3_0 mode=pro` a 12,5cr.

## Proporção é de graça — gerar nativo

16:9, 9:16 e 1:1 custam **exatamente o mesmo**. Então nunca gerar largo para recortar
vertical depois: o recorte joga fora o enquadramento que se dirigiu e reenquadra o
sujeito por acidente.

| Destino | Proporção | Duração típica |
|---|---|---|
| Reels / TikTok / Shorts | **9:16** | 5–10s por plano |
| Feed Instagram | 1:1 (ou 4:5 pelo ffmpeg) | 5s |
| YouTube / página de vendas / VSL | 16:9 | 5–10s |

O `kling3_0` e o `kling3_0_turbo` servem 16:9, 9:16 e 1:1 nativos. **4:5 não existe
como parâmetro** — gerar 1:1 e cortar no ffmpeg, ou gerar 9:16 e cortar.

---

## Custo de um plano acabado

| Regime | Rascunhos 720p | Acabamento 1080p | Total por plano de 5s |
|---|---|---|---|
| Enxuto (prompt travado, 4 tentativas) | 4 × 7,5 = 30 | 10 | **~40cr** |
| Normal (8 tentativas) | 8 × 7,5 = 60 | 10 | **~70cr** |
| Difícil (16 tentativas) | 16 × 7,5 = 120 | 10 | **~130cr** |
| Padrão Hell Grind (67) | 500 | 10 | ~510cr |

**Com 1.000cr/mês, no regime normal: ~14 planos acabados, ou ~70 segundos de
material aprovado por mês.** Um Reels de 30s com 6 planos custa ~420cr — quase
metade do saldo mensal.

Falar esse número antes de começar um projeto de vídeo. É a diferença entre entregar
e descobrir no dia 20 que o saldo acabou.

---

## Iterar ou lotear — a bifurcação

Antes de mexer no prompt, classificar o erro:

- **Sistemático** — falhou **do mesmo jeito** em 3 rolagens: o prompt está errado.
  → Iterar, **uma variável por vez**.
- **Estocástico** — falhou **diferente** a cada vez: o prompt já está certo, a variância
  é do modelo. → **Travar o prompt e lotear**: N rolagens idênticas, escolhendo contra
  o critério escrito antes.

Iterar num erro estocástico é o jeito mais caro de errar: gasta crédito "consertando"
um prompt que estava bom, e ainda estraga o que funcionava.

Lote de variância (N idênticos) não é o mesmo que leque de estilo (N looks diferentes).
O primeiro colhe sorte; o segundo explora direção. Saber qual dos dois se está fazendo.

---

## Critério de aceite — escrever ANTES

Três a cinco itens falsificáveis por plano. Sem isso não existe "pronto", só
racionalização depois do fato. Exemplo:

```
1. O rosto é reconhecivelmente a mesma pessoa da canônica
2. A câmera faz UM movimento e ele é o Dolly In pedido
3. Nenhum membro extra, nenhuma mão deformada
4. A luz vem de UMA fonte, do lado, e deixa metade do rosto na sombra
5. O clipe fecha com o sujeito no terço esquerdo (entra o texto à direita)
```

---

## Disciplina de programação (vale para teaser e VSL)

Primeiro **a peça inteira em rascunho**, mesmo tosca — todos os planos existindo.
Depois concentrar iteração só nos planos que carregam peso. Sem esse corte, a
iteração come o orçamento nos três primeiros planos e a peça nunca fecha.

---

## Registrar o que foi gasto

Nunca medir por delta de saldo — outras sessões rodam na mesma conta em paralelo e o
delta atribui gasto alheio ao seu job.

```bash
higgsfield account status
higgsfield generate list --size 50 --json | jq -r '.[] | "\(.created_at) \(.job_type) \(.status)"'
```

Anotar por plano: quantas tentativas, o que reprovou, qual acertou. Sem denominador
não existe taxa de acerto — e sem taxa de acerto não dá para orçar o próximo projeto.

---

## Onde NÃO gastar

- **Vídeo IA em criativo orgânico** (Caixinha de Pergunta, Respondendo Comentários,
  Vídeo Palestra): esses formatos vendem **por parecerem gravados no celular**.
  Vídeo IA os mata. Vídeo IA serve para vilão abstrato, b-roll de VSL, hook de 2-3s
  e teaser cinematográfico.
- **4K.** Fora de escopo: o destino é rede social e tudo é recomprimido no upload.
  30cr contra 10cr é 3× por pixels que não chegam no espectador.
- **Gerar largo para recortar vertical.** Proporção não custa nada — gerar nativo.
- **`veo3_1 quality=basic`** — custa igual ao `high` (22cr). Sempre `high`.
- **Seedance sem referência** — `kling3_0` pro sai mais barato (12,5 contra 15cr).
- **Clipe de 10s quando dois de 5s resolvem** — custa igual e dá duas chances de acerto.
