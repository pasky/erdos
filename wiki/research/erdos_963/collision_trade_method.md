---
name: research/erdos_963/collision_trade_method
title: 'Collision codes, signed circuits, and global linear trades'
desc: An exact ordered-realization criterion, a circuit-covering inequality, and two proved sparse cases; the logarithmic bound remains unresolved.
tags: []
sources: []
created: 2026-09-19T11:11:01Z
updated: 2026-10-16T06:44:50Z
---


# Collision codes, signed circuits, and global linear trades

***

This approach studies all subset-sum collisions simultaneously, without
congruence splitting or a geometric lift. It gives an exact realization
criterion and new restrictions on a counterexample. It does **not**
prove the requested bound or supply a counterexample.

Write $P=\{p_1<\cdots<p_n\}$, with every $p_i>0$, and $d=d(P)$.
A **circuit** is an inclusion-minimal support of a nonzero ternary
relation. The dissociated subsets are exactly the sets containing
no circuit. Every circuit has size between three and $d+1$.

## Collision fibers and the missing global consistency

Partition $\{0,1\}^n$ by the value of $\sum_i x_i p_i$. A coordinate
set $B$ is dissociated if and only if projection onto $[n]\setminus B$
is injective on every fiber. Indeed, failure of this injectivity is
exactly a collision whose difference is supported on $B$.

Every fiber is an antichain in the coordinatewise order, by positivity.
Distinct points in a fiber have Hamming distance at least three, by
distinctness of the positive weights. These conditions alone are
insufficient. On the four-dimensional cube, prescribe four doubleton
fibers

$$
\{1\}\sim\{2,3\},\qquad
\{2\}\sim\{1,4\},\qquad
\{4\}\sim\{1,3\},\qquad
\{3\}\sim\{2,4\},
$$

and make all other vertices singleton fibers. These are antichains
of minimum distance three, but every three-coordinate origin face
has a collision. This cannot be a subset-sum partition: translating
the first equality by $\{4\}$ and using the second gives

$$
\{2\}\sim\{1,4\}\sim\{2,3,4\},
$$

contradicting antichainness. Thus an argument using only individual
fiber codes loses essential additive consistency.

There is an exact criterion controlling **all linear combinations**
of prescribed relations. For a subspace $L\subseteq\mathbb R^n$,
define

$$
\tau(u)_j=\sum_{i=j}^n u_i,\qquad M=\tau(L).
$$

Then

$$
\boxed{\exists\ 0<p_1<\cdots<p_n\text{ with }L\subseteq p^\perp
\quad\Longleftrightarrow\quad
M\cap\mathbb R_{\ge0}^n=\{0\}.}                           \tag{1}
$$

For necessity, put $p_0=0$ and $\delta_j=p_j-p_{j-1}>0$. Summation
by parts gives

$$
p\cdot u=\sum_j\delta_j\tau(u)_j.
$$

A nonzero nonnegative member of $M$ therefore cannot be orthogonal
to $\delta$.

For sufficiency, let $\Delta=\{x\ge0:\sum x_j=1\}$ and project it
orthogonally onto $M^\perp$. By the assumed intersection condition,
the projected compact convex set does not contain zero. Its point
$\delta$ nearest zero satisfies

$$
\delta\cdot\operatorname{proj}_{M^\perp}(e_j)
\ge\|\delta\|^2>0
\quad\text{for every }j.
$$

Since $\delta\in M^\perp$, the left side is $\delta_j$. Thus all
coordinates of $\delta$ are positive. Setting
$p_i=\sum_{j\le i}\delta_j$ proves (1).

Moreover, the positive vectors in $M^\perp$ form a nonempty relatively
open set. For any ternary $r\notin L$, the functional
$\delta\mapsto\delta\cdot\tau(r)$ is not identically zero there.
Avoiding the finitely many such hyperplanes realizes precisely the
ternary relations belonging to $L$, without additional collisions.
If $L$ is spanned by integer vectors, this relatively open feasible set and
all the excluded hyperplanes are rational. It contains a rational gap vector
outside their finite union. Clearing denominators therefore gives strictly
increasing positive integers with exactly those ternary relations. For an
arbitrary real subspace, (1) alone asserts real realizability.

Consequently a finite counterexample can be specified without a bound
on its integer heights: choose nonzero ternary relations such that every
$(d+1)$-set contains the support of at least one chosen relation,
let $L$ be their span, and verify (1). If $n\ge2^d$,
such a configuration would refute the target. Conversely any
counterexample supplies such a family. This is an exact certificate
formulation, not an existence proof.

## Unique circuit orientation and compatible elimination

Every circuit $C$ has a unique signed relation up to reversal.
If $u,v\in\{\pm1\}^C$ were two relations not equal or opposite,
then $(u-v)/2$ would be a nonzero ternary relation on a proper
subset of $C$, contradicting minimality. Accordingly, the cube on
$C$ has exactly one doubleton fiber and all other fibers singleton.

If two circuit relations can be oriented to agree on their
intersection, subtraction gives a ternary relation supported on
their symmetric difference. That symmetric difference therefore
contains a circuit. In particular, elimination always works for
an intersection of size one. The obstructing case is an intersection
of size at least two with **both** relative sign agreements and
relative sign disagreements: direct cancellation then produces
coefficients of magnitude two.

As a proved sparse case, suppose distinct circuits intersect in at
most one coordinate. Then they are actually pairwise disjoint.
Otherwise compatible elimination yields a circuit $E\subseteq
C\triangle D$ for two circuits meeting once. The intersection
hypothesis implies $|E\cap C|,|E\cap D|\le1$, so $|E|\le2$,
which is impossible. If there are $m$ circuits, disjointness gives

$$
d=n-m\ge2n/3.
$$

This implies the target: for $d\ge2$,
$n\le3d/2\le2^d-1$, and $d=1$ permits only one positive element.

## A circuit-covering inequality

Assume $d<n$, let $R$ be the largest circuit size, and let $e_s$
be the number of circuits of size $s$. Then

$$
\boxed{\sum_{s=3}^{R}
\frac{2^{s-2}\binom{d+1}{s}}{n-s+1}\ge1.}                 \tag{2}
$$


For a fixed $(s-1)$-set $T$, a circuit completion $T\cup\{x\}$
represents $x$ as the absolute value of a full signed sum on $T$.
There are at most $2^{s-2}$ possibilities, after identifying opposite
sign vectors. Counting each circuit by its $s$ deletions gives

$$
e_s\le\frac{2^{s-2}}s\binom n{s-1}.
$$

Every $(d+1)$-set contains a circuit, and therefore

$$
\binom n{d+1}\le
\sum_{s=3}^{R}e_s\binom{n-s}{d+1-s}.
$$

Substitution and cancellation yield (2). In particular,

$$
n\le d+\sum_{s=3}^{R}2^{s-2}\binom{d+1}{s}.              \tag{3}
$$


Let $H_2(x)=-x\log_2x-(1-x)\log_2(1-x)$, and let
$\theta\in(0,1/3)$ be the unique solution of

$$
H_2(\theta)+\theta=1\qquad(\theta\approx0.2271).
$$

Every counterexample $n\ge2^d$ must satisfy

$$
\boxed{R>\theta(d+1).}                                    \tag{4}
$$

Indeed, put $t=\theta/[2(1-\theta)]$, so $0<t<1$ and
$(1+2t)t^{-\theta}=2$. If $R\le\theta(d+1)$, then

$$
\begin{aligned}
\sum_{s=3}^{R}2^{s-2}\binom{d+1}{s}
&<\tfrac14t^{-R}(1+2t)^{d+1}\\
&\le2^{d-1}\le2^d-d\qquad(d\ge2).
\end{aligned}
$$

This contradicts (3). The first strict inequality follows by adding
the omitted positive terms of the binomial expansion.

Together with [[research/erdos_963/algebraic_observations|the established
high-girth bound]], this says that a counterexample of dimension $d\ge9$ has a
circuit of size at most six and a circuit of size greater than $\theta(d+1)$;
these must be different for sufficiently large $d$. Separate counting of the two
kinds does not give a contradiction.

## A direct order argument for one-sided circuits

Suppose every circuit has a singleton side in its unique relation.
Then some maximum dissociated $D\subseteq P$ satisfies

$$
P\subseteq\Sigma(D)\setminus\{0\},
$$

which proves $|P|\le2^{d(P)}-1$ in this case.

Choose a maximum $D$ minimizing its sum. If $x\in P\setminus D$
has no positive subset-sum representation on $D$, every circuit
in $D\cup\{x\}$ has a root $r\in D$ and an equation

$$
r=x+\sum_{a\in A_r}a,\qquad A_r\subseteq D\setminus\{r\}.
$$

There is at most one equation for each root, since two would give
equal subset sums on $D$. For roots $r<s$, positivity implies
$s\notin A_r$. If also $r\notin A_s$, subtracting the two
equations would give a nonzero ternary relation on $D$. Thus
$r\in A_s$. The smallest root belongs to every circuit through
$x$. Replacing it by $x$ consequently preserves dissociation,
but lowers the sum, a contradiction. Hence every omitted point
has the required positive representation.

This is a direct special-case proof, not a treatment of arbitrary
mixed-side circuits.

## Bounded unbounded-height SMT attempt

A separate computational attempt used 32 increasing real variables,
normalized by $p_1\ge1$ and $p_{i+1}-p_i\ge1$, with **no upper
bound**. Scaling makes this normalization legitimate for any finite
positive configuration. When a candidate contained a dissociated
six-set, a disjunction of all its potentially feasible ternary
relations was added. A fully validated model would be a counterexample;
an UNSAT certificate would exclude only this fixed $(n,d)=(32,5)$ case.

Six solver checks
returned models of the partial constraints; every one was rejected
by explicitly verified dissociated six-sets. The seventh check returned
UNKNOWN after its eight-second timeout, with 96 six-set clauses present.
There was neither a counterexample nor an impossibility certificate.
No computational conclusion is used in the proofs above.

## Exact remaining gap

The order-consistency condition (1) constrains arbitrary linear combinations of
circuits, whereas (2) counts their supports separately. No argument yet combines
these constraints to rule out $n\ge2^d$, and pairs of circuits with free
orientation cannot: by
[[research/erdos_963/pairwise_circuit_models|the pairwise-model note]], once
signs and order are free (1) forbids exactly the implied relations of support
at most two, and its two-circuit content is the unique completion already used
in (2). The ternary projective model satisfies all such pairwise data with
$(3^d-1)/2$ points and circuits of every size, so the forced short and long
circuits in (4) coexist there. Mixed-sign overlaps impose no pairwise
restriction when signs and order are free. Replacing a coefficient two by
minus one gives relations in the projective model but not in a real
configuration. Requiring one common positive orientation already excludes
that model. In a fixed order, the exact two-profile test in the pairwise-model
note constrains every short-long pair, including supports of sizes three
through six. No count using those constraints contradicts $n\ge2^d$.
The ordered greedy bound proves the target for $d\le3$, but gives $18$ at
$d=4$ against the target $15$ and grows with base three. This is a stopped
estimate, not a countermodel to the ordered conditions. The retained
$K_{4,4}$ example explicitly has intersecting circuits of sizes four and
seventeen, so coexistence alone is not impossible. Compatible
circuit elimination and the two sparse cases above are proved. The universal
estimates in [[research/erdos_963/proof_sketch|the proof sketch]] are
unchanged.
