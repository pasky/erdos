---
name: research/erdos_132/topological_filtrations
title: Rich distance classes invisible to planar topology
desc: |
  Triangular lattice triangles have arbitrarily many initial rich classes
  while their Rips shadows, Rips fundamental groups, and disk-union topology
  have already stabilized. This rules out specific topological accounting arguments.
sources: []
research_state: closed
created: 2026-09-22T21:50:03Z
updated: 2026-09-24T22:12:56Z
---


# Rich distance classes invisible to planar topology

***

This approach does not resolve either assertion of
[Problem 132](../../problems/distance_problems/E0132/_index.md). What it establishes is
an exact limitation of charging rich distance classes to changes in planar
topology. No computation or external theorem about distance multiplicities is
used.

Let

$$\omega=e^{i\pi/3},\qquad
A_N=\{a+b\omega:a,b\in\mathbb Z_{\ge0},\ a+b\le N\},
\qquad n=\binom{N+2}{2}.$$

For every prescribed integer $K\ge1$, sufficiently large $N$ has
arbitrarily many initial rich distance classes, but all their occurring
thresholds have the same planar Rips shadow and trivial Rips fundamental
group. All but the first also occur after the disk union is contractible.

## Planar shadow and fundamental group

Write $C_N=\operatorname{conv}(A_N)$. For $r\ge0$, let
$\operatorname{VR}_r(A_N)$ denote the abstract complex whose simplices
are the subsets of diameter at most $r$. Its planar shadow is the union
of the geometric convex hulls of those simplices.

The standard triangulation of $C_N$ consists of equilateral unit
triangles. These are simplices of $\operatorname{VR}_r(A_N)$ whenever
$r\ge1$. Every simplex shadow is contained in $C_N$. Therefore the
planar shadow is exactly the same closed triangle $C_N$ for all $r\ge1$.

In fact,

$$\pi_1(\operatorname{VR}_r(A_N))=0\qquad(r\ge1). \tag{1}$$

For an edge $pq$, write $q-p=a+b\omega$. There is a unit-edge lattice
path from $p$ to $q$ in $A_N$ using two adjacent lattice directions,
with the distances from $p$ increasing along the path. Here are the
details ensuring it stays in the finite triangle.

If $a,b$ have the same sign, use the corresponding directions $1,\omega$
or their negatives. Both coordinates and their sum stay between their
endpoint values. If $a\ge0$ and $b=-c\le0$, first take $\min(a,c)$
steps in direction $1-\omega$, then the remaining steps in direction
$1$ if $a\ge c$, or $-\omega$ if $c\ge a$. Both coordinates stay
between their endpoint values; the first part preserves their sum,
and the second changes it monotonically to its final value. The other
mixed-sign case is symmetric. Thus all path vertices satisfy the three
defining inequalities of $A_N$.

The two directions used in each case make angle $60^\circ$. For
nonnegative integer coefficients, adding either direction strictly
increases the squared norm of the partial displacement. Consequently,
writing the path as $p=p_0,p_1,\ldots,p_s=q$,

$$|p-p_i|\le |p-q|\le r.$$

Every nondegenerate fan triangle $(p,p_i,p_{i+1})$ is therefore a Rips
simplex: its two radial edges have length at most $r$, and its third
edge has length one. This fan homotopes $pq$ to the unit-edge path,
fixing its endpoints. Every loop in the Rips complex can first be
represented in its one-skeleton, then homotoped to unit edges by these
fans. The resulting loop contracts in the standard triangular
triangulation of $C_N$, already a subcomplex. This proves (1), and hence
$H_1(\operatorname{VR}_r(A_N);\mathbb Z)=0$.

This argument does **not** show that the abstract Rips complex is
contractible. Its higher homology and full Euler characteristic have
not been controlled.

## Disk unions stabilize before the second distance

Put $U_\rho=\bigcup_{a\in A_N}\overline B(a,\rho)$. Every point of a
unit equilateral triangle is within $1/\sqrt3$ of a vertex, so

$$C_N\subseteq U_\rho\qquad(\rho\ge1/\sqrt3).$$

For these radii, nearest-point projection $\pi$ onto the closed convex
set $C_N$ defines a strong deformation retraction of $U_\rho$ onto
$C_N$. Indeed, if $x\in\overline B(a,\rho)$ with $a\in A_N$, the
convex-projection inequality gives

$$|\pi(x)-a|\le|x-a|\le\rho.$$

The segment joining $x$ to $\pi(x)$ stays in that same convex disk.
Thus $H(x,t)=(1-t)x+t\pi(x)$ is the required homotopy. In particular,
$U_\rho$ is contractible for every $\rho\ge1/\sqrt3$.

For $N\ge2$ the first two distances are $1,\sqrt3$. Squared lattice
lengths are $a^2+ab+b^2$; they cannot equal $2$, since modulo $3$ this
form equals $(a-b)^2$, while $1$ and $3$ both occur. The pair-contact
radius of the second distance satisfies

$$\sqrt3/2>1/\sqrt3.$$

Hence every later distance-class contact occurs while disk-union
homology is already trivial. The same obstruction applies to a complex
model whenever it is known to be homotopy equivalent to that union;
no additional statement about such a model is needed here.

## Arbitrarily many initial classes are rich

For a nonzero lattice displacement $v=a+b\omega$, put

$$S(v)=\max\{|a|,|b|,|a+b|\}.$$

The number of pairs with the chosen oriented displacement $v$ is
exactly $\binom{N-S(v)+2}{2}$ when $N\ge S(v)$. To check this, a
starting point $x+y\omega$ must satisfy

$$x\ge\max(0,-a),\quad y\ge\max(0,-b),\quad
x+y\le N-\max(0,a+b).$$

Translate the two lower bounds to zero and use

$$\max(0,-a)+\max(0,-b)+\max(0,a+b)=S(v).$$

There remain two nonnegative integer coordinates with sum at most
$N-S(v)$, giving the formula.

Rotation through $60^\circ$ sends $(a,b)$ to $(-b,a+b)$ and preserves
$S(v)$. The three resulting unoriented directions are distinct, and
their unordered pair sets are disjoint. Thus

$$m_{A_N}(|v|)\ge3\binom{N-S(v)+2}{2}. \tag{2}$$

If $S(v)\le N/3$, the right side is strictly greater than
$\binom{N+2}{2}=n$. For example, after multiplying by two, the lower
bound from $N-S(v)\ge2N/3$ exceeds $(N+1)(N+2)$ by
$N^2/3+3N+4>0$.

Also $S(v)\le2|v|/\sqrt3$, by completing the square in
$a^2+ab+b^2$ for each of $a,b,a+b$. Therefore

$$N\ge3\left\lceil\frac{2K}{\sqrt3}\right\rceil$$

ensures that every occurring distance at most $K$ is rich. There are
at least $K$ such distances, since $0,1,\ldots,N$ belong to $A_N$.
This proves the claimed richness of the first $K$ classes.

## Exact scope of the obstruction

There can be arbitrarily many consecutive rich class additions with
constant planar Rips shadow, zero Rips $H_1$, and constant disk-union
homotopy type. Thus none of these invariants can require each rich
class to spend a nonzero amount of topology. This does not rule out
more elaborate arguments using additional geometry or higher abstract
Rips homology. No such successful argument was established.

These configurations are not counterexamples to Erdős 132: nothing
here bounds their total number of rare classes.
