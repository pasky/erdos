---
name: research/erdos_25/protected_set_distortion
desc: A uniform polynomial lower bound for finite survivor measure when a positive fraction of an interval as long as the largest modulus survives.
tags: [finite-sieves, distortion, partial-results]
sources: [balister_2018_erdos_covering_problem_density_uncovered_set]
created: 2026-09-22T12:32:00Z
updated: 2026-09-24T22:13:01Z
---


# research/erdos_25/protected_set_distortion

***

## A finite trace-to-measure inequality

There are absolute constants $C,Q_0>0$ with the following property.
Let $Q\ge Q_0$ be an integer, and install one forbidden residue at
each modulus in an arbitrary set $D\subseteq[1,Q]$ of **distinct**
moduli. Let $S$ be the full periodic survivor set and
$$
 \delta=\mu(S),\qquad \alpha=|S\cap I|/Q,
$$
where $I$ is any interval of $Q$ consecutive integers. Set
$$
 \varepsilon(Q)=C\frac{(\log\log Q)^3}{\log Q}.
$$
If $\alpha>\varepsilon(Q)$, then
$$
 \delta\ge(\alpha-\varepsilon(Q))
       \exp\!\left\{-\frac{C\log Q}{\alpha-\varepsilon(Q)}\right\}.
 \tag{1}
$$
In particular, if $\alpha\ge2\varepsilon(Q)$, then
$$
 \delta\ge\exp(-C'\log Q/\alpha).
 \tag{2}
$$
These are finite density bounds, not logarithmic-density existence
theorems. On $I=[Q,2Q)$, all installed congruences are active under
the original rule, so no activation discrepancy is hidden in (1).
If modulus 1 is installed, then $S$ is empty and the hypotheses
requiring positive $\alpha$ are false; hence it may be omitted below.

## Checked distortion inputs

The [BBMST digest](../../../library/covering_systems/balister_2018_erdos_covering_problem_density_uncovered_set/_index.md)
was read first. The following statements and their proofs were checked
in the [full source](../../../library/covering_systems/balister_2018_erdos_covering_problem_density_uncovered_set/_index.md):
Section 2.2, Lemmas 2.1, 3.3, 3.5, Theorem 3.2, and the Jensen step in
the proof of Theorem 3.1. We use their prime-stage distorted measures
with parameters $d_p\in[0,1/2]$, denoting the final measure by
$\mathbb P$. Define
$$
 \nu(m)=\prod_{p\mid m}(1-d_p)^{-1},\qquad
 \Delta=\log_+(d\mathbb P/d\mu).
$$
The needed conclusions are:

* Later prime stages preserve all previously exposed coordinate
  marginals. Setting a stage parameter to zero leaves its measure
  unchanged.
* The final probability of the forbidden set introduced at prime
  $p$ is at most $M_p^{(2)}/(4d_p(1-d_p))$, where
  $$
  M_p^{(2)}\le\frac1{(p-1)^2}
   \prod_{\ell<p}\left(1+
       \frac{3\ell-1}{(1-d_\ell)(\ell-1)^2}\right).
  \tag{3}
  $$
  Distinctness of the original moduli is used in this estimate.
* The mean positive log distortion satisfies
  $$
  \mathbb E_{\mathbb P}\Delta
     \le2\sum_{q\in D}\frac{\nu(q)}q.
  \tag{4}
  $$
  If an event $R$ has final probability $b>0$, Jensen's inequality
  gives
  $$
  \mu(R)\ge b\exp\{-\mathbb E_{\mathbb P}\Delta/b\}.
  \tag{5}
  $$

We will preserve the *actual union* of the small-prime forbidden sets,
rather than bound it by their reciprocal sum.

## An adjustable prime cutoff

Fix a sufficiently large $y$, and choose
$$
 d_p=0\quad(p\le y),\qquad
 d_p=\frac{\log y}{2\log p}\quad(p>y).
 \tag{6}
$$
These are allowed parameters. Elementary prime counting and partial
summation show, uniformly in $y$,
$$
 \sum_{p>y}\frac{d_p}{p}
 =\frac{\log y}{2}\sum_{p>y}\frac1{p\log p}=O(1).
 \tag{7}
$$
Thus $\nu(p)-1\le2d_p$ and
$\prod_p(1+(\nu(p)-1)/p)=O(1)$, uniformly in $y$.
If $g$ is the nonnegative squarefree-supported multiplicative
function with $g(p)=\nu(p)-1$, then $\nu=1*g$. It follows that
$$
 \sum_{q\le Q}\frac{\nu(q)}q
 =\sum_{m\le Q}\frac{g(m)}mH_{\lfloor Q/m\rfloor}
 \ll H_Q.
 \tag{8}
$$

The logarithm of the product in (3) is at most
$$
 3\sum_{\ell<p}\frac1\ell+
 O\!\left(\sum_\ell\ell^{-2}+\sum_{\ell<p}\frac{d_\ell}{\ell}\right)
 \le3\log\log p+O(1).
$$
Here we used the elementary Euler-product estimates already recorded
in [coprime entropy](coprime_entropy.md). Consequently
$M_p^{(2)}\ll(\log p)^3/p^2$. The total final forbidden probability
at primes greater than $y$ is therefore at most
$$
 \eta_y\ll\frac1{\log y}
      \sum_{p>y}\frac{(\log p)^4}{p^2}
 \ll\frac{(\log y)^2}{y}.
 \tag{9}
$$
The last step is partial summation with $\pi(t)\ll t/\log t$.

Let $S_y$ be the survivor set using the installed moduli all of
whose prime factors are at most $y$, and put
$\sigma_y=\mu(S_y)$. Equations (6) and marginal preservation give
$$
 \mathbb P(S_y)=\sigma_y,\qquad
 \mathbb P(S)\ge\sigma_y-\eta_y.
$$
Combining (4), (5), and (8), for
$t=\sigma_y-C_1(\log y)^2/y>0$, yields
$$
 \delta\ge t\exp(-C_2\log Q/t).
 \tag{10}
$$
The function $t\mapsto te^{-K/t}$ is increasing, which justifies
using a lower bound for the final surviving probability.

## Reading the small-prime measure from the integer interval

Put
$$
 M=\exp\!\left(\frac{\log Q}{4\pi(y)}\right).
$$
The subsystem with $y$-smooth moduli at most $M$ has a period $P$
satisfying
$$
 P\mid\prod_{p\le y}p^{\lfloor\log_pM\rfloor},\qquad
 \log P\le\pi(y)\log M=\tfrac14\log Q.
$$
Its survivor set $S_{y,M}$ contains $S$. Periodic counting on the
interval $I$, uniformly in its starting point, gives
$$
 \mu(S_{y,M})\ge\alpha-Q^{-3/4}.
 \tag{11}
$$
The reciprocal sum of all $y$-smooth integers greater than $M$
obeys
$$
 \sum_{\substack{m>M\\P^+(m)\le y}}\frac1m
 \ll (\log y)\exp(-\log M/\log y).
 \tag{12}
$$
Indeed, Rankin's inequality with $\theta=1/\log y$ gives the upper
bound $M^{-\theta}\prod_{p\le y}(1-p^{-1+\theta})^{-1}$.
For $y$ large enough that $\theta\le1/4$, comparison with
$\prod_{p\le y}(1-1/p)^{-1}$ shows this product is $O(\log y)$:
the first-power logarithmic difference is bounded by
$e\theta\sum_{p\le y}(\log p)/p=O(1)$, and the higher powers
are bounded by an absolutely convergent series.

The union bound for the omitted smooth moduli and (11)--(12) imply
$$
 \sigma_y\ge\alpha-Q^{-3/4}
 -C_3(\log y)\exp\!\left\{-\frac{\log Q}{4\pi(y)\log y}\right\}.
 \tag{13}
$$
Finally set $L=\log\log Q$ and $y=\log Q/(A_0L)$, with a large
absolute $A_0$. Chebyshev's bound $\pi(y)\le C_\pi y/\log y$
makes the exponent in (13) at most $-4L$ when
$A_0\ge16C_\pi$. Its error is then
$Q^{-3/4}+O(L/(\log Q)^4)$. Meanwhile (9) is
$O(L^3/\log Q)$. Substitute into (10) to prove (1).
For (2), use $\alpha-\varepsilon\ge\alpha/2$ and absorb the
prefactor by $\alpha\log(2/\alpha)=O(1)$.

## A smaller error using quasipolynomial equidistribution

Combining the preceding distortion argument with the new
[interval equidistribution theorem](quasipolynomial_equidistribution.md)
improves the error in (1) to
$$
 \varepsilon(Q)=\exp\{-c(\log Q)^{1/6}\}
 \tag{14}
$$
for an absolute $c>0$ and sufficiently large $Q$, leaving the
constant $C$ in the exponent of (1) absolute. In particular (2)
holds whenever $\alpha\ge2\varepsilon(Q)$ with this smaller error.
This improvement uses Bazzi's theorem through the linked interval
result; the earlier logarithmic error has the elementary smooth-period
proof above.

Let $A$ be the interval theorem's constant and choose
$$
 v=\left(\frac{\log Q}{2A}\right)^{1/3},\qquad
 M=e^v,\qquad y=e^{\sqrt v}.
$$
The interval of length $Q$ is long enough for that theorem with
largest modulus $M$, since $\exp(A(\log M)^3)=Q^{1/2}$.
Thus (11) is replaced by
$\mu(S_{y,M})\ge\alpha-O(e^{-2v})$. The same smooth-tail
estimate (12) and distortion loss (9) give, respectively,
$$
 \sigma_y\ge\alpha-O(e^{-2v}+\sqrt v\,e^{-\sqrt v}),
 \qquad \eta_y=O(v e^{-\sqrt v}).
$$
For large $Q$ their total error is at most (14), after reducing
$c$. Equation (10) proves the improved assertion.

## Limitation

For fixed positive $\alpha$, (2) allows the full survivor density
to go to zero as a power of the largest modulus. It neither bounds
the incremental Haar mass of arbitrary first-kill cells in terms of
their logarithmic trace nor proves the required tail continuity.
The sparse range below (14) is not treated by these estimates.
