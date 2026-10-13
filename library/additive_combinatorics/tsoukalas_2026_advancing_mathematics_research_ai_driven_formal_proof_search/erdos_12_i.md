---
name: additive_combinatorics/tsoukalas_2026_advancing_mathematics_research_ai_driven_formal_proof_search/erdos_12_i
title: "Erdős #12-(i): a set with property P whose counting function is at least a constant times the square root of N"
desc: |
  An infinite set in which no element divides the sum of two distinct larger
  elements, whose count up to N over N^(1/2) has positive liminf; built from
  progression-free blocks placed by the Chinese remainder theorem.
created: 2026-10-13T10:06:04Z
updated: 2026-10-13T10:06:04Z
---

***

**Source.** Appendix B.4, section "Erdős #12-(i)", Theorem (i) with its proof,
pp. 31--32 of arXiv:2605.22763v2, the edition named on
[[additive_combinatorics/tsoukalas_2026_advancing_mathematics_research_ai_driven_formal_proof_search/_index|the card]];
the published version in Science was not read. Table 1 (p. 7) lists it as
12 (i).

## Statement

**Theorem (i)** (p. 31). There is an infinite set $A\subseteq\mathbb N$ such
that no three distinct elements $a,b,c\in A$ with $a<b$ and $a<c$ satisfy
$a\mid b+c$, and

$$
\liminf_{N\to\infty}\frac{\lvert A\cap\{1,\ldots,N\}\rvert}{N^{1/2}}>0.
$$

The proof gives the constant $1/\sqrt2$ for the liminf (p. 32).

**Discrepancy.** Table 1 (p. 7) summarizes this result as
$|A\cap[1,N]|/\sqrt N>\delta>0$ "infinitely often". The theorem's liminf
bound holds for all large $N$, which is stronger.

**Lean.** The paper links
[`erdos_12.parts.i.lean`](https://github.com/google-deepmind/alphaproof-nexus-results/blob/42f344cfa9d57154f36e6b9bef1f71760a438c54/APNOutputs/ErdosProblems/erdos_12.parts.i.lean)
(1,237 lines), cited at the repository commit of 2026-05-19. Its
`target_theorem_0` proves `answer(True)` for formal-conjectures'
`erdos_12.parts.i`: some set `A` with `IsGood A` has
`0 < liminf (|A ∩ [1,N]| / √N)`, where `IsGood A` says that `A` is infinite and
that `a ∣ b + c`, `a < b` and `a < c` force `b = c`. The file's set is cut out
by congruences ($n\equiv1$ modulo $K_m$, $n\equiv0$ modulo a prime $q_m$) on
intervals $[M_m,2M_m]$ and uses no progression-free set, so it is not the
construction the prose below describes; the two were not compared further. Read
statically, not built.

**Read depth.** Claims checked: the statement was read clause by clause on the
page image of p. 31. The proof was read for its structure only; nothing here
is independently reviewed.

## Proof pointer

Let $f(n)$ be the number whose base-3 digits are the base-2 digits of $n$; its
values have only the digits $0$ and $1$ in base 3, so they contain no
three-term arithmetic progression. With $F_i$ the $i$-th odd prime,
$M_i=\prod_{j<i}F_j$ and $V_i=F_iM_i$, the Chinese remainder theorem gives
$C_i<V_i$ with $C_i\equiv0\pmod{F_i}$ and $C_i\equiv1\pmod{M_i}$. The block
$B_i=\{P_i+V_if(y):y<X_i\}$, with $P_i=10V_iY_i+C_i$, $Y_i=3^{(i+20)^3}$ and
$X_i=\lfloor\sqrt{P_{i+1}}\rfloor$, lies in $[P_i,1.1P_i]$, and $A$ is the
union of the blocks. If $a\in B_i$ divides $b+c$ with $b$ in a later block,
then $b+c$ is $1$ or $2$ modulo $F_i$ while $a$ is $0$, a contradiction; inside
one block $a\mid b+c$ forces $b+c=2a$, which the progression-free values of
$f$ exclude. Counting the block before $N$ gives the liminf (pp. 31--32).

## Dependencies

The Chinese remainder theorem and Bertrand's postulate; no other source.

## Bears on

- [[../wiki/problems/integer_sequences/E0012/_index|Problem 12]]: the first
  question asks for a set with this property and positive liminf of
  $|A\cap\{1,\ldots,N\}|/N^{1/2}$; the theorem answers it yes. The paper notes
  that the answer to the second question implies this one (p. 34). The result
  is recorded on the claim page
  [[../wiki/problems/integer_sequences/E0012/claims/2026_04_03_deepmind|Google DeepMind 2026]].
