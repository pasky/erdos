---
name: research/erdos_940/congruence_preserving_thinning
title: Sparse sequences with the same congruence and major-arc data
desc: Congruence-preserving sampling retains the cubic profinite limit and every established major-arc estimate while losing a logarithmic amount of microscopic entropy.
tags: []
sources: []
created: 2026-09-22T19:54:16Z
updated: 2026-09-22T19:54:16Z
---


# Sparse sequences with the same congruence and major-arc data

***

## Status and scope

The results below are proved. They concern **synthetic integer sequences**,
not representation functions of a diagonal form. In particular, they do
not prove either density conclusion for Erdős 940.

The construction preserves the exact cubic box congruence distribution
modulo a modulus exceeding the square of the root scale, all fixed
congruences, the joint profinite limit, and all the estimates in the
[major-arc note](cubic_major_arcs.md). Nevertheless its support has density
zero at the output scale and its logarithmic multiplicity diverges. Thus
the missing integer-fiber estimate cannot follow from these data alone.
The construction does not preserve the factorization into three cubic
Weyl sums; exploiting that factorization on the minor arcs remains possible.

## Congruence-preserving sampling

**Lemma.** Let $R$ be a nonnegative integer sequence supported in
$\{0,\ldots,B\}$, where $B\ge1$, and put $T=\sum_nR(n)>0$.
For arbitrary positive integers $D,K$, there is a nonnegative integer
sequence $\widetilde R$, supported inside $\operatorname{supp}R$, such that


$$
\sum_{n\equiv a\pmod D}\widetilde R(n)
=\sum_{n\equiv a\pmod D}R(n)\qquad(a\bmod D),                 \tag{1}
$$


$$
|\operatorname{supp}\widetilde R|\le T/K+D,
\qquad
\sum_{\widetilde R(n)\ge K}\widetilde R(n)\ge T-KD,            \tag{2}
$$

and, writing $e(t)=\exp(2\pi it)$,

$$
\sup_{\alpha\in\mathbb R/\mathbb Z}
\left|\sum_n(\widetilde R(n)-R(n))e(n\alpha)\right|
\ll\sqrt{KT\log(2BT)}.                                      \tag{3}
$$

Every such sequence also satisfies

$$
\frac1T\sum_n\widetilde R(n)\log\widetilde R(n)
\ge\log K-\log(1+KD/T),                                    \tag{4}
$$


$$
\sum_n\widetilde R(n)^2\ge\frac{KT}{1+KD/T}.                 \tag{5}
$$

As usual $0\log0=0$.

**Proof.** Write the mass of class $a$ as $M_a=m_aK+r_a$, with
$0\le r_a<K$. When $M_a>0$, sample independently $m_a$ outputs from
the conditional law $R(n)/M_a$ in that class, assigning weight $K$ to
each draw. If $r_a>0$, make one further independent draw with weight
$r_a$. Add weights when several draws choose the same output.

Each class has exactly its prescribed mass, and the number of draws is
at most $T/K+D$. The total weight of the remainder draws is less than
$KD$; every weight-$K$ draw contributes to a fiber of size at least $K$.
This proves (1) and (2) for every realization. Also
$\mathbb E\widetilde R(n)=R(n)$.

Let $Z(\alpha)$ denote the sum in (3). The independent draws have weights
$w_\ell\le K$, and $\sum_\ell w_\ell^2\le KT$. The elementary Hoeffding
bound for the real and imaginary parts gives

$$
\Pr(|Z(\alpha)|\ge u)\le4\exp(-u^2/(4KT)).                  \tag{6}
$$

For completeness, the real part contributed by a weight-$w$ draw lies
in an interval of length $2w$; applying the exponential-moment bound
for a centered variable in an interval, followed by Markov's inequality,
gives the real tail. Use threshold $u/\sqrt2$ for each part and a union
bound to obtain (6).

Deterministically $\|Z'\|_\infty\le4\pi BT$, since both sequences
have mass $T$ and support in $[0,B]$. On a uniform grid of
$L=\lceil8\pi BT\rceil$ frequencies, take
$u=2\sqrt{KT\log(8L)}$. Equation (6) and a union bound give probability
at most $1/2$ of a grid violation. The nearest grid point changes $Z$
by at most $1/4$. Some realization therefore satisfies (3).

Finally, the probability law $\nu(n)=\widetilde R(n)/T$ has entropy at
most $\log(T/K+D)$. The identity
$T^{-1}\sum\widetilde R\log\widetilde R=\log T-H(\nu)$ proves
(4), and Cauchy--Schwarz proves (5). $\square$

## Application to the cubic box distribution

Put $F=x^3+2y^3+4z^3$, take $N=2^k\to\infty$, and let $R_N$ count
representations with $1\le x,y,z\le N$. Thus $T=N^3$ and $B=7N^3$.
Choose integers $m_N\to\infty$ so slowly that

$$
L_N=\operatorname{lcm}(1,\ldots,m_N)\le\sqrt{\log(2N)}.
$$

For example, take the largest $m\le\lfloor\log N\rfloor$ satisfying
this inequality. Set

$$
D_N=N^2L_N,
\qquad K_N=\left\lfloor N/\log(2N)\right\rfloor.
$$

For sufficiently large $N$, $K_N\ge1$ and
$K_ND_N/N^3\le1/\sqrt{\log(2N)}\to0$.
The lemma gives

$$
|\operatorname{supp}\widetilde R_N|\ll N^2\log N=o(N^3),       \tag{7}
$$


$$
N^{-3}\sum_n\widetilde R_N(n)\log\widetilde R_N(n)
\ge\log N-\log\log N-O(1),                                 \tag{8}
$$


$$
\sum_n\widetilde R_N(n)^2\gg N^4/\log N.                    \tag{9}
$$

The congruence marginals agree exactly modulo $N^2$, and eventually
modulo $N^2q$ for every fixed $q$. In particular, every residue modulo
$N$ has mass exactly $N^2$, by the special cubic's dyadic uniformity.
**No uniformity or bounded second moment modulo $N^2$ is asserted.**

With $W_N=\sum_nR_N(n)e(n\alpha)$ and
$\widetilde W_N=\sum_n\widetilde R_N(n)e(n\alpha)$, (3) gives

$$
\|\widetilde W_N-W_N\|_\infty\ll N^2.                      \tag{10}
$$

Thus the normalized Fourier transforms differ by only $O(N^{-1})$
uniformly, and agree exactly at every rational frequency whose denominator
divides $D_N$.

### The joint profinite limit also agrees

Let

$$
\rho_{N;q}(a)=\frac q{N^3}\sum_{n\equiv a\pmod q}R_N(n).
$$

If $q\le N/2$, each root residue occurs between $N/q-1$ and $N/q+1$
times. Comparing each residue triple with the complete residue box gives

$$
(1-q/N)^3\rho_q(a)\le\rho_{N;q}(a)
\le(1+q/N)^3\rho_q(a),                                    \tag{11}
$$

where $\rho_q$ is the complete density from the
[profinite note](profinite_cubic_density.md). Hence

$$
\|\rho_{N;q}-\rho_q\|_2\le5(q/N)\|\rho_q\|_2
\le5\sqrt{\mathfrak S}\,q/N.                              \tag{12}
$$

The norm here uses normalized counting measure modulo $q$.

Exact marginal preservation at $q=L_N$ and the proved profinite
convergence show

$$
\|\widetilde\rho_{N;L_N}-\rho\|_{L^2(\widehat{\mathbb Z})}
\ll L_N/N+m_N^{-1/3}\longrightarrow0.                     \tag{13}
$$

In particular, the joint congruence second moments tend to
$\mathfrak S$, and their entropy deficits are at most
$\log\mathfrak S+o(1)$. This bounded coarse entropy coexists with (8).

## Every established major-arc estimate survives

For the arcs $\mathfrak M(N,Q)$ in the
[major-arc theorem](cubic_major_arcs.md), $1\le Q\le N^{1/2}$,

$$
|\mathfrak M(N,Q)|\le2Q^2/N^3,
\qquad \int_{\mathfrak M}|W_N|^2\ll N^3.
$$

Equation (10) implies
$\int_{\mathfrak M}|\widetilde W_N-W_N|^2\ll NQ^2$.
Cauchy--Schwarz therefore gives

$$
\left|\int_{\mathfrak M}|\widetilde W_N|^2
      -\int_{\mathfrak M}|W_N|^2\right|
\ll N^2Q+NQ^2\ll N^2Q^2.                                \tag{14}
$$

Consequently exactly the same asymptotic holds:

$$
\int_{\mathfrak M(N,Q)}|\widetilde W_N|^2
=N^3\mathfrak J\mathfrak S+
O(N^3Q^{-2/3}+N^2Q^2).                                   \tag{15}
$$

The pointwise approximation survives too: (10) and
$W_N=M_N+O(QN^2)$ imply
$\widetilde W_N=M_N+O(QN^2)$, with the same main function $M_N$.
Thus its integrated squared approximation error remains $O(NQ^4)$.

In contrast, put $E_N=\{n:\widetilde R_N(n)\ge K_N\}$ and
$P_{E_N}(\alpha)=\sum_{n\in E_N}e(-n\alpha)$. Then

$$
|E_N|\ll N^2\log N,
\qquad \sum_{n\in E_N}\widetilde R_N(n)=N^3+O(K_ND_N).
$$

The major-arc correlation is $O(N^{5/2}\sqrt{\log N})$ by
Cauchy--Schwarz and (15). Subtracting it from the full Fourier integral
gives

$$
\int_{\mathfrak M(N,Q)^c}\widetilde W_N P_{E_N}
=N^3+O(K_ND_N+N^{5/2}\sqrt{\log N})=(1+o(1))N^3.          \tag{16}
$$

So essentially all the mass of the heavy fibers can lie in the missing
minor-arc correlation, while the preceding congruence and major-arc
estimates remain valid. An argument for the actual polynomial must use
additional information that excludes this construction; none is supplied
by this lemma.
