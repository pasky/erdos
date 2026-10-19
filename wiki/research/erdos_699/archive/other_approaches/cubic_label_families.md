---
name: research/erdos_699/archive/other_approaches/cubic_label_families
title: "Erdős 699: curves on which the cubic conditions from n−1 and n−2 hold"
desc: "At index three, the Lucas conditions coming from n−1 and n−2 hold along an explicit cubic curve and along Pell conics. Congruences modulo 27 and 73 show that the cubic curve contains no bad row, but the families show that a proof must use the power-of-two form of n or higher Lucas digits."
created: 2026-09-22T18:18:44Z
updated: 2026-09-22T18:18:44Z
---

# Erdős 699: curves on which the cubic conditions from n−1 and n−2 hold

***

This is a retained earlier research note. The [[research/erdos_699/_index|current reading guide]] gives the latest status and distinguishes completed proofs from remaining cases.

[[research/erdos_699/_index|P699 research]] ·
[[problems/factorials_binomials/E0699/_index|Erdős problem 699]] ·
[[research/erdos_699/remaining/details/cubic_followup|Earlier cubic reductions]] ·
[[research/erdos_699/remaining/details/cubic_uniform|The uniform proof attempt]]

This note looks at the index-three problem from the other side: instead of
trying to show that the necessary conditions have no solution, it finds the
solutions of the weaker system obtained by dropping the condition coming
from $n$. They are not scattered: of the 88 found, 69 lie on one explicit
cubic curve, 5 on Pell conics, and 14 elsewhere. This does **not** prove the
cubic case.

**Results.**

1. The first Lucas block conditions at the primes of $n-1$ and $n-2$ hold
   identically along the curve
   $$n=\frac{x^3-9x+16}{8},\qquad j=\frac{x(x-1)(x+5)}{24},
   \qquad x\equiv4\pmod 9.$$
2. No row on this curve satisfies the condition coming from $n$. In
   particular the curve contains no bad triple. The proof is a congruence
   argument modulo $27$ and $73$.
3. The same two conditions hold along the conics
   $k(d^2-1)=(n-1)(n+3k-2)$, away from the primes dividing $k$. A 2-adic
   test excludes most of these conics from rows with a large power of two.
4. Every solution with $4\mid n\le 8\cdot10^9$ of the weaker system was
   found: there are **88**, with 69 on the cubic curve and 5 on the conics.
   None satisfies the condition from $n$, and each one already fails a higher
   Lucas digit at some prime of $n-1$ or $n-2$.
5. The conditions from $n-1$ and $n-2$ therefore have infinitely many
   solutions with $4\mid n$. A proof has to use the condition from $n$, the
   form $n=2^hu$ beyond the divisibility $4\mid n$, or higher Lucas digits.
   When $n$ is a power of two the condition from $n$ is empty.

The deductions and computations are repository work; novelty has not been
assessed.

## 1. The conditions in terms of $d=n-2j$

Keep the notation of the earlier notes: $4\le j<n/2$, $c=n-j$, and an odd
prime-power component $p^a\Vert n-t$, $t\in\{0,1,2\}$, is **active** unless
$p=3$ and $a=1$. Badness forces $j\bmod p^a\in\{0,\ldots,t\}$ at every
active component; these are the three conditions, one from each of
$n,n-1,n-2$. Put

$$
d=n-2j=c-j.
$$

Since $n\equiv t\pmod{p^a}$, the congruence $j\equiv r$ is the same as
$d\equiv t-2r$. The three conditions become:

- every active component of $n$ divides $d$;
- every active component of $n-1$ divides $d-1$ or $d+1$;
- every active component of $n-2$ divides $d-2$, $d$, or $d+2$.

Equivalently, each active component of $n$ divides $j$; of $n-1$ divides
$j$ or $c$; and of $n-2$ divides $j$, $c$, or $d$. The five integers
$d-2,\ldots,d+2$ must absorb the active parts of $n-1$ and $n-2$ in this
matched way.

## 2. The cubic curve

**Proposition 1.** Put

$$n=\frac{x^3-9x+16}{8},\qquad
d=\frac{(x+3)(x^2-11x+16)}{24}.$$

Then

$$\begin{aligned}
n-2&=\tfrac18\,x(x-3)(x+3), &
n-1&=\tfrac18\,(x-1)(x^2+x-8),\\
d-2&=\tfrac1{24}\,x(x^2-8x-17), &
d-1&=\tfrac1{24}\,(x-1)(x^2-7x-24),\\
d&=\tfrac1{24}\,(x+3)(x^2-11x+16), &
d+1&=\tfrac1{24}\,(x-9)(x^2+x-8),\\
d+2&=\tfrac1{24}\,(x-3)(x^2-5x-32), &
j&=\tfrac1{24}\,x(x-1)(x+5).
\end{aligned}$$

If $x\equiv4\pmod9$, and $n,j$ are integers with $4\mid n$ and
$4\le j<n/2$, then the conditions from $n-1$ and $n-2$ hold.

For $x\equiv4\pmod9$, integrality and $4\mid n$ hold exactly when
$x\equiv5,11\pmod{16}$ or $x\equiv16\pmod{32}$. The first values are $x=85,112,139,229$, giving
$n=76672,175492,335548,1500868$; the first two are the positive controls
recorded in the [follow-up note](../../remaining/details/cubic_followup.md).
Along the curve $j/n\to1/3$.

**Proof.** The identities are direct expansions. Let $p\ge5$ and
$p^a\Vert n-1$. The factors $x-1$ and $x^2+x-8$ have greatest common divisor
dividing $1+1-8=-6$, so $p^a$ divides one of them. It therefore divides
$24(d-1)$ or $24(d+1)$, and since $p\nmid24$ it divides $d-1$ or $d+1$.
For $p^a\Vert n-2$, the pairwise greatest common divisors of $x,x-3,x+3$
divide $6$, so $p^a$ divides $d-2$, $d+2$, or $d$ in the same way.

At the prime $3$, write $x=1+3t$ with $t\equiv1\pmod3$. Then
$v_3(x-1)=1$ and $x^2+x-8=3(3t^2+3t-2)$, so $v_3(n-1)=2$ and the component
$9$ is active. Also $x^2-7x-24=3(3t^2-5t-10)$ with
$3t^2-5t-10\equiv0\pmod3$, so $v_3(d-1)\ge1+2-1=2$. Thus $9\mid d-1$.
Finally $x(x-3)(x+3)\equiv1\cdot(-2)\cdot4\not\equiv0\pmod3$, so $3\nmid n-2$.
$\square$

The residue $x\equiv4\pmod9$ is forced. For $x\equiv2\pmod3$, $j$ is not an
integer. For $x\equiv0\pmod3$, the three factors of $n-2$ are divisible by
$3$, while each of $d-2,d,d+2$ has smaller $3$-adic valuation than $n-2$, so
the condition from $n-2$ fails at $3$. For $x=1+3t$, the component of $3$
in $n-1$ is $3^{2+v_3(t)}$; it cannot divide $c$, since $v_3(c)=0$, and it
divides $j$ exactly when $t\equiv1\pmod3$.

## 3. No row on the curve satisfies the condition from $n$

**Proposition 2.** No row on the curve satisfies all three conditions. In
particular no bad triple lies on it.

**Proof.** Put $f(x)=x^3-9x+16=8n$. For integer $x$ and $r$,
$\gcd(f(x),x-r)$ divides $f(r)$, and

$$
f(0)=16,\qquad f(1)=8,\qquad f(-5)=-64.
$$

Hence $\gcd(8n,24j)=\gcd\bigl(f(x),x(x-1)(x+5)\bigr)$ divides $2^{13}$, and
$n$ and $j$ have no common odd prime. Also $f(x)\equiv1+16\equiv2\pmod3$,
so $3\nmid n$ and every odd prime-power component of $n$ is active. The
condition from $n$ therefore forces $n=2^h$, that is,

$$
x^3-9x+16=2^{h+3}.
$$

For $x\equiv4\pmod9$ one checks $f(x)\equiv17\pmod{27}$. The powers of two
modulo $27$ have period $18$, and $2^e\equiv17\pmod{27}$ exactly when
$e\equiv15\pmod{18}$. So $h+3\equiv6\pmod9$. The order of $2$ modulo $73$
is $9$, so $2^{h+3}\equiv2^6=64\pmod{73}$. But $f(x)\not\equiv64\pmod{73}$
for every residue $x$. $\square$

This settles the curve without any appeal to Baker's method. The residue
$x\equiv4\pmod9$ is essential: the equation $x^3-9x+16=2^m$ on its own has
the solution $(x,m)=(1,3)$, so no set of congruences can exclude the class
$m\equiv3$ modulo a fixed modulus.

## 4. Pell conics

Let $m=(d^2-1)/(n-1)$. On the conic

$$k(d^2-1)=(n-1)(n+3k-2),\qquad\text{equivalently}\qquad
(2n+3k-3)^2-k(2d)^2=(9k-1)(k-1),\tag{1}$$

one has $m-3=(n-2)/k$ and

$$d^2-1=\frac{(n-1)(n+3k-2)}k,\qquad
d(d^2-4)=\frac{d(n-2)(n+3k-1)}k.$$

So the conditions from $n-1$ and $n-2$ hold at every active component whose
prime does not divide $k$. For non-square $k$ each nonempty conic carries
infinitely many integer points. Along the conic $d/n\to1/\sqrt k$.

Two restrictions follow for rows in the sparse family.

- **The condition from $n$.** If $p\ge5$ divides $n$ and $d$, reducing
  (1) modulo $p$ gives $-k\equiv-(3k-2)$, so $p\mid k-1$. Every active
  component of $n$ must divide $k-1$.
- **A 2-adic test.** If $2^h\mid n$, then (1) gives
  $kd^2\equiv-2(k-1)\pmod{2^h}$. As $d$ is even, $k$ must be odd. Writing
  $k-1=2^vw$ with $w$ odd, the valuations force $v$ odd and $v_2(d)=(v+1)/2$,
  and the remaining congruence needs $w\equiv-k\pmod8$, once $h$ exceeds
  $v+3$.

For $k=3$ the test fails ($w=1\not\equiv5\pmod 8$); directly,
$(n+3)^2-3d^2=13$ with $n=2^h$, $h\ge4$, leads to $3d'^2\equiv7\pmod8$ for
$d=2d'$. The observed conics $k=7$ and $k=1171$ also fail it. The conic
$k=11$ passes. For $n=2^h$ on it, Legendre-symbol conditions at the primes
$p<3000$ with $\operatorname{ord}_p2\mid2520$ leave only
$h\equiv0,1,11\pmod{2520}$, and $h=11$ is actually attained:
$(n,j)=(2048,713)$ lies on this conic. That is the Erdős–Szekeres example
for $i=2$; at index three it fails the condition from $n-2$ at the prime
$11=k$. The remaining classes of $h$ for this conic are not settled here.

More generally, if $a/b$ is $(m-3)/(n-2)$ in lowest terms, every solution
satisfies $b(d^2-1)=\bigl(a(n-2)+3b\bigr)(n-1)$, and $b\mid d$ in every
recorded case. This places every solution on a conic, but the conic depends
on the point; the curve of Section 2 meets infinitely many of them. In the
recorded data only the conic with $k=3$ contains more than one solution.

## 5. The complete search below $8\cdot10^9$

For each row $4\mid n\le8\cdot10^9$, the search intersected the Chinese
remainder classes for $j$ allowed by the active components of $n-1$ and
$n-2$, pruning a class as soon as its modulus exceeded $n/2$ with no
representative in range. It found 88 solutions $4\le j<n/2$:

| Location | Count |
| --- | ---: |
| Cubic curve of Section 2 | 69 |
| Conics (1) with $k=3,3,7,11,1171$ | 5 |
| Other | 14 |

None satisfies the condition from $n$: in every case the odd part of $n$
is at least $n^{0.56}$ and shares no factor with $j$. Every one also fails a
full Lucas condition at a prime of $n-1$ or $n-2$, usually at most of them:
of 724 tests at primes where $n$ has a digit above the initial block, 653
fail. On the cubic curve the prime $3$ is always active and failed at all
10,416 curve rows with $4\mid n$ and $x<6\cdot10^5$. Since $3j=n+(x^2+x-4)/2$
there, the upper third of the base-three digits of $j$ copies those of $n$
shifted by one place, so the Lucas condition at $3$ would force those digits
of $n$ to be monotone.

The 88 solutions have $v_2(n)\le10$. None comes close to the sparse family
$n=2^hu$, $3u^3<2^h$.

## 6. What this means for a proof

The rigorous consequence is modest but definite. The statement

> for $4\mid n$, no $4\le j<n/2$ satisfies the conditions from $n-1$ and $n-2$

is false infinitely often, by Proposition 1. Any proof of the cubic case
must therefore use at least one of: the condition from $n$ (the divisibility
$u\mid j$), the specific form $n=2^hu$ beyond $4\mid n$, or higher Lucas
digits. For $n=2^h$ the first is empty.

On the curve and on the conics, the condition from $n$ turns into an
exponential equation: $x^3-9x+16=2^{h+3}$ on the curve, and on the conic
(1) the requirement that a binary recurrence take a value $2^hu$ with every
active component of $u$ dividing $k-1$. A proof of the cubic case has to
show that no row in these families is bad, so it has to decide these
equations or show that a higher Lucas digit fails on their solutions. On
the curve the congruences of Section 3 suffice. On the conics each value of
$k$ passing the 2-adic test needs its own argument, and no uniform
treatment was found.

There is also a heuristic reason to doubt a short uniform proof. At $n=2^h$
the conditions from $n-1$ alone are essentially the mechanism of the
Erdős–Szekeres counterexamples to the strict statement at $i=2$
($n=16$, $j=6$ and $n=2048$, $j=713$): choose a unitary divisor $A$ of
$2^h-1$ and take $j\equiv0\pmod A$, $j\equiv1\pmod{(2^h-1)/A}$. Index three
adds one more condition, $j(j-1)(j-2)\equiv0$ modulo the active part of
$2^{h-1}-1$, whose factorization is unrelated to that of $2^h-1$. Among the
roughly $2^{\omega(2^h-1)}$ candidates the expected number passing is about
$2^{\omega(2^h-1)}3^{\omega(2^{h-1}-1)}/2^h$. The index-three statement at
powers of two thus says that an independent filter rejects every candidate.
Nothing found here suggests a structural reason for that; the explicit
families found so far had to be handled one at a time.

## 7. Other routes tried

These did not lead anywhere and are recorded to save repetition.

- **Descent in $d$.** With $m=(d^2-1)/(n-1)$ and
  $\ell=d(m-3)/(n-2)$, eliminating $n$ gives
  $\ell(d^2-m-1)=dm(m-3)$. As a quadratic in $d$ its second root is
  $-(m+1)/d$; as a quadratic in $m$ the second root is also negative. No
  Vieta descent is available.
- **Binary structure at $n=2^h$.** The condition from $n-1$ says that $j$
  is an idempotent modulo $2^h-1$, a binary Kaprekar number. Multiplication
  by $2$ rotates binary strings, so $j$ is periodic with period the order of
  $2$ modulo the part of $2^h-1$ where $j\equiv1$. This constrains $j$ only
  when those orders are proper divisors of $h$, and gives nothing when $h$
  is prime.
- **Global covering congruences.** The conditions constrain $j$ only
  modulo the active components themselves, so they impose no congruence on
  $h$ modulo a fixed small prime. Covering arguments work only after an
  algebraic relation between $n$ and $j$ has been found, as on the curve.

## Reproduction

The [standard-library checker](../../computations/erdos_699_cubic_label_families.py)
verifies the identities of Sections 2 and 4, the congruences of Section 3,
the 2-adic test for the observed conics, and each of the 88 recorded
solutions: the two conditions, the failure of the condition from $n$, the
failure of a higher Lucas digit, and the classification. It reruns the full
search below its limit (default $2\cdot10^7$, 13 solutions, about 20
seconds) and compares with the recorded list:

```sh
python3 wiki/research/erdos_699/computations/erdos_699_cubic_label_families.py
```

Its [output](../../computations/erdos_699_cubic_label_families.json)
lists every solution with its curve or conic. The search from $2\cdot10^7$
to $8\cdot10^9$ used a compiled port of the same enumeration, which is not
retained; the completeness of that part of the list is not rechecked by
the script.
