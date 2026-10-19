---
name: research/erdos_699/remaining/details/cubic_followup
title: "Erdős 699: further restrictions at index three"
desc: "An endpoint divisibility criterion, prime-power and column restrictions, and certified exclusions for n<=10^19 and v_2(n)<=48. Global cubic finiteness remains unproved."
created: 2026-09-21T20:12:33Z
updated: 2026-09-21T21:59:43Z
---

# Erdős 699: further restrictions at index three

[[research/erdos_699/_index|P699 research]] ·
[[problems/factorials_binomials/E0699/_index|Erdős problem 699]] ·
[[research/erdos_699/proofs/details/cutoff_and_cubic|Cutoff 35 and the first cubic reduction]]

***

This continues the cubic investigation for the original threshold $p\ge3$.
It does **not** prove the cubic case or global finiteness of its exceptions.
The subsequent [uniform proof attempt](cubic_uniform.md)
sets aside finite searches and records an integer-moment formulation and
the missing integrality step in a Vieta argument.
The [irreducibility note](cubic_irreducibility.md)
proves that every hypothetical bad triple supplies an irreducible integer
cubic after exact normalization. The
[weighted polynomial note](cubic_weighted.md) explains
why removing powers of two from the row does not close the polynomial argument.
The new conclusions are:

- Every cubic counterexample has **$n>10^{19}$ and $v_2(n)\ge49$**.
  The valuation bound excludes a complete range of valuations, with no
  externally imposed upper bound on $n$.
- Each active prime-power component $P$ of $n-1$ satisfies $P^3<3n^2$;
  each active component of $n-2$ satisfies $P^2<6n$.
- Write $d=n-2j>0$ and let $v$ be its odd part. A counterexample satisfies
  $$
  v(d^2-3n+2)\ge u(n-1)(n-2),\qquad v>u,
  $$
  where $u$ is the odd part of $n$. In particular, every column with
  $n-2j$ a power of two is good.

The arguments below are repository deductions. The computational result uses
the proved restrictions from the [earlier note](../../proofs/details/cutoff_and_cubic.md),
followed by exact integer calculations and independently verified primality
certificates. Novelty has not been assessed.

## 1. The remaining problem as two divisibilities

The earlier proof reduces a bad cubic triple to

$$n=2^h u,\qquad h\ge2,\quad u\text{ odd},\quad
3u^3<2^h,\qquad 4\le j<n/2.$$

Put $c=n-j$ and

$$
W=\frac{\binom n3}{2^h}=\frac{u(n-1)(n-2)}6.
$$

For an odd prime $p$ with $p^a\Vert n-t$, $t\in\{0,1,2\}$, call the
component $p^a$ **active** when $p\mid\binom n3$. The only inactive odd
component is $3$ when $v_3(n-t)=1$.
Badness implies the full prime-power conditions

$$
j\bmod p^a\in\{0,\ldots,t\}.\tag{1}
$$

There is a useful exact reformulation of these necessary conditions.

**Proposition.** The following are equivalent:

1. All the restrictions (1) hold.
2. $W\mid\binom j3$ and $W\mid\binom c3$.
3. Both
   $$u(n-1)\mid3jc,\qquad
   u(n-1)(n-2)\mid j(j-1)(j-2)\tag{2}$$
   hold.

**Proof.** For an active $p^a$, divisibility of each endpoint binomial by
the $p$-part of $W$ forces

$$
j\equiv r,\quad c\equiv s\pmod{p^a},\qquad r,s\in\{0,1,2\}.
$$

For $p\ge5$, this follows because the three consecutive factors have
pairwise distinct residues modulo $p$. For $p=3$, the endpoint binomial
has valuation at least $a-1$, so its numerator has valuation at least
$a$; again one of the three factors is divisible by $3^a$.
Here $a\ge2$, since the component is active. In either case $p^a\ge5$.
Since $r+s\le4<p^a$ and $j+c\equiv t\pmod{p^a}$, we have $r+s=t$.
This gives (1), and the reverse implication follows from the same factors.

Finally,

$$
\binom j3+\binom c3=\binom n3-\frac{jc(n-2)}2.
$$

The endpoint sum divided by $W$ is
$2^h-3jc/[u(n-1)]$, and
$\binom j3/W=j(j-1)(j-2)/[u(n-1)(n-2)]$. This proves the equivalence
with (2). $\square$

These conditions concern the initial blocks of base-$p$ digits. A solution
of (2) would still have to pass the higher Lucas digit conditions to be an
actual counterexample. In particular, the proposition is not a converse to
badness.

## 2. Large individual prime-power components rule out a row

These exclusions use only the labels from $n-1$ and $n-2$.
They therefore also apply when the label from $n$ has been omitted.

**Proposition.** In a bad cubic triple,

$$P^3<3n^2\quad\text{if }P\Vert n-1\text{ is an active prime-power component},
\tag{3}$$

and

$$P^2<6n\quad\text{if }P\Vert n-2\text{ is an active odd prime-power component}.
\tag{4}$$

Here $P\Vert m$ means $P=p^{v_p(m)}$, not that its prime exponent is one.

**Proof of (3).** Write $n-1=dP$ and $j=kP+r$, with $r=0$ or $1$.
Then $d$ is odd and

$$
1\le k\le(d-1)/2.
$$

Let $M$ be the odd part of $n-2$, with its factor $3$ removed only when
$v_3(n-2)=1$. Thus $M\ge(n-2)/6$. By (1),
$M\mid j(j-1)(j-2)$. Modulo $M$ we have $dP\equiv1$, so

$$
M\mid(k+dr)(k+d(r-1))(k+d(r-2)).
$$

None of these factors is zero. If $r=0$, the absolute product is
$k(d-k)(2d-k)<d^3/2$, using $k(d-k)\le d^2/4$.
If $r=1$, it is $k(d-k)(d+k)<d^3/2$ as well.
Consequently

$$
\frac{n-2}{6}\le M<\frac{(n-1)^3}{2P^3},
$$

which gives $P^3<3(n-1)^3/(n-2)<3n^2$.

**Proof of (4).** Write $n-2=dP$ and $j=kP+r$, with
$r\in\{0,1,2\}$. Now $d$ is even and $1\le k\le d/2$.
Let $M$ be $n-1$ with its factor $3$ removed only when $v_3(n-1)=1$.
Then $M\ge(n-1)/3$, and $M\mid j(j-1)$.
As $dP\equiv-1\pmod M$,

$$
M\mid(dr-k)(d(r-1)-k).
$$

Both factors are nonzero. Their absolute product is at most
$3d^2/4$ for $r=0$, at most $d^2/4$ for $r=1$, and strictly less than
$2d^2$ for $r=2$. Hence

$$
\frac{n-1}{3}\le M<\frac{2(n-2)^2}{P^2},
$$

which gives $P^2<6(n-2)^2/(n-1)<6n$. $\square$

The dependence on the last two labels is essential in this argument.
Those labels alone can be simultaneously satisfied: examples are
$(n,j)=(76672,26775)$ and $(175492,60606)$.
They are not counterexamples, because the label from $n$ fails.
The checker retains these as positive controls, so the residue machinery
is tested on nonempty sets as well as on exclusions.

## 3. Alternating coefficients exclude an infinite family of columns

For

$$
R(z)=\sum_{r=0}^3\binom j{3-r}\binom cr z^r,
$$

badness gives $W\mid R$ coefficientwise. Put $d=c-j=n-2j>0$.
Direct expansion gives

$$
6R(-1)=-d\bigl(d^2-3n+2\bigr).
$$

Therefore

$$
Q=\frac{d(d^2-3n+2)}{u(n-1)(n-2)}\in\mathbb Z.\tag{5}
$$

Write $d=2^t v$ with $v$ odd. Since $4\mid n$ and $d$ is even,
$v_2(d^2-3n+2)=1$ and $v_2(n-2)=1$. Thus $Q$ is nonzero and
$v_2(Q)=t$. Comparing its absolute value with $2^t$ yields

$$
v\,|d^2-3n+2|\ge u(n-1)(n-2).\tag{6}
$$

In fact $d^2>3n-2$. Otherwise, setting $A=3n-2$ and using $v\le d/2$,

$$v(A-d^2)\le\max_{x\ge0}\frac{x(A-x^2)}2
=\frac{A^{3/2}}{3\sqrt3}<n^{3/2}<(n-1)(n-2)$$

for $n\ge8$, contradicting (6). We obtain

$$v(d^2-3n+2)\ge u(n-1)(n-2),\qquad
d^3>2u(n-1)(n-2).\tag{7}$$

Since $d<n$, the first inequality also forces **$v>u$**. This proves
that a column is good whenever the odd part of $n-2j$ is at most the odd
part of $n$. In particular, all columns with $n-2j$ a power of two are
good. The second inequality excludes a central interval of width on the
order of $u^{1/3}n^{2/3}$.

## 4. A complete computation for $v_2(n)\le48$

For a fixed $h$, the earlier row bound leaves precisely the finite list

$$
n=2^h u,\qquad u\text{ odd},\quad 3u^3<2^h.
$$

The [follow-up checker](../../computations/erdos_699_cubic_followup.py)
enumerates this entire list for $2\le h\le48$. It first applies (3)
and (4); remaining rows are checked by intersecting the full prime-power
restrictions (1). Any surviving column is tested with the full Lucas
criterion. No column survived the prime-power conditions.

The [completed output](../../computations/erdos_699_cubic_followup.json)
records **110,129 rows**, divided as follows:

| Reason for exclusion | Rows |
| --- | ---: |
| A large active component of $n-1$ | 46,564 |
| A large active component of $n-2$ | 42,222 |
| Incompatible prime-power restrictions | 21,343 |

The largest row requiring consideration is
$12\,789\,941\,466\,755\,497\,984$.
This proves the entire assertion for $v_2(n)\le48$, rather than imposing
that largest row as a cutoff on all valuations.

SymPy 1.14.0 is used only to find factorizations. The verifier checks their
products and proves every factor prime. Small primes are checked against
an exact sieve. For a larger proposed prime $p$, it recursively certifies
the full factorization of $p-1$ and, for every prime $q\mid p-1$, finds
an integer $a$ satisfying

$$a^{p-1}\equiv1\pmod p,\qquad
\gcd\bigl(a^{(p-1)/q}-1,p\bigr)=1.$$

For any prime divisor $r$ of $p$, these conditions force the order modulo
$r$ to contain the full $q$-part of $p-1$, for every $q$. Thus
$p-1\mid r-1$, which forces $r=p$. This is an exact primality proof;
probable-prime answers are insufficient to complete the computation.
The run certified 249,884 primes beyond the sieve using 999,915 witnesses.
The output records the counts of certified primes and witnesses; the
script regenerates and verifies the certificates.

The endpoint criterion was compared with the earlier CRT implementation
in 11,174 cases. The alternating cubic identity was checked in the same
cases, and the proved column family was compared with direct binomial gcds
in 3,145 cases. The earlier direct-binomial comparisons and strict-threshold
positive controls are also retained.

Reproduce the complete valuation range with:

```sh
uv run --with sympy==1.14.0 python wiki/research/erdos_699/computations/erdos_699_cubic_followup.py --max-v2 48
```

For $49\le h\le63$, a second run checks the remaining rows $n\le10^{19}$.
Its [completed output](../../computations/erdos_699_cubic_followup_large_rows.json)
contains **17,763 additional rows**: 7,519 excluded by (3), 6,821 by (4),
and 3,423 by incompatible prime-power restrictions. Again there are no
residue candidates. This run certifies 57,531 primes beyond the sieve
using 229,330 witnesses. Reproduce it with:

```sh
uv run --with sympy==1.14.0 python wiki/research/erdos_699/computations/erdos_699_cubic_followup.py --min-v2 49 --limit 10000000000000000000
```

The first run covers all smaller valuations, and $2^{64}>10^{19}$.
Together the two disjoint runs examine **127,892 rows** and prove both
the bound $v_2(n)\ge49$ and the exclusion of all $n\le10^{19}$.

## 5. The remaining obstruction

We still do not have an upper bound on $h$. The prime-power bounds in
(3)–(4), the endpoint divisibilities (2), and the column restrictions (7)
are additional necessary conditions, but no argument here proves that
they have only finitely many solutions as $h$ varies.

An especially concrete remaining target is to rule out the two
divisibilities (2) for every admissible pair in the sparse row family.
Doing so would settle $i=3$ without needing the higher Lucas digits.
It is currently a stronger sufficient target, not a proved theorem.
