---
name: research/erdos_699/proofs/details/cutoff_and_cubic
title: "Erdős 699: cutoff 35 and the cubic case"
desc: "A certified interval argument excludes i=29 and every i>=35. The cubic case is reduced to n=2^h u with u odd and 3u^3<2^h, verified through 10^12, and its uniform fat-point obstruction is determined exactly."
created: 2026-09-21T19:30:00Z
updated: 2026-10-14T00:26:52Z
---

# Erdős 699: cutoff 35 and the cubic case

[[research/erdos_699/_index|P699 research]] ·
[[problems/factorials_binomials/E0699/_index|Erdős problem 699]] ·
[[research/erdos_699/archive/previous_bounds/effectivity|Earlier effectivity reduction]]

***

Call $(n,i,j)$ admissible if $1\le i<j\le n/2$, and bad if no prime
$p\ge i$ divides both $\binom ni$ and $\binom nj$.
All conclusions below concern this original, non-strict threshold.

**Further small-index progress.** The [cutoff-nine proof](cutoff_9.md)
excludes seven and every $i\ge9$. The four indices $4,5,6,8$ still
lack effective row bounds here. The cubic results below are unchanged.

**Further cubic progress.** The [follow-up note](../../remaining/details/cubic_followup.md)
strengthens the computational exclusions to $n\le10^{19}$ and every row
with $v_2(n)\le48$. It also gives an endpoint divisibility criterion,
bounds on individual prime-power components, and an infinite family of
good columns. Global cubic finiteness remains unproved. The original
computation through $10^{12}$ is retained below.

**Results of this investigation.**

1. There are no bad triples with $i\ge35$, or with $i=29$.
   This is a computer-assisted consequence of the retained algebraic
   arguments: a certified interval calculation handles $i=29$ and
   $35\le i\le905$, and the earlier theorem handles $i\ge906$.
2. A bad triple with $i=3$ must satisfy
   $$n=2^h u,\qquad h\ge2,\quad u\text{ odd},\quad
   3u^3<2^h,\qquad 4\le j<n/2.\tag{1}$$
   An exact search using these reductions excludes every $n\le10^{12}$.
   This does not prove that the remaining cubic exceptions are finite.
3. The least possible degree-to-multiplicity ratio for a nonzero polynomial
   vanishing uniformly on the six Kummer points $\Delta_3$ is exactly
   $9/4$. The manuscript's exponent argument would require a ratio below
   $2$, so optimizing that uniform certificate cannot resolve $i=3$.

**Cutoff statement.** For every admissible $(n,i,j)$ with $i=29$ or
$i\ge35$, there is a prime $p\ge i$ dividing both binomial coefficients.
The proof combines the finite certificates below with the published
prime-gap computation and the $i\ge906$ result.

The deductions and computations here are repository work. Their novelty has
not been assessed. The algebraic inputs come from the retained
detailed manuscript
and its reconstruction. The previous
[$i\ge906$ calculation](../../../../../library/factorials_binomials/van_doorn_rocca_2026_binomial_coefficients_sharing_large_prime_divisor/_index.md)
remains an input for the infinite tail.

## 1. A sharper symmetric discriminant bound

Put

$$c=n-j,\qquad G=\gcd\!\left(\binom ni,\binom nj\right),\qquad
D=\binom ni/G,\qquad K_i=\prod_{r=1}^i r^r.$$

Every coefficient of

$$
R(z)=\sum_{r=0}^i\binom{j}{i-r}\binom cr z^r
$$

is divisible by $D$. Indeed,

$$\binom ni\binom ir\binom{n-i}{j-i+r}
=\binom nj\binom{j}{i-r}\binom cr,$$

and cancellation of the gcd shows that $D$ divides the product on the
right after removing $\binom nj$.
Consequently $D^{2i-2}\mid\operatorname{Disc}R$ for $i\ge2$.

Cancel the displayed factors of $\binom ji$ in the manuscript's Jacobi
discriminant formula, and reverse the index in its $j$-product. This gives
the symmetric identity

$$\begin{aligned}
\left|\operatorname{Disc}R\right|
=\frac{K_i}{(i!)^{2i-2}}
&\prod_{r=1}^i\bigl((j-r+1)(c-r+1)\bigr)^{i-r}\\
&\times\prod_{r=1}^i(n-r+1)^{r-1}>0.
\end{aligned}\tag{2}$$

Since $(j-r+1)(c-r+1)\le n^2/4$ and $n-r+1\le n$,

$$D\le\frac{K_i^{1/(2i-2)}}{i!}\,
\frac{n^{3i/4}}{2^{i/2}}.$$

Thus, without any additional restriction on $j$,

$$G\ge
\left(\prod_{r=0}^{i-1}\left(1-\frac rn\right)\right)
\frac{(4n)^{i/4}}{K_i^{1/(2i-2)}}.\tag{3}$$

This retains much more than the earlier bound with $(4n/27)^{i/4}$.
If $n\ge L$ and

$$
\gamma_i(L)=1-\frac{i(i-1)}{2L}>0,
$$

then the product in (3) is at least $\gamma_i(L)$.

## 2. Two necessary size bounds under badness

Let $S_i=\{p:p<i\}$, $s_i=\pi(i-1)$, and write
$\binom ni=U_i(n)V_i(n)$, where $U_i$ is supported on $S_i$ and $V_i$
on primes at least $i$. Under badness, $G$ divides $U_i$.

For $i\ge5$ put

$$k=\left\lfloor\frac{2i}{3}\right\rfloor,\quad
m=3k-i+1,\quad A=\frac{k(k+1)}2,\quad
\lambda_i=i-\frac{3A}{m}.$$

The reconstructed fat-point divisor gives
$V_i(n)^m<n^{3A}/4^A$: pair the vertical and horizontal factors and use
$(j-r)(c-r)\le n^2/4$.
Together with (3), this gives the two necessary inequalities

$$\begin{aligned}
U_i(n)&>C_{f,i}(L)n^{\lambda_i},&
C_{f,i}(L)&=\frac{\gamma_i(L)4^{A/m}}{i!},\\
U_i(n)&\ge C_{o,i}(L)n^{i/4},&
C_{o,i}(L)&=\frac{\gamma_i(L)4^{i/4}}{K_i^{1/(2i-2)}}.
\end{aligned}\tag{4}$$

The fat-point bound is useful at large $n$ even when $i/4\le s_i$.
The discriminant bound is often stronger near the lower end of the search.

Kummer's formula also gives

$$v_p\!\left(\binom ni\right)
=\sum_{a\ge1}{\bf1}_{\{n\bmod p^a<i\bmod p^a\}}.\tag{5}$$

The first $v_p(i)$ summands vanish, so

$$U_i(n)\le\frac{n^{s_i}}{[i]_{S_i}},\qquad
[i]_{S_i}=\begin{cases}i,&i\text{ composite},\\1,&i\text{ prime}.
\end{cases}\tag{6}$$

For $i=29$ and every $35\le i\le905$, $\lambda_i-s_i>0$.
Combining (4) and (6) therefore gives an explicit last row. When
$i/4-s_i>0$, the discriminant bound supplies another last row, and we take
the smaller certified bound. The checker rounds upward to a power of ten
and includes that endpoint in the interval being checked.

## 3. Excluding the entire remaining interval

Let $P_i$ be the lower endpoint of the first prime gap longer than $i$.
If $n<P_i$, a prime lies in $(n-i,n]$ and divides both required binomial
coefficients. Thus a bad triple must have $n\ge P_i$.
The [retained prime-gap records](../../computations/erdos_699_prime_gap_records.json)
come from the authors' [published computation and data](https://sweet.ua.pt/tos/gaps.html).
Their range covers all the lower endpoints used here. The JSON records the
source URL, publication and retrieval date of the downloaded table.

For each index, use $L=P_i$ in (4) and let $B_i$ be the inclusive upper
bound from (6). It remains to exclude the finite interval $[P_i,B_i]$.
The upper bounds can be enormous—for example, the checker uses $10^{99}$
at $i=35$—so it does not enumerate rows.

For an integer interval $[a,b]$, define

$$E_p(a,b)=\sum_{\substack{p^r\le b\\i\bmod p^r>0}}
{\bf1}_{\{\lfloor a/p^r\rfloor<\lfloor b/p^r\rfloor
\ \text{or}\ a\bmod p^r<i\bmod p^r\}}.\tag{7}$$

The indicator is one exactly when at least one integer in $[a,b]$ can
satisfy the corresponding residue condition in (5). Therefore, for every
$n\in[a,b]$,

$$
U_i(n)\le\prod_{p<i}p^{E_p(a,b)}.\tag{8}
$$

An interval contains no bad row if

$$\max\left\{
\log C_{f,i}(P_i)+\lambda_i\log a,
\log C_{o,i}(P_i)+\frac i4\log a
\right\}
>\sum_{p<i}E_p(a,b)\log p.\tag{9}$$

Both lower bounds increase with $n$, so checking them at the left endpoint
is enough. If (9) is not certified, bisect the interval into disjoint integer
intervals and continue. Every accepted leaf has a rigorous positive margin;
an unexcluded singleton or an exhausted node budget causes the checker to
fail rather than report a proof.

The [complete checker](../../computations/erdos_699_i_ge_35.py) completed
for $i=29$ and all $35\le i\le905$. Its
[recorded output](../../computations/erdos_699_i_ge_35.json) contains
872 index records and **399,713 certified leaf intervals**. The smallest
certified logarithmic margin is

$$
0.000002955528673145503749555906958254425679887042203481750,
$$

at $i=49$. It uses 60-digit Decimal intervals with outward rounding;
floating point guides subdivision but cannot certify a leaf.
The exact valuation bound was also checked against factorial valuations in
37,829 bounded cases. Each index record includes a hash of its interval
partition for reproducibility.

Combining this completed calculation with the retained $i\ge906$ theorem
proves the stated cutoff **$i\ge35$**, together with the additional case
**$i=29$**. The statement is computer-assisted and uses the cited prime-gap
computation.

## 4. What fails at index three

At $i=3$, the small-prime set is just $\{2\}$, and $U_3(n)\le n$ is
already effective. It cannot be replaced by a uniform smaller power of $n$:
for every $h\ge2$,

$$
U_3(2^h)=2^h.
$$

The finiteness argument would need $V_3(n)<n^\rho$ with $\rho<2$, so that
$U_3(n)\gg n^{3-\rho}$ grows faster than $n$. This is an exponent
obstruction, separate from the ineffective constant at the other small indices.

In fact the uniform fat-point method has the following exact limitation.

**Proposition.** If a nonzero polynomial of degree $d$ vanishes to order at
least $m$ at every point of

$$
\Delta_3=\{(0,0),(1,0),(0,1),(2,0),(1,1),(0,2)\},
$$

then $d/m\ge9/4$. Equality is attained.

**Proof.** View these points as the three vertices and three edge midpoints
of the triangle with barycentric coordinates $X,Y,Z=2-X-Y$.
Multiplying the six transforms of the polynomial under permutations of
$X,Y,Z$ makes it symmetric, multiplying both $d$ and the required $m$ by
six. Thus we may assume that the three outer lines $X=0,Y=0,Z=0$ occur
with the same multiplicity $a$, and the three inner lines $X=1,Y=1,Z=1$
with the same multiplicity $b$.

Remove those six line factors. The remaining polynomial $H$ has degree
$D=d-3a-3b$, has none of those lines as a component, and has multiplicities
at least $m-2a$ at the vertices and $m-a-2b$ at the midpoints.
Bézout on an outer line and an inner line, respectively, gives

$$
d+2a-b\ge3m,\qquad d-a+b\ge2m.
$$

Adding shows $a\ge5m-2d$.
For any degree-$D$ polynomial, the sum of its multiplicities at three
noncollinear points is at most $2D$. To see this, send the three points to
the coordinate vertices in the projective plane: every nonzero homogeneous
monomial must have its three exponents at most $D$ minus the corresponding
multiplicities, and its exponents sum to $D$.
Applying this to the midpoints of $H$ gives

$$3m-3a-6b\le2(d-3a-3b),\qquad
a\le(2d-3m)/3.$$

Consequently $5m-2d\le(2d-3m)/3$, or $d\ge9m/4$.
Finally,

$$
X^2Y^2(X-1)(Y-1)(X+Y-1)(X+Y-2)^2\tag{10}
$$

has degree nine and multiplicity four at each of the six points. This
attains equality. $\square$

This proposition rules out fixing the manuscript's cubic exponent argument
by replacing its uniform vanishing polynomial with a better one. Additional
information about the labels or the small-prime part is needed.

## 5. Elementary cubic exclusions

For an odd prime $q$ dividing $n-t$, $t\in\{0,1,2\}$, write
$q^a\Vert n-t$. Such a prime divides $\binom n3$ except when
$q=3$ and $a=1$. If it does divide $\binom n3$, badness and Kummer imply
the **full** prime-power restriction

$$
j\bmod q^a\in\{0,\ldots,t\}.\tag{11}
$$

For $q=3$ and $a\ge2$, this uses the absence of carries in all the first
$a$ digits, even though the denominator $3!$ removes one factor of $3$.

**The central column is good.** Suppose $n$ is even and $n\ge8$.
There is an odd prime divisor $q$ of $n-1$ which divides $\binom n3$:
otherwise $n-1$ would be $1$ or $3$. For $j=n/2$,

$$
j\bmod q=(q+1)/2>1=n\bmod q,
$$

so $q\mid\binom nj$ by Lucas. Thus a bad triple has $j<n/2$.

**Odd rows are good.** If $n$ is odd and $v_3(n)\ne1$, applying (11) at
$t=0$ to all prime powers of $n$ gives $n\mid j$, impossible.
If $v_3(n)=1$, it gives $(n/3)\mid j$, so $j=n/3$.
But $n-2$ has a prime divisor $q\ge5$, and (11) would require
$j\equiv r\pmod q$ for $r\in\{0,1,2\}$. The equation $3j=n$ then
forces $q\mid3r-2\in\{-2,1,4\}$, again impossible.

**Rows $n\equiv2\pmod4$ are good.** Their odd part is $n/2$.
If $v_3(n)\ne1$, (11) gives $(n/2)\mid j$, forcing the already excluded
central column. If $v_3(n)=1$, it gives $(n/6)\mid j$, so
$j\in\{n/6,n/3,n/2\}$.
The central column is good. For $j=n/3$, any prime divisor $q\ge5$ of
$n-1$ would have to divide $3r-1\in\{-1,2\}$, where $r=0$ or $1$.
For $j=n/6$, every prime power $q^a\Vert n-1$ would have to divide
$6r-1\in\{-1,5\}$. As $n-1$ is odd and coprime to $3$, this forces
$n-1\in\{1,5\}$, giving no admissible triple.

We have therefore proved that a bad cubic triple must have $4\mid n$
and $j<n/2$.

## 6. A strong restriction on the odd part of a bad row

Write $n=2^h u$ with $h\ge2$ and $u$ odd. Then

$$
U_3(n)=2^h,\qquad V_3(n)=\frac{u(n-1)(n-2)}6.
$$

For the cubic orbit polynomial, direct expansion of the cubic discriminant gives

$$\operatorname{Disc}R=
\frac{j^2c^2(j-1)(c-1)(n-1)(n-2)^2}{12}
=\frac{F}{12}.\tag{12}$$

Since $V_3(n)$ divides every coefficient under badness,
$V_3(n)^4\mid\operatorname{Disc}R$.
Also $8\mid\operatorname{Disc}R$ when $4\mid n$:
if $j,c$ are odd, $(j-1)(c-1)$ is divisible by $8$, and $(n-2)^2$ by
$4$; if $j,c$ are even, $j^2c^2(n-2)^2$ is divisible by $64$.
Thus in both cases $32\mid F$, and division by $12$ leaves a factor $8$.
As $V_3(n)$ is odd,

$$
8V_3(n)^4\le\operatorname{Disc}R=F/12.
$$

Using $jc\le n^2/4$ and $(j-1)(c-1)\le(n-2)^2/4$ gives

$$F\le\frac{n^4(n-1)(n-2)^4}{64},\qquad
u^4\le\frac{27}{128}\frac{n^4}{(n-1)^3}.$$

Since $n\ge8$,

$$
u^4\le\frac{108}{343}n<\frac n3.
$$

Substituting $n=2^h u$ proves $3u^3<2^h$, completing (1).
Equivalently, the odd part satisfies $u<(n/3)^{1/4}$; for each fixed
$h$ there is an explicit finite list of possible rows.

The missing step for global finiteness is an upper bound on $h$ or another
argument that excludes the family as $h\to\infty$. Condition (1) alone
still allows arbitrarily large powers of two, so it is not a finite-set
reduction.

## 7. Exhaustive cubic verification through one trillion

The [cubic checker](../../computations/erdos_699_i_eq_3.py) generates
every row allowed by (1) up to the requested limit. It factors the three
numerator factors by exact trial division, intersects (11) by CRT, and
tests the full Lucas conditions on any surviving columns.

At $n\le10^{12}$ there are exactly **2,184 rows** requiring this search.
None has even one column $4\le j<n/2$ satisfying all the full
prime-power restrictions (11). Thus there are no bad cubic triples in
that entire range. See the
[recorded output](../../computations/erdos_699_i_eq_3.json).

The implementation was compared with direct binomial gcds for both
thresholds $p\ge3$ and $p>3$ through $n=200$, and the cubic discriminant
identity was checked exactly on those admissible pairs.
As positive controls it detects the strict-threshold exceptions
$(n,i,j)=(10,3,5),(28,3,14),(244,3,122),(2188,3,1094)$ and correctly
rejects them as counterexamples to the original threshold $p\ge3$.

## Reproduction and current remaining cases

Both commands use Python 3.11 or later and only the standard library:

```sh
python3 wiki/research/erdos_699/computations/erdos_699_i_ge_35.py
python3 wiki/research/erdos_699/computations/erdos_699_i_eq_3.py --limit 1000000000000
```

The earlier [effectivity note](../../archive/previous_bounds/effectivity.md) supplies
effective finiteness at $i=28,31,34$, without instantiated numerical
constants. At that stage it left 27 ineffective indices,
$\{4,\ldots,27,30,32,33\}$. The subsequent
[prime-pair argument](../../archive/previous_bounds/small_index_effective.md) lowers the
cutoff to $26$, also excludes $17,23$, and reduces the ineffective list
to nine indices. The earlier reduction recorded here was:

- $i=3$, only in the sparse family (1), with all rows through $10^{12}$ excluded;
- a finite possible exceptional set at $4\le i\le34$, $i\ne29$.

No global finiteness or nonexistence assertion is proved for the first item.
