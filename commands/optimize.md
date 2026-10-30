---
name: optimize
description: "Diagnose and fix UI performance: load, interaction, animation, and bundle size."
argument-hint: "[target]"
---

# /optimize

Thin entry point. The [`craft`](../skills/craft/SKILL.md) skill does the work, using its [optimize.md](../skills/craft/reference/optimize.md) playbook, inside the [`uimaster`](../skills/uimaster/SKILL.md) rules.

## Arguments

`$ARGUMENTS`: the target (a file, route, component, or URL). Omit it to infer the target from the open files or the running app.

## Behavior

1. Parse the target from `$ARGUMENTS`.
2. Load the playbook: [`reference/optimize.md`](../skills/craft/reference/optimize.md).
3. Load [`ux-laws`](../skills/ux-laws/SKILL.md). Pick the mode (Persuade, Operate, Read, Experience) with [modes](../skills/uimaster/references/modes.md).
4. Before any UI edit, read [`craft-floor.md`](../skills/craft/reference/craft-floor.md).
5. Do the work. Finish the job. Verify the render at 360 px and 1440 px.
6. Report what changed, what you decided and why, and what is left.

## Guarantees

- Keeps the existing visual world unless the user asked for a redesign.
- The craft engine is optional and never starts on its own (see the Engine gate in the craft skill).
- When sources disagree, [`CONFLICTS.md`](../CONFLICTS.md) decides.
