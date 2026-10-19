---
name: research/erdos_699/remaining/details/indices_4_5_row_zero
title: "Erdős 699: necessary divisibility of the row at indices 4 and 5"
desc: "Every bad triple at index 4 has 4|n or 9|n; at index 5 it has 8|n or 9|n. An elementary argument and 61 fixed rational-slope cases exclude the complementary classes completely."
created: 2026-09-22T03:56:47Z
updated: 2026-09-22T19:12:28Z
---

# Erdős 699: necessary divisibility of the row at indices 4 and 5

[[research/erdos_699/_index|P699 research]] ·
[[problems/factorials_binomials/E0699/_index|Erdős problem 699]]

***

With the original threshold $p\ge i$, every bad triple satisfies

$$
\boxed{\begin{array}{ll}
i=4:&4\mid n\ \text{or}\ 9\mid n,\\
i=5:&8\mid n\ \text{or}\ 9\mid n.
\end{array}}
$$

These are complete exclusions of the complementary congruence classes.
They do not provide a last row for either entire index. Equivalently,
for at least one of the small primes $2,3$, the numerator factor $n$
has strictly higher valuation than every other numerator factor.
The index-four proof is elementary. The index-five proof reduces every
remaining possibility to 61 rational-slope cases and three candidate
pairs, each with an explicit common prime.

## A fixed-slope consequence of Lucas's theorem

Write $R_t$ for the part of $n-t$ supported on primes at least $5$.
For a bad triple with $i=4$, every prime-power component $p^e$ of $R_t$,
$0\le t\le3$, is active in $\binom n4$. Lucas's theorem therefore gives

$$
j\bmod p^e\in\{0,\ldots,t\}.
$$

In particular $R_0\mid j$. If $j/n=a/q$ in lowest terms, then
$qj=an$. For any fixed $t$, multiplication by $q$ gives

$$R_t\mid F_t(a,q),\qquad
F_t(a,q)=\prod_{r=0}^{t}(at-qr).\tag{1}$$

Indeed, for each prime-power component of $R_t$, one factor $j-r$ is
zero modulo that prime power, while $n\equiv t$.
This argument does not require $q$ to be invertible modulo the prime.

At index five, the factor $5$ in $5!$ requires a small adjustment.
Put

$$
\widetilde R_t=R_t/\gcd(R_t,5).
$$

Then

$$\widetilde R_0\mid j,\qquad
\widetilde R_t\mid F_t(a,q)\quad(0\le t\le4).\tag{2}$$

For primes greater than $5$, the preceding proof applies unchanged.
If $5^e\Vert n-t$ with $e\ge2$, then $5$ is active in
$\binom n5$, and Lucas actually gives the stronger congruence modulo
$5^e$. Removing one factor of $5$ is therefore safe in every case.

## Index four

Suppose $4\nmid n$ and $9\nmid n$. Then the $\{2,3\}$-part of $n$
divides $6$. Since $R_0\mid j$, the reduced denominator of $j/n$ divides
$6$. The condition $0<j/n\le1/2$ leaves exactly

$$
j/n\in\{1/6,1/3,1/2\}.
$$

If $j/n=1/6$, then $6\mid n$, so $n-1$ is coprime to $6$.
Equation (1) at $t=1$ gives $n-1\mid5$, hence $n\le6$.

If $j/n=1/3$, then $3\mid n$. Equation (1), first at $t=1$ and then
at $t=2$, gives $R_1\mid2$ and $R_2\mid8$. Consequently $R_1=R_2=1$.
The consecutive positive integers $n-1,n-2$ are both powers of $2$,
forcing $n=3$.

If $j/n=1/2$, then $n$ is even. Equation (1) at $t=1,3$ gives
$R_1\mid1$ and $R_3\mid9$. Thus the odd integers $n-1,n-3$ are powers
of $3$. Their difference is $2$, forcing $n=4$.

All three conclusions contradict $4<j\le n/2$.

## Index five

Suppose $8\nmid n$ and $9\nmid n$. Then the $\{2,3\}$-part of $n$
divides $12$. By (2), the reduced denominator $q$ of $j/n=a/q$
divides $60$.

For each possible reduced fraction $0<a/q\le1/2$ with $q\mid60$,
and each residue $s=n\bmod6$ compatible with $q\mid n$, choose
$t\in\{1,2,3,4\}$ such that

$$
\gcd(s-t,6)=1,\qquad F_t(a,q)\ne0.\tag{3}
$$

The retained integer checker verifies the existence of such a $t$ in
all 61 cases. Now $n-t$ is coprime to $6$, so (2) implies the fixed
integer divisibility

$$
\boxed{n-t\mid5F_t(a,q).}\tag{4}
$$

Thus the possible $n$ arise from divisors of explicit constants,
independent of $n$. For reproducibility the checker chooses the valid
$t$ minimizing $(|F_t(a,q)|,t)$. The largest constant $5|F_t|$ is
$782\,595$.

After imposing $q\mid n$, $n\equiv s\pmod6$, $5<j\le n/2$, and
$8\nmid n$, $9\nmid n$, these fixed divisor conditions leave exactly

| $n$ | $j$ | Common prime of $\binom n5$ and $\binom nj$ |
| ---: | ---: | ---: |
| 28 | 7 | 5 |
| 210 | 77 | 7 |
| 780 | 247 | 7 |

Each displayed prime has valuation exactly one in both binomial
coefficients. Hence none is bad, completing the proof.

The [checker](../../computations/erdos_699_indices_4_5_row_zero.py)
uses only integer arithmetic and the Python standard library. Its
[certificate](../../computations/erdos_699_indices_4_5_row_zero.json)
records all 61 choices and the three witnesses. It enumerates divisors
of fixed algebraic constants; it does not search an interval of binomial
rows.

```sh
python3 wiki/research/erdos_699/computations/erdos_699_indices_4_5_row_zero.py
```

## What remains

The difficult configurations have a large power of $2$ or $3$ in $n$
itself. For example, maxima at $n$ and $n-1$ permit
$n=2^A u$, $n-1=3^B v$ with both cofactors unbounded. The reduced
denominator of $j/n$ is then also unbounded, and the constants in (4)
grow with it. The fixed-slope argument consequently does not yet make
these remaining configurations effective.

## An additional prime-power criterion at index four

There is also a uniform sufficient condition using the last two numerator
factors. Suppose that prime powers $P=p^e\mid n-2$ and
$Q=q^f\mid n-3$ have $p,q\ge5$ and

$$
PQ>3n.\tag{5}
$$

Then the entire row is good at index four.
Indeed, the primes are distinct because $n-2,n-3$ are consecutive.
If a column were bad, Lucas would give residues

$$j\equiv r\pmod P,\qquad j\equiv s\pmod Q,
\qquad 0\le r\le2,\quad0\le s\le3.$$

The consecutive shifts give an especially simple Chinese remainder
representative:

$$j\equiv s(n-2)-r(n-3)
=(s-r)n-2s+3r\pmod{PQ}.\tag{6}$$

If $s=r$, this representative is $r\le2$. If $s>r$, it lies between
$n-2$ and $3n-6$, strictly above $n/2$ and below $PQ$. If $s<r$,
adding $PQ>3n$ puts its least nonnegative representative above $n/2$.
Thus none of the twelve residue classes meets $4<j\le n/2$.

This criterion uses the full powers dividing the two numerator factors,
and does not depend on their other prime factors. A proof that such a pair
exists in every remaining bad-row candidate has not been obtained.
