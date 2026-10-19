---
name: research/leads/distinct_totient_preimage_ratio
title: The Ratio of the Two Distinct-Totient Counts
desc: |
  Conditional on the unrefereed totients manuscript, a continuous phase
  quotient, finite-prime sums and a tail factorization reduce Problem 417 to
  a cancellation in the cofactor fiber. The bounded tests leave it open: the
  direct rectangle comparison misses the tail, and a proposed renewal
  comparison needs fiber and error estimates not supplied by the premises.
problems:
- 417
research_state: blocked
review_status: needs_update
created: 2026-09-28T06:18:00Z
updated: 2026-10-19T04:19:07Z
---

# The Ratio of the Two Distinct-Totient Counts

[[research/leads/_index|..]]

***

This lead's notes that cite no source are author-recorded research, not claims.

## Conditional phase reduction

The precise remaining question is whether

$$
s\longmapsto\frac{A(1/r;s)}{A(1;s)}\qquad(0\le s<1)     \tag{1}
$$

is constant. Here $r$ is the weight's argument, the least-preimage ratio
$\ell(d)/d$ of a tail totient, and $A$ is the coefficient of the
[[../library/arithmetic_functions/openai_2026_asymptotic_formula_number_totients/_index|unrefereed totients manuscript]].
[[theory/number_theory/L65_conditional_totient_ratio_coefficient/_index|L65]],
an author-recorded conditional deduction at tier 0, proves uniform existence
of $A(1/r;s)$, its uniform positive lower bound, and

$$
V'(x)=\frac{xG_m}{\log x}\bigl(A(1/r;\theta(x))+o(1)\bigr).
                                                               \tag{2}
$$

Its proof extends the manuscript's count of the largest prime, using
Proposition 5.3's identity for the least preimage and the comparison lemma
6.6. Lemma 7.3 supplies the uniform tail bound for
$V-V'=\sum_{k\ge1}N_k$; in particular,
$A(1/r;s)=A(1;s)-\sum_{k\ge1}A(f_k;s)$, uniformly in $s$.
Each phase occurs at arbitrarily large real arguments, so (1) is constant
if and only if $V/V'$ has a limit. If it is nonconstant, Proposition 417.2
gives a nondegenerate interval of limit points. L65 assumes no continuity of
the coefficient.

[[theory/number_theory/L43_continuous_totient_phase_ratio/_index|L43]], a
further tier-0 conditional deduction resting on L65, proves that continuity
from the same premises. Both $A(1;s)$ and $A(1/r;s)$ are continuous on
$0\le s<1$, and each tends to $\lambda/\gamma$ times its value at $s=0$ as
$s\to1$, where $\lambda/\gamma>1$ is the factor by which $G_m$
jumps at the end of a period. Hence $A(1;s)$ is not constant, and (1) is a
continuous function on the circle $\mathbb R/\mathbb Z$. The limit points of
$V/V'$ are exactly the values of the reciprocal of (1), and (1) is constant
if and only if all its nonzero Fourier coefficients vanish. A limit for
$V/V'$ therefore needs an exact cancellation between two nonconstant
coefficients.

[[theory/number_theory/L44_finite_prime_totient_phase/_index|L44]], also
tier 0 and conditional on the manuscript, constructs the phase profiles of
fixed finite-prime divisibility conditions on the global least preimage.
It approximates (1) from above by one finite-prime weighted sum with error
at most $1/(Y-1)$, uniformly in phase, when primes at most $Y$ are retained.
The construction and remaining cancellation are stated below.

[[theory/number_theory/L103_totient_tail_cofactor_factorization/_index|L103]],
a tier-0 deduction from the same manuscript applied at two cuts, shows that
outside vanishing mass every tail totient factors through one prime tuple
and a coprime cofactor, with a multiplicative least preimage. The phase
observable in (1) therefore becomes a function of the smooth cofactor,
averaged over a phase-dependent law. A proposed renewal comparison through
that law still needs a weighted fiber estimate. Even if established with
an error tending to zero, its degenerating kernel would not force
constancy. The section "Tail uniqueness and the cofactor fiber" records
the proposal, its gaps, and one quantitative estimate that would suffice.

Everything in this reduction depends on the manuscript's unrefereed
structural and weighted estimates. The accepted fixed-dilation result for
Problem 416 does not certify those estimates. Theorem 2.2 of the manuscript
also implies $\liminf V/V'>1$ from $N_1(x)\asymp V(x)$, but does not
decide (1). Neither the manuscript nor these deductions claim a solution of
Problem 417.

## Target and exact question

[[problems/arithmetic_functions/E0417/_index|Problem 417]], status open. With
$V(x)=\#\{\varphi(m)\le x:m\ge1\}$, the number of totient values up to
$x$, and $V'(x)=\#\{\varphi(m):1\le m\le x\}$, the number of distinct
totients of the integers up to $x$: does $\lim_{x\to\infty}V(x)/V'(x)$
exist, and is it greater than $1$? The problem page records the formulation
and status evidence; no solution is claimed here. Its
sources on $V'$ are the order of magnitude $V\asymp V'$ that Pollack, Pomerance
and Treviño attribute to Ford, and the closing remark of Maier and Pomerance
that a lower bound for $V(x)-V'(x)$, the number of totients up to $x$ all of
whose preimages exceed $x$, is a harder question than the order of $V$.

## Route and established inputs at their actual scope

The route is the section "Problem 417" of
[[research/erdos_416/connections|the connections page of the Problem 416 folder]],
where every statement below is proved; write $R(x)=V(x)/V'(x)$ and
$V_0(x)=V(x)-V'(x)$.

- Proposition 417.2 (author-recorded): the set of subsequential limits of
  $R$ is the closed interval $[\liminf R,\limsup R]$, so either the limit
  exists or $R$ has continuum many limit points. Inputs: $V'$ has unit
  jumps and $V'(x)\ge\pi(x)$, so the adjacent variation of $R$ tends to
  $0$, and Step 7 of
  [[research/erdos_416/zeraoulia_theorem_1_1_reconstruction|the preprint's reconstruction]]
  runs verbatim; the finiteness of the upper endpoint is the cited order
  of magnitude $V\asymp V'$ (page 7 of the 2013 manuscript on
  [[../library/primes/pollack_et_al_2013_sets_monotonicity_euler_totient_function/_index|its card]],
  quoting Ford's §§4–5, not reread), or alternatively Lemma 4.1(iii) of
  that manuscript as reconstructed on
  [[research/erdos_49/lemma_4_1_reconstruction|the Problem 49 folder's page]]
  with its two imported counts.
- Theorem 417.3 (author-recorded): $V_0(x)\ge\eta V(x)$ for arbitrarily
  large $x$, for some $\eta>0$; hence $\limsup R>1$, and if the limit
  exists it exceeds $1$. Inputs: Ford's Theorem 8
  ([[../library/arithmetic_functions/ford_1998_distribution_totients/_index|card]],
  statement level) with the paper's witness $d=54$, whose preimages $81$ and
  $162$ are verified on the connections page, so that a positive
  proportion of totients have every preimage divisible by $3$ and hence
  least preimage at least $\tfrac32$ times the value; Ford's Theorem 1
  with the derivative bound of Step 1 of the preprint's reconstruction,
  which sums $V$ along a geometric sequence of scales; and Chebyshev's
  bound. The refereed inputs suffice; the accepted doubling law of
  [[research/erdos_416/kruer_kohlmeyer_theorem_1_1_reconstruction|the Theorem 1.1 reconstruction]]
  is not needed and would only sharpen a constant.
- The reformulation $V_0(x)=\#\{v\le x\text{ totient}:f_{\min}(v)>x\}$
  with $f_{\min}$ the least preimage, and the frame under which the limit
  exists and equals the reciprocal of $\int_0^1G(1/u)\,du$, where $G$
  would be a limiting distribution function of $f_{\min}(v)/v$ over
  totients and the general-scale law $V(ux)\sim uV(x)$ is assumed.

Finite-range numbers (exploratory, from a sieve of Euler's function to
$6.2\cdot10^7$, which covers every preimage of every totient up to
$10^7$): $R(x)$ is $1.0991$, $1.1000$, $1.0996$ and $1.1000$ at
$x=10^4,10^5,10^6,10^7$, every totient $v\le10^7$ has
$f_{\min}(v)\le2.0414\,v$, and among the totients in $(5\cdot10^6,10^7]$
the proportions with least-preimage ratio at least $1.1$, $1.25$ and
$1.5$ are $0.319$, $0.266$ and $0.194$. These are observations, not
evidence for the limit.

The same three unconditional statements and the conditional one are derived
independently on
[[research/erdos_49/connections|the Problem 49 connections page]] (Propositions
2, 3 and 4) from Lemma 4.1 as stated, with the seed totient $1$ for boundedness
and the reversed-pair seed $2^{18}\cdot257$, all of whose preimages are even,
for the limit superior; its premise (W) is (P1) in convenient-integer form.

## Provisional premises

- (P1) The short-interval form of Ford's Theorem 8: totients in
  $(2x/3,x]$ all of whose preimages are divisible by $3$ number
  $\gg V(x)$ for all large $x$. Ford's Theorem 4 localizes the paper's
  multiplicity counts to intervals $(x,x+y]$ with $y\ge x^\theta$ by a
  modification of the proofs of Theorems 1 and 2, and Theorem 8 is
  a corollary of the proof of Theorem 2, but the held paper does not
  state the localized form. Under (P1), Proposition 417.4 of the
  connections page gives $\liminf R>1$.
- (P2) A limiting distribution of the least-preimage ratio over
  totients, together with the general-scale law of Problem 416. Under (P2)
  the limit exists
  with the value given by the frame; without it the frame is only a
  reformulation. The general-scale law is an accepted input recorded on the
  problem page; convergence of the distribution is not established here.

(P1) remains a possible route from the refereed literature to a uniform
lower bound above one. It is not needed for the conditional phase test,
whose manuscript already gives that conclusion. (P2) is stronger than
what that test needs: constancy of the single weighted average (1)
suffices, whether or not a whole limiting distribution is available.

## Consequential gap

Whether (1) is constant. For the finite coefficients, let $p_{H,s}(d)$ be
the probability of the **union** of the witness events for $d$ in the
manuscript's Equation (2.7). Cancellation of the common prefactor gives

$$
\frac{A_H(1/r;s)}{A_H(1;s)}
=\frac{\sum_d p_{H,s}(d)/\ell(d)}{\sum_d p_{H,s}(d)/d}. \tag{3}
$$

L65 proves uniform convergence of this quotient. Both the finite witness
set and its union probabilities vary with $s$. The sum is over distinct
totients $d$, and $\ell(d)$ is minimized over all preimages, not over a
chosen witness. A proposed separation of small-prime arithmetic from the
phase must respect both operations. The manuscript's common-prefix
proposition does not itself make the tail law independent of phase.
Applied also at the shorter cut $P$, it removes the union over tail prime
tuples outside vanishing mass (L103). Deduplication and the global minimum
then act only inside the distinct totients of the smooth cofactor, which is
where two phases must be compared.

The earlier near-hit mechanism for Problem 416 also does not decide this:
$R$ compares two functions at one scale, so consecutive ratios do not
telescope. The accepted pair construction bounds least preimages above
without supplying the phase cancellation needed in (3).

## The finite-coefficient test

Write $q_H(s)$ for (3), $g(d)=d/\ell(d)$, $\beta=\gamma/\alpha_s$, and
$\mu_{H,s}$ for the probability measure on tail totients proportional to
$p_{H,s}(d)/d$, so that $q_H(s)$ is the $\mu_{H,s}$-expectation of $g$. The
following observations are author-recorded and unreviewed; they
locate where the phase enters (3) without deciding (1).

- **Scale covariance of a continuous relaxation.** Multiply every tail
  coordinate $v_h=\log\log Q_h$, $P\le h<H$, by $c=\alpha_{s'}/\alpha_s$.
  The bands of (2.5) at phase $s$ become exactly those at phase $s'$, the
  simplex conditions of (2.5) are homogeneous, and every threshold
  $\beta\rho^hD(h,\eta)$ in (2.7) is unchanged, since $\beta$ becomes
  $\beta/c$ while $D$, linear in the $v_l$, becomes $cD$. Replacing
  unrestricted prime reciprocal sums by the Mertens measure $dv_h$ would
  leave a factor $c^{-P}$, from the prefactor
  $(\gamma/\alpha_s)^H$ and the Jacobian $c^{H-P}$. That common factor
  would cancel in a quotient. However, this map supplies no primes with
  the rescaled coordinates, no correspondence of distinct totient values,
  and no transport of the minimum over all preimages. The smooth cofactor
  and its bound also remain arithmetic. Mertens' theorem alone gives no
  error estimate for this weighted, deduplicated transport. The covariance
  is exact for the real inequalities and thresholds; extending it to (3)
  is the missing construction. After the factorization (6) below it must
  compare the restricted pair law and its cofactor fibers, whose smoothness
  bound $Q_P$ moves with the rescaled coordinates.
- **Pieces and drift.** For fixed $H$ the phase enters the witness
  conditions (2.5) only through the bands for $\log\log Q_h$ and the bound
  for $\log a$, so $[0,1)$ splits into finitely many intervals on which every
  witness set is constant (the first step of L43's proof). On such an
  interval only $\beta$ varies, with $d\beta/ds=-\lambda\beta$, and
  differentiating (3) gives $q_H'(s)=-\lambda\beta\,c_H(s)$, where
  $c_H(s)=\mathrm{Cov}_{\mu_{H,s}}(g,\partial_\beta\log p_{H,s})$.
  For a single witness $\eta$,
  $\partial_\beta\log p=-\sum_{h\ge H}\rho^hD(h,\eta)$, which is dominated
  by the largest tail primes, while $g$ is governed by the smallest primes
  of the least preimage. The rest of the variation of $q_H$ is a finite set
  of jumps where a witness enters or leaves a band or the cofactor bound.
  Constancy needs the integrated drift and the jumps between any two phases
  to cancel in the limit, including the jumps at the lowest band and at the
  cofactor bound, next to the smallest primes.
- **Memoryless factorization.** If all witnesses of $d$ share their primes
  $Q_h$ for $H'\le h<H$, then $D(h,\eta)=D'(h)+D''(h,\eta)$ with $D'$ the
  common contribution of those primes. Put $S'=\sum_{h\ge H}\rho^hD'(h)$.
  The memoryless property of the exponential variables gives exactly that
  $p_{H,s}(d)$ equals $e^{-\beta S'}$ times the probability of the union
  over $\eta$ of the events $E_h\ge\beta\rho^hD''(h,\eta)$ for all
  $h\ge H$. This factors a common part of the penalty. By itself it does
  not factor the sum over distinct $d$, the weight $1/d$, or $g(d)$, all
  of which retain the full arithmetic fiber. When all witnesses share the
  whole tuple ($H'=P$), $Q_P$ does not divide the cofactor, and the least
  preimage splits as in L103, all three factor through the cofactor
  totient; L103 shows that these conditions hold outside vanishing mass.
- **Descent supplies no mixing law.** At the nominal lower scale one has
  $\psi(\alpha_sH\rho^{-H})=H+s+o(1)$, so the central grid does not
  average over phases. The actual bands have width, and the cofactor is
  constrained by both size and smoothness. The proposed transition through
  the cofactor fiber, relation (9) below, would shift the phase by the
  relative position of $Q_P$ in its band. Under the coefficient-transfer
  premise stated below, that position concentrates as $P$ grows.
  Lemma 6.4 expressly bounds each phase without comparing
  witness sets at nearby phases, and Proposition 5.3 supplies no such
  comparison. A continuous simplex model omits deduplication and the
  global minimum; its fluctuations or Fourier coefficients therefore give
  no estimate for (1).
- **Grouping the cofactors still requires a union over distinct values.**
  Fix $H,s$ and a prime tuple $\mathbf Q$. Let $\mathcal A_{\mathbf Q,s}$
  be its admissible cofactors in (2.5), and put
  $d_{\mathbf Q}(a)=\varphi(a\prod_hQ_h)$. The event in (2.7) depends
  only on $\mathbf Q$; denote it by $\mathcal E_{\mathbf Q}$ and put
  $\mathcal T_s(d)=\{\mathbf Q:d=d_{\mathbf Q}(a)
  \text{ for some }a\in\mathcal A_{\mathbf Q,s}\}$. The exact weight is
  therefore

  $$
  p_{H,s}(d)=\Pr\!\left(\bigcup_{\mathbf Q\in\mathcal T_s(d)}
                         \mathcal E_{\mathbf Q}\right).
  $$

  A fixed tuple does not make the cofactor-to-value map injective. For
  any admissible tuple of odd primes, $a=1$ and $a=2$ are admissible at
  sufficiently large $H$, and give the same totient and the same event,
  since $\varphi(2w)=\varphi(w)$ for odd $w$. A sum over cofactors with
  weights $1/\varphi(a)$ counts this contribution twice. More generally,
  the same duplication holds for every admissible odd $a$ for which $2a$
  also meets the size bound. This exact duplication does not by itself
  give a lower bound for its share of the limiting mass; it does rule out
  identifying the cofactor sum with the coefficient without correction.

  One exact grouping orders the finite set of tuples and replaces
  $\mathcal E_{\mathbf Q}$, for each $d$, by
  $\mathcal E_{\mathbf Q}\setminus
  \bigcup_{\mathbf Q'\prec\mathbf Q,\ \mathbf Q'\in\mathcal T_s(d)}
  \mathcal E_{\mathbf Q'}$. These disjoint events sum to $p_{H,s}(d)$,
  but their probabilities now depend on the competing tuples for $d$.
  Inside each tuple the sum must still be over distinct values
  $d_{\mathbf Q}(a)$, with the weight $1/d$ and the global minimum
  $\ell(d)$. Even the product identity
  $d_{\mathbf Q}(a)=\varphi(a)\prod_h(Q_h-1)$ needs coprimality:
  (2.5) allows $Q_P\mid a$. Proposition 5.3 at the cut $H$ concerns the long prefix
  before this retained tail, as $x\to\infty$ with $H$ fixed; by itself
  it does not assert uniqueness of the tail tuple under $\mu_{H,s}$ as
  $H\to\infty$.
  A phase-independent cofactor law must consequently be proved for this
  deduplicated, weighted measure, or accompanied by a uniform error for
  replacing it. L103 supplies the
  uniqueness and coprimality outside vanishing mass, and turns the
  duplication of $a$ and $2a$ into a sum over distinct cofactor totients
  $e$; the phase-independent cofactor law remains unproved.

### The finite-prime construction

The unrefereed, non-arXiv note *An explicit bound for Erdős problem 417*, posted on
10 October 2026
([PDF](https://github.com/LeanMeanBean/417/blob/3620821345595c5e2b60de4f86561e1872c81840/417.pdf)),
claims $\limsup V/V'<2.195202$ from Theorem 2.1 and Proposition 5.3 of the
unrefereed manuscript. It compares the mean of $v/\ell(v)$ with $V'/V$
and bounds prime divisibility of $\ell(v)$ by deleting a prime power.
Both pages were read, including the proof and numerical procedure; the
rational prime sum was not rerun, and no independent acceptance is recorded.

L44 carries the needed prime estimates into the coefficient itself. For
fixed squarefree $k$, define

$$
C_k(x)=\#\{v\le x:v\in\mathcal V,\ k\mid\ell(v)\},\qquad
b_{H,k}(s)=\sum_d\mu_{H,s}(d)\mathbf 1_{k\mid\ell(d)}.
$$

It proves $b_{H,k}\to b_k$ uniformly in $s$, where $b_k$ is continuous on
the circle and $C_k(x)/V(x)=b_k(\theta(x))+o(1)$. The construction uses
the common-prefix identity only after all its primes exceed those dividing
$k$; it then applies the manuscript's bounded-weight approximation. It
neither chooses a preferred witness nor replaces the global minimum.

For integers $Y\ge2$, put $P_Y=\prod_{p\le Y}p$ and

$$
Q_Y(s)=\sum_{k\mid P_Y}\frac{\operatorname{mobius}(k)}k b_k(s),
\qquad T_Y=\sum_{p>Y}\frac1{(p-1)^2}\le\frac1{Y-1}.
$$

Then L44 gives the explicit phase-uniform estimate

$$
0\le Q_Y(s)-q(s)\le T_Y,\qquad
\limsup_{H\to\infty}\sup_s
\mathbb E_{\mu_{H,s}}\bigl[w_Y(d)-g(d)\bigr]\le T_Y,       \tag{4}
$$

where $w_Y(d)=\prod_{p\le Y,\,p\mid\ell(d)}(1-1/p)$. The order of
limits is fixed $Y$ first, then $H\to\infty$. Thus large primes in the
weight can be discarded uniformly; the missing input is cancellation in
the single finite-prime weighted sum $Q_Y$. Constancy of every $b_k$ would
suffice but is stronger than needed, and no limiting distribution of the
whole least-preimage ratio is required. The marginal bounds
$b_2\le1/2$ and $b_p\le p/(p-1)^2$ impose no equality between phases.

### Why prime deletion does not give a dilation identity

Even the prime $2$ exposes the missing arithmetic comparison. For a
totient $u$, let $e(u)$ be its least even preimage, which always exists,
and let $o(v)$ be the least odd preimage of $v$, with value $+\infty$ if
there is none. An even global minimum for $2u$ must be divisible by $4$;
halving it gives an even preimage of $u$. Conversely, doubling an even
preimage of $u$ gives a preimage of $2u$. Hence, exactly,

$$
\ell(2u)=\min\{o(2u),2e(u)\},\qquad
C_2(x)=\sum_{\substack{u\le x/2\\u\in\mathcal V}}
             \mathbf 1_{\,2e(u)<o(2u)}.                    \tag{5}
$$

The two finite candidates have opposite parity, so there is no tie. Formula
(5) explains the bound $C_2(x)\le V(x/2)$ and its failure to be an
identity: for $u=4$, $e(4)=8$ and $o(8)=15$, so the summand is zero.
These minima follow by evaluating $\varphi(n)$ for $n\le15$; no claim
about an absent preimage is needed. The reciprocal least-preimage ratio
itself is not monotone under doubling:
$g(2)=2/3<g(4)=4/5$ but $g(8)=8/15<g(4)$. Thus monotonicity of this
elementary arithmetic operation supplies no phase coupling. Estimating
the indicator in (5) with the required phase control remains open here.

### Tail uniqueness and the cofactor fiber

[[theory/number_theory/L103_totient_tail_cofactor_factorization/_index|L103]],
a tier-0 conditional deduction, applies Proposition 5.3 at the cut $H$ and
again at the cut $P=\lfloor\log\log H\rfloor$, whose common prefix ends at
$Q_P$ and so contains every retained tail prime. Outside a set of data
whose normalized mass is at most $\epsilon_H+\epsilon_P$ as $x\to\infty$,
where $\epsilon_K$ is the rate of Proposition 5.3 at the cut $K$, every
witness of the tail totient $d$ has the same prime tuple $\mathbf Q$, the
prime $Q_P$ does not divide the cofactor, and

$$
d=e\prod_{h=P}^{H-1}(Q_h-1),\qquad
\ell(d)=\ell(e)\prod_{h=P}^{H-1}Q_h,\qquad e=\varphi(a)
$$

for every witness $(\mathbf Q,a)$. Such $d$ are called factorized. L103
also gives $q(\theta(x))$, up to an error tending to zero with $H$, as the
mean of $g(e)$ over the factorized data, with the manuscript's weights
$1/(d\prod_{i\le R}(p_i-1))$. Distinct values and the global minimum now
enter only through the cofactor totient $e$.

On a factorized $d$ the union in (2.7) has one event, which depends only
on $\mathbf Q$, so exactly

$$
\frac{p_{H,s}(d)}d=\frac{W_s(\mathbf Q)}e,\qquad
W_s(\mathbf Q)=\frac{\exp(-\gamma S_{\mathbf Q}/\alpha_s)}
                     {\prod_{h=P}^{H-1}(Q_h-1)},\qquad
S_{\mathbf Q}=\sum_{h\ge H}\rho^hD(h,\mathbf Q).
$$

Passing L103 from the manuscript's data to the coefficient's measure
$\mu_{H,s}$ needs Lemma 6.4 and Proposition 6.5 for the indicator of the
factorized set, which is not a function of $\ell(d)/d$. Their proofs bound
the absolute difference between prime sums and volumes for each tail
totient separately and sum these bounds over all tail totients and
witnesses, so they appear to apply verbatim to every weight in $[0,1]$ that
depends only on $d$ and the phase. With that reading of the two proofs as an
additional premise, the $\mu_{H,s}$-mass of the nonfactorized tail totients
tends to zero uniformly in $s$, and

$$
q_H(s)=\frac{\sum_{(\mathbf Q,e)}W_s(\mathbf Q)\,g(e)/e}
            {\sum_{(\mathbf Q,e)}W_s(\mathbf Q)/e}+o_H(1)
=\sum_{\mathbf Q}\pi_{H,s}(\mathbf Q)\,m_{H,s}(\mathbf Q)+o_H(1),
                                                              \tag{6}
$$

uniformly in $s$, where the sums run over the pairs given by factorized
tail totients. Here $m_{H,s}(\mathbf Q)$ is the mean of $g(e)$ with weights
$1/e$ over the cofactor totients $e$ paired with $\mathbf Q$, and
$\pi_{H,s}(\mathbf Q)$ is proportional to $W_s(\mathbf Q)$ times their
total weight. The pairs do not form a product set, since whether
$e\prod_h(Q_h-1)$ is factorized depends on all its witnesses.

In (6) the phase enters in three places: the bands and simplex conditions
of (2.5) on $\mathbf Q$; the threshold factor $\gamma/\alpha_s$ in
$W_s(\mathbf Q)$; and the cofactor conditions $P^+(a)\le Q_P$ and
$\log a\le\exp(2\alpha_sP\rho^{-P})$, which define the fiber. The scale
covariance above matches the continuous regions by rescaling the
coordinates $v_h$. It does not yet match the discrete factorized pairs:
the fiber restriction also affects their total weights. Both the laws
$\pi_{H,s}$ and the fiber means $m_{H,s}$ require comparison, including a
uniform estimate for the prime-sum error with this restriction.

**The fiber at its own scale.** Put $Y=Q_P$. One possible route would
replace the restricted cofactor fiber by all totient values below an
appropriate power of $Y$, with harmonic weight $1/e$. In that unrestricted
sum, partial summation would involve the counting coefficients
$G_{m(t)}A(1;\theta(t))$ in the variable $\log\log t$. If their mass
concentrated within $O(1/P)$ of the upper double-logarithmic scale, the
continuity of $q$
([[theory/number_theory/L43_continuous_totient_phase_ratio/_index|L43]])
would suggest the following fiber identification:

$$
m_{H,s}(\mathbf Q)=q\bigl(\psi(\log\log Q_P)\bigr)+o(1)
\qquad(P\to\infty).                                           \tag{7}
$$

Equation (7) is a proposed estimate, not an established harmonic inner
limit. It requires control of nonfactorized pairs inside the fibers,
counted with their multiplicity, which the distinct-value mass bound of
L103 does not give; the cofactor smoothness and size restrictions near
$Y$; and the weighted concentration just described. An error tending to
zero after averaging with $\pi_{H,s}$, uniformly in $s$, would suffice in
place of a pointwise estimate for every fiber. None is proved here. With
$\log\log Q_P=(1+\epsilon_P)\alpha_sP\rho^{-P}$ and $|\epsilon_P|\le0.1$
by the band, a direct calculation from $\psi(B)=(\log B-\log\log B)/\lambda$
gives

$$
\psi(\log\log Q_P)=P+s+\frac{\log(1+\epsilon_P)}\lambda
+O\Bigl(\frac{\log P}P\Bigr).                                 \tag{8}
$$

If these comparisons were established uniformly in phase, (6)–(8) would
express $q$ through itself:

$$
q(s)=\lim_{H\to\infty}\sum_{\mathbf Q}\pi_{H,s}(\mathbf Q)\,
      q\Bigl(s+\frac{\log(1+\epsilon_P(\mathbf Q))}\lambda\Bigr), \tag{9}
$$

a proposed renewal relation through the cofactor fiber whose kernel is supported in
$[\log(0.9)/\lambda,\log(1.1)/\lambda]\subset[-0.18,0.16]$.

**What a degenerating renewal kernel would give.** Ford's deviation estimate behind the
manuscript's (3.7), applied at the single level $P$, bounds the proportion
of values for which some preimage has $|\epsilon_P|>\eta$ by
$O_\eta(e^{-c\eta^2P})$. Under the same reading of Lemma 6.4 and
Proposition 6.5, a kernel obtained from these weighted data would therefore
tend to the point mass at zero. In the unrestricted continuous simplex
model of Lemma 3.4 the coordinate at level $P$ is
about $\alpha\rho^{-P}$ times a sum of $P+1$ exponential variables, so
$\epsilon_P$ has spread of order $P^{-1/2}$ and the kernel of order
$1/(\lambda\sqrt P)$. This variance description has not been transferred
to the restricted fibers. An identity of the form (9) for any kernels
concentrating at zero is satisfied by every continuous function on the
circle and decides nothing by itself.

One sufficient quantitative route is the following. Suppose that for phase-free
probability kernels $\kappa_P$ on $[-0.18,0.16]$ with
$\int(1-\cos2\pi nt)\,d\kappa_P(t)\gg_n1/P$ for every $n\ne0$, as for a
spread of order $P^{-1/2}$, one had

$$
q(s)=\int q(s+t)\,d\kappa_P(t)+r_P(s),\qquad
\sup_s|r_P(s)|=o(1/P).
$$

Taking Fourier coefficients, $\hat q(n)(1-\hat\kappa_P(n))=\hat r_P(n)$
with $|1-\hat\kappa_P(n)|\gg_n1/P$ and $|\hat r_P(n)|=o(1/P)$, so every
nonzero Fourier coefficient of $q$ vanishes and $q$ is constant. A kernel
that depends on the phase would need a further mixing argument. The
premises supply no such rate. Theorem 2.1 and L65 carry none. The
manuscript's coverage bound at a cut $K$ is $e^{-cP_K}$ with
$P_K=\lfloor\log\log K\rfloor$. In its existing estimates, the smooth
cofactor below $P_K$ costs
$K_K=\exp(CP_K\rho^{-P_K})$, which the $K^{-2}$ saving of Proposition 3.8
must absorb. Applying that coverage estimate at a cut of order
$m(Q_P)\approx P$ gives an upper bound of order $(\log P)^{-c}$, which
does not supply the $o(1/P)$ error needed by this Fourier argument. This
is a limitation of the available bounds, not a lower bound on the actual
error or an obstruction to every possible coupling.

### What the rectangle estimate can compare

Theorem 2.1 of the
[[../library/arithmetic_functions/plasma_ai_2026_normal_order_number_iterations_euler_s_function/_index|totient-iteration paper]]
compares divisibility of $p-1$, for $x<p\le2x$, by one to three distinct
large primes with harmonic weights. Its coefficient is independent of $p$
and of the last prime. Section 3, Proposition 3.2, sums over an auxiliary
prime to allow arbitrary bounded weights on one or two large factors in its
truncated regions, with error $O((\log\log x)^{-7})$. Its hypotheses and
the auxiliary-prime deduction were read; its underlying analytic proof has
not been independently examined here. A collision between products of
several shifted primes is not an event about divisibility of a single $p-1$
without another reduction.

The direct identification of the primes in (3) with those of the rectangle
estimate fails uniformly in phase. With $T=\log\log x=B$, Theorem 2.1 admits
only prime factors $q>x^{cT^{-20}}$, that is
$\log\log q\ge B-20\log B+\log c$, and Proposition 3.2 only factors above
$x^{T^{-6}}$. Every retained tail prime satisfies
$\log\log Q_h\le1.1(\lambda/\rho)(H-1)\rho^{-(H-1)}$ and every cofactor
$\log a\le\exp(2(\lambda/\rho)P\rho^{-P})$, bounds depending on $H$ alone,
while the prefix primes after $p_0$ satisfy $\log\log p_i\le0.61B$. For all
large $x$ the only prime of a basic preimage in the admissible range is
therefore $p_0$. Applying the estimate with $p=p_0$ observes large factors
of $p_0-1$, whereas the remaining statistic is a function of the tail and
its cofactor. In particular fixed primes $q\le Y$ eventually lie below
the allowed range. This direct use supplies neither constancy of the
$b_k$ nor a certified error for the finite cut. An indirect encoding or
application at another scale is not excluded, but would owe an exact
allowed observable, a comparison with (6), and a phase-uniform omitted-mass
bound. None has been constructed. Also, the coverage error relevant to
the proposed renewal argument comes from Proposition 3.3 and Ford's band
deviations at the lowest retained levels; the shifted-prime collisions of
Proposition 5.1 already cost less than every power of $H$. Improving only
that collision bound would leave the coverage estimate unchanged.

### Finite ranges and finite cuts

The phase is $\theta(x)=\psi(\log\log x)-m$ with
$\psi(B)=(\log B-\log\log B)/\lambda$, where $\lambda=\log(1/\rho)\approx
0.6114$ and $\rho\approx0.5426$ is the root of $\sum_ja_j\rho^j=1$. The
function $\psi$ decreases for $B<e$ and increases for $B>e$, with minimum
$1/\lambda\approx1.636$ at $B=e$, that is at $x=\exp(e^e)\approx
3.8\cdot10^6$. Hence $m(x)=1$ for $x$ between about $150$ and about
$10^{213}$, and for $10^4\le x\le10^7$ the phase stays between $0.635$ and
$0.675$. The finite-range values of $R(x)$ recorded above therefore sample
one narrow window of the circle. They neither cover a whole period nor
come with an asymptotic error small enough to certify phase dependence or
its absence. The next period, $m=2$, runs from about $10^{213}$ to about
$\exp(7.6\cdot10^7)$.

The available finite-cut estimates do not supply the certificate described
in the stop verdict. The manuscript bounds its cut errors only by rates such as
$e^{-cP}$, with $P=\lfloor\log\log H\rfloor$ and an unspecified constant
$c$, for cuts that are sufficiently large in an unspecified sense. Already
$P\ge2$ needs $H\ge e^{e^2}>1618$ retained levels, whose largest tail
primes have double logarithm about $\alpha_s(H-1)\rho^{-(H-1)}$. No
direct enumeration at such cuts is available here, and an evaluated
difference would still have to exceed an unquantified cut error.

### An incomplete continuous model

The continuous simplex does not include deduplication or global least
preimages. One can illustrate possible smoothing by replacing a low
coordinate by a sum $X_h$ of $h+1$ independent exponential variables of
mean one. In this equal-weight model,

$$
\mathbb E X_h^{it}=\frac{\Gamma(h+1+it)}{h!}.
$$

Thus convolution in the logarithmic coordinate damps frequency $t$ by
$|\Gamma(h+1+it)|/h!$. At a phase frequency the corresponding value is
$t=2\pi n/\lambda$. This exact identity in the model supplies no estimate
for (1): neither the observable $g$ nor the restricted law in (6) has
been transferred to it. In particular the model gives no reason to assert
that any Fourier coefficient of $q$ is nonzero, or to estimate its size.

## Stop verdict and reopening conditions

The bounded structural test reaches neither conclusion, and this route is
blocked. By L43 the exact missing identity is

$$
\lim_{H\to\infty}\int_0^1 q_H(s)\,e^{-2\pi ins}\,ds=0
\qquad(n\ne0).                                                \tag{10}
$$

Equivalently, by the proved truncation (4), the exact remaining estimate is

$$
\lim_{Y\to\infty}\left(\sup_s Q_Y(s)-\inf_s Q_Y(s)\right)=0. \tag{11}
$$

This is a criterion, not an assumed decoupling theorem. A phase-independent
limit for each fixed finite-prime pattern would be sufficient; cancellation
of just the weighted sums in (11) would also suffice. Neither has been
constructed. A disproof needs some $n\ne0$ for which the limit in (10) is
nonzero. By uniform convergence it would follow from one cut $H$ whose
integral in (10) exceeds $\sup_s|q_H(s)-q(s)|$ in modulus, or from
two phases with $|q_H(s_1)-q_H(s_2)|>2\sup_s|q_H(s)-q(s)|$. The
manuscript's cut errors tend to zero without certified numerical bounds,
so the finite formula alone supplies no such inequality. At the finite-prime
level, set $Q_{H,Y}(s)=\mathbb E_{\mu_{H,s}}w_Y$ and
$\delta_{H,Y}=\sup_s|Q_{H,Y}(s)-Q_Y(s)|$. A concrete sufficient certificate
is $Q_{H,Y}(s_1)-Q_{H,Y}(s_2)>T_Y+2\delta_{H,Y}$: the one-sided
bound (4) then gives $q(s_1)>q(s_2)$. L44 proves
$\delta_{H,Y}\to0$ for fixed $Y$, but gives no certified finite-cut
value for it.

The two bounded tests of the cofactor interface end as follows. The direct
rectangle application does not compare the phases, because its admissible
primes miss every prime of a preimage below the largest. The coupling test
succeeds only structurally: L103 gives tail uniqueness, coprimality and the
multiplicative least preimage outside vanishing mass. Equation (6) also
uses the explicitly stated extension of the prime-sum comparison; (7)
and (9) remain proposals requiring additional fiber estimates. The
exact blocked comparison is the difference of the fiber means of (6) at two
phases,

$$
\lim_{H\to\infty}\Bigl(\sum_{\mathbf Q}\pi_{H,s_1}(\mathbf Q)\,
m_{H,s_1}(\mathbf Q)-\sum_{\mathbf Q}\pi_{H,s_2}(\mathbf Q)\,
m_{H,s_2}(\mathbf Q)\Bigr)=0\qquad(0\le s_1,s_2<1),          \tag{12}
$$

which is equivalent to the constancy of $q$ under the stated premise for
(6). The Fourier route through (9) would suffice with a phase-free kernel,
the displayed lower bound on its Fourier damping, and an error $o(1/P)$
uniformly in phase. The available coverage bound of order
$(\log P)^{-c}$ does not supply that error. No certified phase comparison
or finite-cut separation has been obtained.

Arguments tried that do not close the gap:

- separate constancy of the two coefficients, which L43 excludes;
- fixed dilation and the pair constructions for Problem 416, which compare
  arguments at a single phase;
- the common-prefix proposition and Lemma 6.4, whose bounds hold at each
  phase;
- factorization over independent witnesses, which the union and the
  minimum over all preimages forbid;
- prime deletion, which gives upper bounds but leaves the global-minimum
  comparison in (5);
- tail uniqueness at two cuts (L103), which removes the union, the
  duplicated cofactors and the coprimality question but leaves the fiber;
- descent through the tail and the cofactor: the proposed renewal relation
  (9) still needs a weighted fiber comparison, and even a rateless version
  would be compatible with every continuous $q$ if its kernel tends to a
  point mass;
- the rectangle estimate of the totient-iteration paper, whose admissible
  primes miss the tail.

Reopen the constancy direction on a theorem that the distinct-totient
structure at bounded levels is asymptotically invariant under rescaling the
double-logarithmic grid, for example a renewal or mixing statement for the
smallest prime factors of least preimages that is uniform in the phase, or on
an exact identity expressing $\#\{v\le x:k\mid\ell(v)\}$ through values of
$V$ at fixed dilates, or on a one-sided comparison of phases, such as a
coupling of $\mu_{H,s}$ and $\mu_{H,s'}$ for $s\le s'$ under which $g$ does
not decrease up to $o(1)$; by L43 any such monotonicity forces constancy,
because $q$ returns to $q(0)$ at the end of the period. For the renewal
route specifically, reopen on (9) with an error $o(1/P)$ uniformly in
phase, for a phase-free kernel or with a mixing argument for a
phase-dependent one. A sufficient implementation would control the
coverage, fiber restriction and counting errors at a cut $K$ by $o(1/K)$;
improving the shifted-product collision estimate alone does not do this.
These rates describe one route, not a necessary condition for every
possible proof. Reopen the nonconstancy direction on an evaluated phase
gap exceeding the explicit prime truncation bound and a certified cut
error, or on an exact asymptotic
for a nonzero Fourier coefficient of $q_H$. The continuous model supplies
no estimate of that coefficient. Finite-range stability of $R$ and
finite-cut differences do not settle either direction. Either outcome
remains conditional on the unrefereed manuscript, requires
independent scrutiny of the whole catalog formulation before any solution
claim, and leaves the status of Problem 416 unchanged.

## Current review

Needs update. The coefficient reduction L65, the continuity result L43, the
finite-prime reduction L44, the tail factorization L103, the
finite-coefficient test with its grouped cofactor, cofactor fiber and
rectangle-estimate interfaces, the sections on finite ranges and on the
incomplete continuous model, and the stop verdict above are
author-recorded and outside the scope of the existing review.
The earlier route was independently reviewed on 2026-09-28 in the review
record
[[research/erdos_416/evidence/verify/connections_problem_417_the_two_counts_of_distinct_totients_review|the Problem 417 review]],
whose subject is the Problem 417 section of the connections page together with
this lead, and graded in
[[research/erdos_416/evidence/verify/connections_grade|the grade]], which
records this lead as reviewed. The graded verdicts of the statements the route
rests on, in the review's numbering, are these. Lemma 417.1 (S1):
refutation-failed, its three parts re-derived. Proposition 417.2 (S2):
refutation-failed under (W), the order of magnitude $V\asymp V'$ that the finite
upper endpoint needs, with the Problem 49 folder's Lemma 4.1 route as the
alternative. Theorem 417.3 (S3): refutation-failed, the witness $54$
re-enumerated and the sum of $V$ along the scales re-derived under the
derivative bound on its proved range. Proposition 417.4 (S4): refutation-failed
as a conditional on (P1). The frame without a support bound (S6(a)), as this
page states it: refutation-failed. The finite-range numbers (S7(a)):
refutation-failed, every figure reproduced. This page's route, inputs, premises
and gap (S8): refutation-failed, with its cross-reference to the Problem 49
connections page checked by the grader. Two sentences of the section that this
page does not carry were refuted-as-stated: the support clause $G(t)=1$ for
$t\ge2$ of the frame's hypothesis (S6(b); Ford's witness $2^{18}\cdot257$ at
$k=4$ gives a positive proportion of totients with least-preimage ratio above
$2$) and the sentence placing every element counted by $V_0(x)$ in $(x/2,x]$
(S7(b); witness $v=5888$ with least preimage $11985$ at $x=11900$). The grade's
corrections C1, C2 and C3 were applied to the connections page (the range of the
imported derivative bound, which no proof uses; the frame's hypothesis (H2) and
its display, now without a support bound; and the confinement sentence), so its
current text differs from the reviewed text at those places; no correction
changes the reviewed assertions retained here. The premises (P1) and the
distributional part of (P2) remain provisional. No tier is assigned by those
reviews, and the problem's status is open.
