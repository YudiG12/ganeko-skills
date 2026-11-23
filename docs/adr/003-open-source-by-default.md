# ADR 003: Open source by default

| Status | Date | Deciders |
|---|---|---|
| Accepted | 2026-11-23 | Yudi Ganeko |

## Context
The private version narrated with ElevenLabs and took word times from its API. A public skill can't require an account or a paid plan.

## Decision
- **Narrator is a flag:** `--tts <name>` runs `tts/<name>.py` (script.json in, voice.wav out). Default `kokoro` (Kokoro-82M, Apache 2.0, local); `elevenlabs` ships as the paid example.
- **Word times come from forced alignment** with faster-whisper (MIT), so `at('phrase')` works with any narrator.
- **Remotion stays** for rendering in beta. It is not open source (free for individuals and companies up to 3 people); the README says so.
- **Personal assets stay out:** the author's voice, licensed sound effects, episodes and course pages.

## Alternatives considered
| Option | Why not |
|---|---|
| ElevenLabs required | Locks users into a vendor and a bill |
| Motion Canvas / Revideo (MIT) | Rewriting the animation kit costs weeks; revisit if users ask |

## Consequences
First run downloads the Kokoro and Whisper models. Sound effects are off until the user adds their own files.
