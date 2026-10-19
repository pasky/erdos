---
name: research/erdos_25/dyadic_splitting
desc: Exact delayed binary lifts and their equivalence to the private-endpoint obstruction.
tags: [reductions, counterexamples, endpoints]
sources: []
created: 2026-09-22T01:50:00Z
updated: 2026-09-24T22:13:01Z
---


# research/erdos_25/dyadic_splitting

***

The statements below are proved reductions, **not** a counterexample.
They show that an infinite, measure-preserving binary refinement does not
bypass the positive-private-witness problem in
[unresolved estimates](unresolved_estimates.md#private-witness-reduction-for-endpoints).

## Exact delayed lift

Let the base moduli $q$ be distinct and odd, with normalized residues
$0\le a_q<q$. Replace the base class by
$$
 a_q+2^{k-1}q\pmod{2^kq},\qquad k\ge1.
 \tag{1}
$$
All the new moduli are globally distinct: their odd part identifies $q$
and their 2-adic valuation identifies $k$. The numerator displayed in
(1) is already between zero and $2^kq$.

Inside the base cylinder, put $n=a_q+qt$. The full cylinders (1)
partition the quotient values with finite 2-adic valuation. Their omitted
2-adic fiber has Haar measure zero. Thus the countable full lifted union
has the same Haar measure as the full base union, also when base
cylinders overlap.

For a positive integer $t=2^v u$, $u$ odd, its unique lifted class has
modulus $2^{v+1}q$. It is active exactly when
$$
 a_q+qt\ge 2^{v+1}q,
$$
equivalently $t\ge2^{v+1}$, because $0\le a_q/q<1$. This is equivalent
to $u\ge3$. Consequently the delayed lift misses precisely the
power-of-two quotients of each individual base class. The lift is a
subset of the delayed base union.

Write $L=B_{\rm base}\setminus B_{\rm lift}$. If $n\in L$, then for
**every active base class** containing $n$, its quotient is a power of
two. This qualification is essential when the base classes overlap.

## Positive loss gives positive private endpoints

Let $\beta$ be the full base-union Haar measure. The established
compression bound gives
$$
 \sum_{q\le X}\frac1q\le\beta H_{\lfloor X\rfloor}.
 \tag{2}
$$
Thus points in $L$ whose chosen witnessing quotient is $2^v$ with
$v\ge R$ have harmonic mass at most
$$
 2^{1-R}\beta H_{\lfloor X\rfloor}.
 \tag{3}
$$
If $L$ has positive upper logarithmic density, some fixed $v$ therefore
gives a positive-upper-logarithmic-density set of points
$n=a_q+2^vq$. Restrict further to one residue modulo $2^{v+1}$, keeping
positive upper logarithmic density. Give each selected point modulus
$Q_q=2^vq$. These moduli are distinct and $Q_q\le n<2Q_q$.

Each cylinder $[n]_{Q_q}$ contains only its own selected point. Indeed,
another selected point $m$ in this cylinder has the form
$m=a_q+2^wq$ if $m\ge q$, since it lies in $L$. Congruence modulo
$2^vq$ implies $w\ge v$; if $w>v$, then $m-n$ has exact 2-adic
valuation $v$, contradicting the restriction modulo $2^{v+1}$.
If $w=v$, then $m=n$. The only possible point of the base cylinder
below $q$ is $a_q$, and it also differs from $n$ by an integer of
exact 2-adic valuation $v$. Thus the selected witnesses are globally
private.

Conversely, any positive-upper-logarithmic-density private family
$q\le r_q<2q$ can be reduced to one with odd moduli. The witnesses whose
moduli are divisible by $2^R$ have harmonic mass at most
$$
 \sum_{\substack{q\le X\\2^R\mid q}}\frac1q
 \le2^{-R}H_{\lfloor X\rfloor}.
$$
Choose a fixed valuation $v_2(q)=v$, and then a fixed witness residue
$b\pmod{2^v}$, retaining positive upper logarithmic density. Write
$q=2^vu$, $r_q=2^vs_u+b$. The moduli $u$ are odd and distinct,
$u\le s_u<2u$, and privacy is preserved. Affine rescaling preserves
positivity of upper logarithmic density.

For this odd family set $a_u=s_u-u$. Its private witnesses all have
quotient one. No witness belongs to another base cylinder, and the lift
(1) misses its own quotient-one witness. Hence its loss contains the
entire private witness set. This proves the equivalence:

> Every binary lift (1) has logarithmically null loss if and only if every
> distinct-modulus private family $q\le r_q<2q$ has logarithmic density zero.

The endpoint assertion remains unproved.

## Arbitrary 2-adic splitting centers give the same obstruction

One may instead omit any chosen quotient fiber $c_q\in\mathbb Z_2$.
At level $k$, use the unique residue modulo $2^k$ agreeing with $c_q$
in the first $k-1$ bits and disagreeing in the next bit. As before, the
full lifted union agrees with the base cylinder up to a null set, and
all lifted moduli are distinct.

The positive quotients missed by delayed activation are exactly
$$
 T(c_q)=\{2^j+(c_q\bmod2^j):j\ge0\}.
 \tag{4}
$$
To check this, let $2^j\le t<2^{j+1}$. The first disagreeing bit gives
an inactive class precisely when $t\equiv c_q\pmod{2^j}$; equality
$t=c_q\in\mathbb Z_2$ is omitted altogether and satisfies the same
condition. There is exactly one such $t$ in this dyadic interval.
In particular
$$
 \sum_{t\in T(c_q)}\frac1t\le2,
 \qquad
 \sum_{\substack{t\in T(c_q)\\t\ge2^R}}\frac1t\le2^{1-R}.
 \tag{5}
$$

Equations (2) and (5) show that positive upper logarithmic loss supplies
a positive-mass set $E$ with one selected point $r_q$ per modulus and
$q\le r_q\le Kq$, for some fixed $K$. Greedily retain these points in
increasing modulus order, rejecting a point if it lies in an earlier
retained cylinder. Charge a retained point also to itself. A retained
point $r_q$ receives total harmonic mass at most $2/q\le2K/r_q$, by
(5): every later rejected endpoint is at least
$q$, so no inactive root is involved. For every $X$, all endpoints
of $E\cap[1,X]$ are charged to retained points at most $KX$. Hence
$$
 H_E(X)\le2K H_{E'}(KX).
$$
The retained first-kill endpoints $E'$ have positive upper logarithmic
density. The finite coloring and quotient rescaling already proved in
[the private-witness reduction](unresolved_estimates.md#private-witness-reduction-for-endpoints)
give a positive-density private family in $[q,2q)$. Thus nonzero
splitting centers do not evade the same endpoint problem.

## Why a positive private family would settle the original problem negatively

If $E=\{r_q\}$ were such a private family with upper logarithmic density
$\alpha>0$, let $B$ be its own delayed congruence union and $\beta$ its
limiting periodic density. For every finite prefix $B_F$, its
intersection with $E$ is finite. Since $B\supseteq B_F\cup E$,
$$
 \overline{\operatorname{ld}}(B)\ge d(B_F)+\alpha.
$$
Letting the prefix grow gives $\overline{\operatorname{ld}}(B)\ge
\beta+\alpha$. The cutoff-preserving subfamily extraction in
[basic reductions](basic_reductions.md#why-the-finite-periodic-candidate-is-the-right-universal-target)
then gives a system whose logarithmic density does not exist.
No positive-density private family has been constructed here.
