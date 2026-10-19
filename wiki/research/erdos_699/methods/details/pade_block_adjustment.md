---
name: research/erdos_699/methods/details/pade_block_adjustment
title: "Erdős 699: adjusting the Padé block while retaining the cofactor clause"
desc: "A smaller Padé block reduces the residual denominator cost. A positive-part inequality quantifies that saving for both finite witnesses and uniform numerical source bounds."
created: 2026-09-22T00:00:00Z
updated: 2026-09-22T19:12:28Z
---

# Erdős 699: adjusting the Padé block while retaining the cofactor clause

[[research/erdos_699/_index|P699 research]] ·
[Numerical joint constants](joint_numerical_thresholds.md) ·
[Current seven and nine bounds](../../archive/previous_bounds/seven_nine_bounds.md)

***

The numerical argument need not choose the Padé index as
$m=\lfloor t\log h\rfloor$, even when $t$ was used to define the
retained cofactor clause. Choosing a smaller index decreases the residual
denominator cost. Quantifying this decrease strengthens the numerical
estimate without changing the clause or its polynomial proof forest.

## The denominator saving

Put $x=\log h$. Write a retained clause as

$$
\sum_p(g_p+b_pe_p)_+\ge R,\qquad R>0,
$$

where its outward-rounded intercepts satisfy

$$g_p>t\kappa_p-b_p,\qquad
\kappa_p=L_{s(p)}a_p\log p>0.$$

Here $a_p$ is the exponent of $p$ in its seed product, $b_p$ is its
factor multiplicity, and $L_0=A+B$, $L_1=B+C$ are the two directional
block lengths. Choose any positive rational

$$
\kappa\le\min_p\kappa_p.
$$

At integer Padé index $m\le tx$, the actual logarithmic residual
denominator cost is bounded by

$$
D_m(x)=\sum_p\bigl(m\kappa_p-b_p(1-e_p)x\bigr)_+.
$$

**Lemma.** If the retained clause fails, then

$$
\boxed{D_m(x)\le\bigl(Rx-\kappa(tx-m)\bigr)_+.}\tag{1}
$$

Indeed, set $z_p=(g_p+b_pe_p)x$. The expression inside each actual
positive part is at most $z_p-\kappa_p(tx-m)$. For arbitrary real
$z_p$ and $s_p\ge s\ge0$,

$$
\sum_p(z_p-s_p)_+\le\left(\sum_p(z_p)_+-s\right)_+.
$$

If no summand survives the subtraction, the assertion is immediate.
Otherwise, summing over surviving indices subtracts at least $s$ and
uses at most the original sum of positive parts. Apply this with
$s=\kappa(tx-m)$ and $\sum_p(z_p)_+<Rx$ to obtain (1).

The subtraction in (1) is made once, not once for every prime. No
assumption about the active sign mask is needed.

## A fixed index covering a height interval

Use the finite constants $A_1,A_2$ from the linked numerical argument,
and let $d$ be the product degree. Write $c,k$ for the two exponential
decay rates before adding a coefficient-gcd contribution. If a common
divisor of both adjacent Padé rectangles has logarithm at least $G_m$,
the nonzero-integer argument gives

$$1\le mA_1\exp\bigl(D_m(x)-cm-G_m\bigr)
 +2^dmA_2\exp\bigl(dx+D_m(x)-km-G_m\bigr).\tag{2}$$

Let $y=tx\ge m$. The upper bound in (1) becomes

$$
D_m(x)\le\max\{0,\kappa m+(R/t-\kappa)y\}.\tag{3}
$$

After taking logarithms, twice the first term in (2) is bounded by
the maximum of two affine functions of $y$. Twice the second term is
bounded by the maximum of two affine functions with slopes

$$
d/t,\qquad (R+d)/t-\kappa.
$$

These functions are convex. Checking strict negativity at both endpoints
therefore certifies every height between them. If $\kappa t\ge R$, the
first term is nonincreasing with $y$; only its left endpoint needs checking.

The left endpoint may exceed $m$. Thus, at an already covered height
$x_0$, one can choose $m<tx_0$, check (2) there, and use the same index
until the right endpoint fails. A sequence of overlapping certified
intervals then joins a finite height to an existing uniform analytic
tail. The usual condition $h\ge s+1$ ensures that the shifted factors
are at most $2h$; it is checked separately from the interval inequalities.

## A smaller block for a uniform tail

Choose a rational $0<\sigma\le t$ and set $m=\lfloor\sigma x\rfloor$.
Formula (1) implies

$$D_m(x)\le B_\sigma x,\qquad
B_\sigma=\max\{0,R-\kappa(t-\sigma)\}.\tag{4}$$

Suppose $\log G_m\ge\ell m$ for every $m\ge m_0$. Put
$C=c+\ell$ and $K=k+\ell$. Sufficient positive decay margins are now

$$\boxed{\sigma C>B_\sigma,\qquad
\sigma K>B_\sigma+d.}\tag{5}$$

All floor and integral prefactors are handled exactly as in the original
numerical argument, with block $\sigma$ and denominator exponent
$B_\sigma$. In particular $\sigma x\ge m_0+1$ ensures that the chosen
index lies in the uniform gcd range. The two inequalities force $C,K>0$,
so replacing $m$ by $\sigma x-1$ introduces the valid factors $e^C,e^K$.

When $K>C$, the value

$$
\sigma_* = \frac{d}{K-C}
$$

balances the two margins. It is a useful candidate when
$\sigma_*\le t$; a nearby rational value is checked with directed
bounds. This is a choice to test, not an assertion that it is optimal
in every parameter regime. The difference $K-C=k-c$ is independent
of the chosen gcd lower rate.

Every whole-index bound must certify every source and join the resulting
height to the polynomial and finite bounds. The
[complete proof at seven](../../proofs/details/index_7_complete.md) supplies
these certificates. The [complete proof at nine](../../proofs/details/index_9_complete.md) now does so as well.

## Initial sources with explicit cofactor targets

For an initial alternative, its negation directly bounds each
$e_p\le\alpha_p<1$. One can then use

$$
D_m(x)\le\sum_p\bigl(m\kappa_p-b_p(1-\alpha_p)x\bigr)_+.\tag{6}
$$

This bound does not require $m\le tx$: the nominal block used to
construct a previous clause is irrelevant. In numerical upper bounds
for (6), each $\kappa_p$ is rounded upward.

The right side is the maximum, over all subsets $S$ of the component
primes, of

$$
m\sum_{p\in S}\kappa_p-x\sum_{p\in S}b_p(1-\alpha_p).
$$

Every slope is nonpositive, so the first term of (2) need only be
checked at the left endpoint. After adding $dx$, the second term is
again the maximum of finitely many affine functions. Its endpoint
checks certify the entire interval. For a pair there are only four
subsets. The balanced choice $m\approx d x_0/(K-C)$ can be tested
even when it exceeds the old nominal value $tx_0$.
