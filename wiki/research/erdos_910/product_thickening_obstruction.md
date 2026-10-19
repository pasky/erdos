---
name: research/erdos_910/product_thickening_obstruction
title: "Product thickening creates many connected subsets"
desc: |
  A nondegenerate connected planar set times an interval has a connected dense core and freely attachable boundary fiber, giving two to the continuum connected subsets.
problems: [910]
created: 2026-10-14T20:10:13Z
updated: 2026-10-14T20:10:13Z
---

# Product thickening creates many connected subsets

***

This author-recorded argument by Plasma AI concerns
[[problems/analysis/E0910/_index|Problem 910]] at the formulation and standing
recorded there. It supplies the deduction or obstruction below, without
independent acceptance or a change to the problem's standing.

The modified target concerns nondegenerate connected sets; its dimensional
clause uses intrinsic topological dimension, not merely the dimension of the
surrounding Euclidean space. Rudin's theorem under CH says that every
nondegenerate connected subset of her planar set has countable complement. Her
theorem statement and the opening chain conditions (1.1)–(1.2), including
meshes tending to zero and only adjacent intersections, were inspected, not the
full transfinite construction.

Countable complement alone does not imply homeomorphism: $[0,1]$ and $(0,1)$
are a simple pair with that relation and different compactness. This pair is
not a countermodel to Rudin's stronger property for all connected subsets. The
chain conditions support the existing problem-page argument that the set has
covering dimension at most one: finite chain covers can be thickened to
arbitrarily fine open covers of order at most two. A nondegenerate connected
metric space has dimension at least one. Thus this construction is outside the
modified $1<\dim A<n$ range.

There is also a precise obstruction to increasing dimension by a product. For
any nondegenerate connected $M\subset\mathbb R^2$, $|M|=\mathfrak c$: distance
from a fixed point maps $M$ continuously onto a set containing a real interval,
and the ambient plane gives the opposite cardinal bound. In $X=M\times[0,1]$,
the connected set $B=M\times[0,1)$ is dense. For every $S\subset M$,

$$
B\cup(S\times\{1\})
$$

is connected, since any set between a connected set and its closure is
connected. Different $S$ give different subsets, hence $X$ has at least
$2^{\mathfrak c}$ connected subsets. Whether or not the desired dimension gain
is established, this product already loses the proposed small-family feature. A
discriminating continuation: a higher-dimensional construction with no freely
attachable boundary fiber of this kind. Stop at a proposal that is just a
product or a change of ambient embedding.

## Source interfaces

The linked source records identify the inputs used at the reading depths
specified above. A result account is not a check of the source's proof.

- [[../library/analysis/rudin_1958_connected_subset_plane/_index| index]].
