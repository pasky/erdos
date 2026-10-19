---
name: research/erdos_963/orbit_matching_obstruction
title: 'Complement-orbit matching fails for an arbitrary maximum subset'
desc: An exact positive odd example refutes the every-maximum version, but not the existence or maximum-sum versions or the target.
tags: []
sources: []
created: 2026-09-19T01:37:39Z
updated: 2026-09-19T01:37:39Z
---


# Complement-orbit matching fails for an arbitrary maximum subset

***

This is **not** a counterexample to Erdős 963. It refutes the assertion
that every maximum dissociated subset of a positive odd set satisfies
complement-orbit Hall. The assertion for some maximum subset, including
the possible maximum-sum choice, remains open.

## Construction

First work in $\mathbb Q^2$. Write $z=(1,0)$ and $w=(0,1)$, and set

$$
F=\{9,11,15,19,29,41\},\qquad F'=F\setminus\{15\},
$$


$$
x=5z,\quad y=5w,\quad
E_x=\{(1000+f)z:f\in F'\},\quad
E_y=\{(1000+f)w:f\in F\}.
$$

Let

$$
E=E_x\cup E_y,\quad D=E\cup\{x,y\},\quad c=\sum E,
$$


$$
C=\{c,c+x+y,c+x-y,c-x+y,c-x-y\},\qquad O=D\cup C.
$$

Thus $|D|=13$ and $|O|=18$.

The positive odd integer realization $z\mapsto1,w\mapsto100001$ is

$$
\begin{aligned}
D=\{&5,1009,1011,1019,1029,1041,500005,\\
&100901009,101101011,101501015,101901019,102901029,104101041\},
\end{aligned}
$$

and

$$
C=\{611911223,611911233,612411233,612911233,612911243\}.
$$

Every column has nonnegative first coordinate, and their total first
coordinate is $30659<100001$. Thus no nonzero ternary combination of
the columns can acquire a new zero under this realization: reduction
modulo $100001$ first makes its first coordinate zero, and then its
second coordinate is zero. All arguments below therefore hold for
these positive odd integers.

## The dimension is exactly thirteen

Dissociation of $F$ is proved in
[[research/erdos_963/minimum_sum_matching|the minimum-sum matching note]]. In either
block, a ternary relation has the form

$$
1000\sum_f\varepsilon_f+\sum_f\varepsilon_f f+5\varepsilon_0=0.
$$

Since $\sum F+5=129<1000$, the coefficient sum $\sum_f\varepsilon_f$
vanishes. All $f$ are odd, so the second sum is even, forcing
$\varepsilon_0=0$. Dissociation of $F$ then makes every coefficient
zero. The independent coordinates $z,w$ prove that $D$ is dissociated.

The identities

$$
10=19-9=29-19=41+9-11-29
\tag{1}
$$

remain valid after adding $1000$ to each entry, since their coefficient
sums are zero. The three supports have empty intersection. Thus each
block still ternarily represents $2x$ or $2y$, respectively, after
any single deletion. Destroying both types of representations requires
at least four deletions from $E$.

Consider a fourteen-subset of $O$. If it contains $k$ elements of
$C$, it omits exactly $k-1$ elements of $D$.

* For $k=1$, it contains all of $D$, giving the defining relation.
* For $k=2$ with two noncentral colors, their difference is one of
  $\pm2x,\pm2y,\pm2x\pm2y$. Formula (1) represents it despite the
  possible single deletion. If one color is $c$, use its difference
  $\pm x\pm y$ from the other color when a member of $E$ was deleted;
  otherwise use $c=\sum E$.
* For $k=3$ including $c$, if both $x,y$ remain, use a color minus
  $c$. If both were deleted, use $c=\sum E$. Otherwise at most one
  member of $E$ was deleted, so use the difference between the two
  noncentral colors and (1).
* Any three noncentral colors contain a pair differing by $2x$ and
  a pair differing by $2y$. When $k\le4$, at most three elements of
  $D$ were deleted, so at least one corresponding representation
  from (1) survives. This treats every remaining case with three
  noncentral colors.
* All four noncentral colors satisfy

$$
  (c+x+y)+(c-x-y)=(c+x-y)+(c-x+y).
$$

  This also treats $k=5$.

Each supplied relation has distinct entries and coefficients in
$\{-1,0,1\}$. Thus every fourteen-subset is dependent and $d(O)=13$.

## Five colors occupy four complement orbits

Put $S=\Sigma(D)$ and $T=\sum D=c+x+y$. In any ternary representation
of a color from $C$, every member of $E$ must have coefficient $+1$.
Indeed, decreasing such a coefficient lowers its corresponding
coordinate by at least $1009$, while changing the coefficient of
$x$ or $y$ can compensate by at most $10$.

It follows that the edges of color $c$ are exactly

$$
u\longleftrightarrow c+u,\qquad u\in\{0,x,y,x+y\},
$$

and each noncentral color has one full-support edge. All endpoints
lie in

$$
\{0,x,y,x+y\}\cup\bigl(c+\{0,x,y,x+y\}\bigr).
$$

Under the involution $s\mapsto T-s$, these eight vertices form four
orbits. All four occur as upper-endpoint orbits for color $c$.
Therefore the union of the orbit neighborhoods of the five colors
in $C$ has size exactly four, violating Hall.

The graph of these colors consists of two four-cycles and has graphic
rank six. Hence this construction does **not** refute the weaker
[[research/erdos_963/continuation_routes|rainbow-forest assertion]]. The chosen $D$ is
not maximum-sum among maximum dissociated subsets.
