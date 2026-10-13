---
name: problems/ramsey_theory/E0809/claims/2026_03_19_bucic_chen_ma
title: Bucić, Chen and Ma settle the odd cycles of length at least nine
desc: |
  Theorem 1.2 of the 2026 preprint of Bucić, Chen and Ma shows that, one edge
  past the Turán number, the maximal anti-Ramsey function of $C_{2k+1}$ is
  asymptotically $n^2/8$ for every $k\ge4$. It is unrefereed and formalized in
  the $k\ge4$ branch of L17.
authors:
- Matija Bucic
- Kaizhe Chen
- Jie Ma
status: accepted
claim: proved
scope: partial
evidence:
- formalized
submitted: null
links:
- url: https://arxiv.org/abs/2603.18952v1
  kind: preprint
  date: 2026-03-19
- url: https://www.erdosproblems.com/809
  kind: discussion
- url: https://github.com/plasma-ai/erdos-809/tree/0f27743fabd97b262d2fce7946de9f0b3325a625
  kind: formalization
  date: 2026-09-27
- url: https://github.com/Asad-Shahab/erdos-809-lean/tree/cfa2b4427b523d1dfaa40d538c99776380840374
  kind: formalization
  date: 2026-09-27
created: 2026-10-07T06:38:59Z
updated: 2026-10-08T01:38:41Z
---

***

**Claim.** [[problems/ramsey_theory/E0809/_index|Problem 809]] asks whether
$\chi_S(n,\lfloor n^2/4\rfloor+1,C_{2k+1})\sim n^2/8$ for every $k\ge3$.
Bucić, Chen and Ma's
[[../library/ramsey_theory/bucic_2026_maximal_anti_ramsey_conjecture_burr_erdos/theorem_1_2|Theorem 1.2]]
(arXiv:2603.18952v1, p. 2) states that for every integer $k\ge4$ and every
$e$ with $\lfloor n^2/4\rfloor+1\le e\le\binom n2$,

$$
f(n,e,C_{2k+1})=\frac e2+\frac n2\sqrt{e-\frac{n^2}4}+o(n^2),
$$

where $f(n,e,H)$ is the least number of colors in an edge-coloring of some
$n$-vertex graph with at least $e$ edges in which every copy of $H$ is
rainbow. At $e=\lfloor n^2/4\rfloor+1$ the square-root term is at most $n/2$,
so the theorem gives $n^2/8+o(n^2)$, and the paper's $f$ agrees with the
site's $\chi_S$, defined with exactly $e$ edges, because deleting edges keeps
every remaining copy rainbow and adds no color (two one-line readings made on
the problem page). The upper bound is the two-clique coloring that Burr,
Erdős, Graham and Sós already observed; the lower bound, display (1) of the
paper, is its new content.

**Covers.** Every $k\ge4$, the cycles $C_9,C_{11},\ldots$; the paper states its
Conjecture 1.1 for all $k\ge3$ and proves it for $k\ge4$. The seven-cycle,
$k=3$, is outside Theorem 1.2; the paper proves nothing for it, and its closing
remark (p. 11) says that for $k=3$ the authors have a more involved "stability"
argument, not given in the paper, that gets past the path-length obstacle "in
the second case", leaving "the first case as the main bottleneck".

**Depends on.** The result is the paper's own theorem; its `formalized`
evidence is the $k\ge4$ branch of
[[theory/ramsey_theory/L17_rainbow_odd_cycle_threshold/_index|L17]].

**Acceptance.** Formalized: the $k\ge4$ branch of the project's claim
[[theory/ramsey_theory/L17_rainbow_odd_cycle_threshold/_index|L17]] is Lean that
this corpus built and audited. That branch is
`Erdos.Library.Problem809.BucicChenMa`, a Lean reconstruction of the paper's
argument, linked above. It is kernel-checked on `propext`, `Classical.choice`
and `Quot.sound` only. L17's audited statement contains every $k\ge4$ instance
this page covers. The same development proves the full-range formula, but only
its consequence at $e=\lfloor n^2/4\rfloor+1$ lies inside the audited statement.

The site's curator credits the paper in the problem's commentary, which was
updated after a thread comment of 20 March 2026 (read 2026-09-18 and unchanged
as of 2026-10-07). The site labels the problem OPEN, so that credit is not
acceptance. The site's proof-claim tab did not carry the paper on 2026-10-05.
The paper is an arXiv preprint with one version (19 March 2026). No journal
record was found on 2026-09-18, so no refereeing is listed. This corpus checked
the definition, the statement, display (1) and the Section 2 sketch clause by
clause, and did not read the proof.

Two Lean developments declare a formalization of the theorem and are linked
above as such. The first is the $k\ge4$ branch of L17, which also gives
[[problems/ramsey_theory/E0809/claims/2026_09_27_plasma_ai|the project's own claim page]]
its `formalized` evidence. Its repository is linked at `0f27743`, the commit
the registry entry pins; later commits, through `f2ad237` as of 2026-10-13,
changed only the README and the author line and one broken citation of the
project's write-up, which is current at `eb385a8` of 29 September 2026. The
second is the development of
[[problems/ramsey_theory/E0809/claims/2026_09_27_shahab|Shahab]], which
formalizes the paper's argument beside its own seven-cycle proof. This corpus
built that development at its pinned commit and audited its headline statement,
as Shahab's claim page records. Its theorem
`Erdos809.erdos_809_long_odd_cycles`, which the audited headline
`Erdos809.erdos_809` applies for every $k\ge4$, proves the instances this page
covers at $e=\lfloor n^2/4\rfloor+1$, on `propext`, `Classical.choice` and
`Quot.sound` only. Only that threshold case lies inside the audited statement. A
Lean proof built and audited here that checks the statement is `formalized`
evidence. So Shahab's development gives this page that evidence a second time,
independently of L17.
