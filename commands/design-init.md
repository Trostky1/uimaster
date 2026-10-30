---
name: design-init
description: Capture durable product context in PRODUCT.md so every later design step starts from the same facts.
argument-hint: "[product or surface]"
---

# /design-init

Thin entry point. The [`craft`](../skills/craft/SKILL.md) skill does the work with its [init.md](../skills/craft/reference/init.md) playbook.

## Behavior

1. Load [`reference/init.md`](../skills/craft/reference/init.md) and follow it.
2. Ask only for facts you cannot infer. Write `PRODUCT.md`. Do not set up live mode (not included).
3. Report what changed and what is left.

## Guarantees

- The craft engine is optional. It is downloaded only if the user agrees. Until then the skill reads `PRODUCT.md` and `DESIGN.md` directly.
- When sources disagree, [`CONFLICTS.md`](../CONFLICTS.md) decides.
