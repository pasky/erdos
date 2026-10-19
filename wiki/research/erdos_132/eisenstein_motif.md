---
name: research/erdos_132/eisenstein_motif
title: An exact bounded Eisenstein-grid search and an eleven-point motif
desc: |
  Preserves the finite grid search; a direct five-candidate certificate
  excludes one-point extensions of its eleven-point two-rare-distance motif.
sources: []
research_state: closed
created: 2026-09-22T23:35:00Z
updated: 2026-10-14T00:26:52Z
---


# An exact bounded Eisenstein-grid search and an eleven-point motif

***

Put $\omega=(1+i\sqrt3)/2$ and identify $(a,b)$ with $a+b\omega$.
Squared lengths are the integers

$$Q(a,b)=a^2+ab+b^2.$$

The completed exact search covered all $65{,}535$ nonempty subsets
of $\{0,1,2,3\}^2$ in these coordinates, including $63{,}019$
with at least five points. It found no set with $R\le1$.

| $n$ | 5 | 6 | 7 | 8 | 9 | 10 | 11 | 12 | 13 | 14 | 15 | 16 |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| Minimum $R$ in this window | 2 | 2 | 2 | 3 | 3 | 3 | 2 | 3 | 3 | 3 | 4 | 5 |
| Number of minimizers | 72 | 32 | 4 | 105 | 56 | 59 | 6 | 6 | 12 | 1 | 2 | 1 |

The [script](evidence/util/eisenstein_grid.py) reproduces this
bounded computation, writing its results under the ignored `output/`
directory of the evidence folder, and the [entry point](evidence/main.py)
checks the table above against them. For each subset, the script removes one
vertex and adds its incidences to the previously computed exact
multiplicity vector, checking that the entries sum to
$\binom n2$. It uses integer arithmetic throughout. This is
computational evidence about this window, not a general proof
of either assertion in [Problem 132](../../problems/distance_problems/E0132/_index.md).

## The eleven-point example

The following representative has $R=2$:

$$
S=\{(0,1),(0,2),(0,3),(1,0),(1,1),(1,2),(1,3),
       (2,0),(2,2),(3,0),(3,1)\}.
$$

Its exact squared-distance spectrum is

$$1:18,\qquad3:12,\qquad4:10,\qquad7:12,\qquad9:3.$$

Thus the rare squared distances are $4$ and $9$; the five counts
sum to $55$. Restoring the missing point $(2,1)$ gives the
twelve-point spectrum

$$1:24,\qquad3:15,\qquad4:12,\qquad7:12,\qquad9:3,$$

with $R=3$.

## No one-point extension of this motif has only one rare distance

This conclusion does not need the finite search above. Comparing the
[independent input](independent/largest_distance_ranks_and_small_orders.md) with
the existing argument gives the following direct finite certificate.

Let $p\notin S$ be any planar point. The set $S$ contains two
disjoint collinear triples, so a circle contains at most nine
of its eleven points. Adding $p$ therefore increases the
multiplicity of distance $3$ from three to at most twelve.
It remains rare in the twelve-point set.

Any new distance has at most eleven pairs, all incident with
$p$, and supplies a second rare distance. It remains to consider
an extension introducing no new distance. Every squared
distance from $p$ to $S$ is then an integer in
$\{1,3,4,7,9\}$, and the diameter remains three.

The points $(0,1),(1,1),(0,2)$ form a unit equilateral triangle.
Translate $(0,1)$ to the origin, and write the new point in
the basis $1,\omega$ as $(a,b)\in\mathbb R^2$. Integer squared
distances to $0,1,\omega$ imply

$$u=2a+b\in\mathbb Z,\qquad v=a+2b\in\mathbb Z,$$

and

$$Q(a,b)=(u^2-uv+v^2)/3\in\mathbb Z.$$

Modulo three the numerator is $(u+v)^2$, so $u+v\equiv0\pmod3$.
Consequently $a=(2u-v)/3$ and $b=(2v-u)/3$ are integers.
Undoing the lattice translation, $p$ has integer Eisenstein
coordinates.

Diameter at most three forces both coordinates into $[0,3]$.
For example, if its first coordinate is at most $-1$, its
squared distance to $(3,0)$ is at least
$\tfrac34\cdot4^2=12$, because
$Q(x,y)=(y+x/2)^2+3x^2/4$. A first coordinate at least four
is similarly excluded by $(0,3)$. Interchanging coordinates
gives the other two exclusions. Thus the only candidates outside $S$ are

$$(0,0),\ (2,1),\ (2,3),\ (3,2),\ (3,3).$$

Four violate the diameter bound, as certified by existing points:

| Candidate $p$ | Witness $q\in S$ | $Q(p-q)$ |
| --- | --- | --- |
| $(0,0)$ | $(2,2)$ | 12 |
| $(2,3)$ | $(0,1)$ | 12 |
| $(3,2)$ | $(1,0)$ | 12 |
| $(3,3)$ | $(0,1)$ | 19 |

Only $(2,1)$ survives, restoring the displayed twelve-point set with
$R=3$. Hence every one-point extension has $R\ge2$, without any
exhaustive enumeration or classification theorem.

The [small-order note](small_orders.md) records an exact degree table
for the twelve-point spectrum and the independently checked source
theorem that it is the unique twelve-point five-distance type.
The independent record's eleven-point example deletes $(1,1)$ instead;
the isometry $(x,y)\mapsto(4-x-y,x)$ preserves the twelve-point set
and maps that deletion to the present one. They are congruent motifs.

This rules out only the indicated one-point enlargement strategy.
It produces neither an $R\le1$ counterexample nor an unbounded
family with uniformly bounded $R$. The author checked the
integer-norm argument and window reduction against the search code
and its output, and checked the direct candidate certificate; both
are author-recorded. The enumeration remains finite evidence only.
