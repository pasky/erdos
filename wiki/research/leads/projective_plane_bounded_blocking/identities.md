---
name: research/leads/projective_plane_bounded_blocking/identities
title: Incidence identities and exchange rigidity in every projective plane
desc: Moment, pencil and variance identities for line loads, a lower bound on the number of changed lines when each load change is smaller than q, and a modular form of the pencil identity.
created: 2026-10-16T19:59:11Z
updated: 2026-10-16T19:59:11Z
---

# Incidence identities and exchange rigidity in every projective plane

***

These statements hold in every projective plane, Desarguesian or not. They
are elementary and are recorded here with complete author proofs by Plasma
AI, without independent review. They are the all-plane inputs of the
[[research/leads/projective_plane_bounded_blocking/_index|bounded-blocking proof sketch]].

**Setting.** $\Pi$ is a projective plane of order $q\ge2$ with
$N=q^2+q+1$ points and lines. For an integer-valued function $z$ on points,
write $\partial z(\ell)=\sum_{P\in\ell}z(P)$ for its line sums and
$|z|=\sum_Pz(P)$. For a point set $S$ of size $s$, the load of a line is
$x_\ell=\partial 1_S(\ell)=|S\cap\ell|$.

## Moments, pencils and variance

**Moments.** Counting incidences and ordered pairs of distinct points of $S$,

$$
\sum_\ell x_\ell=(q+1)s,\qquad \sum_\ell x_\ell(x_\ell-1)=s(s-1).
$$

**Pencil identity.** For every integer function $z$ and every point $P$,

$$
\sum_{\ell\ni P}\partial z(\ell)=q\,z(P)+|z|.
$$

*Proof.* The $q+1$ lines through $P$ all contain $P$, and every other point
lies on exactly one of them. $\square$

For $z=1_S$ this reads $\sum_{\ell\ni P}x_\ell=s+q\,1_S(P)$. The map
$z\mapsto\partial z$ is injective: if $\partial z=0$, the identity gives
$qz(P)=-|z|$ for every $P$, so $z$ is a constant $c$ with $(q+N)c=0$. A load
function therefore determines its point set. Conversely, an integer
function $x$ on lines with $\sum_\ell x_\ell=(q+1)s$ whose pencil sums take
only the values $s$ and $s+q$ is the load function of the set $S$ of points
with pencil sum $s+q$. Summing the pencil sums over all points gives
$(q+1)^2s=Ns+q|S|$, so $|S|=s$. Then $x$ and $\partial1_S$ have the same
pencil sums, and they are equal because the pencil-sum map on line
functions is injective: it is the map $\partial$ of the dual plane.

**Variance identity.** With $\mu=(q+1)s/N$ the mean load,

$$
\sum_\ell(x_\ell-\mu)^2=sq\Bigl(1-\frac sN\Bigr).
$$

*Proof.* By the moments, $\sum_\ell x_\ell^2=s^2+sq$. Since
$(q+1)^2=N+q$, $N\mu^2=s^2+s^2q/N$. Subtract. $\square$

So every point set, however it is built, has load variance

$$
v=\frac{sq}N\Bigl(1-\frac sN\Bigr)=\mu\,\frac q{q+1}\Bigl(1-\frac sN\Bigr),
$$

asymptotic to its mean when $s=O(q)$. This is an equality of second
moments, not a Poisson approximation or a constraint on tail shape. If
every load lies in $[1,C]$, then
$v\le(\mu-1)(C-\mu)$, the largest variance of a distribution on $[1,C]$
with mean $\mu$. Written out, this is exactly the quadratic inequality of
[[theory/combinatorics/L27_blocking_set_cap/_index|L27]], whose proof sums
$(x_\ell-1)(C-x_\ell)\ge0$. Any construction with a bounded cap must
therefore realize a load distribution with variance close to its mean on a
bounded range; a concentrated distribution is impossible.

## Exchange rigidity

**Lemma (exchange footprint).** Let $z\ne0$ be an integer function on the
points of $\Pi$ with $|\partial z(\ell)|<q$ for every line, and let
$F=\{\ell:\partial z(\ell)\ne0\}$. Then $|F|\ge q+1$. If $|F|=q+1$ and
$|\partial z(\ell)|<q/2$ for every line, then $F$ is the pencil of a point
$P$ and $z=k\,1_{\{P\}}$ for a nonzero integer $k$.

*Proof.* By the pencil identity, $\sum_{\ell\ni P}\partial z(\ell)\equiv|z|$
(mod $q$) at every point $P$. Since $\partial$ is injective, $F$ is nonempty.

Suppose $|F|\le q$. The lines of $F$ cover at most $q(q+1)<N$ points, so some
point lies on no line of $F$, and the congruence there gives
$|z|\equiv0$. A line $\ell\in F$ meets the other at most $q-1$ lines of $F$
in at most $q-1$ of its $q+1$ points, so some point of $\ell$ lies on no
other line of $F$. The congruence at that point gives
$\partial z(\ell)\equiv|z|\equiv0$ (mod $q$), so $\partial z(\ell)=0$ because
$|\partial z(\ell)|<q$. This contradicts $\ell\in F$. Hence $|F|\ge q+1$.

Suppose $|F|=q+1$. Each $\ell\in F$ meets the other $q$ lines of $F$ in at
most $q$ points, so again some point of $\ell$ lies on no other line of $F$,
and $\partial z(\ell)\equiv|z|$ (mod $q$). If some point lay on no line of
$F$, then $|z|\equiv0$ and the previous contradiction recurs. So the $q+1$
lines of $F$ cover every point, and by the lemma below they form the pencil
of a point $P$. All values $\partial z(\ell)$ with $\ell\in F$ are congruent
to $|z|$ modulo $q$ and lie in $(-q/2,q/2)$, so they equal one integer $k$,
and $k\ne0$ because $F$ is the support. Then $\partial z=k\,\partial 1_{\{P\}}$,
since $\partial 1_{\{P\}}$ is the indicator of the pencil of $P$, and
injectivity gives $z=k\,1_{\{P\}}$. $\square$

**Lemma (covering pencils).** A set of $q+1$ lines covering every point is
the pencil of a point.

*Proof.* Dually, let $B$ be a set of $q+1$ points meeting every line. Take
a point $P\notin B$. The $q+1$ lines through $P$ partition the other points,
and each meets $B$, so each contains exactly one point of $B$. Hence every
line through a point outside $B$ meets $B$ exactly once. For distinct
$X,Y\in B$, the line $XY$ meets $B$ twice, so it contains no point outside
$B$; thus $XY\subseteq B$ and, comparing sizes, $B=XY$. Dualizing, the lines
form a pencil. $\square$

**Consequence for exchanges.** Let $R\subseteq S$ and $A$ disjoint from $S$,
not both empty, with every line meeting $A$ and $R$ in fewer than $q/2$
points. The exchange $S\mapsto(S\setminus R)\cup A$ changes the load of
every line in $F$ for $z=1_A-1_R$. It changes at least $q+1$ loads, and
at least $q+2$ unless it inserts or removes a single point, the case
$z=\pm1_{\{P\}}$.

This is a bound on changed **line loads**, not on the number of changed
points. A single insertion has point support one and line support $q+1$;
swapping two distinct points has point support two and line support $2q$.
A bounded-point absorber is not excluded merely because many lines see
its change. Its legality must account for those lines simultaneously.
The small-change hypothesis also matters: replacing a full line by
another full line changes only those two loads, by $q$ and $-q$.
The stronger, but state-specific,
[[research/leads/projective_plane_bounded_blocking/completion_obstruction|large-deletion obstruction]]
uses saturated pencils of a maximal arc; it does not follow just from
the footprint bound.

## A modular form of the pencil identity

**Lemma.** Let $m\ge2$ be coprime to $q$, and let
$W=\{\ell:x_\ell\not\equiv1\pmod m\}$. For every point $P$,

$$
\sum_{\ell\ni P,\ \ell\in W}(x_\ell-1)\equiv s-q-1+q\,1_S(P)\pmod m.
$$

Hence either every point of $S$ or every point outside $S$ lies on a line
of $W$.

*Proof.* Subtract $q+1$ from the pencil identity for $1_S$; lines outside
$W$ contribute multiples of $m$. The right sides for points in and outside
$S$ differ by $q\not\equiv0$, so at least one of them is nonzero modulo
$m$, and a point on no line of $W$ has left side $0$. $\square$

If $W$ were empty, both alternatives would fail unless $S$ or its
complement were empty; but then every load is $0$ or $q+1$, neither
congruent to $1$, so $W$ is all lines. Hence no point set has all its line
intersections congruent to $1$ modulo a number coprime to $q$. For a set
with exactly the intersection numbers $1$ and $n$ this gives
$\gcd(n-1,q)>1$, a weak form of the classical restriction that $n-1$
divides $q$. For a set with all loads in
$[1,4]$, where L27's argument gives
$t_2+t_3=-\tfrac12\bigl(s^2-(4q+5)s+4N\bigr)\le(24q+9)/8$ for the numbers
$t_i$ of lines with $i$ points, the case $m=3$ with $3\nmid q$ says that
the lines with two or three points cover $S$ or cover its complement. In
the second case at least $(N-s)/(q-1)$ of them are needed, since each
contains at most $q-1$ points outside $S$.
