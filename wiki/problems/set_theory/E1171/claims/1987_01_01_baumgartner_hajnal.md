---
name: problems/set_theory/E1171/claims/1987_01_01_baumgartner_hajnal
title: "Baumgartner and Hajnal: the cases k = 1 and k = 2 in ZFC"
desc: |
  Baumgartner and Hajnal (Contemp. Math. 65, 1987) prove that
  $(\kappa^+)^2\to(\kappa^+\kappa,3,3)^2$ for regular $\kappa$ with
  $\kappa^{<\kappa}=\kappa$. For $\kappa=\omega$ this is the ZFC case $k=2$ of
  Problem 1171, and that case contains the case $k=1$.
authors:
- James E. Baumgartner
- András Hajnal
status: accepted
claim: proved
scope: partial
evidence:
- reviewed
submitted: null
links:
- url: https://doi.org/10.1090/conm/065/891246
  kind: paper
- url: https://www.erdosproblems.com/1171
  kind: discussion
created: 2026-10-07T21:33:46Z
updated: 2026-10-07T21:33:46Z
---

***

**Claim.** As the zbMATH review of the paper (Zbl 0635.03042) states the result,
Baumgartner and Hajnal prove that for every regular cardinal $\kappa$ with
$\kappa^{<\kappa}=\kappa$

$$
(\kappa^+)^2\to(\kappa^+\kappa,3,3)^2;
$$

that is, every coloring of the pairs from the ordinal $(\kappa^+)^2$ with three
colors has a set of order type $\kappa^+\kappa$ homogeneous in color $0$ or a
triangle homogeneous in color $1$ or in color $2$. For $\kappa=\omega$ the
hypothesis $\omega^{<\omega}=\omega$ holds in ZFC and $\kappa^+=\omega_1$, so
$\omega_1^2\to(\omega_1\omega,3,3)^2$ is a theorem of ZFC: the case $k=2$ of
[[problems/set_theory/E1171/_index|Problem 1171]]. Leaving one triangle color
unused gives the case $k=1$, $\omega_1^2\to(\omega_1\omega,3)^2$. Komjáth's 2025
survey of the Erdős--Hajnal problem list restates the relation for
$\kappa=\omega$ (Problem 13 commentary and Problem 54 discussion) and describes
its proof as quite complicated. The result is compiled on the library's
[[../library/set_theory/baumgartner_1987_remark_partition_relations_infinite_ordinals/positive_relation|positive relation]]
page of the
[[../library/set_theory/baumgartner_1987_remark_partition_relations_infinite_ordinals/_index|source card]].

**Covers.** The instances $k=1$ and $k=2$ of the question, in ZFC. The relation
for $k\ge3$ is not addressed; Komjáth records the case $k=3$,
$\omega_1^2\to(\omega_1\omega,3,3,3)^2$, as unknown. The same paper shows that
the continuum hypothesis gives $\omega_1^2\not\to(\omega_1\omega,4)^2$, so the
triangle targets cannot be raised to four; that relation is context, not part of
this claim.

**Source.** James E. Baumgartner and András Hajnal, *A remark on partition
relations for infinite ordinals with an application to finite combinatorics*, in
Logic and combinatorics (Arcata, Calif., 1985), Contemporary Mathematics 65,
American Mathematical Society, Providence, RI, 1987, pp. 157--167; DOI
10.1090/conm/065/891246; Zbl 0635.03042. The paper is paywalled and not held;
its statement is taken from the zbMATH review and from Komjáth's restatement,
and its proof is not checked. The volume carries only the year, so this page is
dated the first of January 1987.

**Acceptance.** Reviewed: Péter Komjáth's survey, *The Erdős–Hajnal problem
list*, Bull. Symbolic Logic 31 (2025), 418–461, DOI 10.1017/bsl.2025.1, covers
the result in its Problem 13 commentary and Problem 54 discussion. It records
that Baumgartner and Hajnal proved $\omega_1^2\to(\omega_1\omega,3,3)^2$ in
ZFC, the case $\kappa=\omega$ of the claim, which is the case the problem uses.
The survey is refereed, and its author is not an author of the paper. The
volume is a conference proceedings, and no evidence that its papers were
refereed was found, so `refereed` is not listed. The site's commentary does not
cite the paper. Nothing on this page is independently reviewed by this project.

**Attribution of $k=1$.** Komjáth attributes the case $k=1$, in the form
$\omega_1^2\to(\omega_1\alpha,3)^2$ for every $\alpha<\omega_1$, to Erdős and
Hajnal, *Some results and problems on certain polarized partitions*, Acta Math.
Acad. Sci. Hungar. 21 (1970), 369--392. That paper says in its §1 that it does
not investigate relations for order types and gives its definitions for
cardinals only, so the attribution is not borne out there. The ordinal relation
$\omega_1^2\to(\mu,3)^2$ for $\mu<\omega_1^2$ is Theorem 5 of Erdős and Hajnal,
*Ordinary partition relations for ordinal numbers*, Period. Math. Hungar. 1
(1971), 171--185 (printed p. 181), stated with no hypothesis beyond ZFC,
although the zbMATH review (Zbl 0257.04004) summarizes the paper's relations
under GCH. So $k=1$ was proved in ZFC in 1971; it is the accepted partial claim
[[problems/set_theory/E1171/claims/1971_09_01_erdos_hajnal|Erdős and Hajnal 1971]],
and the 1987 relation contains it.

**Depends on.**
[[../library/set_theory/baumgartner_1987_remark_partition_relations_infinite_ordinals/positive_relation|Baumgartner and Hajnal 1987, positive relation]].
