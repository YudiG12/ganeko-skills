#!/usr/bin/env bash
# Copies the skills into ~/.claude/skills and runs video-lesson's one-time setup. Safe to re-run.
# usage: scripts/install.sh [skill ...]   (default: every skill in skills/beta)
set -euo pipefail
R="$(cd "$(dirname "$0")/.." && pwd)"; DEST="${CLAUDE_SKILLS_DIR:-$HOME/.claude/skills}"
skills=("$@"); [ ${#skills[@]} -eq 0 ] && skills=($(ls "$R/skills/beta"))
mkdir -p "$DEST"
for s in "${skills[@]}"; do
  [ -d "$R/skills/beta/$s" ] || { echo "no skill named $s"; exit 1; }
  rsync -a --exclude node_modules "$R/skills/beta/$s/" "$DEST/$s/"; echo "installed $s → $DEST/$s"
done
[ -d "$DEST/video-lesson" ] && "$DEST/video-lesson/scripts/setup.sh"
echo "done: open Claude Code and type /lesson <concept>"
