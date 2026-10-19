---
name: research/erdos_699/archive/other_approaches/index_14_boundary
title: "Erdős 699: boundary divisors forced when index 14 has its 13-adic maximum at zero"
desc: "A shifted application of the complete index-13 result forces large prime divisors of both columns; its numerical certificate gives explicit power growth of these boundary gcds."
created: 2026-09-22T07:00:00Z
updated: 2026-09-22T19:12:28Z
---

# Erdős 699: boundary divisors forced when index 14 has its 13-adic maximum at zero

***

This is a retained earlier research note. The [[research/erdos_699/_index|current reading guide]] gives the latest status and distinguishes completed proofs from remaining cases.

Suppose $(n,14,j)$ is bad for the original prime threshold, put $c=n-j$,
and assume $13^2\mid n$. Thus the maximal 13-adic position in
$n,n-1,\ldots,n-13$ is zero. The [prime-index transfer](../../remaining/details/prime_index_transfer.md)
shows that this is one of the possible position cases for a bad triple.

For an integer $a$, let $[a]_{\ge17}$ denote its part supported on primes
at least 17, and define

$$
 D_j=\left[\gcd\!\left(j,\prod_{r=1}^{13}(n-r)\right)\right]_{\ge17},
 \qquad
 D_c=\left[\gcd\!\left(c,\prod_{r=1}^{13}(n-r)\right)\right]_{\ge17}.
$$

Then

$$
D_j>1,\qquad D_c>1,\qquad \gcd(D_j,D_c)=1. \tag{1}
$$

In particular, both $j$ and $c$ have a prime divisor at least 17, and
$j<c$. The numerical [index-13 certificate](../../proofs/details/index_13_effective.md)
also gives, whenever $n-1\ge10^{1732}$,

$$
 \boxed{
 D_j^{114}\ge 10^{-356876}(n-1)^{1287/200},\qquad
 D_c^{114}\ge 10^{-356876}(n-1)^{1287/200}.
 } \tag{2}
$$

Thus each boundary gcd is at least

$$
10^{-356876/114}(n-1)^{1287/22800},
$$

where $1287/22800\approx0.05644736$. This is a conditional constraint on
bad triples, not an effective exclusion of index 14.

## The shifted binomial coefficients

Put $B=\binom nj$. The identities

$$
 \binom{n-1}{j-1}=\frac jn B,
 \qquad
 \binom{n-1}{j}=\frac cn B \tag{3}
$$

relate the two shifted columns to $B$. Every prime $q\ge17$ in the
numerator block $n-1,\ldots,n-13$ also divides $\binom n{14}$.
Badness gives $v_q(B)=0$. If $q\mid n-r$ for $1\le r\le13$, then
$q\nmid n$, so (3) gives the exact valuations

$$
 v_q\binom{n-1}{j-1}=v_q(j),\qquad
 v_q\binom{n-1}{j}=v_q(c). \tag{4}
$$

Moreover $13$ does not divide $\binom{n-1}{13}$: its unique numerator
multiple is $n-13$, whose 13-adic valuation is one, and $13!$ cancels
that factor.

The complete index-13 theorem applies to both binomial pairs in (3).
For the second pair, reflect its column if necessary. In both cases the
smaller column exceeds 13: $j\ge15$ and $c\ge j$. The supplied common
prime is therefore at least 17. Equation (4) proves the first two
assertions of (1).

A prime $q\ge17$ dividing both $D_j$ and $D_c$ would divide $j+c=n$
and some $n-r$ with $1\le r\le13$, which is impossible. This proves
coprimality. If $j=c$, the same contradiction already follows from any
prime divisor of $D_j$, so the central column is excluded.

## Keeping the extra divisors in the numerical proof

Apply the index-13 polynomial certificate to row $N=n-1$. Its row
multiplicities, in the order $t=0,\ldots,12$, are

$$
m=(114,111,111,103,99,99,89,78,70,63,57,51,46).
$$

The certificate has total degree at most 641, and its exact exponent
gain after accounting for primes $2,3,5,7,11$ is $1287/200$. These facts
hold for every assignment of the small-prime maxima, including
coinciding positions. Its source estimates and elementary error bounds
apply for $N\ge10^{1732}$.

For the first shifted column define

$$
Q_{r,j}=[\gcd(n-r,j)]_{\ge17}\qquad(1\le r\le13).
$$

The [exact localization lemma](../../methods/details/gcd_localization.md)
and (4) say that, at a prime $q\ge17$ dividing $n-r$, the missing
valuation in the polynomial divisibility argument is exactly

$$
m_{r-1}\min\{v_q(n-r),v_q(j)\}.
$$

Consequently the index-13 argument remains valid on inserting the
factor

$$
\prod_{r=1}^{13}Q_{r,j}^{m_{r-1}}
$$

on its right side. No new loss is required at 13: its numerator
valuation is one, already covered by the certificate's factor
$13^{114}$. All smaller-prime estimates, coefficient estimates, and
conversion from $N-12$ to $N$ remain the same.

The complete numerical constant in that argument is less than
$10^{356876}$: it combines the coefficient bound $10^{355721}$,
$13^{114}<10^{128}$, the off-maximum factor
$(12!)^{114}<10^{1026}$, and the remaining factor $1000/999<10$.
Thus

$$
 N^{1287/200}
 \le 10^{356876}\prod_{r=1}^{13}Q_{r,j}^{m_{r-1}}
 \le 10^{356876}D_j^{114}. \tag{5}
$$

For the last inequality, each prime at least 17 divides at most one
of the thirteen consecutive factors, so $D_j=\prod_rQ_{r,j}$, and
$m_{r-1}\le114$. The nonvanishing part of the certificate is applicable:
both coordinates $(j-1,c)$ exceed 13. The same argument at $(j,c-1)$
gives the bound for $D_c$, proving (2).

## The divisors contain whole prime powers

If $q\ge17$ divides $n-r$, put $A=v_q(n-r)$. Badness and Kummer give

$$
j\bmod q^A\le r<q.
$$

If $q\mid j$, this residue must be zero. Hence $q^A\mid j$.
Likewise, $q\mid c$ implies $q^A\mid c$. Thus each prime contributing
to $D_j$ or $D_c$ contributes its entire prime-power factor in the
corresponding $n-r$. Its Kummer point is respectively $(0,r)$ or
$(r,0)$ modulo that entire prime power.

## What the bound adds

The usual row multiplicity argument uses only the total large-prime
part of each $n-r$. The divisors in (2) locate a growing part of it at
boundary Kummer points: a prime power dividing $j$ has first coordinate
zero modulo that prime power, and a prime power dividing $c$ has second
coordinate zero. A certificate that gives greater multiplicity at those
boundary points can retain this information. Formula (2) alone leaves
$j$ and $c$ free to be comparable to $n$, so it does not supply a
stopping bound.
