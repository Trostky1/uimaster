# Checking the result

Passing a meter proves nothing banned was measured. It does not prove the design is good. Look at the render. (taste, impeccable)

## Tools and what each one is for
| Tool | What it does | Runs when | Needs |
|---|---|---|---|
| `/ux-audit` | Full UX audit: usability, accessibility, and CUJ auditors. Writes one contract report each plus a go/no-go roll-up to `.ux/audits/`. Web performance is opt-in. | You ask | Nothing extra. The `web-quality-skills` dependency adds the WCAG and performance auditors. |
| `/usability-audit` | Heuristic evaluation: NN/g 10, Shneiderman 8, AI design heuristics, NPCIS, plus the UX laws and design-critique lenses. Severity 0-4. | You ask | Nothing extra. |
| `/critique` | Design critique of the render: design review plus tool evidence, scored. | You ask | A browser for live targets. |
| `/cuj-audit` | Replays a stored journey step by step. Names the step that broke. | You ask | A running app. |
| taste `inspect.mjs`, `lint.mjs`, `scenes.mjs` | Measure the page in a real browser at 1440, 768, 390 px. Lint source for banned patterns. | You run them | Node 22+ and Chrome. |
| craft engine (`detect`, hooks) | Mechanical checks: contrast, overflow, broken images, banned patterns. | Only after you opt in (`/design-doctor`, `/design-hooks on`) | The downloaded engine. |

## Order of checks
1. Mechanical checks (inspector or engine), if installed. Fix every FAIL.
2. Look at the screenshots at every viewport. Open every one. Critique them.
3. Run `/ux-audit`. Fix findings at severity 3 or 4. Record the rest.
4. Re-run the failed check. Look again. Three rounds at most.

## Avoid double reporting (C17)
Two detectors can flag the same defect. Report each finding once, with its source. Do not run both detectors as blocking gates at the same time. Use the taste inspector for page house rules on Persuade pages. Use the craft engine for generic mechanical checks.

## Motion count (C18)
The taste inspector fails a page with fewer than eight moving elements. The craft floor asks for one authored motion moment and warns against identical entrances on every section. For Persuade pages, follow taste but vary the entrances and keep one signature move. For Operate and Read pages, treat the taste motion-count FAIL as a WARN. Feedback on every control is required either way (C7).

## Single sections and components (found in the dry run)
The taste inspector's page-level gates (few pictures, no footage, still page, focal point on the first screen, off-centre) measure a whole page. A pricing section, a card, or a form is a fragment. For a fragment: run `lint.mjs`, check the render at 360 and 1440 px, and run `/ux-audit`. Treat the page-level inspector FAILs as out of scope and say so in the report. Do not add pictures or motion to a fragment only to pass them.

## What "done" means
- Zero FAIL on the final version, checked at 360 and 1440 px.
- Every screenshot opened after the last change.
- A stranger can say in five seconds what this is and what to do.
- Every state exists. Contrast and keyboard checks pass.
- The report says what changed, what was decided, and what is left.

## Deep detail
`../../ux-audit/SKILL.md` · `../../usability-audit/SKILL.md` · `../../usability-audit/references/design-critique.md` · `../../taste/references/critique.md` · `../../craft/reference/critique.md` · `../../craft/reference/audit.md`
