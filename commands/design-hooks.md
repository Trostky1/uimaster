---
name: design-hooks
description: Turn the optional edit-time design checks on or off for this project. Off by default.
argument-hint: "[status|on|off|reset]"
---

# /design-hooks

Thin entry point. The [`craft`](../skills/craft/SKILL.md) skill does the work with its [hooks.md](../skills/craft/reference/hooks.md) playbook.

## Behavior

1. Load [`reference/hooks.md`](../skills/craft/reference/hooks.md) and follow it.
2. Default action is `status`. Turning hooks on needs the craft engine and the user's clear yes. Say what will run on each edit before you enable it.
3. Report what changed and what is left.

## Guarantees

- The craft engine is optional. It is downloaded only if the user agrees. Until then the skill reads `PRODUCT.md` and `DESIGN.md` directly.
- When sources disagree, [`CONFLICTS.md`](../CONFLICTS.md) decides.
