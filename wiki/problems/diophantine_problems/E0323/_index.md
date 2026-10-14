---
name: problems/diophantine_problems/E0323
title: Problem 323
desc: |
  Asks whether $f_{k,k}(x)\gg_\epsilon x^{1-\epsilon}$ and, for $m<k$, whether
  $f_{k,m}(x)\gg x^{m/k}$, where $f_{k,m}(x)$ counts the integers up to $x$ that
  are sums of $m$ nonnegative $k$th powers.
tags:
- Number theory
- Powers
status: open
claim: none
created: 2026-09-04T09:17:27Z
updated: 2026-10-07T20:33:08Z
---

# Problem 323

[[problems/diophantine_problems/_index|..]]

[[problems/diophantine_problems/E0323/claims/_index|claims/]]: The 1 claim page of Problem 323, one per claimant's result; the problem's standing derives from them.

***

**Statement.** Let $1\leq m\leq k$ and $f_{k,m}(x)$ denote the number of
integers $\leq x$ which are the sum of $m$ many nonnegative $k$th powers. Is it
true that

$$
f_{k,k}(x) \gg_\epsilon x^{1-\epsilon}
$$

for all $\epsilon>0$? Is it true that if $m<k$ then

$$
f_{k,m}(x) \gg x^{m/k}
$$

for sufficiently large $x$?

**Status.** Open. Bloom's catalog labeled the problem OPEN. Its commentary
credits Landau with resolving the case $k=2$, through his asymptotic
$f_{2,2}(x)\sim cx/\sqrt{\log x}$. This is recorded as an accepted partial claim
on
[[problems/diophantine_problems/E0323/claims/1908_01_01_landau|Landau's claim page]].
For $k>2$, erdosproblems.com records that it is not even known whether
$f_{k,k}(x)=o(x)$.

**Source.** [erdosproblems.com/323](https://www.erdosproblems.com/323), accessed
2026-09-04. Cite as: T. F. Bloom, Erdős Problem #323,
https://www.erdosproblems.com/323.

**References.**

- [ErGr80] Erdős, P. and Graham, R., Old and new problems and results in
  combinatorial number theory. Monographies de L'Enseignement Mathematique
  (1980). Library card:
  [[../library/number_theory/erdos_1980_old_new_problems_results_combinatorial_number_theory/_index|erdos_1980_old_new_problems_results_combinatorial_number_theory]].

**Formalization.** Statement in
[formal-conjectures](https://github.com/google-deepmind/formal-conjectures/blob/main/FormalConjectures/ErdosProblems/323.lean).

## Current assessment

The erdosproblems.com formulation asks two questions about $f_{k,m}(x)$, the
number of integers up to $x$ that are sums of $m$ nonnegative $k$th powers:
whether $f_{k,k}(x)\gg_\epsilon x^{1-\epsilon}$ for every $\epsilon>0$, and
whether $f_{k,m}(x)\gg x^{m/k}$ for $m<k$ and large $x$. The problem comes from
Erdős and Graham's 1980 monograph [ErGr80], where the authors call it
unattackable by the methods available to them; the erdosproblems.com commentary
notes its bearing on Waring's problem.

The case $k=2$ is settled: Landau's theorem of 1908, that the integers
up to $x$ which are sums of two squares number asymptotically
$cx/\sqrt{\log x}$, gives the first question a yes at $k=2$, and at $k=2$
the second question is the trivial count of squares. This is the accepted
partial claim on
[[problems/diophantine_problems/E0323/claims/1908_01_01_landau|Landau's claim page]],
accepted on the refereed paper alone, with its proof not checked in this
corpus. For $k\ge3$ the first question is not settled, and erdosproblems.com
records that it is not known whether $f_{k,k}(x)=o(x)$. At $k=3$ it is the
weaker form of [[problems/diophantine_problems/E0325/_index|Problem 325]] at
$k=3$, $f_{3,3}(x)\gg_\epsilon x^{1-\epsilon}$, where the best bound recorded
there is Wooley's $f_{3,3}(x)\gg x^{0.91709477}$
([[../library/diophantine_problems/wooley_2015_sums_three_cubes_ii/theorem_1_1|Theorem 1.1]]).
The open standing of the first question for $k\ge3$ rests on the
erdosproblems.com label.

The second question is answered yes at several pairs $(k,m)$ by accepted
results, which have no claim pages here. At $m=1$ it holds for every $k$,
since the $k$th powers up to $x$ number $\lfloor x^{1/k}\rfloor+1$. At $m=2$
and $k=3$ it follows from Heath-Brown's 1997 corollary
([[../library/diophantine_problems/heath_brown_1997_density_rational_points_cubic_surfaces/corollary_p3|Corollary]],
refereed in Acta Arith. 79): the pairs $0\le a\le b\le(x/2)^{1/3}$ number
$\gg x^{2/3}$ and have $a^3+b^3\le x$; an integer $n$ is $a^3+b^3$ for at
most $d(n)\ll_\epsilon x^\epsilon$ such pairs, since $a+b$ divides $n$ and,
with $n$, fixes $a$ and $b$; and the corollary leaves at most
$O(x^{4/9+\epsilon})$ integers up to $x$ with two or more representations,
which take at most $O(x^{4/9+2\epsilon})$ pairs, so the integers with one
representation give $f_{3,2}(x)\gg x^{2/3}$. With $m=1$, this answers the
second question yes at $k=3$. At $m=2$ and every even $k\ge4$ it follows from
Erdős and Mahler's theorem
([[../library/diophantine_problems/erdos_2019_number_integers_represented_binary_form/main_theorem|main theorem (a)]],
refereed in J. London Math. Soc. 13, 1938): $x^k+y^k$ has nonzero
discriminant, and for even $k$ the positive values $\lvert x^k+y^k\rvert$ over
integers $x,y$ are the positive sums of two nonnegative $k$th powers, so
$f_{k,2}(x)\gg x^{2/k}$; for odd $k$ the paper only asserts, without proof,
the restricted form it would need. At $m=3$ and every $k\ge33$ it follows from
Browning and Heath-Brown's corollary,
[[problems/diophantine_problems/E0325/claims/2004_03_17_browning_heath_brown|accepted on Problem 325]]:
$f_{k,3}(x)\ge(c/6+o(1))x^{3/k}$. Other pairs $(k,m)$ with $k\ge4$ are not
assessed here.
<!-- BEGIN problem library links -->

## Linked library material

These entries are derived from explicit links on library pages. They are
navigation only and do not by themselves record mathematical progress.

- [[../library/diophantine_problems/erdos_2019_number_integers_represented_binary_form/_index|erdos_2019_number_integers_represented_binary_form]]
- [[../library/diophantine_problems/erdos_2019_number_integers_represented_binary_form/main_theorem|erdos_2019_number_integers_represented_binary_form / main_theorem]]
- [[../library/diophantine_problems/heath_brown_1997_density_rational_points_cubic_surfaces/_index|heath_brown_1997_density_rational_points_cubic_surfaces]]
- [[../library/diophantine_problems/heath_brown_1997_density_rational_points_cubic_surfaces/corollary_p3|heath_brown_1997_density_rational_points_cubic_surfaces / corollary_p3]]

<!-- END problem library links -->
