---
name: problems/additive_combinatorics/E0335
title: Problem 335
desc: |
  Asks for a characterization of the pairs of sets $A,B$ of integers with
  positive density such that $d(A+B)=d(A)+d(B)$.
tags:
- Number theory
- Additive combinatorics
status: open
claim: none
created: 2026-09-04T09:17:27Z
updated: 2026-10-15T01:58:15Z
---

# Problem 335

[[problems/additive_combinatorics/_index|..]]

[[problems/additive_combinatorics/E0335/claims/_index|claims/]]: The 1 claim page of Problem 335, one per claimant's result; the problem's standing derives from them.

***

**Statement.** Let $d(A)$ denote the density of $A\subseteq \mathbb{N}$.
Characterise those $A,B\subseteq \mathbb{N}$ with positive density such that

$$
d(A+B)=d(A)+d(B).
$$

**Status.** Open, the erdosproblems.com label (OPEN; page last edited
2026-04-15). One partial claim is recorded:
[[problems/additive_combinatorics/E0335/claims/2026_04_14_ackelsberg_richter|Ackelsberg and Richter's inverse theorem]],
a preprint of 2026-04-14. Its Theorem 1.4 characterizes the pairs in which one
of the sets meets every residue class. The characterization without that
assumption is not settled.

**Source.** [erdosproblems.com/335](https://www.erdosproblems.com/335), accessed
2026-09-04. Cite as: T. F. Bloom, Erdős Problem #335,
https://www.erdosproblems.com/335.

**References.**

- [AcRi26] E. Ackelsberg and F. K. Richter,
  [[../library/additive_combinatorics/ackelsberg_2026_inverse_theorem_sumsets_sets_positive_density/_index|An inverse theorem for sumsets of sets of positive density in the integers]].
  arXiv:2604.12864 (2026).

**Formalization.** None recorded.

## Current assessment

The erdosproblems.com formulation above asks for the pairs
$A,B\subseteq\mathbb N$ of positive density with $d(A+B)=d(A)+d(B)$. The
erdosproblems.com commentary, in the corpus's words: equality holds when there
is a $\theta>0$ and sets $X_A,X_B\subseteq\mathbb R/\mathbb Z$ with
$\mu(X_A+X_B)=\mu(X_A)+\mu(X_B)$ such that $A$ and $B$ are the positive integers
$n$ whose fractional parts $\{n\theta\}$ fall in $X_A$ and $X_B$, and
erdosproblems.com asks whether every pair arises in a similar way from other
groups. erdosproblems.com credits Ackelsberg and Richter [AcRi26] with a partial
resolution under the assumption that one of the sets meets every residue class,
recorded at
[[problems/additive_combinatorics/E0335/claims/2026_04_14_ackelsberg_richter|Ackelsberg
and Richter's inverse theorem]]: for $d(A)>0$, $d(A)+d(B)<1$ and $B$ meeting
every residue class, either both sets come, up to density zero, from a
rotation on a subsemigroup $h\mathbb N$ (lifts of parallel Bohr intervals),
or $A$ lies in one residue class modulo some $h$ and $B$ covers almost all of
the other classes, the paper's degenerate case. erdosproblems.com also records
that a full characterization without that assumption looks hopeless, since a
random subset $A$ of the even numbers of density $1/4$ has $d(A+A)=1/2$; the
paper's Example 1.6 is this example. The claim is a preprint without outside
review, so it stays `claimed`, and as a partial claim it leaves the problem
open.

**Search scope.** The account above rests on the erdosproblems.com problem page,
the arXiv record of the paper (version of 2026-04-14) and the library card of
that version. The proof is not checked here, and no literature search beyond
these sources is recorded.
## A periodic case outside the residue-class hypothesis

The sets $A=B=\{n\ge1:n\bmod7\in\{0,1,3\}\}$ have density $3/7$.
Their sumset eventually contains exactly the six residues

$$
\{0,1,3\}+\{0,1,3\}=\{0,1,2,3,4,6\}\pmod7,
$$

so $d(A+B)=6/7=d(A)+d(B)<1$. Yet $B$ misses a residue class modulo $7$,
while $\gcd(B-B)=1$ because $7,8\in B$. Dividing out a common difference
therefore cannot bring this equality case under Ackelsberg–Richter's
all-residue-class hypothesis. Translations still miss a residue class;
an integral dilation of absolute value greater than one misses residue
classes modulo that dilation.

This finite calculation by Plasma AI is an author-recorded obstruction to that
normalization step, not a counterexample to the theorem or to a broader
classification. A general treatment still needs a theorem addressing the
periodic cases outside its hypothesis. No source proof is independently
verified by this example.

<!-- BEGIN problem library links -->

## Linked library material

These entries are derived from explicit links on library pages. They are
navigation only and do not by themselves record mathematical progress.

- [[../library/additive_combinatorics/ackelsberg_2026_inverse_theorem_sumsets_sets_positive_density/_index|ackelsberg_2026_inverse_theorem_sumsets_sets_positive_density]]

<!-- END problem library links -->
