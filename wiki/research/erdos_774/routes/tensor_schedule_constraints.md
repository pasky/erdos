---
name: research/erdos_774/routes/tensor_schedule_constraints
title: Necessary growth of tensor side sizes
desc: A small-column entropy argument rules out uniform proportional dissociation when retained tensor sides satisfy p_i≤Ci for a fixed C; a lattice-volume bound explains the phase-lift cost.
tags: [E0774, proved, tensor, obstruction]
sources: []
created: 2026-09-18T00:24:00Z
updated: 2026-09-18T00:58:28Z
---


# Necessary growth of tensor side sizes

***

## A finite extraction upper bound — proved

For $E=\bigotimes_{i=1}^k S_{p_i}$, with $p_i\geq3$, write

$$
N=\prod_i p_i,\quad d=\prod_i(p_i-1),\quad r=d/N,
\qquad L=\sum_i\frac{\log(p_i-1)}{p_i}.
$$

Let $\eta(E)=\min_{\varnothing\ne F\subseteq E}r_{\rm diss}(F)/|F|$.
Then

$$
\eta(E)<4r\left(1+\frac{2L}{\log2}\right). \tag{1}
$$

Each simplex column has integer $\ell_1$-norm one except its last column,
which has norm $p_i-1$. The $\ell_1$-norm of a pure tensor is the
product of the factor norms. Therefore a uniformly chosen column $v$ has
$\mathbb E\log\|v\|_1=L$. At least $N/2$ columns belong to

$$
F=\{v\in E:\|v\|_1\leq e^{2L}\}.
$$

If $D\subseteq F$ is dissociated, its $2^{|D|}$ subset sums are
distinct integer vectors. The total of their coordinate-box widths is at
most $e^{2L}|D|$. Arithmetic–geometric mean gives

$$
2^{|D|}\leq(1+e^{2L}|D|/d)^d.
$$

For every real $M\geq1$, the inequality $2^t\leq1+Mt$ implies
$t<2\log_2(2M)$. One elementary check uses
$\log_2(2M)\leq2M-1$: at $t_0=2\log_2(2M)$,
$2^{t_0}=4M^2>1+Mt_0$, and
$\log_2(1+Mt)-t$ decreases for $t\geq2$.
Apply this with $M=e^{2L}$, and divide by $|F|\geq N/2$, to get (1).

## Linearly bounded side schedules cannot work

In particular, if $3\leq p_i\leq Ci$ for all $i$, where $C$
is fixed, then

$$
\eta(E_k)=O_C(k^{-1/C}(\log k)^2)\longrightarrow0. \tag{2}
$$

Indeed, put $A=\sum_{i\leq k}1/p_i$ and $a=H_k/C$. We have
$A\geq a$, $r\leq e^{-A}$, and $L\leq A\log(Ck)$.
For $a\geq1$, both $e^{-A}$ and $Ae^{-A}$ decrease as $A$
increases, so (1) is at most

$$
4e^{-a}\left(1+\frac{2a\log(Ck)}{\log2}\right).
$$

This proves (2). Thus choosing tensor side sizes proportional to the number of
successive chromatic stages cannot give the required uniform extraction
constant, regardless of improvements to the analytic proof. Inserting
arbitrarily large nonjump factors does not repair such a jump subsequence:
fixing those extra coordinates leaves a relation-isomorphic linearly bounded
tensor slice, and hereditary extraction restricts to that slice. The explicit
$1000i\log_2(i+1)$ schedule is not excluded by this bound.

## A lower bound on uniform phase-lift variance

There is also an intrinsic limitation on the lattice-rounding approach.
For the tensor zero-line-sum lattice
$\Lambda=\bigotimes_i A_{p_i-1}\subset W\subset\mathbb R^N$,

$$
\det(\Lambda)^{2/d}=
\prod_i p_i^{1/(p_i-1)}. \tag{3}
$$

This follows from $\det(A_{p-1})=\sqrt p$ and the Gram determinant
formula for tensor bases. Suppose **every** torus point in
$W/(2\pi\Lambda)$ has a random radian lift $X\in W$ with
$\mathbb E X_a^2\leq Q$ at every coordinate. Some lift then satisfies
$\|X\|_2^2\leq NQ$, so balls of radius $\sqrt{NQ}$ centered on
$2\pi\Lambda$ cover $W$. Their volume must be at least the
fundamental-domain volume. Writing $v_d$ for unit-ball volume gives

$$
Q\geq\frac{4\pi^2}{N}v_d^{-2/d}
             \prod_i p_i^{1/(p_i-1)}
\geq\frac{2\pi}{e}\frac dN
             \prod_i p_i^{1/(p_i-1)}. \tag{4}
$$

For the second inequality, Gaussian integration yields
$v_d\leq(2\pi e/d)^{d/2}$: on the unit ball,
$e^{-d\|x\|^2/2}\geq e^{-d/2}$.

The logarithm of the product on the right of (4), including $d/N$, is

$$
\sum_i\frac{\log p_i-1}{p_i}
       +O\!\left(\sum_i\frac{\log p_i}{p_i^2}\right).
$$

Thus replacing Gram–Schmidt rounding by a better target-uniform lift cannot
remove the leading $\sum(\log p_i)/p_i$ growth. This statement concerns
that particular uniform-lift method, not all possible analytic constructions.
