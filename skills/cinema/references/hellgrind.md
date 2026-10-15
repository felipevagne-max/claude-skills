# O método Hell Grind — fonte primária

Extraído do brief público do longa **Hell Grind** (Higgsfield Studio, 95 min, 15 pessoas,
<US$500k, 14 dias de geração, Cannes 2026 Marché du Film). O projeto foi aberto inteiro:
**115.451 assets**, com as pastas de cena visíveis — inclusive uma chamada `Regenerations`
com **14.593** itens, que é a queima de iteração tornada visível.
URL: higgsfield.ai/@higgsfield.studio/projects/hell-grind

> ⚠️ Este é o método **deles**, com orçamento deles. Aqui o orçamento é 1.000cr/mês. O que
> se aproveita é a **disciplina**, não a escala. Ver `economia.md`.

Stack que usaram: vídeo e fala **Seedance 2.0** · rostos e locações **Soul Cinema** ·
edição de imagem **Nano Banana Pro / Seedream 4.5** · **texto em quadro, props e
contra-planos de locação: GPT Image 2**.

---

## As 5 regras que eles destilaram

1. **Assets primeiro.** Não gerar um único plano antes de cada personagem, locação e
   objeto estar travado e testado. *"Esta regra sozinha economiza mais dinheiro que todas
   as outras juntas."*
2. **Descrever tudo, toda vez.** O modelo não tem memória. O descritor entra em todo
   prompt, palavra por palavra, nunca encurtado.
3. **Mudar uma coisa por vez.** Reescrever o prompt inteiro perde as partes que
   funcionavam. Uma linha por iteração, tudo no log.
4. **Dar menos liberdade ao modelo.** Um canto em vez de uma sala, uma âncora em vez de
   espaço aberto, um mapa em vez de adivinhação, uma ação por plano.
5. **Se o plano não fecha, simplificar o PLANO, não as palavras.** Partir em dois, tirar
   uma ação, mudar o ângulo.

**Regra das 10–15 iterações:** se não fechou nesse número, o problema não é a redação.

---

## Asset = texto + imagem

O **descritor** (texto completo) entra em todo prompt literal. A **imagem** é âncora.

### Ficha de personagem = 3 imagens
Close do rosto · corpo inteiro de frente · corpo inteiro de costas.
🔑 **E o corpo de frente vai SEM CABEÇA.** Parece loucura e conserta uma classe inteira de
planos quebrados: em plano geral o modelo puxava o rosto da figura pequena da ficha, onde
ele é minúsculo e borrado. Sem aquela cabeça, sobra um único lugar de onde tirar o rosto.

- Ficha **deliberadamente sem graça**: fundo cinza neutro, luz chapada, pele real com poro
  à mostra, zero retoque. **O cinematográfico não mora na ficha** — mora na locação e no
  prompt de vídeo. Assar grão e lente na ficha faz o personagem carregar aquilo para toda
  cena e parar de reagir à luz nova.
- Retrato grande em **3/4**, não de frente.
- Escolher o rosto **mais crível, não o mais bonito** — "bonito e falso" mostra a falsidade
  depois, no vídeo, quando já é tarde.
- **Conferir o olho:** precisa de reflexo de luz na pupila (catch-light). Sem isso o rosto
  fica morto, e nenhum modelo de vídeo atua com rosto morto.

### Nunca passar a imagem duas vezes inteira pelo modelo
Roupa, cicatriz e sangue entram como **mudança pontual**: alterar na ficha original com
Nano Banana Pro / Seedream, e trazer de volta **por máscara** num editor. Cada passe
completo destrói textura e desvia cor — depois de dois passes o rosto fica simétrico,
plástico e sem vida, e essa textura morta estraga a atuação no vídeo.

### Teste de estresse antes de travar
**Dez gerações** em poses e luzes diferentes. Tem que ser reconhecível em **10 de 10** —
e não sozinho: ao lado dos outros assets, na luz das cenas que vêm. Herói que se segura
sozinho costuma quebrar dividindo quadro. Falhou? **O problema é a descrição, não o modelo.**

### Cada ESTADO é um asset separado
`@roco`, `@roco_wet`, `@roco_blood` — cada um com descrição própria. Misturar estados num
texto só faz o modelo misturá-los entre planos. Locação idem: dia, noite e chuva são três
assets. **Props também**: o artefato-chave tinha três versões — completa para close,
pequena e ensanguentada para revelação rápida na palma, e uma "escondida" para plano de
punho fechado, onde o prompt **proíbe mostrar o cristal** e só permite luz azul entre os dedos.
*Separar estados é mais barato que brigar com o modelo.*

### Locação: gerar para os ângulos futuros
- Ficha de locação em **3/4**, nunca frontal. Frontal vira papel de parede chapado no
  geral, e além das bordas o modelo inventa vizinhança nova a cada vez.
- **Deixar uma âncora** em toda locação — coluna, luminária, sofá — e amarrar a marcação
  nela. *"O herói na luminária, de frente para a porta"* funciona; *"o herói na sala"* é loteria.
- **Uma lógica de luz só**: uma fonte, uma direção de sombra, nunca dois sóis.
- **Contra-plano, jeito 1:** gerar um canto da mesma sala no GPT Image 2 / Nano Banana,
  casando o foco suave do original.
- **Contra-plano, jeito 2** (descoberto tarde): gerar um **vídeo da locação vazia** com a
  câmera caminhando devagar pelo espaço — o Seedance desenha os outros lados de forma
  consistente com a ficha. Print do ângulo que quiser → melhorar textura no Seedream.
  *Uma ficha de locação inteira a partir de uma imagem só.*

### Nomear o PAPEL de cada referência
Senão o modelo decide sozinho e decide errado — copia a composição em vez do rosto, ou o
rosto em vez da paleta.
```
@roco for character reference
@loc_cave_front for location reference
```
Referência de locação leva **proibição de herança** explícita:
*"do not use as a starting frame, do not inherit the composition, the angle or the color —
take only the space and the texture."*

---

## O esqueleto de prompt (15 blocos, ordem fixa)

```
SCENE CONTEXT              cabeçalho "EXACT N CHARACTERS — NO DUPLICATES"
ACTIVE REFERENCES          tags com o PAPEL de cada uma nomeado
LOCATION MAP               a geografia do lugar em palavras
FIRST FRAME AND SPATIAL BLOCKING   quem está onde no frame 1
FORMAT MODE                take único ou cortes duros, duração, tempo real
OPTICS                     lente e plano de foco
CAMERA                     como a câmera se comporta E o que ela nunca faz
ACTION TIMING              a ação beat a beat, em segundos
PHYSICS                    peso, contato, inércia de tudo que se move
LIGHTING                   uma lógica de fonte, de onde vem
AUDIO                      descritor de voz + falas exatas; SFX apenas
CHARACTER ACTING           estado, quer o quê, esconde o quê, ritmo, o que muda
STYLE                      o Style Prefix, colado literal
QUALITY                    exigência de detalhe e estabilidade
POSITIVE CONSTRAINTS       toda contagem e proibição escrita como o que ESTÁ no quadro
```

Prompts deles rodavam **3.000–4.000 palavras**. *"Tamanho não é o inimigo; beat sobrecarregado é."*
**Até três frases por beat.** Presente do indicativo, frases curtas.

### 🔑 Regras de redação que quebram o hábito

- **Ação só em forma POSITIVA.** O modelo ignora *"não cai de costas"* — ou faz o oposto.
  Escrever *"cai de barriga"*. Por isso o bloco chama-se **POSITIVE** Constraints:
  toda proibição vira contagem do que existe — *"exactly ONE mannequin, NEVER render a second one"*.
- **Nunca escrever idade, em idioma nenhum** — o filtro de conteúdo fica muito mais rígido
  ao ler menor de idade. Em vez de idade: papel, roupa, ação.
- **Dicionário de banimento** de palavras que o modelo pune: `dark` → `low key`;
  `jolting` → `rapid motion`.
- Personagem está em quadro **desde o primeiro frame**, e nunca olha para a câmera sem pedido.
- Cabeçalho de contagem não é formalidade: o modelo **adora somar gente e clonar móvel**.

### GEO SPATIAL LAYOUT — o bloco que consertou o problema mais caro

Personagens teleportam, trocam de lugar, a câmera pula de lado. Causa: **o modelo não
lembra quem estava onde no plano anterior.** A cura é uma planta baixa em poucas linhas —
objetos-marco, o que está à direita, à esquerda, onde a câmera fica. **Sem heróis, sem
ação, só o lugar.** Escreve-se uma vez por cena e cola-se em todo plano dela sem mudar.

```
GEO SPATIAL LAYOUT (locked across every shot — pure spatial map):
— PLATFORM = raised circular ritual stone disc at the edge of a cliff.
— ALTAR-MONOLITH: at the cliff edge, MID-RIGHT relative to the platform.
— RITUAL CENTER: CENTER-LEFT, ~3 m from the altar.
— 180° AXIS: camera ALWAYS stays on the corpse-field side — it NEVER crosses the line.
— BACK-LIGHTING: crimson horizon glow from BEHIND the platform, rim-lighting silhouettes.
```

**Lados só existem a partir da câmera** — `frame-left` / `frame-right`. O modelo **não
entende "à esquerda do herói"**. Posições vêm dos marcos e **em metros**. Escrever de que
lado a câmera está e que linha ela nunca cruza. Depois de todo corte, **renomear quem está
onde e olhando para onde**. Diálogo estático ganha **um canto**, não a sala inteira —
menos espaço, menos escolha errada.

### O primeiro segundo é sempre um plano geral
Um segundo no início da cena, sem fala e sem ação: o modelo *"fotografa"* o arranjo e o
segura nos planos seguintes. Tirar esse segundo faz os personagens trocarem de lugar.
Truque: alguém solta um *"hm"* nesse segundo — ajuda o Seedance a tratar o geral como plano
separado. E se o plano responde ao anterior, **alimentar a cauda da fala anterior** nesse
primeiro segundo: o ator responde a coisa certa no tom certo e os dois clipes colam na emenda.

### 🔑 Ação complexa nunca fica no MEIO do timing
*"Nossa porta não quebrava: o herói se mexia ao lado dela e congelava."*
A correção: **a ação ABRE o prompt** — *"ele JÁ está no meio do golpe, a porta JÁ rachando"* —
e a aproximação até a porta vira **um plano separado**.

### Outros achados sob pressão de prazo
- **Multidão** = um asset de "personagem" com faixa de alturas e roupas; 1-2 figurantes
  ganham asset próprio para close. Em plano médio, **declarar o número** — "20+" — senão o
  modelo dá três pessoas numa tomada e cem na outra.
- **Transição entre dois espaços** se segura numa soleira: as duas locações no mesmo
  prompt, e a emenda é um vão com contraste de luz — *"sala âmbar quente, corredor azul
  frio além do arco"*. O contraste explica a troca de paleta e perdoa erro de geometria.
- **Gigante precisa de âncora de escala** — comparação de tamanho em todo prompt **mais**
  uma figura humana no quadro para medir. Sem os dois, o modelo encolhe o gigante de volta
  para altura humana.

---

## Style Prefix deles (colado literal no fim de TODO prompt)

```
Style: 8K IMAX. Photorealistic — no 3D render, no game engine, no game-cutscene aesthetic.
Cinematography: floating immersive camera that lives with the actors; natural motivated
light; painterly composed frames, strong silhouettes against the light.
Lighting: Natural light only — contre-jour backlight, camera on shadow side, atmospheric
haze throughout. Key light from sky and windows only.
Color: 60:30:10 — dominant / secondary / accent.
Camera: Physical cine lens. 180° shutter motion blur.
Skin: Pore-level realism — vellus hair, asymmetric moles, capillary flush, pore-shadow
matching on-set light.
Acting: Hollywood — micro-pauses before reactions, precise eye-line, wet living eyes with
catch-lights, visible breath and chest rise.
Physics: Gravity and inertia respected — mass has real weight, correct contact shadows.
Composition: Rule of thirds + golden ratio. Every person moving from frame one.
Continuity: Characters, props, environment identical across every cut. No identity drift.
Technical: 24fps smooth motion. 8K detail. No jitter.
Audio: Environmental SFX only. No music. No subtitles.
```

Fecha com tags técnicas: `Photoreal. NON-IP. [aspect]. [duração]s. SFX only. NO CGI. Cinematic.`

🔑 **"SFX only. No music." é obrigatório.** Música é pós-produção; trilha gerada só atrapalha
a montagem.

---

## Atuação: escrever COMPORTAMENTO, não sentimento

Cena viva = herói que quer algo, algo no caminho, e ele age para conseguir. A emoção nasce
sozinha dessa briga. **Dar meta e obstáculo, e mudar a tática ao longo da cena**: ele
brinca → falha → pressiona → falha → implora. Cada mudança é um evento visível: pausa,
troca de postura, troca de tempo. Cena em que o herói faz a mesma coisa do início ao fim
sai chapada.

**Escrever física, não adjetivo.** Em palavra de emoção — *"triste"*, *"bravo"* — o modelo
improvisa e entrega raso. Descrever o trabalho do músculo: tremor, mandíbula travando e
soltando, maçã do rosto tensionada, expiração leve pelo nariz. Por cima, **intenção**: uma
linha de monólogo interno marcada `INNER (unspoken)`.

- **Piscada em fases** — *"uma piscada preguiçosa → uma DUPLA rápida → uma piscada DURA de
  reset"* — o sinal mais barato de rosto vivo.
- **Direção de olhar clara**, ou olhos correndo.
- **Regra da micro-vida** contra rosto congelado: **um micro-evento visível a cada 1–2s** —
  o peito sobe, a narina mexe, a sobrancelha tensiona e solta.
- **Descrever imobilidade como tensão contida, nunca como congelamento** — frases como
  *"ninguém se move"* congelam o quadro literalmente.

**Três coisas que separam plano vivo de morto:**
1. A reação começa **antes da outra fala terminar** — quem ouve entende no meio da frase e
   o rosto já responde. Depois de evento importante, dar uma fração de segundo antes de falar.
2. **Emoção não desliga na hora** — depois de um momento pesado a respiração ainda está
   irregular, a mão ainda trêmula; esse rastro atravessa para o próximo clipe e costura o corte.
3. **Manter as mãos do herói ocupadas** — ele não "conversa", ele conserta, conta, serve, e
   fala por cima; o acento mais forte da cena é o momento em que ele **para** esse trabalho.

**Fala no prompt:** voz e emoção → a linha entre aspas → ação física → reação facial.
Falas vivem **só** no bloco AUDIO — nenhuma palavra de fala dentro da ação. O Seedance
inventa "uhm", risadinha e frases inteiras, então o prompt carrega bloqueio duro: cada um
fala **somente** a linha entre aspas; quem não tem fala fica em silêncio total; "meio riso"
escrito na ação é **expressão facial, sem som**.

---

## Pós-produção

- A montagem roda **em paralelo** com a geração. O montador pede o que falta ("preciso de
  um inserto de mãos") — regeração custa minutos, então a montagem **molda** a produção.
- 🔑 **Geração quase sempre parece lenta.** Cortar **mais agressivamente do que parece
  certo**, e planejar **aparar o primeiro e o último meio segundo de todo clipe** — as
  bordas derivam.
- Passe de limpeza **depois do corte travado e ANTES da cor**: dedo extra, textura
  "fervendo", texto falso em placa. Prioridade: close de rosto e de mão.
- Cor começa por **unificação** — cada geração vem com grade próprio. O look já foi assado
  na ficha de locação, então o colorista **refina, não inventa**.
- Voz: limpar a fala gerada (ruído, timbre, espaço), não regravar.
- **Ambiência contínua compartilhada** é o que cola planos gerados num espaço só, mesmo
  onde a imagem deriva.

---

## O que isso corrige no fluxo daqui

| Falha comum | Regra do Hell Grind |
|---|---|
| Objeto sai errado (porta, trava, tela) | **É PROP ASSET** — gerar como imagem primeiro, travar, referenciar |
| Personagem/lugar muda entre planos | Descritor literal em todo prompt + ficha 3/4 + âncora |
| Gente troca de lugar, câmera pula de lado | **GEO SPATIAL LAYOUT** colado em todos os planos da cena |
| Ação complexa não acontece | Ação **abre** o prompt, já em curso; aproximação vira outro plano |
| Negativo ignorado | Reescrever como **POSITIVE CONSTRAINT** com contagem |
| Rosto morto | Catch-light + piscada em fases + micro-evento a cada 1–2s |
| Clipe arrasta | Aparar 0,5s de cada ponta, cortar mais duro do que parece |
