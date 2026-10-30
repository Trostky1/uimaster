---
name: uimaster
description: "Master workflow for building, redesigning, or improving any user interface: landing pages, marketing sites, dashboards, app screens, forms, settings, onboarding, and flows. Combines 20 UX laws, art direction, design craft, and audits in one run. Use for 'build a landing page', 'design this screen', 'make this UI look better', 'redesign my dashboard', 'fix the layout and spacing', 'this looks generic', 'make it feel premium', 'improve the user experience of this form'."
user-invocable: true
argument-hint: "[what to design or improve] [target file or URL]"
license: MIT
---

# uimaster

One workflow for all UI work. It joins four sources: UX laws (`ux-laws`), art direction (`taste`), design craft (`craft`), and audits (`ux-audit`, `usability-audit`, `spec-cuj`, `audit-cuj`, `render-report`). This file is the router. It loads only what the task needs.

## When this skill applies

Use it for any task that builds, changes, reviews, or critiques a UI, layout, page, component, form, dashboard, or flow. Do not use it for backend-only work.

## The run

Do the steps in order. Say each decision in one line. Do not stop to ask unless a missing fact blocks the work (for example, no product name).

1. **State the goal.** Write the user's primary goal and the one action the screen must support. (`ux-laws` item 1 of Implementation Requirements.)
2. **Pick the mode.** Choose from the surface, not the product: Persuade, Operate, Read, or Experience. Read [modes](references/modes.md). The mode decides which skills load next.
3. **Read the project.** Find the stack (HTML/CSS, React, Next.js, Vue, Svelte, Astro, Tailwind) and follow its idioms. Read `PRODUCT.md` and `DESIGN.md` if they exist. If they do not exist, and the work is a new surface, run `/design-init`. Inspect the existing look before you edit.
4. **Load the rules.**
   - Always: [ux-laws](../ux-laws/SKILL.md).
   - Persuade or Experience: run the [taste](../taste/SKILL.md) steps (argument, direction, idea). Read [bans-and-tells](references/bans-and-tells.md).
   - Operate or Read: read [operate](references/operate.md) and `../taste/references/app-screens.md`. Do NOT deal a new direction. Use familiar patterns.
5. **Load topic files only as the task needs.** Use the table below.
6. **Read the craft floor.** Before any UI edit, read `../craft/reference/craft-floor.md`. This includes small edits.
7. **Build.** Finish the job. No placeholders except assets the user must supply.
8. **Verify the render.** Look at the result at 360 px and 1440 px. Batch the checks in one look. Use the Verify list below.
9. **Audit.** Run `/ux-audit` for the report in `.ux/audits/`. Run `/critique` for a design critique. Read [audit-checks](references/audit-checks.md).
10. **Fix every finding** at severity 3 or higher. Record the rest.
11. **Report.** Say what changed, what you decided and why, what you did not do, and what the user must do next.

## Topic files

| Sub-task | Read |
|---|---|
| Choosing the mode | [modes](references/modes.md) |
| Type: sizes, measure, fonts | [type](references/type.md) |
| Colour, contrast, themes | [colour](references/colour.md) |
| Layout, spacing, cards, radius | [layout](references/layout.md) |
| Motion and feedback | [motion](references/motion.md) |
| Forms, states, errors, edge cases | [states-forms](references/states-forms.md) |
| Accessibility | [accessibility](references/accessibility.md) |
| Responsive and native | [responsive](references/responsive.md) |
| Words on the screen | [copy](references/copy.md) |
| Multi-step flows, onboarding, ending | [flows](references/flows.md) |
| App UI, dashboards, tools | [operate](references/operate.md) |
| What to avoid | [bans-and-tells](references/bans-and-tells.md) |
| Checking the result | [audit-checks](references/audit-checks.md) |

Each topic file gives the winning rule. Each one links to the deep source file. Read the deep file when the task needs depth.

## Which command to run

| Need | Command |
|---|---|
| Full run on a request | `/design` |
| Plan before code | `/shape` |
| Final quality pass | `/polish` |
| Better typography, colour, layout | `/typeset` `/colorize` `/layout` |
| Bolder or calmer look | `/bolder` `/quieter` `/distill` `/overdrive` `/delight` |
| Motion | `/animate` |
| Edge cases and errors | `/harden` |
| First-run flow and empty states | `/onboard` |
| Words | `/clarify` |
| Other screen sizes | `/adapt` |
| Speed | `/optimize` |
| Design critique of the render | `/critique` |
| Full UX audit with report | `/ux-audit` (also `/usability-audit`) |
| Critical user journeys | `/ux-spec` to write, `/cuj-audit` to replay |
| Report to HTML | `/ux-review` |
| Design system files | `/design-init` `/design-document` `/design-extract` |

## Rules when sources disagree

Priority: (a) accessibility, clarity, task completion, user control; (b) the 20 UX laws and the audit skills; (c) craft; (d) taste. The full list of 17 rulings is in `../../CONFLICTS.md`. The ones you will meet most:

- The user's brief overrides taste defaults. It never overrides accessibility or a line marked as a ban in `craft-floor.md`.
- Direction drawing is for pages that persuade or showcase. App UI uses familiar patterns.
- Real multi-step flows show progress ("Step 2 of 4"). Decorative numbering stays banned.
- Destructive actions need a confirmation. Needless modals stay banned.
- Every interaction gets feedback in 400 ms. Decorative motion stays limited to one authored moment.

## Verify (run on the built result)

- Text contrast 4.5:1 (3:1 for large text). Visible focus. Full keyboard path.
- Touch targets 44x44 px or more.
- Loading, empty, error, and success states exist, with real words.
- Checked at 360 px and 1440 px. No overflow. Real copy at every width.
- `prefers-reduced-motion` respected.
- One primary action per section. The next step is obvious.
- The flow ends with a clear completion state.

## Safety and folders

- Audits write only under `.ux/`. Taste writes under `.taste-skill/`. Craft writes `PRODUCT.md`, `DESIGN.md`, and `.impeccable/`.
- Nothing runs by itself. The craft engine download, the edit hooks, and the taste picture search run only when the user asks. See `/design-doctor` and `/design-hooks`.
- Never invent claims, logos, quotes, or numbers. Label illustrative values.
