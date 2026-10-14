---
name: problems/additive_combinatorics/E0328/claims/1985_01_01_nesetril_rodl
title: Nešetřil and Rödl's unsplittable bounded-representation sets
desc: |
  Nešetřil and Rödl prove that for every integer $C\ge2$ there is a set of
  natural numbers whose pairwise sums each have at most $C$ representations, and
  which no partition into finitely many parts reduces to fewer than $C$
  representations in every part. This answers the question no.
authors:
- J. Nešetřil
- V. Rödl
status: accepted
claim: disproved
scope: full
evidence:
- reviewed
- refereed
submitted: null
links:
- url: https://doi.org/10.1090/S0002-9939-1985-0766553-0
  kind: paper
- url: https://www.erdosproblems.com/328
  kind: discussion
created: 2026-10-07T14:48:57Z
updated: 2026-10-07T21:34:29Z
---

***

Nešetřil and Rödl's Theorem 2 shows that for every integer $k \geq 2$ there is
a $B_2^{(k)}$ sequence $A \subseteq \mathbb N$, a set in which every $n$ has
at most $k$ representations $n = x + y$ with $x, y \in A$, counted without
regard to order and with $x = y$ allowed (the definition on p. 186 does not
exclude $x = y$, and the case count on p. 187 counts each unordered pair
once), and some $n$ has exactly $k$, such that in every partition of $A$ into
finitely many parts $A_1, \ldots, A_t$ some part is again a $B_2^{(k)}$
sequence; the number of parts may depend on $A$ as well as on $k$. With $C =
k$ no part has fewer than $C$ representations of every $n$, so the answer to
the question of Erdős and Newman is no for every integer $C \geq 2$ under that
unordered count. The modified Statement of
[[problems/additive_combinatorics/E0328/_index|Problem 328]] takes Erdős and
Graham's count, which excludes $x = y$; their book (1980, p. 49) reports that
Nešetřil and Rödl showed the answer to the question, as stated with that
count, to be negative for all $c$, and the erdosproblems.com curator credits
them with the same answer for all $C$. The page values the result against the
modified Statement on that report. The case $C = 1$ is trivial, and for
non-integer $C$ the hypothesis already gives fewer than $C$ representations of
every $n$, so the partition into one part works. Erdős had earlier proved the
same for $C = 2$, $3$, every $2^s$ and every $\tfrac12\binom{2s}{s}$, by
Ramsey's theorem, in the paper whose source card is
[[../library/additive_combinatorics/erdos_1980_applications_ramsey_s_theorem_additive_number/_index|Erdős 1980]]
and recorded on
[[problems/additive_combinatorics/E0328/claims/1980_03_01_erdos|its own claim page]];
the note added in proof there records Nešetřil and Rödl's proof of the
conjecture for every $k$. The source is J. Nešetřil and V. Rödl, *Two proofs
in combinatorial number theory*, Proceedings of the American Mathematical
Society **93** (1985), no. 1, 185–188, in the January 1985 issue; the page is
dated to that month because no publication day is recorded. The statement
above is Theorem 2 of the published paper, whose proof counts each unordered
representation once, and its proof is not checked in this corpus.

**Acceptance.** Refereed: Proceedings of the American Mathematical Society
**93** (1985), no. 1, 185–188, at the DOI linked above. Reviewed: the
erdosproblems.com curator, Thomas Bloom, labeled the problem DISPROVED (LEAN).
In the problem's commentary (page last edited 6 April 2026), the curator credits
Nešetřil and Rödl with showing that the answer is no for all $C$, even if $t$
may depend on $A$. The erdosproblems.com Lean mark refers to a separate public
Lean refutation of erdosproblems.com's ordered-count wording. That refutation
settles no instance of the modified Statement. It is recorded on its own,
rejected,
[[problems/additive_combinatorics/E0328/claims/2026_06_18_axiommath|claim page]].
