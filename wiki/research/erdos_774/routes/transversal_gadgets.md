---
name: research/erdos_774/routes/transversal_gadgets
title: Twisted transversals, a scoped reset, and matching gadgets
desc: Arbitrary row twists preserve the phase mechanism; pure-transversal gluing has a two-witness reset under compatible next-step twists, while matching decorations retain uniform extraction and force three colors but no unbounded amplification.
tags: [E0774, proved, construction, coloring, incomplete]
sources: []
created: 2026-09-18T19:40:00Z
updated: 2026-09-18T20:18:00Z
---


# Twisted transversals, a scoped reset, and matching gadgets

***

## 1. The allowed twists

Given a finite $0/1$ configuration on rows $X$, take $d$
row-disjoint copies, indexed by $s\in[d]$. For arbitrary bijections
$T_s:X\to X$, adjoin the disjoint transversal columns
$$
n_x=\sum_{s=1}^d e_{(T_sx,s)}. \tag{1}
$$
The existing root-polygon phase induction survives: correct each point
$(T_sx,s)$ by the same random $Y_x$, where
$Y_x^d$ is the prescribed new-term correction and
$\mathbb EY_x=\cos(\pi/d)$. An old column of weight $w$
lies in one layer and meets $w$ distinct transversals, so its expected
multiplier is exactly $\cos(\pi/d)^w$.
Prescale its coefficient by that multiplier before optimizing old phases.
The proof neither assumes coordinate-preserving permutations nor identical
old phases. It is the mechanism behind the
[ordinary incidence-cover theorem](incidence_cover_extraction.md).

## 2. Two witness colorings and the exact reset scope

Suppose the old configuration admits a proper $q$-coloring, and let
$Y$ be (1)'s extension for $d\ge2$. Choose a nonempty proper
set $S$ of layers and use $q+1$ colors as follows:

- Keep old color 1 in layers in $S$.
- Replace old color 1 by the new color $q+1$ outside $S$.
- Leave all other old colors unchanged.
- Give every new transversal color $q+1$.

This coloring is proper even with arbitrary twists in (1). A fresh-color
relation, restricted to a layer in $S$, has only the transversal
columns there. Their restrictions are a point basis, so every transversal
coefficient vanishes. Remaining relations separate into proper old layers.
All other colors use only old columns and are likewise proper.

Swap $S$ and its complement to obtain a second proper coloring.
The two distinguished color-1 classes are supported in complementary row
sets $U$ and $U^c$, so their rational spans intersect only at zero.

Hence any **next untwisted** pure-transversal extension with at least two
layers remains $(q+1)$-colorable: put those witness colorings in two
layers, arbitrary proper witness colorings elsewhere, and give every
newest transversal color 1. Their required common signed sum is zero.
In particular an actual jump $q\to q+1$ cannot be followed
immediately by another jump under this untwisted operation.

For a next extension with twists $R_s$, the two relevant supports
are instead $R_1^{-1}U$ and $R_2^{-1}U^c$. The same conclusion
holds when $R_1^{-1}U=R_2^{-1}U$, for example when both twists
preserve $U$. **No unconditional arbitrary-successive-twist reset is proved.**
Different row permutations can destroy the disjoint-support argument.
The initial witness construction survives arbitrary twists; its next-step
consequence has this additional compatibility hypothesis.

There is also a [size-conditioned reset](../lemmas/colored_line_preimages.md):
if the old configuration has n rows and the two new layer counts are
d and D, then $nd<d^D$ ensures a $(q+1)$-coloring after both
steps even with arbitrary twists. Choose the sparse distinguished
support independently in each second-stage layer; the expected common
intersection has size $nd/d^D<1$. This does not recover a sparse
distinguished class after the second step, so no indefinitely repeatable
fixed-palette reset is inferred.

## 3. Matching decorations retain a fixed extraction constant

There is a proved enlargement that prevents giving all new columns one
fresh color. Start with the two point-basis columns on two rows. At stage
$i$, take $d_i=i+2$ copies, add all transversals (1), and choose
a perfect matching of their labels. For each matched pair $x,y$, also
add the union column $n_x+n_y$. The number of row labels stays even,
so a perfect matching always exists. Twists and matchings are prescribed
as part of the construction, not selected after seeing a coloring.

The new columns, considered as frequencies in the independent transversal
variables, are disjoint triples
$\{e_x,e_y,e_x+e_y\}$. Each triple has positive-real Sidon
parameter at least $1/2$. To see this directly, conjugate the entire
third term inside the real part: replace $c_3z_xz_y$ by
$\overline{c_3}\,\overline{z_x}\,\overline{z_y}$. The resulting
three simplex characters have product one. Align their ideal phases, then
divide the remaining product error, of angle at most $\pi$, equally
among the three characters. Every real term retains at least
$\cos(\pi/3)=1/2$ of its magnitude. Different matched pairs
are optimized independently.

Now optimize the old coefficients after their attenuation as in Section 1.
Choose the desired transversal values to optimize the new triple polynomial,
then use independent roots to realize those values exactly. A column born
at stage $i$ has weight $d_i$ or $2d_i$, receives at least
$1/2$ of its coefficient magnitude when born, and subsequently has
multiplier
$$
\prod_{j>i}\cos(\pi/d_j)^w
\ge e^{-\pi^2}\quad(w\le2d_i),
$$
by the previously checked telescoping estimate. The initial basis columns
retain at least $\tfrac12e^{-\pi^2/6}$, separating the first side 3
from the later sides. Thus every finite constructed configuration satisfies
$$
\boxed{\rho\ge\tfrac12e^{-\pi^2}.} \tag{2}
$$
One direct-sum application of
[Pisier's Theorem 2](../../../../library/analysis/pisier_1983_arithmetic_characterizations_sidon_sets/_index.md)
gives a uniform full-dissociation extraction constant over all finite stages and
choices. This uses a fixed matching gadget; no degree bound is allowed to grow
silently with the desired number of colors.

## 4. A proved ternary three-color obstruction, not an iteration

Let $R_t$ and $n_t$ be the row and column counts. The construction
has exactly
$$
R_t=2\prod_{i\le t}d_i,\qquad
\frac{n_t}{R_t}=1+\frac32\sum_{i\le t}\frac1{d_i},
\qquad \text{row degree}=1+2t.
\tag{3}
$$
Every old row is copied, and every new row belongs to one transversal and
one matching union, proving the degree formula and the count recurrence.

The already proved variance-entropy bound, with coefficient alphabet
$\{0,1\}$, implies that a proper two-coloring would satisfy
$$
\frac{n_t}{R_t}\log2
\le\log\left(2\pi e\left[\frac{1+2t}{8}+\frac1{12}\right]\right).
\tag{4}
$$
The coefficient of $\log t$ on the left tends to
$\tfrac32\log2>1$, whereas it is one on the right. Thus sufficiently
large stages require at least **three dissociated colors**.

The matched triple itself prevents coloring every new column with one
fresh color, so the pure-basis reset's proof is unavailable here. This is
not evidence of a reusable chromatic jump: no four-color lower bound or
arbitrary-palette amplification is proved. Equations (2)--(4) are the
complete established positive conclusion of this gadget.

The constants, coefficient prescaling, counts, entropy conclusion, and
compatible-twist reset scope passed independent internal review.
