---
name: research/erdos_617/semiregular_parabola_template
desc: Semiregular critical pruning combines the budget, two-support, and bounded exceptions; the explicit square-field completions still lack an independence certificate.
tags: [graph-theory, constructions, conditional, algebra]
sources: []
created: 2026-09-22T14:00:00Z
updated: 2026-09-24T22:12:59Z
---


# research/erdos_617/semiregular_parabola_template

***

**An actual family of edge colorings, but not a counterexample to E617.**
The construction below preserves many prescribed full monochromatic
components. Its residual independence numbers are uncontrolled.
It addresses the semiregular idea in
[Construction attempts](construction_attempts.md), using the additive
group of a square finite field rather than the cyclic group of that
order. No search over individual parameters is used.

Let $q\ge3$ be an odd prime power, $r=q^2$, and $F=\mathbb F_r$.
The vertices are $(F\times F)\cup\{\infty\}$, and the colors are $F$.
Translations act by $T_t(a,x)=(a,x+t)$, fixing infinity and translating
colors by $t$. Prescribe the star color

$$
c(\infty,(a,x))=x.
$$


Choose a nonsquare $\theta\in F$ and put $C=\theta\mathbb F_q$.
Every nonzero element of $\mathbb F_q$ is a square in $F$, so every
nonzero difference in $C$ is a nonsquare. Choose arbitrary $b_j\ne0$
for $j\in C$, and prescribe

$$
Q_{j,t}=\{(j,t+b_j)\}\ \cup\
\{(j+u^2,t+u):u\in F^\times\}
\tag{1}
$$

as a color-$t$ clique, for every $j\in C$, $t\in F$.

## Intersections of the prescribed blocks

Each block has $r$ vertices. Before moving its singleton point, it is
the parabola $a=(x-t)^2+j$. Parabolas with the same $t$ and different
$j$ are disjoint. Two with distinct $t,s$ meet uniquely, by subtracting
their equations and using $2(t-s)\ne0$.

The modification from $(j,t)$ to $(j,t+b_j)$ changes no intersection
between different $j,k\in C$: the parabola for $k$ has no vertex in
row $j$, because $j-k$ is a nonsquare. For two translates of the same
$j$, their original intersection has nonzero parabola parameters
$(s-t)/2$ and $(t-s)/2$, so neither deleted singleton is involved.
Their new singleton points are distinct as well. Consequently

$$
Q_{j,t}\cap Q_{k,t}=\varnothing\ (j\ne k),\qquad
|Q_{j,t}\cap Q_{k,s}|=1\ (t\ne s). \tag{2}
$$

Thus the prescribed clique edges have consistent colors.

The second coordinates in $Q_{j,t}$ comprise every element except
$t$, with $t+b_j$ repeated. Hence its vertices have no color-$t$
star edges to infinity. This differs from the unchanged parabola,
which contains a vertex in its own star fiber.

## Row incidences

Let $f(a)$ be the number of prescribed blocks, across all colors,
through a fixed vertex in row $a$. Equivalently it is the number of
color-zero prescribed vertices in that row. Then

$$
f(a)=\begin{cases}1,&a\in C,\\q+1,&a\notin C.\end{cases} \tag{3}
$$

For $a\in C$ only the shifted singleton for $j=a$ contributes.
For $a\notin C$, the number of nonzero solutions to $u^2=a-j$,
summed over $j\in C$, is $q+\sum_{j\in C}\chi_F(a-j)$.

To compute the latter sum, write $z=a/\theta\notin\mathbb F_q$.
The quadratic characters satisfy $\chi_F(w)=\chi_q(N(w))$, so

$$
\sum_{j\in C}\chi_F(a-j)
=-\sum_{s\in\mathbb F_q}\chi_q(N(z-s))=1.
$$

Indeed $N(z-s)$ is a monic quadratic in $s$ with nonzero
discriminant, and its character sum is $-1$. One elementary proof
of this identity completes the square and counts solutions to
$y^2=x^2-D$ for $D\ne0$: the equation
$(x-y)(x+y)=D$ has $q-1$ solutions. This proves (3), and gives

$$
\sum_{a\in F}f(a)=rq,\qquad
\sum_{a\in F}f(a)^2=r(r+q-1). \tag{4}
$$


## Equivariant completion preserving the components

Every orbit of an unordered old edge under $T_t$ has length $r$.
A nonidentity stabilizer would swap its endpoints and force $2t=0$,
impossible in odd characteristic. The prescribed edges form whole
edge orbits, with colors changing equivariantly.

For an unprescribed orbit, at most $f(a)+f(b)\le2(q+1)<r$
translates touch a prescribed color-zero block, where $a,b$ are
the endpoint rows. Choose any other translate, color it zero, and
color its $T_t$-translate with color $t$. Repeating for all remaining
orbits completes the coloring. This can be made deterministic by
fixing orders of the finite field and the edge orbits and always
choosing the first permitted translate.

No new color-zero edge touches a prescribed color-zero block;
equivariance gives the same assertion in every color. The prescribed
cliques are therefore whole components. The star prescription also
preserves them, as checked above. All colors have equal edge count

$$
e(G_t)=\binom{r^2+1}{2}/r=r(r^2+1)/2. \tag{5}
$$

This proves existence of completed colorings with the prescribed
geometry. It supplies **no bound** $\alpha(G_t)\le r$.

## A conditional exact light-anchor identity

Suppose hypothetically that a completion also satisfied
$\alpha(G_t)\le r$ in every color. Remove the $q$ prescribed
color-zero components and call the residue $H$, putting $a_0=r-q$.
Component additivity and a foreign full clique give

$$
|H|=a_0r+1,\qquad \alpha(H)=a_0.
$$

For each $j\in C$, $t\ne0$, the set
$I_{j,t}=Q_{j,t}\cap H$ is maximum independent in $H$, of size $a_0$.

Equivariance gives a row-degree identity independent of how the
unprescribed orbits were completed:

$$
\sum_{x\in F}d_0(a,x)=\sum_{t\in F}d_t(a,0)=r^2.
$$

There are $f(a)$ removed vertices in row $a$, each of degree $r-1$.
The remaining vertices have no edges into the removed components.
Every such vertex belongs to $f(a)$ foreign prescribed anchors.
Consequently (4) yields

$$
\begin{aligned}
\frac1{q(r-1)}\sum_{j\in C,\ t\ne0}\sum_{v\in I_{j,t}}d_H(v)
&=\frac{\sum_{a\in F}f(a)[r^2-f(a)(r-1)]}{q(r-1)}\\
&=a_0(r-1)+r+1+\frac1{r-1}.
\end{aligned} \tag{6}
$$

Since every anchor degree sum is integral, some anchor has sum at
most $a_0(r-1)+r+1$.

The foreign-full-clique argument gives one or two anchor neighbors
at every outsider. If $b$ is its two-supported exception count,
the exact private-row identity is

$$
\sum_{v\in I}d_H(v)=a_0(r-1)+b+1.
$$

Thus (6) supplies $b\le r$ in a residue that also retains the
least-color budget.

This remains true after removing any additional full components:
each foreign anchor loses exactly one vertex of degree $r-1$ per
component, so both the parameter and the average decrease accordingly.
It does not justify deleting a noncomponent full clique or critically
pruning without reconsidering the degree identity.
The final section below supplies a replacement identity after
equivariant critical pruning, with all full components removed.

## The unmet condition

The sole construction claim proved unconditionally is the existence
of the complete edge colorings in (1)--(5). The requirement

$$
\alpha(H_t)\le r-q
$$

on all residuals has neither been proved nor disproved. The conditional
common-budget, bounded-exception residue need not have minimum degree $r$, and
it need not be $K_r$-free. Therefore neither minimum-anchor normalization nor
the new [maximum-set surplus inequality](maximum_set_surplus.md) can be applied
while silently keeping its original parameter $r-q$.

## Conditional divisibility of residual components

Continue to suppose that a completion is independence-valid, and remove
the $q$ prescribed color-zero components. For a component $D$ of the
residue, put $n_D=|D|$, $h_D=\alpha(D)$,
$\varepsilon_D=\mathbf1_{\{\infty\in D\}}$, and
$z_D=|D\cap(C\times F)|$. Then

$$
\boxed{(q+1)(n_D-\varepsilon_D)-qz_D=q(r-1)h_D.} \tag{7}
$$

Every foreign prescribed clique meets $D$ in exactly $h_D$ vertices:
its intersection with the whole residue is maximum independent, and
independence is additive over components. Sum over the $q(r-1)$
foreign prescribed cliques. By (3), each residual vertex in a special
row has one such incidence, each other old residual vertex has $q+1$,
and infinity has none. This proves (7).
In particular

$$
|D|\equiv\mathbf1_{\{\infty\in D\}}\pmod q.
$$

Any additional full $K_r$ component therefore excludes infinity and
has exactly $q+1$ vertices in special rows. These restrictions have
not ruled out the template.

The distinct
[complementary-parabola criterion](parabola_completion_criterion.md) handles
retaining the intercepts outside a small set without shifting the singleton
points. It likewise supplies no independence certificate.

The block intersections, quadratic character sum, orbit completion, and exact
anchor average were checked by the author and are author-recorded. This is not a
counterexample and establishes no positive case of E617.

## General semiregular averaging after critical pruning

**Proved conditional reduction, not an exclusion of the template.**
The light-anchor conclusion survives equivariant critical pruning,
without assuming that infinity avoids full components. This works for
any odd-order additive group $A$ of order $r\ge12$, with vertices
$\{\infty\}\cup([r]\times A)$ and palette $A$, when translation of the
second coordinate fixes infinity and translates the palette. Assume,
conditionally, that every color has independence at most $r$.

Every translated edge orbit has one edge of each color. If an edge can
be deleted while retaining its color's independence bound, delete its
whole orbit. Isomorphism makes every deletion safe in its respective
color. At termination the colors remain isomorphic and are
independence-critical, each with independence $r$ and at most
$E_0=r(r^2+1)/2$ edges. The
[critical-component lemma](critical_component_reduction.md) therefore
makes every full clique a component. Each color has the same number
$k\ge3$ of them.

Write the color-zero components as $Q_1,\ldots,Q_k$, set $a=r-k>0$,
and remove them to obtain $H$. Then

$$
|H|=ar+1,\quad \alpha(H)=a,\quad \omega(H)\le r-1,\quad
2e(H)\le ar(r-1)+r(r+1).
$$

The residue is independence-critical, but is not asserted connected
or to have minimum degree $r$.

Let $\varepsilon$ indicate whether infinity belongs to a full
component, and put

$$
m_j(u)=|Q_j\cap(\{u\}\times A)|,\qquad f(u)=\sum_jm_j(u).
$$

Every foreign full component meets every $Q_j$ once and $H$ in exactly
$a$ vertices: it is a color-zero independent $r$-set, and those
componentwise upper bounds sum to $r$.
Counting old intersections with all translates gives

$$
\sum_u f(u)=kr-\varepsilon,\qquad
\sum_u f(u)^2=kr+k^2(r-1)-\varepsilon r. \tag{8}
$$

Indeed the zero translate contributes $kr-\varepsilon$ to the second
sum. Each nonzero translate contributes $k^2-\varepsilon$: the only
intersection that can occur at infinity is between the unique
infinity-containing component and its translate.

Equivariance gives the row-degree inequality

$$
D_u:=\sum_{x\in A}d_0(u,x)=\sum_{t\in A}d_t(u,0)\le r^2.
$$

Every removed old vertex has degree $r-1$. Every old residual vertex
in row $u$ belongs to exactly $f(u)$ of the $k(r-1)$ foreign-component
anchors $I_{j,t}=T_tQ_j\cap H$, $t\ne0$. Infinity belongs to none:
either it was removed, or no full component contains it. Hence (8)
gives

$$
\begin{aligned}
\frac1{k(r-1)}\sum_{j,t\ne0}\sum_{v\in I_{j,t}}d_H(v)
&\le\frac{\sum_u f(u)[r^2-(r-1)f(u)]}{k(r-1)}\\
&=a(r-1)+r+1+\frac1{r-1}
 -\frac{\varepsilon r}{k(r-1)}. \tag{9}
\end{aligned}
$$


Every outsider has one or two color-zero neighbors in such an anchor.
Its edges into the foreign full clique must supply each other color,
even in the partial coloring, and no target edge can enter a removed
target component. If $b$ counts the two-supported outsiders, private-row
counting gives
$\sum_{v\in I}d_H(v)=a(r-1)+b+1$.
Integrality in (9), and $k<r$, supply an anchor with

$$
\boxed{b\le r-\varepsilon.} \tag{10}
$$

Thus this restricted symmetry class does combine the least-color
budget, $K_r$-freeness, criticality, two-support, and $b\le r$ in one
residue. It still does not give full private minimum degree or the
proper-induced minimal-ratio condition, and has not been excluded.

An earlier attempted proof incorrectly treated the row graphs as
matchings. Semiregularity fixes their edge counts, not their degree
sequences. The resulting claims of unique singleton rows and exclusion
of infinity from all full components were discarded. Equations
(8)--(10) use neither claim. No assertion of an independence-valid
completion follows from this conditional calculation.
