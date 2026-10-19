---
name: theory/additive_bases/L209_singer_level_maximal_sidon
title: A Singer set with one point per level is maximal Sidon in Z_q x H
desc: |
  A perfect difference set modulo q = p^2+p+1 placed at level zero, plus one
  greedily chosen point at each level of an abelian group H of odd order
  h <= p/4, is a maximal strong Sidon set of size p+h in Z_q x H; for cyclic
  H coprime to q this is a cyclic group of order about p^3/4.
tags: []
sources:
- problems/additive_bases/E0156
id: L209
statement: |
  Let p be a prime power, q = p^2+p+1, and let B be a subset of Z_q with
  p+1 elements whose differences b-b', b != b', represent every non-zero
  residue modulo q exactly once. Let H be a finite abelian group of odd
  order h with h <= p/4. Then there is a map c: H -> Z_q with c(0) in B
  such that the set A = {(b, 0) : b in B} union {(c(x), x) : x in H} of the
  group Z_q x H has exactly p+h elements, is strong Sidon (the sums a+b
  over unordered pairs {a, b} of elements of A, doubles a = b included, are
  pairwise distinct), and is maximal (every element of Z_q x H outside A
  equals a+b-c for some a, b, c in A with c not in {a, b}). When H is
  cyclic and gcd(h, q) = 1, the group Z_q x H is cyclic of order qh.
status: proved
tier: 0
depends_on: []
created: 2026-10-15T18:15:30Z
updated: 2026-10-15T18:15:30Z
---

# A Singer set with one point per level is maximal Sidon in Z_q x H

[[theory/additive_bases/_index|..]]

[[theory/additive_bases/L209_singer_level_maximal_sidon/_proof|_proof]]: Maximality follows from the perfect difference property at every level;
the strong Sidon property reduces to three families of conditions on the
level map, and a greedy count satisfies them when h <= p/4.

[[theory/additive_bases/L209_singer_level_maximal_sidon/evidence/_index|evidence/]]: Build Singer sets for primes from 13 to 53, run the greedy rule of the proof for odd groups of order at most p/4, and verify maximality and the strong Sidon property by brute force.

***

This author-recorded result is due to Plasma AI. The [proof](_proof.md) is
elementary and complete; the [finite check](evidence/_index.md) runs the
proof's greedy rule for twelve pairs $(p,H)$ and verifies the resulting
sets by brute force.

**Significance.** Perfect difference sets of the required kind exist for
every prime power $p$ by
[[../library/additive_bases/singer_1938_theorem_finite_projective_geometry_some_applications_number_theory/theorem_p380|Singer's
theorem, which supplies the set B]]. Choosing a cyclic $H$ of odd order
$h\le p/4$ coprime to $q$ with $h\ge p/8$, which is possible for every
large $p$, gives cyclic groups $\mathbb Z_{qh}$ of order between about
$p^3/8$ and $p^3/4$ with maximal strong Sidon sets of at most $5p/4$
elements, that is $O(|G|^{1/3})$. In a group of odd order the counting
bound recorded in
[[theory/additive_bases/L208_two_parabola_maximal_sidon/_index|L208, the
non-cyclic analogue in F_q^3]] shows that the cube-root order cannot be
improved. The construction answers the cyclic-group analogue of
[[problems/additive_bases/E0156/_index|Problem 156]] for these orders only;
it gives nothing for other cyclic orders or for integer intervals.

**Mechanism.** Maximality is automatic: the point $(c(s),s)$ of level
$s\ne0$ and the differences of $B$, which cover every non-zero residue,
block every other element of that level, and level $0$ is blocked by
$B+B-B$. The map $c$ only has to keep $A$ Sidon, and three families of
conditions do that. The worst of them excludes about half of $\mathbb Z_q$
for each value $c(x)$, because $c(x)+c(-x)$ must avoid $B+B$; the others
exclude $O(hp)$ residues, and a greedy choice therefore succeeds while $h$
is at most about $0.3p$. The constant is not optimized: the evidence
program also checks retained valid maps with $(p,h)=(5,7)$ and $(11,13)$,
where $h$ exceeds $p$.

**Relation to the integers.** The integer analogue of this set is the
anchored Singer lift, with $B$ at height $0$ and one point $c(s)+qs$ at
each height $s$. There the residue sum of a blocking triple can wrap past
$q$, and the corresponding integer is then off by a multiple of $q$. That
carry defeats the automatic maximality; the
[[research/small_maximal_sidon_attack/integer_transfer|integer transfer
analysis]] records the precise failure.

**Standing.** Tier 0. No independent review is recorded. Verification
consists of reading the proof, chiefly the count of excluded residues in
the greedy step. The evidence program checks the greedy rule and the
conclusion on finite cases and does not replace the proof. There is no
remaining obligation inside the stated scope. The attack this result
serves is recorded in the
[[research/small_maximal_sidon_attack/proof_sketch|proof sketch for the
small maximal Sidon problem]].
