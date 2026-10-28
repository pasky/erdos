---
name: diophantine_problems/plasma_ai_2026_powerful_sum_complements/evidence/verify/statement_fidelity/review
title: Statement-fidelity review of the Problem 940 targets
desc: |
  Independent adversarial comparison of the frozen cubic and quartic
  complement claims with four external Lean target declarations.
tags: []
sources: []
created: 2026-10-20T15:16:31Z
updated: 2026-10-28T16:00:09Z
---

***

## Subject and independence

**Examination date:** 2026-10-20 UTC. **Role:** independent statement-fidelity
reviewer. The reviewer had a fresh context, did not author or help construct
the subject, and received the commission and governance instructions without
the author's working discussion, other reviews, or acceptance decisions.

The subject was the extraction frozen on 2026-10-20 UTC under
`library/diophantine_problems/plasma_ai_2026_powerful_sum_complements/evidence/assets/statement_fidelity/`.
The following paths, relative to that explicitly identified directory, were
read in full:

- `mathematical_subject.md`: the reproduced Problem 940 Statement and both
  reproduced Claim and Covers sections, including their consequence and scope
  sentences.
- `Challenge.lean`: both definitions and all four target types, with the
  surrounding comments distinguished from theorem statements.
- `Solution.lean`: all four exported target types and their immediate aliases.
- `Erdos940/Powerful.lean`: `Nat.Full`.
- `Erdos940/Statement.lean`: `Erdos940.Representable` and
  `Erdos940.CoinfiniteFor`.
- `Erdos940/FinalAssembly.lean`: the adapter interfaces and four final target
  types. Its short proof text was visible in the supplied extraction but was
  not audited as a proof.

The reviewer read supplied copies, not an extraction made from current
claim pages. The [subject custody record](_index.md#subject-custody) identifies
the two retained inputs and the four files preserved in the pinned external
source. The copies were not edited during this review; the verdict identifies
the supplied frozen text, not independently established custody of another
checkout. The canonical source card, current problem and claim pages, source
README, main discussion, other reviews, and excluded proof modules were not
read. No excluded mathematical communication or search exposure occurred. An
administrative correction supplied the accessible authorized dependency source
location after the original location was unavailable; it supplied no
mathematical guidance.

Governance reading comprised all of `docs/verification.md`, the statement
fidelity rules in `docs/lean_authoring.md` (with surrounding authoring and native
surface guidance), and `docs/anatomy.md`, sections “Tiers” and “Problems and
claims.” No links from those documents expanded the mathematical read set.

Imported semantics were checked in the authorized Mathlib source for the
commission's Lean 4.35.0-rc4 environment. The following are dependency-relative
paths, not additional repository subjects:

- `Mathlib/Data/Nat/PrimeFin.lean`, lines 15–85: `primeFactors`, its membership
  characterization, and the zero and one cases; additional declaration-name
  search in the same file.
- `Mathlib/Data/Set/Card.lean`, lines 620–698: `ncard`, finite-cardinality
  interpretation, the infinite-set default, and `ncard_coe_finset`; additional
  declaration-name search in the same file.
- `Mathlib/Order/Filter/AtTopBot/Basic.lean`, lines 60–90:
  `eventually_atTop` and `frequently_atTop`; additional name search.
- `Mathlib/Data/Multiset/Defs.lean`, lines 50–85 and 207–245: quotient by list
  permutation and cardinality as list length; additional name search.
- `Mathlib/Algebra/BigOperators/Group/Multiset/Defs.lean`, lines 20–95:
  additive sum semantics, empty sum, cons, and repeated entries.
- `Mathlib/Algebra/BigOperators/Group/Multiset/Basic.lean`, lines 1–65 and
  declaration-name search: import and additive-operation context.
- `Mathlib/Data/Set/Finite/Basic.lean`: targeted search returning
  `finite_lt_nat` and a use of it. Targeted searches of
  `Mathlib/Order/Interval/Finset/Nat.lean` and
  `Mathlib/Data/Set/Finite/Lemmas.lean` returned no relevant declarations.

This is definition and theorem-interface inspection, not verification of
Mathlib proofs. The standard library was authorized but not read. Build
configuration, toolchain and dependency lock files, native manifests,
Comparator implementation and output, and proof replay records were outside
the supplied subject and were not inspected. The stated environment version is
commission information, not a newly verified pin.

The independent reasoning is retained below. No mathematical computation,
generated witness, or executable check is used in the verdict, so no rerun
program is required. The four declarations are assessed for meaning only;
their proof correctness, buildability, axiom closure, and acceptance remain
separate questions.

## Restatement and per-target findings

For a fixed exponent \(r\), let \(R_r\) consist of the nonnegative integers
expressible as a finite sum of at most \(r\) nonnegative integers \(s\), with
repetitions allowed, such that every prime divisor \(p\) of \(s\) satisfies
\(p^r\mid s\). Let
\(A_r(N)=\#\{n\in\mathbb N:n<N,\ n\notin R_r\}\).

### Cubic density

`Erdos940.cubic_complement_density` in both `Challenge.lean` and
`Solution.lean` says that there exist natural numbers \(C>0\) and \(N_0\)
such that \(N\le C A_3(N)\) for every natural \(N\ge N_0\). This is
equivalent to positive lower natural density of the complement. It covers the
full density conclusion of the frozen cubic Claim; its infinitude consequence
is considered separately below.

The strongest attempted mismatch was that a natural reciprocal constant might
encode a stronger result than an arbitrary positive real lower density, or
that an infinite subsequence of favorable cutoffs might suffice. Neither
occurs: choose any positive real \(\delta\) strictly below the positive
liminf, and an integer \(C\ge1/\delta\). Eventually
\(A_3(N)/N\ge\delta\), yielding the displayed inequality. Conversely, the
target gives liminf at least \(1/C\). `eventually_atTop` requires every
cutoff beyond one threshold. No statement mismatch was found.

### Quartic density

`Erdos940.quartic_complement_density` in both files says that there exist
\(C\in\mathbb N\), \(C>0\), and a natural threshold \(N_0\) with
\(N\le C A_4(N)\) for every natural \(N\ge N_0\). This is the frozen
quartic Claim's displayed assertion. Allowing its prose threshold to be an
integer makes no difference: replace it by its maximum with zero when cutoffs
are natural. The same real-density argument gives precisely its first
consequence.

The strongest attempted mismatch was an implicit distinct-summand convention
or an exact-four-positive-summand condition, each of which would change the
represented set. The formal existential uses multisets, counts occurrences,
and bounds their cardinality above by four. It permits the four ones summing
to four, and the singleton containing one. Neither hidden restriction is
present. No statement mismatch was found.

### Cubic infinitude

`Erdos940.cubic_large_integers` in both files says it is false that all
sufficiently large natural numbers admit a multiset representation of the
specified kind with cardinality at most three. Equivalently, for every
\(M\in\mathbb N\) there is an \(x\ge M\) outside \(R_3\).
This is infinitude of the positive nonrepresentable integers, as asserted in
the cubic Claim and Covers section.

The strongest attack was that negating an eventual statement might merely
produce one exception, or might count only zero. Negating
\(\exists M\,\forall x\ge M\) gives arbitrarily large exceptions. Any
finite set of naturals is bounded; zero is representable by the empty
multiset. Thus neither proposed weakening survives. This target covers the
infinitude consequence, not the cubic density conclusion by itself.

### Quartic infinitude

`Erdos940.quartic_large_integers` in both files has the same quantifier
structure with cardinality at most four and exponent four. It asserts an
unbounded, hence infinite, set of positive integers outside \(R_4\), exactly
the frozen quartic Claim's second consequence and its Covers section.

The strongest attack was a domain substitution making the conclusion trivial
by counting negative integers, or treating four copies of one as only one
summand. Every quantified object is natural, and multiset cardinality is list
length, so neither mechanism occurs. This target alone does not assert density.

For all four targets, the external premise is the ordinary interpretation of
the inspected definitions and imported interfaces. No result from a native
L-claim is used to justify this semantic comparison. The actual mathematical
proofs of the four targets have not been assessed, and no dependency-standing
verdict about those proofs is made.

## Weakest semantic steps and boundary attacks

### 1. Powerful numbers and the representation model

For \(s\ne0\), `Nat.mem_primeFactors` says exactly that membership means
primality and divisibility. Thus `Nat.Full r s` is the required prime-divisor
condition, with no bound on which primes are tested. At zero, the prime-factor
set is empty, so `Nat.Full r 0` is true. This still agrees with the direct
divisibility formulation: every prime power divides zero. At one there are no
prime divisors, so one is full. These conventions do not rely on the
conclusions under review.

As concrete exponent probes, eight is 3-full but not 4-full; sixteen is
4-full; \(72=2^3 3^2\) is not 3-full because \(27\nmid72\). The
definition checks the power of each prime dividing the whole number, not
whether the number is itself an exact \(r\)-th power.

`Multiset` is a quotient of finite lists by permutation. Its cardinality is
list length, and its sum retains multiplicity. Thus three copies of one
represent three cubically, and four copies represent four quartically.
Replacing multisets by finite sets would lose these representations: the only
positive full number below eight in the cubic case, or below sixteen in the
quartic case, is one. The target does not make that substitution. Conversely,
the singleton containing one is permitted, refuting an
exact-number-of-positive-terms reading.

Deleting every zero from a representing multiset preserves its sum and the
fullness of its other entries while reducing its cardinality. For positive
totals the remaining multiset is nonempty. Conversely a positive-summand
representation is already a natural-summand representation. Consequently the
cubic Claim's positive convention and the quartic Claim's zero-removal sentence
are faithful. An empty multiset represents zero. No convention excluding one,
requiring distinct summands, or allowing signed summands is encoded or needed.

### 2. Counting and positive lower density

`Set.ncard` has a default value of zero on infinite sets, so finiteness cannot
be presumed merely from the notation. Here the counted set is a subset of
\(\{0,\ldots,N-1\}\), hence finite with cardinality between zero and
\(N\). The inspected `ncard_eq_toFinset_card` and `ncard_coe_finset`
interfaces give its ordinary finite cardinality. The infinite-set default
therefore cannot weaken or falsify the intended count.

For \(N\ge\max(N_0,1)\), casting the natural inequality to the reals and
dividing by the positive \(CN\) yields \(A_r(N)/N\ge1/C>0\). All
exceptions lie before one fixed threshold; the constant is chosen before the
eventual quantifier, not separately for each cutoff. Conversely a positive
liminf yields a uniform bound by the argument given for cubic density.
Changing the count to positive integers at most \(N\) changes it by at most
one, so it leaves the lower density unchanged. The zero cutoff has count zero
and inequality \(0\le0\); it creates no special obligation at infinity.

This argument also independently checks each density-to-infinitude consequence:
if there were only \(K\) missing numbers, then \(A_r(N)\le K\) for every
\(N\). Taking \(N\) beyond both the threshold and \(CK\) contradicts
\(N\le C A_r(N)\).

### 3. Infinitude and the comparison boundary

Unfolding `Representable` in each final infinitude interface gives exactly the
multiset existential printed in its Challenge and Solution target. Unfolding
`CoinfiniteFor` gives infinitude of the complement of the same represented
set. A finite complement has a largest element, or is empty, and therefore
implies eventual representability. An eventual representation threshold bounds
the complement by the finite interval below it. This establishes both
directions of the intended equivalence independently of the adapter proof.

The definitions of `Nat.Full` and `Representable` in the Challenge match their
frozen solution-side definitions. Each density target also matches its
`FinalAssembly` exported type, including the exponent, strict cutoff, `ncard`,
positivity condition, inequality direction, and order of quantifiers. Each
Solution declaration aliases the correspondingly named final theorem. There
is no extra visible hypothesis, free parameter, or strengthened conclusion in
these signatures.

The extraction does not include definitions of `missingCount` or
`HasPositiveLowerDensityComplementFor`, nor the imported cubic and quartic
proof modules. Their internal correspondence and the actual execution of
Comparator have not been certified. The direct target signatures have the
intended meaning regardless of those proof dependencies; whether the supplied
proofs actually establish the signatures is reserved for mechanical checking
and proof review.

## Checklist

The following verdicts apply to all four targets unless a row specifies the
density pair. “Not relevant” is a scope judgment for this statement audit, not
a finding that an unread proof has no such defect.

| Repository checklist item | Relevance and finding |
| --- | --- |
| Quantifiers and scope | Relevant. Both exponents are fixed. Density is eventual at every cutoff, with one positive constant; infinitude negates eventual representability. No all-cutoff, density-zero, or exponent-at-least-five conclusion appears. |
| Circularity | Relevant at the statement boundary: no target is assumed in its exported type. Circular proof use and induction are not relevant to this proof-excluding audit and remain unchecked. |
| Model and convention changes | Relevant. Prime-divisor semantics, zero, one, multiset multiplicity, natural domains, and zero deletion were checked above. No mismatch found. |
| Finite and statistical overreach | Not relevant as evidence: the verdict uses definitions and mathematical equivalences, not samples or finite verification. Boundary examples are counterexample probes, not universal proof certificates. |
| Uniformity | Relevant to the density pair. Each exponent has its own fixed positive integer constant and threshold; no common constant for arbitrary exponents or exchanged limits is claimed. |
| Extremal conclusions | Relevant only to the lower-density interpretation. The ratios lie in [0,1]; the lower bound is in the same ratio units. No sharp constant, attained optimum, or density limit is asserted. |
| Consequences and composition | Relevant. Both density-to-infinitude implications and both Covers restrictions were checked separately. Signatures cross the visible adapter boundary faithfully; hidden proof dependencies remain outside scope. |
| Computation | Not relevant. No numerical certificate, cap, enumeration, or arithmetic program supports this verdict. `ncard` is a mathematical finite cardinality here. |
| Reproduction | Not relevant to the commissioned semantic comparison. No build, replay, Comparator success, or cached result is claimed or relied on. |
| Source and verdict fidelity | Relevant for the exact frozen Claim and Covers texts: conclusions match. Bibliographic attribution, manuscript Corollary 1.2, historical priority, and current open-problem status were not verified. Other reviewers' rulings were excluded. |

For completeness, the canonical failure modes and named patterns in
`docs/verification.md` were also classified individually:

| Canonical mode or named pattern | Relevance and finding |
| --- | --- |
| “Almost all” upgraded to “all” | Relevant. The density targets retain an eventual threshold and assert only a lower bound on the complement; neither asserts every integer is missing. |
| Induction presupposing termination | Not relevant to target meanings; proof bodies are not audited. |
| Probabilistic or averaging heuristics as proof | Not relevant: no such argument supports this semantic verdict. |
| Circular use of an equivalent target | Relevant at exported types, where no such hypothesis appears; internal proof circularity is unexamined. |
| Exceptional sets dropped from density arguments | Relevant. The threshold, strict cutoff, and possible endpoint discrepancy were accounted for. |
| Finite verification exceeding base-case coverage | Not relevant: finite probes are used only to distinguish definitions, never to establish the theorems. |
| Relaxed or averaged convergence substituted for actual objects | Relevant. The target counts the actual complement of the multiset sumset, not a surrogate set. |
| Model-class transport instead of entailment | Not relevant: no classification of axiom systems occurs. The relevant definitional transport was established directly. |
| Uniformity over an infinite family from finite instances | Relevant to scope. Only r=3 and r=4 occur, with separate constants; no inference to arbitrary r is made. |
| Extremal claims in their own units | Relevant to density: the lower bound concerns A_r(N)/N itself; no sharpness claim occurs. |
| Consequence sentences as claim surfaces | Relevant. Positive lower density and infinitude were checked individually; the stronger density-zero question is expressly excluded. |
| Carry hypotheses used by quantified arguments | Relevant. Positive C and bounded counting intervals are present; no infinite-cardinality default or missing boundedness is used in the semantic derivation. |
| Composition inherits unproved premises | Relevant as a limitation. Visible exported types match; no assertion is made that unread imported proofs discharge their premises. |
| Reproducibility notes are claims | Not relevant to this verdict: no execution or replay note is verified. Challenge/Solution comments about Comparator remain outside the finding. |
| Verifier quotations are claims | Not relevant: no other verification report or standing quotation was provided or used. |
| Verdict words spelled in full | Relevant to this report. Its scoped result is stated explicitly below; it makes no whole-proof refutation-failed claim. |
| Certified-bracket functions fail loudly | Not relevant: no bracket routine or numerical enclosure is involved. |
| Harness leg with no failing input | Not relevant: this report has no computational harness. Its mathematical distinction probes would detect exclusion of one, discarded multiplicity, or wrong prime exponents. |
| Gate reading caches instead of re-running | Not relevant: the verdict relies on no gate or cached success. Mechanical validation remains unverified here. |

The neighboring statistical-independence discipline is inapplicable because no
statistical inference is made. Coverage is explicitly limited to the inspected
mathematical statement surfaces and imported semantic interfaces.

## Premises, coverage, and verdict

No local theorem is consumed as an established mathematical premise of this
statement comparison, so a live L-claim ledger reading is unnecessary and was
not performed. The relevant external interfaces are precisely the Mathlib
definitions and theorem statements listed above. Their proofs were not
reconstructed. The four target proofs, their transitive axioms, and their
build and replay environment are unexamined.

**Verdict: no statement-fidelity defect found for any of the four frozen
Challenge/Solution targets.** The cubic density target covers positive lower
density as stated in the frozen cubic Claim. The quartic density target covers
the frozen quartic counting assertion and its lower-density consequence. The
two infinitude targets cover the corresponding first-question conclusions at
their respective exponents. The two definitions and visible final adapter
types preserve these meanings.

No correction to the reviewed mathematical statements is required. This
finding does not cover a progression theorem, density zero of representable
integers, an exponent beyond four, manuscript attribution, priority, or the
truth of comments about current mathematical knowledge. In particular, a
positive density complement need not have density one: these targets cannot
settle the density-zero question for the represented set. The cubic Covers
discussion of a progression is a scope explanation, not a progression result
proved by these targets.

The report awards no tier or acceptance and does not certify proof correctness.
Any acceptance that uses it still requires its distinct grading and the
separate mechanical evidence required by repository policy. The missing
proof-internal definitions and Comparator implementation are limitations of
this review, not demonstrated errors in the target statements.
