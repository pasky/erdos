---
name: group_theory/brouwer_1986_inequality_binary_vector_spaces
title: An inequality in binary vector spaces
desc: "Brouwer's codimension bound for irredundant covers of a binary vector space by affine subspaces."
license: reserved
created: 2026-10-16T16:08:20Z
updated: 2026-10-16T16:08:20Z
---

# An inequality in binary vector spaces

[[group_theory/_index|..]]

***

A. E. Brouwer, *An inequality in binary vector spaces*, Discrete Mathematics
**59** (1986), no. 3, 315–317. The edition read is the three-page journal
facsimile supplied by the [CWI repository](https://ir.cwi.nl/pub/2507), at its
[PDF address](https://ir.cwi.nl/pub/2507/2507D.pdf), accessed 2026-10-16.

## Theorem (printed page 315)

In the finite-dimensional setting, let $X$ be a vector space over
$\mathbb F_2$, let $V,U_1,\ldots,U_k$ be linear subspaces of $X$, and let
$a_1,\ldots,a_k\in X$. Suppose the cosets $a_i+U_i$ cover $V$, and deleting
any one coset leaves some point of $V$ uncovered. Set

$$
W=V\cap\bigcap_{i=1}^{k}U_i.
$$

Then $\dim V-\dim W\leq k-1$. In particular, an irredundant cover of a
binary vector space by $k$ affine subspaces has common direction-space
intersection of codimension at most $k-1$. Irredundancy is relative to the
covered space; it cannot be dropped while retaining the same conclusion.

**Read status: claims checked.** The statement's field, cover condition,
irredundancy and common-intersection definition were checked against the
printed page. The paper's proof occupies pages 315–316; it has
not been independently verified here. The remarks on other finite fields
are outside this card's consumed scope.

**Bears on.** The theorem supplies the affine-cover premise for
[[../wiki/research/schur_number_growth/invariant_palette_rule|Proposition 8's bound on binary coset-fibre constructions]]
toward [[../wiki/problems/ramsey_theory/E0483/_index|Problem 483]]. The
application restricts to an affine half, takes an irredundant subcover,
and intersects its directions to remove colors. That native deduction
is author-recorded and unreviewed; the source theorem itself gives no
bound for general Schur numbers.

No file of this source is held: no license on record permits its
redistribution. The journal facsimile's printed page 315 carries Elsevier
Science Publishers' 1986 copyright notice. The CWI record read on 2026-10-16
names no open license for this edition, so the recorded term is reserved.
