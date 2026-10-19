---
name: theory/irrationality
desc: |
  Project claims about arithmetic series and mechanisms relevant to their
  irrationality, with each claim's exact scope and standing recorded locally.
tags: []
sources: []
created: 2026-09-17T06:05:14Z
updated: 2026-10-15T16:35:43Z
---

# theory/irrationality

[[theory/_index|..]]

[[theory/irrationality/L16_totient_kernel_separation/_index|L16_totient_kernel_separation/]]: Every nonzero real absolutely summable kernel of shifted phi(n)/n has
positive absolute limsup on each fixed arithmetic progression; a fresh
prime gives an explicit pair of separating refinements.

[[theory/irrationality/L189_lcm_series_cone_no_product/_index|L189_lcm_series_cone_no_product/]]: For three or more primes, the lattice-point set whose weighted count is the
running-lcm reciprocal series is not a product of two lower-dimensional
sets after any unimodular change of variables; for two primes it is.

[[theory/irrationality/L190_three_prime_no_finite_planar_partition/_index|L190_three_prime_no_finite_planar_partition/]]: The expanded lattice set for three distinct primes is not a finite real
linear combination of indicators of polyhedra whose facet coefficients
span at most two dimensions over the rationals.

[[theory/irrationality/L218_sparse_perturbation_any_value/_index|L218_sparse_perturbation_any_value/]]: Changing Euler's totient only on a set with gaps at most g, by multiples of
2^s and by at most the square root except at the first change, makes
sum psi(n)/2^n equal any real number when s+g is at most half of log2 n.

[[theory/irrationality/L219_dilation_design_prime_count/_index|L219_dilation_design_prime_count/]]: A signed family of prime dilations, with admissible shifts and primes above
K, that cancels levels 1 to K for every function uses at least K+1
distinct primes, whose product therefore exceeds K^(K+1).

[[theory/irrationality/L220_partial_multiplicativity_interval/_index|L220_partial_multiplicativity_interval/]]: Positive integer sequences arbitrarily close to the totient, agreeing at
every prime power and obeying its multiplication laws at any fixed finite
set of primes, can have any binary sum in an interval about the totient sum.

[[theory/irrationality/L228_sparse_prime_position_interpolation/_index|L228_sparse_prime_position_interpolation/]]: An interval of binary-series values is attained by increasing integer
sequences agreeing with the nth prime outside one density-zero set,
preserving nested congruences of modulus o(log n), and changing halved
gaps by o(log n). In particular, such a sequence can have a dyadic
rational sum. The altered terms need not be prime.

[[theory/irrationality/L229_critical_modulus_interpolation/_index|L229_critical_modulus_interpolation/]]: Increasing integer sequences that agree with the nth prime at density
one and preserve nested congruences of modulus at least c log n have
a set of binary-series values of Hausdorff dimension zero. Together
with L228, this distinguishes the logarithmic and sublogarithmic
regimes for interval interpolation; it excludes no individual value.

[[theory/irrationality/L230_sparse_interpolation_support/_index|L230_sparse_interpolation_support/]]: The binary-series values of increasing integer sequences that change
only o(N/log log N) of the first N prime positions form a set of
Hausdorff dimension zero. No congruence condition is required. Thus
an interval interpolation cannot have a common exceptional set this
sparse, although an individual rational value is not excluded.

***

These claims concern arithmetic series and tools for studying their values.
The separation theorem for normalized totient kernels supports the
[[research/leads/totient_binary_series/_index|binary totient research]], but
does not settle [[problems/irrationality/E0249/_index|Problem 249]].

Two families test which coefficient information can force irrationality.
[[theory/irrationality/L218_sparse_perturbation_any_value/_index|L218]] and
[[theory/irrationality/L220_partial_multiplicativity_interval/_index|L220]]
construct totient comparisons with prescribed binary sums; the latter keeps
prime-power values and multiplication laws at any fixed finite set of primes.
[[theory/irrationality/L228_sparse_prime_position_interpolation/_index|L228]]
constructs increasing integer comparisons agreeing with almost all prime
positions and preserving sublogarithmic nested congruences.
[[theory/irrationality/L229_critical_modulus_interpolation/_index|L229]] and
[[theory/irrationality/L230_sparse_interpolation_support/_index|L230]]
limit intervals of attainable values when the congruences or support bounds
are strengthened. Their preserved classes are different: neither full totient
multiplicativity nor primality of every modified position is established.
All these claims are author-recorded at tier 0 and leave both catalog
irrationality questions open.
