---
name: problems/ramsey_theory/E1105/claims/2005_09_01_montellano_ballesteros_neumann_lara
title: Montellano-Ballesteros and Neumann-Lara, the exact anti-Ramsey number of cycles
desc: |
  Theorem 5 of Montellano-Ballesteros and Neumann-Lara (Graphs Combin. 2005):
  for all $n\ge p\ge3$ the least number of colors forcing a rainbow $p$-cycle in
  $K_n$ is the value $\mathbf E(n,p)$ conjectured in 1975. So
  $\mathrm{AR}(n,C_k)=\mathbf E(n,k)-1$, which settles the cycle half.
authors:
- J.J. Montellano-Ballesteros
- V. Neumann-Lara
status: accepted
claim: proved
scope: partial
settles: [cycles]
evidence:
- reviewed
- refereed
submitted: null
links:
- url: https://doi.org/10.1007/s00373-005-0619-y
  kind: paper
- url: https://www.erdosproblems.com/1105
  kind: discussion
- url: https://github.com/plby/lean-proofs/blob/8822f7ddef30fadbd92e1c6ab4ed897af356af5e/src/latest/ErdosProblems/Erdos1105.lean
  kind: formalization
  date: 2026-08-23
- url: https://github.com/linrock/math-proofs/tree/ba96303b34a95ac458958c1eb0bbdee54733484a/erdos-1105
  kind: formalization
  date: 2026-10-06
created: 2026-10-07T05:35:15Z
updated: 2026-10-08T01:29:59Z
---

***

**Claim.**
[[../library/ramsey_theory/montellano_ballesteros_neumann_lara_2005_anti_ramsey_theorem_cycles/theorem_5|Theorem 5]]
of Montellano-Ballesteros and Neumann-Lara (Graphs Combin. 21 (2005),
p. 352) states that for all integers $n\ge p\ge3$, $h(n,p)=\mathbf E(n,p)$,
where $h(n,p)$ is the least number of colors such that every edge-coloring
of $K_n$ with exactly that many colors has a rainbow (the paper's
"heterochromatic") cycle of length $p$, and

$$
\mathbf E(n,p)=\binom{p-1}{2}\Bigl\lfloor\frac{n}{p-1}\Bigr\rfloor
+\binom{r}{2}+\Bigl\lceil\frac{n}{p-1}\Bigr\rceil,
$$

with $r$ the residue of $n$ modulo $p-1$. Since $\mathrm{AR}(n,C_k)$ is the
largest number of colors with no rainbow $C_k$,
$\mathrm{AR}(n,C_k)=h(n,k)-1=\mathbf E(n,k)-1$ for all $n\ge k\ge3$.
Writing $n=q(k-1)+r$, $\mathbf E(n,k)$ differs from
$(\frac{k-2}2+\frac1{k-1})n$ by a quantity bounded in terms of $k$, so

$$
\mathrm{AR}(n,C_k)=\Bigl(\frac{k-2}{2}+\frac{1}{k-1}\Bigr)n+O(1)
$$

for every fixed $k\ge3$: the paper's Corollary 1 (p. 353) and the cycle
question of [[problems/ramsey_theory/E1105/_index|Problem 1105]], answered
yes. The lower bound $h(n,p)\ge\mathbf E(n,p)$ and the case $p=3$ are the
1975 results of Erdős, Simonovits and Sós, whose Conjecture 1 the theorem
proves; the paper proves the upper bound through its Proposition 1 (the
range $4\le p\le n\le2p-3$) and the structure of its selective graphs.

**Covers.** The cycle half: the asymptotic formula for $\mathrm{AR}(n,C_k)$
for every $k\ge3$, with the exact value behind it. The path half, the exact
formula for $\mathrm{AR}(n,P_k)$ for $n\ge k\ge5$, is the subject of
[[problems/ramsey_theory/E1105/claims/2021_02_01_yuan|Yuan 2021]]
(accepted on the curator's credit, all $n\ge k\ge5$) and
[[problems/ramsey_theory/E1105/claims/1984_03_01_simonovits_sos|Simonovits and Sós 1984]]
(accepted, long paths for large $n$).

**Depends on.** Nothing in this wiki; the result rests on the cited paper
and the 1975 lower bound it takes over.

**Acceptance.** Reviewed: the erdosproblems.com curator, T. F. Bloom, labeled
the problem PROVED. In the commentary (accessed 2026-09-18), the curator credits
the paper with the exact formula for $\mathrm{AR}(n,C_k)$ and the asymptotic it
implies. The curator is independent of the authors. Refereed: Graphs and
Combinatorics 21 (2005), no. 3, 343--354, received April 2003, final version 26
March 2005. Its Crossref record dates the issue September 2005 without a day, so
the page's day is a placeholder. On 2026-09-18 the paper's citation record
showed no dispute: 98 citing works per OpenAlex, and 27 Semantic Scholar records
read by title. The printed Corollary 1 has a minus sign between $\frac{p-2}2$
and $\frac1{p-1}$, where the abstract, the introduction and the formula have the
plus sign. The result page records this misprint.

**Formalization.** Two outside Lean developments, linked above, prove the
cycle half's asymptotic for every $k\ge3$; neither proves Theorem 5's exact
value for every $n$ beyond $k=3$. Linmiao Xu's development, registered in the
Palomar registry as PALOMAR-2026-10-13-000006 on 13 October 2026 and pinned at
its registered commit of 11 October 2026, proves the formal-conjectures
declaration `erdos_1105.parts.i`, the triangle value
$\mathrm{AR}(n,C_3)=n-1$, and, for all $n\ge k\ge3$,
$\lfloor\frac n{k-1}\rfloor(\binom{k-1}2+1)-1\le\mathrm{AR}(n,C_k)\le
(\frac{k-2}2+\frac1{k-1})n-1$. When $k-1$ divides $n$ both bounds equal
$\frac n{k-1}(\binom{k-1}2+1)-1=\mathbf E(n,k)-1$, so in that case it proves
Theorem 5's exact value. Its record names this paper and Chapter 3 of
Jongook Choi's 2011 Iowa State dissertation as adapted sources, and its upper
bound follows Choi's argument through private colors and weak anticyclic
block decompositions. The registry ran the proof through two kernels and
records a model review by GPT-6 Sol through Codex with a neutral outcome,
which is not an independent review. `Erdos1105.lean` of Boris Alexeev's
repository plby/lean-proofs, a file whose proofs were posted on 23 August 2026,
pinned at the commit of 15 September 2026, proves the same asymptotic through
a private-color linear upper bound, over its own definition of
$\mathrm{AR}(n,G)$; the repository's source list credits the informal
argument to GPT-5.6 Sol and the formal proof to Codex and GPT-5.6 Sol, and
its notes cite no published source for the cycle argument. Both prove the
cycle half that this page settles, so they are links here and not claims of
their own. This corpus has not built either or audited its statement, so no
`formalized` evidence is listed.

**Read depth.** The definitions, Theorem 5 and Corollary 1 are checked
clause by clause; the proof (pp. 351--353 with the lemmas of Sections 2--3)
is followed for structure only and not checked. Nothing here is independent
review.
