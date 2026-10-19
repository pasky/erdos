---
name: research/smooth_successor_estimates
title: Elementary estimates for the smooth-successor extraction
desc: "Independently graded elementary smooth-successor estimates: the unrestricted cutoff statement is refuted, while operative z >= 1 and E2–E5 survive under explicit classical premises; P and the catalog conclusion remain unaccepted."
problems:
- 824
created: 2026-10-15T15:28:45Z
updated: 2026-10-16T04:55:23Z
---

# Elementary estimates for the smooth-successor extraction

[[research/_index|..]]

[[research/smooth_successor_estimates/block_sieve|block_sieve]]: The weighted-dilation manuscript's block sieve (its Lemma 2.9) derived with
explicit constants for z >= 1: pointwise upper and lower polynomials with
coefficients of modulus at most one and level z^(4h+2), relative error O(e^(-h)) uniformly
in growing h, and the fixed h=2 upper bound, with the five instances the
successor extraction consumes checked against its hypotheses.

[[research/smooth_successor_estimates/candidate_mass|candidate_mass]]: The weighted-dilation manuscript's Proposition 7.1 derived for the successor
candidate: pointwise bounds, prime support in [L^20,x^delta], harmonic
masses, the P-part Euler product and tail, and the comparison
X_A of order (x/L)H_Q H_P with constants independent of the later exceptional
band j_** at least j_0; the micro-band mass comparison used by the balanced
box is included.

[[research/smooth_successor_estimates/classical_inputs|classical_inputs]]: The exact Section 2 consumption of the successor extraction and the signed
Type II estimate: the classical theorems used in standard form (prime number
theorem, Mertens, Siegel-Walfisz, the multiplicative large sieve), the
derived divisor moments and Fourier separation, and the Type I
large-sieve application written out with its parameter order.

[[research/smooth_successor_estimates/evidence/_index|evidence/]]: Frozen subjects and the independently graded elementary examination, preserving the cutoff counterexample and exact surviving classical-premise scopes.

[[research/smooth_successor_estimates/proxy_densities|proxy_densities]]: The weighted-dilation manuscript's Lemma 7.4 derived at the ranges the
successor extraction consumes: an absolute bound for the balanced prime
proxy, short-cell upper densities for x^gamma-rough integers on compact sets
with w-gamma bounded below, the cofactor bound (7.17) with w-gamma at least
2kappa, the minimum-coordinate identity (7.18), the bound (7.19) from a lower
count and the block sieve, and the mesh step that sums the bins.

[[research/smooth_successor_estimates/proxy_discrepancy|proxy_discrepancy]]: The weighted-dilation manuscript's Lemma 7.3 derived at the ranges the
successor extraction consumes: full-cell rough counts, proxies bounded by
one independently of the cell precision S, and character and Mellin
discrepancy for every interval restriction inside the ambient range, all
moduli and twists up to L^B, principal and imprimitive characters included,
once S is at least 2B+2.

***

This folder's results that are not drawn from a cited source are Plasma AI's,
with the exact scope warranted by their
[[research/smooth_successor_estimates/evidence/verify/elementary_estimates/_index|independently graded examination]].
Its **PASS** grade accepts the literal E1 refutation and the surviving
$z\ge1$ and E2–E5 deductions relative to the stated classical premises. The estimates themselves are
OpenAI's, from Sections 2 and 7 of the
[[../library/arithmetic_functions/openai_2026_weighted_dilation_graphs_smooth_shifted_primes_totient_fibers/_index|weighted-dilation manuscript]],
read in the retained library transcription; result and equation numbers refer
to that manuscript. Classical theorems are cited by their standard statements.

## Target

The [[research/smooth_successor_primes/_index|smooth-successor route]] to
[[problems/arithmetic_functions/E0824/_index|Problem 824]] derives Li and
Zhuang's Hypothesis $\mathrm A^+$, and from it $h(x)>x^{2-\varepsilon}$ for
every $\varepsilon>0$ and all large real $x$, from two source premises: the
uniform shift-cancellation estimate (P) and the elementary estimates (E). This
folder is the editable proof sketch for (E). Its target is (E) exactly as the
[[research/smooth_successor_primes/signed_type_ii|signed Type II estimate]] and
the
[[research/smooth_successor_primes/successor_prime_extraction|extraction of primes 2u-1]]
consume it, with their factor ranges, uniformity and order of choices:

- **E1**, the block sieve (Lemma 2.9) for $z\ge1$, at its five consumed scales;
- **E2**, proxy discrepancy (Lemma 7.3): the restricted differences
  $(I-B_I)\mathbf 1_K$ satisfy $(\mathrm D_B)$ for every interval restriction
  $K$, every character of modulus at most $L^B$ and every twist up to $L^B$,
  once the cell precision $S$ is large in terms of $B$, with the coefficient
  bound independent of $S$;
- **E3**, the densities (Lemma 7.4): the balanced prime proxy bound (7.16) with
  an absolute constant, the cofactor bound (7.17) on the range
  $w-\gamma\ge2\kappa+o(1)$, the identity (7.18) and the bound (7.19), and the
  mesh step that sums the bins;
- **E4**, candidate mass (Proposition 7.1) with comparison constants
  independent of the exceptional band $j_{**}\ge j_0$, and the micro-band
  comparison (7.25);
- **E5**, the other Section 2 inputs: harmonic character sums
  (Corollary 2.4), divisor moments (Lemma 2.5), Fourier separation (Lemma 2.8),
  and the large-sieve application in Type I.

## The sketch

Every item below is a written derivation by Plasma AI. The
[independent grade](evidence/verify/elementary_estimates/grade.md) accepts
the operative E1 and exact E2–E5 scopes relative to the quoted classical
premises. These elementary proofs do not use P; the weighted E3 consumer
consequence additionally assumes the Type II/P replacement. No elementary
proof involves
the sign of $2u\pm1$ beyond the size relation $x\le2u-1\le5x$.

1. **E1.** The [[research/smooth_successor_estimates/block_sieve|block sieve]]
   is derived for $z\ge1$ with coefficients in $\{-1,0,1\}$, level $z^{4h+2}$, relative
   error $c_1e^{-h}$ uniformly in growing even $h$, and the fixed $h=2$ upper
   bound, with $c_1$ and the threshold for $h$ depending only on the density
   constants. All five consumed instances are checked: cells and residue
   classes at $z=W$ with $h=2\lceil T^2\rceil$, the per-prime sieve of the
   composite subtraction, the preliminary sieve and ordinary rough integers at
   $z=x^{b_1}$ with $h=2\lfloor1/(40b_1)\rfloor$, and the balanced box at
   $h=2$. Every consumed cutoff tends to infinity. The unrestricted
   cutoff statement fails for $0<z<1$, as the block-sieve page shows;
   that range supplies no premise here.
2. **E2.** The
   [[research/smooth_successor_estimates/proxy_discrepancy|proxy discrepancy]]
   is proved for every interval $K$ inside the ambient range
   $[x^{b_1/4},x^{1-b_1/4}]$, which contains every restriction the extraction
   makes, and for every $S\ge2B+2$; the extraction's choice $S>2B+3$ is
   included. Principal characters cancel on full cells, with at most two cut
   cells; nonprincipal characters are handled for the actual tests by
   nondecreasing prime lists and Siegel–Walfisz on one last-prime interval,
   and for the proxy by residue-class counts on every subinterval, as
   absolute-error statements. The losses $L^{S+1}$ from the number of cells
   meet savings $e^{-2T^2}$ and $x^{-b_1/4+o(1)}$ that beat every fixed power
   of $L$.
3. **E3.** The [[research/smooth_successor_estimates/proxy_densities|densities]]
   are derived from short-cell prime counts with prime-number-theorem accuracy
   $L^{-S-2}$ and a cube comparison of reciprocal-prime measures with $dt/t$.
   The bound (7.17) is proved only where it is used, with $(\gamma,w)$ in the
   compact set $\gamma\ge b_1$, $w-\gamma\ge\kappa$, $w\le1$; no density at
   $w=\gamma$ is used. The identity (7.18) is the minimum-coordinate
   decomposition with factor $l/l!$, and (7.19) follows from an ordinary lower
   count by ordered prime lists and the block-sieve upper bound at $z=x^{b_1}$.
   The balanced constant in (7.16) is $3$, independent of $\kappa$ and $S$.
4. **E4.** The
   [[research/smooth_successor_estimates/candidate_mass|candidate mass]]
   is derived in a sampling model. The upper comparison uses one pure slot of
   band $0$; the lower comparison restricts a fixed prefix and the P-part and
   uses only the deterministic range of the tail, which contains the
   exceptional slot because $j_{**}\ge j_0$. Both comparison constants and the
   exponent $C_A$ are independent of $j_{**}$; only the threshold for $x$
   depends on it.
5. **E5.** The
   [[research/smooth_successor_estimates/classical_inputs|Section 2 inventory]]
   lists every consumed input with its parameters, derives the divisor moments
   and Fourier separation, and writes out the Type I large-sieve application
   with the order $D$, then the conductor split $C'$, then the Siegel–Walfisz
   exponent.

**Classical boundary.** The prime number theorem with error
$O_A(y(\log y)^{-A})$, Mertens' estimates, Chebyshev's bound, the
Siegel–Walfisz theorem and the multiplicative large sieve are used in their
standard forms, with moduli and twists explicitly bounded by fixed powers of
$L$. These are the only inputs not derived in this folder or on the pages it
links.

**Order of choices.** The reconstruction respects the extraction's order with
no feedback: the candidate geometry, the prefix, $(j',\theta)$ and $j_0$; then
$\kappa$, using the balanced constant, which depends only on the absolute bound
in (7.16), the comparison constants of E4 and absolute sieve constants; then
$b_1$, $b_*=b_1/3$, $j_{**}$ and the bin mesh; then the Type II saving, $K_0$,
$D_0$ and the discrepancy exponent $B$ supplied by (P); then the extraction's
choice $S>2B+3$ and the prime-number-theorem accuracy $A=S+2$; then
$x\to\infty$. The proxy coefficient
bound is $1$ and does not depend on $S$, so the choice of $S$ cannot change
$B$.

**Examination scope.** The examination of 2026-10-15 records
**refuted-as-stated** for E1's frozen unrestricted cutoff domain, and
**refutation-failed** for its operative $z\ge1$ range and E2–E5 relative to
the stated classical premises. The current E1 statement adds $z\ge1$, and
the block-sieve proof adds the empty-prime boundary case; these statement
and proof additions differ from the examined wording. The frozen subjects
and exact counterexample remain with the report. Its attacks include E3's
cube comparison, E4's uniformity in the later fixed exceptional slot and
E5's parameter order. The distinct whole-contract grade, examined on
2026-10-16 UTC, is **PASS** for these separate scopes. Neither the examination
nor its grade establishes P or an unconditional Problem 824 conclusion.

## Consequence for Problem 824

The [graded interface comparison](../smooth_successor_primes/evidence/verify/conditional_chain/interface_disposition.md)
matches the accepted E scopes to the signed Type II, extraction and counting
arguments. Conditional on the exact P endpoint hypothesis and the quoted
classical premises, their independently graded composition gives
$h(x)\ge h_{\rm sf}(x)>x^{2-\varepsilon}$ for each fixed $\varepsilon>0$ and
every sufficiently large real $x$, with strict $1\le a<b<x$, coprimality
and squarefreeness. P's separate
[[research/erdos_824_uniformity/shift_cancellation_reconstruction|author reconstruction]]
has no accepted independent weight: its grade remains VOID. The OpenAI
manuscript remains unrefereed, and the original classical proofs and PDF
fidelity were outside these examinations. No unconditional acceptance of
Problem 824 or conclusion about Problem 821 follows.
