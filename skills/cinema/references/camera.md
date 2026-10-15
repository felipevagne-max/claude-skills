# Câmera — vocabulário que a plataforma reconhece

Escrever o **nome exato do preset, em linha própria**: `Camera: Dolly In`.
Descrição em prosa ("a câmera se aproxima devagar") é a causa nº1 de clipe sem
movimento nenhum.

> Tabelas de preset adaptadas de `OSideMedia/higgsfield-ai-prompt-skill` (MIT),
> v3.35.0. O resto — economia, roteamento e o que executa pela CLI — é medido aqui.

---

## Dolly (translação)

| Preset | O que faz | Serve para |
|---|---|---|
| **Dolly In** | Avanço linear suave em direção ao sujeito | Intimidade, revelação, tensão subindo |
| **Dolly Out** | Recuo linear suave | Isolamento, despedida, abrir contexto |
| **Dolly Left / Right** | Trilho lateral | Acompanhar movimento horizontal, revelar cena |
| **Dolly Zoom In** | Avança e desafasta junto (efeito Hitchcock) | Vertigem, choque, ficha caindo |
| **Dolly Zoom Out** | Recua e fecha junto | Sufoco, mundo fechando |
| **Super Dolly In / Out** | Versão exagerada e rápida | Choque súbito, revelação de escala |

## Grua / vertical

| Preset | O que faz | Serve para |
|---|---|---|
| **Crane Up** | Sobe do chão para cima | Revelar escopo, íntimo → grandioso |
| **Crane Down** | Desce de posição alta | Apresentar local, depois personalizar |
| **Crane Over The Head** | Vertical direto de cima | Vulnerabilidade, vigilância, coreografia |
| **Levitation** | Flutuação suave para cima | Místico, transcendência |

## Órbita

| Preset | O que faz | Serve para |
|---|---|---|
| **360 Orbit** | Círculo completo ao redor | Isolamento emocional, ênfase dramática |
| **Arc** | Meia-lua ao redor | Virada emocional, revelação |
| **Lazy Susan** | Giro de prato, sujeito centrado | Produto, entrada de personagem, figurino |
| **Robo Arm** | Arco mecânico de precisão | Revelação de produto, cena coreografada |

## Zoom

| Preset | O que faz | Serve para |
|---|---|---|
| **Crash Zoom In** | Zoom brusco para dentro | Choque, ênfase num detalhe |
| **Crash Zoom Out** | Zoom brusco para fora | Desconexão, contexto súbito |

## Perseguição / ação

| Preset | O que faz | Serve para |
|---|---|---|
| **FPV Drone** | Drone ágil costurando o espaço | Perseguição, ação aérea, energia |
| **Action Run** | Baixa, atrás de quem corre | Fuga, encalço |
| **Handheld** | Mão orgânica, trepidação | Documentário, intimidade, caos |
| **Head Tracking** | Travada na cabeça do personagem | Primeira pessoa, desorientação |
| **Snorricam** | Presa no ator, fundo balança | Estresse, embriaguez, surto |

## Especiais

| Preset | O que faz | Serve para |
|---|---|---|
| **Bullet Time** | Sujeito congelado, câmera varre | Clímax de ação, impacto |
| **Dutch Angle** | Horizonte inclinado | Tensão psicológica, presságio |
| **Fisheye** | Distorção de grande angular | Surreal, skate, experimental |
| **Whip Pan** | Pan lateral borrado | Transição dinâmica |
| **Overhead** | Zenital direto | Coreografia, relação espacial |

## Tempo

| Preset | O que faz | Serve para |
|---|---|---|
| **Hyperlapse** | Timelapse com câmera andando | Cidade, viagem, transformação |
| **Timelapse Human** | Fixa, gente acelerada | Rotina urbana |
| **Timelapse Landscape** | Fixa, natureza acelerada | Clima, estação, nascer do sol |
| **Low Shutter** | Obturador lento, rastro | Velocidade, urgência, embriaguez |

## Através de objeto

| Preset | O que faz |
|---|---|
| **Through Object In** | Atravessa uma fresta para dentro de outro espaço |
| **Through Object Out** | Sai por uma fresta revelando o exterior |
| **Mouth In** | Entra pela boca aberta — transição para memória/sonho |

## Veículo

| Preset | O que faz |
|---|---|
| **Car Chasing** | Segue rente ao chão ao lado do carro |
| **Car Grip** | Presa no veículo, treme em cada buraco |
| **Buckle Up** | Trepidação violenta, perda de controle |

## Ângulos

**Low Angle** (poder) · **High Angle** (vulnerabilidade) · **Eye Level** (neutro) ·
**Bird's-Eye View** (zenital) · **Worm's-Eye View** (escala esmagadora) ·
**Ground Level** (rente ao chão) · **Canted Angle Left / Right** (inclinado, inquietação) ·
**Static Oblique** (fora de eixo) · **Over-the-Shoulder (OTS)** (conversa) ·
**POV / First Person** (imersão, terror) · **Two-Shot** (relação) · **Cowboy Shot** (meia-coxa).

## Tamanhos de plano

**ELS** vastidão, figura minúscula · **LS/WS** corpo inteiro + ambiente ·
**MLS** meia-coxa · **MS** cintura · **MCU** peito · **CU** rosto preenche o quadro ·
**ECU** um traço só (olho, mão) · **Insert** detalhe de objeto.

---

## Combinar movimentos

**Simultâneos** — no máximo dois, e compatíveis:

| Combinação | Efeito |
|---|---|
| Dolly In + Dutch Angle | Tensão fechando + instabilidade → revelação do vilão |
| Crane Up + 360 Orbit | Escala épica + isolamento → fim de batalha |
| FPV Drone + Crash Zoom In | Cinética + foco súbito → clímax de perseguição |
| Handheld + Action Run | Realismo cru + urgência → fuga |

**Nunca combinar contraditórios** — Dolly In com Dolly Out, Crane Up com Crane Down.

**Sequenciais** — declarar as fases com tempo, para o modelo renderizar em etapas
e não colapsar tudo num movimento ambíguo:
`Camera pans left from 0-3s tracking the character, holds, then pushes in on the face from 4-8s`

**Pan × glide.** Pan gira de um ponto fixo; glide translada pelo espaço. Pan estático
lê como ponto de vista escolhido; glide lê como câmera solta. Dizer qual dos dois.

---

## Sincronia câmera–emoção

A câmera é o dublê emocional do personagem focal. Cena calma com câmera trêmula lê
errado mesmo quando o resto está certo; cena de raiva com dolly liso lê como distante.

| Emoção do personagem | Prescrição de câmera |
|---|---|
| Raiva / tensão / no limite | Handheld respirando, trêmula e instável — ritmo quebrado, micro-espasmos nos dois eixos, amplitude pequena, ritmo irregular. Sem estabilizador. |
| Calma / controle / confiança | Handheld respirando, suave — ritmo regular, micro-amplitude constante. Vivo, mas estável. |
| Tristeza / vulnerabilidade | Handheld lento e baixo — respiração mais lenta, leve deriva para baixo, peso maior no operador. |
| Choque / revelação | Estático + push-in ou pull-out muito lento — congela no instante da revelação, movimento mínimo por 0,5–2s. |
| Ação | 60fps, obturador 180° — borrão de movimento limpo, sem arrasto de obturador longo. |
| Veredito / beat final | Plano zenital congelado, 0,3–0,5s — o tempo para, tudo travado. |
| Desabamento emocional | Recuo lento de médio/close para geral — "deixa o personagem em paz". Distância visual lida como espaço emocional, não abandono. |

**Arco dentro do mesmo plano** (raiva → controle numa tomada só): escrever em fases
nomeadas — abertura com a câmera da emoção de entrada, transição descrevendo como o
caráter da câmera muda (amplitude do handheld cai, deriva assenta, push-in desacelera),
fechamento com a câmera da emoção de saída. A câmera se move **com** o ator, não no
relógio dela.

Emoção genérica ("surpreso", "tenso") se decompõe num dos registros nomeados antes de
escolher a câmera.

---

## Lente e abertura pelo propósito do plano

| Propósito | Lente | Abertura |
|---|---|---|
| Close emocional extremo (testa ao queixo) | 85mm ou 100mm | F1.4 |
| Diálogo médio, two-shot | 50mm | F2.0–F2.8 |
| Geral / estabelecimento | 35mm | F4–F5.6 |
| Insert / detalhe de objeto | 50mm ou 85mm | F1.4 |
| Macro (poro, gota, tecido) | 45mm macro | F2.8 |

Duas cláusulas que andam junto com essas escolhas:
- **Trava de foco** em insert e close fechado:
  `focus plane locked on [objeto] from first frame to last — no focus drift, no rack focus, no autofocus hunting`
- **Proibição de distorção** em grande angular:
  `straight rectilinear lines, no barrel or pincushion distortion, no fisheye, no wide-angle warp`

---

## Duração por tipo de plano

| Tipo | Duração |
|---|---|
| Estabelecimento relâmpago / corte seco de abertura | 0,3–0,5s — **fração** de segundo |
| Uma fala média | 3–7s |
| Reação sem fala, com arco | 5–10s |
| Insert / geral / congelado | 0,3–2s |
| Close emocional com arco completo | 8–15s |

Como o custo é linear na duração, dividir um envelope de 15s por esta tabela é o que
separa um teaser com ritmo de três clipes de 5s colados.

---

## Micro-movimento precisa de distância

Dolly muito lento sem número: o modelo exagera. Declarar **percurso total e tempo**:
`over the full 7 seconds the camera pulls back only 10–15 centimeters — slow enough to barely register. No zoom, no sudden push.`

Nunca escrever `zoom` para movimento físico — nomear dolly / track / push-in / pull-out.

**E conferir ao contrário: o movimento declarado tem que conseguir produzir o
enquadramento final declarado.** "Push lento" não termina num close extremo saindo
de um geral; 10cm de recuo não entrega revelação de corpo inteiro. Quando movimento e
quadro final se contradizem, o prompt é internamente impossível — o modelo escolhe um
e improvisa o outro. Consertar pelo lado mais barato: aumentar o percurso ou reduzir a
mudança de enquadramento.

---

## Câmera por gênero

| Gênero | Primária | Secundária | Evitar |
|---|---|---|---|
| Produto / e-commerce | Orbit, push-in lento, estático | Crane down | Handheld, whip pan |
| Lifestyle / social | Handheld, estático, pan lento | Dolly ao lado | Dutch angle, crash zoom |
| Drama | Push-in lento, dolly out, tracking | Crane up | Movimento rápido, snap zoom |
| Videoclipe | Whip pan, snap zoom, tracking rápido | 360 orbit | Estático (entedia) |
| Terror | Aproximação lenta, plano fixo, Dutch angle | Crane down | Tracking rápido (quebra a tensão) |
| Ação / perseguição | FPV drone, tracking, handheld correndo | Crash zoom | Estático, orbit lento |
| Paisagem / viagem | Crane up, pan lento, sobrevoo | Dolly out revelando | Handheld, planos fechados |
| Comédia | Estático (deadpan), snap zoom | Whip pan | Movimento dramático lento |

## Frases de resultado previsível

| Intenção | Frase |
|---|---|
| Sem movimento | `locked-off static camera, no movement` |
| Aproximação lenta | `slow dolly push from medium shot to tight close-up over 8 seconds` |
| Seguir o sujeito | `handheld tracking following the subject, subtle shake, not chaotic` |
| Revelar escala | `crane shot rising from ground level to overhead` |
| Circular | `smooth 180-degree orbit at eye level, constant distance` |
| Zoom dramático | `crash zoom from wide to extreme close-up on impact` |
