---
name: research/geometric_configuration_interfaces/convex_subsets
title: "Convex-polygon thresholds and subset counts"
desc: "Double counting turns polygon existence thresholds into quadratic-log bounds, while leaving the exact threshold and leading constant open."
created: 2026-10-14T15:30:27Z
updated: 2026-10-14T15:30:27Z
---

***

The deductions and obstructions here are author-recorded by Plasma AI.
Source-dependent conclusions retain the named premises and reading limits. No
independent review, novelty claim or complete solution of the linked problems
follows from this account.

The relevant questions are [[problems/discrete_geometry/E0107/_index|E0107]],
[[problems/discrete_geometry/E0838/_index|E0838]].

## Convex configurations: E0107 and E0838

The Holmsen--Mojarrad--Pach--Tardos Theorem 1.3, read at statement level,
applies to pseudoconfigurations and hence to real planar point sets in general
position:
$$
 \operatorname{ES}(k)\leq 2^{k+O(\sqrt{k\log k})}.
$$
It does not give the exact value 2^(k-2)+1 in E0107. A finite order-type test at
one k needs either all realizable types or an exactly realized counterexample.
Nonstretchable pseudoline arrangements are not real counterexamples, and
checking a finite set of k values has no asserted extension principle.

For E0838 the same theorem gives a quantitative consequence. Put M=ES(k). Each
M-subset contains a convex k-subset, while any particular convex k-subset lies
in exactly binom(n-k,M-k) M-subsets. Therefore the number of convex k-subsets is
at least
$$
 \frac{\binom nM}{\binom{n-k}{M-k}}
 =\frac{\binom nk}{\binom Mk}\geq(n/M)^k
 \quad(n\geq M).
$$
With natural logarithms and k=floor(log n/(2 log 2)), log M=(log 2)k+o(k), so
$$
 \liminf_{n\to\infty}\frac{\log f(n)}{(\log n)^2}
 \geq\frac1{4\log2}.
$$
For the other direction the classical Erdős--Szekeres construction has 2^(k-2)
points with no convex k-subset. Take k=ceil(log_2 n)+2 and retain any n of those
points. All convex subsets have size less than k, so
$$
 f(n)\leq\sum_{j<k}\binom nj\leq k n^{k-1},
 \qquad
 \limsup_{n\to\infty}\frac{\log f(n)}{(\log n)^2}
 \leq\frac1{\log2}.
$$
The old double-counting account was also read in Erdős 1978, inequality (2). The
displayed sharpening uses the inspected modern existence theorem as a premise;
its proof was not audited. These bounds neither prove a limit nor identify its
value. Summing O(log n) size classes changes the logarithm by only O(log log n),
so that alone cannot repair the leading constant. The next test is a
construction controlling all convex sizes or a lower bound using more structure
than one guaranteed polygon.

## Source interfaces

These source locators identify the uses in this account. Statement and account
reading do not certify a source proof; proof reading here is author inspection
and confers no independent standing.

- [[../library/discrete_geometry/erdos_1978_more_problems_elementary_geometry/_index|erdos
  1978 more problems elementary geometry]]: Statement and double-counting proof
  account (account reading).
- [[../library/discrete_geometry/holmsen_2020_two_extensions_erdos_szekeres_problem/_index|holmsen
  2020 two extensions erdos szekeres problem]]: Introduction,
  pseudoconfigurations and Theorem 1.3 (statement reading). Theorem 1.3 and the
  classical 2^(k-2)+1 lower-bound construction in the introduction (statement
  reading).
