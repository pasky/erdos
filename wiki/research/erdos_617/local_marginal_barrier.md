---
name: research/erdos_617/local_marginal_barrier
desc: Affine proper-subset marginals satisfy linear consistency, but their first edge-indicator moment matrix is not positive semidefinite.
tags: [graph-theory, proved, relaxations, constructions]
sources:
  - erdos_gyarfas_1999_split_balanced_colorings_complete_graphs
created: 2026-09-22T08:59:28Z
updated: 2026-09-24T22:12:59Z
---


# research/erdos_617/local_marginal_barrier

***

**A limitation of a specified relaxation, not a coloring counterexample.**
For every prime-power $r\ge3$, there is a mutually consistent system
of probability distributions on the colorings of **every proper
vertex subset** of $[r^2+1]$, satisfying all the required local
color conditions with probability one. A genuine joint distribution
on the full vertex set is not asserted.

## Construction

Put $q=r^2$ and take the affine-plane coloring on $q$ points: $r-1$ directions
get separate colors and the remaining two directions share a color. Every
$(r+1)$-set sees every color. This construction is the paragraph after
Conjecture 1 in the
[Erdős--Gyárfás source](../../../library/extremal_graph_theory/erdos_gyarfas_1999_split_balanced_colorings_complete_graphs/_index.md),
whose digest and relevant passage were checked.

For every $S\subseteq[q+1]$ with $|S|\le q$, choose uniformly
an injective map from $S$ into the $q$ affine points and pull
back their edge coloring. Let $\mu_S$ be its distribution.
One may also apply an independent uniformly random permutation
of the $r$ color names, using the same rule for every $S$.

If $T\subseteq S$, every injection of $T$ into the affine points
has the same number of injective extensions to $S$, namely
$(q-|T|)_{|S|-|T|}$ in falling-factorial notation. Consequently

$$
\mu_S|_T=\mu_T.
$$

Every coloring in the support of $\mu_S$ is an induced coloring
of the affine example. Therefore every $(r+1)$-subset of $S$
contains every color. All induced consequences of those local
independence bounds hold on $S$ as well.

## Exact consequence and its limits

Consider the linear feasibility system whose variables are
probabilities for colorings of proper vertex subsets, whose
constraints are nonnegativity, normalization, consistency under
restriction, and zero probability for a forbidden local pattern.
The distributions above are a feasible solution even when all
sets of order up to $r^2$ are included.

Thus this entire proper-subset marginal relaxation cannot refute
the desired counterexample at affine orders. Adding linear
expectations of any further inequalities valid for each supported
local coloring cannot change that conclusion. With the optional
color permutation, each edge has every color with probability
$1/r$, so each full color edge count also has the formal expected
value $r(r^2+1)/2$.

This does not say that local lemmas cannot occur in a proof:
the obstruction applies to the specified linear probability
system, not arbitrary deductions coupling all vertices.
Nor is it a positive-semidefinite pseudoexpectation. Local
positivity does not guarantee positivity of the square of a
polynomial whose terms collectively involve the whole vertex set.
No claim is made about the feasible levels of a sum-of-squares
hierarchy or about a genuine coloring of $K_{r^2+1}$.
The levels here are measured by vertices, not by edge variables:
a small collection of edges can already touch every vertex.
Thus no corresponding edge-variable hierarchy claim is implicit.

The construction isolates the obstruction to the first
local-probability version of the new algebraic approach:
it exactly inherits the sharp example one vertex below.
A global positivity or compatibility condition beyond proper-set
marginal consistency is necessary for that approach.
The restriction calculation and this precise scope were checked
independently.

## The affine marginal system fails the first edge-moment PSD test

**Proved.** The particular consistent system above is not merely
uncertified as a positive-semidefinite pseudoexpectation: it violates
positivity for the square of an explicit linear polynomial in the
edge indicators. This does not rule out other marginal systems.

More generally, let $F$ be a $d$-regular graph on $q>3$ vertices, with
$0<d<q-1$. Pull it back by uniformly random injections on every proper
subset of $n=q+1$ formal labels. Write $X_{ab}$ for the edge indicator
in this one graph. For distinct indicated labels, these marginals fix

$$
p=\mathbb E X_{ab}=\frac d{q-1},\qquad
s=\mathbb E(X_{ab}X_{ac})
=\frac{d(d-1)}{(q-1)(q-2)},
$$


$$
t=\mathbb E(X_{ab}X_{cd})
=\frac{d((q-4)d+2)}{(q-1)(q-2)(q-3)}.
$$

For the last formula, after choosing an oriented edge $ab$, there are
$qd-4d+2$ oriented edges disjoint from its endpoints. All these
expectations involve at most four labels, so they are specified by
proper-subset marginals.

Fix distinct $u,v$ and put

$$
Z=\sum_{w\notin\{u,v\}}(X_{uw}-X_{vw}).
$$

A summand has second moment $2(p-s)$, and two distinct summands have
mixed moment $2(s-t)$. Consequently

$$
\begin{aligned}
\mathbb E Z^2
&=2(n-2)(p-s)+2(n-2)(n-3)(s-t)\\
&=\frac{2(n-2)d(q-1-d)(q-n)}
{(q-1)(q-2)(q-3)}\\
&=-\frac{2d(q-1-d)}{(q-2)(q-3)}<0.
\end{aligned}
$$

Thus the moment matrix indexed by edge indicators is not positive
semidefinite, even though every individual moment used has a valid
proper-subset distribution.

For the affine coloring, $q=r^2$, and each fixed color graph is regular
of degree $r-1$ or $2(r-1)$. Both degrees meet the strict hypotheses.
An optional random permutation of color names just averages the
negative expressions and does not repair positivity.

This calculation rules out extrapolating the **specified affine
marginals** to a first edge-moment PSD certificate. It does not prove
infeasibility of that relaxation with different moments. In a genuine
coloring, $Z$ is a difference of color degrees and its square is
nonnegative. No argument forces a hypothetical irregular coloring to
have the affine system's moments, so this is not a solution of E617.
