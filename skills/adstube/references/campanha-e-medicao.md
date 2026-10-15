# Campanha, segmentação e medição — o contexto que muda o criativo

Destilado de `fonte-campanha-2026-09.md` (Google Ads Help oficial + r/PPC + Inceptly, Define
Digital, Solutions 8). Corte 17/09/2026. É o briefing de subida que acompanha o pacote; a skill
não opera a conta.

## 1. Qual campanha

- **Video Action Campaign acabou** (sem criação desde 04/2025; migração final 04/2026). Conversão
  com vídeo = **Demand Gen** meta Vendas/Leads.
- Demand Gen só-YouTube: controle de canal no grupo de anúncios (YouTube only; dá até Shorts only).
  Desligar Display/Discover/Gmail, CTAs automáticos e melhorias de vídeo automáticas.
- Separar grupos por superfície quando o criativo é diferente: in-stream (mini-VSL 16:9) ×
  Shorts (9:16). Relatório segmentado por formato existe.
- **Não pôr YouTube DR dentro de PMax** (sem controle de gasto/público) [consenso].
- Não pulável 15s e bumper só em campanha de alcance (tCPM) — não servem para conversão.
- Relatos de piora VAC→Demand Gen (ROI −25%, CPA +40-50%, "pega tráfego mais quente") ⇒ olhar
  caixa, não painel.

## 2. Segmentação

- **Custom segment por termos de busca** ("pessoas que pesquisaram estes termos no Google") é o
  trunfo DR do YouTube — alcança no YouTube quem buscou no Google. URLs de concorrente viram
  sinal (não posicionamento).
- Público amplo + corte de idade (25+ / 45+) é prática de anunciante DR veterano.
- Lookalike (só Demand Gen): desde 03/2026 é SINAL, não trava. Semente mínima 100.
- Optimized targeting: OFF para ler público/remarketing; ON para escalar.
- **Categoria sensível (saúde, religião, sexual, dificuldade financeira):** sem Customer Match,
  remarketing, lookalike, expansão. Demand Gen pode ficar com 0 impressão. Usar públicos
  predefinidos do Google (in-market, afinidade, eventos de vida, demografia) e testar custom
  segment (fontes oficiais conflitam). A classificação lê anúncio + página.
- Exclusões: conteúdo infantil (Made for Kids), jogos, `mobileappcategory::69500` (todos os
  apps), canais em idioma errado; auditar "Where ads showed" — já houve 60% do gasto em "Outros"
  com 0 clique. Cobertura de exclusão é limitada em Shorts/in-feed.

## 3. Orçamento, lance, aprendizado

| Regra | Fonte |
|---|---|
| Orçamento diário ≥ 10× o CPA alvo (praticantes: 15-20× ou US$100/dia) | Oficial + consenso |
| Mínimo técnico US$5/dia (desde 01/04/2026) | Oficial |
| Começar em Maximize Conversions; tCPA só após ~50 conversões (ativa com 15/30 dias) | Oficial |
| <15-30 conversões/mês no evento final ⇒ otimizar para evento intermediário (lead/checkout) | Consenso |
| Não mexer 5-7 dias; mudanças nas últimas 72h reiniciam; ajuste ≤15%/semana | Oficial |
| Caso real: 14 dias nada, 21 dias CPL caindo — "leva mais tempo que a Search" | Isolado típico |
| Não abrir campanha nova a cada teste ("every reset hurts learning") | Consenso |

Orçamento de teste de Meta (US$10-30/dia) em Demand Gen nunca sai do aprendizado.

## 4. Teste de criativo

- Estrutura de teste: **1 corpo + 3-5 ganchos** (troca só os primeiros 5-20s) — o gancho move
  a maior parte do resultado. Refresh de vencedor = trocar gancho/visual, manter esqueleto
  (Inceptly; Derick Carneiro no VTurb faz igual).
- 1-5 vídeos por anúncio Demand Gen; Google recomenda 3 por proporção; `{creative}` identifica o
  ANÚNCIO, não qual vídeo ⇒ para ler gancho vencedor, **um anúncio por gancho**.
- Experimento formal: 2 campanhas idênticas exceto 1 variável, 50 conversões por braço.
- Fadiga no YouTube é mais lenta que no Meta (4-10 semanas estimadas; vencedores rodam anos).
  Antes de culpar fadiga, auditar placements.
- Matar: sem regra oficial. Referência de campo: gasto ≥ 2-3× o CPA alvo sem conversão.

## 5. Medição — o painel mente para os dois lados

- **Decide:** CPA / custo por lead qualificado / caixa. **Diagnostica:** retenção aos 5s, 15s,
  30s (queda aos 5s = gancho; aos 15-25s = identificação/mecanismo); add-to-cart por clique.
- **View rate:** <20% no pulável sugere gancho fraco. Vídeo EM BRANCO já deu 40% (bot) — não
  premiar view rate.
- **CTR não compara entre contas** desde que o YouTube mistura inventário. Vários casos com CTR
  >2% e 0 venda.
- **EVC (engaged-view conversion):** 10s in-stream / 5s in-feed e Shorts, entra na coluna
  Conversões e INFLA. Segmentar por "tipo de evento do anúncio" e decidir por conversão de clique
  + caixa. Janela de EVC curta (1 dia) para venda direta.
- Last-click/GA4 SUBESTIMA (YouTube gera busca de marca). Régua única: vendas totais/dia × gasto,
  com holdout quando possível.
- Tag do Google Ads como conversão primária; enhanced conversions (e-mail com hash).
- **Checkout BR (Cakto/Payt/Lastlink/Hotmart):** o gclid/wbraid/gbraid precisa sobreviver até a
  venda — link fixo de checkout no HTML descarta (mesmo furo do "UTM morre no link fixo").
- Template de URL: `?utm_source=youtube&utm_medium=cpc&utm_campaign={campaignid}&utm_content={creative}&utm_term={adgroupid}&dev={device}`

## 6. Benchmarks (ordem de grandeza, nunca meta)

CPV global ~US$0,03-0,09 (30s) · CPM US$5-10 · view rate ~30% · CTR vídeo ~0,5-0,65%
(skippable 0,5-2%, Shorts 0,1-0,5%) · BR: CPV R$0,10-0,30 e CPM R$20-35 (fontes fracas).
**Não existe benchmark sério de YouTube DR no Brasil**: a régua é o CPA-teto do próprio funil.
