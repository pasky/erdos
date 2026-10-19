---
name: polynomials/price_2026_perturbed_lobatto_nodes
title: "Price: Perturbed Lobatto nodes"
desc: |
  An unsigned write-up, posted by Liam Price, who credits the disproof to
  GPT-5.5 Pro, claiming that the least interpolation integral of Problem 1131
  is at most 2 - (1 + epsilon)/n for all large n, witnessed by the roots of
  the integral of P_{n-1} + a P_{n-3}, a perturbation of the Legendre-Lobatto
  nodes; so it is not 2 - (1 + o(1))/n.
license: unstated
created: 2026-10-14T22:51:14Z
updated: 2026-10-14T23:06:55Z
---

# Price: Perturbed Lobatto nodes

[[polynomials/_index|..]]

[[polynomials/price_2026_perturbed_lobatto_nodes/theorem_1|theorem_1]]: Claimed in an unsigned write-up credited to GPT-5.5 Pro: for some
epsilon > 0 and n_0, the least integral over [-1, 1] of the sum of the
squared Lagrange cardinal polynomials of n nodes in [-1, 1] is at most
2 - (1 + epsilon)/n for every n >= n_0, witnessed by the roots of the
integral of P_{n-1} + a P_{n-3} for a fixed small a > 0.

***

*Perturbed Lobatto nodes*, preprint (2026), 11 pp., posted by Liam Price. The
print has no author line, no date, no acknowledgment and no bibliography, and
names no AI system; its information dictionary has no author entry and a
creation timestamp of 14 October 2026, 22:19 UTC, consistent with the compile
that produced the copy read here. The attribution is the erdosproblems.com
thread's: Liam Price linked the project in the Problem 1131 discussion thread
on 26 April 2026 with the words "GPT-5.5 Pro claims a disproof of the claimed
asymptotic here", as the
[[../wiki/problems/polynomials/E1131/claims/2026_04_26_price|claim page]]
records. No notice is printed in the eleven pages, which state no license;
the hosting site's terms speak for the site, not the paper: Overleaf's terms
page (https://www.overleaf.com/legal), as read on 2026-10-02 for the card of
Price's
[[additive_bases/price_2026_counterexample_erdos_problem_346/_index|counterexample to Problem 346]],
says "We don't claim any ownership of your stuff" and grants readers of a
shared project no license; the term is unstated.

Theorem 1 (p. 1) concerns $M_n$, the least value over nodes
$x_0,\dots,x_{n-1}\in[-1,1]$ of $\int_{-1}^1\sum_{i=0}^{n-1}l_i(x)^2\,dx$,
where $l_i$ is the Lagrange cardinal polynomial of $x_i$: there are
$\varepsilon>0$ and $n_0$ with $M_n\le2-(1+\varepsilon)/n$ for every
$n\ge n_0$, so that $M_n\ne2-(1+o(1))/n$. Section 1 (pp. 1--2) puts $N=n-1$
and takes as nodes the $N+1$ roots of
$Q_{N,a}(x)=\int_{-1}^x(P_N(t)+aP_{N-2}(t))\,dt$, with $P_m$ the Legendre
polynomial normalized by $P_m(1)=1$ and $a$ a real parameter; for $N\ge3$ and
$|a|\le1/100$ these roots are real, simple and include $\pm1$, and at $a=0$
they are the Legendre--Lobatto nodes. Section 2 (pp. 2--6) writes the
integral $I_N(a)$ at these nodes as the trace of the inverse of the Legendre
Christoffel kernel matrix, splits that matrix exactly into a positive diagonal
part and a rank-three part, and reaches
$I_N(a)=2-\operatorname{tr}(\mathcal A(a)^{-1}C(a)B(a))$ with explicit
$3\times3$ matrices ((28), p. 6). Section 3 (pp. 6--8) proves
$|I_N''(a)|\le C/N$ for $|a|\le a_0$, with $C$ and $a_0>0$ absolute ((29),
(53)). Section 4 (pp. 8--10) computes $I_N(0)=2-2/(2N+1)$ ((55)) and
$I_N'(0)=-4(N+1)/(3(N-1)(2N+1))$ ((64)). Section 5 (pp. 10--11) combines
them into $n(2-I_N(a))=1+2a/3+O(a^2)+o(1)$ ((66)) and fixes a small $a>0$.
The [[polynomials/price_2026_perturbed_lobatto_nodes/theorem_1|Theorem 1 page]]
states the node family and the uniform expansion exactly.

At $a=0$ the nodes are the roots of $\int_{-1}^xP_{n-1}(t)\,dt$, the
extremal nodes of
[[polynomials/fejer_1932_bestimmung_derjenigen_abszissen_eines_intervalles/main_theorem|Fejér's theorem on the least maximum of the sum of squares]],
and the value (55), $2-2/(2n-1)$ with $n=N+1$, is the one computed on that
page and recorded on the problem page as the upper bound of Erdős, Szabados,
Varma and Vértesi. The write-up lowers that bound within one explicit family
of perturbed nodes; it proves no lower bound for $M_n$.

Source: <https://www.overleaf.com/read/mhmzxwcsqjyd>, the project Price's post
links. The copy read is the PDF that Overleaf's viewer compiled from it,
downloaded on 2026-10-14. A project can be edited and recompiled at that
address, so the copy is of 2026-10-14; no copy of the document as it stood
when it was posted is known to the corpus.

Read status: claims checked. Theorem 1 (p. 1), the node family of Section 1
(pp. 1--2) and the displays (28), (29), (48)--(55) and (64)--(66) (pp. 6--10)
were read clause by clause on the page images; the proofs were read for
structure only. Of the proof, only the closing arithmetic was redone by hand:
(55) from the three weight sums before it, (64) from (61) and (63), and (66)
from (65) with $n=N+1$. No other step was checked, the rank-three formula
(17) and the uniform bound (53) included, and nothing here is independently
reviewed.
Result page:
[[polynomials/price_2026_perturbed_lobatto_nodes/theorem_1|theorem_1]].

**Bears on.**

- [[../wiki/problems/polynomials/E1131/_index|#1131]]: Theorem 1 (p. 1) gives
  $n(2-M_n)\ge1+\varepsilon$ for every $n\ge n_0$, so the displayed
  asymptotic $\min I=2-(1+o(1))/n$ fails and the problem's second question
  is answered no; it proves no lower bound for $\min I$ and leaves the first
  question open. Neither $\varepsilon$ nor $n_0$ is evaluated. The write-up
  is the document behind the pending
  [[../wiki/problems/polynomials/E1131/claims/2026_04_26_price|claim of Price]].

**Results.**

- Theorem 1 (p. 1), with the node family of Section 1 (pp. 1--2) and the
  uniform expansion (65)--(66) (p. 10): $M_n\le2-(1+\varepsilon)/n$ for every
  $n\ge n_0$, witnessed by the $n$ roots of $Q_{n-1,a}$ for a fixed small
  $a>0$.

No file of this source is held: no license on record permits its redistribution,
and the card cites the edition it names above.
