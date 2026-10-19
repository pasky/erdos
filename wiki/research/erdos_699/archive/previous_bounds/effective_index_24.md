---
name: research/erdos_699/archive/previous_bounds/effective_index_24
title: "Erdős 699: an effective cutoff at index 24"
desc: "Two certified applications of Bennett–Filaseta–Trifonov's Padé theorem yield an effective S-part exponent saving 1.3237, exceeding the 1.32 needed at i=24."
created: 2026-09-22T02:30:17Z
updated: 2026-10-14T00:26:52Z
---

# Erdős 699: an effective cutoff at index 24

***

This is a retained earlier research note. The [[research/erdos_699/_index|current reading guide]] gives the latest status and distinguishes completed proofs from remaining cases.

[[research/erdos_699/_index|P699 research]] ·
[[research/erdos_699/archive/previous_bounds/effectivity|The effectivity question]]

**Complete exclusion.** The
[completed interval proof](../../proofs/details/further_interval_certificates.md)
excludes every bad triple with $i=24$, as part of the cutoff $i\ge21$. The
effective estimate below was an intermediate step.

**Numerical follow-up.** Every bad triple with $i=24$ now satisfies
$n<10^{976}$. The [further effective bounds](further_effective_bounds.md)
combine explicit source thresholds with a weighted polynomial. They also
shrink the algebraic term for the original thresholds below from
$10^{10000}$ to $10^{228}$.

**There is an effectively computable last row for bad triples with
$i=24$.** The proof combines the published prime-pair estimates of
Bennett, Filaseta, and Trifonov (BFT) with two further applications of
their general Padé theorem. In this initial argument the last row is computable in principle;
the thresholds in that general theorem have not been numerically
evaluated here. This does not assert that the exceptional set is empty.

The source is the BFT paper, Theorem 2.2 and Corollary 2.3.

## Two further prime pairs

For every fixed positive integer $D$, the following implications hold
beyond effectively computable thresholds:

$$\begin{aligned}
|17^a u-19^b v|\le D
&\quad\Longrightarrow\quad
\max(u,v)>(17^a u)^{0.21},\\
|23^a u-11^b v|\le D
&\quad\Longrightarrow\quad
\max(u,v)>(23^a u)^{0.145}.
\end{aligned}\tag{1}$$

Here all exponents and cofactors are nonnegative integers, and the
quantity on the right must exceed the relevant threshold. These are
the same hypotheses as in BFT Theorem 2.2; no coprimality restriction
or requirement that the difference be nonzero is added.

The parameter choices in that theorem are

$$\begin{array}{c|c|c|c}
\{p,q\}&a_0p^{k_0}-b_0q^{\ell_0}=D_0&s&\epsilon\\\hline
\{17,19\}&5\cdot17^2-4\cdot19^2=1&19/10&1/1000\\
\{11,23\}&23-2\cdot11=1&5/3&1/1000.
\end{array}\tag{2}$$

The theorem defines $\Omega_1,\Omega_2$ and
$\lambda_1=\log\Omega_2/\log(\mathcal M_2^s\Omega_2)$.
The following outward-rounded intervals certify its hypotheses and
the claimed exponents:

$$\begin{array}{c|c|c|c}
\{p,q\}&\log\Omega_1&\log\Omega_2&\lambda_1\\\hline
\{17,19\}&(0.09575127,0.09575131)&(3.04802304,3.04802307)&(0.21409330,0.21409331)\\
\{11,23\}&(0.01975719,0.01975729)&(0.90676513,0.90676522)&(0.14786008,0.14786011).
\end{array}\tag{3}$$

In particular $\Omega_1,\Omega_2>1$, and $\lambda_1-\epsilon$
is greater than the exponent claimed in (1).

The [certificate](../../computations/erdos_699_bft_pair_extension.py)
uses directed interval arithmetic at 80 decimal digits. It bounds the
digamma differences in BFT's definition of $\log L(s)$ without treating
a floating-point digamma evaluation as evidence. For rational $f>g>0$,
put

$$
S_N(f,g)=\sum_{k=0}^{N-1}\frac{f-g}{(k+g)(k+f)}.
$$

The positive summand decreases with $k$, so the integral comparison gives

$$S_N(f,g)+\log\frac{N+f}{N+g}
\le\Psi(f)-\Psi(g)
\le S_N(f,g)+\log\frac{N-1+f}{N-1+g}.\tag{4}$$

The certificate uses $N=1000$ in each difference. All remaining
operations are rational arithmetic, logarithms, and square roots of
positive intervals. It checks two fixed analytic parameter choices;
it does not enumerate binomial rows.

## Combining the cofactor inequalities

For each prime $p<24$, choose $r_p\in\{0,\ldots,23\}$ maximizing
$a_p=v_p(n-r_p)$, and write

$$
n-r_p=p^{a_p}u_p.
$$

Take $n$ beyond all BFT thresholds for $D=23$. Set
$x_p=\log u_p/\log(n-23)$. The published Corollary 2.3 implies

$$
\max(x_p,x_q)\ge\lambda_2(p,q)\tag{5}
$$

for its fourteen prime pairs, while (1) supplies the same inequalities
with weights $0.21$ at $(17,19)$ and $0.145$ at $(11,23)$.

We claim that these inequalities force

$$
\sum_{p<24}x_p\ge1.3237.\tag{6}
$$

Here is a short verification using only the displayed numerical
weights, regarded as exact rationals. For a triangle with edge weights
$a\le b\le c$, its three vertex values have sum at least $a+c$:
one endpoint of the largest edge is at least $c$, and the edge joining
the other two vertices has weight at least $a$.

First, the published six-prime constraints give

$$
x_2+x_3+x_5+x_7+x_{11}+x_{13}\ge1.012.\tag{7}
$$

For completeness, if $x_{11}\ge0.3453$, the triangle $(3,5,13)$
contributes $0.4210$ and the edge $(2,7)$ contributes $0.2757$, giving
at least $1.0420$. Otherwise $x_3\ge0.3453$. If $x_{13}\ge0.1243$,
the triangle $(2,5,7)$ contributes $0.5424$, proving (7). In the
remaining case, $x_7\ge0.1243$ and $x_5\ge0.1838$.
If $x_2\ge0.2757$, the edge $(5,7)$ makes
$x_2+x_5+x_7\ge0.6667$. If $x_2<0.2757$, then
$x_7\ge0.2757$: when $x_5<0.2679$, the edge $(2,5)$ gives
$x_2+x_5+x_7\ge0.7274$; when $x_5\ge0.2679$, the triangle
$(2,11,13)$ gives $0.1496$ in addition to
$x_5+x_7\ge0.5436$. This proves (7) in every case.

Next,

$$
x_2+x_3+x_5+x_7+x_{11}+x_{13}+x_{23}\ge1.1137.\tag{8}
$$

If $x_{23}\ge0.145$, this follows from (7). Otherwise
$x_{11}\ge0.145$. If also $x_{11}\ge0.3453$, consider the five
vertices $2,3,5,7,13$. Their largest, second largest, third largest,
and fourth largest values are respectively at least
$0.2921,0.2667,0.2372,0.0505$. The first bound follows from the edge
$(2,3)$; the second from the triangle $(2,5,7)$; the third from that
triangle together with the disjoint edge $(3,13)$; the fourth from
the complete graph on those five vertices. Their sum is at least
$0.8465$, more than needed for (8).

If instead $x_{11}<0.3453$, then $x_3\ge0.3453$. The other four
vertices $2,5,7,13$ have sum at least $0.6234$. Indeed, when
$x_2\ge0.2757$, the triangle $(5,7,13)$ adds $0.3910$. Otherwise
$x_7\ge0.2757$; if $x_5\ge0.2679$, the edge $(2,13)$ adds
$0.0798$, and if $x_5<0.2679$, the edge $(2,5)$ forces
$x_2\ge0.2679$ while $(5,13)$ adds $0.1838$.
Thus the total in (8) is at least
$0.145+0.3453+0.6234=1.1137$.

Finally $x_{17}+x_{19}\ge0.21$ proves (6). Consequently

$$
\prod_{p<24}u_p\ge(n-23)^{1.3237}.\tag{9}
$$

## The effective last row

The selected-maxima bound from the effectivity note gives, for $i=24$,

$$U_{24}(n)\le\frac1{24}\prod_{p<24}p^{a_p}
\le\frac{n^9}{24(n-23)^{1.3237}}.$$

For $n\ge46$, this implies

$$
U_{24}(n)\le\frac{2^{1.3237}}{24}\,n^{7.6763}.\tag{10}
$$

The retained fat-point certificate has
$\rho_{24}=408/25$, so badness requires

$$U_{24}(n)>24^{-24}n^{24-408/25}
=24^{-24}n^{7.68}.\tag{11}$$

The exponent difference is $0.0037=37/10000>0$. Combining (10)
and (11) gives

$$
n^{37/10000}<24^{23}2^{1.3237}.\tag{12}
$$

Let $X$ be the maximum of the finitely many effective BFT thresholds
used above with $D=23$. For $n\ge X+23$, all the cofactor estimates
apply. Hence one effective exclusive cutoff is

$$
\boxed{n<\max\{X+23,10^{10000}\}.}\tag{13}
$$

The deliberately loose power of ten follows from
$24^{23}2^{1.3237}<10^{36}$ and $360000/37<10000$.
The number $X$ is effectively computable from the cited theorems;
no numerical value for it is claimed here.
