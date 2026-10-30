# Conflicts and decisions

Priority: (a) accessibility, clarity, task completion, user control (S4 rule) → (b) S4 laws and S1 → (c) S3 impeccable → (d) S2 taste-skill.
"Conditional" = the losing rule stays, with a stated condition.

| # | Conflict | Winner | Decision |
|---|---|---|---|
| C1 | **Novelty vs familiar patterns.** S2 deals a "researched direction" for every build and says: adopt it, never use the familiar layout. S4 Jakob's Law says use conventions. S3 says Operate and Read surfaces need native expectations. | S4 + S3 | S2 direction-dealing is CONDITIONAL: runs only for Persuade and Experience surfaces. Operate and Read follow Jakob + S3 `operate.md` + S2 `app-screens.md`. |
| C2 | **Decide vs ask.** S2: "decide and state your reading in one line; ask only if a missing fact blocks." S1 `spec-cuj`: interview one question at a time. | Both, by context | Building a UI: decide, state the reading. Authoring CUJs: interview (S1 unchanged). |
| C3 | **Section/step numbering.** S2 bans "01 / 02 / 03" and "Step 2" everywhere. S4 Zeigarnik and Goal-gradient require visible progress in multi-step flows. | S4 | Ban stays for decorative section markers. Functional progress ("Step 2 of 4", progress bar) in a real flow is REQUIRED. |
| C4 | **Border radius.** S2 tells: "one medium radius (12-16px) on everything" is a tell; choose square or fully round. S3 Codex rule: "card radii stay at 12-16px". | Neither absolute | Rule: choose the radius ONCE per system, from the brand world (S4 Similarity). No fixed number. |
| C5 | **Cards.** S3: cards are lazy, nested cards always wrong. S2: no rows of identical icon cards. S4 Uniform Connectedness: containers show relation. | S4 (conditional) | Cards allowed when each card is a distinct entity (a record, a plan, a product). Banned as the page structure. Nested cards stay banned. |
| C6 | **Modals.** S3 bans a modal for tasks that need no interruption. S4 requires a warning before risky or destructive action. | S4 | Confirmation dialog REQUIRED for destructive or irreversible actions. S3 ban stays for everything else. |
| C7 | **Decorative motion vs feedback.** S2/S3: one authored motion moment; no hover lift on every card; no fade on every section. S4 Doherty: acknowledge every action within 400 ms. | S4 | Functional feedback (press, loading, success, error) on EVERY interaction. Decorative motion stays limited to one authored moment. `prefers-reduced-motion` always honored. |
| C8 | **Headline length.** S2: headlines two lines or fewer, about five words. S4 clarity. | S4 | Keep S2 limit unless the headline must say what the product is. Then add a short sentence under it. Never cut meaning to fit. |
| C9 | **Status chips and dots.** S2 bans pill badges and decorative status dots. S4 says show state. | S4 | Functional status (error, success, live, beta where real) allowed and labelled with text. Decorative badges stay banned. |
| C10 | **Monospace / tabular.** S2 bans mono outside code. S3 bans mono as "technical" costume but allows data and measurement. | S3 | Mono allowed for code, data, measurement. Banned as a style label. Tabular figures always in tables. |
| C11 | **Borders and thin rules.** S2 bans all thin rules and 1px boxes (except tables, forms, `data-ui`). S4 Proximity: prefer spacing over borders. S2 `app-screens.md` allows quiet borders in app UI. | S2 app rules | Marketing pages: no hairlines. App screens: quiet borders allowed. Tables and form fields always allowed. |
| C12 | **Routing.** S3: with no argument, show a menu and never auto-run. Master skill must auto-trigger on UI work. | Master skill | `uimaster` auto-triggers on UI work. S3 commands run only when asked by name. `/design` with no argument shows the S3 menu. |
| C13 | **"Brief wins" vs bans.** S3: honor the pinned brief even against its own warnings, except lines marked as a ban. S2: bans hold with no exception. | S3 rule, S4 limit | The user's explicit brief overrides taste defaults. It never overrides accessibility (a) or a line marked BAN in S3 `craft-floor`. |
| C14 | **Audit overlap.** S3 `critique` + `audit` vs S1 `usability-audit` + `ux-audit` (`ux-review` only renders reports). | S1 | S1 owns the report schema and `.ux/` output. S3 and S2 critique passes become extra lenses inside `usability-audit/references/design-critique.md`. The report contract is NOT changed. |
| C15 | **Output folders.** S1 writes `.ux/`; S2 writes `.taste-skill/`; S3 writes `.impeccable/` and PRODUCT.md / DESIGN.md. | Keep all three | Each keeps its own folder (no shared state to merge). S1 safety rule applies only to S1 audit skills. Documented in README. |
| C16 | **Software supply chain.** S3 launcher downloads a binary on first run; S3 hooks run on every Edit/Write; S2 `assets.mjs` fetches pictures over the network. | Safety (a) | Nothing runs automatically. Binary download and hooks are OFF by default and need an explicit command. See decisions D1-D3. |
| C17 | **Lint scope.** S2 `lint.mjs` / `inspect.mjs` ban lists vs S3 detector rules overlap and can disagree. | S3 detector for generic checks, S2 inspector for page house rules | Do not run both as blockers at once. Report each finding with its source. |

## Open decisions for you
- **D1** Include impeccable launcher (downloads the Rust engine on first run, checksum verified)? Recommended: **include, OFF until you run it**.
- **D2** Hooks that run on every edit? Recommended: **ship disabled**; enable with `/design-hooks on`.
- **D3** taste-skill scripts and library (Node 22+, Chrome, 1.7 MB)? Recommended: **include**; they run only when called.
- **D4** `live` and `generate` commands? Recommended: **defer** (need engine and browser extension).
- **D5** S4 author and license? Needed before public release.
- **D6** Author name for `plugin.json`.

## Added during Step 4
| # | Conflict | Winner | Decision |
|---|---|---|---|
| C18 | **Entrances on every section.** taste step 9 requires a staggered rise-and-fade entrance for the parts of every section, and its inspector fails a page with fewer than 8 moving elements. taste's own tells list "fade-and-rise on every section" as a tell. craft-floor says one authored moment, no identical entrance on every section. | craft-floor, conditional | Persuade pages: follow taste, but vary the entrances and keep one signature move. Operate and Read pages: the taste motion-count FAIL becomes a WARN. Feedback on every control stays required (C7). |
