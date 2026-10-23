---
name: arithmetic_functions/plasma_ai_2026_divisor_counts_shifted_factorials/evidence/verify/statement_fidelity/report
title: Whole-statement fidelity examination
desc: |
  A fresh-context review finds both density statements faithful, with explicit
  transfer for negative floors and finite prefixes; proof validation is separate.
tags: []
sources: []
created: 2026-10-20T18:35:14Z
updated: 2026-10-20T18:35:14Z
---

# Whole-statement fidelity examination

***

## Subject and independence

Examination date: 2026-10-20. The reviewer worked in a fresh context,
independently of the authors, with a charge to refute the correspondence and
with no prior examination supplied. The subsequent grader is a distinct role.
This report concerns statement fidelity only; it does not audit the mathematical
proof, validate compiled declarations, report a kernel replay, or assign a
verification tier.

The owning source directory is
`library/arithmetic_functions/plasma_ai_2026_divisor_counts_shifted_factorials/`.
Paths below beginning with `evidence/` are relative to that directory. The
frozen subject is the Statement of
`wiki/problems/arithmetic_functions/E0420/_index.md` as supplied in
`evidence/assets/statement_fidelity/extraction/problem_statement.md`, dated
2026-10-20, together with the extracted declarations listed below. The original
problem page was not opened.

The allowed extraction files were all read in full: `assignment.md`,
`problem_statement.md`, `challenge.lean`, `statement.lean`, `solution.lean`,
`lean-toolchain`, `lake-manifest.json`, `comparator.json`, and
`report_contract.md`, all under
`evidence/assets/statement_fidelity/extraction/`. The source archive was not
opened. The solution imports `Erdos420.FinalAssembly`, but that module and the
bodies of `parts_iii_proved` and `parts_ii_proved` were not read. The source
card, metadata, proof note, previous or sibling reviews, research notes, build
and replay output, and other corpus pages were not inspected. No web research or
numerical computation was used.

The additional permitted reading consisted of targeted definitions and theorem
interfaces in the pinned Mathlib version, with some adjacent implementation
lines read; the inventory is under Premises. Preloaded general repository
instructions and the commissioning message were contextual exposures outside the
extracted files. They supplied operational and reporting rules, not the
subject's standing, its proof, or any previous verdict. No additional
mathematical evidence was obtained from them. There was no other exposure
outside the allowed set. A lookup of the nonexistent standard-library path
`Mathlib/Data/Real/Defs.lean` returned no content; the actual real-number
definitions were reached through the import in `Mathlib/Data/Real/Basic.lean`.

## Restatement and clause-by-clause comparison

Write

$$
R_f(n)=\frac{\tau((n+\lfloor f(n)\rfloor_+) !)}{\tau(n!)},
\qquad n\in\mathbb N,
$$

where the natural floor is zero for negative arguments and is the ordinary floor
for nonnegative arguments. Both divisor counts are cast to real numbers before
division.

### The function F

`Nat.factorial` is defined by `0! = 1` and `(n+1)! = (n+1)n!`. `Nat.divisors m`
is the finite set of positive natural divisors of a positive integer `m`; it is
empty at `m=0`. Its `Finset.card` counts distinct divisors, rather than prime
divisors, multiplicities, signed divisors, or proper divisors. Every factorial
in F is positive, so the convention for divisors of zero is never used. In
particular, 1 divides `n!`, giving a positive denominator cardinality at every
n, including n=0. The casts preserve the natural cardinalities, and division is
real field division, not natural-number quotient or a rounded ratio.

For a nonnegative noninteger x, the shift is the unique natural k with k ≤ x <
k+1. For example, x=1.5 gives shift 1; there is no implicit rounding to nearest
integer. For x=0 the shift is zero. At n=0 the denominator is 1 and the
numerator is the divisor count of the factorial of the natural floor; F need not
be 1 for arbitrary f(0). If f(n)≤0, the implemented shift is zero and F(f,n)=1.

There is a real difference from the printed integer floor at negative inputs:
for n=2 and f(2)=-1/2, the printed expression, where defined, is
τ(1!)/τ(2!)=1/2, whereas the Lean expression is 1. For more negative values the
printed factorial may be undefined. Thus the definition is not an identical
totalization of the printed expression for arbitrary real-valued f at every
input. This difference does not invalidate either density statement: the
logarithmic case is nonnegative at every natural input under the supplied
extension, and the hypotheses of iii imply f(n)≥0 eventually. The required
transfer for iii is given below, rather than assuming unrestricted equality of
definitions.

Also n! divides (n+k)! for k≥0. Every divisor of the first is a divisor of the
second, so R_f(n)≥1 for all n in the implementation. This explains the natural
density region without asserting that every term is strictly greater than 1.

### Part iii

For every function f:ℕ→ℝ satisfying all three conditions

1. for all a,b∈ℕ, a≤b implies f(a)≤f(b);
2. for every real B there is an integer M such that every n≥M satisfies f(n)≥B;
3. there is an integer K such that every n≥K satisfies f(n)≤log(n);

the assertion is: for every natural N, every real x>1, and every ε>0, there is a
natural n≥N with |R_f(n)-x|<ε.

`Monotone` means nondecreasing, not strictly increasing. If the printed word
“monotonic” also permits nonincreasing functions, none of those can tend to
positive infinity: such a function is bounded above by its first value. Thus
this interpretation excludes no admissible case of that reading. The domain ℕ
samples f at exactly the integer arguments used by the printed formula. A
function given on the positive integers extends monotonically to ℕ by setting
f(0)=f(1); a function given on a real half-line restricts to such an integer
sequence. Neither continuity nor differentiability is imposed. There is no
restriction of the real-valued function to integer values.

The filter bound on log is eventual, whereas the printed bound is unqualified. A
pointwise bound on the positive domain implies the eventual bound, so the formal
hypothesis is weaker and covers a larger class. The special value log(0) does
not impose an extra constraint because the bound is eventual. `Tendsto f atTop
atTop` is divergence to positive infinity, not mere unboundedness along a
subsequence.

`Set.Ici N` is the set of indices n≥N, its image is the set of their values
R_f(n), and closure is ordinary closure in ℝ. Membership in `Set.Ioi 1` means
strictly greater than 1. The conclusion therefore says that every tail is dense
throughout (1,∞). It does not assert density in all of ℝ, exact attainment of
each real value, or convergence of the sequence. The third question inherits
(1,∞) from the preceding question; it cannot sensibly ask for density in all of
ℝ for these eventual ratios.

Taking N beyond the threshold where f≥0 makes the Lean ratio exactly the printed
ratio. Consequently the statement answers the third question affirmatively.
Explicit density of every tail looks stronger than density of the whole range,
but for a sequence and an open interval these are equivalent: removing finitely
many values cannot destroy density in that interval, as proved under Weakest
steps. The eventual upper bound is a genuine enlargement of the admissible
class, not a missing hypothesis that weakens the requested conclusion.

### Part ii

For every real x>1 and every ε>0, there is a natural n with

$$
\left|\frac{\tau((n+\lfloor\log n\rfloor_+) !)}{\tau(n!)}-x\right|<\varepsilon.
$$

Here `Set.range` means all values for n∈ℕ. Mathlib sets log(0)=0 and log(1)=0,
hence R_log(0)=R_log(1)=1. Both values are harmless boundary terms. For n≥1 the
logarithm is the ordinary logarithm and is nonnegative. The range can contain 1
while being dense in (1,∞): for any x>1 one can choose ε<x-1, which forces the
witness value into that open interval. Thus the closure formulation is
equivalent to density of the range intersected with (1,∞) in the interval's
subspace topology. It does not assert that the entire range is a subset of
(1,∞).

The zero index supplies only the value 1 and cannot supply all sufficiently
small neighborhoods of any x>1. Removing it leaves the requested
positive-integer formulation. The implication from iii to ii is valid: n↦log(n)
is nondecreasing on ℕ including zero, tends to positive infinity, and satisfies
the eventual bound by equality. Setting N=0 makes the image of `Ici 0` its
range. The monotonicity and divergence checks are rederived below; they do not
assume that real log is monotone on all of ℝ or on [0,∞).

### Challenge and solution correspondence

`challenge.lean` and `statement.lean` give the same namespace, argument and
result types, and expression defining F. The statements of both named theorems
in `challenge.lean` and `solution.lean` agree, including the explicit N
parameter, the three iii hypotheses, the closure inclusions, and the absence of
hypotheses in ii. The comparator selects precisely
`Erdos420.erdos_420.parts.iii` and `Erdos420.erdos_420.parts.ii`. The
challenge's placeholders are specifications, not accepted evidence. The
solution's references to `parts_iii_proved` and `parts_ii_proved` do not by
themselves establish their truth. No visible mismatch was found. Identity of the
entire elaborated statement dependency closure, absence of additional axioms,
and proof validity remain for independent replay; they were not inferred from
textual agreement.

## Checklist

- **Quantifiers and scope — faithful for both statements.** The quantifiers,
  eventual bound, all-tail conclusion, natural domain, and boundary cases are
  expanded above. There is no density proportion or almost-all assertion. The
  first question is outside both statements.
- **Circularity — no circular premise in the statements; proof assessment
  excluded.** Neither displayed theorem assumes its density conclusion or a
  local claim. The imported solution proofs were not read, so their circularity
  or axiom dependence is not certified here.
- **Model and convention changes — faithful for the claimed density scope, with
  a disclosed finite-prefix difference.** Natural floor changes negative inputs;
  eventual nonnegativity supplies the required transfer. Real division, positive
  divisors and the topology match the question. The log extension at zero is
  harmless as shown above.
- **Finite and statistical overreach — inapplicable.** No sample, finite
  computation, or statistical evidence is used to justify the statements or
  their correspondence.
- **Uniformity — faithful at statement level.** N, x and ε are universally
  quantified after f and its hypotheses; the witness n may depend on all of
  them. No bound uniform in f, rate of density, or uniform threshold for the
  eventual hypotheses is asserted. Proof estimates are outside scope.
- **Extremal conclusions — faithful at statement level.** Closure asserts
  arbitrarily close approximations, not attained targets or extrema. The
  endpoint 1 is excluded from the quantified targets. No sharp constant or rate
  is claimed.
- **Consequences and composition — faithful for ii and iii only.** The floor
  transfer, log specialization and finite-prefix argument are supplied below. No
  conclusion for powers (log n)^C with large C follows.
- **Computation — inapplicable to this noncomputational examination.** No
  computational proof or enclosure was used. The simple rational boundary
  example is an explicit semantic witness, not a numerical experiment.
- **Reproduction — no required computation within scope.** Reading the listed
  frozen files and interfaces reproduces the comparison. No rerun of a
  mathematical program was commissioned. Kernel validation remains separate and
  unverified here; no cached output was read or relied on.
- **Source and verdict fidelity — faithful within the frozen source.** The
  comparison uses the supplied Statement, not the source's title or assessed
  status. It distinguishes the two density questions from the divergence
  question and does not upgrade statement correspondence to proof acceptance.

## Weakest steps

1. **Floor and finite-prefix transfer.** From divergence choose M with f(n)≥0
   for every n≥M. For those n, natural floor and ordinary integer floor have the
   same nonnegative integer value, so both factorials and divisor counts
   coincide. For any desired tail start N, apply iii at max(N,M); every witness
   is a value of the printed expression on a valid input. Conversely, density of
   a whole range in an open interval implies density of each tail: fix a
   nonempty open subinterval J and a cutoff N. The values at indices below N
   form a finite set S. Choose a nonempty smaller open interval J′⊆J disjoint
   from S. Density supplies a range value in J′, necessarily at an index ≥N.
   Every neighborhood of an interior point contains such a J. This also proves
   invariance under any finite initial alteration without relying on the altered
   values being outside (1,∞).

2. **Log specialization, including zero.** If 1≤a≤b, positivity of a permits
   `Real.log_le_log`, giving log(a)≤log(b). If a=0 and b=0, equality holds. If
   a=0 and b≥1, log(a)=0=log(1)≤log(b), where the last inequality uses the
   strictly positive lower argument 1. These cases prove monotonicity on ℕ
   despite the invalid real-domain assertion that log is monotone on all
   nonnegative reals. For divergence, given a real B, `Real.tendsto_log_atTop`
   gives a real threshold T above which log(t)≥B. Choose a natural M≥max(1,T);
   then every natural n≥M satisfies the required inequality after casting to ℝ.
   The natural numbers are unbounded in ℝ. The log upper bound is equality, and
   `Ici 0=ℕ`, completing iii⇒ii.

3. **Closure versus interval density.** The inspected closure interface says
   every open neighborhood intersects the set. For x>1 and ε>0 take a smaller
   radius δ with 0<δ<min(ε,x-1). A value in that δ-neighborhood is strictly
   greater than 1 and within ε of x. This proves the relative-density
   interpretation even when the original range contains 1 or other outside
   values. Conversely, density of the intersection with (1,∞) supplies a value
   in every ambient neighborhood of an interior x. Hence neither ambient closure
   nor inclusion rather than equality creates a weaker answer to the printed
   density question.

## Strongest attack

The strongest attempted refutation was the concrete negative-floor mismatch at
n=2, f(2)=-1/2: the printed and formal ratios are 1/2 and 1. This succeeds
against an unrestricted assertion that F agrees with the printed expression for
every real-valued input function at every index. It fails against iii because
divergence makes all such discrepancies confined to a finite prefix, and the
conclusion supplies witnesses beyond any chosen cutoff. It does not apply to ii
because log is nonnegative on the natural inputs. Attempts to turn the zero
logarithm or the value 1 into a false density conclusion also fail: sufficiently
small neighborhoods about a target x>1 cannot be witnessed by 1. These are
explicit transfer arguments, not appeals to theorem names or a claimed
successful build.

## Premises and actual external reading

No local L-claim was consumed, and there is no batch acceptance order. The only
explicit mathematical hypotheses are iii's nondecreasing f, divergence to
positive infinity, and eventual logarithmic upper bound. Part ii has none. The
examination assumes the usual real numbers and their topology and interprets the
third question's density region by its immediate preceding question. Theorems ii
and iii are being compared as propositions; their proofs await independent
kernel validation.

The toolchain is `leanprover/lean4:v4.35.0-rc4`; the exact dependency selection
is retained in the extraction's `lake-manifest.json`. The following Mathlib
interfaces were inspected at that pin. Reading was targeted to the named
declarations and surrounding definitions or short proofs, not a full audit of
these modules:

- `Mathlib/NumberTheory/Divisors.lean`: `Nat.divisors`, `mem_divisors`,
  `one_mem_divisors`, `nonempty_divisors`, `divisors_zero`, `divisors_one`, and
  `divisors_subset_of_dvd`.
- `Mathlib/Data/Nat/Factorial/Basic.lean`: `Nat.factorial`, `factorial_pos`,
  `factorial_ne_zero`, `factorial_dvd_factorial`.
- `Mathlib/Data/Finset/Card.lean`: `Finset.card`, `card_pos`, and the adjacent
  cardinality monotonicity interface.
- `Mathlib/Algebra/Order/Floor/Defs.lean`: `FloorSemiring`'s floor properties,
  `Nat.floor`, and its notation; `Mathlib/Algebra/Order/Floor/Semiring.lean`:
  `Nat.floor_le`, `floor_eq_iff`, `lt_floor_add_one`, `floor_of_nonpos`.
- `Mathlib/Analysis/SpecialFunctions/Log/Basic.lean`: `Real.log`, `log_of_pos`,
  `log_zero`, `log_one`, `log_le_log_iff`, `log_le_log`, `strictMonoOn_log`, and
  `tendsto_log_atTop`.
- `Mathlib/Order/Monotone/Defs.lean`: `Monotone`, `Antitone`, and their
  restricted-domain variants.
- `Mathlib/Order/Filter/Defs.lean`: `Filter.Eventually`, its notation,
  `Filter.map`, and `Filter.Tendsto`; `Mathlib/Order/Filter/AtTopBot/Defs.lean`:
  `Filter.atTop`; `Mathlib/Order/Filter/AtTopBot/Basic.lean`: `eventually_atTop`
  and `tendsto_atTop_atTop`.
- `Mathlib/Order/Interval/Set/Defs.lean`: interval definitions and their
  order-dual generated `Ioi` and `Ici` forms;
  `Mathlib/Data/Set/Operations.lean`: image notation, `Set.mem_image`,
  `Set.range`, and `Set.mem_range`.
- `Mathlib/Topology/Closure.lean`: `mem_closure_iff`, including its proof.
  `Mathlib/Topology/Basic.lean` was inspected only at its import/header to
  locate the definition layer; no additional interface from that file is a
  premise.
- `Mathlib/Data/Real/Basic.lean`: its re-export of `Mathlib.Basic.Real.Basic`;
  `Mathlib/Basic/Real/Basic.lean`: `Real.instNatCast`, `commRing`'s natural-cast
  laws, `instIsStrictOrderedRing`, `instDivInvMonoid`, `ofCauchy_div`, and
  `instField`. These confirm exact casts and ordinary field division. No machine
  arithmetic is involved.

No standard Lean implementation file beyond these Mathlib interfaces was needed.
The elementary arguments using finite sets, real open intervals, and the
unboundedness of the natural numbers in ℝ are rederived mathematical reasoning,
not claims of additional library declarations having been read or executed.

## Verdict and grading

**Part iii: faithful.** It answers the third density question, with an eventual
upper bound that permits more functions, and with explicit density of every
tail. The natural-floor convention is not literally the printed integer floor at
negative inputs, but the hypotheses and all-tail conclusion rigorously transfer
to the intended expression wherever its eventual positive arguments are used.

**Part ii: faithful.** It answers exactly the second question, density of the
logarithmic factorial-divisor ratios throughout (1,∞). Its zero-index extension
and possible value 1 do not affect that conclusion.

**Coverage: the second and third questions only.** There is no theorem here
asserting divergence for sufficiently large C in the first question. In
particular, for fixed C>1, (log n)^C exceeds log n eventually, so iii's
hypothesis does not apply. Density for the smaller shifts supplies no growth
estimate establishing the first question. An accurate partial claim may assert
that the displayed formal statements express affirmative answers to the two
density questions, subject to separate validation of their proofs; it may not
assert a solution of all three questions or of the large-power divergence
question.

The distinct grader is to assess the report contract and the disclosed
exposures. No grading verdict, native tier, or successful replay is asserted in
this report.
