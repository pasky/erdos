---
name: research/leads/odd_covering_distortion
title: Odd covers by the distortion sieve on prime-power digits
desc: |
  An exact digit-sieve calibration and large-prime interfaces for odd
  coverings. An explicit distinct family refutes the universal 138.877
  small-prime certificate. A more flexible exact-loss tail is proved,
  but a supported measure meeting it uniformly remains an open gap.
problems:
- 7
research_state: blocked
review_status: unreviewed
created: 2026-10-16T13:49:49Z
updated: 2026-10-17T08:45:47Z
---

# Odd covers by the distortion sieve on prime-power digits

[[research/leads/_index|..]]

[[research/leads/odd_covering_distortion/cube_free_obstruction|cube_free_obstruction]]: Exact bounds rule out the complete-prefix first/second-moment LPs with
consecutive digit order: initial blocks through 7 for any class-mass
bounds, through 17 for the capped Lemma 3.3 recursion, and through 11
when the weighted recursion is also allowed.

[[research/leads/odd_covering_distortion/deep_digit_obstruction|deep_digit_obstruction]]: The inflation-free floor of the cube-free test, repeated at uniform depth
D at every odd prime up to 73, exceeds the tail threshold for every
initial block through {3,...,17} once D >= 4, in three digit orders and
at every larger depth. In consecutive order the block {3,...,19} is not
excluded at any depth.

[[research/leads/odd_covering_distortion/digit_sieve|digit_sieve]]: Base-p digits turn a distinct-moduli cover into a hyperplane cover of a
digit box with prefix-shaped fixed sets. The distortion sieve then runs
digit by digit, with a (t+1)-set loss bound, a pigeonhole step, two
class-mass recursions and the tail interface at the prime 73.

[[research/leads/odd_covering_distortion/e273_calibration|e273_calibration]]: The digit-coordinate distortion sieve proves, with an exact certificate,
that the 149 moduli p-1 with 5 <= p <= 877 cover the integers for no
choice of residues: the 7-smooth block loses at most 115/126 and every
later digit loses nothing.

[[research/leads/odd_covering_distortion/evidence/_index|evidence/]]: Exact rational checks for the lead: the Problem 273 calibration
certificate, a cross-check of the sieve recursions against actual
distorted measures, cube-free LP failure bounds with exact logarithmic
weak-duality margins, the depth-four floor in three digit orders, and a
realizable support-concentration counterexample to the universal tail
threshold, and an exact-loss tail certificate from uniform density 1/4.

[[research/leads/odd_covering_distortion/exact_loss_tail|exact_loss_tail]]: A convex-order bound for weighted indicator sums, applied coordinate by
coordinate, bounds each exact large-prime loss of the source's tail by an
aligned model with independent dominated agreement depths and the worst
small-prime system. An outward rational certificate accepts any uniform
surviving density at least 1/4 in the reduced small-prime box through 73,
including a configuration that defeats the 138.877 moment interface.

[[research/leads/odd_covering_distortion/point_kernel|point_kernel]]: The source's tail needs at each large prime only the small-prime
projections of the classes present. Bounding their pair sums directly
replaces the class-mass constant by an actual-system constant. Its
universal worst-system bound dominates the point-kernel value of the
small-prime measure. The demand for a supported measure with this bound
at most 138.877 is false: a realizable residue configuration forces a
value above 152.14. The actual-system tail implication remains valid.

[[research/leads/odd_covering_distortion/sketch|sketch]]: Canonical conditional route for distinct odd coverings. The universal
138.877 small-prime certificate is false by an explicit concentration
example. The exact-loss tail remains valid; the open obligation is a
supported measure satisfying its system-functional bounds at every
small-prime depth and residue assignment.

[[research/leads/odd_covering_distortion/support_concentration|support_concentration]]: A valuation form of Harrington's repeated-3 construction gives a distinct
odd family whose survivors have one fixed first 3-digit. At depth 16
through 73, every supported measure has point-kernel value above 152.14.
Thus the universal 138.877 small-prime certificate is false, independently
of its digit order, class-mass recursion, or initial block.

***

This lead's results that are not drawn from a cited source are Plasma AI's,
credited to Plasma AI. All of them are author-recorded at tier 0, and no
independent review has examined the lead.

## Target and route

The target is the negative answer to
[[problems/covering_systems/E0007/_index|Problem 7]]: no finite family of
congruence classes with pairwise distinct odd moduli greater than one covers
the integers. The problem page's current assessment records the problem as
open, and this lead does not change that.

The route extends the square-free proof of Balister, Bollobás, Morris,
Sahasrabudhe and Tiba along each $p$-adic tree. Base-$p$ digits make every
congruence class a hyperplane whose fixed coordinates form an initial segment
of each prime's digits, and the distortion sieve then runs digit by digit. The
large primes are handled by the source's tail, so the whole difficulty lies in
the odd primes up to $73$ with arbitrary exponents.

## Pages

The [[research/leads/odd_covering_distortion/sketch|proof sketch]] is the
canonical account of the route, with its held steps, its gap and its failure
account. The [[research/leads/odd_covering_distortion/digit_sieve|digit
page]] derives the digit form of the sieve: the reduction, a loss bound over
$(t+1)$-sets of completed classes with a pigeonhole case, two class-mass
recursions, the prefix pair count and the tail interface.

The [[research/leads/odd_covering_distortion/e273_calibration|calibration
page]] proves with an exact certificate that the $149$ moduli $p-1$ with
$5\le p\le877$ cannot cover the integers, a finite statement about
[[problems/covering_systems/E0273/_index|Problem 273]]. The
[[research/leads/odd_covering_distortion/cube_free_obstruction|cube-free
obstruction]] proves that specified moment LPs cannot certify the cube-free
case of Problem 7. They keep the full prefix inventory, charge all single
and pair terms without using residue compatibility, and process each
prime's two digits consecutively in increasing prime order. Initial blocks
through $7$ are excluded for any valid class-mass bounds, and those through
$17$ for the capped source recursion. The
[[research/leads/odd_covering_distortion/deep_digit_obstruction|depth-four
obstruction]] repeats the inflation-free floor at every uniform depth and in
three digit orders, and excludes every initial block through $17$ for any
valid class-mass bounds once the depth is at least four.

The [[research/leads/odd_covering_distortion/point_kernel|point-kernel
page]] derives the tail with the pair sums of the classes actually present,
with the point kernel giving a lower bound for the universal system constant.
The [[research/leads/odd_covering_distortion/support_concentration|support
concentration construction]] gives an actual distinct odd family whose
survivors have one fixed first 3-digit. Every supported measure then has
system constant above $152.14$, refuting both the universal $138.877$ demand
of Step 3* and the stronger sieve certificate of Step 3.

The [[research/leads/odd_covering_distortion/exact_loss_tail|exact-loss tail]]
proves a convex-order bound for exact large-prime losses, in terms of the
worst small-prime system. Its Corollary D allows a different interface and is
not refuted by the concentration argument. Corollary E and its outward
rational certificate accept uniform surviving density at least $1/4$, which
handles that example. An explicit extension has density below $1/4$, so this
sufficient condition is not a universal substitute for the missing measure.

## Why the lead is blocked

The universal $138.877$ certificate is false with its stated definitions.
A different initial block, digit order, or class-mass recursion cannot fix it.
The cube-free and depth-four moment-model exclusions retain their narrower
scope, but no longer supply the decisive failure account for that threshold.

The remaining route asks for a measure on the uncovered set of every family
of $73$-smooth classes, at arbitrary depth, satisfying Corollary D of the
exact-loss tail. That condition needs bounds on the system count's upper tail
under a supported measure. Its universal existence is unknown and includes the
nonemptiness of the $73$-smooth uncovered set itself. The full sketch states
its quantifiers and how it would compose to a negative answer to Problem 7.

## Evidence

The [evidence program](evidence/main.py) checks the calibration certificate,
the pigeonhole steps, the implementation of the recursions against actual
distorted measures on small domains, the cube-free bounds and the depth-four
bounds, and the explicit concentration construction and kernel bound, all in
exact rational arithmetic. It also certifies the exact-loss tail from density
$1/4$ and its handoff to the source's termination theorem. The checks take a
few seconds:

```sh
uv run --no-sync python wiki/research/leads/odd_covering_distortion/evidence/main.py
```
