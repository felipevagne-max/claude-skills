# Por que a estratégia do Meta é reprovada no YouTube/Google Ads — pesquisa de políticas

Pesquisa feita em 17/09/2026. Fontes: Central de Políticas do Google Ads (páginas em inglês lidas direto do HTML; **a versão em inglês é a que vale** para a fiscalização), Reddit (r/PPC, r/googleads, r/Affiliatemarketing, r/PayPerClickMarketing, lidos via JSON do old.reddit) e blogs de especialistas (Search Engine Land/Roundtable, PPC.land, StubGroup).

Legenda: **[oficial]** = texto do Google · **[consenso reddit]** = vários relatos/comentários na mesma direção · **[isolado]** = 1 relato, blog de agência ou inferência minha · **[inferência]** = conclusão minha a partir do texto oficial, sem o Google dizer isso com essas palavras.

---

## 0. Resumo: por que o que passa no Meta cai aqui

1. **O YouTube tem uma camada a mais além das políticas gerais.** Os anúncios em vídeo seguem todas as políticas do Google Ads **e ainda** os "YouTube and Discover Feed ad requirements", com três proibições extras: *Exaggerated or inaccurate claims*, *Negative events and imagery* e *Improper content* (partes do corpo/condições de saúde, conteúdo picante, palavrão). Foram reescritos em 30/09/2025 e de novo em **11/08/2026**; o Google diz que a fiscalização não mudou. [oficial] https://support.google.com/adspolicy/answer/10249050 · [isolado] https://ppc.land/google-rewrites-youtube-and-discover-ad-rules-for-a-second-time-in-11-months/
2. **O Google julga a página e o domínio inteiros, não só o criativo.** "Quando uma campanha nova, com criativos totalmente diferentes, também é reprovada, o alerta está no destino, não na copy" (tradução). [consenso reddit] https://www.reddit.com/r/googleads/comments/1wfi3dh/ · Numa escala de agência: "No Google, o diferencial é a transparência da landing page; no Meta, o alerta pesa mais na copy." [isolado] https://www.reddit.com/r/PPC/comments/1qb02ez/
3. **Esconder é punido mais do que exagerar.** Circumventing systems, cloaking, *unacceptable business practices* e personificação de figura pública são violações **"egregious"**: a conta é suspensa na detecção, **sem aviso**, e "você não poderá anunciar no Google Ads de novo". Clickbait, alegações não confiáveis, preço desonesto e requisitos de destino levam **aviso com pelo menos 7 dias** de antecedência antes da suspensão. [oficial] https://support.google.com/adspolicy/answer/2375414
4. **Escala da fiscalização em 2025:** 8,3 bilhões de anúncios bloqueados ou removidos e **24,9 milhões de contas suspensas**. Por categoria: abuso da rede de anúncios 1,29 bi, personalização 755 mi, *misrepresentation* 421,5 mi. [isolado, relatado a partir do Ads Safety Report] https://ppc.land/googles-2025-ads-safety-report-gemini-blocked-8-3-billion-bad-ads/
5. **A análise é por IA.** "Uma combinação da IA do Google com avaliação humana". Recursos genéricos são recusados automaticamente. [oficial] https://support.google.com/adspolicy/answer/7187501 · Um consultor brasileiro ex-Google disse que "as contestações são analisadas por IA, então precisa usar palavras-chave". [isolado, BR, 10/2025] https://www.reddit.com/r/googleads/comments/1ojbrq3/

---

## 1. Mapa: padrão de criativo DR do Meta → política do Google → reescrita

> Os "depois" são sugestões minhas **[inferência]**, construídas a partir dos exemplos oficiais. O Google dá um modelo explícito: *"Cure baldness in a week"* → *"Hairstyles and tips for thinning hair"* (em vez de "Cure a calvície em uma semana", algo como "Cortes e dicas para cabelo ralo"). [oficial, 10249050]

| # | Padrão típico do Meta | Política violada (nome como aparece no painel) | Trecho oficial | Antes → Depois |
|---|---|---|---|---|
| 1 | Hook de segredo/escândalo: "O segredo que os médicos escondem", "A verdade que ninguém te conta" | Misrepresentation › **Clickbait ads** | "Ads that claim to reveal secrets, scandals or other sensationalist information" [oficial] https://support.google.com/adspolicy/answer/15936667 | "O segredo proibido pra secar a barriga" → "Como funciona o [mecanismo] — explicado pela Dra. X" |
| 2 | Curiosidade aberta: "Assista até o fim", "Você não vai acreditar", "Descubra o que aconteceu" | **Clickbait ads** | "'Click here to find out', 'You won't believe what happened' or phrases synonymous" [oficial, 15936667] | "Você não vai acreditar no que ela fez" → "O protocolo de 3 passos que a [nome] usa com as pacientes" (dizer o que é) |
| 3 | Antes e depois do corpo (emagrecimento, gordura localizada, cabelo, pele) | **Clickbait ads** + YouTube **Exaggerated or inaccurate claims** | "'before and after' images to promote significant alterations to the human body"; no YouTube, "Showing a misleading 'before-and-after' image" [oficial, 15936667 + 10249050] | Tirar o par antes/depois → produto, especialista, rotina, resultado descrito com ressalva ("resultados variam") |
| 4 | Close na barriga, celulite, estria, acne, calvície, ferida, unha com fungo | YouTube **Improper content › Body parts and health conditions** | "close-ups of symptoms like wrinkles, stretch marks, or acne with negative sentiment"; "bodily symptoms like fluids, rashes, visible pus" [oficial, 10249050] | Close na estria + "vergonha" → pessoa confiante / produto / explicação do mecanismo. "Ads for weight loss, hair loss, skin conditions... are allowed as long as the imagery isn't disturbing" [oficial] |
| 5 | Pergunta na 2ª pessoa sobre a condição: "Essa mancha está se espalhando?", "Você tem diabetes?", "Está endividado?" | YouTube Improper content + **Imposing negativity** (categoria sensível) + Clickbait (evento negativo) | Exemplo oficial reprovado: **"Is this horrifying rash spreading on your body? Get a consultation now."** [oficial, 10249050]. Imposing negativity: "Suggesting negative outcomes for users if they don't take specific actions" [oficial] https://support.google.com/adspolicy/answer/16700847 | "Você tem pré-diabetes e não sabe?" → "O que a glicemia de jejum diz — guia da Dra. X". Tirar o "você tem/está" e trocar diagnóstico por informação |
| 6 | Medo/urgência de dano: "Se não fizer isso, vai infartar", "Antes que seja tarde", "Seu fígado está morrendo" | **Clickbait ads** (negative life events) + YouTube **Negative events and imagery** + Shocking content | "pressure the user to purchase, subscribe to or stop consuming a product... in order to avoid harm"; exemplo YouTube: "There's no turning back. There's no guarantee of a healthy future."; Shocking: "Promotions that suggest you may be in danger, be infected with a disease" [oficial, 15936667 / 10249050 / 16490051] | "Pare de comer isso antes que seu fígado pare" → "3 hábitos que especialistas associam à saúde do fígado" |
| 7 | Cura/resultado garantido: "Acabe com a diabetes", "100% eficaz", "Seque 10 kg em 30 dias comendo de tudo" | **Unreliable claims** + YouTube Exaggerated claims + Healthcare › **Unapproved substances** | "Miracle cures for... arthritis, diabetes, Alzheimer's disease, or cancer"; "A weight loss ad that says you can eat whatever you want and lose 10 pounds in a month"; "Claiming a product is '100% effective'" [oficial] https://support.google.com/adspolicy/answer/15936857 | "Elimine a diabetes em 21 dias" → "Apoio nutricional para quem quer cuidar da glicemia*" + "*não substitui tratamento médico" |
| 8 | "Funciona igual remédio" / "o Ozempic natural" / nome parecido com medicamento | Healthcare › **Unapproved substances** | "Products that imply they're as effective as prescription drugs"; "names that are confusingly similar to an unapproved pharmaceutical" [oficial] https://support.google.com/adspolicy/answer/15595718 | Tirar qualquer comparação com remédio e qualquer termo de receita (GLP-1, "Ozempic", "remédio"). No Reddit: "anything with the words prescription, medication, medicine, glp1" dispara reprovação [consenso reddit] https://www.reddit.com/r/googleads/comments/1eua569/ |
| 9 | Ganho financeiro: "R$ 5 mil em 7 dias", "renda extra sem esforço", "método infalível", print de saque | **Unreliable claims** (money making) + YouTube clickbait | "'Get rich quick' schemes; guaranteeing returns"; "Make $5,000 in 5 minutes!" [oficial, 15936857 / 10249050] | "Faça R$ 10 mil/mês do zero" → "Curso de [habilidade]: o que você aprende em 8 módulos". Exemplo liberado: "Ads promising money that clearly indicate the legitimate steps required" [oficial] |
| 10 | Depoimento com resultado específico ("perdi 18 kg", "quitei 40 mil de dívida") | **Unreliable claims** (regra de depoimento) | "Testimonials that claim specific results must include a visible disclaimer... results can vary"; resultado garantido exige "a clear and easily accessible refund (money-back) policy" [oficial, 15936857] | Manter o depoimento + legenda visível "Resultados variam de pessoa para pessoa" no vídeo e na página + link da garantia |
| 11 | Botão falso, seta piscando, "notificação" de WhatsApp/iPhone na arte, enquete falsa ("A ou B?") | Misrepresentation › **Misleading ad design** (reforçada em 23/01/2025, fiscalização plena em 23/03/2025) | "Ads that look like messages, dialog boxes... request notifications"; "Ads with features that don't work, such as close buttons, text input boxes, multiple choice options"; "Moving and clicking arrows" [oficial] https://support.google.com/adspolicy/answer/15937463 · datas: https://www.seroundtable.com/google-misleading-ad-design-policy-update-38464.html | Criativo "print de conversa" → cena real gravada, sem imitar a interface do sistema |
| 12 | Celebridade, médico famoso ou youtuber "recomendando" (inclusive com IA), logo de TV/portal | Unacceptable business practices › **Public figure impersonation** (**egregious**) | "Falsely stating that a professional athlete sponsors your weight loss product"; "AI-generated videos of popular YouTubers" [oficial] https://support.google.com/adspolicy/answer/15938071 | Só com autorização documentada. Sem logo de Globo/G1/"Como visto em" se não for verdade |
| 13 | Palavrão, gíria pesada (mesmo com bip), linguagem sexual ("destruir na cama") | YouTube Improper content › **Inappropriate language** / **Racy content**; Shocking content | "Censoring a word with a sound effect is still considered a violation" [oficial, 16490051]; "bleeping or censoring is often insufficient" [oficial, 10249050] | Tirar do áudio **e** da legenda |
| 14 | Cena de funeral, choro, acidente, "a sociedade está desmoronando", vício retratado de forma crua | YouTube **Negative events and imagery › Mentally distressing** | "Ads that focus on abuse or addiction and that are likely to cause distress"; exemplo reprovado: "Your home could be next." [oficial, 10249050] | Narrativa de vilão abstrato → trocar a imagem de sofrimento por imagem neutra/positiva e contar a história de forma factual |
| 15 | Preço escondido ("clique pra ver o desconto"), teste grátis que vira assinatura, "de R$ 997 por R$ 37" irreal, parcela como se fosse o preço | Misrepresentation › **Dishonest pricing practices** (atualização com fiscalização a partir de **28/10/2025**) | "Omitting recurring costs and the billing interval"; "Promoting a free trial without clearly stating the trial period"; "Bait-and-switch tactics" [oficial] https://support.google.com/adspolicy/answer/15938375 · data: https://searchengineland.com/google-ads-updated-policies-to-target-dishonest-pricing-practices-462555 | Página mostra o preço total, o modelo (único/assinatura) e o intervalo de cobrança antes do checkout |
| 16 | Vídeo que não diz quem vende (hook "UGC" sem marca nenhuma) | Editorial › **Unidentified business**; Video ad requirements › **Unclear content** | "Videos must include a name or logo that clearly represents the advertiser, product, or service" [oficial] https://support.google.com/adspolicy/answer/2679940 | Logo ou nome da marca visível em algum ponto do vídeo (idealmente no fim) |
| 17 | Vídeo de celular tremido, legenda ilegível, áudio ruim | Editorial › **Video quality** | "Videos with illegible text, poor sound quality, or blurry, unclear, or unrecognizable visuals" [oficial] https://support.google.com/adspolicy/answer/14848298 | O formato "gravado no celular" continua valendo, mas com legenda legível e áudio limpo |
| 18 | O mesmo criativo reprovado subido de novo com uma letra trocada ("em@grecer", "0zempic") | Abusing the ad network › **Evasive ad content** / **Circumventing systems** (egregious) | "Bypassing enforcement mechanisms... by creating variations of ads, domains or content that have been disapproved" [oficial] https://support.google.com/adspolicy/answer/15938075 | Nunca contornar. Corrigir a causa ou recorrer. Blog BR lista trocar "o" por "0" em marca e reenviar anúncio reprovado sem mudança como gatilhos [isolado] https://blog.direcionar5.com/google-ads-fraude-em-sistemas/ |

**Aviso sobre falso positivo** [consenso reddit]: anúncios neutros também caem em *unreliable claims*/*clickbait* ("Contact Us Today" foi marcado; um app de idiomas com "Learn a new language" também). O relato mais comum é que a reprovação vem do **domínio/landing page**, não do texto. https://www.reddit.com/r/PPC/comments/17m5yf5/ · https://www.reddit.com/r/googleads/comments/1jwqzov/ · https://www.reddit.com/r/PPC/comments/1ht8odr/ · https://www.reddit.com/r/googleads/comments/1q8chvy/ (depois de reescrever tudo: "if the website content contains clickbait elements then that can also cause an ad to be flagged").

---

## 2. Regras por nicho

### 2.1 Saúde, emagrecimento, suplemento, dores

- **Rótulo quase automático: "Health in personalized advertising"** (categoria sensível). Cobre condições físicas ou mentais, crônicas, íntimas (genital, intestinal, urinária), procedimentos invasivos "including cosmetic surgery, surgical procedures, or injections", e aconselhamento para "depression, anxiety, and addiction, such as gambling addiction and alcohol addiction". [oficial] https://support.google.com/adspolicy/answer/16701855
  - **O que proíbe:** o uso de **públicos criados pelo anunciante** (Customer Match, segmentos de dados/remarketing, expansão de público, lookalike). Segmentos personalizados só rodam em Display com públicos não sensíveis ou por contexto; nos outros tipos de campanha "won't be eligible to serve". [oficial] https://support.google.com/adspolicy/answer/143465
  - **O que continua liberado:** públicos predefinidos do Google (in-market, afinidade, demografia, eventos da vida, localização). [oficial, 143465]
  - 🔴 **Demand Gen/Discovery** usa públicos do anunciante por padrão e "may be restricted from serving" em categoria sensível. Esclarecimento de **03/06/2026**. [oficial, 143465] · https://ppc.land/google-tightens-demand-gen-and-discovery-ad-serving-for-sensitive-categories/
  - Consenso: o rótulo **não é reprovação**. Na Busca, sem remarketing, costuma rodar normal; o que ele mata é remarketing e Customer Match. [consenso reddit] https://www.reddit.com/r/PPC/comments/1jbrahk/ · https://www.reddit.com/r/PPC/comments/1qlq6oz/ · https://www.reddit.com/r/googleads/comments/1j4xipn/
  - Contraponto: "reduz o alcance real em 95-99%" (2023). [isolado] https://www.reddit.com/r/PPC/comments/13pytr7/
  - O gatilho pode ser **uma palavra em qualquer página do site** ("addiction", "medication"). Uma dica que funcionou: landing page de uma página só, genérica, em domínio próprio para anúncios. [consenso reddit] https://www.reddit.com/r/PPC/comments/1uupdbi/ · https://www.reddit.com/r/googleads/comments/1kayfsn/ · https://www.reddit.com/r/PPC/comments/16vrfp0/
- **Proibido de vez (Unapproved substances):** efedra; hCG para emagrecer; suplemento com ingrediente farmacêutico; produto que "imply they're as effective as prescription drugs"; produto não aprovado apresentado como capaz de "preventing, curing, or treating a particular disease"; produto que já teve ação ou alerta de regulador; nome parecido com remédio; DHEA fora dos EUA. Referência de lista: LegitScript. [oficial] https://support.google.com/adspolicy/answer/15595718
- **Unreliable claims (saúde):** cura milagrosa, cura-tudo, emagrecimento irreal em prazo ou sem esforço, e alegação contra o consenso científico. O Google "may defer to local regulatory guidelines for health-related claims, including testimonial content". [oficial] https://support.google.com/adspolicy/answer/15936857
  - [inferência] No Brasil, o parâmetro local é a ANVISA: RDC 243/2018 (alegações de suplemento precisam de autorização prévia) e RDC 843/2024, com adequação até 01/09/2026. https://pronutrition.com.br/rdc-anvisa-suplementos-2024/
- **YouTube, específico:** proibido prometer "secret cure", "unrealistic personal transformation", antes/depois enganoso ou "100% effective". Exemplos oficiais reprovados: "Reduce your gray hairs with just some potato peels!" e "Cure yourself overnight from arthritis". Liberado: depoimento sem exagero e sem apelo emocional negativo. [oficial, 10249050]
- **Remédio de receita / farmácia (BR):** farmácia online só com registro na ANVISA e **sem** promover remédio de receita no anúncio, na página e nas palavras-chave, além de certificação do Google. [oficial] https://support.google.com/adspolicy/answer/176031
- **Menores de 18:** "Body modification and weight loss" é categoria restrita para adolescentes no YouTube e na Display. [oficial] https://support.google.com/adspolicy/answer/15416897
- **Certificação LegitScript não tira o "limitado":** mesmo certificado, o anúncio de emagrecimento/hormônio continua *Eligible (limited)*. [consenso reddit] https://www.reddit.com/r/googleads/comments/1j4xipn/

### 2.2 Sexualidade, pornografia, vício (NoFap)

- **Sexual content não roda no YouTube.** "Sexual content ads can't run on... YouTube"; não roda na Display; **TrueView video ads** e image ads também estão fora. Só a Busca aceita, e com limites de idade, SafeSearch e consulta. Entra aqui: "Sexually suggestive elements and themes", "Lewd or sexual language", poses sugestivas. [oficial] https://support.google.com/adspolicy/answer/6023699
- **YouTube › Racy content:** proíbe anúncio "focused on nudity or sexual topics". Liberado: produto de saúde sexual "if not sexualized", com nome genérico ou de marca. [oficial, 10249050]
- **Sexual health and wellness:** no Brasil, só **lubrificante** é permitido. Remédio de receita para disfunção erétil só em CA/NZ/EUA. Exige anúncio sem foco em "sexual pleasure or enhancement" e público 18+. [oficial] https://support.google.com/adspolicy/answer/15275138
- **Vício:**
  - *Addiction services* (certificação) cobre só drogas e álcool, e só em AU, CA, FR, IE, NZ e EUA. "Services for impulse control disorders, behavioral addiction... are out of scope". [oficial] https://support.google.com/adspolicy/answer/15598649
  - ⇒ [inferência] Um programa contra vício em pornografia **não precisa** dessa certificação. Mesmo assim cai em *Health in personalized advertising* (a categoria cita "addiction" em aconselhamento) e, se a copy ou a imagem sexualizar, em *Sexual content*, que bloqueia o YouTube inteiro.
  - YouTube proíbe anúncio "that focus on abuse or addiction and that are likely to cause distress". Conteúdo educativo de prevenção é aceito desde que sem imagem "visceral or shocking portrayals of the consequences". [oficial, 10249050]
- **Reescrita para NoFap [inferência]:** tirar "pornografia/masturbação/ereção/destrói sua vida sexual" do hook de vídeo e trocar por disciplina, foco, autocontrole, "hábito digital", energia e relacionamento. Nada de mulher em pose sugestiva nem de "recupere sua potência". A dor pode aparecer no corpo do vídeo, dita de forma factual, sem imagem sexual e sem cena de sofrimento. Não achei no Reddit nenhum caso documentado de NoFap aprovado ou reprovado no Google Ads.

### 2.3 Finanças, dívida, revisão de contrato

- **Brasil exige Financial Services Verification** para anúncio de serviço financeiro **e** para mostrar anúncio a brasileiros "who appear to be seeking financial services". Passo a passo: verificação de terceiro (G2RS) → verificação de anunciante do Google → código. Afiliados e agências aprovados precisam que o anunciante autorizado os indique. [oficial] https://support.google.com/adspolicy/answer/15332527
  - Uma loja virtual teve os ativos marcados "limited by policy: Financial Services Verification" só por citar parcelamento/pague depois (Klarna). [isolado, 09/2026] https://www.reddit.com/r/PPC/comments/1w9gs3o/
- **Credit repair services: proibido no mundo todo.** [oficial] https://support.google.com/adspolicy/answer/2464998
- **Debt services** (negociar dívida com credor, pagamento à vista reduzido ou parcelas menores) só em alguns países, com cadastro prévio. [oficial, 2464998] Não confirmei se o Brasil está na lista; checar a página *Debt services* antes de subir.
- **Loan modification:** proibido garantir a modificação, cobrar taxa antecipada (exceto escritório de advocacia) ou orientar a não falar com o credor ou advogado. [oficial, 2464998]
- **Revisão de contrato / revisional de juros [inferência]:** tende a cair em *debt services* ou *loan modification* e, se for afiliado ou gerador de leads, em *Misleading representation*. Exemplo oficial: "An affiliate marketer advertising legal services without disclosing that they do not provide legal services". [oficial] https://support.google.com/adspolicy/answer/15936666
- **Divulgações obrigatórias** na página de serviço financeiro: endereço físico, todas as taxas e link para acreditação alegada. Tudo "clearly and immediately visible", nunca em tooltip ou outra aba. [oficial, 2464998]
- **Categoria sensível:** "Negative financial status" inclui "Debt-focused products and support", falência e crédito predatório. Sem públicos do anunciante. [oficial] https://support.google.com/adspolicy/answer/16700443
- **Trading/educação financeira:** "we teach predictable patterns" foi apontado como linguagem de resultado. Campanhas novas também foram reprovadas porque o domínio já estava marcado. [consenso reddit, 09/2026] https://www.reddit.com/r/googleads/comments/1wfi3dh/
- **Opções binárias e sinais de trading: proibidos**, inclusive blog educativo sobre o tema. [oficial, 2464998]

### 2.4 "Você" personalizado ("Você tem diabetes?", "Está endividado?")

- A política atual de personalização (reestruturada; a página de 2023 tinha outro formato) fala em **segmentação** e não traz mais uma regra textual separada de "não sugerir que conhece o usuário". A proibição de copy vem de três lugares:
  1. **Imposing negativity** (categoria sensível): "Body shaming", "Suggesting negative outcomes for users if they don't take specific actions". [oficial] https://support.google.com/adspolicy/answer/16700847
  2. **YouTube Improper content:** exemplo reprovado "Is this horrifying rash spreading on your body?". [oficial, 10249050]
  3. **Clickbait › negative life events:** "illness, arrests or bankruptcy to induce fear, guilt". [oficial, 15936667]
- Exemplo antigo do Google citado por blogs: "You're buried in debt. Get help today." como anúncio que finge conhecer a situação financeira do usuário. [isolado, histórico, sem confirmação na página atual] https://www.maqe.com/insight/personalized-google-ads-what-you-are-not-allowed-to-do/
- Leitura prática: tirar da copy "struggling with X?" e qualquer enquadramento que pressuponha condição ou sintoma. [consenso reddit, embora o comentário mais votado falasse do Meta, a lógica vale igual] https://www.reddit.com/r/PPC/comments/1uupdbi/
- **Regra de reescrita [inferência]:** trocar a 2ª pessoa diagnóstica pela 3ª pessoa informativa ou por curiosidade sobre o mecanismo. "Você está endividado?" → "Como funciona a renegociação de dívidas em 2026". "Sua barriga não diminui?" → "Por que a gordura abdominal é a última a sair, segundo a Dra. X".

---

## 3. Página de destino: o que derruba

| Elemento do funil DR | Política | Trecho oficial / relato | Gravidade |
|---|---|---|---|
| **Presell/bridge page** que só leva a outro site (hoplink, página do produtor) | Destination requirements › **Insufficient original content** | "Bridge pages, doorways, gateways, or other intermediate pages that are only used to link to other sites"; "Templates or pre-generated websites that provide duplicate content" [oficial] https://support.google.com/adspolicy/answer/16427718 | Reprovação (aviso de 7 dias) |
| Presell que **agrega valor** (quiz que recomenda, comparativo) | idem | "Se a bridge page conduz o usuário por um caminho personalizado, isso costuma bastar para mostrar que há troca de valor" (tradução) [isolado, 2022] https://www.reddit.com/r/PPC/comments/zm2pgl/ | Zona cinzenta |
| Site com **links de afiliado** | Misrepresentation / UBP | "O Google suspende contas rápido quando há qualquer link de afiliado", salvo conta antiga ou gasto alto (tradução) [consenso reddit, 11/2025] https://www.reddit.com/r/googleads/comments/1omr5e3/ | Suspensão |
| **URL final redireciona** para outro domínio (bitly → hoplink → produtor) | **Destination mismatch** | "Redirects from the final URL take the user to a different domain" [oficial] https://support.google.com/adspolicy/answer/16428020 · [consenso reddit] https://www.reddit.com/r/PPC/comments/hgct1p/ | Reprovação; repetido pode virar circumventing |
| Link de afiliado Hotmart no **modelo de acompanhamento** apontando para a página do produtor | Circumventing systems | Caso brasileiro: conta suspensa por "evasão de sistemas" [isolado, BR] https://support.google.com/google-ads/community-guide/316589721 (resumo na busca) | **Suspensão egregious** |
| **"Notícia" falsa / advertorial** imitando portal (logo do G1, "Globo Repórter") | UBP ("Make it seem like you're affiliated with another brand") + Misleading representation | [oficial] https://support.google.com/adspolicy/answer/15938071 · "O Google apertou bastante em advertorial faz tempo" (tradução) [isolado] https://www.reddit.com/r/PPC/comments/kjmp3m/ | **Egregious** |
| **Chat simulado**, notificação falsa, pop-up imitando WhatsApp/sistema na página | Destination experience › **abusive experiences** | "Fake messages: Ads or other elements that resemble chat apps, warnings, system dialogs, or other notifications" [oficial] https://support.google.com/adspolicy/answer/16427615 | Reprovação |
| **Back-button hijack** (exit redirect, trocar o histórico) | Destination experience | "Sites that disable or interfere with the browser's back button"; "Browser history manipulation" [oficial, 16427615] | Reprovação |
| **Auto-redirect** (VSL que pula sozinha para o checkout sem clique) | Destination experience | "Websites that auto-redirect the page with no action from the user" [oficial, 16427615] | Reprovação |
| **Pop-up/interstitial** que cobre o conteúdo, countdown antes do conteúdo | Destination experience + Better Ads | "pop-ups or interstitials that interfere with the user's ability to see the content"; "Prestitial 'countdown' ads" [oficial, 16427615] | Reprovação |
| Pop-up que **impede o crawler** de ver a página | **Cloaking** | "A pop-up... that blocks access to the majority of your website's content, meaning Google cannot access your landing page" [oficial, 15938075] | **Egregious** |
| **VSL sem controles / sem preço até o minuto X** | [inferência] não há regra explícita contra VSL; o risco é *Dishonest pricing* (preço e modelo de cobrança não visíveis) + *Destination experience* ("unnecessarily difficult or frustrating to navigate") + *Insufficient original content* se o vídeo é só um player sem texto | — | Risco médio |
| **Preço oculto**, assinatura sem intervalo, trial sem data de cobrança | **Dishonest pricing practices** | ver item 15 da tabela da seção 1 [oficial, 15938375] | Reprovação; repetido gera suspensão |
| **Oferta do anúncio ≠ página** ("R$ 37" no vídeo e R$ 97 no checkout) | **Unavailable offers** | "promoting a price that is inaccurate"; "Call-to-action in the ad that isn't easily available from the destination" [oficial] https://support.google.com/adspolicy/answer/15937063 | Reprovação |
| **Depoimento** com número, sem ressalva | Unreliable claims | exige aviso visível de que resultados variam + política de reembolso se houver garantia [oficial, 15936857] | Reprovação |
| **Sem rodapé/contato/Sobre** | UBP (boas práticas) + Limited ad serving | "Make sure your website has updated contact information and a clear explanation of what your company does, like on an 'About us' page" [oficial, 15938071] | Aumenta a chance de suspensão por UBP |
| Checklist de agência para a página | — | nome legal/fantasia no rodapé, telefone ou e-mail que funcionam, política de reembolso a 2 cliques [isolado] https://dailyintelservice.com/compliance/google-ads-misrepresentation-suspension-what-fixes-it | — |
| **Página diferente para o Googlebot** (JS que quebra, plugin, firewall/CDN, bloqueio geográfico dos EUA) | Not crawlable / **Cloaking** | "Destinations that return an HTTP error code for Google AdsBot"; ingressos: "Do not block US-based crawlers via IP geolocation" [oficial] https://support.google.com/adspolicy/answer/6368661 · https://support.google.com/adspolicy/answer/6368711 · Search Console mostrou renderização diferente para o Googlebot; recuperou após 6 recursos [isolado, 05/2026] https://www.reddit.com/r/googleads/comments/1t7qt23/ · CDN/firewall/"site não acessível dos EUA" como causa [consenso reddit] https://www.reddit.com/r/PPC/comments/1nadqkg/ | **Egregious** |
| **Site hackeado / malware** (WordPress com plugin velho) | Compromised sites / Malicious software | Reativada depois de escanear com Sucuri e limpar [isolado, 2022] https://www.reddit.com/r/PPC/comments/ttej1c/ | Egregious |
| **Quiz** na página | Sem regra específica para quiz na página [inferência]. No **anúncio**, opções de múltipla escolha que não funcionam = *Misleading ad design*. Quiz que coleta dado de saúde → *Health* (sem público do anunciante) | — | Baixo na página, alto se estiver no criativo |
| Várias ofertas ou temas no mesmo domínio (ex.: um funil NoFap e um cristão) | [inferência] o Google avalia o domínio e fala em "Destination... that violate Google Ads' policies, even if it's within the same domain" (cloaking) | [oficial, 15938075] | Contaminação cruzada |

**Ferramenta do próprio Google:** dá para trocar o user agent no Chrome DevTools e ver a página como o AdsBot. [oficial] https://support.google.com/adspolicy/answer/16431325 (link citado dentro de 6368661)

---

## 4. Suspensão de conta

### 4.1 Gatilhos
- **Lista oficial de egregious (suspensão imediata e permanente):** Circumventing systems, Coordinated deceptive practices, Counterfeit, Malicious software, Prescription opioid painkillers, Unauthorized pharmacies, **Unacceptable business practices**, Trade sanctions, Sexually explicit content, CSAE. [oficial] https://support.google.com/adspolicy/answer/2375414
- **Circumventing systems:** abrange conta nova depois de suspensão; variações de anúncio ou domínio reprovado; informação falsa na verificação; "Spreading ads that violate Google Ads' policies across 2 or more accounts"; e suspensão por "adverse regulatory warnings... or direct complaints from users". **Não** suspende por erro editorial. Atualização de 07/2023 inclui "repeated and simultaneous policy violations across any of your accounts". [oficial] https://support.google.com/adspolicy/answer/15938075 · https://support.google.com/adspolicy/answer/13666794
- **Contas relacionadas:** "Any related accounts (for example, accounts using the same payment method) will also be suspended, and any new accounts you create will be automatically suspended." [oficial] https://support.google.com/adspolicy/answer/7187501
- **Sistema de strikes (não egregious):** sem strike na primeira violação; strike 1 = bloqueio de 3 dias; strike 2 = 7 dias; strike 3 = suspensão. Máximo de 3 por política. [oficial, 2375414]
- Segundo a StubGroup, Circumventing systems é ~37% das suspensões que atendem; UBP vem em seguida. Gatilhos ocultos citados: redirect para outro domínio, anúncio pausado antigo ("Google crawls paused ads even if they haven't run for years") e site hackeado. [isolado, atualizado em 16/09/2026] https://stubgroup.com/blog/how-to-fix-a-circumventing-systems-suspension/
- Rodar vários negócios numa conta só, ou abrir conta de cliente a partir da conta da agência, derrubou as duas contas. [consenso reddit] https://www.reddit.com/r/PPC/comments/1k5yoq7/
- Emprestar a conta a um amigo suspenso resultou em ban por "Cloaking". [isolado, 08/2026] https://www.reddit.com/r/googleads/comments/1w2tu05/
- **Fingerprint:** "uma vez que uma conta é marcada, eles registram tudo: IP, dispositivo, navegador, forma de pagamento, dados da empresa" (tradução). Abrir contas novas no mesmo computador "só confirma". [consenso reddit, 02/2026] https://www.reddit.com/r/googleads/comments/1qxi9fy/
- **Conta nova:** dados errados de empresa ou cobrança no cadastro geram suspensão rápida. Um blog de agência afirma que o motivo principal é "dados de cobrança suspeitos". [consenso reddit + isolado] https://www.reddit.com/r/PPC/comments/1chi104/
- **Pagamento (BR):** alternar cartão de pessoa física e jurídica sem casar com o tipo de conta; criar conta nova com o mesmo CPF/CNPJ. [isolado, BR, 01/2024] https://blog.direcionar5.com/google-ads-fraude-em-sistemas/

### 4.2 Verificação de anunciante
- "All advertisers will eventually be required to complete advertiser verification." Motivos para ser selecionado: conteúdo "potentially suspicious", setores como finanças, "features that are often misused". A conta pode ser **pausada** até a verificação quando há suspeita de *Misleading representation*, **Unreliable claims**, *Unidentified business* etc. [oficial] https://support.google.com/adspolicy/answer/9703665
- **Para recorrer de suspensão, alguns anunciantes precisam verificar primeiro.** São 3 tentativas; depois disso não podem recorrer (desde 10/10/2023). [oficial] https://support.google.com/adspolicy/answer/13993199 · [oficial, 2375414]
- Dica: o nome no perfil de pagamento deve bater com os documentos. "Não abra conta nova, ou vem ban permanente por circumventing." [consenso reddit, 01/2026] https://www.reddit.com/r/googleads/comments/1qebfaj/

### 4.3 Limited Ad Serving (não é suspensão, mas mata o volume)
- Limita impressões de anunciante "não qualificado". Critérios: atributos da conta, **maturidade da conta**, denúncias de usuários, histórico de conformidade, setor e status da verificação. No YouTube: cumprir as políticas, verificar a conta e "continue to build campaigns and creatives with positive user engagement". **Anúncios individuais não são reprovados.** Recurso por formulário próprio. [oficial] https://support.google.com/adspolicy/answer/13889491
- **Atualização de 08/2026:** passa a cobrir **todo o Google Ads**, com implementação gradual até **2028**. [oficial] https://support.google.com/adspolicy/answer/17344822
- Relatos: 6-7 semanas para liberar mantendo a marca consistente (domínio, anúncio, página, pagamento). Em outro caso, 3 meses e ainda limitado. [consenso reddit, 04/2026] https://www.reddit.com/r/PPC/comments/1sj0wys/ · Tirar palavras de marcas de terceiros liberou sozinho em ~2 meses; fixar o domínio no título 1. [isolado] https://www.reddit.com/r/PPC/comments/189aym6/

### 4.4 Recurso: o que funciona segundo os relatos
- **Oficial:** um recurso por vez; recursos em excesso podem deixar de ser processados por **7 dias**. Dicas: aplicar as boas práticas, explicar o caso (para cloaking, "why you were showing different content"), mandar provas, verificar a identidade. [oficial, 2375414]
- **Diagnosticar, corrigir e recorrer uma vez, com provas.** "Um recurso que diz 'olhem de novo, não fiz nada' é recusado automaticamente" (tradução). [isolado, 06/2026] https://www.reddit.com/r/PayPerClickMarketing/comments/1ucozsd/
- Search Console → Inspeção de URL (teste em tempo real) para comparar a renderização do Googlebot com a do usuário; foram 6 recursos até dar certo. [isolado] https://www.reddit.com/r/googleads/comments/1t7qt23/
- Escanear malware (Sucuri), limpar e recorrer; reativada no 4º recurso. [isolado, 2022] https://www.reddit.com/r/PPC/comments/ttej1c/
- Contratar um ex-Google no Brasil, que escreveu o recurso com as palavras-chave da política e listou as correções. [isolado, BR] https://www.reddit.com/r/googleads/comments/1ojbrq3/
- Recurso honesto, assumindo o erro, é a única chance em circumventing ("improvável, mas não zero"). [isolado] https://www.reddit.com/r/googleads/comments/1w2tu05/
- Ligar para o escritório local do Google ou escalar pelo @AdsLiaison no X. [isolado] https://www.reddit.com/r/PPC/comments/1k5yoq7/ · https://www.reddit.com/r/googleads/comments/1qebfaj/
- **Não funciona / piora** [consenso reddit + isolado StubGroup]: abrir conta nova para contornar; repetir o mesmo recurso; ligar para o suporte comum; deixar anúncios reprovados pausados na conta; usar "agências de reativação" suspeitas.
- **Divergência** [consenso reddit dividido]: "conta nova em nome de outra empresa (CNPJ diferente) funciona se o negócio for legítimo" versus "nunca abra conta nova com suspensão pendente". A regra oficial fica com o segundo grupo: contas novas de anunciante suspenso "will be automatically suspended". https://www.reddit.com/r/PPC/comments/1l7s3nl/ · https://www.reddit.com/r/googleads/comments/1w2tu05/
- Métrica do Google: o Gemini "cortou 80% das suspensões incorretas" em 2025. [isolado, citando o relatório] https://stubgroup.com/blog/the-state-of-google-ads-suspensions/

---

## 5. Reprovado × Qualificado (limitado) × restrição por idade/sensível no YouTube

| Status | O que significa | Roda? | Fonte |
|---|---|---|---|
| **Eligible** | Passou | Sim | [oficial, 10249050] |
| **Eligible (limited)** / "Limited by policy" | Cumpre a política, mas com restrição de país, idade, dispositivo ou certificação. Também quando "your website content contains terms associated with regulated industries" | Sim, com alcance menor (pode ficar em 0) | [oficial] https://support.google.com/google-ads/answer/2684542 |
| **Health in personalized advertising** (aparece como limitado) | Categoria sensível: bloqueia remarketing, Customer Match e lookalike; Demand Gen pode não rodar | Sim na Busca/Vídeo com público do Google; campanha que depende de público do anunciante não roda | [oficial, 143465] · [consenso reddit] |
| **Limited by YouTube automated content decision** | Decisão automática sobre o vídeo; um relato diz que o CPA alvo baixo parecia ser a causa e outro diz que editar os primeiros segundos resolveu | Não ou pouco | [isolado] https://www.reddit.com/r/PPC/comments/1c9qa14/ |
| **Disapproved** | Viola a política | Não, até corrigir (nova análise em 24-48h) ou recorrer | [oficial, 15936667] |
| **Restricted access video** | Vídeo **com restrição de idade** no YouTube, com reivindicação de propriedade intelectual ou com restrição de conteúdo | **Reprovado como anúncio**; recorrer da restrição de idade no YouTube Studio ou trocar o vídeo | [oficial] https://support.google.com/adspolicy/answer/15577022 |
| **Unavailable video** | Vídeo privado, excluído, "live premiere" ou só para membros | Reprovado; tem que ser **público ou não listado** | [oficial] https://support.google.com/adspolicy/answer/15576014 |
| **Sexual content (moderately restricted)** | Recebe *Eligible (limited)* no Google Ads em geral | **Não roda no YouTube nem na Display**, só na Busca | [oficial, 6023699 + 2684542] |
| **Proteções para menores de 18** | Emagrecimento/modificação corporal, namoro, conteúdo chocante: não aparecem para adolescentes nem para usuário não logado | Sim, só para adultos identificados | [oficial, 15416897 + 7187501] |
| **Limited Ad Serving** (nível de conta) | Anunciante "não qualificado"; impressões limitadas **sem** reprovar anúncio | Pouco | [oficial, 13889491] |
| **Account paused** (verificação) | Aguardando verificação de anunciante | Não | [oficial, 9703665] |
| **Temporary account hold** | Strike 1 = 3 dias; strike 2 = 7 dias | Não, durante o bloqueio | [oficial, 2375414] |
| **Suspended** | Egregious (imediata) ou 3º strike / aviso de 7 dias | Não; contas relacionadas também caem | [oficial, 7187501] |

Notas:
- Aviso de política só no nível do conjunto de recursos, sem dizer qual recurso: "Financial Services Verification" vem de texto sobre parcelamento; "Shocking content" costuma ser uma **imagem**. [isolado, 09/2026] https://www.reddit.com/r/PPC/comments/1w9gs3o/
- **Anúncio em vídeo sem limite de duração** para in-stream pulável ("videos that are less than 3 minutes long typically perform better"). In-stream não pulável: máximo de 30 s em leilão. [oficial] https://support.google.com/adspolicy/answer/2679940

---

## 6. Checklist antes de subir

### A. Criativo (vídeo + título + CTA)
- [ ] Nenhum hook de segredo, escândalo, "você não vai acreditar", "assista até o fim" ou curiosidade que esconda o que é o produto
- [ ] Sem antes/depois do corpo; sem close em barriga, estria, acne, ferida, pus ou calvície com tom negativo
- [ ] Sem pergunta diagnóstica na 2ª pessoa ("Você tem X?", "Sua Y está...?", "Está endividado?"); diagnóstico trocado por informação
- [ ] Sem ameaça ou dano ("antes que seja tarde", "vai morrer", "seu órgão está falhando"), funeral, choro, acidente, "a sociedade está ruindo"
- [ ] Sem cura, "100%", "garantido", prazo com número de kg ou R$, "sem esforço", "coma de tudo"
- [ ] Sem comparação com remédio nem termos de receita (GLP-1, Ozempic, "remédio", "medicação") no anúncio, **nas palavras-chave e na página**
- [ ] Depoimento com número → legenda visível "resultados variam" + garantia acessível
- [ ] Sem celebridade, médico famoso, youtuber ou logo de TV sem autorização documentada; nada de IA imitando pessoa real
- [ ] Sem botão falso, seta animada, notificação ou print de WhatsApp/iPhone imitando interface, enquete falsa
- [ ] Sem palavrão (nem com bip), sem linguagem ou pose sexual; em NoFap, nada que sexualize
- [ ] Nome ou logo da marca aparece no vídeo; legenda legível; áudio limpo
- [ ] Oferta ou preço citado no vídeo = o que está na página e no checkout
- [ ] Vídeo **público ou não listado**, sem restrição de idade, sem reivindicação de direitos autorais, não é "estreia"
- [ ] Se já foi reprovado: **corrigir a causa**; não subir variação com letra trocada

### B. Landing page / funil
- [ ] URL final no **mesmo domínio** da URL de exibição; sem redirect para outro domínio (hoplink, bitly, página do produtor); rastreamento com `{ignore}` ou tracker certificado
- [ ] Página própria com **conteúdo original e valor** (não é ponte nem template duplicado)
- [ ] Sem cara de notícia falsa, portal imitado ou "como visto na TV" falso
- [ ] Sem chat simulado ou notificação imitando app, sem exit-redirect, sem back-button hijack, sem auto-redirect, sem pop-up que cubra o conteúdo, sem countdown antes do conteúdo
- [ ] Preço total, modelo de cobrança (único ou assinatura) e intervalo visíveis antes do checkout; trial com data de cobrança
- [ ] Rodapé com nome legal/CNPJ, contato que funciona, página "Sobre", políticas de privacidade, reembolso e termos; reembolso a no máximo 2 cliques
- [ ] Nenhuma palavra-gatilho em **qualquer página do domínio** (vício, remédio, dívida, alegação de cura) que não seja necessária; considerar um domínio exclusivo para cada oferta sensível
- [ ] Página idêntica para o Googlebot e para o usuário: testar no Search Console (teste de URL ativa) e com o user agent do AdsBot no DevTools; firewall, CDN e bloqueio geográfico liberando crawler dos EUA
- [ ] WordPress/plugins atualizados; escanear malware
- [ ] Finanças BR: verificação de serviços financeiros (G2RS) **antes** de subir; endereço e taxas visíveis; afiliado deixa claro que não é o prestador
- [ ] Saúde BR: alegação dentro do que a ANVISA permite (RDC 243/2018 e 843/2024); nada de remédio de receita
- [ ] Um tema por domínio: funil de vício/sexualidade separado do funil de saúde ou religião

### C. Conta
- [ ] Verificação de anunciante concluída, com nome do pagador = documentos = marca no site
- [ ] Tipo de conta (PF/PJ) = cartão; sem trocar de cartão ou perfil de pagamento sem necessidade
- [ ] **Uma empresa por conta**; contas de cliente com pagamento próprio, ligadas à MCC
- [ ] Nunca emprestar a conta; nunca abrir conta nova com suspensão pendente (mesmo IP, dispositivo, pagamento ou CNPJ = circumventing)
- [ ] Remover anúncios reprovados antigos, inclusive pausados
- [ ] Oferta sensível (saúde/finanças/vício): não usar remarketing, Customer Match, lookalike nem expansão de público; em Demand Gen, trocar para públicos predefinidos do Google
- [ ] Conta nova: começar com a oferta mais "limpa" para ganhar maturidade (critério do *Limited ad serving*) antes de subir a oferta agressiva [inferência a partir de 13889491]
- [ ] Se reprovar: ler o motivo exato na coluna Status → corrigir anúncio **e** página → **um** recurso com a lista do que mudou → esperar 24-48h
- [ ] Se suspender: não abrir conta nova; diagnosticar (malware, renderização, redirects, pagamento, verificação) → corrigir → um recurso detalhado com provas (CNPJ, contratos, autorizações)

---

### Limitações desta pesquisa
- O Reddit só foi acessível pelo JSON do old.reddit via navegador (a busca e o fetch direto estão bloqueados). Foram lidas ~60 threads; nenhuma trata especificamente de NoFap, revisional de contrato ou VSL brasileira no Google.
- Não confirmei a lista de países de *Debt services* nem se o Brasil está incluído.
- Várias páginas oficiais não mostram data de atualização. As datas citadas vêm do registro de mudanças do Google ou da imprensa especializada (SER/SEL/PPC.land).
