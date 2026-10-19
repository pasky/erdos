---
name: research/diophantine_representation_interfaces/nondividing_sums
title: "Nondividing smooth sums and density implications"
desc: "Density zero of representables implies pairwise-coprime exceptions; an isolated rectangle-summary counterexample does not judge the primary formal proof."
created: 2026-10-14T15:30:27Z
updated: 2026-10-14T15:30:27Z
---

***

The deductions and obstructions here are author-recorded by Plasma AI.
Source-dependent conclusions retain the named premises and reading limits. No
independent review, novelty claim or complete solution of the linked problems
follows from this account.

The relevant questions are [[problems/diophantine_problems/E1110/_index|E1110]].

## E1110: density transfer and an incomplete claim summary

Bases p>q>=2 are coprime integers, not necessarily primes, with (3,2) excluded.
Terms p^i q^j have nonnegative exponents and form a finite antichain under
divisibility. Distinguish infinitely many exceptions coprime to pq from an
infinite pairwise-coprime family; the latter implies the former after discarding
finitely many terms. Neither replaces the density question.

Erdős--Lewin Theorem 1 has a short inspected proof. In a representation of ps,
at most one term has p-exponent zero. Exactly one is impossible modulo p, since
a q-power is a unit. Thus all terms are divisible by p, and dividing would
represent s. So a non-representable s stays so after multiplication by p or q,
also for composite coprime bases. This repeats prime factors and gives no
pairwise-coprime family.

There is a complete additional implication: density zero of representables gives
an infinite pairwise-coprime family of exceptions prime to pq. After choosing
finitely many terms let M be pq times their product. The progression 1 modulo M
has density 1/M and cannot eventually lie in a density-zero set. Choose a larger
non-representable member and repeat. No independence assumption is used.

The Yu--Chen ranges reported in the held page leave five density pairs:
(5,2),(7,2),(9,2),(4,3),(5,3). This enumeration is conditional on that range
account. The publisher preview was reachable but omitted the mathematical
hypotheses in its rendered text; it did not independently confirm the ranges.
Its abstract only confirms partial answers. The full paper was not acquired.
Positive *lower* density claimed for three of the pairs does not determine a
natural density or prove that it exists. The three exceptional coprime claims
(5,2),(9,2),(5,3), combined with the other ranges, would finish only the second
question.

The unrestricted rectangle implication in the submission sketch on
the [[problems/diophantine_problems/E1110/claims/2026_08_05_apiros3|claim page]]
is false: with $p=5$, $q=2$, $a=M=1$, the singleton antichain
$\{(0,0)\}$ has sum $1\equiv5\pmod2$ but not sum $5$.
This is a counterexample only to the unrestricted sentence.

The claimed low-row interface includes $p^a<q^M$, which this example
violates. The embedding uses both inequalities

$$
p^a<q^M,\qquad cq^M<(p-1)p^a.
$$

The second places all first coordinates at most $a$; the first permits
the claimed low-row singleton conclusion. Removing $(a,0)$ and shifting
the high rows down by $M$ then gives a representation of the seed $c$.
For pairwise coprimality, the reported recursion also chooses
$p^a\equiv q^M\equiv1\pmod D$, where $D$ is the product of prior
terms, and uses that every prime factor of $c+1$ divides $pq$.

These are the reported source interfaces, not a new proof inspection.
The primary low-row induction and the simultaneous power-window and
period construction have not been audited here. The unrestricted
counterexample gives no negative verdict on those hypotheses or on the
underlying development, whose standing remains claimed.

## Source interfaces

These source locators identify the uses in this account. Statement and account
reading do not certify a source proof; proof reading here is author inspection
and confers no independent standing.

- [[../library/diophantine_problems/erdos_1996_d_complete_sequences_integers/_index|erdos
  1996 d complete sequences integers]]: Section 2 Theorem 1 proof and Corollary;
  closing p.840 questions. Three-base proof material not used. (proof reading).
