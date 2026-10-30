# Design critique lens (uimaster)

An extra lens for the usability audit and for `/critique`. It judges **the render**, not the code. You wrote the code, so you read your intentions into it. The pictures only show what is there. (taste critique, impeccable critique)

Sources: tasteskill v2 `critique.md` (14 passes, score, caps) and impeccable `critique.md` (two isolated assessments). Full texts: [taste](../../taste/references/critique.md) · [craft](../../craft/reference/critique.md).

## How findings enter the report
File each finding under a valid framework (Nielsen, Shneiderman, or NPCIS). Name the pass in the finding text. Example: "NPCIS Presentation — Pass 2 (squint): the page reduces to six equal masses, so nothing leads." The report contract does not change.

## Two isolated assessments (impeccable)
1. **Assessment A: design review.** A person or agent reads the screenshots and judges the design.
2. **Assessment B: tool evidence.** The mechanical detector or inspector results.
3. Run A and B as isolated sub-agents when a sub-agent tool exists. Finish A before B enters the synthesis, so tool output does not anchor judgment.
4. If you must run both in one context, start the report with: `⚠️ DEGRADED: single-context (<reason>)`.
5. The close of the response is the question to the user. Write the whole report first.

## The fourteen passes (taste)
Open the screenshots at every viewport. Make each pass on its own.

1. **One second, then five.** One clear thing seen? Can a stranger say what it is, who it is for, and what to do?
2. **Squint.** Two or three large masses with clear size differences.
3. **Cover the logo.** Could a competitor or another industry use this screen? Does the idea reach the lower sections?
4. **Edges.** Count the distinct left edges. Two or three, reused on purpose.
5. **Space and frame.** Related close, unrelated far. Holes versus rests. Equal margins.
6. **Type.** Decisive jump from body to headline. Five sizes or fewer. No orphan last word. Measure about 75 characters or less.
7. **Colour.** Name the proportions. The accent means "here".
8. **Images.** Real pictures doing a job. Shared crops and grade. No grey boxes or fake screens.
9. **Sameness.** One word per section layout. No repeat twice in a row.
10. **Phone.** A composition of its own, not squeezed desktop.
11. **Fullness.** Each screen is composed. Not an unfinished wireframe.
12. **Substance.** Every requested section delivers its information. The primary action is a real button on the first screen.
13. **Collisions.** Nothing covers a headline. Nothing runs off the phone edge.
14. **The competitor and the live thing.** Does the idea survive the nearest competitor's name? Name the one live thing.

## Score (optional, for Persuade pages)
Four criteria, 1-10 each: design 40%, usability 30%, creativity 20%, content 10%. Overall = 0.4 design + 0.3 usability + 0.2 creativity + 0.1 content. The caps in the taste file override the arithmetic (for example, any inspector FAIL caps overall at 6.0). Do not round up. Score again as a juror who did not build it.

## What to fix first
Idea, hierarchy, composition, typography, imagery, colour, detail, motion (last). When removing something leaves a gap, close it or enlarge what remains. Do not refill it with an ornament. Run at most three rounds.

## Not for app screens
Passes 3, 8 (real photographs), and 14 (idea and live thing) are about pages that persuade. For Operate surfaces, replace them with: is it familiar to a category-fluent user (UX law 3), and can the user finish the task with few choices (UX law 1)?
