---
name: research/prime_binary_new_attack
title: Parity prediction for the prime binary series
desc: |
  Plasma AI's attack on the irrationality of the sum of p_n/2^n: a parity
  criterion, its missing prime estimate, zero-phase certificates and the
  counts they need, and sparse rational interpolation preserving almost all
  prime positions and subcritical residues, with a dimension-zero boundary
  at logarithmic moduli.
created: 2026-10-15T18:43:21Z
updated: 2026-10-18T10:09:26Z
---

# Parity prediction for the prime binary series

[[research/_index|..]]

[[research/prime_binary_new_attack/consecutive_block_counts|consecutive_block_counts]]: For Problem 251, a rational sum would make one weighted gap-tail value
repeat about N_X/(d log X) times among starts X<p_n<=2X, and put most
starts in a narrow carry window for about log_2 log X consecutive gaps.
An upper comparison tolerates a loss c^K with c<2 at longer blocks.
Exact model bounds, a signed majorant, a survivor count at the
square-root sieve level and a signed deletion sum isolate the missing
prime estimate.

[[research/prime_binary_new_attack/critical_length_obstructions|critical_length_obstructions]]: Limits of specified phase-counting mechanisms for Problem 251, a
rational interpolation theorem preserving residues below the critical
length, and a comparison with known consecutive-prime theorems.

[[research/prime_binary_new_attack/evidence/_index|evidence/]]: Finite observations of the parity-prediction rule on the primes below
2 * 10^7: the rule's two forms agree on every start, mispredicted fractions
stay near one half, and later residues add almost nothing to predicting
the parity of a gap; and a separately graded mathematical review of the
conditional matching-window argument.

[[research/prime_binary_new_attack/harmonic_phase_ceiling|harmonic_phase_ceiling]]: Finite normalized mixtures of doubled phase deficits have optimal
universal ceiling 3/2, attained by weights 2/3 and 1/3. For a resonant
prime-tail reference, the deficit below this ceiling is an exact
nonnegative energy. A positive proportion of that energy remains an
arithmetic hypothesis, and integer carries make every doubled site
weight identical.

[[research/prime_binary_new_attack/matching_gap_windows|matching_gap_windows]]: Exact repeated gap windows with small enough tails would force a congruence between their starting indices and, for every odd denominator including the dyadic case, between their preceding gaps modulo 4. Such windows occur in abundance unconditionally; producing them in different index classes or preceding classes remains open.

[[research/prime_binary_new_attack/phase_transport|phase_transport]]: Composite deletion yields two signed sums with different unconditional
endpoints. Integer carries make their corresponding root increments
agree. Removing each root's phase retains the actual carry coefficient.
A periodic reference and an odd multiple of every denominator give
the common rationality endpoint 3N/2. The signed cofactor estimate
needed to improve that endpoint remains unproved.

[[research/prime_binary_new_attack/prediction_overlap|prediction_overlap]]: Rationality forces the preceding half-gap parity to be determined by
the weighted future window modulo two, except at O(dX/2^K) starts.
A scalar minority count gives a sufficient occurrence target using
less window information. Repetition, PNT growth and balanced parity
marginals alone do not supply the required overlap.

[[research/prime_binary_new_attack/proof_sketch|proof_sketch]]: The canonical sketch for Problem 251, from a rational sum through an
integer carry lattice to a contradiction conditional on a consecutive
prime-block estimate. An upper comparison may lose c^K for any c<2.
Parity prediction, zero-phase alternatives, model computations and an
exact failure log distinguish the held reductions from the missing
arithmetic estimate.

[[research/prime_binary_new_attack/rational_deletion_signs|rational_deletion_signs]]: A rational prime binary series forces only o(N_X) downward residue
transitions when composites are deleted from a periodic set, so the
positive mass is the final count up to o(N_X). Gains are decided at the
prime endpoints; high ranks cost arbitrarily little and rough sites at
most log 2. The small-factor estimate is open. Dropping integrality
gives too much mass, and certificates with nonnegative prime-pair costs
fail on stationary integer transitions.

[[research/prime_binary_new_attack/residue_switch_moments|residue_switch_moments]]: A moment criterion turns a bound for same-class prime pairs into a
positive proportion of residue switches. The inspected tuple sieve gives
the criterion when phi(q)>8; reaching modulo 4 needs a smaller pair
constant. This fixed-length information does not supply the growing
prime-block estimate for Problem 251.

[[research/prime_binary_new_attack/short_span_sieve|short_span_sieve]]: A rational prime binary series forces at least N_X/24 qualifying blocks
in a shorter span. Their monotone enlargement is rare in the reference
model and can be posed for actual sieve survivors. The survivor estimate
is unproved. Its centered-moment cost is equivalent to a prime-rooted
short-interval estimate. A damped signed form isolates the remaining
truncated phase cost, whose required bound is also unproved. The band-loss
alternative has an exact divisor expansion but no arithmetic estimate.

[[research/prime_binary_new_attack/survivor_moments|survivor_moments]]: A fixed-dimensional sieve bounds rough-composite contamination of the
rooted second moment by O(N_X) and of bounded local counts by O(N_X/K).
The centered-moment input is therefore equivalent to its prime-rooted
version. At the lower sieve cutoff, a positive base moment must be
canceled by the signed transport. Neither missing estimate is proved.

[[research/prime_binary_new_attack/zero_phase_certificates|zero_phase_certificates]]: For Problem 251, one congruence among K+1 consecutive primes would force
a large following tail under rationality; a two-cutoff count turns this
into a criterion, the counts that known cluster theorems supply fall short
of it, and under the Riemann hypothesis a frequency bound for the
congruence alone would suffice.

***

## What the folder holds

[[problems/irrationality/E0251/_index|Problem 251]] asks whether
$S=\sum_{n\ge1}p_n/2^n$ is irrational. This folder continues the
[[research/prime_binary_series/_index|earlier notes on the prime binary series]],
reusing their identities and mean-tail bound without repeating the proofs.

[[research/prime_binary_new_attack/proof_sketch|The parity-prediction sketch]]
is the editable proof sketch. A rational $S$ with odd denominator part $d$
would make an explicit rule predict the parity of a halved prime gap from
the next $K-1$ gap residues, with at most $O(dX/2^K)$ exceptions among starts
$X<p_n\le2X$. A count exceeding this bound at
$K=\log_2\log X+O_d(1)$ would exclude $d$; such a count for every odd $d$
would prove irrationality. It remains unproved. A single hypothesis free of
$d$, that these residue laws retain a fixed amount of overlap with a
one-coordinate translate, would also suffice.
The sketch opens with the digit identity, which makes the binary digits of
$S$ from the second on the parities of the integer parts of the gap tails,
and with a step lemma, which turns every rational value into a dyadic case
for the gaps $p_{n+t}-p_n$.
[[research/prime_binary_new_attack/zero_phase_certificates|The zero-phase analysis]]
builds mispredicted starts from one congruence among $K+1$ consecutive primes
and size bounds on the gaps after them. It states the count this needs, shows
that the counts proved by the known cluster theorems fall short of it, and
shows that under the Riemann hypothesis a frequency bound for the congruence
alone would suffice.
[[research/leads/prime_binary_irrationality/_index|The lead page]] summarizes
the route for Problem 251.
[[research/prime_binary_new_attack/consecutive_block_counts|The upper-count note]]
turns the lattice into two lower counts, a repeated tail value and a
narrow carry window for most blocks. A comparison for the latter may lose
$Cc^K$ for any $c<2$ at a suitable length $K=A\log_2\log X+O(1)$;
the repeated-tail criterion is free of $d$. Independent and periodically
restricted references have the needed phase bound. No comparison with
actual consecutive primes is proved. The note also gives an exact
obstruction to bounding a signed majorant by its adverse termwise errors.
The
[[research/prime_binary_new_attack/rational_deletion_signs|conditional
sign analysis]] retains the actual integer carries in an increasing
composite-deletion process. It bounds downward residue transitions by
$o(N_X)$ at $K=\lceil A\log_2\log X\rceil$, $A>2$, and counts span
losses separately. With span $K(\log X)^2$, the negative deletion weight
is negligible under rationality, so the positive mass equals the
final count up to $o(N_X)$. Its residue gains have an endpoint
criterion; the full gains also retain their span cutoff. High ranks
have arbitrarily small relative cost, bad gaps and multiple gains have
negligible total cost, and sites with least prime factor above $X^{1/3}$
cost at most $(\log2+o(1))N_X$. The small-factor, low-rank bound remains
open. The endpoint identity does not rule out estimating it.
Proposition D19 rules out a specific relaxation instead: dropping
integrality gives an ordinary real-tail crossing count with an
unconditional lower bound above the proposed upper target.
The
[[research/prime_binary_new_attack/phase_transport|phase-transport note]]
distinguishes those original prime-root increments from the dephased sum
$Q$. Integer carries make corresponding root increments agree; the two
unconditional endpoints differ. The original sum gives a positive-density digit-change
criterion; the dephased sum gives a signed cofactor estimate with a
carry-dependent coefficient. Both fixed-saving targets are unknown, and
the bound $Q\le2N_X+o(N_X)$ is insufficient.
[[research/prime_binary_new_attack/critical_length_obstructions|The obstruction record]]
states, with their exact scope, why fixed block lengths, residue-pattern
certificates, pointwise brackets, weighted means, combinations of tails and
upper-bound counts do not supply that statement, and compares the known
theorems on consecutive primes. For block lengths with $2^K/\log X\to0$,
it also constructs comparison sequences with the same pointwise residue
patterns, the same cumulative growth and a dyadic rational sum. Residue-window
laws on the corresponding value ranges $X<p_n\le2X$ differ by at most $o(1)$
in total variation; this does not preserve relative counts of rare events.

[[theory/irrationality/L228_sparse_prime_position_interpolation/_index|L228 gives a stronger comparison with a rational sum]]:
an interval of series values can be attained while retaining the actual nth
prime outside one density-zero set, preserving nested moduli $o(\log n)$,
and changing every gap by $o(\log n)$. Its proof uses paired positive and
negative gap corrections and the classical prime-pair upper bound. The
altered terms need not be prime.

[[theory/irrationality/L229_critical_modulus_interpolation/_index|L229 gives the complementary boundary at logarithmic moduli]]:
when $q_n\ge c\log n$ eventually, all values attainable with density-one
agreement and the same nested congruences form a set of Hausdorff dimension
zero. This prevents interval interpolation in that regime, but does not
exclude any specified rational value.

[[theory/irrationality/L230_sparse_interpolation_support/_index|L230 limits further sparsification]]:
even without congruences, changing only $o(N/\log\log N)$ of the first
$N$ positions gives a set of values of dimension zero. It rules out that
support bound for an interval construction, while leaving individual
rational targets open. L228 achieves the corresponding big-oh bound
for nested moduli $O((\log n)^\alpha)$ with fixed $\alpha<1$.

The parity-prediction and interpolation deductions above are author-recorded
and not independently reviewed. The separate
[[research/prime_binary_new_attack/matching_gap_windows|matching-window
conditional]] has an independently accepted review at its stated conditional
scope, with a localized wording correction disclosed there. None supplies a
new estimate for the unaltered prime sequence, and the problem remains open.
The remaining obligation is an estimate for the actual consecutive primes, or a different argument using information the comparisons discard.

The
[[research/totient_binary_new_attack/_index|totient binary-series comparisons]]
use the same test of which coefficient information permits rational sums,
but preserve different hypotheses: prime-power values and fixed-prime
multiplication laws, rather than increasing positions and prime congruences.
No implication between the two irrationality questions follows. In each
case the open route must use information the corresponding comparisons do
not retain.
