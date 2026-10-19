---
name: research/erdos_824
title: Coprime pairs with equal divisor sums from smooth successor primes
desc: "The independently graded conditional route from exact shift cancellation and surviving elementary estimates to smooth successor primes and coprime squarefree pairs; P and original-source reading boundaries remain explicit."
problems:
- 824
created: 2026-10-15T04:45:32Z
updated: 2026-10-15T04:45:32Z
---

# Coprime pairs with equal divisor sums from smooth successor primes

[[research/_index|..]]

[[research/erdos_824/smooth_successor_sign_audit|smooth_successor_sign_audit]]: Every place where the sign of 2u+1 enters the weighted-dilation
manuscript's proof of its smooth-predecessor count, with the identity,
divisor bound, unit class, residue count or range that replaces it for
primes 2u-1; the sign-free steps remain the manuscript's unrefereed
argument.

***

This folder's results that are not drawn from a cited source are Plasma
AI's, credited to Plasma AI. The route itself is Shisheng Li and Zhong
Zhuang's, recorded on
[[problems/arithmetic_functions/E0824/claims/2026_10_07_li_zhuang|their claim page]]:
the reduction follows Pollack and Pomerance after an idea of Erdős, and the
counting argument it adapts is OpenAI's
[[../library/arithmetic_functions/openai_2026_weighted_dilation_graphs_smooth_shifted_primes_totient_fibers/_index|weighted-dilation manuscript]].

The [[research/smooth_successor_primes/_index|complete conditional derivation]]
writes out the signed Type II estimate, the sieve, and the squarefree
counting reduction. It identifies the exact uniform analytic premise (P)
and elementary source inputs (E), and includes an author examination of
the analytic core. This page gives the route and the final counting
argument; the linked derivation states the full endpoint interface.

## Target

[[problems/arithmetic_functions/E0824/_index|Problem 824]], status open. Let
$h(x)$ count the pairs $1\le a<b<x$ with $(a,b)=1$ and $\sigma(a)=\sigma(b)$.
The question is whether $h(x)>x^{2-o(1)}$, that is, whether for every
$\varepsilon>0$ one has $h(x)>x^{2-\varepsilon}$ for all large $x$.
Pollack and Pomerance proved $h(x)>x^{1.4}$
([[../library/arithmetic_functions/pollack_2016_problems_erdos_sum_divisors_function/theorem_p24|their Section 6 result]]).
Nothing here answers the question unconditionally.

## The conditional route

Write $P^+(m)$ for the largest prime factor of $m$. Hypothesis
$\mathrm A^+$ is Definition 1.2 of Li and Zhuang's draft: for every
$0<\delta<1/4$ and every $\eta>0$ there is $y_0$ such that every real
$y\ge y_0$ has

$$
\#\{p\text{ prime}:\ p\le5y,\ P^+(p+1)\le y^\delta\}\ge y^{1-\eta}.
$$

The route has three links.

1. **Premises.** The weighted-dilation manuscript's lifted
   shift-cancellation Theorem 5.1 holds uniformly for the endpoints
   consumed by the [[research/smooth_successor_primes/signed_type_ii|signed
   Type II estimate]]; this is (P). Its Section 2 estimates, candidate
   mass Proposition 7.1 and proxy Lemmas 7.3–7.4 supply (E). Both remain
   unrefereed source premises. The
   [[research/smooth_successor_primes/shift_sign_analytic_core|author
   examination of the analytic core]] does not independently establish (P).
2. **Sign change.** Under these premises, for every fixed $0<\delta<1/4$ at
   least $x^{1-o(1)}$ primes $p$ with $2x-1\le p\le4x-1$ have
   $P^+(p+1)\le x^\delta$, and hence $\mathrm A^+$ holds. This is Li and
   Zhuang's Theorem 1.4, with a slightly narrower range. The
   [[research/erdos_824/smooth_successor_sign_audit|sign audit]] lists every
   step of the manuscript's Sections 6 and 7 at which the sign enters and
   proves the replacement for primes $2u-1$: the determinant identity of
   the Type II estimate and its converse, the divisor-moment bounds, the
   unit class of the Type I estimate, the residue counts of the sieve for
   balanced composites, and the final range. This compact source comparison
   remains author-recorded; the full conditional derivation has the separate
   passing grade described below.
3. **Reduction.** $\mathrm A^+$ implies $h(x)>x^{2-\varepsilon}$ for every
   $\varepsilon>0$ and all large $x$, with $a,b$ squarefree. This is Li
   and Zhuang's Theorem 1.3, whose proof is rederived below.

Composed, the links give the requested bound conditional on (P) and (E).
The conditional whole-conclusion grade matches the surviving E scopes
to this chain. An unconditional answer still requires accepted P at its
full consumed uniformity, together with the explicit classical boundaries. Li and Zhuang report a Lean proof of the
implication in link 3, replayed by the Palomar registry; this corpus has not
built or audited it, and it is not this corpus's Lean acceptance.

## The reduction from Hypothesis A+

The argument is Li and Zhuang's Section 3, with every parameter checked
here. Fix $0<\varepsilon<1$, a real $B\ge8/\varepsilon$, $\eta=\varepsilon/16$
and $\delta=1/(2B)\in(0,1/4)$. Write $L=\log x$, put $y=L^B$, let
$\mathcal P$ be the set of primes $p\le5y$ with $P^+(p+1)\le y^\delta=L^{1/2}$,
and $M=|\mathcal P|$. By $\mathrm A^+$, $M\ge L^{B(1-\eta)}$ for large $x$.
Let $k=\lfloor L/\log(5y+1)\rfloor$, so that $(5y+1)^k\le x$ and
$k=(1+o(1))L/(B\log L)$; also $M\ge2k$ for large $x$.

Let $\mathcal A$ be the set of products of $k$ distinct primes of
$\mathcal P$. Each $a\in\mathcal A$ is squarefree and satisfies
$a\le(5y)^k<(5y+1)^k\le x$. Distinct sets give distinct products, and

$$
\log N:=\log|\mathcal A|\ge k\log(M/k)
\ge L\Bigl(1-\eta-\frac1B\Bigr)(1+o(1)).
$$

For $a=p_1\cdots p_k$, $\sigma(a)=\prod_i(p_i+1)\le x$ is $L^{1/2}$-smooth.
An $L^{1/2}$-smooth integer up to $x$ is $\prod_{q\le L^{1/2}}q^{e_q}$ with
$0\le e_q\le L/\log2$, so at most $U=(1+L/\log2)^{L^{1/2}}$ values occur and
$\log U=o(L)$. With $r(s)=\#\{a\in\mathcal A:\sigma(a)=s\}$, Cauchy's
inequality gives at least $N^2/U$ ordered pairs $(a,b)\in\mathcal A^2$ with
$\sigma(a)=\sigma(b)$.

Let $t=\lceil\eta k\rceil$. Ordered pairs sharing at least $t$ primes
number at most $N\binom kt\binom M{k-t}$, and since $M\ge2k$,

$$
\binom M{k-t}\Big/\binom Mk=\prod_{i=0}^{t-1}\frac{k-i}{M-k+t-i}
\le\Bigl(\frac{2k}M\Bigr)^t .
$$

With $\binom kt\le2^k$, $k\le L$ and $M\ge L^{B(1-\eta)}$,

$$
\log\Bigl(2^k\Bigl(\frac{2k}M\Bigr)^t\cdot2U\Bigr)
\le(k+1)\log2+\log U-\eta k\bigl(B(1-\eta)\log L-\log(2L)\bigr)
=-\eta L\Bigl(1-\eta-\frac1B\Bigr)(1+o(1))+o(L),
$$

which is negative for large $x$. So at least $N^2/(2U)$ ordered pairs with
$\sigma(a)=\sigma(b)$ share fewer than $t$ primes, and $a\ne b$ for them.

For such a pair put $g=(a,b)$, $u=a/g$, $v=b/g$. As $a,b$ are squarefree,
$g$, $u$ and $v$ are pairwise coprime, so
$\sigma(g)\sigma(u)=\sigma(g)\sigma(v)$ gives $\sigma(u)=\sigma(v)$, with
$(u,v)=1$, $u\ne v$, and $u,v<x$ squarefree.
Since $g$ is a product of at most $t-1<\eta k$ primes below $5y+1$,
$g\le x^\eta$; each unordered pair $\{u,v\}$ therefore comes from at most
$2x^\eta$ ordered pairs. Hence

$$
h(x)\ge\frac{N^2}{4Ux^\eta},\qquad
\log h(x)\ge\Bigl(2-3\eta-\frac2B\Bigr)L-o(L)>(2-\varepsilon)L
$$

for large $x$, since $3\eta+2/B\le7\varepsilon/16$. Only the values of
$\mathrm A^+$ at $\delta=1/(2B)$ and $\eta=\varepsilon/16$ are used, at the
point $y=(\log x)^B$.

## Standing and what remains

Links 2 and 3 have independently graded coverage through the full conditional
chain. The
[[research/smooth_successor_primes/evidence/verify/conditional_chain/_index|whole conditional examination]]
records **refutation-failed** for their composition from P and the operative
E estimates, including every sufficiently large real input and the strict
squarefree-pair conclusion; its distinct whole-contract grade is **PASS**,
examined on 2026-10-16 UTC. The
[[research/smooth_successor_estimates/evidence/verify/elementary_estimates/_index|E examination]]
has a separate passing grade for its adverse and surviving scopes, while the
[[research/erdos_824_uniformity/evidence/verify/endpoint_cancellation/_index|P grade remains VOID with zero accepted independent weight]].
The authors' externally replayed Lean proof covers the lower-bound
implication for natural $x$, without the squarefree addendum. No build,
axiom audit or statement-fidelity audit of it is supplied here. P remains
without accepted independent weight; the accepted E scopes are relative to
their quoted classical premises. The problem stays open. The route still
depends on the unrefereed weighted-dilation manuscript; original classical
proofs and PDF fidelity remain unexamined.

The [[research/smooth_successor_primes/_index|combined sketch]] records the
exact remaining uniformity: the discrepancy exponent must be chosen before
the proxy's final cell precision, for all consumed endpoints, intervals,
cutoffs and both shift signs. The two signs use a common permitted class,
but their separated cutoff coefficients need not coincide. Establishing
only selected predecessor instances does not justify the successor count.
No sign-specific failure was found; that author observation supplies no
independent acceptance of the analytic estimates.
