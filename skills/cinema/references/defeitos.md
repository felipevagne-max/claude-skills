# Defeitos — o que quebra, por quê, e a frase que previne

Anexar **só** os constraints da categoria que este plano corre risco de ter.
Despejar a tabela inteira no prompt polui e piora o resultado.

> Adaptado de `OSideMedia/higgsfield-ai-prompt-skill` (MIT) + o que já foi medido aqui.

---

## Corpo e movimento

| Defeito | Por que acontece | Frase que previne |
|---|---|---|
| Membro extra / flutuando | Pose ambígua ou ocluída | `anatomically correct, all limbs visible and naturally positioned` |
| Braços fundidos entre dois | Personagens colados demais | Manter distância de um braço, ou separar em dois planos; `distinct body separation between characters` |
| Proporção estranha | Descritores contraditórios (alto + compacto) | Um descritor de corpo só, mantido igual |
| Movimento tremido / travando | Ações demais no mesmo clipe | 1 ação principal + no máx. 2 secundárias; quebrar em clipes |
| Deformação em ação rápida | Velocidade excede a coerência temporal | Gerar em câmera lenta e **acelerar no ffmpeg** |
| Golpe nomeado falha | "Chute giratório" exige coreografia multi-frame | Descrever o resultado, não a técnica: `general fighting energy`, `struggling` |
| Luta vira abraço | Contato próximo é ambíguo | Descrever posições do corpo, não o nome do golpe |

## Rosto e identidade

| Defeito | Por que acontece | Frase que previne |
|---|---|---|
| Rosto mudando entre frames | Sem referência canônica, ou descrições conflitantes | `--start-image` com a canônica; remover descritor contraditório |
| Identidade deriva entre planos | Descrição varia de prompt para prompt | **Copiar e colar idêntico** o bloco de identidade em todos |
| Rosto deformando no movimento | Identidade misturada com linguagem de movimento | Bloco de Identidade estático separado do bloco de Movimento |
| Expressão errada / congelada | Sem direção de micro-expressão, ou emoções conflitantes | Uma emoção por plano, nomeada |
| Pele de cera | Modelo errado ou descrição alisada demais | `natural skin texture, subtle imperfections` |

## Luz e textura

| Defeito | Por que acontece | Frase que previne |
|---|---|---|
| Cena chapada / sobre-iluminada | Prompt sem luz — o modelo cai no padrão neutro | Sempre nomear **fonte e qualidade**: `single hard side-light from a window`, `practicals only` |
| Textura piscando | Dois estilos competindo | Um estilo nomeado só |
| Produto parece barato | Sem superfície nem fundo especificados | Nomear a superfície (`raw concrete`, `black velvet`) e como a luz pega a borda |
| Cor inconsistente entre planos | Descrição de cor muda a cada prompt | Repetir a mesma frase de color grade, literal, em todos |

🔑 **Luz feia é a alavanca nº1 para tirar cara de estúdio.** Pedir "luz suave" é montar
um set. Luz dura de uma fonte só, contraluz, sombra cortando o rosto — é o que faz
parecer filmado.

## Degradação do quadro inteiro — palavra de qualidade × escolha de look

Alguns tokens que parecem "deixar mais filme" são lidos como instrução de **renderização**
e caem sobre o quadro todo. `film grain` solto amacia tudo; `imperfect focus` tira o
sujeito de foco junto.

**A distinção que governa:** o *conteúdo* pode ser imperfeito — luz desigual, composição
torta, quarto bagunçado, tremor do operador. A *qualidade de imagem* tem que ser nítida.
Imperfeição é escolha de assunto, nunca instrução de render.

| Escrito como nota solta | O que o modelo faz | Escrever no lugar |
|---|---|---|
| `film grain` (solto no fim) | Ruído no quadro todo, detalhe some junto | Nomear como look com o estoque e o dono: `Super 8MM warm grain, soft vignette` |
| `imperfect focus` / `soft focus` / `dreamy` | Perde nitidez global | Nomear o evento óptico, o elemento e o instante: `a brief focus hunt on the badge before it locks` |
| `edges not perfectly sharp`, `slight natural deviation` | Resolução efetiva cai, quadro empapa | Tirar, e pôr a imperfeição **no assunto**: quadro torto na parede, caneca lascada, luz chegando em um lado só do rosto |
| `blurry background` | O sujeito borra junto | Dizer **qual plano fica nítido** (abaixo) |
| `hazy` / `foggy` sem número | Névoa no quadro todo, sujeito incluído | Quantificar e localizar: `haze ramps 20% → 70% behind the ridge`, declarando a nitidez do sujeito |

### Profundidade de campo — dois pedidos diferentes

| O que se quer | Frase positiva | Quando |
|---|---|---|
| Tudo nítido, da frente ao fundo | `sharp focus throughout, deep depth of field` | Paisagem, estabelecimento, grupo, produto em set onde o fundo é informação |
| Sujeito nítido e fundo macio **de propósito** | `subject in sharp focus, background falling into soft bokeh` | Retrato, diálogo, isolar uma figura em cena cheia |

`blurry background` sozinho não responde nem um nem outro, porque nunca diz qual plano
deve continuar nítido.

## Temporal e continuidade

| Defeito | Por que acontece | Frase que previne |
|---|---|---|
| I2V quase parado | O prompt re-descreve a imagem estática | Descrever **só o que muda ou se move** + movimento de câmera explícito + movimento atmosférico (`dust floats`, `steam rises`) |
| Câmera não obedece | Movimento descrito em prosa | Nome exato do preset, em linha própria: `Camera: Dolly In` |
| Movimentos contraditórios | Dois movimentos conflitantes no mesmo prompt | Um movimento primário por plano |
| Continuidade quebra entre planos | Descrição de cena/personagem varia | Copiar e colar literal; travar a paleta em frase repetida |

## Filtro de conteúdo

O `nsfw` reage a **objeto do cenário**, não só a corpo — uma caixa de remédio barrou
duas gerações. Roupa curta também. **Job barrado não cobra**, então bloqueio não é
prejuízo, é retrabalho: trocar o objeto do cenário e repetir.

## Vieses do modelo (valem para vídeo também)

- Entrega **metade** de toda mudança de corpo e de geometria pedida — pedir o dobro
  da inclinação, do recuo, do ângulo.
- Rejuvenesce ao emagrecer.
- Amplifica adjetivo de imperfeição.
- Negação não vence prior de simetria: "não centralizado" perde para o hábito de centralizar.
