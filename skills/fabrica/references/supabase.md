# Supabase — como rodar o schema sem psql
```bash
TOK=$(security find-generic-password -s "Supabase CLI" -w | sed 's/^go-keyring-base64://' | base64 -d)
REF=mwedjbufjmdeakvaiokp   # olimpo-system (consolidar no existente — regra minimalizar custos)
python3 -c "import json,sys;print(json.dumps({'query':open('sql/schema.sql').read()}))" \
 | curl -s -X POST "https://api.supabase.com/v1/projects/$REF/database/query" \
   -H "Authorization: Bearer $TOK" -H "Content-Type: application/json" --data-binary @-
```
- Conferir: `select relname from pg_class where relname like '<slug>_%'`.
- Anon key do projeto vai em `shared/track.js` (A.k) e `app/dados.js` (SB_ANON) — já é a do olimpo-system; trocar se o projeto for outro.
- Advisor engana; corte de 1.000 linhas no REST (paginar na RPC).
- Service key: `supabase projects api-keys --project-ref $REF`.
