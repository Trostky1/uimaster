---
name: design
description: End-to-end design run for any UI request. Picks the mode, loads the UX laws, art direction, and craft rules, builds, verifies the render, audits, and fixes. With no argument it shows the command menu.
argument-hint: "[what to design or improve] [target]"
---

# /design

The full run. Thin entry point. The [`uimaster`](../skills/uimaster/SKILL.md) skill does the work.

## Arguments

`$ARGUMENTS`: what to design or improve, and an optional target file or URL.

## Behavior

1. With no argument, show the "Which command to run" table from the `uimaster` skill. Do not run anything.
2. Otherwise follow the run in the skill: goal, mode, project, rules, build, verify, audit, fix, report.
3. Use [`ux-laws`](../skills/ux-laws/SKILL.md) on every run. Use [`taste`](../skills/taste/SKILL.md) for Persuade and Experience surfaces only.

## Guarantees

- Nothing runs by itself: no engine download, no hooks, no picture search.
- Audits write only under `.ux/`.
- When sources disagree, [`CONFLICTS.md`](../CONFLICTS.md) decides.
