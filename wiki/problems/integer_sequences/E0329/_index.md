---
name: problems/integer_sequences/E0329
title: Problem 329
desc: |
  Asks how large $\limsup_{N\to\infty}|A\cap\{1,\ldots,N\}|/N^{1/2}$ can be for
  an infinite Sidon set $A\subseteq\mathbb{N}$.
tags:
- Number theory
- Sidon sets
status: open
claim: none
created: 2026-09-04T09:17:27Z
updated: 2026-10-15T01:58:15Z
---

# Problem 329

[[problems/integer_sequences/_index|..]]

***

**Statement.** Suppose $A\subseteq \mathbb{N}$ is a Sidon set. How large can

$$
\limsup_{N\to \infty}\frac{\lvert A\cap \{1,\ldots,N\}\rvert}{N^{1/2}}
$$

be?

**Status.** Open.

**Source.** [erdosproblems.com/329](https://www.erdosproblems.com/329), accessed
2026-09-04. Cite as: T. F. Bloom, Erdős Problem #329,
https://www.erdosproblems.com/329.

**References.**

- [CiTr01] Cilleruelo, Javier and Trujillo, Carlos, Infinite $B_2[g]$ sequences.
  Israel J. Math. (2001), 263-267.
- [Er80] Erdős, Paul, A survey of problems in combinatorial number theory. Ann.
  Discrete Math. (1980), 89-115.
- [ErTu41] Erdős, P. and Turán, P., On a problem of Sidon in additive number
  theory, and on some related problems. J. London Math. Soc. (1941), 212-215.
- [Ko96] Kolountzakis, Mihail N., On the additive complements of the primes and
  sets of similar growth. Acta Arith. (1996), 1-8. The erdosproblems.com
  commentary credits Kolountzakis under the key [Ko96] with an infinite $B_2[2]$
  sequence whose $\limsup$ of $|A\cap\{1,\ldots,N\}|/N^{1/2}$ is $1$; the
  erdosproblems.com reference record resolves the key to this paper on additive
  complements of the primes (Acta Arith. 77), the entry it shares with
  Problem 32. The construction is Theorem 4 of M. N. Kolountzakis, The density
  of $B_h[g]$ sequences and the minimum of dense cosine sums, J. Number Theory
  56 (1996), 4-11, DOI 10.1006/jnth.1996.0002, which [CiTr01] lists as its
  reference [4]
  ([[../library/additive_bases/kolountzakis_1996_density_b_h_g_sequences_minimum/_index|library card]]).
- [Kr61] Krückeberg, Fritz, $B\sb{2}$-Folgen und verwandte Zahlenfolgen. J.
  Reine Angew. Math. (1961), 53-60.

**Formalization.** Statement in
[formal-conjectures](https://github.com/google-deepmind/formal-conjectures/blob/main/FormalConjectures/ErdosProblems/329.lean).

## Current assessment

The question, as erdosproblems.com states it (page last edited 6 April 2026):
over all infinite Sidon sets $A\subseteq\mathbb N$, how large can
$\limsup_{N\to\infty}|A\cap\{1,\ldots,N\}|/N^{1/2}$ be? No independent
assessment of proof coverage is recorded, and the problem has no claim page.
The erdosproblems.com commentary credits bounds from both sides. Erdős and Turán
[ErTu41] proved that a Sidon set in $\{1,\ldots,N\}$ has at most
$N^{1/2}+O(N^{1/4})$ elements, so the $\limsup$ is at most $1$ for every
infinite Sidon set
([[../library/additive_bases/erdos_1941_problem_sidon_additive_number_theory_related/_index|library card]]).
Erdős [Er80] showed that the value $1/2$ is attained, and Krückeberg [Kr61]
that $1/\sqrt2$ is attained. Erdős and Krückeberg conjectured [Er80] that $1$
is attained; erdosproblems.com records that this would follow from a positive
answer to [[problems/additive_bases/E0044/_index|Problem 44]], on extending a
finite Sidon set to a Sidon set of near-maximal size. The bounds bracket the
asked value between $1/\sqrt2$ and $1$ but do not determine it, so they settle
no instance and have no claim page. For the relaxation to $B_2[g]$ sequences, in
which $n=a_1+a_2$ with $a_1\le a_2$ has at most $g$ solutions, Theorem 4 of
Kolountzakis ([Ko96] above) gives an infinite $B_2[2]$ sequence with
$\limsup=1$, and Cilleruelo and Trujillo [CiTr01] give, for every $g\ge2$, an
infinite $B_2[g]$ sequence with a larger explicit value, $(3/2)^{1/2}$ for
$g=2$
([[../library/additive_bases/cilleruelo_2001_infinite_b_2_g_sequences/_index|library card]]);
these concern a wider class of sets than the problem asks about and are not
claims on it.

Search scope. On 2026-10-07 the erdosproblems.com page listed no proof claim,
its discussion thread held one comment, of 18 November 2025, on the page's tags,
and the formal-conjectures statement file stated the question as open and
recorded the three credited bounds as variants without a formal proof.

## Research

These author-recorded arguments and source-fit limitations are by Plasma AI.
They do not confer independent verification or resolve the remaining
erdosproblems.com question.

Sidon sums are unordered, with doubles allowed; the target concerns an infinite
set's limsup.

Let $A\subset[1,M]$, $B\subset[1,L]$ be Sidon, $L\ge M$.
Each positive difference of $A$ occurs in at most one ordered pair in
$B$. Delete one endpoint of every such pair to obtain $B'$, losing
at most $\binom{|A|}{2}$ points. Then $A,B'$ share no positive
difference. For $T=L+M+1$, old-old, old-new and new-new sums in
$A\cup(T+B')$ occupy disjoint intervals
$$
 [2,2M],\quad[T+2,T+L+M],\quad[2T+2,2T+2L].
$$
A middle-interval collision would give a common nonzero difference;
the other two intervals are Sidon already. Thus the union is Sidon
and lies in $[1,2L+M+1]$.

For a fixed prefix and near-optimal finite block of size $(1-o(1))\sqrt L$, this
gives ratio $1/\sqrt2$, not an improvement. A displacement $o(L)$ leaves mixed
relations with three new elements and one old, $T+b_1+b_2-b_3=a$, uncontrolled
by difference deletions.

E0044's exact extension statement and the held Kolountzakis Theorem 4 account
were read. The latter is $B_2[2]$; permitting a second representation is
precisely the relaxation that cannot be removed.

The unresolved obligation is to adjoin a near-optimal block at displacement
o(block length) while controlling all mixed sum coincidences. A useful test is
to use a fixed old prefix and a translated new block T+B of length L with
T=o(L), bound the deletions needed to exclude T+b1+b2-b3=a with a in the prefix,
beyond the easy repeated-difference deletions. Stop at an unproved o(sqrt(N))
deletion estimate or use of a B2[2] construction as if it were Sidon.

Source interfaces:
[[../library/additive_bases/kolountzakis_1996_density_b_h_g_sequences_minimum/theorem_4|Theorem
4, definitions and extension proof account]].

<!-- BEGIN problem library links -->

## Linked library material

These entries are derived from explicit links on library pages. They are
navigation only and do not by themselves record mathematical progress.

- [[../library/additive_bases/cilleruelo_2001_infinite_b_2_g_sequences/_index|cilleruelo_2001_infinite_b_2_g_sequences]]
- [[../library/additive_bases/cilleruelo_2001_infinite_b_2_g_sequences/theorem_1|cilleruelo_2001_infinite_b_2_g_sequences / theorem_1]]
- [[../library/additive_bases/erdos_1941_problem_sidon_additive_number_theory_related/_index|erdos_1941_problem_sidon_additive_number_theory_related]]
- [[../library/additive_bases/erdos_1941_problem_sidon_additive_number_theory_related/remark_p214|erdos_1941_problem_sidon_additive_number_theory_related / remark_p214]]
- [[../library/additive_bases/erdos_1941_problem_sidon_additive_number_theory_related/theorem_p212_upper_bound|erdos_1941_problem_sidon_additive_number_theory_related / theorem_p212_upper_bound]]
- [[../library/additive_bases/kolountzakis_1996_additive_complements_primes_sets_similar_growth/_index|kolountzakis_1996_additive_complements_primes_sets_similar_growth]]
- [[../library/additive_bases/kolountzakis_1996_density_b_h_g_sequences_minimum/_index|kolountzakis_1996_density_b_h_g_sequences_minimum]]
- [[../library/additive_bases/kolountzakis_1996_density_b_h_g_sequences_minimum/theorem_4|kolountzakis_1996_density_b_h_g_sequences_minimum / theorem_4]]

<!-- END problem library links -->
