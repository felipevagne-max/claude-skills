# Prompt — como escrever o plano

O prompt de vídeo tem duas metades que **não podem se misturar**: o que é estável
(identidade, cenário) e o que se transforma (câmera, ação, tempo). Misturar as duas
é a causa mecânica do rosto derretendo entre frames.

---

## O esqueleto

```
[IDENTIDADE]
Descritores visíveis e estáticos. Copiar e colar IDÊNTICO entre planos.
Marcadores visíveis — roupa, corpo, postura, cabelo. Nunca nome próprio,
nunca idade, nunca atributo não observável.

[CENA]
Lugar, hora, e a luz nomeada com FONTE e QUALIDADE.
"single hard side-light from a window, half the face in shadow" — não "boa iluminação".

[CÂMERA]
Camera: <nome exato do preset>      ← uma linha, UM movimento

[LENTE]
mm + abertura escolhidos pelo propósito do plano (ver camera.md)
+ trava de foco se for insert ou close fechado

[AÇÃO]
1 ação principal + no máximo 2 secundárias. O que MUDA, não o que existe.

[NEGATIVOS]
Só os constraints do defeito que ESTE plano corre risco de ter (ver defeitos.md)
```

**Por que marcador visível e não nome:** "Jack, 42 anos, executivo" não sobrevive à
regeneração — nada disso é visível. "Homem de casaco de lã cinza, barba de três dias,
ombros caídos" sobrevive, porque o modelo pode desenhar cada pedaço.

---

## Exemplo — plano de vilão

```
A man in a charcoal wool overcoat, three-day stubble, shoulders squared,
standing in an empty parking garage at night.

Single hard sodium-vapor light from a fixture above and behind him;
half his face in shadow, sharp falloff, wet concrete catching the light.

Camera: Dolly In

85mm, F1.4. Focus plane locked on his face from first frame to last —
no focus drift, no rack focus, no autofocus hunting.

He does not move. Only his jaw tightens; his breath fogs once in the cold air.

Natural skin texture, subtle imperfections. Anatomically correct.
```

Cinco planos com esse mesmo vilão? Os blocos IDENTIDADE e CENA vão **literais** nos
cinco; só CÂMERA e AÇÃO mudam.

---

## Imagem → vídeo (i2v)

O erro clássico: o prompt re-descreve a imagem que já foi enviada, e o clipe sai
praticamente parado.

**Descrever só o que MUDA.** A imagem já diz como as coisas são.

```bash
higgsfield generate create kling3_0 \
  --prompt "Camera: Dolly In. Her eyes lift to meet the lens. Dust drifts through the light beam." \
  --start-image ./canonica.png --mode pro --aspect_ratio 9:16 --duration 5 --wait
```

Somar sempre **movimento de câmera explícito** + **movimento atmosférico**
(poeira, vapor, tecido, fumaça, chuva) — é o que tira o clipe do congelamento.

`--start-image` + `--end-image` no `kling3_0` = interpolação entre dois quadros.
É o jeito de controlar exatamente onde o plano começa e termina.

---

## Referência: colocar o SEU produto ou a SUA pessoa na cena

**Só o Seedance tem `image_references`.** O Kling aceita quadro de partida e de
chegada, não um conjunto.

```bash
higgsfield generate create seedance_2_0 \
  --prompt "..." \
  --image ./frasco.png --image ./rotulo-detalhe.png \
  --resolution 480p --duration 5 --wait
```

Limites: 9 imagens (contando start/end), 3 vídeos, 3 áudios, 12 no total.

⚠️ **A referência vem INTEIRA.** Ela carrega junto o enquadramento, o carimbo e os
defeitos da foto original — não só o assunto. Referência com produto de lado entrega
produto de lado. Recortar a região que importa antes de mandar.

⚠️ **Peça pronta como referência de estilo carrega o DADO dela.** Reusar um clipe
anterior como referência traz os números, o texto e a marca daquele clipe junto.

---

## Multi-shot

`seedance_2_0` / `seedance_2_5` aceitam `multi_shots` + `multi_prompt` — várias cenas
encadeadas num job só. **O schema da CLI não lista esses campos**; eles aparecem no
`params` de um job executado. Se for tentar, tentar e conferir o retorno — não assumir.

O caminho garantido continua sendo: **N clipes de 5s + ffmpeg**. Custa igual (o preço é
linear na duração), dá controle de corte por plano, e cada plano falha sozinho em vez
de derrubar a sequência inteira.

---

## Gênero, no Seedance

`--genre` aceita `action / horror / comedy / noir / drama / epic` (ou `auto`).
Muda grading, ritmo e escolha de movimento sem gastar tokens do prompt com isso.

---

## Áudio

- `kling3_0` — `sound on/off`, ambiente genérico.
- `seedance_2_0` — `generate_audio` + `audio_references[]` (exige pelo menos uma
  imagem ou vídeo junto).
- `veo3_1` — o melhor quando tem **gente falando**: áudio sincronizado com a boca.
  Duração só 4, 6 ou 8s. Usar `quality=high` (custa igual ao basic).

Trilha, mixagem e legenda de verdade: **ffmpeg**, depois.

---

## O que NUNCA vai no prompt

Texto legível, logo, tarja, marca, corte, junção, legenda e watermark.
O modelo **re-sintetiza, nunca preserva** — vai reescrever o texto errado, redesenhar
a marca e reenquadrar o corte. Tudo isso é **camada por cima, no ffmpeg**:

```bash
# legenda / logo sobre o clipe
ffmpeg -i clipe.mp4 -i logo.png -filter_complex "overlay=W-w-40:40" out.mp4

# concatenar a sequência
printf "file '%s'\n" plano*.mp4 > lista.txt
ffmpeg -f concat -safe 0 -i lista.txt -c copy teaser.mp4
```

---

## Enriquecer prompt de graça

O enhancer do `product-photoshoot` **lê a imagem de referência** e devolve prompt
estruturado. Custa **0**. Serve de rascunho para qualquer modelo:

```bash
higgsfield product-photoshoot create --mode product_shot \
  --prompt "..." --image ./ref.png --enhance-only --json | jq -r '.prompts[0].prompt'
```

⚠️ Só o `--enhance-only`. Executar o `product-photoshoot` com produto que já existe
**redesenha o rótulo** — ele trata a referência como inspiração de estilo.
