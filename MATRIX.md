# Concept matrix

Source key: **S1** UX Agent Skills · **S2** taste-skill · **S3** impeccable · **S4** ux-laws-design.
"Home" = the ONE place the rule lives in the final plugin. Other sources fold into it.

## Rule counts per source (to check coverage in Step 5)
| Source | Units to place |
|---|---|
| S1 | 5 skills, 5 commands, 3 agents, 6 heuristic/contract references (NN/g 10, Shneiderman 8, AI design, NPCIS 5 dimensions, report contract, CUJ contract), 4 scripts, 7 test files, evals |
| S2 | SKILL.md run (10 steps), 18 house rules, laws of the craft, tells registry (8 groups, about 50 tells), 14-pass critique + score + caps, 11 references, 9 library JSON files, 6 scripts, assets |
| S3 | SKILL.md (4 modes, 23 commands, routing), 41 references, 4 agents, 150 tagged rules, craft floor (Verify 9 checks + Refuse list), engine + hooks |
| S4 | 20 laws (3 repeated names: Hick x2, Fitts x2, Postel x2), 8 implementation requirements, 1 conflict rule |

## Topic table
| # | Topic | Canonical home (in uimaster) | S1 | S2 | S3 | S4 |
|---|---|---|---|---|---|---|
| 1 | UX laws (20) + 8 implementation requirements + conflict rule | `skills/ux-laws/SKILL.md` | — | — | — | all 20, all 8 |
| 2 | Usability heuristics (NN/g 10, Shneiderman 8, AI design, NPCIS) | `skills/usability-audit/references/` (S1 files unchanged) + new lens `ux-laws.md` | 4 files | — | critique heuristic scoring folds in | laws as a 5th lens |
| 3 | Design context and mode choice (Persuade / Operate / Read / Experience) | `skills/uimaster/references/modes.md` | — | page vs app split | modes, init, PRODUCT.md, DESIGN.md | goal first (req 1) |
| 4 | Art direction run: argument, direction, idea, one live thing | `skills/taste/SKILL.md` + `references/` | — | steps 1-10 | new-work, shape | Hick: 1 purpose |
| 5 | Visual style, tells and bans (anti-"AI slop") | `skills/craft/references/bans-and-tells.md` | — | tells registry, house rules | craft-floor Refuse list | Prägnanz |
| 6 | Typography | `skills/craft/references/type.md` | — | type.md | typeset, craft-floor type | Miller (chunking) |
| 7 | Colour and contrast | `skills/craft/references/colour.md` | — | colour.md | colorize, craft-floor | Von Restorff |
| 8 | Layout, spacing, rhythm | `skills/craft/references/layout.md` | — | layout.md | layout | Proximity, Connectedness, Similarity |
| 9 | Motion and feedback | `skills/craft/references/motion.md` | — | motion.md, scenes.md | animate, overdrive, craft-floor motion | Doherty 400 ms |
| 10 | Interaction states, forms, errors, edge cases | `skills/craft/references/states-forms.md` | auth-handoff | — | harden, clarify | Postel x2, defaults, Parkinson |
| 11 | Accessibility | `skills/craft/references/accessibility.md` + dependency `web-quality-skills` | wraps accessibility | — | audit | Fitts (targets) |
| 12 | Responsive and native (iOS, Android) | `skills/craft/references/responsive.md`, `ios.md`, `android.md` | — | layout phone | adapt, ios, android | Fitts |
| 13 | Copy and microcopy | `skills/craft/references/copy.md` | — | copy.md | clarify | Peak-End |
| 14 | Imagery and pictures | `skills/taste/references/imagery.md` | — | imagery.md, assets.mjs | visualize | — |
| 15 | App screens / Operate surfaces | `skills/taste/references/app-screens.md` + `craft/references/operate.md` | — | app-screens.md | operate, mode-operate, component-review | Jakob |
| 16 | Flows: onboarding, progress, completion | `skills/craft/references/flows.md` | CUJ | — | onboard, delight | Zeigarnik, Goal-gradient, Peak-End, Serial position |
| 17 | Critical user journeys (spec + replay) | `skills/spec-cuj`, `skills/audit-cuj` (S1 unchanged) | all | — | — | — |
| 18 | Design critique (look at the render) | `skills/usability-audit/references/design-critique.md` (new, merges S2 14 passes + S3 critique) | — | critique.md | critique.md | — |
| 19 | Technical audit (a11y, perf, responsive) | `skills/ux-audit` (S1) + `craft/references/audit-checks.md` | roll-up | inspect/lint rules | audit, optimize | — |
| 20 | Audit reports (schema, HTML) | `skills/usability-audit/references/report-contract.md`, `skills/render-report` (S1 unchanged) | all | — | — | — |
| 21 | Polish and finishing | commands `/polish`, `/distill`, `/bolder`, `/quieter`, `/delight`, `/overdrive` | — | step 9-10 | polish and siblings | Peak-End |
| 22 | Design system capture (tokens, DESIGN.md) | commands `/design-init`, `/design-document`, `/design-extract` | — | — | init, document, extract | Similarity |
| 23 | Agent and machine readability | `skills/ux-audit` (humans and agents) + Verify block | plugin theme | — | — | — |
| 24 | Safety: audits write only under `.ux/` | S1 `audit_safety.py` (unchanged) | yes | — | — | — |
| 25 | Live variants in browser (`live`, `generate`) | DEFERRED (decision D4) | — | — | live, generate | — |

## Commands (final target list)
- S1 kept, names unchanged: `/cuj-audit` `/usability-audit` `/ux-audit` `/ux-review` `/ux-spec`
- From S3 (thin command files that load one reference): `/shape` `/polish` `/distill` `/bolder` `/quieter` `/harden` `/onboard` `/animate` `/colorize` `/typeset` `/layout` `/delight` `/overdrive` `/clarify` `/adapt` `/optimize`
- S3 `critique` -> new thin command `/critique` (runs agent `design-critic` + skill `usability-audit` with the new `design-critique.md` lens). S3 `audit` -> folded into `/ux-audit`.
- S1 `/ux-review` renders existing `.ux/audits` reports to HTML (it is the S1 front door of `render-report`). It is NOT a critique command. Unchanged.
- S3 `init` `document` `extract` -> `/design-init` `/design-document` `/design-extract` (prefix avoids the S1 name space and `init`).
- S3 `craft` and `teach`: dropped (S3 marks `craft` deprecated, `teach` is an alias of `init`).
- New: `/design` (end-to-end run).
- Deferred: `live`, `generate` (D4).

## Agents (final target list)
- S1 kept: `usability-auditor` `cuj-author` `cuj-auditor`
- S3 kept: `impeccable-asset-producer`, `impeccable-documenter`, `impeccable-finish-reviewer` (craft references call it by name; `design-critic` is the broader new persona). `impeccable-manual-edit-applier` needs live mode: deferred (D4). Final count: 7 agents.
- New: `design-critic` (read-only: Read, Grep, Glob) uses `ux-laws` + `taste` + `craft`.
