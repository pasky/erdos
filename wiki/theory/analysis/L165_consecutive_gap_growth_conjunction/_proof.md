---
name: theory/analysis/L165_consecutive_gap_growth_conjunction/_proof
title: Composing the three consecutive-gap bounds
desc: Checks the common sequence model, absolute quantifiers, separate limits and extremum directions, then restricts to the distinct-point subclass.
created: 2026-10-15T20:39:29Z
updated: 2026-10-15T20:39:29Z
---

# Composing the three consecutive-gap bounds

***

Let $\mathcal A$ be all circle sequences and $\mathcal D\subset\mathcal A$
those with distinct terms. Both are nonempty. Use the cyclic labels, real
lifts and extrema defined in
[[theory/analysis/L165_consecutive_gap_growth_conjunction/_index|L165]].
For $n\ge r$, each cyclic gap occurs in exactly $r$ spans, so

$$
0\le nm_n^{(r)}\le r\le nM_n^{(r)}.
$$

This also gives $M_n^{(r)}>0$, making the extended ratio convention
unambiguous. All following limits ignore the finite prefix $n<r$.

[[theory/analysis/L163_all_sequence_span_ratio/_index|L163]] gives an
absolute threshold $r_R$ and, for every $r\ge r_R$ and every
$X\in\mathcal A$, the ratio lower bound with coefficient $1/200$.
[[theory/analysis/L164_all_sequence_span_deviations/_index|L164]] gives
absolute $c>0,r_O$ and the two separate deviation lower bounds for every
$r\ge r_O$ and every $X\in\mathcal A$. Both use circumference one,
ordering by position with index breaking ties, the lifts $y_{i+n}=y_i+1$,
$r$ consecutive gaps, multiplicity, integer $n\ge r$, and natural logs.
The ratio convention is $M/0=+\infty$; the one-sided proof divides by no
minimum. Set $r_0=\max(r_R,r_O)$. Then all three assertions hold for every
fixed $r\ge r_0$ and every sequence. Their limsups need not be witnessed
by the same subsequence.

For any such $r$, put $a=c\sqrt{\log r}$ and $b=\log r/200$.
The universal upper-span deviation bound gives
$\limsup_n nM_n^{(r)}\ge r+a$ for every sequence. Taking its infimum over
$\mathcal A$ gives $\Lambda_r^{\mathcal A}-r\ge a$.
Since the scaled minima are in $[0,r]$,

$$
\limsup_n(r-nm_n^{(r)})=r-\liminf_n nm_n^{(r)}.
$$

The lower-deviation bound therefore gives
$\liminf_n nm_n^{(r)}\le r-a$ for each sequence. Taking the supremum
proves $r-\lambda_r^{\mathcal A}\ge a$. Taking the infimum of the actual
sequence limsup ratios gives
$\mu_r^{\mathcal A}\ge1+b/r$, hence
$r(\mu_r^{\mathcal A}-1)\ge b$.
None of these operations exchanges a limit with an infimum or supremum,
requires attainment, or combines separately optimized numerator and denominator.

For the subclass, order alone gives

$$
\Lambda_r^{\mathcal D}\ge\Lambda_r^{\mathcal A},\qquad
\lambda_r^{\mathcal D}\le\lambda_r^{\mathcal A},\qquad
\mu_r^{\mathcal D}\ge\mu_r^{\mathcal A}.
$$

Thus the same three lower bounds hold for $\mathcal D$. Equality between
these extrema is not needed. As $r$ tends through the positive integers,
both $a$ and $b$ tend to infinity, proving each claimed divergence.

In the modified Statement of
[[problems/analysis/E1221/_index|Problem 1221]], the extrema range over
$\mathcal A$. The displayed maximum and minimum mean the extrema over the
$n$ cyclic starting labels, and its distance is the forward arc through
$r$ consecutive gaps, as its Notes specify. These are exactly the definitions
used above. Its three requested expressions are exactly the three just bounded.
The printed first two expressions $r(\Lambda_r-1)$ and $r(1-\lambda_r)$
are different quantities; no conclusion about them is substituted for the
modified Statement. Their historical interpretation is outside this proof.
