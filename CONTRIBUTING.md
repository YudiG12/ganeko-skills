# Contributing

## Development

```sh
scripts/install.sh                                   # install your working copy
~/.claude/skills/video-lesson/scripts/review.sh lessons/<slug>
docs/render.sh                                       # README images
```

## How changes are made

- Open an issue first for a new skill or a change in a skill's steps.
- Run the skill end to end on a real concept before opening the PR, and attach the output (a screenshot of `lesson.html` or a link to the video).
- Keep each skill atomic and open source by default ([ADR 001](docs/adr/001-atomic-skills.md), [ADR 003](docs/adr/003-open-source-by-default.md)).
