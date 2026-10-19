---
name: research/erdos_132/mixed_valuation_selector
title: An exact obstruction to a mixed dyadic-triadic selector
desc: |
  Two equilateral triangles joined by a bridge defeat maximal triadic
  valuation followed by maximal length inside a dyadic norm shell.
sources: []
research_state: closed
created: 2026-09-23T06:20:00Z
updated: 2026-09-24T22:12:56Z
---


# An exact obstruction to a mixed dyadic-triadic selector

***

The [dyadic investigation](dyadic_distances.md) left open whether every
occurring norm-valuation level contains some rare length. A proposed
refinement was to select, within a dyadic level, the maximal triadic
valuation and then the largest Euclidean length. The following exact
example disproves that selector, not the per-level existence question
or either assertion of [Problem 132](../../problems/distance_problems/E0132/_index.md).

Put $\omega=e^{i\pi/3}$, so $N(a+b\omega)=a^2+ab+b^2$, and define

$$
z=\frac{-95-24\omega}{109},\quad
w=\frac{13-48\omega}{43},\quad
a=1-w=\frac{30+48\omega}{43}.
$$

Both $N(z)$ and $N(w)$ equal one. Take

$$
(p_0,p_1,p_2,p_3,p_4,p_5)
=(0,1,\omega,a,a+z,a+z\omega).
$$

In coordinates, $p_4=(-815+4200\omega)/4687$ and
$p_5=(4302+115\omega)/4687$, where $4687=43\cdot109$.
The seven unit pairs are

$$01,\ 02,\ 12,\quad34,\ 35,\ 45,\quad13.$$

Every remaining squared distance occurs once:

| Pair | Squared distance | $v_2$ | $v_3$ |
|---|---:|---:|---:|
| $03$ | $108/43$ | 2 | 3 |
| $23$ | $25/43$ | 0 | 0 |
| $04$ | $3175/4687$ | 0 | 0 |
| $14$ | $5292/4687$ | 2 | 3 |
| $24$ | $277/4687$ | 0 | 0 |
| $05$ | $4057/4687$ | 0 | 0 |
| $15$ | $25/4687$ | 0 | 0 |
| $25$ | $4212/4687$ | 2 | 4 |

Thus all six values in the norm shell $v_2=0$ have $v_3=0$.
Its largest value is one, with multiplicity seven, greater than
the number of vertices six. The other five shell values are rare.
The entire set has $R=8$, so is emphatically not an Erdős counterexample.

The example also defeats a geometric shortcut. Color the points by

$$\{p_0,p_3\},\qquad\{p_1,p_4\},\qquad\{p_2,p_5\}.$$

Their residues modulo two are $0,1,\omega$, respectively. Modulo
$1+\omega$ they are $0,1,-1$, respectively. Thus the three residue
parts agree for both primes. All cross-color distances are at most one.
The unit graph consists of two disjoint equilateral triangles of the
same color orientation, joined by one bridge. It has no four-cycle
but has seven edges on six vertices. Consequently excluding four-cycles
and oppositely oriented triangles cannot supply the missing edge bound.

The [exact rational certificate](evidence/util/mixed_valuation_selector.py)
checks all fifteen pairs, multiplicities, and valuations. The author
recomputed its spectrum.
