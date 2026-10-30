---
name: ux-laws
description: "Apply 20 UX laws (Hick, Fitts, Jakob, Miller, Doherty, Postel, Zeigarnik, Peak-End, and more) whenever designing, building, or revising any UI, layout, flow, form, onboarding, settings screen, or dashboard. Use for 'reduce choices', 'make the button easier to hit', 'simplify this form', 'show progress in this flow', 'handle errors gracefully', 'which pattern do users expect'."
---

> **Source.** The 20 laws and the 8 implementation requirements come from the `ux-laws-design` skill supplied by the user. Its author and license are not stated in the file (see `../../LICENSES.md`, decision D5). The text below the line is unchanged except for the two sections added at the end.

---


# UX Design Instructions

Follow these instructions whenever you design, build, or revise a user interface. Apply them across layouts, navigation, onboarding, forms, settings, dashboards, and interactive flows.

Your goal is to minimize confusion, reduce effort, prevent mistakes, and help users complete their intended task as quickly as possible.

## 1. Reduce Choices per Screen: Hick's Law

The time required to make a decision increases with the number and complexity of available choices.

* Give each screen one clear purpose.
* Remove irrelevant or low-priority options.
* Break complicated decisions into smaller steps.
* Recommend an option when users may struggle to choose.

## 2. Make Targets Large: Fitts's Law

Large, nearby targets are faster and easier to interact with.

* Make buttons and controls easy to click or tap.
* Give interactive elements sufficient spacing.
* Avoid tiny icons as the only interaction target.
* Increase the clickable area around important controls.

## 3. Follow Familiar Patterns: Jakob's Law

Users expect your product to work like products they already understand.

* Use established interface conventions.
* Place navigation, search, settings, and account controls where users expect them.
* Use familiar icons and interaction patterns.
* Do not invent a new pattern unless it provides a meaningful advantage.

## 4. Group Related Information: Law of Proximity

Elements positioned near one another are perceived as related.

* Place related labels, controls, and information together.
* Use spacing to communicate relationships.
* Separate unrelated groups with additional space.
* Do not rely on borders when spacing can establish the hierarchy.

## 5. Break Content Into Chunks: Miller's Law

Working memory can only process a limited amount of information at once.

* Divide long content into small, meaningful groups.
* Break complex forms and tasks into manageable steps.
* Use headings, sections, and concise labels.
* Avoid asking users to remember information between screens.

## 6. Respond Within 400 Milliseconds: Doherty Threshold

Interfaces feel more productive when feedback appears within approximately 400 milliseconds.

* Acknowledge every user action immediately.
* Show loading, processing, or success states when results are not instant.
* Use optimistic updates when they are safe.
* Never leave users wondering whether their action registered.

## 7. Highlight the Primary Action: Von Restorff Effect

An element that visually differs from surrounding elements receives more attention.

* Give the primary action the strongest visual emphasis.
* Use one dominant call to action per section.
* Keep secondary actions visually quieter.
* Avoid making every button compete for attention.

## 8. Place Key Actions Nearby: Fitts's Law

Interaction becomes faster when important targets are close to the user's current focus.

* Place actions beside the content they affect.
* Keep form submission near the final input.
* Position frequent actions within easy reach.
* Avoid forcing unnecessary cursor or eye movement.

## 9. Put Essentials First: Serial Position Effect

People remember the first and last items in a sequence most clearly.

* Put the most important information first.
* Place the final action or takeaway at the end.
* Keep lower-priority information in the middle.
* Order navigation and lists according to user importance.

## 10. End Flows Memorably: Peak-End Rule

Users judge an experience largely by its most intense moment and how it ends.

* Create a clear and satisfying completion state.
* Confirm what the user accomplished.
* Explain what happens next.
* Avoid ending flows on an empty or ambiguous screen.

## 11. Show Visible Progress: Zeigarnik Effect

Incomplete tasks remain mentally active and encourage users to return.

* Clearly show completed and unfinished steps.
* Save progress whenever possible.
* Make it easy to resume interrupted tasks.
* Use checklists or completion states for multi-step work.

## 12. Simplify Complex Interfaces: Law of Prägnanz

People interpret complex or ambiguous designs in the simplest form possible.

* Prefer simple structures and recognizable shapes.
* Remove unnecessary decoration and visual noise.
* Create an obvious visual hierarchy.
* Make the interface understandable at a glance.

## 13. Use Sensible Defaults: Hick's Law

Helpful defaults reduce the number of decisions users must make.

* Preselect the safest and most common option.
* Use existing context to reduce unnecessary input.
* Never use defaults that create unexpected commitments.
* Make every default easy to change.

## 14. Prevent Errors Proactively: Postel's Law

Interfaces should accept reasonable variations in user input while producing clear, predictable results.

* Accept common input formats and variations.
* Explain requirements before submission.
* Disable impossible or unavailable actions.
* Warn users before risky or destructive actions.

## 15. Make Errors Recoverable: Postel's Law

The interface should handle user mistakes gracefully without creating unnecessary failure.

* Preserve the user's work after an error.
* Explain what went wrong in plain language.
* Tell the user exactly how to fix it.
* Provide undo, retry, restore, or cancel options where appropriate.

## 16. Maintain Pattern Consistency: Law of Similarity

Elements that look similar are perceived as having related purposes.

* Give similar components the same appearance and behavior.
* Use consistent colors, labels, icons, spacing, and interaction states.
* Do not use the same visual treatment for different actions.
* Reuse established components before creating new ones.

## 17. Connect Related Elements Visually: Law of Uniform Connectedness

Visually connected elements are perceived as more closely related.

* Use containers, lines, backgrounds, or shared states to show relationships.
* Visually connect controls to the content they affect.
* Keep unrelated elements visually separate.
* Use connection deliberately, not decoratively.

## 18. Reduce Task Completion Time: Parkinson's Law

Tasks tend to expand to consume the time made available for them.

* Minimize the number of steps required.
* Remove unnecessary confirmations and screens.
* Prefill information the user has already provided.
* Offer shortcuts for frequent or repeat actions.

## 19. Reveal Complexity Gradually: Tesler's Law

Every system contains some complexity that cannot be removed, only managed or transferred.

* Show essential controls first.
* Reveal advanced options only when relevant.
* Let the system handle complexity whenever possible.
* Do not force users to understand internal technical details.

## 20. Make Completion Feel Closer: Goal-Gradient Effect

Motivation increases as users perceive themselves getting closer to a goal.

* Show progress throughout multi-step flows.
* Divide long tasks into visible milestones.
* Emphasize progress already made.
* Make the remaining work feel specific and achievable.

## Implementation Requirements

When creating or revising an interface:

1. Identify the user's primary goal.
2. Design the shortest clear path to that goal.
3. Make the next action visually obvious.
4. Remove anything that distracts from task completion.
5. Provide immediate feedback after every interaction.
6. Prevent errors before they occur.
7. Preserve user work when something goes wrong.
8. Confirm clearly when the goal has been completed.

When laws appear to conflict, prioritize clarity, accessibility, user control, and successful task completion. Do not apply these laws mechanically. Use them to make deliberate decisions based on the user's context and goal.

## Cross-references (repeated laws)

Three laws appear twice in the list above. Treat each pair as one law with two uses.

| Law | Items | Use |
|---|---|---|
| Hick's Law | 1 and 13 | 1 = fewer choices per screen. 13 = defaults remove choices. |
| Fitts's Law | 2 and 8 | 2 = large targets. 8 = key actions placed near the focus. |
| Postel's Law | 14 and 15 | 14 = prevent errors. 15 = recover from errors. |

## Rulings when other design rules disagree

These rulings come from `../../CONFLICTS.md`. They apply when `taste` or `craft` give different advice.

- **Progress in flows (items 11, 20) wins over the ban on step numbers.** Show "Step 2 of 4" or a progress bar in real multi-step flows. Do not number page sections for decoration.
- **Confirmation for risky actions (item 14) wins over the ban on needless modals.** Always confirm destructive or irreversible actions.
- **Feedback within 400 ms (item 6) wins over "one motion moment".** Every interaction gets functional feedback. Limit only the decorative motion.
- **State must be visible (items 6, 11).** A real status (error, success, live, beta) gets a text label. Decorative badges stay banned.
- **Familiar patterns (item 3) win on app screens.** Novel layouts are for pages that persuade or showcase.

## Verify (run on the built result)

- [ ] Text contrast 4.5:1 or more (3:1 for large text).
- [ ] Visible focus state on every control, and a full keyboard path.
- [ ] Touch targets 44x44 px or more, with spacing between them.
- [ ] Loading, empty, error, and success states exist and are worded for the user.
- [ ] Checked at 360 px and 1440 px wide.
- [ ] `prefers-reduced-motion` is respected.
- [ ] One primary action per section. The next step is obvious.
- [ ] The flow ends with a clear completion state that says what happens next.
