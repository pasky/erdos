---
name: research/leads/prime_binary_irrationality
title: Irrationality of the Prime Binary Series
desc: |
  Lead for Problem 251: a rational sum of p_n/2^n would put every late
  weighted prime-gap tail on one lattice. The canonical sketch reduces a
  contradiction to an unproved upper estimate for consecutive prime blocks,
  allowing comparison loss c^K for any c<2. Model calculations, rejected
  certificate classes and a failure log distinguish the reductions from the
  missing estimate on about log log X consecutive primes.
tags: []
sources:
- problems/irrationality/E0251
problems:
- 251
research_state: blocked
review_status: unreviewed
created: 2026-10-16T14:53:50Z
updated: 2026-10-17T23:52:10Z
---

# Irrationality of the Prime Binary Series

[[research/leads/_index|..]]

***

This lead's results that are not drawn from a cited source are Plasma AI's,
credited to Plasma AI.

## Target and standing

[[problems/irrationality/E0251/_index|Problem 251]] asks whether
$S=\sum_{n\ge1}p_n2^{-n}$ is irrational, $p_n$ being the $n$th prime. The
problem is open; its page carries the status search, the current assessment
and the two conditional claim pages. This lead records the project's route
toward an unconditional proof. It contains no proof or disproof of the
target. The counting criteria and model calculations are author-recorded.
The matching-window alternative has the separately graded review described
below; that review does not cover the whole route.

The editable proof sketch is
[[research/prime_binary_new_attack/proof_sketch|the parity-prediction sketch]].
It states the whole argument from a rational value to a contradiction, with
its held links, its single open step and a failure log. The other pages of
the route support it:

- [[research/prime_binary_new_attack/zero_phase_certificates|The zero-phase analysis]]
  builds the certificates the sketch needs from one congruence among
  consecutive primes and size bounds on the gaps after them, and measures the
  counts that known cluster theorems supply against the count it needs.
- [[research/prime_binary_new_attack/critical_length_obstructions|The obstruction record]]
  states where fixed lengths, residue-pattern certificates, pointwise
  brackets, weighted means and combinations of tails stop, counts original
  gaps after filtering, and keeps the dependence among overlapping carry
  constraints explicit. It also compares the known consecutive-prime theorems.
- [[research/prime_binary_new_attack/matching_gap_windows|The matching-window note]]
  gives an alternative contradiction from repeated gap windows in different
  index classes, for odd denominator parts greater than one. Its unreviewed
  extension permits explicitly graded congruences of the halved gaps, and
  its unreviewed repeated-window lemma shows that equal windows with small
  later tails occur at all but $X^{o(1)}$ of at least
  $(3/4-o(1))N_X$ starts satisfying its fixed span bound. Its unreviewed
  preceding-gap congruence shows that, for every odd denominator part,
  the dyadic case included, such windows must also have preceding gaps in
  one class modulo $4$; the reversed form makes the tail constant on each
  class of graded congruences of the preceding gaps. Producing one late
  pair with equal windows and preceding gaps in different classes modulo
  $4$ is a missing input for every $d$; a pair in different index classes
  remains an alternative for $d>1$.
- [[research/prime_binary_new_attack/prediction_overlap|The prediction-overlap comparison]]
  groups future windows by one weighted phase modulo two. Rationality
  bounds their minority preceding-gap parity count by
  $(1+\varepsilon)dX/2^{K+1}$. A lower bound exceeding every fixed
  multiple of $X/2^K$ would suffice, but is unproved; repetition and
  balanced marginals alone do not imply it.
- [[research/prime_binary_new_attack/harmonic_phase_ceiling|The doubled-phase comparison]]
  gives the sharp universal ceiling $3/2$ for finite normalized phase
  averages. The resonant references of P9 meet its hypotheses for every
  odd denominator. A strict saving requires a positive proportion of
  square energy, for which no actual-prime estimate is proved.
- [[research/prime_binary_new_attack/residue_switch_moments|The moment analysis]]
  separates aggregate residue switches from a prescribed pattern, and
  identifies the pair-count constant missing at modulus $4$. Its
  fixed-modulus consequence does not provide a growing-block estimate.
- [[research/prime_binary_new_attack/consecutive_block_counts|The upper-count note]]
  shows that a rational value would repeat one tail value at a proportion
  of order $1/(d\log X)$ of the starts and would put most starts in a narrow
  carry window, and states the upper comparisons for consecutive primes
  that would contradict this. A comparison can lose $Cc^K$, $c<2$;
  the note proves phase bounds for independent and periodically restricted
  references and identifies a false termwise estimate for a signed majorant.
- [[research/prime_binary_new_attack/short_span_sieve|The shorter-span note]]
  keeps a positive rationality lower count while enlarging the upper event
  to a monotone subset-existence test on actual sieve survivors. Its
  reference calculation is proved; its two arithmetic costs remain open.
- [[research/prime_binary_new_attack/survivor_moments|The survivor-moment note]]
  removes rough composites from bounded short-window events and the
  rooted second moment by a fixed-dimensional sieve. It identifies the
  unresolved centered estimate on the primes and proves that the
  stopped-sieve transport must cancel a nonzero base moment.
- [[research/prime_binary_new_attack/rational_deletion_signs|The deletion-sign note]]
  uses the rational carry lattice to bound negative deletion mass at an
  enlarged span. The positive mass is then the final count up to
  $o(N_X)$. The finite-rank, small-factor upper test remains open;
  dropping integrality gives a distinct continuous-crossing count with
  too much mass. The fixed-wheel pointwise certificates specified in
  Proposition D24, with bounded potentials and nonnegative prime-pair
  costs, fail already at $d=1$.
  The sign bound supplies no estimate for the shorter-span event.
- [[research/prime_binary_new_attack/phase_transport|The phase-transport note]]
  separates the original prime-root increments from the sum obtained by
  removing each root's phase. The corresponding increments agree under
  rationality; their unconditional endpoints differ. The original sum leads to a binary
  digit-change density test; the dephased sum retains a carry-dependent
  signed cofactor test. Both fixed-saving bounds are unknown. Its
  unconditional bound $Q\le2N_X+o(N_X)$ is too weak for the contradiction.
  Proposition P9 chooses a periodic reference and an odd multiple $b$
  of each denominator $d$ so that the real reference phase is always
  $-1/2$. Rationality then forces $Q_{b,q}=(3/2+o(1))N_X$ for every
  odd $d$. The strict upper bound remains open; the sign issue at
  $d=7$ concerns only the more restricted reference family in P8.
- [[research/prime_binary_series/_index|The earlier notes]] hold the
  truncation identities, the mean-tail bound and the single-phase comparison
  that the sketch reuses.

## The forced structure

Write $g_n=p_{n+1}-p_n$ and $G_n=\sum_{j\ge0}g_{n+j}2^{-j-1}$. For $n\ge2$
the $n$th binary digit of $S$ is the parity of $\lfloor G_{n+1}\rfloor$, so
$S$ is rational exactly when these parities are eventually periodic. If
$S=a/(2^sd)$ with $d$ odd, every tail $G_n$ with $n\ge\max(s+2,3)$ lies in
the lattice $(2/d)\mathbb Z$; replacing the gaps by $p_{n+t}-p_n$, with $t$ the
order of $2$ modulo $d$ and $t=1$ when $d=1$, puts the corresponding tails in
$2\mathbb Z$. Then one congruence among the positions of $K+1$ consecutive
primes, a zero phase,
forces the halved tail $G_{n+K}/2$ after them to be at least $2^K/d$, about
$2^{K+1}/(d\log X)$ times its average near $X$. The prime number theorem
bounds these tails only on average,
so a rational value would force at most $O(dX/2^K)$ exceptions to an explicit
parity rule among the starts with $X<p_n\le2X$, at every length $K$.

## Current gap

The main proposed contradiction is an upper count. Put
$I_X=\{n:X<p_n\le2X\}$, $N_X=|I_X|$,
$K=\lceil A\log_2\log X\rceil$, $R=\lfloor4d\log X\rfloor$ and
$D=\lfloor16K\log X\rfloor$. Let $B_d(X;K)$ count starts in $I_X$
with span at most $D$ and with the least positive residue of
$-d\sum_{j<K}2^{K-1-j}g_{n+j}/2$ modulo $2^K$ at most $R$.
Rationality and the prime number theorem force
$B_d(X;K)\ge(13/16-o(1))N_X$. An upper bound
$B_d(X;K)/N_X\le Cc^K R/2^K+o(1)$, for $1\le c<2$ and
$A>1/\log_2(2/c)$, tends to zero and would contradict this. Theorem U8
proves the implication, including $d=1$ and every preperiod. The upper
estimate for actual consecutive primes is unknown. Constants may depend
on $d$; uniformity in $d$ is unnecessary. The same count for the integers
with no prime factor up to $X^{1/2-1/K^2}$ differs from $B_d(X;K)$ by
$O(N_X/K)$, so the estimate may be posed for those survivors. The lower
sieve cutoffs examined leave an unknown base count and signed sums over
deleted composites whose terms depend on about $K$ nearby survivors
(Lemmas U10 and U11 and Proposition U12 of the upper-count note).
Proposition U15 gives an exact alternative with no unknown base count:
start with the odd integers avoiding one fixed prime $q$ with
$2^{q-1}-1>d$, whose small-carry count is zero, and delete composites
in increasing order. The resulting identity is $B_d(X;K)=\sum\Phi(m)$,
with each weight determined by the preceding $K$ actual primes and a
fixed periodic continuation. The signed upper bound (PD*) remains open.
For $K=\lceil A\log_2\log X\rceil$ with fixed $A>2$ and sufficiently
large $X$, every weight is at most a constant depending on $d$ and $q$,
so the composites with two large prime
factors contribute at most $(1/4+o(1))N_X$ (Lemma U16 and Corollary
U17). The remaining sum equals $B_d(X;K)$ minus that part, so it is
not a weaker target than the upper estimate itself.

Conditioning on rationality also gives the common-carry sign bound
(D12) of the deletion-sign note. At $D=\lfloor K(\log X)^2\rfloor$
with $A>2$, negative deletion mass is $o(N_X)$, whereas rationality
forces the final count to be at least $(7/8-o(1))N_X$. A positive-mass
upper bound $(7/8-\varepsilon_d)N_X$ would finish this variant; it is
unproved. The negative bound makes the positive mass equal to the final
count up to $o(N_X)$, so this target is the direct count bound in
another form. The endpoint criterion concerns the residue gain; the full
gain also keeps its span cutoff. High ranks have arbitrarily small
relative cost, multiple gains at a site have negligible total cost, and
rough sites cost at most $(\log2+o(1))N_X$. The remaining sufficient
test is $P_{\rm SF}^{<T_0}\le N_X/6$ for a sufficiently large fixed
$T_0$, still unknown. The identities do not rule out an arithmetic
estimate for that sum. Proposition D19 instead rules out dropping
integrality: the corresponding ordinary real-tail crossings have an
unconditional lower count exceeding $N_X/6$. The actual residue event
retains the origin $Mc_n$ of (D20). The exact locator (D21) expresses
the remaining site through an increasing integer carry orbit, and
(D22b) keeps all of its prime-gap restrictions. A residue predicate on
that orbit is not an unweighted prime progression count. The artificial
integer-tail ensemble (D23), with uniform endpoint classes modulo $30$
and $5/16$ of its rank-two sites divisible by $5$, rejects that marginal
shortcut only; it is not a sequence of actual primes. The changed span
and rationality hypothesis are part of this interface; neither the sign
bound nor the telescoping identity estimates the shorter-span count below.
A certificate for D24's enlarged crossing event, using a bounded potential
in the carry and a fixed wheel and paying nonnegative costs by the
prime-pair upper bound, cannot reach the budget: stationary integer
transitions give every such certificate cost at least $(1-o(1))N_X$
(Proposition D24). That rejects only the stated class.

The shorter-span alternative takes $K=\lceil12\log_2\log X\rceil$ and
$D_*=\lfloor(6/5)K\log X\rfloor$, keeping the same positive-residue cutoff $R$.
Rationality forces at least $N_X/24-o(N_X)$ consecutive blocks. Counting roots
with any compatible $K$-subset gives a monotone upper event, so an upper bound
$N_X/48$ for that event on the actual survivors at $z=X^{1/2-1/K^2}$ would
suffice. This is (MS) of the shorter-span note, unproved for every odd $d$.
The weaker sufficient target (BC), also unproved, asks only for a fixed saving
below $N_X/24$ for the bounded event on actual primes. Proposition S22
gives $N_X/32$ as a concrete target, with margin $N_X/96$, and an
alternative single weighted band-error budget $N_X/64$. These bounds
would contradict the forced lower count directly; neither is claimed to
give the particular numerical bound in (MS). The aggregate band identity
does not estimate its arithmetic error.
The reference event is rare, while the untruncated sum of its certificates still
has divergent reference expectation. Its two costs are located as follows.
Bounding the roots with more than $5K/4$ later survivors through the centered
survivor moment (VM) would imply a law of large numbers for sums of about
$(6/5)K$ consecutive gaps after almost every prime, for which no proof is known
here, even under the Riemann hypothesis. The survivor-moment note shows
that (VM) differs from its prime-rooted version by only $O(N_X)$, and
that composites change the bounded event by $O(N_X/K)$. Its lower-cutoff
base moment has order $K^2N_X$, so the exact signed transport must cancel
a nonzero contribution. Neither comparison estimates the remaining
prime-rooted moment. At the other roots the specified nonnegative
polynomial cutoff bounds are at least the untruncated subset count;
the damped signed alternative leaves a growing-order correlation bound
unproved. Its weights are too large for the affected-root estimate to
transfer it at the needed precision. Both arithmetic costs remain open.
Lowering the sieve level and proving the band-loss inequalities (PB)
would address the bounded event directly and imply (MS). The exact
losses have the semiprime expansion (S20). The attempted progression
estimate leaves signed coefficients of growing degree and moduli outside
the inspected Bombieri--Vinogradov ranges. Its weighted remainder and
the required lower comparison remain unknown. The one-site calculation
(S21) rules out simply replacing the full divisor sum by periodic
density with an $o(N_X)$ error; it does not refute (PB). Prime-supported
roots survive every band, consistently with (PB) implying the upper
bound that would contradict rationality.

An alternative is more exceptions to the parity rule than the rational
bound allows, along arbitrarily large $X$. The sketch names two sufficient counts, each open
for every odd $d$, including $d=1$: a positive proportion of exceptions at
length $\log_2(d\log X)+O(1)$, and a count of zero-phase starts with tame
continuations, proposed at total length about $2\log_2\log X$. Both seek lower
bounds for joint statistics of about $\log\log X$ consecutive gaps. The known theorems on
consecutive primes, including bounded gaps, dense clusters, congruent strings
and long gaps, stop at stated inequalities on the sketch's pages: they control
fixed lengths, constant residue patterns or rare clusters whose proved counts
fall short of the required count. Under the Riemann hypothesis, a lower bound
for the frequency of zero phases alone at length $A\log_2\log X$, $A>4$, would
suffice. Proposition Z8′ instead uses an explicit large-gap count
$N(x,H)\ll x(\log x)^{B'}/H^2$ and proves the implication for $A>B'+1$,
with its far tail controlled. That conditional refinement does not supply
the zero-phase count. The conditional claims on the problem page assume
uniform prime-tuple hypotheses and are not premises of this route.

The resonant phase-transport alternative writes $d=3^\nu d_0$ with
$3\nmid d_0$ and takes $q=2\cdot3^\nu+1$ and
$b=d_0(2^{q-1}-1)/3$, an odd multiple of $d$. Proposition P9 proves that
the periodic reference has real phase $-1/2$ at every site, also when
$q$ is composite. Under rationality the dephased sum is therefore
$(3/2+o(1))N_X$. A strict upper bound below $3N_X/2$ on unbounded scales
for each $d$ would finish the contradiction beyond every finite preperiod.
This is (RFPT), unproved even for $d=1$. The actual carry coefficient,
least-factor conditions and rank remainder of (P6) remain in the target.
An upper proof may use integrality; an unconditional endpoint-correlation
bound would also suffice. Rank by rank the complete site sums of (P6)
are differences of prime-endpoint sums. This identity gives no bound for
the parts selected by least prime factor and does not prohibit estimating
them under rationality. The reference construction and the signed
boundary exchange (P9h) supply no strict saving. The multiple-crossing
payment (P9i) works for shifts $o(\sqrt{\log X})$, but the examined
decoupling theorem's stated interval bound is too large at that range on
the $N_X$ scale. A stronger estimate remains unproved.
Frequency doubling leaves the same site weight, and the direct shift
comparison needed by the examined decoupling method costs $O(uN_X)$.
The original transport still has its different unconditional endpoint
and the separate, unproved digit-change density test.

The finite-window attempts for the counting and phase targets reach roughly
$\log_2\log X$ consecutive primes, with power-of-two moduli of order a power
of $\log X$. The inspected fixed-length results and cluster bounds have not
supplied the required estimates at that scale. This is a limitation of the
attempts recorded here, not a necessary-input theorem for every proof of
those targets. No proof of irrationality or required arithmetic saving is held.

There is also an upper criterion independent of $d$. A rational value would make one value
of the tails $G_n$ recur at a proportion of order $1/(d\log X)$ of the
starts with $X<p_n\le2X$. So a bound, within any fixed factor of an independent-gap
model, on how often the weighted sums of the next $\log_2\log X+O(1)$ gaps
fall in a short interval would exclude every rational value at once. The
same kind of comparison motivates the carry bound above. The examined
tuple sieve estimate has a factorial loss and does not keep the primes
consecutive; this does not rule out a sharper direct count. Fixed
nonnegative combinations of tuple indicators which majorize the event on
every finite set, at the stated span, have reference mass nearly one
(Lemma U13 and Proposition U14). A bound in that class needs an aggregate
deficit of prime tuples relative to the reference; the argument does not
exclude every arithmetic or signed majorant. An exact signed majorant
retains consecutiveness, but its termwise adverse-error bound
around independent Bernoulli sites is false: tuples excluded modulo $3$
already give too much error. Lemma U9 incorporates small odd-prime
exclusions into a reference without losing its relative phase bound.
Transferring that bound to the actual primes remains the missing theorem;
the model calculation does not supply it. No equivalence between the
signed estimate and a uniform prime-tuples conjecture is proved.

An unspecified selected subtuple cannot be made sufficient simply by
designing a certificate for every possible selection: Lemmas Z6 and Z6b
exhibit failing selections, including when the root is chosen inside the
selected block afterward. Lemma Z6c tests grouped selection as well:
sufficiently large prescribed groups admit representatives with all
half-gaps too large for any internal score certificate. This concerns a
universal guarantee, not which representatives actually occur as primes.
The alternative remains an arithmetic estimate
for favorable selections and their continuations. A single witness would
suffice, but one built from a single residue class is either a chain of
about $\log_2\log p_n$ gaps, each at least a constant times $\log p_n$, or
is followed at once by a cluster denser than the mean (Proposition Z9);
the stated chain and cluster theorems supply neither. Clearing the odd
denominator does not reduce the required number of original gaps in the
mean-based test (O9), and imposing carry integrality at every cut is one
endpoint congruence rather than independent restrictions (O10).

## Review status

No independent review covers the whole route. The
[[research/prime_binary_new_attack/evidence/verify/matching_gap_windows/_index|separately graded review]]
accepts only the conditional matching-window argument at the exact scope
stated on its owning page, without a prime-pair existence theorem. The other
deductions here remain author-recorded. The comparison results
[[theory/irrationality/L228_sparse_prime_position_interpolation/_index|L228]],
[[theory/irrationality/L229_critical_modulus_interpolation/_index|L229]] and
[[theory/irrationality/L230_sparse_interpolation_support/_index|L230]], which
show which local or sparse information about the primes cannot decide the
question, are tier 0.
