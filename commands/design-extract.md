---
name: design-extract
description: Pull reusable tokens and components out of a codebase into a design system.
argument-hint: "[target]"
---

# /design-extract

Thin entry point. The [`craft`](../skills/craft/SKILL.md) skill does the work with its [extract.md](../skills/craft/reference/extract.md) playbook.

## Behavior

1. Load [`reference/extract.md`](../skills/craft/reference/extract.md) and follow it.
2. Extract only patterns used in more than one place. Keep names from the codebase.
3. Report what changed and what is left.

## Guarantees

- The craft engine is optional. It is downloaded only if the user agrees. Until then the skill reads `PRODUCT.md` and `DESIGN.md` directly.
- When sources disagree, [`CONFLICTS.md`](../CONFLICTS.md) decides.
