---
name: problems/set_theory/E1168/claims/1965_03_01_erdos_hajnal_rado
title: The negative relation at aleph_{omega+1} under GCH
desc: |
  Corollary 7 of Erdős, Hajnal and Rado (Acta Math. Acad. Sci. Hungar., 1965)
  gives, under GCH, the negative relation of Problem 1168. GCH is consistent
  with ZFC, so ZFC, if consistent, does not refute the relation.
authors:
- P. Erdős
- A. Hajnal
- R. Rado
status: accepted
claim: not_disprovable
scope: partial
evidence:
- refereed
submitted: null
links:
- url: https://doi.org/10.1007/BF01886396
  kind: paper
  date: 1965-03
- url: https://www.erdosproblems.com/1168
  kind: discussion
created: 2026-10-13T14:08:51Z
updated: 2026-10-13T14:08:51Z
---

***

**Claim.** Corollary 7 of P. Erdős, A. Hajnal and R. Rado, Partition
relations for cardinal numbers, Acta Math. Acad. Sci. Hungar. 16 (1965),
no. 1--2, 93--196 (the corpus's
[[../library/ramsey_theory/erdos_1965_partition_relations_cardinal_numbers/_index|source card]]),
stated in §15.6 (p. 132) as one of the three propositions behind part (i) of
the first Main Theorem, carries the mark $(*)$ that the paper prefixes to
results whose proofs assume the General Continuum Hypothesis (pp. 96--97). For
$r=2$ it states
$\aleph_\beta\not\to(\aleph_\beta,(3)_{\aleph_{\mathrm{cr}(\beta)}})^2$
for every ordinal $\beta$, where $\mathrm{cr}(\beta)$ is the paper's critical
number (§15.1, p. 130); when $\beta=\alpha+1$,
$\aleph_{\mathrm{cr}(\beta)}=\mathrm{cf}(\aleph_\alpha)$ (pp. 96 and 130). For
$\beta=\omega+1$ this gives
$\aleph_{\mathrm{cr}(\omega+1)}=\mathrm{cf}(\aleph_\omega)=\aleph_0$, and the
statement is the relation of
[[problems/set_theory/E1168/_index|Problem 1168]],

$$
\aleph_{\omega+1}\not\to(\aleph_{\omega+1},(3)_{\aleph_0})^2,
$$

the case written as display (11) in the proof (p. 133). GCH holds in Gödel's
constructible universe, so if ZFC is consistent, so is ZFC with the relation,
and ZFC does not refute it. The specialization to $\beta=\omega+1$ is this
page's.

**Covers.** The not-disprovable side of Problem 1168, relative to the
consistency of ZFC: the relation holds in every model of ZFC with GCH. It does
not prove the relation in ZFC, which is what the problem asks, and one side
alone leaves the question open. Garti, Hayut and Shelah
([[../library/set_theory/garti_2025_problem_erdos_hajnal/_index|card]])
restate the result as their Theorem 0.1, for singular $\lambda$ with
$2^\lambda=\lambda^+$, and force the relation at $\aleph_{\omega+1}$ together
with $2^{\aleph_\omega}>\aleph_{\omega+1}$; the problem page records that
work as context.

**Acceptance.** Refereed: the result is a journal paper in the Acta
Mathematica Academiae Scientiarum Hungaricae, volume 16, issue 1--2. The issue
is dated March 1965 and carries no day, so this page's date is the first of
that month. The site credits the result to the paper, under GCH, on a problem
it labeled OPEN, so no curator acceptance is listed. The proof of the case
$\beta=\alpha+1$ with $\aleph_\alpha$ singular (Case 1b, p. 133) cites
Theorem 10, which is printed (p. 117) for $a>a'>\aleph_0$, where $a'$ is the
cofinality of $a$; at $\alpha=\omega$ the cardinal $a=\aleph_\omega$ has
$a'=\aleph_0$, outside that printed hypothesis. This corpus has not checked
whether the proof of Theorem 10 covers countable cofinality, and the proofs
are not reviewed here. The result does not rest on that printed route alone:
Garti, Hayut and Shelah
([[../library/set_theory/garti_2025_problem_erdos_hajnal/_index|card]];
Theorem 0.1, p. 2) state it for every singular $\lambda$ with
$2^\lambda=\lambda^+$, countable cofinality included, as phrased and proved in
the 1984 monograph of Erdős, Hajnal, Máté and Rado, *Combinatorial set
theory: partition relations for cardinals* (North-Holland), whose Theorem 20.2
they cite as a stronger form. The monograph is not read here.

**Depends on.** No other wiki page; the claim rests on the paper above.
