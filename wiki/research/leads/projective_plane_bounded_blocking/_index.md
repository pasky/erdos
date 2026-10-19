---
name: research/leads/projective_plane_bounded_blocking
title: Bounded line intersections of blocking sets in every finite projective plane
desc: Both directions of Problem 1159 remain open. The sketch records exact limitations of a cap-only repair rule, special-plane constructions, finite Singer-invariant searches, and a conditional negative answer, sharpened by a pencil count to a positive-proportion curve-extraction premise that is unproved.
problems: [1159]
research_state: blocked
review_status: unreviewed
created: 2026-10-16T19:59:11Z
updated: 2026-10-17T02:50:52Z
---

# Bounded line intersections of blocking sets in every finite projective plane

[[research/leads/_index|..]]

[[research/leads/projective_plane_bounded_blocking/completion_obstruction|completion_obstruction]]: An exact Bernoulli calculation leaves quadratically many empty and overloaded lines, while maximal arcs force any exchange adding a point to remove linearly many points; these obstruct specified repair rules, not every absorbing construction.

[[research/leads/projective_plane_bounded_blocking/covering_polynomial|covering_polynomial]]: Duality turns a blocker into a covering line arrangement, whose characteristic polynomial and logarithmic freeness are explicit. A tangent-line normalization gives exact split-polynomial divisibilities; neither interface supplies the fixed-degree structure needed for a negative answer.

[[research/leads/projective_plane_bounded_blocking/curve_reduction|curve_reduction]]: A source estimate for lines missing nonlinear curves survives exceptional points. Derangement densities give the exact coefficient needed by a sufficient extraction argument for minimal bounded-cap blocking sets; the structural premise remains unproved.

[[research/leads/projective_plane_bounded_blocking/evidence/_index|evidence/]]: Exact finite checks of prime-plane witnesses, characteristic-two conics, maximal-arc repair obstructions, restricted Singer searches, single orbits and pencil counts for conics and cubics, together with numerical reproduction of explicitly heuristic estimates.

[[research/leads/projective_plane_bounded_blocking/identities|identities]]: Moment, pencil and variance identities for line loads, a lower bound on the number of changed lines when each load change is smaller than q, and a modular form of the pencil identity.

[[research/leads/projective_plane_bounded_blocking/parity_construction|parity_construction]]: Three conics give cap six in PG(2,2^h) for h at least two; the proof uses additive characters, while a specified multiplicative identity for distinct conics in odd characteristic is impossible and additive graphs force cap at least p.

[[research/leads/projective_plane_bounded_blocking/pencil_threshold|pencil_threshold]]: A pencil count shows that a bounded-cap blocking set has at least p minus O(sqrt(p)) points off any curve of fixed degree in sufficiently large prime planes. The author-recorded proof uses tame monodromy and uniform Chebotarev; the positive-proportion extraction premise needed for a negative answer remains unproved.

***

[[problems/set_systems/E1159/_index|Problem 1159]] asks for one absolute
constant $C$ such that every finite projective plane has a point set meeting
every line in at least $1$ and at most $C$ points. This account proves
neither answer. Its positive sketch lacks a cap-preserving completion
rule; its negative sketch lacks a uniform structural theorem for arbitrary
point sets. It retains the following supporting work at author standing:

- [[research/leads/projective_plane_bounded_blocking/identities|All-plane identities]],
  including the precise hypotheses of the exchange-footprint bound. A
  bound on changed lines does not rule out a move involving few points.
- [[research/leads/projective_plane_bounded_blocking/completion_obstruction|Exact completion obstructions]]:
  an independent random start has quadratically many empty and overloaded
  lines, and explicit maximal arcs force linearly many deletions whenever
  an exchange adds a point. The latter disproves a bounded-deletion rule
  that advances coverage in every move from every cap-bounded state,
  not every absorbing strategy.
- A [[research/leads/projective_plane_bounded_blocking/parity_construction|three-conic construction]]
  with cap six in PG$(2,2^h)$ for $h\ge2$, a known kind of result, and
  limitations of specified extensions to odd characteristic.
- Exact finite witnesses and searches in prime planes, with an
  independent-load heuristic whose numbers are not bounds.
- A [[research/leads/projective_plane_bounded_blocking/curve_reduction|complete conditional negative argument]]:
  a uniform bounded-degree approximation theorem would make
  $c(\operatorname{PG}(2,p))$ tend to infinity. The approximation theorem
  remains unproved; the implication uses the stated source estimate for
  lines missing curves, at its disclosed reading depth.
- A [[research/leads/projective_plane_bounded_blocking/pencil_threshold|pencil count]]
  proving that a bounded-cap blocking set in PG$(2,q)$ with $q$ odd has
  at least $q-O(\sqrt q)$ points off any bounded union of lines and conics.
  A proof using tame monodromy and uniform Chebotarev extends this to
  every curve of bounded degree in sufficiently large prime planes.
  Then a fixed positive proportion extracted onto
  curves of fixed degree from every bounded-cap set of at least
  $(1-\varepsilon)p$ points would answer the problem negatively. That
  extraction premise is not proved for any cap above two.

Prime planes are a sufficient family for a possible negative answer and
an unresolved part of the positive question. Even a positive construction
there would leave other Desarguesian and non-Desarguesian planes to handle.

## Target and conventions

For a finite projective plane $\Pi$ of order $q$, with $N=q^2+q+1$ points
and lines, let $c(\Pi)$ be the least integer $C$ for which some point set
$S$ has $1\le|S\cap\ell|\le C$ for every line $\ell$. A line itself shows
$c(\Pi)\le q+1$. The question is whether $\sup_\Pi c(\Pi)$ is finite over
all finite projective planes. A positive answer needs one bound for every
plane, Desarguesian or not, of every order. A negative answer needs an
infinite family of planes on which $c(\Pi)$ is unbounded, which means
excluding every point set, not only curves, random sets or the output of
one algorithm. The size of $S$, cover numbers of line families and
completeness of arcs are different parameters. Szőnyi's survey writes
property $B(c)$ for a blocking set with fewer than $c$ points on every
line, so $B(c)$ means cap $c-1$. Below, the load of a line is
$x_\ell=|S\cap\ell|$ and $t_i$ is the number of lines with load $i$.

## Held results and their standing

- [[theory/combinatorics/L27_blocking_set_cap/_index|L27]], author-recorded
  at tier 0: $c(\Pi)\ge4$ when $q\ge5$. At cap four its proof gives the
  size interval $s\in\frac{4q+5}2\pm\frac{\sqrt{24q+9}}2$ and the identity
  $t_2+t_3=-\frac12\bigl(s^2-(4q+5)s+4N\bigr)\le(24q+9)/8$, so almost
  every line has one or four points.
- The [[../library/set_systems/erdos_1983_intersection_properties_families_containing_sets_nearly/corollary_p255|Erdős–Silverman–Stein corollary]]:
  for every $a>2e$ and every plane of sufficiently large order $q$,
  $c(\Pi)<a\log q$. Statement read; proof not audited here.
- Statements reported in
  [[../library/set_systems/szonyi_1992_blocking_sets_finite_planes_spaces/_index|Szőnyi's 1992 survey]],
  printed p. 102, read from the page image; none of the originals was read.
  Abbott and Liu (Ars Combin. 20 (1985), 217–220): for PG$(2,q)$ with $q$
  an odd prime power, the condition $c>2e$ of the Erdős–Silverman–Stein
  bound $c\log q$ may be replaced by $c>2/\log2$. Ughi
  (Geom. Dedicata 26 (1988), 241–245): in PG$(2,q)$, $q$ odd, a union of
  $c$ conics never blocks every line once $q$ is large compared to $c$.
  Bruen and Fisher (Pacific J. Math. 53 (1974), 73–84): PG$(2,3^r)$ has
  cap $4$. Boros (Ars Combin. 25 (1988), 111–114): PG$(2,p^r)$ with $p$ an
  odd prime has a blocking set of $2p^r$ points with cap $p+1$. Illés,
  Szőnyi and Wettl (1991): PG$(2,2^r)$ has cap $5$ for even $r$ and $6$
  for odd $r$.
- Kahn's theorem on random line families
  ([doi:10.1007/BF01305234](https://doi.org/10.1007/BF01305234)) controls
  the cover number of a uniformly random family of at least
  $22(q+1)\log(q+1)$ full lines. In the dual form of Problem 1159, a family
  of lines covering every point between $1$ and $C$ times, that many lines
  already force an average point degree of at least $22\log(q+1)$. The
  theorem is therefore no input here.

Together: $c$ is bounded on the Desarguesian planes of each fixed
characteristic $p$, by $p+1$ for odd $p$ and by $6$ when $p=2$. For the
prime-order planes PG$(2,p)$ the bounds read are logarithmic, and for
non-Desarguesian planes only the Erdős–Silverman–Stein bound applies. This
summarizes the material read, not a complete survey.

The elementary proofs and finite checks here are author-recorded by
Plasma AI, without independent review. The curve reduction additionally
uses an explicitly cited source theorem; it does not independently verify
that theorem or establish its own structural premise.

## Positive direction: the whole argument and where it breaks

A possible route chooses an absolute cap $C$, constructs a partial set
$S_0$, and then covers the remaining lines while controlling every load.
One proposed start samples points independently with probability
$\lambda/q$ and trims overloaded lines. It gives a cap-bounded partial
set, but no useful completion invariant is proved for the resulting state.
For fixed $\lambda,C$, the
[[research/leads/projective_plane_bounded_blocking/completion_obstruction|exact random-start calculation]]
shows quadratically many empty and overloaded lines before trimming.
Deleting all points would also satisfy the cap, so the upper bound by
itself says nothing about the distribution after that operation.

The complete conditional construction is:

1. Specify a family $\mathcal I$ of states in every plane and an absolute
   integer $C$. Construct an initial state $S_0\in\mathcal I$, with each
   line load at most $C$.
2. For $S\in\mathcal I$, let $U(S)$ be its empty lines and $T_C(S)$ its
   lines of load $C$. If $U(S)$ is empty, return $S$.
3. Otherwise construct $R\subseteq S$ and $A$ disjoint from $S$ such that
   $S'=(S\setminus R)\cup A$ belongs to $\mathcal I$, every line has new
   load at most $C$, every covered line stays covered, and at least one
   line of $U(S)$ becomes covered. The exact load change on each line is
   $-|R\cap\ell|+|A\cap\ell|$.
4. Repeat. The number of empty lines strictly decreases, so in at most
   $q^2+q+1$ moves the output meets every line in $1$ to $C$ points.

Step 4 is proved once the preceding conditions hold. Steps 1 and 3
require a sufficient invariant and its repair construction; neither is
supplied. An insertion is legal exactly when its point lies on no line
of $T_C(S)$, and it advances coverage only if that point lies on an empty
line. No count here guarantees such a point in a state produced by a
specified process.

There is an exact reason not to set $\mathcal I$ equal to all cap-bounded
partial sets and require only boundedly many deletions per move while
each move covers a new line. For each fixed power of two $C\ge4$, the
[[research/leads/projective_plane_bounded_blocking/completion_obstruction|maximal-arc construction]]
gives states in PG$(2,2^h)$ with quadratically many empty lines, while
any exchange adding an outside point requires at least $q+1-q/C$
deletions. Thus this universal bounded-deletion premise is false. The
example is not asserted to arise when each greedy insertion must hit an
empty line, and it does not exclude a more selective state invariant,
preparatory moves that only delete points, or exchanges with $O(q)$
deletions.

The exchange-footprint lemma supplies a separate accounting constraint:
when $q>2C$, any nonzero change between cap-$C$ sets changes at least
$q+1$ line loads, and at least $q+2$ unless it changes just one point.
It supplies no lower bound on the point support of an absorber. Similarly,
the variance identity fixes a second moment, not a tail distribution;
it is compatible with bounded loads. There is no theorem here that
random, greedy, nibble or absorption methods as a class must fail.

Reopening the positive route requires an explicit sufficient invariant
and a construction of the moves in step 3, or a different all-plane
construction. Merely asserting a completion for an arbitrary partial set
leaves the desired construction missing.

## Constant-cap mechanisms in special planes and their limits

The [[research/leads/projective_plane_bounded_blocking/parity_construction|parity page]]
proves that three conics $\gamma X^2=YZ$ with
$\gamma_1+\gamma_2+\gamma_3=0$ meet every line of PG$(2,2^h)$, $h\ge2$, in
$1$ to $6$ points. For each slope, meeting a conic is an affine condition
over $\mathbb F_2$ on the intercept, and the linear relation forces an odd
number of the conditions to hold. The same page limits two extensions.
For $q$ odd, meeting a conic is governed by a quadratic character of a
quadratic form in the line coordinates, and distinct conics admit no
multiplicative identity that would play the role of the relation. In
characteristic $p$, any point set containing the graph of an
$\mathbb F_p$-linear map meets some line in at least $p$ points, and for
prime $q$ such graphs are lines. Every constant-cap result read uses a
fixed characteristic, and the caps obtained grow with $p$. Subplane-type
objects, Baer subplanes and unitals, have caps $\sqrt q+1$.

In prime order the structured candidates in the material read are
curves, and Ughi's theorem excludes bounded unions of conics. Random sets
give logarithmic caps.
These particular positive mechanisms give no uniform construction in
PG$(2,p)$, and none is supplied for all non-Desarguesian planes.

## Negative direction: a conditional full argument

The family PG$(2,p)$ with $p$ prime suffices for a disproof if its necessary
caps can be shown unbounded. The
[[research/leads/projective_plane_bounded_blocking/curve_reduction|curve reduction]]
gives an end-to-end conditional argument. For each fixed cap $C$, suppose
there is a fixed degree $D=D(C)$ such that every inclusion-minimal
cap-$C$ blocking set in each sufficiently large prime plane lies on a
degree-at-most-$D$ curve except for at most $p/(4M(D))$ points. Here
$M(D)$ is the maximum product of integers at least two with sum at most
$D$, explicitly evaluated on that page. Remove the curve's line
components and its non-geometrically-irreducible components, losing at
most $CD+D^2$ further points. The remaining curve misses at least
$(1/M(D)-o(1))p^2$ lines, uniformly at fixed degree, by the precise source
estimate. The exceptional points hit at most
$(p/(4M(D))+CD+D^2)(p+1)$ lines. Some line misses the minimal blocking
set, a contradiction. Since every cap-$C$ blocking set contains a
minimal one, this premise for every fixed $C$ would give
$c(\operatorname{PG}(2,p))\to\infty$.

The
[[research/leads/projective_plane_bounded_blocking/pencil_threshold|pencil count]]
improves the tolerance. Through a point off $Y$ pass about
$\alpha(Y)p$ of the missed lines, not $p+1$, when the projection from that
point has full monodromy. Exceptional points then number about $p$ rather
than $\alpha(Y)p$ before they can block all missed lines. This is proved
for unions of lines and conics in PG$(2,q)$ with $q$ odd. For curves of
bounded degree the author-recorded proof shows that the projection from a point off
boundedly many special lines keeps the full product monodromy.
It uses connectedness of an ample pullback, tame local ramification
and Entin's uniform Chebotarev theorem, at the reading depths recorded
on that page. With it, the negative answer follows
from a positive-proportion premise: for each $C$, a fixed fraction of every
cap-$C$ set of at least $(1-\varepsilon)p$ points lies on a curve of fixed
degree.

The source estimate is about curves, and the structural premise is about
arbitrary sets. The latter bridge is unknown. A stronger conjecture,
with $o(p)$ exceptions at fixed degree, occurs in Green's commentary to
Problem 68; it is not supplied as a theorem. Neither the source's curve
obstruction nor the finite searches below prove this bridge.

Several restrictions guide a possible proof. A lower bound tending to
infinity with $q$ and asserted for every plane is impossible: the cap is
bounded for PG$(2,2^h)$ and PG$(2,3^h)$. A prime-plane argument can instead
use primality, characteristic, or other hypotheses particular to its
family. Incidence moments alone do not distinguish these families.

Also, membership of the load vector in the $\mathbb F_p$-code spanned by
pencils, together with residues in a bounded range, is too weak. This
code contains the all-one word (the sum of all pencils) and hence the
word $1+x_O$ for an oval $O$, with entries in $\{1,2,3\}$. L27 excludes
an actual cap-three blocking set for $p\ge5$. This example refutes that
particular relaxation; it does not exclude arguments over $\mathbb F_p$
that retain the indicator variables and their binary constraints.

An alternative way to retain multiplicities is the Rédei polynomial.
Take a line of least load $j\le C$ as the line at infinity and let $S'$
be the affine part. For every non-vertical slope $m$ whose point at
infinity is not in $S$,

$$
\prod_{(a,b)\in S'}(T-b+ma)=(T^p-T)\,G_m(T),\qquad
G_m(T)=\prod_{c\in\mathbb F_p}(T-c)^{x_{m,c}-1},
$$

where $x_{m,c}\in[1,C]$ is the load of $y=mx+c$ and
$\deg G_m=|S'|-p$. A direct approach requiring $\deg G_m<p-1$ only
addresses $|S'|<2p-1$; no reason here confines every bounded-cap blocking
set to that size range. The
[[research/leads/projective_plane_bounded_blocking/covering_polynomial|covering-polynomial route]]
uses a tangent as the line at infinity to retain all nonvertical
slopes, the upper-multiplicity divisibility and the essential-point
condition. In the dual formulation Yoshinaga's theorem makes every
covering arrangement free, but its basis degrees grow with $p$.
Neither interface yields the missing fixed-degree structure.

**A cap-four polynomial test.** There $x_{m,c}-1\in\{0,3\}$ except
on the $t_2+t_3\le(24p+9)/8$ lines with two or three points, so
$G_m=U_m^3V_m$ with $\sum_m\deg V_m\le(24p+9)/4$. In characteristic three
a cube $U(T)^3$ is a polynomial in $T^3$, and cap-four sets exist.
For $p\ge5$ a theorem forcing a long secant from such near-cube
specializations for all sufficiently large primes would force any
universal cap to be at least five.
The
[[research/leads/projective_plane_bounded_blocking/identities|modular lemma]]
adds, for $3\nmid q$, that the lines with two or three points cover $S$ or
cover its complement. The witness in
PG$(2,11)$ below shows that such a theorem must exclude small primes or
sporadic sets.

The near-cube identity is exact, but no theorem extracting a long secant
or a curve of bounded degree from it is proved here. Even such a theorem
only at cap four would leave all larger fixed caps unresolved.

## Small orders and Singer-invariant sets

The [evidence entry point](evidence/main.py) checks three sets, retained
in [`assets/cap4_witnesses.json`](evidence/assets/cap4_witnesses.json),
each meeting every line in one to four points.

| Order | Size | $t_1$ | $t_2$ | $t_3$ | $t_4$ |
| --- | --- | --- | --- | --- | --- |
| 5 | 14 | 7 | 4 | 11 | 9 |
| 7 | 17 | 21 | 7 | 15 | 14 |
| 11 | 21 | 84 | 0 | 28 | 21 |

In PG$(2,11)$ every point of the set lies on four lines of each of the
sizes one, three and four, and there are no two-point lines. This
incidence profile does not classify the set up to projective equivalence. In PG$(2,9)$ a Baer subplane meets every line in one or four
points. So L27's bound four is attained for $q=5,7,9,11$ and, by the
reported Bruen–Fisher bound, for every power of three at least nine. Any
proof that a universal cap must
exceed four has to use other orders. These three sets were found by a
weighted local search, which is not retained. The same search found
nothing for cap four at $q=13,17$ or cap five at $q=23,\dots,37$, but it
also failed on PG$(2,64)$ at cap six and PG$(2,27)$ at cap four, where sets
are known to exist, so its failures are not evidence of nonexistence.

**Singer-invariant sets.** Identify the points of PG$(2,p)$ with
$\mathbb Z/N$ through a Singer cycle, so that the lines are the translates
$D+t$ of a planar difference set $D$. For $M\mid N$, a union of orbits of
the subgroup of order $N/M$ is a union of residue classes $r\in K$ modulo
$M$, and it meets $D+t$ in $\sum_{r\in K}\mu(r-t)$ points, where
$\mu(a)=|\{d\in D:d\equiv a\pmod M\}|$. So an invariant set with all loads
in $[1,C]$ is a covering of $\mathbb Z/M$ by translates of the single
histogram $\mu$ with multiplicities between $1$ and $C$. Because every
nonzero residue modulo $N$ is a difference of $D$ exactly once,
$\sum_a\mu(a)=p+1$ and $\sum_a\mu(a)\mu(a+d)$ equals $p+N/M$ for $d=0$ and
$N/M$ otherwise. The load mean and variance are therefore fixed exactly,
as in the identities for arbitrary sets. A depth-first search that
branches on the least-covered class, implemented in
[`util/singer.py`](evidence/util/singer.py), decides small cases exactly.

| Plane | $M$ | Cap | Classes | Points | Symmetric estimate | Result |
| --- | --- | --- | --- | --- | --- | --- |
| PG$(2,11)$ | 19 | 3 | | | excluded by L27 | none, exhaustive |
| PG$(2,11)$ | 19 | 4 | 3 | 21 | $10^{-1.0}$ | found |
| PG$(2,13)$ | 61 | 4 | | | $10^{-2.2}$ | none, exhaustive |
| PG$(2,23)$ | 79 | 5 | 9 | 63 | $10^{2.3}$ | found |
| PG$(2,29)$ | 67 | 5 | 6 | 78 | $10^{-0.5}$ | found |
| PG$(2,37)$ | 67 | 5 | | | $10^{-3.2}$ | none, exhaustive |
| PG$(2,47)$ | 61 | 5 | | | $10^{-3.5}$ | none, exhaustive |
| PG$(2,31)$ | 331 | 6 | 34 | 102 | $10^{25.9}$ | found |
| PG$(2,37)$ | 201 | 6 | 17 | 119 | $10^{11.0}$ | found |
| PG$(2,61)$ | 97 | 6 | | | $10^{0.0}$ | none, exhaustive |
| PG$(2,67)$ | 93 | 6 | | | $10^{-0.9}$ | none, exhaustive |
| PG$(2,67)$ | 147 | 6 | 7 | 217 | $10^{-0.8}$ | found |

The found sets are retained in
[`assets/singer_witnesses.json`](evidence/assets/singer_witnesses.json)
and checked by direct incidence counts over all lines, independently of
the reduction; the exhaustive cases are rerun by the checker. The
PG$(2,11)$ set has the same line types as the local-search witness above.
The symmetric estimate is the first-moment count of the next section
applied to these families: the number of class sets $K$ containing $0$,
times the probability, with the forced load mean and variance and the
loads treated as independent, that all $M$ line orbits have loads in
$[1,C]$. For the displayed cases, all estimates above $100$ accompany found
witnesses, and all estimates below $0.01$ accompany exhaustive failures
within the specified symmetric family. Intermediate estimates have mixed
outcomes. This is a description of this finite table, not a statistical
test or a prediction theorem. A failure in one symmetry family leaves
arbitrary point sets untouched. In particular the cap-five witness at
$p=29$ exceeds the heuristic unrestricted crossover $23$; that crossover
is not a nonexistence bound.

**Single orbits.** The simplest invariant sets are single orbits. The
points $i\equiv0\pmod m$ form one orbit of the subgroup of index $m$, and
it meets $D+t$ in $|\{d\in D:d\equiv-t\pmod m\}|$ points. So a single orbit
is blocking with cap $C$ exactly when every residue class modulo $m$
contains between $1$ and $C$ elements of $D$. For every prime $5\le p\le2000$
and every divisor $m\ge2$ of $N$ with $m\le p+1\le8m$, $269$ pairs in all, the
evidence entry point computes these class counts. In $68$ pairs every
class is hit, but the largest count is at most $8$ only for $(p,m)$ equal
to $(7,3)$, $(13,3)$, $(37,7)$, $(67,21)$, $(79,21)$, $(83,19)$ and
$(283,73)$, with caps $4$, $7$, $8$, $6$, $6$, $8$ and $8$. Beyond
$p=283$ every orbit that blocks has a class with at least $9$ elements of
$D$, and for $p>1500$ the least such largest count is $11$. This scan
supplies no uniform family and no asymptotic lower bound for single orbits
beyond the stated range.

## First-moment heuristic

For a set of $Kq$ points the identities fix the load mean $K$ and variance
$K$ up to lower-order terms. Treating the $N$ loads as independent, the
probability that all lie in $[1,C]$ is about $e^{-ND}$, where $D=D(K,C)$ is
the least relative entropy $D(\nu\,\|\,\mathrm{Po}(K))$ over distributions
$\nu$ on $\{1,\dots,C\}$ with mean $K$ and variance $K$. There are about
$e^{Kq\log(eq/K)}$ sets of that size. In this independent-load model the
crossover condition is $Kq\log(eq/K)\ge q^2D$. Maximizing the largest
such $q$ over the grid of $K$ values in the evidence program gives the
orders below.

| Cap | Mean load | Heuristic largest order |
| --- | --- | --- |
| 5 | 2.5 | 23 |
| 6 | 2.95 | 70 |
| 7 | 3.35 | 168 |
| 8 | 3.75 | 360 |

This is an independent-load model, not an established probability law
for point sets in a plane. It gives no bound on $c(\Pi)$. Structured
planes contradict it: PG$(2,2^r)$ has cap at most six for every $r$,
beyond the cap-six order $70$ from $q=128$ on, and PG$(2,3^r)$ has cap
four. The failure of the model does not require every successful
construction to have an algebraic description. The exact first two
moments do not justify independence, and no concentration or counting theorem here
controls the simultaneous line constraints for arbitrary sets.

## How the contributions compose

The incidence identities hold in every plane. The exact maximal-arc trap
applies to a stated class of partial sets, with fixed power-of-two cap,
and refutes the bounded-deletion repair rule requiring a new covered line
in every move from every cap-bounded state. The parity construction
covers characteristic-two Desarguesian planes only; for
fixed power-of-two caps at least eight it also gives a wholesale repair
of the maximal-arc trap using $O_C(q)$ changed points. The
conic-identity and additive-graph lemmas constrain their specified
mechanisms. The witnesses and exhaustive searches are finite facts;
the numerical load model has no mathematical warrant. The negative
curve argument is conditional on a uniform approximation theorem and
the stated source estimate. The pencil count is unconditional for
unions of lines and conics in PG$(2,q)$ with $q$ odd and has an author-recorded
proof for curves of arbitrary fixed degree in sufficiently large prime
planes; with it positive-proportion extraction suffices for the negative
answer. The covering-polynomial identities retain the blocking
hypothesis but provide no extraction theorem. None of these
qualifications is discharged by composing the results.

## Next discriminating full-solution test

The full-solution target of the
[[research/leads/projective_plane_bounded_blocking/curve_reduction|negative sketch]]
reduces, through the
[[research/leads/projective_plane_bounded_blocking/pencil_threshold|pencil count]],
to the positive-proportion extraction premise for every fixed cap: a fixed
fraction of every cap-$C$ set of at least $(1-\varepsilon)p$ points in a large
prime plane lies on a curve of fixed degree, for some fixed
$\varepsilon>0$. For arcs this follows from a theorem of Voloch reported
in a survey; for caps of three or more no proof is known to us. It
concerns arbitrary bounded-cap sets, which exist. A sufficient relative
form instead concerns residuals which block the lines missing a given
curve, with constants uniform through the extraction steps. Retaining
the captured point set as well gives a stronger relative-minimality
invariant with tangents. None of these extraction premises is proved.

The
[[research/leads/projective_plane_bounded_blocking/covering_polynomial|covering-polynomial route]]
gives a different exact interface to the covering condition, but
freeness and bounded local multiplicities alone do not force bounded
derivation degree. Reopening it requires a structural use of the
distinct linear factors and bounded fibre multiplicities.

Restricting the original approximation premise to minimal blockers
is logically equivalent to nonexistence, given the source count.
This does not exclude a proof by contradiction from their covering
and tangent properties. In every curve route the degree must remain
independent of $p$; interpolation at degree $O(\sqrt p)$ is insufficient.
