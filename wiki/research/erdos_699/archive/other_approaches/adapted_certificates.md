---
name: research/erdos_699/archive/other_approaches/adapted_certificates
title: "Erdős 699: certificates adapted to the small-prime positions"
desc: "An explicit weighted polynomial confines the remaining position patterns at indices 27, 30, and 33 to 67, 97, and 139 possibilities, with effective bounds for all other patterns."
created: 2026-09-22T02:17:46Z
updated: 2026-10-14T00:26:52Z
---

# Erdős 699: certificates adapted to the small-prime positions

***

This is a retained earlier research note. The [[research/erdos_699/_index|current reading guide]] gives the latest status and distinguishes completed proofs from remaining cases.

[[research/erdos_699/_index|P699 research]] ·
[[problems/factorials_binomials/E0699/_index|Erdős problem 699]] ·
[[research/erdos_699/archive/previous_bounds/effectivity|Effectivity reduction]]

The uniform certificate discards which numerator factor contains the largest
power of each small prime. Retaining these positions gives effective bounds
for additional families. It does not give a row bound for an entire new
index.

At $i=27,30,33$, put $s=\pi(i-1)$, so $i=3s$ and respectively $s=9,10,11$.
For a bad triple beyond an effectively computable bound, the selected
positions of the $s$ small primes must be distinct. If their set is $T$, then

$$
 \sum_{t\in T}t\le\frac{s(s+1)}2-1,
 \qquad \max T\le2s-2.                                      \tag{1}
$$

There are respectively **67, 97, and 139** sets $T$ satisfying (1), before
assigning the individual small primes to these positions. This is a finite
list of position patterns, each still allowing unbounded rows. It is not a
finite exceptional set of triples.

**Superseded.** The
[prime-pair estimates](../previous_bounds/small_index_effective.md) exclude all
three indices $27,30,33$ completely. The weighted construction below also
supplies the
[effective index-eleven proof](../../proofs/details/index_11_effective.md).

## A weighted polynomial

As usual, $c=n-j$, $i<j\le n/2$, and badness means that no prime $p\ge i$
divides both binomial coefficients. For each prime $p<i$, select
$r_p\in\{0,\ldots,i-1\}$ maximizing $v_p(n-r_p)$, and put

$$
 P_p=p^{v_p(n-r_p)},\qquad T=\{r_p:p<i\}.
$$

For an integer $1\le k\le i$, take

$$
 F_k(X,Y)=\prod_{a=0}^{k-1}
             ((X-a)(Y-a))^{k-a},\qquad D=k(k+1).             \tag{2}
$$

At each Kummer point $(x,y)$ with $x+y=t<i$, its multiplicity is

$$
 (k-x)_++(k-y)_+\ge m_t:=(2k-t)_+.
$$

The polynomial is positive at $(j,c)$, and pairing the factors gives

$$
 0<F_k(j,c)\le n^D/2^D.                                    \tag{3}
$$

Let $Q_t$ be the part of $n-t$ supported on primes at least $i$, with the
corresponding denominator factor from $i!$ removed. Thus
$\prod_tQ_t=V_i(n)$. Under badness, a prime-power component of $Q_t$ forces
$(j,c)$ to reduce to one of the Kummer points on $x+y=t$. Taylor expansion
of the integer polynomial (2) therefore gives

$$
 \prod_{t=0}^{i-1}Q_t^{m_t}\mid F_k(j,c).                    \tag{4}
$$

This remains valid at prime indices. If $i$ is prime, the factor $i!$
removes one power of $i$ from the unique numerator factor it divides; every
power remaining in $Q_t$ still comes from an active prime.

Put

$$
 H=[i!]_{\{p:p\ge i\}}
 =\begin{cases}1&i\text{ composite},\\i&i\text{ prime},\end{cases}
 \quad M=\sum_t m_t,\quad L=\sum_t t m_t,
 \quad C=2^{1-D}\bigl(H(i-1)!\bigr)^{2k}.                    \tag{5}
$$

For each $p<i$ and $t\ne r_p$, maximality gives
$v_p(n-t)\le v_p(t-r_p)$. Since $m_t\le2k$, the factors away from the
selected position contribute at most

$$
 \prod_{p<i}p^{\sum_{t\ne r_p}m_t v_p(n-t)}
 \le ((i-1)!)^{2k}.                                       \tag{6}
$$

The removed rough denominator contributes at most $H^{2k}$.
For $n\ge2L$, the product inequality

$$
 \prod_t(1-t/n)^{m_t}\ge1-L/n\ge\tfrac12
$$

and (3)--(6) now imply

$$
 \boxed{\displaystyle
  \prod_{p<i}P_p^{m_{r_p}}\ge\frac{n^{M-D}}{C}.}            \tag{7}
$$

In particular, if the selected positions are distinct and

$$
 E=\sum_{t\notin T}m_t-D>0,
$$

then $P_p\le n$ gives the explicit bound

$$
 n^E\le C\qquad(n\ge2L).                                  \tag{8}
$$

All constants are rational and can be compared exactly. For example, any
integer $B\ge2L$ with $B^E>C$ excludes every row $n\ge B$ having this
position pattern.

## The critical position sums

For $i=3s\in\{27,30,33\}$, set $k=2s-1$. Every $m_t=4s-2-t$ is positive.
If $|T|=s$, direct summation gives

$$
 E=\sum_{t\notin T}m_t-D
   =\sum_{t\in T}t-\frac{s(s+1)}2.                         \tag{9}
$$

Thus (8) handles every pattern whose position sum exceeds $s(s+1)/2$.
The constants in this calculation are:

| $i$ | $k$ | $D$ | $2L$ | $C$ |
| --- | --- | --- | --- | --- |
| 27 | 17 | 306 | 11466 | $(26!)^{34}/2^{305}$ |
| 30 | 19 | 380 | 15950 | $(29!)^{38}/2^{379}$ |
| 33 | 21 | 462 | 21472 | $(32!)^{42}/2^{461}$ |

The equality patterns also have an effective bound. If
$\sum T=s(s+1)/2$, then (7) becomes

$$
 \prod_{p<i}(n/P_p)^{m_{r_p}}\le C.                        \tag{10}
$$

All factors $n/P_p$ are at least one. A set of $s$ distinct nonnegative
integers having this sum has maximum at most $2s-1=k$, so
$m_{r_p}=2k-r_p\ge k$. Consequently the integer cofactors satisfy

$$
 \frac{n-r_p}{P_p}\le C^{1/m_{r_p}}
 \le C^{1/k}<((i-1)!)^2.                                  \tag{11}
$$

In particular, write $n-r_2=2^a u$ and $n-r_3=3^b v$. There are only
finitely many possibilities for $u,v,r_2,r_3$, all bounded explicitly by

$$
 1\le u,v<((i-1)!)^2,\qquad
 0<|r_3-r_2|\le2s-1,
$$

and they satisfy

$$
 2^a u-3^b v=r_3-r_2.                                    \tag{12}
$$

A lower bound for a nonzero linear form in logarithms makes this finite
family effective. Equivalently, the effective $S$-part theorem already used
in the [effectivity note](../previous_bounds/effectivity.md) applies to the
product of the selected distinct linear factors: all weights in (10) are
positive, so any effective positive saving contradicts (10) for sufficiently
large $n$. Equation (11) gives a direct route to numerical constants without
using that general theorem.

Repeated selected positions are effective as well. In this case the set of
selected factors has size at most $s-1$. The degree-reduction argument in the
effectivity note gives an elementary bound $U_i(n)\ll_i n^{s-1}$, whereas the
existing uniform certificate gives respectively

$$
 U_{27}(n)\gg n^{243/28},\qquad
 U_{30}(n)\gg n^{300/31},\qquad
 U_{33}(n)\gg n^{363/34}.
$$

Each exponent exceeds $s-1$. This proves (1) after combining the finitely
many effective bounds just described.

Finally write $T=\{t_0<\cdots<t_{s-1}\}$ and $a_q=t_q-q$. The integers
$a_q$ are nonnegative and nondecreasing. Condition (1) is equivalent to

$$
 \sum_{q=0}^{s-1}a_q\le s-1.
$$

These patterns are counted by $\sum_{h=0}^{s-1}p(h)$, where $p(h)$ is the
partition function, giving 67, 97, and 139. Since
$t_{s-1}\le(s-1)+\sum a_q$, the maximum-position bound in (1) follows too.
The [exact checker](../../computations/erdos_699_adapted_certificates.py)
verifies these identities and counts; it does not enumerate binomial rows.

## What the position restriction leaves open

The remaining list includes $T=\{0,\ldots,s-1\}$. Coordinate-line products
cannot eliminate this pattern, even with arbitrary weights. Indeed, write
$w_a\ge0$ for the weight of each line $X=a$ and $Y=a$, and let

$$
 \mu_t=\min_{a+b=t}(w_a+w_b).
$$

For $a=0,\ldots,s-1$, use the decompositions

$$
 s+2a=(s+a)+a,\qquad s+2a+1=a+(s+a+1).
$$

They give

$$
 \sum_{t=s}^{3s-1}\mu_t
 \le2\sum_{a=0}^{2s}w_a-w_s-w_{2s}
 \le2\sum_{a\ge0}w_a,
$$

which is the degree of the line product. Adding row-diagonal factors adds
equally to both sides. Thus this elementary position-sensitive method still
needs another arithmetic input on its remaining patterns. In particular,
it does not distinguish the assignments of the primes 2 and 3 to the
positions, and cannot by itself force their positions to be consecutive.
