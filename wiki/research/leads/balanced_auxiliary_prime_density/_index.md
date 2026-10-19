---
name: research/leads/balanced_auxiliary_prime_density
title: Balanced auxiliary-prime density
desc: |
  Closed (resolved): A balanced auxiliary-prime schedule sharpens the explicit
  loss at exponent root six minus two; exact review and grade scopes are
  retained.
problems:
- 158
research_state: closed
review_status: reviewed
created: 2026-09-15T05:31:30Z
updated: 2026-10-19T04:19:07Z
---

# Balanced auxiliary-prime density

[[research/leads/_index|..]]

[[research/leads/balanced_auxiliary_prime_density/evidence/_index|evidence/]]: Exact reviewed subject and scoped independent assessment and contract-grade
records for the balanced-prime loss refinement.

[[research/leads/balanced_auxiliary_prime_density/loss_refinement|loss_refinement]]: The full balanced-schedule proof, with its exact reviewed subject and
qualified independent review and distinct contract-grade records.

***

This lead's notes that cite no source are author-recorded research, not claims.

## Exact result

Put $\gamma=\sqrt6-2$. There exist one infinite set
$A\subseteq\mathbb Z_{>0}$, a real constant $C>0$, and a real
$x_0>e$ such that, writing

$$
A(x)=|A\cap[1,x]|,\qquad
r_A(n)=|\{(a,b)\in A^2:a\le b,\ a+b=n\}|,
$$

one has $r_A(n)\le2$ for every integer $n$ and

$$
A(x)\ge x^\gamma
\exp\{-C\sqrt{\ln x\,\ln\ln x}\}
\qquad\text{for every real }x\ge x_0.
$$

The representations are unordered and a diagonal is counted once.
The same set consequently has

$$
\liminf_{x\to\infty}\frac{\log A(x)}{\log x}\ge\gamma,
$$

and, for each real $\alpha<\gamma$, it satisfies $A(x)\ge x^\alpha$
for every sufficiently large real $x$. Only that latter threshold may
depend on $\alpha$.

The [full proof](loss_refinement.md) chooses independent auxiliary primes
with dyadic exponent $w_j=\lceil j\log_2(j+1)\rceil$. It supplies the
arithmetic, conditional expectation, simultaneous selection and all-cutoff
deductions, rather than applying a theorem outside its parameter range.

## Current scoped standing

The exact original author proof is retained as a
[byte-exact review subject](evidence/assets/loss_refinement_reviewed.txt).
It received a fresh-context, independent whole-argument
[refutation-failed assessment](evidence/verify/loss_refinement_review.md).
A [distinct grader's PASS](evidence/verify/loss_refinement_grade.md)
accepted the original report contract and reviewer independence.

That verdict relies on exact standard external theorem interfaces and does
not recursively certify their proofs. The review did not authenticate the
Cilleruelo method attribution, L2 standing, historical author reading, or
novelty. Those exclusions remain explicit. The reviewer, author and grader
are distinct roles and contexts; the grade is not a second blind review.

This native filing was prepared by the exposed author. The original
mathematical assessment and contract grade are retained without extending
them to an unchecked transfer, later repair, numerical tier, formal proof,
publication, or public record. No mathematical computation or formal
reproduction is claimed. The source artifact identities, exact locators,
reading depth and raw-transfer accounting limitations accompany the review.

## Ownership and relationships

This is a separate research lead for the balanced-schedule loss refinement,
not a new L-claim and not an amendment to
[L4](../../../theory/additive_bases/L4_random_modulus_exponent/_index.md).
L4's existing statement has loss
$\exp\{-C\sqrt{\ln x}\,\ln\ln x\}$ and records author standing
at tier 0. The retained refinement improves the order of that loss; it
does not improve the leading exponent $\gamma$. No L4 statement, status,
tier, proof or historical evidence is altered by this record.

The original author attributes the shifted discrete-logarithm method to
[Cilleruelo's selected manuscript](../../../../library/additive_bases/cilleruelo_2014_infinite_sidon_sequences/_index.md),
arXiv:1209.0326v2, dated 15 May 2013. Its density theorem is background,
not an established premise of this proof. The canonical source index
supplies source identity and its own separate reading qualifications.

The result bears on
[Erdős Problem 158](../../../problems/additive_bases/E0158/_index.md), whose
intended question concerns zero square-root lower density for every
infinite B2[2] set. Since $\gamma<1/2$, this result does not settle that
question. There is no claim of positive square-root lower density,
a positive constant multiple of $x^\gamma$, sharpness, priority, or a
current public record. The problem page's dated status assessment is not
renewed by retaining this argument.
