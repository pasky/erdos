---
name: research/powerful_numbers_and_products
title: Powerful integers and consecutive-product tests
desc: Exact divisor and interval certificates, a uniform sum bound, and the gaps between fixed parameters and the unbounded powerful-number questions.
created: 2026-10-14T12:38:34Z
updated: 2026-10-14T12:38:34Z
---

# Powerful integers and consecutive-product tests

[[research/_index|..]]

[[research/powerful_numbers_and_products/evidence/_index|evidence/]]: Exact integer checks for the retained square quotients, Pell interval and product witnesses; all domains and limitations are stated on the owning research page.

***

These author-recorded arguments by Plasma AI distinguish finite certificates
from unbounded conclusions in several problems about powerful integers and
products of consecutive integers. A positive integer is powerful when every
prime divisor has exponent at least two; this includes 1. Each argument
states the parameter range it reaches. No complete catalog resolution or
independent verification is claimed.

## Fixed square quotients at length two

For [[problems/diophantine_problems/E0686/_index|Problem 686]], fix a square
$N=a^2$, $a\ge2$, and length $k=2$. The equation is
$(m+1)(m+2)=a^2(n+1)(n+2)$ with $n\ge0$ and $m\ge n+2$.
Put $X=2m+3$, $Y=2n+3$. Then both are odd,
$Y\ge3$, $X\ge Y+4$, and $X^2-a^2Y^2=1-a^2$.
Since $X<aY$, the positive factors $u=aY-X$, $v=aY+X$ satisfy

$$
uv=a^2-1,\qquad Y=\frac{u+v}{2a},\qquad X=\frac{v-u}{2}.
$$

Conversely every divisor $1\le u\le\sqrt{a^2-1}$, with
$v=(a^2-1)/u$, gives a solution precisely when these formulas give odd
integers satisfying the stated inequalities. Recover
$n=(Y-3)/2$, $m=(X-3)/2$. This proves an exhaustive finite test for this
length, without an arbitrary height cutoff.

| $a$ | $N$ | All $(n,m)$ at $k=2$ |
| --- | --- | --- |
| 2 | 4 | none |
| 3 | 9 | none |
| 4 | 16 | none |
| 5 | 25 | none |
| 6 | 36 | $(0,7)$ |
| 10 | 100 | $(1,23)$ |
| 35 | 1225 | $(0,48)$ |

The evidence exhausts those seven divisor domains and checks each returned
pair in the original equation. Empty rows do not exclude other lengths.
A settling finite test for a square still needs a proved bound on all
possible lengths, or a uniform construction at some length.

## Adjacent and separated blocks

In [[problems/diophantine_problems/E0389/_index|Problem 389]], put
$s=n-1$ and $t=s+k$. The adjacent-block quotient is
$Q=s!(2t-s)!/(t!)^2$. Legendre's formula gives the exact integrality test

$$
\sum_{j\ge1}\left(
\left\lfloor\frac{2t-s}{p^j}\right\rfloor+
\left\lfloor\frac{s}{p^j}\right\rfloor
-2\left\lfloor\frac{t}{p^j}\right\rfloor\right)\ge0
\quad\text{for every prime }p\le2t-s.
$$

The sums are finite. Direct multiplication checks $(n,k)=(1,1),(2,5),(3,4)$.
This formulation tests a given $k$; it does not construct or bound one for
arbitrary $n$. The theorem text of Ulas's *A note on Erdős–Straus and
Erdős–Graham divisibility problems*, IJNT 9 (2013), 583–599,
doi:10.1142/S1793042112501497, remains uninspected here. Its title alone
does not determine whether it covers this universal quantifier.

For [[problems/diophantine_problems/E0930/_index|Problem 930]], separate
nonsquare block products need not have a nonsquare product:

$$
(2\cdot3\cdot4)(48\cdot49\cdot50)=24\cdot117600=1680^2.
$$

The disjoint blocks each have length three. This defeats the inference from
two separate one-block exclusions, not the existence of a larger threshold
$K(2)$. A successful extension must control each prime's total exponent
across the blocks.

## A certified Pell interval

For [[problems/diophantine_problems/E0938/_index|Problem 938]], the
construction in
[[../library/diophantine_problems/doorn_2026_three_term_arithmetic_progressions_consecutive_powerful/_index|van Doorn's paper]]
uses $x^2-343y^2=2$ and the powerful progression
$(x-2)^2,(x-1)^2,x^2-2=7^3y^2$. Its common difference is $2x-3$.
The seed $x=11427$, $y=617$ gives the closed interval
$[130530625,130576327]$.

Every powerful integer has a unique representation $a^2b^3$ with
$b$ squarefree. Hence the complete enumeration in a positive interval
$[L,H]$ has domain

$$
1\le b\le\lfloor H^{1/3}\rfloor,\qquad
\left\lfloor\sqrt{(L-1)/b^3}\right\rfloor+1
\le a\le\left\lfloor\sqrt{H/b^3}\right\rfloor.
$$

The upper bound on $b$ for the seed is 507. The exact output is:

| Integer | Canonical expression | Role |
| --- | --- | --- |
| 130530625 | $11425^2$ | first endpoint |
| 130533497 | $163^2 17^3$ | extra |
| 130553476 | $11426^2$ | middle |
| 130560500 | $1022^2 5^3$ | extra |
| 130561227 | $2199^2 3^3$ | extra |
| 130572800 | $4040^2 2^3$ | extra |
| 130576327 | $617^2 7^3$ | last endpoint |

The four intruders disprove consecutiveness only at this seed. Van Doorn's
Theorem 4 supplies infinitely many good indices for each fixed squarefree
$b\ge648560$; it does not exchange those quantifiers to avoid every
unwanted core at one index. A useful continuation needs simultaneous
avoidance and a uniform tail estimate, or an obstruction for every index.
No such estimate or index cutoff is supplied by this finite check.

## Smooth parts of neighbors

Let $A(m)=2^{v_2(m)}3^{v_3(m)}$, as in
[[problems/diophantine_problems/E0933/_index|Problem 933]]. At
$n=1487503359=311\cdot3^{14}$ one has $v_2(n+1)=15$. The inequalities
$n<2^{31}$ and $32768>3\cdot311\cdot31$ prove exactly, without
floating-point logarithms,

$$
\frac{A(n(n+1))}{n\log n}
=\frac{2^{15}}{311\log n}>\frac3{\log2}.
$$

This is a counterexample to a uniform bound by that constant, not proof of
an infinite limsup. On the family $n=2^t$ with odd $t$, lifting the
exponent gives $v_3(2^t+1)=1+v_3(t)$ and the ratio is
$3^{1+v_3(t)}/(t\log2)\le3/\log2$, with equality for $t=3^j$.
For even $t$ the ratio is $1/(t\log2)$. Thus this entire pure-power
family is bounded. A variable-cofactor construction must prove unbounded
normalized values, beyond finitely many records.

## What the Pell construction proves about a powerful part

Let $Q_2(m)$ retain every prime power in $m$ whose exponent is at least
two. The existing
[[../library/distance_problems/feng_2026_semi_autonomous_mathematics_discovery_gemini_case/solution_p22|Pell solution of the middle part]]
of [[problems/diophantine_problems/E0935/_index|Problem 935]] has an
explicit parameter choice. Put $\alpha=3+\sqrt8=(1+\sqrt2)^2$ and
$\alpha^k=x_k+y_k\sqrt8$. Then $n_k=8y_k^2$ and $n_k+1=x_k^2$ are
powerful.

For a prime $p\equiv5\pmod8$, Frobenius in
$\mathbb Z[\sqrt2]/(p)$ sends $\sqrt2$ to $-\sqrt2$, giving
$\alpha^{(p+1)/2}\equiv-1\pmod p$. Write $m=(p+1)/2$, which is odd.
Raising $\alpha^m=-1+p\delta$ to the power $p$ gives
$\alpha^{mp}\equiv-1\pmod{p^2}$. At the positive integer

$$
k=\frac{mp+1}{2}=\frac{p(p+1)+2}{4},
$$

one has $\alpha^{2k}\equiv-\alpha$ and
$\alpha^{-2k}\equiv-\alpha^{-1}\pmod{p^2}$.
Since $4x_k^2=\alpha^{2k}+\alpha^{-2k}+2$ and
$\alpha+\alpha^{-1}=6$, it follows that $p^2\mid n_k+2$.
Prime valuations give $Q_2(AB)\ge Q_2(A)Q_2(B)$, so

$$
\frac{Q_2(n_k(n_k+1)(n_k+2))}{n_k^2}>p^2.
$$

Dirichlet's theorem supplies infinitely many such primes. Both $k(p)$
and the positive Pell sequence increase, so the inputs are distinct and
tend to infinity. Adding factors through $n_k+\ell$, $\ell\ge2$,
preserves the lower bound. This reconstructs the known middle conclusion;
it supplies no upper estimate and changes no source claim's standing.

For each fixed $\ell\ge2$, the first proposed upper estimate would imply
the third conclusion: choose $\epsilon=(\ell-1)/2$ to bound the ratio to
$n^{\ell+1}$ by $n^{-(\ell-1)/2}$. For $\ell=1$ the first estimate is
already immediate from $Q_2(n(n+1))\le n(n+1)$. The remaining upper
problem begins at $\ell=2$.

## Conditional finiteness keeps its premise

Assume the abc conjecture in the form
$c\le C_\epsilon\operatorname{rad}(abc)^{1+\epsilon}$ for coprime
positive integers $a+b=c$. If $B=2^n\pm1$ is powerful, then
$\operatorname{rad}(B)\le\sqrt B$ and, with $\epsilon=1/2$,

$$
B\le C_{1/2}(2\sqrt B)^{3/2},\qquad
B^{1/4}\le C_{1/2}2^{3/2}.
$$

Thus both signs occur powerfully only finitely often. For powerful
$B=n!\pm1$, the elementary primorial bound
$\prod_{p\le n}p\le4^n$ similarly gives
$B^{1/4}\le C_{1/2}8^n$. Since $B\ge n!/2$ for $n\ge3$ and
$n!\ge\lfloor n/2\rfloor^{\lfloor n/2\rfloor}$, this too is possible
only finitely often. All four cases of
[[problems/diophantine_problems/E0936/_index|Problem 936]] follow under
abc. No effective value of its constant or unconditional bound is supplied.

The orientation in [[problems/diophantine_problems/E0366/_index|Problem 366]]
is also essential: it asks for powerful $n$ followed by 3-full $n+1$.
Then $\operatorname{rad}(n(n+1))\le(n+1)^{5/6}$, and abc with
$0<\epsilon<1/5$ implies finiteness. Reversing the two types changes
the question; known reverse-oriented pairs are not witnesses here.

## The loss when cube factors vary

[[theory/number_theory/L24_powerful_sum_bound/_index|L24]] gives
$R(N)\le N^{2/5+o(1)}$ for the ordered sum count in
[[problems/diophantine_problems/E0943/_index|Problem 943]]. For each fixed
pair of squarefree cube factors its imaginary-quadratic norm argument is
uniformly subpower. Summing those factors is the remaining loss. When all
four parameters $a,b,c,d$ in $a^2b^3+c^2d^3=N$ are of order
$N^{1/5}$, each of the three dyadic bounds used in the proof is of order
$N^{2/5}$ up to subpower factors. Repeating the fixed-core count cannot
by itself remove this loss. A sharper estimate in that balanced range, or
subpower control of the core pairs occurring for each $N$, would change
the research decision. L24 does not prove the desired $N^{o(1)}$ bound.

## Evidence and standing

The finite input is [finite_cases.json](evidence/assets/finite_cases.json).
The [checker](evidence/main.py) uses exact integers, exhaustive divisors and
the full powerful-number domain in the displayed closed interval. From the
repository root, run

```sh
uv run --no-sync python wiki/research/powerful_numbers_and_products/evidence/main.py
```

Runtime is a few seconds. The checker covers the seven square roots, one
Pell interval, the smooth-part counterexample, three divisibility witnesses
and the separated-block witness. It certifies no recurrence tail or
unbounded catalog statement. The mathematical reductions and the finite
replay are author work; no verification tier is asserted by this note.
