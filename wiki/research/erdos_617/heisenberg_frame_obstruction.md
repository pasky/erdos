---
name: research/erdos_617/heisenberg_frame_obstruction
desc: An anisotropic-norm component template has an explicit low-row independence certificate, but its natural frame completion is too robust to accommodate infinity.
tags: [graph-theory, proved, constructions, finite-fields]
sources: []
created: 2026-09-22T16:20:00Z
updated: 2026-09-24T22:12:59Z
---


# research/erdos_617/heisenberg_frame_obstruction

***

**Rejected parameterized construction, not a counterexample.** The
template below has a rigorous independence certificate on one special
row. That certificate cannot extend over the extra vertex. No claim of
independence control on the entire old vertex set is made.

## 1. Prescribed full components

Let $q\ge3$ be an odd prime power, $r=q^2$, and
$W=\mathbb F_q^2$. Choose a nonsquare $D$, put

$$
N(x_1,x_2)=x_1^2-Dx_2^2,\qquad
\Omega(x,y)=x_1y_2-x_2y_1,
$$

and let $B_N$ be the polar bilinear form of $N$.
For $d\ne0$, the linear forms $B_N(a,d)$ and
$\Omega(a,d)$ are independent: their determinant is
$-2N(d)\ne0$.

Take vertices $(x,z,t)\in W\times\mathbb F_q\times\mathbb F_q$,
together with $\infty$, and colors $a\in W$. Prescribe the
$q$ color-$a$ full components

$$
Q_{a,b}=\{(x,b+\Omega(a,x),N(x-a)):x\in W\},
\qquad b\in\mathbb F_q.
$$

Each has order $r$. Components in the same color are disjoint.
Two prescribed components of different colors meet once: equality
of their $t$ and $z$ coordinates gives the two independent
linear equations just described. Thus their clique edges are
compatible.

The transformations

$$
T_{h,c}(x,z,t)=(x+h,z+c+\Omega(h,x),t)
$$

fix $\infty$, form a group of order $q^3$, and translate the
colors by $a\mapsto a+h$. They preserve the prescribed components.
For $t=0$, a point belongs to prescribed components in one color;
for $t\ne0$, it does so in $q+1$ colors. This uses the norm
fiber sizes $|N^{-1}(0)|=1$ and $|N^{-1}(s)|=q+1$ for $s\ne0$.

Every unprescribed pair therefore has at least
$q^2-2(q+1)>0$ colors whose prescribed components contain neither
endpoint. The action has trivial stabilizers on unordered edges:
an element fixing an old point is the identity, and a group of odd
order cannot interchange the two endpoints of an edge. One may choose
a permitted color on each edge orbit and propagate it. Consequently
equivariant component-preserving completions exist as colorings. This
is a completion statement only, not an independence statement.

## 2. The frame coloring of the low-incidence row

Put $S=\{(x,z,0)\}$, of order $q^3$. In color $a$, the
$q$ points with $x=a$ are isolated in $S$, since they lie in
different prescribed full components. Call them holes.

For every $s\in\mathbb F_q^\times$ and $b\in\mathbb F_q$,
color the clique

$$
R_{a,s,b}=\{(x,b+\Omega(a,x),0):N(x-a)=s\}
$$

with color $a$. These are $q(q-1)=r-q$ cliques of order $q+1$,
partitioning the nonholes in that color. Their edges over all colors
partition exactly the pairs in $S$ with different $x$-coordinates.
Indeed the equal-norm and equal-intercept equations uniquely determine
$a$ for such a pair, and their common norm is nonzero by anisotropy.
Pairs with the same $x$-coordinate can be colored equivariantly while
avoiding the hole color $x$.

Each resulting color graph on $S$ has independence exactly $r$.
The clique partition and holes give the upper bound. To attain it,
take all holes. For each $s\ne0$, select one vertex from each of
its $q$ blocks with distinct $x$-coordinates, using a matching
from the $q$ block labels into the $q+1$ points of the norm
circle. Different norm circles use different coordinates. Thus the
selected vertices also avoid all additional same-coordinate edges.

## 3. Robustness defeats the extra vertex

Deleting any $q$ nonhole vertices from $S$ still leaves an
independent $r$-set in every specified color $a$. In a fixed
norm circle, the preceding matching problem is $K_{q,q+1}$ with
some cells deleted. A Hall obstruction on $k$ left vertices
requires at least

$$
k(q+2-k)\ge q+1\qquad(1\le k\le q)
$$

deleted cells. At most $q$ deletions in total cannot create one.
Make the matchings separately for all norm circles and retain all
holes.

Equivariance forces $\infty$ to have exactly $q$ neighbors of
each color in $S$: the action is transitive on $S$, on the
$q^2$ colors, and has color kernel the central $z$-translations.
Those neighbors are nonholes by component preservation. The robust
independent $r$-set can avoid them, and adjoining $\infty$
gives an independent $(r+1)$-set.

Thus this particular frame completion is rigorously excluded. A
successful modification would need a low-row color graph with a
$q$-vertex nonhole set meeting every maximum independent set;
the frame graph has no such set. No simultaneous replacement, or
whole-graph independence certificate, was obtained.

## 4. Every clique-component certificate fails when q is prime

For odd **prime** $q$, there is a broader obstruction. No
equivariant component-preserving completion can satisfy the desired
independence bounds if each color graph restricted to $S$ is a
disjoint union of cliques. This does not assume the norm-frame
partition of Section 2.

Equivariance makes all color graphs on $S$ have the same edge
count

$$
e_0=\frac{\binom{q^3}{2}}{q^2}=\frac{q^4-q}{2}.
$$

Their independence number must equal $q^2$ in any proposed
counterexample. It is at most $q^2$ by assumption. If it were
at most $q^2-1$, deleting the $q$ isolated holes and using
complementary Turan would instead give

$$
e_0\ge p_{q^2-q-1}(q^3-q)=e_0+2q+1.
$$


Fix a color. Under the clique-component assumption it has exactly
$q^2-q$ nonhole components. The central group of order $q$
permutes them in orbits of length one or $q$. Thus the number
$f$ of fixed nonhole components is divisible by $q$. Every
fixed component contains a whole $x$-column of $q$ points.
The number of such full columns per color is the same by equivariance
and is at most one: each uses $\binom q2$ same-coordinate edges,
and the $q^2$ colors must share just $q^2\binom q2$ such edges.
Hence $f\le1$, and therefore $f=0$.

Every nonhole component now contains at most one point of any column.
Indeed two points in a column differ by a nonidentity central
translation. That translation makes the component intersect its image,
so stabilizes it. Since $q$ is prime this would make the component
fixed by the entire central group, which was excluded.

The color-neighborhood of $\infty$ in $S$ is one whole
nonhole column. To meet every maximum independent set in a union of
cliques, a set must contain some entire component: otherwise choose
one vertex outside it from each component. The star column must
therefore contain an entire nonhole component, necessarily a singleton.
Its central orbit supplies $q$ additional isolated vertices.

After removing these and the original holes, complementary Turan
gives, with $n=q^3-2q$ and $b=q^2-2q>0$,

$$
2e_0\ge2p_b(n)\ge\frac{n^2}{b}-n.
$$

But direct subtraction yields

$$
\frac{n^2}{b}-n-(q^4-q)
=q^3+3q+\frac{4q}{q-2}>0,
$$

a contradiction. Thus, at least for prime $q$, replacing the
frame by another clique partition cannot produce the missing low-row
certificate. Non-clique color components remain a possible direction,
with no established global independence certificate.

The Hall obstruction and this broader prime-order argument were checked
independently. No finite search was used.
