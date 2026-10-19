---
name: research/design_size_multiplicity
title: Near-uniform designs and size multiplicity
desc: The near-square-root block sizes sought in Problem 665 cannot supply the O(sqrt(n)) size multiplicities sought in Problem 734.
created: 2026-10-14T12:38:34Z
updated: 2026-10-14T12:38:34Z
---

# Near-uniform designs and size multiplicity

[[research/_index|..]]

***

[[problems/set_systems/E0665/_index|Problem 665]] asks for pairwise
balanced designs whose blocks are almost of square-root size, whereas
[[problems/set_systems/E0734/_index|Problem 734]] asks that no size occur
too often. The two requirements do not compose through near-uniformity.
The complete author-recorded obstruction is
[[theory/combinatorics/L26_design_size_multiplicity/_index|L26]]:
a nontrivial design has at least $n$ blocks; minimum size
$(1-o(1))\sqrt n$ confines all its sizes to an interval containing only
$o(\sqrt n)$ integers. A fixed bound of $C\sqrt n$ blocks of each size
would then allow only $o(n)$ blocks.

The constructive proof of
[[../library/set_systems/erdos_1982_pairwise_balanced_block_designs_sizes_blocks/theorem_1|Erdős–Larson Theorem 1]]
uses at most six sizes, so some size occurs at least $n/6$ times. More
generally, a successful construction for Problem 734 must use at least
$\sqrt n/C$ distinct sizes. This is a necessary condition, not a
construction or a disproof of the problem.

The source's nearby-prime construction has a separate limitation for
Problem 665. Starting with a plane of prime order $p$, write the excess
$p^2+p+1-n=rp+1+s$, $0\le s<p$, when it is nonzero. Deleting a point,
$r$ suitable lines through it, and $s$ conic points leaves block sizes at
least $\min(p-2,p-r-1)\ge p-r-2$. Since
$rp\le p^2+p-n$, this is at least $n/p-3$. For $p\ge\sqrt n$ the
deficit from $\sqrt n$ is at most $p-\sqrt n+3$; for
$p<\sqrt n$ the bound exceeds $\sqrt n-3$. At zero excess the plane
itself suffices. The construction therefore transfers the prime gap into
the block deficit; it does not make the deficit bounded by an absolute
constant. Its geometric construction was inspected as an author source
check. The converse embedding result cited on Problem 665 was read only
through its existing account and is not a checked premise here.

A useful new route must construct many sizes while keeping each
multiplicity small, or replace the nearby-prime reduction with an all-order
construction having a bounded deficit. The present obstruction only excludes
the near-uniform route to the multiplicity target.
