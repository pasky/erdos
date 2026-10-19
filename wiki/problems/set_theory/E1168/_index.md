---
name: problems/set_theory/E1168
title: Problem 1168
desc: |
  Asks for a proof of
  $\aleph_{\omega+1}\not\to(\aleph_{\omega+1},3,\ldots,3)_{\aleph_0}^2$ without
  the generalized continuum hypothesis.
tags:
- Set theory
- Ramsey theory
status: open
claim: none
created: 2026-09-04T09:17:27Z
updated: 2026-10-19T04:19:00Z
---

# Problem 1168

[[problems/set_theory/_index|..]]

[[problems/set_theory/E1168/claims/_index|claims/]]: The 1 claim page of Problem 1168, one per claimant's result; the problem's standing derives from them.

***

**Statement.** Prove that

$$
\aleph_{\omega+1}\not\to (\aleph_{\omega+1}, 3,\ldots,3)_{\aleph_0}^2
$$

without assuming the generalised continuum hypothesis.

**Status.** Open.

**Source.** [erdosproblems.com/1168](https://www.erdosproblems.com/1168),
accessed 2026-09-04. Cite as: T. F. Bloom, Erdős Problem #1168,
https://www.erdosproblems.com/1168.

**Formalization.** None recorded.

## Current assessment

The status above is imported from the dated erdosproblems.com record. The
assessment covers two sources. Corollary 7 of Erdős, Hajnal and Rado (p. 132)
was read at $r=2$ and $\beta=\omega+1$, with Case 1b of its proof (p. 133) and
the printed hypothesis of Theorem 10 (p. 117), which that case cites, as
[[problems/set_theory/E1168/claims/1965_03_01_erdos_hajnal_rado|its claim page]]
records; no proof is reviewed here. The preprint of Garti, Hayut and Shelah
(arXiv:2502.16625v2) was read for its Theorem 0.1, its Section 2 and Theorem
1.3, and its statement that the question is open in ZFC. No wider literature
search is recorded. Komjáth's 2025 survey of the Erdős–Hajnal problem list was
not read for this question; Garti, Hayut and Shelah report that it records no
progress on it. The note below points to author-recorded research, which is
not independently reviewed.

## Known Results

[[research/erdos_1171/connections|The Problem 1171 connections page]] holds
author-recorded research on transferring the color-reduction lemma of
[[research/erdos_1171/lemma_2_1_reconstruction|the Problem 1171 folder]] to
this problem; it is not a claim.

Erdős, Hajnal and Rado proved the negative relation under the hypothesis
$2^{\aleph_\omega}=\aleph_{\omega+1}$, which the generalized continuum
hypothesis implies (Erdős, P., Hajnal, A. and Rado, R., Partition relations
for cardinal numbers, Acta Math. Acad. Sci. Hungar. 16 (1965), 93--196; the
erdosproblems.com remark credits this paper; Corollary 7, p. 132, at $r=2$ and
$\beta=\omega+1$). The result is recorded on
[[problems/set_theory/E1168/claims/1965_03_01_erdos_hajnal_rado|its claim page]]
as an accepted not-disprovable partial claim, which leaves the problem open.
Garti, Hayut and Shelah
([[../library/set_theory/garti_2025_problem_erdos_hajnal/_index|card]];
arXiv:2502.16625v2, 25 June 2026, Section 2) force the relation
$\aleph_{\omega+1}\not\to(\aleph_{\omega+1},(3)_{\aleph_0})^2$ from a
supercompact cardinal together with $\aleph_\omega$ a strong limit and
$2^{\aleph_\omega}>\aleph_{\omega+1}$, so the relation is consistent
without the local instance of the generalized continuum hypothesis; their
Theorem 1.3 obtains the same from a strong cardinal at
$\mu=\aleph_{\omega^2}$ in place of $\aleph_\omega$. Whether the relation
holds in ZFC, which is what the problem asks, the paper leaves open and says
it does not know. The consistency result settles no instance of the question
and is not a claim.
<!-- BEGIN problem library links -->

## Linked library material

These entries are derived from explicit links on library pages. They are
navigation only and do not by themselves record mathematical progress.

- [[../library/set_theory/garti_2025_problem_erdos_hajnal/_index|garti_2025_problem_erdos_hajnal]]

<!-- END problem library links -->
