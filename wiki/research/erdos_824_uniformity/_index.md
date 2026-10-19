---
name: research/erdos_824_uniformity
title: "Erdős 824: the uniform shift-cancellation premise"
desc: "Author reconstruction of the exact uniform shift-cancellation premise P for Problem 824. Its grade remains VOID; the separately graded elementary and conditional-chain scopes retain P as an unaccepted hypothesis."
problems:
- 824
created: 2026-10-15T11:02:06Z
updated: 2026-10-16T04:10:53Z
---

# Erdős 824: the uniform shift-cancellation premise

[[research/_index|..]]

[[research/erdos_824_uniformity/evidence/_index|evidence/]]: The full cancellation examination, its unaccepted grade, exact subjects and separate eligibility boundary.

[[research/erdos_824_uniformity/shift_cancellation_reconstruction|shift_cancellation_reconstruction]]: An author reconstruction of weighted-dilation Theorem 5.1 for the exact successor endpoints, with the original restricted sequence, common residual factor, both shift signs, and a discrepancy exponent fixed before proxy precision. Source standing remains unrefereed.

***

This folder's results that are not drawn from a cited source are Plasma
AI's, at author-recorded standing. The
[[research/erdos_824_uniformity/evidence/verify/endpoint_cancellation/_index|full P examination and its grade]]
are retained with zero accepted independent weight; the grade is VOID and
the separate exposure ruling does not supply a whole-contract PASS.

## Target

[[problems/arithmetic_functions/E0824/_index|Problem 824]] asks whether
the number of coprime pairs $a<b<x$ with $\sigma(a)=\sigma(b)$ exceeds
$x^{2-o(1)}$. Its status is open. The
[[research/erdos_824/_index|conditional route]] recorded in this corpus
follows Shisheng Li and Zhong Zhuang: it counts primes $p$ with $p+1$
free of large prime factors, by rerunning the
[[../library/arithmetic_functions/openai_2026_weighted_dilation_graphs_smooth_shifted_primes_totient_fibers/_index|weighted-dilation manuscript]]
with $2u-1$ in place of $2u+1$, and then applies the Pollack–Pomerance
construction. The route has two source premises:

- **(P)**, the uniform shifted-correlation estimate of the manuscript's
  Theorem 5.1, proved in its Sections 3–5;
- **(E)**, the elementary estimates: the manuscript's Section 2 bounds,
  the candidate mass of Proposition 7.1, the proxy discrepancy of
  Lemma 7.3 and the proxy densities of Lemma 7.4.

This folder concerns (P). The
[[research/erdos_824/smooth_successor_sign_audit|sign audit]] checks every
step where the sign of $2u\pm1$ enters, but it does not check Sections
3–5.

## The sketch

1. **The consumed statement.** The Type II estimate
   for $mn=2u-1$ needs (P) only on one endpoint class, uniformly in
   $0<|k|\le L^C$ of either sign, scales $xL^{-C}\le Z\le xL^C$, frequencies
   and cutoffs of polynomial logarithmic size, with the discrepancy
   exponent $B$ fixed before the proxy precision. The
   [[research/erdos_824_uniformity/shift_cancellation_reconstruction|reconstruction page]]
   states this class exactly. It is contained in the manuscript's
   Theorem 5.1 with that theorem's own uniformity.
2. **The proof of (P) (author reconstruction).** The manuscript proves
   Theorem 5.1 by transference for weighted dilation graphs (Section 3),
   independent-label comparison kernels (Section 4), and a lifted
   correlation analysis with minor and major arcs (Section 5). The
   reconstruction re-derives or checks every step of these sections for
   the consumed class, together with the Section 2 inputs they use. It
   closes the transfer and local-energy estimates with explicit choices
   of their logarithmic savings. The resulting $B$ is independent of the
   later proxy precision and of the sign of $k$. This supplies an
   author-recorded reconstruction of P; the manuscript remains
   unrefereed and P has no independent acceptance here.
3. **(E) (a separate reconstruction).** The
   [[research/smooth_successor_estimates/_index|elementary estimates]] have
   written proofs and a distinct passing grade for the operative E1 and
   exact E2–E5 scopes relative to their quoted classical premises. The
   Section 2 inputs that P itself uses were also checked in its own proof;
   neither examination silently inherits the other's accepted weight.
4. **Composition (conditional).** Under (P) and (E), the conditional route
   gives Hypothesis $\mathrm A^+$ and then $h(x)>x^{2-\varepsilon}$ for
   every $\varepsilon>0$. Its
   [[research/smooth_successor_primes/evidence/verify/conditional_chain/_index|whole conditional examination]]
   has a distinct passing grade at its conditional scope. Its graded
   comparison uses the separately accepted E fragments, retaining P and
   the exact classical premises.

## Gaps

P's accepted independent weight remains unresolved despite the separate
ruling that its grader's exposure was immaterial. E and the whole conditional
chain have passing independent grades at their exact surviving and
conditional scopes; neither grade accepts P. The frozen unrestricted
sieve-cutoff and dyadic assertions were refuted at their stated scopes; the
consumed ranges and their repairs are identified on the owning pages. These
records supply no accepted unconditional solution, and Problem 824 stays
open.
