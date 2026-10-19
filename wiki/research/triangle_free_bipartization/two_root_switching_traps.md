---
name: research/triangle_free_bipartization/two_root_switching_traps
title: Finite traps for two-root switching
desc: A probabilistic construction with an exact finite gain table refutes the two-root stability implication for the middle band; an exhibited three-root move escapes, and the original bipartization bound holds throughout the construction.
created: 2026-10-17T07:19:38Z
updated: 2026-10-17T07:19:38Z
---

# Finite traps for two-root switching

***

The stronger two-root implication proposed in
[[research/triangle_free_bipartization/proof_sketch|the canonical sketch]]
is false. There are finite triangle-free graphs in the middle-density band
with a cut that is stable under every single-vertex flip and every
deterministic two-root coloured-profile recolouring, but has more than
$N^2/25$ monochromatic edges. These graphs have much better cuts and are not
counterexamples to [[problems/extremal_graph_theory/E0023/_index|Problem 23]].
An exhibited three-root rule improves the trapped cut below $N^2/25$.

The construction and argument are by Plasma AI, author-recorded and not
independently reviewed. The exact finite calculation is replayed by
[[research/triangle_free_bipartization/evidence/_index|the evidence entry point]].
The finite existence proof is probabilistic; no adjacency list of the large
graph is asserted to be retained.

## The precise implication that fails

For a colouring $\chi$, roots $r_1,r_2$, and a Boolean function $h$, recolour
each vertex $v$ by

$$
h\bigl(\chi(v),[v\sim r_1],[v\sim r_2]\bigr).
$$

The failed assertion is that every triangle-free graph with
$1243/5000<p=2e/N^2<3197/10000$, and every colouring stable under all such
recolourings and all single-vertex flips, has at most $N^2/25$
monochromatic edges. Stability means that the number of monochromatic edges
does not decrease. The assertion was sufficient for the target because a
maximum cut is stable, but the converse qualification matters here.

## Template and exact gain table

Index the even subsets of $[5]$ by their five-bit masks in increasing order,
starting at index zero. Let $H$ join two subsets when their symmetric
difference has size four. This is the triangle-free Clebsch graph, with
sixteen vertices and forty edges. Put

$$
\chi_i=\left\lfloor\frac{831}{2^i}\right\rfloor\bmod2.
$$

This cut has twelve monochromatic edges. Its vertex slacks, opposite-colour
degree minus same-colour degree, are $5$ at indices $0,1,14,15$ and $1$
at the other twelve indices.

Replace each template vertex by $t$ vertices of its colour. Retain each
possible edge between adjacent parts independently with probability
$q=7/8$, and retain no other edges. Put $N=16t$. Every outcome is
triangle-free. The limiting edge and monochromatic densities of this
colouring are

$$
p=\frac{2q\cdot40}{16^2}=\frac{35}{128},
\qquad
\frac{M}{N^2}=\frac{q\cdot12}{16^2}=\frac{21}{512}>\frac1{25},
\qquad
m=\frac{2M}{N^2}=\frac{21}{256}>\frac2{25}. \tag{1}
$$

For the gain calculation, fix the template parts $r,s$ of two distinct
roots. The parts may coincide; the two roots are still distinct vertices,
so their incident edge trials to a third vertex are independent. Number a
coloured profile by
$c=\chi_i+2b_1+4b_2$, where $b_j$ is adjacency to root $j$.
For each part $i$ let $P_{i,c}$ be $64$ times the probability of profile
$c$. This is an integer: a supported root edge has numerators $7,1$ for
presence and absence, and an unsupported root edge has numerators $0,8$.

Write $A$ for the adjacency matrix of $H$ and
$J_{ij}=A_{ij}(1-2[\chi_i=\chi_j])$. A switch vector
$z\in\{0,1\}^8$ flips exactly the cells with $z_c=1$. Set

$$
Q=7P^{\mathsf T}JP,
\qquad
B_{r,s}(z)=z^{\mathsf T}Q\mathbf1-z^{\mathsf T}Qz.
\tag{2}
$$

Then the expected change in monochromatic edges, divided by $N^2$ and
ignoring the two roots themselves, tends to
$B_{r,s}(z)/(16^2 8^5)$. This uses the unordered-edge convention
$M/N^2$ for gains; the density $m$ in (1) is twice that convention.
Indeed $z^{\mathsf T}Q\mathbf1-z^{\mathsf T}Qz$ is
$\frac12\sum_{c,d}Q_{cd}|z_c-z_d|$, and the factors in the denominator
are the two endpoint parts, four root-adjacency trials, and the edge trial.

A profile is *possible* when its column of $P$ has positive sum. A switch
is nontrivial when it is not constant on the possible profiles. Constant
switches preserve the cut or complement it. Complementing $z$ leaves (2)
unchanged, so it suffices to fix its final coordinate at zero.

The exact calculation scans all $16^2$ ordered part pairs and all $128$
switches with that fixed coordinate. Of the $32768$ cases, $31796$ are
nontrivial. The minima of their integer numerators are:

| Root-part relation | Old root colours | Least numerator |
|---|---|---:|
| Same part | Same | 6272 |
| Distinct nonadjacent parts | Same | 6272 |
| Distinct nonadjacent parts | Different | 6272 |
| Adjacent parts | Different | 12544 |
| Adjacent parts | Same | 50176 |

Thus every nontrivial two-root switch has limiting gain at least

$$
\delta=\frac{6272}{16^2 8^5}=\frac{49}{65536}>0. \tag{3}
$$

Parts $(0,6)$ and switch mask $16$ attain the minimum. The checker builds
$H,P,Q$ from the definitions, verifies their probability masses, checks
every case and the table, and checks this attaining case separately. As a
negative control, at retention probability one the same old colouring has
a two-root switch on parts $(2,4)$ with gain $-1/256$. The strict margin
therefore depends on edge retention, not just on the template or colouring.

## Passing from the table to finite graphs

For completeness, a function of independent variables with bounded
coordinate differences $c_i$ obeys

$$
\Pr(F-\mathbb EF\le-u)
\le \exp\left(-\frac{2u^2}{\sum_i c_i^2}\right). \tag{4}
$$

The upper tail has the same bound. One proof exposes the variables in
order. Each martingale increment has conditional mean zero and lies in an
interval of length at most $c_i$, by coupling the remaining variables.
Its conditional log moment-generating function is at most
$\lambda^2c_i^2/8$: the second derivative of that log function is a
variance supported in an interval of length $c_i$, at most $c_i^2/4$,
and integration twice gives the bound. Multiplication of these conditional
bounds, exponential Markov, and optimization over $\lambda$ prove (4).

Fix two actual distinct roots and a switch. Every possible profile of a
root itself is also possible for ordinary vertices in its part: self
adjacency is zero, and the edge to the other root, when supported, has
both outcomes of positive probability. Consequently a switch constant on
the possible profiles preserves or complements the whole cut exactly.
There is no exceptional root-only cell.

For a nontrivial switch, let $D$ be its actual change in monochromatic
edges. The contribution of edges with neither endpoint a root agrees in
expectation with the independent-profile calculation. At most $2N$ edges
touch a root. Comparing the actual and formal contributions, each bounded
between $-1$ and $1$, gives

$$
\mathbb ED\ge\delta N^2-4N\ge\frac{\delta N^2}{2}
\quad\text{if }N\ge8/\delta. \tag{5}
$$

Changing one edge trial away from the roots changes $D$ by at most one.
A trial incident to a root can change the cell of one other vertex, or
the cells of both roots if it is their mutual edge. In either case it
affects at most $2N$ edge contributions. There are at most $2N$ such
trials, so the squared difference bounds sum to at most
$8N^3+N^2/2\le9N^3$. Equations (4) and (5) give

$$
\Pr(D\le0)\le\exp(-\delta^2N/18).
$$

A union bound over fewer than $128N^2$ root-pair/switch cases shows that
every nontrivial two-root switch strictly worsens the cut except with
probability at most
$128N^2\exp(-\delta^2N/18)$. Switches using one root or the same vertex
twice are covered: add an arbitrary distinct second root and ignore its
adjacency coordinate.

At each vertex the expected slack is at least $qt=qN/16$. Its incident
edge trials have difference bound one and number at most $N$, so the
probability of any nonpositive vertex slack is at most
$N\exp(-q^2N/128)$. Furthermore,
$M$ is binomial with $12t^2$ trials and mean $(21/2)t^2$. Its distance
above $N^2/25=(256/25)t^2$ is $(13/50)t^2$, giving

$$
\Pr(M\le N^2/25)\le\exp(-169t^2/15000). \tag{6}
$$

The total edge count has $40t^2$ trials and mean $35t^2$. The upper band
endpoint is automatic, because even the complete template blow-up has
$p=5/16<3197/10000$. The mean exceeds the lower endpoint by
$(1987/625)t^2$ edges. Thus

$$
\Pr\left(\frac{2e}{N^2}\le\frac{1243}{5000}\right)
\le\exp\left(-\frac{1987^2t^2}{20\cdot625^2}\right). \tag{7}
$$

All these failure probabilities tend to zero. An explicit sufficient order
is $N=2^{32}$, with $t=2^{28}$. Here
$\delta^2N/18=2401/18>128$, so the switching union bound is less than
$2^{-57}$, using $e>2$. The vertex bound is less than $2^{-32}$, and
each of (6) and (7) is less than $2^{-64}$. Their sum is below one.
This proves the existence of a finite graph with all the asserted trap
properties, and in fact gives them with probability tending to one.

## A third root escapes

Take three distinct roots in template parts $(2,2,4)$: two different
vertices in part $2$ and one in part $4$. Number cells by
$c=\chi_i+2b_1+4b_2+8b_3$. Flip cells $\{3,5,7,8\}$, the switch mask
$424$. The same integer calculation, now with denominator
$16^2 8^7$, gives limiting gain

$$
-\frac{931}{524288}.
$$

The resulting limiting monochromatic cost is

$$
\frac{21}{512}-\frac{931}{524288}
=\frac{20573}{524288}<\frac1{25}. \tag{8}
$$

This conclusion also holds simultaneously with the finite trap properties
with positive probability at the explicit order above. Fix such a triple
of actual vertices. Put
$\eta=1/25-20573/524288=9963/13107200>\delta$.
The expected new cost differs from (8) times $N^2$ by at most $6N$.
At most $3N$ trials touch these roots, each with difference bound $2N$;
the squared bounds sum to at most $13N^3$. When $N\ge12/\eta$, the
probability that this new cost is at least $N^2/25$ is at most
$\exp(-\eta^2N/26)$. At $N=2^{32}$ this is less than $2^{-64}$.
Adding that fifth failure bound still leaves the sum below one. The exact
rational comparisons used for this explicit order are checked in the
evidence; no numerical probability estimate is a premise.

## A richer averaged row detects the trap

The distinction between pointwise switching and an averaged row matters.
Here is one explicit averaged inequality, valid at every maximum cut,
whose limiting value on the construction is negative. For three ordered
roots $r=(r_0,r_1,r_2)$ let $\tau$ specify colours $(1,0,0)$ and just the
edge $r_1r_2$. Let $Z(r)$ be the mass of vertices adjacent to none of the
roots. Switch the following cells:

- vertices of old colour $1$ adjacent to none of the roots;
- vertices of old colour $0$ adjacent to $r_0$ and to exactly one of
  $r_1,r_2$.

These are cells $\{1,6,10\}$, or switch mask $1090$, in the numbering
above. Write $\Delta(r)$ for the change in the **monochromatic density**
$2M/N^2$, twice the gain convention of (2). A maximum cut satisfies

$$
\mathbb E_r[1_\tau(r)\Delta(r)Z(r)^2]\ge0. \tag{9}
$$

This is an order-seven flag row: three roots, two endpoints for the gain,
and two independent points for $Z^2$. It is also a quadratic form of the
gain-weighted moment matrix in the canonical sketch. In fact its multiplier
is a sum of ordinary nonnegative rooted flag probabilities, so this
particular row does not require a general signed square.

The exact limiting value for the retained-edge construction is

$$
\mathbb E_r[1_\tau(r)\Delta(r)Z(r)^2]
=-\frac{164741871}{2^{47}}<0. \tag{10}
$$

The checker sums the $96$ supporting ordered template-part placements.
For each placement the root-type probability has denominator $8^3$,
the unordered gain has denominator $16^2 8^7$, and $Z$ has denominator
$16\cdot8^3$. The uniform root-part choice contributes $16^{-3}$.
Thus the common denominator before reduction is $16^7 8^{16}$ for the
unordered gain; doubling gives (10). The scalar products are accumulated
as arbitrary-precision integers. This exact separation supplies a concrete
stronger row for the certificate route. It does not show that the row,
alone or with other order-seven rows, proves the full band bound.

There is also a two-root separator using the sketch's hereditary comparison
with the imported uniform bound $B=4/47$. Choose root parts $(2,3)$ and let
$U$ consist of coloured cells $\{0,3,5\}$, subset mask $41$. Thus $U$
contains old-colour-$0$ vertices adjacent to neither root and old-colour-$1$
vertices adjacent to exactly one root. For the limiting construction,

$$
R_{4/47}(r)=\int_U\sigma
-\iint_{U\times U}W[\chi(x)\ne\chi(y)]
+\frac4{47}|U|^2
=-\frac{1077}{1540096}<0.
$$

The evidence recomputes this rational value from the two-root profile
probabilities. This does not contradict two-root switching stability:
hereditary comparison uses a best cut of the entire induced graph on $U$,
which need not be constant on the two-root profile cells. Its validity
assumes global optimality of the old cut and the stated uniform source bound.

## Consequences for the attack

Every constructed graph has a homomorphism to the Clebsch graph. Its five
coordinate cuts leave each supported edge uncut in exactly one coordinate,
so some coordinate cut leaves at most $e/5\le8t^2<N^2/25$ edges uncut.
Thus the graph satisfies the original conjectured bound regardless of the
random edge choices. The bad colouring, not the graph, is the obstruction.

No valid system using only single-vertex stability, deterministic two-root switching
stability, their nonnegative rooted multipliers, and conditions valid for
every coloured triangle-free graph can force $M\le N^2/25$ in the band:
the finite trap itself satisfies all those hypotheses. This includes
arbitrary flag positivity at every order. It does not obstruct a system
using consequences of genuine global optimality that the trap violates.
Fractional two-root switching is a further family not tested by this table.
The exhibited improving three-root move violates another necessary
condition for global optimality. The
full-band maximum-cut argument must therefore retain stronger consequences
of global optimality, such as the exhibited three-root row or hereditary
comparison; neither separation proves the universal three-root implication
or the target.

Run the exact table and constant checks from the repository root:

```sh
uv run --no-sync python wiki/research/triangle_free_bipartization/evidence/main.py --switching-only
```

The ordinary full and quick evidence runs include these checks. Their
scope is the finite calculation supporting this author-recorded argument,
not independent review and not a proof of Problem 23.
