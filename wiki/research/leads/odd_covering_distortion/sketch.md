---
name: research/leads/odd_covering_distortion/sketch
title: Proof sketch for odd covers along prime-power digits
desc: |
  Canonical conditional route for distinct odd coverings. The universal
  138.877 small-prime certificate is false by an explicit concentration
  example. The exact-loss tail remains valid; the open obligation is a
  supported measure satisfying its system-functional bounds at every
  small-prime depth and residue assignment.
created: 2026-10-16T13:49:49Z
updated: 2026-10-16T13:49:49Z
---

# Proof sketch for odd covers along prime-power digits

***

This is the canonical sketch of the
[[research/leads/odd_covering_distortion/_index|odd-covering distortion lead]],
author-recorded by Plasma AI and unreviewed. The target remains unresolved.
The universal small-prime certificate at $138.877$ is false. A more flexible
route through the exact-loss tail remains conditional on an unproved measure
construction.

## Target and common definitions

[[problems/covering_systems/E0007/_index|Problem 7]] asks whether finitely many
congruence classes with pairwise distinct odd moduli greater than one can
cover $\mathbb Z$. The proposed conclusion is that no such family covers.
A positive resolution would require an explicit family and a proof covering
one full period; no such family is supplied here.

For a common period $N$, the
[[research/leads/odd_covering_distortion/digit_sieve|digit page]] identifies
$\mathbb Z/N\mathbb Z$ with the box $Q(N)$ of base-$p$ digits. A modulus $d$
fixes the first $v_p(d)$ digits at each prime. Distinct moduli give distinct
prefix shapes. Missing classes modulo the primes can be added, and their
first-digit values deleted. The resulting small-prime box $Q_s$ has $p-1$
values at the first digit and $p$ at each later digit, for the odd primes
through $73$. Let $R$ be the part of $Q_s$ avoiding all small-prime classes.

For a prefix shape $Y$, its pair weight is

$$
W(Y)=\prod_p(2t_p(Y)+1).
$$

It counts ordered pairs of prefix shapes whose union is $Y$. Class-mass
bounds must cover every such shape, including shapes absent from the exposed
family but possible in a later intersection.

A small-prime *system* $S$ chooses one cylinder $H_b$ of each prefix shape,
including $H_\varnothing=Q_s$, and $w_S(x)=\sum_b\mathbf1_{H_b}(x)$.
For a probability $P$ on $Q_s$, the
[[research/leads/odd_covering_distortion/point_kernel|system interface]] uses

$$
\sigma(P)=\max_S\mathbb E_Pw_S^2,
\qquad
\Phi_P^\delta(c)=\frac1{1-\delta}\sup_S
                  \mathbb E_P(cw_S-\delta)_+.
$$

The systems in these suprema can be future large-prime projections; they are
not restricted to the classes that have already been removed.

## Held links

1. **Digit reduction.** The prime-power digit correspondence turns a distinct
   odd cover into a nonparallel prefix-cylinder cover. This is Lemma 1 of the
   digit page, an elementary CRT argument, consistent with the
   [[../library/covering_systems/berger_1986_necessary_condition_odd_covering_systems/prime_adic_boxes|Berger–Felzenbaum–Fraenkel
   box correspondence]].
2. **Distortion sieve.** The digit page derives preservation of old marginals,
   the pointwise distortion cap, the identity
   $\mathbb P_k(B_k)=\mathbb E_{k-1}(\alpha_k-\delta_k)_+/(1-\delta_k)$,
   and survival whenever the summed losses are less than one. It records
   the extension from the source's $\delta_k\le1/2$ to $\delta_k<1$.
3. **Second-moment tail.** Lemma 2 of the system-interface page proves, for
   every $k>21$, the bound
   $M_k^{(2)}\le\sigma(P)/(p_k-1)^2$ times the product of earlier
   large-prime distortion factors. It permits arbitrary exponents and residue
   assignments, and every subsequent legal distortion. For a particular
   family, its smaller actual-system constant $\kappa^*$ can replace
   $\sigma(P)$.
4. **Exact-loss tail.** Lemmas A and B of the
   [[research/leads/odd_covering_distortion/exact_loss_tail|exact-loss page]]
   give a convex-order comparison for weighted cylinder indicators under
   sequential conditional-mass bounds. Its Theorem C applies this to every
   large-prime loss. Corollary D joins finitely many such exact bounds to
   the source's second-moment recurrence and termination theorem. Its
   Corollary E, with an outward rational certificate, proves that uniform
   surviving density at least $1/4$ in $Q_s$ suffices.

The native deductions have author standing only. The imported tail results
are from the published BBMST square-free paper, Algebra & Number Theory 15
(2021), and the published density paper, Inventiones 228 (2022), at the
versions and read scope identified on their library pages. No conditional,
rejected, or pending outside E7 assertion is a premise.

## The remaining end-to-end candidate

Given any finite odd family, extract its $73$-smooth classes. For every such
family, at every finite depth vector, construct a probability $P$ supported
on $R$, an integer $K>21$, and distortions $\delta_k\in(0,1)$ for
$21<k\le K$. For independent agreement depths $g_i$ with

$$
\Pr(g_i\ge t)=\min\{1,p_i^{-t}/(1-\delta_i)\}\quad(t\ge1),
\qquad N_k=\prod_{21<i<k}(g_i+1),
$$

establish valid upper bounds on $\Phi_P^{\delta_k}(N_k/(p_k-1))$ giving

$$
\mu_K=1-\sum_{21<k\le K}
\mathbb E\,\Phi_P^{\delta_k}\!\left(\frac{N_k}{p_k-1}\right)>0.
$$

The same definitions must give a bound for

$$
f_K=\frac{\sigma(P)}{\mu_K}
\prod_{21<i\le K}
\left(1+\frac{3p_i-1}{(1-\delta_i)(p_i-1)^2}\right)
$$

from which the source's
[[../library/covering_systems/balister_2018_erdos_covering_problem_density_uncovered_set/lemma_6_2|Lemma
6.2 recurrence]] reaches the termination criterion of its
[[../library/covering_systems/balister_2018_erdos_covering_problem_density_uncovered_set/theorem_6_1|Theorem
6.1]], with positive survival throughout. Subsequent distortions use the
source's range $(0,1/2]$. Families ending earlier are handled by survival at
their last stage, or by appending free prime coordinates.

**Open obligation.** Construct this $P$ and these bounds uniformly over all
small-prime configurations and depths. The measure and schedule may depend on
the configuration. A favorable sample, an exponent cap, or a product model
with unspecified support does not prove the obligation.

**Established case.** If uniform measure $U$ on $Q_s$ has $U(R)\ge1/4$,
take $P=U(\,\cdot\mid R)$ and $\delta_k=2/5$ through $p_{2262}=19997$.
Corollary E certifies positive mass and $f_{2262}<94000$, below the certified
lower bound $101000$ for the source's termination threshold. This includes
the concentration example
that refutes the old $138.877$ demand. Its 16-class extension has
$0<U(R)<1/4$, so this established case does not cover all configurations.
For that extension, an adapted product subset has surviving relative density
at least $24005/28512$; conditioning its uniform measure on $R$ also satisfies
Corollary D, with certified $f_{2262}<21000$.

**Composition.** If this obligation holds, start the sieve at $P$. All
small-prime classes have zero mass. Theorem C bounds the exact phase, and
Corollary D supplies positive survival through every remaining prime. The
original family misses a residue modulo its period and cannot cover the
integers. This is a complete conditional implication with an unproved
antecedent; it is not a proof of E7.

## The refuted stronger certificate

The stronger Step 3 asks for a small-prime sieve with valid cylinder bounds
$c_{21}(Y)$, losses $L_k\ge\mathbb P_k(B_k)$, and

$$
\mu_{21}=1-\sum_kL_k>0,\qquad
\kappa=\sum_YW(Y)c_{21}(Y),\qquad
\kappa/\mu_{21}\le138.877.
$$

Here index $21$ denotes the prime $73$, not a digit count. These conclusions
would satisfy the retained
[[../library/covering_systems/balister_2021_erdos_selfridge_problem_square_free_moduli/corollary_5_2|Corollary
5.2]] tail interface. Conditioning the final measure on $R$ would also give
Step 3*: a supported probability with $\sigma(P)\le138.877$.

Both universal demands are **false**, by the
[[research/leads/odd_covering_distortion/support_concentration|support
concentration construction]]. A valuation form of Harrington's repeated-3
example supplies a distinct odd family, with primes through 73 and depth 16,
whose nonempty uncovered set has first 3-digit fixed. Averaging the point
kernel over centres in that branch forces $k(P)>152.14$ for every supported
$P$, and $\sigma(P)\ge k(P)$. This is an actual residue configuration,
independent of any choice of moment bounds, digit order, or initial block.

The source's square-free certificate remains valid in its own domain: its
[[../library/covering_systems/balister_2021_erdos_selfridge_problem_square_free_moduli/lemma_5_3|Lemma
5.3]] and
[[../library/covering_systems/balister_2021_erdos_selfridge_problem_square_free_moduli/lemma_5_4|Lemma
5.4]] give $f_{21}\le138.874$. Its
[[../library/covering_systems/balister_2021_erdos_selfridge_problem_square_free_moduli/remark_p625|higher-power
remark]] permits arbitrary exponents above 73, not at the small primes.
The counterexample does not contradict those hypotheses or conclusions.

## Failure account and next discriminating question

- **Failed link:** the universal $138.877$ small-prime certificate and its
  Step 3* relaxation, with the retained class bounds and pair weights.
- **Reason:** an explicit distinct family forces survivor concentration at 3;
  every supported measure exceeds the required system constant. The missing
  input at that constant is false, not merely unproved here.
- **Surviving route:** the exact-loss tail and a configuration-dependent
  supported measure satisfying Corollary D. Its existence is unknown. It
  includes nonemptiness of the $73$-smooth uncovered set, which is itself
  part of the target problem.
- **Resolved test:** uniform conditioning on the concentration example
  satisfies Corollary D, since its density is at least $773/1920$.
  The exact certificate bounds the supremum over systems, includes every
  depth through stochastic domination, and reaches a certified infinite-tail
  termination criterion. A product measure adapted to the first-digit
  constraints also handles its 16-class extension, whose uniform density
  falls below $1/4$.
- **Next test:** for a configuration with $U(R)<1/4$, construct a supported
  measure with simultaneous bounds on $\Phi_P$ and $\sigma(P)$, and prove
  how that construction applies without an exponent or residue restriction.
  The explicit examples show how product subsets can help, but give no
  uniform selection rule. A tail calculation on a favorable concentrated system alone does not bound
  the supremum over systems, and solving one configuration does not prove
  the universal measure assertion.

The [[research/leads/odd_covering_distortion/cube_free_obstruction|cube-free]]
and [[research/leads/odd_covering_distortion/deep_digit_obstruction|depth-four]]
results remain scoped exclusions of complete-prefix moment models. A larger
block or a different loss bound can escape those model assumptions, but cannot
repair the refuted universal $138.877$ condition with the same definitions.
The [[research/leads/odd_covering_distortion/e273_calibration|exact E273
calibration]] is a finite-domain success and supplies no missing E7 premise.

The exact-loss page's floating-point inflation experiments suggest extra room,
but do not certify a uniform replacement threshold or a supported measure.
They truncate distributions and cover only the prime ranges stated there.
A full proof must retain the same loss, system, and distortion definitions at
every interface and justify its entire remaining-prime tail.
