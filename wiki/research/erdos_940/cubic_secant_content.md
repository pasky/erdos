---
name: research/erdos_940/cubic_secant_content
title: Local content of a cubic secant
desc: An exact valuation formula relates secant content to output divisibility and coordinate alignment; squarefree targets can still have integral third secants.
tags: []
sources: []
created: 2026-09-22T22:14:11Z
updated: 2026-09-22T22:14:11Z
---


# Local content of a cubic secant

***

## Status

The local formula and examples below are proved and checked. They refine
the arithmetic of the [uncontrolled secant ranges](cubic_collision_ranges.md),
but give no averaged collision or density estimate.

Let $a_1,a_2,a_3$ be positive integers, and suppose

$$
F(\mathbf x)=\sum_i a_i x_i^3
            =F(\mathbf x+t\mathbf k)=n>0,
\qquad t\in\mathbb Z\setminus\{0\},\quad
\mathbf x,\mathbf x+t\mathbf k\in\mathbb N^3.
$$

Set

$$
C=F(\mathbf k),\qquad
B=\sum_i a_i x_i k_i^2,\qquad
A=\sum_i a_i x_i^2 k_i,\qquad
g=\gcd(C,3B).
$$

Expansion gives

$$
3A+3tB+t^2C=0.                                      \tag{1}
$$


## Exact good-prime content

Fix a prime $p\nmid6a_1a_2a_3k_1k_2k_3$ and suppose that both
endpoints are primitive at $p$, meaning that neither has all
coordinates divisible by $p$. Write

$$
h=v_p(n),\qquad
j=\min_{i<\ell}v_p(x_i k_\ell-x_\ell k_i).
$$

Then

$$
\boxed{v_p(g)=\min(h,2j).}                           \tag{2}
$$


**Proof.** Work in $\mathbb Z_p$, and put
$b_i=a_i k_i^3$, $r_i=x_i/k_i$. All $b_i$ are units, and

$$
C=\sum_i b_i,\quad B=\sum_i b_i r_i,\quad
A=\sum_i b_i r_i^2,\quad n=\sum_i b_i r_i^3.
$$

Set $e=v_p(g)=\min(v_p(C),v_p(B))$. Equation (1) implies
$p^e\mid A$. The identity

$$
n=(r_1+r_2+r_3)A
 -(r_1r_2+r_1r_3+r_2r_3)B+r_1r_2r_3C
$$

shows that $e\le h$; in particular $e$ is finite.

Put $\lambda=r_3$, $\delta_i=r_i-\lambda$, and

$$
L=\sum_i b_i\delta_i,\quad Q=\sum_i b_i\delta_i^2,\quad
R=\sum_i b_i\delta_i^3.
$$

Then $\delta_3=0$ and $L=B-\lambda C$, $Q=A-2\lambda B+\lambda^2C$
are divisible by $p^e$. If $e>0$, eliminate $\delta_2$ modulo $p^e$
from

$$
b_1\delta_1+b_2\delta_2=0,\qquad
b_1\delta_1^2+b_2\delta_2^2=0.
$$

This gives

$$
\frac{b_1(b_1+b_2)}{b_2}\delta_1^2=0\pmod{p^e}.
$$

The coefficient is a unit, since $b_1+b_2\equiv-b_3\pmod p$.
Hence both $\delta_1,\delta_2$ are divisible by
$p^{\lceil e/2\rceil}$. As the $k_i$ are units, this proves
$e\le2j$. It is automatic when $e=0$.

For the reverse inequality it remains to consider $j\ge1$.
Primitivity of the endpoints implies that $\lambda$ and $\lambda+t$
are units. Since $Q,R$ are divisible by $p^{2j}$, equation (1) and
the expression for $n$ give, modulo $p^{2j}$,

$$
(3\lambda^2+3t\lambda+t^2)C+3(2\lambda+t)L=0,
\qquad \lambda^3C+3\lambda^2L=n.
$$

The coefficient determinant is $3\lambda^2(\lambda+t)^2$, a unit.
Therefore $C,L$, and thus $B$, are divisible by
$p^{\min(h,2j)}$. This proves (2). The case $j=\infty$ would make
the two positive endpoints proportional over $\mathbb Q$; homogeneity
and equality of their positive cubic values would force $t=0$.
Thus it does not occur here. $\square$

## Cube-free and squarefree targets

If $n$ is cube-free, every representation is primitive at every prime.
At a good prime, $h\le2$, so (2) gives

$$
v_p(g)\in\{0,v_p(n)\}.
$$

Thus the part of $g$ supported away from
$6a_1a_2a_3k_1k_2k_3$ is a **unitary divisor** of $n$.
If $n$ is squarefree and

$$
m=\gcd_{i<\ell}(x_i k_\ell-x_\ell k_i),
$$

that good part is exactly the corresponding part of $\gcd(n,m)$.
It is governed by congruence alignment, not by the square part of $n$.

For the special form $F(x,y,z)=x^3+2y^3+4z^3$, one has

$$
F(1,31,10)=F(3,28,17)=63583=13\cdot67\cdot73.
$$

With $t=1$, $\mathbf k=(2,-3,7)$, the quantities are
$C=1326$, $B=2522$, $g=78$. The prime $13$ is good and divides
$g$, although the target is squarefree.

More strongly,

$$
F(2,37,15)=F(4,15,30)=114814=2\cdot7\cdot59\cdot139.
$$

Here $t=1$, $\mathbf k=(2,-22,15)$, $C=-7788$, $B=49324$, and
$3B/C=-19$. Consequently $g=|C|$. The cubic polynomial
$F(\mathbf x+s\mathbf k)-n$ has roots $0$, $1$, and
$-3B/C-1=18$, giving the integral third point

$$
F(38,-359,285)=114814.
$$

All the displayed factors are distinct primes. These identities
disprove the proposed elimination of integral third secants by
restricting to squarefree targets.

## Remaining gap

Formula (2) does not bound the alignment indices $m$ among actual
equal-output partners. It also leaves the primes dividing a direction
coordinate outside its scope. The quadratic-fiber discriminant
depends on $k_1k_2k_3F(\mathbf k)$, rather than just on $n$; squarefree
outputs do not make that discriminant squarefree. No estimate for the
unrestricted collision tail follows.

## A large target prime cannot occur in the secant content

The following additional lemma removes the restriction that the direction
coordinates be units at the prime. It does not bound the remaining content.

**Lemma.** In the notation above, suppose
$\|\mathbf x\|_\infty\le H$, $\|\mathbf k\|_\infty\le K$,
$p\nmid6a_1a_2a_3$, $p\mid n$, and $p>2HK$. Then $p\nmid g$.

**Proof.** If $p\mid g$, then $B$, $C$, and by (1) also $A$ vanish
modulo $p$. Together with $p\mid n$, the cubic expansion shows that the
entire projective line spanned by $\mathbf x,\mathbf k$ lies on
$F=0$ over $\mathbb F_p$, provided these vectors are independent modulo
$p$. The plane cubic $F=0$ is geometrically smooth at this prime, hence
cannot contain a line.

It follows that all minors $x_i k_j-x_j k_i$ vanish modulo $p$.
Their absolute values are at most $2HK<p$, so they vanish as integers.
Thus $\mathbf k$ is proportional to $\mathbf x$ over $\mathbb Q$.
The distinct positive vectors $\mathbf x,\mathbf x+t\mathbf k$ cannot
then have the same positive cubic value. This contradiction proves the
lemma. $\square$

The conclusion does not imply height-decreasing secant descent, even
when the target itself is prime. For $F=x^3+2y^3+4z^3$,

$$
F(7,4,2)=F(1,1,5)=503,
$$

where $503$ is prime and $503>10\cdot7^2$. Take
$t=3$, $\mathbf k=(-2,-1,1)$. Then $C=-6$, $B=44$, and $g=6$.
The third line-intersection parameter is $-3B/C-t=19$, giving
the integral point

$$
F(-31,-15,21)=503.
$$

It has greater height and lies outside the positive region. Thus even
small content and a large prime target do not force a smaller positive
partner. No positive-input-mass sieve or multiplicity estimate is
asserted here.

## Bounded logarithmic content under uniform direction sampling

For the special form $F=k_1^3+2k_2^3+4k_3^3$, put

$$
J(\mathbf k)=\gcd\bigl(F(\mathbf k),|k_1k_2k_3|\bigr)
$$

for primitive integer $\mathbf k$ with nonzero coordinates.
Then

$$
\sum_{\substack{\|\mathbf k\|_\infty\le K\\
                 \gcd(k_1,k_2,k_3)=1\\k_1k_2k_3\ne0}}
        \log J(\mathbf k)\ll K^3.                       \tag{3}
$$

Pairwise coprimality is not needed.

To prove (3), let an odd prime divide $J$. Exactly one coordinate is
divisible by it: if two were divisible, the third term in $F$ would
be a unit, by primitivity. For $q=p^e\mid J$, relabel the divisible
coordinate as $k_i$. Then $q\mid k_i$, and
$a_jk_j^3+a_\ell k_\ell^3=0\pmod q$ with both remaining coordinates
units. For each $k_j$ there are at most three possibilities for
$k_\ell$ modulo $q$. The unit cube map has kernel of size at most three
over every odd prime power, including powers of three. Also $q\le K$.
The number of these directions is consequently

$$
O(K^3/q^2+K^2/q).
$$

Summing with weight $\log p$ gives
$O(K^3+K^2\log^2(2K))=O(K^3)$; the weaker $\log^2$ bound follows
by summing over all integers rather than just prime powers.
At two, the three term valuations are in different classes modulo
three; primitivity makes their minimum at most two. Thus
$v_2(F(\mathbf k))\le2$, completing the proof.

There is a direct relation to the preceding large-prime restriction.
Clearing denominators in the identity expressing $n$ in terms of
$A,B,C$ in the proof of (2) shows

$$
g\mid 3n k_1k_2k_3.
$$

Indeed, multiplication by $k_1k_2k_3$ clears every symmetric function
of $x_i/k_i$, and $g$ divides $C,3B,3A$.
If $n=p^\nu m$ and the large-prime lemma excludes $p$ from $g$, then

$$
g\le \gcd(C,3m k_1k_2k_3)\le 3mJ(\mathbf k).             \tag{4}
$$


Equations (3)--(4) control the direction-dependent factor under
**uniform direction sampling**. Collision directions are not known to
obey this sampling law; their weights are the unknown numbers of
integral points in the associated quadratic fibers. No bounded
logarithmic multiplicity follows by replacing those weights by one.
