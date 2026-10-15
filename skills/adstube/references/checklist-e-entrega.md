# Checklist de auditoria + modelo de entrega

Rodar a Parte A em TODA peça antes de exportar. Cada item que falhar vira linha na tabela de
auditoria da entrega, com a política e a correção. Nunca "passa com ressalva" em item marcado
⛔ — esses são egregious ou bloqueio total.

## Parte A — Checklist por peça

### A1. Aprovação do criativo (áudio + legenda + tela + título)
- [ ] Sem "segredo/escândalo/ninguém te conta", "você não vai acreditar", "assista até o fim"
- [ ] O gancho diz O QUE é (o loop é sobre como/por quê)
- [ ] Sem pergunta ou afirmação diagnóstica em 2ª pessoa ("você tem/está/sofre de…")
- [ ] Sem ameaça/dano/urgência de perigo ("antes que seja tarde", "vai morrer", "sua casa pode ser a próxima")
- [ ] Sem cura, "100%", "garantido", kg/R$ com prazo, "sem esforço", "coma de tudo"
- [ ] Sem nome/comparação com remédio (Ozempic, GLP-1, "remédio", "medicação")
- [ ] Sem antes/depois do corpo; sem close de sintoma com tom negativo
- [ ] Depoimento com número ⇒ legenda "resultados variam de pessoa para pessoa"
- [ ] ⛔ Sem celebridade/médico famoso/youtuber/logo de TV sem autorização (inclui IA)
- [ ] Sem botão falso, seta, notificação, print de WhatsApp/iPhone, enquete falsa
- [ ] Sem palavrão (bip não salva) e sem linguagem/pose sexual
- [ ] ⛔ Nicho sexual/NoFap: nenhuma palavra sexual em áudio, legenda, título ou página
- [ ] Sem funeral/choro/acidente/vício retratado cru
- [ ] Nome ou logo da marca aparece (não na abertura)
- [ ] Preço/oferta citados = página = checkout (inclusive parcela)

### A2. Conversão (física do YouTube)
- [ ] Voz já falando no segundo 0 (sem vinheta/logo/música de abertura)
- [ ] Os 5s qualificam pelo CONTEXTO e repelem quem não compra
- [ ] In-stream: promessa de aula ou motivo para passar dos 30s até o segundo 15
- [ ] Ensina o quê e o porquê, nunca o como
- [ ] Mecanismo com nome próprio aparece
- [ ] CTA de baixo atrito, falado E escrito, com o próximo passo descrito
- [ ] CTA aparece antes do fim em peça >90s (e no 1º minuto em VSL longa)
- [ ] Duração dentro da faixa do papel (E1 60-180s · E2 15-30s · E3 3-8min · E4 20-60s)
- [ ] ≥10s (senão não roda in-stream)
- [ ] Shorts é roteiro próprio, não o in-stream recortado

### A3. Landing page e domínio (auditar uma vez por pacote)
- [ ] URL final no mesmo domínio; sem redirect para outro domínio (hoplink/bitly/produtor)
- [ ] Conteúdo original com valor (não é ponte)
- [ ] ⛔ Sem notícia falsa/portal imitado/"como visto na TV" falso
- [ ] Sem chat simulado, notificação falsa, exit redirect, back-button hijack, auto-redirect, pop-up cobrindo
- [ ] Preço total, modelo e intervalo de cobrança visíveis antes do checkout
- [ ] Rodapé: razão social/CNPJ, contato que funciona, Sobre, privacidade, termos, reembolso
- [ ] Sem palavra-gatilho desnecessária em QUALQUER página do domínio
- [ ] ⛔ Página igual para Googlebot e usuário (Search Console + user agent AdsBot; crawler dos EUA liberado)
- [ ] Um tema por domínio (oferta sensível em domínio próprio)
- [ ] gclid/wbraid sobrevive até o checkout
- [ ] Finanças BR: Financial Services Verification feita; endereço e taxas visíveis; quem presta o serviço está claro
- [ ] Saúde BR: alegação dentro do permitido pela ANVISA

### A4. Conta
- [ ] Verificação de anunciante; pagador = documentos = marca
- [ ] ⛔ Nunca conta nova para contornar reprovação/suspensão
- [ ] Anúncios reprovados antigos REMOVIDOS (não só pausados)
- [ ] Nicho sensível: sem remarketing/Customer Match/lookalike no grupo
- [ ] Conta nova: começar pela oferta mais limpa

## Parte B — Modelo de entrega

### B1. Arquivo `00 - Briefing e Auditoria.docx`

```
[PROJETO] — YouTube Ads
Data · Modo (CRIAR / TRADUZIR / AUDITAR)

ESPINHA DORSAL
Público (contexto, não diagnóstico): …
Mecanismo (nome próprio): …
Inversão: …
Prova-âncora: …
Destino do CTA: …
Categoria sensível: sim/não — qual — consequência de público
Risco de política dominante: …

MAPA DO PACOTE
| Peça | Estrutura | Duração | Proporção | Superfície | Gancho |

AUDITORIA DE APROVAÇÃO
| Peça | Item | Política | Status (OK / CORRIGIDO / ⛔ BLOQUEIO) | O que mudou |

AUDITORIA DA LANDING PAGE
| Item | Status | Correção necessária |

BRIEFING DE SUBIDA
Campanha: Demand Gen, meta …, só YouTube, grupos por superfície
Público: …
Orçamento mínimo: 10× CPA alvo = R$ …/dia
Lance: Maximize Conversions até ~50 conversões
Teste: 1 anúncio por gancho; decidir por CPA de clique + caixa
Rastreamento: tag Google Ads + enhanced conversions; template de URL …

LACUNAS
[LACUNA: …]
```

### B2. Um arquivo por peça: `NN - [Estrutura] - [Nome].docx`

```
[NOME DA PEÇA]
Estrutura: E1 Mini-VSL · Duração-alvo: 90s (~230 palavras) · 16:9 · In-stream

GANCHO A — [nome do ângulo]
"…"

GANCHO B — …
"…"

(3 a 5 ganchos, cada um de 0-5s, trocáveis sobre o mesmo corpo)

CORPO
[00:05] "…"
[00:15] "…"

[TELA: texto preto em fundo branco — "…"]
[B-ROLL: contrato na tela, dedo apontando a linha]

CTA
"…"
[TELA: "…" + logo]

FICHA DO ANÚNCIO (Demand Gen)
Títulos (≤40): 1) … 2) … 3) … 4) … 5) …
Título longo (≤90): …
Descrições (≤90): 1) … 2) …
CTA do botão: …
Nome da empresa (≤25): …
```

Formatação: sem negrito/itálico/bullets dentro da copy falada; fala entre aspas em parágrafos
curtos (cada quebra = respiração); marcações de cena entre colchetes; números ditos por extenso
quando abrem frase ("noventa e cinco por cento"). Contar caracteres dos títulos/descrições com
código, não de olho.

Ritmo de fala para estimar duração: ~150 palavras/min (tom institucional) a ~180 (conversa).
