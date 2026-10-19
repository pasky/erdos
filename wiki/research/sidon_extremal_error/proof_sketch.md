---
name: research/sidon_extremal_error/proof_sketch
title: "Proof sketch: the subpolynomial error for finite Sidon sets"
desc: "Editable argument for Problem 30: separate upper and lower obligations, an explicit probability-measure obstruction to linear capacities, an exact failed quartic extension, sufficient variance inputs, and the remaining nonuniform moment and construction gaps."
created: 2026-10-15T18:04:27Z
updated: 2026-10-15T18:04:27Z
---

***

This is Plasma AI's editable argument. Its original results are
**author-recorded**, without independent review. Source results retain their
recorded standing. Neither half of Problem 30 is proved, and no improvement
of the extremal error exponent is claimed.

## Target and independent obligations

Let $h(N)$ be the maximum size of a strong Sidon subset of
$\{0,\ldots,N-1\}$, equivalently of $\{1,\ldots,N\}$. Strong Sidon means
$a+b=c+e$ implies equality of the unordered pairs, including repetitions.
[[problems/additive_bases/E0030/_index|Problem 30]] asks whether

$$
\forall\epsilon>0\ \exists C_\epsilon,N_\epsilon\quad
\forall N\ge N_\epsilon:\quad
|h(N)-\sqrt N|\le C_\epsilon N^\epsilon.
$$

The upper estimate for every $N$ and the lower construction for every $N$ are
separate obligations. Improving the coefficient of $N^{1/4}$ addresses
neither exponent gap. Singer's construction at prime powers does not by
itself supply the lower interpolation.

## What the retained argument establishes

1. [[theory/additive_bases/L216_sidon_linear_capacity_barrier/_index|L216 gives a genuine probability measure on k-subsets satisfying every ordinary difference and sum capacity in expectation]]
   for all $N\ge2^{20}$ and
   $k\le\sqrt N+N^{1/4}/2-10$. It samples fixed occupancies in consecutive
   blocks and rotates. Therefore a single separating certificate whose Sidon
   input consists only of constant nonnegative linear combinations of those
   capacities cannot lower the exponent below $1/4$. Its universal
   inequalities may use arbitrary-degree positivity or integrality. An
   adaptive case split is outside the proved scope.
2. [[theory/additive_bases/L217_sidon_block_quartic_obstruction/_index|L217 proves that zeroing forbidden moments of the exact block family and renormalizing each degree uniformly does not give a degree-four pseudo-expectation]].
   For $N=s^4-s^3+s^2$, $k=s^2$ and $D=s^3-s^2+s-1$, the original short-pair
   count has variance at most $(3+2\sqrt2)s^3/12+o(s^3)$, but repeated
   differences contribute $s^3+o(s^3)$. Zeroing removes the latter; uniform
   renormalization restores only $O(s^2)$ in this direction. A square then
   has negative expectation. An exact finite witness is retained at $N=63$.
   A weighted cyclic pair count extends the failure to every fixed excess
   coefficient $c\in(0,1/2]$ in the corresponding block-and-uniform mixture
   family, whenever its first difference capacity holds. This is an
   asymptotic statement; the weighted square itself is still positive in
   the retained small mixture.
3. [[research/sidon_extremal_error/linear_capacity_barrier|Explicit degree-two moments reach the same limiting coefficient 1/2]],
   with a proof for every integer in a stated finite-parameter range. This
   is a relaxation result, not a construction of Sidon sets.
4. [[research/sidon_extremal_error/perfect_difference_cuts|The perfect-difference cut ceiling confines a successful moderate-order Singer cut to a parameter within O(N^(1/4) log N) of sqrt(N)]].
   This gives a necessary prime-power interpolation condition for that
   construction class. It leaves very large-order cuts and other
   constructions unaddressed.
5. [[theory/additive_bases/L273_sidon_parity_obstruction/_index|L273 gives a parity obstruction to zeroing block and uniform laws, with a complete author-recorded proof at tier 0]].
   For integers $s$ sufficiently large and even $W$ with
   $s^3/2\le W\le s^3$, put $N=sW$, $k=s^2$. For either block rotation
   convention, every mixture with the uniform $k$-set law, and either plain
   zeroing or uniform degreewise renormalization, the alternating quadratic
   $A=\sum_d(-1)^dP_d$ has centered square at most
   $-(k^2/2N)(k^2-N)+O(k)$. The identity $2A=B^2-Z$ explains the mechanism:
   every disjoint-pair sum collision has even element sum. In this family the
   bound is negative once $k-\sqrt N$ exceeds an absolute constant. For
   even $W=s^3-\beta s^2+O(s)$ it is $-\beta s^3/2+O(s^2)$.
   The [[research/sidon_extremal_error/parity_obstruction|parity budget]]
   applies to every correction of these zeroed laws. Even shifts protect
   this statistic under a compatible kernel construction. L274 below gives a
   different global signed repair with this square restored.
6. The
   [[research/sidon_extremal_error/local_repair_gap|progression-extension example]]
   refutes the proposed small-error estimate for product-kernel repeated
   zeroing. Moving the fourth point of a support containing a progression
   leaves a forbidden support with total absolute mass at least one,
   uniformly in the kernel width. The conditional cardinality lift remains
   valid. The
   [[research/sidon_extremal_error/short_count_covariance|exact short-count covariance]]
   supplies an additional usable calculation, including the two
   absolute-value kernels and their negative cumulative-sum form.
7. [[theory/additive_combinatorics/L274_signed_sidon_moment_extension/_index|L274 gives a signed degree-four completion of every genuine fixed-cardinality first and second moments for N at least 55]].
   It satisfies all Sidon zeros and local cardinality identities. For
   $N\ge58$ it can also restore the alternating square exactly to its
   genuine variance. The incidence Gram bounds are $N-13$ and $N-54$;
   they prove a global right inverse on the compatible data and give explicit
   Euclidean norm bounds. These are complete author-recorded results at tier
   0. They provide no positivity of the full quadratic moment matrix.

These results compose to locate the missing mathematics, not to prove the
extremal assertion. L216 supplies a complete obstruction to a specified
certificate class. L217 shows why one natural attempt to extend the
obstruction to degree four fails. L274 supplies signed extensions, while
existence of more general matrix-positive degree-four extensions remains open.

## The window identity and a sufficient variance input

Normalize a Sidon set by $\min A=0$, $\max A=D$, $|A|=k$. For integer
$T\ge1$, let $c_i=|A\cap[i-T,i)|$ for $1\le i\le D+T$, let $V_T$ be the
sum of squared deviations of these counts from $kT/(D+T)$, and put
$S_T=\sum_{1\le d<T,\ d\notin A-A}(T-d)$. Direct counting gives
$\sum_i\binom{c_i}{2}=\binom T2-S_T$ and $\sum_i c_i=kT$. Thus

$$
2S_T+V_T=T(T+k-1)-\frac{k^2T^2}{D+T}.                 \tag{1}
$$

This is the rearranged form of
[[../library/additive_bases/obryant_2022_size_finite_sidon_sets/theorem_4|O'Bryant's Theorem 4]],
with the required counting argument supplied here. It is not used at a
stronger standing than its source card.

Write $W=k^2-D$. Equation (1) is equivalently

$$
V_T=T(k-1)-\frac{T^2(W-T)}{D+T}-2S_T.                 \tag{2}
$$

Large positive $W$ therefore forces a reduction of the variance below
$T(k-1)$ at $T$ near $W/2$. Conversely, the additional estimate
$V_T\ge(1-\eta)T(k-1)$ would imply

$$
W\le T+\frac{\eta(k-1)D}{T}+\eta(k-1).               \tag{3}
$$

Taking $T=\lceil\sqrt{\eta(k-1)D}\rceil$ bounds the right side by
$2\sqrt{\eta(k-1)D}+\eta(k-1)+1$. At $k\asymp\sqrt D$, a relative error
$\eta=O(D^{-\delta})$ would thus give an upper error
$O(D^{1/4-\delta/2})$. A fixed $\delta>0$ gives an exponent improvement,
not the full target. For the full target this sufficient route would need,
for every small $\epsilon>0$, a suitable estimate with
$\eta=O_\epsilon(D^{-1/2+2\epsilon})$ at
$T\asymp D^{1/2+\epsilon}$.

No such lower variance estimate is proved here. It is a **sufficient
premise**, not an equivalent reformulation: a small value of $W$ in (2)
does not control the missing-difference term $S_T$ from above. For a perfect
cyclic difference set of size $k$ modulo $M$, a separate cyclic count gives
$V_T=T(k-1)(1-T/M)$ for $1\le T\le M$. That identity illustrates the desired
scale but supplies no universal lower bound for ordinary Sidon sets.

## Degree-four frontier

The
[[research/sidon_extremal_error/degree_four_extension|degree-four account defines R_4(N,k), proves its Boolean-count constraints, and records the exact failed extension and possible repairs]].
The open decision is whether $R_4(N,k)$ is nonempty at
$k=\sqrt N+cN^{1/4}$ for some fixed $c>0$ along an unbounded sequence. A
construction would extend the obstruction to that relaxation. An explicit
infeasibility argument, with a uniform quantitative range, would be a
candidate upper estimate. Failure of one extension proves neither.

The necessary correction to the zeroed block law is of order $s^3$ in the
short-pair square; a uniform degreewise change supplies only $O(s^2)$.
Full cyclic translation symmetry is unavailable: for odd $N$ it propagates
the ordinary zeros to all cyclic zeros and forces $k(k-1)\le N-1$.

A global signed repair is supplied by L274; locality and full matrix
positivity remain open. The
[[research/sidon_extremal_error/local_repair_gap|local-repair analysis]]
separates three further obligations for that strategy:

- **Control of the correction.** L274 gives the exact compatibility space
  and a global right inverse. A localized version must treat
  progression-containing four-sets jointly with their triple margins: the
  square operator on all forbidden supports is singular and the claimed
  small off-center error is false. The cardinality lift is valid. Distinct
  positions, boundary effects and matrix-norm bounds still need control.
- **Difference-count covariance.** The exact covariance of the genuine
  unrotated block law has a low-rank polynomial part and kernels
  $K_D|d-e|+K_A|d+e-W|$, with $K_D\sim s^{-6}$ and $K_A\sim-s^{-6}$.
  A heuristic interior comparison with diagonal slack $(1-\beta)/s$
  suggests $s/(1-\beta)\ll L\ll\sqrt{1-\beta}\,s^{5/2}$ for a common
  even-shift kernel. Neither a global high-frequency floor nor the errors
  of a completed repair are proved. The long-difference block is also open.
- **Whole moment matrix.** A covariance of counts is only a principal part
  of the positivity requirement. Position-dependent quadratic statistics
  and their coupling to counts remain to be controlled. Requiring positivity
  for counts localized to every singleton already recovers the full
  quadratic-square condition, by the local cardinality identities; it is
  not an intermediate relaxation.

The alternating square can be restored exactly by L274's finite signed trade.
This passes one necessary test, without supplying the three further
obligations above. A construction meeting them at
$k=\sqrt N+cN^{1/4}$ would extend the relaxation barrier. A failure of one
kernel construction would still leave general degree-four feasibility open.

## Lower construction and source interfaces

[[../library/additive_bases/singer_1938_theorem_finite_projective_geometry_some_applications_number_theory/theorem_p380|Singer's prime-power theorem]]
supplies $q+1$ elements modulo $q^2+q+1$. If a prime power lies within $g$ of
$\sqrt N$, its whole set or a best arc gives
$h(N)\ge\sqrt N-g-O(1)$. This conditional interpolation does not assert an
available subpolynomial bound for $g$. The perfect-difference cut ceiling
is necessary only for its explicitly stated moderate-order class.

The complete original claims use no unproved external premise. The lower
construction discussion uses Singer at its recorded statement and proof-pointer
standing. Haoyu Chen's 2026 write-up claims
$h(N)\le\sqrt N+(2\sqrt2/3)N^{1/4}+1$ for $N\ge120^4$, credits proofs to
GPT-6 Astra and referee reports to Claude Opus, and is recorded without
acceptance on the problem page. Its proof is not consumed here. The Hou–Zhao
coefficient claim likewise is not a premise. Coverage of particular published
coefficient proofs by the linear-capacity class has not been established.

## Remaining routes

- Prove a sufficiently strong variance estimate in (3), or find a different
  nonlinear inequality that lowers the upper exponent. Neither follows from
  the capacity barrier or its failed extension.
- Obtain a matrix-positive nonuniform completion, potentially by refining
  L274's global right inverse or by a local repair with progression extensions
  and overlapping perturbations handled together. The parity budget and the
  exact genuine short-count covariance constrain this route; they do not
  establish positivity.
- Find an all-$N$ construction with subpolynomial loss, or a counterexample
  family. Prime-power-only sets and finite computations do not meet this
  obligation.
- For a weaker counterexample to a bounded upper error, seek a Singer arc $J$
  of length $L\le q^{3/2}$ with $|S\cap J|\le L/(2q)-G$, $G\to\infty$.
  Removing that arc gives $k-\sqrt N=L/(2q)-|S\cap J|+O(1)$. No such family
  is constructed here, and even logarithmic excess would be consistent with
  Problem 30.
