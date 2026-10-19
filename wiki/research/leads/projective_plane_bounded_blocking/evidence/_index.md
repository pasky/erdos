---
name: research/leads/projective_plane_bounded_blocking/evidence
title: Evidence
desc: Exact finite checks of prime-plane witnesses, characteristic-two conics, maximal-arc repair obstructions, restricted Singer searches, single orbits and pencil counts for conics and cubics, together with numerical reproduction of explicitly heuristic estimates.
tags: []
sources: []
created: 2026-10-16T19:59:11Z
updated: 2026-10-16T19:59:43Z
---

# Evidence

[[research/leads/projective_plane_bounded_blocking/_index|..]]

***

The [entry point](main.py) checks the finite statements of the
[[research/leads/projective_plane_bounded_blocking/_index|bounded-blocking account]].
Run it from the repository root with
`uv run --no-sync python wiki/research/leads/projective_plane_bounded_blocking/evidence/main.py`;
the full run takes under a minute on one core and needs a C compiler for
the single-orbit clause, and `--quick` stops the three-conic clause at $h=5$,
the single-orbit scan at $p=100$ and the conic-pencil clause at $p=31$.

**Witnesses.** [`assets/cap4_witnesses.json`](assets/cap4_witnesses.json)
holds, for $q=5,7,11$, a point set of PG$(2,q)$ in normalized homogeneous
coordinates over $\mathbb Z/q$: points $(x,y,1)$, $(x,1,0)$ and $(1,0,0)$.
The sets were found by a weighted local search that is not retained; the
checker does not repeat the search. It verifies that each set consists of
distinct normalized points, meets every one of the $q^2+q+1$ lines in one
to four points, and has the size and line-type counts recorded on the
account, and that its size lies in the cap-four interval of
[[theory/combinatorics/L27_blocking_set_cap/_index|L27]]. For $q=11$ it also
verifies that every point lies on four lines of each of the sizes one,
three and four.

**Three conics.** [`util/geometry.py`](util/geometry.py) builds
GF$(2^h)$ from addition and multiplication tables for the first monic
modulus whose quotient ring is a field, and counts every line's
intersection with a point set by direct incidence tests. For $h=2,\dots,7$
the checker forms the union of the conics $\gamma X^2=YZ$ for
$\gamma\in\{1,g,1+g\}$, with $g$ the class of the indeterminate, and
checks that it has $3q-1$ points and meets every line in one to six
points, six being attained for $h\ge3$. The negative control replaces
$1+g$ by $g^2$, which breaks the relation $\gamma_1+\gamma_2+\gamma_3=0$
for $h\ge3$, and checks that some line is then uncovered. The finite
checks support but do not replace the proof on the
[[research/leads/projective_plane_bounded_blocking/parity_construction|parity page]],
which covers every $h\ge2$.

**Heuristic orders.** [`util/heuristic.py`](util/heuristic.py) solves the
convex dual of the relative-entropy minimization by damped Newton steps in
floating point and maximizes the crossover order over mean loads
$K=1.05,1.10,\dots$ below $C$. The checker confirms the mean loads and the
rounded orders quoted on the account for caps five to eight. These are
heuristic numbers; agreement shows only that the quoted values are what
the stated formula gives.

**Singer-invariant sets.** [`util/singer.py`](util/singer.py) finds, for a
prime $p$, the first cubic $w^3=aw^2+bw+c$ (lexicographic in $(a,b,c)$,
$c\ne0$) whose root generates the points of PG$(2,p)$ as the classes of
$w^0,\dots,w^{N-1}$, and the trace-zero difference set $D$. For each entry
of [`assets/singer_witnesses.json`](assets/singer_witnesses.json) the
checker confirms the cycle and the planarity of $D$, rebuilds the union of
the listed classes modulo $M$, and counts every line's intersection
directly. It then compares these loads with the circulant loads
$\sum_{r\in K}\mu(r-t)$, which checks the reduction used by the search.
The witnesses were found by a compiled version of the search in
`singer.cover_search`, not retained; for the recorded cases without a
witness the checker reruns that exact search to exhaustion. It also
recomputes the symmetric first-moment estimates quoted on the account,
which are heuristic.

**Single orbits.** [`util/orbitscan.c`](util/orbitscan.c), compiled into
ignored `output/`, repeats the cycle and difference-set construction for
every prime from $5$ to $2000$ and prints the least and largest class
counts of $D$ modulo each divisor $m\ge2$ of $N$ with
$m\le p+1\le8m$. The
checker confirms the recorded number of pairs, the number with every class
hit, and the exact list of pairs whose counts all lie in $[1,8]$, and
compares the program with `util/singer.py` for $p\le100$. In quick mode
only that Python range runs.

**Maximal arcs.** For $q=2^h$ with $h=2,3,4,5$ and every $d=2^r$ with
$1\le r<h$, the checker builds the point set $Q(x,y)\in H$ from
[[research/leads/projective_plane_bounded_blocking/completion_obstruction|the repair obstruction]].
Here $\alpha$ is the first field element of trace one and $H$ is the span
of the first $r$ polynomial basis vectors. It counts every line's load,
checks that the set has $(d-1)q+d$ points and precisely
$q(q+1-d)/d$ empty lines, and checks that every outside point lies on
exactly $q+1-q/d$ saturated lines. All ten parameter pairs run in both
modes. This tests the construction and its boundary cases; the large
exchange lower bound and the infinite family rest on the exposed proof,
not an enumeration of exchanges.

**Pencil counts.** [`util/pencil.py`](util/pencil.py) enumerates the
points and lines of PG$(2,p)$ for an odd prime $p$ and, for a union $Y$ of
conics, the lines missing $Y$ and the number $N_P$ of them through each
point $P$ off $Y$. For $p=31,37,41,43$ and $m=1,2,3$ conics drawn from a
seeded generator, the checker confirms the pencil bound (3) of
[[research/leads/projective_plane_bounded_blocking/pencil_threshold|the pencil page]]
outside at most $\binom{2m(m-1)}2$ points, the exact values for one conic,
and the lower bound for the number of missed lines derived in the proof of
(4). In these random cases no point violates the bound. The control at
$p=151$ uses two conics with the same tangents from the origin, and checks
that the origin lies on at least $(p-3)/2$ missed lines, far outside the
bound, so the exceptional set in the proposition is needed. The
small-order multi-conic error bounds are wide and supply only weak
tests. The exact single-conic counts and the $p=151$ control are the
nonvacuous comparisons. The proposition for every odd order rests on
the proof on that page.

**Cubic pencils.** `util/pencil.py` also computes $N_P$ for an arbitrary
plane curve with vectorized integer arithmetic. It accumulates the
points of missed lines in batches of at most 256 lines to bound temporary
storage, and the checker first compares it with the direct counts for
the Fermat cubic at $p=31$. At
$p=211$ it takes the Fermat cubic $x^3+y^3+z^3$, the nodal cubic
$y^2z=x^3+x^2z$, the cuspidal cubic $y^2z=x^3$ and the smooth cubic
$y^2z=x^3+3xz^2+5z^3$. Every point off the curve has
$|N_P-p/3|\le2\sqrt p$ except exactly $3$, $3$, $1$ and $0$ points
respectively, each with $N_P>p/2$. For the Fermat cubic these are the
three coordinate points, from which the projection is a cyclic cover.
For the union of the Fermat cubic with the conic $x^2+y^2=3z^2$, and of the
smooth cubic with $x^3+2y^3+7z^3+xyz=0$, the same bound with $\alpha=1/6$
and $1/9$ in place of $1/3$ fails at exactly $2$ and $0$ points.
These central values use the products of the component densities.
The exact exception counts and the constant $2$ are finite observations,
not predictions of the general
[[research/leads/projective_plane_bounded_blocking/pencil_threshold|pencil estimate]].
The two-cubic example has degree six, so $p=211$ does not satisfy that
estimate's sufficient condition $p>D!$. These checks prove nothing
for other primes or curves.

The incidence checks use exact finite-field arithmetic. The heuristic
estimates and the square-root thresholds in the pencil comparisons
are evaluated in floating point. Every failed obligation gives a
nonzero exit through the shared `Checker`.
