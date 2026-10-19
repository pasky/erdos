---
name: research/arithmetic_construction_interfaces/odd_greedy
title: Two odd-greedy termination conventions
desc: |
  An elementary finite-prefix reduction equates universal termination for
  ordinary odd greedy and for odd greedy with distinct denominators, without
  asserting equal behavior on each input or proving termination.
created: 2026-10-14T22:16:04Z
updated: 2026-10-14T22:16:04Z
---

# Two odd-greedy termination conventions

***

[[problems/unit_fractions/E0282/_index|Problem 282]] uses the least unused
allowed denominator whose reciprocal does not exceed the remainder. The usual
odd-greedy algorithm allows a denominator to be used again. Pihko's
[[../library/unit_fractions/pihko_2001_remarks_greedy_odd_egyptian_fraction_algorithm/_index|paper]]
defines the latter rule in equations (2.1)--(2.2), and Remark 2.4 identifies
the possible repetition. The following elementary reduction compares the
universal questions. It does not identify the two trajectories for every input.

Write $G$ for ordinary odd greedy and $U$ for the rule requiring unused odd
denominators. Both start from a rational $x$ with $0<x<1$, in lowest terms
with odd denominator. Both stop at remainder zero. Subtracting an odd-denominator
unit fraction preserves the property that the reduced denominator is odd.

For any remainder $0<r<2/3$, let $d$ be the smallest positive odd integer
with $1/d\le r$. Then $d\ge3$. If $d=3$, the new remainder is
$r-1/3<1/3$. If $d\ge5$, minimality gives $r<1/(d-2)$, and therefore

$$
0\le r-\frac1d<\frac{2}{d(d-2)}<\frac1d.
$$

Consequently every subsequent denominator in $G$ strictly increases until
termination. In this starting range $G$ and $U$ coincide.

If $2/3\le x<1$, $G$ chooses $3$ twice and reaches $x-2/3\in[0,1/3)$.
Thus universal termination of $G$ on $0<x<1$ is equivalent to its universal
termination on $0<x<2/3$.

For $U$, consider instead the initial consecutive prefix $3,5,7,\ldots,d$.
If the remainder after choosing $d$ is at least $1/d$, the next choice is
$d+2$: all smaller odd denominators have been used, and $1/(d+2)<1/d$ is
affordable. The prefix must reach remainder less than $1/d$, or zero, by
$d=13$ at latest. Indeed, if it has reached $13$, then

$$
\sum_{j\in\{3,5,7,9,11,13\}}\frac1j+\frac1{13}
=\frac{46489}{45045}>1>x.
$$

At that point every used reciprocal exceeds the remainder. Ordinary greedy
from the remainder can use none of those denominators; the strict-increase
argument applies thereafter. Hence the rest of $U$ is an ordinary odd-greedy
trajectory from a rational in $(0,2/3)$ with odd reduced denominator, unless
it has already terminated.

It follows that these three assertions are equivalent:

1. $G$ terminates for every rational $0<x<2/3$ with odd reduced denominator.
2. $G$ terminates for every rational $0<x<1$ with odd reduced denominator.
3. $U$ terminates for every rational $0<x<1$ with odd reduced denominator.

The reduction is author-recorded. Its only source use is to identify the
ordinary algorithm; the inequalities above give the complete argument. No
computational experiment or unproved termination premise is used. The precise
finite assertion is a prefix of at most six choices before $U$ reduces to
$G$, not a bound on total running time. Neither universal assertion has been
proved here. For example, at $x=2/3$ ordinary greedy immediately repeats $3$,
whereas the unused rule cannot do so.

The remaining hard step is termination of ordinary odd greedy in the smaller
range. Checking bounded numerators, denominators or trajectory lengths cannot
replace it without an additional descent invariant. A useful test of a proposed
invariant is whether it decreases across every greedy subtraction in this
range; stop the route if it only bounds finitely many initial inputs. The
reduction says nothing about other residue classes, square denominators, or an
arbitrary allowed set in Problem 282.
