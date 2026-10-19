---
name: research/small_maximal_sidon_attack/integer_transfer
title: Integer transfer and the carry
desc: |
  Why the exact group constructions do not transfer to integer intervals:
  in an anchored Singer lift the main-type blocking triples have pointers
  shifted by carries. Equal residues give one coherence mechanism, while
  long intervals of uniquely represented differences face a separate bound.
tags: []
sources:
- problems/additive_bases/E0156
problems:
- 156
created: 2026-10-15T18:15:30Z
updated: 2026-10-15T18:15:30Z
---

# Integer transfer and the carry

[[research/small_maximal_sidon_attack/_index|..]]

***

The group constructions of
[[theory/additive_bases/L208_two_parabola_maximal_sidon/_index|L208, exact
coverage in F_q^3]] and
[[theory/additive_bases/L209_singer_level_maximal_sidon/_index|L209, exact
coverage in Z_q x H]] block every target by an identity. This page
records, with proofs, what happens to that mechanism in the integers. The
lemmas are author-recorded by Plasma AI and checked on small cases by the
[evidence program](evidence/_index.md); they bear on the gap stated in the
[proof sketch](proof_sketch.md) and settle nothing about
[[problems/additive_bases/E0156/_index|Problem 156]] itself.

## Setting

Let $q\ge3$ and let $B\subset[0,q)$ be a set of integers whose
residues form a perfect difference set modulo $q$: every non-zero residue
is $b-b'$ for exactly one ordered pair of elements of $B$. Singer sets with
$q=p^2+p+1$ are the main example. Write $D=B-B$ for the set of integer
differences, so $D\subset(-q,q)$. A **point** is an integer $u=c+qs$ with
residue $c\in[0,q)$ and height $s$. The **anchored lift** with level map
$c$ is

$$
A=B\cup\{c(s)+qs:1\le s<M\},
$$

the integer analogue of L209. Its **main-type triples** are $u+b-b'$ with
$u$ a point and $b,b'\in B$.

## The half-set lemma

**Lemma 1.** $0\in D$, $D=-D$, and for each integer $1\le d\le q-1$
exactly one of $d$ and $d-q$ lies in $D$.

*Proof.* The ordered pair realizing the residue of $d$ gives an integer
difference in $(-q,q)$ congruent to $d$, which is $d$ or $d-q$; no other
pair realizes that residue. Symmetry and $0\in D$ are immediate.
$\square$

So $D$ contains exactly one integer from each non-zero residue class in a
window of length $2q-1$. In the group $\mathbb Z_q$ the same set is the
whole group.

## The pointer lemma

**Lemma 2.** Let $u=c+qs$ and let $\rho\in[0,q)$ with $\rho\ne c$. Exactly
one integer congruent to $\rho$ lies in $u+D$, namely $\rho+q(s+\kappa)$,
where $\kappa=0$ if $\rho-c\in D$, $\kappa=-1$ if $\rho>c$ and
$\rho-c\notin D$, and $\kappa=1$ if $\rho<c$ and $\rho-c\notin D$.

*Proof.* The elements of $u+D$ congruent to $\rho$ are $u+d$ with
$d\equiv\rho-c\pmod q$, and $D$ has exactly one such $d$. It is the
integer $\rho-c\in(-q,q)$ when that lies in $D$. Otherwise Lemma 1 gives
$\rho-c-q\in D$ when $\rho>c$ and $\rho-c+q\in D$ when $\rho<c$, which
are the other two cases. $\square$

Thus the main-type triples of one point block, in each residue class other
than its own, exactly one integer, at height $s-1$, $s$ or $s+1$. In the
group $\mathbb Z_q\times\mathbb Z_M$ the same triples block the whole level
$s$; the shift $\kappa$ is the carry of the residue sum. Call
$s+\kappa$ the **pointer** of $u$ in class $\rho$. If the points of $A$ are
to block every non-member of the interval by main-type triples, then in
every residue class the pointers must reach each required height. With one
high point per height, that family has no excess of pointers; overlaps
must be compensated by existing elements or by other types of blocker.
The group construction has no carry and covers each level directly.

## Coherence

**Lemma 3.** (i) If $u'=u+q$, then in every class $\rho\not\equiv u$ the
pointer of $u'$ is one more than the pointer of $u$. Consequently, for a
residue $c\notin B$ and the progression $u_s=c+qs$, $1\le s<M$, the
main-type triples block every integer $\rho+qs$ with $\rho\ne c$ and
$2\le s\le M-2$. (ii) A strong Sidon set has at most one pair of elements
at distance $q$, and no three elements in progression with difference $q$.

*Proof.* (i) The value of $\kappa$ in Lemma 2 depends only on
$\rho-c$, which is the same for $u$ and $u'$. For the progression, the
pointers in a class $\rho\ne c$ are $s+\kappa$ for $1\le s<M$ with one
fixed $\kappa\in\{-1,0,1\}$, and these cover $2\le s\le M-2$.
(ii) Two pairs $\{a,a+q\}$ and $\{b,b+q\}$ with $a\ne b$ give the repeated
sum $a+(b+q)=b+(a+q)$, and a progression gives
$a+(a+2q)=2(a+q)$. $\square$

Thus equal residues at distance $q$ supply coherent carries, and the Sidon
property allows this once. The lemma does not classify all ways that
different triple types could give complementary coverage. When the
residues $c(s)$ vary, the pointer of a point in class $\rho$ is decided by
whether the single integer $\rho-c(s)$ lies in $D$. No uniform
complementarity rule for different residues is established here, and the
heuristic expectation is that they behave independently. Two structured
possibilities are excluded by the
[translated-difference-set note](translated_difference_sets.md): every
run of consecutive residues on which membership in $D$ is constant has
$O(p^{5/3})$ elements, and for $p$ above an explicit bound membership is
not decided by a condition $\{\rho\alpha+\beta\}<1/2$. For independent
uniform heights,
[[theory/additive_bases/L125_random_singer_lift_residual/_index|L125
proves that a linear residual remains]]. No uniform construction from
this pointer mechanism has been proved here.

## Finite observations

The [evidence program](evidence/_index.md) reproduces the following counts
for the anchored lifts in which every element of $B$ also receives one
high copy, $B\cup\{b_i+qi:1\le i\le p+1\}$, with heights assigned in
increasing or decreasing order of $b_i$, in $[1,(p+2)q]$. These lifts are
strong Sidon and block every target in the classes of $B$; the counts are
the unblocked targets.

| $p$ | $q$ | $N$ | size | increasing | decreasing |
|---|---|---|---|---|---|
| 5 | 31 | 217 | 12 | 3 | 2 |
| 7 | 57 | 513 | 16 | 0 | 17 |
| 11 | 133 | 1729 | 24 | 69 | 80 |
| 13 | 183 | 2745 | 28 | 54 | 113 |
| 17 | 307 | 5833 | 36 | 339 | 391 |
| 19 | 381 | 8001 | 40 | 288 | 405 |

The case $p=7$ in increasing order is a maximal set of 16 elements in
$[1,513]$, a finite witness only. The counts are exploratory and support no
asymptotic statement.

## Sidon difference bases and the winding lemma

A carry-free alternative would be a strong Sidon set $B$ of integers with

$$
B-B\supseteq[-L,L],\qquad |B|=O(L^{1/2}).
$$

Then every integer $x$ with $0<|x-u|\le L$, for a point $u\notin B$, is
$u+b-b'$ with $b\ne b'$, and points spaced at most $2L+1$ apart would block
an interval of length $N$ with $O(N/L)$ points. With $L\asymp N^{2/3}$ this
is the cube-root scale. Two further conditions would remain: the points
must keep $A$ strong Sidon, in particular their mutual differences must
avoid $B-B$, which contains $[-L,L]$ and about $|B|^2$ further integers up
to the diameter of $B$; and such a $B$ must exist at all.

Two observations bear on the first condition. If $B-B\supseteq[-L,L]$,
then $B$ itself blocks every integer $x\notin B$ within distance $L$ of
$B$, as $x=b_0+(b-b')$ with $b_0\in B$ and $b'\ne b_0$, so points are
needed only away from $B$. On the other hand a Sidon set of $m$ elements
has diameter at least $(1-o(1))m^2\ge(2-o(1))L$, by the Erdős–Turán bound
on Sidon sets in an interval, so points spaced at most $2L+1$ apart cannot
avoid $B-B$ merely by being spaced beyond its diameter. A greedy count with
random-like densities suggests that suitable points can still be chosen
when $|B|^2$ is a small multiple of $L$, leaving the existence of $B$ as
the main issue. That count is a heuristic, not a proof. Differences beyond
$L$ are allowed here, but the [sliding-count argument](consecutive_differences.md)
proves $L=O(|B|^{5/3})$ without a diameter assumption. Thus the proposed
quadratic-length difference basis cannot exist; the compatibility
discussion above describes a conditional mechanism whose premise fails.

Small cases do not settle the question. Among Golomb rulers with $m$ marks
and length at most $m(m-1)$, an exhaustive search by the
[evidence program](evidence/_index.md) finds the following largest $L$ with
every integer $1,\dots,L$ a difference.

| $m$ | 3 | 4 | 5 | 6 | 7 | 8 | 9 |
|---|---|---|---|---|---|---|---|
| largest $L$ | 3 | 6 | 9 | 13 | 18 | 21 | 28 |
| $L/m^2$ | 0.33 | 0.38 | 0.36 | 0.36 | 0.37 | 0.33 | 0.35 |

For $m=9$ the ruler $\{0,7,10,16,18,30,31,35,57\}$ realizes every
difference up to $28$. The ratio $L/m^2$ stays near $0.35$ in this range,
which corresponds to $|B|^2\approx 2.9L$. Longer witnesses retained in the
same program, Sidon rulers with $12$, $14$, $18$ and $20$ marks, have
initial runs $47$, $55$, $90$ and $97$, so $L/m^2$ between about $0.24$
and $0.33$; they are not claimed to be optimal. The sliding-count bound
shows that these ratios tend to zero for every family as $m$ grows.

Lifting a modular perfect difference set does not give one.

**Lemma 4 (winding).** Let $n\ge2$, let $L\ge0$ be an integer, and let
$B'$ be a finite set of at least two integers with distinct residues
modulo $n$, every non-zero residue being
the difference of at most one ordered pair of these residues. If
$B'-B'\supseteq[1,L]$, then two cyclically consecutive residues of $B'$
modulo $n$ are more than $L$ apart.

*Proof.* Let $r_1<\dots<r_m$ be the residues of $B'$ in $[0,n)$, $m\ge2$,
with cyclic gaps $g_i=r_{i+1}-r_i$ for $i<m$ and $g_m=r_1+n-r_m$, and
suppose every $g_i\le L$. The residue $g_i$ is the difference of the
consecutive pair $(r_{i+1},r_i)$ and of no other ordered pair. The integer
$g_i$ lies in $B'-B'$, say $g_i=\beta-\beta'$, and $(\beta,\beta')$ realizes
the residue $g_i$, so $\beta\equiv r_{i+1}$ and $\beta'\equiv r_i$. Writing
$\beta_i$ for the element of $B'$ with residue $r_i$, this gives
$\beta_{i+1}-\beta_i=g_i$ for $i<m$ and $\beta_1-\beta_m=g_m$. Summing
around the cycle gives $0=\sum_i g_i=n$, a contradiction. $\square$

For a Singer set modulo $q=p^2+p+1$, every non-trivial Fourier coefficient
has absolute value $\sqrt p$, because the differences cover every non-zero
residue once. If an arc $I$ of length $\ell$ misses the set, Fourier
inversion gives

$$
\frac{(p+1)\ell}{q}
 \le \frac{\sqrt p}{q}\sum_{k=1}^{q-1}|\widehat{1_I}(k)|
 =O(\sqrt p\log q).
$$

Here the geometric-sum bound
$|\widehat{1_I}(k)|\le \min(\ell,1/|\sin(\pi k/q)|)$ and summation over
$\min(k,q-k)$ give $\sum_{k=1}^{q-1}|\widehat{1_I}(k)|=O(q\log q)$.
Thus every empty arc has length $O(p^{3/2}\log p)$. By Lemma 4, any
integer lift of a Singer set satisfies $B'-B'\supseteq[1,L]$ only for
$L=O(q^{3/4}\log q)$, far below the $L\asymp q$ that the alternative needs.

## Reopening conditions

The integer route should be reopened by any of the following.

- Several translates or distinct types of blocker covering one another's
  gaps, with the complete union remaining strong Sidon. A single
  quadratic-length difference basis is excluded by the
  [consecutive-differences bound](consecutive_differences.md).
- Residues $c(s)$, possibly with more than one point per height, and a
  base for which the pointers at neighbouring heights reach every height in
  all but $O(1)$ residue classes per height, with the Sidon property kept.
  Lemma 3 shows that exact distance $q$ achieves this but can be used once.
- Maximal Sidon sets of size $O(n^{1/3})$ in every cyclic group
  $\mathbb Z_n$, combined with a mechanism that controls the single
  wraparound at $n$.
