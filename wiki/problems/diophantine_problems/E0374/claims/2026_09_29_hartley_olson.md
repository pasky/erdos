---
name: problems/diophantine_problems/E0374/claims/2026_09_29_hartley_olson
title: Hartley and Olson's orders of growth of the factorial classes
desc: |
  Hartley and Olson show that $D_3(X)\asymp\sqrt X$ and $D_k(X)\asymp X$ for
  $k=4,5,6$, the order of growth of $D_k$ for every $k$ from 3 to 6, including
  the Erdős–Graham conjecture that $D_6$ has positive lower density. It is
  accepted on Jacob Parish's review and on the corpus's build and audit of its
  Lean.
authors:
- Jonathan S. Hartley
- Matthew A. Olson
status: accepted
claim: answered
scope: full
evidence:
- reviewed
- formalized
submitted: 2026-10-02
links:
- url: https://papers.ssrn.com/sol3/papers.cfm?abstract_id=7537279
  kind: preprint
  date: 2026-09-29
- url: https://github.com/jon-hartley/erdos374_lean_verification/blob/2453326558a5a197ccf500796f849d143de0c108/paper/A_Resolution_of_Erdos_374.pdf
  kind: preprint
  date: 2026-10-06
- url: https://github.com/jon-hartley/erdos374_lean_verification/tree/2453326558a5a197ccf500796f849d143de0c108
  kind: formalization
  date: 2026-10-06
- url: https://www.erdosproblems.com/forum/thread/374/proof-claims#proof-claim-385
  kind: discussion
  date: 2026-10-02
created: 2026-10-07T07:03:21Z
updated: 2026-10-08T03:53:38Z
---

***

**Claim.** Let $\mathcal A$ be the set of squarefree $m$ such that
$\gcd(m,q_a)^2\le q_a$ for every $a\ge2$, where $q_a$ is the squarefree part
of $a!$, the product of the primes dividing $a!$ to an odd power (the paper
writes it $\operatorname{sf}(a!)$ and, in its Section 7, calls it a kernel).
Theorem 1.1 of the paper: $\mathcal A$ has a positive natural density
$\delta_A$, the members of $\mathcal A$ up to $X$ with a prime factor above
$m^{99/100}$ that lie in $D_6$ number $(\delta_A\log(100/99)+o(1))X$, and so
the lower density of $D_6$ is at least $\delta_A\log(100/99)>0$. This answers
the example question of
[[problems/diophantine_problems/E0374/_index|Problem 374]], the conjecture of
Erdős and Graham that $D_6(X)\gg X$; the paper's own statement adds that it
neither asserts that $D_6$ has a natural density nor gives an effective value
of $\delta_A$. The source is J. S. Hartley and M. A. Olson, *A Resolution of
Erdos 374*; by the paper's title footnote, the first version, containing
Theorem 1.1, was posted on SSRN on 2026-09-29. The revised paper is in the
`paper/` folder of the repository linked above, first committed on 2026-10-04;
the page follows it at the pinned commit of 2026-10-06. The revised paper
extends the claim: its Theorem 7.1 adds, for every $\varepsilon>0$,
$D_3(X)=\kappa_3\sqrt X+O_\varepsilon(X^{2/5+\varepsilon})$ with
$\kappa_3=\sum_{q}q^{-1/2}=2.70975\ldots$ over the distinct values $q_a\ne1$
of the squarefree parts, and lower densities at least $1/4$ for $D_4$ and
$\log2/40000$ for $D_5$, so that $D_3(X)\asymp\sqrt X$ and $D_k(X)\asymp X$
for $k=4,5,6$, the orders of growth the problem asks for. The forum claim of
2026-10-02, labeled partial, described only the positive lower density of
$D_6$; the revised paper and the claimant's comment of 2026-10-05 assert the
whole determination, which is the claim this page records.

The argument runs as follows. Canceling squares turns a five-factorial product
$a!b!c!d!m!$ with $a<b<c<d<m$ into the condition that $q_aP_h(c)P_\ell(m)$ be
a square, where $P_h(t)=t(t-1)\cdots(t-h+1)$, $h=c-b$ and $\ell=m-d$, so every
representation is governed by two blocks of consecutive integers (four
factorials being the case $a=0$). The gcd conditions defining $\mathcal A$
rule out exactly the paired representations $q_a c m=\square$ with $c<m$, and
$\mathcal A$ has a positive natural density because the squarefree integers
failing the $a$th condition are divisible by a divisor of $q_a$ above
$\sqrt{q_a}$, so the proportion failing it is at most
$2^{\omega(q_a)}/\sqrt{q_a}\le\exp(-(1/4-o(1))a)$, since
$\log q_a\ge(1/2+o(1))a$ and $\omega(q_a)=O(a/\log a)$, a bound summable in
$a$. The squarefree integers with no prime factor up to $B$ meet every
condition with $a\le B$ and have density $\asymp1/\log B$, more than the
$O(\exp(-cB))$ removed by the conditions with $a>B$ once $B$ is large, and the
densities for finitely many conditions converge uniformly to that of
$\mathcal A$. For an endpoint $m$ with a prime factor above $m^{99/100}$ the
remaining representations are handled in two steps: a lemma on the logarithmic
mass of the primes dividing a long block exactly once, proved with the
equidistribution theorem of Matomäki, Radziwiłł, Shao, Tao and Teräväinen for
sums over primes of smooth functions of $N/p$ and $M/p^2$, shows that the
lower block cannot be much longer than the upper one, and the largest prime
below $m$, which Harman's almost-all theorem on primes in short intervals
places within $m^{11/100}$ of $m$ for all but $o(X)$ endpoints, forces the
upper block to be that short; the surviving short-block representations are
then counted by a sieve anchored at the large prime factor of $m$, in which
Weil's bound for quadratic character sums of polynomials and the analytic
large sieve show that only $o(X)$ endpoints admit one. The six-factorial
identity of Erdős and Graham supplies a representation of length six for each
of these $m$, so $F(m)=6$ for a proportion $\delta_A\log(100/99)+o(1)$ of the
integers up to $X$, the factor $\log(100/99)$ arising from the sum over the
cofactors $m/p$ of the large prime factor $p>m^{99/100}$.

**Submission note.** Posted to erdosproblems.com as a proof claim by Jusvin
Dhillon, Jonathan S. Hartley, Matthew A. Olson (account jonhartley) on 2 October
2026, giving "ChatGPT Astra; Google’s Gemini 3.1 Pro and Gemini 3.8 Flash;
Anthropic’s Claude Opus 5.5 and Claude Fable 5.1; xAI’s Grok 4.7" as the AI
used:

> Hartley, Olson, and Dhillon give a proof that \(D_6\) has positive lower
> density, proving the Erdős–Graham conjecture \(D_6(X)\gg X\). They construct a
> positive-density family of squarefree integers with a very large prime factor,
> excluding the principal paired representations. Other four- and five-factor
> representations reduce to two intervals of consecutive integers. A
> reciprocal-prime equidistribution theorem of
> Matomäki–Radziwiłł–Shao–Tao–Teräväinen, together with Harman's short-interval
> theorem, forces both intervals to be short for almost all endpoints. The large
> prime factor then anchors the remaining square condition; Weil's bound and the
> large sieve show that the exceptions are \(o(X)\). The Erdős–Graham six-factor
> identity then gives \(F(m)=6\) for a positive proportion of integers. Posted
> to SSRN on 29 Sep 2026.

**Authorship and the parallel proof.** The forum claim of 2026-10-02 names
three claimants, Dhillon, Hartley and Olson; the paper at the pinned commit
lists Hartley and Olson, after a commit of 2026-10-06 that updated the author
list, and this page follows the paper. The title footnote records that
[[problems/diophantine_problems/E0374/claims/2026_10_01_yudin|Yudin]]
independently proved the positive lower density of $D_6$, the bound
$D_5(X)\asymp X$ and the asymptotic for $D_3$, Yudin's preprint appearing on
arXiv on 2026-10-01, two days after the SSRN posting, and lists the differences
between the arguments: Huxley's short-interval theorem against Harman's
almost-all theorem for the primes, a direct use of the equidistribution
estimate for both block lengths against the valuation-one prime-mass lemma
(Lemma 4.1) combined with the short-gap corollary drawn from Harman's theorem
(Corollary 6.2), a different arithmetic set of endpoints, and Tao's uniform
Pell bound against an elementary count for $D_3$.

**Acceptance.** Reviewed and formalized. Reviewed: Jacob Parish checked the
claim and accepted it; the acceptance was recorded on 2026-10-12.

Formalized: this corpus's verification built the repository at the pinned commit
`24533265` of 2026-10-06 (Lean `v4.35.0-rc2`, with the Mathlib commit its
manifest pins) on 2026-10-12. The default build stops with one error: the
library `E374` is declared as the module `E374` with its submodules, and the
repository has no root file `src/E374.lean`. Every other module built, among
them `Erdos374CompleteWork` and all 27 modules under `src/E374/`, and a second
build naming the integration modules `E374.IntegrationD34` and
`E374.IntegrationD5` and the authors' audit modules `E374.AuditIntegration` and
`E374.AuditD34` succeeded. The verification checked the axioms of
`Erdos374CompleteWork.conclusions` and
`Erdos374CompleteWork.positive_lower_density`, of
`LiteratureReduction.minimumSix_eq_D6`, and of
`Erdos374.D35.Integration.growth_summary`, its parts `D3_order_closed`,
`D4_order_closed`, `D5_order_closed` and `D6_order_closed`, and
`D3_asymptotic_closed`. Each depends on exactly `propext`, `Classical.choice`
and `Quot.sound`, and the build's own axiom reports, for 803 declarations, name
no other axiom.

The repository has no comparator challenge, so the statements were audited
clause by clause against the Statement. A representation of $m$ of length
$k\ge2$ is a strictly increasing list of positive integers ending at $m$ whose
factorials multiply to the square of a natural number. Each $D_k$ is the set of
$m>1$ with a representation of length $k$ and none shorter. Should the
Statement's indices include $0$, nothing changes for $k\ge3$: since $0!=1$, a
shortest representation of an $m>1$ never uses $0$, and only $m=1$, then in
$D_2$, is left out. `prefixCount` counts $D_k\cap\{1,\ldots,X\}$, and positive
lower density means that $D_k(X)/X$ has a positive lower limit. The final
theorems take no hypotheses. `growth_summary` gives
$\sqrt X/2\le D_3(X)\le C\sqrt X$ for all large $X$, and positive lower density
for $D_4$, $D_5$ and $D_6$ with each count at most $X$. `D3_asymptotic_closed`
gives $\lvert D_3(X)-\kappa_3\sqrt X\rvert\le C_\varepsilon X^{2/5+\varepsilon}$
for every $\varepsilon>0$ and all large $X$, where $\kappa_3$ sums $q^{-1/2}$
over the distinct values $q=q_a\ne1$ with $a\ge1$.
`Erdos374CompleteWork.conclusions` states Theorem 1.1 as the claim above gives
it, together with the positive lower density of `MinimumSix`, which
`minimumSix_eq_D6` identifies with $D_6$. So the formalization proves the order
of growth of $D_k$ for every $k$ from 3 to 6, including $D_6(X)\gg X$. It
certifies these statements only: the paper's bound $\log2/40000$ on the lower
density of $D_5$ and the value $2.70975\ldots$ of $\kappa_3$ are not in the
formal statements.

Not refereed: the paper is a preprint, first on SSRN and now in the repository.
The site's proof-claims tab lists the claim as a partial proof claim, matching
that submission; the revised paper and the claimant's comment of 2026-10-05,
which calls the repository a full Lean verification of the problem, assert the
whole determination. The site's label is unchanged and the curator has not
credited the result. The paper's acknowledgment says it was prepared with AI
assistance in derivation, internal checking, source verification, exposition and
formalization, naming ChatGPT Astra, Google's Gemini 3.1 Pro and Gemini 3.8
Flash, Anthropic's Claude Opus 5.5 and Claude Fable 5.1, and xAI's Grok 4.7, the
systems the claim's tools field also names.
