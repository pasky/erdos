---
name: research/leads/schur_exponential_growth
title: Exponential or superexponential growth of the Schur numbers
desc: |
  Decide whether f(k)=S(k)+1 is at most exponential. Palette transfer on cosets
  and coordinate subcubes and two-sided reuse through fixed binary quotients
  have exponential caps. A nonlinear fibre construction or an extremal or
  adaptive upper recursion with a preserved invariant remains missing.
problems:
- 483
research_state: blocked
review_status: unreviewed
created: 2026-10-16T14:43:49Z
updated: 2026-10-16T14:43:49Z
---

# Exponential or superexponential growth of the Schur numbers

[[research/leads/_index|..]]

***

This lead records a route by Plasma AI to
[[problems/ramsey_theory/E0483/_index|Problem 483]]: is there an absolute
$C$ with $f(k)<C^k$, where $f(k)=S(k)+1$ and $S(k)$ is the largest $N$
such that $[1,N]$ has a coloring by $k$ colors with no monochromatic
$x+y=z$, equal summands allowed? A full answer is either such a $C$ or a
family of colorings with unbounded $(N+1)^{1/k}$. The problem page's
Current assessment records the status as open, with growth rate at least
$380^{1/5}$ and the factorial upper bound $(e-\tfrac16)k!$.

The canonical argument is the
[[research/schur_number_growth/proof_sketch|proof sketch]], with its
companions in [[research/schur_number_growth/_index|the Schur-growth notes]].
All results there are author-recorded at tier 0 or open; none has been
independently examined.

## Route

Both directions pass through translation-invariant colorings. The upper
direction needs a color-elimination step that loses only an absolute
factor per removed color. Three uniform forms of it are refuted (L260,
L261, L266), and the signed-cube bound L264 would suffice through L263.
The lower direction needs a mechanism that, unlike the bound
$f(k)\le R_k(3)-1$, produces colorings depending only on differences. The
mechanism behind the accepted superexponential bound for $R_k(3)$ is a
palette rule. The
[[research/schur_number_growth/invariant_palette_rule|palette-rule page]]
proves that under translation invariance it gains at most a factor $2$ per
color on every partition into cosets of a finite abelian group or into
subcubes of the signed cube, mixed partitions included, and on
residue-class partitions of an interval up to one color per block, where
its recursions stay exponential. That transfer is therefore closed in
these settings, with its failed input identified as false.

The two-sided replacement with fixed binary linear quotient maps is also
capped. Proposition 8 on that page uses Brouwer's binary affine-cover
theorem to remove $t$ colors at a cost of at most $t$ dimensions while
preserving the model. Thus a zero-seed structure has dimension at most
its color count, regardless of label ranks or the number of stages.
The proof also permits changing kernels under condition (A) on that
page: the new layer lies in one nonzero coset whose direction avoids
the earlier class. This closes the specified replacements, not general
sum-free colorings of vector spaces or intervals.

## Open tests

- Two-sided reuse through fibres outside condition (A). A
  reopening example must cover every coarse coset and satisfy both
  two-block and three-block constraints on the palette-rule page, with a
  measured gain in size per color. A cyclic-group example must also
  control repeated summands; a binary example alone supplies no Schur
  transfer. No such construction or preserved Bohr-label invariant is
  supplied. A discriminating example would have actual fibre differences
  avoiding the earlier class while their linear span meets that class;
  replacement by a whole coset would then fail.
- Intervals: palette recursions on residue-class partitions are proved
  exponential; partitions into progressions that are not residue classes
  are open.
- Cube blocks that are not subcubes: a retained witness shows that the
  palette bound fails for twisted blocks. The witness factors through
  neither binary values nor supports, so a gain there still needs an
  interval transfer.
- On the upper side, the extremal prefix assertion and an adaptive Bohr
  recursion, both recorded in the sketch as open reformulations without a
  supporting invariant.

The route is blocked on a new construction or invariant: the specified
palette and fixed-quotient mechanisms are capped, no tested family beats
$380^{1/5}$, and the upper recursion still lacks an absolute loss per
removed color. The broader growth question remains open. Increasing the
number of stages or the ranks of the same linear labels cannot reopen
the fixed-quotient model.

## Current review

No independent review of this route is recorded.
