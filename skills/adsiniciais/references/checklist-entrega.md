# Checklist de Entrega

Rode inteiro antes de exportar. Reporte ao Felipe apenas o que **nao** passou.

---

## 1. Espinha dorsal (contamina tudo)

- [ ] O vilao e **um so** nas 20 pecas — resumivel em uma unica frase de acusacao
- [ ] O mecanismo tem **nome proprio** e ele aparece nos 4 corpos
- [ ] A inversao (frase de 1 linha) aparece em pelo menos 1 hook de cada pacote
- [ ] A promessa nunca vira garantia — compliance do nicho respeitado

## 2. Sub-personas

- [ ] 5 portas por pacote, cada uma com **sintoma proprio, frase propria e
      falsa-explicacao propria**
- [ ] Nenhuma falsa-explicacao demolida duas vezes dentro do mesmo pacote
- [ ] Os nomes das portas sao concretos, nao categorias vagas
      (bom: "O Refem do Cliente" · ruim: "O Insatisfeito")

## 3. Moldes

- [ ] Nenhum molde repetido dentro do mesmo pacote
- [ ] Pacote 3 abre com afirmacao, nunca com pergunta
- [ ] Pacote 4 contem pelo menos um hook que batiza o vilao com "Isso tem nome."
- [ ] Pacote 4 contem a Historia de Origem — ou `[LACUNA]` marcada

## 4. Arco da Resposta

Em **cada um dos 20 hooks**:
- [ ] Batida 2 (ABSOLVICAO) presente
- [ ] Batida 4 (VILAO) presente
- [ ] Batida 7 (VIRADA SUSPENSA) presente
- [ ] O metodo/produto **nao** foi entregue no hook
- [ ] O expert nao acusa o lead (excecao: molde 21, com absolvicao na frase seguinte)

## 5. Prova

- [ ] Todo numero de autoridade veio do brief — **nenhum inventado**
- [ ] Cada pacote tem pelo menos 2 provas numericas distintas
- [ ] Zero adjetivo-autoridade sozinho ("renomado", "referencia", "experiente")
- [ ] Lacunas marcadas como `[LACUNA: ...]` no proprio DOCX

## 6. Estrutura do pacote

- [ ] 5 hooks + **1 CORPO** + **1 CTA** por pacote — corpo e CTA nao variam por hook
- [ ] Corpo cumpre as 5 batidas (credencial tripla · padrao · tres alternativas ·
      vilao+mecanismo · reorganizacao)
- [ ] CTA cumpre as 5 batidas (ponte · convite com data/hora · tres negacoes ·
      tres entregas · instrucao fisica)
- [ ] CTA vende o **evento**, nao o produto. Preco nao aparece
- [ ] Data/hora reais — ou `[DATA]` / `[HORA]` marcados
- [ ] Instrucao fisica do link condiz com o destino real

## 7. Comprimento

| Bloco | Faixa |
|---|---|
| Hook P1 | 150–255 |
| Hook P2 | 165–225 |
| Hook P3 | 185–250 |
| Hook P4 | 190–260 |
| CORPO | 200–290 |
| CTA | 90–165 |

- [ ] Todos os blocos dentro da faixa

Conferir com:
```bash
python3 - <<'EOF'
import subprocess, re, os, glob
for f in sorted(glob.glob(os.path.expanduser('~/Downloads/[Projeto]-Criativos/*.docx'))):
    t = subprocess.run(['pandoc','-t','plain',f],capture_output=True,text=True).stdout
    for p in re.split(r'\n(?=HOOK|CORPO|CTA)', t):
        w = len(p.split())
        if w > 40:
            print(f"{os.path.basename(f)[:9]} | {p.strip().splitlines()[0][:32]:34} {w}")
EOF
```

## 8. Registro e voz

- [ ] Vocabulario B2C e B2B nao se misturaram
- [ ] O expert e chamado como o publico realmente o chama
- [ ] Frases transportaveis usadas 2–3x por pacote, nao em todos os hooks
- [ ] Perguntas do Pacote 1 e comentarios do Pacote 2 vieram de **frases reais do
      dossie**, nao inventadas
- [ ] Handles do Pacote 2 soam reais e dizem algo sobre a pessoa

## 9. Anti-IA

- [ ] Zero "nao se trata apenas de", "em um mundo onde", "mais do que nunca"
- [ ] Zero adjetivos empilhados
- [ ] Paragrafos de 1 a 4 linhas, quebrados por respiracao
- [ ] Oralidade brasileira presente ("ta", "pra", "me acompanha", "sabe por que?")
- [ ] Ha fragmentos sem verbo e repeticoes deliberadas — a fala nao e simetrica
- [ ] Leia um hook em voz alta mentalmente: soa como gente falando?

## 10. Arquivo

- [ ] 4 DOCX em `~/Downloads/[Projeto]-Criativos/`
- [ ] Sem negrito, italico ou bullet dentro da copy
- [ ] Copy falada entre aspas
- [ ] Direcao de cena `[Nome olha pra camera e fala:]` **apenas** no Pacote 3
- [ ] Numeros de impacto por extenso quando abrem frase ("95 por cento")
- [ ] Cabecalho de cada arquivo: `[PROJETO] — PACOTE N` + nome do pacote

## 11. Fechamento

- [ ] Nota do projeto atualizada em `~/Obsidian/Brain/Projetos/`
- [ ] Memoria salva com lacunas pendentes (data, link, numero faltando)
- [ ] Resumo entregue ao Felipe: caminho + `20 pecas · 4 pacotes · vilao: [X]` +
      lista de lacunas
