---
name: research/leads/aliquot_collision_density
title: Collision Counts for the Sum of Proper Divisors
desc: |
  Problem 955 is equivalent to linear collision bounds after arbitrarily
  small input deletions; density-zero deletions cannot suffice. A small
  cofactor and large primes give explicit class equations. The large-prime
  sieve is proved, with an open large-divisor core. Full equations with
  at least three primes have a proved local average but an open global
  prime count. A census through 10^10 proves no asymptotic bound.
problems:
- 955
research_state: ready
review_status: needs_update
created: 2026-10-16T14:07:43Z
updated: 2026-10-17T05:45:32Z
---

# Collision Counts for the Sum of Proper Divisors

[[research/leads/_index|..]]

[[research/leads/aliquot_collision_density/evidence/_index|evidence/]]: Exact census of collisions s(n) = s(n') through 10^10 in classes cut out by s(n)/n, by the number of prime factors and by the largest prime factor, with an independent small-range reference and external count checks.

[[research/leads/aliquot_collision_density/large_prime_class_average|large_prime_class_average]]: Exact local factors and a Brun–Titchmarsh compatibility argument bound the
averaged sieve input G1 of the large-prime class, after removing few
inputs, except for common divisors of s(a) and s(a') that divide a'-a and
exceed every prime factor of both cofactors by a fixed power; that core
is open.

[[research/leads/aliquot_collision_density/rough_prime_local_density|rough_prime_local_density]]: For at least three free primes on each side, the collision polynomial has
uniformly summable local factors away from its coefficients. After a
negligible removal of small cofactors, their full local majorants have
the required reciprocal-weighted average. The count of prime solutions
in integer boxes remains unproved.

[[research/leads/aliquot_collision_density/uniform_two_form_sieve|uniform_two_form_sieve]]: An elementary Selberg-weight construction proves the uniform sieve input
G0 for the large-prime class, including nonprimitive forms, the interval
enlargement and a remainder absorbed uniformly in the main term.

***

This lead's results that are not drawn from a cited source are Plasma AI's,
credited to Plasma AI.

## Current review

The independent [review](evidence/verify/analytic_conclusions/review.md) of
2026-10-16, accepted by a separate
[grade](evidence/verify/analytic_conclusions/grade.md), found Theorems A and B
and every specified analytic mathematical consequence through the semiprime
separation inequality **refutation-failed**. This records the grader's tier-1
judgment for those exact propositions at the source interfaces retained in the
[verification record](evidence/verify/analytic_conclusions/_index.md).
It establishes neither (D) nor a solution of Problem 955. The numerical
census, the G0/G1/G2 route and the rough-prime classes are outside that
examination and retain author standing.

The [frozen subject](evidence/assets/analytic_conclusions/subject.md) contains
an unsupported assertion about what is known concerning equivalence of (D).
Affirmative certification of that assertion is **void**; no disproof is given.
The current D paragraph makes only the grade-authorized body correction to
"The argument does not establish the converse." Other examined mathematical
statements and proofs are unchanged, apart from standing descriptions.
The [later excerpt](evidence/assets/analytic_conclusions/later_wording.md)
is separately identified and was not the reviewer's subject.

The reviewer received excluded motivational advocacy, which the separate
grader ruled immaterial to this examination under the content test. The
exposure and ruling remain disclosed. The external PNT, Mertens and PPT
premises were checked at their supplied statement interfaces; original
source proofs and PDF fidelity are not certified.

## Target and conventions

The target is
[[problems/arithmetic_functions/E0955/_index|Problem 955, whose page records the general assertion as open]]:
for $s(n)=\sigma(n)-n$, does every set $A\subseteq\mathbb N$ of natural
density zero have a preimage $s^{-1}(A)$ of natural density zero? Nothing on
this page changes that status.
Here inputs are positive integers, and $s(1)=0$.

For $x\ge1$ and $m\ge0$ write $r_x(m)=\#\{n\le x:s(n)=m\}$. For a set $S$ of
admitted inputs, which may depend on $x$, write $r_{S,x}(m)$ for the number
of $n\in S\cap[1,x]$ with $s(n)=m$, $R_S(x)=\#(S\cap[1,x])$, and

$$
C_S(x)=\sum_m r_{S,x}(m)^2
=\#\{(n,n')\in(S\cap[1,x])^2:\ s(n)=s(n')\}.
$$

Pairs are ordered and the diagonal $n=n'$ is included. So $C_S(x)-R_S(x)$
counts the ordered pairs of distinct inputs with equal values, and
$(C_S(x)-R_S(x))/2$ the unordered ones.

The route recorded here is the second-moment route: if few pairs collide,
Cauchy–Schwarz bounds the number of inputs that any sparse target can
capture. The sections below show which form of that route is false, which
form is exactly as strong as the problem, and what an exact computation
shows about each.

## The density-zero form is false

The proposed form removes a density-zero set of degenerate inputs, such as
the semiprimes with $s(pq)=p+q+1$ for distinct primes $p,q$, and asks for
$C_S(x)=O(x)$ for the rest.
No density-zero exclusion can give this.

**Theorem A.** Let $E_x\subseteq[1,x]$ satisfy $|E_x|=o(x)$ and put
$S_x=[1,x]\setminus E_x$. Then $C_{S_x}(x)/x\to\infty$.

*Proof.* Fix $\delta\in(0,1/10]$ and put $z=1/\delta$ and $Z=100z$. Let
$\mathcal R_Z$ be the set of positive integers with no prime factor at most
$Z$ (so $1\in\mathcal R_Z$), let $m_Z=\prod_{q\le Z}(1-1/q)$, and let
$f(k)=\sum_{q\mid k}1/(q-1)$, summed over the primes $q$ dividing $k$.

*A class with small $s(n)/n$.* Let $V_\delta$ be the set of $n=pk$ with $p$
prime, $z/1.8<p\le z/1.1$, $k\in\mathcal R_Z$ and $f(k)\le\delta/10$. Since
$p<Z$, $p\nmid k$, so $\sigma(n)/n=(1+1/p)\,\sigma(k)/k$ and

$$
1\le\frac{\sigma(k)}{k}\le\prod_{q\mid k}\Bigl(1-\frac1q\Bigr)^{-1}
\le e^{f(k)}\le1+0.11\,\delta,
$$

so $\delta\le1/p\le s(n)/n\le(1+1.8\delta)(1+0.11\delta)-1\le2\delta$. The
pair $(p,k)$ is determined by $n$, since $p$ is the only prime factor of $n$
at most $Z$.

*Its size.* $\mathcal R_Z$ is a union of residue classes modulo
$\prod_{q\le Z}q$, so $\#(\mathcal R_Z\cap[1,y])=m_Zy+O_Z(1)$. For a prime
$q>Z$, the members of $\mathcal R_Z$ divisible by $q$ are exactly the $qk'$
with $k'\in\mathcal R_Z$. Hence

$$
\sum_{\substack{k\le y\\ k\in\mathcal R_Z}}f(k)
=\sum_{Z<q\le y}\frac{\#(\mathcal R_Z\cap[1,y/q])}{q-1}
\le m_Zy\sum_{m>Z}\frac1{m(m-1)}+O_Z(\log\log y)
\le\frac{1.01\,m_Zy}{Z}+O_Z(\log\log y),
$$

using $\sum_{m>Z}1/(m(m-1))=1/\lfloor Z\rfloor$ and $Z\ge1000$. By Markov's
inequality at most $(10/\delta)\,1.01\,m_Zy/Z+o(y)\le0.11\,m_Zy+o(y)$
members of $\mathcal R_Z\cap[1,y]$ have $f(k)>\delta/10$. Summing over the
finitely many $p$,

$$
\#(V_\delta\cap[1,x])\ge(d_\delta-o(1))\,x,\qquad
d_\delta=0.89\,m_Z\sum_{z/1.8<p\le z/1.1}\frac1p.
$$

As $\delta\to0$, Mertens' product theorem gives
$m_Z\sim e^{-\gamma}/\log(1/\delta)$ and the prime number theorem gives
$\sum_{z/1.8<p\le z/1.1}1/p\sim\log(18/11)/\log(1/\delta)$. Since
$0.89\,e^{-\gamma}\log(18/11)>0.24$, every sufficiently small $\delta$ has
$d_\delta\ge0.2/\log^2(1/\delta)$. The convergence is slow, because
$\log Z=\log(1/\delta)+\log100$; the bound is asymptotic and is not claimed
for every $\delta\le1/10$.

*Pigeonhole.* The set $N_x=(V_\delta\cap[1,x])\setminus E_x$ has at least
$(d_\delta-o(1))x$ members, and their values $s(n)$ lie in $[1,2\delta x]$.
By Cauchy–Schwarz over those values,

$$
C_{S_x}(x)\ge\sum_{m\le2\delta x}r_{N_x,x}(m)^2\ge\frac{|N_x|^2}{2\delta x}
\ge\frac{(d_\delta-o(1))^2}{2\delta}\,x .
$$

So $\liminf_x C_{S_x}(x)/x\ge d_\delta^2/(2\delta)\ge
0.02/(\delta\log^4(1/\delta))$ for every small $\delta$, which is unbounded
as $\delta\to0$. $\square$

The mechanism is general: the inputs of $V_\delta$, whose least prime factor
is near $1/\delta$ and whose other prime factors are large, have their values
in $[1,2\delta x]$ although they range over $[1,x]$, and they form a
proportion of order $1/\log^2(1/\delta)$ of all inputs. The degenerate
families that an exclusion is meant to remove, such as the semiprimes, are
only the extreme case. The same argument with $|E_x|\le\varepsilon x$ gives

$$
\liminf_{x\to\infty}\frac{C_{S_x}(x)}{x}
\ge\sup_{\delta:\ d_\delta>\varepsilon}\frac{(d_\delta-\varepsilon)^2}{2\delta},
$$

and taking $\delta=\exp(-\sqrt{0.1/\varepsilon})$, where
$d_\delta\ge2\varepsilon$ for small $\varepsilon$, shows that the right side
is at least $(\varepsilon^2/2)\exp(\sqrt{0.1/\varepsilon})$. Any constant $K$ in
the corrected form below must therefore grow faster than every power of
$1/\varepsilon$.

This proof has the independent review and grade described above. Its external
inputs are the prime number theorem and Mertens' product theorem, at the
retained statement-interface reading depth.

## An equivalent form of the problem

The second-moment route loses nothing in principle once the exceptional set
may have small positive density and the constant may depend on it.

**Theorem B.** The following are equivalent.

1. Every $A\subseteq\mathbb N$ of natural density zero has $s^{-1}(A)$ of
   natural density zero.
2. The fiber sizes are tight:
   $\lim_{T\to\infty}\limsup_{x\to\infty}x^{-1}\#\{n\le x:r_x(s(n))>T\}=0$.
3. For every $\varepsilon>0$ there are $K$ and $x_0$ such that every
   $x\ge x_0$ has a set $E_x\subseteq[1,x]$ with $|E_x|\le\varepsilon x$ and
   $C_{[1,x]\setminus E_x}(x)\le Kx$.
4. For every $\varepsilon>0$ there are $\eta>0$ and $x_0$ such that
   $\#\{n\le x:s(n)\in B\}\le\varepsilon x$ for every $x\ge x_0$ and every
   set $B\subseteq\mathbb N\cup\{0\}$ of at most $\eta x$ integers.

*Proof.* (2 ⇒ 3) Given $\varepsilon$, choose $T$ and $x_0$ with
$\#\{n\le x:r_x(s(n))>T\}\le\varepsilon x$ for $x\ge x_0$, and let $E_x$ be
that set. Every value taken on $[1,x]\setminus E_x$ is taken at most $T$
times there, so
$C_{[1,x]\setminus E_x}(x)\le T\,R_{[1,x]\setminus E_x}(x)\le Tx$.

(3 ⇒ 1) Let $A$ have density zero, and fix $\varepsilon>0$ and $L\ge1$. For
$x\ge x_0$ the inputs $n\le x$ with $s(n)\in A$ are of three kinds. At most
$\varepsilon x$ lie in $E_x$. Those with $s(n)>Lx$ have
$\sigma(n)/n>L+1$, and

$$
\sum_{n\le x}\frac{\sigma(n)}n=\sum_{d\le x}\frac1d\Bigl\lfloor\frac xd
\Bigr\rfloor\le\zeta(2)\,x
$$

bounds their number by $2x/L$. The rest have values in $A\cap[0,Lx]$, and
Cauchy–Schwarz bounds them by $(|A\cap[0,Lx]|\cdot Kx)^{1/2}=o(x)$. So the
upper density of $s^{-1}(A)$ is at most $\varepsilon+2/L$ for all
$\varepsilon$ and $L$.

(1 ⇒ 2) Suppose (2) fails. The quantity in (2) is nonincreasing in $T$, so
there is $\eta>0$ such that for every $T$ arbitrarily large $x$ have
$\#\{n\le x:r_x(s(n))>T\}>\eta x$. Write $m_w=\prod_{p\le w}(1-1/p)$ and fix
$L\ge4$ with $L^{-1/2}+m_{\sqrt L}\le\eta/4$. An input $n\in(x/\sqrt L,x]$
with $s(n)<x/L$ has $\sigma(n)/n<1+L^{-1/2}$, hence no prime factor at most
$\sqrt L$; so $\#\{n\le x:s(n)<x/L\}\le(\eta/4)x+O_L(1)$. Put $x_0=1$ and
choose inductively $x_k$ with $\#\{n\le x_k:r_{x_k}(s(n))>k\}>\eta x_k$,
$x_k\ge k^2L\,x_{k-1}$ and $O_L(1)\le\eta x_k/4$, and let

$$
A_k=\{m\ge x_k/L:\ r_{x_k}(m)>k\},\qquad A=\bigcup_kA_k .
$$

Then $\#\{n\le x_k:s(n)\in A\}\ge\eta x_k-(\eta/2)x_k$, so $s^{-1}(A)$ has
upper density at least $\eta/2$. On the other hand
$|A_k|<x_k/k$, because $\sum_mr_{x_k}(m)\le x_k$, so
$\sum_{j<k}|A_j|<\sum_{j<k}x_j\le k\,x_{k-1}$. If $k$ is the largest index
with $x_k/L\le y$, then $A\cap[1,y]\subseteq A_1\cup\dots\cup A_k$ and

$$
\frac{|A\cap[1,y]|}{y}\le\frac{L}{x_k}\Bigl(\frac{x_k}{k}+k\,x_{k-1}\Bigr)
\le\frac{L}{k}+\frac1k ,
$$

so $A$ has density zero and (1) fails.

(2 ⇔ 4) If (2) holds, choose $T$ with $\#\{n\le x:r_x(s(n))>T\}\le\varepsilon
x/2$ for large $x$ and put $\eta=\varepsilon/(2T)$: a set $B$ of at most
$\eta x$ values captures at most $\varepsilon x/2$ inputs in fibers larger
than $T$ and at most $T\eta x$ others. If (4) holds, take $T=1/\eta$; the set
$B=\{m:r_x(m)>T\}$ has fewer than $x/T=\eta x$ members, so it captures at
most $\varepsilon x$ inputs. The quantity in (2) is therefore at most
$\varepsilon$ for every $T\ge1/\eta$, and $\varepsilon$ is arbitrary.
$\square$

This proof has the independent review and grade described above. Statement 4
places the problem beside
[[../library/arithmetic_functions/pollack_2018_divisor_sum_fibers/theorem_1_2|Pollack, Pomerance and Thompson's Theorem 1.2, which proves the same uniform control for targets of total size at most $x^{1/2+\epsilon(x)}$]]:
the problem asks for it at size $\eta x$, with $\varepsilon\to0$ as
$\eta\to0$. The problem page's countermodel shows that control at the smaller
size cannot be extended by an abstract argument; Theorem B says that control
at linear size is exactly what is needed.

Statement 3 is the corrected form of the route. Its natural explicit version
uses the sets

$$
D(\delta)=\{n\ \text{composite}:\ s(n)\ge\delta n\}.
$$

An input outside $D(\delta)$ is $1$, a prime, or has no prime factor at most
$1/\delta$, so the complement of $D(\delta)$ has upper density at most
$\prod_{p\le1/\delta}(1-1/p)\to0$. The bound

$$
\text{(D)}\qquad C_{D(\delta)}(x)\le K_\delta\,x\quad\text{for every fixed
}\delta>0\text{ and all large }x
$$

therefore implies statement 3, by choosing $\delta$ with
$\prod_{p\le1/\delta}(1-1/p)<\varepsilon$ and
$E_x=[1,x]\setminus D(\delta)$, and hence the problem. The argument does not establish the converse. The class $V_\delta$ of Theorem A, apart from its finitely many
primes, lies in $D(\delta)$, so the pigeonhole step gives
$K_\delta\ge0.02/(\delta\log^4(1/\delta))$ for small $\delta$, and
$K_\delta\to\infty$. The semiprimes in $D(\delta)$ are harmless. For
distinct primes $p<q$, $s(pq)=p+q+1\ge\delta pq$ forces $p\le3/\delta$, and
$s(p^2)=p+1$ comes from one prime square at most; so each value is taken by
at most $\pi(3/\delta)+1$ semiprimes in $D(\delta)$, and they contribute at
most $(\pi(3/\delta)+1)x$ to the sum of squares, which
$(r_1+r_2)^2\le2r_1^2+2r_2^2$ separates from the rest.

## Exact census through 10^10

The census computes $R$ and $C$ exactly for composite inputs $n\le x$ in the
classes

$$
D_k=\{n\ \text{composite}:\ 2^ks(n)\ge n\},\qquad
DT_k=\{n\in D_k:\ \Omega(n)\ge3\},
$$

for $k=0,\dots,14$, and for all composites, written $Q$, and the composites
with $\Omega(n)\ge3$, written $T$; $\Omega$ counts prime factors with
multiplicity. So $D_k=D(2^{-k})$, $D_0$ is the set of abundant and perfect
composites, and $T$ is the proposed density-zero exclusion: it removes $1$,
the primes and every input with exactly two prime factors, including the
prime squares with $s(p^2)=p+1$. By Landau's estimate at most
$O(x\log\log x/\log x)$ inputs $n\le x$ are removed, so the excluded set has
density zero, as the proposed route requires. The checkpoints are
$x=\lfloor10^{3+j/4}\rfloor$, $j=0,\dots,28$, so the range reaches $10^{10}$.
All arithmetic is exact. The program and its checks are described in
[the evidence record](evidence/_index.md).

The ratio $C/x$ at each decade, rounded to four decimals:

| $x$ | $Q$ | $T$ | $D_0$ | $D_2$ | $D_4$ | $D_6$ | $DT_2$ | $DT_4$ | $DT_6$ |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| $10^5$ | 3.2315 | 1.3879 | 0.3802 | 1.4514 | 1.9332 | 2.4930 | 1.1948 | 1.3790 | 1.3879 |
| $10^6$ | 4.3050 | 1.6220 | 0.3944 | 1.5132 | 2.0265 | 2.5000 | 1.2978 | 1.5557 | 1.6220 |
| $10^7$ | 6.0138 | 1.8504 | 0.4042 | 1.5533 | 2.0698 | 2.6320 | 1.3686 | 1.6666 | 1.8450 |
| $10^8$ | 9.0391 | 2.0798 | 0.4098 | 1.5758 | 2.0949 | 2.6833 | 1.4142 | 1.7427 | 1.9890 |
| $10^9$ | 14.8769 | 2.3232 | 0.4128 | 1.5893 | 2.1101 | 2.6986 | 1.4458 | 1.7977 | 2.0846 |
| $10^{10}$ | 26.8423 | 2.5949 | 0.4143 | 1.5968 | 2.1186 | 2.7121 | 1.4676 | 1.8377 | 2.1603 |

At $x=10^9$ the exact restricted values are $C_T=2323154413$ and
$R_T=788363929$, with $211636071$ excluded inputs. At $x=10^{10}$ the
exact values are $C_T=25949106637$ with
$R_T=8051171045$, $C_{D_0}=4143350299$ with $R_{D_0}=2476238927$, and
$C_{D_4}=21185514129$ with $R_{D_4}=8188172635$. The proportions of
$n\le10^{10}$ outside each class are $0.1949$ for $T$, $0.7524$ for $D_0$,
$0.2997$ for $D_2$, $0.1812$ for $D_4$ and $0.1280$ for $D_6$.

**Reading.** No numerical tolerance for leveling off was fixed in advance.
This page reads "levels off" as decade increments of $C/x$ that shrink from
one decade to the next, and "does not level off" as increments that do not
shrink. The reading was chosen when the computation was made, so the census is
exploratory evidence, not a test of a prediction stated in advance.

- The ratio for $Q$ rises by a factor of about $1.8$ from $10^9$ to
  $10^{10}$. Balanced semiprimes alone force superlinear collisions: there
  are $\gg x/\log^2x$ distinct products $pq$ with
  $\sqrt x/2<p<q\le\sqrt x$, and their values $p+q+1$ occupy
  $O(\sqrt x)$ integers. Cauchy–Schwarz therefore gives
  $C_Q(x)\gg x^{3/2}/\log^4x$. This aggregate argument uses the prime
  number theorem; it asserts no estimate for any individual Goldbach sum.
- $T$ does not level off. Its decade increments from $10^6$ to $10^{10}$ are
  $0.228$, $0.229$, $0.243$ and $0.272$. Theorem A
  predicts unbounded growth for every density-zero exclusion, but its
  pigeonhole bound is far below this observed rate at these scales; the
  observed rate is not derived here. The growth sits in
  inputs with small $s(n)/n$. At $10^6$ the classes $T$ and $DT_6$ differ by
  seven inputs, the prime cubes $p^3$ with $64<p<100$, and their ratios agree
  to four decimals; at $10^{10}$ the ratios differ by $0.435$, and $DT_6$
  alone decelerates.
- Every $D_k$ with $k\le7$ and every $DT_k$ with $k\le6$ levels off over the
  last three decades. From $10^6$ to $10^{10}$ the increments of $D_0$ are
  $0.0098$, $0.0055$, $0.0030$, $0.0015$; of $D_4$ $0.0434$, $0.0251$,
  $0.0152$, $0.0085$; of $DT_2$ $0.0708$, $0.0457$, $0.0315$, $0.0219$; of
  $DT_6$ $0.2230$, $0.1440$, $0.0956$, $0.0757$. Classes with larger $k$ are
  still in transition: the restriction $s(n)\ge2^{-k}n$ removes nothing
  when $x\le4^k$, since $s(n)>\sqrt n$ for composite $n$.
- Large fibers are rare in the restricted classes. At $10^{10}$ the largest
  value multiplicity is $47$ in $D_0$ and $68$ in $D_4$, against $124$ in $T$;
  the number of admitted inputs lying in fibers of more than eight inputs,
  divided by $x$ rather than by $R_S(x)$, is $0.0007$ in $D_0$, $0.0128$ in
  $D_4$ and $0.0472$ in $T$.

**Split by the largest prime factor.** A second run of the census flags the
inputs whose largest prime factor exceeds $\sqrt n$, a set of density
$\log2$, which is the model of the class S1 of the sketch below; the other
composites model S2. The table gives the ordered off-diagonal pairs per
input range, $(C-R)/x$, inside S1, inside S2, and across the two (both
orders), within $D_k$:

| $x$ | S1, $k=0$ | S2, $k=0$ | across, $k=0$ | S1, $k=2$ | S2, $k=2$ | across, $k=2$ | S1, $k=4$ | S2, $k=4$ | across, $k=4$ |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| $10^6$ | 0.0512 | 0.0227 | 0.0730 | 0.4287 | 0.0618 | 0.3226 | 0.6171 | 0.0967 | 0.4930 |
| $10^7$ | 0.0601 | 0.0225 | 0.0740 | 0.4580 | 0.0657 | 0.3291 | 0.6679 | 0.0931 | 0.4898 |
| $10^8$ | 0.0667 | 0.0218 | 0.0737 | 0.4769 | 0.0678 | 0.3308 | 0.6905 | 0.0956 | 0.4900 |
| $10^9$ | 0.0715 | 0.0210 | 0.0727 | 0.4879 | 0.0691 | 0.3320 | 0.7002 | 0.0989 | 0.4922 |

For $k\le4$ the S1 and cross components level off, the S2 components for
$k\le2$ level off or decrease, and the S2 component for $k=4$ stays between
$0.093$ and $0.099$. The collisions inside S2 are far fewer than inside S1.
Without the restriction the S2 part does not level off: over all composites
with no prime factor above $\sqrt n$, $(C-R)/x$ is $0.1267$, $0.1667$,
$0.2158$ and $0.2779$ at $10^6,\dots,10^9$, with growing increments, again
from inputs with small $s(n)/n$.

The census cannot prove any asymptotic statement, and over these few
decades it cannot separate convergence of $C/x$ from growth like
$\log\log x$. It does
show that the proposed density-zero route fails its own test already at these
scales, and that nothing in the corrected classes, or in their split by the
largest prime factor, contradicts (D).

## Proof sketch of the corrected route

**Target.** Statement 3 of Theorem B, through the sufficient bound (D) or
another family of exceptional sets whose upper densities tend to zero.
Theorems A and B have the independent review described above. The
argument in this section remains conditional on G1, whose trimmed form
is reduced to Gap G1-core below, and on G2. Its
coefficient-uniform sieve input G0 has a complete author-recorded proof.

**Splitting.** For a disjoint union of two admitted classes,
$(r_1+r_2)^2\le2r_1^2+2r_2^2$, so bounds for collisions inside the classes
control collisions between them too. A finite number of classes is allowed,
with that number depending on the discarded proportion.

**Class S1: a prime factor above $x^{1/2+\eta}$.** Fix $\delta>0$ and
$0<\eta<1/2$, put $y=x^{1/2-\eta}$, and let $S_1(x)$ consist of the
composite $n=aP\le x$ with $P$ prime, $P>x^{1/2+\eta}$ and
$s(n)\ge\delta n$. Then $P\nmid a$, $2\le a<y$, and

$$
s(aP)=s(a)P+\sigma(a).
$$

Since $\sigma(a)/a\le1+\log a$, the identity
$s(aP)/(aP)=s(a)/a+\sigma(a)/(aP)$ implies $s(a)\ge\delta a/2$ for
sufficiently large $x$, uniformly over these cofactors. The same cofactor
$a$ gives no off-diagonal collision because $s(a)>0$.

For $a\ne a'$ put $g=\gcd(s(a),s(a'))$ and
$h=\sigma(a')-\sigma(a)$. A collision requires

$$
s(a)P-s(a')P'=h,\qquad g\mid h.
$$

If $h=0$, there is no collision in these ranges: both large primes exceed
$s(a)$ and $s(a')$ for large $x$, so
$s(a)P=s(a')P'$ forces $P=P'$ and $s(a)=s(a')$; together with $h=0$ this
forces $a=a'$. For $h\ne0$ and $g\mid h$, write the integer solutions as

$$
P=u+\beta t,\quad P'=v+\lambda t,\qquad
\beta=s(a')/g,\quad\lambda=s(a)/g.
$$

The admissible parameters lie in an interval contained in one of length
$L=xg/(a\,s(a'))$. This is an upper length supplied by the first prime's
range, not a lower bound on the actual intersection of the two prime ranges.
It satisfies $L\ge x^{2\eta}/(1+\log x)$, so it is possible to enlarge the
interval to this length when seeking an upper bound.

For these pairs let $\omega_{a,a'}(p)$ be the number of residues $t$ modulo
$p$ where at least one of the two forms vanishes, and define

$$
\mathfrak S_z(a,a')=\prod_{p\le z}
\Bigl(1-\frac{\omega_{a,a'}(p)}p\Bigr)\Bigl(1-\frac1p\Bigr)^{-2}.
$$

A different integer solution $(u,v)$ translates $t$ and leaves this
quantity unchanged. Pairs with no solution, and pairs with $h=0$, are
omitted from the sum below; no singular series is needed for them.

**Uniform sieve input G0.** For every eligible pair,

$$
N(a,a')\ll_\eta
\frac{xg}{a\,s(a')\log^2x}\,\mathfrak S_x(a,a').
$$

The [coefficient-uniform two-form argument](uniform_two_form_sieve.md)
proves this by an explicit Selberg-weight construction. Its interval error
is bounded by $z^2(1+\log z)^{10}$, uniformly in all coefficients. With
$z=L^{1/4}$ and $L\ge x^{2\eta}/(1+\log x)$, this error is absorbed in the
main term, whose singular series has an absolute positive lower bound
whenever the forms are admissible. Nonprimitive forms and the obstruction
$\omega(2)=2$ give no prime pair in the stated range. The proof also
justifies the interval enlargement and the comparison of singular-series
cutoffs. G0 therefore needs no separate error sum and no unexamined
sieve theorem. It is author-recorded and outside the analytic review.

Set $\mathcal A_\delta(y)=\{2\le a\le y:s(a)\ge\delta a/2\}$ and

$$
\Lambda_\delta(y;z)=
\sum_{\substack{a,a'\in\mathcal A_\delta(y),\ a\ne a'\\
h\ne0,\ g\mid h}}
\frac{g\,\mathfrak S_z(a,a')}{aa'}.
$$

Summing G0 gives

$$
C_{S_1}(x)\ll_\eta x+
\frac{x}{\delta\log^2x}\Lambda_\delta(x^{1/2-\eta};x).
$$

**Gap G1 (averaged singular series).** The missing estimate is
$\Lambda_\delta(x^{1/2-\eta};x)\ll_{\delta,\eta}\log^2x$ for every fixed
$\delta,\eta$. The prime cutoff and the cofactor cutoff are distinct in this
statement. For statement 3 of Theorem B a trimmed form suffices: the same
bound after removing a set of cofactors $a<y$ with
$\sum1/a\le\varepsilon'\log y$, whose inputs number at most
$2\varepsilon'x$. The trimmed form is not G1 as stated for every cofactor,
and it does not prove (D) for the whole class.

The [averaged estimate for the large-prime class](large_prime_class_average.md)
reduces the trimmed form to one estimate, at author standing. Its local
lemmas are complete. For an eligible pair and a prime $p$, with $e_1=v_p(s(a))$,
$e_2=v_p(s(a'))$, $e=v_p(g)$ and $f=v_p(h)$, the factor of
$g\,\mathfrak S_x(a,a')$ is $p^ep/(p-1)$ when $e_1\ne e_2$ or $f>e$, and
$p^e(1-(p-1)^{-2})$ otherwise; a pair with $e_1\ne e_2$ and $f>e$ has no
prime solutions. If $v_p(\sigma(a))>v_p(a)$ and the same holds for $a'$,
the factor is exactly $p^{v_p(a)}p/(p-1)$, and the pair is excluded unless
$v_p(a)=v_p(a')$. Under independent geometric valuation frequencies
$\Pr(v_p(a)=e)=(1-1/p)p^{-e}$ this factor has mean

$$
\sum_{e\ge0}(1-1/p)^2p^{-2e}\,p^e\frac p{p-1}=1,
$$

which is why the small primes balance. The page then restricts to good
cofactors: their two largest primes exceed $y^\nu$, $(a,\sigma(a))$ has no
prime factor above $W=\log\log y/(4\log\log\log y)$, and $\sigma$ satisfies
the small-prime condition above at the cofactor $a/P(a)$; the others carry
reciprocal weight $O(\nu\log(1/\nu)\log y)$. For good cofactors, every
divisor $d$ of the part of $g$ above $W$ fixes the largest prime of $a$
modulo $d$, and the congruence $a\equiv a'\pmod d$ restricts the second
largest prime through a quadratic congruence. Removing a further set of
reciprocal weight $o(\log y)$ ensures that no prime above $W$ divides
both $s(a)$ and $P(a)-P_2(a)$. The quadratic roots representing retained
cofactors are then simple, giving at most $2^{\omega(d)}$ classes modulo
$d$, including all its prime powers. With Brun–Titchmarsh
this bounds by $O(\log^2y)$ every part of the trimmed sum except the
divisors $d$ with $d\ge\max(P(a),P(a'))^{1-\kappa}$, for a fixed small
$\kappa>0$. The density of these good cofactors and the averages of the
small-prime and singular-series weights are proved there, with constants
not computed explicitly.

**Gap G1-core.** Bound by $O(\log^2y)$ the part of the trimmed sum coming
from common divisors $d$ of $s(a)$ and $s(a')$ that divide $a'-a$ and
satisfy $d^{1/(1-\kappa)}\ge\max(P(a),P(a'))$. When such a $d$ exceeds
$P(a)$, the prime $P(a)$ is the least positive residue of
$-\sigma(c)s(c)^{-1}$ modulo $d$, where $c=a/P(a)$. The estimate asks
that these least residues fall in short initial intervals no more often
than their length predicts, on average over the pairs. Counting
arguments on the linked page remove further core divisors: those for which
a cofactor has its largest prime above $d^{1-\kappa''}$, for a small fixed
$\kappa''$; those for which the two cofactors' largest primes have product
at least $d^{1+\epsilon}$; and those for which one cofactor's two largest
primes have product at least $d^{1+\epsilon}$. The simple-root condition
makes these removals valid without a restriction on the radical of $d$.
What remains are large divisors exceeding, up to the factor $d^\epsilon$, the
product of the two largest of these primes. It is not a local-factor
question; it is the same kind of input as the slice estimate G2-bal
below.

The reduced coefficients $u=s(a)/g$, $v=s(a')/g$ of an eligible pair
satisfy
$\max(u,v)>\prod_{p\le W}p/(1+2/\delta)$, by Lemma 7 of the linked
page. In particular $s(a)=s(a')$ gives no retained eligible pair for
large $y$. A descent must therefore control scaled collisions with
unbounded reduced coefficients and the extra congruence, rather than
just ordinary cofactor fibers. Removing the largest primes produces
affine equations with a generally nonzero right side; no contracting
recurrence is derived. Luca and Pomerance avoid
this regime only through cofactors $m=q\ell$ with $\ell\le x^{1/10}$, as
recorded on the linked page.

**What S1 would give.** G0 and G1 imply $C_{S_1}(x)\ll_{\delta,\eta}x$.
G0 with the trimmed form of G1 implies the same bound after removing at
most $\varepsilon x$ inputs, for each $\varepsilon>0$.
The upper-output truncation in Theorem B then gives
$\#\{n\in S_1(x):s(n)\in A\}=o(x)$ for every density-zero $A$.
The number of integers with a prime factor above $x^{1/2+\eta}$ is
$(\log(2/(1+2\eta))+o(1))x$, by summing $\lfloor x/P\rfloor$ over
those primes; the factor is unique. The discarded condition
$s(n)<\delta n$, together with the primes, has upper density tending to
zero as $\delta\to0$. Therefore G0 and either form of G1 for every
$\delta,\eta$ would bound the upper density of $s^{-1}(A)$ by $1-\log2$.
This is conditional partial progress, not a conclusion proved by the
census or by this sketch.

**Class S2: the remaining inputs.** Define
$S_2(x)=(D(\delta)\cap[1,x])\setminus S_1(x)$. The unrestricted complement of
the large-prime class has density $1-\log(2/(1+2\eta))$, tending to $1-\log2$
as $\eta\to0$; it cannot be discarded as a density-zero family.

The S1 argument supplies no uniform long parameter interval for S2. On input
intervals comparable to $x$, cofactors can exceed $\sqrt x$; for pairs with
small $g$ the upper interval length is then only $O(1)$ or smaller. This
defeats that particular uniform application of the sieve, not every possible
use of a large prime factor or another parametrization.

**Gap G2.** Prove $C_{S_2}(x)\ll_{\delta,\eta}x$, or replace this estimate by
another decomposition that proves Theorem B's statement 3. The section on
rough-prime classes below gives such a decomposition. It reduces the
smooth inputs to explicit collision equations in boundedly many primes,
proves that the uncovered proportion tends to zero, and identifies a
failure of summing a unit error over every pair of short-slice fixed parts.

**Standing and composition.** Theorems A and B and the implication
(D) $\Rightarrow$ E0955 have the independent review and separate grade
described above; (D) itself remains unproved. G0 has the author-recorded uniform
sieve proof linked above; G1 is reduced, in its trimmed form, to Gap
G1-core; G2 is the unresolved
smooth-input estimate. For every $\delta$, G0 and G1 together
with G2 at one fixed $\eta\in(0,1/2)$ would give (D), because
$C_{D(\delta)}(x)\le2C_{S_1}(x)+2C_{S_2}(x)$; with the trimmed forms of
G1 and G2 they would give statement 3 of Theorem B instead. Theorem B
then supplies the image truncation and the density conclusion. Theorem C below replaces this
split by rough-prime classes whose collision bounds would give statement 3
without (D). The finite census proves none of G0, G1, G2 or the class
bounds. There is no full proof of E0955 here.

The density-zero exclusion route is closed by the independently reviewed
Theorem A at its stated source interfaces.
Changing which density-zero family is removed cannot reopen it. Allowing
an arbitrarily small positive discarded proportion gives the distinct,
still-open route of Theorem B; establishing that reformulation does not
establish its equivalent asymptotic assertion.

## Rough-prime classes

This section gives a decomposition that meets statement 3 of Theorem B
directly. Outside a set of at most $\varepsilon x$ inputs, every input is a
small cofactor times a bounded number of distinct large primes, so G2 becomes
a finite family of explicit collision equations. The section describes
the estimates needed for these equations and the limitation of summing
unit errors over all short slices. Theorem C, the identities and
Proposition D below are complete
author-recorded arguments, outside the review described above. The
[full-equation local calculation](rough_prime_local_density.md) gives an
alternative that can omit every fixed finite list of small prime counts;
its remaining gap is the global count G2-full below. The gaps G2-quad,
G2-bal and G2-full are open.

**Classes.** Fix $0<\theta<\tau<1$ and $\delta>0$, and put $y=x^\theta$. For
$n\le x$ let $b(n)$, the product of the prime powers $p^a\,\|\,n$ with
$p\le y$, be its $y$-smooth part, and let $e(n)=n/b(n)$ be its $y$-rough part.
For $k\ge1$ let $\mathcal S_k(x)$ be the set of $n\in D(\delta)\cap[1,x]$ with
$b(n)\le x^\tau$ whose rough part $e(n)$ is squarefree with exactly $k$ prime
factors. Writing $P(b)$ for the largest prime factor of $b$, with $P(1)=1$,
its members are

$$
n=bP_1\cdots P_k,\qquad P(b)\le x^\theta<P_k<\dots<P_1,\qquad b\le x^\tau,
$$

and $k<1/\theta$, since $x^{k\theta}<e(n)\le x$. Since
$\sigma(e)/e=\prod_i(1+1/P_i)\le\exp(x^{-\theta}/\theta)$, membership in
$D(\delta)$ forces $s(b)\ge\delta b/2$ for large $x$; in particular $b\ge2$.

**Theorem C.** (i) For every $x$ with $x^\theta\ge2$, with an absolute
implied constant,

$$
\#\Bigl((D(\delta)\cap[1,x])\setminus\bigcup_{1\le k<1/\theta}
\mathcal S_k(x)\Bigr)
\le\frac\theta\tau\,x+O\Bigl(\frac{x}{\tau\log x}\Bigr)
+\frac{2x}{x^\theta}+x^\tau .
$$

(ii) Suppose that there is $\tau\in(0,1)$ such that for every $\delta>0$,
every $\theta\in(0,\tau)$ and every $k<1/\theta$ there are $K$ and $x_0$ with
$C_{\mathcal S_k(x)}(x)\le Kx$ for all $x\ge x_0$. Then every set of natural
density zero has a preimage under $s$ of natural density zero.

*Proof.* (i) An input $n\in D(\delta)\cap[1,x]$ in no class has
$b(n)>x^\tau$, or a rough part that is not squarefree, or $e(n)=1$. Since
$\log b(n)$ is the sum of $\log p$ over the prime powers $p^j\mid n$ with
$p\le y$,

$$
\sum_{n\le x}\log b(n)=\sum_{p\le y}\log p\sum_{j\ge1}
\Bigl\lfloor\frac{x}{p^j}\Bigr\rfloor
\le x\sum_{p\le y}\frac{\log p}{p-1}=x\,(\theta\log x+O(1))
$$

by Mertens' estimate $\sum_{p\le y}(\log p)/p=\log y+O(1)$, and Markov's
inequality bounds the inputs of the first kind by
$(\theta/\tau)x+O(x/(\tau\log x))$. A rough part that is not squarefree is
divisible by $p^2$ for some prime $p>y$, which happens for at most
$\sum_{p>y}x/p^2\le x/(y-1)\le2x/y$ inputs. If $e(n)=1$ and
$b(n)\le x^\tau$, then $n\le x^\tau$. Every other $n$ lies in
$\mathcal S_k(x)$, with $k$ the number of prime factors of $e(n)$.

(ii) Let $0<\varepsilon<1$. Choose $\delta$ with
$\prod_{p\le1/\delta}(1-1/p)<\varepsilon/3$ and put $\theta=\varepsilon\tau/3$.
An input outside $D(\delta)$ is $1$, a prime, or a composite with no prime
factor at most $1/\delta$, because a composite $n$ with a prime factor
$p\le1/\delta$ has $s(n)\ge n/p\ge\delta n$. The last kind is a union of
residue classes modulo $\prod_{p\le1/\delta}p$, so for large $x$ at most
$(\varepsilon/3)x+o(x)$ inputs lie outside $D(\delta)$. Let $E_x$ be the
complement in $[1,x]$ of the union of the classes. By (i),
$|E_x|\le\varepsilon x$ for large $x$. There are at most $1/\theta$ classes,
and
$(r_1+\dots+r_L)^2\le L(r_1^2+\dots+r_L^2)$ gives

$$
C_{[1,x]\setminus E_x}(x)\le\frac1\theta\sum_{1\le k<1/\theta}
C_{\mathcal S_k(x)}(x)\le\frac{K}{\theta^2}\,x
$$

for large $x$, with $K$ the largest of the finitely many class constants.
This is statement 3 of Theorem B. $\square$

Since $\mathcal S_k(x)\subseteq D(\delta)$ and $C_S$ increases with $S$, (D)
for every $\delta$ implies the hypothesis of (ii). The converse is not
shown, and the hypothesis of (ii) is not shown to follow from the problem.
The logarithmic prime sum in (i) has an elementary proof. The Chebyshev
bound established in the
[sieve argument](uniform_two_form_sieve.md#uniform-lower-bound-for-the-sieve-denominator)
gives $\sum_{p^j\le N}\log p\ll N+\sqrt N\log N\ll N$. For an integer
$N\ge2$, counting prime
factors in $N!$ and replacing each floor by its argument gives

$$
\log N!=\sum_{p^j\le N}\Bigl\lfloor\frac{N}{p^j}\Bigr\rfloor\log p
=N\sum_{p^j\le N}\frac{\log p}{p^j}+O(N).
$$

Integral bounds give $\log N!=N\log N-N+O(\log N)$, and
$\sum_{p,j\ge2}(\log p)/p^j=\sum_p(\log p)/(p(p-1))<\infty$.
This proves the stated logarithmic
prime sum, also for real $y$ by taking $N=\lfloor y\rfloor$. Thus the only
external asymptotic input of Theorem C is Mertens' product theorem. The
reduction fixes the shape of the inputs that need collision bounds and
proves none of those bounds.

**The class equations.** For $n=bP_1\cdots P_k\in\mathcal S_k(x)$,
multiplicativity of $\sigma$ gives

$$
s(n)=\sigma(b)\prod_{i\le k}(P_i+1)-b\prod_{i\le k}P_i ,
$$

an equation of degree $k$ in the primes whose coefficients $\sigma(b)$ and
$b$ are at most $x^{\tau+o(1)}$. For pairwise coprime $d,e_1,e_2$, expanding
$s(de)=\sigma(d)\sigma(e)-de$ gives the exact identity

$$
s(de_1)\,s(de_2)=s(d)\,s(de_1e_2)+d\,\sigma(d)\,s(e_1)\,s(e_2).
$$

Put $X_i=s(bP_i)=s(b)P_i+\sigma(b)$. Since $s(P)=1$ for a prime $P$, the
identity with $d=b$, $e_1=P_1$ and $e_2=P_2$ gives the two-prime identity

$$
s(b)\,s(bP_1P_2)=X_1X_2-b\,\sigma(b).
$$

With $e_1=P_1$ and $e_2=P_2P_3$ instead, the two-prime identity for $P_2P_3$
and $s(b)(P_2+P_3+1)=X_2+X_3-2\sigma(b)+s(b)$ give

$$
s(b)^2\,s(bP_1P_2P_3)=X_1X_2X_3-b\,\sigma(b)(X_1+X_2+X_3)
+b\,\sigma(b)\bigl(2\sigma(b)-s(b)\bigr).
$$

So inside $\mathcal S_1$ a collision is a linear equation in two primes.
Inside $\mathcal S_2$ it is the split quaternary quadric

$$
s(b')X_1X_2-s(b)X_1'X_2'=s(b')\,b\,\sigma(b)-s(b)\,b'\sigma(b')
$$

in four variables of the form $s(b)P+\sigma(b)$. Inside $\mathcal S_3$ it is
a cubic in six such variables, and inside $\mathcal S_k$ an equation of
degree $k$ in $2k$ primes.

**Full equations with at least three primes per input.** The
[local-density argument](rough_prime_local_density.md) gives a possible
replacement for the linear and quadratic slices. Fix $0<\beta<1/2$.
The number of prime divisors of a uniform $n\le x$ in
$(x^\theta,x^\beta]$ has mean
$M=\log(\beta/\theta)+o(1)$ and variance at most $M+o(1)$, by expanding
its first two moments. Thus, for every fixed $K<M$, the proportion of
inputs with at most $K$ prime factors above $x^\theta$ is at most
$(M+o(1))/(M-K)^2$. This proportion tends to zero as $\theta\to0$.
Theorem C's proof therefore still reaches Theorem B(3) if its class
estimates are required only for $k\ge3$: the small-$k$ classes can be
included in the discarded proportion.

For $b,b'\le y=x^\tau$, the linked page removes a set of reciprocal
weight $o(\log y)$ so that
$v_p(\sigma(b))>v_p(b)$ for $p\le W$ and
$p\nmid(b,\sigma(b))$ for $p>W$, where
$W=\log\log y/(4\log\log\log y)$, and likewise for $b'$. This removes
$o(x)$ class inputs. Let $\rho_{p^r}(b,b')$ be $p^r$ times the
probability that the two class polynomials agree modulo $p^r$ when
their $2k$ variables are independent units. For $k\ge3$ the page proves

$$
\rho_{p^r}(b,b')=1+O_k(p^{-2})
\quad\bigl(p>k,\ p\nmid b\sigma(b)b'\sigma(b')\bigr)
$$

uniformly in $r$, and $\rho_{p^r}\le1+O_k(p^{-1})$ at every prime
where each coefficient pair is primitive. At a small prime, unequal
valuations of $b,b'$ prevent an integer collision; equal valuations
$e$ give $\sup_r\rho_{p^r}=p^e p/(p-1)$. The corresponding local
majorant $\mathfrak U_k(b,b')$, defined there using these suprema and
set to zero for incompatible small-prime valuations,
satisfies

$$
\sum_{b,b'\ {\rm retained}}\frac{\mathfrak U_k(b,b')}{bb'}
\ll_k\log^2y.
$$

The continuous output density obtained by weighting each prime variable
with $dP/\log P$ is $O_{\delta,\theta,k}(1/(b\log x))$. On any fixed
output interval $[0,Cx]$, the local majorants times the overlaps of
these densities therefore have total $O(x)$.

**Gap G2-full.** Bound the off-diagonal prime solutions of the full
class equations by these local and continuous majorants with aggregate
error $O(x)$, uniformly over the growing cofactors and the prime boxes.
The diagonal contributes at most $x$. The proved local average does
not control this error. The full leading homogeneous form has a
singular locus of codimension four regardless of $k$, even though the
affine critical points at the coefficient-free primes are isolated.
Thus increasing the number of free prime variables supplies no
automatic point-counting theorem. With G2-full for all the retained
classes, Theorem C, the small-$k$ removal and Theorem B would finish the
whole target without G1-core or G2-quad. No such global estimate is
proved here.

**Slices.** Assume $\tau<1/2$ from here on; Theorem C(ii) allows any
$\tau\in(0,1)$. For a pair $(n,n')$ in one class and $1\le j\le k$, the
$j$-slice fixes the parts $d=n/(P_1\cdots P_j)$ and $d'=n'/(P_1'\cdots P_j')$
and leaves the $j$ largest primes of each input free. The colliding pairs with
given fixed parts are the prime solutions of the class equation with $b$
replaced by $d$ and $k$ by $j$, the free primes exceeding $P(d)$ and $P(d')$
respectively. There are about $x/d$ free $j$-tuples on one side and $x/d'$ on
the other, up to logarithmic factors, and the common value has size about $x$. A
heuristic count, not a proved estimate, therefore gives about $x/(dd')$
solutions for each pair of fixed parts, before logarithmic and local factors.
Any bound for a class obtained by bounding each pair of fixed parts separately,
with an error of at least one per pair, is at least the number of such pairs.

- The linear slice, $j=1$, is the S1 computation with cofactors $m=d$ and
  $m'=d'$, with two changes. When $h=0$ a collision with $P\ne P'$ forces
  $P\mid s(m')$, and a form vanishing identically modulo $p$ allows only
  $P=p$ or $P'=p$; these cases give $O(\log x)$ solutions per pair of fixed
  parts and need a count of their own, which is not made here. Otherwise
  the G0 argument, with a sieve exponent smaller than $\theta/2$,
  bounds a pair of fixed parts when
  $mm'\le x^{1-\epsilon}$, because the parameter interval then has length
  at least $x^{\epsilon}g/(1+\log x)$, and the analogue of G1 over the range
  $mm'\le x^{1-\epsilon}$ sums those bounds. Every pair in $\mathcal S_1$ is
  of this kind, with $mm'\le x^{2\tau}$.
- The quadratic slice, $j=2$, is the quaternary quadric with $b$ replaced by
  $d$. When $P_2P_2'\le x^{1-\epsilon}/(dd')$, fixing $P_2$ and $P_2'$ too
  reduces the pair to the linear slice. Otherwise each free prime lies
  within a factor $x^{\epsilon}\sqrt{dd'}$ of $\sqrt{x/d}$ or of
  $\sqrt{x/d'}$, on its own side. When the right side vanishes, for example
  when $d=d'$, the quadric becomes $s(d')X_1X_2=s(d)X_1'X_2'$, whose solutions
  include the diagonal and the coincidences between products of two such
  variables.
- The full slice, $j=k$, leaves only $b$ and $b'$ fixed, so
  $dd'\le x^{2\tau}$ and the heuristic count per pair is large, but the
  equation has degree $k$ in $2k$ primes.

**Gap G2-quad.** An upper bound of the heuristic order for the prime
solutions of the quaternary quadric, uniform in fixed parts with
$dd'\le x^{\gamma}$ for some fixed $\gamma>0$ and with congruence conditions
sufficient for a four-dimensional upper-bound sieve, together with the
matching average of its local factors and a count of the vanishing-right-side
components. With $\tau<\gamma/2$, G0, the G1 analogue for pairs that reduce
to the linear slice, and a bound for that slice's exceptional prime cases,
it would settle $\mathcal S_2$, whose
pairs all have $dd'\le x^{2\tau}$. None of these is proved here. A count of
points on a quaternary quadric with error a power below its main term, such
as a delta-method estimate, is a natural tool, but no uniform version has
been checked against these coefficients and boxes. The right side is
$\Delta(d,d')=d\sigma(d)s(d')-d'\sigma(d')s(d)$, the integer that governs
large common divisors in the
[large-prime average](large_prime_class_average.md). Its Lemma 5 shows that
$\Delta(d,d')=0$ forces $d=d'$ when both fixed parts satisfy
$v_p(\sigma(d))>v_p(d)$ for $p\le W$, have $(d,\sigma(d))$ free of primes
above $W$, and have the same part supported on primes up to $W$. Fixed
parts failing these conditions are not covered.

**Proposition D (the cost of summing errors over all short slices).** Let $J\ge1$ and
$k\ge2J$, put $\alpha=1/(k+1/2)$, and fix $\iota>0$ with
$k\alpha(1+\iota)<1$; then $c'=1-2J\alpha(1+\iota)>0$. Let $B_k(x)$ be the set
of $n=mp_1\cdots p_k$ with $x/2<n\le x$, $m$ even and $p_1,\dots,p_k$ distinct
primes in $(x^\alpha,x^{\alpha(1+\iota)}]$. Then $B_k(x)\subseteq D(1/2)$ and
$\#B_k(x)\ge(c_k-o(1))x$ with $c_k=(\log(1+\iota))^k/(4\cdot k!)$. For every
$j\le J$, every $j$-slice fixed part of a member of $B_k(x)$ exceeds
$x^{(1+c')/2}/2$, so every pair of them has $dd'>x^{1+c'}/4$, and for large
$x$ these fixed parts form at least $(c_k/2)^2x^{1+c'}$ pairs.

*Proof.* Since $\alpha>1/(k+1)$, every such $n$ has
$m\le x^{1-k\alpha}<x^\alpha$, so $p_1,\dots,p_k$ are exactly the prime factors
of $n$ above $x^\alpha$ and the representation is unique. For $p_1>\dots>p_k$
the $j$-slice fixed part is
$d=n/(p_1\cdots p_j)>x^{1-j\alpha(1+\iota)}/2\ge x^{(1+c')/2}/2$. An even
composite $n$ has $s(n)\ge n/2$. Counting the even $m$ in
$(x/(2p_1\cdots p_k),\,x/(p_1\cdots p_k)]$,

$$
\#B_k(x)\ge\frac x4\sum_{p_1<\dots<p_k}\frac1{p_1\cdots p_k}
-\pi\bigl(x^{\alpha(1+\iota)}\bigr)^k ,
$$

where Mertens' theorem gives $\sum_{x^\alpha<p\le x^{\alpha(1+\iota)}}1/p
=\log(1+\iota)+o(1)$, the distinctness condition costs $o(1)$ because
$\sum_{p>x^\alpha}p^{-2}\to0$, and the subtracted term is at most
$x^{k\alpha(1+\iota)}=o(x)$. A fixed part determines $n$ up to the choice of
$p_1,\dots,p_j$, so for large $x$ there are at least
$(c_k/2)\,x^{1-j\alpha(1+\iota)}\ge(c_k/2)\,x^{(1+c')/2}$ distinct fixed parts,
and at least $(c_k/2)^2x^{1+c'}$ pairs. $\square$

So for $j\le J$ the members of $B_k$ have heuristic count below
$4x^{-c'+o(1)}$ for every pair of $j$-slice fixed parts, and those pairs
exceed $x$ in number by a power. A summation that charges an error of at least one to every pair of
represented fixed parts therefore cannot bound their collisions by $O(x)$.
This does not count how many pairs remain after additional arithmetic
eliminations: such eliminations require their own argument. Their
positive density means that they cannot be deleted once $\varepsilon<c_k$.
For $\delta\le1/2$ and $\theta<\alpha$, a member of $B_k$ outside the
exceptions of Theorem C(i) lies in $\mathcal S_{k'}(x)$ for some $k'\ge k$,
and its $j$ largest primes are still $p_1,\dots,p_j$. Those exceptions number
at most $(\theta/\tau)x+o(x)$ and there are fewer than $1/\theta$ classes, so
once $\theta/\tau<c_k/2$ some class contains at least $\theta c_kx/3$ members
of $B_k$, and the counts above apply to them with a factor of order
$\theta^2$. The all-pairs error sum already fails for the linear slices of $B_2$,
and for the quadratic slices of $B_k$ with $k\ge4$. A proof confined to
separate slice bounds with such an error must allow arbitrarily large
slice degree as $\varepsilon\to0$. Proposition D concerns only that
summation rule. It does not show that the collisions of $B_k$ are
numerous, and it does not exclude other arguments.

**Gap G2-bal.** Bound the collisions of inputs whose large primes are
comparable, such as $B_k$ for $k\ge4$, by an argument that does not bound
each pair of short-slice fixed parts separately. Two forms of the missing
input are visible.

- Detect slice solutions on average. With $Q=P+1$ and $Q'=P'+1$, the identity
  $s(mP)=m+(P+1)s(m)$ turns a collision of $n=mP$ and $n'=m'P'$ into
  $s(m)Q-s(m')Q'=m'-m$. With $g=\gcd(s(m),s(m'))$, a solution requires
  $g\mid m'-m$ and $Q\equiv((m'-m)/g)\,(s(m)/g)^{-1}$ modulo $s(m')/g$, with
  $Q-1$ a prime at most $x/m$ and $Q'-1$ prime. When $s(m')/g>x/m+1$, $Q$ is the
  least positive residue of that class. For cofactors of size about
  $x^{1/2+\kappa}$ with small $g$, the residue must fall in an interval of
  relative length about $x^{-2\kappa}$. An approach using a Fourier majorant of this interval and uniform
  termwise bounds would seek exponential sums of these residues over pairs
  of cofactors, at frequencies up to about $x^{2\kappa}$, with a saving of
  about $x^{2\kappa}$ and with both prime conditions. This is a sufficient
  route to the expected count, not a necessary bound on each frequency. A bound saving
  a fixed small power reaches only cofactors slightly above $x^{1/2}$. The
  inputs $B_k$ have cofactors near $x^{1-\alpha}$, so $\kappa$ is near
  $1/2-\alpha$. With $M\approx x^{1-\alpha}$ cofactors on each side they need a
  saving of about $x^{1-2\alpha}=M^{(1-2\alpha)/(1-\alpha)}$ in sums of about
  $M^2$ terms, close to square-root cancellation when $k$ is large. These are
  Kloosterman fractions whose numerator, inverse and modulus are all arithmetic
  functions of the cofactors. No estimate for them is proved here.
- A level of distribution beyond $x^{1/2}$. Counting one input's largest prime
  with a sieve and its partners through the residues of $s(n')$ needs the values
  $s(n')$ in progressions to moduli $s(m)e$ of size about $x^{1-\alpha}$ or more
  when that input lies in $B_k$. The same holds when the two-prime identity
  turns one side into a divisor count, with moduli of size about $\sqrt{bx}$ or
  larger. A collision bound gives such distribution through the large sieve only
  on average over moduli up to about $x^{1/2}$, and for general sequences the
  large sieve cannot do better. In outline, an Elliott–Halberstam-type estimate
  for the values of $s$, with explicit local main terms, would bound every pair
  whose first cofactor is at most $x^{1-2\epsilon}$. Its main term would need
  only the local densities of $s(n')$ modulo $q$, in place of the pairwise
  average G1. This outline is not a proved implication: the hypothesis would
  need an exact formulation, and the repetition of one modulus $s(m)e$ for many
  cofactors $m$ would need its own bound.

The missing estimates concern the distribution at scale one of $s(n)$ on
inputs with several large prime factors of comparable size and none above
about $x^{1/2}$. They remain unproved here; Proposition D does not refute
them. A route that
proves tightness without bounding collisions class by class is not affected
by Proposition D. Gap G1-core in the large-prime class is the same kind of
requirement at the cofactor scale: there the modulus is a common divisor of
$s(a)$ and $s(a')$, and the residue whose least representative must
rarely lie in a short initial interval is $-\sigma(c)s(c)^{-1}$. In both places Brun–Titchmarsh-type counting
works exactly when some free prime has a range longer than the modulus.

**The averaged sieve error, with its weights retained.** There is a
precise form of the first proposed estimate. Fix a rough-prime class
$\mathcal S_k(x)$ and write each member uniquely as $mP$, where $P$ is its
largest prime. For a fixed eligible $m$, the allowed $P$ form the primes in
an interval $I_m$: the conditions $P>\max\{x^\theta,P(m)\}$ and $mP\le x$
are interval conditions, and $s(mP)\ge\delta mP$ supplies at most another
upper endpoint. The remaining class conditions depend only on $m$.
For large $x$, every such cofactor has $s(m)\ge\delta m/2$.

Consider the pairs $m\ne m'$ with $h=\sigma(m')-\sigma(m)\ne0$, $g\mid h$,
and two primitive, locally admissible forms
$P=u+\beta t$, $P'=v+\lambda t$, where
$g=(s(m),s(m'))$, $\beta=s(m')/g$ and $\lambda=s(m)/g$.
Call these the regular pairs. Let $J_{m,m'}$ be their actual parameter
interval, of length $\ell_{m,m'}\le xg/(m s(m'))$, with the same endpoint
conventions as $I_m,I_{m'}$. Let $f_{m,m'}(t)$ be the product of the forms.
The prime-pair count for all other off-diagonal cofactor pairs is denoted
$C_{\rm deg}(x)$. This count includes the $h=0$ case and the possible
prime values of nonprimitive forms; it is not silently discarded.

Fix $0<\kappa<\theta$ and set $z=x^\kappa$. Use, for each regular pair,
the explicit weights $\lambda_d^{(m,m')}$ of
[the uniform sieve argument](uniform_two_form_sieve.md), and put

$$
\begin{aligned}
R_q(m,m')&=\#\{t\in J_{m,m'}\cap\mathbb Z:q\mid f_{m,m'}(t)\}
-\frac{\ell_{m,m'}\omega_{m,m'}(q)}q,\\
\mathcal E_z(x)&=
\sum_{\substack{(m,m')\\\text{regular}}}\ \sum_{d,e<z}
\lambda_d^{(m,m')}\lambda_e^{(m,m')}R_{[d,e]}(m,m').
\end{aligned}
$$

The sums on $d,e$ use the squarefree support specified with those weights.
They are finite sums of explicitly given real numbers; the remainders and
the total $\mathcal E_z$ are signed. All relevant primes exceed $z$, so
summing the finite sieve inequality gives, for an absolute constant $C$,

$$
C_{\mathcal S_k(x)}(x)
\le x+C_{\rm deg}(x)+
\frac{Cx}{\delta\kappa^2\log^2x}
\sum_{\substack{(m,m')\\\text{regular}}}
\frac{g\,\mathfrak S_x(m,m')}{mm'}+\mathcal E_z(x).
$$

The $x$ term covers equal cofactors, which force $P=P'$. The main term
uses only the proved denominator bound and the comparison of singular
series cutoffs. It is valid even when $\ell_{m,m'}<1$; unlike G0, it does
not absorb the remainders individually. Consequently, a $O(\log^2x)$
bound for the displayed local-factor sum, $C_{\rm deg}(x)=O(x)$ and the
upper bound $\mathcal E_z(x)\le Kx$ for some fixed $K$ would prove the class estimate in
Theorem C. The constants may depend on $\delta,\theta,\tau,k,\kappa$.
None of these three bounds for general rough-prime classes is established
here. Bounding each $|R_q|$ by $\omega(q)$ and summing absolute weights
produces an error majorant of at least one per regular pair, from $d=e=1$.
Proposition D explains why charging that bound to every represented
cofactor pair cannot work; a reduction to regular pairs must quantify
which pairs it removes. Merely displaying the signed sum supplies no
cancellation. Its explicit weights specify an analytic estimate to attack
without assuming that the residues are independent.

**Other whole-target attempts and their failure points.** The proof of
[[../library/arithmetic_functions/pollack_2018_divisor_sum_fibers/theorem_1_2|Pollack, Pomerance and Thompson's finite-target theorem]]
(2017 manuscript, Section 2, pp. 3–4) writes $n=de$ with $d$ the largest
divisor below $\sqrt x$. For fixed output $a$, the identity
$a=\sigma(d)s(e)+s(d)e$ determines $s(e)$ modulo
$s(d)/(d,\sigma(d))$. Its count is a bound for each output; multiplying
that bound by the number of targets retains the square-root restriction.
Averaging it without a new estimate for which residues actually occur
does not give Theorem B(4).

[[../library/arithmetic_functions/luca_pomerance_2015_range_sum_of_proper_divisors_function/theorem_1|Luca and Pomerance's positive-density range theorem]]
(15-page preprint, Section 3, pp. 6–13) does supply a linear collision
bound on selected classes. Its inputs have $n=mp\in(x/2,x]$ with
$m\le x^{7/15}$, hence $p>x^{8/15}/2$. Its proof therefore does not bound
the positive-density complement in G2. Its further prime ranges are used
in the local-factor argument and cannot be removed just by summing
cofactor boxes. These two source proofs were read in their transcriptions
for the stated uses; no new verification of their external premises or
PDF fidelity is asserted.

For a counterexample, the large localized fibers of the same
[[../library/arithmetic_functions/pollack_2018_divisor_sum_fibers/theorem_1_4|Pollack–Pomerance–Thompson paper]]
(Section 3, pp. 4–6) do not themselves supply positive input density.
Common multiplication does not amplify an equal-value fiber into another
one: if $s(n_i)=a$ and $r>1$ is coprime to every $n_i$, then

$$
s(rn_i)=\sigma(r)a+s(r)n_i.
$$

Since $s(r)>0$, these values are distinct for distinct $n_i$. This exact
identity rules out that amplification step only. Different multipliers or
another construction are not excluded. No positive-upper-density
preimage of a density-zero target is constructed here.

## Next discriminating tests

- **Full equations.** Gap G2-full can bypass the large-divisor core
  and the quadratic slice. The prime-power local densities, their
  reciprocal-weighted cofactor average and the continuous main term
  are supplied by [the full-equation calculation](rough_prime_local_density.md).
  The missing test is an integer prime-solution estimate for
  $F_{\sigma(b),b,k}(\mathbf P)=F_{\sigma(b'),b',k}(\mathbf P')$
  with $k\ge3$, $b,b'\le x^\tau$ and all $P_i,P_i'>x^\theta$,
  whose total error is $O(x)$ after summing the boxes and cofactors.
  It must include off-diagonal solutions sharing some prime variables.
  A count for one fixed $b,b'$ or one fixed $k$ does not cover every
  class needed as the discarded proportion tends to zero. Complete
  residue counts alone do not bound this error.
- **Large common divisors.** Gap G1-core is the first target in the
  large-prime class. In the core, a divisor $d$ of $s(a)$ with
  $d\ge P(a)^{1-\kappa}$ has complementary divisor
  $s(a)/d\ll c\,P(a)^\kappa\log y$, where $c=a/P(a)$, so the core
  partners of $a$ lie among $a+js(a)/\lambda$ for divisors $\lambda$ of
  $s(a)$ of that size. Enumerating them without using $d\mid s(a')$
  overshoots $\log^2y$ by about the average number of such $\lambda$, a
  factor of order $\log y$ in a random model. A proof must recover that
  factor from the condition $d\mid s(a')$, for example by bounding, on
  average over $\lambda$ and $j$, the number of $a$ for which
  $s(a+js(a)/\lambda)$ is divisible by $s(a)/\lambda$. Finite sums say
  little about this regime: $W=\log\log y/(4\log\log\log y)$ is below
  $1$ unless $y$ exceeds $10^{2000}$.
- **Quadratic slice.** For cofactors $b,b'\le x^\tau$, count the prime
  solutions of the quaternary quadric in the balanced box, with the
  congruence conditions of a four-dimensional upper-bound sieve, and
  separately its components with vanishing right side. Report the error
  term against the main term, of order $x/(bb'\log^2x)$ up to local and
  doubly logarithmic factors, as $b$ and $b'$ grow. A uniform bound of that
  order, with G0, the G1 analogue for pairs that reduce to the linear
  slice, and a bound for that slice's exceptional prime cases, settles
  $\mathcal S_2$ through G2-quad. It leaves the balanced
  inputs $B_k$ with $k\ge4$, so it cannot complete the route.
- **Balanced classes.** The first family forcing Proposition D's
  all-pairs error obstruction for quadratic slices is $B_4$, whose
  cofactors $n/P_1$ lie near $x^{7/9}$. For these inputs, seek
  an upper bound of order $x$ for the explicit signed remainder
  $\mathcal E_z(x)$ above, together with the local-factor sum and the
  degenerate count appearing in the same finite inequality. This states
  exactly what an averaged use of the linear sieve would need. Fourier
  estimates for the short residue intervals are one possible tool;
  uniform bounds on each individual frequency are not necessary. A result
  for $B_4$ alone would still need extension to every rough-prime class
  required by Theorem C. No such estimate is supplied here.
