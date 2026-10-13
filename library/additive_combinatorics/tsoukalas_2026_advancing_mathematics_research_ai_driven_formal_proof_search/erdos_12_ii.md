---
name: additive_combinatorics/tsoukalas_2026_advancing_mathematics_research_ai_driven_formal_proof_search/erdos_12_ii
title: "Erdős #12-(ii): for each epsilon, a set with property P and at least N^(1-epsilon) elements up to N"
desc: |
  For every epsilon > 0 there is an infinite set in which no element divides
  the sum of two distinct larger elements and which has at least
  N^(1-epsilon) elements up to N for all large N; built from Behrend spheres.
created: 2026-10-13T10:06:04Z
updated: 2026-10-13T10:06:04Z
---

***

**Source.** Appendix B.4, section "Erdős #12-(ii)", Theorem (ii) with its
proof, pp. 32--34 of arXiv:2605.22763v2, the edition named on
[[additive_combinatorics/tsoukalas_2026_advancing_mathematics_research_ai_driven_formal_proof_search/_index|the card]];
the published version in Science was not read. Table 1 (p. 7) lists it as
12 (ii).

## Statement

**Theorem (ii), as printed** (p. 32). There is an infinite set $A$ of
positive integers such that no three distinct elements $a,b,c\in A$ with
$b,c>a$ satisfy $a\mid b+c$, and such that for every $\varepsilon>0$

$$
\lvert A\cap\{1,\ldots,N\}\rvert\ge N^{1-\varepsilon}
$$

for all sufficiently large $N$. Consequently no absolute constant $c>0$ makes
every such set satisfy $|A\cap\{1,\ldots,N\}|<N^{1-c}$ for infinitely many
$N$.

**As proved** (pp. 32--34). For every $\varepsilon\in(0,1)$ there is an
infinite set $A$ with the same property and
$|A\cap\{1,\ldots,N\}|\ge N^{1-\varepsilon}$ for all sufficiently large $N$:
one set for each $\varepsilon$, not one set for every $\varepsilon$. The
construction fixes the exponent first (the proof calls it $c$) and chooses an
integer $m\ge2$ with $m>(2m+1)^{1-\varepsilon/2}$ (p. 33), so the printed
order of the quantifiers is stronger than the proof. The proved form is what
the theorem's "consequently" sentence needs and what the Lean target states. A
single set with at least $N^{1-\varepsilon}$ elements for every $\varepsilon$
does exist, by the sharpening recorded on the problem page, but this proof
does not supply it.

**Lean.** The paper links
[`erdos_12.parts.ii.lean`](https://github.com/google-deepmind/alphaproof-nexus-results/blob/42f344cfa9d57154f36e6b9bef1f71760a438c54/APNOutputs/ErdosProblems/erdos_12.parts.ii.lean)
(794 lines), cited at the repository commit of 2026-05-19. Its
`target_theorem_0` proves `answer(False)` for formal-conjectures'
`erdos_12.parts.ii`, that is, it refutes the existence of some $c>0$ such that
for every set `A` with `IsGood A` the set of $N$ with
$|A\cap[1,N]|<N^{1-c}$ is infinite. Read statically, not built.

**Read depth.** Claims checked: the statement and the parameter choices on
pp. 32--33 were read clause by clause on the page images. The proof was read
for its structure only; nothing here is independently reviewed.

## Proof pointer

The blocks are as in
[[additive_combinatorics/tsoukalas_2026_advancing_mathematics_research_ai_driven_formal_proof_search/erdos_12_i|Erdős #12-(i)]],
with a denser progression-free set. Fix $\varepsilon$ and $m$ as above, take
pairwise coprime $P_k\ge3$ with $P_k\le4^{k+2}$ (for instance the odd primes),
$L_k=\prod_{i\le k}P_i$ and $R_k<L_k$ with $R_k\equiv0\pmod{P_k}$ and
$R_k\equiv1\pmod{P_i}$ for $i<k$. In dimension $V_k-1$ with $V_k=(k+10)^4$, the
vectors with entries in $\{1,\ldots,m\}$ on a sphere holding at least
$m^{V_k-1}/(V_km^2+1)$ of them, read in base $2m+1$ and shifted by the leading
digit $m(2m+1)^{V_k-1}$, form a set $S_k$ with no three-term progression inside
$[m(2m+1)^{V_k-1},(m+1)(2m+1)^{V_k-1})$. The blocks are
$A_k=\{L_kx+R_k:x\in S_k\}$. Across blocks the congruences exclude
$a\mid b+c$; inside a block $b+c<3a$ forces $b+c=2a$, which $S_k$ excludes. The
count up to the start of each block is compared through the exponents
$(1-\varepsilon/2)k^4$ and $(1-\varepsilon)k^4$ of $2m+1$ (pp. 33--34).

The paper adds that the answer to (ii) implies the answer to (i), that both
proofs are included because the agent found them separately, and that the
third question, whether $\sum_{a\in A}1/a$ can diverge, is open (p. 34).

## Dependencies

Behrend's construction of sets without three-term progressions and the Chinese
remainder theorem; no other source.

## Bears on

- [[../wiki/problems/integer_sequences/E0012/_index|Problem 12]]: the second
  question asks whether some absolute $c>0$ makes every such set thinner than
  $N^{1-c}$ infinitely often; the theorem answers it no, and with it the first
  question yes. The result is recorded on the claim page
  [[../wiki/problems/integer_sequences/E0012/claims/2026_04_03_deepmind|Google DeepMind 2026]].
