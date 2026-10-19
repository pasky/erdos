---
name: research/erdos_1145/counting_regularity
desc: Elementary consequences of termwise balance and bounded cross representations.
tags: [proved, reductions]
sources: []
created: 2026-09-22T18:15:49Z
updated: 2026-09-24T22:12:57Z
---


# research/erdos_1145/counting_regularity

***

Write $A(x)=|A\cap[1,x]|$, $B(x)=|B\cap[1,x]|$, and suppose

$$
a_n/b_n\longrightarrow1,\qquad 1\le r_{A,B}(n)\le M
\quad(n\text{ sufficiently large}).
$$

Increasing $M$ if necessary makes the upper bound hold for every $n$.
All claims below are proved elementary consequences, not a resolution of the
problem.

Section 1 of the independent investigation
recovers these estimates. Its explicit rank constants, uniform local form,
and coverage-only gap restriction have been checked and are included below.

Sections 2--3 of the later independent input
also check out. Its common limiting measure and
$dt\le\mu*\mu\le M\,dt$ are already included in the
energy formulation; the continuous square-root
model does not settle the discrete question. Its Narkiewicz-based
product bound $\limsup A(x)B(x)/x>1$ is weaker than the established
$4/\pi$ bound in [collision density](collision_density.md), proved
without a representation upper bound. That note also excludes eventual
uniqueness under balance, without classifying eventually unique pairs.

### Comparison with the third independent input

Sections 2.1--2.4 of the
third independent input correctly
recover the square-root bounds, equal counting functions to first order,
local continuity, and the common convolution limit. Its conclusion under
eventual uniqueness,
$$
 A(x)\sim B(x)\sim\frac2{\sqrt\pi}\sqrt x,
$$
is a valid necessary condition, but does **not** leave eventual uniqueness
as an open subcase of the current research. The established
[collision-density argument](collision_density.md) already excludes it;
[nonconstant representations](nonconstant_representations.md) forces
disagreement with every nonzero periodic pattern on a set of positive
lower density. No classification of eventually unique complements is
needed for either conclusion.

Its continuous square-root model correctly shows that
$dx\le\mu*\mu\le M\,dx$ alone is insufficient. This is consistent
with, but weaker than, the checked bounded models for the additional
second-moment constraints in energy deficit.
Likewise, its bounded-displacement thickening argument in Section 2.5
is valid; the finite-shift union reduction below already gives a more
general statement and a smaller bound when $D\ge1$. These comparisons
do not change the unresolved status of the unrestricted problem.

## Square-root size

Counting covered integers and all pairs below $x$ gives

$$
x-O(1)\le A(x)B(x)\le2Mx.
$$

Balance gives $A(x)\le B(2x)+O(1)$. Thus

$$
A(x)(A(x)-O(1))\le A(2x)B(2x)\le4Mx,
$$

and symmetrically $B(x)=O(\sqrt x)$. The lower product bound now gives

$$
A(x),B(x)=\Theta(\sqrt x),\qquad a_n,b_n=\Theta(n^2).
$$

More precisely, the first $n$ elements of each set supply $n^2$
pairs with sums at most $a_n+b_n$, whereas every represented integer
below $\min(a_n,b_n)$ uses only the first $n-1$ elements of each set.
Thus
$$
n^2\le M(a_n+b_n),\qquad
\min(a_n,b_n)\le(n-1)^2+O(1).
$$
Termwise balance and inversion of these bounds give
$$
\frac{1-o(1)}{2M}n^2\le a_n,b_n\le(1+o(1))n^2,
\qquad
(1-o(1))\sqrt x\le A(x),B(x)
\le(\sqrt{2M}+o(1))\sqrt x.
$$

## Same counting function to first order

Fix $0<\varepsilon<1/2$, and take $x$ sufficiently large that all relevant
ranks satisfy $(1-\varepsilon)b_i\le a_i\le(1+\varepsilon)b_i$.
If $K=A(x)-B(x)>0$, each rank $B(x)<i\le A(x)$ has

$$
(1-\varepsilon)x<a_i\le x<b_i\le x/(1-\varepsilon).
$$

The $K^2$ pairs drawn from these two rank blocks have sums in an interval
of length $(\varepsilon+\varepsilon/(1-\varepsilon))x$. Consequently

$$
K^2\le M\bigl((\varepsilon+\varepsilon/(1-\varepsilon))x+2\bigr).
$$

Interchanging $A,B$ handles negative $K$. Taking the limsup as
$x\to\infty$ and then $\varepsilon\downarrow0$ proves

$$
A(x)-B(x)=o(\sqrt x),\qquad A(x)/B(x)\longrightarrow1.
$$

Without the representation bound, replacing termwise balance by equal
counting functions is not justified in this way.

## Local continuity

For fixed $0\le s<t$, let $K=A(tX)-A(sX)$. The corresponding $B$-ranks
lie between $sX/(1+\varepsilon)$ and $tX/(1-\varepsilon)$, apart from a
fixed finite initial block. Their $K^2$ sums lie in an interval of length

$$
\left(t-s+\frac{t}{1-\varepsilon}-\frac{s}{1+\varepsilon}\right)X.
$$

Hence

$$
\limsup_{X\to\infty}\frac{A(tX)-A(sX)}{\sqrt X}
\le\sqrt{2M(t-s)}.
$$

The same holds for $B$. In particular, subsequential rescaled counting
measures have a common, nonatomic limit with a (1/2)-Hölder distribution
function. This regularity alone does not contradict bounded multiplicity:
the measure $c x^{-1/2}\,dx$ has a constant self-convolution density.

There is also the uniform formulation
$$
A(x+h)-A(x)\le\sqrt{2Mh+o(x)}\qquad(0\le h\le x),
$$
and the analogous bound for $B$, where the error is independent of
$h$. Indeed, the corresponding ranks have $a_i\in(x,x+h]$
and $b_i=a_i+o(x)$, uniformly over $a_i\in(x,2x]$.
All cross pairs from these rank blocks therefore lie in an interval of
length $2h+o(x)$. The representation bound proves the assertion,
with the endpoint error absorbed into $o(x)$.

## A gap restriction using only balance and coverage

Drop the representation upper bound. For every sufficiently large $n$,
coverage of $a_n+b_n+1$ forces
$$
\min(a_{n+1},b_{n+1})\le a_n+b_n+1.
$$
Otherwise a representation could use neither a later $A$-element nor
a later $B$-element, and its sum would be at most $a_n+b_n$.
Using balance at ranks $n$ and $n+1$ yields
$$
\limsup_{n\to\infty}\frac{a_{n+1}}{a_n}\le2,
\qquad
\limsup_{n\to\infty}\frac{b_{n+1}}{b_n}\le2.
$$
This necessary condition does not control multiplicities.

## Bounded displacement reduces to the diagonal problem

Section 7.4 of the later independent input gives a correct reduction
which works at every fixed capacity, unlike the stronger exclusions
at capacities two or three in discrepancy fibers.
Here is a slightly more general version, not requiring rank balance.

Suppose $A+B$ is cofinite, $r_{A,B}\le M$ eventually, and finite
sets $E,F\subset\mathbb Z$ satisfy
$$
 A\subseteq\bigcup_{t\in E}(B+t),\qquad
 B\subseteq\bigcup_{s\in F}(A+s).
$$
Choose one witnessing shift for each element. Mapping
$(a,a')$ to $(a,a'-t(a'))$, separately for each fixed shift,
gives
$$
 r_{A,A}(n)\le\sum_{t\in E}r_{A,B}(n-t).
$$
The map is injective on each shift fiber. Similarly, mapping
$(b,b')$ to $(b-s(b),b')$ gives
$$
 r_{B,B}(n)\le\sum_{s\in F}r_{A,B}(n-s).
$$
Thus $C=A\cup B$ is a one-set asymptotic basis with
$$
 r_{C,C}(n)
 \le r_{A,A}(n)+2r_{A,B}(n)+r_{B,B}(n)
 \le (|E|+|F|+2)M
$$
for all sufficiently large $n$. Finitely many initial counts are
also bounded. Finite exceptions to the inclusions can be absorbed by
adding finitely many witnessing shifts.

In particular, if $S=\{b_i-a_i:i\ge1\}$ is finite, take
$E=-S,F=S$ to obtain the bound $2(|S|+1)M$. If
$|a_i-b_i|\le D$, this is at most $(4D+4)M$.
Such a counterexample would therefore be a counterexample to the
diagonal Erdős--Turán conjecture. Conversely the diagonal case has
zero displacement. This is an equivalence of the restricted assertion
with that conjecture, not a proof of unboundedness. General sublinear
displacement need not take finitely many values.
