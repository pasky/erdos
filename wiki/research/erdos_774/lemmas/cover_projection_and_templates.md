---
name: research/erdos_774/lemmas/cover_projection_and_templates
title: Cover projection, simultaneous cyclic lifts, and a fixed-template limit
desc: Row duplication is chromatically redundant and inherits the stronger ordinary-cover extraction constant; fixed repeated-type partial templates cannot be fiber-focused with three colors.
tags: [E0774, proved, covers, reduction, incomplete]
sources: []
created: 2026-09-18T20:00:00Z
updated: 2026-09-19T00:48:35Z
---


# Cover projection, simultaneous cyclic lifts, and a fixed-template limit

***

These elementary results sharpen the
[covering obligation](../routes/incidence_cover_extraction.md). They do not
prove unbounded dissociated coloring.

## 1. Common row duplication is redundant for the chromatic supremum

Let A be a finite zero-one matrix with distinct nonzero columns. An
m-sheet incidence cover has rows (x,a), columns (v,b), and an incidence
at (x,`pi[x,v](b)`) for each base incidence (x,v), where every pi[x,v]
is a permutation of the m sheets. Let A^[R] duplicate every row R times.

Given any cover B of A^[R], keep only rows (x,1,a). The remaining
matrix C is an ordinary m-sheet cover of A, on exactly the same indexed
columns. Different base columns are distinguished by their projected base
supports; distinct lifts of one column have disjoint nonempty supports.
Thus the projection retains distinct nonzero columns, and

$$
\ker_{\mathbb Z}B\subseteq\ker_{\mathbb Z}C,
\qquad \chi_h(B)\leq\chi_h(C)\quad(h\geq1).
\tag{1}
$$

Here chi_h forbids relations with integer coefficients in [-h,h]; h=1
is full dissociation, without any bound on support size. Since R=1 is
allowed, (1) proves

$$
\boxed{\sup_{R,\;B\text{ covers }A^{[R]}}\chi_h(B)
=\sup_{C\text{ covers }A}\chi_h(C).}
\tag{2}
$$

It also simplifies extraction. Every dissociated subfamily of C remains
dissociated in B. Analytically, set all deleted-row torus phases to one;
then the polynomial on B becomes exactly the corresponding polynomial on C.
For the positive-real Sidon parameter this gives rho(B)>=rho(C).

Consequently **all** covers of duplicated linear-side line matrices inherit
the ordinary-cover bound

$$
\boxed{\rho(B)\geq e^{-\pi^2/2},}
\tag{3}
$$

and the same full-dissociation extraction constant, directly. The earlier
sine-moment proof and its weaker bound remain valid, but are unnecessary
for this enlargement. Row duplication supplies no new extremal coloring
freedom. This observation is author-recorded; two separate reviewers obtained it
independently.

## 2. Every prescribed integer relation lifts in a cyclic cover

Let 0!=a be in ker_Z A, and put

$$
p_x=\sum_{v:A_{xv}=1,\,a_v>0}a_v
=\sum_{v:A_{xv}=1,\,a_v<0}|a_v|,
\qquad m=\max_xp_x.
$$

Then m>=1 and m>=|a_v| for every supported v. Use sheet group Z/mZ.
Select the consecutive sheets S_v={0,...,|a_v|-1} with sign(a_v).
At each row x, order the positive incident columns arbitrarily and tile
{0,...,p_x-1} by consecutive intervals of their lengths a_v. Tile the
same interval separately using the negative lengths |a_v|. If the tile
assigned to v starts at g[x,v], set `pi[x,v](b)`=b+g[x,v] modulo m.
For unused incidences choose any translation.

At every covered row sheet, selected positive and negative incidences
then balance exactly: each side is the indicator of {0,...,p_x-1}.
This constructs a nonzero ternary relation in a **cyclic translation cover**.
It strengthens the earlier arbitrary-permutation lift without solving its
coloring quantifier.

A finite list of integer relations can be lifted simultaneously in one
abelian cover. Take the product of the individual cyclic sheet groups and
use the componentwise voltages. For relation j, select its sheets in
coordinate j and all sheets in every other coordinate. The other factors
are invariant under translations, so balance follows coordinatewise.
The selected columns need not share any color of a subsequent coloring.

### One palette splits the entire canonical lift menu

The particular simultaneous construction above has a stronger limitation
than the general finite-template bound below. For any finite list of
prescribed integer relations, all their canonical cylindrical lifts and
all deck translates can be split with at most 3 chi_1(A) colors,
independently of the list length.

For each cyclic sheet factor Z/m_j Z with m_j>=2, choose a proper
three-coloring c_j of its cycle; for m_j=1 use the constant zero.
The sheet color c(g)=sum_j c_j(g_j) modulo three changes when one
coordinate moves across any nonloop cycle edge. Pair this color with
a fixed proper dissociated coloring of the base columns.

For a canonical lift of relation j with some |a_v|>=2, the selected
cylinder in that v-fiber contains two adjacent j-coordinate sheets with
identical other coordinates. Their sheet colors differ, also after any
deck translation. If all |a_v|<=1, the projected support is a base
ternary relation and its base colors already differ. These two cases
prove the claimed bound.

This colors only the designated canonical supports and their translates,
not every ternary relation of the product cover. It does not bound the
cover's dissociated coloring number or retire the arbitrary-cover route.
It shows precisely why simply increasing this prescribed relation menu
does not by itself prove arbitrary-color amplification.

## 3. A fixed partial template with repeated type can always be split

Let H be a fixed finite partial incidence pattern over A. Suppose a
connected component contains distinct column vertices u,w with the same
base type v. Fix an H-path from u to w. In any host cover C, a two-edge
step through row type x from column type s to type t acts on sheets by

$$
\pi_{x,t}^{-1}\pi_{x,s}.
$$

The path therefore induces a permutation P of the v-fiber. Form the
undirected graph on that fiber with nonloop edges {b,P(b)}. Its maximum
degree is at most two, so it has a proper three-coloring (color its path
and cycle components). Color all other column fibers arbitrarily with
these same three colors.

Any type-preserving incidence embedding H -> C sends u,w to b,P(b).
Injectivity ensures b!=P(b), so these endpoints have different colors.
Thus no embedded H is fiber-monochromatic, or monochromatic.

**Unused row ports do not repair this obstruction.** Unlike the earlier
full-cover component argument, this proof applies to partial patterns.
It concerns one fixed template and type-preserving embeddings, not
arbitrary templates or embeddings that change the base labeling.

If A itself is dissociated, every connected component of a nonzero
ternary relation support in a cover repeats a base column type. Indeed,
include all incidences of its selected columns. The coefficients balance
separately in each connected component. Without repeated types their
projection would be a nonzero base ternary relation, a contradiction.

For any finite menu of K repeated-type templates, product the K
three-colorings to avoid them all with at most 3^K colors. This does not
give a fixed finite coloring avoiding the infinitely many possible
templates, and does not refute the conjectural lower bound
sup_covers chi_1 >= chi_Q(A).

## Consequence for the live route

The target is now exactly an **ordinary** cover whose different ternary
relation templates jointly defeat a prescribed palette. Neither common
row duplication, a simultaneous finite relation menu, nor fixed-template
fiber focusing establishes that statement.


## Actual colors in one-circuit canonical covers

A stronger but scoped [spectral theorem](canonical_circuit_cover_colors.md)
colors **all** ternary relations of sufficiently large degree-2P
canonical lifts of a primitive nonternary rational circuit by sheet parity.
Their actual coloring number is exactly two. Fixed voltage assignments
also preserve each rationally independent type subset at sufficiently
large prime degrees. These results do not bound arbitrary covers or
simultaneous mixed-circuit constructions.

The [fixed-symbol automaton framework](../routes/translation_cover_automata.md)
handles arbitrary actual colors and all ternary relations of a given
one-dimensional translation cover. It does not supply a density-based
lower bound or choose a symbol defeating every palette.
