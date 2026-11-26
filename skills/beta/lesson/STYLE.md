# Lesson style

This is the author's style, shipped as the default. Edit it to make lessons look like yours.

The look is a **clean technical document**: white page, navy ink, sand as the one warm highlight.

## File
- One HTML file: inline CSS, inline SVG, a few lines of vanilla JS for the Check answers. No build, no framework. Opens offline and prints well (`@media print`: answers shown).
- Fonts from Google Fonts with a system fallback so it still reads offline: `family=Onest:wght@400;500;600;700&family=Oxanium:wght@600&family=JetBrains+Mono:wght@400;500`.
  - Onest for text and titles (h1 700, h2 600, `letter-spacing:-0.03em`, `text-wrap:balance`). Small titles: h1 `clamp(24px,3.4vw,30px)`, h2 ~20px.
  - Oxanium only for section headings: 12px, 600, uppercase, `letter-spacing:.08em`.
  - JetBrains Mono for code, numbers and data (`tabular-nums`).
- `color-scheme: light` and an explicit `body` background. Light by default; with `--dark`, see [Dark theme](#dark-theme---dark).

## Layout
- One reading column, max 760px, 16px side gutter on phones.
- Title + one-sentence promise, then the ladder sections, then Terms, Check, Sources.
- Section heading = Oxanium heading with a 26px icon in a square tinted with the section colour (`color-mix` 12%, radius 4px).
- Hierarchy comes from thin 1px borders, section colour and type, never from shadows.

## Tokens
| Role | Value |
|---|---|
| Background / subtle | `#FFFFFF` / `#F5F7F9` |
| Ink strong / body / muted / subtle | `#1B2632` / `#263444` / `#4A5D72` / `#677A8E` |
| Line / strong line | `#E3E8ED` / `#CBD3DB` |
| Sand highlight | bg `#FCFAF7`, border `#E6D5C1`, text `#5B4630` |
| Terms accent | `#5A4BD1` on `#ECEAFB` |
| Right / wrong | `#2F8A5B` on `#E3F3EA` · `#B83A31` on `#FBE6E3` |
| Focus | `#3767A8` |
| Radius | `4px` on everything |

Section colours (icon and heading): blue `#3767A8`, amber `#B87A12`, purple `#5A4BD1`, green `#2F8A5B`, teal `#0E7C86`, sand `#8A6A3F`.

## Components
- **Key idea:** the one sand box of the lesson, heading in sand ink.
- **Terms:** term in the purple accent, then the definition.
- **Check:** each option is a full-width button with a 1px strong-line border; the pick turns right/wrong and the reason appears below.
- **Code:** dark block `#0F161E`, text `#D9DFE5`.
- **Bold sparingly:** buttons and labels 500, UI titles 500–600; 700 only on the page title.
- Text only where the visual can't say it: no eyebrows, captions or helper notes the drawing already makes obvious.
- Colour marks a whole element (tinted background, full 1px border, coloured text or icon), never a single coloured side.

## Diagrams
- Inline SVG, drawn for this lesson's example (its names and values), labels inside boxes, arrows that never cross a box.
- Blue `#3767A8` = request/data going out, sand `#C9A96E` = result coming back, red `#B83A31` = attack/error. Same meaning in every diagram.
- Real logos (Simple Icons path inline, brand colour) when the subject is a product; small Lucide icons for generic ideas.

## Dark theme (`--dark`)
Same layout, type, components and colour meanings; only the values change. Dark only on screen: `<meta name="color-scheme" content="dark">`, `color-scheme: dark`, explicit `body` background, no `prefers-color-scheme` switching. Print stays light (`@media print` restores the light tokens), so put every colour in a CSS custom property and use `var(--…)` in CSS and SVG.

| Role | Value |
|---|---|
| Background / subtle / raised | `#0F161E` / `#16202B` / `#1D2936` |
| Ink strong / body / muted / subtle | `#EEF2F6` / `#D3DBE3` / `#9AAABB` / `#7D8FA2` |
| Line / strong line | `#243140` / `#34465A` |
| Sand highlight | bg `#221C14`, border `#5C4A33`, text `#E6D3B8` |
| Terms accent | `#A99FF5` on `#231F45` |
| Right / wrong | `#5BC48C` on `#12301F` · `#F0857B` on `#3A1714` |
| Focus | `#7FA8E6` |

Section colours: blue `#6F9BE0`, amber `#E0A63C`, purple `#A99FF5`, green `#5BC48C`, teal `#3CBAC4`, sand `#C9A26E`. Every text pair passes WCAG AA (4.5:1) on background and subtle.

- Section icon square tint: `color-mix` 18% (12% is too faint on dark).
- Hover and nested surfaces use raised; still no shadows or glows.
- **Code:** block `#0A0F14` with a 1px line border (darker than the page, so the border defines it), text `#D9DFE5`.
- **Diagrams:** boxes fill subtle with a strong-line stroke, labels in body ink, never white boxes. Data out `#6F9BE0`, result back `#C9A96E`, error `#F0857B`.
- **No light hex in SVG.** Every `fill`/`stroke` on text, lines, arrows and boxes is a `var(--…)` (e.g. `fill="var(--ink)"`), never a value from the light table: `#1B2632` or `#263444` text is invisible on the dark page. Only a drawing *of* a screen or pixel (a white app, a lit pixel) may use a fixed colour, and its label still uses `var(--ink)`. Before finishing, grep the SVGs for light-table hex and fix each hit.
- **Logos:** brand colour only if it reads on subtle (≥ 3:1); dark marks (GitHub, Vercel, Next.js, Apple…) use ink strong.
