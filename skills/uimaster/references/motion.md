# Motion and feedback

## Winning rules
- **Feedback on every interaction (C7).** Acknowledge each action within about 400 ms: press state, loading, success, error. Use optimistic updates only when safe. Never leave the user wondering if an action registered. (UX law 6, Doherty)
- **Decorative motion: one authored moment.** Not scattered effects. Not one identical entrance on every section. (craft-floor, taste)
- **Easing:** exponential ease-out, starting from an already-visible default. No bounce. No infinite loops that mean nothing. (craft-floor, taste motion tells)
- **Materials:** beyond transform and opacity, blur, backdrop-filter, clip-path, mask, and shadow may be used when they stay smooth. (craft-floor)
- **No hover lift on every card.** No fade-and-rise on every section. A reveal must not fail and leave a blank band. (taste tells)
- **Operate and Read:** motion serves feedback, state, and continuity. Routine transitions are fast. No page-load choreography that makes users wait. (S3 animate)
- **Persuade and Experience:** prefer one rehearsed focal sequence to repeated reveals. (S3 animate)
- **Reduced motion:** always honor `prefers-reduced-motion`. Native: follow the platform's Reduce Motion. (craft-floor, accessibility)
- **Performance:** animate cheap properties. Check frame rate on a weak device. (S3 optimize)

## Deep detail
`../../taste/references/motion.md` · `../../taste/references/scenes.md` · `../../craft/reference/animate.md` · `../../craft/reference/overdrive.md`
