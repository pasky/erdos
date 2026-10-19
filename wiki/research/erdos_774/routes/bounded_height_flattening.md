---
name: research/erdos_774/routes/bounded_height_flattening
title: Uniform coefficient height and conditional flattening
desc: A fixed palette forces uniformly bounded-height relations; Hall-tight determinant supports flatten coefficients safely, but forcing the needed monochromatic support is unproved.
tags: [E0774, proved, conditional, incomplete]
sources: []
created: 2026-09-18T01:48:00Z
updated: 2026-09-18T17:37:54Z
---


# Uniform coefficient height and conditional flattening

***

## Standing

The
[coefficient-growth theorem](coefficient_growth_flattening.md) extends the
algebraic flattening criterion beyond Hall-tight magnitude sets. Actual
monochromatic factors satisfying its inequality have not been forced.
[Root circuit products](../lemmas/root_height_escape.md) show that
height-free flattening fails even for actual roots.

This isolates a quantitative coefficient gap in the
[unrestricted coloring problem](../proof_sketch.md). For each fixed palette
size, a monochromatic relation with coefficients bounded by one uniform
integer is unavoidable. A separate lemma converts sufficiently many such
dependent factors into a relation with coefficients in $\{-1,0,1\}$,
**provided their full Cartesian product is monochromatic**. That hypothesis
has not been forced for arbitrary colorings. Thus this page is not a proof of
unbounded dissociated coloring.

All proofs are elementary and require no computation or external theorem.

[Fixed-height focusing](fixed_height_focusing.md)
proves a valid color-adaptive use of the determinant: unbounded chromatic
number at one fixed coefficient height would suffice. The available height
bound depends on the palette and does not establish that hypothesis.
[Prescribed-support splitting](adaptive_determinant_support.md) and
[private conductor lifts](../lemmas/private_conductor_lifts.md) delimit two
shortcuts without ruling out adaptive focusing.

## 1. Radical counting gives many small columns

Fix a prime $\ell$, $P\geq2$, and

$$
E=\bigotimes_{\substack{p\leq P\\p\ne\ell}}S_p,
\qquad d=\prod_{\substack{p\leq P\\p\ne\ell}}(p-1),
\qquad H=\sum_{\substack{n\leq P\\\ell\nmid n}}\frac1n.
$$

The case $\ell=2$ is the main odd-prime prefix. Use the standard integer
coordinates for each simplex. For a column, let $a$ be the product of
the primes at which its last simplex symbol was chosen. Its $\ell_1$-norm
is $\varphi(a)$, and exactly $d/\varphi(a)$ columns have this index
$a$. Consequently

$$
\#\{v\in E:\|v\|_1\leq P\}
\geq d\sum_{\substack{a\leq P\text{ squarefree}\\\ell\nmid a}}
\frac1{\varphi(a)}\geq dH. \tag{1}
$$

For the second inequality, group positive integers by their radical and use

$$
\sum_{\operatorname{rad}(n)=a}\frac1n
=\prod_{p\mid a}\sum_{j\geq1}\frac1{p^j}
=\frac1{\varphi(a)}.
$$

This includes $a=1$, with its single integer $n=1$. Every integer
$n\leq P$ has $\operatorname{rad}(n)\leq P$, so the grouped
infinite sums dominate the required finite harmonic sum. Finally,

$$
H=H_{\lfloor P\rfloor}-\ell^{-1}H_{\lfloor P/\ell\rfloor}
\geq(1-1/\ell)\log P\geq\tfrac12\log P. \tag{2}
$$

## 2. Every fixed palette forces bounded-height dependence

Say a set is $h$-degree independent when it has no nonzero integer
relation with all coefficient magnitudes at most $h$. For an integer
$h\geq1$, if $E$ has a partition into $q$ such sets, then

$$
\log(h+1)\leq\frac qH\log\left(1+\frac{hPH}q\right)
\leq\frac{2q}{\log P}
\log\left(1+\frac{hP\log P}{2q}\right). \tag{3}
$$

Indeed some color contains $s\geq dH/q$ of the small columns from
(1). Its $(h+1)^s$ sums with coefficients in $\{0,\ldots,h\}$
are distinct. Coordinate widths total at most $hPs$, hence

$$
(h+1)^s\leq(1+hPs/d)^d.
$$

The function $t\mapsto\log(1+hPt)/t$ is decreasing for $t>0$,
as follows from $\log(1+x)>x/(1+x)$. Insert
$t=s/d\geq H/q\geq\log P/(2q)$ to get (3).

In particular, put

$$
h_q=\lceil e^{3q}\rceil,\qquad P\geq e^{8(q+1)}. \tag{4}
$$

**Every $q$-coloring of $E$ has a nonzero monochromatic integer
relation with coefficient magnitudes at most $h_q$.**

To check the constants, set $u=\log P\geq8(q+1)$. Since
$he^u u\geq2$, the right side of (3) is at most

$$
2q+\frac{2q}{u}(\log h+\log u).
$$

Here $\log h<3q+1$. The function
$(3q+1+\log u)/u$ decreases on this range, and at
$u_0=8(q+1)$ it is less than $1/2$, since
$\log(8(q+1))<q+3$. The displayed upper bound is therefore less
than $3q$, whereas $\log(h+1)>3q$, contradicting (3).

For the [prime-selector formulation](roots_coloring_structure.md), take
$q=\ell$ on the conductor coprime to $\ell$. A hypothetical
dissociated selector already has, at the finite stage in (4), an integer
relation whose primitive coefficient height lies between 2 and
$\lceil e^{3\ell}\rceil$. Dividing a relation's coefficient gcd
normalizes it, but does not make it a rational circuit or a ternary relation.

## 3. Coefficient-safe finite templates

Suppose a dissociated color class supports a nonzero relation
$\sum_x a_xx=0$ of height at most $h$. Divide out its coefficient
gcd, and group by coefficient magnitude:

$$
w_m=\sum_{|a_x|=m}\operatorname{sign}(a_x)x,
\qquad I=\{m:w_m\text{ has a nonempty defining support}\}.
$$

Each $w_m$ is nonzero, the indexed family $(w_m)_{m\in I}$ is
dissociated, and

$$
\sum_{m\in I}m w_m=0. \tag{5}
$$

A signed relation between these sums expands over disjoint original supports,
keeping all coefficient magnitudes at most one; dissociation rules it out.
Thus $2\leq|I|\leq h$. The finite possibilities for $I\subset[h]$
give a finite set of relation templates, but **not** a finite set of actual
root supports, whole color profiles, or rational isomorphism types. Additional
rational dependencies can occur among the $w_m$.

## 4. Hall/determinant flattening

Let $h\geq2$. Let $X_1,\ldots,X_h$ be finite sets of roots in
pairwise coprime conductor groups, each supporting a nonzero integer relation
of height at most $h$. If their entire multiplicative Cartesian product
has one color, that color is not dissociated.

More generally, group one relation in factor $i$ by its nonzero coefficient
magnitudes $I_i$, as in (5). It suffices that some nonempty subfamily $R$
satisfy

$$
\left|\bigcup_{i\in R}I_i\right|\leq |R|. \tag{6}
$$

The uniform-height assertion follows because $h$ subsets of $[h]$
necessarily have such a subfamily.

### Proof

If any factor already has a ternary relation, hold all other coordinates
fixed. Otherwise every magnitude group is a nonzero signed sum, and each
$I_i$ has at least two elements. Choose $R$ minimal nonempty satisfying
(6), and write $U=\bigcup_{i\in R}I_i$, $r=|R|$. Every nonempty proper
$J\subset R$ has $|\bigcup_{i\in J}I_i|>|J|$. Deleting one index from
$R$ therefore gives $|U|\geq r$; (6) gives equality. These inequalities
are Hall's matching condition, so there is a bijection from $R$ to $U$
assigning every row $i$ one of its magnitudes in $I_i$.

For completeness, the needed finite matching implication is elementary.
Take a maximum matching. If a row is unmatched, explore alternating paths
from it. Every reached column is matched, or the matching could be enlarged.
Let $J$ be the reached rows and $K$ all their neighboring columns. Matched
columns correspond bijectively to the reached rows other than the initial
one, so $|K|=|J|-1$, contrary to the stated inequalities. Hence the
matching is perfect.

Form the square complex matrix

$$
W=(w_{i,m})_{i\in R,m\in U},\qquad
w_{i,m}=\sum_{|a_{i,x}|=m}\operatorname{sign}(a_{i,x})x,
$$

putting zero in absent groups. Each row annihilates the same nonzero column
vector $(m)_{m\in U}$, since $\sum_m m w_{i,m}=0$. Thus

$$
0=\det W=\sum_{\pi:R\to U\ {\rm bijective}}
 \operatorname{sign}(\pi)\prod_{i\in R}w_{i,\pi(i)}. \tag{7}
$$

Expand every signed block sum. Distinct permutations choose disjoint
Cartesian product blocks, because in some factor their magnitude groups
differ. Within each block the expansion coefficients are also $\pm1$.
The matching guarantees at least one nonempty block. Multiplication is
injective on root tuples from pairwise coprime conductor groups: their
multiplicative subgroups have direct product. Therefore (7) is a genuinely
nonzero formal ternary relation on distinct root products. Fix arbitrary
roots in factors outside $R$ to keep its support within the original
monochromatic product.

This proof makes no rational-circuit assumption about the grouped sums, and
it does not require the maps from universal coefficient templates to be
injective. Disjoint original supports and coprime conductors are what ensure
that no nonzero formal coefficient is lost. The result and the uniform-height
theorem are author-recorded; separate reviewers checked each.

The proof in fact needs only the union of the nonempty permutation-product
blocks in (7) to have one color (after fixing any other factors). A full
monochromatic product is a stronger convenient sufficient condition. Forcing
this determinant support is therefore a narrower possible research target.

This remains a conditional use: the algebra supplies a
nonzero formal relation on the specified support, not its monochromaticity.
The minimal subfamily is Hall-tight (equal union and factor sizes), and Hall's
matching theorem is satisfied, not contradicted.

## 5. Exact outstanding focusing step

The uniform height in (4) does not give the monochromatic rectangle required in
Section 4. Coloring a multiplier $y$ by its entire pattern $(f(xy))_{x\in X}$
can use $q^{|X|}$ colors. Reapplying (4) to that palette makes the height bound
depend on $q^{|X|}$, not just on the original $q$. Repeating the argument has
not provided $h$ factors with one common controlled height $h$, or more
generally the matching obstruction (6).

There is a second quantitative loss when conductors must stay coprime. If a
finite set $S$ of already used primes is excluded, the same radical count
uses
$H_S(P)=\sum_{n\leq P,\ (n,\prod_{p\in S}p)=1}1/n$, with
$H_S(P)\geq\alpha_S\log P$,
$\alpha_S=\prod_{p\in S}(1-1/p)$. To prove this bound inductively,
use $H_{S\cup\{p\}}(P)=H_S(P)-p^{-1}H_S(P/p)\geq(1-1/p)H_S(P)$.
The necessary inequality (3) then has $1/2$ replaced by $\alpha_S$.
The available eventual height condition is
$\log(h+1)>q/\alpha_S$, so the single-excluded-prime bound cannot
be reapplied unchanged to arbitrarily many disjoint conductors.

Nor can an arbitrary dependence simply be flattened without height control:
the abstract scalar factors $\{1,2^{2^{i-1}}\}$ are each rationally
dependent, but their indexed tensor product is
$\{2^a:0\leq a<2^k\}$, which is dissociated. This is an obstruction
to an abstract height-free lemma, not a coloring of the root family.

Likewise, disjoint primitive-root expansions of a point cannot automatically
preserve its color: if a point of a dissociated class were a signed sum of
other points of that class, it would already give a forbidden relation.
The next proof obligation is a quantitatively controlled focusing or
height-descent mechanism, not an assumption that rational dependence suffices.
It must address actual colors on the surviving determinant blocks, as well
as their magnitude-set condition. No such forcing statement is
established.

### A single short-relation direction cannot supply one-prime descent

Let $C$ be $h$-degree independent. Suppose all its integer relation
vectors of height at most $2h$ lie in one rational line (or there are
none). Then every height-at-most-$h$ relation in $C\otimes S_p$
has a full $p$-fiber in its support.

Indeed let $v_j\in[-h,h]^C\cap\mathbb Z^C$ be the layer coefficient
vectors. Their vector sums in the base are all equal, so every difference
$v_j-v_0$ is a height-at-most-$2h$ base relation. If they all vanish,
any nonzero coordinate of $v_0$ gives a full fiber. Otherwise let $a$
be the primitive integer generator of the relation line and write
$v_j=v_0+t_j a$, with $t_j\in\mathbb Z$. Its height $H$ is
strictly greater than $h$. The layer bounds give
$(\max t_j-\min t_j)H\leq2h$, so the integer parameters have at most
two consecutive values. At a coordinate with $|a_b|=H$, the two layer
coefficients differ by $H>h$. Neither can be zero, since both lie in
$[-h,h]$. This is the required full fiber.

Consequently a coloring making each $p$-fiber nonmonochromatic prevents
all such descent. To avoid this elementary polygon obstruction, a
one-prime step confined to the old support needs at least two independent
short relation directions, not merely one monochromatic rational circuit.
