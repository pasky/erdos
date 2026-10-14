---
name: arithmetic_functions/plasma_ai_2026_normal_order_number_iterations_euler_s_function/evidence/verify/statement_fidelity/report
title: Fidelity audit of the Problem 408 challenge statements
desc: |
  Fresh-context refutation-charge audit, on 2026-10-14, of the three
  statements of the Problem 408 formalization's challenge file against the
  problem's first two questions and the preprint's Theorem 1.1: all three
  faithful, coverage partial.
created: 2026-10-14T20:39:30Z
updated: 2026-10-14T20:39:30Z
---

***

# Fidelity audit of the Problem 408 challenge statements

## Subject

- **Role.** An independent reviewer with a fresh context, charged with finding
  unfaithfulness, auditing whole-statement fidelity. I did not write any part of
  the material under audit.
- **Examination date.** 2026-10-14 (UTC). The extraction was frozen on
  2026-10-14.
- **Files read.** All are in `extraction/`, beside this report, and I read each
  one in full:
  - `extraction/assignment.md`: the assignment.
  - `extraction/problem_statement.md`: the Statement and Formulation of Problem
    408 (lines 5–24). This is the target for `parts.i` and `parts.ii`.
  - `extraction/challenge.lean`: the file under audit. It defines `f` (lines
    52–59) and `HasDensity` (lines 61–64), and states `normal_order_rate`
    (lines 66–77), `erdos_408.parts.i` (lines 79–87) and `erdos_408.parts.ii`
    (lines 89–96).
  - `extraction/paper_theorem_1_1.tex`: the paper's definition of f (lines 3–6)
    and Theorem 1.1 (lines 9–26). This is the target for `normal_order_rate`.
  - `extraction/fc_408.lean`: the formal-conjectures statement file. It
    contains `f` (lines 50–57), `parts.i` (lines 105–122), `parts.ii` (lines
    124–137), and the Pillai and Ford–Konyagin–Luca variants (lines 139–169).
  - `extraction/fc_density.lean`: the formal-conjectures density definitions.
    It contains `partialDensity` (lines 41–44) and `Set.HasDensity` (lines
    83–93).
- **Scope.** The scope is the fidelity of the three theorem statements and the
  two definitions in `challenge.lean`, compared against the targets above. It
  covers objects, quantifiers, hypotheses, conventions, constants, domains,
  exceptional cases, junk values and conclusions. It also covers the coverage
  of Problem 408's three questions. Out of scope: the proofs (each theorem ends
  in `sorry`), whether the file compiles, the provenance claims in the module
  docstring (lines 24–31 and 41–42), and any solution file or checking tool.

## Independence

I was launched with a fresh context. My only task input was a short launch
instruction that pointed to `extraction/assignment.md` and restated its
constraints. I read only the six files listed above. I did not search the
filesystem, run git, run any build, or use the web.

**Exposure outside the read set.** The agent environment placed some material
into my context automatically, before I read anything. It contained:

- the organization's and the repository's general instruction files, with
  coding and writing conventions, the repository's binding conventions and its
  verification-tier definitions;
- a repository status snapshot: the branch name and the subject lines of five
  recent commits, all about tooling and review procedure;
- environment details.

None of it concerned Problem 408, its mathematics, or the files under audit.
The launch instruction gave no hint about the expected verdict.

**Background knowledge.** I state Mathlib's conventions from general knowledge,
not from reading Mathlib source, which is outside the read set. These are
`Real.log 0 = 0`, `Real.log 1 = 0`, real division by zero giving 0,
`Nat.totient 0 = 0`, `sInf ∅ = 0` on `ℕ`, and the notation precedences. Where
the read set confirms one of them, I cite it:

- `fc_408.lean` lines 61–66 prove `f 0 = 0` from `Nat.totient_zero` and
  `Nat.sInf_eq_zero`.
- `fc_density.lean` lines 46–49 bound the partial density using
  `Nat.cast_nonneg` on its denominator, which shows the division is real
  division of casts.
- `fc_408.lean` lines 113–114 state that the quotient is 0 in Lean for n ≤ 1.

I do not reliably recall how Erdős himself defined "distribution function" in
the original sources. Section (d) treats that as residual uncertainty.

## (a) Restatement

**Definitions in `challenge.lean`.**

- `f n` is the least k ≥ 1 such that applying Euler's totient to n k times
  gives 1. If no such k exists, `f n` is 0.
- `HasDensity S a` says the following. Count the members of S among
  0, 1, …, b−1 and divide by b. This ratio tends to a as b → ∞ through the
  natural numbers.

**Target Q1 (problem statement, line 13).** Does f(n)/log n have a
distribution function? That is, is there a distribution function F such that
the natural density of {n : f(n)/log n ≤ c} exists and equals F(c)? This
density condition is the usual one: it must hold at every continuity point c
of F.

**Lean `erdos_408.parts.i`.** There is a function F : ℝ → ℝ with these
properties:

- F is non-decreasing;
- F(c) tends to 0 as c → −∞ and to 1 as c → +∞;
- at every point c where F is continuous, the set {n ∈ ℕ : f(n)/log n ≤ c}
  has natural density F(c).

The statement asserts that the answer to Q1 is yes.

**Target Q2 (problem statement, lines 13–14 and 17–24).** Is f(n)/log n almost
always constant? The Formulation reads this as asking for a normal order: is
there a constant α such that f(n)/log n → α on a set of natural (asymptotic)
density one?

**Lean `erdos_408.parts.ii`.** There is a real α such that, for every ε > 0, the
set {n ∈ ℕ : |f(n)/log n − α| < ε} has natural density 1. The statement asserts
that the answer to Q2 is yes.

**Target T (paper, lines 9–26).** The paper uses φ_0(n) = n, so its f(n) is the
least k ≥ 0 with φ_k(n) = 1, for n ≥ 1. Theorem 1.1 says there is a constant α
with 1/log 3 ≤ α ≤ 1/log 2 such that:

- for all sufficiently large x, the sum over n ≤ x of (f(n) − α log n)² is
  at most a constant times x(log x)²/(log log x)⁵;
- the number of n with 3 ≤ n ≤ x and |f(n) − α log n| > log n/log log n is
  at most a constant times x/(log log x)³ + √x;
- in particular, f(n)/log n → α on a set of natural density one.

**Lean `normal_order_rate`.** There are a real α with
1/log 3 ≤ α ≤ 1/log 2 and a real C such that both of the following hold for
all large real x:

- the sum over 1 ≤ n ≤ ⌊x⌋ of (f(n) − α log n)² is at most
  C·x(log x)²/(log log x)⁵;
- the number of 1 ≤ n ≤ ⌊x⌋ with log n/log log n < |f(n) − α log n| is at
  most C·(x/(log log x)³ + √x).

## (b) Clause-by-clause comparison

### b.1 The definition of f (assignment item 4)

`f n = sInf {k : ℕ | 1 ≤ k ∧ Nat.totient^[k] n = 1}`. Here `Nat.totient^[k]` is
the k-fold iterate, so `Nat.totient^[1] = Nat.totient`. `Nat.totient` agrees
with Euler's φ for n ≥ 1 and has `Nat.totient 0 = 0`.

| n | Problem (φ_1 = φ, k ≥ 1) | Paper (φ_0 = id, k ≥ 0, n ≥ 1) | Lean `f` |
|---|---|---|---|
| 0 | undefined | undefined | 0 (junk: every iterate of 0 is 0, the set is empty, and `sInf ∅ = 0`) |
| 1 | 1 (since φ(1) = 1) | 0 (since φ_0(1) = 1) | 1 |
| ≥ 2 | least k ≥ 1 with φ_k(n) = 1 | the same, because φ_0(n) = n ≠ 1 | the same |

For n ≥ 2 the set is non-empty, because φ(m) < m when m ≥ 2 and φ(m) ≥ 1
when m ≥ 1. So all three definitions agree for n ≥ 2. The Lean `f` matches the
problem's f exactly for n ≥ 1, as it claims at lines 54–55. It differs from the
paper's f only at n = 1, and from both only at the junk value n = 0.

**Does either difference matter?**

- **`parts.i` and `parts.ii`: no.** At n = 0 and n = 1 the denominator is
  `Real.log 0 = Real.log 1 = 0`, so the quotient is 0 whatever f is. The value
  f(1) never reaches these statements. Changing finitely many n also cannot
  change a natural density.
- **`normal_order_rate`: no.** n = 0 is excluded by `Finset.Icc 1 ⌊x⌋₊`. At
  n = 1 the Lean sum gets the term (1 − α·0)² = 1, where the paper's term is
  (0 − 0)² = 0. n = 1 also counts as exceptional in Lean, though the paper's
  count excludes it through 3 ≤ n. Both differences are bounded constants and
  are absorbed (b.6).

**Verdict: faithful to the problem's definition.** It differs from the paper's
definition at n = 1 only, which has no effect on any of the three statements.

### b.2 `HasDensity` against formal-conjectures' `Set.HasDensity` (assignment item 5)

With the default `A = Set.univ`, `Set.HasDensity S a` unfolds to

`Tendsto (fun b => (((S ∩ univ) ∩ Iio b).ncard : ℝ) / ((univ ∩ Iio b).ncard : ℝ)) atTop (𝓝 a)`.

The division is real division of natural-number casts. The proof at
`fc_density.lean` lines 46–49 confirms this.

`challenge.lean` lines 63–64 give

`Tendsto (fun b : ℕ => ((S ∩ Iio b).ncard : ℝ) / ((Iio b).ncard : ℝ)) atTop (𝓝 a)`.

The two differ only in `S ∩ univ` against `S` and `univ ∩ Iio b` against
`Iio b`. These are equal sets by `Set.inter_univ` and `Set.univ_inter`. The
filter (`atTop` on ℕ), the limit (`𝓝 a`) and the casts are the same. The texts
are not syntactically identical, and the two may not be equal by unfolding
alone, but rewriting with those two lemmas turns one into the other.

**Verdict: the same proposition.**

Both count from 0 and divide by b, while the textbook natural density counts
1 ≤ n ≤ N and divides by N. The two counts differ by at most 1, and
b/(b − 1) → 1, so the limits agree. At b = 0 the ratio is 0/0 = 0, which does
not affect a limit.

### b.3 Unfolded primitives (assignment, "What to decide")

- **`Real.log` at 0 and 1.** Both are 0. So for n ∈ {0, 1}, f(n)/log n is
  x/0 = 0. Also log log 1 = log 0 = 0, so the count's threshold at n = 1 is
  0/0 = 0. log log 2 = log(0.6931…) ≈ −0.3665, which is negative, so the
  threshold at n = 2 is ≈ −1.891. log log n > 0 exactly when n ≥ 3.
- **ℕ-to-ℝ casts.** `(f n : ℝ)` and `Real.log n`, which is `Real.log (↑n)`,
  are both real. Cardinalities are cast before dividing. Every division is real
  division. Nothing is truncated in ℕ.
- **`Finset.Icc 1 ⌊x⌋₊`.** This is {n ∈ ℕ : 1 ≤ n ≤ x} for x ≥ 1, and it is
  empty below 1. `⌊x⌋₊` is `Nat.floor`. This is the paper's range n ≤ x with
  n ≥ 1.
- **`atTop` and `∀ᶠ`.** `∀ᶠ x : ℝ in atTop, P x` means there is an x₀ with P x
  for all x ≥ x₀, which is "for all sufficiently large x". `∃ C` comes before
  `∀ᶠ`, so C does not depend on x. That is the correct order: the reverse
  order would make both bounds trivial.
- **`Monotone F`** means a ≤ b implies F a ≤ F b (non-decreasing).
  **`Tendsto F atBot (𝓝 0)`** and **`Tendsto F atTop (𝓝 1)`** mean F(−∞) = 0
  and F(+∞) = 1. **`ContinuousAt F c`** means F is continuous at c.
- **Parsing.**
  - The body of `∑ n ∈ s, …` is `((f n : ℝ) - α * Real.log n) ^ 2`, and `≤`
    and `∧` lie outside it.
  - `Real.log x ^ 2` is `(Real.log x)^2`, and `Real.log (Real.log x) ^ 5` is
    `(log log x)^5`.
  - `C * x * L ^ 2 / M ^ 5` is `(C·x·L²)/M⁵`.
  - The filter predicate closes before `.card`.
  - `A ∧ B ∧ ∃ C, …` associates to the right, so both bounds sit under the one
    `∃ C, ∀ᶠ x`.

**Verdict: no unfolding changes any statement's meaning, beyond the junk
values handled in b.1 and b.6.**

### b.4 `erdos_408.parts.i` against Q1 (assignment item 1)

| Clause | Q1 (standard meaning) | Lean | Verdict |
|---|---|---|---|
| F non-decreasing | required | `Monotone F` | match |
| F(−∞) = 0, F(+∞) = 1 | required | `Tendsto F atBot (𝓝 0)`, `Tendsto F atTop (𝓝 1)` | match |
| F right-continuous | usually part of the definition | not required | equivalent (below) |
| Points where the density must exist | continuity points of F | `∀ c, ContinuousAt F c → …` | match |
| Density notion | natural density | `HasDensity` (b.2) | match |
| The event | f(n)/log n ≤ c | `(f n : ℝ) / Real.log n ≤ c` | match |
| n ∈ {0, 1} | quotient undefined | quotient 0 (junk) | finite set, no effect |
| Form | a yes/no question | asserts the yes answer | appropriate for a claimed yes |

**Why right-continuity can be dropped.** Take an F satisfying the Lean
conditions. Let F⁺(c) be the limit of F(t) as t decreases to c. F⁺ is
non-decreasing and right-continuous, with the same limits at ±∞. It has the
same continuity points as F, because F(c−) ≤ F(c) ≤ F(c+). At those points it
equals F. So a Lean witness gives a distribution function in the strict sense,
and the reverse is immediate.

**The condition is not vacuous.** A monotone F has at most countably many
discontinuities, so the density condition applies at all but countably many
real c.

**Strength.** Under the standard definition, the conclusion is neither stronger
nor weaker than a yes answer to Q1. `parts.ii` implies it: take F to be the
indicator of [α, ∞).

- For c < α, the set {f/log ≤ c} lies inside the complement of
  {|f/log − α| < α − c}, so it has density 0.
- For c > α, the set contains {|f/log − α| < c − α}, so it has density 1.

`parts.i` therefore adds no content beyond `parts.ii`, but it states Q1
correctly on its own. A point mass is a distribution function, and nothing in
Q1 asks for a non-degenerate one. Under a non-standard "every real c" reading,
the Lean statement would be weaker at the single atom c = α; see (d).

**Verdict: faithful.**

### b.5 `erdos_408.parts.ii` against Q2 under the Formulation (assignment item 2)

The Formulation asks for a constant α and a set A of natural density 1 with
f(n)/log n → α as n → ∞ through A. Write g(n) = f(n)/log n. The Lean
statement asks for an α such that, for every ε > 0,
{n : |g(n) − α| < ε} has density 1. The two are equivalent.

- **Formulation implies Lean.** For each ε, the Lean set contains A minus a
  finite set. Its partial densities are squeezed between those of A minus that
  finite set, which tend to 1, and 1 itself.
- **Lean implies Formulation.** Use a diagonal construction.
  - Choose N₁ < N₂ < … so that for N ≥ N_j at most N/j of the n < N have
    |g(n) − α| ≥ 1/j.
  - Let E be the union over j of the n in [N_j, N_{j+1}) with
    |g(n) − α| ≥ 1/j.
  - For N in [N_k, N_{k+1}), every element of E in [N₁, N) satisfies
    |g − α| ≥ 1/k, because 1/j ≥ 1/k for j ≤ k. So E has at most N₁ + N/k
    elements below N, and E has density 0.
  - Off E, g(n) → α.

| Clause | Target | Lean | Verdict |
|---|---|---|---|
| "almost always" | on a density-one set | density 1 for each ε; exceptions allowed | match, not upgraded to "all" |
| Exceptional set | a density-zero set is allowed | the complement of each ε-set (density 0) | kept, not dropped |
| "constant" | some constant α | `∃ α : ℝ`, no sign condition | match; the Formulation imposes no sign either |
| Density notion | asymptotic (natural) density | `HasDensity` | match |
| n ∈ {0, 1} | quotient undefined | quotient 0 | finite, no effect |

The literal catalog reading, "f(n)/log n = c for almost all n", is not
formalized. The Formulation sets it aside as trivially false, and its reason
checks out:

- if c ≠ 0, then f(n)/log n = c forces n = exp(f(n)/c), so each value of f
  gives at most one such n;
- c = 0 is impossible for n ≥ 2, since f(n) ≥ 1 there.

The literal set therefore has O(log x) members up to x, which is density 0.
The Lean statement follows the Formulation's reading, which is the stated
target.

**Verdict: faithful.**

### b.6 `normal_order_rate` against Theorem 1.1 (assignment item 3)

| Clause | Paper | Lean | Verdict |
|---|---|---|---|
| Range of the constant | 1/log 3 ≤ α ≤ 1/log 2 | `1 / Real.log 3 ≤ α ∧ α ≤ 1 / Real.log 2` | match (log is the natural log in both) |
| Meaning of "≪" | some absolute constant | `∃ C : ℝ` before `∀ᶠ` | match; one C for both bounds is harmless (take the larger) |
| "for all sufficiently large x" | variance bound | `∀ᶠ x : ℝ in atTop` | match |
| Variance range | n ≤ x with f defined for n ≥ 1 | `Finset.Icc 1 ⌊x⌋₊` | match |
| Variance summand | (f(n) − α log n)² | `((f n : ℝ) - α * Real.log n) ^ 2` | match |
| Variance bound | x(log x)²/(log log x)⁵ | `C * x * Real.log x ^ 2 / Real.log (Real.log x) ^ 5` | match |
| Count range | 3 ≤ n ≤ x | 1 ≤ n ≤ ⌊x⌋ | Lean adds n = 1, 2 (below) |
| Count predicate | \|f(n) − α log n\| > log n/log log n | `log n / log (log n) < \|f n − α log n\|` | match (the same strict inequality) |
| Count bound | x/(log log x)³ + √x | `C * (x / Real.log (Real.log x) ^ 3 + √x)` | match |
| x-range of the count | stated after "Moreover", inside the theorem | inside the same `∀ᶠ` | equivalent (below) |
| "In particular, … density one" | stated | not stated | implied (below) |

**The n = 1 variance term.** The Lean sum equals the paper's sum plus 1 for
x ≥ 1 (b.1). The right side tends to infinity. So the paper's bound with
constant C₀ gives the Lean bound with C₀ + 1 once the right side is at least 1.
The Lean bound gives the paper's directly.

**n = 1 and n = 2 in the count.**

- At n = 1 the Lean predicate is 0/0 = 0 < |1 − α·0| = 1, which is true.
- At n = 2 it is −1.891… < |1 − α log 2|, which is true for every α, since
  the right side is non-negative.

So for x ≥ 2 the Lean count equals the paper's count plus 2. Since √x ≥ 1, the
paper's bound with C₀ gives the Lean bound with C₀ + 2. The Lean form is the
stronger by this additive 2 and is never weaker.

**The count's x-range.** If the paper's count bound holds for every x ≥ 3
rather than eventually, the two readings still agree up to C. On a bounded
range 3 ≤ x ≤ x₀, the count is at most x₀ and the right side is at least
C√3.

**Non-vacuity.**

- Pillai's bounds give only O(x(log x)²) for the sum, and the trivial count
  bound is x. Both right sides are o(x(log x)²) and o(x) respectively, so the
  bounds have content.
- For α away from the true normal-order constant, the sum is of order
  x(log x)², so α is pinned down.
- For x > e, log log x > 0, so no division-by-zero value enters inside the
  `∀ᶠ` range.

**The "In particular".** Off the exceptional set, |f(n)/log n − α| ≤
1/log log n → 0. The exceptional set has counting function
O(x/(log log x)³ + √x) = o(x), so it has density 0. Hence the Lean conjunction
implies the "In particular" clause, and leaving it out loses no content.

**Verdict: faithful.**

### b.7 Coverage (assignment item 6)

- **Q1 is covered whole** by `parts.i`, as its yes answer.
- **Q2 is covered whole** by `parts.ii`, as its yes answer under the
  Formulation's normal-order reading.
- **Q3 is not covered.** Q3 asks about the largest prime factor of φ_k(n) when
  k = log log n. No statement in `challenge.lean` mentions prime factors.
  `fc_408.lean` lines 153–157 say the third question is open-ended and not
  formalized. The related Ford–Konyagin–Luca variant (`fc_408.lean` lines
  164–169) is not copied into `challenge.lean`.
- **Theorem 1.1 is covered whole** by `normal_order_rate`. Its "In particular"
  clause is implied rather than stated (b.6).

### b.8 The copy claims in `challenge.lean` (lines 33–37)

- `f` and its docstring (`challenge.lean` lines 52–59) are identical to
  `fc_408.lean` lines 50–57.
- The statements of `parts.i` and `parts.ii` are identical to `fc_408.lean`
  lines 118–121 and 134–136. The only change is `{…}.HasDensity a` written as
  `HasDensity {…} a`, which is the same proposition (b.2).
- The docstrings of `parts.i` and `parts.ii` differ from the formal-conjectures
  ones. They do not change the propositions; the extra claim they add is
  discussed in (c).
- Two points need a build to check, and builds are outside my scope:
  - the two files import different modules (`FormalConjecturesUtil` against
    four Mathlib modules);
  - inside `namespace Erdos408`, I assume `HasDensity` resolves to
    `Erdos408.HasDensity`.

  Nothing in the statement text depends on notation outside Mathlib other than
  `HasDensity`, which `challenge.lean` defines itself.

## (c) Checklist

1. **"Almost all" quietly upgraded to "all": applicable; not present.**
   - `parts.ii` asks for density 1 for each ε and allows an exceptional set.
   - `parts.i` speaks only of densities.
   - `normal_order_rate` counts its exceptions explicitly.
2. **Exceptional sets dropped from density arguments: applicable; not
   present.**
   - The count in `normal_order_rate` keeps the exceptional set, including the
     √x term from small n. Including n = 1 and n = 2 only makes the set
     larger.
   - In `parts.ii`, each complement is an allowed exceptional set.
3. **Consequence sentences as claim surfaces: applicable; no defect.**
   - Paper line 25, "In particular … density one": not formalized, but implied
     by the count bound (b.6).
   - `challenge.lean` line 19, "Hence |f(n) − α log n| ≤ log n/log log n
     outside a set …": stated formally as the second conjunct. It does not
     rest on the derivation, and the derivation is correct anyway. For n > √x
     the threshold squared is at least about (log x)²/(4(log log x)²), and
     Chebyshev's inequality then turns the variance bound into
     O(x/(log log x)³). The n ≤ √x contribute at most √x.
   - Line 20, "Then f(n)/log n tends to α on a set of natural density one":
     stated by `parts.ii` and also implied by `normal_order_rate`. The two
     theorems' α values are not formally linked. Any α that satisfies
     `parts.ii` is unique, because two density-one sets meet in a density-one
     set, so the values must agree.
   - Lines 20–21, "its distribution function is the point mass at α", and the
     `parts.i` docstring (lines 80–81), "the point mass at the constant of
     `normal_order_rate`": **these are docstring claims only.** The Lean
     statement asserts only that some F exists. Q1 asks only for existence, so
     the formal statement matches the target. The point-mass identification is
     true as a consequence (b.4) but is not part of any formal statement.
   - Line 22, "This answers the first two questions": correct (b.7).
   - The Formulation's "trivial answer no" for the literal reading: checked,
     correct (b.5).
   - `fc_408.lean` lines 113–114, "For n ≤ 1 the quotient is 0 in Lean, which
     does not affect densities": correct.
4. **Junk values and edge cases: applicable; harmless.**
   - f(0) = 0.
   - f(1) = 1, against the paper's 0.
   - The quotient is 0 at n = 0, 1.
   - log log 1 = 0 gives a threshold of 0/0 = 0 at n = 1.
   - log log 2 < 0 makes n = 2 always exceptional.
   - The partial density at b = 0 is 0/0 = 0.
   - Small and negative x are handled by `∀ᶠ` and `Nat.floor`.

   Each effect is a finite set (no effect on densities) or a bounded additive
   constant absorbed into C (b.1, b.2, b.6).
5. **Convention drift: applicable; harmless.**
   - φ_1 against φ_0 as the starting point: n = 1 only (b.1).
   - Density counted over 0 ≤ n < b against 1 ≤ n ≤ N: equivalent (b.2).
   - "≪" read as ∃ C, eventually: equivalent (b.6).
   - Count range 3 ≤ n against 1 ≤ n: an additive 2 (b.6).
   - log is the natural log in all three sources.
   - Distribution function without right-continuity: equivalent (b.4).

## (d) Strongest attack

**Attack 1 (the strongest): the meaning of "distribution function" in
`parts.i`.**

`parts.i` requires the density of {n : f(n)/log n ≤ c} only at continuity
points of F. Suppose Q1 meant instead that this density exists for every real
c. The limit law is a point mass at α (by `parts.ii` or `normal_order_rate`).
Under that reading, Q1 would also require the set {n : f(n) ≤ α log n} to have
a natural density. That is a fine question about the sign of f(n) − α log n.
`normal_order_rate` does not settle it, since the variance bound allows typical
fluctuations of size about log n/(log log n)^{5/2} on either side.

The witness to the gap: F equal to the indicator of [α, ∞) satisfies `parts.i`
whatever happens at c = α, because α is not a continuity point.

This attack fails for four reasons:

1. The problem statement does not define the term, so the standard definition
   applies. In probabilistic number theory, a function has a distribution
   function when its empirical distributions converge weakly. That condition
   applies only at continuity points.
2. The paper restates Q1 as "has a limiting distribution" (line 7), which is
   the weak-convergence notion.
3. Under the every-c reading, a yes answer to Q2 would not settle Q1. Yet Q2 is
   posed after Q1 as the sharper question, and the problem's order assumes
   that a normal order yields a distribution function.
4. formal-conjectures documents the continuity-point reading explicitly
   (`fc_408.lean` lines 111–113).

Residual uncertainty: I cannot check Erdős's own usage in the cited sources,
which are outside the read set. A reader who holds the every-c reading would
see this defect: `parts.i` leaves out the existence of the density of
{n : f(n) ≤ α log n}.

**Attack 2: junk values in `normal_order_rate`.**

- The n = 1 term adds exactly 1 to the Lean sum, against 0 in the paper.
- n = 1 and n = 2 always satisfy the Lean exceptional predicate:
  0 < 1 and −1.891… < |1 − α log 2|.

This fails because the differences are the bounded constants 1 and 2. Both
right sides tend to infinity, and √x ≥ 1, so changing C absorbs them. The Lean
form is also the stronger one, so it cannot be easier to prove than the paper's
theorem.

**Attack 3: no formal link between the α of `parts.ii` and that of
`normal_order_rate`, or between the F of `parts.i` and the point mass.**

This fails because Q1 and Q2 ask only for existence, and any α satisfying
`parts.ii` is unique (c.3).

**Attack 4: `HasDensity` drift.**

`HasDensity` counts from 0, whereas formal-conjectures writes `S ∩ univ`. This
fails: the two are the same proposition and the same limit (b.2).

**Attack 5: trivial satisfiability.**

I looked for choices of C, α or F that would make a statement trivially true,
and found none.

- Both bounds in `normal_order_rate` beat the trivial bounds by unbounded
  factors.
- `parts.i` binds at all but countably many c.
- The sets in `parts.ii` behave genuinely for n ≥ 2.

## Verdict

- **`Erdos408.normal_order_rate`: faithful.** It is equivalent to Theorem 1.1.
  The "In particular" clause is implied rather than stated. The n = 1 and n = 2
  differences change the sum by 1 and the count by 2, which C absorbs.
- **`Erdos408.erdos_408.parts.i`: faithful.** It is equivalent to a yes answer
  to Q1 under the standard, continuity-point definition of a distribution
  function. Residual: under the non-standard every-c reading it would leave out
  the density of {n : f(n) ≤ α log n}.
- **`Erdos408.erdos_408.parts.ii`: faithful.** It is equivalent to a normal
  order on a set of natural density one, as the Formulation reads Q2. No
  "almost all" is upgraded to "all", and no exceptional set is dropped.
- **Coverage: partial.**
  - The first and second questions of Problem 408 are covered whole, the
    second under the Formulation's normal-order reading.
  - The third question, on the largest prime factor of φ_k(n) when
    k = log log n, is not covered.
  - Theorem 1.1 is covered whole by `normal_order_rate`.
