---
name: research/erdos_25/quasipolynomial_equidistribution
desc: Uniform interval equidistribution for arbitrary finite congruence unions at length exp(C log-cubed Q), and natural density under a correspondingly stronger activation rule.
tags: [density, boolean-functions, strong-activation, partial-results]
sources: []
created: 2026-09-22T12:32:00Z
updated: 2026-09-24T22:13:01Z
---


# research/erdos_25/quasipolynomial_equidistribution

***

This is a proved result for **much longer intervals than the largest
modulus**, not a solution with activation at the modulus. It permits any
number of distinct forbidden residues at a given modulus.

## Finite theorem

There are absolute constants $A,C>0$ such that the following holds.
Let $Q\ge3$, and let $U$ be any union of residue classes with moduli
at most $Q$. If $I$ is an interval of $H$ consecutive integers and
$$
 H\ge \exp\{A(\log Q)^3\},
$$
then
$$
 \left|\frac{|U\cap I|}{H}-\mu(U)\right|\le C Q^{-2}.
 \tag{1}
$$
Here $\mu(U)$ is its full periodic density. The bound is independent
of the location of $I$, the common period, and all residue choices.

The external input is the bounded-independence theorem for disjunctive
normal form (DNF) Boolean formulas: for absolute $B,c,C_0>0$, an
$m$-term DNF has expectation error at most
$$
 C_0m^B e^{-c\sqrt{k}}
 \tag{2}
$$
under any $k$-wise independent unbiased bit distribution, relative
to independent unbiased bits. This is Theorem 1, page 2, of
[Razborov, *A simple proof of Bazzi's theorem*](https://homepage.mi-ras.ru/~razborov/bazzi.pdf),
September 10, 2008. The theorem and its definition of $k$-independence
were checked in the author-hosted full paper. No independence of the
arithmetic bits is assumed below: a quantitative correction supplies it.

## Encoding one prime by one real coordinate

Put $E_p=\lfloor\log_p Q\rfloor$ for each prime $p\le Q$. For
$$
 r=\sum_{j=0}^{E_p-1}d_jp^j,
 \qquad
 \operatorname{rev}_{E_p}(r)=\sum_{j=0}^{E_p-1}d_jp^{E_p-1-j},
$$
define
$$
 u_p(n)=\frac{\operatorname{rev}_{E_p}(n\bmod p^{E_p})+V_p}{p^{E_p}},
 \tag{3}
$$
where the $V_p$ are independent uniform random variables on $[0,1)$.
Under Haar sampling of $n$, the $u_p$ are independent and uniform
on $[0,1)$. For $e\le E_p$, the condition $n\equiv a\pmod{p^e}$
is exactly the condition
$$
 u_p(n)\in
 \left[\frac{\operatorname{rev}_{e}(a\bmod p^e)}{p^e},
       \frac{\operatorname{rev}_{e}(a\bmod p^e)+1}{p^e}\right).
 \tag{4}
$$
Indeed fixing the first $e$ base-$p$ digits of $n$, starting
with the least significant digit, fixes the first $e$ digits after
the radix point in (3). Endpoint ambiguities have probability zero.

Take $b=\lceil6\log_2(Q+1)\rceil$ binary digits of each $u_p$.
Every interval in (4) has inner and outer approximations by the
grid of mesh $2^{-b}$, each a union of at most $2b+2$ binary-prefix
cylinders, with total outer-minus-inner length at most $2^{1-b}$.
The prefix decomposition follows by taking the maximal dyadic
subintervals of a grid interval; there are at most two of each length.

A class modulo $q$ is a conjunction of $\omega(q)$ conditions
(4). Distributing the unions gives an inner and outer DNF, each
with at most $(2b+2)^{\omega(q)}$ terms. There are fewer than
$(Q+1)^2$ possible classes with moduli at most $Q$, so the entire
union has DNF bounds $f_-\le\mathbf1_U\le f_+$ with
$$
 m\le (Q+1)^2(2b+2)^{w_Q},
 \qquad w_Q=\max_{q\le Q}\omega(q),
 \qquad N=b\pi(Q)
 \tag{5}
$$
terms and bits, respectively. Under the independent uniform-bit law,
$$
 \mathbb E(f_+-f_-)
 \le 2(Q+1)^2w_Q2^{-b}=O(Q^{-3}).
 \tag{6}
$$
Using $q\ge\omega(q)!$ gives
$w_Q=O(\log Q/\log\log Q)$. Consequently
$$
 \log(m+1)=O(\log Q),\qquad N\le Qb.
 \tag{7}
$$
Using one coordinate per prime, rather than per prime-adic digit,
is essential to this polynomial bound on $m$.

## Correcting almost independent bits

Now sample $n$ uniformly from $I$, still using independent jitters
$V_p$, and let $\rho$ be the resulting bit probability density
relative to the uniform law on $\{0,1\}^N$. For a nonempty set
$T$ of at most $k$ bit positions, write
$$
 a_T=\mathbb E_\rho\chi_T,
 \qquad \chi_T(x)=(-1)^{\sum_{j\in T}x_j}.
$$
After averaging the jitters, this parity is a bounded function of
$n$ with period dividing
$$
 D_T=\prod_{\substack{p:\text{some bit at }p\text{ belongs to }T}}
                p^{E_p}\le Q^{|T|}.
$$
Its average over one period is zero: CRT and the jitters make those
prime coordinates independent uniform real variables. Splitting $I$
into complete periods and a remainder therefore gives
$$
 |a_T|\le Q^k/H.
$$
Let
$$
 s=\sum_{1\le|T|\le k}|a_T|
 \le (N+1)^k Q^k/H.
 \tag{8}
$$
If $k>N$, the sums simply include all nonempty subsets. Define
$$
 \rho'=
 \frac{\rho+s-\sum_{1\le|T|\le k}a_T\chi_T}{1+s}.
 \tag{9}
$$
This is nonnegative because the absolute value of the character sum
is at most $s$. It has mean one, and all nonconstant Fourier
coefficients of degree at most $k$ vanish. Thus its bits are exactly
$k$-wise independent (fully independent if $k>N$). Moreover,
$$
 \|\rho'-\rho\|_{\mathrm{TV}}\le \frac{3s}{2(1+s)}\le\tfrac32s.
 \tag{10}
$$
For (10), subtract the densities in (9), use
$\mathbb E|1-\rho|\le2$, and bound the character sum in $L^1$
by $s$.

Choose $k=\lceil K(\log Q)^2\rceil$, with $K$ an adequately
large absolute constant. By (2) and (7), the error for each of
$f_-,f_+$ under $\rho'$ is $O(Q^{-3})$. By (7)--(8), choosing
$A$ sufficiently large makes $s=O(Q^{-3})$ for every interval
length in (1). Equations (6), (10), and the pointwise sandwich now
prove (1), in fact with the stronger $O(Q^{-3})$ error after adjusting
constants. We retain the less restrictive displayed $O(Q^{-2})$.

## A natural-density theorem for stronger activation

For each modulus $q$, allow an arbitrary forbidden residue set $R_q$,
including the empty set. Let $F(q)$ be increasing, tending to infinity,
and suppose, eventually,
$$
 F(q)\ge\exp\{A(\log q)^3\},
 \tag{11}
$$
with $A$ as in (1). Activate those congruences only when $n\ge F(q)$.
Then the resulting survivor set has **natural density** equal to
$$
 \delta=\lim_{Q\to\infty}
   \mu\{x:x\bmod q\notin R_q\text{ for every }q\le Q\}.
 \tag{12}
$$
It consequently also has logarithmic density $\delta$.

Take $X$ to be an integer. To prove the lower bound, let
$Q(X)=\max\{q:F(q)\le X\}$, rounded
to an integer. The full finite survivor set using all moduli at most
$Q(X)$ is contained in the delayed survivor set on $[1,X]$.
By (1), its proportion there is its Haar measure plus $o(1)$, hence
at least $\delta-o(1)$. The finitely many exceptions in (11) can
be included once $X$ is large. For the upper bound, every fixed
finite collection of congruences is active beyond a fixed integer;
its periodic survivor density bounds the upper natural density.
Let the finite collection increase to obtain $\overline d\le\delta$.

For example, (11) holds for
$F(q)=\lceil\exp((\log(q+2))^{3+\epsilon})\rceil$, any fixed
$\epsilon>0$. This does **not** treat $F(q)=q^C$, much less the
original $F(q)=q$. Applying (1) with $Q=X$ would violate its
interval-length hypothesis. No original-activation tail estimate
follows from this theorem.
