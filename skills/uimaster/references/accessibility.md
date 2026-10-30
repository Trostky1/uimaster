# Accessibility

Accessibility is priority (a). It wins over every style rule.

## Winning rules
- **Contrast:** text 4.5:1, large text 3:1, UI components 3:1.
- **Focus:** a visible focus ring on every interactive control. Theme it from the palette. A full keyboard path through every task. (craft-floor)
- **Targets:** 44x44 px or more on touch, with space between. Enlarge the clickable area around small icons. Do not rely on a tiny icon as the only target. (UX law 2)
- **Not colour alone.** Pair colour with text, icon, or shape.
- **Semantic HTML first.** Real buttons, links, headings, lists, labels, and tables. ARIA only to fill a gap. Every form field has a label. Every image has useful alt text or is marked decorative.
- **Reduced motion:** respect `prefers-reduced-motion`.
- **Text scaling and zoom:** layout survives 200% zoom. Real copy does not overflow.
- **Agents too.** A UI for agents needs stable names, roles, and states in the accessibility tree. Semantic structure helps people and agents alike. (S1 theme: "humans and agents alike")
- **Browser surfaces carry the design:** selection colour, caret, scrollbars, focus rings, underline offset. (craft-floor)

## How it is checked
- `/ux-audit` runs the accessibility auditor through the `web-quality-skills` dependency (WCAG 2.2).
- If that dependency is not installed, `/ux-audit` falls back to the checklist above and states that the result is a reduced check. It never reports a silent pass.
- Mechanical checks (contrast, overflow, broken images) run in the optional craft engine or the taste inspector. See [audit-checks](audit-checks.md).

## Deep detail
`../../ux-audit/SKILL.md` · `../../craft/reference/audit.md` · `../../craft/reference/craft-floor.md`
