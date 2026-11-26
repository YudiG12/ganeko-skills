<p align="center"><a href="https://www.youtube.com/@yudiganeko"><img src="docs/assets/banner.png" alt="ganeko-skills: atomic Claude Code skills I actually use. A project by Yudi Ganeko" width="100%"></a></p>

<p align="center"><img alt="Claude Code" src="https://img.shields.io/badge/Claude_Code-skills-D97757?style=flat-square&labelColor=1B2632&logo=claude&logoColor=white"> <img alt="Status beta" src="https://img.shields.io/badge/status-beta-B87A12?style=flat-square&labelColor=1B2632"> <img alt="Remotion" src="https://img.shields.io/badge/video-Remotion-5A4BD1?style=flat-square&labelColor=1B2632"> <img alt="Kokoro" src="https://img.shields.io/badge/voice-Kokoro_(local)-0E7C86?style=flat-square&labelColor=1B2632"> <a href="LICENSE"><img alt="MIT license" src="https://img.shields.io/badge/license-MIT-8A6A3F?style=flat-square&labelColor=1B2632"></a></p>

<p align="center"><a href="README.md">English</a></p>

**Skills atômicas do Claude Code que eu uso de verdade**: cada uma faz um trabalho só, pra você encaixar no seu fluxo e mudar do seu jeito. Open source por padrão; serviço pago é opção, nunca obrigação.

<p align="center"><img src="docs/assets/hld-light.png" alt="You run /lesson in Claude Code and get lesson.html; /video-lesson reads it, makes the voice and the animated scene, and outputs video.html" width="720"></p>

> Tudo aqui está em **beta**: eu uso todo dia e ainda muda toda semana. Nomes e arquivos podem mudar.

## Instalar

Precisa de Claude Code, Python 3.10+, Node 18+ e ffmpeg.

```sh
git clone https://github.com/YudiG12/ganeko-skills && cd ganeko-skills
scripts/install.sh            # ou: scripts/install.sh lesson
```

Ou peça pro seu agente de IA:

```txt
Clona https://github.com/YudiG12/ganeko-skills e instala as skills pra mim, seguindo o AGENTS.md.
```

## Como usar

```txt
/lesson o que é um eval
/video-lesson o-que-e-um-eval
/video-lesson https://hamel.dev/blog/posts/evals/ --tts elevenlabs --voice <voice-id>
```

Tudo vai pra `./lessons/<slug>/`: `lesson.html`, depois `video.mp4` e `video.html`.

| Skill | O que gera |
|---|---|
| [`lesson`](skills/beta/lesson) | Uma aula em HTML: mapa no topo, do problema real até o nome técnico, termos, perguntas e fontes primárias. |
| [`video-lesson`](skills/beta/video-lesson) | Um vídeo narrado e animado de ~4 min de qualquer conceito ou origem (um tema, um link, um PDF ou um `lesson.html`), mais uma página de teatro com capítulos e marcadores de conceito. |

Cada skill traz um `STYLE.md` com o meu estilo como padrão. Edite e o resultado fica com a sua cara.

## Exemplo

Gerado com `/lesson o que é um eval` e depois `/video-lesson`. Sem edição manual.

<table><tr>
<td width="50%"><img src="docs/assets/example-lesson.png" alt="lesson.html: a map of the eval loop up top, the video embedded, then the scenario of a support-ticket classifier"></td>
<td width="50%"><img src="docs/assets/example-video.gif" alt="video-lesson: a 50-case dataset runs through the prompt and a grader, scoring 45/50"></td>
</tr><tr>
<td align="center"><code>lesson.html</code></td>
<td align="center"><code>video.mp4</code> (14 s de 4 min)</td>
</tr></table>

## Arquitetura

| Tema | Como | Decisão |
|---|---|---|
| Um trabalho por skill | `lesson` escreve, `video-lesson` filma qualquer origem; o `lesson.html` é uma entrada possível | [ADR 001](docs/adr/001-atomic-skills.md) |
| Maturidade | Tudo começa em `skills/beta/` | [ADR 002](docs/adr/002-beta-folder.md) |
| Voz | Kokoro local por padrão; qualquer narrador é um `tts/<nome>.py` | [ADR 003](docs/adr/003-open-source-by-default.md) |
| Sincronia | Tempo de cada palavra pelo faster-whisper, então a animação segue qualquer voz | [ADR 003](docs/adr/003-open-source-by-default.md) |

```
skills/beta/
  lesson/          SKILL.md · STYLE.md
  video-lesson/    SKILL.md · STYLE.md · engine/ (Remotion) · tts/ · scripts/ · template/ · example/
scripts/install.sh
```

## Links

[ADRs](docs/adr) · [Changelog](CHANGELOG.md) · [Contributing](CONTRIBUTING.md) · [AGENTS.md](AGENTS.md) · Licença MIT. A `video-lesson` renderiza com [Remotion](https://www.remotion.dev/license), grátis pra pessoa física e empresas de até 3 pessoas. Fontes: SIL OFL 1.1. Voz: [Kokoro-82M](https://huggingface.co/hexgrad/Kokoro-82M), Apache 2.0.
