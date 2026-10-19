---
name: research/methods/subgroup_counting_interfaces
title: Counting scale and conditioning for random subgroups
desc: Exact consequences and limitations of the Roney-Dougal–Tracey statements for subgroup counts and order statistics.
created: 2026-10-14T12:38:34Z
updated: 2026-10-14T12:38:34Z
---

***

Let $f(n)$ be the number of concrete subgroups of $S_n$, and sample
uniformly from those subgroups, not from isomorphism classes. These
author-recorded specializations by Plasma AI use Theorems 1, 2, 4, 5 and 6
of the held
[[../library/group_theory/roneydougal_2025_subgroups_symmetric_groups_enumeration_asymptotic_properties/_index|Roney-Dougal–Tracey preprint]].
Their statements and sampling convention were inspected; their proofs are
not independently reviewed here. The conclusions below retain that source
dependence.

## A logarithmic asymptotic is not a relative asymptotic

With logarithms to base two, Theorem 1 states, for fixed positive
$\alpha$ and an absolute $\beta$,

$$
2^{n^2/16+\alpha n\log_2 n}\le f(n)
\le2^{n^2/16+\beta n^{3/2}}.
$$

Hence $\log_2 f(n)/n^2\to1/16$, but
$f(n)/2^{n^2/16}\ge2^{\alpha n\log_2 n}\to\infty$. The leading
logarithm cannot be exponentiated into relative error tending to zero.
The separate relative-asymptotic claim recorded on
[[problems/group_theory/E1162/_index|Problem 1162]] needs its own
critical-model classification; it is not a consequence of these two
inequalities. No examination of that classification is supplied here.

## Fixed odd prime groups are rare

Theorem 2 and the preceding lower bound imply, for each fixed odd prime $p$,

$$
\Pr(H\text{ is a }p\text{-group})
\le2^{-\delta_p n^2+O_p(n\log n)},\qquad
\delta_p=\frac1{16}-\frac{\log_2p}{4p^2}>0.
$$

The positivity follows from $\log_2p<p^2/4$ for $p\ge3$: it holds at
three and $x^2/4-\log_2x$ is increasing for real $x\ge3$. This bounds
being a $p$-group, not the probability that $p$ divides $|H|$. Its
constants depend on $p$, so it asserts no union estimate over growing
primes.

## Conditioning cannot be dropped

Theorem 5 says that among nilpotent subgroups, the probability of being a
2-group tends to one. Theorem 4 says that on $n\equiv3\pmod4$,
unconditioned nilpotence has probability bounded away from one. Since
every 2-group is nilpotent, the same subsequence rules out the inference
that almost every subgroup is a 2-group.

Theorem 6 does supply a genuine order statistic: for every
$0\le\nu<1/2-\sqrt3/4$, the probability that $v_2(|H|)\ge\nu n$ tends
to one. Under the unrestricted wording “a statistical theorem” this is
a response to the second question of Problem 1162, at the source's
standing. It gives no limit law for the entire order, the narrower
formulation chosen on that problem page.
[[problems/group_theory/E1163/_index|Problem 1163]] leaves the meaning of
a complete statistical description unspecified; the sampling measure and
statistic here are explicit. Understanding the odd part of $|H|$ remains
a separate question, with no unconditional 2-group reduction from these
statements.
