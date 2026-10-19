---
name: research/leads/property_p_sieve_multiplicity
title: Composite-modulus large sieve for property P
desc: |
  Author-recorded sieve and Fourier arguments for property P: convergence
  for pairwise coprime sets, equivalence with a uniform finite bound, a
  reduction to odd primitive sets, biased smooth guards, a bound
  O(log log N), a whole sketch whose one open step is the joint guard
  budget, and certified congruence-block bounds with explicit counting
  errors. Mixed constraints and an unproved inverse estimate retain the
  missing global charge. The reciprocal-sum question remains open.
problems: [12]
research_state: blocked
review_status: unreviewed
created: 2026-10-16T13:21:37Z
updated: 2026-10-17T19:26:20Z
---

# Composite-modulus large sieve for property P

[[research/leads/_index|..]]

[[research/leads/property_p_sieve_multiplicity/certified_mass_selection|certified_mass_selection]]: A positive-mass extraction into jointly certified short blocks would
prove E12(iii). A maximal matching pairs all but a bounded reciprocal
mass locally, while an exact four-element example prevents those local
pairs from being certified together in any eligible representation.

[[research/leads/property_p_sieve_multiplicity/evidence/_index|evidence/]]: Exact finite normalization, occupancy and obstruction checks, retained
admissible-window witnesses, and certified two-block harmonic upper
bounds, with exploratory solver maxima kept at their finite scope.

***

The remaining question in
[[problems/integer_sequences/E0012/_index|Problem 12]] asks whether every
infinite $A\subseteq\mathbb N_{>0}$ with property P has
$\sum_{a\in A}1/a<\infty$. Here property P means that no $a\in A$ divides
$b+c$ for distinct $b,c\in A$ both greater than $a$.

This note supplies a precise composite-modulus sieve inequality and tests
the proposed use of its multiplicity factor. It then adds a
residue-occupancy bound with exponential gain, a convergence rate in terms
of a greedy sequence of coprime elements, convergence for every pairwise
coprime set, and a bound in terms of the primes that elements share. A
gluing construction shows that the infinite question is equivalent to a
uniform bound for finite property-P sets, and a Fourier argument shows that
early elements can coexist with a heavy late part only through small
smooth guard moduli. With a smooth-part normalization this gives a bound
$O(\log\log N)$ for the reciprocal sum of every property-P subset of
$\{1,\ldots,N\}$. An exact signed identity gives another sufficient
criterion, whose energy premise is unproved and implies the uniform bound
directly. The note assembles these links into one argument whose single
open step is a joint guard budget. It bounds certified full congruence
blocks by $\log2$ plus an explicit counting error under the block-shape and
size hypotheses stated below. The error must also be bounded; certification
alone does not control arbitrary sets. It identifies the missing multiscale
charge and refutes
proposed normalization potentials with explicit families. These are
author-recorded arguments by Plasma AI, without independent review. The
large-sieve, Brun--Titchmarsh, and prime-number-theorem inputs are used at
statement level; no result here resolves the reciprocal sum
question.

## The exact inequality

Let $2\le Q<X$ be integers. Write

$$
S=A\cap[1,Q],\qquad T=A\cap(Q,X],\qquad m=|S|,
$$

and, for $d\ge2$, put

$$
D_Q(d)=|\{a\in S:d\mid a\}|,\qquad
M_Q=\max_{2\le d\le Q}D_Q(d).
$$

The empty case has $M_Q=0$. Define also

$$
\kappa(a)=\frac{a-\gcd(a,2)}{a+\gcd(a,2)},\qquad
W_Q=\sum_{a\in S}\kappa(a).
$$

An infinite property-P set contains neither 1 nor 2. The first would
forbid any two larger elements. For 2, an infinite tail has two distinct
elements of the same parity. Thus every $a\in S$ is at least 3, and
$\kappa(a)\ge1/3$. The inequality is

$$
\boxed{\quad W_Q\,|T|\le M_Q(X+Q^2).\quad}                 \tag{1}
$$

Moreover,

$$
M_Q=\max_{\substack{p\le Q\\p\ \mathrm{prime}}}D_Q(p),
\qquad
W_Q=m-O(\log(m+1)).                                    \tag{2}
$$

Consequently, as $m\to\infty$, (1) gives

$$
|A\cap[1,Q]|\,|A\cap(Q,X]|
\le (1+o(1))M_Q(X+Q^2).                                \tag{3}
$$

The error is uniform in $X$ and $T$. In particular, the multiplicity in
(3) is an explicit divisor count, not an unspecified loss.

## Proof and the distinct-elements convention

Set $N=|T|$ and
$F(\alpha)=\sum_{b\in T}\exp(2\pi i b\alpha)$. For $a\in S$, let
$c_r$ count the elements of $T$ congruent to $r$ modulo $a$. If
$r\not\equiv-r\pmod a$, at most one of $c_r,c_{-r}$ is nonzero.
Otherwise elements in the two classes would be distinct forbidden larger
summands. A self-inverse class can contain at most one element, but it
need not be empty. There are $s=\gcd(a,2)$ such classes, so at most
$(a+s)/2$ classes are occupied.

Cauchy--Schwarz and finite Fourier orthogonality give

$$
\begin{aligned}
\sum_{r=1}^{a-1}|F(r/a)|^2
 &=a\sum_{t\bmod a}c_t^2-N^2\\
 &\ge\left(\frac{2a}{a+s}-1\right)N^2
 =\kappa(a)N^2.                                      \tag{4}
\end{aligned}
$$

For $N=0$ the desired result is immediate. For $N>0$, sum (4) over $a\in S$.
A reduced fraction $u/d$ with $1\le u<d$ and $(u,d)=1$ appears among
the fractions $r/a$, $a\in S$, $1\le r<a$, exactly $D_Q(d)$ times:
it appears once for each multiple $a$ of $d$, with $r=au/d$. Hence

$$
W_QN^2\le
\sum_{d=2}^Q D_Q(d)
 \sum_{\substack{1\le u<d\\(u,d)=1}}|F(u/d)|^2.
                                                               \tag{5}
$$

Apply the analytic large sieve in the form of Schoen, *On a Problem of
Erdős and Sárközy*, Lemma 1, equation (4), printed p. 192:
the sum over reduced fractions of denominator at most $Q$ is at most
$(X+Q^2)N$ for $T\subseteq[1,X]$. Its hypotheses impose no coprimality on
the elements of $T$. Bounding $D_Q(d)$ by $M_Q$ in (5) and dividing by
$N$ proves (1). The cited large sieve is stated without proof in Schoen,
with a reference to Montgomery; its proof is not audited here.

If $p\mid d$ then $D_Q(d)\le D_Q(p)$, proving the first identity in (2).
Also $0\le1-\kappa(a)\le4/a$. Listing the distinct positive integers of
$S$ in increasing order bounds their reciprocal sum by the $m$th harmonic
number. Thus $0\le m-W_Q\le4(1+\log m)$ for $m\ge1$, which proves the
second statement and (3).

This is the same analytic input as
[[../library/integer_sequences/schoen_2001_problem_erdos_sarkozy/theorem|Schoen's pairwise-coprime theorem]],
but with collisions of fractions counted explicitly. For pairwise coprime
$S$, $M_Q\le1$. The proof above also allows the singleton self-inverse
residues permitted by the distinct-elements formulation. It does not
silently impose the source's stronger convention allowing equal larger
summands. All fractions in (4)--(5) are nonzero modulo 1; repeated zero
frequencies would not satisfy the multiplicity bound.

The finite property-P set $\{4,6,8,9\}$ tests the exceptional classes.
For the modulus $a=4$ and $T=\{6,8,9\}$, three residue classes are
occupied and the left side of (4) is 3. This equals
$\kappa(4)|T|^2=3$, whereas replacing $\kappa(4)$ by 1 would demand
9. This local check is an exact calculation, not an infinite counterexample.

## Why removing a common divisor is insufficient

Property P is preserved by dilation and by taking a subset of multiples
of $d$ and dividing by $d$. Thus an arbitrary dilation already shows that
one cannot expect $M_Q=o(m)$ for every property-P set. Even imposing
$\gcd(A)=1$ does not fix the problem.

Let $\mathcal P$ be the primes $p\equiv3\pmod4$ other than 3, and set

$$
A=\{3\}\ \cup\ \{2p^2:p\in\mathcal P\}.              \tag{6}
$$

There are infinitely many such primes by the usual elementary argument:
if only finitely many primes were $3$ modulo 4, the number four times their
product minus one would have a new prime divisor $3$ modulo 4. The set in
(6) has gcd one, since it contains 3 and 98.

For the element 3, any sum of two elements of the tail is 1 modulo 3,
since $2p^2\equiv2\pmod3$. For $a=2p^2$ and distinct larger tail
elements $2q^2,2r^2$, divisibility by $a$ would give
$p\mid q^2+r^2$. Neither $q$ nor $r$ equals $p$, so this would make $-1$
a square modulo $p\equiv3\pmod4$, which is impossible. Therefore (6)
has property P.

All but one of its elements are even. For $Q\ge98$,

$$
M_Q=m-1,\qquad\frac{M_Q}{m}\longrightarrow1.           \tag{7}
$$

Indeed, the prime 2 divides the $m-1$ tail elements; every odd prime
divides at most one member of $S$. This example has a convergent reciprocal
sum, by comparison of $\sum_p1/(2p^2)$ with $\sum_n1/(2n^2)$.
It refutes an automatic multiplicity gain even in the gcd-one setting; it
does not refute the target.

Nor does merely weighting the original moduli remove this obstruction.
For arbitrary nonnegative weights $w_a$, the same proof gives (1) with
$W_Q=\sum_{a\in S}w_a\kappa(a)$ and
$M_Q=\max_p\sum_{a\in S,\ p\mid a}w_a$. In (6), write $U$ for the
total weight of the even elements. Then $M_Q\ge\max(U,w_3)$ and
$W_Q\le U+w_3$, so $W_Q/M_Q\le2$ whenever $M_Q>0$.
There is no growing sieve gain from this weighted first step alone.

## What the optimal weighted gain detects

The qualitative information in this weighting step has a simple exact
description. For a finite $S\subseteq A$, define

$$
 K(S)=\sup_{\substack{w_a\ge0\\\sum_{a\in S}w_a>0}}
 \frac{\sum_{a\in S}\kappa(a)w_a}
      {\max_p\sum_{a\in S,\ p\mid a}w_a},
 \qquad K(\varnothing)=0.                             \tag{W}
$$

The denominator is positive for nonzero weights, since every $a\in A$
is at least 3. The maximum is over primes dividing some member of $S$.
For $S=A\cap[1,Q]$, the weighted proof above gives
$K(S)|A\cap(Q,X]|\le X+Q^2$.

For an infinite set $A$ of integers at least 3, the values
$K(A\cap[1,Q])$ stay bounded as $Q\to\infty$ if and only if some finite
set of primes meets the prime divisors of every element of $A$.
This assertion does not require property P; its use here is a test of
what the one-scale inequality can detect.

Indeed, if a set $F$ of $r$ primes meets every element, then

$$
 \sum_{a\in S}\kappa(a)w_a
 \le\sum_{a\in S}w_a
 \le\sum_{p\in F}\sum_{a\in S,\ p\mid a}w_a
 \le r\max_p\sum_{a\in S,\ p\mid a}w_a.
$$

Thus $K(S)\le r$. Conversely, if no finite prime set meets all elements,
choose successively $a_1,a_2,\ldots\in A$, each avoiding the prime
divisors of its predecessors. They are pairwise coprime. Give the first
$r$ elements weight one and all other elements weight zero. Once $Q$
contains them the denominator in (W) is one, while the numerator is at
least $r/3$. Hence the gain is unbounded.

This dichotomy is not a summability theorem. For a prime $p$, the
normalized set $A_p=\{a/p:a\in A,\ p\mid a\}$ again has property P, and

$$
\sum_{\substack{a\in A\\p\mid a}}\frac1a
=\frac1p\sum_{b\in A_p}\frac1b.                                       \tag{8}
$$

In the finite-prime case, if $\sum_{a\in A}1/a$ diverges, at least one of
the finitely many prime-divisible subseries diverges, so normalization by
that prime preserves divergence and property P. Repeating this observation
need not terminate: the selected subset and prime may change at every
passage. In the other case, the weighted gain itself gives no rate for
$K(A\cap[1,Q])$ and no summable estimate for the dyadic masses;
Proposition R below supplies a rate through residue occupancy instead. A
proof must relate the gain or the successive normalizations to those
actual masses; an unbounded gain or a factor $1/p$ in isolation is
insufficient.

## Residue occupancy beyond a product of moduli

The large sieve in (1) gains only linearly in the weighted gain. Counting
residue classes directly gains exponentially, at the price of working only
beyond the least common multiple of the moduli used.

Let $A$ have property P, let $S\subseteq A$ be finite and nonempty, and put
$s^*=\max S$ and $L=\operatorname{lcm}(S)$. Call a class $t$ modulo $a$
self-inverse when $2t\equiv0\pmod a$; there are $\gcd(a,2)$ of them. Call a
set of classes modulo $L$ admissible for $S$ when its image modulo every
$a\in S$ contains no self-inverse class and no pair $\{t,-t\}$, and let
$\rho^\circ(S)$ be the largest density $|R|/L$ of an admissible set $R$.
Then, for every $X>s^*$,

$$
|A\cap(s^*,X]|\le\sum_{a\in S}\gcd(a,2)+\rho^\circ(S)\,(X+L).          \tag{9}
$$

Indeed, every element of $A$ above $s^*$ is larger than every $a\in S$.
For each $a\in S$, a self-inverse class modulo $a$ holds at most one of
these elements, since two of them would be distinct larger summands with
sum $2t\equiv0\pmod a$. Remove these at most $\sum_a\gcd(a,2)$ elements.
Two remaining elements in classes $t\not\equiv-t$ and $-t$ modulo $a$ would
be distinct forbidden summands, so the remaining elements occupy an
admissible set of classes modulo $L$. Each class holds at most $X/L+1$
integers of $(0,X]$.

When the elements of $S$ are pairwise coprime, the Chinese remainder
theorem places an admissible set inside the product of its images, and an
admissible image modulo $a$ has at most $(a-\gcd(a,2))/2$ classes. Thus

$$
\rho^\circ(S)\le\prod_{a\in S}\frac{a-\gcd(a,2)}{2a}\le2^{-|S|},       \tag{10}
$$

with equality in the first inequality, and at most one element of $S$ is
even. For $k$ pairwise coprime elements, (1) gives a factor of about $1/k$
beyond $Q^2$; (10) gives $2^{-k}$ beyond their product.

A shared prime weakens (10) in the way the example (6) predicts. Let $p$ be
an odd prime and $m_1,\ldots,m_s$ pairwise coprime integers, each coprime
to $p$. Then

$$
\rho^\circ(\{pm_1,\ldots,pm_s\})
=\frac{p-1}{2p}+\frac{\rho^\circ(\{m_1,\ldots,m_s\})}{p}.               \tag{11}
$$

Write $M=m_1\cdots m_s$. For a nonzero class $\sigma$ modulo $p$, let
$U_j$ and $V_j$ be the images modulo $m_j$ of the admissible classes in
the fibres over $\sigma$ and $-\sigma$. A sum of one class from each fibre
is divisible by $p$, so admissibility modulo $pm_j$ makes $U_j$ and $-V_j$
disjoint, and $|U_j|+|V_j|\le m_j$. The two fibres together hold at most
$\prod_j|U_j|+\prod_j|V_j|\le\prod_j(|U_j|+|V_j|)\le M$ of their $2M$
classes; since $p$ is odd, these fibres contain no self-inverse class. In
the fibre over 0, a class $py$ is admissible exactly when $y$ is admissible
for $\{m_1,\ldots,m_s\}$, the self-inverse classes included. This proves
the upper bound in (11). Taking every class
over a set of $(p-1)/2$ residues containing one of each pair
$\{\sigma,-\sigma\}$, together with an optimal set in the fibre over 0,
attains it. For $\{15,21\}$, (11) gives $1/3+(2/5)(3/7)/3=41/105$. That is
close to one half, whereas the product in (10), applied formally to these
two moduli, would give $(14/30)(20/42)<1/4$: the common prime does the work
of both.

## A rate when coprime elements recur

For a nonempty set $A$ of positive integers, define its greedy coprime
sequence by $c_1=\min A$ and
$c_{k+1}=\min\{a\in A:a>c_k,\ \gcd(a,L_k)=1\}$, where
$L_k=c_1\cdots c_k$, for as long as such an element exists. It is increasing
and pairwise coprime; the strict inequality also excludes selecting 1 twice
when the definition is applied to a normalized finite set.

**Proposition R.** Let $A\subseteq\mathbb N_{\ge3}$ have property P and an
infinite greedy coprime sequence. Then, for every $k\ge1$,

$$
\sum_{a\in A\cap(L_k,L_{k+1}]}\frac1a
\le\frac{3+\log c_{k+1}}{2^k}+\frac{2(k+1)}{L_k},
\qquad
\sum_{a\in A}\frac1a\le6+\sum_{k\ge1}\frac{\log c_{k+1}}{2^k}.          \tag{12}
$$

*Proof.* Apply (9) and (10) to $S=\{c_1,\ldots,c_k\}$. Since $L_k\ge c_k$,
the count $N_k(t)=|A\cap(L_k,t]|$ satisfies
$N_k(t)\le k+1+2^{-k}(t+L_k)$ for $t\ge L_k$. Partial summation over
$(L_k,Y]$ gives

$$
\sum_{a\in A\cap(L_k,Y]}\frac1a
=\frac{N_k(Y)}{Y}+\int_{L_k}^{Y}\frac{N_k(t)}{t^2}\,dt
\le\frac{2(k+1)}{L_k}+\frac{3+\log(Y/L_k)}{2^k},
$$

and $Y=L_{k+1}$ gives the first bound. The only element of $A$ in
$[1,L_1]$ is $c_1\ge3$. Moreover $L_k\ge3^k$ and
$\sum_{k\ge1}2(k+1)3^{-k}=5/2$, so summing the first bound over $k$ gives
the second. $\square$

So the unbounded-gain branch of the dichotomy above has an explicit rate.
The reciprocal sum converges when the coprime elements recur often enough
that $\sum_k2^{-k}\log c_{k+1}<\infty$, for instance when
$\log c_{k+1}=O(2^k/k^2)$. A divergent property-P set therefore satisfies
one of two alternatives. Either its greedy coprime sequence stops at some
$c_K$, and every other element shares a prime factor with $L_K$: this is
the finite-prime-cover branch. Or $\log c_{k+1}>2^k/k^2$ for infinitely
many $k$, and for each such $k$ every element of $A$ in $(c_k,c_{k+1})$
has a prime factor dividing $L_k$. The bound (12) leaves room for
divergence only on the ranges $(L_k,L_{k+1}]$ for such $k$.

## Pairwise coprime sets

**Proposition C.** Every pairwise coprime set $C\subseteq\mathbb N_{\ge3}$
with property P has $\sum_{c\in C}1/c<10$.

*Proof.* A composite $c$ is at least the square of its least prime factor,
and pairwise coprime elements have distinct least prime factors. So the
composite elements contribute less than $\sum_p p^{-2}<0.46$. The last
constant follows by summing the primes up to 1000 and bounding the rest by
$\sum_{n>1000}n^{-2}<1/1000$.

Let $q_1<q_2<\cdots$ be the primes in $C$ and $Q_m=q_1\cdots q_m$. They
form a property-P set of odd primes. Apply (10) to $\{q_1,\ldots,q_m\}$.
The only self-inverse class modulo an odd prime is 0, and no prime other
than $q_i$ lies in it, so (9) needs no exceptional elements. Every prime of
$C$ above $q_m$ lies in a set $R_m$ of reduced classes modulo $Q_m$ with
$|R_m|\le\prod_{i\le m}(q_i-1)/2=2^{-m}\varphi(Q_m)$.

For $m\ge1$, the primes of $C$ in $[Q_m^2,Q_{m+1}^2)$ exceed $q_m$, hence
lie in $[u,v)$ with $u=\max(Q_m^2,q_{m+1})$ and $v=Q_m^2q_{m+1}^2$. In
both cases $\log v\le3\log u$. The Brun--Titchmarsh inequality in the form
of Montgomery and Vaughan gives
$\pi(t;q,r)\le2t/(\varphi(q)\log(t/q))$ for $(r,q)=1$ and $t\ge2q$. For $t\ge u\ge Q_m^2$
this is at most $4t/(\varphi(Q_m)\log t)$. Partial summation over each
class of $R_m$ then bounds the contribution of this range by

$$
\frac{4|R_m|}{\varphi(Q_m)}\Bigl(\frac1{\log v}+\log\frac{\log v}{\log u}\Bigr)
\le2^{2-m}\Bigl(\frac1{\log9}+\log3\Bigr)<1.56\cdot2^{2-m}.
$$

The sum over $m\ge1$ is less than $6.23$. The primes of $C$ in
$[q_1,q_1^2)$ contribute at most
$1/q_1+2/\log(q_1^2)+2\log2<2.64$, by the same inequality with modulus 1.
For a finite prime list, stop after the range containing its last prime;
a one-prime list uses just the initial range, and an empty list costs zero.
These ranges cover every prime of $C$, so the primes contribute less than
$8.87$ and $\sum_{c\in C}1/c<9.33$. $\square$

The composite part uses no property of $C$; property P enters only through
(10) for the primes. The pairwise coprime class is the one in which
[[problems/integer_sequences/E0012/claims/2001_04_01_schoen|Schoen]] and
[[problems/integer_sequences/E0012/claims/2004_10_08_baier|Baier]] bound the
counting function along a sequence of $N$. Proposition C answers the
reciprocal-sum question inside that class. It is author-recorded, its
Brun--Titchmarsh input is used at its published statement, and it was not
compared with literature beyond the sources this lead cites.

The same argument works inside admissible classes, with a discount.

**Proposition C′.** Let $m_1,\ldots,m_k\ge3$ be pairwise coprime with
product $L$, where $k\ge1$. Let $C$ be a pairwise coprime property-P set
whose elements exceed $L$ and lie in classes admissible for
$\{m_1,\ldots,m_k\}$. Then $\sum_{c\in C}1/c<22\cdot2^{-k/2}$.

*Proof.* A composite $c>L$ satisfies $1/c\le\min(1/L,1/p_c^2)$, where
$p_c$ is its least prime factor, and these primes are distinct. So the
composite elements contribute at most
$\pi(\sqrt L)/L+\sum_{n>\sqrt L}n^{-2}\le3/\sqrt L\le3\cdot2^{-k/2}$.
A prime above $L$ is a unit modulo each $m_i$, and no unit is self-inverse
modulo $m_i\ge3$, so an admissible set of units modulo $m_i$ has at most
$\varphi(m_i)/2$ classes.

For the primes of $C$ in $(L,L^2]$, let $L'$ be the product of the
$\lfloor k/2\rfloor$ smallest moduli, so $L'\le L^{1/2}$. The primes lie
in at most $2^{-\lfloor k/2\rfloor}\varphi(L')$ classes modulo $L'$, and for
$t\ge L\ge L'^2$ the Brun--Titchmarsh inequality gives
$\pi(t;L',r)\le4t/(\varphi(L')\log t)$. Partial summation bounds their
contribution by
$2^{2-\lfloor k/2\rfloor}(1/\log(L^2)+\log2)<6.5\cdot2^{-k/2}$.

For the primes above $L^2$, let $q_1<q_2<\cdots$ be the primes of $C$, put
$Q_0=1$ and $Q_m=q_1\cdots q_m$, and split at the points $L^2Q_m^2$. The
primes in $[L^2Q_m^2,L^2Q_{m+1}^2)$ are at least $q_{m+1}$. By (9) and
(10) inside $C$, together with the admissible classes modulo $L$, they lie
in at most $2^{-k-m}\varphi(LQ_m)$ reduced classes modulo $LQ_m$. The
argument of Proposition C, with $LQ_m$ in place of $Q_m$, bounds this range
by $1.56\cdot2^{2-k-m}$, and the sum over $m\ge0$ by
$12.5\cdot2^{-k}$. Adding the three parts gives the bound. $\square$

## Shared primes

Proposition C extends from pairwise coprime sets to all property-P sets,
at the cost of a factor depending only on the primes that two elements
share.

**Proposition S.** Let $A\subseteq\mathbb N_{\ge3}$ have property P, and
let $P_2$ be the set of primes dividing at least two elements of $A$. Write
each $a\in A$ as $a=s(a)r(a)$, where $s(a)$ is the largest divisor of $a$
composed of primes in $P_2$, and put $\mathcal S=\{s(a):a\in A\}$. Then

$$
\sum_{a\in A}\frac1a\le9.33\sum_{s\in\mathcal S}\frac1s
\le9.33\prod_{p\in P_2}\frac{p}{p-1}.                                \tag{13}
$$

*Proof.* A prime dividing $r(a)$ and $r(b)$ for $a\ne b$ would divide
two elements, hence lie in $P_2$, which no prime factor of $r(a)$ does. So
the parts $r(a)$ are pairwise coprime. For $s\in\mathcal S$ let
$A_s=\{a\in A:s(a)=s\}$ and $R_s=\{a/s:a\in A_s\}$. Dividing every
element of a subset of $A$ by a common divisor preserves property P, so
$R_s$ is a pairwise coprime property-P set, and
$\sum_{a\in A_s}1/a=s^{-1}\sum_{r\in R_s}1/r$. If $1\in R_s$, then $R_s$
has at most one other element, since 1 divides every sum. If $2\in R_s$
and $1\notin R_s$, then $R_s$ has at most one odd element above 2 and, being
pairwise coprime, no other even one. In both cases
$\sum_{r\in R_s}1/r\le3/2$. Otherwise $R_s\subseteq\mathbb N_{\ge3}$ and
Proposition C gives $\sum_{r\in R_s}1/r<9.33$. Summing over $s$ gives the
first inequality, interpreted in the extended nonnegative reals; it is
strict for nonempty $A$ when the right side is finite. The elements of
$\mathcal S$ are distinct integers
composed of primes in $P_2$, which gives the second. $\square$

Three consequences follow. If no prime above $G$ divides two elements, in
particular if every two elements have greatest common divisor at most $G$,
then $\sum_{a\in A}1/a<9.33\prod_{p\le G}p/(p-1)$.
The example (6) has $P_2=\{2\}$, so (13) bounds its
reciprocal sum by $18.66$. Applied to the truncations $A\cap[1,X]$, (13)
shows that a divergent property-P set has
$\sum_{p\in P_2}1/p=\infty$: infinitely many primes are shared, with
divergent reciprocal sum. Finally, the prime elements of any property-P set
form a pairwise coprime property-P set, so they contribute less than $8.87$
by the proof of Proposition C.

The bound (13) is far from sharp. It charges every shared part $s$ with a
full pairwise coprime set, whereas property P also limits how the sets
$sR_s$ for different $s$ coexist; that interaction is the same unresolved
question as below.

## The remaining multiscale obligation

Write $h(B)=\sum_{b\in B}1/b$ and
$u_j=2^{-j}|A\cap[2^j,2^{j+1})|$. The
[[research/property_p_reciprocal_sum/_index|dyadic criterion]] says that the
question is exactly whether $\sum_j u_j$ converges. The supported links
compose as follows. The weighted sieve detects a finite prime cover; the
occupancy bound supplies an exponential saving after the product scale;
Proposition R integrates that saving when its explicit recurrence condition
holds; and Propositions C and S handle coprime sets and controlled shared
primes. What remains is a bound on the mass accumulated through arbitrary
normalizations and through the scales preceding the occupancy estimate.
Corollary H below bounds the mass of $A\cap[1,N]$ by $O(\log\log N)$; the
target is to remove that doubly logarithmic growth. The subsection "The
whole argument and its open step" below is the canonical sketch of the
current route, with its one missing estimate and the reasons it is open.

One proposed induction statement is still open:

> **(H)** There are constants $K<\infty$ and $0<\lambda<1$ such that, for
> every $k\ge0$, all pairwise coprime $m_1,\ldots,m_k\ge3$ with product
> $L$, and every finite property-P set $B\subseteq\mathbb N_{\ge3}$ above
> $L$ occupying admissible classes for these moduli, $h(B)\le K\lambda^k$.

Its $k=0$ case is the uniform finite-set assertion

$$
\sup\{h(B):B\subseteq\mathbb N_{\ge3}\text{ finite with property P}\}
<\infty.                                                        \tag{U}
$$

This would imply E12(iii) by truncation and monotone convergence.
Proposition E below proves the converse: unbounded finite examples can be
glued into one infinite property-P set with divergent reciprocal sum. So
(U) is equivalent to E12(iii). Neither (H) nor (U) follows from the results
above. Proposition C′ supplies (H) only when $B$ is itself pairwise
coprime.

### Gluing finite sets into one infinite set

**Lemma E1.** Let $L\ge1$ and let $B$ be a finite property-P set of positive
integers. There is a finite property-P set $C$ whose elements are all
congruent to 1 modulo $L$, with $h(C)\ge h(B)/L^2$.

*Proof.* For $y\in B$ let $g(y)$ be its largest divisor composed of primes
dividing $L$. For each occurring $g$, divide the corresponding part of $B$
by $g$ and call the quotient $B_g$. It has property P, its elements are
coprime to $L$, and

$$
h(B)=\sum_g\frac{h(B_g)}g,\qquad
\sum_{\substack{g\ge1\\p\mid g\Rightarrow p\mid L}}\frac1g
=\prod_{p\mid L}(1-1/p)^{-1}=\frac{L}{\varphi(L)}.
$$

Thus some $C'=B_g$ has $h(C')\ge\varphi(L)h(B)/L$. The empty set is
immediate, and for nonempty $B$ this follows by bounding each $h(B_g)$ by
their finite maximum in the displayed identity.

The elements of $C'$ lie in the $\varphi(L)$ reduced classes modulo $L$,
so some reduced class $r$ holds a subset $C''$ with
$h(C'')\ge h(C')/\varphi(L)$. Choose $1\le u\le L$ with $ur\equiv1\pmod L$
and put $C=uC''$. Subsets and dilations of property-P sets have property
P, every element of $C$ is congruent to 1 modulo $L$, and
$h(C)=h(C'')/u\ge h(C'')/L\ge h(B)/L^2$. $\square$

This normalization keeps the full reciprocal Euler factor: the smooth
parts have weights $1/g$, and their sum is exactly $L/\varphi(L)$.
The quotient can contain 1 or 2; neither is discarded. For $L\ge2$ the
constant can be sharpened to $h(C)\ge2h(B)/L^2$ by maximizing jointly over
$g$ and the reduced class. Indeed, the inverses $u$ permute the reduced
residues in $[1,L]$, whose sum is $L\varphi(L)/2$, and
$h(B)=\sum_{g,r}(u(r)/g)h(u(r)B_{g,r})$, where $B_{g,r}$ is the
$r$-class of $B_g$. The coefficients in that sum
are bounded in total by $L^2/2$.

**Proposition E.** Suppose that finite property-P sets have unbounded
reciprocal sums. Then there is an infinite property-P set
$A\subseteq\mathbb N_{\ge3}$ with $\sum_{a\in A}1/a=\infty$.

*Proof.* Build finite blocks $E_1,E_2,\ldots$ in turn. Before building
$E_k$, let $L_k$ be the least common multiple and $M_k$ the largest element
of $E_1\cup\cdots\cup E_{k-1}$, with $L_1=1$ and $M_1=0$. Choose an
integer $D_k\ge3$ with $D_k\equiv1\pmod{L_k}$ and $D_k>M_k$. By
hypothesis there is a finite property-P set $B$ with
$h(B)\ge D_kL_k^2$. Lemma E1 turns it into a property-P
set $C_k$, with every element congruent to 1 modulo $L_k$ and
$h(C_k)\ge D_k$. Put $E_k=D_kC_k$. Then $E_k$ has property P, its
elements are congruent to 1 modulo $L_k$, they exceed $M_k$ and are at
least 3, and $h(E_k)\ge1$.

Let $A=\bigcup_kE_k$. Every element of $E_k$ exceeds every element of an
earlier block, so $A$ is infinite and $h(A)=\sum_kh(E_k)=\infty$. Let
$a<b,c$ be elements of $A$ with $b\ne c$, and let $a\in E_j$. Then $b$
and $c$ lie in blocks $E_k$ with $k\ge j$. There are three cases.

- If $b,c\in E_j$, then $a\nmid b+c$ because $E_j$ has property P.
- If $b\in E_j$ and $c\in E_l$ with $l>j$, then $a\mid L_l$, so
  $c\equiv1\pmod a$. A relation $a\mid b+c$ would give $a\mid b+1$. But
  $D_j$ divides both $a$ and $b$, so it would divide 1, which is false.
  The same holds with $b$ and $c$ exchanged.
- If $b\in E_k$ and $c\in E_l$ with $j<k\le l$, then $a$ divides $L_k$
  and $L_l$, so $b+c\equiv2\pmod a$. Since $a\ge3$, $a\nmid b+c$.

Thus $A$ has property P. $\square$

Consequently the following are equivalent: every infinite property-P set
has a convergent reciprocal sum; the assertion (U); and, for any one fixed
$L\ge1$, a uniform bound on $h(C)$ over the finite property-P sets $C$
contained in the class $1\bmod L$. The first implies the second by
Proposition E. The second implies the first by truncation, and the third
trivially. The third implies the second by Lemma E1. Elements 1 and 2
change none of these bounds by more than $3/2$, so it does not matter
whether they are admitted. In particular Erdős and Sárközy's two
statements, convergence for each set and a bound by one absolute
constant, are equivalent.

The gluing uses congruence blocks: block $k$ needs mass at least
$D_kL_k^2$ before restriction, which grows without bound. It therefore
turns the infinite question into the finite
one without supplying the finite examples.

The class form changes the local interaction. If every element is
congruent to 1 modulo $L$ and $a\mid b+c$ with $b,c>a$, then
$b+c=ta$ with $t\equiv2\pmod L$ and $t\ge3$, so $t\ge L+2$. Elements whose
sums stay below $(L+2)a$ never interact with $a$. Choosing $L$ divisible
by every prime up to $y$ also removes every prime up to $y$ from the
elements. The finite question therefore needs to be solved only for sets
without small prime factors and with interaction ratio at least
$(L+2)/2$. This reduction does not bound the masses of such sets.

The convention allowing equal larger summands can also be reached by an
explicit reduction. Call a set *primitive* if no two distinct elements
divide one another. Write $M_N$ for the largest reciprocal sum of any
property-P subset of $\{1,\ldots,N\}$, and let $P_N$ be the corresponding
maximum over odd primitive property-P sets, with a singleton 1 allowed.
Then

$$
P_N\le M_N\le3P_N.                                      \tag{O}
$$

Indeed, let $B\subseteq\{1,\ldots,N\}$ be any property-P set and let $C$
be its elements minimal under divisibility. Every $b\in B\setminus C$
has a proper divisor in $C$; assign it to one such divisor $c$. No $c$
receives two elements, since it would divide their sum and both would
exceed $c$. The assigned element is at least $2c$, so
$h(B\setminus C)\le h(C)/2$. The set $C$ is primitive. For each $k\ge0$,
divide the elements of $C$ of exact 2-adic valuation $k$ by $2^k$, obtaining
an odd primitive property-P set $C_k\subseteq\{1,\ldots,N\}$. Thus

$$
h(B)\le\tfrac32 h(C)
=\tfrac32\sum_{k\ge0}2^{-k}h(C_k)
\le3P_N.
$$

For odd primitive sets, $a\mid2b$ with $a<b$ would imply $a\mid b$,
which is impossible. They therefore satisfy the stronger version of P
that also forbids equal larger summands. A uniform bound on this subclass
would prove (U) and hence the full infinite conclusion. In the signed
identity below its early/late pair sums have no diagonal exceptions:
$\sum_{d\mid a}\sigma_d=aP_a(T)=0$. This removes the diagonal error only
after the reduction (O); it does not remove denominator multiplicities or
give a uniform bound on the remaining signed sum.

### Large elements do not reduce the problem to one interval

Put $\mu(Y)=\sup\{h(B):B$ a finite property-P set with $\min B>Y\}$. Since
$h(B)\le\sum_{n\le Y}1/n+h(B\cap(Y,\infty))$, (U) holds if and only if
$\mu(Y)<\infty$ for one $Y$, and then for every $Y$. Taking intervals
$(X,3X/2)$ with $X\to\infty$ gives $\mu(Y)\ge\log(3/2)$. A tempting
sharper target, that
$\mu(Y)\to\log(3/2)$ as for the cardinality version of the problem, is
false.

Let $B'$ be a finite property-P set, $Z\ge3\max B'$, and

$$
C_Z=\{n:Z<n\le5Z/2,\ n\equiv1\pmod3\}.
$$

Then $3B'\cup C_Z$ has property P. In $C_Z$ a relation $b+c=ta$ forces
$t\equiv2\pmod3$, so $t\ge5$, whereas $b+c<5Z<5a$. For $a\in3B'$ and
$b,c\in C_Z$, $b+c\equiv2\pmod3$ while $3\mid a$. For $a,b\in3B'$ and
$c\in C_Z$, $b+c\equiv1\pmod3$. Triples inside $3B'$ are excluded by
dilation. As $Z\to\infty$, $h(C_Z)\to\log(5/2)/3$. Taking $\min B'>Y/3$,
then letting $Z\to\infty$ and taking the supremum over $B'$, gives
$\mu(Y)\ge\mu(Y/3)/3+\log(5/2)/3$. Since $\mu$ is nonincreasing,
$\mu(Y)\ge\log(5/2)/2>\log(3/2)$ for every $Y$; the conclusion is
immediate when $\mu(Y)=\infty$, and follows by rearrangement otherwise.

The same argument gives a recursion for classes. If every element of $B'$
is $1\bmod L$, $q$ is an odd prime with $q\equiv1\pmod L$, and $C$ is a
property-P set above $q\max B'$ inside the class $1\bmod Lq$, then $qB'\cup
C$ is a property-P set inside $1\bmod L$. The window
$\{n:Z<n\le(L+2)Z/2,\ n\equiv1\pmod L\}$ supplies mass about
$\log((L+2)/2)/L$; for the upper windows in that recursion, replace $L$
by $Lq$. For one fixed $q$, iterating the lower branch of
$qB'\cup C$ multiplies each inherited mass by $1/q$. If each new upper
window has limiting mass $w$, the limiting total contribution after $k$
iterations is $w\sum_{j<k}q^{-j}<wq/(q-1)$; the initial mass has coefficient
$q^{-k}$. This geometric calculation controls that particular recursion.
It does not bound arbitrary mixtures of guard primes or the independent
windows at different class moduli. These constructions show structures
that a proof of (U) must accommodate; they do not decide (U).

### Early elements need biased smooth guards

The following proposition shows that, apart from a small mass, an early
element can coexist with a heavy late part only through a divisor with
small prime factors modulo which the late part is biased. It turns the
informal guard primes of the constructions above into a proved dichotomy.

Fix $N$ and let $M$ be the largest reciprocal sum of a property-P subset of
$\{1,\ldots,N\}$. Let $B\subseteq\{1,\ldots,N\}$ have property P, let
$Q\ge2$ and $K\ge2$, and take an early part $E\subseteq B\cap[3,Q]$ and the
late part $L=B\cap(KQ,N]$. Weight $b\in L$ by $c_b=2^{-j}$ when
$2^j<b\le2^{j+1}$, so that $1/b\le c_b\le2/b$. Put $m=\sum_{b\in L}c_b$, let
$J$ be the number of $j$ for which $L$ meets $(2^j,2^{j+1}]$, and for
$g\ge1$ put

$$
P_g=\sum_{\substack{b,c\in L\\ g\mid b+c}}c_bc_c,
$$

the sum over ordered pairs, $b=c$ included. Thus $P_1=m^2$, while a
late part spread evenly over the classes modulo $g$ has $gP_g$ close to
$m^2$. For an integer $D\ge1$ let
$\ell_D=\operatorname{lcm}(1,\ldots,D)$, and for $a\in E$ put
$g_a=\gcd(a,\ell_D)$. Call $a$ *guarded* if
$g_aP_{g_a}<m^2/2$, and *free* otherwise. Elements without prime factors
up to $D$ have $g_a=1$, so they are free.

**Proposition F.** If $L$ is nonempty and $K\ge4/m$, the free elements
$F\subseteq E$ satisfy

$$
h(F)\le\frac{3M}{m}\Bigl(\frac{32}{K}+\frac{4J}{D}\Bigr).
$$

*Proof.* Put $G(\theta)=\sum_{b\in L}c_be(b\theta)$, where
$e(x)=e^{2\pi ix}$, and for $d\ge1$ let
$\sigma_d=\sum_{1\le u\le d,\,(u,d)=1}G(u/d)^2$. Pairing $u$ with $d-u$
shows that $\sigma_d$ is real, and $\sigma_1=m^2$. For every $n\ge1$,
grouping the fractions $h/n$ by their reduced denominators gives

$$
\sum_{d\mid n}\sigma_d=\sum_{h=0}^{n-1}G(h/n)^2
=n\sum_{\substack{b,c\in L\\ n\mid b+c}}c_bc_c=nP_n.
$$

Let $a\in E$. Every element of $L$ exceeds $a$, so property P leaves only
the pairs $b=c$ with $a\mid2b$ in $P_a$. Such $b$ lie in the at most two
self-inverse classes modulo $a$, and each class holds at most one element
of $L$, since two would have sum divisible by $a$. Each such $b$ has
$c_b\le2/b<2/(Ka)$, so $\eta_a:=aP_a<8/(K^2a)$. The divisors of $a$ that
divide $\ell_D$ are
exactly the divisors of $g_a$. Hence

$$
S_a:=\sum_{\substack{d\mid a\\ d\nmid\ell_D}}\sigma_d=\eta_a-g_aP_{g_a}.
$$

For a free $a$ this gives $|S_a|\ge m^2/2-8/(3K^2)\ge m^2/3$, using $a\ge3$
and $K\ge4/m$. A divisor $d$ of $a$ that does not divide $\ell_D$ has a
prime power factor larger than $D$, so $D<d\le Q$. Dividing the elements of
$B$ divisible by $d$ by $d$ leaves a property-P subset of
$\{1,\ldots,N\}$, so $\lambda_d:=\sum_{a\in F,\,d\mid a}1/a\le M/d$.
Therefore

$$
\frac{m^2}{3}\,h(F)\le\sum_{a\in F}\frac{|S_a|}{a}
\le\sum_{D<d\le Q}\lambda_d|\sigma_d|
\le M\,W,\qquad
W=\sum_{D<d\le Q}\frac1d\sum_{(u,d)=1}|G(u/d)|^2.
$$

Write $L_j=L\cap(2^j,2^{j+1}]$, $n_j=|L_j|$, $\delta_j=2^{-j}n_j$ and
$G_j=2^{-j}S_{L_j}$, where $S_{L_j}$ is the exponential sum of $L_j$. Then
$m=\sum_j\delta_j$. Split $(D,Q]$ into ranges $(D_i,2D_i]$ with
$D_i=2^iD<Q$, and apply the large sieve in the form of Schoen's Lemma 1,
equation (4), cited above, with modulus bound $2D_i$ and $L_j\subseteq
[1,2^{j+1}]$. This gives

$$
\sum_{D<d\le Q}\frac1d\sum_{(u,d)=1}|G_j(u/d)|^2
\le4^{-j}n_j\sum_i\Bigl(4D_i+\frac{2^{j+1}}{D_i}\Bigr)
\le\delta_j\Bigl(\frac{8Q}{2^j}+\frac4D\Bigr).
$$

The form $W$ is a weighted sum of squares, so the triangle inequality and
the Cauchy--Schwarz inequality give
$W\le(\sum_jW(G_j)^{1/2})^2\le m\sum_j(8Q2^{-j}+4/D)$, the last sum over
the $J$ indices with $L_j$ nonempty. Those indices have $2^{j+1}>KQ$, so
$\sum_j8Q2^{-j}\le32/K$. Hence $W\le m(32/K+4J/D)$, and the bound
follows. $\square$

The proposition uses property P through the early elements' relation to
$L$ and through the normalized sets behind $\lambda_d\le M/d$, and the
large sieve only through the cited statement. Choosing $D$
a large multiple of $J$, which is at most $\log_2N+1$, and $K$ large makes
the free mass small whenever $m$ is a fixed fraction of $M$.

Without small prime factors there are no guards, and the bound closes.

**Corollary R.** Let $N\ge3$ and $D\ge8(\log_2N+1)$. Every property-P
subset of $\{1,\ldots,N\}$ whose elements have no prime factor at most $D$
has reciprocal sum at most 30.

*Proof.* Let $M_R$ be the largest reciprocal sum of such a set; dividing
the multiples of $d$ in one of them by $d$ gives another, possibly
containing 1. So the proof of Proposition F holds with $M_R$ in place of
$M$ for subsets $E$ of such a set. Suppose $M_R>30$ and take a set $B$
attaining it. It does not contain 1, since a property-P set containing 1
has at most two elements, so its elements exceed $D\ge16$. Let $Q$ be the
least element of $B$ with $h(B\cap[1,Q])\ge M_R/2$, put $E=B\cap[1,Q]$,
$K=64$ and $L=B\cap(KQ,N]$. Then $h(E)\le M_R/2+1/17$, the gap
$(Q,KQ]$ carries at most $\log64<4.16$, and so
$m\ge h(L)\ge M_R/2-4.22\ge M_R/4$, with $m>10$ and hence $K\ge4/m$. Every
element of $E$ has $g_a=1$ and is free. The number $J$ of dyadic ranges is
at most $\log_2N+1\le D/8$, so Proposition F gives
$h(E)\le(3M_R/m)(1/2+1/2)\le12$, contradicting $h(E)\ge M_R/2>15$.
$\square$

The cutoff $D$ depends on $N$. A general set may use primes up to that
cutoff as guards, so this corollary does not give (U).

If Corollary R held with $D$ a constant independent of $N$, Lemma E1 with
$L=\operatorname{lcm}(1,\ldots,D)$ would give (U), since every element of
a set in the class $1\bmod L$ has no prime factor up to $D$. The
dependence on $N$ enters only through the term $4J/D$, which comes from
the triangle inequality across the $J$ dyadic ranges of $L$. That loss is
real for the large sieve alone: a late part lying in one nonzero class
modulo a prime $q$ with $D<q\le Q$ has $|G(u/q)|=m$ for every $u$, so
$W\ge(1-1/q)m^2$, while $m\le J/q+O(2^{-j_0})$ with $2^{j_0}$ the
smallest range. One way to control this coherence would be to show that
property-P sets confined to one class modulo $q$ across many ranges carry
mass tending to 0 as $q$ grows, a quantitative class form of (U). Such an
estimate must retain the lower size cutoff:
here every late element exceeds $KQ\ge Kq$. A bound such as
$h(C)\le C_0(1+\log q)/q$ for all unit classes with no size cutoff is
false, since the class $1\bmod q$ contains the property-P singleton
$\{1\}$. Even excluding 1 and 2 leaves the same problem for a fixed
singleton in a unit class. With the required size restriction the
quantitative class bound is unproved. It and the rough-set bound would
have to be proved together.

Consequently a nearly extremal set with large $M$ has the following shape.
Cut it where the early mass first reaches about $M/2$, leave a gap of
ratio $K$, whose mass is at most $\log K+1$, and keep the rest as $L$. Then
almost all early mass is guarded: it sits on elements $a$ whose part
$g_a$ composed of prime powers at most $D$ is a modulus modulo which the
late part has less than half of its expected number of pair sums divisible
by $g_a$. In the example $3B'\cup C_Z$ the guard is $3$ and $P_3=0$.

To finish a proof of (U) along this line it would suffice to prove a
guard accounting: for some $\theta<1/2$ and constant $C_0$, whenever $m$ is
at least a fixed fraction of $M$, the guarded early mass is at most
$\theta M+C_0$. Then the cut above would give $M/2\le\theta M+C_0+O(1)$, a
bound on $M$ independent of $N$. The obvious charge, $M/\gamma$ for the
multiples of each minimal guard $\gamma$, is the sibling charge that the
families below defeat: their sum over many guards is unbounded. A correct
charge must also use that each guard costs the late part, which is biased
modulo every guard at once, and that early multiples of different guards
constrain one another: in (16) many guards share one window whose total
mass is at most $\log(3/2)$. This guard accounting is not proved here.

An idealized model shows why such an accounting is plausible and where it
must work. Split the set into windows of ratio $K$ separated by gaps of
ratio $K$; the odd-numbered and even-numbered windows each form such a
family, so this costs a factor 2. Suppose every element of a window is a
multiple of one of its guard primes, every later element avoids the class
0 and lies in a fixed half of the nonzero classes modulo each earlier guard
prime, and integers in a window are counted by class density. Let $x_i$ be
the density left after the guards of the first $i$ windows and
$\Pi_{i+1}=\prod(1-1/p)$ over the guards of window $i+1$. That window has
mass at most $x_i(1-\Pi_{i+1})\log K$, while
$x_{i+1}\le x_i\Pi_{i+1}/2$. Hence
$x_i(1-\Pi_{i+1})\le x_i-2x_{i+1}$, and the window masses of each family
telescope to at most $\log K$. Real sets leave this model in three places.
Guards need only be biased, not perfect. Guards may be composite smooth
numbers, so later multiples of a guard survive in its zero class, as in
$3B'\cup C_Z$. And the windows lie far below the least common multiple of
the guards, where class densities do not count integers. A guard
accounting must handle all three.

After Proposition E the whole question is the finite assertion (U). A proof
must bound $h(B)$ uniformly over finite property-P sets, and its charge
must pay for the guarded recursions above, in which a dilated copy below a
guard prime coexists with a long window in one class above it. A negative
answer needs finite property-P sets of unbounded reciprocal sum, in any one
class $1\bmod L$; Proposition E then supplies the infinite set. Every
explicit construction recorded here pays a factor $1/q$ for each guarded
lower copy and passes the rest to a finer class, so none has unbounded mass.

Explicit normalization potentials fail below. Their failure does not
refute (H), (U), or convergence, and does not rule out potentials retaining
more information about scale and residues.

### A doubly logarithmic bound

Corollary R already bounds every finite property-P set by a doubly
logarithmic quantity, through the smooth-part normalization of Lemma E1.
For $N\ge3$ and $D\ge1$ let $R_N(D)$ be the largest reciprocal sum of a
property-P subset of $\{1,\ldots,N\}$ whose elements have no prime factor at
most $D$; thus $R_N(1)$ is the quantity $M_N$ of the signed criterion below.
Put

$$
\Delta_N=\lceil8(\log_2N+1)\rceil,\qquad
\Pi(D,\Delta)=\prod_{D<p\le\Delta}\Bigl(1-\frac1p\Bigr)^{-1},\qquad
\delta_\Delta=\prod_{p\le\Delta}\Bigl(1-\frac1p\Bigr),
$$

with an empty product equal to 1.

**Corollary H.** For $N\ge3$ and every $D\ge1$,
$R_N(D)\le30\,\Pi(D,\Delta_N)$. In particular every property-P subset of
$\{1,\ldots,N\}$ has reciprocal sum at most

$$
\frac{30}{\delta_{\Delta_N}}\le1440\log\Delta_N .
$$

Consequently every infinite property-P set $A$ satisfies
$\sum_{a\in A,\ a\le N}1/a=O(\log\log N)$, and

$$
\sum_{a\in A}\frac1{a(\log\log a)^{1+\varepsilon}}<\infty
\qquad(\varepsilon>0).
$$

*Proof.* Write $\Delta=\Delta_N$ and let $B$ be a property-P subset of
$\{1,\ldots,N\}$ with no prime factor at most $D$. For $b\in B$ let $g(b)$
be its $\Delta$-smooth part, the largest divisor of $b$ composed of primes
at most $\Delta$. It is composed of primes in $(D,\Delta]$. For each
occurring $g$, the elements with $g(b)=g$, divided by $g$, form a
property-P subset $G_g$ of $\{1,\ldots,N\}$ with no prime factor at most
$\Delta$; it may contain 1. Corollary R applies to $G_g$, since
$\Delta\ge8(\log_2N+1)$, and gives $h(G_g)\le30$. Hence

$$
h(B)=\sum_g\frac{h(G_g)}g
\le30\sum_{\substack{g\ge1\\p\mid g\Rightarrow D<p\le\Delta}}\frac1g
=30\,\Pi(D,\Delta).
$$

With $D=1$ the product is $1/\delta_\Delta$. For the explicit bound, let
$x\ge2$, $n=\lfloor x\rfloor$ and
$S(x)=\sum_{p\le x}(\log p)/p$. Counting prime factors in $n!$ gives
$\log n!\ge nS(x)-\theta(n)$, where
$\theta(n)=\sum_{p\le n}\log p<n\log4$. For the latter elementary
bound, put $P(n)=\prod_{p\le n}p$. The primes in $(m,2m]$ divide
$\binom{2m}{m}$, and those in $(m+1,2m+1]$ divide
$\binom{2m+1}{m}$. Hence

$$
P(2m)\le P(m)\binom{2m}{m},\qquad
P(2m+1)\le P(m+1)\binom{2m+1}{m}.
$$

Both binomial coefficients are less than $4^m$ for $m\ge1$; for the
odd case the two equal central coefficients together are less than
$2^{2m+1}$. Induction from $P(1)=1$ gives $P(n)<4^n$.
Since $\log n!\le n\log n$, it follows that
$S(x)\le\log x+\log4$. Partial summation gives

$$
\sum_{p\le x}\frac1p
=\frac{S(x)}{\log x}+\int_2^x\frac{S(t)}{t\log^2t}\,dt
\le\log\log x+3-\log\log2<\log\log x+3.37 .
$$

Since $-\log(1-1/p)\le1/p+1/(2p(p-1))$ and
$\sum_{n\ge2}1/(n(n-1))=1$, the product $1/\delta_x$ is at most
$e^{3.87}\log x<48\log x$. With $x=\Delta_N$ this gives
$1440\log\Delta_N$.

For an infinite $A$, apply the bound to $A\cap[1,N]$; $\Delta_N$ is
$O(\log N)$. With $S_A(x)=\sum_{a\in A,\,a\le x}1/a\le C\log\log x$ for
large $x$ and $f(x)=(\log\log x)^{1+\varepsilon}$, partial summation
writes the tail of the displayed series as $S_A/f$ at the endpoints plus
$\int S_Af'/f^2\,dx$. The integrand is at most
$C(1+\varepsilon)/(x\log x(\log\log x)^{1+\varepsilon})$, which is
integrable, and $S_A/f\to0$. The elements of $A$ are at least 3, so
$\log\log a>0$. $\square$

Mertens' product theorem, $1/\delta_x\sim e^\gamma\log x$, recorded in
[[../library/primes/granville_1995_harald_cramer_distribution_prime_numbers/_index|Granville's survey, equation (1), printed p. 13]],
improves the constant to
$(30e^\gamma+o(1))\log\log N$; it is not needed for the order of growth. It
also shows that $R_N(D)$ is bounded by a constant depending only on $c$ when
$D\ge(\log N)^c$ for a fixed $c>0$, since
$\limsup_{N\to\infty}\Pi(D,\Delta_N)\le\max(1,1/c)$. This
extends Corollary R from $D\gg\log N$ to every fixed power of $\log N$.

The density-zero theorem alone gives
$\sum_{a\le N}1/a=o(\log N)$ for an infinite property-P set.
Corollary H does not prove (U).

The same decomposition locates the loss, once the element 1 is separated.
For $\Delta\ge2$ let $R^*_N(\Delta)$ be the largest reciprocal sum of a
property-P subset of $\{2,\ldots,N\}$ with no prime factor at most
$\Delta$, and $S_N(\Delta)$ that of a property-P subset of $\{1,\ldots,N\}$
composed of primes at most $\Delta$. In the proof above, $1\in G_g$ exactly
when $g\in B$, and then $G_g$ has at most one other element, which exceeds
$\Delta$; a property-P set containing 1 has at most one larger element.
Hence, for every property-P subset $B$ of $\{1,\ldots,N\}$ and every
$\Delta\ge2$,

$$
h(B)\le\Bigl(1+\frac1\Delta\Bigr)h(B_{\rm sm})+\frac{R^*_N(\Delta)}{\delta_\Delta},
$$

where $B_{\rm sm}$ is the set of $\Delta$-smooth elements of $B$. For
fixed $\Delta$, the $\Delta$-rough integers in $(X,3X/2)$ form a property-P
set of reciprocal sum tending to $\delta_\Delta\log(3/2)$ as
$X\to\infty$, by periodic counting. Thus a bound uniform in $N$ cannot
be smaller than that order for fixed $\Delta$. A proposed bound at growing
cutoffs is

> **(RS)** Put $\Delta'_N=\max(\Delta_N,\lceil(\log N)^2\rceil)$.
> There is an absolute constant $C$ such that
> $R^*_N(\Delta'_N)\le C\,\delta_{\Delta'_N}$ for every $N\ge3$.

This would bound rough property-P mass by the density scale of a bounded
number of automatic windows. Rough sets have no guards composed of primes
at most $\Delta$; larger guard primes remain possible. Even so, (RS) would
not by itself give (U) through the displayed split. For $\Delta\ge3$,
Rankin's inequality with $\alpha=1/(2\log\Delta)$ gives

$$
\sum_{\substack{g>\Delta^u\\p\mid g\Rightarrow p\le\Delta}}\frac1g
\le e^{-u/2}\prod_{p\le\Delta}(1-p^{-1+\alpha})^{-1}
\ll e^{-u/2}\log\Delta.
$$

For the last bound, the logarithm of the ratio of this Euler product to
$1/\delta_\Delta$ is at most an absolute constant times
$\alpha\sum_{p\le\Delta}(\log p)/p$, which is bounded by the estimate for
$S(x)$ in the proof of Corollary H. Taking
$u=4\log\log\Delta+C_0$ with a sufficiently large absolute $C_0$ bounds
the displayed tail by 1. Thus the smooth part reduces to $M_Y+1$ with
$Y=\lfloor\Delta^u\rfloor$, which is smaller than $N$ for all sufficiently
large $N$ at the prescribed cutoff.
The resulting recursion still pays an additive constant at each step; it
does not give a uniform bound.

A proof of (U) along this line must charge the smooth guards $B_{\rm sm}$
and the rough fibres above them from one budget. For a smooth guard $a$
and a fixed fibre $gG_g$ lying above $a$, the inherited modulus for $G_g$
is $a/\gcd(a,g)$. Mixed fibres retain the condition
$a\nmid g_1r_1+g_2r_2$ for distinct larger summands. One cannot replace
these conditions by independent restrictions on each prime or by one
unweighted union of the rough quotients. (RS), and the joint residue
estimate that such an accounting needs, are unproved.

There are two separate obstacles to proving (RS) by the bootstrap of
Corollary R. First, the normalizations behind $\lambda_d\le M_R/d$ can
contain 1: in particular $\lambda_a\ge1/a$ for each $a\in E$. Thus
$M_R$ cannot be replaced throughout by $R^*_N(\Delta)$ when the latter is
smaller than 1. For a $\Delta$-rough set, reduction (O) gives a primitive
early set with the exact split

$$
\lambda_d=1/d\quad(d\in E),\qquad
\lambda_d\le R^*_N(\Delta)/d\quad(d\notin E).
$$

The first equality holds because no other early element is a multiple of
$d\in E$. In the second case the normalized fibre contains no 1 and
remains $\Delta$-rough. A proof at the scale $R^*_N(\Delta)\asymp
\delta_\Delta$ must control the first group separately; omitting it is
not a valid bootstrap.

Second, $32/K$ in Proposition F comes from moduli near $Q$ and late
elements just above $KQ$. If one uses the existing bound $M_R\le30$ and
seeks early and late masses of order $\delta_\Delta$, that inequality
requires $32/K+4J/\Delta$ to be of order $\delta_\Delta^2$. A direct
use therefore needs $K$ of order $\delta_\Delta^{-2}$, with a sufficiently
large constant, rather than a fixed gap. Even an improved treatment of
the self-quotients leaving a term of order $1/K$ would need $K$ of order
$\delta_\Delta^{-1}$. Neither calculation controls the rough property-P
mass in the intervening window. Even an upper sieve bound of order
$\delta_\Delta$ per fixed-ratio interval would sum to order
$\delta_\Delta\log K$ over that gap, whereas a successful cut needs order
$\delta_\Delta$. The factor $J/\Delta$ can be made smaller than
$\delta_\Delta^2$ by taking $\Delta\ge(\log N)^2$ for large $N$.

Thus a useful near-range test is to bound rough property-P sets inside
windows whose ratio is a fixed power of $\log\Delta$, while retaining the
self-quotient terms. If that ratio is $K$ and $2K<\Delta$, a relation
$b+c=ta$ inside the window has $t<\Delta$; then $t$ is exactly the
$\Delta$-smooth part of $b+c$ and $a$ is its rough part. This identifies a
more restricted arithmetic problem, not a proof of (RS). Even a positive
answer still has to be combined with the joint smooth-guard budget above.

Any one of the following would close the gap: a guard charge for
Proposition F bounded independently of the cutoff; the free-mass bound of
Proposition F with a cutoff independent of $N$; or the fixed-$D$ rough-set
bound. The last is equivalent to (U) by the decomposition above with a
fixed cutoff, and the second implies it by the proof of Corollary R.
Corollary H is an author-recorded argument without independent review; it
rests on Corollary R and therefore on the large-sieve statement cited in
Proposition F.

### A signed harmonic criterion

The squares in the exact Fourier identity can be retained longer than in
Proposition F. This gives a complete conditional implication to (U) from
one unproved energy estimate, which already contains the fixed-class form
of (U), as shown below. The identity also separates a residue bias from the
much larger unsigned Fourier energy that the usual large sieve bounds.

Let $B\subseteq[1,N]$ have property P, take $E\subseteq B\cap[3,Q]$ and
$T\subseteq B\cap(KQ,N]$ with $Q,K\ge2$, and use the exact weights
$w_b=1/b$ on $T$. Put $m=h(T)$ and

$$
G(\theta)=\sum_{b\in T}w_be(b\theta),\qquad
\sigma_d(T)=\sum_{\substack{1\le u\le d\\(u,d)=1}}G(u/d)^2,
\qquad
R_Q(T)=\sum_{d=2}^Q\frac{(-\sigma_d(T))_+}{d}.
$$

Pairing $u$ and $d-u$ makes $\sigma_d(T)$ real; $(x)_+=\max(x,0)$.
Let $M_N$ denote the maximal mass of any property-P subset of $[1,N]$.
Then

$$
\boxed{\quad
\left(m^2-\frac{2}{3K^2}\right)h(E)\le M_N R_Q(T).
\quad}                                                        \tag{SE1}
$$

To prove it, write $P_a(T)=\sum_{b,c\in T,\ a\mid b+c}w_bw_c$ and
$\eta_a=aP_a(T)$. As in Proposition F, only the at most two singleton
self-inverse residue classes contribute, so
$\eta_a\le2/(K^2a)\le2/(3K^2)$ for $a\in E$. Grouping the frequencies
by reduced denominator gives

$$
\sum_{\substack{d\mid a\\d>1}}\sigma_d(T)=\eta_a-m^2.
$$

Consequently, with the exact multiplicities
$\lambda_d=\sum_{a\in E,\ d\mid a}1/a$,

$$
m^2h(E)-\sum_{a\in E}\frac{\eta_a}{a}
=-\sum_{d=2}^Q\lambda_d\sigma_d(T)
\le\sum_{d=2}^Q\lambda_d(-\sigma_d(T))_+
\le M_N R_Q(T).
$$

The last inequality uses $\lambda_d\le M_N/d$, obtained by dividing the
multiples of $d$ by $d$. Thus shared-prime multiplicity is retained before
the bound, and no normalized element is excluded. This proves (SE1).

Here is the missing assertion, stated separately from the proved identity:

> **(SE)** There is an absolute constant $C$ such that
> $R_Q(T)\le C h(T)$ for every integer $Q\ge2$ and every finite
> property-P set $T\subset(64Q,\infty)$.

**Conditional conclusion.** If (SE) holds, then
$M_N\le\max(30,16C)$ for every $N$, and E12(iii) follows.

Indeed, suppose $M_N>30$ and choose a maximizing $B$. Such a set contains
neither 1 nor 2, since a property-P set containing either has mass at most
$3/2$. Choose $Q$ at the first crossing of half the mass, put
$E=B\cap[1,Q]$ and $T=B\cap(64Q,N]$. Then

$$
\frac{M_N}{2}\le h(E)\le\frac{M_N}{2}+\frac13,\qquad
m\ge\frac{M_N}{2}-\frac13-\log64>\frac{M_N}{4},\qquad m>10.
$$

In (SE1) the factor on the left is therefore at least $m^2/2$. Assertion
(SE) would give $h(E)\le2CM_N/m\le8C$, hence $M_N\le16C$. This is the
entire implication; the hypothesis (SE) itself has no proof here.

The fixed-class case of (SE) already implies (U) without (SE1).
Let $T$ be any finite property-P set in the class $1\bmod3$
with $\min T>192$, and take $Q=3$. For $u=1,2$ one has $G(u/3)=m\,e(u/3)$,
so $\sigma_3(T)=m^2(e(2/3)+e(4/3))=-m^2$ and $R_3(T)\ge m^2/3$. Assertion
(SE) would give $m\le3C$. Every finite property-P set in the class
$1\bmod3$ would then have reciprocal sum at most
$\sum_{n\le192}1/n+3C$, and (U) follows from the class form of the
equivalence after Proposition E. Thus (SE) already requires a uniform bound
on this class; no reverse implication from (U) to (SE) is established here.
An energy bound of this form, linear in $h(T)$, bounds the mass of a
coherent tail outright. One possible alternative is to keep negative energy
of order $m^2$ on a coherent class paired with the early multiplicity
$\lambda_d$ at that modulus, as in $3B'\cup C_Z$, where the guard 3 has
$\sigma_3=-m^2$ and $\lambda_3=h(B')/3$. This calculation does not
disprove (SE).

The distinction from an unsigned estimate matters already for one prime.
If $T$ lies in a nonzero class modulo an odd prime $q$, then
$\sigma_q(T)=-m^2$, whereas
$\sum_{(u,q)=1}|G(u/q)|^2=(q-1)m^2$. Its contribution to $R_Q$, when
$q\le Q$, is $m^2/q$, smaller by a factor $q-1$ than the unsigned
contribution in Proposition F. The obstruction there to discarding the
number of scales does not by itself refute (SE).

Multiple coherent primes still have to be paid for. If $r\ge3$ is odd and
square-free and $T$ lies in a unit class modulo $r$, then for every
$d\mid r$ one has $\sigma_d(T)=\mu(d)m^2$, by the Ramanujan-sum identity
$c_d(2s)=\mu(d)$ when $(s,r)=1$, where
$c_d(n)=\sum_{(u,d)=1}e(nu/d)$. For square-free $d$ this follows by the
Chinese remainder theorem: each prime factor contributes $-1$. Thus the
contribution of all divisors of
$r$ to the negative-part sum is

$$
\frac{m^2}{2}
\left(\prod_{p\mid r}(1+1/p)-\prod_{p\mid r}(1-1/p)\right).       \tag{SE2}
$$

When some divisors exceed $Q$, (SE2) is an upper bound for their included
contribution. It can grow relative to $m^2$, so paying a separate constant
for each prime is insufficient. For the automatic property-P window
$T=\{n:X<n\le(r+2)X/2,\ n\equiv1\pmod r\}$, however,
$m\to\log((r+2)/2)/r$ as $X\to\infty$ with $r$ fixed. Since
$\prod_{p\mid r}(1+1/p)\le1+\log r$, the limit of (SE2) divided by $m$
is at most $\log r(1+\log r)/(2r)<1$. These windows therefore do not
defeat a linear charge for their coherent divisors. This calculation
covers neither the other denominators nor a union of many windows.

There is also cancellation between composite and prime denominators before
taking negative parts. For example, if $T$ lies in the class $1\bmod3$,
then $\sigma_6(T)=-\sigma_2(T)$: for every sum $b+c\equiv2\pmod3$,
$c_6(b+c)=c_2(b+c)c_3(b+c)=-c_2(b+c)$. With $E=\{3,6\}$ the exact
multiplicities are $\lambda_2=\lambda_6=1/6$, so these two terms cancel in
the identity preceding (SE1). This is compatible with property P, for
example for a late class window above 384 and of ratio at most $5/2$.
Replacing each signed term by its negative part loses that cancellation.
Thus even the proposed signed-energy bound discards some of the structure
in the exact identity.

The proposed alternative signed route estimates the weighted sum
$\sum_d\lambda_d\sigma_d(T)$ jointly, retaining its composite cancellation
and the early mass associated with each coherent modulus. No uniform
estimate of this kind is proved here. Bounding the energies by absolute
Fourier squares returns the term proportional to the number of scales,
and dropping their composite denominators loses genuine multiplicity and
cancellation. Formula (SE1) and its conditional conclusion are
author-recorded algebraic arguments. (SE) remains an unproved sufficient
premise, with neither a proof nor an equivalence to (U) established here;
its failure would not refute the exact weighted identity or (U).

### The whole argument and its open step

The links above compose into one argument for (U) that is complete except
for one estimate. This subsection is the canonical sketch of the route; the
subsections it cites carry the proofs. Work in the odd primitive class of
reduction (O). Write $P=P_N$ for its largest reciprocal sum in
$\{1,\ldots,N\}$, so that $M_N\le3P_N$. A bound on $P_N$ independent of $N$
proves (U), hence E12(iii) with the distinct-summand convention. Fix
$0\le\theta<1$ and put

$$
\alpha=\frac{1+\theta}2,\qquad\beta=\frac{1-\theta}4,\qquad
L=\log64+\frac13 .
$$

**Step 1, the cut.** Let $B$ attain $P$, and suppose $P>4L/(1-\theta)$,
which exceeds $3/2$. A property-P set containing 1 has at most two
elements, so $1\notin B$, and every element of $B$ is odd and at least 3.
Let $Q$ be the least element of $B$ with $h(B\cap[1,Q])\ge\alpha P$, and
put $E=B\cap[1,Q]$, $T=B\cap(64Q,N]$ and $m=h(T)$. Then
$\alpha P\le h(E)\le\alpha P+1/3$. The integers of $(Q,64Q]$ have
reciprocal sum at most $\log64$, so

$$
m\ge(1-\alpha)P-L>\beta P .
$$

**Step 2, the exact identity.** For $a\in E$, no ordered pair $b,c\in T$,
equal or distinct, has $a\mid b+c$: distinct pairs are excluded by property
P, and $a\mid2b$ would give $a\mid b$ for odd $a$, against primitivity.
With exact weights $w_b=1/b$, grouping the frequencies $h/a$ by reduced
denominators as in the signed criterion gives

$$
m^2h(E)=-\sum_{d=2}^{Q}\lambda_d\sigma_d(T),\qquad
\lambda_d=\sum_{\substack{a\in E\\d\mid a}}\frac1a\le\frac Pd .
\tag{I}
$$

For even $d$, $\lambda_d=0$. For odd $d$, its bound holds because dividing
the multiples of $d$ by $d$ keeps a set odd, primitive and property P; the
quotient may be $\{1\}$. The equality in (I) retains the exact
multiplicities; it has not used their upper bound.

**Step 3, free elements.** Apply Proposition F to $E$ and $T$ with $K=64$
and an integer $D\ge8(\log_2N+1)$, with $P$ in place of $M$; its normalization
step stays inside the odd primitive class. Its dyadic late mass $m'$ is at
least $m>L$, so $K\ge4/m'$ as required. Its number $J$ of dyadic ranges is
at most $\log_2N+1$, so the free elements have

$$
h(F)\le\frac{3P}{m'}\Bigl(\frac{32}{64}+\frac{4J}D\Bigr)\le\frac{3P}m
\le\frac3\beta=\frac{12}{1-\theta}.
$$

In the odd primitive class the proof of Proposition F needs only negative
parts. With its dyadic weights, $\eta_a=0$, so $S_a=-g_aP_{g_a}\le-m'^2/2$
for a free $a$, and

$$
\frac{m'^2}2h(F)\le-\sum_{a\in F}\frac{S_a}a
\le P\sum_{\substack{d\le Q\\d\nmid\ell_D}}\frac{(-\sigma_d(T))_+}d .
$$

**Step 4, the open step.** It remains to prove that the guarded elements
of $E$, those with $g_aP_{g_a}(T)<m'^2/2$ in Proposition F, satisfy

$$
h(E_{\rm guarded})\le\theta P+C_0
$$

with $C_0$ independent of $N$, $Q$, $D$ and the number of scales. This is
the joint guard budget. It is neither proved nor refuted. Given Steps 1--3
it is equivalent to (U): if every $P_N$ were at most $U$, it would hold with
$C_0=(1-\theta)U$.

**Step 5, conclusion.** Steps 1, 3 and 4 give
$\alpha P\le\theta P+C_0+12/(1-\theta)$, so

$$
P_N\le\max\Bigl(\frac{4L}{1-\theta},\
\frac{2C_0}{1-\theta}+\frac{24}{(1-\theta)^2}\Bigr),
$$

and truncation and monotone convergence give E12(iii). If Step 4 is
instead stated through (I), as a bound
$-\sum_d\lambda_d\sigma_d(T)\le\theta Pm^2+CPm$, the same cut gives
$P_N\le\max(4L/(1-\theta),\,8C/(1-\theta)^2)$, using $m>\beta P$.

Steps 1--3 and 5 are author-recorded arguments without independent review.
Proposition F rests on the large-sieve statement it cites. Every
coefficient $\theta<1$ suffices, so the open step does not ask for the
early part to lose half of the maximal mass, only a fixed fraction.

**Decoupled energy bounds already contain (U).** Bounding each $\lambda_d$
in (I) by $P/d$ leaves a statement about $T$ alone, of the form
$R_Q(T)\le\theta'h(T)^2+Ch(T)$ in the notation of the signed criterion.
For every $\theta'\ge0$ and $C\ge0$, that assertion for all $Q\ge2$ and all
finite property-P sets $T\subset(64Q,\infty)$ already implies (U). Indeed,
let $r$ be a product of distinct odd primes and

$$
\kappa(r)=\sum_{\substack{d\mid r\\\mu(d)=-1}}\frac1d
=\frac12\Bigl(\prod_{p\mid r}\Bigl(1+\frac1p\Bigr)
-\prod_{p\mid r}\Bigl(1-\frac1p\Bigr)\Bigr).
$$

If $T$ lies in the class $1\bmod r$ and $Q=r$, then
$G(u/d)=m\,e(u/d)$ for every $d\mid r$, so
$\sigma_d(T)=m^2c_d(2)=\mu(d)m^2$ and $R_r(T)\ge\kappa(r)m^2$. Since
$\prod_p(1+1/p)$ diverges, some $r$ has $\kappa(r)>\theta'$, and the
assertion gives $m\le C/(\kappa(r)-\theta')$ for every such $T$ above
$64r$. With the elements below $64r$ this bounds every finite property-P
set in the class $1\bmod r$, which is (U) by the class form of the
equivalence after Proposition E. For example $r=3\cdot5\cdots19=4849845$
has $\kappa(r)=4976640/4849845>1$, from the exact products
$11612160/4849845$ and $1658880/4849845$. So the coefficient in (SE) is
not what makes it strong: with any coefficient on $h(T)^2$, a bound of this
form implies (U). The joint route instead keeps the actual multiplicities
$\lambda_d$, including the cancellation in identity (C) of the next
paragraph. A proof of a decoupled bound would also resolve (U); none is
provided here.

**The coherent case inside the identity.** Suppose $r$ is odd and
squarefree, every divisor of $r$ is at most $Q$, and $T$ lies in one unit
class modulo $r$. Then $\sigma_d(T)=\mu(d)m^2$ for $d\mid r$, and
interchanging the finite sums with $\sum_{d\mid g}\mu(d)=[g=1]$ gives

$$
-\sum_{1<d\mid r}\lambda_d\sigma_d(T)
=m^2\sum_{\substack{a\in E\\\gcd(a,r)>1}}\frac1a .
\tag{C}
$$

The coherent divisors pay for the union of the guarded early elements,
once each. Keeping only the negative terms and bounding each $\lambda_d$ by
$P/d$, as the decoupled assertions do, replaces the right side by at most
$\kappa(r)Pm^2$. For $r=4849845$ this exceeds $Pm^2$, while the union of the
multiples of the primes of $r$ has density
$1-\prod_{p\mid r}(1-1/p)<0.66$.

**Where the current estimates lose.** Split $T$ into its dyadic pieces
$T_j$ of masses $m_j$. For every pair of pieces, equal or not, the same
grouping gives

$$
m_jm_{j'}h(E)=-\sum_{d=2}^{Q}\lambda_d\sigma_d(T_j,T_{j'}),\qquad
\sigma_d(T_j,T_{j'})=\sum_{\substack{1\le u\le d\\(u,d)=1}}
G_j(u/d)G_{j'}(u/d),
$$

and (I) is their sum. The large sieve controls each diagonal energy at
denominators above $D$ by a multiple of $m_j/D$, plus a near-range term
that decays geometrically in $j$. Free-mass control with a cutoff $D$
independent of $N$ would follow if the off-diagonal terms were negligible.
They are not in general. A late part lying in one nonzero class modulo a
prime $q>D$ at every scale has aligned pieces, which is the example after
Corollary R. The signed identity pays such a coherent prime only about
$Pm^2/q$, but then $q$ acts as a guard. Admitting coherent guards at all
primes up to about $\log N$ returns the Euler factor of Corollary H. Thus
each estimate available here loses about $1/D$ for every dyadic scale of
late mass, either as free mass in the unsigned bound or as guard Euler
weight in the signed one. Over $J\approx\log_2N$ scales the two losses
balance at $D\asymp\log N$ and give the bound $O(\log\log N)$. This
describes the present estimates; it is not a proof that every method must
lose. The estimates leave sparse late parts occupying many scales uncontrolled;
they provide no lower bound on the mass of an individual occupied scale.
The constructions on the
[[problems/integer_sequences/E0012/_index|problem page]] demonstrate why
small density alone cannot replace this missing bound.

The same balance appears in the smooth-part normalization. Corollary H
charges each $D$-smooth fibre an additive 30, and the Euler sum
$\sum_g1/g=1/\delta_D$ multiplies that constant. Paying an independent
constant for every possible fibre leaves this loss. A charge proportional
to the rough density, as (RS) proposes, would remove that factor, but the
smooth recursion would still need a joint bound.

**Mixed pairs retain additional constraints.** The cut identity (I) uses only
pairs from $T$. For each $a\in E$, put $E_a=E\cap(a,\infty)$ and define
$\sigma_d(E_a,T)=\sum_{(u,d)=1}G_{E_a}(u/d)G_T(u/d)$ with exact reciprocal
weights. Property P also excludes $a\mid b+c$ with $b\in E_a$ and $c\in T$.
Thus, by the same grouping of frequencies,

$$
-2\sum_{a\in E}\frac1a\sum_{\substack{d\mid a\\d>1}}\sigma_d(E_a,T)
=m\left(h(E)^2-\sum_{a\in E}\frac1{a^2}\right).
\tag{M}
$$

Indeed, the zero frequency for each $a$ is $h(E_a)m$, and
$2\sum_{a\in E}h(E_a)/a=h(E)^2-\sum_{a\in E}a^{-2}$. The early cutoff
inside $E_a$ must stay in the expression. It cannot be replaced by one
multiplicity $\lambda_d$ paired with the Fourier transform of all of $E$.
These constraints require consistency between the residue supports of the
early elements above $a$ and those of the late set, beyond the absence of
opposite pairs within $T$ itself.

One way to retain all these constraints at once is to use the full tail
$B_a=B\cap(a,\infty)$ for each $a\in B$. Write $H=h(B)$,
$H_a=h(B_a)$ and $S_2=\sum_{a\in B}a^{-2}$. In the odd primitive class,
including the empty-tail case, the exact quantity is

$$
\mathcal X(B)=-\sum_{a\in B}\frac1a
 \sum_{\substack{d\mid a\\d>1}}\sigma_d(B_a)
=\sum_{a\in B}\frac{H_a^2}{a}.
\tag{T}
$$

For each $a$, integrate $t^2$ from $H_a$ to $H_a+1/a$. These intervals
partition $[0,H]$, and hence

$$
\frac{H^3}3-\mathcal X(B)
=\sum_{a\in B}\frac{H_a}{a^2}+\frac13\sum_{a\in B}\frac1{a^3},
\qquad
\frac{H^3}3-HS_2\le\mathcal X(B)\le\frac{H^3}3.
$$

For $B\subseteq\mathbb N_{\ge3}$ one has $S_2<1$, by comparison with
$\sum_{n\ge3}1/(n(n-1))=1/2$. A uniform estimate
$\mathcal X(B)\le\eta H^3+CH^2$, with $0\le\eta<1/3$ and absolute $C$,
would therefore give $(1/3-\eta)H^2\le CH+1$ and close (U). No such
estimate is proved. Conversely a uniform bound $H\le U$ implies it with
$C=(1/3-\eta)U$, so this is another full-strength formulation. Its purpose
is to keep the mixed constraints available to the charge, not to claim a
weaker problem. Taking absolute values separately at each $a$ again loses
the reuse of the same original elements and supplies no strict coefficient.

**Unclosed mechanisms.** The following three mechanisms do not close Step 4.

- Pairwise window charges. Comparing one early window with one later window
  of bounded ratio uses only a bounded number of scales, so a constant $D$
  suffices there. But a bound of the form $h(F_i)m_k\le\varepsilon$ for
  every pair of windows still allows $n$ windows of mass $\sqrt\varepsilon$
  each. Summing over all later windows at once restores the cross terms
  above. This route reopens with an estimate for those cross terms.
- Diagonal identities alone. Using only the pairs $j=j'$ weights the
  pieces by $\sum_jm_j^2$ instead of $m^2$. For mass spread evenly over $J$
  scales this is a factor $J$ smaller, which is the $J/D$ loss again. It
  reopens with the same off-diagonal estimate.
- First-divisor events. For any finite set $B$, the sets
  $b\widehat{\mathbb Z}\setminus\bigcup_{a<b,\,a\in B}a\widehat{\mathbb Z}$
  are disjoint, so $\sum_b\rho_b/b\le1$. Here $\rho_b$ is the density of
  the integers $y$ for which no smaller element of $B$ divides $by$. This
  bounds $h(B)$ only when $\rho_b$ stays bounded below, and property P gives
  no visible lower bound. For the primes, which do not have property P,
  $\rho_p$ is about $1/\log p$. The route reopens if property P can be shown
  to keep most $\rho_b$ above a constant.

**Best proved replacement and the missing inverse statement.** The uniform
step remains open. The best bound proved here for general finite sets is
Corollary H's $O(\log\log N)$. Identities (M) and (T) retain mixed
constraints but are not upper estimates. The next subsection bounds full
certified congruence blocks, and Lemma D extends its bound to arbitrary
residue sets at odd moduli. These results suggest a concrete inverse
statement, with the counting error included.

For a block satisfying the hypotheses below, assign one of these errors:
$|R_k|/(X_k+1)$ for a block of ratio at most $3/2$; $3/X_k$ for a
single-class block covered by Lemma W; or $3|R_k|/X_k$ for an odd-modulus
block covered by Lemma D. Each proved block estimate is at most
$(\log2)\mu(\mathcal T(C_k))$ plus its assigned error. Write
$\mathcal E=\sum_k e_k$ for the sum of those errors. The unproved input is:

> **(IC)** There are absolute constants $0\le\theta<1$ and $C\ge0$ such
> that every finite odd primitive property-P set
> $B\subseteq\mathbb N_{\ge3}$ is contained in a finite certified family
> of full congruence blocks, each satisfying one of the three block
> hypotheses, whose errors satisfy $\mathcal E\le\theta h(B)+C$.

If (IC) holds, Lemma T and the block estimates give
$h(B)\le\log2+\mathcal E\le\log2+\theta h(B)+C$, hence
$h(B)\le(\log2+C)/(1-\theta)$. Reduction (O), with the singleton 1
handled separately, then gives
$M_N\le3\max(1,(\log2+C)/(1-\theta))$ and proves E12(iii). This is a
complete conditional replacement for the joint guard estimate in Step 4.
No covering with that strict error allowance is constructed here.
Certification alone is insufficient: the singleton representation below
certifies every odd primitive set but has error exactly $h(B)$. Conversely,
if (U) held with bound $U$ on this subclass, that representation would
satisfy (IC) with $C=(1-\theta)U$. Thus (IC) is equivalent to (U), not a
weaker consequence already supplied by the block estimates.

The precise missing step is to turn simultaneous biases, including the
mixed constraints (M), into such a cover with a strict global error
allowance, or into the signed bound of Step 4 directly. Lemma P supplies
only a two-window density estimate, with its separation and tameness
hypotheses. Bound (V) pays for the nontame early mass, but does not control
the accumulation over windows or the errors of short blocks lying below
their moduli. A proposed refinement must charge the shared prime covers
and these errors once against the same original set.

A sufficient alternative is to
[[research/leads/property_p_sieve_multiplicity/certified_mass_selection|extract a fixed fraction of the original reciprocal mass]]
into jointly certified short blocks, each used residue containing at least
two original elements. Their total extracted mass is at most
$4\log(3/2)$, so the unproved selection statement (EX) on that page would
give (U), without covering the omitted elements. A maximal matching in
short windows pairs all but less than 14 units of reciprocal mass into
pairs sharing a prime factor. This local construction still lacks joint
certification: the exact property-P set $\{21,27,115,125\}$ prevents its
two local pairs from being certified together under any representation
with that occupancy requirement. The selection and strict signed global
estimates both remain open; neither the matching nor the block bounds
give a further bound for general property-P sets.

The term $4/D$ in Proposition F is an upper large-sieve allowance. It does
not by itself classify sets that approach it or prove concentration in
one residue class at a modulus near $D$. Turning a substantial part of
that allowance into certified guard structure requires an inverse
estimate with quantitative counting error; none is held here. The column
bound $h(T)\le C_1(1+\log q)/q$ above a cutoff $Kq$ also remains unproved
and already implies (U) when applied at any fixed modulus in the class
$1\bmod q$, by Lemma E1. It is not an established substitute for this
inverse step. The discriminating test is a strict error bound in (IC), or
a strict signed global inequality, including sparse windows and mixed
fibres. Pairwise density bounds and exact Fourier expansions alone do not
supply it.

### Certified congruence blocks carry bounded mass

This subsection bounds full blocks with certified residue protection by
$\log2$ plus explicit counting errors. Theorem B covers blocks of ratio at
most $3/2$ and single classes with its lower size cutoff. Lemma D covers
arbitrary residue sets at odd moduli with $X\ge q$. Convergence for an
infinite family also requires the errors to be summable. These are scoped
bounds for congruence constructions, not an inverse theorem for all sets.

For an integer $q\ge1$ and $\xi\in\widehat{\mathbb Z}$, write
$\gcd(\xi,q)$ for $\gcd(n,q)$ with any integer $n\equiv\xi\pmod q$. A
*block* is a set

$$
C=\{n\in(X,Y]:\ n\bmod q\in R\}
$$

with integers $q\ge1$ and $1\le X<Y$ and a nonempty set
$R\subseteq\mathbb Z/q\mathbb Z$. A block includes these specified
parameters; its *type* is attached to this representation and is

$$
\mathcal T(C)=\{\xi\in\widehat{\mathbb Z}:\ \gcd(\xi,q)=\gcd(s,q)
\text{ for some }s\in R\}.
$$

For each divisor $g$ of $q$, the set of $\xi$ with $\gcd(\xi,q)=g$ has Haar
measure $\varphi(q/g)/q$. The type contains the classes
$R+q\widehat{\mathbb Z}$, of measure $|R|/q$. Blocks $C_1,\ldots,C_n$ with
$Y_i\le X_k$ for $i<k$ are *certified* if for all $i<k$, $s\in R_i$ and
$t\in R_k$ some prime power divides $s$, $q_i$ and $q_k$ but not $2t$.

The usual protection is certified. Suppose a prime power $p^e$ divides every
residue in $R_i$, $q_i$ and every later modulus, and divides no sum $t+t'$
of residues of later blocks. Taking $t'=t$ gives the certificate. Then no
element of $C_i$ divides a sum of two elements of later blocks.

**Lemma T.** The types of certified blocks are pairwise disjoint.

*Proof.* Let $i<k$ and suppose $\gcd(\xi,q_i)=\gcd(s,q_i)$ and
$\gcd(\xi,q_k)=\gcd(t,q_k)$ with $s\in R_i$ and $t\in R_k$. Take a
certificate $p^e$ for $(s,t)$. It divides $\gcd(s,q_i)$, hence $\xi$; it
also divides $q_k$, hence $\gcd(\xi,q_k)=\gcd(t,q_k)$, which divides $2t$.
This contradicts the certificate. $\square$

**Lemma W.** Let $C=\{n\in(X,Y]:n\equiv s\pmod q\}$ lie in a property-P set,
put $g=\gcd(s,q)$ and $u=q/g$, and suppose $X\ge2g$. Then

$$
Y<\frac{u+2}2(X+q)+q .
$$

*Proof.* If $C$ is empty, then $Y<X+q$ and the bound holds. Otherwise let
$a$ be the least element of $C$, so $X<a\le X+q$ and $a>2g$. Put $t=u+2$.
Since $g\mid s$, $us\equiv0\pmod q$, so $ta\equiv2s\pmod q$.
Suppose $Y\ge ta/2+q$. Let $b$ be the largest integer congruent to $s$
modulo $q$ with $b<ta/2$, and put $c=ta-b$. Then $b\ge ta/2-q>a$ because
$ua>2q$, and $c\equiv s\pmod q$ with $ta/2<c\le ta/2+q\le Y$. So $b$ and $c$
are distinct elements of $C$, both larger than $a$, with $a\mid b+c$. This
contradicts property P, so $Y<ta/2+q\le(u+2)(X+q)/2+q$. $\square$

**Theorem B.** Let $C_1,\ldots,C_n$ be certified blocks. Suppose each $C_k$
either has $Y_k\le3X_k/2$, or is a single class $R_k=\{s_k\}$ with
$X_k\ge2\gcd(s_k,q_k)$ contained in a property-P set. Then

$$
\sum_{k=1}^nh(C_k)\le\log2+\sum_{k=1}^n\frac{|R_k|+3}{X_k}.
$$

If every block has $Y_k\le3X_k/2$, property P is not used, and
$\sum_kh(C_k)\le\log(3/2)+\sum_k|R_k|/(X_k+1)$.

*Proof.* For one residue class modulo $q$ in $(X,Y]$, comparing each term
after the first with an integral gives a reciprocal sum at most
$1/(X+1)+q^{-1}\log(Y/X)$. A block with $Y_k\le3X_k/2$ therefore has
$h(C_k)\le|R_k|/(X_k+1)+(|R_k|/q_k)\log(3/2)$, and
$|R_k|/q_k\le\mu(\mathcal T(C_k))$. For a single-class block, Lemma W gives

$$
\log\frac{Y_k}{X_k}\le\log\frac{u_k+2}2+\log\Bigl(1+\frac{5q_k}{3X_k}\Bigr)
\le\log\frac{u_k+2}2+\frac{5q_k}{3X_k},
$$

so $h(C_k)\le q_k^{-1}\log((u_k+2)/2)+3/X_k$. Here
$\mu(\mathcal T(C_k))=\varphi(u_k)/q_k$, and for every $u\ge1$

$$
\log\frac{u+2}2\le(\log2)\,\varphi(u),
$$

with equality only for $u=2$ and $u=6$. The values $u\le6$ are checked
directly. For $7\le u\le30$, $\varphi(u)\ge4$ and $(u+2)/2\le16$. For
$31\le u\le254$, $\varphi(u)\ge8$ and $(u+2)/2\le128$. The first two bounds
hold because $\varphi(u)\le3$ only for $u\le6$, and $\varphi(u)\le7$ only for
$u\le18$. For $u\ge255$, $\varphi(u)\ge\sqrt{u/2}$, which follows from
$\varphi(p^e)\ge p^{e/2}$ for odd $p$ and $\varphi(2^e)\ge2^{(e-1)/2}$.
Also $\sqrt{u/2}\ge\log_2((u+2)/2)$ at $u=255$, and the left side grows
faster from there. So every block has
$h(C_k)\le(\log2)\mu(\mathcal T(C_k))+(|R_k|+3)/X_k$, and Lemma T gives
$\sum_k\mu(\mathcal T(C_k))\le1$. With only blocks of ratio at most $3/2$,
the classes $R_k+q_k\widehat{\mathbb Z}$ are already disjoint, which gives
the second bound. $\square$

The bound does not depend on how many guards are used or how they are
encoded. Block constructions of the kind described on the problem page are
certified when their protection is the one stated there. In those, each
block is a set of residues modulo $q_k$ in a window of ratio at most $3/2$.
Every residue of an earlier block is divisible by a guard prime that
divides the later moduli, and no sum of two later residues is divisible by
it. The descriptions there were read for this structure only, not
re-verified. Any such construction, and any subset of one, has reciprocal
sum at most $\log(3/2)+\sum_k|R_k|/(X_k+1)$. The error is at most
$\sum_k q_k/(X_k+1)$, which is summable, for example, when
$X_k\ge2^kq_k$. This covers one guard prime per block and guard systems
encoded by the digits of the block index, whenever
each pair of blocks is separated by a guard of this kind. Consequently a
divergent property-P set cannot be covered by such blocks
with a summable displayed error. Certification without control of that
error gives no convergence conclusion, as the singleton representation
below shows.

The single-class restriction can be removed for odd block moduli, while
retaining an explicit counting error.

**Lemma D.** Let $q$ be odd, $X\ge q$, and let
$C=\{n\in(X,Y]:n\bmod q\in R\}$ have property P. Then

$$
h(C)\le(\log2)\mu(\mathcal T(C))+\frac{3|R|}{X}.
$$

Consequently certified blocks with odd $q_k$, $X_k\ge q_k$, and property P
inside each block satisfy
$\sum_k h(C_k)\le\log2+3\sum_k|R_k|/X_k$, without a restriction on their
ratios or on the number of residue classes.

*Proof.* If $Y<X+2q$, the progression estimate in Theorem B gives
$h(C)\le |R|/(X+1)+(|R|/q)\log(1+2q/X)\le3|R|/X$. Otherwise let $J\ge0$
be the largest integer with $2^J(X+q)+q\le Y$. The sets of residues
$R,2R,\ldots,2^J R$ are pairwise disjoint. To see this, an intersection,
after division by a power of 2 modulo odd $q$, would give
$2^k r\equiv s\pmod q$ with $r,s\in R$ and $1\le k\le J$. Let $a$ be the
least integer above $X$ in the class of $r$, so $a\le X+q$. The integers
$b=2^ka-q$ and $c=2^ka+q$ both lie in the class of $s$. Since $a>X\ge q$,
we have $a<b<c\le Y$, and $b+c=2^{k+1}a$, a forbidden relation.

Doubling preserves every gcd type modulo odd $q$. Therefore
$(J+1)|R|/q\le\mu(\mathcal T(C))$. The maximality of $J$ gives

$$
\log\frac YX<(J+1)\log2+
\log\left(1+\frac qX+\frac{q}{2^{J+1}X}\right)
\le(J+1)\log2+\frac{3q}{2X}.
$$

Combining this with the progression estimate proves the claimed bound.
Summing and applying Lemma T proves the consequence. $\square$

The counting errors cannot be omitted. In fact every finite odd primitive
set $A=\{a_1<\cdots<a_n\}\subseteq\mathbb N_{\ge3}$ has a certified
representation by singleton blocks: take
$q_i=\operatorname{lcm}(a_1,\ldots,a_i)$, $R_i=\{a_i\bmod q_i\}$,
$X_i=a_i-1$ and $Y_i=a_i$. These are full blocks of ratio at most $3/2$.
For $i<k$, primitivity supplies an odd prime power dividing $a_i$ but not
$a_k$. It divides both moduli and not $2a_k$, so it is a certificate.
The short-block error in Theorem B is now
$\sum_i|R_i|/(X_i+1)=h(A)$, and its inequality supplies no bound on $h(A)$.
For example the odd primes give certified singleton blocks with divergent
mass and divergent error; their union does not have property P.
Thus certification alone is not a useful inverse conclusion for arbitrary
property-P sets. A successful use must also pay for the counting error
uniformly. Lemma D does not apply to this representation, since $X_i<q_i$.

Certification is forced when the blocks are full residue classes over long
windows.

**Lemma S.** Let $C=\{n\in(X,Y]:n\equiv t\pmod q\}$ lie in a property-P
set $B$, and let $a\in B$ with $a\le X$ and
$Y-X\ge q+\operatorname{lcm}(a,q)$. Then $\gcd(a,q)\nmid2t$.

*Proof.* Let $b\le X+q$ be the least element of $C$. If
$\gcd(a,q)\mid2t$, the congruences $c\equiv t\pmod q$ and
$c\equiv-b\pmod a$ are compatible, since $b\equiv t\pmod q$. Their common
class modulo $\operatorname{lcm}(a,q)$ has an element $c$ with
$b<c\le b+\operatorname{lcm}(a,q)\le Y$. Then $b,c\in C$ are distinct, both
exceed $a$, and $a\mid b+c$, contradicting property P. $\square$

**Corollary S.** Let a property-P set contain blocks $C_1,\ldots,C_n$ with
$Y_i\le X_k$ for $i<k$, and suppose that for all $i<k$

$$
Y_k-X_k\ge q_k(1+Y_i),\qquad Y_i-X_i\ge q_i\operatorname{rad}(q_k).
$$

Then the blocks are certified.

*Proof.* Fix $i<k$, $s\in R_i$ and $t\in R_k$. The elements of $C_i$ in
the class of $s$ are $a=s_0+q_ij$ for at least $\operatorname{rad}(q_k)$
consecutive integers $j$. For each prime $p\mid q_k$, the condition
$v_p(a)=v_p(\gcd(s,q_i))$ excludes at most one residue of $j$ modulo $p$.
It is automatic when $v_p(s)<v_p(q_i)$. Otherwise it requires
$a/p^{v_p(q_i)}\not\equiv0\pmod p$, or $p\nmid a$ when $p\nmid q_i$, and
$q_i/p^{v_p(q_i)}$ is a unit modulo $p$. So some admissible $j$ meets every
condition, and that $a$ has $\gcd(a,q_k)=\gcd(s,q_i,q_k)$. If no prime
power divides $s$, $q_i$ and $q_k$ without dividing $2t$, then
$\gcd(s,q_i,q_k)\mid2t$. The class of $t$ in $C_k$ has length at least
$q_k+\operatorname{lcm}(a,q_k)$, because $a\le Y_i$, so Lemma S gives a
contradiction. $\square$

The richness condition $Y_i-X_i\ge q_i\operatorname{rad}(q_k)$ asks earlier
blocks to be long compared with later moduli, which constructions with
growing moduli do not satisfy. Short early blocks can be protected through
prime factors of individual early elements, which the block residues do not
record. That is where an uncertified protection can enter.

Without saturation, a pair of compatible classes in two far-apart windows
still cannot both be dense. This is the one-pair form of the charge that
the open step needs.

**Lemma P.** Let $B$ have property P, let $q\ge2$ be even, and let $z_q$ be the
least prime not dividing $q$. Let $x$ and $y$ be residues modulo $q$ with
$\gcd(x,q)\mid2y$. Let $S$ be the set of $a\in B\cap(X,Y]$ with
$a\equiv x\pmod q$ and $\gcd(a,q^\infty)\mid q$, where
$\gcd(a,q^\infty)$ is the largest divisor of $a$ supported on the primes
dividing $q$. Let
$K=\{b\in B\cap(X',Y']:b\equiv y\pmod q\}$, where the endpoints are integers,
$q\le X<Y\le X'<Y'$ and $Y'-X'\ge qY^2$. Write $\rho_S=q|S|/(Y-X)$,
and $\rho_K=|K|/L$ where
$L$ is the number of integers in $(X',Y']$ congruent to $y$ modulo $q$.
Then

$$
\rho_S\,\rho_K\le\frac6{z_q}+\frac{6q}{Y-X}.
$$

*Proof.* If $S$ or $K$ is empty the assertion is immediate. Otherwise, for
$a\in S$ put $g_a=\gcd(a,q)$ and $r_a=a/g_a$. Then $r_a$ is
coprime to $q$, so its prime factors are at least $z_q\ge3$, and $r_a>1$
because $a>X\ge q$. For $b,c\in K$, $b+c\equiv2y\pmod q$, and $g_a$
divides both $q$ and $2y$, so $g_a\mid b+c$. Hence $a\mid b+c$ exactly
when $r_a\mid b+c$. Write the
elements of $K$ as $b_0+qk$ with $1\le k\le L$, where $b_0+q$ is the least
integer in $(X',Y']$ congruent to $y$, and let $K'$ be the set of these $k$.
Since $q$ is invertible modulo $r_a$, property P says that $K'$ has no two
distinct elements whose sum is congruent to a fixed $h_a$ modulo $r_a$.
So at most one of two classes $t\ne h_a-t$ modulo $r_a$ is occupied, and a
class with $2t\equiv h_a$ holds at most one element. As in (4), with
$F(\theta)=\sum_{k\in K'}e(k\theta)$ and $N=|K'|$,

$$
\sum_{j=1}^{r_a-1}|F(j/r_a)|^2\ge\kappa(r_a)N^2\ge\frac{N^2}3 .
$$

Take weights $w_a\ge0$ and put $\Lambda_d=\sum_{a\in S,\ d\mid r_a}w_a$.
Grouping the fractions $j/r_a$ by reduced denominators and using
$\Lambda_d\le\Lambda_p$ for a prime $p\mid d$, the large sieve cited for (1),
applied to $K'\subseteq[1,L]$ with denominators at most $Y$, gives

$$
\frac{N^2}3\sum_{a\in S}w_a\le\max_p\Lambda_p\,(L+Y^2)N .
$$

By linear-programming duality, the largest $\sum_aw_a$ with every
$\Lambda_p\le1$ equals the least $\tau=\sum_py_p$ over $y_p\ge0$ with
$\sum_{p\mid r_a}y_p\ge1$ for every $a\in S$, the fractional covering number
of the rough parts by primes. So $N\le3(L+Y^2)/\tau\le6L/\tau$. The same
cover counts $S$: for a prime $p\nmid q$ the elements of $(X,Y]$ congruent
to $x$ modulo $q$ and divisible by $p$ form one class modulo $pq$, so

$$
|S|\le\sum_{a\in S}\sum_{p\mid r_a}y_p
\le\sum_py_p\Bigl(\frac{Y-X}{pq}+1\Bigr)
\le\tau\Bigl(\frac{Y-X}{qz_q}+1\Bigr).
$$

Multiplying the two bounds gives the lemma. $\square$

Lemma P gives a dichotomy for the tame early part and a later class in
windows with its stated separation. Either a prime power dividing the
early residue and $q$ does not divide twice the late residue, in which case
their types are disjoint as in Lemma T, or the product of the two relative
densities is at most $6/z_q$ plus its boundary term. It does
not bound a sum over many windows. A bound $\rho_k\rho_{k'}\le\varepsilon$
for every pair still allows $n$ compatible windows of relative density
$\sqrt\varepsilon$. Fractional covers for different comparisons can reuse
the same primes outside $q$; Lemma P gives no combined charge for that reuse.

The restriction on prime-power valuations in Lemma P must be retained. Its
exceptional early mass has a controlled cost relative to $P_N$, as follows.
Work in the odd primitive class, let $P=P_N$, take an integer
$D\ge4$ and put $q=\ell_D$. Call an early element *tame* when its largest
divisor supported on primes dividing $q$ divides $q$. If $W$ is the set of
nontame early elements, then

$$
h(W)\le\frac{3P}{\sqrt D}.
\tag{V}
$$

For each prime $p\le D$, let $p^{k_p}$ be its least power exceeding $D$.
A nontame element is divisible by at least one such power. The quotient
bound $\sum_{a\in E,\,p^{k_p}\mid a}1/a\le P/p^{k_p}$ therefore gives
$h(W)\le P\sum_{p\le D}p^{-k_p}$; the even-prime term is zero in this
class. For $p\le\sqrt D$ each term is less than $1/D$, so these terms sum
to at most $1/\sqrt D$. For $p>\sqrt D$ the power is $p^2$, and
$\sum_{n>\sqrt D}n^{-2}\le1/\lfloor\sqrt D\rfloor\le2/\sqrt D$. This proves
(V). At square cutoffs $D=t^2$, the same proof gives $h(W)<2P/t$.

Thus Lemma P has a controlled prime-power exception when used with this
choice of $q$. Bound (V) is a harmonic mass estimate, not a bound on the
relative density of the exceptional elements in every window. It does not
remove the many-window accumulation problem or the counting-error problem
in Theorem B.

Lemmas T, W, D, S and P, bound (V), Theorem B and Corollary S are
author-recorded arguments without independent review. Lemma P uses the cited
large-sieve statement and finite linear-programming duality. None of them bounds
general property-P sets.

### Exact normalization and ownership

For a finite nonempty property-P set $B$, form its greedy coprime list
$C(B)=(c_1,\ldots,c_k)$. An unselected $b\in B$ has a unique first index
$i$ with $\gcd(b,c_i)>1$. Assign it to the least prime $p$ dividing that
gcd, and let $B_{i,p}$ consist of the assigned numbers divided by $p$.
Then $b>c_i$: otherwise $b$, coprime to all earlier $c_j$, would have been
selected before $c_i$. Each nonempty child is a property-P set, and

$$
h(B)=h(C(B))+\sum_{(i,p)}\frac{h(B_{i,p})}{p}.                    \tag{14}
$$

Every original element has one owner. This is an identity, with no overlap
loss and no dyadic rounding. Iterate at every child. Along an edge the
maximum element decreases, so a finite input gives a finite tree. If $d_v$
is the product of edge primes on the path to node $v$, put $w_v=1/d_v$ and
$h_v=h(C(B_v))$. Then

$$
h(A)=\sum_v w_vh_v.                                             \tag{15}
$$

No exclusion of 1 or 2 is applied to a normalized child. A property-P set
containing 1 has at most two elements; one containing 2 has at most one
larger element of each parity. These small cases also satisfy (14).
Every selected coprime list has mass less than 10, by Proposition C or
these small cases. Replacing every $h_v$ by 10, however, loses too much.

### Why geometric sibling discounts fail

Let $p_1=3<p_2<\cdots<p_k$ be the first $k$ odd primes and
$Q=p_1\cdots p_k$. Take $M=3^tQ$ large enough that $M>2p_k$, and put

$$
A_{k,t}=\{M\}\cup
 \{n:M<n<3M/2,\ \gcd(n,Q)>1\}.                                 \tag{16}
$$

Every subset of $[M,3M/2)$ has property P: for $a<b<c$ in that interval,
$2a<b+c<3a$, so $a$ cannot divide $b+c$. The greedy coprime list of (16)
is just $(M)$. Its $j$-th branch consists of multiples of $p_j$ avoiding
$p_1,\ldots,p_{j-1}$, divided by $p_j$. Its first original element is
$M+p_j$, so ordering branches by their first elements gives exactly this
prime order.

Write $\delta_j=\prod_{i<j}(1-1/p_i)$. For fixed $k$, periodic counting
and partial summation give

$$
h(B_j)\longrightarrow \delta_j\log(3/2)
\quad(t\longrightarrow\infty),\qquad \delta_j\ge1/j.             \tag{17}
$$

For example, inclusion-exclusion over the $j-1$ excluded primes gives an
error at most $2^{j+1}p_j/M$ in (17): the reciprocal sum of the multiples
of any fixed divisor on $(x,3x/2)$ differs from $\log(3/2)/d$ by at most
$2/x$, with $x=M/p_j$. The lower bound follows from $p_i\ge i+1$ and
telescoping $\prod_{i<j}i/(i+1)$.

Consequently **no fixed $K$ and $0<\lambda<1$ can bound every normalized
$j$-th branch by $K\lambda^{j-1}$**. Choose $j$ with
$K\lambda^{j-1}<\log(3/2)/(2j)$, then choose $t$ large in (17). This
refutes a scale-independent geometric sibling mass discount, including the
proposed factor $2^{1-j}$. It does not refute the product-scale occupancy
identity (11). The many normalized branches here come from a single
original size interval.

It also refutes a constant toll at every normalization node: the root and
its first generation already have
$\sum_vw_v\ge1+\sum_{j\le k}1/p_j$, unbounded as $k$ grows. Nevertheless,

$$
h(A_{k,t})\le M^{-1}+\log(3/2),\qquad
h(A_{k,t})\longrightarrow\log(3/2)(1-\delta_{k+1}).                \tag{18}
$$

Thus the excess is in the charging rule. These finite blocks have not
been joined into an infinite property-P set.

### Euler weights and a complete failed proof

A node also inherits a finite set $F_v$ of primes dividing none of its
normalized elements. Initially $F_\varnothing=\varnothing$. The exact
inheritance along $(i,p)$ is

$$
F_{i,p}=F_v\cup\bigcup_{j<i}\{q:q\mid c_j,\ q\text{ prime}\}
 \cup\{q:q\mid c_i,\ q<p,\ q\text{ prime}\}.                      \tag{19}
$$

Division by $p$ preserves all these exclusions. Set
$\delta(F)=\prod_{q\in F}(1-1/q)$ and let $P(C)$ be the primes dividing
the selected coprime list. They are disjoint from $F_v$. Flatten the primes
of $c_1,c_2,\ldots$ in that order, increasingly within each $c_i$.
The elementary identity
$\sum_j p_j^{-1}\prod_{r<j}(1-1/p_r)=1-\prod_j(1-1/p_j)$ gives

$$
\sum_{(i,p)}\frac{\delta(F_{i,p})}{p}
\le\delta(F_v)(1-\delta(P(C(B_v)))).                              \tag{20}
$$

The sum is over nonempty children; omitting empty ones only decreases it.
This includes prime 2. Define the positive leftover weight

$$
\ell_v=\delta(F_v)-\sum_{(i,p)}\frac{\delta(F_{i,p})}{p}.
\qquad \sum_vw_v\ell_v=1.                                       \tag{21}
$$

The second equality telescopes over the finite tree, including its leaves.
For (16), the first-generation sum in (20) is $1-\delta_{k+1}$, tending
to one: these correct weights still have no uniform strict contraction.

A direct bound $h_v\le K\ell_v$ also fails for every fixed $K$. To see
this, let $Q$ be the product of the first $k$ primes at least 5, choose
$M=Q^{2t}>6\max_{p\mid Q}p$, and take

$$
B=\{3,M,M+2\}\cup
 \{n:M<n<3M/2,\ n\equiv1\pmod3,\ \gcd(n,Q)>1\}.
$$

Here $M\equiv1\pmod3$. The terms at least $M$ lie in an automatic
property-P interval; relative to 3 they occupy residue 1 and the single
residue-0 term $M+2$. Thus $B$ has property P. Its greedy list is
$(3,M)$. The 3-child is nonempty, and every prime $p\mid Q$ has the
assigned witness $M+3p$. All possible root children are therefore
nonempty, giving $\ell_\varnothing=(2/3)\prod_{p\mid Q}(1-1/p)\to0$,
whereas $h_\varnothing\ge1/3$. This only disproves charging the current
selected list to the current leftover weight; it does not disprove a
charge that transfers a budget between generations.

Here is an end-to-end attempt with a specific missing inequality. Put

$$
t_v=\sum_{(i,p)}\frac{h(C(B_{i,p}))}{p}.
$$

If some absolute $\beta$ satisfied

$$
t_v\le\tfrac12h_v+\beta\ell_v                                \tag{22}
$$

at every node of every finite property-P tree, then (15) and (21) would
imply
$h(A)-h_\varnothing\le h(A)/2+\beta$, hence
$h(A)<20+2\beta$. Truncation and the dyadic criterion would prove
E12(iii). This implication is complete at author standing.
**Its premise (22) is false for every fixed $\beta$**, as the following
family proves. Increasing a constant cannot repair this potential.

### Semiprimes refute the two-generation charge

Let $y$ be a sufficiently large integer, $M=y^3$, and

$$
A_y=\{pq:M<pq<3M/2,\ p\le y,\ p,q\text{ prime}\}.                \tag{23}
$$

Here $q>y^2$, so the two factors have unique roles. The set is contained
in an automatic property-P interval. Its greedy coprime list is a maximal
matching between the small primes $p\le y$ and the large primes $q$.

The prime number theorem implies, uniformly for $x\ge y^2$ once $y$ is
large, that $(x,3x/2)$ contains at least $x/(4\log x)$ primes. For a fixed
$p\le y$, this supplies more than $y$ possible partners $q$. If $p$ were
unmatched, each partner would have to occur in a selected edge, by
maximality, but there are at most $\pi(y)\le y$ selected edges. Thus every
small prime is matched. Write $Q_y$ for the $\pi(y)$ selected large
primes. Every small-prime branch is nonempty, since there are more
partners than elements of $Q_y$.

All partners $q\notin Q_y$ are assigned to the small prime $p$: it is
their only factor occurring in the root list. After division they are
primes, so are selected by that child's coprime extraction. The interval
prime count above also gives
$\sum_{M/p<q<3M/(2p)}1/q\ge1/(18\log y)$. Removing the selected large
primes costs at most $\pi(y)p/M$ in each such sum. Consequently, with
$S(y)=\sum_{p\le y}1/p$,

$$
h_\varnothing\le y^{-2},\qquad
t_\varnothing\ge\frac{S(y)}{18\log y}-\frac1y.                   \tag{24}
$$

In the complete prime-by-prime sum behind (20), the only possible empty
branches belong to $Q_y$. Each omitted term is at most $1/q$. Hence

$$
0<\ell_\varnothing
\le\prod_{p\le y}(1-1/p)+\sum_{q\in Q_y}1/q
\le\frac1{\log(y+1)}+\frac1y.                                   \tag{25}
$$

The last product bound is elementary: its reciprocal includes every term
of $\sum_{n\le y}1/n\ge\log(y+1)$ in its Euler-product expansion. Also
$S(y)\to\infty$; otherwise the same Euler products would stay bounded,
contradicting the divergence of the harmonic series.

Equations (24)--(25) show

$$
\frac{t_\varnothing-\theta h_\varnothing}{\ell_\varnothing}
\longrightarrow\infty
\quad\text{for every fixed }\theta\ge0.                           \tag{26}
$$

In particular (22) fails, even at roots with no inherited exclusions.
This is a complete author-recorded obstruction using the prime number
theorem as an external statement, not an inference from finite solver
runs. It rules out this two-generation Euler-weight charge, with any
fixed coefficients on the current toll and leftover weight. It does not
rule out an argument grouping more information about the original scale.
The sets (23) themselves have $h(A_y)\le\log(3/2)$.

### What a repair must retain

The normalization identity (14), the exact ownership rule, and the Euler
accounting (19)--(21) survive. The geometric sibling discount and (22) do
not. The missing input is a charge that controls the **total** mass (15)
while grouping the many prime branches that represent one original size
interval. Assigning a full coprime capacity to each branch loses that
common origin; assigning only its Euler leftover weight also loses the
prime-cofactor contribution in (24). Neither (H) nor any replacement
providing this global charge is proved here.

Residue inheritance alone does not close the gap. Under division by $p$,
a constraint modulo $m$ becomes one modulo $m/\gcd(m,p)$; new moduli need
not be coprime to old ones, and normalized elements need not exceed their
least common multiple. Actual property-P tails also permit the singleton
self-inverse exceptions in (9). These interfaces, as well as prime 2 and
terminal sets, must be included in any use of (H). Identity (11), with its
specific common-prime hypotheses, cannot be applied indiscriminately to
siblings through different primes.

For a constraint $a$ and a different prime $q\nmid a$, two summands from
$qA_q$ below $qa/2$ cannot have sum divisible by $a$: such a sum would be
at least $qa$. This protection concerns two summands in the same branch.
Mixed summands from different branches do not receive it. A replacement
must account for those mixed constraints as well as the delayed ones.

Harmonic mass also cannot be bounded by an absolute constant times the
density of an occupied residue class. For fixed $L\ge3$ and $x>0$, the set
$B_x=\{n:x<n\le Lx/2,\ n\equiv1\pmod L\}$ has property P. Indeed, a
forbidden relation $b+c=ka$ would give $k>2$ and $k\equiv2\pmod L$,
hence $k\ge L+2$, whereas $b+c\le Lx<La$. As $x\to\infty$,
$h(B_x)\to L^{-1}\log(L/2)$ by summing one arithmetic progression.
Its ratio to the class density $1/L$ is therefore unbounded as $L$ grows.
This refutes that density-only mass charge, not (H) or (U).

A finite two-block check tests the interaction left out of these
potentials. Let $D_1,D_2$ contain every $pq$ with $p\in\{2,3,5\}$ and
$q$ prime in the respective intervals $(125,187.5)$ and
$(15625,23437.5)$. They have 14 and 902 elements, and each entire block has
property P. Their separate masses sum to more than $0.137$, whereas

$$
0.0929<\max\{h(B):B\subseteq D_1\cup D_2\text{ has property P}\}
\le0.101959737<0.102.                                            \tag{27}
$$

The lower bound is a retained witness checked against every forbidden
triple. The upper bound is an exact finite computation, independent of
solver optimality. For every one of the $2^{14}$ choices of early elements,
remove late elements forbidden by an early pair and form disjoint pairs of
remaining late elements whose sum is divisible by a chosen early element.
At most one endpoint of each such pair can remain. Round each reciprocal
upward to an integer multiple of $10^{-9}$; subtracting the smaller rounded
weight on each disjoint pair gives a rigorous upper bound. The largest of
these 16,384 bounds is at most $101959737/10^9$. The
[evidence entry point](evidence/main.py) regenerates this covering of all
cases and checks the matching edges. Thus joint mass is less than $74.5\%$
of the sum of the separate capacities in this exact domain. This is a
finite interaction bound, not a uniform loss at arbitrary scales.

The same exhaustive calculation at other later scales gives the following
certified upper bounds. The early block always has 14 candidates and
mass approximately $0.090327$; the separate masses in the table are
rounded numerical summaries, not inputs to the certificates.

| Later interval start | Later candidates | Sum of separate masses | Joint upper bound |
| --- | --- | --- | --- |
| 625 | 57 | 0.164102 | 0.111012802 |
| 3125 | 217 | 0.146748 | 0.105285764 |
| 15625 | 902 | 0.137276 | 0.101959737 |
| 78125 | 3852 | 0.130341 | 0.100627648 |

A finite variant of this interaction test keeps the early block and enlarges the
later small-prime cutoff from 5 to 7, 11 and 13 at these scales, retaining
exact matching bounds. The proposed finite target is
$h(B)\le h(D_1)+h(D_2)/3$ for every property-P subset of the two blocks.
A feasible set above this threshold refutes that target; a matching bound
below it certifies only the specified finite domain. A weaker matching
bound alone decides neither outcome. Matchings of mixed forbidden triples
are the proposed charges. The
research obligation is to turn these losses into a bound independent of
both the cutoff and the number of intervals, with each deleted element
charged a bounded number of times. The present matchings reuse early
constraints separately for every later block; no bounded multiplicity
across blocks has been proved. A fixed finite prime cover does not ensure
that (13) is finite: it does not control the primes shared by distinct
elements. Indeed, every dilation $2A$ has the prime cover $\{2\}$,
while preserving property P and reciprocal divergence. Proposition S
handles a finite shared-prime set, or more generally a convergent sum of
their reciprocals; the finite-prime-cover branch remains unresolved.

Unconditional linear weighting of the original triple constraints cannot
alone supply that bound. On any finite candidate domain they have the
form $x_a+x_b+x_c\le2$. The fractional assignment $x_n=2/3$ satisfies
all of them and has unbounded harmonic objective as the domain grows.
Thus a linear relaxation using only those constraints and $0\le x_n\le1$
cannot prove (U). The conditional matchings above use the chosen early
elements as actual Boolean decisions. A repair must preserve that
conditioning or supply stronger consequences; this is not an obstruction
to nonlinear or multiscale arguments.

By Proposition E, a negative answer needs no infinite construction beyond
the gluing: finite property-P sets of unbounded reciprocal sum suffice, and
they may be sought inside one class $1\bmod L$. Neither unbounded finite
sets nor the bound (U) is established here.

Ordinary multiplication of a finite set does not provide the required
amplification. The odd pairwise coprime set $B=\{3,5,47\}$ has property P,
since its only triple has $3\nmid5+47$. But $BB$ contains $25$, $141$ and
$2209$, and $141+2209=94\cdot25$. Both larger summands are distinct, so
$BB$ fails P even when the input is odd and primitive. Moreover, a product
of reciprocal sums counts factorizations, whereas $h(BB)$ counts distinct
integers. An amplification route must supply both a P-preserving operation
and a lower bound on the reciprocal mass after these multiplicities are
removed. This example rules out only the unmodified product operation.

## Finite computations

The [evidence entry point](evidence/main.py) checks, in exact arithmetic,
the property-P claims of the examples above, the occupancy values in (10)
and (11) for small moduli, and the greedy coprime sequence $(3,98)$ of the
truncated example (6). It also builds greedy property-P sets: the primes
below $10^6$, with reciprocal sum about $0.760$ and each region of the proof
of Proposition C far below its bound, and the integers from 3 below
$10^5$, with 72 elements and reciprocal sum about $1.108$. Both satisfy
(13), as does the truncated example (6). Finally it runs
SciPy's mixed-integer solver for the largest reciprocal sum of a
property-P subset of $[3,N]$, and for the admissible-class maxima quoted
above. On $[3,N]$ the solver reports $85/88\approx0.966$ for $N=20$,
$1.048$ for $N=40$, $1.066$ for $N=60$, and $1.080$ for $N=80$ and
$N=100$. The returned sets have property P and these sums exactly; their
optimality is the solver's floating-point report, not a certificate. These solver results alone bear on (U) and (H) only through consistency.

Nine additional retained witnesses use the same prescribed residue halves
on $[L+1,rL]$, where $L$ is the product of the first $k=2,3,4$ odd primes
and $r=2,4,8$. Their exact domains, property P and rational masses are
replayed from [the retained inputs](evidence/assets/above_product.json).
The solver-reported masses for $r=8$ are approximately $0.221837$,
$0.101727$ and $0.045856$; optimality is not certified. These windows meet
(H)'s product-scale condition, but do not prove it.

Lemma E1, Proposition E, reduction (O), the class constructions, Proposition F,
Corollary R, Corollary H, inequality (SE1) with its conditional implication, the
whole argument with its cut at any fraction, the implication from decoupled
energy bounds to (U), identities (C), (M) and (T), Lemmas T, W, D, S and P,
bound (V), Theorem B and Corollary S are written arguments in the text; the
entry point does not check them. The implication from (IC) to (U) and its
converse are written arguments; (IC) itself remains unproved. The exact
products behind $\kappa(4849845)$ and the cases of
$\log((u+2)/2)\le(\log2)\varphi(u)$ are stated with their values and are checked
by hand in the text. Proposition F and Corollaries R and H also use the stated
large-sieve interface. The proposed estimate (SE) remains unproved and has no
computational warrant here.

The normalization checks cover exact ownership and both telescoping
identities, including normalized sets containing 1 or 2; finite instances
of (16) and (23), and of the direct-toll obstruction; the semiprime
matching and discarded-cofactor bounds;
and the explicit constant in Proposition C. The infinite obstruction (26)
uses its written prime-number-theorem argument, not these samples. The
separate [two-block witness](evidence/assets/two_block.json) and integer
matching computations certify only (27) and the four finite table bounds.

## Source scope

Schoen's definitions, Lemma 1 and equations (7)--(9) were read in the
primary transcription. Printed p. 194 was also inspected: the lower
index $r=0$ in its later comparison of frequency sums is printed that
way. The argument here explicitly uses $r\ge1$, as required by (9).
This is not a transcription repair or an independent audit of the paper.
The bibliography and canonical result are on the
[[../library/integer_sequences/schoen_2001_problem_erdos_sarkozy/_index|source card]].

The Brun--Titchmarsh input is read from H. L. Montgomery and R. C. Vaughan,
*Multiplicative Number Theory I: Classical Theory*, Cambridge University
Press, 2006,
[[../library/primes/montgomery_vaughan_2006_multiplicative_number_theory_i/theorem_3_9|Chapter 3, Theorem 3.9, printed p. 90, and the Section 3.5 notes on Section 3.3, p. 102]].
For $(a,q)=1$, $x\ge0$, and $y\ge2q$, the number of primes in
$(x,x+y]$ congruent to $a$ modulo $q$ is at most
$2y/(\varphi(q)\log(y/q))$: the notes explicitly remove the error term
in Theorem 3.9 using the authors' 1973 paper *The large sieve*, Mathematika
20, 119--134. Both cited book pages were read on page images. The uses
here have $t\ge q^2$ for $q\ge2$, or $q=1$ and $t\ge3$, so lie in the
read domain. The original 1973 statement and proof were not inspected,
and this is not a proof audit of the book's theorem.

The semiprime obstruction uses the prime number theorem
$\pi(x)\sim x/\log x$, read at statement depth on the page image of
[the same book, Chapter 6, printed p. 168](https://personal.science.psu.edu/rcv4/personal/Publications/MNTI/10.0_pp_168_198_The_Prime_Number_Theorem.pdf).
Its proof is not reconstructed here. The interval lower bound used in
(24) follows by subtracting the asymptotics at $3x/2$ and $x$; its
uniformity for $x\ge y^2$ follows directly from the eventual bound in the
definition of that asymptotic. No error term or prime progression theorem
is required. The Euler-product estimates in (25) are proved in the text.

Corollary H's explicit bound includes an elementary proof of
$\prod_{p\le x}p<4^x$. Mertens' product theorem is used at statement level
only for the sharper constant $30e^\gamma$ and for the remark on cutoffs
$D\ge(\log N)^c$. Its statement is recorded in A. Granville, *Harald Cramér
and the distribution of prime numbers*, Scand. Actuar. J. 1995, no. 1,
12--28, equation (1), printed p. 13, as extracted on the linked source
card. That card was read at statement scope; no proof or new page image
was checked for this use.

The erdosproblems.com discussion, accessed 16 October 2026, supplies
congruence constructions and Tao's inverse-theorem proposal; it supplies
no inverse theorem. The known AlphaProof results settle parts (i) and
(ii). The reciprocal-sum claim on the proof-claims tab is the already
[[problems/integer_sequences/E0012/claims/2026_07_30_ndikum_ndikum|rejected claim whose growth axiom is false]].
The same day's inspected erdosproblems.ai, Palomar, arXiv and
formal-conjectures records yielded no additional full claim for part (iii).
That is a bounded source finding, not certification of openness.
