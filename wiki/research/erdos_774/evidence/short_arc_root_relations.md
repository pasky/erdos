---
name: research/erdos_774/evidence/short_arc_root_relations
title: Short-arc flat root relations and what they force
desc: An explicit degree-49 flat multiple of a cyclotomic polynomial gives a 26-point signed root relation in a short arc; short arcs force angular color variation, not a coloring contradiction, and no o(n)-degree flat family was found.
tags: [E0774, computational, proved, incomplete]
sources: []
created: 2026-09-24T23:30:00Z
updated: 2026-09-24T23:30:00Z
---

# Short-arc flat root relations and what they force

[[research/erdos_774/evidence/_index|..]]

***

## An explicit degree-49 flat relation

Bzdęga's jump-one theorem for ternary cyclotomic coefficients, Theorem 1.5 of
[*Bounds on ternary cyclotomic coefficients*](../../../../library/number_theory/bzdega_2010_bounds_ternary_cyclotomic_coefficients/_index.md)
(printed page 6, proof in Section 5, pages 14--15, checked in the held copy),
implies that $(1-x)\Phi_{pqr}(x)$, and hence $(1+x)\Phi_{2pqr}(x)$, are flat for
distinct odd primes $p,q,r$.

The particular polynomial $F=(1+x)\Phi_{210}$ has positive exponents

$$
\{0,3,5,7,8,10,12,37,39,41,42,44,46,49\}
$$

and negative exponents

$$
\{18,20,21,22,23,24,25,26,27,28,29,31\}.
$$

Its elementary exact certificate is

$$
F(x)(1+x^{15})(1+x^{21})(1+x^{35})
=(1+x^{105})(1+x^3)(1+x^5)(1+x^7).
$$

Evaluation at a primitive 210th root is legitimate because the three
factors on the left other than $F$ are nonzero there, and $1+x^{105}=0$.
This gives a 26-point signed relation in an arc of angular length
$2\pi\cdot49/210=7\pi/15$. Polynomial multiplication checks the identity
exactly; it is short exposed arithmetic and needs no separate checker.

Degree 49 is minimal for a nonzero flat multiple of $\Phi_{210}$:
$\deg\Phi_{210}=48$, its height is two, and a degree-48 multiple would be
a scalar multiple with scalar $\pm1$, by its constant coefficient. The same
degree argument applies to $\Phi_{105}$. This is a finite fact, not an
$o(n)$-degree family. Within the displayed ternary-derived even-conductor
family, the degree/conductor ratio is minimized at $(p,q,r)=(3,5,7)$,
giving $49/210$: $(\varphi(pqr)+1)/(2pqr)$ increases in each prime
separately.

## What a short-arc relation actually forces

For a proper coloring $c:\mathbb Z/n\to[q]$, put
$\rho_c(t)=n^{-1}|\{x:c(x+t)\ne c(x)\}|$. If $S$ supports a signed
relation and $T$ is any spanning tree on $S$, then

$$
\sum_{\{a,b\}\in T}\rho_c(b-a)\geq1.
$$

Every translated support is nonmonochromatic, so at least one of its tree
edges is bichromatic; averaging proves the inequality. If $S\subset[0,d]$
and $B=n\rho_c(1)$, ordering its exponents and using $\rho_c(t)\leq tB/n$
gives $B\geq n/d$. Thus hypothetical arbitrarily short flat relations force
unbounded angular color variation, not impossibility of arbitrary finite
coloring.

Neither a finite palette nor averaging implies angular continuity. Write a
root as $e^{2\pi ix}$, let $x_2\in[0,1)$ be its 2-primary component, and
color by $\lfloor2x_2\rfloor$. For every odd prime $p$, $e^{-\pi i/p}\to1$
has 2-primary component $1/2$, so multiplication by it flips every color.
This example is not asserted proper; it refutes only the proposed
automatic continuity inference. Bare measurability also adds nothing on
this countable group: every coloring has a Borel-measurable extension to
the circle, assigning all nonroots one color.

No $o(n)$-degree flat family or unrestricted-coloring contradiction was
proved on this route.

## Exact ranges of the exploratory searches

All runs below were bounded finite searches and supplied no new
negative-solution ingredient. No script is retained.

- For $n=105,1155,15015$, exhaustively tested
  $\Phi_n(x)\prod_{p\in U}(1-x^p)(1-x)^\epsilon$, with
  $U\subseteq\{p:p\mid n\}$, $\epsilon\in\{0,1\}$. Minimum heights were
  respectively 1, 3, 14. The next conductor 255255 was interrupted during
  polynomial construction after the completed cases ceased to
  discriminate, and has no search conclusion.
- At $n=1155$, one integer-feasibility experiment used multiplier degree
  at most 48, constant coefficient 1, all remaining multiplier coefficients
  bounded in magnitude by 1000, product coefficients constrained to
  $[-1,1]$, and a 20-second solver limit. It timed out without a feasible
  point. This is not infeasibility.
- At $n=1155$, tested all 465 squarefree products of proper cyclotomic
  factors of total multiplier degree at most 58. Eligible divisors were
  $1,3,5,7,11,15,21,33,35,55,105$. None gave a flat product. The minimum
  height was two, attained by $\Phi_1\Phi_3\Phi_5$, degree seven.
- Consecutive-power differences $(1-x^s)\Phi_m(x)$ for
  $m\in\{105,165,195,1155\}$ and $s\in\{1,2,3,5,7\}$, a fixed total of 24
  polynomials, were formed exactly to test whether a consecutive-power
  recurrence could yield a useful bounded-height mandatory root
  configuration. Height means the maximum absolute coefficient.

| $m$ | Degree of $\Phi_m$ | Height | Difference heights, in the displayed $s$-order |
|---:|---:|---:|---|
| 105 | 48 | 2 | 1, 1, 2, 3, 3 |
| 165 | 80 | 2 | 1, 2, 3, 3, 3 |
| 195 | 96 | 2 | 1, 2, 3, 3, 2 |
| 1155 | 480 | 3 | 6, 4, 4, 4, 4 |

The low-height multiples did not supply a general recurrence construction;
the [prime staircase](../lemmas/prime_staircase_obstruction.md) supplied
the needed circuits directly. These numbers are recorded observations, not
an asymptotic assertion.
