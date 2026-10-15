# Argument Bible Contract

The Argument Bible is the immutable strategic contract for one run. It records the
belief transformation, causal argument, evidence boundaries, and unresolved gaps
that every writer and reviewer must obey. The Chief approves the first Bible and is
the only role allowed to publish a new version; workers may identify conflicts or
request a change, but they must never silently alter a frozen Bible.

## Version metadata

Every published Bible must begin with:

```yaml
version: 1
created_at: 2026-10-10T14:30:00-03:00
approved_by_chief: true
```

- `version`: A positive integer increased by one for every Chief-approved change.
- `created_at`: The ISO 8601 timestamp at which that version was frozen.
- `approved_by_chief`: Must be `true` before the Bible can be dispatched.

A worker always cites the received `version`. A requested correction does not create
a version; only the Chief can reconcile the request, publish the next integer version,
and redispatch it to every affected worker.

## Required fields

All fields below are required and must appear at the top level of
`03-argument-bible.md`.

| Field | Definition | One-sentence quality test |
|---|---|---|
| `piece_type` | The requested persuasive format, such as VSL, webinar, or advertorial. | A reader can name the delivery format and its expected reading or listening context without inference. |
| `audience` | A qualitative description of the specific prospect, situation, and relevant identity. | The description is narrow enough that the intended prospect recognizes themselves and an adjacent audience does not. |
| `emotional_state` | The prospect's current emotional temperature and posture before encountering the piece. | It explains how the prospect is likely to interpret the opening rather than merely listing an emotion. |
| `awareness` | What the prospect already knows about the problem, available solutions, and this solution. | The chosen level makes clear what can be assumed and what must first be explained. |
| `sophistication` | How many similar promises, mechanisms, and approaches the prospect has already encountered. | It identifies the familiar language or claims that the piece must avoid, deepen, or reframe. |
| `current_belief` | The belief that currently keeps the prospect in the old interpretation or behavior. | It is written as a proposition the prospect could naturally say or think. |
| `target_belief` | The belief the prospect must hold before the requested action becomes reasonable. | If the prospect accepts it, the next action follows without an unrelated logical leap. |
| `one_belief` | The single unifying conviction that connects the prospect's problem, the new explanation, and the solution. | Every major section can reinforce it without requiring a second competing thesis. |
| `accepted_premise` | A truthful starting point the prospect is already likely to accept. | It can open the argument with low resistance and does not smuggle in the conclusion. |
| `single_villain` | The one named force, pattern, or process responsible for the persistent problem. `EXPLICIT_VILLAIN_CANDIDATE_SET_IS_CLOSED`: if the user provides a finite candidate set and asks for a choice among it, select exactly one member of that set; an alias must still identify that member, and the system must never introduce a fourth villain. | All causal layers point to this same villain without blaming or humiliating the prospect, and any explicit user-supplied candidate-set constraint is preserved. |
| `root_cause` | The deepest supported cause that explains why the problem persists. | It explains repeated failure and is supported, demonstrable, or explicitly marked as a gap. |
| `broken_process` | The sequence by which the villain and root cause produce the unwanted outcome. | Each step follows causally from the previous one and can be expressed without vague magic. |
| `solution_mechanism` | The distinct process by which the solution interrupts or reverses the broken process. | It directly answers the stated root cause and can be explained or demonstrated concretely. |
| `central_promise` | The primary desired outcome the piece may persuasively present. | It is specific enough to matter and no stronger than the available evidence permits. |
| `promise_boundary` | The conditions, limits, exclusions, and wording constraints around the central promise. | It makes clear what the copy must not imply, guarantee, or universalize. |
| `dominant_emotion` | The one emotion that leads the piece and organizes its pressure and relief. | Secondary emotions support it rather than causing the piece to change emotional direction. |
| `argument_chain` | An ordered list of stable-ID claims from accepted premise through problem, cause, process, solution, and conclusion. | Removing any link reveals either a necessary bridge or a genuinely redundant step. |
| `proof_ledger` | A list mapping every material `claim_id` to evidence state, support, authorization, permitted wording, and source or gap. | Every factual or outcome claim can be traced to one ledger entry with an allowed use. |
| `objections` | The prospect's conscious and silent resistance, ordered by dependency and paired with an answer and resolution status. | Each objection has a truthful answer or is explicitly left unresolved instead of being evaded. |
| `known_facts` | Facts supplied by the user or an authorized source as input evidence with provenance and use limits, not automatic permission to publish. | Every entry records enough provenance to distinguish it from interpretation or positioning. |
| `assumptions` | Working inferences used to continue despite incomplete inputs. | Each assumption is visible, reversible, and never presented to the prospect as established fact. |
| `open_gaps` | Missing evidence, decisions, examples, quotations, or facts required for stronger or publish-ready copy. | Every unresolved dependency is named together with what would close it and where it affects the piece. |

`COMPONENT_EXISTENCE_DOES_NOT_AUTHORIZE_FUNCTION`: a component's existence does not authorize its purpose.
A list of modules, meetings, calls, bonuses, or deliverables
permits the Bible to record only their existence unless an authorized source defines
their function. Never infer that modules organize learning, meetings provide support,
calls create accountability, or bonuses improve results. Record the unknown function
in `open_gaps` instead of laundering a plausible convention into a product fact.

## Optional context extensions

The approved specification also defines the following optional-but-recommended context
extensions: `project`, `objective`, `declared_desire`, `private_desire`,
`dominant_fear`, `current_identity`, `desired_identity`, `approved_vocabulary`, and
`forbidden_vocabulary`. They improve continuity and voice but are not required by the
current validator. When one or more extensions are absent, writers must receive the
accepted Prospect Mind Map alongside the identical frozen Bible rather than infer the
missing psychology or vocabulary.

## Structured field schemas

Every link in `argument_chain` receives a stable `claim_id` that does not change when
wording is edited. Use these object shapes:

```yaml
argument_chain:
  - claim_id: "C01"
    role: "accepted_premise"
    claim: "The exact proposition used in the argument."
    depends_on: []
    material: true

proof_ledger:
  - evidence_id: "E01"
    claim_id: "C01"
    state: "PROVEN"
    support: "What the evidence actually establishes."
    source: "Internally traceable source or authorized input."
    fact_ids: ["F01"]
    authorization: "How this evidence may be used publicly."
    permitted_use: "The narrowest allowed wording or demonstration."

objections:
  - objection_id: "O01"
    objection: "The prospect's resistance in natural language."
    answer: "Truthful answer or [PROVA NECESSÁRIA] — exact missing input."
    status: "ANSWERED"
    affects_claim_ids: ["C01"]

known_facts:
  - fact_id: "F01"
    fact: "A fact supplied as input evidence."
    source: "Internally traceable source."
    authorized_use: "Internal only, public, anonymous, or another explicit limit."

assumptions:
  - assumption_id: "A01"
    assumption: "A reversible working inference."
    rationale: "Why work can continue provisionally."
    validation_needed: "What would confirm or reject it."
    risk_if_wrong: "Which argument or copy section would change."

open_gaps:
  - gap_id: "G01"
    need: "The missing fact, proof, decision, quotation, or example."
    affects_claim_ids: ["C01"]
    resolution: "What would close the gap."
    status: "OPEN"
```

Allowed objection statuses are `ANSWERED`, `PARTIAL`, and `UNRESOLVED`; `PARTIAL` and
`UNRESOLVED` require a visible placeholder and matching `open_gaps` entry. A material
argument link must have at least one linked `proof_ledger` entry, even when its state
is `POSITIONING`, `PLACEHOLDER`, or `FORBIDDEN`. `known_facts` records input evidence,
not permission to publish a claim directly: every material claim used in public copy
must still pass through `proof_ledger` and cite its stable `claim_id`.

## Proof Ledger states

Each ledger entry must contain at least `evidence_id`, `claim_id`, `state`, `support`,
`source`, `fact_ids`, `authorization`, and `permitted_use`; use `fact_ids: []` when a
positioning entry has no factual input dependency.

| State | Meaning | Use rule |
|---|---|---|
| `PROVEN` | The claim is supported by user-provided or authorized verifiable evidence. | State only what the cited evidence supports and preserve material conditions. |
| `TESTIMONIAL` | The statement is a real account whose identity and authorization for use are internally verifiable. | Preserve the person's meaning and scope; public attribution may be anonymized when privacy or consent requires it, but the internal source and authorization must remain auditable. |
| `DEMONSTRABLE` | The claim can be shown directly in the piece through an honest demonstration. | Describe only what the demonstration visibly establishes. |
| `POSITIONING` | The statement is an explicit opinion, interpretation, or strategic frame rather than an objective fact. | Use it as framing and never disguise it as research, measurement, or neutral reporting. |
| `PLACEHOLDER` | A real fact or evidence item is still required before publish-ready delivery. | Mark the exact location with `[PROVA NECESSÁRIA]` or another validator-recognized placeholder. |
| `FORBIDDEN` | The claim is unsupported, unsafe, misleading, disallowed by the user, or outside the promise boundary. | Do not use, imply, paraphrase, or route around it. |

When evidence supports only part of a claim, narrow the claim or assign
`PLACEHOLDER`; never inflate the evidence to match the desired sentence.

## Compact fictional example

The following example is invented for this contract and makes no external factual
claims.

```yaml
version: 1
created_at: 2026-10-10T14:30:00-03:00
approved_by_chief: true

piece_type: "VSL"
audience: "Freelancers que terminam o dia ocupados, mas sem concluir a tarefa mais importante."
emotional_state: "Cansados e desconfiados de mais um método; querem alívio sem uma rotina rígida."
awareness: "Reconhecem a dispersão e já tentaram listas de tarefas, mas não conhecem esta solução fictícia."
sophistication: "Já viram promessas genéricas de foco, hábitos e produtividade em excesso."
current_belief: "Meu problema é falta de disciplina para seguir uma lista maior."
target_belief: "Eu concluo melhor quando decido uma prioridade e protejo um bloco curto antes das demandas reativas."
one_belief: "Quando uma prioridade protegida vem antes do ruído, terminar o que importa deixa de depender de uma lista infinita."
accepted_premise: "Uma tarefa importante recebe menos atenção quando compete o dia inteiro com mensagens e pedidos."
single_villain: "A Lista Sem Fim"
root_cause: "Todas as tarefas parecem igualmente urgentes, então nenhuma recebe proteção deliberada."
broken_process: "Capturar tudo -> tratar tudo como prioridade -> reagir ao item mais recente -> adiar a tarefa central."
solution_mechanism: "O Bloco Um: escolher uma entrega, definir o primeiro movimento e protegê-la antes de abrir o fluxo reativo."
central_promise: "Ajudar o usuário a começar o dia pela entrega que escolheu como mais importante."
promise_boundary: "Não promete horas extras, renda, desempenho universal nem eliminação de distrações."
dominant_emotion: "Alívio"
argument_chain:
  - claim_id: "C01"
    role: "accepted_premise"
    claim: "Quando mensagens e pedidos disputam atenção ao mesmo tempo, a tarefa escolhida também entra nessa disputa."
    depends_on: []
    material: true
  - claim_id: "C02"
    role: "broken_process"
    claim: "Tratar cada entrada nova como prioridade retira proteção da entrega central."
    depends_on: ["C01"]
    material: true
  - claim_id: "C03"
    role: "solution_mechanism"
    claim: "Escolher uma entrega e seu primeiro movimento antes do fluxo reativo interrompe essa competição inicial."
    depends_on: ["C02"]
    material: true
  - claim_id: "C04"
    role: "conclusion"
    claim: "O produto fictício organiza essa escolha em um ritual chamado Bloco Um."
    depends_on: ["C03"]
    material: true
proof_ledger:
  - evidence_id: "E01"
    claim_id: "C01"
    state: "POSITIONING"
    support: "Enquadramento causal explícito, não apresentado como pesquisa ou resultado medido."
    source: "Argumento fictício deste exemplo."
    fact_ids: []
    authorization: "Uso público apenas como raciocínio, sem atribuição científica."
    permitted_use: "Descrever a disputa de atenção como interpretação, não como descoberta comprovada."
  - evidence_id: "E02"
    claim_id: "C02"
    state: "POSITIONING"
    support: "Interpretação lógica do processo fictício A Lista Sem Fim."
    source: "Argumento fictício deste exemplo."
    fact_ids: []
    authorization: "Uso público apenas como posicionamento."
    permitted_use: "Explicar o processo sem alegar frequência, causalidade científica ou resultado universal."
  - evidence_id: "E03"
    claim_id: "C03"
    state: "DEMONSTRABLE"
    support: "A demonstração pode mostrar a escolha da entrega antes de abrir o fluxo reativo."
    source: "Brief fictício deste exemplo."
    fact_ids: ["F01"]
    authorization: "Demonstração pública do fluxo fictício."
    permitted_use: "Mostrar a ordem das ações; não alegar ganho de produtividade."
  - evidence_id: "E04"
    claim_id: "C04"
    state: "DEMONSTRABLE"
    support: "Demonstração fictícia da interface durante a VSL."
    source: "Brief fictício deste exemplo."
    fact_ids: ["F01"]
    authorization: "Demonstração pública do recurso fictício."
    permitted_use: "Mostrar a seleção e o registro acontecendo; não alegar resultados de produtividade."
objections:
  - objection_id: "O01"
    objection: "Parece apenas outra lista de tarefas."
    answer: "Demonstrar que o fluxo aceita uma única entrega e exige o primeiro movimento, em vez de acumular itens."
    status: "ANSWERED"
    affects_claim_ids: ["C04"]
  - objection_id: "O02"
    objection: "Minha manhã muda todos os dias."
    answer: "[PROVA NECESSÁRIA] — confirmar se o bloco pode ser reagendado no produto real."
    status: "UNRESOLVED"
    affects_claim_ids: ["C03", "C04"]
known_facts:
  - fact_id: "F01"
    fact: "Neste cenário fictício, o produto deixa o usuário escolher uma prioridade e um primeiro movimento."
    source: "Brief fictício deste exemplo."
    authorized_use: "Demonstração pública dentro do exemplo fictício."
assumptions:
  - assumption_id: "A01"
    assumption: "O público prefere uma rotina curta."
    rationale: "Permite testar uma rota provisória sem afirmar a preferência como fato."
    validation_needed: "Pesquisa qualitativa com o público pretendido."
    risk_if_wrong: "A abertura e o enquadramento de simplicidade precisam mudar."
open_gaps:
  - gap_id: "G01"
    need: "Demonstração real da interface para substituir o exemplo fictício."
    affects_claim_ids: ["C03", "C04"]
    resolution: "Gravar ou fornecer o fluxo real autorizado."
    status: "OPEN"
  - gap_id: "G02"
    need: "Confirmação de que o bloco pode ser reagendado."
    affects_claim_ids: ["C03", "C04"]
    resolution: "Validar a propriedade no produto real antes de responder O02."
    status: "OPEN"
```
