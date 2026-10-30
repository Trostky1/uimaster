# AGENTS.md

Instructions for AI agents working **on this repo** (changing the plugin). If you only use the plugin, read [README.md](README.md).

## Layers
- Agents (`agents/*.md`): who. A point of view and an output format. No workflow.
- Skills (`skills/<name>/SKILL.md`): how. Steps, exit criteria, own `references/`.
- Commands (`commands/*.md`): when. Thin: parse arguments, call a skill, nothing more.

Components are found by convention from `agents/`, `skills/*/SKILL.md`, and `commands/`. `plugin.json` holds metadata and `dependencies` only.

## Where things come from
- `skills/usability-audit`, `ux-audit`, `spec-cuj`, `audit-cuj`, `render-report`, `scripts/`, `tests/test_*.py` (except `test_uimaster.py`), `evals/`: UX Agent Skills. Do not rename them. Their tests check names and wording.
- `skills/taste`: tasteskill v2. `skills/craft` and `agents/impeccable-*`: impeccable. `skills/ux-laws`: user supplied.
- `skills/uimaster`, `commands/design*.md`, `commands/critique.md`, `agents/design-critic.md`, `skills/usability-audit/references/{ux-laws,design-critique}.md`: original to this plugin.

## Rules the tests enforce
1. Every `skills/*/SKILL.md` needs `evals/cases/<skill>.json`: 3 or more positive triggers, 2 or more negative triggers, 1 or more behavioral eval. Routing must rank each positive prompt within `top_k`.
2. Relative links in the files listed in `tests/test_docs.py` must resolve. `README.md` must keep the terms the test checks.
3. `tests/test_uimaster.py` checks the merged structure: names, counts, all 20 laws, link integrity of new files, no live-mode leftovers.
4. Audits write only under `.ux/` (`scripts/audit_safety.py`).

## Run the tests
```bash
python3 -m pip install pyyaml
for t in tests/test_*.py; do python3 "$t" || echo "FAIL $t"; done
```

## When you add or change a rule
Add it to `MATRIX.md` (home) and, if it disagrees with another source, to `CONFLICTS.md` with the winner and the reason.
