# YouTube Ads DR — Estrutura de campanha e segmentação (estado set/2026)

Pesquisa para skill de criativos YouTube Ads (direct response, BR). Data de corte: 17/09/2026.
Legenda: **[oficial]** = Google Ads Help / blog Google / Ads API · **[consenso]** = 3+ fontes independentes de praticante apontando igual · **[isolado]** = 1 fonte / 1 conta / contestável.

> Limitação de coleta: WebSearch/WebFetch recusam reddit.com e old.reddit.com. Os threads foram lidos pelo feed RSS público (`/r/PPC/comments/<id>/.rss`), sob rate limit forte — r/PPC ficou bem coberto; r/affiliatemarketing, r/Entrepreneur, r/ecommerce, r/agency ficaram praticamente sem cobertura. searchengineland.com respondeu 403 (usado só via snippets/replicações). Dado específico do Brasil é escasso e de baixa qualidade (ver §6).

---

## 0. TL;DR para a skill (o que muda no criativo por causa da campanha)

1. **Video Action Campaign (VAC) não existe mais.** Conversão/lead em vídeo no YouTube = **Demand Gen** (ou PMax com vídeo). Todo criativo DR tem que caber nas 3 superfícies de YouTube do Demand Gen: **in-stream pulável, in-feed, Shorts** — cada uma com gatilho de "engaged view" diferente (10s in-stream × 5s in-feed/Shorts). [oficial]
2. **Subir as 3 proporções (16:9, 1:1, 9:16)** do mesmo anúncio; vídeo <10s não roda in-stream. [oficial] + [consenso]
3. **Nichos de saúde (nutra, emagrecimento, cabelo, sexual, vício), religião, finanças pessoais negativas, relacionamento sexual = categoria sensível**: sem lista de clientes, remarketing, lookalike e (dependendo da fonte) custom segment. Demand Gen usa público curado por padrão e **pode simplesmente não entregar**. O criativo + LP também disparam a classificação. [oficial] — crítico para os projetos do Felipe.
4. **Painel mente nos dois sentidos**: engaged-view conversions (EVC) inflam; last-click/GA4 subestima. Ler caixa, busca de marca e vendas totais. [consenso]
5. **Orçamento**: oficial ≥10× o tCPA/dia; praticantes 15–20× ou US$100/dia; piso técnico da API US$5/dia. Nada de Smart Bidding com <15–30 conversões/mês. [oficial]+[consenso]

---

## 1. Tipos de campanha para vídeo hoje

### 1.1 Cronologia VAC → Demand Gen [oficial]
- "**April 2025**: Google removes the option to create new Video Action Campaigns" · "**July 2025**: Google will start to automatically upgrade existing Video Action Campaigns to Demand Gen" · dez/2025 bloqueia data final além de 31/01/2026 · "**April 2026**: Final automatic upgrades completed". — https://support.google.com/google-ads/answer/15110871?hl=en
- Ferramenta de upgrade manual disponível desde mar/2025 (Inceptly recomendava usar para preservar configurações). — https://inceptly.com/google-expands-demand-gen-more-control-better-performance-new-features/ [isolado, consistente com oficial]
- O que muda no upgrade [oficial, mesma URL]: inventário passa a incluir Discover, Gmail, GDN; ganha formatos "In-feed image" e "Shorts image"; ganha Maximize clicks; **perde bid modifiers**; **perde "seasonal events" e "new customer acquisition"** (no contexto do upgrade); ganha lookalike; cobrança vira "mixed billing" (CPM/CPC/engaged view conforme superfície); ganha relatório segmentado por formato (Skippable In-Stream / In-Feed / Shorts).

### 1.2 Mapa atual de campanhas com vídeo

| Campanha | Formatos YouTube | Lance | Uso DR |
|---|---|---|---|
| **Demand Gen** (meta Vendas/Leads) | in-stream pulável, in-feed, Shorts (+ imagem/carrossel; Discover/Gmail/GDN opcionais) | Max conv., tCPA, tROAS, Max conv. value, Max clicks, tCPC | **Padrão para conversão/lead** [oficial] |
| **Performance Max** | YouTube entre todos os canais (Search, Shopping, Display, Discover, Gmail, Maps) | Max conv./valor, tCPA/tROAS | Conversão, mas **sem controle de YouTube**; gera vídeo automático se você não subir [oficial] |
| **Video views** (Video campaign) | skippable in-stream, in-feed, Shorts | tCPV | Visualização barata / construir público de remarketing [oficial] |
| **Video reach** – Efficient reach | bumper, skippable, in-feed, Shorts | tCPM | Alcance |
| **Video reach** – Non-skippable | bumper + **não pulável 15s** | tCPM | Alcance/frequência (não DR) |
| Target frequency / Ad sequence | bumper, skippable, não pulável | tCPM (maxCPV saiu do sequencing em jul/2025) | Marca/sequência |

Fontes: https://support.google.com/google-ads/answer/2375497?hl=en · https://support.google.com/google-ads/answer/13695777?hl=en · https://inceptly.com/9-google-and-youtube-ads-updates-june-2025/ (VAS só tCPM desde jul/2025; "Multi-format opt-out removed" em Video views) [oficial/isolado]

- **Não pulável e bumper NÃO rodam em Demand Gen** — só em campanhas de alcance com tCPM. Não servem para otimizar conversão. [oficial, por exclusão das listas de formatos]
- **PMax**: se não subir vídeo, "one or more videos may be auto-generated" — https://support.google.com/google-ads/answer/14528532?hl=en [oficial]. Vídeo automático "underperform custom video by 25 to 40%" [isolado, sem fonte primária — groas.com]. Limite subiu para 15 vídeos por asset group no início de 2026 [isolado].
- Novo: meta "**YouTube Engagements**" dentro de Demand Gen (abr/2025) e otimização "follow-on views" (jun/2025) — são para crescer canal, não DR. — https://inceptly.com/youtube-engagements-now-available-as-a-demand-gen-goal/ [oficial via praticante]
- Teste (ago/2026): anúncio Demand Gen no YouTube que abre **conversa em app de mensagens** — relevante para funil de WhatsApp no BR quando chegar. — https://blog.google/products/ads-commerce/demand-gen-drop-august-2026/ [oficial, em teste]

### 1.3 Qual usar para DR e por quê
- **Demand Gen com meta Conversões, só YouTube** é a recriação do VAC. Inceptly: escolher "Conversions" — "Don't water it down" com cliques/engajamento; colocar in-stream para VSL longa, in-feed para UGC/demos, Shorts para vertical <60s; e **desmarcar** as versões vertical/quadrada/encurtada geradas pelo Google — "it's often better to leave these boxes unchecked" se o criativo já estiver pronto. — https://inceptly.com/how-to-recreate-vac-in-demand-gen/ [isolado, agência especialista]
- **Controle de canal** existe desde mar/2025 no nível do grupo de anúncios: todos / só superfícies Google / manual (dá para YouTube-only e até Shorts-only). — https://support.google.com/google-ads/answer/15890515?hl=en [oficial]
- Reddit r/PPC (mar/2026, e-commerce 5 anos de YouTube, VSL in-stream 2–3 min, broad + idade 25+/45+, EUA): "Since the forced migration from VAC to Demand Gen… our **baseline ROI has dropped roughly 25%** across the board." Mesmo já isolando in-stream por controle de canal. Outro usuário: "Talking to the reps, it seems to hit **more warm traffic** than the old VAC." Recomendação no thread: separar Demand Gen de vídeo (perto do VAC) da de inventário discovery, e quebrar por superfície/formato. — https://www.reddit.com/r/PPC/comments/1rljdfz/demandgen_killed_our_youtube_roi_anyone_else/ [consenso fraco: 3 relatos concordando no thread]
- Reddit abr/2025, "The Youtube to Demand Gen Video switch … Is absolutely disastrous": 5 anos de venda direta (vídeo → funil → checkout), in-stream only, testou max conv/tCPA/tROAS/desktop/mobile — "almost impossible to make sales", gasto diário "erratic". Outro: página de opt-in "can't get… above 9%… They previously converted at 40%" (sinal de tráfego de pior qualidade, não de criativo). — https://www.reddit.com/r/PPC/comments/1k6qr5u/the_youtube_to_demand_gen_video_switch/ [consenso: 3 relatos]
- Reddit jan/2025: "I've A/B tested demand gen campaigns already against youtube conversion campaigns and every time the YouTube conversion campaign performs better"; "Demand Gen performed markedly worse with just video assets, twice"; checklist de setup citado: "turn off display network, automated CTAs, video enhancements". Contraponto TTFV: "I don't see any reason why you can't make it perform similarly". — https://www.reddit.com/r/PPC/comments/1iebin7/how_do_you_guys_feel_about_being_forced_to_turn/ [consenso de praticantes, pré-controle de canal]
- Reddit mai/2025: £800k/ano em Search testou DG (YouTube sem Shorts, Discover, Gmail) 4 semanas — "Not 1 conversion". Outro: DG "won't convert cold traffic quickly… mainly as a warm up tool". — https://www.reddit.com/r/PPC/comments/1klqfrf/demand_gen_vs_youtube/ [isolado]
- Reddit out/2025: "YouTube still converts but only with precise intent signals… remarketing and custom intent segments from search data, skip broad affinity"; outro diz que vídeo dentro de PMax rende mais que Demand Gen standalone (contradiz TTFV). — https://www.reddit.com/r/PPC/comments/1oi0kg5/do_youtube_ads_still_convert/ [conflito]
- Solutions 8 (John Moran, CMO), ~20 dias e US$30k em Demand Gen: resultados "looked good initially, but then kind of fell apart as soon as you start to dig a little deeper"; "Demand Gen is targeting warmer traffic, and simply inserting itself into the conversion path"; "is it generating demand, or is it attributing more existing demand to itself?" — https://www.lunio.ai/blog/google-demand-gen-campaigns [isolado, mas agência de US$70M/ano]
- Contraponto oficial: Google diz que só com vídeo "similar conversions and CPAs" aos VAC (via Inceptly https://inceptly.com/google-ads-update-demand-gen-will-replace-video-action-campaigns/); vídeo+imagem = "20% more conversions" (help do upgrade) / "6% more conversions per dollar" (Creative Excellence Guide) — **números oficiais divergentes entre si**. Nielsen "58% higher ROAS than VAC" é citado por terceiros sem link primário. [oficial, autointeressado]
- Aaron Young (Define Digital): "Demand Gen is not a 'starter' campaign — it is a supporting campaign"; primeiro Search/Shopping validado. — https://www.definedigitalacademy.com/blog/the-biggest-mistakes-i-see-with-demand-gen-campaigns [isolado; é visão de conta de busca, não de DR de oferta fria]
- Reddit jun/2026: conta com 86% do gasto cross-network em YouTube (Demand Gen + PMax), €31,5k → €71,6k receita (ROAS 2,27 em receita) só topo de funil; resposta de TTFV (mod veterano): YouTube via PMax é má ideia — "it should be under YouTube/Demand Gen only so you can control ad spend". — https://www.reddit.com/r/PPC/comments/1u9hrze/is_youtube_the_most_underrated_cold_traffic/ [consenso: não misturar YouTube DR dentro de PMax]

---

## 2. Segmentação

### 2.1 Custom segments [oficial]
- Duas leituras de palavra-chave: "People with any of these interests or purchase intentions" (padrão) ou "**People who searched for any of these terms on Google**". A leitura por busca só vale "on campaigns running on Google properties. On other campaigns, they will be used as interests". URLs/apps **não** são posicionamento: "This doesn't mean your ads will show on those URLs" — é gente que navega em sites parecidos. — https://support.google.com/google-ads/answer/9805516?hl=en
- Em Demand Gen o recurso se chama "Custom segment"; em Video era dividido em custom intent / custom search terms. Com optimized targeting desligado e segmento por termos de busca, serve só em inventário Google (YouTube, Discover, Gmail). — https://learn.jyll.ca/blog/where-can-you-use-custom-segments-in-google-ads [isolado, Jyll Saskin Gales, ex-Google]
- **Combined segments deixaram de funcionar em campanhas de vídeo em 2025**, sem anúncio. — https://learn.jyll.ca/blog/can-you-apply-a-combined-segment-to-youtube-ads [isolado]
- Tom Breeze (Viewability): o trunfo de DR no YouTube é a intenção — segmentar quem digitou a busca no Google e alcançá-lo no YouTube. — https://viewability.co/ · https://www.socialmediaexaminer.com/how-to-create-youtube-video-ads-that-convert-tom-breeze/ [consenso histórico entre agências DR]
- Reddit set/2025→jun/2026 (agência testando infoproduto para founders): um conselho "Skip URL placements… start with custom intent audiences built from your keyword lists"; réplica de quem roda lead gen no YouTube: URLs de concorrente "are absolutely fine… Those URLs act more like signals… Google's machine learning goes out and finds similar patterns" — olhar o tamanho estimado do público. — https://www.reddit.com/r/PPC/comments/1niq16j/advice_on_youtube_ads_targeting/ [conflito; ambos aceitam termos de busca]
- Reddit mar/2026: pergunta aberta "Anyone testing custom segments with search-term keywords specifically, and seeing results?" sem resposta conclusiva → não há prova recente de que ainda superem broad em Demand Gen. [isolado]

### 2.2 Lookalike (só Demand Gen) [oficial + mudança de 2026]
- Tiers: Narrow 2,5% / Balanced 5% / Broad 10% da população do local; semente mínima **100 pessoas correspondidas** (um documento Google recomenda 1.000); atualiza a cada 1–2 dias. — https://support.google.com/google-ads/answer/13541369?hl=en
- **Mar/2026: lookalike virou SINAL, não trava.** Anunciado 17/02/2026: o sistema "may go beyond those parameters if its models predict better conversion"; existe formulário de opt-out. Reação (Adriaan Dekker): "another step toward AI-led targeting similar to Meta's". — https://ppc.land/google-quietly-strips-lookalikes-hard-targeting-control-in-demand-gen/ [oficial via imprensa]
- Ironia: em 01/09/2026 campanhas **Video (brand)** ganharam lookalike com tier **rígido**; lookalike criado lá aparece "Eligible - Limited" fora. — https://ppc.land/google-video-campaigns-gain-the-lookalike-reach-controls-demand-gen-lost/
- Dica isolada (Thomas Eccel): semear lookalike com leads de campanha de lead do Meta — "the purest lookalike audiences ever". — https://www.lunio.ai/blog/google-demand-gen-campaigns [isolado]

### 2.3 Optimized targeting
- Google: ligar no grupo de anúncios para escapar de segmentação estreita que trava o lance. — https://support.google.com/google-ads/answer/14713361?hl=en-GB [oficial]
- Aaron Young: desligar em remarketing/listas segmentadas — "Optimised targeting can absolutely ruin your segmentation if used incorrectly"; ligar só em frio amplo. — https://www.definedigitalacademy.com/blog/the-biggest-mistakes-i-see-with-demand-gen-campaigns [consenso entre praticantes: OFF para ler o público, ON para escalar]
- Para teste limpo de semente/remarketing, desligar durante a janela do teste. — https://www.1clickreport.com/blog/google-demand-gen-lookalike-changes-2026 [isolado]

### 2.4 Remarketing, listas, aquisição de cliente novo
- Demand Gen aceita Customer Match, visitantes, usuários de app, espectadores/inscritos do canal YouTube vinculado; "new customer acquisition" permite "targeting exclusively new users or bidding higher for new users". — https://support.google.com/google-ads/answer/15594567?hl=en [oficial]
- Reddit jan/2026 (hipoteca, US$50/dia): dois conselhos recorrentes para lead financeiro — usar YouTube para construir público e converter via remarketing; e "if you don't spend enough to get 30 conversions per month it'll never work". — https://www.reddit.com/r/PPC/comments/1q9ncf8/why_do_youtube_ads_click_but_not_convert/ [consenso]

### 2.5 ⚠️ Categorias sensíveis (saúde, religião, sexual, finanças) — [oficial, crítico para nutra/fé/NoFap]
- Anunciante de categoria sensível **não pode usar público curado pelo anunciante**: "Customer match · Your data segments · Audience expansion · Lookalike segments". Podem: segmentos predefinidos Google (in-market, afinidade, demografia, eventos de vida), local. — https://support.google.com/adspolicy/answer/143465?hl=en
- Saúde inclui "Physical or mental health conditions, including… sexual health", "Products, services, or procedures to treat or manage chronic health conditions", "health issues associated with intimate body parts or functions", "Counseling… depression, anxiety, and addiction". Emagrecimento/suplemento/queda de cabelo não são nomeados, mas caem em "tratamento de condição". Religião ("Religious beliefs") também é sensível. — https://support.google.com/adspolicy/answer/16701855?hl=en
- "Discovery and Demand Gen campaigns use advertiser-curated audiences by default and **may be restricted from serving**" (esclarecimento de 03/06/2026). — https://ppc.land/google-tightens-demand-gen-and-discovery-ad-serving-for-sensitive-categories/
- **Conflito de fontes sobre custom segments**: a página de saúde lista "Custom segments" entre os permitidos, e em 12/12/2025 o Google ampliou o acesso a custom segments para setores regulados (https://digitalhipsterinc.com/googles-december-2025-personalized-ads-update-what-it-means-for-your-targeting-strategy/); já o troubleshooting oficial ainda diz "avoid custom segments and lookalike audiences for sensitive categories" (https://support.google.com/google-ads/answer/14713361?hl=en-GB). **Testar na conta** e checar status do grupo.
- Implicação para criativo: a classificação lê anúncio + LP. Criativo que fala da condição em 2ª pessoa ("você que tem X") tende a disparar a política — mesma lógica do Meta com atributos pessoais.
- Relatos de "Demand Gen não gasta / 0 impressões" são frequentes no r/PPC em 2026 (https://www.reddit.com/r/PPC/comments/1u7stkr/demand_gen_youtube_campaigns_wont_spend_0_0/, https://www.reddit.com/r/PPC/comments/1t1fx8m/demand_gen_youtube_ads_campaign_refusing_to_spend/, https://www.reddit.com/r/PPC/comments/1s8vvq0/demand_gen_not_spending_at_all_after_5_days/, https://www.reddit.com/r/PPC/comments/1tcezmk/youtube_ads_refuse_to_spend_for_2_weeks/) — causas oficiais: asset reprovado/baixa qualidade ("Demand Gen maintains a stricter creative quality threshold"), público sensível, tCPA "far below the historical average", segmentação estreita, até 24h de processamento. — https://support.google.com/google-ads/answer/14713361?hl=en-GB [oficial] · [consenso sobre o sintoma]

### 2.6 Exclusões (crianças, jogos, apps)
- Nível de conta, **Content suitability**: tema excluído "Content suitable for families" (inclui Made for Kids), jogos (luta/maduros), saúde sensível, notícias, política, religião; até **65.000** posicionamentos excluídos; até **1.000** palavras-chave de conteúdo; inventory type Expanded/Standard/Limited. Aplica a YouTube, GDN, GVP. **"Performance Max and Demand Gen campaigns have limited coverage" (ex.: Shorts e in-feed).** — https://support.google.com/google-ads/answer/12764663?hl=en [oficial]
- Excluir todos os apps: `mobileappcategory::69500` ("App categories > All Apps") ainda funciona, mas não pega tudo (webviews) e em PMax/Demand Gen é parcialmente sobreposto pela automação. — https://www.takesomerisk.com/google-ads-shows-ads-in-mobile-apps/ · https://support.google.com/google-ads/thread/227233180/mobileappcategory-69500?hl=en [consenso]
- Relatório "Where ads showed" existe para Demand Gen (Insights and reports → When and where ads showed); script retorna YouTube como `youtube.com`, então exclusão de canal/vídeo é pela interface. — https://searchengineland.com/google-ads-placements-guide-websites-apps-youtube-462050 [consenso]
- Reddit jun/2025 (UK, B2B, só imagem no feed YouTube, sem optimized targeting): "A large majority of the channels… are Islamic / African / foreign language channels". Respostas: script que exclui canal com caracteres não latinos; placement report diário + blocklist; "inclusion lists… not available to all for demand gen yet". Jan/2025: "we can't exclude gaming sites completely… the most bot traffic ever" e o "other" nos posicionamentos onde "half of the budget goes". — https://www.reddit.com/r/PPC/comments/1l2yll7/demand_gen_placements_showing_on_foreign_channels/ · https://www.reddit.com/r/PPC/comments/1iebin7/ [consenso]
- Reddit: "Demand Gen placements – showing on foreign channels" (jun/2025) e "Demand Gen Sh*t placements" (fev/2024) — queixa recorrente de inventário lixo/idioma errado. — https://www.reddit.com/r/PPC/comments/1l2yll7/demand_gen_placements_showing_on_foreign_channels/ · https://www.reddit.com/r/PPC/comments/1apugfd/demand_gen_sht_placements/ [consenso sobre o problema]
- Não excluir segmento com <1.000 impressões (sem significância). — https://www.negator.io/post/demand-gen-campaign-negative-signal-strategies-2025-playbook [isolado]

### 2.7 Idade/gênero
- Suportado em Demand Gen (idade, gênero, renda familiar, parentalidade). [oficial, 15594567]
- Prática relatada por anunciante DR veterano: broad + corte de idade (25+ ou 45+) como única restrição. — thread 1rljdfz [isolado]
- CPV por idade quase plano (US$0,024–0,029) — idade não é alavanca de custo, é de qualidade. — https://www.storegrowers.com/youtube-ads-benchmarks/ (dado Strike Social, 2018 — velho) [isolado]

---

## 3. Lances, orçamento e aprendizado

### 3.1 Orçamento
| Fonte | Regra | Tipo |
|---|---|---|
| Google Help (About Demand Gen + Performance guide + troubleshooting) | "at least **10 times** your target CPA" por dia | [oficial] |
| Guias antigos / ALM / Search Engine Land | **15×** CPA esperado | [consenso antigo] |
| Aaron Young | "$100 per day, or **20×** your Target CPA" | [isolado] |
| Google Ads API (27/02/2026) | desde **01/04/2026**, **mínimo US$5/dia** (ou equivalente local) para toda Demand Gen; campanhas antigas abaixo continuam, mas não aceitam edição | [oficial] https://ads-developers.googleblog.com/2026/02/minimum-budget-requirement-for-demand.html |
| Praticantes genéricos | <US$30/dia tende a falhar; US$50–100/dia por campanha | [consenso fraco] |

- Campanha saudável gasta "~80% or less of their daily budget"; subir no máximo **15%** por vez. — https://support.google.com/google-ads/answer/16797388?hl=en [oficial]
- Reddit ago/2026 (produto US$300, VSL de 30 min até o 1º CTA, US$645 em 18 testes, 1 venda): "That budget is too small for YouTube"; o maior problema apontado não foi lance e sim **VSL com CTA só aos 30 minutos para tráfego frio**; e "every reset hurts learning" — parar de abrir campanha nova a cada teste. — https://www.reddit.com/r/PPC/comments/1ve1t81/spent_645_on_youtube_ads_for_1_sale_what_would/ [consenso no thread]

### 3.2 Estratégia de lance e volume de conversão
- Começar em **Maximize Conversions**; passar a tCPA/tROAS "after your campaign received at least **50 conversions**". — https://support.google.com/google-ads/answer/14509385?hl=en [oficial]
- tCPA em geral: exige ≥15 conversões/30 dias para ativar; recomendado 30/30 dias. — https://support.google.com/google-ads/answer/6268632?hl=en [oficial]
- Após mudança, esperar "at least 30-50 conversions to evaluate"; ajuste de lance "5-10% (no more than 15%) per week", "+/-15% across the campaign duration"; consolidar grupos com dias seguidos de 0 conversões. — 16797388 [oficial]
- tCPA muito abaixo do histórico trava entrega; subir tCPA 20–30% se não gasta. — 14713361 [oficial]
- Reddit: com 1 conversão, "target cpa… is basically asking google to steer a strategy off a single data point"; limiar prático citado 15–30 conv./mês. Um relato antigo "you needed 100+ conversions" (VAC) — não confirmado para Demand Gen. [consenso 15–30]

### 3.3 Aprendizado e tempo
- Oficial não fixa dias; não mexer "during the initial learning period"; mudanças nas últimas 72h reiniciam; "Allow 5–7 days" para estabilizar. — 16797388 / 14713361 [oficial]
- Relato real (hipoteca, Demand Gen Max conv., US$50/dia): nada nos primeiros 14 dias; em ~21 dias: 14 leads, 7 agendamentos, CPL ~US$100 e caindo — "YouTube does work for us — it just takes more time than Search." — thread 1q9ncf8 [isolado, mas típico]
- Aaron Young: rodar **3 meses** antes de decidir escala. [isolado]
- Semana 1–2: ROAS 1,5–2× antes de estabilizar em 2–5× (e-commerce). — https://www.storegrowers.com/demand-gen-benchmarks/ [isolado]

### 3.4 Janelas de conversão, EVC, VTC — e inflação
- **Engaged-view** [oficial]: in-stream pulável = assistiu **≥10s** (ou inteiro se <10s); **in-feed e Shorts = ≥5s** (Shorts também conta clique no CTA). Janela padrão para Demand Gen/PMax/Video Action = **1 dia**; web geral 3 dias; editável. EVC entra na coluna **Conversions** (não só All conv.) e em Interactions. Upload offline deve ocorrer em até 14 dias para atribuir EVC. — https://support.google.com/google-ads/answer/10048752?hl=en
- GA4: desde **11/08/2026** a janela de EVC deixou de ser fixa em 3 dias e aceita 1–30 dias; clique 1–90 dias. — https://ppc.land/google-analytics-drops-the-fixed-3-day-engaged-view-conversion-window/ [oficial via imprensa]
- **VTC optimization** (teste out/2025, lançado em Google Ads abr/2026): Demand Gen passa a otimizar para conversões pós-impressão sem clique no YouTube — "more conversions in less time". — https://blog.google/products/ads-commerce/demand-gen-drop-april-2026/ · https://ppcnewsfeed.com/ppc-news/2025-10/demand-gen-gets-smarter-with-view-through-conversion-optimization/ [oficial]. A própria documentação admite que isso "does not directly target incrementality" — https://ppc.land/view-through-conversion/ [oficial via imprensa]
- Inflação: Solutions 8 atribuiu o "aumento" de leads qualificados a EVC: "counting it as its own, spiking spend, getting 1,000 more conversions — but our brand is actually suffering". — https://www.lunio.ai/blog/google-demand-gen-campaigns [isolado, forte]
- Prática derivada [consenso de praticantes]: segmentar a coluna Conversões por **Ad event type** (clique × engaged view × view) e decidir criativo/campanha pela conversão de **clique + caixa real**; manter janela de EVC curta (1 dia) quando o objetivo é venda direta.

---

## 4. Quantidade de criativos, teste, fadiga, proporção

### 4.1 Quantos por grupo
- Anúncio de vídeo Demand Gen: **1–5 vídeos por anúncio**, até 5 títulos (40c), título longo (90c), até 5 descrições (90c), CTA, nome da empresa (25c), logo. Mín. 5s; **<10s não serve in-stream**; recomendado >15s. — https://support.google.com/google-ads/answer/17141078?hl=en [oficial]
- "Rule of three": pelo menos **3 imagens ou vídeos em cada proporção** (vertical, quadrada, horizontal) por grupo. — https://business.google.com/us/accelerate/resources/articles/creative-excellence-guide-for-demand-gen-campaigns/ [oficial]
- Inceptly: ≥5 vídeos por grupo. — https://inceptly.com/unlocking-the-potential-of-demand-gen-campaigns/ [isolado]
- "Ad Strength Excellent" é uma das 4 boas práticas; "at least 3 of the 4… saw on average over 40% more conversions". — https://blog.google/products/ads-commerce/demand-gen-drop-february-2026/ [oficial, autointeressado]
- Dá para atribuir vídeos diferentes a superfícies diferentes dentro do mesmo grupo ("Choose where your videos show"). — https://inceptly.com/how-to-recreate-vac-in-demand-gen/ [isolado]

### 4.2 Teste A/B [oficial]
- Experimentos Demand Gen: testam "creatives, audience, product feed and bidding"; exigem **2 campanhas Demand Gen prontas e não rodando**, "differ in only one variable"; teste de orçamento não recomendado; com lance por conversão, "**minimum of 50 conversions per arm**"; confiança 70% (padrão, direcional) / 80% / 95%. — https://support.google.com/google-ads/answer/13719071?hl=en-GB
- Conversion Lift (incrementalidade): mínimo caiu para **US$5.000** (anúncio 11/11/2025) para Video, Discovery e Demand Gen, com modelo bayesiano; resultado direcional com >US$5k e ~1.000 conversões. — https://ppc.land/google-lowers-incrementality-testing-threshold-to-5-000-for-advertisers/ [oficial via imprensa]
- Prática fora do experimento: 7 dias e ≥10.000 impressões por variante, uma variável por vez [isolado, groas.com]; Inceptly: "two weeks or until you reach a statistically significant sample size" [isolado].

### 4.3 Quando matar
- Não há regra oficial de pausa por criativo. Regras de praticante (majoritariamente importadas do Meta): 3× CPA-alvo gasto sem conversão = problema estrutural; pausar se CPA >1,5× alvo em 7 dias com gasto mínimo. — https://adspyder.io/blog/ad-fatigue-benchmarks/ e agregadores [isolado/consenso fraco]
- Reddit abr/2025 (Demand Gen com resultado): 3–5 anúncios por grupo, um interesse por grupo ou vários num grupo, "I kill the adsets that don't perform after they spend **2x my target CPA**" — e reclama que vira "a nightmare to manage" (estrutura de Meta transplantada). — https://www.reddit.com/r/PPC/comments/1jsa3lr/been_getting_decent_results_from_youtube_demand/ [isolado]
- Em Demand Gen, pausar criativo dentro de um grupo com Smart Bidding também mexe no aprendizado — por isso Google recomenda mudanças ≤15%/semana. [oficial, inferência]
- Sinal antecedente específico de YouTube: **view rate / retenção dos primeiros 5s** cai antes do CPA. — https://www.dataslayer.ai/blog/how-to-track-youtube-ads-performance-in-2026-metrics-benchmarks-reporting-guide [consenso]
- Reddit: CTR e view rate bons não garantem venda ("CTR is irrelevant…"); criativo "too professional" tende a perder para o menos polido. — thread 1q9ncf8 [consenso]

### 4.4 Fadiga
- "ad fatigue hits after 7-10 days" (dataslayer) [isolado]; duração mediana observada de criativo no YouTube 5,1 dias (amostra AdSpyder mai/2026 — mede rotação, não fadiga) [isolado]; DR: 3–5 exposições/semana [isolado]; padrão de CPA +5–8%/semana e depois salto de 15–25% [isolado].
- Demand Gen **não tem limite de frequência manual**: "The system automatically controls impression frequency". — https://support.google.com/google-ads/answer/14509385?hl=en [oficial]

### 4.5 Horizontal × vertical × quadrado
- **Subir as 3.** Inceptly (ago/2023): "Campaigns that incorporate all three aspect ratios of the same ad achieve 10-20% more conversions." — https://inceptly.com/ar-conversions/ [isolado, velho mas coerente com o oficial]
- Oficial: 16:9 (1920×1080), 1:1 (1080×1080), 4:5 (1080×1350), 9:16 (1080×1920); áudio: Shorts som ligado por padrão; in-stream som após toque; Discover/Home/Gmail mudo por padrão → **legenda queimada obrigatória** para in-feed. — 17141078 [oficial]
- Multimodal Video Creation (Asset Studio, GA ago/2026) gera horizontal e vertical num fluxo só. — demand-gen-drop-august-2026 [oficial]
- Imagem 9:16 também roda em Shorts em tela cheia. — https://inceptly.com/you-can-now-use-916-vertical-image-ads-in-demand-gen-even-on-youtube-shorts/ [oficial via praticante]
- Relatos reddit de imagem estática no feed do YouTube gerando cliques suspeitos ("Are they just bots?") — https://www.reddit.com/r/PPC/comments/1jwtolg/static_image_ads_on_youtube_feed_are_they_just/ [isolado]

---

## 5. Rastreamento e atribuição

### 5.1 Tag e sinais
- **Use a tag de conversão do Google Ads como primária** em YouTube; GA4 importado não traz EVC nem cross-device — "you will not benefit from cross-device capability… loss of conversions". GA4 como secundária para comparar. — https://adswerve.com/blog/google-ads-ga4-conversions-best-practices-recommendations [consenso]
- Boas práticas oficiais de medição 2026: "sitewide tagging with **Google tag gateway**" e ligar fontes offline ao **Data Manager**. — https://blog.google/products/ads-commerce/demand-gen-drop-february-2026/ [oficial]
- **Enhanced conversions for leads** substitui a importação offline por GCLID puro (hash de e-mail/telefone). — https://support.google.com/google-ads/answer/14274408?hl=en [oficial]
- iOS: gclid pode sumir; **wbraid** (clique em app iOS → conversão web — caso típico do app do YouTube) e gbraid. iOS 26 (set/2025) estendeu Link Tracking Protection a todo Safari, removendo gclid/fbclid; wbraid/gbraid permanecem. Importação simultânea gclid+gbraid desde out/2025; Data Manager API virou padrão no início de 2026. — https://www.wickedreports.com/blog/gclids-gbraids-wbraids-what-is-going-on · https://www.customerlabs.com/blog/google-ads-wbraid-gbraid-offline-conversion-tracking/ [consenso técnico; datas de iOS 26 e Data Manager isoladas]
- Reddit: "ideally add server side tracking" como condição para YouTube funcionar em lead. — thread 1q9ncf8 [isolado]
- Consequência prática para checkouts BR (Cakto/Payt/Lastlink/Hotmart): o gateway precisa receber e devolver `gclid`/`wbraid`/`gbraid` (ou o e-mail para enhanced conversions) para a venda voltar ao Google — mesmo problema já documentado no vault de "UTM morre no link fixo".

### 5.2 UTMs / ValueTrack
- ValueTrack é compatível com "Search, Display, AI Max, Shopping, **Video** and App campaigns"; o help não lista Demand Gen parâmetro a parâmetro. — https://support.google.com/google-ads/answer/2375447?hl=en [oficial]
- Template seguro para Demand Gen (sem depender de {keyword}/{placement}/{targetid}): `?utm_source=youtube&utm_medium=cpc&utm_campaign={campaignid}&utm_content={creative}&utm_term={adgroupid}&dev={device}&net={network}` — `{creative}` = ID do anúncio. — https://metricfixer.com/publications/online-advertising/google-ads-valuetrack-parameters-tracking-templates-utm-guide [isolado; testar com o "Test" do template]
- Limitação: `{creative}` identifica o **anúncio**, não qual dos 1–5 vídeos/proporções serviu; para saber o vídeo vencedor, usar o relatório de assets/"segment by format" no Google Ads, ou um anúncio por vídeo quando o teste for de criativo. [inferência]

### 5.3 Por que YouTube "não converte" no painel e converte no caixa (e o inverso)
- Last-click dá o crédito à busca de marca/direto: "YouTube creates demand that other campaigns capture". — https://medium.com/hellotegra/your-youtube-ads-campaigns-arent-failing-your-attribution-is-full-tracking-framework-61cc706b7f4b [consenso]
- Aaron Young: "Demand Gen results often do not show up accurately inside the Google Ads interface" — uma conta viu **+4 vendas/dia** reais com **2 conversões** reportadas. — https://www.definedigitalacademy.com/blog/the-biggest-mistakes-i-see-with-demand-gen-campaigns [isolado]
- Reddit jun/2026: YouTube como maior first-touch; usuários voltam por Search/Direct/Remarketing. — thread 1u9hrze [isolado]
- **Attributed Branded Searches** (Demand Gen Drop jan/2026): conversão sempre-ativa que conta buscas de marca no Google/YouTube até **7 dias** após impressão; precisa de brand mapping (via representante). — https://support.google.com/google-ads/answer/16212033?hl=en · https://blog.google/products/ads-commerce/demand-gen-drop-january-2026/ [oficial]
- Mas o inverso também vale: EVC e VTC colocam o YouTube no caminho de quem já ia comprar (ver §3.4, Solutions 8). **Régua única: vendas totais/caixa por dia × gasto de YouTube, com holdout ou Conversion Lift.** [consenso]

---

## 6. Benchmarks (use como ordem de grandeza, não meta)

| Métrica | Valor | Nicho/país/data | Fonte | Tipo |
|---|---|---|---|---|
| CPM YouTube | US$5–10 (Adzoola US$9,29; PME US$8,15) | global, 2024–25 | storegrowers.com/youtube-ads-benchmarks | [consenso] |
| CPM por formato | skippable 5–10 · bumper 3,24–4,37 · in-feed 3–8 · Shorts ~4 | global | idem | [isolado] |
| CPM sazonal | jan–fev ~US$2–2,5 · out–nov 5–7+ · dez pico 6,93 | global 2024–25 | idem (Strike Social/Lenos) | [isolado] |
| CPV | US$0,05 médio (0,01–0,19) — view = 30s | B2B SaaS EUA, US$1,04M, 2023–24 | https://www.adconversion.com/blog/youtube-ads-cost-benchmark | [isolado] |
| CPV | ~US$0,026 (Q1/2026 US$0,024) | global | digitalapplied / dataslayer | [isolado] |
| CPV Shorts | US$0,10–0,30 | global | storegrowers | [isolado] |
| CPM Brasil | R$20–35 | BR | https://www.shopify.com/br/blog/cpm-do-youtube (fonte fraca) | [isolado] |
| CPV Brasil | R$0,10–0,25 B2C · R$0,20–0,40 apps · R$0,40–1,00 B2B | BR | https://ebrg.com.br/cost-per-view-cpv/ (fonte fraca, sem amostra) | [isolado] |
| View rate | 31,9% média; B2B SaaS 29,24% (3,5–51%) | global / EUA | Strike Social / AdConversion | [consenso] |
| CTR vídeo | 0,65% média; B2B 0,51% (0,09–1,64%) | global / EUA | Pixability/AdConversion | [consenso] |
| CTR por formato | skippable 0,5–2% · não pulável <0,3% · bumper <0,1% · in-feed 1–3% · Shorts 0,1–0,5% | global | storegrowers | [isolado] |
| CTR por indústria | varejo 0,84% · viagem 0,78% · finanças 0,52% · saúde 0,48% (CPV saúde US$0,071, CPM US$7,10) | global 2026 | dataslayer | [isolado] |
| CPC YouTube | US$3,56 médio (B2B) | EUA | AdConversion | [isolado] |
| Demand Gen CTR / CPC | 0,5–2% / US$0,30–1,50 (YouTube 0,50–2+, Discover 0,20–0,80) | e-commerce, fev/2026 | https://www.storegrowers.com/demand-gen-benchmarks/ | [isolado] |
| Demand Gen CVR / CPA / ROAS | 0,5–2% / US$15–60 / 2–5× (sem. 1–2: 1,5–2×) | e-commerce | idem | [isolado] |
| Demand Gen × Search (conta real) | Search CPC US$7,33, CVR 0,83% · DG CPC US$0,09, CVR 0,01% · CPA **US$880 × US$878** | B2B | https://tntgrowth.com/blog/google-demand-gen-campaign-benchmarks | [isolado — lição: clique barato não é CPA barato] |
| CPL real | ~US$100 (hipoteca, 21 dias, US$50/dia) | EUA 2026 | reddit 1q9ncf8 | [isolado] |
| Conclusão de vídeo (skippable) | 25%: 60–70% · 50%: 45–55% · 100%: 25–35% | global | storegrowers | [isolado] |
| Conversão lead "40–60%" | — | — | storegrowers | **descartar** (número sem definição, incoerente) |

Aviso: quase todos os "benchmarks" de blog de 2026 reciclam Strike Social 2018 e AdConversion 2023–24. **Não há benchmark sério de YouTube DR para o Brasil**; o mais confiável para a skill é medir a própria conta e usar o CPA-teto do funil.

---

## 7. Erros comuns de quem vem do Meta

1. **Orçamento de teste de Meta** (US$10–30/dia) em Demand Gen → nunca sai do aprendizado. Oficial ≥10× tCPA; Aaron Young: "Ten dollars a day won't even scratch the surface". [oficial]+[consenso]
2. **Abrir campanha nova a cada teste** (hábito de ABO) → cada reset zera aprendizado; Reddit: "every reset hurts learning"; oficial: consolidar grupos com conversão esparsa. [consenso]
3. **Achar que controla frequência e posicionamento como no Meta** → Demand Gen não tem cap de frequência manual e exclusões de conteúdo têm "limited coverage" em Shorts/in-feed. [oficial]
4. **Colocar YouTube DR dentro de PMax** → sem controle de gasto/público. [consenso]
5. **Levar o hook de feed do Meta para in-stream sem ajuste**: in-stream exige sobreviver aos 5s do botão pular e conta engaged view aos 10s; in-feed/Shorts contam aos 5s e in-feed começa **mudo**. Sagum (sobre pulável × não pulável): "adapting the same concept into both formats with only minor edits" é erro comum que "usually underperforms" — https://sagum.com/2026/08/02/youtube-ads-skippable-vs-non-skippable/ ; no pulável "The first five seconds are a complete micro-ad"; no não pulável "Lead with the payoff, not the setup" e "Assume sound is off" — https://sagum.com/2026/04/08/the-youtube-ad-format-strategy-that-actually-drives-results/ [consenso]
6. **Criativo polido demais**: "sometimes things that look less professional do a lot better on YouTube". — reddit 1q9ncf8 [consenso]
7. **Julgar pelo painel como no Meta**: no Google o painel mistura EVC/VTC (infla) e perde a venda que volta por busca de marca (desinfla). Olhar caixa + busca de marca + segmentação por ad event type. [consenso]
8. **Usar o lookalike como se fosse o do Meta 1%** — desde mar/2026 é sinal, não trava; e em nicho sensível nem existe. [oficial]
9. **Levar a lógica de público curado de nicho sensível** (lista, remarketing, lookalike) → no Google, saúde/religião/sexual não podem, e Demand Gen pode ficar com 0 impressão. [oficial]
10. **VSL longa com CTA tardio para tráfego frio**: thread com CTA só aos 30 min → 0 order-form em US$209 de Max conversions; recomendação unânime foi antecipar o CTA antes de mexer em lance. — reddit 1ve1t81 [consenso no thread]
11. **Passar a tCPA cedo demais** (com 1–10 conversões). Oficial: Max conv. até 50 conversões. [oficial]
12. **Otimizar por evento raso/leve** para "dar sinal": Inceptly — objetivo Conversões, "Don't water it down"; contraponto no reddit — para lead financeiro, alguns preferem evento mais raso ou remarketing. [conflito — decidir pelo volume disponível: <30 conv./mês do evento final → evento intermediário ou remarketing]

---

## Fontes principais (oficiais)
- Upgrade VAC → Demand Gen: https://support.google.com/google-ads/answer/15110871?hl=en
- About Demand Gen: https://support.google.com/google-ads/answer/13695777?hl=en
- Demand Gen FAQ: https://support.google.com/google-ads/answer/14509385?hl=en
- Performance guide: https://support.google.com/google-ads/answer/16797388?hl=en
- Troubleshooting: https://support.google.com/google-ads/answer/14713361?hl=en-GB
- Audiences: https://support.google.com/google-ads/answer/15594567?hl=en
- Lookalike: https://support.google.com/google-ads/answer/13541369?hl=en
- Custom segments: https://support.google.com/google-ads/answer/9805516?hl=en
- Video specs Demand Gen: https://support.google.com/google-ads/answer/17141078?hl=en
- A/B experiments: https://support.google.com/google-ads/answer/13719071?hl=en-GB
- Engaged-view conversions: https://support.google.com/google-ads/answer/10048752?hl=en
- Content suitability: https://support.google.com/google-ads/answer/12764663?hl=en
- Personalized ads / sensitive: https://support.google.com/adspolicy/answer/143465?hl=en · https://support.google.com/adspolicy/answer/16701855?hl=en
- Channel controls: https://support.google.com/google-ads/answer/15890515?hl=en
- Mínimo US$5 (API): https://ads-developers.googleblog.com/2026/02/minimum-budget-requirement-for-demand.html
- Demand Gen Drops: fev/2026 https://blog.google/products/ads-commerce/demand-gen-drop-february-2026/ · abr/2026 https://blog.google/products/ads-commerce/demand-gen-drop-april-2026/ · ago/2026 https://blog.google/products/ads-commerce/demand-gen-drop-august-2026/
- Creative Excellence Guide: https://business.google.com/us/accelerate/resources/articles/creative-excellence-guide-for-demand-gen-campaigns/
