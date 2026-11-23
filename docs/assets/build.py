"""Writes the README images' sources: banner.html and hld.html, each with a light and a dark theme
(?theme=dark). Render with docs/render.sh; the README uses the light ones.
Style: the author's brand book (navy + sand, 1px borders, 4px corners, Onest / Oxanium)."""
import json, os
D = os.path.dirname(os.path.abspath(__file__))
B = json.load(open(os.path.join(D, "..", "architecture", "brands.json")))
L = {
 "book": '<path d="M4 19.5A2.5 2.5 0 0 1 6.5 17H20V3H6.5A2.5 2.5 0 0 0 4 5.5z"/><path d="M8 7h8M8 11h6"/>',
 "clapper": '<path d="M20.2 6 3 11l-.9-2.4c-.3-1.1.3-2.2 1.3-2.5l13.5-4c1.1-.3 2.2.3 2.5 1.3Z"/><path d="m6.2 5.3 3.1 3.9M12.4 3.4l3.1 4"/><path d="M3 11h18v8a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2Z"/>',
 "file": '<path d="M15 2H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V7Z"/><path d="M14 2v4a2 2 0 0 0 2 2h4"/><path d="M10 13H8M16 17H8M16 13h-2"/>',
 "mic": '<path d="M12 2a3 3 0 0 0-3 3v7a3 3 0 0 0 6 0V5a3 3 0 0 0-3-3Z"/><path d="M19 10v2a7 7 0 0 1-14 0v-2M12 19v3"/>',
 "play": '<rect x="2" y="4" width="20" height="16" rx="2"/><path d="m10 9 5 3-5 3z"/>',
 "search": '<circle cx="11" cy="11" r="7"/><path d="m20 20-3.5-3.5"/>',
 "sparkles": '<path d="M9.94 15.5A2 2 0 0 0 8.5 14.06l-6.14-1.58a.5.5 0 0 1 0-.96L8.5 9.94A2 2 0 0 0 9.94 8.5l1.58-6.14a.5.5 0 0 1 .96 0L14.06 8.5a2 2 0 0 0 1.44 1.44l6.14 1.58a.5.5 0 0 1 0 .96l-6.14 1.58a2 2 0 0 0-1.44 1.44l-1.58 6.14a.5.5 0 0 1-.96 0z"/>',
}
def ic(n, c, z):
    if n in B: return f'<svg viewBox="0 0 24 24" width="{z}" height="{z}"><path d="{B[n]}" fill="{c}"/></svg>'
    return f'<svg viewBox="0 0 24 24" width="{z}" height="{z}" fill="none" stroke="{c}" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">{L[n]}</svg>'
HEAD = '''<!doctype html><html><head><meta charset="utf-8">
<link href="https://fonts.googleapis.com/css2?family=Onest:wght@400;500;600;700;800&family=Oxanium:wght@600&family=JetBrains+Mono:wght@500&display=swap" rel="stylesheet">
<script>if (location.search.includes("theme=dark")) document.documentElement.dataset.theme = "dark";</script>
<style>
:root{--bg:#FFFFFF;--line:#E3E8ED;--line2:#CBD3DB;--ink:#1B2632;--muted:#4A5D72;--subtle:#677A8E;--arrow:#677A8E;
 --sand-bg:#FCFAF7;--sand-line:#E6D5C1;--sand-ink:#5B4630;--sand:#8A6A3F;
 --tag-bg:#ECEAFB;--tag-line:#CFC9F5;--tag:#5A4BD1;--bezel:#1B2632;--screen:#E8EEF4;--bar:#CBD3DB;--base:#C3CBD3}
[data-theme=dark]{--bg:#0D1117;--line:#30363D;--line2:#3D4752;--ink:#F0F3F6;--muted:#B6C1CC;--subtle:#8E9DAD;--arrow:#8E9DAD;
 --sand-bg:#1A1712;--sand-line:#5B4630;--sand-ink:#E6D5C1;--sand:#C9A77F;
 --tag-bg:#1C1838;--tag-line:#3D3480;--tag:#A99BFF;--bezel:#4A5866;--screen:#E8EEF4;--bar:#CBD3DB;--base:#8E9DAD}
*{box-sizing:border-box;margin:0}body{background:var(--bg);font-family:Onest,sans-serif;color:var(--ink)}
.eb{font-family:Oxanium;font-weight:600;font-size:13px;letter-spacing:.08em;text-transform:uppercase;color:var(--subtle)}
.tile{display:flex;align-items:center;justify-content:center;border-radius:4px;flex:none}
.nm{position:absolute;width:200px;text-align:center;font-weight:700;font-size:17px;color:var(--ink);letter-spacing:-.01em}
.cmd{font-family:"JetBrains Mono",monospace;font-weight:500}
</style></head><body>'''
def tile(n, c, s, i): return f'<div class="tile" style="width:{s}px;height:{s}px;background:color-mix(in srgb,{c} 14%,var(--bg))">{ic(n, c, i)}</div>'

# ---------- banner 1280 x 364 ----------
cl = [("book", "#3767A8", "/lesson"), ("clapper", "#5A4BD1", "/video-lesson")]
rows = "".join(f'<div style="display:flex;align-items:center;gap:12px">{tile(n, c, 40, 20)}<span class="cmd" style="font-size:17px">{l}</span></div>' for n, c, l in cl)
tags = "".join(f'<span style="font-size:13px;font-weight:600;padding:4px 9px;border-radius:4px;background:var(--tag-bg);color:var(--tag);border:1px solid var(--tag-line)">{t}</span>' for t in ["Claude Code", "Remotion", "Kokoro", "faster-whisper", "MIT"])
SUBS = "120K"  # YouTube subscribers, update when it grows
banner = HEAD + f'''<div style="width:1280px;height:364px;position:relative;border:1px solid var(--line);border-radius:4px;background:var(--bg);overflow:hidden">
<div style="position:absolute;left:64px;top:54px;width:660px">
 <div style="font-weight:800;font-size:62px;line-height:1.02;letter-spacing:-.03em">ganeko-skills</div>
 <div style="font-size:21px;color:var(--muted);margin-top:14px;line-height:1.35">Atomic Claude Code skills I actually use.<br>Open, free, and adaptable to your workflow.</div>
 <div style="display:flex;gap:8px;margin-top:22px;align-items:center">{ic("claude", "#D97757", 26)}{tags}</div>
</div>
<div style="position:absolute;left:800px;top:98px;display:flex;flex-direction:column;gap:30px">{rows}</div>
<svg style="position:absolute;left:1000px;top:96px" width="60" height="110" fill="none" stroke="var(--line2)" stroke-width="1.5">
 <path d="M4 22 C34 22 26 56 56 56"/><path d="M4 92 C34 92 26 56 56 56"/></svg>
<div style="position:absolute;left:1060px;top:84px;width:170px;height:134px;border:1px solid var(--sand-line);background:var(--sand-bg);border-radius:4px;display:flex;flex-direction:column;align-items:center;justify-content:center;gap:8px">
 {tile("sparkles", "#B08A5A", 50, 26)}<div style="font-weight:700;color:var(--sand-ink);font-size:16px">Your workflow</div>
 <div style="font-size:12.5px;color:var(--sand)">one skill per job</div></div>
<div style="position:absolute;left:0;right:0;bottom:0;height:64px;border-top:1px solid var(--line);background:var(--sand-bg);display:flex;align-items:center;gap:12px;padding:0 64px">
 <img src="avatar.jpg" style="width:36px;height:36px;border-radius:50%;object-fit:cover;border:1px solid var(--sand-line)">
 <span style="font-size:15px;color:var(--muted)">A project by <b style="color:var(--ink);font-weight:700">Yudi Ganeko</b> · software engineer, code and dev careers</span>
 <span style="margin-left:auto;display:flex;align-items:center;gap:8px;font-size:15px;color:var(--muted)"><svg width="26" height="19" viewBox="0 0 18 13"><rect width="18" height="13" rx="3" fill="#E5322D"/><path d="M7 3.5v6l5-3z" fill="#fff"/></svg><b style="color:var(--ink);font-weight:700">{SUBS}</b> subscribers on YouTube</span>
</div>
</div></body></html>'''
open(os.path.join(D, "banner.html"), "w").write(banner)

# ---------- high-level design 1200 x 500 ----------
def sq(cx, cy, n, c, name, s=104):
    return (f'<div style="position:absolute;left:{cx-s/2}px;top:{cy-s/2}px;width:{s}px;height:{s}px;border:1px solid var(--line2);border-radius:4px;background:color-mix(in srgb,{c} 12%,var(--bg));display:flex;align-items:center;justify-content:center">{ic(n, c, 50)}</div>'
            f'<div class="nm" style="left:{cx-100}px;top:{cy+s/2+12}px">{name}</div>')
mac = '''<svg width="170" height="112" viewBox="0 0 170 112"><rect x="22" y="4" width="126" height="84" rx="6" fill="var(--bezel)"/><rect x="28" y="10" width="114" height="72" rx="2" fill="var(--screen)"/>
<rect x="36" y="18" width="46" height="5" rx="1" fill="var(--bar)"/><rect x="36" y="28" width="70" height="4" rx="1" fill="var(--bar)"/><rect x="36" y="36" width="60" height="4" rx="1" fill="var(--bar)"/><rect x="36" y="44" width="66" height="4" rx="1" fill="var(--bar)"/>
<rect x="36" y="56" width="28" height="18" rx="2" fill="#D97757" opacity=".85"/><path d="M4 92 H166 L160 104 Q158 107 154 107 H16 Q12 107 10 104 Z" fill="var(--base)"/><rect x="72" y="92" width="26" height="4" rx="2" fill="var(--bezel)" opacity=".4"/></svg>'''
M = '<defs><marker id="a" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto"><path d="M0 0L10 5L0 10z" style="fill:var(--arrow)"/></marker></defs>'
hld = HEAD + f'''<div style="width:1200px;height:500px;position:relative;background:var(--bg)">
<div style="position:absolute;left:290px;top:110px;width:880px;height:300px;border:1px dashed var(--line2);border-radius:4px"></div>
<div style="position:absolute;left:308px;top:124px;display:flex;align-items:center;gap:8px" class="eb">{ic("claude", "#D97757", 18)}<span>Claude Code</span></div>
<svg style="position:absolute;left:0;top:0" width="1200" height="500">{M}
<g fill="none" style="stroke:var(--arrow)" stroke-width="1.8" marker-end="url(#a)">
 <path d="M222 260 H330"/><path d="M442 260 H510"/><path d="M622 260 H690"/><path d="M802 260 H870"/><path d="M982 260 H1046"/></g></svg>
<div style="position:absolute;left:52px;top:204px">{mac}</div><div class="nm" style="left:37px;top:324px">You</div>
{sq(386, 260, "book", "#3767A8", "/lesson")}{sq(566, 260, "file", "#2F8A5B", "lesson.html")}{sq(746, 260, "clapper", "#5A4BD1", "/video-lesson")}{sq(926, 260, "mic", "#0E7C86", "Voice + scene")}{sq(1100, 260, "play", "#8A6A3F", "video.html")}
</div></body></html>'''
open(os.path.join(D, "hld.html"), "w").write(hld)
