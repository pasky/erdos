---
name: polynomials/price_2026_perturbed_lobatto_nodes/theorem_1
title: "Theorem 1 (p. 1): M_n <= 2 - (1 + epsilon)/n for all large n, so min I is not 2 - (1 + o(1))/n"
desc: |
  Claimed in an unsigned write-up credited to GPT-5.5 Pro: for some
  epsilon > 0 and n_0, the least integral over [-1, 1] of the sum of the
  squared Lagrange cardinal polynomials of n nodes in [-1, 1] is at most
  2 - (1 + epsilon)/n for every n >= n_0, witnessed by the roots of the
  integral of P_{n-1} + a P_{n-3} for a fixed small a > 0.
created: 2026-10-14T22:51:14Z
updated: 2026-10-14T22:51:14Z
---

***

## Statement

For nodes $x_0,\dots,x_{n-1}\in[-1,1]$, distinct as the abstract says, $l_i$
is the Lagrange cardinal polynomial attached to $x_i$: the polynomial of
degree at most $n-1$ with $l_i(x_i)=1$ and $l_i(x_j)=0$ for $j\ne i$. Put

$$
M_n=\min_{x_0,\dots,x_{n-1}\in[-1,1]}\int_{-1}^1\sum_{i=0}^{n-1}l_i(x)^2\,dx .
$$

**Theorem 1** (p. 1). There are constants $\varepsilon>0$ and $n_0$ such that

$$
M_n\le2-\frac{1+\varepsilon}{n}\qquad\text{for every }n\ge n_0 .
$$

Consequently $M_n\ne2-(1+o(1))\frac1n$: the quantity $n(2-M_n)$, at least
$1+\varepsilon$ for every $n\ge n_0$, does not tend to $1$.

**Source.** *Perturbed Lobatto nodes*, preprint (2026), 11 pp., posted by
Liam Price; Theorem 1 on p. 1, the node family on pp. 1--2, (28) and (29) on
p. 6, (48)--(54) on p. 8, (55) on p. 9, (64)--(66) on p. 10 and the
completion on pp. 10--11. The edition read, the Overleaf compile of
2026-10-14, is identified on the
[[polynomials/price_2026_perturbed_lobatto_nodes/_index|source card]].

**Read depth.** Claims checked: Theorem 1 and the displays stated below were
read clause by clause on the page images. The proof was read for structure
only. Of it, only the arithmetic of (55), of (64) from (61) and (63), and of
(66) from (65) was redone by hand; the rank-three formula (17) and the
uniform bound (53), on which the theorem rests, were not checked. Nothing
here is independently reviewed.

## The node family and the uniform expansion

**The family** (Section 1, pp. 1--2). $P_m$ is the Legendre polynomial
normalized by $P_m(1)=1$. For $n\ge4$ put $N=n-1\ge3$ and, for real $a$,

$$
Q_{N,a}(x)=\int_{-1}^x\bigl(P_N(t)+aP_{N-2}(t)\bigr)\,dt
=\frac{P_{N+1}(x)-P_{N-1}(x)}{2N+1}+a\,\frac{P_{N-1}(x)-P_{N-3}(x)}{2N-3}
=(x^2-1)\Bigl[\frac{P_N'(x)}{N(N+1)}+a\,\frac{P_{N-2}'(x)}{(N-1)(N-2)}\Bigr].
$$

The nodes are the $N+1=n$ roots of $Q_{N,a}$. The paper shows, for every
$N\ge3$ and $|a|\le a_*=1/100$, that these roots are real and simple,

$$
-1=x_0(a)<x_1(a)<\dots<x_{N-1}(a)<x_N(a)=1,
$$

and real-analytic in $a$. At $a=0$, $Q_{N,0}(x)=(x^2-1)P_N'(x)/(N(N+1))$
and the nodes are the Legendre--Lobatto nodes $\xi_0=-1<\xi_1<\dots<\xi_N=1$,
the endpoints and the zeros of $P_N'$ (p. 7).

**The uniform bound** (Section 3, pp. 6--8). Write
$I_N(a)=\int_{-1}^1\sum_{i=0}^Nl_i(x)^2\,dx$ for the nodes $x_i(a)$ (p. 3).
The paper takes

$$
a_0=\min\Bigl\{\frac1{100},\ \frac1{4C_{\mathcal A}\sup_N\lvert\mathcal A(0)^{-1}\rvert}\Bigr\}
$$

((50), p. 8), where $\mathcal A(a)$ is the $3\times3$ matrix of the formula
$I_N(a)=2-\operatorname{tr}(\mathcal A(a)^{-1}C(a)B(a))$ ((28), p. 6),
$\mathcal A(0)^{-1}$ is bounded uniformly in $N$ ((48), p. 8), and
$C_{\mathcal A}$ is an absolute constant with
$|\mathcal A'(a)|+|\mathcal A''(a)|\le C_{\mathcal A}$ on $|a|\le a_*$ ((49),
p. 8). It proves

$$
\lvert I_N''(a)\rvert\le\frac CN\qquad\text{for }\lvert a\rvert\le a_0
$$

((29), p. 6, proved as (53), p. 8), with $C$ and $a_0>0$ absolute constants,
independent of $N$ and $a$. None of $C$, $C_{\mathcal A}$ and $a_0$ is
evaluated.

**The expansion** (Sections 4--5, pp. 8--10). Taylor's theorem with that
bound gives $I_N(a)=I_N(0)+aI_N'(0)+O(a^2/N)$ uniformly for $|a|\le a_0$
((54), p. 8). At the Lobatto nodes $I_N(0)=2-2/(2N+1)$ ((55), p. 9), and the
first variation is $I_N'(0)=-4(N+1)/(3(N-1)(2N+1))$ ((64), p. 10). Hence,
uniformly for $|a|\le a_0$, the paper's (65) (p. 10):

$$
I_N(a)=2-\frac2{2N+1}-a\,\frac{4(N+1)}{3(N-1)(2N+1)}+O\Bigl(\frac{a^2}N\Bigr).
$$

In terms of $n=N+1$, the display before (66) and (66) itself (p. 10) read

$$
n\bigl(2-I_N(a)\bigr)=\frac{2n}{2n-1}+a\,\frac{4n^2}{3(n-2)(2n-1)}+O(a^2)
=1+\frac{2a}3+O(a^2)+o(1),
$$

the $o(1)$ tending to $0$ as $n\to\infty$. With $C_1$ the implicit constant
of $O(a^2)$ in (66), the paper fixes $a\in(0,a_0)$ with $2a/3-C_1a^2>0$ and
concludes that $n(2-I_N(a))\ge1+\varepsilon$ for some $\varepsilon>0$ and all
large $n$ (pp. 10--11). The $n$ roots of $Q_{n-1,a}$ are admissible nodes, so
$M_n\le I_{n-1}(a)\le2-(1+\varepsilon)/n$.

Read off the printed constants, and not stated in the paper: the
$\varepsilon$ this argument yields is at most $2a/3$, hence less than $1/150$,
since $a<a_0\le1/100$.

## Proof pointer

Sections 1--5, pp. 1--11, in outline.

- Roots (pp. 1--2). The endpoints $\pm1$ are roots, with
  $Q_{N,a}'(\pm1)=(\pm1)^N(1+a)\ne0$. The interior roots are the zeros of
  $P_N'+\gamma_NaP_{N-2}'$, $\gamma_N=N(N+1)/((N-1)(N-2))$, a positive
  multiple of the characteristic polynomial of a Jacobi matrix with zero
  diagonal and positive off-diagonal entries built from the Gegenbauer
  recurrence ((2), p. 2), so they are real and simple; interlacing and the
  signs at $\pm1$ put them in $(-1,1)$.
- Kernel reduction (pp. 2--6). With $V_{im}=\phi_m(x_i)$ for the orthonormal
  Legendre polynomials $\phi_m$, the integral is
  $\operatorname{tr}((VV^T)^{-1})=\operatorname{tr}K(a)^{-1}$, where
  $K(a)_{ij}=K_N(x_i,x_j)$ is the Christoffel kernel at the nodes ((3)).
  Identities at the roots ((5)--(8)) and the Christoffel--Darboux formula
  give $K(a)=D(a)+U(a)C(a)U(a)^T$ with $D(a)$ positive diagonal, $U$ of size
  $(N+1)\times3$ and $C(a)$ of size $3\times3$ ((17)). The reciprocals of the
  diagonal entries are the interpolatory quadrature weights, which sum to $2$
  ((26)--(27)), and the Woodbury identity gives (28).
- Uniform bound (pp. 6--8). The node velocities satisfy
  $|x_i'|,|x_i''|\le C(1-x_i^2)/N$ ((9)--(10), p. 3). Bounds on the weights
  along the moving nodes ((30)--(40)) give $|M|+|M'|+|M''|\le C/N$ and
  $|B|+|B'|+|B''|\le C/N^2$ for $M=U^T\Lambda U$ and $B=U^T\Lambda^2U$
  ((44), (46)), with $|C|+|C'|+|C''|\le CN$ ((18)). A perturbation of the
  explicit $\mathcal A(0)=I_3+C(0)M(0)$ ((48)) bounds $\mathcal A(a)^{-1}$
  and its first two derivatives for $|a|\le a_0$ ((51)--(52)), which gives
  (53).
- Value and first variation at $a=0$ (pp. 8--10). There $K(0)$ is diagonal
  plus rank one, and the Sherman--Morrison formula gives (55).
  Differentiating $l_k(x_j)=\delta_{kj}$ along the motion of the nodes, with
  the node velocities (60) and the Lobatto identities $\sum_i\xi_i=0$ and
  $\sum_i\xi_i^2=N(N+1)/(2N-1)$ ((47)), gives (64).
- Conclusion (pp. 10--11). (54), (55) and (64) give (65) and (66), and a
  fixed small $a>0$ gives the theorem.

## Dependencies

The write-up labels no other result and has no bibliography. It uses without
proof the Legendre recurrence, differential equation and integration
identity, the Christoffel--Darboux formula, the Gegenbauer recurrence,
the reality, simplicity and interlacing of the zeros of Jacobi-matrix
characteristic polynomials, the Woodbury and Sherman--Morrison formulas, and
the exactness of the Lobatto quadrature for $1$ and $x^2$.

## Bears on

- [[../wiki/problems/polynomials/E1131/_index|Problem 1131]]: the theorem
  gives $n(2-\min I)\ge1+\varepsilon$ for every $n\ge n_0$, so the displayed
  asymptotic $\min I=2-(1+o(1))/n$ fails and the second question is answered
  no. It proves no lower bound for $\min I$, so the first question stays
  open. At $a=0$ the nodes are the roots of the integral of the Legendre
  polynomial $P_{n-1}$, and (55) is the value $2-2/(2n-1)$ that the problem
  page records as the upper bound of Erdős, Szabados, Varma and Vértesi. The
  theorem is the result behind the pending
  [[../wiki/problems/polynomials/E1131/claims/2026_04_26_price|claim of Price]].
