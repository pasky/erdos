---
name: research/erdos_699/proofs/details/index_9_effective
title: "Erdős 699: index nine is effective"
desc: "Integer polynomial certificates and exact rational branch trees give an effectively computable bound for every bad triple at index nine, including all prime-position collisions."
created: 2026-09-22T07:21:00Z
updated: 2026-10-14T00:26:52Z
---

# Erdős 699: index nine is effective

[[research/erdos_699/_index|P699 research]] ·
[[problems/factorials_binomials/E0699/_index|Erdős problem 699]] ·
[[research/erdos_699/methods/details/off_diagonal_pade|Unequal Padé blocks]] ·
[[research/erdos_699/methods/details/coprime_kernels|Coprime kernel polynomials]]

***

**Theorem.** There is an effectively computable integer $N_9$ such that
any bad triple with $i=9$ satisfies $n<N_9$. Here badness means

$$9<j\le n/2,\qquad
p\nmid\gcd\!\left(\binom n9,\binom nj\right)
\quad\text{for every prime }p\ge9.$$

This uses the original prime threshold. The
[subsequent numerical proof](../../archive/previous_bounds/index_9_numerical_tail.md)
gives $N_9=10^{11514327437548}$, while a separate
[finite certificate](index_9_finite.md) excludes a lower
range. The new interval covers join both ranges and complete the case. The theorem supplies a terminating
procedure to enumerate the possible exceptional triples.

The complete [checker](../../computations/erdos_699_index_9_effective.py)
and [compressed proof data](../../computations/erdos_699_index_9_effective.json.gz)
cover all $9^4\cdot16=104\,976$ labeled root cases. The finite case division
concerns prime positions and cofactor inequalities, rather than rows $n$.

**Complete result.** The [combined proof](index_9_complete.md)
excludes every admissible bad triple at nine. The estimates below
are retained as components of that proof.

## Cofactor variables and the complete root partition

For $p\in\{2,3,5,7\}$ choose $r_p\in\{0,\ldots,8\}$ maximizing
$v_p(n-r_p)$, and set

$$P_p=p^{v_p(n-r_p)},\qquad u_p=\frac{n-r_p}{P_p},\qquad
h=n-8,\qquad e_p=\frac{\log u_p}{\log h}.$$

Every selected $P_p$ is at least $p\ge2$. Admissibility gives $n\ge20$,
so $1\le u_p\le n/2<h$ and

$$
0\le e_p<1.
$$

The retained pair estimates give 16 componentwise minimal lower vectors
for $(e_2,e_3,e_5,e_7)$. The
[baseline checker](../../computations/erdos_699_index_9_baseline.py)
reconstructs these vectors from their exact rational source endpoints and
enumerates every position assignment, preserving prime labels. Its 70
integer polynomial certificates cover 104,059 root cases. The remaining
917 cases are listed explicitly in the
[baseline data](../../computations/erdos_699_index_9_baseline.json).

Twelve remaining cases have coinciding positions. They are exactly
$r_2=r_5$, with $(r_2,r_3,r_7)$ a permutation of $(0,1,2)$, and lower vector

$$(.3296,.0505,.3931,0)
\quad\text{or}\quad(.3296,.0502,.3931,.0505).$$

They are included in the final proof trees. No collision case is inferred
from a distinct-position calculation.

## Polynomial inequalities, including collisions

Let $F(X,Y)$ have multiplicity at least $m_t$ at every nonnegative integer
point $x+y=t<9$. The Kummer divisibility argument and the bound on the
unselected small-prime powers give, under badness,

$$\prod_{t=0}^8(n-t)^{m_t}
 \le (8!)^{\max m_t}|F(j,n-j)|
       \prod_{p<9}P_p^{m_{r_p}},$$

provided $F(j,n-j)\ne0$. At a row occupied by several selected primes,
their product divides $n-r$ and is at most $n$. Let $S$ be the occupied
rows, and let $U$ be the primes that are alone at their selected row.
If $F$ has degree at most $D$, then, above its computable coefficient
threshold, badness necessarily implies

$$\boxed{\quad
\sum_{p\in U}m_{r_p}e_p
 \le D-\sum_{t\notin S}m_t+10^{-6}.
\quad} \tag{1}$$

Thus a collision group has total capacity one and contributes **no**
cofactor term to the left side of (1). This deliberately uses only that
capacity bound. In addition, a group $G$ at a common position satisfies

$$\prod_{p\in G}u_p
 =\frac{(n-r)^{|G|}}{\prod_{p\in G}P_p}
 \ge(n-r)^{|G|-1}\ge h^{|G|-1},$$

and hence

$$
\sum_{p\in G}e_p\ge |G|-1. \tag{2}
$$

For the twelve collision cases, (2) is $e_2+e_5\ge1$. Equations (1) and
(2), with the occupied-row constant in (1), are the exact inequalities
used by the checker.

The polynomials have explicit coordinate, row, and diagonal factors,
followed by a residual symmetric interpolation problem. The
[additional polynomial checker](../../computations/erdos_699_nine_polynomial_cuts.py)
and [data](../../computations/erdos_699_nine_polynomial_cuts.json)
retain their integer multiplicities, modular ranks, and coefficient bounds.
The proof uses 58 of these additional certificates together with the
70 baseline certificates. All required ranks were computed over
$\mathbf F_{251}$; the largest matrix is $18494\times18496$.

Two nonvanishing constructions are used. A surjective degree-$d$ jet map
provides the established degree-$(d+1)$ family. Alternatively, two
full-degree kernel polynomials whose reductions are coprime lift to
coprime rational polynomials of degree $d$. Their common zero set has an
explicit resultant height bound. This second construction saves one degree
and is essential for the tightest retained certificates. The
[coprime-kernel lemma](../../methods/details/coprime_kernels.md) supplies the
integer lift and resultant bounds; the actual modular kernel vectors and
gcd checks are retained.

Diagonal factors are permitted because the central column is impossible.
If $n=2j$ were bad, each of $n-1,n-3,n-5,n-7$ would have all prime factors
in $\{3,5,7\}$: any prime at least 11 in one of these odd factors creates
a central Kummer carry. Each of 5 and 7 divides at most one of the four
factors, since their pairwise distances are 2, 4, or 6. At least two would
therefore be powers of 3 exceeding 12 and at distance at most 6. Distinct
such powers differ by at least 54, a contradiction.

All coefficient and coprime-basepoint bounds used in the proof are
satisfied once

$$
h\ge10^{5\,109\,634\,000\,001}. \tag{3}
$$

This is the numerical bound for the polynomial part, not the full bound
$N_9$: the effective analytic source thresholds must also be included.

## Analytic alternatives and exact linear contradictions

The [source checker](../../computations/erdos_699_nine_cofactor_clauses.py)
and [compressed source data](../../computations/erdos_699_nine_cofactor_clauses.json.gz)
retain 790 directed interval certificates from the unequal-block Padé
argument. They have the form

$$
\sum_p\max\{0,g_p+w_pe_p\}\ge T,\qquad T>0, \tag{4}
$$

with exact rational $g_p,w_p,T$. Each certificate reserves a strict
analytic margin. Its coefficient-gcd lower bound is a finite rational
sum, so the starting height is effectively computable. Pair estimates
apply independently of the other positions; product estimates are used
only when the checker verifies their required integer position identity.
Four previously retained ordinary cofactor alternatives are also used.

To branch on (4), choose the nonempty set of its nonnegative summands.
The sign conditions and their sum give rational linear inequalities.
Every branch is retained, including equality boundaries. At each leaf,
positive rational multipliers annihilate every variable coefficient while
making the combined right side strictly negative. Thus the leaf would
imply $0<0$. These are exact Farkas certificates, checked using integer
and rational arithmetic. Floating point linear programs were used only
to find candidates.

The final forest has 31,615 nodes and 23,973 Farkas leaves. It closes every
one of the 917 residual roots, including all twelve collision cases.
Together with the independently reconstructed baseline partition, this
covers all 104,976 root cases. Every input estimate has a computable
threshold, and only finitely many are used. Taking their maximum, the
polynomial threshold (3), and the elementary initial bounds proves the
theorem.

The ordinary checker run reconstructs the directed sources and verifies
all exact coverage identities. Its optional `--ranks` flag repeats the
modular rank calculations already performed during construction. The
compressed artifacts are ordinary gzip files read by Python's standard
library. The remaining dependencies are pinned in the retained
[interpolation requirements](../../evidence/assets/erdos_699_interpolation_requirements.txt).
