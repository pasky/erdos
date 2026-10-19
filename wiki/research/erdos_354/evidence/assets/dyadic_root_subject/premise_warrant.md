[cut]

status: accepted
claim: proved
scope: partial
evidence:
- formalized

[cut]

**Acceptance.** Formalized. This corpus's verification rebuilt the record's
solution file on the repository's pinned toolchain, `leanprover/lean4:v4.34.1`
with Mathlib at the revision `lean/lake-manifest.json` pins, after changes for
Mathlib's `ProbabilityMeasure.map`, which now takes the function rather than its
measurability proof, and for two renamed lemmas; the target's statement is
unchanged. The kernel replayed, from an empty environment, every declaration the
target `Bounty.target` depends on, Lean core, Mathlib and formal-conjectures
included, and accepted them all. The target's axioms are exactly `propext`,
`Classical.choice` and `Quot.sound`. Its type, and every definition its
statement reaches, are identical to the formal-conjectures statement of
Conjectures.io's task, which **Claim.** above reads as the first question:
`interleave α β 2` lists the floors of $2^k\alpha$ and $2^k\beta$, and sums run
over finite index sets. Acceptance rests on this replay and that check.

[cut]
