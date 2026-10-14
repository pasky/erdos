---
name: arithmetic_functions/plasma_ai_2026_normal_order_number_iterations_euler_s_function/evidence/verify/statement_fidelity/grade
title: Grade of the Problem 408 fidelity audit
desc: |
  A distinct grader's check, on 2026-10-14, of the Problem 408 fidelity
  audit: PASS, every part of the contract present, each verdict re-derived,
  the exposure immaterial and the refutation charge met.
created: 2026-10-14T20:39:30Z
updated: 2026-10-14T20:39:30Z
---

***

# Grade of the Problem 408 fidelity audit

- **Grader:** I am an independent grader with a fresh context. I did not write the material under audit or the report. Examination date: 2026-10-14 (UTC). I read these files in full, all in the folder the records were written in:
  - `grading_assignment.md`
  - `report.md`
  - `extraction/assignment.md`
  - `extraction/problem_statement.md`
  - `extraction/challenge.lean`
  - `extraction/paper_theorem_1_1.tex`
  - `extraction/fc_408.lean`
  - `extraction/fc_density.lean`

  I read nothing else. I ran no search, git command or build, and did not use the web. **My own exposure:** the environment put the same kinds of material into my context that the report describes. These were the organization's and the repository's instruction files, a status snapshot (a branch name and five commit subjects about tooling and review procedure) and environment details. None of it concerns Problem 408. I took Lean and Mathlib conventions from general knowledge, as the report did: `Real.log 0 = Real.log 1 = 0`, division by zero gives 0, casts are inserted at the leaves, and the operator precedences.

- **Contract:** every part is present.
  - **Subject:** present. It gives the role, says the reviewer did not write any of the material, and names no one. It lists the files read with line ranges, gives the freeze date 2026-10-14 and states an exact scope with exclusions.
  - **Independence:** present. It says what was read, lists the exposure (instruction files, status snapshot, environment details) and says which background facts came from general knowledge.
  - **(a) Restatement:** present. It covers Q1, Q2, Theorem 1.1, the three Lean statements and both definitions.
  - **(b) Clause-by-clause comparison:** present. It covers assignment items 1–6 and every primitive the assignment lists: `Real.log` at 0 and 1, the casts, `Finset.Icc 1 ⌊x⌋₊`, `atTop` and `∀ᶠ`, and `Monotone`, `Tendsto` and `ContinuousAt`. It also checks the copy claims.
  - **(c) Checklist:** present. All five modes are marked applicable, each with a verdict.
  - **(d) Strongest attack:** present. There are five attacks. The strongest gives an explicit witness and states what remains uncertain.
  - **Verdict:** present. Each theorem gets "faithful" in full words, and there is a coverage statement ("partial", saying what is missing).

- **Soundness:**
  - **f at n = 0 and n = 1.** Correct. Every iterate of the totient at 0 is 0, so the set is empty and `sInf ∅ = 0` gives f(0) = 0. φ(1) = 1 puts k = 1 in the set, so f(1) = 1. The problem defines φ_1 = φ, so k starts at 1 and the problem's f(1) is 1. The paper sets φ_0 = id, so its f(1) is 0. For n ≥ 2 all three definitions agree, because φ(m) < m for m ≥ 2 and φ_0(n) = n ≠ 1. In `parts.i` and `parts.ii` the denominator at n = 0 and n = 1 is `Real.log` = 0, so the quotient is 0 whatever f is. Changing finitely many n cannot change a density.
  - **`HasDensity` against `Set.HasDensity` with A = univ.** Correct. `partialDensity` with A = univ is `(((S ∩ univ) ∩ Iio b).ncard) / ((univ ∩ Iio b).ncard)`, divided in ℝ. The proof of `partialDensity_le_one` uses `Nat.cast_nonneg` on the denominator, which confirms real division of casts. The rewrites `inter_univ` and `univ_inter` turn it into the local definition. The filter and the limit are the same.
  - **`parts.ii` equals a normal order on a density-one set.** Correct in both directions.
    - Formulation to Lean: each ε-set contains A minus a finite set, and a squeeze gives density 1.
    - Lean to Formulation, by the diagonal argument. Let E_j = {n : |g(n) − α| ≥ 1/j}, which has density 0. Choose N_j so that E_j has at most N/j members below N for every N ≥ N_j. Let E be the union of E_j ∩ [N_j, N_{j+1}). Then E_j ⊆ E_k for j ≤ k, so for N in [N_k, N_{k+1}), E has at most N_1 + N/k members below N, and E has density 0. Off E, g(n) → α, because j → ∞ as n → ∞.
  - **Meaning of "distribution function" in `parts.i`.** Correct.
    - Dropping right-continuity is harmless. F⁺ (the right limit of F) has the same limits at ±∞. Because F(c−) ≤ F(c) ≤ F(c+), F⁺ has the same continuity points as F and equals F there.
    - `parts.ii` implies `parts.i` with F the indicator of [α, ∞). I checked both cases, c < α and c > α.
    - The condition is not vacuous: a monotone F has only countably many discontinuities.
    - The residual "every c" reading is identified correctly. Under it, Q1 would also need the density of {n : f(n) ≤ α log n} to exist. The variance bound leaves typical fluctuations of size about log n/(log log n)^{5/2} on both sides, so `normal_order_rate` does not settle that.
    - The standard weak-convergence definition, the paper's "limiting distribution" (line 7) and `fc_408.lean` lines 111–113 all support the continuity-point reading.
  - **Junk values in `normal_order_rate`.** Correct.
    - n = 1 adds (1 − 0)² = 1 to the Lean sum.
    - n = 1 is always exceptional in the Lean count: its threshold is 0/0 = 0 < 1.
    - n = 2 is always exceptional too: log log 2 ≈ −0.3665 gives a threshold of about −1.891, which is below any absolute value.
    - log log n > 0 exactly when n ≥ 3, so for n ≥ 3 the Lean and paper counts agree.
    - So the Lean count is the paper's count plus 2 once x ≥ 2. Both right-hand sides tend to infinity and √x ≥ 1, so changing C₀ to C₀ + 1 or C₀ + 2 absorbs the differences. Taking the larger of two constants gives one C for both bounds. The Lean form implies the paper's with the same C.
    - I also checked the precedences: the sum's body stops before `≤`, `C * x * L ^ 2 / M ^ 5` means (C·x·L²)/M⁵, and both bounds sit under one `∃ C, ∀ᶠ`.
    - The report's Chebyshev check of the docstring's "Hence" step is right: it gives at most 4x/(log log x)³ for n > √x, and the n ≤ √x add at most √x.
  - **Coverage.** Correct. Q1 is covered by `parts.i`. Q2 is covered by `parts.ii` under the Formulation's reading. Nothing covers Q3, and `fc_408.lean` lines 153–157 confirm it is not formalized. Theorem 1.1 is covered by `normal_order_rate`, whose count bound implies its "In particular" clause.
  - **Errors that change no verdict.**
    - Section (c) item 3 cites `challenge.lean` lines 20–21 for "its distribution function is the point mass at α". That text is on lines 21–22.
    - The remark "b/(b − 1) → 1" in b.2 is loosely worded, but its conclusion (the limits agree) is correct.
    - Calling the every-c gap "the single atom c = α" assumes the point-mass law. In general the gap is at the atoms of F, and given the theorems, α is the only one.

- **Exposure ruling:** immaterial. The exposed material says nothing about Problem 408, its mathematics, the Lean files or any expected verdict. Every mathematical claim in the report comes from the read set or from general knowledge the report labels as such. Each attack follows the assignment's checklist or the extraction itself. For example, the every-c attack follows from the `ContinuousAt` clause in `parts.i`, and the junk-value attack follows from the assignment's list of primitives to unfold. Nothing in the exposure weakens the refutation. At most it shaped the writing style and the no-names form, which is form, not substance.

- **Charge:** met. The reviewer made five separate attacks. They computed the edge cases explicitly, checked the docstrings' "Hence" and "In particular" sentences, including the Chebyshev step, and gave an exact witness for the strongest attack. They kept the remaining interpretive doubt rather than dismissing it.

- **Grade:** PASS. The report has every part the contract requires. I checked each point of its mathematics against the extraction and it holds:
  - the treatment of f at 0 and 1;
  - the `HasDensity` identity;
  - the equivalence of `parts.ii` with a normal order, including the diagonal argument;
  - the continuity-point reading of "distribution function" and the equivalence without right-continuity;
  - the junk values at n = 1 and n = 2, and their absorption into C;
  - the coverage.

  The only slips are a line citation and two loosely worded remarks, and none changes a verdict. The exposure was immaterial, and the reviewer genuinely tried to refute the statements.

- **Accepted judgment:**
  - **`Erdos408.normal_order_rate`: faithful.** It is equivalent to Theorem 1.1. The "In particular" clause is implied rather than stated. The n = 1 and n = 2 junk terms add 1 to the sum and 2 to the count, and C absorbs them.
  - **`Erdos408.erdos_408.parts.i`: faithful.** It states a yes answer to Q1 under the standard, continuity-point definition of a distribution function. Residual: under the non-standard every-c reading, it leaves out the existence of the density of {n : f(n) ≤ α log n}.
  - **`Erdos408.erdos_408.parts.ii`: faithful.** It states a normal order on a set of natural density one, as the Formulation reads Q2. No "almost all" is upgraded to "all", and no exceptional set is dropped.
  - **Coverage: partial.** The first and second questions are covered whole, the second under the Formulation's reading. The third question, on the largest prime factor of φ_k(n) when k = log log n, is not covered. Theorem 1.1 is covered whole by `normal_order_rate`.
