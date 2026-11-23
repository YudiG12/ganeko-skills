# AGENTS.md

## Installing the skills for someone

```sh
scripts/install.sh            # every skill; or name them: scripts/install.sh lesson
```

- It copies each skill to `~/.claude/skills/<name>` and, for `video-lesson`, runs `scripts/setup.sh` (Python venv at `~/.cache/video-lesson/venv` with kokoro + faster-whisper, `npm install` in `engine/`).
- Check first: `python3 --version` (3.10+), `node --version` (18+), `ffmpeg -version`. If one is missing, tell the person how to install it; don't install system packages yourself.
- ElevenLabs is optional. If they want it, they set `ELEVENLABS_API_KEY` in their own shell profile. **Never ask for the key in chat or write it to a file.**
- When it finishes, tell them to open Claude Code and run `/lesson <concept>`.

## Working on the skills

- Write and edit skills with the `writing-for-agents` principles: small `SKILL.md`, steps with completion criteria, reference pushed to `STYLE.md` or other files behind a pointer.
- Decisions are ADRs in `docs/adr/`.
- Test a change by running the skill end to end on a real concept; for `video-lesson`, `scripts/review.sh` must exit 0.
- README images: edit `docs/assets/build.py`, run `docs/render.sh`, open every PNG before committing.
