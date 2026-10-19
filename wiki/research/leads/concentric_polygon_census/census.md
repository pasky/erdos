---
name: research/leads/concentric_polygon_census/census
title: Exact finite census and its limits
desc: |
  Complete positive critical-parameter counts for half-step concentric
  polygons of orders 3 through 32 and diagonal stretches of regular polygons
  of orders 8 through 24, with strict convexity and every vertex checked.
created: 2026-10-16T13:41:30Z
updated: 2026-10-16T13:41:30Z
---

***

Neither family in the [canonical sketch](sketch.md) contains a counterexample
to [[problems/distance_problems/E0982/_index|Problem 982]] within its stated
order range. These are author-recorded computations by Plasma AI, with no
independent review. The parameter domains are continuous, not floating grids:
all positive critical parameters are enumerated exactly, and the sketch
proves that their complements cannot supply a witness.

The [evidence entry point](evidence/_index.md) rebuilds all exact event labels,
convexity classifications and vertex counts. The retained JSON files contain
the actual parameter-defining events, not just the following totals.

## Half-step concentric polygons

Here $n=2m$ and the threshold is $m$. Let $C$ count distinct positive
critical radii, $I$ those strictly inside the convexity interval, $B$ those
on its two endpoints, and $R$ the positive critical radii with both orbit
counts below $m$, without imposing convexity. Every one of the $R$ radii
is outside the strict-convex domain. At the two interior events the counts
are $(m-1,m)$ and $(m,m-1)$; elsewhere in that domain they are $(m,m)$.

| $m$ | $C$ | $I$ | $B$ | $R$ |
| --- | --- | --- | --- | --- |
| 3 | 4 | 2 | 2 | 0 |
| 4 | 6 | 2 | 0 | 2 |
| 5 | 10 | 2 | 0 | 2 |
| 6 | 12 | 2 | 0 | 0 |
| 7 | 20 | 2 | 0 | 0 |
| 8 | 24 | 2 | 0 | 4 |
| 9 | 26 | 2 | 0 | 4 |
| 10 | 42 | 2 | 0 | 2 |
| 11 | 52 | 2 | 0 | 0 |
| 12 | 40 | 2 | 0 | 6 |
| 13 | 68 | 2 | 0 | 0 |
| 14 | 82 | 2 | 0 | 0 |
| 15 | 84 | 2 | 0 | 2 |
| 16 | 100 | 2 | 0 | 8 |
| 17 | 120 | 2 | 0 | 0 |
| 18 | 114 | 2 | 0 | 0 |
| 19 | 148 | 2 | 0 | 0 |
| 20 | 158 | 2 | 0 | 10 |
| 21 | 168 | 2 | 0 | 4 |
| 22 | 200 | 2 | 0 | 0 |
| 23 | 216 | 2 | 0 | 0 |
| 24 | 188 | 2 | 0 | 12 |
| 25 | 250 | 2 | 0 | 2 |
| 26 | 278 | 2 | 0 | 0 |
| 27 | 280 | 2 | 0 | 4 |
| 28 | 310 | 2 | 0 | 14 |
| 29 | 344 | 2 | 0 | 0 |
| 30 | 306 | 2 | 0 | 10 |
| 31 | 388 | 2 | 0 | 0 |
| 32 | 400 | 2 | 0 | 16 |

The total $C$ is 4,438 across these orders. No identification between
parameters of different orders is intended by that total. At $m=3$ the
endpoints $r=1/2$ and $r=2$ are explicitly rejected as degenerate. At $m=4$
the nonconvex control $r=(1+\sqrt3)/\sqrt2$ and its reciprocal give
$(D_A,D_B)=(3,3)$; both fail the convexity interval. A checker that omitted
convexity or checked only one vertex orbit would therefore report false
positives.

## Diagonal stretches of regular polygons

The exact coordinates are $p_k=(\cos(2\pi k/n),\sqrt{s}\sin(2\pi k/n))$
for all real $s>0$. They are strictly convex throughout the parameter domain.
The axes are fixed as in this formula; arbitrary affine images are not
covered.

Here $C$ counts distinct positive critical parameters, including $s=1$.
The generic column is the range of pinned counts over all vertices away
from those parameters. The final column is the minimum of $\max_i D_i$
over positive critical parameters other than $1$. The generic maximum is
$n-1$, so the same minimum holds over all positive $s\ne1$. At $s=1$ all
pinned counts equal $\lfloor n/2\rfloor$ by the regular-polygon formula.

| $n$ | Threshold | $C$ | Generic pinned counts | Minimum noncircular maximum |
| --- | --- | --- | --- | --- |
| 8 | 4 | 15 | 4--7 | 6 |
| 9 | 4 | 49 | 4--8 | 8 |
| 10 | 5 | 31 | 5--9 | 8 |
| 11 | 5 | 102 | 5--10 | 10 |
| 12 | 6 | 51 | 6--11 | 11 |
| 13 | 6 | 183 | 6--12 | 12 |
| 14 | 7 | 95 | 7--13 | 13 |
| 15 | 7 | 301 | 7--14 | 14 |
| 16 | 8 | 149 | 8--15 | 15 |
| 17 | 8 | 455 | 8--16 | 16 |
| 18 | 9 | 186 | 9--17 | 17 |
| 19 | 9 | 660 | 9--18 | 18 |
| 20 | 10 | 311 | 10--19 | 19 |
| 21 | 10 | 912 | 10--20 | 20 |
| 22 | 11 | 461 | 11--21 | 21 |
| 23 | 11 | 1228 | 11--22 | 22 |
| 24 | 12 | 493 | 12--23 | 23 |

The total $C$ is 5,682 across these orders. All $n$ pins are checked, including
odd $n$; no unproved orbit-transitivity assumption removes any vertex.

A useful exact control is $n=8$, $s=1+2\sqrt2$. In vertex order the counts
are $(3,6,4,6,3,6,4,6)$. This strictly convex octagon has some pins below
four, but others above it; checking only the first pin would produce a false
counterexample. The parameter is the exact event $[0,2,3]$ in
[the affine order-eight data](evidence/assets/affine_08.json), and the checker
pins the entire count vector.

## What is excluded

The two bounded order ranges are exhausted over their entire positive
one-parameter domains. The failure is the simultaneous every-vertex distance
requirement inside strict convexity, not a lack of numerical resolution.
The result excludes no untested order and no other family. In particular it
does not address other relative angular offsets, additional radial orbits,
or arbitrary orientations of affine stretching axes. Problem 982 remains
unresolved by this census. The sketch states the precise condition for
reopening the construction route.
