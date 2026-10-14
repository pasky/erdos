---
name: problems/extremal_graph_theory/E1157/claims/2026_09_29_chao_huang_liu
title: Chao, Huang and Liu's leading constants at the integer exponents
desc: |
  An arXiv preprint of Chao, Huang and Liu claims the limit of
  $\mathrm{ex}_r(n,\mathcal F)/n^t$ whenever $k=(r-t)s+t$ with $r>t\ge2$, in
  closed form depending on the parity of $s$, except for $3$-graphs with even
  $s$, where it shows for $s\ge4$ that the limit exceeds $1/6$. This answers the
  problem to first order on that family only.
authors:
- Ting-Wei Chao
- Xinqi Huang
- Hong Liu
status: claimed
claim: answered
scope: partial
submitted: null
links:
- url: https://arxiv.org/abs/2609.38115v1
  kind: preprint
  date: 2026-09-29
created: 2026-10-13T10:10:58Z
updated: 2026-10-13T12:26:33Z
---

***

**Claim.** Ting-Wei Chao, Xinqi Huang and Hong Liu, *Asymptotics of the
Brown–Erdős–Sós problem at integer exponents*, arXiv:2609.38115v1 (29 September
2026, 22 pages, the only version), write $f^{(r)}(n;s,k)$ for the largest
number of edges of an $n$-vertex $r$-graph in which no $k$ distinct edges span
at most $s$ vertices. Their $s$ is erdosproblems.com's vertex count $k$ and
their $k$ is erdosproblems.com's edge count $s$, so their function is
erdosproblems.com's $\mathrm{ex}_r(n,\mathcal F)$, as the Formulation note of
[[problems/extremal_graph_theory/E1157/_index|Problem 1157]] explains; this page
uses erdosproblems.com's letters. When $(rs-k)/(s-1)$ is an integer $t$ with
$2\le t<r$, that is $k=(r-t)s+t$, the order of $\mathrm{ex}_r(n,\mathcal F)$ is
$n^t$, and the paper asks for
$\pi(r,t,s)=\lim_{n\to\infty}n^{-t}\mathrm{ex}_r(n,\mathcal F)$. Theorem 1.1
(p. 2): for all $r>t\ge2$ and $s\ge2$,

$$
\pi(r,t,s)=\frac{2}{t!\,\bigl(2\binom rt-1\bigr)}\ \text{for odd }s,\qquad
\pi(r,t,s)=\frac{1}{t!\binom rt}\ \text{for even }s\text{ and }r\ge4.
$$

For $3$-graphs ($r=3$, $t=2$, $k=s+2$) this gives $\pi(3,2,s)=1/5$ for every
odd $s$. The theorem does not cover $3$-graphs with even $s$. There the limit
exists by Delcourt and Postle's theorem, which the paper cites, and
$\pi(3,2,2)=1/6$ is Rödl's packing value; the paper notes (p. 2) that with
Delcourt and Postle's theorem, Theorem 1.1 gives the existence of the limit
for all $r>t\ge2$ and $s\ge2$. Theorem 1.2 (p. 2): $\pi(3,2,s)>1/6$ for
every even $s\ge4$. With Theorems 2.3 and 2.4 this gives
$1/6<\pi(3,2,s)\le1/5$ (Section 5, p. 20), and Question 5.1 asks for the
value at even $s\ge8$.

The upper bounds are in Section 2. Theorem 2.3 (p. 5) deletes at most
$(s-1)^2\binom n{t-1}$ edges to destroy every small dense subgraph, which the
paper calls a block. Theorem 2.4 (p. 6), for every $s$, counts the $t$-sets
covered by edges and the crossing $t$-sets of diamonds (two edges meeting in $t$
vertices) through an auxiliary forest, and bounds the remaining edges by
$\frac{2}{2\binom rt-1}\binom nt$. Theorem 2.6 (p. 7), for even $s$ and $r\ge4$,
attaches two uncovered $t$-sets to each diamond and gives the bound
$\binom nt/\binom rt$. The lower bounds are in Section 3. For even $s$ a
high-girth partial Steiner system from the packing theorem of Delcourt and
Postle suffices (display (3), p. 11). For odd $s$, Proposition 3.7 (p. 13)
builds finite seeds whose packing ratio approaches $2/(2\binom rt-1)$, starting
from one diamond and applying a random alteration (Lemma 3.8) finitely often.
Lemma 3.4 (p. 12) then turns a seed into $n$-vertex hypergraphs. It is a
strengthened form of Theorem 3.1 of Glock, Joos, Kim, Kühn, Lichev and
Pikhurko, which the paper says is implicit in that theorem's proof (footnote 1,
p. 12). Theorem 1.2 (pp. 17–19) feeds Lemma 3.4 with a recursive seed grown
from the seven-edge configuration of that paper (Definition 3.19, Proposition
3.20). The paper's statement of AI use (p. 5) says that the lower bounds were
found without AI, that ChatGPT-5.6 served as a collaborative tool for the upper
bounds and the manuscript, and that the authors verified all arguments. At
$r=3$ the odd-$s$ value $1/5$ agrees with the refereed limits at $s=3$, $5$
and $7$ that [[problems/set_systems/E1076/_index|Problem 1076]] records.

**Covers.** The first-order asymptotics of $\mathrm{ex}_r(n,\mathcal F)$ on the
integer-exponent family $k=(r-t)s+t$ with $r>t\ge2$ and $s\ge2$, one vertex
below the range $k\ge(r-t)s+t+1$ of the Brown–Erdős–Sós conjecture, except
$3$-graphs with even $s$: there the value at $s=2$ is Rödl's, and for even
$s\ge4$ only $1/6<\pi(3,2,s)\le1/5$ is shown. The $3$-graph part, $k=s+2$, is
the case erdosproblems.com routes to Problem 1076. Not
covered: the exact values of $\mathrm{ex}_r(n,\mathcal F)$, every other triple
$(r,k,s)$, the conjecture itself, and the linear case $t=1$, which the paper
calls elementary and cites. The problem stays open.

**Depends on.** No page of this wiki. The lower bounds use two published or
posted results as black boxes: Theorem 3.1 of Glock, Joos, Kim, Kühn, Lichev
and Pikhurko, On the $(6,4)$-problem of Brown, Erdős, and Sós, Proc. Amer. Math.
Soc. Ser. B 11 (2024), 173–186, in the strengthened form above, and Theorem 1.3
of Delcourt and Postle, arXiv:2204.08981, on high-girth packings. The upper
bounds are self-contained.

**Standing.** Claimed: an arXiv preprint with no refereed version, Lean proof or
outside review known to this corpus. Read depth: the statements of Theorems
1.1, 1.2, 2.3, 2.4, 2.6 and 3.6 and of Lemma 3.4 were checked against the
problem's statement. The proof of Theorem 2.3 and the closing count of Theorem
2.4 were checked here; the acyclicity arguments of Theorems 2.4 and 2.6, the
random alteration of Lemmas 3.8 and 3.13 and the proof of Proposition 3.20 were
read through but not checked. Independently, Bodnár, Pikhurko, Sun, Wang and
Zeng (arXiv:2610.03323v1, 2 October 2026, Theorem 1.1) claim the single value
$\pi(3,2,9)=1/5$ by another construction; that agreement is not review. The
erdosproblems.com page for the problem was last edited on 24 January 2026,
before the result, and no proof claim on erdosproblems.com records it; Bloom's
catalog labeled the problem OPEN.
