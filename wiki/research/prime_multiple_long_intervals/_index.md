---
name: research/prime_multiple_long_intervals
title: Prime-multiple blocks longer than three times the largest prime
desc: Exact third-layer counts obstruct separated and full Cartesian prime grids, while nonrectangular cell sets give a uniform u^0.56213 upper bound and an arithmetic Kakeya comparison for every length ratio from three up to four.
created: 2026-10-15T15:58:15Z
updated: 2026-10-15T15:58:15Z
---

# Prime-multiple blocks longer than three times the largest prime

[[research/_index|..]]

***

**Target and conventions.** For
[[problems/primes/E1143/_index|Problem 1143]], let $G_\alpha(u)$ minimize
once-counted prime-multiple locations over all sets of $u$ distinct
primes with largest member $P$ and all blocks of
$\lfloor\alpha P\rfloor$ consecutive positive integers. This account
studies $3\le\alpha<4$. It does not determine the minimum for a
prescribed prime set, and the catalog problem remains open.

The three-position test has two different outcomes. Separated repeated
prime grids incur a sharp linear cost. Even without separated rows,
full Cartesian grids retaining their row and column locations incur at
least a constant times $u^{2/3}$. Nonrectangular cell sets avoid these
obstructions: an explicit rational measure on Lemm's seven-point
configuration gives $G_\alpha(u)\le C u^{0.56213}$ throughout
$3\le\alpha<4$, with $C$ absolute. All project arguments below are
recorded at tier 0, without independent review.

**Source boundaries.** The author-recorded
[[theory/number_theory/L37_prime_multiple_block_extremum/_index|L37 gives
G_alpha(u)=ceil(2 sqrt(u)) for 2<alpha<3]], extending the
Erdős--Selfridge square construction; the
[[research/prime_multiple_interval_extrema/_index|short-block account]]
keeps its scope explicit. For longer intervals,
[[../library/integer_sequences/erdos_1986_problems_number_theory/theorem_p62|Erdős's
p. 62 theorem]] gives $(6u)^{1/2}$ for square $u$ when the real interval
length is at least $3P$. A block of $K\ge3P+1$ integers meets that
printed length convention; this quotation is not used to settle the
endpoint $K=3P$.
[[../library/primes/ruzsa_1995_few_multiples_many_primes/theorem|Ruzsa's
1995 theorem]] gives an upper bound $O_\alpha((u\log u)^{2/3})$ in the
present range. His constructed block has at least $\alpha P$ integers,
so taking a subblock gives the convention used here.
[[../library/primes/green_2017_arithmetic_kakeya_conjecture_katz_tao/proposition_4_1|Green
and Ruzsa's Proposition 4.1]] compares the integer-ratio minimum with
arithmetic Kakeya sets. None of these results gives a formula for each
prescribed prime set.

## The exact three-layer model

Index primes by integer cells $(x,y)$ with distinct differences $y-x$,
the prime of a cell being $q+y-x$. Choose $z\equiv-x$ modulo each
prime. Its multiples are

$$
z+tq+(1-t)x+ty\qquad(t\in\mathbb Z).
$$

The three central layers are $z+x$, $z+q+y$ and $z+2q+2y-x$.
[[theory/number_theory/L198_three_layer_prime_blocks/_index|L198 proves]]
that, if $|x|,|y|\le\omega$ and
$(4-\alpha)q\ge16\omega+1$, a positive block of exactly
$\lfloor\alpha P\rfloor$ integers contains precisely those layers.
Their disjointness makes its count exactly $|X|+|Y|+|W|$, where
$X,Y,W$ are the value sets of $x,y,2y-x$. Multiple divisibility within a
layer is counted once.

L37's grid $q+a_i+b_j$ corresponds to $x=-a_i$, $y=b_j$.
The old two positions are the row $z-a_i$ and column $z+q+b_j$.
A third consecutive multiple is forced once the block has $3P$
integers. The right extension adds $z+2q+a_i+2b_j$; the left extension
adds $z-q-2a_i-b_j$. Counting only the old row and column positions
therefore misses an entire forced set.

## Separated grids have a sharp linear cost

In the repeated groups used in L37, $a_{i+1}-a_i>b_s$. Under the narrow
condition $2a_r+3b_s<q$, and with $K=\lfloor\alpha P\rfloor<4q$,
[[theory/number_theory/L199_separated_grid_third_layer/_index|L199 gives
the exact minimum over blocks retaining the row and column positions]]:

$$
r_S+s_S+|T_S|,\qquad T_S=\{a_i+2b_j:(i,j)\in S\}.
$$

Here $S$ is any selected set of grid cells and $r_S,s_S$ count its
occupied rows and columns. Every value in $T_S$ has at most two cells,
so $|T_S|\ge\lceil|S|/2\rceil$. The canonical positive translate of
$[z-q+1,z-q+K]$ attains the minimum. Moving it while retaining the core
cannot help: every missing following location forces a distinct
preceding location into the block. L199 also proves a linear lower
bound for all blocks in the specified window around $z$.

For a full $r\times s$ separated grid,

$$
|T_S|\ge rs-(r-1)\lfloor s/2\rfloor.
$$

This is sharp for every $r,s$ and every $3\le\alpha<4$. Columns
$0,1,\ldots,s-1$ and rows spaced $2\lceil s/2\rceil$ apart attain the
projection bound; the prime-realization theorem below realizes a dilate
of this pattern with all the endpoint hypotheses. Its core-retaining
minimum is exactly $r+s+rs-(r-1)\lfloor s/2\rfloor$.

This conclusion fixes the CRT placement and the stated block families.
Distant blocks for the same primes can realize other residue patterns;
no lower bound for all such blocks follows.

## Full Cartesian grids also have an obstruction

Dropping row separation does not make full rectangles competitive.
For finite sets $A,B\subset\mathbb Z$ with unique sums $a+b$, put
$r=|A|$, $s=|B|$. Then
[[theory/number_theory/L204_cartesian_prime_grid_obstruction/_index|L204 proves]]

$$
|A+2\cdot B|\ge s\sqrt r,\qquad
|2\cdot A+B|\ge r\sqrt s.
$$

The dot denotes dilation. To see why sumset growth applies, take a subset
$X\subseteq2\cdot B$ with minimal growth under adding $A$.
Petridis's lemma bounds $|X+A+A|$ by
$(|A+2\cdot B|/s)^2|X|$, while the unique sums force its subset
$X+2\cdot A$ to have $r|X|$ elements. The complete proof is in L204.

For a narrow full grid of $u=rs$ distinct primes, a median cut chooses a
large subrectangle whose following multiples are all present, or whose
preceding multiples are all present. Thus every block with $K\ge3P$
retaining all row and column locations has count at least

$$
r+s+\frac{\min(s\sqrt r,r\sqrt s)}{2\sqrt2}
\ \ge\ \frac{3}{2^{5/3}}u^{2/3}.
$$

This includes mixtures of the preceding and following layers. It rules
out full Cartesian grids as an asymptotically optimal family in this
range. It does not assert that $2/3$ is the optimal exponent even within
that family.

Deleting $v$ cells removes at most $v$ values from a projection. Thus
for a subset $S\subseteq A\times B$ with $u=rs-v$ cells, its canonical
following layer still has at least $s\sqrt r-v$ locations. In
particular, nearly full balanced rectangles with $r,s\asymp\sqrt u$
and $v=O(\sqrt u)$ pay order $u^{3/4}$ in that layer. The argument
allows sparse, nonrectangular selections to behave differently.

A useful comparison family is the base-six product of rows
$\{0,2,4\}$ and columns $\{0,1\}$ in cell coordinates. It has $6^n$
cells with distinct differences and at most $4^n$ third-projection
values, giving exponent $\log4/\log6\approx0.774$ after prime
realization. The universal rectangular lower exponent and this explicit
upper exponent do not match; neither approaches the nonrectangular
bound below.

## Prime realization and arithmetic Kakeya

The exact prime-set comparison holds across the whole half-open range.
Define $F'_3(u)$ using finite integer sets containing three-term
progressions with $u$ distinct positive common differences. Then
[[theory/number_theory/L202_prime_realization_three_projections/_index|L202 proves]]

$$
F'_3(u)\le G_\alpha(u)\le3F'_3(u)
\qquad(3\le\alpha<4,\ u\ge1).
$$

For the lower bound choose three consecutive multiples of every prime.
For the upper bound turn a progression $a,a+d,a+2d$ into the cell
$(a,a+d)$. All three projections lie in the progression-containing set.
Every finite cell set can be realized without discarding any cell: use
a sufficiently late segment of a much longer prime progression, with
its common difference as the cell dilation. Green--Tao's ordinary
arbitrarily-long-progression theorem supplies it. The construction makes
$q$ large enough relative to every dilated coordinate for L198; no
additional short-interval progression theorem is needed.

The source statement used is Theorem 1.1, p. 2, of Green and Tao,
[arXiv:math/0404188v6](https://arxiv.org/abs/math/0404188v6), checked on
the page image on 2026-10-15. Its proof is an external premise. The deduction
extends Green--Ruzsa Proposition 4.1's construction to noninteger
ratios, not a new Green--Tao theorem. It also shows
$G_3(u)\le G_\alpha(u)\le3G_3(u)$, with constants uniform below four.

## Nonrectangular type classes and the remaining exponent

For a cell set $S$ let
$N(S)=\max(|X(S)|,|Y(S)|,|W(S)|)$ and let

$$
\beta=\sup_S\frac{\log|S|}{\log N(S)},
$$

where $|S|\ge2$ and $y-x$ is injective. The author-recorded
[[theory/number_theory/L200_long_block_sums_differences_exponent/_index|L200]]
proves

$$
G_\alpha(u)\ge u^{1/\beta}\quad(\alpha\ge3),\qquad
\lim_{u\to\infty}\frac{\log G_\alpha(u)}{\log u}=\frac1\beta
\quad(3\le\alpha<4).
$$

Its proof uses tensor powers and prime-number-theorem averaging, which
loses only a logarithmic factor. The change of variables
$(a,b)=((2y-x)/2,x/2)$ identifies $\beta$ with the sums--differences
constant for input slopes $0,1,\infty$ and output slope $-1$.
Determining this constant is the missing independent progression
estimate, not a consequence of the prime construction.

The cells $(0,1),(2,1),(2,2)$ yield a first explicit improvement over
rectangles. Words using each cell exactly $m$ times have
$(3m)!/(m!)^3$ distinct differences and exactly $\binom{3m}{m}$ values
in each projection. Hence
[[theory/number_theory/L201_type_class_long_block_bound/_index|L201 gives]]

$$
G_\alpha(u)\le C u^\theta(\log u)^{\theta-1/2},\qquad
\theta=\frac{\log(27/4)}{\log27}=0.57938\ldots.
$$

The exponent comes from Ruzsa's three-point example and
[[../library/additive_combinatorics/lemm_2015_new_counterexamples_sums_differences/proposition_1_1|the entropy-to-type-class method recorded by Lemm]].
L201 also retains a proof using only the
prime number theorem, with bound $O_\alpha(u^\theta(\log u)^2)$.
The complete type classes themselves have a residual logarithmic factor;
realizing all their differences as primes does not prove $O(u^\theta)$.

Using the seven-point configuration from
[[../library/additive_combinatorics/lemm_2015_new_counterexamples_sums_differences/theorem_2_1|Lemm's Theorem 2.1]] instead,
[[theory/number_theory/L203_rational_entropy_prime_block_bound/_index|L203 gives]]

$$
G_\alpha(u)\le C u^{56213/100000},
\qquad 3\le\alpha<4,
$$

with $C$ absolute. Its rational measure has joint entropy $H$ and largest
projection entropy $h$ with $h/H<0.56213$. Exact multinomial counts,
not finite searches, give the unbounded family. The numerical inequality
is certified by rational logarithm enclosures. Lemm retains authorship
of the configuration; this is a rigorous prime-block application, with
no claim of a new sums--differences record.

For comparison, Katz and Tao, *Bounds on arithmetic projections, and
applications to the Kakeya conjecture*, Math. Res. Lett. 6 (1999),
625--630, [arXiv:math/9906097v3](https://arxiv.org/abs/math/9906097v3),
Theorem 1.1, bounds the number of differences by $N^{11/6}$ when the
three input projections have size at most $N$. The statement and its
hypotheses were checked on the p. 1 image on 2026-10-15; the source proof
is not reconstructed here. Applied to the cell change of variables it gives
$\beta\le11/6$,
and therefore the known lower bound $G_\alpha(u)\ge u^{6/11}$ for every
$\alpha\ge3$. Together with L203,

$$
u^{6/11}\le G_\alpha(u)\le C u^{0.56213}
\qquad(3\le\alpha<4).
$$

The library's Theorem 2.1 page separates Lemm's claimed optimized ratio
from the weaker ratio of the printed rounded probabilities. Its
Proposition 1.1 page also records the limiting qualification in the
entropy-to-set passage. L203 uses its own exact rational witness and a
strict entropy margin, so neither qualification is silently removed.
The three-slope interval is also
recorded in Section 1.1 of Tao,
[arXiv:2511.15135v1](https://arxiv.org/abs/2511.15135v1). Only that
introductory comparison was used; neither this account nor its narrow
literature search establishes a new record.

## Sketch, standing and precise gap

The settled author-recorded chain is L198 for exact locations, L202 for
full prime realization, and L201 or L203 for the cell construction. L199
settles the separated-grid optimum, using L202 only for its prime
sharpness examples. L204 rules out every full Cartesian grid retaining
its core at the scale achieved by L203. L200 identifies the unrestricted
asymptotic obstruction as the sums--differences constant. All these
project deductions are credited to Plasma AI at tier 0. L37 is contextual
and is not consumed by their proofs.

The remaining gap is an estimate for arbitrary nonrectangular cell
sets: either a configuration with a better projection-to-joint entropy
ratio, or a stronger universal three-projection inequality. The exact
value of $\beta$, the exact finite function $F'_3(u)$, and any sharper
comparison than the factor three above are not settled. Improving the
prime realization alone cannot determine the exponent, because every
finite cell pattern already has such a realization. An argument for
prescribed primes would need additional information about that prime set.
Ratios $\alpha\ge4$ require further layers and are outside this
three-position argument.

The
[[theory/number_theory/L198_three_layer_prime_blocks/evidence/_index|L198
finite checks]] test actual positive blocks and once-only counting;
one contains 220 multiples of 302 primes at $\alpha=3$.
[[theory/number_theory/L199_separated_grid_third_layer/evidence/_index|L199's
checks]] enumerate its two block families for small prime grids.
[[theory/number_theory/L203_rational_entropy_prime_block_bound/evidence/_index|L203's
certificate]] checks the exact entropy witness. The universal assertions
rest on their written proofs and stated source premises. None of these
author checks supplies independent acceptance or changes the general
problem's standing.
