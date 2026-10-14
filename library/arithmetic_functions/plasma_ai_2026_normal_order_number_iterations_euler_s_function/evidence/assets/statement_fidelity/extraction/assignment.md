# Assignment: whole-statement fidelity audit of a Lean challenge file for Erdős Problem 408

You are an independent reviewer under a refutation charge. Your task is to find any defect in the fidelity of three Lean statements to the mathematical statements they claim to formalize. Your task is not to agree with them. The commissioner prepared this extraction and froze it on 2026-10-14. You did not write any of it, and you have no other context.

## Read set (read only these files, all in this folder)

- `assignment.md`: this file.
- `problem_statement.md`: the corpus's statement and formulation of Erdős Problem 408. This is the target.
- `challenge.lean`: the Lean file under audit. It contains the definitions `Erdos408.f` and `Erdos408.HasDensity` and the theorems `Erdos408.normal_order_rate`, `Erdos408.erdos_408.parts.i` and `Erdos408.erdos_408.parts.ii`, each with a deliberate `sorry`.
- `paper_theorem_1_1.tex`: the definition of f and Theorem 1.1 from the preprint the formalization accompanies. It is the target for `normal_order_rate`.
- `fc_408.lean` and `fc_density.lean`: the formal-conjectures statement of Problem 408 and its density definitions at commit 7db2ea3b91 (2026-10-14). `challenge.lean` says it copies them. Read them as supporting definitions.

Read no other file. Do not search the filesystem, run git, use the web, or consult any other source. If you do see anything outside this read set, say what it was and how you saw it, in your report at the point it happened.

## What to decide

For each of the three theorems, decide whether the Lean statement is faithful to its target. Compare objects, quantifiers, hypotheses, conventions, constants, domains, exceptional cases, junk values, and the conclusion. Unfold every definition it uses: `f`, `HasDensity`, `Real.log` at 0 and 1, `ℕ`-to-`ℝ` casts, `Finset.Icc 1 ⌊x⌋₊`, `atTop` and `∀ᶠ`, and `Monotone`/`Tendsto`/`ContinuousAt`.

1. **`erdos_408.parts.i` against the first question** ("Does f(n)/log n have a distribution function?"). Does the Lean statement say exactly that a distribution function exists, in the natural-density sense? Is its conclusion neither stronger nor weaker than the question, or if it is, how?
2. **`erdos_408.parts.ii` against the second question**, read as a normal order under the Formulation. Is "almost always constant" captured, with no "almost all" upgraded to "all" and no exceptional set dropped?
3. **`normal_order_rate` against the paper's Theorem 1.1.** Check the constant's range, the variance bound, the exceptional-count bound, the range of n (the paper writes 3 ≤ n ≤ x for the count), and the "for all sufficiently large x" quantifier.
4. **The definition of f.** Check it against the problem's definition (φ_1 = φ, so k starts at 1) and against the paper's (φ_0(n) = n). State what happens at n = 0 and n = 1, and whether either difference matters for any of the three statements.
5. **`HasDensity` against formal-conjectures' `Set.HasDensity`** with its default `A = univ`. Are they the same proposition?
6. **Coverage.** Do `parts.i` and `parts.ii` together cover the first two questions whole? Confirm that the third question (the largest prime factor) is not covered.

## Report

Write your report to `../report.md`, the folder above this one. It is the only file you write. Use these sections:

- **Subject:** your role, as an independent fresh-context reviewer, with no names. List the files read, with their paths in this folder, the freeze date 2026-10-14, and the exact scope.
- **Independence:** how you were separated from the authorship, what you read, and any exposure.
- **(a) Restatement:** each target and each Lean statement, in your own words.
- **(b) Clause-by-clause comparison:** a verdict for every clause and definition listed above.
- **(c) Checklist:** a verdict for each of these modes, applicable or not, saying which. "Almost all" quietly upgraded to "all". Exceptional sets dropped from density arguments. Consequence sentences as claim surfaces (each "hence" or "in particular"). Junk values and edge cases. Convention drift.
- **(d) Strongest attack:** the strongest attempt you made to show unfaithfulness, and why it failed, or the defect with its exact witness.
- **Verdict:** for each theorem, either "faithful" or "not faithful (defect: …)", and a coverage statement (whole or partial, with what is missing). Write verdict words in full.
