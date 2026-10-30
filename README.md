# UIMaster

One plugin for all UI work. It merges four works into one system:

| Part | What it gives you | Source |
|---|---|---|
| **UX laws** | 20 laws (Hick, Fitts, Jakob, Miller, Doherty, Postel, Zeigarnik, Peak-End, and more) with 8 implementation requirements | `ux-laws-design` (user supplied) |
| **Art direction** | Researched directions, a no-slop house style, a real-browser inspector, a look-and-fix loop | [taste-skill](https://github.com/Leonxlnx/taste-skill) (MIT) |
| **Design craft** | 16 refine and build playbooks, the craft floor, modes, DESIGN.md capture | [impeccable](https://github.com/pbakaus/impeccable) (Apache 2.0) |
| **Audits** | Heuristic usability audit, suite roll-up, critical user journeys, HTML reports | [UX Agent Skills](https://github.com/carlsz/ux-agent-skills) (MIT) |

## Use it

Just ask for UI work: "build a landing page for…", "redesign this dashboard", "this looks generic", "fix the spacing". The `uimaster` skill starts on its own. It picks a mode, loads the UX laws, loads art direction or app-screen rules, builds, checks the render, and audits.

Or run `/design [what to design] [target]`. With no argument it shows the command menu.

## Install

Claude Code (tested with the `claude plugin` commands). Add the dependency's marketplace first, then this one:
```
/plugin marketplace add addyosmani/web-quality-skills
/plugin marketplace add Trostky1/uimaster
/plugin install uimaster
```
The plugin depends on `web-quality-skills` (WCAG and performance auditors for `ux-audit`). `marketplace.json` allows that one cross-marketplace dependency. If the dependency marketplace is not added, the install stops with a clear message.

claude.ai or Cowork: upload `uimaster.zip` in Plugins. If the dependency is not available there, `ux-audit` runs a built-in reduced accessibility checklist and says so.

## Commands (28)

| Command | Job | From |
|---|---|---|
| `/design` | Full run on any UI request | uimaster |
| `/shape` | Plan UX and UI before code | impeccable |
| `/polish` `/distill` `/bolder` `/quieter` `/delight` `/overdrive` | Refine the look | impeccable |
| `/typeset` `/colorize` `/layout` | Fix type, colour, spacing | impeccable |
| `/animate` | Purposeful motion | impeccable |
| `/harden` `/onboard` `/clarify` `/adapt` `/optimize` | Edge cases, first run, words, devices, speed | impeccable |
| `/critique` | Design critique of the render | taste + impeccable + UX laws |
| `/ux-audit` | Full UX audit roll-up with go/no-go | UX Agent Skills |
| `/usability-audit` | Heuristic evaluation, static, live, or hybrid mode | UX Agent Skills |
| `/ux-spec` `/cuj-audit` | Write critical user journeys; replay them | UX Agent Skills |
| `/ux-review` | Render `.ux/audits` reports to HTML | UX Agent Skills |
| `/design-init` `/design-document` `/design-extract` | PRODUCT.md, DESIGN.md, tokens | impeccable |
| `/design-hooks` `/design-doctor` | Optional edit checks and engine setup (off by default) | impeccable |

## Skills (9) and agents (7)

Skills: `uimaster` (router), `ux-laws`, `taste`, `craft`, `usability-audit`, `ux-audit`, `spec-cuj`, `audit-cuj`, `render-report`.
Agents: `usability-auditor`, `cuj-author`, `cuj-auditor`, `design-critic`, `impeccable-documenter`, `impeccable-asset-producer`, `impeccable-finish-reviewer`.

## Audits and the report contract

Every audit writes the same shared report contract under `.ux/audits/` in your project. The `usability-audit` skill evaluates in **static** mode (read source), **live** mode (drive the running app), or **hybrid** mode (both). It records the mode actually used. Audits are findings-only: they never edit your app code and never write outside `.ux/`. Journeys are stored in `.ux/cujs/`. See [`SPEC.md`](SPEC.md) and the [report contract](skills/usability-audit/references/report-contract.md).

## When sources disagree

Priority: accessibility, clarity, task completion, user control; then the UX laws and the audit skills; then craft; then taste. All 18 rulings are in [`CONFLICTS.md`](CONFLICTS.md). Examples: art-direction "deal a new look" runs only for pages that persuade, not for app UI; real flows show "Step 2 of 4"; destructive actions get a confirmation; every interaction gets feedback in 400 ms.

## Safety: nothing runs by itself

- The craft engine (a signed-checksum binary that the launcher downloads once) is **off** until you run `/design-doctor`.
- Edit hooks are **off**. `hooks/hooks.json` is empty. Turn them on with `/design-hooks on`.
- The taste scripts (Node 22+, Chrome) and its picture search run only when called.
- Live variant mode and the `generate` command from impeccable are **not included**.

## Project folders

| Folder | Written by |
|---|---|
| `.ux/` | audits and CUJs |
| `.taste-skill/` | art direction run, inspector output |
| `.impeccable/`, `PRODUCT.md`, `DESIGN.md` | craft |

## Files in this repo

[`MATRIX.md`](MATRIX.md) (where every rule lives) · [`CONFLICTS.md`](CONFLICTS.md) · [`NOTES.md`](NOTES.md) · [`LICENSES.md`](LICENSES.md) · [`ATTRIBUTION.md`](ATTRIBUTION.md)

## License

Original parts: MIT. Bundled parts keep their own licenses (MIT, Apache 2.0). See [`LICENSES.md`](LICENSES.md). The author and license of the UX laws file are not yet confirmed.
