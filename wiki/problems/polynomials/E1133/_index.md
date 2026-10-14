---
name: problems/polynomials/E1133
title: Problem 1133
desc: |
  Asks whether each $C>0$ has an $\epsilon>0$ such that, for large $n$ and any
  $x_1,\ldots,x_n\in[-1,1]$, some $y_i\in[-1,1]$ give
  $\max_{[-1,1]}\lvert P\rvert>C$ whenever $\deg P<(1+\epsilon)n$ and
  $P(x_i)=y_i$ for at least $(1-\epsilon)n$ values of $i$.
tags:
- Analysis
- Polynomials
status: claimed
claim: proved
created: 2026-09-04T09:17:27Z
updated: 2026-10-08T17:47:46Z
---

# Problem 1133

[[problems/polynomials/_index|..]]

[[problems/polynomials/E1133/claims/_index|claims/]]: The 2 claim pages of Problem 1133, one per claimant's result; the problem's standing derives from them.

***

**Statement.** Let $C>0$. There exists $\epsilon>0$ such that if $n$ is
sufficiently large the following holds.

For any $x_1,\ldots,x_n\in [-1,1]$ there exist $y_1,\ldots,y_n\in [-1,1]$ such
that, if $P$ is a polynomial of degree $m<(1+\epsilon)n$ with $P(x_i)=y_i$ for
at least $(1-\epsilon)n$ many $1\leq i\leq n$, then

$$
\max_{x\in [-1,1]}\lvert P(x)\rvert >C.
$$

**Status.** The site labeled the problem OPEN (page last edited 31 December
2025; proof-claims tab accessed 2026-10-06). This page records the claims below
without adopting them, and the standing in the frontmatter follows from them.
Two manuscripts claim the assertion in full, and neither is reviewed or
refereed.

The first is a note posted in the site's thread by Przemek Chojecki on 29
April 2026. It was produced with GPT-5.5 Pro, as Chojecki wrote there, and is
hosted at ulam.ai. It derives a finite obstruction from Beurling's
interpolation-density theorem for the Bernstein space and plants it on short
blocks of nodes ([[problems/polynomials/E1133/claims/2026_04_29_chojecki|claim
page]]). The second is the manuscript of Jia-Qi Yang, submitted to the site's
proof-claims tab on 2026-09-13 (using GPT-6, as the tab writes it). It claims to
prove the obstruction for sign data at any pointwise tolerance, with $\epsilon$
of optimal exponential order in $C$. It also claims the sharp coefficient
$\pi/2$ on Chebyshev–Lobatto grids
([[problems/polynomials/E1133/claims/2026_09_13_yang|claim page]]).

The site's commentary credits Erdős with a weaker statement. He gives it as
Theorem 4 of [Er67, p. 72] and says he had stated it without proof in an earlier
paper. It says that for every $C>0$ there is $\epsilon>0$ such that, for large
$n$ and any $m=\lfloor(1+\epsilon)n\rfloor$ nodes in $[-1,1]$, some polynomial
$P$ of degree $n$ has $\lvert P(x_i)\rvert\le1$ at every node and
$\max\lvert P\rvert>C$. The assertion of the problem would imply it. Erdős
remarks in [Er67] that he could not prove the assertion even for $m=n$.

**Source.** [erdosproblems.com/1133](https://www.erdosproblems.com/1133),
accessed 2026-09-04. Cite as: T. F. Bloom, Erdős Problem #1133,
https://www.erdosproblems.com/1133.

**References.**

- [Er67] Erdős, P., Problems and results on the convergence and divergence
  properties of the Lagrange interpolation polynomials and some extremal
  problems. Mathematica (Cluj) 10 (33) (1968), 65-73.

**Formalization.** Statement in
[formal-conjectures](https://github.com/google-deepmind/formal-conjectures/blob/6fbb54f24ccc2e64dcfaffc28c58950e377110d2/FormalConjectures/ErdosProblems/1133.lean);
the file states the problem and a weaker variant without proofs and names no
formal proof. Its
[commit of 8 October 2026](https://github.com/google-deepmind/formal-conjectures/blob/121d72ce6ac513360240a84cd49af59684e3f6fc/FormalConjectures/ErdosProblems/1133.lean)
relabels the statement research solved with `answer(True)`, citing Yang's
arXiv preprint, a catalog label change and not acceptance (Current
assessment). The community database at teorth/erdosproblems lists the statement
as formalized since 2026-06-08 and the problem as unformalized otherwise.

## Current assessment

**The question (site formulation, page last edited 31 December 2025).** For
every $C>0$ there is $\epsilon>0$ such that, for all large $n$ and every $n$
nodes in $[-1,1]$, some labels in $[-1,1]$ force every polynomial of degree
below $(1+\epsilon)n$ that matches at least $(1-\epsilon)n$ of them to
exceed $C$ in absolute value somewhere on $[-1,1]$. OPEN. The site's
commentary credits Erdős with the weaker statement, Theorem 4 of [Er67, p.
72], which he says he had stated without proof in an earlier paper, with
$m=\lfloor(1+\epsilon)n\rfloor$ nodes and a polynomial of degree $n$ bounded
by $1$ at every node, and his remark in [Er67] that he could not prove the
assertion even for $m=n$. The statement fixes no dependence of $\epsilon$ on
$C$.

**Pending claims.** Two full claims, neither reviewed nor refereed, and
neither adopted.
[[problems/polynomials/E1133/claims/2026_04_29_chojecki|Chojecki 2026]]: a
note posted in the site's thread on 29 April 2026, produced with GPT-5.5 Pro
as the poster wrote, which derives from Beurling's interpolation-density
theorem for the Bernstein space a finite forbidden label pattern on short
blocks of nodes and plants it on more than $\epsilon n$ blocks after the
substitution $x=\cos\theta$; it gives no rate for $\epsilon$ in $C$, and a
same-day reply reporting a tool-assisted check is not a review.
[[problems/polynomials/E1133/claims/2026_09_13_yang|Yang 2026]]: a
manuscript submitted to the proof-claims tab on 2026-09-13, using GPT-6 as
the tab discloses, and posted the same day as arXiv:2609.14769, which claims
the obstruction for sign data at any pointwise tolerance $\rho$ with
$\epsilon$ of exponential order in $C/(1-\rho)$, shows that order optimal
through interpolation at
Chebyshev–Lobatto nodes, and identifies the sharp coefficient $\pi/2$ on the
full Chebyshev–Lobatto grids, the sharp coefficient for arbitrary nodes
being left open; it credits the earlier note for the angular reduction and
grouping and takes its quantitative input from Olevskii and Ulanovskii. The
derived standing is `claimed` with the claim value `proved`. Neither proof
is compiled or reviewed in this wiki.

**Formalization.** The formal-conjectures file linked above states the problem
and a weaker variant without proofs and names no formal proof. The
formal-conjectures commit of 8 October 2026 changes the statement's category
from research open to research solved and its answer from `sorry` to `True`,
citing Theorem 2.1 of Yang's arXiv preprint; this is a catalog label change, not
a formal proof, a review or an acceptance, and Yang's claim stays `claimed`. No
Lean development of either claim is known.

**Search scope.** The site's problem page, its thread (three posts by
2026-10-07, of 29 April and 13 September 2026), and its proof-claims tab with
Yang's claim; the community database at teorth/erdosproblems; the
formal-conjectures file at the pinned commit; the note at ulam.ai through
its card and Yang's manuscript at its pinned commit.
<!-- BEGIN problem library links -->

## Linked library material

These entries are derived from explicit links on library pages. They are
navigation only and do not by themselves record mathematical progress.

- [[../library/polynomials/anon_2026_bernstein_density_proof_erdos_s_robust/_index|anon_2026_bernstein_density_proof_erdos_s_robust]]
- [[../library/polynomials/anon_2026_bernstein_density_proof_erdos_s_robust/lemma_3_2|anon_2026_bernstein_density_proof_erdos_s_robust / lemma_3_2]]
- [[../library/polynomials/anon_2026_bernstein_density_proof_erdos_s_robust/lemma_4_1|anon_2026_bernstein_density_proof_erdos_s_robust / lemma_4_1]]
- [[../library/polynomials/anon_2026_bernstein_density_proof_erdos_s_robust/proposition_3_1|anon_2026_bernstein_density_proof_erdos_s_robust / proposition_3_1]]
- [[../library/polynomials/anon_2026_bernstein_density_proof_erdos_s_robust/theorem_1_1|anon_2026_bernstein_density_proof_erdos_s_robust / theorem_1_1]]
- [[../library/polynomials/erdos_1967_problems_results_convergence_divergence_properties_lagrange/_index|erdos_1967_problems_results_convergence_divergence_properties_lagrange]]
- [[../library/polynomials/erdos_1967_problems_results_convergence_divergence_properties_lagrange/conjecture_p72|erdos_1967_problems_results_convergence_divergence_properties_lagrange / conjecture_p72]]
- [[../library/polynomials/erdos_1967_problems_results_convergence_divergence_properties_lagrange/theorem_3|erdos_1967_problems_results_convergence_divergence_properties_lagrange / theorem_3]]
- [[../library/polynomials/erdos_1967_problems_results_convergence_divergence_properties_lagrange/theorem_4|erdos_1967_problems_results_convergence_divergence_properties_lagrange / theorem_4]]

<!-- END problem library links -->
