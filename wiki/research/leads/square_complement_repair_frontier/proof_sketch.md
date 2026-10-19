---
name: research/leads/square_complement_repair_frontier/proof_sketch
title: "Square complements from lifted root choices"
desc: |
  Lifted-root repair routes, a seven-adic skeleton counterexample family,
  and author-recorded comparisons with no improved square complement.
problems:
- 33
review_status: unreviewed
created: 2026-09-15T18:23:11Z
updated: 2026-10-08T01:29:59Z
---

***

## Exact target and present standing

Seek a set B of positive integers such that every sufficiently large integer
t has a representation t = n^2 + b, with n a nonnegative integer and b in B,
and limsup B(X)/sqrt(X) < 9/2 over all real cutoffs X.

This is an upper-bound improvement within
[[problems/additive_bases/E0033/_index|Erdős Problem 33]]. It does not ask for the exact
infimum. The recorded literature background includes a liminf lower bound
of 4/pi; it does not settle the limsup improvement sought here. The [recorded source context](#source-context-and-reading-limits)
makes no claim of novelty or accepted solution.

The local [[theory/additive_bases/L3_square_complement_nine_halves/_index|L3]]
construction and its complete
[[theory/additive_bases/L3_square_complement_nine_halves/_proof|all-prefix calculation]]
are author-recorded. They are used as the comparison target, not as independently
accepted mathematics. The present note records exploratory arguments.

## Initial route: seven-adic root routing

Put R = {0,1,5}. Every residue modulo 7 belongs to R + {1,2,4}.
Choose r in R such that t-r is a nonzero quadratic residue modulo 7.
For q = 7^k, k >= 1, elementary lifting and the parity condition give a
unique bounded root 0 < m_q < q of t-r modulo 2q, up to sign.
Its lift to 7q is one of

    m, 2q-m, 2q+m, 4q-m, 4q+m, 6q-m, 6q+m.

Consider the existing skeleton

    A7 = union over q = 7^k of
         {a > 0 : a = 0,1,5 (mod 2q)} intersect [4q^2/49, 4q^2].

Any positive residual at scale q of size at most 4q^2 is caught by a
smaller skeleton annulus, by divisibility of the moduli. This implication
does not help when the lifted residual is nonpositive.

The exact local task is to repair first crossings from t-m_q^2 > 4q^2
to t-m_(7q)^2 <= 0. Other representatives of the old root class may
already give a positive residual <= 4q^2. The surviving hard cases must
be specified before a repair cost can be counted.

## Gaps and next deductions

No repair set is yet claimed. The skeleton itself has the explicit infinite
family of omissions proved below. Repairs must therefore add residuals; merely
waiting for later lifts of the same center cannot close these cases. The next
route is to choose extra residue classes using the finite multiplicative
action of the lift digit, and to account for their actual radial locations.
Coverage and every intervening cutoff remain separate obligations.

A replacement construction must deliberately use roots outside the old ternary
class, change the outer skeleton, or combine both actions. For the seven-adic
route, repair choices for every middle lift must be specified before optimizing
counts. The entire prefix profile matters, especially immediately after repairs
begin.

A possible finite-state check would use the explicit ternary forced family and
all seven lift positions, recording alternative roots and residual membership.
The quantitative escape corollary rejects candidates that cannot escape enough
forced targets. A finite passing check would not establish infinite coverage or
asymptotic cost.

## A surviving quantitative result from a different route

The separate [discrete ternary barrier](triadic_one_step_barrier.md) proves
an unconditional implication for a precisely restricted repair policy.
For the target family (3q-1)^2+r-6q*ell, with q a power of 3,
r=0,1,2 and 1<=ell<=2q/3-2, every representation using the old root
class n=+/-1 (mod q) consumes a distinct new point in (q^2,9q^2).
These intervals are disjoint across scales. If the outer ternary skeleton
is retained, the resulting all-prefix limsup is at least 9/2.

This proof closes the limiting-realizability and prefix-accounting gaps for
that old-root policy without assuming radial regularity. It is not a
universal obstruction to square complements or to seven-adic repairs.

The [essential bridge interval](triadic_essential_bridge_interval.md) is a
second completed author argument. It finds q/10000+O(1) bridge points
at every sufficiently large ternary scale that cannot simply be deleted:
each supports targets uniquely represented in the original L3 set. This
does not rule out replacement constructions or deletions in other intervals.

Two attempted constructions are retained at their actual outcomes. The
[five-adic comparison](five_adic_comparison.md) has complete coverage but
upper limit 99/20, above the target. The
[seven-adic residue repair](seven_adic_repair_failure.md) has both an exact
coverage counterexample and an excessive intermediate prefix. Neither is an
improved square complement.

## A fixed-center lift cannot return after overshooting

For q = 7^k and 0 < m_q < q, every listed lift to 7q is at least m_q.
Consequently m_q is nondecreasing with q. If m_Q > sqrt(t), every later
bounded root for that same center also exceeds sqrt(t). Every nonnegative
root in that modular sign class is at least its bounded representative.
Thus no later positive residual t-n^2 has the required center congruence.
This concerns a fixed center; it does not prohibit a repair set with new
centers or new residue classes.

## An infinite family missed by the seven-adic skeleton

For any integer j >= 1, put

    q = 49^j,
    t = (25q^2 - 13q + 16)/4.

These are positive integers. The claim is that t is not a square plus an
element of A7. This is an author-recorded exact counterexample to coverage
by the specified skeleton, not a lower bound for repaired constructions.

First q = 1 (mod 8), q = 49 (mod 56), and

    t - 4 = q(25q-13)/4,

where (25q-13)/4 is odd. In particular t = 4 (mod 7). Among the centers
0, 1, 5, only center 0 is possible modulo 7: t-1 = 3 and t-5 = 6 are
quadratic nonresidues. For every power s of 7 with 7 <= s <= q, the roots
of t modulo 2s are exactly s-2 and s+2, since t = 4+s (mod 2s).

Write z = 5q/2 - 13/20. Direct algebra gives

    t - z^2 = 1431/400,
    sqrt(t) = z + epsilon,    0 < epsilon < 1/q.

The epsilon bound follows from z > 2q for q >= 49, so
epsilon = (1431/400)/(sqrt(t)+z) < 1431/(1600q) < 1/q.

At s=q the largest root below sqrt(t) is q+2: it lies between q+2 and
3q-2. Its residual is

    t-(q+2)^2 = (21q^2-29q)/4 > 4q^2.

All smaller eligible roots give still larger residuals, so the annulus at q
does not cover t.

Now suppose 49 <= s <= q/7. Every eligible root is an odd multiple of s,
plus or minus 2. Since q/s is odd, 5q/(2s) is a half-integer. For an
eligible n < sqrt(t) < 5q/2, this gives

    sqrt(t)-n > s/2 - 53/20.

Because sqrt(t)>2q, q>=7s and s>=49,

    t-n^2 > q(s-53/10)
            >= 7s(s-53/10) > 4s^2.

Thus no such s contributes a representation.

At s=7, use q=21 (mod 28). The largest eligible root below sqrt(t) is

    n = (5q-3)/2 = 9 (mod 14),

and

    t-n^2 = (17q+7)/4 >= 210 > 4*7^2.

The same n is floor(sqrt(t)), so even the unrestricted initial annulus
{1,2,3,4} at s=1 cannot represent t.

At Q=7q, the bounded root is M=3q-2. Indeed

    t-M^2 = q(-11q+35)/4

is divisible by 14q because q=49 (mod 56). Also 0<M<Q and
M>sqrt(t). The monotonicity lemma excludes all later scales. This
exhausts every power of 7 and every center, proving the omission.

For j=1 the displayed values are q=49 and t=14851. The best residuals at
s=1,7 are 210; at s=49 the best eligible root is 51 with residual 12250;
at s=343 the bounded root is 145 > sqrt(14851). These exposed integer
calculations are a witness, not output from a search program.

One can repair just this family with an added set with O(log X) points up
to X, for example by adjoining (17*49^j+7)/4. Therefore the family supplies
no positive asymptotic lower bound on the cost of all possible repairs.

## Source context and reading limits

The recorded source context is Ding, Krause, Sándor, Sun and
Zhang, *Cross representations of additive complements of r-th powers*,
[arXiv:2512.15407v6](https://arxiv.org/abs/2512.15407v6), dated 2026-07-09.
The [versioned PDF](https://arxiv.org/pdf/2512.15407v6) is the retained file.
The native
[[../library/additive_bases/ding_2025_cross_representations_additive_complements_r_th/_index|source account]]
identifies the retained source family. The source-reading record reported that
the PDF's identity matched the local LFS pointer; the pointer alone was not PDF
proof access.

The recorded visual reading covered complete printed pages 1, 3 and 4. Page 1
supplied the title, authors, version, additive-complement definition and lower-bound
background. Page 3 supplied statements of Theorem 1, Corollary 1, the definition
of T(N), Theorem 2 and the beginning of Corollary 2. Page 4 supplied the end of
Corollary 2 and the limsup question with van Doorn's reported upper construction.
This was statement and context inspection, not a reconstruction of any complete
source proof.

The cited v6 statements concern representation excess, including Theorem 2's
N^(3/4)/sqrt(T(N)) lower bound. The introductory 4/pi liminf background and
reported upper construction do not settle the exact limsup or the improvement
below 9/2 sought here. Stronger claims associated with an earlier preprint title
were not transferred to v6. The liminf background above preserves the author's dated source-context
assessment; its source proof is not reconstructed in these notes.

The search covered primary preprint context, author publication metadata
and targeted recent-announcement searches. Direct access to the problem and
discussion pages failed; indexed formulations and the primary preprint supplied
context. The bounded search does not certify absence of a solution, openness,
priority, or publication acceptance. No complete source-theorem proof or fresh
source-status determination is part of the coverage recorded here.

The barriers and explicit counterexamples use their displayed set definitions
and elementary arguments. L3's coverage and attainment proof remains a separate
author-recorded comparison. The public-source context supplies no independent
acceptance of the research arguments or of a square complement below 9/2.
