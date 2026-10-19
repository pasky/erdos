---
name: problems/set_systems/E0734
title: Problem 734
desc: |
  Asks, for all large $n$, for a non-trivial pairwise balanced design on $n$
  points in which each block size is used only $O(n^{1/2})$ times.
tags:
- Combinatorics
status: open
claim: none
created: 2026-09-04T09:17:27Z
updated: 2026-10-15T01:58:15Z
---

# Problem 734

[[problems/set_systems/_index|..]]

***

**Statement.** Find, for all large $n$, a non-trivial pairwise balanced block
design $A_1,\ldots,A_m\subseteq \{1,\ldots,n\}$ such that, for all $t$, there
are $O(n^{1/2})$ many $i$ such that $\lvert A_i\rvert=t$.

**Status.** Open.

**Source.** [erdosproblems.com/734](https://www.erdosproblems.com/734), accessed
2026-09-04. Cite as: T. F. Bloom, Erdős Problem #734,
https://www.erdosproblems.com/734.

**References.**

- [Er81] Erdős, P., On the combinatorial problems which I would most like to see
  solved. Combinatorica (1981), 25-42.
- [dBEr48] de Bruijn, N. G. and Erdős, P., On a combinatorial problem. Nederl.
  Akad. Wetensch., Proc. (1948), 1277-1279 = Indagationes Math. 10, 421-423.

**Formalization.** Statement in
[formal-conjectures](https://github.com/google-deepmind/formal-conjectures/blob/main/FormalConjectures/ErdosProblems/734.lean).

## Current assessment

Under the usual nontrivial design convention $2\le|A_i|<n$, the
incidence argument in [[theory/combinatorics/L26_design_size_multiplicity/_index|L26]]
forces at least $\sqrt n/C$ distinct sizes if each size occurs at most
$C\sqrt n$ times. It also proves that minimum size
$(1-o(1))\sqrt n$ leaves only $o(\sqrt n)$ possible sizes. Thus a
near-uniform construction of the kind sought in Problem 665 cannot also
satisfy this multiplicity bound. The
[[research/design_size_multiplicity/_index|research account]]
records the six-size obstruction for the held Erdős–Larson construction.
The result is author-recorded at tier 0 and does not exclude designs with
a wider size range. No full construction or broader standing search is
supplied here.
<!-- BEGIN problem library links -->

## Linked library material

These entries are derived from explicit links on library pages. They are
navigation only and do not by themselves record mathematical progress.

- [[../library/set_systems/bruijn_1948_combinatorial_problem/_index|bruijn_1948_combinatorial_problem]]
- [[../library/set_systems/bruijn_1948_combinatorial_problem/theorem_1|bruijn_1948_combinatorial_problem / theorem_1]]
- [[../library/set_systems/erdos_1981_combinatorial_problems_which_i_would_most/_index|erdos_1981_combinatorial_problems_which_i_would_most]]

<!-- END problem library links -->
