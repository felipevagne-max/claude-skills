# Roteiro — da ideia à shotlist

O que separa "uns clipes bonitos" de uma peça é **a sequência**. Esta é a camada que
decide quantos planos existem, quanto cada um dura, em que ordem entram e o que
segura a continuidade entre eles.

> Heurísticas de densidade, tempo e monotonia adaptadas de
> `OSideMedia/higgsfield-ai-prompt-skill` (MIT). **Adaptação importante:** lá o alvo é
> o Seedance, que empacota `CUT 1..N` dentro de um prompt de 15s. Aqui o executável é
> o Kling em clipes de 5s — então **um plano = um job**, e o corte acontece no ffmpeg.

---

## A arquitetura de três camadas

Toda peça se escreve em três níveis, de cima para baixo:

```
1. PREFIXO DE ESTILO GLOBAL   — grade de cor, registro, textura, época.
                                 Vai LITERAL em todos os prompts.
2. GLOSSÁRIO DE ELENCO/ASSETS — cada personagem e objeto recorrente definido UMA vez,
                                 com descritores travados.
3. PROMPTS POR PLANO           — o que muda: câmera, ação, luz do plano.
```

**Editar uma vez, propagar em todos.** Mudou o grading? Muda no prefixo, e todos os
planos herdam. Um plano precisa quebrar o look global? Ele carrega um *override*
explícito — nunca uma divergência silenciosa.

**Prompt em inglês, sempre.** Os modelos foram treinados em inglês; o brief pode ser
em português, o prompt não.

---

## Orçamento de tempo — o portão aritmético

Orçar **antes** de escrever. Média de 4–6s por plano, com **um plano-herói de 6–8s**
reservado para o momento que carrega a peça.

| Runtime | Nº de planos |
|---|---|
| ≤15s | ~3 |
| ~20s | 4–5 |
| ~30s | ~6 |
| ~45s | 7–8 |
| ~60s | 9–11 |

**A soma das durações tem que fechar exatamente com o runtime pedido.** Orçamento que
não fecha entrega tempo morto ou um corte impossível — e o erro só aparece na timeline,
depois de gastar os créditos.

Aqui o clipe gerado é de 5s. Plano de 3s = gerar 5s e **aparar no ffmpeg** (aparar é
grátis; gerar mais curto não é mais barato, o preço é linear). Plano de 8s = gerar 10s
e aparar, ou dois de 5s emendados numa ação contínua.

---

## Densidade — quando agrupar, quando separar

**Agrupar num plano só** quando TODAS forem verdade: mesmo elenco · mesmo lugar ·
uma unidade emocional · cabe no envelope · dentro do limite de duração.

**Separar em planos distintos** quando QUALQUER uma for verdade:
- corte de locação
- entra ou sai alguém do elenco
- muda o setup de câmera/luz
- há um **arco de performance** (a emoção muda dentro do beat)
- é um insert

🔑 **Não fragmentar o luto.** Um momento emocional que respira quer UM plano longo, não
três curtos. Picotar emoção é o erro mais comum de shotlist gerada — o ritmo fica
publicitário e a cena não pousa.

---

## Auditoria de monotonia — ler a COLUNA, não o prompt

Depois de escrever tudo, ler **só a linha de enquadramento + movimento** de cada plano,
de cima a baixo, como uma coluna única.

**Nenhuma sequência de três planos consecutivos pode compartilhar o mesmo tamanho de
plano E o mesmo movimento de câmera.**

Quando todo plano lê "médio, push-in lento", o problema não é a duração — é que a
*função* e a *escala* dos planos não variam. Revisão plano a plano **não enxerga esse
defeito**; ele só aparece lendo a coluna. É o sinal mais denunciador de shotlist gerada
por máquina.

---

## Continuidade — o que carrega entre planos

### Bloco de identidade travado
Descritores visíveis, **copiados literalmente** em todos os planos onde a pessoa aparece.
Nunca nome próprio, nunca idade, nunca atributo não observável.

### Estado carregado
O que o plano anterior deixou no corpo: cabelo molhado, alça caída de um ombro, mão suja,
mesma roupa a menos que tenha trocado em cena. Sem isso o personagem "reseta" a cada corte.

### Linha de fora-de-quadro — o que mantém a reentrada legal
Quem estava no plano anterior e **não está** neste: declarar **lado de saída + último estado**.

```
Off-screen: o homem de casaco — saiu pela esquerda do quadro, ainda com a caixa.
```

Carregar por **um** plano; largar depois de dois planos ausente.

🔑 Reentrada pelo lado errado é a quebra de continuidade que o espectador **sente antes
de saber nomear**. Uma linha por personagem que saiu compra o lado certo de graça.
É a regra dos 180° escrita em prompt: se ele saiu pela esquerda, volta pela esquerda.

### Grade de cor
Repetir a **mesma frase** de grading, literal, em todos os prompts. Descrição de cor que
varia entre planos dá clipes que não pertencem à mesma peça — e no ffmpeg não tem conserto
barato.

---

## Match cut — costurar clipes gerados separados

Clipes gerados independentemente não cortam bem por acaso. O truque é **terminar um plano
e começar o seguinte no MESMO gesto** — a mão que toca a orelha, o copo que sobe, a
cabeça que vira. O movimento repetido permite "cortar na ação", que é o corte que o olho
não percebe.

Escrever o gesto-âncora explicitamente nos dois prompts, com as mesmas palavras.

---

## Âncora de personagem por plano

Para cada pessoa em quadro, o prompt declara:

| # | Atributo | Exemplo |
|---|---|---|
| 1 | Identidade | qual personagem (bate com o glossário) |
| 2 | Posição no quadro | "terço esquerdo", "centro" |
| 3 | Camada de profundidade | frente / meio / fundo |
| 4 | Ocupação do quadro | quanto da área ele preenche |
| 5 | Orientação do corpo | de frente, de costas, perfil, 3/4 |
| 6 | Pose | em pé, sentado, apoiado, em movimento |
| 7 | Direção do olhar | para a lente, para o outro personagem, fora de quadro |
| 8 | Pontos de contato | no que está apoiado/encostado |
| 9 | Estado travado | calmo, exausto, encharcado, ferido |
| 10 | Expressão facial | contido, mandíbula travada, sorriso pequeno |

Não é para despejar os dez em toda cena — é a lista de checagem do que, faltando,
o modelo inventa. Dois ou mais personagens no quadro ⇒ os itens 2, 3 e 4 viram
obrigatórios, ou eles se fundem.

---

## Coreografia é beat a beat, não verbo

"Ele dança" não significa nada para o modelo. Soletrar o movimento:

> *dois acenos secos de cabeça no tempo, ombros rolando um de cada vez, uma flexão leve
> de joelho, um estalo de dedos solto, fechando num quarto de giro.*

Vale para qualquer ação: soletrar gesto, olhar, respiração, micro-pausa.

---

## Entregável da fase de roteiro

Antes de gastar o primeiro crédito, existe:

1. Prefixo de estilo global (1 bloco)
2. Glossário de elenco/assets (1 bloco por entidade recorrente)
3. Tabela de planos: **nº · duração · enquadramento · movimento · ação · proporção**
4. Soma das durações = runtime pedido ✅
5. Auditoria de monotonia passada ✅
6. Critério de aceite (3–5 itens falsificáveis) por plano-herói
7. Custo total cotado (`generate cost` × nº de planos × tentativas previstas)

Só então rodar.
