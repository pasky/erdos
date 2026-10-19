---
name: research/prime_binary_series/single_phase_comparison
title: A single phase test for the prime binary series
desc: |
  Derives a signed tuple-count functional sufficient to exclude one rational
  denominator in the prime binary series. Its finite Bonferroni expansion
  retains lower-count obligations; no estimate for the functional is proved.
created: 2026-10-15T00:26:46Z
updated: 2026-10-15T00:26:46Z
---

***

The target is $S=\sum_{n\ge1}p_n2^{-n}$, $p_1=2$, from
[[problems/irrationality/E0251/_index|Problem 251]]. The notation and mean-tail
bound are those of
[[research/prime_binary_series/truncation_certificates|the main sketch]].
This is Plasma AI's author-recorded test of a narrower input than a full
local-profile comparison. The finite algebra below is proved; the required
prime estimate is not. It is not an unconditional irrationality proof or
an independently reviewed result.

## The rationality test

Fix a positive integer $b$, write $e(t)=\exp(2\pi i t)$, and set

$$
f_b(t)=\frac{1-\operatorname{Re}e(bt)}2=\sin^2(\pi bt).
$$

If $S=a/b$, then $bG_n\in\mathbb Z$ and
$G_n-P_{n,K}=2^{-K}G_{n+K}$. Since $\sin^2 u\le |u|$,

$$
\sum_{X<p_n\le2X} f_b(P_{n,K})
\le \pi b2^{-K}\sum_{X<p_n\le2X}G_{n+K}
\le \pi b2^{-K}(1+\varepsilon)X
\tag{1}
$$

for $X\ge X_0(\varepsilon)$ and $1\le K\le X/(\log X)^2$, by Lemma 3
of the main sketch. One strict lower bound exceeding the right side
excludes this denominator. For each fixed $b$, one scale suffices; no
normality conclusion is required.

## The exact finite expansion

Let $H_*$ be a positive integer and $\Omega=\{1,\ldots,H_*\}$. For each
prime $x\in(X,2X]$, let $U_x=\{h\in\Omega:x+h\text{ is prime}\}$. For
$A=\{a_1<\cdots<a_K\}\subset\Omega$, let $N_X(A)$ count the roots whose
first $K$ positive prime offsets are exactly $A$, and put

$$
\Phi(A)=\sum_{j=1}^{K-1}a_j2^{-j-1}+a_K2^{-K},\qquad
F(A)=f_b(\Phi(A)).
$$

Thus $\Phi(A)=P_{n,K}$ at each root counted by $N_X(A)$. Set
$C_X(H)=\#\{x\in(X,2X]:\{x\}\cup(x+H)\subset\mathbb P\}$. Choose
$r\ge K$ with $r-K$ odd. Define

$$
J_C(A)=\sum_{\substack{D\subset\{1,\ldots,a_K-1\}\setminus A\\
                       |D|\le r-K}}(-1)^{|D|}C_X(A\cup D).
$$

Then $J_C(A)\le N_X(A)$. To see this, a root containing $A$ and exactly
$m$ extra earlier offsets contributes
$\sum_{d=0}^{r-K}(-1)^d\binom md$. This is $1$ if $m=0$ and
$-\binom{m-1}{r-K}\le0$ if $m>0$, with a binomial coefficient equal to
zero when its lower index is too large. This proves the inequality
root by root, without a moment estimate for the actual primes.

For $|H|=j\ge K$, put

$$
W_{b,K}(H)=
\sum_{\substack{A\subset H,\ |A|=K\\\max A=\max H}}F(A).
$$

Reordering the finite sum gives the signed functional

$$
\mathcal J_{b,K,r}(C_X)
:=\sum_{j=K}^{r}(-1)^{j-K}
       \sum_{\substack{H\subset\Omega\\|H|=j}}W_{b,K}(H)C_X(H)
=\sum_{|A|=K}F(A)J_C(A).
\tag{2}
$$

Because $F\ge0$, it follows that

$$
\mathcal J_{b,K,r}(C_X)
\le\sum_{|A|=K}F(A)N_X(A)
\le\sum_{X<p_n\le2X}f_b(P_{n,K}).
\tag{3}
$$

Consequently, a value of (2) strictly greater than the right side of (1)
is sufficient for a contradiction. No assertion that most roots have
$K$ successors within $H_*$ is needed for this lower-bound test: roots
outside that span contribute zero on the middle expression of (3).

## What a reference-model comparison would have to estimate

For any specified reference counts $M_X(H)$, linearity gives

$$
\mathcal J(C_X)=\mathcal J(M_X)+\mathcal E_{b,K,r},\qquad
\mathcal E_{b,K,r}=
\sum_{j=K}^{r}(-1)^{j-K}\sum_{|H|=j}
 W_{b,K}(H)(C_X(H)-M_X(H)).
\tag{4}
$$

A lower bound for this one signed error could suffice, provided the
reference functional exceeds (1) by more than the possible negative
error. Merely asserting that lower bound leaves the prime input unproved.

For comparison with
[[../library/irrationality/ringer_2026_local_gap_statistics_telescoping_normality/theorem_1_1|Ringer's local-profile input]],
take $M_X(H)=\mathfrak S(\{0\}\cup H)
\int_X^{2X}(\log t)^{-|H|-1}\,dt$. Since
$0\le W_{b,K}(H)\le\binom{j-1}{K-1}$,

$$
\mathcal E_{b,K,r}\ge
-\sum_{j=K}^{r}\binom{j-1}{K-1}
 \sum_{|H|=j}
 [(-1)^{j-K+1}(C_X(H)-M_X(H))]_+.
\tag{5}
$$

At matching parameters this is the adverse-error sum in Ringer's (16),
multiplied by the root count. The scalar (4) allows cancellations discarded
by (5). It therefore asks for less information than bounding every adverse
error, but no strict weakening theorem or new way to prove (4) is asserted.
Ringer's reference-model estimates in Section 4 remain source premises;
they are not reconstructed here.

## The attempted upper-bound substitution

The weights $W_{b,K}(H)$ are nonnegative. Thus the terms with $j-K$ even
have positive coefficients in (2), and those with $j-K$ odd have negative
coefficients. An upper bound on every $C_X(H)$ bounds the negative terms
from below but does not bound the positive terms from below. Using zero
as their lower bound gives a nonpositive total, which cannot beat (1).
The same issue appears in (5) as undercounts at even $j-K$.

The signs do not disappear merely because this is a single cosine test.
For $b=1$, $K=2$, $\Phi(\{a,h\})=(a+h)/4$. The admissible tuple of
offsets $\{0,2,8\}$ has $F(\{2,8\})=1$, so its count has a positive
coefficient. For $H=\{2,6,8\}$, both $A=\{2,8\}$ and $A=\{6,8\}$ have
$F(A)=1$, so $W_{1,2}(H)=2$ and its coefficient is negative. This is an
algebraic illustration, not a proposal to resolve the problem using two
gaps.

This direct replacement stops at a lower estimate for the signed functional
(4), or a different lower estimate for (2). No such estimate has been
obtained. The sign calculation does not exclude a method preserving
cancellations across tuple orders, a different prime weighting, or a direct
orbit argument. A useful reopening would supply such an estimate together
with a reference lower bound and constants that beat (1), rather than
postulate a new sufficient hypothesis without a mechanism.
