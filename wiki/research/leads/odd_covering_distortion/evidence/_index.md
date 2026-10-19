---
name: research/leads/odd_covering_distortion/evidence
desc: |
  Exact rational checks for the lead: the Problem 273 calibration
  certificate, a cross-check of the sieve recursions against actual
  distorted measures, cube-free LP failure bounds with exact logarithmic
  weak-duality margins, the depth-four floor in three digit orders, and a
  realizable support-concentration counterexample to the universal tail
  threshold, and an exact-loss tail certificate from uniform density 1/4.
tags: []
sources: []
created: 2026-10-16T13:49:49Z
updated: 2026-10-16T13:49:49Z
---

# research/leads/odd_covering_distortion/evidence

[[research/leads/odd_covering_distortion/_index|..]]

***

The [entry point](main.py) runs seven parts in exact rational arithmetic, with
the Python standard library and the repository checker, in a few seconds.
Part 1 rebuilds the $149$ moduli $p-1$ with $5\le p\le877$, reads the digit
order and thresholds from the [schedule asset](assets/e273_schedule.json), and
recomputes the certified block losses $115/126$ (Lemma 3.3 class masses) and
$538793/604800$ (weighted class masses). It also checks that every later digit
completes fewer moduli than its size, and that a control without distortion
returns the union bound, which exceeds one. Part 2 compares the implemented
loss and class-mass bounds with actual distorted measures on two small domains
for four residue choices each. Part 3 recomputes the inflation-free floor
$\kappa_0/\mu_0$ of the cube-free test, including rational enclosures for
the four excluded initial blocks and the unexcluded four-prime floor.
Part 4 checks the six rational weak-duality margins and integer lower
bounds in the obstruction page's table, with the capped source recursion
and with the weighted recursion also allowed. Part 5 recomputes the same
floor at uniform depth four in three digit orders for the seven initial
blocks through $17$. It also checks the exclusions of the smaller blocks at
depths two and three, the depth-three case of the block through $17$, which
is not excluded, a bound valid at every depth showing that the
block through $19$ is never excluded in the consecutive order, and the
infinite-depth value of $\kappa_0$ with its ratio to the threshold. Part 6
reconstructs a repeated-3 covering by a finite valuation partition, checks
its distinct-modulus partial family and explicit surviving point, and verifies
the rational kernel lower bound above $152.14$ for all supported measures.
A deleted-class negative control rejects a broken partition certificate.
An explicit 16-class extension retains a surviving point while reducing its
uniform surviving density below $1/4$. Part 7 uses lower atom probabilities
and outward-rounded full moments to certify the exact-loss tail through
$p_{2262}=19997$ from any uniform density at least $1/4$. Every omitted atom
is charged through its first moment. The resulting $f_{2262}<94000$ is
below a rationally certified lower bound $101000$ for the source's
termination criterion. The same check with an adapted product measure
handles the 16-class extension, giving $f_{2262}<21000$ after conditioning.

The schedule asset records the digit order of the seven-smooth block and the
thresholds $t$ for both recursions; it was found by a local search over orders
and thresholds that is not part of the evidence. The cube-free checks bound
entire families of fixed-schedule LPs through their proved relaxations;
they do not solve a configuration LP or certify a numerical optimum.
The $400$ cells per prime cover every real distortion in $[0,1)$, using
monotone lower bounds on each cell, and logarithms have rational
remainder bounds. The program checks finite computations only. The
reductions that make them proofs are on the
[[research/leads/odd_covering_distortion/digit_sieve|digit page]], the
[[research/leads/odd_covering_distortion/e273_calibration|calibration page]],
the [[research/leads/odd_covering_distortion/cube_free_obstruction|obstruction
page]] and the
[[research/leads/odd_covering_distortion/deep_digit_obstruction|depth-four
page]] and the
[[research/leads/odd_covering_distortion/support_concentration|support
concentration page]], and on the
[[research/leads/odd_covering_distortion/exact_loss_tail|exact-loss page]].

All work is author-recorded. The small-domain runs check the implementation,
not the universal digit-sieve lemmas. The cube-free results concern the
full prefix inventory and full first/second-moment sums, in the stated
digit order; the depth-four checks concern the same model at uniform depth
four in three orders. Part 6 supplies a realizable configuration for which
no measure on the uncovered set meets the universal $138.877$ system bound,
including measures obtained by conditioning a sieve certificate. It does not
refute the exact-loss tail condition, prove an odd cover, or exclude all odd
covers. The huge period is covered by the proved recursive partition, not
pointwise enumeration. Part 7 is a sufficient condition with an explicit
density hypothesis, not a construction of a measure for every small-prime
configuration. Its geometric-depth domination covers arbitrary finite
exponents; the source's termination theorem covers the remaining primes.

```sh
uv run --no-sync python wiki/research/leads/odd_covering_distortion/evidence/main.py
```
