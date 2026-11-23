# ADR 001: Atomic skills

| Status | Date | Deciders |
|---|---|---|
| Accepted | 2026-11-23 | Yudi Ganeko |

## Context
Bundled workflows (one plugin that runs a whole process) are hard to adapt: people take all of it or none. The private `explainer` skill did script, voice, scene, render and a personal course page in one.

## Decision
- **One job per skill.** `lesson` writes a lesson; `video-lesson` turns a lesson into a video.
- **Skills meet at files, not calls.** `video-lesson` films any source; a `lesson.html` is one input among others, never a requirement.
- **Every skill is user-invoked** (`disable-model-invocation: true`): zero context load, and the expensive ones never fire on their own.

## Alternatives considered
| Option | Why not |
|---|---|
| One `explainer` skill end to end | Can't use the lesson without the video, or swap one step |
| Model-invoked skills | Permanent context cost and unpredictable firing |

## Consequences
People compose the skills in their own flow. Each new skill must stand alone and read/write plain files.
