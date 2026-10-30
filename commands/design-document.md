---
name: design-document
description: "Generate DESIGN.md from the shipped code: tokens, components, and the visual decisions already in use. Runs the documenter agent."
argument-hint: "[target]"
---

# /design-document

Thin entry point. The [`craft`](../skills/craft/SKILL.md) skill does the work with its [document.md](../skills/craft/reference/document.md) playbook.

## Behavior

1. Load [`reference/document.md`](../skills/craft/reference/document.md) and follow it.
2. Derive the design system from the shipped artifact, not from intentions. Use the [`impeccable-documenter`](../agents/impeccable-documenter.md) agent when sub-agents are available.
3. Report what changed and what is left.

## Guarantees

- The craft engine is optional. It is downloaded only if the user agrees. Until then the skill reads `PRODUCT.md` and `DESIGN.md` directly.
- When sources disagree, [`CONFLICTS.md`](../CONFLICTS.md) decides.
