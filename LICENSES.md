# Licenses of bundled sources

| Source | Author | License | Copyright line | What we must do |
|---|---|---|---|---|
| S1 UX Agent Skills 0.6.0 | Carl Sziebert | MIT | Copyright (c) 2026 Carl Sziebert | Keep the copyright line and the MIT text. |
| S2 taste-skill 2.1.5 | Leonxlnx | MIT | Copyright (c) 2026 Leonxlnx | Keep the copyright line and the MIT text. |
| S3 impeccable | Paul Bakaus | Apache 2.0 | Copyright 2025 Paul Bakaus | Keep the LICENSE text and NOTICE. State every change we make to impeccable files. Keep the attribution to ehmo (see below). |
| S3 sub-source: platform-design-skills (ios.md, android.md) | ehmo | MIT | see https://github.com/ehmo/platform-design-skills | Keep the notice from impeccable NOTICE.md. |
| S4 ux-laws-design | unknown (supplied by the user) | not stated | none in file | Ask the user for the author and license before any public release. |

## Rules for this plugin
- Original text written for uimaster (master skill, router, glue, `/design`, `design-critic`): MIT.
- Each bundled component keeps its own license. Files copied from S3 keep the Apache 2.0 header and carry a "Modified by uimaster" line when changed.
- Full license texts go in `licenses/` (one file per source) in the final plugin.

## Changes made to impeccable files (Apache 2.0, section 4)
All files under `skills/craft/` and the three `agents/impeccable-*.md` files come from the impeccable Claude plugin build (`plugin/skills/impeccable/` and `plugin/agents/`). uimaster changed them as follows:
- `skills/craft/SKILL.md`: renamed `impeccable` to `craft`; new description and argument hint; added a notes block; added an engine gate to Setup step 1; removed the `craft`, `live`, and `generate` command rows and the `teach` and `craft` alias line; pointed the `audit` row at `/ux-audit`.
- `skills/craft/reference/`: removed `live.md`, `live-setup.md`, `generate.md`, `craft.md`; removed the sentences that pointed to `live.md` in `typeset.md`, `colorize.md`, `layout.md`, `init.md`; changed every `/impeccable <command>` to the matching uimaster command name.
- `skills/craft/scripts/`: removed the live-mode browser files (`live-browser*.js`, `modern-screenshot.umd.js`). The launcher, checksums, and data files are unchanged.
- `agents/impeccable-*.md`: changed the path `skills/impeccable` to `skills/craft`.
Each changed file keeps its original header. Original license text: `licenses/LICENSE-impeccable-Apache-2.0`. Original notice: `licenses/NOTICE-impeccable.md`.
