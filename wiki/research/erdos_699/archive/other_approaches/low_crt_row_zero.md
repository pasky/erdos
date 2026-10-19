---
name: research/erdos_699/archive/other_approaches/low_crt_row_zero
title: "Erdős 699: a forced valuation gap at indices six and seven"
desc: "Every bad triple at index six or seven has a gap of at least three at 2, or two at 3 or 5, between the row and column valuations. Exact slope divisibilities exclude all complementary cases."
created: 2026-09-22T06:20:00Z
updated: 2026-09-22T19:12:28Z
---

# Erdős 699: a forced valuation gap at indices six and seven

***

This is a retained earlier research note. The [[research/erdos_699/_index|current reading guide]] gives the latest status and distinguishes completed proofs from remaining cases.

[[research/erdos_699/_index|P699 research]] ·
[[research/erdos_699/remaining/details/indices_4_5_row_zero|The corresponding row restriction at indices four and five]]

**Proposition.** If $(n,i,j)$ is bad with $i=6$ or $i=7$, then

$$
\boxed{v_2(n)-v_2(j)\ge3\quad\text{or}\quad
v_3(n)-v_3(j)\ge2\quad\text{or}\quad
v_5(n)-v_5(j)\ge2.} \tag{1}
$$

In particular, every such row satisfies

$$
\boxed{8\mid n\quad\text{or}\quad9\mid n\quad\text{or}\quad25\mid n.} \tag{2}
$$

This excludes entire row and column congruence classes, uniformly in their
size. It does not bound the rows in the three alternatives of (1).

## Fixed slope divisibilities

Put $j/n=a/q$ in lowest terms. Let $R_t$ be the part of $n-t$ supported
on primes greater than five, and put $H=1$ at index six and $H=7$ at
index seven. Badness and Lucas's theorem imply

$$
\frac{R_t}{\gcd(R_t,H)}\mid F_t(a,q),\qquad
F_t(a,q)=\prod_{r=0}^{t}(at-qr),\quad 0\le t<i. \tag{3}
$$

For each prime-power factor $p^e$ in this divisor, the prime is active
in $\binom ni$. Lucas gives $j\bmod p^e\le t$. Multiplying the relevant
congruence $j\equiv r\pmod{p^e}$ by $q$, and using $qj=an$ and
$n\equiv t\pmod{p^e}$, gives $p^e\mid at-qr$. At index seven,
removing one factor of seven safely handles the possible cancellation
in $7!$. When the numerator has seven-adic valuation at least two,
Lucas gives the stronger congruence modulo the full power.

At $t=0$, Lucas itself gives $R_0/\gcd(R_0,H)\mid j$.
Thus $q$ has no prime factors other than $2,3,5$ and possibly one factor
of seven at index seven. If (1) fails, then

$$
q\mid60H. \tag{4}
$$

We prove the stronger assertion that **no bad triple at index six has
$q\mid60$, and no bad triple at index seven has $q\mid420$**, without
any independent restriction on the valuations of $n$.

## Finite exact certificate

For each divisor $q\ge2$ of $60H$, each $1\le a\le q/2$ coprime to
$q$, and each residue $s=n\bmod30$ compatible with $q\mid n$, choose
$t\in\{1,\ldots,i-1\}$ satisfying

$$
\gcd(s-t,30)=1,\qquad q\nmid t. \tag{5}
$$

The checker verifies such a choice in every case. Since $a,q$ are
coprime, $q\nmid t$ implies $F_t(a,q)\ne0$. Also $n-t$ is coprime to
$30$, so (3) gives

$$
n-t\mid H F_t(a,q). \tag{6}
$$

Consequently each slope and residue class has finitely many candidates,
obtained from the positive divisors of the fixed integer $H|F_t(a,q)|$.
The checker uses the choice minimizing the number of divisors, followed
by the constant and the shift.

| Index | Slope and residue cases | Largest constant in (6) | Candidates after (6) and admissibility | Candidates satisfying all of (3) |
| ---: | ---: | ---: | ---: | ---: |
| 6 | 105 | 48,754,475 | 9 | 0 |
| 7 | 780 | 41,172,708,702,125 | 64 | 0 |

Every one of the 73 residual candidates violates (3) at another shift.
The record gives that shift, the required divisor, and the polynomial
value. Thus no binomial factorization or search through a row interval
is needed. This proves (4) impossible and establishes (1).

The [integer checker](../../computations/erdos_699_low_crt_row_zero.py)
uses only the Python standard library. Its
[certificate](../../computations/erdos_699_low_crt_row_zero.json)
contains every slope and residue case and every rejected candidate.

```sh
python3 wiki/research/erdos_699/computations/erdos_699_low_crt_row_zero.py
```

## Consequence for the selected positions

Condition (2) means that at least one of the primes $2,3,5$ has its
unique maximal numerator valuation at the position $r=0$. Indeed, among
$n,n-1,\ldots,n-6$, a multiple of eight, nine, or twenty-five cannot
be accompanied by another multiple of that same power. The stronger
statement (1) also requires that the column have a strictly smaller
valuation at that prime.

This supplies a position restriction for the weighted interpolation
argument. It does not exclude configurations in which a selected
small-prime power at $n$ grows without bound.
