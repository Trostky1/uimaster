# Dry run: a pricing section

A test of the plugin workflow on a small pricing section (plain HTML). `before.html` is the generic version a model builds by default. `after.html` follows the uimaster rules.

| Check | Before | After |
|---|---|---|
| taste `lint.mjs` | 17 FAIL, 10 WARN | 0 FAIL, 0 WARN |
| taste `inspect.mjs` | 14 FAIL, 8 WARN | 3 FAIL, 2 WARN (page-level gates; see below) |

What changed: no eyebrow, no gradient text, no emoji icons, no glass, no glow, no shadows at rest. The headline says what the product charges for. One recommended plan with the one strongest button. Real status in words. Buttons are at least 44 px high with a visible focus ring. Reduced motion is respected. Prices are labelled as illustrative.

The 3 remaining FAILs (few pictures, still page, off-centre) are page-level gates. They measure a whole page, and this is one section. The audit-checks reference now says so ("Single sections and components").

Method note: this run used the plugin's own tools (taste lint and inspector, with Chrome). The audit skills (`/ux-audit`) need a live agent session with the plugin installed, so they were not run here. Screenshots: `before.jpg`, `after.jpg` (desktop and tablet widths side by side).
