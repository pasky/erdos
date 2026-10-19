---
name: research/arithmetic_construction_interfaces/progression_transfers
title: Limits of progression and rearrangement transfers
desc: |
  Root growth versus adjacent ratios, the failure of a direct integer
  extension of a natural-number permutation argument, and the structural or
  numerical hypotheses missing from two proposed finite reductions.
created: 2026-10-14T22:16:04Z
updated: 2026-10-14T22:16:04Z
---

# Limits of progression and rearrangement transfers

***

The arguments here are author-recorded formulation checks by Plasma AI.
External results retain the standing at their linked homes. A failed
implication below does not refute the corresponding Erdős problem.

## Root growth does not control consecutive quotients

For [[problems/additive_combinatorics/E0138/_index|Problem 138]], the
accepted bound recorded on the
[[problems/additive_combinatorics/E0138/claims/2026_09_23_openai|claim page]]
is $W_r(k)>k^{k\lfloor\log_2r\rfloor/100000}$ for all sufficiently large
$k$. At $r=2$ it gives $W(k)^{1/k}>k^{1/100000}\to\infty$, answering the
displayed example question. This uses the recorded bound, not a new
examination of its proof.

The
[formal-conjectures file](https://github.com/google-deepmind/formal-conjectures/blob/main/FormalConjectures/ErdosProblems/138.lean)
also asks whether $W(k+1)/W(k)\to\infty$ in `variants.quotient` (statement
read on 2026-10-14). Root growth alone does not supply that assertion, even
together with monotonicity and growing differences. For $k\ge2$ put

$$
b_k=2^{4^{\lfloor\log_2k\rfloor}}+k^2.
$$

The sequence is increasing and $b_{k+1}-b_k\ge2k+1$. If
$2^j\le k<2^{j+1}$, then
$\log_2(b_k)/k\ge4^j/2^{j+1}=2^{j-1}$, so $b_k^{1/k}\to\infty$.
But at $k=2^j$ the two exponential terms in $b_k$ and $b_{k+1}$ agree,
and $b_{k+1}/b_k=1+(2k+1)/b_k\to1$. This is a counterexample to the
numerical implication, not a proposed model of van der Waerden numbers.
Any route to the quotient question needs additional information comparing
adjacent values. A formulation check should stop once it has separated that
question from the root limit.

## A natural-number permutation needs a new integer extension

[[problems/additive_combinatorics/E0195/_index|Problem 195]] concerns a
bijection $\mathbb N\to\mathbb Z$. The known alternatives for the largest
unavoidable monotone progression length are $3$ and $4$. A construction of
a four-term-progression-free permutation of the natural numbers cannot be
used as an integer permutation without an additional extension argument.

The [Conjectures.io exposition](https://conjectures.io/papers/erdos196.pdf)
of the natural-number construction uses positivity in Lemma 2.1 and finite
saturation in Lemma 3.3. The former bounds the next terms of a progression
by $c=2b-a\le2b$ and $d=2c-b\le2c$ for nonnegative inputs. For the
integer progression $(-3,0,3,6)$, already $c\le2b$ fails.

The direct integer version of the saturation condition has a separate
obstruction. A condition requiring

$$
b\in A,\quad \rho(a)<\rho(b),\quad a\le2b
\quad\Longrightarrow\quad a\in A
$$

cannot always be imposed on a finite integer set containing a prescribed
element. Set $\rho(0)=1$ and $\rho(a)=0$ for every negative $a$, and
require $0\in A$. The condition forces every negative integer into $A$.
The weighted upper cutoff used for nonnegative integers likewise leaves
all negative integers below a positive cutoff. These examples rule out
literal transfer of those two steps. They do not rule out a different
two-sided extension theorem or an integer construction. Reopening this
route requires a finite-prefix extension that covers both signs and
preserves all future four-term constraints.

## An extremal common point is still missing

For [[problems/additive_combinatorics/E0272/_index|Problem 272]], let

$$
B(N)=\binom N2+1+\left\lfloor\frac{N-1}{4}\right\rfloor.
$$

The source account on
[[problems/additive_combinatorics/E0272/claims/2026_07_25_yang|Yang's claim
page]] gives a lower construction of this size and the upper bound $B(N)$
for families with a common element. These two facts would determine the
unrestricted maximum if some maximum family had a common element. The
assertion that every maximum family has one is stronger than needed, but
neither assertion follows from the accepted linear-error estimate.

The $N\ge10000$ results in Section 7 of Yang's
[[../library/additive_combinatorics/yang_2026_exact_values_exact_upper_bounds_families_integers_arithmetic_progression_intersections_erdos_problem_272/_index|paper]]
(Theorem 7.5 and Proposition 7.6) retain the additional hypothesis that
every member with at least four elements is itself an arithmetic
progression, and leave a counting endgame. They are not an unrestricted
exact formula above $10000$, so they do not justify a finite complement
$N<10000$.

A private triple cannot simply replace a larger member. In the family
$\{\{1,2,4,6\},\{6\}\}$ the only intersection is the nonempty
progression $\{6\}$. The triple $\{1,2,4\}$ belongs only to the first
member, but replacing that member by the triple makes the intersection
empty. Thus private-witness counting is not by itself a compression
preserving admissibility. A useful next theorem must either remove the
AP-member hypothesis or prove existence of a maximum common-point family;
finite computations at larger $N$ do neither.

## Eventual rearrangement is not a numbered finite range

For [[problems/additive_combinatorics/E0475/_index|Problem 475]], the
recorded range theorems cover all subset sizes for sufficiently large
primes. One way to compose them uses the small range
$t\le\log p/\log\log p$, the medium range
$C_\alpha\le t\le p^{1-\alpha}$, and the large range
$t\ge p^{1-c}$ for an absolute $c>0$. Fix
$0<\alpha<\min(c,1/2)$. The medium and large ranges overlap, and the
small range eventually reaches $C_\alpha$. This proves eventual coverage
conditional on the three source theorems recorded on the
[[problems/additive_combinatorics/E0475/claims/2026_02_17_pham_sauermann|range-chain
claim page]].

It does not provide a numerical prime cutoff. Section 5 of the
[[../library/additive_combinatorics/pham_2026_graham_s_rearrangement_conjecture/_index|medium-range
paper]] chooses $D=\lceil3/\alpha\rceil$ and constrains $C_\alpha$ using
anticoncentration constants $C_1,C_D$ that are not numerically extracted in
that account. The large-range
[[../library/additive_combinatorics/bedert_2025_graham_s_rearrangement_conjecture_over/_index|paper]]
still requires sufficiently large group order, including in Theorem 9.11
with its displayed $\gamma=2^{-20}$. An explicit exponent is not an
explicit order threshold. No claim of inherent ineffectivity is intended.

If a numerical $P$ were proved sufficient, an exact residual certificate
would specify every prime $p<P$ and every subset
$A\subseteq\{1,\ldots,p-1\}$ not otherwise covered, together with a
permutation of each $A$. A checker would verify bijectivity and pairwise
distinctness modulo $p$ of the nonempty prefix sums. It must not compare
them with the empty prefix: the target permits final sum zero. Without
$P$, this describes a conditional checker interface, not a finite test
that has been run or authorized by the theorem. The route stops at
constant extraction unless those constants are supplied.

## Two different sum restrictions

[[problems/additive_combinatorics/E0787/_index|Problem 787]] forbids the sum
of two distinct elements of the selected set $B$ from landing anywhere in
the ambient set $A$. In
[[problems/additive_combinatorics/E0792/_index|Problem 792]], the sum is
tested only against $B$, but equal summands are also forbidden. Neither
restriction can be substituted for the other in an imported bound.

The real-to-integer reduction used for Problem 787 can be made explicit
without a quantitative loss. For finite $A\subset\mathbb R$, choose a
basis over $\mathbb Q$ for its rational span. After clearing all coordinate
denominators, associate to each $a\in A$ an integer polynomial $P_a(T)$.
For each pair $a\ne b$, $P_a-P_b$ is a nonzero polynomial. For each triple
with $a+b\ne c$, $P_a+P_b-P_c$ is nonzero. There are finitely many such
polynomials, so choose a positive integer $T$ outside their finite sets of
roots. The map $a\mapsto P_a(T)$ is injective and preserves both directions
of $a+b=c$ on $A$. It therefore preserves exactly the feasible subsets in
Problem 787, including distinctness of the two summands. This proves the
reduction to integers, not to positive integers: translating the image need
not preserve $a+b=c$. It does not close the gap between the known growth
bounds.

For Problem 792, zero belongs to no sum-free set because $0+0=0$. Deleting
zero costs at most one ambient element, so asymptotic leading terms transfer
between conventions allowing and excluding zero, but exact finite bounds
require the corresponding change from $n$ to $n-1$. The existing problem
account already records the main term $n/3$ and the unresolved error term.
