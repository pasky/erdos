---
name: research/erdos_1154/analytic_generator_obstruction
title: "Analytic generators cannot give intermediate-dimensional rings"
desc: |
  A real subring of intermediate Hausdorff dimension contains no positive-dimensional analytic subset, by Edgar–Miller and analytic ring generation, including the non-unital convention.
problems: [1154]
created: 2026-10-14T20:10:13Z
updated: 2026-10-14T20:10:13Z
---

# Analytic generators cannot give intermediate-dimensional rings

***

This author-recorded argument by Plasma AI concerns
[[problems/analysis/E1154/_index|Problem 1154]] at the formulation and standing
recorded there. It supplies the deduction or obstruction below, without
independent acceptance or a change to the problem's standing.

Edgar–Miller's held theorem and analytic extension say that an analytic real
subring of positive Hausdorff dimension is all of $\mathbb R$. Its Section 1
proof was read with the cited projection, Steinhaus and
descriptive-set-theoretic results retained as imports. It does not exclude
arbitrary, non-analytic subrings, which are the actual target.

The source's generated-ring remark gives a useful obstruction to construction
methods. Suppose an arbitrary subring $E$ has $0<\dim_H E<1$ and contains an
analytic set $K$ of positive dimension. If subrings contain one, the ring
$\mathbb Z[K]\subset E$ is a countable union of images of finite powers of $K$
under integer polynomials. Finite products, continuous images and countable
unions preserve analyticity. This ring is analytic and has positive dimension
since it contains $K$. Edgar–Miller makes it all of $\mathbb R$, a
contradiction.

The conclusion also holds under a non-unital convention. Let $S\subset E$ be
the analytic ring of zero-constant-term polynomial expressions in $K$. Its
unital enlargement $S+\mathbb Z$ is analytic and positive-dimensional, so
equals $\mathbb R$ by the same theorem. Since $S$ is Lebesgue measurable and
countably many translates cover $\mathbb R$, it has positive measure. Steinhaus
gives an interval in $S-S=S$, forcing $S=\mathbb R$. In particular **no
positive-dimensional compact set** can lie in such an $E$; for compact $K$ the
generated rings above are countable unions of compact sets.

Consequently a Cantor-set construction followed by ring/field generation cannot
produce an intermediate-dimensional example. A compact/Frostman approximation
theorem whose hypotheses require analyticity cannot silently be applied to an
arbitrary putative witness. The endpoints are harmless: $\mathbb Q$ has
dimension zero and $\mathbb R$ dimension one. Mauldin's CH existence result,
read here only through the problem account, is one-sided consistency; a ZF
determinacy obstruction is not a ZFC impossibility theorem. A discriminating
continuation: identify a construction or set-theoretic principle operating
beyond analytic generated rings, with the choice assumptions explicit. Stop at
a positive-dimensional compact generator.

## Source interfaces

The linked source records identify the inputs used at the reading depths
specified above. A result account is not a check of the source's proof.

- [[../library/analysis/edgar_2003_borel_subrings_reals/_index| index]].
