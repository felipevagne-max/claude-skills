# Claude Skills — Felipe Loriem

Skills e comandos que eu uso no [Claude Code](https://claude.com/claude-code) para copy de resposta direta, criativos de anúncio, webinários, funis e organização no Obsidian.

## Instalação

```bash
git clone https://github.com/felipevagne-max/claude-skills.git
cd claude-skills

# todas as skills
cp -R skills/* ~/.claude/skills/

# ou só uma
cp -R skills/mentecopy ~/.claude/skills/

# comandos /resume e /save
cp commands/*.md ~/.claude/commands/
```

Depois é só chamar no Claude Code: `/mentecopy`, `/raiox`, `/fabrica`…

## Skills autorais

### Copy e persuasão
| Skill | O que faz |
|---|---|
| `mentecopy` | Lente de copy direct response e psicologia da persuasão que fica ativa durante a conversa |
| `black-copy-chief` | Produção de ponta a ponta de copy agressiva e baseada em evidência (pesquisa → mecanismo → peça → revisão) |
| `masterbelief` | Roteiro One Belief a partir de pesquisa de mercado: as 10 perguntas de persuasão em narrativa contínua para VSL/webinário |
| `sherlocktube` | Pesquisa de audiência pelos comentários do YouTube: desejos, dores, crenças, objeções e a linguagem exata do público |
| `raiox` | Diagnóstico de funil pela Máquina de Crença (funil = paciente, sintoma = doença) |

### Anúncios
| Skill | O que faz |
|---|---|
| `adsiniciais` | Pacote inicial de criativos de Meta Ads no modelo validado |
| `adsloriem` | Adapta criativos validados de Meta Ads para novos nichos, experts e públicos |
| `adstube` | Cria, traduz e audita criativos de YouTube Ads de resposta direta (mini-VSL in-stream, curto) |
| `cinema` | Direção de vídeo cinematográfico no Higgsfield pela CLI, do brief ao clipe |

### Webinário e funil
| Skill | O que faz |
|---|---|
| `slides` | Gera a apresentação completa de um webinário de vendas (3 Verdades ou Mecanismo/Demolição) |
| `vortice` | Cria ou adapta apresentações de webinário com o mesmo framework |
| `comentarios` | Gera comentários de chat cronometrados para webinário a partir da transcrição do vídeo |
| `superfluxo` | Fluxos de automação UniChat (WhatsApp) para webinários: Captura + Antecipação, com JSON de importação |
| `fabrica` | Fábrica de Micro Ofertas: funil em grade página×preço, quiz, PVs, checkout, painel, webhook e ads |

### Produtividade
| Skill / comando | O que faz |
|---|---|
| `conselho` | Mesa redonda deliberativa com grandes mentes da história para decisões |
| `lint` | Audita um vault Obsidian: links quebrados, notas órfãs, conteúdo desatualizado |
| `superenglish` | Aprender inglês lendo fantasia (Brandon Sanderson) |
| `/resume` (comando) | Retoma o contexto da última sessão pelos logs do Obsidian |
| `/save` (comando) | Salva o progresso da sessão no log do Obsidian e na memória do Claude |

> Algumas skills assumem a minha estrutura de pastas (`~/Obsidian/Brain/`, `~/Projects/`). Ajuste os caminhos no `SKILL.md` para o seu ambiente.

## Skills de terceiros que eu uso

Não estão copiadas aqui: instale da fonte original.

| Pacote | Skills | Fonte |
|---|---|---|
| Marketing Skills | copywriting, page-cro, paid-ads, email-sequence, pricing-strategy, launch-strategy… | [coreyhaines31/marketingskills](https://github.com/coreyhaines31/marketingskills) |
| Superpowers | brainstorming, writing-plans, systematic-debugging, test-driven-development… | [obra/superpowers](https://github.com/obra/superpowers) |
| Cloudflare | cloudflare, wrangler, durable-objects, agents-sdk, workers-best-practices, web-perf… | [cloudflare/skills](https://github.com/cloudflare/skills) |
| Anthropic | frontend-design, skill-creator | [anthropics/skills](https://github.com/anthropics/skills) |
| Higgsfield | higgsfield-generate, higgsfield-product-photoshoot… | Higgsfield CLI |
| graphify | graphify | [graphify](https://github.com/safishamsi/graphify) |
