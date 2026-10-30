# UX laws lens (uimaster)

An extra evaluation lens for the usability audit. It applies the 20 laws from [`ux-laws`](../../ux-laws/SKILL.md). It is not a sixth framework. The report contract and `frameworks:` vocabulary do not change.

## How to cite
1. Find the violation with this table.
2. File the finding under the **primary framework** in the last column (Nielsen, Shneiderman, or NPCIS). That value is valid in the report contract.
3. Name the law in the finding text. Example: "Nielsen #1 — Doherty Threshold: no feedback within 400 ms after Save."
4. If the same defect is already filed under another framework, merge it. Do not file it twice (see the de-duplication step in the skill).

## The lens
| # | Law | Look for | Primary framework |
|---|---|---|---|
| 1 | Hick | Too many choices on one screen. No recommended option. Hard decision not split into steps. | Nielsen #8 |
| 2 | Fitts (size) | Small buttons or icon-only targets. Cramped controls. Under 44x44 px on touch. | NPCIS Interaction |
| 3 | Jakob | Unfamiliar pattern with no clear gain. Nav, search, settings, or account in unusual places. | Nielsen #4 |
| 4 | Proximity | Related items far apart. Unrelated items close. Borders used where spacing would do. | NPCIS Presentation |
| 5 | Miller | Long unchunked content or forms. User must remember data between screens. | Nielsen #6 |
| 6 | Doherty | No feedback within about 400 ms. No loading, processing, or success state. | Nielsen #1 |
| 7 | Von Restorff | Primary action not the strongest element. Several actions compete. | NPCIS Presentation |
| 8 | Fitts (distance) | Action far from the content it affects. Submit far from the last input. | NPCIS Interaction |
| 9 | Serial position | Key information buried in the middle. Last step or takeaway unclear. | NPCIS Presentation |
| 10 | Peak-End | Flow ends on an empty or unclear screen. No confirmation or next step. | NPCIS Strategy |
| 11 | Zeigarnik | No visible progress. Work lost on interrupt. Hard to resume. | Shneiderman #4 |
| 12 | Prägnanz | Visual noise. No clear hierarchy. Not understandable at a glance. | Nielsen #8 |
| 13 | Defaults | No sensible default. Default creates a surprise commitment. Default hard to change. | Nielsen #7 |
| 14 | Postel (prevent) | Strict input formats. Requirements shown only after failure. Risky action with no warning. | Nielsen #5 |
| 15 | Postel (recover) | Work lost after error. Vague error text. No undo, retry, or cancel. | Nielsen #9 |
| 16 | Similarity | Same look for different actions. Different look for the same action. | Nielsen #4 |
| 17 | Uniform connectedness | Controls not visibly tied to what they change. Unrelated items visually joined. | NPCIS Presentation |
| 18 | Parkinson | Extra steps and confirmations. Known data not prefilled. No shortcut for repeat tasks. | Nielsen #7 |
| 19 | Tesler | All options shown at once. User must learn internal details. | Shneiderman #2 |
| 20 | Goal-gradient | Long task with no milestones. Remaining work feels vague. | NPCIS Strategy |

## Severity hint
- Severity 4: a law violation that blocks the primary goal (for example, no way to recover from an error that destroys work).
- Severity 3: a violation on the main path that slows or confuses most users.
- Severity 2 or lower: edge paths and polish.
When laws conflict, put clarity, accessibility, user control, and task completion first.

## Rulings (from CONFLICTS.md)
Do not report these as defects: functional progress such as "Step 2 of 4" (C3), confirmation dialogs for destructive actions (C6), labelled status (C9), quiet borders in app screens (C11).
