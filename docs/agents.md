# Personas

**Personas** (`agents/*.md`) — roles with a perspective and an output format. *The who.*

Each file defines a subagent with a point of view (e.g. a senior UX auditor) and a
structured way of reporting. Drop one Markdown file per persona in this directory.

The heuristics a persona's reviews cite live beside the skill that loads them, in
[`../skills/usability-audit/references/`](../skills/usability-audit/references/), to keep
that skill self-contained.

## Personas here

- [`usability-auditor.md`](../agents/usability-auditor.md) — senior UX auditor; evaluates against
  Nielsen / Shneiderman / AI-heuristics / NPCIS and emits a 0–4 severity report. Driven by
  the [`usability-audit`](../skills/usability-audit/SKILL.md) skill.
- [`cuj-author.md`](../agents/cuj-author.md) — UX researcher who defines critical user journeys by
  interview, and **refuses vague ones** (no "the user", no unobservable outcomes, no invented
  steps). Driven by the [`spec-cuj`](../skills/spec-cuj/SKILL.md) skill.
- [`cuj-auditor.md`](../agents/cuj-auditor.md) — the inverse of the usability auditor: holds **no
  heuristics and no opinions**. The journey file is the whole rubric; it reports whether each
  step happened, and which one broke. Driven by the
  [`audit-cuj`](../skills/audit-cuj/SKILL.md) skill.

## Added by uimaster
- [`design-critic`](../agents/design-critic.md) — read-only design director. Judges the render with the UX laws, the craft floor, and the critique passes.
- [`impeccable-documenter`](../agents/impeccable-documenter.md) — records `DESIGN.md` from the shipped build (from impeccable, Apache 2.0).
- [`impeccable-asset-producer`](../agents/impeccable-asset-producer.md) — produces raster assets from an approved comp (from impeccable). Needs the craft engine and image generation.
- [`impeccable-finish-reviewer`](../agents/impeccable-finish-reviewer.md) — reviews a finished build against its direction (from impeccable).
