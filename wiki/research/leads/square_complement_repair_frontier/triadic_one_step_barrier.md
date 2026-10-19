---
name: research/leads/square_complement_repair_frontier/triadic_one_step_barrier
title: "A discrete obstruction to repairs using the old ternary root class"
desc: |
  A discrete 9/2 barrier for repairs retaining the ternary outer skeleton
  and its old root class, with an author-recorded quantitative escape bound.
problems:
- 33
review_status: unreviewed
created: 2026-09-15T18:23:11Z
updated: 2026-09-15T18:23:11Z
---

***

## Statement and scope

For a positive integer M define

    R_M = {a in Z_{>0} : a = 0, 1, or 2 (mod M)},

with repeated residue classes identified, and define the outer skeleton

    O = union over s = 3^k, k >= 0,
        R_(2s) intersect [4s^2/9, 4s^2].

Let B be a set of positive integers containing O. Suppose that for every
sufficiently large power q of 3, every r in {0,1,2}, and every integer

    1 <= ell <= 2q/3 - 2,

the integer

    t_(q,r,ell) = (3q-1)^2 + r - 6q*ell

has a representation t_(q,r,ell) = n^2+b with b in B, n >= 0, and
n = 1 or -1 (mod q). Then

    limsup_(X -> infinity) B(X)/sqrt(X) >= 9/2.

Here X ranges over real cutoffs and B(X) = |B intersect [1,X]|.
The hypothesis concerns only the displayed test targets. It follows, in
particular, from a policy that repairs every hard transition while retaining
the old root class modulo q. It allows arbitrary repair sets, dependence on
q, and all eligible old roots, including the root 3q-m omitted from the
earlier four-root repair model. No Jordan measurability or limiting coverage
assumption is used.

This is not a lower bound for arbitrary square complements. Such a complement
may use another root class for these targets, or may omit points of O. The
argument does not rule out either possibility. The proof below is
author-recorded, without independent acceptance.

## Exact hard targets and all eligible roots

Fix q >= 9. Put M=3q-1 and L=2q/3-2. Since q is a power of 3, L is an
integer. For 1 <= ell <= L,

    5q^2+6q+1+r <= t_(q,r,ell) <= 9q^2-12q+1+r < M^2.

The last inequality follows from t-M^2 = r-6q*ell < 0. Also
t-r = 1 (mod q). The nonnegative integers n = +/-1 (mod q) whose
squares are below t are exactly

    1, q-1, q+1, 2q-1, 2q+1.

Indeed t > (2q+1)^2, while the next eligible root is M=3q-1 and
t<M^2. At the old scale q the bounded root is q-1; its other
same-parity representative q+1 also has residual >4q^2. At every smaller
power s>=3 the bounded root is s-1, and t-(s-1)^2>4s^2. The bounded
root at 3q is M, with negative residual. Thus these are actual first hard
transitions, rather than merely points of a relaxed parameter space.

For each of the five roots the residual b=t-n^2 is as follows. The last
column is j in b = r+jq (mod 6q).

| Root n | Residual b | j |
| --- | --- | --- |
| 1 | r+9q^2-6q(ell+1) | 3 |
| q-1 | r+8q^2-4q-6q*ell | 2 |
| q+1 | r+8q^2-8q-6q*ell | 4 |
| 2q-1 | r+5q^2-2q-6q*ell | 1 |
| 2q+1 | r+5q^2-10q-6q*ell | 5 |

The congruences use q=3 (mod 6). All five residuals lie strictly in
(q^2,9q^2). For the smallest one, at ell=L and root 2q+1,

    b = q^2+2q+r > q^2.

For the largest one, root 1 and ell=1 give

    b = 9q^2-12q+r < 9q^2.

Ordering the five root squares proves the same bounds for the others.
The residuals from q-1 and q+1 are both >4q^2: their smallest values
are 4q^2+8q+r and 4q^2+4q+r, respectively.

## No candidate residual is in the outer skeleton

In the radial interval (q^2,9q^2), only the outer annuli at q and 3q
can contribute. All annuli through q/3 end by 4q^2/9; all annuli from
9q onward start at least at 36q^2.

The two candidates with j=2 or 4 lie above 4q^2, outside the annulus
at q. The other three have odd j; below or at 4q^2 their residues
modulo 2q are r+q, which is none of 0,1,2 for q>=3. Above 4q^2,
every candidate has one of the nonzero lift classes r+jq modulo 6q,
which is again none of 0,1,2. Therefore every candidate is outside O.

## Distinct targets require distinct added points

For q>=3 the fifteen classes

    r+jq (mod 6q),    r in {0,1,2}, j in {1,2,3,4,5},

are pairwise distinct. Thus a candidate value b determines r and the
root row in the table. Within a fixed row its value decreases by exactly
6q when ell increases by one. It therefore determines ell as well.

Consequently no single b can supply an allowed representation for two
different displayed targets at this q. There are 3L=2q-6 targets,
so the hypothesis forces

    |(B minus O) intersect (q^2,9q^2)| >= 2q-6.             (1)

This is a finite injection argument. In particular, oscillating or
digit-dependent choices of which candidate to retain do not evade (1)
as long as the allowed root class is unchanged.

## The all-prefix counting consequence

For consecutive powers q and 3q, the intervals (q^2,9q^2) are
disjoint. Hence the contributions forced by (1) at different scales do
not share points. Summing through q=3^k, while ignoring a fixed initial
segment, gives

    |(B minus O) intersect [1,9q^2]| >= 3q-O(k).            (2)

For completeness, the outer skeleton has

    O(9q^2) = (21/2)q+O(k).                               (3)

To verify (3), its annulus at a large scale s has length 32s^2/9 and
three residue classes modulo 2s, hence count (16/3)s+O(1).
Annuli meet only at endpoints. Summing through s=q gives
O(4q^2)=8q+O(k). The additional interval (4q^2,9q^2] belongs to
the annulus at 3q, with density 3/(6q), so it contributes
(5/2)q+O(1). These periodic counts are uniform in the indicated endpoints.

Since the points in (2) lie outside O, addition of (2) and (3) yields

    B(9q^2) >= (27/2)q-O(k).

Dividing by sqrt(9q^2)=3q and letting k tend to infinity proves the
stated limsup lower bound. This is a subsequence lower bound and therefore
applies directly to the limsup over all real cutoffs. It does not assert
a lower bound at every cutoff.

## A quantitative escape requirement

There is also a necessary condition for a general set B, without assuming
that it contains O. Let D(X)=|(O minus B) intersect [1,X]|. Let E_s
count the displayed targets at scale s that have no representation in B
using a root congruent to +/-1 modulo s. The same finite injection gives

    B(9q^2) >= (27/2)q - D(9q^2) - sum_(9<=s<=q) E_s - O(log q),

where the sum is over powers of 3. If C=limsup B(X)/sqrt(X)<9/2,
then

    liminf_(q=3^k -> infinity)
      [D(9q^2)+sum_(9<=s<=q) E_s]/q >= 3*(9/2-C).

Thus a proposed improvement must quantitatively remove outer-skeleton
mass, use other root classes on these targets, or combine both actions.
This is a necessary counting condition; satisfying it is not a coverage
proof. In particular, the other root classes can come from smaller scales.

## Relation to the existing frontier

The [prior one-step mass calculation](_index.md#a-conditional-one-step-mass-bound)
assumed a radial inclusion derived from m/q approaching 1. Its discrete-to-radial passage and its global
prefix consequence were left unproved. The explicit targets above avoid
both passages. They also include every old root below sqrt(t), so adding
the previously omitted root 3q-m to that model does not remove this
obstruction.

The existing [[theory/additive_bases/L3_square_complement_nine_halves/_index|L3]]
construction attains upper limit 9/2 while containing O and using this old-root
repair policy. Its attainment argument remains the separate author-recorded
[[theory/additive_bases/L3_square_complement_nine_halves/_proof|L3 proof]]. The new lower-bound proof does not
consume L3 or any external theorem.

The useful escape condition is concrete: a construction below 9/2 must
either alter the outer skeleton or represent at least some of these
forced targets through roots outside +/-1 modulo their corresponding q.
This statement is necessary within the displayed setup, not sufficient
for constructing an improvement.
