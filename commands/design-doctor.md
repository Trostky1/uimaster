---
name: design-doctor
description: Report and repair drift between this project's design files (PRODUCT.md, DESIGN.md, .impeccable config) and the installed craft version. Also the opt-in step for the craft engine.
argument-hint: "[check|install]"
---

# /design-doctor

Thin entry point. The [`craft`](../skills/craft/SKILL.md) skill does the work with its [doctor.md](../skills/craft/reference/doctor.md) playbook.

## Behavior

1. Load [`reference/doctor.md`](../skills/craft/reference/doctor.md) and follow it.
2. This is maintenance, not design. Do not redesign anything. To install the engine, explain the one-time download (checksum verified) and get a yes first.
3. Report what changed and what is left.

## Guarantees

- The craft engine is optional. It is downloaded only if the user agrees. Until then the skill reads `PRODUCT.md` and `DESIGN.md` directly.
- When sources disagree, [`CONFLICTS.md`](../CONFLICTS.md) decides.
