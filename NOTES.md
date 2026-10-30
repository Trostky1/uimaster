# Notes

## Baseline (Step 1)
S1 test suite, run on the untouched copy, command from `.github/workflows/tests.yml`
(`for t in tests/test_*.py; do python3 "$t"; done`, needs `pyyaml`):
7 of 7 test files PASS: components (16 checks), cuj_contract (12), docs, evals (15/15 trigger rank-1), render_html, report_contract (12), safety.
The final plugin must match this: 7 of 7.

## Differences between screenshot and files
- Screenshot: "6 commands, 4 agents". Files: 5 commands (cuj-audit, usability-audit, ux-audit, ux-review, ux-spec) and 3 agents (usability-auditor, cuj-author, cuj-auditor). Trust the files.
- Screenshot also showed skills as slash items (audit-cuj, render-report, spec-cuj, usability-audit, ux-audit). Those are the 5 skills. OK.

## S3 (impeccable) source of truth
- `skill/` is the source: `SKILL.src.md` (template), 41 reference files, 4 agents, scripts.
- 22 harness folders (.claude, .cursor, .gemini, .codex-style, .kiro ...) and `plugin/` are generated copies. We use `skill/` only, plus `plugin/skills/impeccable/SKILL.md` to read the template values resolved.
- `skill/SKILL.src.md` uses `{{scripts_path}}` and `{{command_hint}}`. Resolve these when we write the final files.
- 150 tagged rule IDs (`<!-- rule:... -->`) exist across skill + references. We keep the tags: they make the coverage check exact.
- Engine: a Rust binary (`impeccable`), pinned to ENGINE_VERSION 0.1.18, downloaded by the launcher on first run and checked against `engine-checksums.txt`.
- Hooks (`plugin/hooks/hooks.json`): run `impeccable hook` on SessionStart, after Edit/Write, and on Stop.

## S2 (taste-skill) facts
- Skill name in source: `design-taste-frontend`. Files: SKILL.md (542 lines), 11 references (5,200 lines total), library/ (9 JSON files, 1.7 MB), scripts (Node 22+, Chrome), assets (CSS/JS, scroll scenes).
- `assets.mjs` needs network (open image collections). The other scripts are local.

## Decisions needed from the user (see checkpoint)
D1. Impeccable engine binary + launcher: include or leave out?
D2. Impeccable hooks (run on every edit): ship ON, ship OFF, or leave out?
D3. taste-skill scripts + library (Node, Chrome, 1.7 MB): include?
D4. `live` and `generate` commands (need engine + browser extension): include or defer?
D5. S4 author and license (unknown).
D6. Plugin author name: set to the GitHub login Trostky1. Change it if you want a real name.

## Architecture note (Step 3)
- "Canonical home" in MATRIX.md = a short merged topical file in `skills/uimaster/references/` (the rules that win after conflicts). Deep detail stays in the original S2 and S3 reference files, kept near-verbatim in `skills/taste/references/` and `skills/craft/reference/`, and linked from the topical file. This keeps every rule and its S3 rule tag, and avoids rewriting 10,000 lines by hand.
- S1 skill folders keep their depth (`skills/<name>/`, `scripts/` at the plugin root), so the relative links `../../scripts/...` stay valid. No script path changes are needed.
- Correction: S1 `/ux-review` renders reports. It is not a critique command. `MATRIX.md` and `CONFLICTS.md` are fixed.

## Coverage check (Step 5)
- S1: 57 files identical. Changed on purpose: `skills/README.md` (appended), `skills/usability-audit/SKILL.md` (one added sentence linking the two new lenses), `evals/README.md` and four eval cases (plugin namespace `/ux-agent-skills:` renamed to `/uimaster:`). `agents/README.md` and `commands/README.md` moved to `docs/agents.md` and `docs/commands.md` (Claude Code treats a README in `commands/` as a command).
- S2: all files present. One changed: `skills/taste/SKILL.md` (frontmatter, notes block, the House rules / Laws of the craft / Special cases sections moved to `references/house-rules.md` to stay under 500 lines; text unchanged).
- S3: 3,294 source lines compared. 33 not found, all explained: 13 are my edits (live-mode sentences removed, `/impeccable <cmd>` renamed), 15 are the Codex-only sub-agent permission gate in `critique.md` (Codex mechanics, not design; skipped), 5 are the Codex-tagged design rules in `craft-floor.md` (now kept for all models in an added section). The generated Claude build strips the `<!-- rule:... -->` tags, so the 150 tags cannot be compared. Line coverage replaces the tag check.
- S4: the original body is contained verbatim in `skills/ux-laws/SKILL.md`.
- Not copied on purpose: S1 `tasks/` (its own dev plans), S1 `.github/dependabot.yml`, S3 engine binary and Rust source, S3 live-mode files and agent `impeccable-manual-edit-applier`, S2 `install.sh`.
- Decisions still open: D5 (UX laws author and license), D6 (author name), D4 stays deferred.
