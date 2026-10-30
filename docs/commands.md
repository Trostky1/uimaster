# Slash commands

**Slash commands** (`commands/*.md`) — user-facing entry points. *The when.*

Each Markdown file becomes a `/ux-agent-skills:<name>` command that invokes a persona
or skill on demand. Keep them thin — a command wires a user request to the workflow
that does the work.

## Commands here

- [`usability-audit.md`](../commands/usability-audit.md) — `/ux-agent-skills:usability-audit`: run the
  usability auditor against one target.
- [`ux-audit.md`](../commands/ux-audit.md) — `/ux-agent-skills:ux-audit`: the suite roll-up. Default fans
  out to usability + accessibility + cuj; web-performance is opt-in (`--only`/`--all`).
- [`ux-spec.md`](../commands/ux-spec.md) — `/ux-agent-skills:ux-spec`: interview the user to author
  critical user journeys under `.ux/cujs/` and regenerate the host `SPEC.md` index.
- [`cuj-audit.md`](../commands/cuj-audit.md) — `/ux-agent-skills:cuj-audit`: replay the stored journeys
  and report the step that broke.
- [`ux-review.md`](../commands/ux-review.md) — `/ux-agent-skills:ux-review`: render existing `.ux/audits`
  reports into self-contained HTML (findings as cards, screenshots as a walk-through flipbook,
  the roll-up as a dashboard).

## Added by uimaster (23 commands)
Build and refine: `/design`, `/shape`, `/polish`, `/distill`, `/bolder`, `/quieter`, `/harden`, `/onboard`, `/animate`, `/colorize`, `/typeset`, `/layout`, `/delight`, `/overdrive`, `/clarify`, `/adapt`, `/optimize`.
Evaluate: `/critique`.
Design system and maintenance: `/design-init`, `/design-document`, `/design-extract`, `/design-hooks`, `/design-doctor`.
