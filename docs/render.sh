#!/usr/bin/env bash
# Regenerates the README images (banner, HLD) and renders them to PNG at 2x with headless Chrome.
set -euo pipefail
cd "$(dirname "$0")"
CHROME="${CHROME:-/Applications/Google Chrome.app/Contents/MacOS/Google Chrome}"
shot() { "$CHROME" --headless=new --disable-gpu --hide-scrollbars --force-device-scale-factor=2 --virtual-time-budget=4000 --window-size="$2,$3" --screenshot="$PWD/$4" "file://$PWD/$1" 2>/dev/null; }
python3 assets/build.py
shot assets/banner.html 1280 364 assets/banner.png
shot assets/hld.html 1200 500 assets/hld-light.png
echo "rendered; now open every PNG and check it"
