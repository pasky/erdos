---
name: research/leads/projective_plane_bounded_blocking/completion_obstruction
title: What a bounded-cap completion lemma must preserve
desc: An exact Bernoulli calculation leaves quadratically many empty and overloaded lines, while maximal arcs force any exchange adding a point to remove linearly many points; these obstruct specified repair rules, not every absorbing construction.
created: 2026-10-16T20:53:47Z
updated: 2026-10-16T20:53:47Z
---

***

The completion step of the
[[research/leads/projective_plane_bounded_blocking/_index|bounded-blocking sketch]]
needs more than the upper load bound. The following author-recorded
arguments by Plasma AI identify two limitations. They use no independent
review, and neither limitation disproves Problem 1159.

## The independent random start

Fix constants $\lambda>0$ and an integer $C\ge1$. In any plane of order
$q>\lambda$, select each point independently with probability
$\rho=\lambda/q$. Let $Z_j$ count the lines containing exactly $j$
selected points. For each fixed $j\ge0$,

$$
\frac{Z_j}{q^2+q+1}\ \longrightarrow
e^{-\lambda}\frac{\lambda^j}{j!}
\quad\text{in probability as }q\to\infty.
$$

This assertion is uniform over the choice of plane. Indeed, a line's load
is binomial with parameters $(q+1,\rho)$, giving the stated limit of its
point probabilities. Two distinct lines share exactly one point. If $X$
is that point's selection indicator, their remaining loads are independent
binomial variables with parameters $(q,\rho)$, also independent of $X$.
Writing

$$
a=\Pr[\operatorname{Bin}(q,\rho)=j],\qquad
b=\Pr[\operatorname{Bin}(q,\rho)=j-1]
$$

(with $b=0$ for $j=0$), the covariance of the two load-$j$ indicators is
$\rho(1-\rho)(b-a)^2\le\rho$. Consequently, with $N=q^2+q+1$,

$$
\operatorname{Var}(Z_j)\le N/4+N(N-1)\rho,
\qquad \operatorname{Var}(Z_j/N)=O_\lambda(q^{-1}).
$$

Chebyshev's inequality proves the assertion. Apply it to $j=0$ and
$j=C+1$: with probability tending to one there are $\Theta_\lambda(q^2)$
empty lines and $\Theta_{\lambda,C}(q^2)$ overloaded lines. Thus this
independent start needs a substantial alteration. The calculation does
not describe the distribution after trimming, and it supplies no
nonexistence theorem for a dependent random construction. In particular,
neither a positive density of saturated lines after trimming nor a
Poisson upper tail for a greedy process follows from it.

## A family requiring large exchanges

Let $q=2^h$ and $d=2^r$ with $1\le r<h$. There is an explicit point set
$M$ in PG$(2,q)$ of size $(d-1)q+d$ such that every line has load $0$ or
$d$. Such a set is called a maximal arc of degree $d$. The construction
below is included for its repair obstruction; no novelty is claimed.

Choose $\alpha\in\mathbb F_q$ of absolute trace $1$ and an additive
subgroup $H\le(\mathbb F_q,+)$ of order $d$. In the affine chart $Z=1$,
put

$$
Q(x,y)=x^2+xy+\alpha y^2,\qquad
M=\{(x:y:1):Q(x,y)\in H\}.
$$

The quadratic form is anisotropic: for $y\ne0$, a zero would give
$(x/y)^2+x/y=\alpha$, contrary to the trace condition; for $y=0$ only
$x=0$ is a zero. A nonzero trace value exists because the trace polynomial
is nonzero and has degree $q/2<q$.

On a line through the origin with direction $u\ne0$, the values are
$Q(tu)=t^2Q(u)$, a bijection of $\mathbb F_q$. Thus that line contains
$d$ points of $M$. For an affine line not through the origin, write its
points as $v+tu$, where $u,v$ are linearly independent. Then

$$
Q(v+tu)=Q(v)+at^2+bt,
\qquad a=Q(u)\ne0,\quad b=v_1u_2+v_2u_1\ne0.
$$

The additive map $t\mapsto at^2+bt$ has kernel of order two and image an
additive subgroup $W$ of index two. Anisotropy implies $Q(v)\notin W$,
since the affine line does not contain the zero vector. If $H\subseteq W$,
then $H\cap(Q(v)+W)$ is empty. Otherwise this intersection has $d/2$
elements, each with two inverse images. This line therefore meets $M$ in
$0$ or $d$ points. The line at infinity misses $M$. Finally the $q+1$
lines through the origin partition $M\setminus\{0\}$ into sets of size
$d-1$, giving $|M|=(d-1)q+d$.

For any point $P\notin M$, the lines through $P$ partition $M$, so exactly

$$
r_d=\frac{|M|}{d}=q+1-\frac qd
$$

of them have load $d$, and the other $q/d$ are empty. There are in total
$q(q+1-d)/d$ empty lines, by counting incidences of $M$ with its secants.

**Exchange obstruction.** Suppose $R\subseteq M$, $A$ is disjoint from
$M$, and $A\ne\emptyset$. If

$$
M'=(M\setminus R)\cup A
$$

has all line loads at most $d$, then $|R|\ge r_d$. To see this, take
$P\in A$. Each of the $r_d$ saturated lines through $P$ receives at least
one new point and therefore must lose at least one old point. These
required deletions are distinct, since the lines intersect only at
$P\notin M$. This proves the bound even without requiring preservation of
previously covered lines.

In particular, fix any power of two $d\ge4$ and let $q$ grow through
powers of two. No rule promising, from **every** cap-$d$ partial set,
an exchange that covers a new line and uses only a bounded number of
deletions can work. Pure insertion already stops at $M$, with
quadratically many empty lines. This does not exclude preparatory moves
that only delete points: deleting one point of $M$ preserves all its
covered lines because $d\ge2$. A sequence allowing such moves need not
make its first insertion from the original maximal arc.
The direct incidence checks in [the evidence entry point](evidence/main.py)
test the construction and saturated-pencil counts for $q=4,8,16,32$ and
every proper subgroup size $d=2^r$ in that range. The proof, not this
finite check, supplies the unbounded family.

For fixed $d\ge8$, the same planes nevertheless have the cap-six blocking
set from the
[[research/leads/projective_plane_bounded_blocking/parity_construction|three-conic construction]].
Replacing $M$ wholesale by that set is a valid cap-$d$ repair and keeps
every previously covered line covered. It uses at most $|M|=O_d(q)$
deletions and $3q-1$ insertions. Thus the trap can coexist with a blocking
set below its cap: it is an obstruction to small exchanges that immediately
advance coverage, not to the existence of a completed set in those planes.

## Scope and the next completion obligation

The maximal arc is a trap for the cap-only invariant. It is not asserted
to be a state reached by a specified greedy process: if every insertion
must hit a previously empty line, its last inserted point has a tangent
line, whereas $M$ has none. A process with that additional history might
avoid this example. Likewise, a prearranged absorber can have bounded
point support while affecting many lines. The
[[research/leads/projective_plane_bounded_blocking/identities|exchange-footprint bound]]
alone does not exclude it.

A sufficient repair theorem must specify a class $\mathcal I$ of states,
an absolute cap $C$, an initial state in $\mathcal I$ in every plane,
and a construction of exchanges $R,A$ that stay in $\mathcal I$ and obey,
for every line $\ell$,

$$
0\le x_\ell-|R\cap\ell|+|A\cap\ell|\le C.
$$

The new load must be at least one whenever the old load was positive,
and at least one empty line must become covered. These conditions give
termination in at most $N$ moves. Their quantifiers apply only to the
specified states; asserting them for all cap-bounded states with bounded
deletions is false by the construction above. No such sufficient invariant
or repair construction is supplied here. That missing construction is
the positive route's gap, rather than a theorem against all nibble or
absorption methods.
