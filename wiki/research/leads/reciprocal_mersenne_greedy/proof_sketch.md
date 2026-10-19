---
name: research/leads/reciprocal_mersenne_greedy/proof_sketch
title: Greedy Expansions of Rationals as Reciprocal Mersenne Subseries
desc: |
  A negative answer to Problem 257 would follow from one rational's
  all-future greedy survival, or half seeds for unbounded initial multiplier
  segments. This sketch gives exact residual and carry criteria, finite
  certificates, and the seed's doubling extension. Mixed carries restrict
  half-target two-cycles but do not yet exclude them or construct a repair.
  The uniform seed and all-future survival obligations remain open.
tags: []
sources: []
problems:
- 257
created: 2026-10-16T14:05:38Z
updated: 2026-10-16T14:05:38Z
---

# Greedy Expansions of Rationals as Reciprocal Mersenne Subseries

***

The results on this page that are not drawn from a cited source are Plasma
AI's, credited to Plasma AI. They are author-recorded and have had no
independent review.

## Target and standing

[[problems/irrationality/E0257/_index|Problem 257]] asks whether
$\sum_{n\in A}\frac{1}{2^n-1}$ is irrational for every infinite set
$A\subseteq\mathbb N$. This sketch aims at the negative answer: a rational $q$
and an infinite $A$ with

$$
\sum_{n\in A}\frac{1}{2^n-1}=q ,
$$

with the base exactly $2$ and every denominator exactly $2^n-1$. Sums with
shifted denominators or several bases are a different question (see "What
composes" below). The two speculations Kovač and Tao quote
(arXiv:2406.17593v4, section 2.1.2) point opposite ways: Erdős wrote on p. 222
of his 1968 paper in *Math. Student* that a rational value for some base
"seems likely", while Erdős and Graham later suggested that the base-$2$ sums
are perhaps always irrational, the form recorded as Problem 257.

Lemmas 1–8, 10, 12 and 13 below have elementary author-recorded proofs.
Lemmas 9 and 14 import the classical Bang–Zsigmondy primitive-divisor
theorem; their deductions are given here, but the external theorem is not
re-proved. The construction
linked in Lemma 11 uses Bertrand's postulate and applies only to weights
with at most four geometric multipliers. Lemma 12 generates candidate digits
from already fixed digits by one explicit rule; it follows the greedy
expansion until the orbit comes close to $\frac12$. Its never-failure
condition is sufficient for Step 4 and is unproved. Lemma 13 replaces a
fixed finite multiplier problem by one finite integer seed equation and an
explicit extension. Seeds for unbounded initial segments would prove Step 4;
that family is also unproved. The route is blocked at Step 4 of "The route":
no rational with infinite support is proved to be such a sum, and nothing
here proves any sum irrational. The computations
are finite and certify only what they state. Throughout,
$\mathbb N=\{1,2,\ldots\}$.

## Notation

For $n\ge1$ let $w_n=\frac1{2^n-1}$, and for $n\ge0$ let
$T_n=\sum_{k>n}w_k$; $E=T_0=1.60669515\ldots$ is the Erdős–Borwein constant.
The achievement set is
$\Sigma=\{\sum_{n\in A}w_n:A\subseteq\mathbb N\}\subseteq[0,E]$. Put
$g_n=w_n-T_n$ and $\sigma_n=2^nT_n$. For $F\subseteq\{1,\ldots,n\}$ let
$S_F=\sum_{k\in F}w_k$ and let $C_n(F)=[S_F,S_F+T_n]$ be the level-$n$
cylinder of $F$. Write $A_{<n}=A\cap\{1,\ldots,n-1\}$, $\lambda$ for Lebesgue
measure and $\{x\}$ for the fractional part.

## Held links

### Lemma 1: tails and gaps

For $n\ge0$ and $n\ge1$ respectively,

$$
T_n=\sum_{j\ge1}\frac{2^{-jn}}{2^j-1},\qquad
g_n=\sum_{j\ge2}\frac{2^j-2}{2^j-1}\,2^{-jn},
$$

so that $\frac23\,4^{-n}<g_n<\frac{4^{-n}}{1-2^{-n}}$. Moreover
$\sigma_n=1+\frac{2^{-n}}3+\frac{4^{-n}}7+\cdots$ decreases to $1$, and
$2\sigma_{n-1}=1+w_n+\sigma_n$.

*Proof.* Expand $w_k=\sum_{j\ge1}2^{-jk}$, exchange the nonnegative sums and
sum the geometric series in $k$. In $g_n=\sum_j2^{-jn}(1-\frac1{2^j-1})$ the
term $j=1$ vanishes, the term $j=2$ is $\frac23 4^{-n}$, and the factors
$\frac{2^j-2}{2^j-1}$ are below $1$. Finally
$2\sigma_{n-1}=2^n(w_n+T_n)$ and $2^nw_n=1+w_n$. $\square$

The inequality $T_n<w_n$ is also Remark 4.1 of
[[../library/irrationality/kovac_2024_several_irrationality_problems_ahmes_series/_index|Kovač and Tao]].

### Lemma 2: the Cantor structure

For $F\subseteq\{1,\ldots,n\}$ the cylinder $C_n(F)$ is the disjoint union of
$C_{n+1}(F)$, the open gap $(S_F+T_{n+1},S_F+w_{n+1})$ of length $g_{n+1}$,
and $C_{n+1}(F\cup\{n+1\})$. Hence the $2^n$ level-$n$ cylinders are pairwise
disjoint, $\Sigma=\bigcap_n\bigcup_FC_n(F)$, every point of $\Sigma$ is the sum
over exactly one set $A$, and $A\mapsto\sum_{n\in A}w_n$ is an
order-preserving homeomorphism from $\{0,1\}^{\mathbb N}$, ordered
lexicographically, onto $\Sigma$. Every interval $(S_F+T_n,S_F+w_n)$ with
$F\subseteq\{1,\ldots,n-1\}$ is disjoint from $\Sigma$.

*Proof.* A sum whose set agrees with $F$ below $n+1$ is at most $S_F+T_{n+1}$
when $n+1\notin A$ and at least $S_F+w_{n+1}$ when $n+1\in A$, and
$w_{n+1}>T_{n+1}$ by Lemma 1. Induction gives the disjoint cylinders and
their nested intersection. Two supports first differing at $n$ have sums
separated by at least $g_n>0$, which proves uniqueness and order preservation.
The coding map is continuous because agreement through $n$ bounds the
difference by $T_n\to0$; its compact domain and Hausdorff image make it a
homeomorphism. Flipping a sufficiently late digit gives a distinct arbitrarily
nearby point, so the image is perfect. Its cylinder lengths tend to zero and
each cylinder has a later gap, so it has empty interior. $\square$

### Lemma 3: the measure

For every $n$ and every $F\subseteq\{1,\ldots,n\}$,
$\lambda(\Sigma\cap C_n(F))=2^{-n}$. Consequently $\lambda(\Sigma)=1$,
$\lambda(\Sigma\cap[0,1))=\frac12$, and the restriction of $\lambda$ to
$\Sigma$ is the image of the fair-coin product measure under the coding map.
For $N\ge1$,

$$
\prod_{n=1}^N\Bigl(1-\frac{g_n}{T_{n-1}}\Bigr)=\frac{2^NT_N}{E}
\longrightarrow\frac1E=0.62239560\ldots .
$$

*Proof.* $\Sigma\cap C_n(F)$ is the decreasing intersection over $m\ge n$ of the
$2^{m-n}$ disjoint level-$m$ cylinders inside $C_n(F)$, whose total length is
$2^{m-n}T_m=2^{-n}\sigma_m\to2^{-n}$. A sum with $1\in A$ is at least $1$ and a
sum without is at most $T_1=E-1<1$, so $\Sigma\cap[0,1)=\Sigma\cap
C_1(\emptyset)$. For the product, $1-g_n/T_{n-1}=(T_{n-1}-w_n+T_n)/T_{n-1}
=2T_n/T_{n-1}$, which telescopes. $\square$

The gap of each level-$(n-1)$ cylinder occupies the fraction
$g_n/T_{n-1}=\frac13 2^{-n}(1+O(2^{-n}))$ of it, and the product is the
fraction of $[0,E]$ that the level-$N$ cylinders cover. A point placed
uniformly at random in $[0,E]$ therefore lies in $\Sigma$ with probability
$1/E$; this *uniform-position model* is a heuristic for rationals, not a
statement about them. Conditional on lying in any level-$N$ cylinder, a
uniformly placed real point lies in $\Sigma$ with probability
$2^{-N}/T_N=1/\sigma_N$. This too is a statement about Lebesgue measure,
not a survival probability established for any rational.

### Lemma 4: the greedy criterion

For $q\in[0,E]$ put $r_0=q$ and, for $n\ge1$, let $\epsilon_n=1$ if
$r_{n-1}\ge w_n$ and $\epsilon_n=0$ otherwise, and $r_n=r_{n-1}-\epsilon_nw_n$.
If $0\le r_{n-1}\le T_{n-1}$, then $0\le r_n\le T_n$ unless
$T_n<r_{n-1}<w_n$; call such a step a *gap at step $n$*. At a gap,
$q\notin\Sigma$, since $q$ lies in the interval $(S+T_n,S+w_n)$ of Lemma 2
with $S=q-r_{n-1}$. If no step is a gap, then $q=\sum_{\epsilon_n=1}w_n$, and
$A=\{n:\epsilon_n=1\}$ is the only set with sum $q$. The point $q$ passes the
first $N$ steps exactly when $q\in C_N(F)$ for $F=\{n\le N:\epsilon_n=1\}$.

*Proof.* When $r_{n-1}\ge w_n$, $r_n\in[0,T_{n-1}-w_n]=[0,T_n]$. Otherwise
$r_n=r_{n-1}$, which is admissible exactly when $r_{n-1}\le T_n$. If no step is
a gap then $0\le r_n\le T_n\to0$. If $q=\sum_{n\in A}w_n$ for some $A$, then
$r_{n-1}=\sum_{k\in A,k\ge n}w_k$ is at least $w_n$ when $n\in A$ and at most
$T_n<w_n$ when $n\notin A$, so the greedy choices reproduce $A$. $\square$

A gap is certified by any $F\subseteq\{1,\ldots,n-1\}$ with
$T_n<q-S_F<w_n$, whether or not $F$ is the greedy prefix (Lemma 2).

### Lemma 5: the scaled and mod-one forms

Put $s_n=2^nr_n$. Then $s_n=2s_{n-1}-\epsilon_n(1+w_n)$, the admissible range
of $s_n$ is $[0,\sigma_n]$, step $n$ selects $n$ exactly when
$s_{n-1}\ge\frac{1+w_n}2$, and step $n$ is a gap exactly when $s_{n-1}$ lies in

$$
W_n=\Bigl(\frac{\sigma_n}2,\ \frac{1+w_n}2\Bigr)\subseteq\Bigl(\frac12,\
\frac12+2^{-n}\Bigr],
$$

an interval of length $2^{n-1}g_n$, between $\frac13 2^{-n}$ and
$\frac{2^{-n-1}}{1-2^{-n}}$. Moreover

$$
s_{n-1}\equiv\{2^{n-1}q\}-\sum_{k\in A_{<n},\,k\ge2}
\frac{2^{(n-1)\bmod k}}{2^k-1}\pmod 1 ,
$$

and, when no earlier step is a gap, step $n$ is a gap exactly when the
fractional part of the right side lies in $W_n$.

*Proof.* Multiply the recurrence of Lemma 4 by $2^n$ and use $2^nw_n=1+w_n$;
the thresholds are those of Lemma 4 multiplied by $2^{n-1}$, and the bounds on
$W_n$ come from Lemma 1. For the congruence,
$s_{n-1}=2^{n-1}q-\sum_{k\in A_{<n}}2^{n-1}w_k$; the term $k=1$ is an integer,
and for $k\ge2$, $2^{n-1}\equiv2^{(n-1)\bmod k}\pmod{2^k-1}$ with
$0<2^{(n-1)\bmod k}<2^k-1$. With no earlier gap, $0\le s_{n-1}\le\sigma_{n-1}$.
If $s_{n-1}\ge1$, then $\{s_{n-1}\}\le\sigma_{n-1}-1\le\sigma_1-1<\frac12$
for $n\ge2$ (and $\{q\}\le T_1$ when $n=1$), so neither $s_{n-1}$ nor its
fractional part lies in $W_n$; otherwise $s_{n-1}=\{s_{n-1}\}$. $\square$

The test at step $n$ therefore depends on $q$ only through $\{2^{n-1}q\}$,
which is periodic in $n$ when $q$ has odd denominator, and on the earlier
choices only through the residues $(n-1)\bmod k$: each selected $k$ adds to
every later test a term of period $k$ in $n$, its echo at the multiples of
$k$.

### Lemma 6: carries

Let $0\le q<1$ have binary digits $d_m$ (the terminating expansion when $q$ is
dyadic). For any $A$ put $\theta(m)=\#\{a\in A:a\mid m\}$, $c_0=0$ and
$c_m=2c_{m-1}+d_m-\theta(m)$. Then $\sum_{a\in A}w_a=q$ if and only if
$0\le c_m\le m+2$ for every $m$; in that case $c_m=\lfloor H_m\rfloor$ with
$H_m=\sum_{j\ge1}\theta(m+j)2^{-j}$ and $H_m-c_m=\{2^mq\}$. The coefficient
transform is $\theta_A$, the number of members of $A$ dividing $m$, not
$\tau(m)\mathbf 1_A(m)$.

*Proof.* Telescoping gives
$\sum_{m\le N}\theta(m)2^{-m}=\sum_{m\le N}d_m2^{-m}-c_N2^{-N}$, and
nonnegative summation gives $\sum_{a\in A}w_a=\sum_m\theta(m)2^{-m}$, which
proves sufficiency. Under the identity, $H_m=c_m+\{2^mq\}$, and
$0\le H_m\le\sum_j(m+j)2^{-j}=m+2$ because $\theta(m')\le m'$. $\square$

A sum $q\ge1$ forces $1\in A$ (Lemma 3's proof), and the lemma applies to
$q-1$ with $A\setminus\{1\}$. The carry and scaled forms describe the same
orbit: $H_m=P_m+s_m$, where $P_m=\sum_{j\ge1}\theta_{\le m}(m+j)2^{-j}$ is the
pending contribution of the members up to $m$ and $\theta_{\le m}$ counts only
those members.

The raw carries of a representation are not bounded, nor eventually
periodic, for any infinite $A$: if $m$ is the least common multiple of $K$
members of $A$, then $\theta(m)\ge K$ and, since $c_m\ge0$ under the identity,
$2c_{m-1}=\theta(m)+c_m-d_m\ge K-1$.

This excludes periodicity of the literal integer carries. It does not exclude
a finite description using unbounded integer parameters, a periodic normalized
state, or a nonperiodic arithmetic invariant.

### Lemma 7: dyadic targets

Every finite subsum $S_F$ has odd reduced denominator, as a sum of fractions
with odd denominators. So for $q=p/2^J$ with $p$ odd and $J\ge1$, membership
$q\in\Sigma$ forces $A$ to be infinite. For $n>J$, $\{2^{n-1}q\}=0$ and the
test of Lemma 5 involves only the echo sum. For $q=\frac12$: $\epsilon_1=0$,
and the first gap, if there is one, is at the least $n\ge2$ with
$\{-\Psi_n\}\in W_n$, so that $\frac12\in\Sigma$ exactly when
$\{-\Psi_n\}\notin W_n$ for every $n\ge2$, where

$$
\Psi_n=\sum_{k\in A_{<n}}\frac{2^{(n-1)\bmod k}}{2^k-1}
$$

and $A$ is the set the greedy expansion of $\frac12$ generates.

For a rational with odd denominator, such as $\frac1{21}$, Lemma 9 supplies
the infinite-support conclusion instead.

### Lemma 8: certificates

For $n,J\ge1$ let $L_{n,J}=\sum_{j=1}^J\frac{2^{-jn}}{2^j-1}$ and
$E_{n,J}=\frac{2^{1-(n+1)(J+1)}}{1-2^{-(n+1)}}$. Then
$L_{n,J}\le T_n\le L_{n,J}+E_{n,J}$, since each omitted factor
$\frac1{2^j-1}$ is at most $2^{1-j}$. A gap at step $n$ is therefore
certified in exact rationals by $F\subseteq\{1,\ldots,n-1\}$ and $J$ with
$L_{n,J}+E_{n,J}<q-S_F<w_n$, and passing $N$ steps by
$0\le q-S_F\le T_N$ for the selected set $F$, which interval enclosures of
$S_F$ and $T_N$ certify (Lemma 4).

For example, $q=2/3$, $n=1$, $F=\emptyset$ and $J=2$ give
$L_{1,2}+E_{1,2}=7/12+1/24=5/8<2/3<1=w_1$, a strict gap certificate.

### Lemma 9: where a finite representation can end

Let $q$ have reduced denominator $Q$, and suppose $q=S_F$ for a finite
nonempty $F$ with largest element $n$. Then $n\in\{1,6\}$, or $n$ is the
multiplicative order of $2$ modulo some odd prime factor of $Q$. Consequently
the greedy expansion of $q$ can terminate (reach residual $0$) only at a step
at most
$N_Q=\max(\{6\}\cup\{\operatorname{ord}_p2:p\mid Q,\ p\text{ odd prime}\})$,
and if $q\in\Sigma$ and its greedy expansion has not terminated by step $N_Q$,
its support is infinite.

*Proof.* Since $w_n=q-S_{F\setminus\{n\}}$, the number $2^n-1$ divides
$\operatorname{lcm}(Q,2^k-1:k\in F,\ k<n)$. By the theorem of Bang and
Zsigmondy (K. Zsigmondy,
[*Zur Theorie der Potenzreste*](https://doi.org/10.1007/BF01692444),
Monatsh. Math. Phys. 3 (1892), 265--284), $2^n-1$ has a prime factor $p$ with
$\operatorname{ord}_p2=n$ unless $n\in\{1,6\}$. Such a $p$ divides no
$2^k-1$ with $k<n$, so it divides $Q$. $\square$

The precise base-two input is also stated in Erdős and Graham,
[[../library/number_theory/erdos_1980_old_new_problems_results_combinatorial_number_theory/_index|*Old and new problems and results in combinatorial number theory*]],
p. 24, footnote 1, in the context of moduli greater than one. That statement
was checked against the printed page; the classical theorem's proof is an
external dependency, not a proof reconstructed here.

This bounds every possible finite support by $\{1,\ldots,N_Q\}$, so a
rational's being a finite subsum is decidable by exact rational arithmetic.
The maximum is defined even when $Q$ has no odd prime factor, and
$N_Q\le\max(6,Q-1)$, since $\operatorname{ord}_p2\mid p-1$.

For $\frac1{21}$, $\operatorname{ord}_32=2$ and $\operatorname{ord}_72=3$,
so $N_{21}=6$. Its greedy expansion skips steps $1$ to $4$, selects $5$ and
skips $6$, with residual $1/21-1/31=10/651$ strictly between $0$ and $1/63$.
It therefore never reaches residual zero: $\frac1{21}$ is not a finite
subsum, and
$\frac1{21}\in\Sigma$ exactly when no step is a gap. For every denominator
$Q\le200$, $N_Q<200$, so each fraction of the census below that passes step
$1000$ would have infinite support if it lies in $\Sigma$.

### Lemma 10: rational shadows

Let $m\ge1$, suppose no step up to $m$ is a gap, and write $s_m=y-\delta$,
where $y\in(0,1)$ is a rational whose reduced denominator $D$ is not a power
of $2$ and $\delta$ is real. Let $e_1e_2\cdots$ be the binary digits of $y$ and
$y_i=\{2^iy\}$. If $h\ge1$ satisfies

$$
2^{h-1}|\delta|+\frac49\,2^{h-1-m}\le\frac1{2D},
$$

then for $1\le i\le h$ step $m+i$ is not a gap and selects $m+i$ exactly when
$e_i=1$, and

$$
s_{m+i}=y_i-\delta_i,\qquad
\delta_i=2^i\delta+\sum_{l=1}^{i}e_l\,2^{i-l}w_{m+l}.
$$

*Proof.* Since $y$ is not dyadic, no $y_i$ is; as $y_{i-1}$ and $\frac12$ both
lie in $\frac1{2D}\mathbb Z$, $|y_{i-1}-\frac12|\ge\frac1{2D}$, and
$e_i=1$ exactly when $y_{i-1}>\frac12$. Suppose
$s_{m+i-1}=y_{i-1}-\delta_{i-1}$, as holds for $i=1$ with $\delta_0=\delta$.
From $w_n\le\frac43 2^{-n}$ for $n\ge2$,

$$
|\delta_{i-1}|+\frac{w_{m+i}}2\le2^{i-1}|\delta|
+\sum_{l=1}^{i}2^{i-1-l}w_{m+l}
<2^{i-1}|\delta|+\frac49\,2^{i-1-m}\le\frac1{2D},
$$

the last step by the hypothesis, whose left side increases with $h$. If
$e_i=1$, then $s_{m+i-1}\ge\frac12+\frac1{2D}-|\delta_{i-1}|$, which is at
least $\frac{1+w_{m+i}}2$, so step $m+i$ selects $m+i$, and $s_{m+i-1}$ is not
in the open window $W_{m+i}$. If $e_i=0$, then
$s_{m+i-1}\le\frac12-\frac1{2D}+|\delta_{i-1}|<\frac12<\frac{\sigma_{m+i}}2$,
so $m+i$ is skipped and the step is not a gap. In both cases
$s_{m+i}=2s_{m+i-1}-e_i(1+w_{m+i})=y_i-\delta_i$. $\square$

**Corollary (dyadic roundings).** Let $J\ge1$ and
$F\subseteq\{1,\ldots,J\}$ with $S_F\notin\mathbb Z$, let $D$ be the reduced
denominator of $S_F$, and put $q=\lceil2^JS_F\rceil/2^J$. Then $q$ is a dyadic
rational and not an integer, its greedy expansion selects exactly $F$ among the
steps $1,\ldots,J$, and no step $n\le2J+1-\lceil\log_2D\rceil$ is a gap. If
$q\in\Sigma$, its support is infinite.

*Proof.* $D$ is odd and at least $3$ (Lemma 7). Since
$0<q-S_F<2^{-J}<T_J$, $q$ lies in $C_J(F)$, so by Lemmas 2 and 4 the first
$J$ steps are not gaps and select exactly $F$. Then
$s_J=y=\lceil2^JS_F\rceil-2^JS_F\in(0,1)$, whose reduced denominator is $D$
because $2$ is invertible modulo $D$. Put $h=J+1-\lceil\log_2D\rceil$.
If $h\le0$, the stated horizon is already covered by the first $J$ steps.
If $h\ge1$, Lemma 10 with $m=J$ and $\delta=0$ applies, since
$2^h\le2^{J+1}/D$ gives
$\frac49 2^{h-1-J}\le\frac4{9D}<\frac1{2D}$. If $1\notin F$, then
$0<q<S_F+T_J\le T_1<1$; if $1\in F$, the same holds for $q-1$ and
$F\setminus\{1\}$. So $q$ is not an integer, and Lemma 7 gives the infinite
support. $\square$

The case $F=\{2\}$, $J=2$ is $q=\frac12$, where the corollary covers only
step $3$. For $F=\{2\}$ and every $J\ge2$ it gives the dyadic rationals
$\lceil2^J/3\rceil/2^J$, each passing its first $2J-1$ steps by this argument
alone. A single member of such a family in $\Sigma$ would answer Problem 257.

**How far one shadow reaches.** Running the recursion of Lemma 5 backward
gives the converse constraint. If step $n$ is a gap and $1\le m<n$, then
$s_{n-1}=\frac12+\theta$ with $0<\theta<2^{-n}$, and

$$
s_m=2^{m+1-n}s_{n-1}+\sum_{l=m+1}^{n-1}\epsilon_l(1+w_l)2^{m-l}
=\frac b{2^{n-m}}+\eta,\qquad
0<\eta<2^{m+1-2n}+\frac49\,2^{-m}<2^{-m},
$$

with $b$ an odd integer. An exact shadow ($\delta=0$) of denominator $D$
therefore excludes a gap at step $n$ whenever $2^{n-m}\le2^m/D$, the same
horizon as Lemma 10 up to an additive constant. For $n\ge2m+2$ the constraint
is empty, because the odd multiples of $2^{m-n}$ are then closer together than
$2^{-m}$, so it excludes nothing. Lemma 10 never reaches step $2m$ either,
since $D\ge3$ forces $h\le m-1$. A proof by shadows therefore needs fresh
shadows at steps $m_1<m_2<\cdots$ with $m_{j+1}<2m_j$, each with denominator
and error small relative to $2^{m_j}$.

**Shadows from Dirichlet's theorem.** Such shadows exist at every step whose
state is not close to a dyadic rational, so a chain of them is not an
independent mechanism. Let $2\le k<m$. Dirichlet's theorem gives a fraction
$a/D$ in lowest terms with $1\le D\le2^k$ and $|s_m-a/D|<1/(D2^k)$. Suppose
$s_m$ lies within $2^{-t-k}$ of no fraction $b/2^t$ with $0\le t\le k$. Then
$D$ is not a power of $2$; $a/D\in(0,1)$, since $s_m\in[0,\sigma_m]$ and
$\frac1D-\frac1{D2^k}>\sigma_m-1$; and Lemma 10 applies with
$\delta=a/D-s_m$ and $h=\min(k-1,m-k)$, since $2^{h-1}|\delta|<\frac1{4D}$
and $\frac49 2^{h-1-m}\le\frac29 2^{-k}<\frac1{4D}$. With
$k=\lceil m/2\rceil$, every such step $m\ge3$ protects the next
$\lceil m/2\rceil-1$ steps. Conversely, by the backward computation, a gap at
step $n$ puts $s_m$ within $2^{-m}$ of an odd multiple of $2^{m-n}$, which is
such a near-dyadic position, at every step $m$ with $n-m\le\lfloor m/2\rfloor$.
The Dirichlet criterion leaves only near-dyadic steps uncovered, and every
gap is preceded by an unbroken run of them from about two thirds of its step
onward. Proving that a
chain of renewals continues means excluding such runs along the orbit, a
statement of the same pointwise kind as Step 4 and slightly stronger, not a
reduction of it. No such chain is proved here for either rational target; a
proof along these lines needs shadows with additional structure that makes
their renewal provable.

A different arithmetic protection applies to residuals with numerator one. If
$r_{n-1}=1/R$ for a positive integer $R$, step $n$ is not a gap: a gap needs
$T_n<1/R<w_n$, that is $2^n-1<R<1/T_n$, and $1/T_n<2^n$ by Lemma 1. The
expansion of $\frac12$ selects $2,3,6,7,14$ with residuals
$\frac16,\frac1{42},\frac1{126},\frac1{16002},\frac1{688086}$, so its first
$20$ steps are not gaps by this remark alone. Step $20$ selects $20$ and leaves
the residual $120163/240503259150$, whose numerator is prime, and the remark
stops applying. A residual $a/R$ in lowest terms is a gap at step $n$ exactly
when $a(2^n-1)<R<a2^n/\sigma_n$, an interval of length below $a$; for $a=2$ it
holds exactly when $R=2^{n+1}-1$, the residual $2w_{n+1}$.

### Lemma 11: a construction for finitely many multipliers

For every $C=\{1\}\cup B$ with $B\subseteq\{2,3,\ldots\}$ and $|B|\le3$,
there is an infinite $A\subseteq\{2,3,\ldots\}$ satisfying

$$
\sum_{n\in A}\sum_{a\in C}2^{-an}=\frac12.
$$

The [[research/leads/reciprocal_mersenne_greedy/multiplier_carries|construction and proof]]
define each digit using only earlier digits, with carries in
$\{1,2\}$. Bertrand's postulate bounds the necessary lookahead by $2n$.
When $C\ne\{1\}$, strict domination of each tail identifies the constructed
digits with the greedy digits for these weights. These are truncated
geometric weights, not the full weights $w_n$.

The same page proves the transfer that would finish this route: half
representations for $C=\{1,\ldots,J\}$ along an unbounded sequence of $J$
give a full Mersenne half representation by compactness, since the omitted
mass is at most $\frac23 4^{-J}$ uniformly over supports omitting 1.
The construction covers only $J\le4$. Its direct two-state extension fails
for $C=\{1,2,3,4,6\}$ at step 108, although the actual truncated greedy
orbit passes that step by using carry 3. The source-linked finite decision
procedure for fixed $J$ also leaves the unbounded sequence of $J$ open.
The page also makes the transfer's relation to Step 4 explicit. A half
representation for $C=\{1,\ldots,J\}$ already places
$\frac12$ outside every gap of $\Sigma$ of level at most $J$, apart from a
strip of length $\frac23 4^{-J}$ at its right end. The truncated and full
weights also have the same forcing values, for the same digits, at all
positions up to $2J+1$. These facts do not rule out a construction using the
bounded carries of each finite set, such as the extension in Lemma 13.

### Lemma 12: a window rule

One explicit rule generates digits from already fixed digits and follows the
greedy expansion of $\frac12$ until its scaled residual comes close to
$\frac12$. Put $\epsilon_1=0$ and $c_1=1$. For $n\ge2$, once
$\epsilon_1,\ldots,\epsilon_{n-1}$ are fixed, let $f_m$ be the number of
$d<m$ with $d\mid m$ and $\epsilon_d=1$; it is determined for every
$m\le2n-1$, since a proper divisor of $m$ is at most $m/2$. Define

$$
F_n=\sum_{m=n+1}^{2n-1}f_m2^{n-m},\qquad
c_n=\max(1,\lceil F_n\rceil),\qquad
\epsilon_n=2c_{n-1}-f_n-c_n,
$$

and put $\eta_n=f_{2n-2}2^{2-n}+f_{2n-1}2^{1-n}$, the part of $F_n$ from the
two positions that enter the window at step $n$.

(a) If every $\epsilon_n$ is $0$ or $1$, then $A=\{n:\epsilon_n=1\}$
satisfies $\sum_{n\in A}w_n=\frac12$, and $A$ is the greedy support of
$\frac12$.

(b) $\epsilon_2=\epsilon_3=1$. For $n\ge4$, if
$\epsilon_2,\ldots,\epsilon_{n-1}$ are bits, then $\epsilon_n\le1$, and
$\epsilon_n<0$ exactly when $\lceil F_{n-1}\rceil-F_{n-1}<\eta_n/2$.
Equivalently, let $N_{n-1}=2^{n-2}F_{n-1}$, an integer, and let $k$ be the
least nonnegative integer with $N_{n-1}+k\equiv0\pmod{2^{n-2}}$. Then
$\epsilon_n=\lfloor(4k-2f_{2n-2}-f_{2n-1})2^{1-n}\rfloor$, and the rule fails
at step $n$ exactly when $4k<2f_{2n-2}+f_{2n-1}$.

(c) Let $n\ge4$, and suppose the digits through step $n-1$ are the greedy
digits of $\frac12$, no step up to $n-1$ is a gap, and the window rule has
agreed with those digits through step $n-1$. Let
$\theta_{<n}(m)$ count the selected $d<n$ dividing $m$, and
$R_n=\sum_{m\ge2n}\theta_{<n}(m)2^{n-1-m}$. Then

$$
s_{n-1}=\lceil F_{n-1}\rceil-F_{n-1}-\frac{\eta_n}2-R_n ,
$$

the rule's digit at step $n$ is $\lfloor2(s_{n-1}+R_n)\rfloor$, and it is the
greedy digit unless $\frac12-R_n\le s_{n-1}<\frac{1+w_n}2$.

*Proof.* (a) Since $F_n$ is at most the largest $f_m$ with $n<m<2n$, and
$f_m$ is at most the number $\tau(m)\le2\sqrt m$ of divisors of $m$, we have
$2^{-n}c_n\to0$. As $\epsilon_n+f_n=\theta_A(n)$ for every $n$, with
$\theta_A$ as in Lemma 6, telescoping gives
$\sum_{n=2}^N\theta_A(n)2^{-n}=\frac12-2^{-N}c_N$, and
$\sum_m\theta_A(m)2^{-m}=\sum_{a\in A}w_a$ as in the proof of Lemma 6. By
Lemma 4, $A$ is the greedy support.

(b) $F_2=f_3/2=0$, so $c_2=1$ and $\epsilon_2=1$. Then $f_4=1$ and $f_5=0$,
so $F_3=\frac12$, $c_3=1$ and $\epsilon_3=2c_2-f_3-c_3=1$. For $n\ge3$ the
window $(n,2n)$ contains an even $m\ge4$, where $f_m\ge\epsilon_2=1$, so
$F_n>0$ and $c_n=\lceil F_n\rceil$. For $n\ge4$ the definitions give
$F_n=2F_{n-1}-f_n+\eta_n$, so with $x=F_{n-1}$ the digit is
$\epsilon_n=2\lceil x\rceil-\lceil2x+\eta_n\rceil$. As
$2x+\eta_n>2\lceil x\rceil-2$, $\epsilon_n\le1$, and $\epsilon_n\ge0$ exactly
when $2x+\eta_n\le2\lceil x\rceil$. Moreover
$\epsilon_n=\lfloor2(\lceil x\rceil-x)-\eta_n\rfloor$. Since
$x\in2^{2-n}\mathbb Z$, $\lceil x\rceil-x=k2^{2-n}$, which gives the
congruence form.

(c) Write $c^{\mathrm g}_{n-1}$ for the carry computed from the actual
greedy digits. By telescoping through step $n-1$,
$2^{n-1}\bigl(\frac12-\sum_{m<n}\theta_A(m)2^{-m}\bigr)=c^{\mathrm g}_{n-1}$.
The selected
$d<n$ contribute $\theta_{<n}(m)$ at each position $m\ge n$, and
$\theta_{<n}(m)=f_m$ for $n\le m\le2n-1$. Hence
$s_{n-1}=c^{\mathrm g}_{n-1}-F_{n-1}-\eta_n/2-R_n$.
Prior agreement with the rule and the common initial carry imply
$c^{\mathrm g}_{n-1}=c_{n-1}=\lceil F_{n-1}\rceil$; this is where the
agreement hypothesis is used. It gives the displayed formula, and by (b)
the rule's digit is $\lfloor2(s_{n-1}+R_n)\rfloor$. The
greedy digit is $1$ exactly when $s_{n-1}\ge\frac{1+w_n}2$ (Lemma 5). Since
$s_{n-1}\ge0$ and $s_{n-1}+R_n=\lceil F_{n-1}\rceil-F_{n-1}-\eta_n/2<1$, the
two digits agree unless $\frac12-R_n\le s_{n-1}<\frac{1+w_n}2$. $\square$

Without prior agreement, the actual-carry identity in the proof still
holds, but substituting $\lceil F_{n-1}\rceil$ for
$c^{\mathrm g}_{n-1}$ is not justified. In particular, survival of the
greedy prefix alone does not supply that substitution. The statement that
the rule follows the greedy orbit until the first indicated close approach
uses (c) inductively, starting with their common first three digits.

By $\tau(m)\le2\sqrt m$, $R_n\le4\sqrt n\,2^{-n}$ for $n\ge4$. The window
$W_n$ of Lemma 5 lies inside the interval of (c). So the rule reproduces the
greedy expansion of $\frac12$ while the orbit avoids these intervals, of
length at most $(4\sqrt n+1)2^{-n}$, and by (a) it gives a half
representation if it never fails. Its success is therefore sufficient for
Step 4 and follows from avoidance of the slightly longer intervals at every
step $n\ge4$. This gives a sufficient congruence condition on integers
computed from the rule's own digits. A proof that this condition holds at
every step is missing; equivalence with gap avoidance is not asserted.

For a finite set $C$ of multipliers containing $1$, let $f_m$ count only the
$d$ for which $m/d$ lies in $C\setminus\{1\}$. Then (a) holds with $v_n(C)$ in
place of $w_n$, with carries at most $\max(1,|C|-1)$, and the computation in
(b) applies at every step where $F_{n-1}$ and $F_n$ are positive. For
$C=\{1,2,3,4,6\}$ the rule uses the carries $1,2,3,1$ at steps $105$ to
$108$. These are the actual truncated greedy carries, at the step where the
two-state rule of Lemma 11 fails. Check 6 of the [evidence](evidence/_index.md)
confirms this and the agreements stated there. A rule allowing larger carries
therefore exists for every $C$. What it lacks is a proof that it meets no
coincidence in (b), and that is a pointwise property of one orbit.

### Lemma 13: a finite seed and a doubling extension

Let $C$ be a finite set of positive integers containing $1$, and let $M\ge2$
be a common multiple of its elements. Define

$$
Q_C(M,d)=\sum_{\substack{a\in C\\ad\le M}}2^{M-ad}
\qquad(2\le d\le M).
$$

There exists a support omitting $1$ that represents $\frac12$ for the weights
$v_n(C)$ if and only if some $D\subseteq\{2,\ldots,M\}$ satisfies

$$
\sum_{d\in D}Q_C(M,d)=2^{M-1}-1.
$$

There is at most one seed $D$, and decreasing greedy on these integer weights
decides whether it exists. The
[[research/leads/reciprocal_mersenne_greedy/multiplier_carries|proof and construction]]
use $c_M=1$: any representation has a positive integer carry there, and
$c_M\le1+\sum_{a\in C\setminus\{1\}}(2^a-1)^{-1}<2$. Given a seed ending
at $H=2^jM$ with carry $1$, all proper-multiplier forcing $f_m$ for
$H<m\le2H$ is known. Set $c_{2H}=1$ and work backward by

$$
c_{m-1}=\left\lceil\frac{f_m+c_m}{2}\right\rceil,
\qquad \epsilon_m=2c_{m-1}-f_m-c_m\in\{0,1\}.
$$

The computed carry at $H$ is $1$, because the positive quantity inside its
ceiling is less than $\frac23+2^{-H}<1$. Every block therefore joins the
preceding one, retains its divisor contributions and has bounded positive
carries. Telescoping proves the half representation. This construction
allows $C$ to be arbitrary, but requires its seed.

For $C=\{1,2,3,4,6\}$, $M=12$ has seed $\{2,3,6,7,10\}$; the extension
passes the carry-$3$ transition of Lemmas 11 and 12. Adjoining a common
multiple of every element of a solved $C$ preserves solvability: at that
boundary the added multiplier contributes no seed coefficient. Such
extensions do not exhaust all multipliers. The same page proves that an
old seed cannot be reused at a common boundary $M\ge2b$ after adding a
multiplier $b$: its row sum increases by at least $2^{M-2b}$. The exact
$C=\{1,2\}$ and $C'=\{1,2,3\}$ seeds at $M=6$ also show that identical
forcing through position $5$ can give different fifth digits, because the
later forcing changes the carry. Check 7 checks the finite seeds and four
doubling blocks for its stated six sets, not an unbounded family.

For $C_J=\{1,\ldots,J\}$, seeds at $M=\operatorname{lcm}(1,\ldots,J)$
for unbounded $J\ge2$ would finish the full target by Lemma 11's transfer.
Their existence remains unproved. No common carry bound as $J\to\infty$ is
required.

The multiplier page also writes the doubling blocks for the full weights
directly. After step $H$ the block word through $2H$ is one of at most two
adjacent integers determined by $s_H$, and the values of $r_H$ admissible
for the two words are separated by an interval of length exactly $g_k$, the
level-$k$ gap of Lemma 2, where $k$ is the last selected position of the
larger word.
Choosing between them is Lemma 4 on the whole block, so a selection rule
valid at every doubling boundary is equivalent to Step 4. The block cannot
restart at carry $1$ either: the carry at $2H$ exceeds the pending mass of
the digits through $H$, which for $\frac12$ already exceeds $1$ at $H=16$,
so $c_{32}\ge2$. If this pending mass is $E_H$, the multiplier page proves
that the only possible terminal carries are $\lfloor E_H\rfloor+1$ and
$\lfloor E_H\rfloor+2$. It gives their exact candidate words, proves
automatic feasibility at the two word-boundary cases, and identifies the
remaining interior failure interval. No uniform avoidance of that
interval is proved. Its equivalence to the greedy test does not preclude
proving a selection invariant in these variables.

For a discrete induction, the linked multiplier page proves a necessary
interface when passing from $C_{b-1}$ to $C_b$: if both half representations
exist, their digits agree through $b-1$, and their binary prefix integers
through $2b-1$ differ by $0$ or $1$. The corresponding carry difference is
$0$ or $1$ in that early window. The unchanged prefix, and the decremented
prefix if its borrow starts at or after $b$, satisfy the finite coefficient
recurrence. An infinite continuation is not implied. The page states the
exact signed repair equation, retaining every later divisor contribution.
A repair for every $b$ would supply all the seeds and stabilize every digit,
hence prove Step 4. This repair remains
unknown. Later carry differences can be negative: the displayed $C_4$ and
$C_5$ seeds give carries $2$ and $1$ at position $29$. Thus a nonnegative
carry-change invariant cannot prove this induction.

The multiplier page also gives the exact first-failure test for the finite
row. If $B_n$ is its remaining capacity and $r_{n-1}$ is the actual greedy
remainder, failure first occurs when $B_n<r_{n-1}<Q_C(M,n)$; this is
impossible for $n>M/2$, where the remaining row consists of binary powers.
Its identity $r_n=2^{M-n}c_n-1-E_n$ keeps the selected prefix's pending
contributions $E_n$. Positive bounded carries alone do not control this
remainder. Uniform exclusion of the first-failure interval is unproved.

An alternative on that page iterates an order-reversing map on whole
binary words. Collapse of its nested integer bounds constructs a seed,
but finiteness only gives a fixed point or a two-cycle. An explicit
different-target example has both a unique seed and a persistent
two-cycle. The page's stable-pair proposition locates every such pair: if
the stabilized bounds first differ at position $k$, they agree through
position $2k-1$ with the two sides of the dyadic point $Y$ there, and a
seed, if one exists, lies within $\frac{16}{9}2^{M-4k}$ of $Y$, so its
word has a run of at least $\min(3k-1,M-k)$ digits right after $k$, all
different from its digit at $k$. Without a seed the bounds always form
such a pair. Collapse therefore implies a seed and is implied by a seed
with no such run after any position. Proving collapse for unbounded
initial segments would construct their seeds. The necessary long-run
condition does not prove collapse or show that this construction cannot
work.

At the half target the linked page's mixed carries are positive integers
ending at $1$, each at most $\lfloor(|C|-1)/2\rfloor+1$. If their words
first differ at $k$, their difference is $1$ through $2k-1$, with a forced
binary borrow block. For $C_b$, $b\ge4$, the mixed carries rejoin at $2k$.
This is not an ordinary carry splice: the two ordinary prefix carries are
$r+1$ and $r-1$ when the mixed carry is $r$. Their old digits also force
a nonzero discrepancy at $2k+2$ when that position is in the row. The
page records the exact next-block
forcing and the coupled carry-sum and carry-difference constraints.
These prove collapse only in the already solved case $|C|\le4$; no
uniform exclusion or Boolean repair for unbounded $b$ is established.

The same page records that every set $C$ with
$1\in C\subseteq\{1,\ldots,12\}$ has its half seed, and asks whether every
finite set of multipliers does. That uniform question would contain the
initial segments and allows adjoining multipliers in any order. It is
open. Two exact examples there show what its proof must use: integer
multiplicities, such as the weights $2^{-n}+4^{-n}+3\cdot8^{-n}$, can meet
a gap although their carries are integers and each weight dominates its
tail, and multiplier sets chosen separately at each index can lose the
half target. A proof must use the bit coefficients of one fixed multiplier
set, that is, the Dirichlet structure of the coefficients in (1) of that
page.

### Lemma 14: exact Mersenne renewals

The identities

$$
\frac{w_d}{2}=\sum_{n\in G}w_n+\frac{w_L}{2},\qquad
1\le d<L,\qquad G\subseteq\{d+1,\ldots,L\},
$$

are exactly

$$
(d,L,G)=(1,2,\{2\}),\quad
(1,6,\{2,3,6\}),\quad (2,6,\{3,6\}).
$$

In particular, no chain of these renewals continues after endpoint $6$.

*Proof.* Put $e=\mathbf1_{L\in G}$ and multiply the identity by $2$:

$$
w_d-2\sum_{n\in G\setminus\{L\}}w_n=(1+2e)w_L.
$$

If $L\ge3$ and $L\ne6$, Bang–Zsigmondy, in the precise form used in
Lemma 9, supplies a prime $p$ with $\operatorname{ord}_p2=L$. Thus
$p\ge L+1>3$. It divides none of the denominators on the left, whereas
the right side has negative $p$-adic valuation because $1+2e$ is $1$
or $3$. This is impossible. Only $L=2,6$ remain.

For $L=2$ necessarily $d=1$, and $e=1$ gives the first identity. For
$L=6$, a denominator $31$ occurs only at index $5$, and a factor $5$
only at index $4$. Their valuations rule out $d=4,5$ and force
$4,5\notin G$ when $d<4$. If $d=3$, multiplication by $63$ would give
$9=1+2e$, impossible. If $d=2$, it gives
$21=18\mathbf1_{3\in G}+1+2e$, forcing $G=\{3,6\}$. If $d=1$, it
gives $63=42\mathbf1_{2\in G}+18\mathbf1_{3\in G}+1+2e$, forcing
$G=\{2,3,6\}$. The three displayed identities check directly.
$\square$

There is a quantitative restriction on replacing $1/2$ by a varying
terminal coefficient. Suppose a half-prefix through $L\ge2$ survives,
with selected set $F$, and write

$$
\frac{r_L}{w_L}=\frac uv,\qquad 0<u<v,\quad \gcd(u,v)=1,
\qquad e=\mathbf1_{L\in F}.
$$

The strict range follows from $0<r_L\le T_L<w_L$. For every prime $p$
with $\operatorname{ord}_p2=L$ one has

$$
p\nmid v,\qquad
p^{v_p(2^L-1)}\mid u+ev.
$$

Indeed,
$\frac12-S_{F\setminus\{L\}}=(u+ev)/(v(2^L-1))$, whose left side
has no $p$ in its reduced denominator. Coprimality gives
$\gcd(u+ev,v)=1$, so $p\mid v$ is impossible and the divisibility
follows. Writing $P=p^{v_p(2^L-1)}$, this implies $v\ge P+1$ when
$e=0$ and $v\ge(P+1)/2$ when $e=1$. Thus, for $L\ne6$, some such
$p\ge L+1$ forces $v\ge\lceil(L+2)/2\rceil$.

Consequently, no finite set of fixed rational coefficients $u/v$ can
describe terminal residuals $r_L=(u/v)w_L$ at unbounded surviving
positions of the half orbit. This excludes only that form of renewal.
It does not exclude approximate rational shadows, terminal coefficients
with growing denominators, or a full half representation. The variable
terminal carries in Lemma 13's full-weight block formulation remain
available, with their selection theorem unproved.

## The route

1. Take $q=\frac12$, the case $F=\{2\}$, $J=2$ of the corollary to Lemma 10;
   $\frac1{21}$ is a second test case, with odd denominator. Any member of
   that corollary's dyadic family would serve in place of $\frac12$: its first
   $2J+1-\lceil\log_2D\rceil$ steps are then held by the corollary, and its
   later steps carry the same obligation as Step 4.
2. By Lemmas 4 and 5, $q\in\Sigma$ exactly when no step is a gap. *Held.*
3. No step $n\le20000$ is a gap, for $\frac12$ and for $\frac1{21}$ (check 2
   of the [evidence](evidence/_index.md)). *Held, finite.*
4. **Gap.** No step $n>20000$ is a gap: by Lemma 7, $\{-\Psi_n\}\notin W_n$
   for every $n>20000$. Lemma 12 gives a sufficient integer form: the rule
   there meets no coincidence, which check 6 confirms through step 20000.
   Alternatively, construct the seeds of Lemma 13 for unbounded initial
   segments of multipliers and apply the uniform approximation of Lemma 11.
   Two sufficient approaches are to exclude the exact first-failure interval
   at every successor or to prove that the half-target whole-word iteration
   collapses. The mixed-carry rejoin supplies neither conclusion.
5. By Lemma 7, $A$ is then infinite with $\sum_{n\in A}\frac1{2^n-1}=\frac12$,
   a negative answer to Problem 257. *Held, given Step 4.* For $\frac1{21}$,
   Lemma 9 gives the infinite support in the same way.

The steps use one convention throughout: base $2$, the denominators
$2^n-1$, and the single greedy sequence of $q$; Lemmas 4–6 are three
descriptions of that sequence, and Lemmas 7 and 9 turn membership into an
infinite support.

### Failure account

- **Step.** Step 4, for every $n>20000$; any finite range can be checked,
  with unresolved interval comparisons reported as undecided. The missing
  obligation is all later steps, not a longer finite prefix.
- **Missing input.** A proof that the scaled residual of one specific rational
  avoids, at every step $n$, the window $W_n$ of length about
  $\frac13 2^{-n}$ just above $\frac12$. For $\frac12$ this is, by Lemma 7,
  the statement that the sum $\Psi_n$ of the rationals
  $2^{(n-1)\bmod k}/(2^k-1)$ over the self-generated set $A_{<n}$ never has
  $\{-\Psi_n\}\in W_n$.
- **Why it fails.** For $\frac12$ the residual $r_{n-1}$ is a rational whose
  reduced denominator divides $2\operatorname{lcm}\{2^k-1:k\in A_{<n}\}$.
  The elementary upper bound obtained by replacing this least common multiple
  by a product is as large as $2^{1+n(n-1)/2}$, and supplies no separation from
  an interval of length $g_n<2\cdot4^{-n}$. This does not assert that the
  reduced denominator attains that bound. The raw-carry obstruction below
  excludes literal periodic carries; the finite census tests only the stated
  periodic supports. Neither supplies pointwise avoidance for this orbit.
  In binary, a gap at step $n$ means that $r_{n-1}$ has a
  one at position $n$ followed by $n-1$ zeros, so the obligation resembles
  questions about long zero runs in the binary digits of specific constants.
  The two arithmetic protections proved here are local. A rational shadow at
  step $m$ (Lemma 10) excludes gaps only before step $2m$, and the necessary
  condition that the backward computation after it places on $s_m$ is empty
  for gaps at steps $n\ge2m+2$; the numerator-one remark covers the first 20
  steps of $\frac12$ and then stops. Continuing the remark needs a residual
  with numerator one after every selection; continuing the shadows needs a
  renewal at least once per doubling of the step index. By Dirichlet's
  theorem shadows renew at every step that is not near-dyadic, and each gap
  is preceded by a run of near-dyadic steps, so proving the renewals is again
  a pointwise property of the orbit, of the same kind as the missing input.
  The alternative through geometric multipliers needs representations for
  unbounded initial segments $\{1,\ldots,J\}$. Lemma 11 supplies only
  $J\le4$. Lemma 12 supplies a rule with the larger carries for every such
  segment, but its digits are bits only away from the coincidences of
  Lemma 12(b), a pointwise condition again. A representation for one such
  segment already excludes the gaps of $\Sigma$ of level at most $J$, apart
  from a strip at each right end. Lemma 13 supplies a different completion
  from a finite integer seed. Its block recurrence is proved, but existence
  of the seeds for unbounded $J$ is missing. Adjoining common multiples
  cannot fill arbitrary missing multipliers, and finitely many seeds do not
  approximate the full weights to arbitrarily small error. Keeping an old
  seed at a common boundary fails by the positive row increment in Lemma 13;
  keeping earlier digits merely because their forcing agrees fails in the
  explicit position-$5$ example. A replacement induction must control the
  changed digits and their carries. Convex interpolation does not supply
  that control: the multiplier page gives a gap at position $4$ for weights
  $2^{-n}+\frac79 4^{-n}$, between two solvable Boolean endpoints.
  The necessary two-prefix interface for adjoining $b$ only controls the
  first $2b-1$ positions. Its signed repair equation has no proved uniform
  solution. Requiring later carry changes to stay nonnegative is false,
  even from $C_4$ to $C_5$, where the carry decreases at position $29$.
  This refutes that proposed invariant, not Boolean seed extension.
  The exact remaining-capacity test retains the pending contributions
  through $r_n=2^{M-n}c_n-1-E_n$, but supplies no uniform avoidance bound.
  The alternative whole-word iteration has no proof of collapse at the
  half target. Its stable-pair proposition gives a necessary long-run
  condition when a seed coexists with a nontrivial pair, but does not
  exclude all such pairs. The special half-target mixed carries force a
  borrow block through $2k$ and rejoin there; using that rejoin as a splice
  fails because the ordinary boundary carries are two apart and the old
  digits force another discrepancy at $2k+2$ when the row continues that
  far. A valid replacement must
  retain both mixed carries, the common forcing, those boundary offsets
  and the pending mass. The displayed joint constraints supply no
  all-future invariant, so uniform collapse remains unknown, not refuted.
  The direct full-weight construction retains two candidate terminal
  carries determined by the actual pending mass. Its endpoint cases
  always pass; its interior case leaves the explicit phase interval on
  the multiplier page. No successor invariant excludes that interval.
  Restarting every block at carry $1$ is false, since $c_{32}\ge2$ for
  $\frac12$. Always choosing the smaller of the two candidate carries
  is also false: $E_{32}<1$ but $c_{64}=2$. Exact renewals
  $\frac{w_d}2=S_G+\frac{w_L}2$ cannot replace
  it: Lemma 14 classifies all such identities and proves that they stop
  at endpoint $6$. A finite set of fixed rational multiples of $w_L$
  also cannot provide unbounded renewal positions. The variable-carry
  selection theorem remains unknown, not refuted by these failures.
  Finally, the finite census
  of all multiplier sets inside $\{1,\ldots,12\}$ suggests that every
  finite set has a half seed, but integer multiplicities and
  index-dependent sets can lose the half target, so an argument blind to
  the fixed Boolean multiplier structure cannot prove it.
- **Standing of the input.** Unproved here and not refuted by the finite
  checks. The uniform-position model is no premise about either rational.
  No weaker sufficient input is established here: selection at the full-weight
  doubling boundaries is equivalent to it, while seeds for unbounded
  initial segments, the window rule and whole-word collapse imply it.

## Computations

The [evidence program](evidence/_index.md) certifies the following finite
statements; none proves membership in the full Mersenne achievement set or an
irrationality.

1. **Census.** Of the 19654 reduced fractions $p/Q\in(0,E)$ with $Q\le200$,
   41 are finite subsums, each ending at a step allowed by Lemma 9, 7395 meet a
   certified gap, every one at a step at most 12, and the remaining 12218 pass
   step 1000 without terminating, so by Lemma 9 any of them that lies in
   $\Sigma$ has infinite support. The fraction passing among
   those that are not finite subsums is $12218/19613=0.6230$, against
   $1/E=0.6224$. The step-$n$ gap counts, as fractions of the fractions that
   met no gap before step $n$, follow the gap fractions $g_n/T_{n-1}$ of
   Lemma 3:

   | step $n$ | 1 | 2 | 3 | 4 | 5 | 6 | 7 |
   | --- | --- | --- | --- | --- | --- | --- | --- |
   | gaps | 4809 | 1470 | 600 | 268 | 132 | 66 | 32 |
   | observed fraction | 0.2447 | 0.0990 | 0.0449 | 0.0210 | 0.0106 | 0.0053 | 0.0026 |
   | $g_n/T_{n-1}$ | 0.2448 | 0.0988 | 0.0452 | 0.0217 | 0.0106 | 0.0053 | 0.0026 |

   The later gaps are 8, 6 and 4 at steps 8, 9 and 12.
2. **Long orbits.** $\frac12$ and $\frac1{21}$ pass every step up to 20000,
   selecting 10028 and 10006 of the first 20000 integers. The least value of
   $|2^nr_{n-1}-1|$ over $15\le n\le20000$ is about $2^{-13.3}$ for
   $\frac12$ and $2^{-13.5}$ for $\frac1{21}$, at steps 15999 and 2215
   respectively. Both minima lie strictly between $2^{-14}$ and $2^{-13}$,
   as the integer enclosures certify. A gap at step $n$ requires
   $\sigma_n-1<2^nr_{n-1}-1<w_n$, with $w_n=2^{-n}/(1-2^{-n})$.
3. **Near misses.** Among the 6830 reduced fractions with $Q\le150$ that pass
   step 400 without terminating, the steps $15\le n\le400$ with $n>t+2$ and
   $|2^nr_{n-1}-1|<2^{t-n}$ number 2, 10, 22, 120 and 438 for
   $t=2,4,6,8,10$, against 1.7, 6.7, 26.7, 106.7 and 426.9 if each
   $2^nr_{n-1}-1$ were uniform on $[-1,1]$. Distinct fractions can have equal
   residuals at the same step, meaning $q-S_F=q'-S_{F'}$ for their selected
   prefixes. Their later greedy choices then coincide. The events are not
   independent: they come from 1, 3, 9, 36 and 139 distinct pairs
   $(n,r_{n-1})$, respectively. The comparison is
   descriptive and makes no asymptotic prediction for these dependent orbits.
4. **Periodic supports.** For each of the 1965 nonempty residue sets $R$ modulo
   $M\le10$ that are not periodic with a smaller period, the certified
   enclosure of $\sum_{n\ge1,\,n\bmod M\in R}w_n$ contains no fraction with
   denominator below $2^{1000}$. So no nonempty support periodic with period at
   most 10 has a rational sum with denominator below $2^{1000}$. Changing
   finitely many members adds to the sum a rational $\rho$ with odd denominator,
   so an eventually periodic infinite support with eventual period at most 10
   and rational sum $a/b$ is excluded when the least common multiple of $b$ and
   the denominator of $\rho$ is below $2^{1000}$. The empty support is excluded
   from this census; its sum is zero.
5. **Finite arithmetic witnesses.** The reduced dyadic rational
   $q=4203/32768$ first meets a gap at step 17, after selecting exactly
   $F=\{4,5,6,7,8,10,11,13,14,16\}$. Its residual satisfies
   $L_{17,2}+E_{17,2}<q-S_F<w_{17}$, with the exact bounds of Lemma 8.
   Thus a dyadic denominator $2^J$ alone does not confine gaps to steps
   below $J$: here $J=15$. The same check reproduces the failed two-state
   extension and the actual truncated greedy carries at steps 106--108 in
   [[research/leads/reciprocal_mersenne_greedy/multiplier_carries|the multiplier construction]].
6. **Window rule.** The rule of Lemma 12 gives bits through step 20000 and
   reproduces there the greedy digits of $\frac12$ certified by check 2; at
   every step $4\le n\le20000$ its digit equals the closed form of
   Lemma 12(b). With $f_m$ restricted to the multipliers of $C$, it
   reproduces the exact truncated greedy digits for $C=\{1,2,3,4,6\}$ and
   $C=\{1,\ldots,8\}$ through step 400, with the carries $1,2,3,1$ at steps
   105 to 108 for the first set.
7. **Finite seeds.** The integer equation of Lemma 13 is checked for
   $C=\{1\}$, $\{1,2\}$, $\{1,2,3\}$, $\{1,2,3,4,6\}$,
   $\{1,2,3,4,6,12\}$ and $\{1,\ldots,8\}$ at
   $M=\max(2,\operatorname{lcm}(C))$. Four doubling blocks are constructed;
   every bit, carry, earlier divisor contribution and boundary carry is
   checked through $16M$. Exact greedy comparison runs through
   $\min(400,16M)$, with index 1 omitted. The stated seed at $M=12$ and its
   carry-$3$ transition are pinned, and an altered seed is rejected. These
   finite checks support the implementation of the extension; the extension
   proof is in Lemma 13 and the linked multiplier page.

8. **Signed seed repair.** The displayed seeds at $M=60$ for $C_4$ and
   $C_5$ have exact row sum $2^{59}-1$. Their finite carries obey (1) on
   the multiplier page and lie in $[1,|C|]$, ending at $1$, but at position
   $29$ the carry changes from $2$ to $1$. Check 8 recomputes the row
   identities, all finite carries, the transition at positions $28$--$30$
   and the signed repair equation. The seed theorem supplies their infinite
   extensions. This excludes a nonnegative-carry repair invariant; it does
   not construct seeds for unbounded initial segments.
9. **Multiplier sets.** Every set $C$ with
   $1\in C\subseteq\{1,\ldots,12\}$, 2048 sets, has its half seed at
   $M=\max(2,\operatorname{lcm}(C))$, and for the 1542 with $M\le2520$ the
   whole-word iteration of the multiplier page collapses to it. For
   $C=\{1,2,3,4,6\}$ and $M=12$, the stable-pair proposition is tested at
   all 2048 targets below $2^{11}$, 427 of which give a nontrivial pair.
   Two multiplicity examples and one index-dependent family are checked to
   lose the half target in exact arithmetic. These finite checks construct
   no seed for an unbounded family of sets. The 169 nontrivial
   different-target pairs with first disagreement $k\ge3$ also check the
   mixed-carry rejoin, the ordinary-carry offsets and the subsequent forcing.
   Their terminal carries need not be $1$, so they do not test the
   half-target bound or prove collapse there.
10. **Full-weight doubling blocks.** Along the certified prefix of
    $\frac12$, the block identity and its two-candidate window of the
    multiplier page hold exactly at $H=2,4,\ldots,64$, and its gap
    separation holds for every word with $H\le7$. The value of $E_{16}$,
    the carry $c_{32}=2$, and the two explicit terminal-carry candidates
    and their residuals are checked, including $E_{32}<1$, $c_{64}=2$,
    which requires the larger candidate. A different-target control has both
    candidates fail. The exceptional endpoints $L=2,6$ in Lemma 14 give
    exactly the three displayed renewal identities by exhaustive subset
    checking. Bang–Zsigmondy and the written argument, not this finite
    check, exclude all other endpoints. No later doubling block is decided.

## Limits of proposed full-weight certificates

These are scoped obstructions to certificates of the kinds tried here, not
barriers to every route.

- **Raw carries.** By Lemma 6 the carries of any infinite support are
  unbounded, so no finite list of carry values, and no eventually periodic
  carry sequence, can certify membership.
- **Dyadic denominators.** Check 5 gives a gap at step 17 for a rational
  of denominator $2^{15}$. Parity excludes finite representations of
  nonintegral dyadics but does not exclude their later gaps. This witness
  refutes that proposed uniform cutoff, not the half target or Lemma 10's
  horizon, which also depends on the denominator of the finite subsum.
- **Periodic supports.** Check 4 above excludes the stated period and
  denominator ranges. It does not exclude larger periods, larger denominators,
  or periodic normalized carry rules for nonperiodic supports. The computed
  prefixes of $\frac12$ and $\frac1{21}$ each select about half of their
  indices; this proves neither an asymptotic density nor a structural rule.
- **Averaging over many rationals.** For $n\ge\log_2Q+2$ a level-$(n-1)$
  cylinder has length $T_{n-1}\le\sigma_1 2^{1-n}<1/Q$ and contains at most one
  point of $\frac1Q\mathbb Z$, so the number of fractions $p/Q$ with a gap at
  step $n$ is a sum of single-orbit events. A bound by interval length plus
  one per occupied cylinder then permits every remaining fraction to fail.
  This is a limitation of that bound, not of every counting or Fourier
  argument. Poisson summation expresses the number of fractions $p/Q$ in the
  $2^{n-1}$ gaps of step $n$ through the transforms at the frequencies $hQ$,
  whose moduli are $2^{n-1}\prod_{k<n}|\cos(\pi hQw_k)|$ times the transform
  of one gap. A bound computed from these moduli alone holds equally for every
  translate of the union of gaps, since translation changes only the phases,
  and some translate puts a fraction $p/Q$ in a gap of step $n$. Such a bound
  is therefore at least $1$ at every step, and its sum over $n$ diverges; a
  counting argument for a fixed $Q$ needs the phases, which encode the
  positions of the individual orbits. Measure-class information alone
  (Lebesgue density, $L^p$ norms, Fourier coefficients of
  $\mathbf 1_\Sigma$) is unchanged on removing the countable set
  $\mathbb Q$ from $\Sigma$. Without additional pointwise
  information it cannot decide rational membership. The modified set need not
  be closed, so this observation does not rule out using the closed-set
  structure of $\Sigma$ together with analytic estimates.
- **Fixed points.** Each binary expansion $(\epsilon_n)$ of
  $t=\sum_n\epsilon_n2^{-n}\in[0,1]$ gives the point $\sum_n\epsilon_nw_n$
  of $\Sigma$, and the order is preserved. The two expansions of an interior
  dyadic point of depth $n$ give two points $g_n$ apart, the ends of a gap, so
  either convention gives a map from $[0,1]$ to $\Sigma$ that jumps at every
  interior dyadic point. Writing the target
  as a fixed-point equation for $t$ and invoking a continuity theorem is
  therefore invalid; an invariant must avoid every jump.
  The finite whole-word iteration on the
  [[research/leads/reciprocal_mersenne_greedy/multiplier_carries|multiplier page]]
  has a separate obstruction: nested integer bounds can stabilize in a
  two-cycle around a valid seed. Its explicit witness changes the target
  from $2^{M-1}-1$. By the stable-pair proposition there, such a
  two-cycle coexisting with a seed forces a long run of equal digits beside
  a dyadic point, and without a seed a two-cycle always occurs. These are
  restrictions on a possible proof, not an exclusion of this route. At the
  half target, positivity and the terminal value $1$ give the additional
  mixed-carry bounds of that page, but no uniform contradiction is proved.
- **Exact renewals.** Lemma 14 classifies every identity
  $\frac{w_d}2=S_G+\frac{w_L}2$ with $d<L$ and
  $G\subseteq\{d+1,\ldots,L\}$. The half orbit can restart in this
  form only at $2$ and $6$, so this proposed infinite renewal chain is
  impossible. More generally, at a surviving half-prefix the reduced
  denominator of $r_L/w_L$ is at least $\lceil(L+2)/2\rceil$ for
  $L\ne6$. Finitely many fixed rational multiples of $w_L$ therefore
  do not give an alternative renewal chain. These conclusions concern
  exact terminal forms, not arbitrary half membership, approximate
  shadows, or the variable terminal carries of the multiplier page.
- **Base two is critical.** For an integer $t\ge2$, the sums of distinct
  $1/(t^n-1)$ form a Cantor set of measure $\lim_n2^nT^{(t)}_n$, where
  $T^{(t)}_n=\sum_{k>n}\frac1{t^k-1}$; the limit is $1$ for $t=2$ and $0$ for
  every $t\ge3$. The proof of Kovač and Tao's Theorem 2.3 shows that merged
  sums over several bases contain a nondegenerate interval under their
  hypothesis $\sum_k\frac1{t_k-1}>1$; for the single base $2$ that sum equals
  $1$, the boundary case, and the route cannot borrow that flexibility.
- **Deforming the base.** For $\frac12<x<1$,
  $\frac{x^n}{1-x^n}\le\sum_{k>n}\frac{x^k}{1-x^k}$ once $x^{n+1}\le2x-1$, so
  by Kakeya's criterion the sums of distinct $\frac{x^n}{1-x^n}$ have gaps at
  only finitely many levels. The pairs (base, sum) for bases in
  $[\frac12,x_0]$ with $x_0<1$ form a compact set, so $q\in\Sigma$ would
  follow from $q$ being such a sum along a sequence of bases tending to
  $\frac12$. But a gap of $\Sigma$ at step $n$ that contains $q$ stays a gap
  containing $q$ at every base close enough to $\frac12$, because the
  inequalities $w_k>T_k$ for $k\le n$ and the gap's defining inequalities are
  strict at $\frac12$. The number of levels with gaps grows without bound as
  the base tends to $\frac12$, so certifying membership this way means
  excluding gaps at more and more levels, the same infinite family of tests.

## What composes

- [[../library/irrationality/borwein_1992_irrationality_certain_series/theorem_1|Borwein's Theorem 1]]
  and the other classes on the problem page give irrational values for
  particular supports; they constrain where a rational sum can come from but
  supply no membership.
- Kovač and Tao's Theorems 2.3 and 2.5 produce rational values with several
  bases or with shifted denominators. Their constructions use exactly the
  freedom that Problem 257 removes.
- [[problems/irrationality/E0257/claims/2026_09_11_cook|Cook's note]] and his
  [[problems/irrationality/E0257/claims/2026_09_25_cook|weighted-support claim]]
  are pending partial claims, used here as no premise. If the first holds, a
  support with rational sum has divergent reciprocal sum. The computed
  prefixes select about half of their indices, but no limiting density or
  reciprocal-sum divergence for their infinite continuations is proved here.
- The binary attacks on
  [[research/totient_binary_new_attack/proof_sketch|Problem 249]] and
  [[research/prime_binary_new_attack/proof_sketch|Problem 251]] concern other
  coefficient sequences; their comparison classes do not preserve
  $\theta_A$ for an arbitrary zero-one support, and nothing from them is used
  here.

## Next steps and reopening

The route is blocked at Step 4. It reopens on any of the following.

- A structural invariant of the orbit of $\frac12$, or of another explicit
  rational, forcing $\{s_{n-1}\}\notin W_n$ for all large $n$. A renewal rule
  for the rational shadows of Lemma 10 counts only if it carries structure
  beyond Dirichlet's theorem: its argument does not guarantee renewal at
  near-dyadic states, including those necessarily preceding a gap.
  The dyadic roundings of the corollary supply an exact first shadow at step
  $J$.
- A rational whose infinite greedy support has a finite description
  (eventually periodic, automatic, or otherwise) together with a proof that
  the sum over it is that rational. Check 4 excludes the periodic supports
  with period at most 10 for denominators below $2^{1000}$.
- An argument that certifies a rational point of $\Sigma$ outside the finite
  subsums without following one orbit, using additional structure beyond the
  measure calculation or finite counts alone.

For truncated weights $\sum_{a=1}^J2^{-an}$, Lemma 13 gives a finite
construction task: produce the seed at $M=\operatorname{lcm}(1,\ldots,J)$
for unbounded $J$. The doubling extension then supplies the entire infinite
support for each such $J$, and Lemma 11's transfer proves Step 4. The
common-multiple adjoining rule alone does not produce these sets. A proposed
seed construction must solve the exact integer equation, not just a longer
prefix or a bounded list of values of $J$. The necessary two-prefix
interface restricts an induction adjoining the next multiplier; its
continuation must solve the signed repair equation with the Boolean digit
bounds. A sufficient invariant must permit negative carry changes and
control their effects at later multiples. No such invariant is supplied.
The exact residual-capacity bounds on the multiplier page give another
test: exclude its first-failure interval at every position through $M/2$,
for unbounded initial segments, while retaining every pending divisor
contribution. Collapse of the whole-word iteration is another sufficient
construction. Its stable-pair proposition and mixed-carry bounds leave a
concrete test: exclude the coupled continuation after the first borrow
block for unbounded $b$, or repair it to an ordinary seed while paying both
boundary offsets and every later divisor contribution. Equality of the
mixed carries at $2k$ does not discharge this test. The
census of all multiplier sets inside $\{1,\ldots,12\}$ suggests proving
the seed for every finite multiplier set at once, which would permit
adjoining multipliers in any order. Its proof must use the bit
coefficients of one fixed set: integer multiplicities and index-dependent
sets can lose the half target. These are proposed constructions, not
additional completed steps of the full proof.

Each of these interfaces implies gap avoidance along one orbit, the full
orbit of $\frac12$ or its truncated orbit through $M/2$, and none is weaker
than that avoidance. Selection at the full-weight doubling boundaries and
exclusion of the first-failure interval are equivalent to it; the window
rule, whole-word collapse and exclusion of the mixed-carry continuation
imply it and are not known to be equivalent to it.
These implication directions do not rule out proving one of the
construction theorems. In particular, the multiplier page's explicit
replacement for a fixed terminal carry keeps $E_H$ and chooses between
$\lfloor E_H\rfloor+1$ and $\lfloor E_H\rfloor+2$. Its endpoint cases
are proved, and its interior phase avoidance is unproved. The fixed
carry-$1$ restart and the exact renewals of Lemma 14 cannot supply that
missing argument. A successful invariant must derive the needed bounds
from the half-rooted states and the divisor contributions; those bounds
cannot be assumed merely because the variables describe the orbit.

The next discriminating test for the direct orbit route requires a proposed
invariant. State its exact state variables, prove it contains a certified
prefix of one rational, and prove that every successor both remains in the
invariant and avoids $W_n$.
A normalized state must also imply the original carry bound or residual tail
bound and retain the divisor contributions of all earlier choices. Such a
proof would discharge Step 4; failure would refute that particular invariant.
For a renewal rule the test is concrete: express the shadow at $m_{j+1}$
through the shadow at $m_j$ and the digits selected in between, and bound its
denominator and error well enough that Lemma 10 reaches $m_{j+2}$, without
assuming that the intermediate states avoid near-dyadic positions. No
invariant or renewal rule with these properties is supplied here. An
invariant may instead be stated through Lemma 12; it must then show that the
integers $N_{n-1}$ never come within the bound of Lemma 12(b) below a multiple
of $2^{n-2}$. Extending the finite prefix or inspecting additional digits
alone does not perform this test.
