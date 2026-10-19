---
name: research/leads/odd_covering_distortion/exact_loss_tail
title: The large-prime tail with exact losses
desc: |
  A convex-order bound for weighted indicator sums, applied coordinate by
  coordinate, bounds each exact large-prime loss of the source's tail by an
  aligned model with independent dominated agreement depths and the worst
  small-prime system. An outward rational certificate accepts any uniform
  surviving density at least 1/4 in the reduced small-prime box through 73,
  including a configuration that defeats the 138.877 moment interface.
created: 2026-10-17T07:00:25Z
updated: 2026-10-17T07:00:25Z
---

# The large-prime tail with exact losses

***

This page is author-recorded work by Plasma AI at tier 0, with no independent
review and no novelty asserted. It bounds the exact losses of the source's
large-prime tail, instead of their second moments, for use in Step 3 of the
[[research/leads/odd_covering_distortion/sketch|odd-covering sketch]]. The
notation is that of the
[[research/leads/odd_covering_distortion/point_kernel|point-kernel page]]: the
reduced small-prime box $Q_s$, systems $S$, and counts $w_S$. The lemmas are
proved below. The quarter-density condition has executable exact evidence;
the separate section of exploratory computations confers no certificate.

## A convex-order bound

**Lemma A.** Let $\nu$ be a probability measure on a finite set, let
$E_1,\ldots,E_m$ be events with $\nu(E_i)\le\beta_i\le1$, let $\omega_i\ge0$,
and put $F=\sum_i\omega_i\mathbf 1_{E_i}$. Let $U$ be uniform on $[0,1]$ and
$F^*=\sum_i\omega_i\mathbf 1[U\le\beta_i]$. Then
$\mathbb E\varphi(F)\le\mathbb E\varphi(F^*)$ for every convex nondecreasing
$\varphi$ on $[0,\infty)$.

*Proof.* Fix $\tau\ge0$ and let $A=\{F>\tau\}$, $a=\nu(A)$. Since
$\nu(E_i\cap A)\le\min\{\beta_i,a\}$,

$$
\mathbb E(F-\tau)_+=\mathbb E\bigl[(F-\tau)\mathbf 1_A\bigr]
\le\sum_i\omega_i\min\{\beta_i,a\}-\tau a
=\mathbb E\bigl[(F^*-\tau)\mathbf 1[U\le a]\bigr]\le\mathbb E(F^*-\tau)_+.
$$

Also $\mathbb EF\le\sum_i\omega_i\beta_i=\mathbb EF^*$. On the bounded range
of $F$ and $F^*$, a convex nondecreasing $\varphi$ is $\varphi(0)$ plus a
nonnegative multiple of $u$ plus a nonnegative mixture of the functions
$(u-\tau)_+$, so the two inequalities give the claim. $\square$

When each $\beta_i$ is a nonincreasing function $\beta(t_i)$ of a depth $t_i$,
with $\beta(0)=1$, the variable $g=\max\{t:U\le\beta(t)\}$ has
$\mathbb P(g\ge t)=\beta(t)$ and $F^*=\sum_i\omega_i\mathbf 1[g\ge t_i]$: the
events are replaced by nested ones of the largest allowed probabilities.

**Lemma B (sequential form).** Let $z=(z_1,\ldots,z_n)$ be random, possibly
together with a further variable $x$ on which everything below is
conditioned. Suppose that for each $c$ and each ball $B$ of depth $t$ in the
digit tree of $z_c$, $\mathbb P(z_c\in B\mid x,z_1,\ldots,z_{c-1})\le
\beta_c(t)$, with $\beta_c$ nonincreasing and $\beta_c(0)=1$. Let
$G_\lambda=\prod_cB_{\lambda,c}$ with $B_{\lambda,c}$ a ball of depth
$t_c(\lambda)$, let $\omega_\lambda\ge0$ depend only on $x$, and put
$F=\sum_\lambda\omega_\lambda\mathbf 1_{G_\lambda}(z)$. Then for every convex
nondecreasing $\varphi$,

$$
\mathbb E\bigl[\varphi(F)\bigm|x\bigr]\le
\mathbb E\,\varphi\Bigl(\sum_\lambda\omega_\lambda
\prod_c\mathbf 1[g_c\ge t_c(\lambda)]\Bigr),
$$

where $g_1,\ldots,g_n$ are independent of each other and of $x$, with
$\mathbb P(g_c\ge t)=\beta_c(t)$.

*Proof.* Induction on $n$. Given $x$ and $z_1,\ldots,z_{n-1}$, $F$ is a
weighted sum of indicators of balls in the last tree, with weights
$\omega_\lambda\mathbf 1[z_{<n}\in\prod_{c<n}B_{\lambda,c}]$. Lemma A in
nested form bounds the conditional expectation by an expectation over an
independent $g_n$. For each fixed $g_n$ the integrand is a convex
nondecreasing function of a weighted sum over the first $n-1$ coordinates,
with weights $\omega_\lambda\mathbf 1[g_n\ge t_n(\lambda)]$, so the induction
hypothesis applies after exchanging the expectation over $g_n$ with that over
$z_{<n}$. $\square$

## The exact-loss tail

Run the source's tail from a measure $P$ on $Q_s$, with distortions
$\delta_k\in(0,1)$ at the primes $p_k>73$. For a small-prime system $S$ and
$c>0$ put

$$
\Phi_P^{\delta}(c)=\frac1{1-\delta}\sup_S\mathbb E_P\bigl(cw_S-\delta\bigr)_+ .
$$

**Theorem C.** For every $k>21$ the loss of the tail step at $p_k$ satisfies

$$
\mathbb P_k(B_k)\le\mathbb E\,\Phi_P^{\delta_k}\!\Bigl(\frac{N_k}{p_k-1}\Bigr),
\qquad N_k=\prod_{21<i<k}(g_i+1),
$$

where the $g_i$ are independent with
$\mathbb P(g_i\ge t)=\min\{1,p_i^{-t}/(1-\delta_i)\}$ for $t\ge1$.

*Proof.* By the loss identity of the digit page,
$\mathbb P_k(B_k)=\mathbb E_{k-1}(\alpha_k-\delta_k)_+/(1-\delta_k)$. Write
$x$ for the small-prime coordinates and $z$ for the large ones before $p_k$.
As in Lemma 2 of the point-kernel page, with $\lambda=(L,e)$ running over the
large parts at this stage and $b$ over the small shapes,

$$
\alpha_k(x,z)\le\sum_\lambda\sum_b p_k^{-e}\,
\mathbf 1_{H_b(\lambda)}(x)\,\mathbf 1_{G_b(\lambda)}(z),
$$

where $G_b(\lambda)$ is a congruence modulo $L$, a product of balls of depths
$t_i(L)$, and $(\cdot-\delta_k)_+$ is nondecreasing. The marginal of $x$ under
$\mathbb P_{k-1}$ is $P$, since later steps preserve old marginals. Given $x$
and the earlier large coordinates, the coordinate of $p_i$ was extended
uniformly and then distorted with multipliers at most $1/(1-\delta_i)$, so a
ball of depth $t$ there has conditional probability at most
$\min\{1,p_i^{-t}/(1-\delta_i)\}$. Later steps preserve these conditional
laws. Lemma B, with the pairs $(\lambda,b)$ as index and weights
$p_k^{-e}\mathbf 1_{H_b(\lambda)}(x)$, therefore bounds the conditional
expectation given $x$ by the same expression with
$\mathbf 1_{G_b(\lambda)}(z)$ replaced by $\mathbf 1[\lambda\le g]$, meaning
$t_i(L)\le g_i$ for every $i$. Summing over $b$ turns the weights into
$p_k^{-e}w_{S_\lambda}(x)$. Each $S_\lambda$ may be a partial system;
completing it by arbitrary hyperplanes only increases its count. Exchange
the expectations over $g$ and $x$. For fixed $g$ put
$C(g)=\sum_{\lambda\le g}p_k^{-e}$. When $C(g)=0$ the loss bound is zero;
otherwise the bound is
$\mathbb E_x(C(g)\sum_\lambda\theta_\lambda w_{S_\lambda}(x)-\delta_k)_+$
with fixed weights $\theta_\lambda\ge0$ summing to one. Convexity gives at
most $\max_\lambda\mathbb E_x(C(g)w_{S_\lambda}-\delta_k)_+\le
(1-\delta_k)\Phi_P^{\delta_k}(C(g))$. Finally
$C(g)\le N_k/(p_k-1)$, counting every exponent vector at most $g$ and
summing over $e\ge1$, and $\Phi_P^{\delta}$ is nondecreasing in $c$.
$\square$

**Corollary D.** If $P$ is supported on the uncovered part of $Q_s$, and for
some $K>21$ and some distortions the certified mass
$\mu_K=1-\sum_{21<k\le K}\mathbb E\,\Phi_P^{\delta_k}(N_k/(p_k-1))$ is
positive and the source's recurrence of
[[../library/covering_systems/balister_2018_erdos_covering_problem_density_uncovered_set/lemma_6_2|Lemma
6.2]], started at $K$ with $f_K=\sigma(P)\prod_{21<i\le K}
\bigl(1+(3p_i-1)/((1-\delta_i)(p_i-1)^2)\bigr)/\mu_K$, reaches the
termination criterion of
[[../library/covering_systems/balister_2018_erdos_covering_problem_density_uncovered_set/theorem_6_1|Theorem
6.1]], then the family does not cover.

*Proof.* The first $K-21$ tail steps lose at most the stated amounts by
Theorem C. From $K$ on, Lemma 2 of the point-kernel page with
$\kappa^*\le\sigma(P)$ supplies the interface of Lemma 6.2 at every later
stage, whatever distortions were used before, and the source's argument
applies with the certified $\mu_K$. $\square$

The bound uses no cap $\alpha_k\le1$: the convexity in Lemmas A and B does not
survive truncation, so rare points with very large $w_S$ count in full.

## The extremal small measure

Lemma B also identifies the worst system for product measures. If $P$ is the
uniform measure on $Q_s$, apply it to the small-prime trees, with the depth
$t$ balls of prime $p$ of probability $c_0(p,t)=1/((p-1)p^{t-1})$. For every
system $S$, $w_S(x)=\sum_b\prod_p\mathbf 1[x_p\in C_{b,p}]$ with $C_{b,p}$ a ball
of depth $b_p$. So $\mathbb E_P\varphi(w_S)\le\mathbb E\varphi(\prod_p(a_p+1))$
with independent $a_p$, $\mathbb P(a_p\ge t)=c_0(p,t)$, and the concentrated
system at any point attains it. Thus

$$
\Phi_U^{\delta}(c)=\frac1{1-\delta}\,
\mathbb E\Bigl(c\prod_{p\le73}(a_p+1)-\delta\Bigr)_+ .
$$

The same inequality holds for any measure built digit by digit, in any order,
with each digit's conditional value masses bounded by a constant independent
of the earlier digits: apply Lemma B with the digits as coordinates, and use
the products of those constants in place of $c_0(p,t)$. Useful conditional
mass bounds are not automatic for a measure supported on an uncovered set;
in general its $\Phi_P$ depends on the residue configuration.

More generally, let $V$ be uniform on a product subset of $Q_s$ allowing
$r_p\ge1$ first digits at prime $p$, and all later digits. The same proof
uses $\Pr(a_p\ge t)=1/(r_p p^{t-1})$ and gives

$$
\sigma(V)\le\prod_{p\le73}
\left(1+\frac{p(3p-1)}{r_p(p-1)^2}\right),\qquad
\Phi_V^\delta(c)\le\frac1{1-\delta}
\mathbb E\left(c\prod_{p\le73}(a_p+1)-\delta\right)_+.
$$

The corresponding first-moment local factor is $1+p/(r_p(p-1))$.
Infinite depths on the right dominate every finite depth vector. If
$d_V=V(R)>0$, then $P=V(\,\cdot\mid R)$ is supported on $R$, with
$\sigma(P)\le\sigma(V)/d_V$ and
$\Phi_P^\delta(c)\le\Phi_V^\delta(c)/d_V$. Choosing the product subset is
part of the problem; its existence with useful bounds is not automatic.

## A uniform-density sufficient condition

**Corollary E.** Let $U$ be uniform on the reduced small-prime box through
$73$, at any finite vector of depths. If its part $R$ avoiding the
$73$-smooth classes satisfies $U(R)\ge1/4$, then no extension by distinct odd
classes whose moduli have a prime greater than $73$ can cover the integers.

*Proof.* Put $d=U(R)$ and $P=U(\,\cdot\mid R)$. Nonnegative integrands give

$$
\Phi_P^\delta(c)\le\Phi_U^\delta(c)/d,
\qquad \sigma(P)\le\kappa_0/d,
$$

where, allowing infinite depth as an upper bound,

$$
\kappa_0=\prod_{3\le p\le73}
\left(1+\frac{p(3p-1)}{(p-1)^3}\right).
$$

Take $\delta_k=2/5$ for $22\le k\le K=2262$, whose last prime is $19997$.
Let $W=\prod_{3\le p\le73}(a_p+1)$, with the independent infinite-depth
variables defined above, and put $T_k=WN_k$. Write

$$
L=\sum_{22\le k\le2262}
\frac53\mathbb E\left(\frac{T_k}{p_k-1}-\frac25\right)_+,
\qquad
M=\kappa_0\prod_{22\le i\le2262}
\left(1+\frac{5(3p_i-1)}{3(p_i-1)^2}\right).
$$

The exact certificate described below proves

$$
L<\frac{201}{1000}<\frac14,
\qquad \frac{M}{1/4-L}<94000.
$$

Thus $\mu_K\ge1-L/d>0$, and $f_K\le M/(d-L)<94000$.
Rational logarithm enclosures give $\log2262>77/10$ and
$\log(77/10)>2$. Therefore

$$
K(\log K+\log\log K-3)^2
>2262(67/10)^2>101000>f_K.
$$

The source's termination theorem applies, so Corollary D concludes the
proof. Appending unused prime coordinates handles a family ending before
$p_K$. $\square$

**Certificate and rounding.** Part 7 of the
[evidence program](evidence/main.py), in
[the tail-density helper](evidence/util/tail_density.py), computes lower
probabilities at integer values of $T_k$ and upper first and second moments.
Every stored quantity is an integer in units of $S=2^{128}$. Atom weights
are rounded down at every convolution; moment bounds are rounded up.
Only agreement depths $0,\ldots,10$ and products at most $4096$ are stored.
These cutoffs discard probability, but do not discard its possible loss.

Indeed, if $u_v/S\le\Pr(T_k=v)$ and $A/S\ge\mathbb ET_k$, the identity

$$
\mathbb E(T_k/(p-1)-2/5)_+
=\frac{\mathbb ET_k}{p-1}
 -\mathbb E\min\{T_k/(p-1),2/5\}
$$

gives the upper bound on the step loss

$$
\frac{5A-\sum_vu_v\min\{5v,2(p-1)\}}{3S(p-1)}.
$$

The first and second moments are the full infinite-depth moments, not
moments of the stored atoms. Their local factors are respectively
$1+p/(p-1)^2$ and $1+p(3p-1)/(p-1)^3$ at a small prime, and
$1+5/(3(p-1))$ and $1+5(3p-1)/(3(p-1)^2)$ at a large prime. Thus omitted
depths, large products, and all rounding errors are included in the upper
bound. The check uses the complete prime list, exact integer arithmetic,
and the rational logarithm series from the lead's other certificates.

The [[research/leads/odd_covering_distortion/support_concentration|support
concentration family]] has $U(R)\ge773/1920>1/4$, so this certificate
handles it despite its forced $\sigma(P)>152.14$. This verifies that the
replacement tail escapes that configuration. The same page gives an
extension whose uniform surviving density is below $1/4$: Corollary E's
density hypothesis is not a universal property of small-prime families.
An adapted product subset handles that extension too. Its first-digit sizes
are $r_3=1$, $r_q=q-2$ for
$q\in\{11,13,19,23,29,31,37,41,43,47,53,59,61,67,71,73\}$,
and $r_p=p-1$ otherwise. The page proves $d_V\ge24005/28512$.
The same outward certificate, using the displayed general local factors,
gives total unconditioned exact loss below $417/1000$ and
$f_{2262}<21000$ after conditioning. Thus Corollary D applies. For arbitrary
families, a supported measure satisfying it remains unconstructed.

## Exploratory computations

The following floating-point runs are exploratory and are not part of the
evidence. They evaluate the bound of Theorem C for the uniform measure, and
for one distortion $\delta=0.4$ at every prime from $79$ to $20000$, with
$N_k$ and the small-prime product computed as exact distributions truncated
at $10^6$. They then add the second-moment losses of the source's interface
from $20000$ to $3\cdot10^6$.

- With $P$ uniform, $\mathbb E[w^2]=\kappa_0\approx86.94$, the exact-loss
  bounds sum to about $0.19$ and the remainder to about $0.04$. With the same
  distortion, the second-moment bounds sum to about $0.66$ up to $20000$.
- Inflating every agreement probability $c_0(p,t)$ by a factor $\gamma$, at
  $\gamma=1.3$ ($\mathbb E[w^2]\approx2.61\kappa_0\approx227$) the sum is
  about $0.61+0.10$, and at $\gamma=1.4$ ($\mathbb E[w^2]\approx3.53\kappa_0
  \approx307$) about $0.85+0.13$, still below one. The retained source
  certificate suffices for $\kappa\le138.877$ when $\mu_{21}=1$, about
  $1.6\kappa_0$; it does not assert that larger values are impossible.
- Replacing the uniform measure at $3,5,7$ by the measure minimizing the
  point kernel on a greedy configuration of that block at depths $3,2,1$,
  and taking the large-prime systems concentrated at its point of largest
  potential, gives about $0.21+0.04$. The block's point kernel is about
  $1.34$ times its own floor, but $\mathbb E[w^2]$ is only about
  $1.08\kappa_0$ because the block is truncated at those depths. For such
  block measures the concentrated system is not always the worst: a
  coordinate-ascent search over all block systems found
  $\mathbb E_P(cw_S-0.4)_+$ up to about $19\%$ above the best concentrated
  system at $c=0.2$, about $4$ to $9\%$ above at $c=0.1$, and nothing above
  at $c=0.05$, for the blocks $\{3,5,7\}$ at depths $2,2,1$ and $3,2,1$.
- Lemma B applies equally to the digits of medium primes after an initial
  block, since each distorted digit has conditional value masses at most
  $1/((1-\delta)q)$. This does not rescue a sieve over the medium primes. With
  the measure above on $\{3,5,7\}$ at depths $2,2,2$, the primes from $11$
  to $73$ at depth two, and one distortion per digit between $0.2$ and
  $0.5$, the aligned medium-prime losses alone were $0.75$ to $1.06$.
- A cruder hybrid that keeps exact losses only for the part with no earlier
  large prime and charges the rest by second moments gained little: in the
  same inflation model it accepted $\mathbb E[w^2]$ up to between $142$ and
  $167$.

So in these models the exact-loss tail accepts a small-prime constant about
twice the source's, and the room over the floor grows from about $1.6$ to
about $3.5$. The medium primes, by contrast, are not helped: the aligned
model is the worst case for a measure built by distortion, and at those
primes its losses are not small. The useful form keeps every small prime in
the initial block. The inflation model is not a worst case. For a measure on an
actual uncovered set, Corollary D needs $\Phi_P$, a supremum over all
systems, which is not computed here.

## What it changes

With Corollary D, Step 3\* of the point-kernel page can be weakened: a measure
$P$ on the uncovered set suffices if its system functionals $\Phi_P$ and
$\sigma(P)$ satisfy the conditions of Corollary D, rather than
$\sigma(P)\le138.877$. The Corollary D condition remains open. Step 3* itself is false by the
[[research/leads/odd_covering_distortion/support_concentration|support
concentration construction]], which forces $\sigma(P)>152.14$ for every
measure on a particular nonempty uncovered set. This does not refute
Corollary D, since its hypothesis is not a bound by $138.877$ on $\sigma$.
A proof of the remaining universal condition still needs a
measure on the uncovered set of every configuration of $73$-smooth classes,
now with control of the upper tail of $w_S$ under $P$ for every system $S$.
