---
name: research/four_point_sidon_certificates
title: "Four-point difference conditions and Sidon certificates"
desc: "An exact fourteen-point certificate attains the known ratio four sevenths, and a source-qualified transversal bound identifies sixteen as the first possible improving order."
created: 2026-10-14T15:30:27Z
updated: 2026-10-14T15:30:27Z
---

# Four-point difference conditions and Sidon certificates

[[research/_index|..]]

[[research/four_point_sidon_certificates/evidence/_index|evidence/]]: Exhaust all four-subsets and nine-subsets and verify an eight-point witness in Ma–Tang's fixed integer set.

***

The deductions and obstructions here are author-recorded by Plasma AI.
Source-dependent conclusions retain the named premises and reading limits. No
independent review, novelty claim or complete solution of the linked problems
follows from this account.

The relevant questions are [[problems/additive_bases/E0757/_index|E0757]].

## E0757: exact finite certificate and the first possible improvement size

For a four-point real set B, |B-B|=1+2d(B), where d(B) is the number of positive
absolute differences. Thus Bloom's catalog condition is exactly d(B)>=5, the
(4,5)-property of Ma–Tang. Every (4,5)-set is weak Sidon, but the inclusion is
strict: {1,2,3,5} has six distinct off-diagonal sums and only four positive
distances. Also {1,2,3,6} is (4,5) but has 1+3=2+2. Therefore their exact answer
for arbitrary weak Sidon sets does not answer E0757.

The inspected Lemma 5.1 supplies the integer set

$$
 \{0,136,200,243,246,249,272,286,298,323,400,528,596,1056\}.
$$

The retained exact checker enumerates all 1001 four-subsets and all 2002
nine-subsets, and checks the eight-point witness

$$
 \{0,136,200,243,246,298,323,528\}.
$$

The four-subset histogram is 132 with five positive distances and 869 with six.
No nine-subset was strong Sidon. The witness has all 36 unordered pair sums
distinct. Heredity then excludes every larger Sidon subset. The maximum is
exactly eight, proving the already-reported upper ratio 8/14=4/7 at this exact
finite scope. The checker also covers empty/singleton and diagonal-collision
boundaries. This is not an independent global proof audit.

For the next test, retain a constant term that the source discards. In the AP
hypergraph H of a weak Sidon set, edges are three-term progressions and strong
Sidon subsets are independent sets. Distinct edges have different midpoints,
because otherwise two different off-diagonal pairs have equal sums. Neither
endpoint of the ordered set is a midpoint. Thus m_H<=n-2. For a (4,5)-set,
Ma–Tang also proves linearity and cites exclusion of the five-edge configuration

$$
 F_7=\{012,034,056,135,246\}
$$

on vertices 0,...,6. This is not the seven-edge Fano plane. Its quoted
Henning–Yeo theorem gives 17 tau(H)<=5n+3m_H. Therefore

$$
 h(A)=n-\tau(H)\ge(9n+6)/17,
 \qquad h(A)\ge\lceil(9n+6)/17\rceil \quad(n\ge2).
$$

This specialization is checked; the external transversal theorem and the cited
F_7 exclusion were not independently audited. For n<=8 the unrounded bound
already exceeds 4n/7. For n=9,...,15 the rounded bounds are respectively
6,6,7,7,8,8,9, none giving a ratio below 4/7. The n=1 case is immediate. Hence
no certificate with at most 15 points can improve 4/7 under these source
premises. At n=16 the bound is 9, and 9/16<4/7. A 16-point (4,5)-set with h=9 is
the first possible improving witness, not an assertion that one exists.

At n=16, a witness must have tau=7. The same inequality forces 119<=80+3m, so m
is 13 or 14. A finite investigation could test 16-vertex linear hypergraphs with 13
or 14 edges, the specified F_7 excluded, distinct ordered midpoints and
independence number nine, then seek real AP realizations satisfying the whole
(4,5)-condition. A rational solution to a fixed consistent pattern of equalities
and strict inequalities can be scaled to integers; this does not justify a
universal coordinate-box bound. A successful witness needs checks of all 1820
four-subsets and all 8008 ten-subsets. No such search was run. Failure in one
coordinate box would settle nothing about all reals.

The source's Lemma 3.6 and Proposition 3.7 also explain why finite ratios are
relevant asymptotically. For finite (4,5)-sets A,B, choose a scale for B
avoiding all equal nonzero within-set differences of A and the scaled B.
Translate B far enough that mixed distances exceed both internal diameters. All
mixed differences are distinct. A four-set split 3+1 has three distinct mixed
and at least two internal distances; a 2+2 split has four mixed and at least one
internal distance. Thus the union remains (4,5), while any Sidon subset has at
most h(A)+h(B) points. This proves subadditivity of the minimum h(n), and the
usual block division proves lim h(n)/n=inf h(n)/n. The argument does not make
the upper ratio optimal.

The exact input and deterministic checker live in
[[research/four_point_sidon_certificates/evidence/_index|the certificate
evidence]]. The 16-point search described above has not been run. Failure in a
bounded coordinate box would not exclude real realizations outside that box.

## Source interfaces

These source locators identify the uses in this account. Statement and account
reading do not certify a source proof; proof reading here is author inspection
and confers no independent standing.

- [[../library/additive_bases/ma_2026_largest_sidon_subsets_weak_sidon_sets/_index|Ma
  and Tang: Largest Sidon subsets in weak Sidon sets]]: Introduction Theorems
  1.2-1.6 and the explicit five-edge F7 definition; Section 5.2 quoted Lemma 5.2
  and Theorem 5.3 (statement reading). Propositions 2.1-2.2; Lemmas 2.3-2.5;
  Lemmas 3.5-3.6 and Proposition 3.7; Lemma 5.1; Section 5.2 lower-bound
  assembly (external theorem and F7 exclusion only quoted) (proof reading).
