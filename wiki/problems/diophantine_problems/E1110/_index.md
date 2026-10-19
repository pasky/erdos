---
name: problems/diophantine_problems/E1110
title: Problem 1110
desc: |
  Asks, for coprime $p>q\geq 2$ with $\{p,q\}\neq\{2,3\}$, about the density of
  integers that are not sums of numbers $p^kq^l$, none dividing another, and
  whether infinitely many coprime such integers exist.
tags:
- Number theory
status: claimed
claim: proved
parts: [coprime]
created: 2026-09-04T09:17:27Z
updated: 2026-10-15T01:58:15Z
---

# Problem 1110

[[problems/diophantine_problems/_index|..]]

[[problems/diophantine_problems/E1110/claims/_index|claims/]]: The 3 claim pages of Problem 1110, one per claimant's result; the problem's standing derives from them.

***

**Statement.** Let $p>q\geq 2$ be two coprime integers. We call $n$
representable if it is the sum of integers of the form $p^kq^l$, none of which
divide each other.

If $\{p,q\}\neq \{2,3\}$ then what can be said about the density of
non-representable numbers? Are there infinitely many coprime non-representable
numbers?

**Formulation.** erdosproblems.com asks whether there are infinitely many
"coprime non-representable numbers", and Erdős and Lewin (p. 840) also say only
coprime. The phrase reads either as infinitely many non-representable numbers
coprime to $pq$ or as an infinite pairwise coprime family of non-representable
numbers. The pairwise reading implies the other, since each prime factor of $pq$
divides at most one member of a pairwise coprime family. The formal-conjectures
statement takes the pairwise reading. The page's standing targets the
erdosproblems.com wording, and each claim page that bears on the second question
says which reading it covers. The second question is the part `coprime`. The first asks what can be said about the density rather
than a definite question, so it is open-ended: it is not a part, and it never blocks the standing.

**Status.** Claimed: a pending partial claim would settle the definite second part,
and the open-ended first question does not block the standing. Bloom's catalog
labeled the problem open (page last edited 1 April 2026; proof-claims thread
accessed 2026-10-06). The erdosproblems.com proof-claims tab carries three
partial proof claims. Each is recorded on its own claim page, and none is
adopted here. In a claim of 2026-08-05, the forum user
Apiros3 claims that each of the three pairs Yu and Chen left open has an
infinite pairwise-coprime sequence of non-representable numbers prime to $pq$
([[problems/diophantine_problems/E1110/claims/2026_08_05_apiros3|claim page]]).
In a claim of 2026-08-24, Ding, Li, Liu and Zhang claim that the representable
integers for $(5,2)$ have positive lower density
([[problems/diophantine_problems/E1110/claims/2026_08_24_ding_li_liu_zhang|claim page]]).
In a claim of 2026-09-29, Bécart claims the same for $(7,2)$, with a repository
draft of the same date for $(4,3)$
([[problems/diophantine_problems/E1110/claims/2026_09_29_becart|claim page]]).

**Source.** [erdosproblems.com/1110](https://www.erdosproblems.com/1110),
accessed 2026-09-04. Cite as: T. F. Bloom, Erdős Problem #1110,
https://www.erdosproblems.com/1110.

**References.**

- [BMS98] Blecksmith, Richard and McCallum, Michael and Selfridge, J. L.,
  $3$-smooth representations of integers. Amer. Math. Monthly (1998), 529-543.
- [Er92b] Erdős, Paul, Some of my favourite problems in various branches of
  combinatorics. Matematiche (Catania) (1992), 231-240.
- [ErLe96] Erdős, P. and Lewin, Mordechai,
  [[../library/diophantine_problems/erdos_1996_d_complete_sequences_integers/_index|$d$-complete sequences of integers]].
  Math. Comp. (1996), 837-840.
- [YaZh25] Yang, Quan-Hui and Zhao, Lilu, A conjecture of Yu and Chen related to
  the Erd\H os-Lewin theorem. Acta Arith. (2025), 277-286.
- [YuCh22] Yu, Wang-Xing and Chen, Yong-Gao, On a conjecture of Erdős and Lewin.
  J. Number Theory 238 (2022), 763-778.

**Formalization.** Statement in
[formal-conjectures](https://github.com/google-deepmind/formal-conjectures/blob/83397bad317ac2cf180ffd418f791b8613d1a78f/FormalConjectures/ErdosProblems/1110.lean),
which reads the second question as an infinite pairwise coprime family of
non-representable integers, in the category `research open` with no formal
proof named.

## Current assessment

The erdosproblems.com formulation (accessed 2026-09-04) poses two questions for
coprime $p>q\geq 2$ with $\{p,q\}\neq\{2,3\}$: what can be said about the
density of the non-representable numbers, and whether there are infinitely many
coprime non-representable numbers. Both questions are the ones Erdős and Lewin
put on p. 840 of
[[../library/diophantine_problems/erdos_1996_d_complete_sequences_integers/_index|Erdős and Lewin 1996]],
after their Theorem 1 and its Corollary showed that every integer is
representable only for $\{p,q\}=\{2,3\}$ and that the non-representable
numbers are closed under multiplication by $p$ and $q$. The erdosproblems.com
remarks record that Erdős [Er92b] had conjectured the $\{2,3\}$ case and that it
has a short induction proof. In the literature erdosproblems.com cites, Yu and
Chen [YuCh22] proved that the representable numbers have density zero when
$q>3$, when $q=3$ and $p>6$, and when $q=2$ and $p>10$, and that there are
infinitely many coprime non-representable numbers when $q>3$, when $q=3$ and
$p\neq 5$, and when $q=2$ and $p\notin\{3,5,9\}$. erdosproblems.com also records
a threshold question of Erdős and Lewin for the pair $\{2,3\}$: with $f(n)$ the
fastest-growing function such that every large $n$ is a sum of numbers $2^k3^l$,
none dividing another, all exceeding $f(n)$, Yu and Chen proved
$n/(\log n)^{\log_2 3}\ll f(n)\ll n/\log n$, Yang and Zhao [YaZh25] raised
the lower bound to $n/\log n$, and a comment on erdosproblems.com observes that
a result of Blecksmith, McCallum and Selfridge [BMS98] already gives
$f(n)\sim\tfrac{1}{2}(\log 2)(\log 3)\,n/\log n$.
[[problems/diophantine_problems/E0123/_index|Problem 123]],
[[problems/diophantine_problems/E0845/_index|Problem 845]] and
[[problems/diophantine_problems/E0246/_index|Problem 246]] treat three
bases, the $\{2,3\}$ density question and the problem without the
non-divisibility condition.

Three pending partial claims, all unreviewed, bear on the two questions.
[[problems/diophantine_problems/E1110/claims/2026_08_05_apiros3|Apiros3 2026]]
claims that each of the three pairs $(5,2)$, $(9,2)$ and $(5,3)$ has an
infinite pairwise-coprime sequence of non-representable numbers prime to
$pq$, the second question in its stronger reading, and its Lean development
also proves Yu and Chen's range, so the development asserts the second
question for every coprime pair other than $\{2,3\}$.
[[problems/diophantine_problems/E1110/claims/2026_08_24_ding_li_liu_zhang|Ding, Li, Liu and Zhang 2026]]
and [[problems/diophantine_problems/E1110/claims/2026_09_29_becart|Bécart 2026]]
claim that the representable integers have positive lower density for
$(5,2)$ and $(7,2)$, two pairs outside Yu and Chen's density-zero range, and
Bécart's repository adds a draft of the same for $(4,3)$, a third such pair,
so that the first question's answer differs between pairs. Apiros3's claim
settles the part `coprime`, the definite part, so the derived standing is
claimed; the open-ended question does not block the standing, and none
of the three claims is accepted. The search behind this account covered the
erdosproblems.com page, its proof-claims thread, the claimants' postings and
the formal-conjectures statement file; the statements attributed above to Yu
and Chen [YuCh22] and to Yang and Zhao [YaZh25] follow the erdosproblems.com
remarks, not the papers.

## Route analysis

The
[[research/diophantine_representation_interfaces/nondividing_sums|nondividing
smooth sums and density implications]] account records the following scope.
Density zero of representables would imply an infinite pairwise-coprime family
of exceptions prime to $pq$. The note distinguishes the unrestricted
rectangle sentence from the two size conditions of the claimed embedding.
The primary lemma and recursion remain uninspected here; the development's
standing remains claimed.

<!-- BEGIN problem library links -->

## Linked library material

These entries are derived from explicit links on library pages. They are
navigation only and do not by themselves record mathematical progress.

- [[../library/diophantine_problems/erdos_1996_d_complete_sequences_integers/_index|erdos_1996_d_complete_sequences_integers]]
- [[../library/extremal_graph_theory/erdos_1992_my_favourite_problems_various_branches_combinatorics/_index|erdos_1992_my_favourite_problems_various_branches_combinatorics]]

<!-- END problem library links -->
