---
name: fabrica
description: Fábrica de Micro Ofertas — lança uma oferta de ponta a ponta (funil em grade página×preço, quiz, PVs, checkout, painel, webhook, app opcional e ads) a partir do template validado Dominus→Pack 2K. Trigger quando o usuário disser '/fabrica', 'fabrica', 'nova oferta', 'novo funil', 'montar funil', 'micro oferta', 'micro app', 'clonar o dominus', 'fazer igual o pack 2k', 'próximo passo da oferta', ou estiver dentro de um repo criado pelo novo.sh (tem _brief/ESTADO.md). Sem argumento = executar a PRÓXIMA etapa pendente do ESTADO.md. Subcomandos 'nova <slug>', 'qa', 'ler', 'status'.
---

# /fabrica — Fábrica de Micro Ofertas

Você opera o template `~/Projects/_template-microoferta/` (leia o README dele).
O Felipe NÃO repete contexto: tudo que você precisa está em `_brief/` e em
`_brief/ESTADO.md`. Se algo faltar, é o documento que está incompleto — peça o
campo, não o contexto.

## Princípios (não negociáveis)
1. **Replicar o validado.** O template é o código. Você preenche config, escreve
   copy e conteúdo. Não reescreve motor. Se precisar tocar em `shared/core.js`,
   `go/`, `api/webhook.js` ou `painel/`, pare e diga por quê.
2. **Uma pergunta por vez**, com alternativas e saída livre.
3. **Checkpoint antes de avançar**: cada etapa termina mostrando o resultado e
   esperando aprovação. Etapa aprovada = `[x]` no ESTADO.md + data.
4. **Honestidade**: se a prova não existe, o campo fica vazio e o bloco não
   renderiza. Nunca inventar depoimento, número ou claim.
5. **Auto-save**: toda decisão vai para `ESTADO.md › Decisões` na hora, e ao
   final da sessão para `~/Obsidian/Brain/Notas/Log de Sessões.md`.

## Despacho
```
/fabrica                → ler ESTADO.md, executar a 1ª etapa sem [x]
/fabrica nova <slug>    → etapa 0 (criar repo)
/fabrica status         → resumo do ESTADO.md + pendências
/fabrica qa             → só QA.md, num funil já no ar
/fabrica ler            → só LEITURA.md sobre o painel
```
Se não houver `_brief/ESTADO.md` no cwd e não for `nova`: perguntar o slug e
`cd ~/Projects/<slug>`.

## Etapas

### 0 · nova <slug>
Perguntar (uma por vez): NOME comercial · domínio · modo (`externa` | `app`) ·
provedor (`cakto` | `lastlink`) · pixel. Rodar
`~/Projects/_template-microoferta/novo.sh <slug> "<NOME>" <dominio> <modo> <pixel>`.
Dizer ao Felipe: "preencha `_brief/pesquisa.md`, `onebelief.md` e `entregavel.md`
(o entregavel é formulário: marque os blocos). Depois `/fabrica`."
Criar nota `~/Obsidian/Brain/Projetos/<NOME>.md` (template de projeto) e linkar no Home.

### 1 · config
Ler os 3 arquivos de `_brief/`. Preencher `shared/config.js` **campo a campo
pela fonte indicada no próprio arquivo** (§1-2 entregavel · §3 onebelief · §4
pesquisa · §5 perguntar ao Felipe). Campo sem fonte no documento → listar como
"falta no brief", não inventar. Grade inicial padrão: `PAGES` = 2 PVs + quizA1/A2,
`ARMS` = 2 preços (pedir os dois), `ABERTURAS` = a1/a2.
Mostrar o config preenchido + lista de faltas. Esperar aprovação.

### 2 · copy
Carregar `/mentecopy`. Escrever na ordem:
1. `quiz/index.html › STEPS` — 8-12 passos, tipos já existentes (cards, slider,
   rows, yesno, intro). Cada passo com `react` que ecoa a linguagem da pesquisa.
2. PVs em `v1/` e `v2/` (dois MOTORES distintos — ex. absolvição × culpa, ou
   argumento × história), mantendo TODOS os ganchos `data-*` (`data-p`,
   `data-cta`, `data-claim`, `data-bonus`, `data-proofs`, `data-expert`,
   `data-entrega`, `data-stack`). Copy vive no HTML; core hidrata o resto.
3. `obrigado/` — só os textos de ENTREGA no config.
Regras de copy: `references/copy-regras.md`. Entregar também em DOCX
(`pandoc`) na pasta `_brief/copy/` para revisão. Esperar aprovação.

### 3 · build
1. **Supabase**: rodar `sql/schema.sql` no projeto olimpo-system via management
   API (token no keychain "Supabase CLI", decodar go-keyring-base64). DDL não
   passa por psql — ver `references/supabase.md`.
2. **Vercel**: `vercel link` novo projeto · envs (`OFZ_*` já renomeadas pelo
   novo.sh: `<SLUG>_SB_URL`, `_SB_SERVICE`, `_STATS_KEY`, `_HOOK_KEY`; app:
   `_HOOK_SECRET`, `_ADMIN_KEY`, `_VAPID_PUB/PRIV`, `CRON_SECRET`) · deploy
   de worktree limpo · região gru1 · domínio.
3. **Checkouts**: pedir ao Felipe as URLs por braço; preencher `PRECOS`.
4. **Webhook**: URL `https://<dominio>/api/webhook?key=<HOOK_KEY>` — o Felipe
   cadastra no provedor (eventos venda + estorno + chargeback). Cakto: copiar o
   `secret` gerado para `_HOOK_SECRET` DEPOIS de criar.
5. **QA.md inteiro**, marcando linha a linha. Deploy só sobe para tráfego com
   QA verde e **1 compra real** confirmada no painel.
Mostrar URLs + QA marcado. Esperar aprovação.

### 4 · app (só modo app)
1. `app/conteudo.json` — formato `{dia, titulo, fase, corpo[2], ordem}`; quantidade
   e fases do entregavel §4. Se o conteúdo não existe: escrever com `/mentecopy`
   em lotes de 10 dias, aprovando o 1º lote antes dos demais.
2. `APP.BLOCOS` / `APP.NOMES` no config — a barra do app lê daqui.
3. `APP.ITENS` — regex por nome EXATO dos produtos no checkout (entregavel §5).
4. Vocabulário: `grep -n "Ordem\|Altar\|Patente\|Aliado\|Arsenal\|Escudo\|Irmão" app/index.html`
   e trocar pelo vocabulário do nicho. Listar o que NÃO coube no menu como
   "desenvolvimento novo" com estimativa em dias — o Felipe decide.
5. QA.md › Modo app, com compra real. Esperar aprovação.

### 5 · ads
Chamar `/adsiniciais` (4 pacotes) com `_brief/` como insumo. Depois `/adsloriem`
para a grade em L (ângulo × container) a partir do pacote vencedor, com as
regras de `references/ads-regras.md`. Entregar DOCX em `_brief/ads/`.
Lembrar ao Felipe: criativo de ângulo específico aponta DIRETO para a página
(`/v1/?p=27`), genérico passa pelo `/go/` — o `sck` separa as duas origens.

### 6 · leitura
`LEITURA.md` sobre `/painel/` (chave em `_STATS_KEY`). Saída fixa: tabela por
célula · dimensão vencedora · cortes · amostra faltante · próximo teste (UMA
variável). Registrar em ESTADO.md e na nota do projeto no vault.

## Ao terminar qualquer etapa
- `ESTADO.md`: marcar `[x]`, `etapa:` N+1, `atualizado:` hoje, decisões.
- Nota do projeto no vault: status de uma linha.
- Dizer ao Felipe em 3 linhas: o que foi feito · o que ele precisa fazer · o próximo `/fabrica`.
