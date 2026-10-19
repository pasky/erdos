---
name: theory/additive_bases/L126_path_shell_resonance/_proof
title: Exact resonances between a path shell and many smaller shells
desc: |
  A lattice choice of the small index fixes the carry, and a prefix made
  from 12 and 112 realizes the required height. The resulting sums agree
  exactly while their small summands lie in disjoint scale intervals.
tags: []
sources:
- theory/additive_bases/L126_path_shell_resonance/_index
created: 2026-10-15T11:57:22Z
updated: 2026-10-15T11:57:22Z
---

***

This proves [[theory/additive_bases/L126_path_shell_resonance/_index|L126]].
Only the increment bounds $1\le\Delta h_Q\le2$ are needed of the large
path in the finite construction.

## One representation at each smaller dyadic scale

Put $Q=2^k$, $V=2Q$ and $n=Q^2+QV+h_Q(V)$. For a dyadic $q$ in the
stated range,

$$
16\sqrt Q\le q\le Q/256,\qquad m=Q/q\in\mathbb N.
$$

Choose an integer of the form $y=mt-q+1$ in the interval
$[7q/10,18q/25]$. This is possible because the interval has length $q/50$,
whereas the spacing $m=Q/q$ is at most $q/256$. This also defines an
integer $t$, and gives

$$
q^2+qy=Qt+q,\qquad
0<t\le\frac{43q^2}{25Q}\le\frac{43q}{6400}<\frac q{128}.
\tag{1}
$$

In particular $V-t$ is an integer in $[0,4Q]$. Write

$$
\Delta=h_Q(V)-h_Q(V-t),\qquad H=q-\Delta.
$$

The increment bounds give $t\le\Delta\le2t$, so
$H\le q$ and $H\ge(3157/3200)q$. Our choice of $y$ therefore ensures

$$
\frac43y\le\frac{24}{25}q<H\le q<\frac32y.
\tag{2}
$$

There is an admissible path with $h_q(y)=H$. To construct it, put
$b=H-y$ and $c=3y-2H$. Equation (2) implies $0\le c\le b$. Concatenate
$c$ copies of the word $112$ and $b-c$ copies of the word $12$, in any
order. The resulting word has length $3c+2(b-c)=y$ and sum
$4c+3(b-c)=H$. It contains neither $111$ nor $22$, including at the
concatenation boundaries. Extend it by repetitions of $12$ and truncate
at length $4q$. This defines the required admissible $h_q$.

Use the bare points, with cluster shifts both zero:

$$
a_q=Q^2+Q(V-t)+h_Q(V-t)\in A_Q,\qquad
b_q=q^2+qy-h_q(y)\in B_q.
$$

Equations (1) and $h_q(y)=q-\Delta$ give the exact integer equality

$$
a_q+b_q=Q^2+QV+h_Q(V-t)+\Delta=n.
\tag{3}
$$

Thus no discarded carry or approximate equality is involved.

## Distinct pairs and an infinite family

For these small summands,

$$
\frac{17}{10}q^2-q\le b_q\le\frac{43}{25}q^2.
$$

The intervals are disjoint at successive dyadic values of $q$: the next
lower endpoint is $(34/5)q^2-2q>(43/25)q^2$. Hence all $b_q$ are
distinct, so (3) gives distinct ordered pairs in the actual sets, even
after taking unions. The number of available dyadic scales is

$$
(k-8)-(\lceil k/2\rceil+4)+1=\lfloor k/2\rfloor-11.
$$

For the infinite assertion choose dyadic scales $Q_l\to\infty$ with
$16\sqrt{Q_{l+1}}>Q_l$. At step $l$, prescribe any admissible large path
at $Q_l$ and apply the finite construction. Every smaller scale used in
this step is larger than $Q_{l-1}$, so none of its paths has been assigned
earlier. After these assignments choose arbitrary admissible paths on
the unused scales, including all $3\cdot2^{j-1}$. No earlier path is
changed, and taking further unions preserves each displayed set of
distinct pairs.

For $Q_l=2^{k_l}$, the target satisfies
$3Q_l^2\le n_l\le3Q_l^2+4Q_l\le4Q_l^2$. Consequently

$$
r_{A,B}(n_l)\ge\lfloor k_l/2\rfloor-11
\ge\tfrac14\log_2 n_l-13.
$$

The $n_l$ tend to infinity, proving the claim. $\square$
