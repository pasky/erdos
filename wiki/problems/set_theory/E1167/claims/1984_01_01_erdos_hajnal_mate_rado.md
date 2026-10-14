---
name: problems/set_theory/E1167/claims/1984_01_01_erdos_hajnal_mate_rado
title: Five cases of the negative stepping-up lemma
desc: |
  Erdős, Hajnal, Máté and Rado's monograph (North-Holland, 1984) proves the
  stepping-up implication in five cases, under the conditions of the
  Erdős–Hajnal list. It is accepted on Komjáth's refereed survey, which records
  the five cases as proved.
authors:
- Paul Erdős
- András Hajnal
- Attila Máté
- Richard Rado
status: accepted
claim: proved
scope: partial
evidence:
- reviewed
submitted: null
links:
- url: https://mathscinet.ams.org/mathscinet-getitem?mr=795592
  kind: paper
  date: 1984
- url: https://www.erdosproblems.com/1167
  kind: discussion
created: 2026-10-07T19:24:20Z
updated: 2026-10-07T19:24:20Z
---

***

**Claim.** Let $2\le r<\omega$, let $\gamma\ge2$, and let $\kappa_\alpha>r$ for
$\alpha<\gamma$. Section 24 of Erdős, Hajnal, Máté and Rado's monograph
Combinatorial Set Theory: Partition Relations for Cardinals proves that
$2^\lambda\to(\kappa_\alpha+1)^{r+1}_{\alpha<\gamma}$ implies
$\lambda\to(\kappa_\alpha)^r_{\alpha<\gamma}$ in each of five cases: all
$\kappa_\alpha$ are finite; $\kappa_0$ and $\kappa_1$ are infinite and
$\kappa_0$ is regular; $r\ge3$ and $\kappa_0$ is infinite and regular;
$r\ge3$ and $\kappa_0$ and $\kappa_1$ are infinite; $r\ge4$ and $\kappa_0$ is
infinite. Komjáth's Problem 2 commentary
([[../library/set_theory/komjath_2025_erdos_hajnal_problem_list/_index|source card]])
records the same five cases as proved, citing that section of the monograph,
and the erdosproblems.com remark lists them too.

**Covers.** The implication of
[[problems/set_theory/E1167/_index|Problem 1167]] in the five cases above,
under the list's conditions $2\le r<\omega$, $\gamma\ge2$ and $\kappa_\alpha>r$.
Without the condition on $\gamma$ the third case would include the literal
counterexample $\gamma=1$, $\kappa_0=\lambda^+$, recorded on
[[problems/set_theory/E1167/claims/2026_01_31_zeraoulia|Zeraoulia's page]].
The case Erdős and Hajnal named as the hardest, $r=2$ with one singular
$\kappa_\alpha$ and the others finite, is not covered.

**Depends on.** No page of this wiki.

**Source.** P. Erdős, A. Hajnal, A. Máté and R. Rado, Combinatorial Set
Theory: Partition Relations for Cardinals, Studies in Logic and the
Foundations of Mathematics 106, North-Holland, Amsterdam, 1984 (MR 795592).
The record carries no day or month, so this page's date is the first of the
year.

**Acceptance.** Reviewed: Péter Komjáth's survey, *The Erdős–Hajnal problem
list*, Bull. Symbolic Logic 31 (2025), 418–461, DOI 10.1017/bsl.2025.1, covers
the result in its Problem 2 commentary. It records the five cases as already
proved, citing Section 24 of the monograph. The survey is refereed, and its
author is not an author of the monograph. The result is in a monograph, not a
journal paper, so `refereed` is not listed. Bloom's catalog labeled the problem
OPEN, and its remark listing the cases is commentary, not counted. Nothing on
this page is independently reviewed by this project.
