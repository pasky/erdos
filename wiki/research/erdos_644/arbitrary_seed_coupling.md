---
name: research/erdos_644/arbitrary_seed_coupling
desc: A conceptual separation proof establishes the Fano disjoint-triple coupling for every finite seed, settling the constant-composition inclusion.
tags: [proved, finite-coupling, restricted-upper-bounds]
sources: []
created: 2026-09-23T06:28:56Z
updated: 2026-09-24T22:12:53Z
---


# research/erdos_644/arbitrary_seed_coupling

***

This proves the arbitrary-seed polytope inclusion left open in
[Constant-composition families](constant_composition_families.md).
It gives the three-quarter upper coefficient for all fixed-seed
constant-composition constructions, not for arbitrary uniform families.

## The two polytopes

Let $V$ be a finite set of size $N\ge1$. For pairwise disjoint
$A,B,C\subseteq V$, allowing repeated empty sets, put

$$
\Gamma(A,B,C)=\frac{4\delta_A+2\delta_B+\delta_C}{7},
\qquad
K_N=\operatorname{conv}\{\Gamma(A,B,C)\}.
$$

Let $Q_N$ be the probability laws $\alpha$ on $2^V$ satisfying

$$
|D|\Pr_\alpha(I\cap D=\varnothing)
\ge\frac34\mathbb E_\alpha|I|
\qquad(\varnothing\ne D\subseteq V).
\tag{1}
$$


**Theorem.** For every finite $N$, $Q_N\subseteq K_N$.

## Reduction to nonnegative separating weights

Project $K_N$ onto its nonempty coordinates. This projected polytope
is coordinatewise downward closed. In a generating triple, replacing
one nonempty state by the empty set decreases only its coordinate;
convex mixing permits any smaller decrease. Repeating this operation
decreases any selected collection of nonempty coordinates.

Consequently a nonnegative point outside this polytope has a
nonnegative separating vector. For any separating vector $w$, replace
its negative coordinates by zero. The support function of a
downward-closed polytope is unchanged by this replacement, whereas
the value on a nonnegative point cannot decrease.

It suffices, therefore, to take $w_I\ge0$ for $I\ne\varnothing$,
put $w_\varnothing=0$, and prove the support-function inequality.
A nonzero such vector has positive support function on $K_N$, since
$\Gamma(I,\varnothing,\varnothing)\in K_N$ for every nonempty $I$.
Normalize so that

$$
4w_A+2w_B+w_C\le7
\quad\text{whenever }A,B,C\text{ are pairwise disjoint}.
\tag{2}
$$

We will prove $\mathbb E_\alpha w_I\le1$ for every $\alpha\in Q_N$.

## A single deletion set certifies the inequality

Put

$$
u=\max_{I\ne\varnothing}\frac{w_I-1}{|I|}.
$$

If $u\le0$, the claim is immediate. Suppose $u>0$. Choose a
maximizing state $A$ and put $x=u|A|=w_A-1$. Taking the other
two states empty in (2) gives $0<x\le3/4$.

We claim that some nonempty $D\subseteq V$ satisfies

$$
u|D|\le\frac34,
\qquad
w_I\le1-\frac43u|D|\,\mathbf1_{\{I\cap D=\varnothing\}}+u|I|
\quad(I\subseteq V).
\tag{3}
$$

If every state $B$ disjoint from $A$ satisfies

$$
w_B\le1-\frac43x+u|B|,
\tag{4}
$$

take $D=A$. For states meeting $D$, (3) follows from the definition
of $u$; for disjoint states it is (4).

Otherwise choose $B$ violating (4), and put $y=u|B|$.
It is nonempty, since $1-4x/3\ge0=w_\varnothing$.
Applying (2) to $A,B,\varnothing$ gives

$$
7\ge4w_A+2w_B>6+\frac43x+2y,
\qquad
u|A\cup B|=x+y<\frac12+\frac13x\le\frac34.
\tag{5}
$$

Take $D=A\cup B$. If a state $C$ disjoint from $D$ violated
(3), then

$$
\begin{aligned}
4w_A+2w_B+w_C
&>4(1+x)+2(1-4x/3+y)+1-4(x+y)/3+u|C|\\
&=7+\frac23y+u|C|>7,
\end{aligned}
$$

contradicting (2). States meeting $D$ satisfy (3) by the definition
of $u$. The empty state satisfies it by (5). This proves the claim.

Writing $a=\mathbb E_\alpha|I|$, average (3) and use (1):

$$
\mathbb E_\alpha w_I
\le1-\frac43u|D|\Pr_\alpha(I\cap D=\varnothing)+ua
\le1-\frac43u\frac34a+ua=1.
$$

Finite-dimensional separation proves the theorem. No computational
certificate is needed. $\square$

## Consequence and scope

The generators of $K_N$ have the Fano-cap realizations described in
[Constant-composition families](constant_composition_families.md#2-the-finite-fano-coupling-problem).
The integral rounding argument there now gives, for every $P_7$
constant-composition family with an $N$-point seed,

$$
\boxed{\tau\le\frac34 k+C_N,
\qquad C_N=N+49\cdot2^N\bigl(2N(N+1)+1\bigr).}
\tag{6}
$$

The asymptotic upper coefficient is therefore at most $3/4$ for
each fixed seed size, with arbitrarily varying compositions. The
same holds when $N^2 2^N=o(k)$.

An arbitrary uniform family is not a constant-composition family:
it need not contain all block permutations of a prescribed
multiset of local states. No operation imposing that closure has
been shown to preserve $P_7$ and the transversal ratio. Thus this
settles the coupling question, but not either unrestricted
assertion of Problem 644.
