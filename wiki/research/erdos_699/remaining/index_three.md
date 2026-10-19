---
name: research/erdos_699/remaining/index_three
title: "Erdős 699 at index three: results and the remaining gap"
desc: "Rational abc implies cubic finiteness; unconditional residue restrictions and the nonexistence question remain open."
created: 2026-09-22T19:09:27Z
updated: 2026-10-18T10:11:24Z
---

# Erdős 699 at index three: results and the remaining gap

[[research/erdos_699/_index|Erdős 699 research guide]] ·
[The remaining indices](_index.md)

***

The question is whether every $4\le j\le n/2$ shares an odd prime
divisor between $\binom n3$ and $\binom nj$. Nonexistence and global
finiteness of counterexamples remain unproved unconditionally. The theorem
that settles all sufficiently large rows for each fixed $i\ge4$ does not
cover $i=3$.

**Conditional result.** Assuming the ordinary rational $abc$ conjecture,
there are only finitely many bad cubic triples. The [proof](details/cubic_abc.md)
uses the [integer factorization](details/cubic_abc_factorization.md) and only
the fixed $abc$ exponent $10/9$. If $K$ is a valid constant for that exponent,
then every bad row satisfies $n<10^{263}K^{69}$. This does not prove that
any bad triple exists or that the finite exceptional set is empty.

## What every counterexample would satisfy

The [cubic reductions](details/cubic_followup.md)
give

$$
n=2^h u,\qquad u\text{ odd},\qquad
n>10^{19},\qquad h\ge49,\qquad 3u^3<2^h,
\qquad 4\le j<n/2.
$$

Thus fixing $h$ already leaves only finitely many rows and columns.
The unresolved issue is uniformity as $h$ grows.

With $c=n-j$, badness implies the two exact divisibilities

$$u(n-1)\mid3jc,\qquad
u(n-1)(n-2)\mid j(j-1)(j-2). \tag{1}$$

They are equivalent to the initial prime-power residue conditions at
the odd primes dividing $\binom n3$. They are **necessary, not
sufficient**, for a counterexample: they omit higher Lucas digits.
Further necessary restrictions include

$$P^3<3n^2\quad(P\Vert n-1),\qquad
Q^2<6n\quad(Q\Vert n-2),$$

for active odd prime-power components. If $d=n-2j$ and $v$ is its odd
part, then

$$
v(d^2-3n+2)\ge u(n-1)(n-2),\qquad v>u.
$$

These exclude large prime-power components and whole families of columns;
they do not bound all rows.

There is a stronger effective restriction on the column. For every
fixed positive rational $C$, all bad pairs satisfying either

$$
j\le Cn^{3/4}\qquad\text{or}\qquad n-2j\le Cn^{3/4}
$$

form an effectively computable finite set. Thus along any infinite
sequence of distinct bad pairs, both $j/n^{3/4}$ and
$(n-2j)/n^{3/4}$ tend to infinity. The
[quotient argument](details/cubic_residue_groups.md#8-effective-finiteness-near-the-edge-and-the-center)
reduces each bounded range to finitely many explicit elliptic curves.
It uses no new finite search. Columns proportional to $n$ remain outside
these excluded ranges, so this is not global finiteness.

## All three residues must occur at the odd part of n minus two

There is a further uniform restriction. Partition the full prime-power
components of $M=(n-2)/2$ into the products

$$C_r=\prod_{\substack{p^a\Vert M\\j\equiv r\pmod{p^a}}}p^a,
\qquad r=0,1,2.$$

The initial Lucas conditions make this a partition, including the possibly
inactive component $3$, where the three residues exhaust all possibilities.
The [residue-group theorem](details/cubic_residue_groups.md) proves

$$C_0,C_1,C_2>1,\qquad
\omega\!\left(\frac{n-2}{2}\right)\ge3.$$

Thus every row for which $(n-2)/2$ has at most two distinct prime divisors
is excluded, without an upper bound on the row. The proof reduces a missing
outer group to a small square identity. Its last possible branch forces
$n=2^h$ with $h$ even, and gives contradictory values for the Jacobi
symbol $(2/C_1)$.

For each fixed $B$, the same note also proves **effective finiteness of all
bad pairs with $\min(C_0,C_1,C_2)\le B$**. A bounded group gives finitely
many conics and bounds the odd part of $n$. Writing $n=u2^\epsilon X^2$
with $\epsilon\in\{0,1\}$ and $X$ a power of two then gives finitely many
fixed genus-one equations, whose integer points can be computed.

This leaves the case in which all three groups grow without bound. No
uniform upper bound on their minimum has been proved, so this does not
establish global finiteness.

The active prime-power components of $n-1$ must also split between both
possible labels $j\equiv0,1$. If $D_0,D_1$ are the products assigned to
these labels and $\mu=3$ only when $v_3(n-1)=1$ (otherwise $1$), then

$$n-2<\frac34(\mu D_0)^3,\qquad
n-2<\frac{4}{3\sqrt3}(\mu D_1)^3.$$

The [two-label proof](details/cubic_residue_groups.md#9-both-labels-at-n-minus-one-must-have-large-groups)
uses only the endpoint divisibility. In particular, a bad row needs at
least two distinct active prime factors of $n-1$, in addition to the
three distinct odd primes required at $(n-2)/2$. One of those three
can be an inactive factor of three, so the unconditional combined count
is five distinct odd primes and at least four active primes. Both
$D_r$ groups can still grow with $n$.

## Why the original polynomial argument stops here

Removing the known power of two from $n$ leaves five congruence points
on the two lines $X+Y=1,2$. A polynomial vanishing to order $m$ at
all five has degree at least $2m$. At equality it is necessarily

$$
\lambda((X+Y-1)(X+Y-2))^m.
$$

After evaluation at $(j,c)$ and the two-adic normalization, this becomes
the same row divisor the argument started with. It has no dependence
on the column and gives an identity instead of a strict inequality.
The [five-point proof](details/cubic_weighted.md)
pinpoints the obstruction; better numerical constants do not remove it.

An analogous obstruction persists in the surface-approximation approach:
when $\log j/\log n\to1$, **arbitrary endpoint weights**, including
nonsymmetric choices, cannot give its required strict height inequality.
The [general Bezout argument](../archive/other_approaches/cubic_nested_heights.md#4-arbitrary-endpoint-weights-still-cannot-give-strictness)
extends the earlier calculation for symmetric weights.

An algebraic reformulation of (1) also produces a quadratic with an
integer root $j$ and a second root

$$
j^*=1+\frac{j(n-j)}{(n-1)(j-2)},\qquad 1<j^*<2.
$$

Its leading coefficient need not divide the next coefficient, so there
is no reason for $j^*$ to be an integer. The
[integer-moment and Vieta calculation](details/cubic_uniform.md)
records the exact denominator and explains why the proposed descent
does not follow. That note also contains useful two-prime Lucas criteria.

## Finiteness on every fixed algebraic curve

There is a stronger theorem than finiteness for fixed $h$:

> For every nonzero $F\in\mathbb Q[n,j]$, only finitely many bad cubic
> pairs satisfy $F(n,j)=0$.

The [proof on fixed curves](details/cubic_curves.md)
uses the $\{2,3\}$-integrality of

$$\frac jn,\qquad \frac{3j(j-1)}{n-1},\qquad
\frac{j(j-1)(j-2)}{(n-1)(n-2)},$$

Siegel's theorem, and a polynomial abc argument. It permits the odd part
$u$ to vary. Consequently, if infinitely many bad pairs exist, every
infinite subset is Zariski dense in the $(n,j)$-plane.

The theorem supplies no general effective height bound on those curves.
More importantly, no polynomial relation or other global nondensity
theorem has been found that applies to all bad pairs. Finiteness on each
fixed curve therefore does not establish global finiteness.

## What the elliptic curves contribute

Put $t=v_2(j)$ and $W=u(n-1)(n-2)/6$. The normalized polynomial

$$P(z)=\frac1{2^tW}\sum_{r=0}^3
\binom j{3-r}\binom c r z^r$$

is a primitive irreducible integer cubic with three roots in $(-1,0)$,
$P(1)=2^{h-t}$, and $P'(1)$ odd. The
[normalization and irreducibility proof](details/cubic_irreducibility.md)
establishes these facts uniformly.

For $D\in\{1,2\}$ chosen so that $D2^{h-t}$ is a square, the curve
$y^2=DP(z)$ has a specified rational point above $z=1$ of infinite
order. The [elliptic-curve analysis](details/cubic_elliptic.md)
proves this, but positive rank is compatible with a counterexample.
The curves vary with $(n,j)$, and primes from the column factors enter
their bad reduction. Finiteness of integral points on one curve, or
finiteness of curves with a fixed set of bad primes, gives no uniform
conclusion here.

There is a useful conditional reduction: for each fixed $B$, the bad
triples with $\operatorname{Disc}P\le B$ lie in an effectively bounded
finite set. The [conductor argument](details/cubic_conductor.md)
proves this after removing an odd twist. A uniform bound on
$\operatorname{Disc}P$ would therefore suffice, but none is known.

## The additional information still available from Lucas's theorem

If $p$ is an active odd prime and $P=p^a\Vert n-r$, write
$n=PA+r$, $j=Pk+b$, where $r\in\{0,1,2\}$. Full badness requires

$$
b\le r,\qquad k\preceq_p A,
$$

where $\preceq_p$ means digitwise comparison in base $p$. Equation (1)
retains only the first condition. The second must hold simultaneously
at every active prime and can strengthen the row-only constraints.

The [higher-digit guide](details/cubic_after_cutoff_9.md)
gives a concrete sufficient criterion. If active components
$P\mid n-1$, $Q\mid n-2$ satisfy

$$
2n/3\le PQ\le n-3,
$$

and some power $U$ of any active prime satisfies $PQ+1<U\le n$, then
the row has no bad cubic column. The initial residues force
$j\ge n-PQ-1$, whereas the higher digits force $j\le n-U$.

The missing step is to supply suitable components for all remaining
rows, or prove an incompatibility using the digit conditions without
those size hypotheses. Two limitations are already established:
the two-adic overlap is maximal when $n=2^h$ and $j$ is odd, and no
fixed finite set of odd primes is active on every such row. Any complete
argument along this route must use odd primes that vary with the row.
