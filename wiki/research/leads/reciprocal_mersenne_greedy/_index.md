---
name: research/leads/reciprocal_mersenne_greedy
title: Greedy Search for Rational Reciprocal Mersenne Subseries
desc: |
  Route to a negative answer to Problem 257 through the greedy expansion of
  one rational such as 1/2. Exact criteria, a measure-one achievement set and
  certified checks (1/2 and 1/21 pass 20000 steps; nonempty periodic supports of
  period at most 10 give no rational of denominator below 2^1000) leave one
  gap: every later step of one orbit. Finite integer seeds extend for
  truncated multiplier sets containing 1. Seeds for unbounded initial
  segments would finish, but are unproved.
problems:
- 257
research_state: blocked
review_status: unreviewed
created: 2026-10-16T14:05:38Z
updated: 2026-10-17T21:17:13Z
---

# Greedy Search for Rational Reciprocal Mersenne Subseries

[[research/leads/_index|..]]

[[research/leads/reciprocal_mersenne_greedy/evidence/_index|evidence/]]: Exact finite checks of rational greedy prefixes, gaps, periodic supports,
multiplier carry rules and finite seeds with doubling extensions. Explicit
seeds refute nonnegative carry changes when a multiplier is added; every
set containing 1 inside {1,...,12} has a half seed, while repeated
multipliers and index-dependent sets can lose it. Every full Mersenne
rational-membership conclusion stays open.

[[research/leads/reciprocal_mersenne_greedy/multiplier_carries|multiplier_carries]]: Half expansions for at most four geometric multipliers containing 1,
an exact seed criterion and doubling extension, and the residual bounds
needed to exclude a seed's first failure. Mixed carries of a half-target
two-cycle force a borrow block but do not splice the ordinary carries.
Full-weight doubling blocks reduce exactly to the gap test and require
variable terminal carries. Seeds for unbounded initial segments, which would
give the full Mersenne half expansion, are unproved.

[[research/leads/reciprocal_mersenne_greedy/proof_sketch|proof_sketch]]: A negative answer to Problem 257 would follow from one rational's
all-future greedy survival, or half seeds for unbounded initial multiplier
segments. This sketch gives exact residual and carry criteria, finite
certificates, and the seed's doubling extension. Mixed carries restrict
half-target two-cycles but do not yet exclude them or construct a repair.
The uniform seed and all-future survival obligations remain open.

***

This lead's results that are not drawn from a cited source are Plasma AI's,
credited to Plasma AI. They are author-recorded and unreviewed.

The target is the negative answer to
[[problems/irrationality/E0257/_index|Problem 257]]: an infinite
$A\subseteq\mathbb N$ with $\sum_{n\in A}\frac1{2^n-1}$ rational, in base
exactly $2$ with the denominators exactly $2^n-1$. The sums over all
$A\subseteq\mathbb N$ form a Cantor set of Lebesgue measure one, and a rational
$q$ belongs to it exactly when its greedy expansion never meets a gap: at step
$n$ the scaled residual $2^{n-1}r_{n-1}$ must avoid a window of length about
$\frac13 2^{-n}$ just above $\frac12$. For $q=\frac12$ membership forces the
support to be infinite, because every finite subsum has odd denominator. For
any rational, by the theorem of Bang and Zsigmondy, a finite representation
can end only at step 1, at step 6 or at the order of 2 modulo a prime factor
of the denominator, so $\frac1{21}$ is not a finite subsum either.

The [[research/leads/reciprocal_mersenne_greedy/proof_sketch|proof sketch]]
holds the exact greedy, scaled, mod-one and carry criteria, the measure
computation, the termination bound, and the route with its single gap. It
also proves that a scaled residual close to a non-dyadic rational with small
denominator protects a run of later steps, which gives an explicit family
of dyadic rationals $\lceil2^JS_F\rceil/2^J$, rounding up a finite subsum
$S_F$, each passing $2J+1-\lceil\log_2D\rceil$ steps by proof alone, where
$D$ is the reduced denominator of $S_F$. Such protection never reaches
twice the step where it starts. Dirichlet's theorem supplies renewals away
from specified dyadic neighborhoods, and a gap forces preceding states into
those neighborhoods. Proving an indefinite chain of renewals remains an
unproved pointwise condition on the orbit. Its
[evidence](evidence/_index.md) certifies that $\frac12$ and $\frac1{21}$ pass
their first 20000 greedy steps, that about 62 percent of the reduced fractions
with denominator at most 200 pass their first 1000 steps, close to the share
$1/E$ a uniformly placed point would have, with every gap among them at a step
at most 12, and that no nonempty support periodic with period at most 10 has a
rational sum with denominator below $2^{1000}$.

The [[research/leads/reciprocal_mersenne_greedy/multiplier_carries|multiplier construction]]
gives an infinite half expansion for weights $\sum_{a\in C}2^{-an}$ when
$C$ contains 1 and at most three other integers. It chooses each digit from
already fixed digits and uses carries 1 and 2. Constructions for
$C=\{1,\ldots,J\}$ along unbounded $J$ would give the full Mersenne half
expansion. For each finite $C$, that page also proves an exact finite seed
criterion at a common multiple of its elements. Once a seed exists, a
backward carry recurrence on doubling blocks supplies the infinite
representation, retaining all earlier divisor contributions. The missing
input is a construction of these seeds for unbounded initial segments.
A truncated half expansion already excludes the full gaps below its level,
apart from a thin strip; this explains the transfer without ruling out the
finite construction route. The sketch's window rule
chooses each digit from already fixed digits for every multiplier set and
for the full weights. For the full weights it reproduces the certified
greedy digits of $\frac12$ through step 20000, and it fails only at an
explicit congruence coincidence among integers computed from its own digits,
which is again a pointwise condition on one orbit.

The lead is blocked. The missing input is pointwise: one rational's orbit must
avoid every later window. Raw integer carries are necessarily unbounded,
excluding an eventually periodic sequence of their literal values. The finite
periodic-support check has only its stated period and denominator coverage.
Neither excludes normalized carry invariants or every rational. The sketch
also explains why the measure calculation, a continuous fixed-point argument,
and the cited interval-filling theorem do not supply the missing input, nor
do the modulus-only Fourier bounds or the bare deformation-of-base
reformulation discussed there.
The route reopens on a structural invariant of one explicit orbit, on a
rational with an infinite support described by a finite rule and a proof of
its sum, or on an argument that certifies a rational point of the Cantor set
outside the finite subsums without following one orbit. A uniform
construction of the finite seeds is another sufficient route. The
common-multiple adjoining rule and the finitely many checked seeds do not
supply that construction. The multiplier page also records two limits on
an induction: adding a multiplier generally forces a changed seed, and
agreement of early forcing does not preserve early digits. Its explicit
fractional-coefficient gap rules out convex interpolation between solved
multiplier sets as a sufficient argument. These obstructions leave the
Boolean seed construction open. Adjoining multiplier $b$ has at most two
possible binary prefixes through $2b-1$ if the new half representation
exists; this necessary interface is proved on the multiplier page. Its
finite compatibility does not prove a continuation. Later carry changes
can be negative, as the explicit $C_4$ and $C_5$ seeds show at position
$29$, so the remaining discrete repair must allow signed changes and retain
their divisor contributions.
The same page makes the first-failure test exact: the actual finite-row
residual must never exceed the suffix capacity while remaining below the
next weight. Its carry identity retains the pending contributions; no
uniform bound is proved. A whole-word iteration constructs the seed when
its bounds collapse. A nontrivial stable pair can coexist with a seed only
beside a long run of equal digits. For initial multiplier segments
$C=\{1,\ldots,b\}$ with $b\ge4$, a half-target pair's mixed carries force
a borrow block and rejoin at its end, but the ordinary prefix carries
remain two apart and later divisor contributions still differ. The
coupled continuation and the residual-capacity invariant both remain
unproved for unbounded initial segments. Every multiplier set containing
$1$ inside $\{1,\ldots,12\}$ has a half seed, which suggests proving the
seeds for all finite multiplier sets at once. Integer multiplicities and
index-dependent multiplier sets can lose the half target, so such a proof
must use the bit coefficients of one fixed set.
A doubling construction for the full weights has two possible terminal
carries, determined by the old prefix's pending mass. The word-boundary
cases always pass; the interior choice leaves an explicit phase interval
whose avoidance is unproved. The boundary carries cannot all be fixed at
$1$. Lemma 14 of the sketch classifies exact renewals with terminal
residual $w_L/2$: their only endpoints are $2$ and $6$, so they cannot
restart an infinite construction. Finitely many fixed rational multiples
of $w_L$ also fail to give unbounded renewal positions. These restrictions
leave the variable-carry selection theorem and the uniform finite-seed
construction open.
