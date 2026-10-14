---
name: problems/set_theory/E1171/claims/1971_09_01_erdos_hajnal
title: "Erdős and Hajnal: the case k = 1 in ZFC"
desc: |
  Erdős and Hajnal (Period. Math. Hungar., 1971) proved in ZFC that
  $\omega_1^2\to(\omega_1\omega,3)^2$, the case $k=1$ of Problem 1171.
authors:
- P. Erdős
- A. Hajnal
status: accepted
claim: proved
scope: partial
evidence:
- refereed
submitted: null
links:
- url: https://doi.org/10.1007/BF02029142
  kind: paper
  date: 1971-09-01
- url: https://users.renyi.hu/~p_erdos/1971-15.pdf
  kind: paper
- url: https://www.erdosproblems.com/1171
  kind: discussion
created: 2026-10-13T12:51:01Z
updated: 2026-10-13T12:51:01Z
---

***

**Claim.** Theorem 5 of the paper (printed p. 181, in §4, "Some positive
relations") states that for an arbitrary ordinal $\xi$, every $k<\omega$ and
every $t$ with $1\le t<\omega$,

$$
\omega_{\xi+1}^{(t+1)(k+1)}\to(\mu,t+2)^2
\quad\text{for every }\mu<\omega_{\xi+1}^{k+2}.
$$

The results of the paper that use the generalized continuum hypothesis open
with "Assume G.C.H.", Theorem 4 and Corollary 3 among them; Theorem 5 carries
no hypothesis beyond ZFC. With $\xi=0$, the paper's $k=0$, $t=1$ and
$\mu=\omega_1\omega<\omega_1^2$ it gives

$$
\omega_1^2\to(\omega_1\omega,3)^2,
$$

the case $k=1$ of [[problems/set_theory/E1171/_index|Problem 1171]]: every
coloring of the pairs from $\omega_1^2$ with two colors has a set of order
type $\omega_1\omega$ homogeneous in color $0$ or a triangle homogeneous in
color $1$. The same theorem is recorded for the triangle case of Problem 597
on
[[problems/set_theory/E0597/claims/1971_09_01_erdos_hajnal|the E0597 claim page]].

**Covers.** The instance $k=1$ of the question, in ZFC. It does not address
$k\ge2$: the case $k=2$, which contains $k=1$, is on the accepted page
[[problems/set_theory/E1171/claims/1987_01_01_baumgartner_hajnal|Baumgartner and Hajnal 1987]],
and the question is open in ZFC for $k\ge3$.

**Source.** P. Erdős and A. Hajnal, Ordinary partition relations for ordinal
numbers, Periodica Mathematica Hungarica 1 (1971), no. 3, 171–185,
doi:10.1007/BF02029142; the issue is dated September 1971 and carries no day, so
this page is dated the first of that month. The second paper link is the open
scan in the Rényi Institute's Erdős archive, on which the statement was read on
the page image and the paper's uses of G.C.H. in the text layer. The zbMATH
review (Zbl 0257.04004) summarizes the paper's relations, this one among them,
under GCH, which the paper itself assumes only where it says so. The proof, by
induction on $t$, begins on p. 182 with the case $t=1$ and rests on a lemma
derived from the free-set theorem of Erdős, Hajnal and Milner; it was not
checked, and nothing on this page is independently reviewed by this project.

**Acceptance.** Refereed: a journal paper in Periodica Mathematica Hungarica.
The site's commentary on Problem 1171 does not cite the paper, so `reviewed`
is not listed.
