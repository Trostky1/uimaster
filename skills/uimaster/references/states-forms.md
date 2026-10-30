# States, forms, errors, edge cases

## Winning rules
- **Ship every state:** hover, focus, active, disabled, loading, error, empty, success. Plus real content and working controls. (craft-floor)
- **Defaults help (UX law 13).** Preselect the safest and most common option. Use known context to cut input. Never default to a surprise commitment. Every default is easy to change.
- **Prevent errors first (UX law 14).** Accept common input formats. Explain requirements before submission. Disable impossible actions. Warn before risky actions.
- **Confirm destructive actions (C6).** A confirmation dialog is required for destructive or irreversible actions. Do not use a modal for a task that needs neither interruption nor protected focus. (UX law 14 wins over the craft-floor modal ban)
- **Recover from errors (UX law 15).** Keep the user's work. Say what went wrong in plain language. Say exactly how to fix it. Offer undo, retry, restore, or cancel.
- **Error text names the problem and the recovery.** Controls name their action. (craft-floor)
- **Chunk long forms (UX laws 5, 18).** Break into steps. Prefill what is known. Keep the submit button near the last input (UX law 8). Cut needless confirmations.
- **Reveal advanced options only when relevant (UX law 19).** Do not force users to learn internal details.
- **Harden against real input.** Test very long and very short text, emoji, RTL, accents, huge numbers, 1000+ items, no data, offline, slow network, API errors (400, 401, 403, 404, 500), and validation errors. (S3 harden)
- **Auth walls:** for audits that meet a login wall, follow `../../usability-audit/references/auth-handoff.md`. Never read back or store credentials.

## Deep detail
`../../craft/reference/harden.md` · `../../craft/reference/clarify.md` · `../../ux-laws/SKILL.md` (items 13, 14, 15, 18, 19)
