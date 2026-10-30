---
name: critique
description: Design critique of the rendered result. Scores hierarchy, composition, type, colour, and substance, then lists the top fixes. Runs the design-critic persona with the usability-audit skill.
argument-hint: "[target] [--scope <area>]"
---

# /critique

Judge the **render**, not the code. Thin entry point. The [`usability-audit`](../skills/usability-audit/SKILL.md) skill does the work with its [design critique](../skills/usability-audit/references/design-critique.md) and [UX laws](../skills/usability-audit/references/ux-laws.md) lenses. The [`design-critic`](../agents/design-critic.md) persona gives the point of view.

## Arguments

`$ARGUMENTS`: a URL or a file path, and an optional `--scope`. Omit to infer from the running dev server or open files.

## Behavior

1. Resolve one stable target (prefer a source path over a dev-server URL).
2. Take screenshots at 1440, 768, and 390 px. Ask before starting a server or navigating.
3. Run the two isolated assessments (design review and tool evidence) as described in the design critique lens. If you cannot isolate them, start the report with the DEGRADED banner.
4. File findings in the `usability-audit` report contract under `.ux/audits/`. Name the pass or law in each finding.
5. Print the top three fixes, most visible first, and the report path. Ask what to improve next. The question is the last thing in the reply.

## Guarantees

- Findings only. Never edits host application code.
- Writes only under `.ux/audits/`.
- When sources disagree, [`CONFLICTS.md`](../CONFLICTS.md) decides.
