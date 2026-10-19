---
name: theory/number_theory/L53_divisor_product_collision_criterion/_proof
title: Proof of the product collision criterion
desc: |
  The bilinear bound for products modulo powers of two, its composition into
  L63's representatives, a character form of the hypothesis, and the
  geometric-progression example.
created: 2026-10-14T10:22:48Z
updated: 2026-10-14T10:22:48Z
---

***

We prove [[theory/number_theory/L53_divisor_product_collision_criterion/_index|L53]].
Write $e(x)=e^{2\pi ix}$ and $L(t)=1+\log_2(t+1)$. For a probability law
$\beta$ on $\mathbb Z/2^j\mathbb Z$ put $\|\beta\|_2^2=\sum_x\beta(x)^2$,
its collision probability, and
$\widehat\beta(t)=\sum_y\beta(y)e(ty/2^j)$. Let $N_K$ be the odd part of
$K!$, $e_p=v_p(K!)$, and $\alpha(K,s,j)$, $\mathrm{Coll}(K,s,j)$ as in the
statement.

## The bilinear bound

Let $j\ge1$, let $a$ be odd, and let $\alpha,\beta$ be probability laws on
$\mathbb Z/2^j\mathbb Z$. Then

$$
\Bigl|\sum_{x,y}\alpha(x)\beta(y)\,e\Bigl(\frac{axy}{2^j}\Bigr)\Bigr|
\le2^{j/2}\|\alpha\|_2\|\beta\|_2.                                  \tag{1}
$$

The left side is $|\sum_x\alpha(x)\widehat\beta(ax)|$. By Cauchy–Schwarz
its square is at most $\|\alpha\|_2^2\sum_x|\widehat\beta(ax)|^2$, the sum
running over all residues. Since $a$ is a unit, $x\mapsto ax$ permutes the
residues, and Parseval's identity gives
$\sum_t|\widehat\beta(t)|^2=2^j\|\beta\|_2^2$.

The [held source for part (b)](../../../../library/number_theory/conjectures_io_2026_lean_solutions_erdos_problems/evidence/assets/solution_e93a2766/Main.lean)
uses this bound in its last step (`norm_dft_unit_mixture_sq_le`), for a
unit law against the law produced by its sum-product averaging. Its loss
comes from the earlier comparison `norm_dft_unit_product_final_power_le`,
which bounds the product law's coefficient raised to the power $2^{R+1}$
by the coefficient of a unit mixture of that averaged law. The proof below
applies (1) to two halves of the product law itself.

## Proof of (i)

Take $k$ large and $K,s,J_0,\eta$ as in the hypothesis. Let $\sigma$ be
the law modulo $2^k$ of $z=d_1\cdots d_{2s}$, where $d_1,\ldots,d_{2s}$
are independent uniform divisors of $N_K$. Fix $1\le j\le k$ and an odd
$a$. The value $e(az/2^j)$ depends only on $z$ modulo $2^j$. The halves
$x=d_1\cdots d_s$ and $y=d_{s+1}\cdots d_{2s}$ are independent, and each
has law $\alpha(K,s,j)$ modulo $2^j$. By (1), for $J_0\le j\le k$,

$$
\Bigl|\mathbb E\,e\Bigl(\frac{az}{2^j}\Bigr)\Bigr|
\le2^{j/2}\,\mathrm{Coll}(K,s,j)\le2^{-\eta j}.                      \tag{2}
$$

Put $b=J_0$ and $q=\lceil2/\eta\rceil$; for large $k$, $b<k$. Let
$\nu_b$ be the uniform law on $\{0,1,\ldots,2^b-1\}$, viewed modulo
$2^k$. For $1\le j\le b$ this set is a union of complete residue systems
modulo $2^j$, so $\nu_b$ has Fourier coefficient zero at every character
$x\mapsto e(ax/2^j)$ with $a$ odd. Every nontrivial additive character of
$\mathbb Z/2^k\mathbb Z$ has this form for exactly one $1\le j\le k$, and
$2^{j-1}$ of them have conductor $2^j$. Let $\lambda$ be the additive
convolution of $q$ copies of $\sigma$ and one copy of $\nu_b$. Since
$\eta q\ge2$, (2) bounds the total modulus of its nontrivial Fourier
coefficients by

$$
\sum_{j=b+1}^{k}2^{j-1}2^{-2j}<\frac12.
$$

Fourier inversion makes $\lambda$ positive at every residue modulo $2^k$.
So every residue has a representative

$$
S=z_1+\cdots+z_q+B,\qquad 0\le B<2^b,
$$

where each $z_i$ is a product of $2s$ divisors of $N_K$. Such a product
divides $(K!)^{2s}$ and hence $(2sK)!$. Writing $B$ in binary uses at most
$b$ of the powers $1,2,4,\ldots,2^{b-1}$, each a divisor of $(2b)!$. Thus
$S$ is a sum of at most $q+b$ positive divisors of $F!$, repetitions
allowed, where $F=2sK+2b$, and

$$
0\le S\le q(K!)^{2s}+2^b.
$$

The hypothesis bounds give $F=O(kL(k)^{2A})$ and $q+b=O(L(k)^A)$. Since
$K!\le K^K$ and $\log_2K=O(L(k))$,

$$
\log_2\bigl(q(K!)^{2s}+2^b\bigr)\le1+\log_2q+2sK\log_2K+b
=O\bigl(kL(k)^{2A+1}\bigr).
$$

Hence $S\le2^{kD}$ for an integer $D=O(L(k)^{2A+1})$. These are the
hypotheses of
[[theory/number_theory/L63_polylogarithmic_dyadic_representatives/_index|L63]]
with exponents $a=2A$, $b=A$ and $d=2A+1$, after enlarging its constant;
L63's exponent $b$ is unrelated to the binary cutoff $b$ above. L63 gives
$h(n!)=O((\log n)^{5A+4})$.

## A character form of the hypothesis

Every divisor of $N_K$ is odd, so $\alpha(K,s,j)$ lives on the group
$(\mathbb Z/2^j\mathbb Z)^\times$ of order $2^{j-1}$, for $j\ge2$. The
exponents $v_p(d)$ of a uniform divisor $d$ of $N_K$ are independent and
uniform on $\{0,\ldots,e_p\}$. For a Dirichlet character $\chi$ modulo
$2^j$ this gives
$\mathbb E\chi(d)=\prod_{3\le p\le K}\phi_{e_p}(\chi(p))$, where
$\phi_e(\omega)=(e+1)^{-1}\sum_{i=0}^{e}\omega^i$. Parseval's identity on
that group therefore gives

$$
\mathrm{Coll}(K,s,j)=\frac1{2^{j-1}}\sum_{\chi\bmod2^j}\,
\prod_{3\le p\le K}\bigl|\phi_{e_p}(\chi(p))\bigr|^{2s}.             \tag{3}
$$

The principal character contributes $1$. A factor
$|\phi_{e_p}(\chi(p))|$ is close to $1$ only when the powers
$\chi(p)^i$, $0\le i\le e_p$, cluster near one point of the circle, and in
particular only when $\chi(p)$ is close to $1$. Thus the hypothesis of (i)
at level $j$ says exactly that

$$
\sum_{\chi\bmod2^j}\ \prod_{3\le p\le K}
\bigl|\phi_{e_p}(\chi(p))\bigr|^{2s}\le2^{(1/2-\eta)j-1},
$$

a bound on how many characters can stay close to $1$ on most odd primes
up to $K$, weighted by how close they stay.

A stronger sufficient hypothesis has a simple conductor count. Write
$M_K(\chi)=\prod_{3\le p\le K}|\phi_{e_p}(\chi(p))|$. If

$$
M_K(\chi)\le2^{-l/(2s)}
\quad\text{for every nonprincipal character of conductor }2^l,
\quad 2\le l\le k,                                           \tag{4}
$$

then the sum in (3) is at most $(j+3)/4$. Indeed the principal character
contributes $1$, there is one character of conductor $4$, and there are
$2^{l-2}$ characters of conductor $2^l$ for $l\ge3$. After the power
$2s$, each nonprincipal conductor contributes at most $1/4$ in total.
Thus

$$
\mathrm{Coll}(K,s,j)\le\frac{j+3}{2^{j+1}}\le2^{-3j/4}
\qquad(j\ge12).
$$

For the last inequality, $(j+3)/2\le2^{j/4}$ holds at $j=12$ and persists
because $(j+4)/(j+3)\le16/15<2^{1/4}$ for $j\ge12$. This would give
$\eta=1/4$ and $J_0=12$ in (i), with the required bounds on $K$ and $s$.
Condition (4) is unproved and stronger than the needed moment bound (3);
it is not an equivalent reformulation of it.

Counting supports gives a lower bound on the index. A law on at most $M$
residues has collision probability at least $1/M$, and the product of $s$
divisors of $N_K$ is a divisor of $N_K^s$. So
$\mathrm{Coll}(K,s,k)\ge1/\tau(N_K^s)$, and

$$
\log\tau(N_K^s)=\sum_{3\le p\le K}\log(se_p+1)
\le\pi(K)\log s+\sum_{p\le K}\log\frac{4K}p,
$$

since $e_p+1\le2K/(p-1)\le4K/p$ for $p\ge3$. Partial summation gives
$\pi(K)\log K-\theta(K)=\int_2^K\pi(t)\,dt/t=O(K/\log K)$, so the last
sum is $O(K/\log K)$ by Chebyshev's bounds, and
$\log\tau(N_K^s)=O(K(1+\log s)/\log K)$. If the hypothesis holds at
$j=k$, then $\log_2\tau(N_K^s)\ge k/2$. Since $s\le CL(k)^A$, this first
gives $K\ge\sqrt k$ for large $k$, and then
$K\ge c\,k\log k/(1+\log s)$ for an absolute $c>0$.
With $s$ polylogarithmic, the index must exceed $k$ by a factor of order
at least $\log k/\log\log k$. L63 permits this.

## Proof of (ii)

Put $m=\lceil gJ\rceil\ge1$ and $N=2^m$, so $X=\{3^i:0\le i<N\}$ consists
of $N$ distinct odd integers. Modulo $4$, the powers $3^i$ alternate
between $1$ and $3$; since $N$ is even, each class holds a fraction $1/2$,
and $1/2\le2^{-2g}$ because $g\le1/2$. For $l\ge3$ the order of $3$ modulo
$2^l$ is $2^{l-2}$, so $i\mapsto3^i$ is periodic modulo $2^l$ with period
$2^{l-2}$ and injective on each period. If $2^{l-2}\le N$, then
$2^{l-2}\mid N$ and each class meets $X$ in $0$ or $N/2^{l-2}$ members, a
fraction at most $2^{2-l}$. This is at most $2^{-gl}$ because
$(1-g)l\ge\tfrac23l\ge2$. If $2^{l-2}>N$, each class meets $X$ at most
once, a fraction $2^{-m}\le2^{-gJ}\le2^{-gl}$ for $l\le J$.

A product of $s$ members of $X$ is $3^I$ with $0\le I\le s(N-1)$. Its law
modulo $2^J$ is therefore supported on at most $s(N-1)+1\le sN$ residues,
and by Cauchy–Schwarz its collision probability is at least
$1/(sN)\ge2^{-gJ-1}/s$, since $N\le2^{gJ+1}$.

For this $X$, (1) applied to two product halves gives a nontrivial bound
only if $s>2^{(1/2-g)J-1}$, which is exponential in $J$. The weighted
mixing theorem of the held source still gives Fourier decay after a
sufficiently large number of factors depending only on $g$; its proof
reaches it through additive convolution. A proof of the hypothesis of (i)
therefore needs information about the factorial-divisor law beyond this
nonconcentration.
