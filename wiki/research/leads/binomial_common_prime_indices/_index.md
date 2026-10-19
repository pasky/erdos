---
name: research/leads/binomial_common_prime_indices
title: Common primes of two binomial coefficients, index by index
desc: |
  Computer-assisted, author-recorded proofs that Problem 699 has no bad
  triple at i = 7 or at any i >= 9, building on van Doorn and Rocca's
  unreviewed manuscripts. At i = 3 a bad triple needs n > 10^19,
  v_2(n) >= 49 and three distinct primes dividing (n-2)/2, and rational abc
  gives finiteness. No effective row bound is known at i = 4, 5, 6 or 8.
problems: [699]
research_state: blocked
review_status: unreviewed
created: 2026-10-18T03:08:34Z
updated: 2026-10-18T03:08:34Z
---

# Common primes of two binomial coefficients, index by index

[[research/leads/_index|..]]

***

This lead's results that are not drawn from a cited source are Plasma AI's,
credited to Plasma AI. All of them are author-recorded at tier 0. No
independent review of the lead or of any of its results is retained, and no
claim of novelty is made for them.

## Target and route

The target is the affirmative answer to
[[problems/factorials_binomials/E0699/_index|Problem 699]]: for every
$1\le i<j\le n/2$, some prime $p\ge i$ divides both $\binom ni$ and
$\binom nj$. A triple is *bad* when no such prime exists. The threshold
includes $p=i$ when $i$ is prime; the second manuscript cited below works
with the strict threshold $p>i$. The problem page's current assessment
records the problem as open, and this lead does not change that.

The route excludes bad triples one index at a time. Write
$\binom ni=U_i(n)V_i(n)$, where $U_i(n)$ is supported on the primes below
$i$ and $V_i(n)$ on the primes at least $i$. For a bad triple, van Doorn and
Rocca's localization places each prime power of $V_i(n)$ at a point of the
triangle $\Delta_i=\{(r,s):r,s\ge0,\ r+s<i\}$, so an integer polynomial $F$
vanishing to order $m$ on $\Delta_i$ gives $V_i(n)^m\mid F(j,n-j)$. Their
finiteness argument then uses an ineffective $S$-part theorem. The lead
replaces that input. For each prime $p<i$, choose $r_p$ maximizing
$v_p(n-r_p)$ and write $n-r_p=P_pu_p$ with $P_p$ a power of $p$. Padé
approximation gives effective alternatives forcing some cofactors $u_p$ to be
large. Polynomials with different multiplicities on different rows of
$\Delta_i$ turn these alternatives into a strict exponent gain and a
numerical height above which no bad triple exists. Interval certificates and
exact binomial gcd checks then exclude every row below that height. Large
indices use an orbit polynomial whose discriminant bounds the gcd of the two
coefficients from below; comparing it with a small-prime upper bound confines
a bad row, and a prime in $(n-i,n]$ then divides both coefficients.

## Results

1. **No bad triple at $i=7$ or at any $i\ge9$.** For every admissible triple
   with $i=7$ or $i\ge9$, some prime $p\ge i$ divides both coefficients. At
   seven the analytic estimates hold for $n-6\ge10^{100000000}$ and the
   finite exclusion reaches $n\le10^{100000001}$; at nine they hold for
   $n-8\ge10^{241547627}$ and the finite exclusion reaches
   $n\le10^{241547629}$. The proof uses van Doorn and Rocca's localization,
   fat-point divisor, orbit polynomial and discriminant, and for $i\ge906$
   Lemma 1 of their second manuscript.
2. **Restrictions at $i=3$.** Unconditionally, a bad triple with $i=3$ has
   $n=2^hu$ with $u$ odd and $3u^3<2^h$, $4\le j<n/2$, $n>10^{19}$,
   $v_2(n)\ge49$, and at least three distinct prime factors of $(n-2)/2$.
   The bounds on $n$ and $v_2(n)$ come from an exact search of 127,892 rows
   with certified primality; the other restrictions are uniform proofs.
   Neither nonexistence nor finiteness at $i=3$ is proved.
3. **Finiteness at $i=3$ under abc.** Assuming the abc conjecture over
   $\mathbb Q$, only finitely many bad triples have $i=3$. A single exponent
   $1+\epsilon=10/9$ suffices, and a valid constant $K\ge1$ for that exponent
   gives $n<10^{263}K^{69}$ for every bad row. With van Doorn and Rocca's
   fixed-index finiteness at $i=4,5,6,8$, rational abc therefore makes the
   set of all bad triples finite. This does not show that the set is empty,
   and abc supplies no value of $K$.

Van Doorn and Rocca's manuscripts settle $i=1$ and $i=2$, exclude every
$i\ge1476$, and prove finiteness for each fixed $i\ge4$ without an effective
bound. These are on their
[[problems/factorials_binomials/E0699/claims/2026_07_25_van_doorn_rocca|pending claim page]],
not results of this lead. Together with item 1, they leave every possible
counterexample with $i\in\{3,4,5,6,8\}$.

## Pages

The [[research/erdos_699/_index|Problem 699 research guide]] is the reading
route and tabulates what is known at each index. The
[[research/erdos_699/proofs/_index|proof guide]] explains the five steps of
the argument and names the proof of each completed index in a table that
partitions them. The
[[research/erdos_699/proofs/details/cutoff_9|cutoff-nine theorem]] states
item 1, joining the
[[research/erdos_699/proofs/details/index_7_complete|complete proof at seven]]
and the
[[research/erdos_699/proofs/details/index_9_complete|complete proof at nine]]
to the earlier cutoff at ten. The
[[research/erdos_699/proofs/details/cutoff_and_cubic|discriminant and interval proof]]
excludes $i=29$ and $35\le i\le905$ with 399,713 certified intervals and
takes $i\ge906$ from the calculation retained beside the
[[../library/factorials_binomials/van_doorn_rocca_2026_binomial_coefficients_sharing_large_prime_divisor/_index|second manuscript's card]].
It also gives the first cubic reduction, and proves that a nonzero
polynomial vanishing to order $m$ at every point of $\Delta_3$ has degree at
least $9m/4$.

The [[research/erdos_699/remaining/_index|remaining-indices guide]] records
what is known at $i=4,5,6,8$ and the precise gaps. The
[[research/erdos_699/remaining/index_three|index-three guide]] collects the
case $i=3$. Within it, the
[[research/erdos_699/remaining/details/cubic_followup|cubic follow-up]]
proves the bounds $n>10^{19}$ and $v_2(n)\ge49$, the
[[research/erdos_699/remaining/details/cubic_residue_groups|residue-group theorem]]
proves the three prime factors of $(n-2)/2$, and the
[[research/erdos_699/remaining/details/cubic_abc|conditional cubic argument]]
proves item 3. The [[research/erdos_699/methods/_index|methods guide]]
states the divisibility, approximation, nonvanishing and finite-range tools,
and the [[research/erdos_699/computations/_index|computation guide]] gives
the entry points of the retained certificates. Superseded bounds and
approaches that did not finish are kept in the guide's
[[research/erdos_699/archive/_index|archive]].

## Why the lead is blocked

At $i=4,5,6,8$ only finiteness is known, from van Doorn and Rocca's
ineffective $S$-part argument; the available effective version saves too
little there. Numerical improvements to the existing cofactor bounds are not
enough by themselves. At specified cofactor profiles at five, six and
eight, exact all-degree bounds show that polynomials with the given row
multiplicities cannot give the strict degree saving the divisor argument
needs. A new argument must supply stronger cofactor inequalities,
restrictions from the actual column, or a relation putting all remaining bad
pairs on finitely many algebraic curves, where an effective Runge criterion
would apply.

At $i=3$ even global finiteness is open. The small-prime part satisfies
$U_3(n)\le n$, and no uniform smaller power of $n$ bounds it, since
$U_3(2^h)=2^h$. The least degree-to-multiplicity ratio on $\Delta_3$ is
$9/4$, while the manuscript's exponent argument would need a ratio below $2$.
The missing step is an upper bound on $v_2(n)$, or another argument
excluding the family as $v_2(n)$ grows. Finiteness is proved on every fixed
algebraic curve, and effective finiteness is proved when $j$ or $n-2j$ is at
most a fixed multiple of $n^{3/4}$ or when one residue group of $(n-2)/2$ is
bounded; none of these gives global finiteness.

## Evidence

The proofs are computer-assisted, by exact integer and rational
certificates and directed analytic estimates; no Lean formalization is
claimed. The combined checkers at seven and nine verify the numerical source
bounds, every retained initial interval inequality, exact polynomial
coverage, the joint interval bindings and the overlap with the finite range.
They reuse the retained interpolation ranks. By default they then regenerate
every joint Padé witness sequence, 9,811,438 witnesses at seven and
11,599,987 at nine, in roughly an hour of processor time per index; the
`--quick` option skips that regeneration and says so. With the pinned
dependencies of the [[research/erdos_699/evidence/_index|evidence folder]]
installed in the repository's `.venv/`, run from the repository root:

```sh
.venv/bin/python wiki/research/erdos_699/computations/erdos_699_index_7_complete.py
.venv/bin/python wiki/research/erdos_699/computations/erdos_699_index_9_complete.py
```

The large-index interval calculation and the cubic searches have their own
entry points, named on the pages above. These checks are author evidence and
confer no tier.

## Sources

The manuscripts are Wouter van Doorn and Stefano Rocca's
[[../library/factorials_binomials/van_doorn_rocca_2026_partial_progress_erdos_problem_699/_index|Partial Progress on Erdős Problem #699]]
and
[[../library/factorials_binomials/van_doorn_rocca_2026_binomial_coefficients_sharing_large_prime_divisor/_index|Binomial coefficients sharing a large prime divisor]],
both unpublished. The first says that its specific arguments follow L.
Price's Overleaf project *Common Prime Divisor of Binomial Coefficients*
(2026). Their proofs have not been reviewed here: both cards stand at
author-recorded reading, and their proofs count as not verified. The cutoff
$i\ge906$ is the repository calculation of the second card's
[[../library/factorials_binomials/van_doorn_rocca_2026_binomial_coefficients_sharing_large_prime_divisor/evidence/_index|evidence leg]],
which supplies the cutoff $i\ge1000$ that the manuscript states without its
calculation and lowers it to $906$. The cofactor estimates build on the Padé
construction of Bennett, Filaseta and Trifonov, *On the factorization of
consecutive integers* (2009), read in its 2007 author preprint. The proofs
also use explicit prime estimates and the exhaustive prime-gap computation of
Oliveira e Silva, Herzog and Pardi (Math. Comp. 83 (2014)), as cited on the
pages that use them.
