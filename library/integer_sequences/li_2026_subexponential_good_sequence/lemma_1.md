---
name: integer_sequences/li_2026_subexponential_good_sequence/lemma_1
title: "Lemma 1 (p. 3): certificate exclusion for the random sequence of primes"
desc: |
  For the manuscript's random sequence of primes and fixed C ≥ 1 and η > 0,
  almost surely, for all large t, no integer 0 ≤ n < N_t has ⌈(1+η)t⌉ distinct
  terms of index above K_0(C,η) dividing translates n + j with 1 ≤ j ≤ Ct;
  statement checked, proof unreviewed.
created: 2026-10-14T22:08:31Z
updated: 2026-10-14T22:08:31Z
---

***

## Statement

**Setting (pp. 2--3).** The lemma concerns the random sequence of Section 2.
For large $n$, $\mathcal P_n$ is the set of primes in
$I_n=[e^{\sqrt n},e^{\sqrt n+1/(10\sqrt n)}]$. The integer $n_0$ is so large
that the intervals $I_n$, $n\ge n_0$, are disjoint, that
$|\mathcal P_n|\gg e^{\sqrt n}/n$ for $n\ge n_0$ (the paper's (1)), and that
at least $n_0-1$ primes lie below $e^{\sqrt{n_0}}$. The terms
$u_1<\cdots<u_{n_0-1}$ are fixed primes below $e^{\sqrt{n_0}}$, and for each
$n\ge n_0$ the term $u_n$ is drawn uniformly from $\mathcal P_n$,
independently of the others. With the constant $B$ of the paper's (4), put

$$
N_t=\exp\Bigl(\frac23(t+1)^{3/2}+B\sqrt t\Bigr),
$$

which bounds $u_1\cdots u_{t+1}$ for every outcome and all large $t$.

**Lemma 1** (Certificate exclusion, p. 3). Fix $C\ge1$ and $\eta>0$, and for
each $t$ write $M=\lceil(1+\eta)t\rceil$. There is an integer
$K_0=K_0(C,\eta)$ such that, with probability one, for every sufficiently
large $t$ no integer $n$ with $0\le n<N_t$ admits distinct indices
$i_1,\dots,i_M>K_0$ and positions $j_1,\dots,j_M$ with $1\le j_r\le Ct$ and

$$
u_{i_r}\mid n+j_r\qquad(1\le r\le M).
$$

The integer $K_0$ comes before the almost-sure quantifier and does not depend
on the outcome; the threshold beyond which $t$ counts as large may. The
indices must be distinct and the positions need not be. The proof calls such
a configuration a certificate at level $t$ (p. 5).

**Source.** Peter Li, *A Subexponential Good Sequence*, manuscript dated
April 27, 2026, 7 pp.; the construction on pp. 2--3, Lemma 1 on p. 3 and its
proof on pp. 3--5. The edition read is identified on the
[[integer_sequences/li_2026_subexponential_good_sequence/_index|source card]].

**Read depth.** Claims checked: the statement and the construction it
concerns were read clause by clause on the page images of pp. 2--3. The proof
was read through for structure only; no step of it was checked.

## Proof sketch

The steps as the manuscript presents them (pp. 3--5); none was checked here.
Fix $\beta<1$ with $\beta(1+\eta)^{3/2}>1$, the paper's (5). For $N=n+j$
with $n<N_t$ and $1\le j\le Ct$ one has $\log N\ll t^{3/2}$, and the primes
of $I_i$ are at least $e^{\sqrt i}$, so at most $\log N/\sqrt i$ of them
divide $N$. With (1) this gives
$\mathbb P(u_i\mid N)\ll t^{3/2}\sqrt i\,e^{-\sqrt i}$ (7), and with
$K_0\ge n_0$ large in terms of $\beta$ it gives
$\mathbb P(u_i\mid N)\le\min\{1,t^2e^{-\beta\sqrt i}\}$ whenever $i>K_0$ and
$t$ is large ((8), (9)). Terms with distinct indices are independent, so a
fixed certificate has probability at most the product of these bounds. The
sum $S_M(t)$ of these products over increasing index tuples is at most the
coefficient of $w^M$ in $\prod_{i\ge1}(1+wt^2e^{-\beta\sqrt i})$, hence at
most $z^{-M}$ times that product for any $z>0$. Taking $z=e^\alpha/t^2$, an
integral comparison makes the logarithm of the product
$\alpha^3/(3\beta^2)+O_\beta(\alpha^2)$ (10), and $\alpha=\beta\sqrt M$ gives
$S_M(t)\le\exp(-\frac{2\beta}3M^{3/2}+o(t^{3/2}))$ (11). With at most
$N_t+1$ choices of $n$ and $(Ct)^M$ of positions, the expected number $X_t$
of certificates at level $t$ is at most
$\exp\bigl((\frac23-\frac{2\beta}3(1+\eta)^{3/2})t^{3/2}+o(t^{3/2})\bigr)$,
which by (5) is at most $e^{-ct^{3/2}}$ for some $c=c(C,\eta)>0$ and all
large $t$. Hence $\sum_t\mathbb P(X_t>0)<\infty$, and the Borel--Cantelli
lemma gives $X_t=0$ for all large $t$ almost surely.

## Dependencies

The construction of Section 2 with its displays (1) and (4) (pp. 2--3),
which rest on the prime number theorem with the de la Vallée Poussin error
term; the Borel--Cantelli lemma (p. 5).

## Bears on

- [[../wiki/problems/integer_sequences/E1101/_index|Problem 1101]]: the
  lemma is the probabilistic input of
  [[integer_sequences/li_2026_subexponential_good_sequence/theorem_1|Theorem 1]].
  Section 4 turns a gap of length at least $(1+\varepsilon)t_xD^{-1}$ into a
  certificate, so an outcome satisfying the lemma for every integer $C\ge1$
  and rational $\eta>0$ is good. On its own the lemma does not answer the
  problem.
