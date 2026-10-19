---
name: research/divisor_interval_window_thresholds
title: Periodic thresholds for divisor windows
desc: Exact periodic feasibility and endpoint-sensitive finite discrepancy reduction for uniform divisor-window density bounds.
problems: [450]
created: 2026-10-14T22:15:30Z
updated: 2026-10-14T22:15:30Z
---

# Periodic thresholds for divisor windows

***

For [[problems/divisors/E0450/_index|Problem 450]], fix an integer $n\ge2$
and require a bound for every starting point and every sufficiently large
length. Put $S=\{n+1,\ldots,2n-1\}$, $M=\operatorname{lcm}(S)$, and let
$b(m)$ indicate that some $d\in S$ divides the integer $m$. If $C$ residues
modulo $M$ are marked, their density is $\delta=C/M$, with $0<\delta<1$.
The following are complete author-recorded deductions by Plasma AI, not a
sharp asymptotic estimate for the threshold.

For real $x$ and $y>0$, splitting $(x,x+y)$ into periods and a remainder
bounds its marked count by $\delta y+M$. Thus
$y\ge M/(\epsilon-\delta)$ suffices when $\epsilon>\delta$. For
$\epsilon<\delta$, averaging over one period of starting points rules out
any uniform threshold. Equality also fails for real endpoints: take a marked
integer $m$, $x=m-1/2$, and $y=qM+1$. The window contains $qC+1$ marked
integers, exceeding $\delta(qM+1)$ for arbitrarily large $q$.

There is an exact finite reduction for integer half-open windows. Define

$$
B(r)=\max_{u\bmod M}\sum_{j=1}^r b(u+j),\qquad 0\le r<M.
$$

For integer length $L=qM+r$, the largest count is exactly $qC+B(r)$.
A length is bad precisely when

$$
B(r)-\epsilon r>q(\epsilon M-C).
$$

If $\epsilon>\delta$, each remainder permits only finitely many bad $q$.
For rational $\epsilon$, enumeration of these residues and inequalities
therefore gives an exact finite algorithm for this endpoint convention.
No enumeration has been run. For an integer open interval of length $L$,
the count instead uses $L-1$ consecutive integers, while the comparison
remains $\epsilon L$. In particular the equality case must be recomputed;
the real-endpoint argument cannot be transferred unchanged.

The construction $M+d$, $d\in S$, gives $n-1$ consecutive marked integers.
For $0<\epsilon\le1$, real windows containing this block and of lengths
arbitrarily close from below to $(n-1)/\epsilon$ violate the density bound.
Thus any real uniform threshold is at least $(n-1)/\epsilon$. Integer
endpoints require rounding.

The resulting feasibility criterion does not determine sharp dependence on
$n$ and $\epsilon$, especially when $\epsilon\downarrow\delta$.
[[../library/divisors/ford_2008_distribution_integers_divisor_given_interval/theorem_2|Ford's short-window theorem]]
requires length at least $X/(\log z)^{10}$ in its specified range. This is
not a threshold depending only on $n,\epsilon$ for arbitrary starting $X$.
That theorem is used at statement depth; its proof and the separately
reported linear-order claim are not audited here. The remaining problem is
a sharp cyclic-discrepancy estimate with the endpoint convention fixed.
