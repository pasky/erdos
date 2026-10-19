---
name: theory/additive_bases/L4_random_modulus_exponent/_proof
title: Proof of the random-modulus exponent
desc: |
  Product probabilities and collision-plane counts give one auxiliary basis
  and simultaneous shell selections with the original quantitative loss.
tags: []
sources: []
created: 2026-09-09T01:21:03Z
updated: 2026-10-13T13:08:56Z
---

***

We prove [L4](_index.md). Throughout, put $\gamma=\sqrt6-2$.
Logarithms in exponent estimates have base two; $\ln$ denotes the
natural logarithm. Constants may depend on this fixed $\gamma$, but not
on the lower shell index or the auxiliary-prime outcome. All thresholds
called deterministic have this same uniformity.

## External interfaces

We use Bertrand's postulate to make every auxiliary-prime interval
nonempty, cyclicity of the nonzero residues modulo a prime to define the
digits, and the prime number theorem to count source and auxiliary primes.
The probability input is the product measure on a countable sequence of
finite probability spaces. Finite expectation linearity, Markov's inequality,
and the first Borel--Cantelli lemma are used at the places stated below.
The exact source versions, locators, and reading scope are recorded in the
source record at the end of this proof.

All divisor estimates, congruence deductions, integer lattice bounds, and
finite hypergraph selection estimates needed here are proved below.
In particular, no theorem about primes in progressions or about the density
of Sidon sets, and no native L-claim, is an external mathematical premise.

## One random sequence and fixed source shells

For $j\ge1$ define the finite set

$$
\mathcal Q_j=\{q\text{ prime}:2^{2j-1}<q\le2^{2j}\}.
\tag{1}
$$

Bertrand's postulate makes each set nonempty. To construct the probability
space, regard each uniform law as a measure on $\mathbb R$. Their finite
product laws are consistent, so the countable extension theorem supplies
a measure on $\mathbb R^{\mathbb N}$. The complement of
$\Omega=\prod_j\mathcal Q_j$ is a countable union of coordinate
exceptions of measure zero. Restrict to $\Omega$, where finite cylinder
probabilities are the products of the coordinate masses. Thus the
coordinates $q_j$ are independent and uniform. For each possible prime,
fix its least positive primitive root; write $g_j$ for that of $q_j$.
The intervals (1) are disjoint, so all $q_j$ are distinct. Put

$$
Q_k=\prod_{j=1}^kq_j,\qquad b_j=4q_j,\qquad
B_k=\prod_{j=1}^kb_j=4^kQ_k,\qquad B_0=1.
$$

For every outcome, multiplication of the bounds in (1) gives

$$
2^{k^2}<Q_k\le2^{k^2+k},\qquad
2^{k^2+2k}<B_k\le2^{k^2+3k}.
\tag{2}
$$

Choose one deterministic integer $k_0$ large enough that
$\gamma(k-1)^2>2k$ for $k\ge k_0$, and that the uniform comparisons
below hold. Each comparison will have a fixed negative quadratic leading
term, so one such choice suffices. Only source shells below $k_0$ are
omitted; the auxiliary sequence starts at $j=1$. Define

$$
\mathcal P_k=\{p\text{ prime}:
2^{\gamma(k-1)^2}<p\le2^{\gamma k^2}\}
\quad(k\ge k_0).
\tag{3}
$$

These shells are deterministic and disjoint. Every $p\in\mathcal P_k$
exceeds all $q_j$ with $j\le k$. There is therefore a unique integer
$x_j(p)$ in $[q_j+1,2q_j-1]$ such that

$$
g_j^{x_j(p)}\equiv p\pmod{q_j}\quad(j\le k).
$$

The interval has exactly $q_j-1$ consecutive integers and represents
each exponent class modulo $q_j-1$ once. Put $x_j(p)=0$ for $j>k$,
and define

$$
a_p=\sum_{j=1}^kx_j(p)B_{j-1}.
\tag{4}
$$

Mixed-radix expansions with digits between $0$ and $b_j-1$ are unique:
reduce an equality modulo $b_1$, subtract the first digit, divide by
$b_1$, and repeat. The digits in (4) satisfy these bounds and have a
positive top digit. Telescoping gives

$$
1\le a_p\le\sum_{j=1}^k(b_j-1)B_{j-1}=B_k-1.
\tag{5}
$$

The map $p\mapsto a_p$ is injective. The top nonzero digit determines
the shell. Within shell $k$, equality of labels gives $p\equiv p'$
modulo every $q_j$, hence modulo their product $Q_k$. Both source
primes are at most $2^{\gamma k^2}<Q_k$, so they are equal.

Write $n_k=|\mathcal P_k|$ and $X_k=2^{\gamma k^2}$. The prime
number theorem gives

$$
n_k\sim\frac{X_k}{\ln X_k},\qquad
\log_2 n_k=\gamma k^2+O(\log(k+1)).
\tag{6}
$$

Indeed, the contribution of the lower endpoint is at most $X_{k-1}$,
and $X_{k-1}\ln X_k/X_k$ tends to zero. Formula (6) is used only
for sufficiently large, nonempty shells.

## Atoms of a lower product and uniform divisor control

For $M=\prod_{j=1}^Lq_j$ and any integer $m$,

$$
\mathbb P(M=m)\le2^{-L^2+O(L\log(L+1))}.
\tag{7}
$$

The same bound holds conditionally on any values of
$q_{L+1},\ldots,q_K$. To prove it, the prime number theorem applied to
$(2^{2j-1},2^{2j}]$ gives $|\mathcal Q_j|\gg2^{2j}/j$ for large
$j$. By enlarging a fixed constant, this holds for every $j\ge1$.
Unique factorization and disjointness of the intervals recover each
coordinate $q_j$ from a possible product $m$. Thus at most one lower
tuple has product $m$, and its probability is

$$
\prod_{j=1}^L|\mathcal Q_j|^{-1}
\le2^{-L(L+1)+O(L\log(L+1))}.
$$

Every specified finite upper tuple has positive probability. Dividing its
joint cylinder probability with a lower tuple by its own cylinder
probability cancels exactly the upper factors. The lower coordinates
therefore remain independent and uniform under the indicated conditioning.
This proves both versions of (7), without a separate assertion about
regular conditional probabilities.

We also need, for each fixed $C_0>0$, the uniform estimate

$$
\max_{1\le m\le2^{C_0K^2}}2\tau(m)
\le2^{O_{C_0}(K^2/\log K)},
\tag{8}
$$

where $\tau(m)$ counts the positive divisors of $m$. Here is a direct
proof. Let $H\ge e^4$, $u=\ln H$, and factor any $1\le m\le H$
as $\prod_p p^{e_p}$. Every exponent is at most $u/\ln2$. The
primes at most $\sqrt u$ contribute at most
$\sqrt u\ln(1+u/\ln2)$ to $\ln\tau(m)$. For larger primes,

$$
\sum_{p>\sqrt u}e_p\le\frac{2u}{\ln u},\qquad
\sum_{p>\sqrt u}\ln(e_p+1)\le\frac{2(\ln2)u}{\ln u}.
$$

The first contribution is also $O(u/\ln u)$, since
$(\ln u)^2/\sqrt u\to0$. The argument includes $m=1$, with an
empty factorization. Set $H=2^{C_0K^2}$ to obtain (8). A nonzero
integer $F$ has exactly $2\tau(|F|)$ ordered signed factor pairs:
choose a positive divisor $|v|$ and either sign of $v$, then $F/v$
is fixed. Thus (8) controls signed factorizations uniformly as well.

## Repeated sums lie in congruence fibers

The addition of two labels has no carries: every digit sum is at most
$4q_j-2<b_j$. For a sum with shell indices $K\ge L$, its digits
belong to the following disjoint ranges:

$$
\begin{array}{c|c}
j\le L &[2q_j+2,4q_j-2]\\
L<j\le K &[q_j+1,2q_j-1]\\
j>K &\{0\}.
\end{array}
\tag{9}
$$

Mixed-radix uniqueness therefore recovers the unordered shell pair from
the sum, including the case $K=L$. For two representations within that
same shell $K$, exponentiating equality of digit sums gives equality of
the prime products modulo $Q_K$. Both products are at most
$2^{2\gamma K^2}<Q_K$, since $2\gamma<1$. They are equal as
integers, and unique factorization identifies the unordered pair. This
also proves uniqueness when a pair is diagonal.

Now let $K>L\ge k_0$, and put

$$
M=Q_L,\quad N=Q_K/Q_L,\quad
X=2^{\gamma K^2},\quad Y=2^{\gamma L^2},\quad
\lambda=L^2/K^2.
$$

The moduli are coprime and satisfy

$$
2^{L^2}<M\le2^{L^2+L},\qquad
2^{K^2-L^2}<N\le2^{K^2-L^2+K-L},\qquad MN=Q_K.
\tag{10}
$$

Define a fiber to be a level set of the map

$$
\Phi_{K,L}(P,R)=(P\bmod N,PR\bmod M),
\qquad(P,R)\in\mathcal P_K\times\mathcal P_L.
\tag{11}
$$

Equal label sums imply equal images in (11): the digits above $L$
give equality of the upper primes modulo $N$, and the digits through
$L$ give equality of the products modulo $M$. The converse is not
needed and is not asserted.

Both coordinate projections are injective within a fiber. If the upper
coordinate is fixed, cancellation modulo $M$ gives equality of the
lower coordinates because they lie below $M$. If the lower coordinate
is fixed, cancellation modulo $M$ and the first residue in (11) give
equality of the upper coordinates modulo $MN$; they lie below $MN$.
All cancellations are valid: both source primes exceed the auxiliary
primes dividing $M$. The upper prime is also coprime to $N$.

Two distinct pairs in a fiber force $N<X$, from their nonzero upper
difference. Their prime products are distinct by unique factorization and
disjointness of the shells, so they also force $M<XY$. By (10),

$$
1-\gamma<\lambda<\frac\gamma{1-\gamma}.
\tag{12}
$$

There are no triples outside this strict collision band. In particular,
within the band $L$ is comparable with $K$, with fixed comparison
constants, and $\lambda>1/2$.

Let $T_{K,L}$ count three-element subsets of one fiber, summed over
all fibers. In a triple order the upper primes as $P_1<P_2<P_3$.
The corresponding lower primes $R_1,R_2,R_3$ are distinct. There are
unique integers $a,b,s,t$ such that

$$
\begin{aligned}
P_2&=P_1+Na,&P_3&=P_1+Nb,&0<a<b<X/N,\\
P_2R_2-P_1R_1&=Ms,&P_3R_3-P_1R_1&=Mt.
\end{aligned}
\tag{13}
$$

The integers $s,t$ are nonzero and distinct. Each forbidden equality
would equate two prime products from disjoint shells and hence repeat a
pair. Both signs of these offsets must be retained.

## Fixed-modulus count for the lower part of the band

In this section use the actual moduli and write

$$
U=X/N,\qquad Z=XY/M,\qquad W=2XY^2/(MN).
$$

We prove, for every auxiliary outcome and uniformly on (12) with
$\lambda\le2/3$,

$$
T_{K,L}\le
2^{(5\gamma-3)K^2+4\gamma L^2+O(K^2/\log K)}.
\tag{14}
$$

If $T_{K,L}=0$, (14) holds. Otherwise fix a triple. Its parameters
satisfy $0<a<b<U$ and
$0<|s|,|t|<Z$. Rewriting (13) gives

$$
\begin{aligned}
P_1(R_2-R_1)+NaR_2&=Ms,\\
P_1(R_3-R_1)+NbR_3&=Mt.
\end{aligned}
\tag{15}
$$

Eliminate $P_1$. The result is $NE=MF_0$, where

$$
\begin{aligned}
E&=aR_2(R_3-R_1)-bR_3(R_2-R_1),\\
F_0&=s(R_3-R_1)-t(R_2-R_1).
\end{aligned}
$$

Coprimality gives an integer $d$ with

$$
E=dM,\qquad F_0=dN,\qquad |d|<W,
\tag{16}
$$

the last inequality following from $|E|<2UY^2$.

Here are all four size comparisons needed below. The source lower
endpoints, (10), and $\lambda\le2/3$ give

$$
\begin{aligned}
\log_2(U/R_i)
&<-(1-\gamma)(K^2-L^2)+2\gamma L-\gamma\\
&\le-(1-\gamma)K^2/3+2\gamma K,\\
\log_2(U/P_i)
&<-(K^2-L^2)+2\gamma K-\gamma\\
&\le-K^2/3+2\gamma K,\\
\log_2(2XY/(P_2P_3))
&<1-\gamma(K^2-L^2)+4\gamma K-2\gamma\\
&\le-\gamma K^2/3+4\gamma K+1,\\
\log_2(WU^3/M)
&<1+[4\gamma-4+(2\gamma+2)\lambda]K^2\\
&\le1+(16\gamma-8)K^2/3.
\end{aligned}
\tag{17}
$$

All leading coefficients are negative because $0<\gamma<1/2$.
For all sufficiently large $K$, uniformly in $L$ and the outcome,

$$
U<R_i,\qquad U<P_i,\qquad 2XY<P_2P_3,\qquad WU^3<M.
\tag{18}
$$

If $d=0$, reduce $E=0$ modulo the prime $R_2$. Distinctness of
the three lower primes gives $R_2\mid b$, impossible since
$0<b<U<R_2$. Thus $0<|d|<W$.

Fix $(a,b,s,t,d)$ and set $\Delta=at-bs$. Suppose first that
$\Delta\ne0$, and define

$$
\rho=R_2-R_3,\qquad \sigma=atR_2-bsR_3.
$$

Multiply $E=dM$ by $s-t$ and use
$(s-t)R_1=sR_3-tR_2-dN$ from (16). Its quadratic part is
$atR_2^2-(at+bs)R_2R_3+bsR_3^2=\rho\sigma$, giving

$$
\rho\sigma=d\{M(s-t)-NaR_2+NbR_3\}.
$$

Also

$$
R_2=\frac{\sigma-bs\rho}{\Delta},\qquad
R_3=\frac{\sigma-at\rho}{\Delta}.
\tag{19}
$$

Substitution and multiplication by $\Delta$ yield

$$
\Delta\rho\sigma=d\Delta M(s-t)
+dN(b-a)\sigma+dNab(s-t)\rho.
$$

Multiply by $\Delta$ once more and complete the product:

$$
\begin{aligned}
&(\Delta\rho-dN(b-a))(\Delta\sigma-dNab(s-t))\\
&\qquad=d(s-t)\{\Delta^2M+dN^2ab(b-a)\}=:F.
\end{aligned}
\tag{20}
$$

This integer $F$ is nonzero. Otherwise, as $d(s-t)\ne0$, the
braces vanish. Reduction modulo $M$ and coprimality of $M,N$ give
$M\mid dab(b-a)$. But

$$
0<|dab(b-a)|<WU^3<M,
$$

a contradiction. Every factor in the defining expression for $F$ is
at most $2^{C_1K^2}$ in absolute value for a fixed $C_1$: this
follows directly from $L<K$, (10), and the bounds on $a,b,s,t,d$.
Because the expression is a fixed polynomial, $|F|\le2^{C_2K^2}$
for a fixed $C_2$. Estimate (8) gives at most
$2^{O(K^2/\log K)}$ ordered signed factor pairs in (20).

Each factor pair determines $\rho,\sigma$ because $\Delta\ne0$,
then $R_2,R_3$ by (19), then $R_1$ by (16) because $s-t\ne0$.
Finally (15) determines $P_1$ because $R_2-R_1\ne0$, and (13)
determines $P_2,P_3$. Invalid or nonintegral reconstructions are simply
discarded. No additional choice of a prime or a fiber remains.

If instead $\Delta=0$, put $e=\gcd(a,b)$, $a=ea'$, $b=eb'$.
Then $\gcd(a',b')=1$ and $a't=b's$, so $s=fa'$, $t=fb'$
for a nonzero integer $f$. Let $C_3=fM-NeR_1$. Substituting in
(15), or replacing $P_1$ by $P_2-Nea'$, gives

$$
a'C_3=P_2(R_2-R_1),\qquad b'C_3=P_3(R_3-R_1).
$$

The bounds $a'<U<P_2$ and $b'<U<P_3$ show that the distinct
primes $P_2,P_3$ both divide $C_3$. But $|f|<Z$, $e<U$ imply

$$
|C_3|<ZM+NUY=2XY<P_2P_3.
$$

Thus $C_3=0$, which would give $R_2=R_1$. The singular case is
impossible.

A triple forces $U,Z,W>1$. There are at most $U^2$ gap pairs,
$4Z^2$ signed offset pairs, and $2W$ possible nonzero $d$. The
uniform factor-pair bound therefore gives

$$
T_{K,L}\ll U^2Z^2W\,2^{O(K^2/\log K)}
=\frac{2X^5Y^4}{(MN)^3}\,2^{O(K^2/\log K)}.
$$

Use $MN>2^{K^2}$ to obtain (14). If no triple exists, (14) holds
without these parameter restrictions. This proof uses the fixed-modulus
estimate only on $\lambda\le2/3$.

## Integer points on a plane

Let $c\in\mathbb Z^3$ be nonzero and primitive, meaning that its
coordinates have greatest common divisor one. Define

$$
\Lambda=\{v\in\mathbb Z^3:c\cdot v=0\},\qquad
D=\|c\|_2,
$$

and let $\ell$ be the length of a shortest nonzero vector of
$\Lambda$. For $Y\ge1$ we claim

$$
|\Lambda\cap[-Y,Y]^3|\ll1+Y/\ell+Y^2/D,
\tag{21}
$$

with an absolute constant, including the displayed line term.

We first justify the lattice facts used in this count. If $c_1=c_2=0$,
then $c_3=\pm1$, and the first two coordinate vectors are a basis of
$\Lambda$. Otherwise put $d_0=\gcd(c_1,c_2)>0$ and choose integers
$u,v$ with $c_1u+c_2v=d_0$. Since $\gcd(d_0,c_3)=1$, choose
integers $a_0,b_0$ with $d_0a_0+c_3b_0=1$. The vectors

$$
w_1=(c_2/d_0,-c_1/d_0,0),\qquad
w_2=(uc_3,vc_3,-d_0),\qquad z=(ua_0,va_0,b_0)
$$

satisfy $w_1\times w_2=c$ and $c\cdot z=1$. Their determinant
is one, so their matrix has an integer inverse by the cofactor formula.
They form a basis of $\mathbb Z^3$, and $w_1,w_2$ form a basis of
the kernel. Thus its rank is two and its fundamental parallelogram has
area $D$. The same area conclusion holds in the coordinate-plane case.

A shortest vector exists because a bounded ball contains only finitely
many integer vectors and this rank-two lattice has a nonzero vector.
Write a shortest vector $v_1$ in any lattice basis. Its two integer
coordinates are coprime, since otherwise division by their common divisor
would give a shorter nonzero vector. Bezout's identity extends those two
coordinates to a determinant-one integer matrix. Hence $v_1$ extends
to a lattice basis $v_1,v_2$.

Subtract a multiple of $v_1$ from $v_2$ so that its parallel
component has absolute value at most $\ell/2$. If its perpendicular
component has length $h_0$, shortestness gives
$h_0\ge\sqrt3\ell/2$, and the area formula gives $D=\ell h_0$.
The lattice is the union of lines $jv_2+\mathbb Z v_1$ with
perpendicular spacing $h_0$. A ball of radius $R$ meets at most
$1+2R/h_0$ lines; each contains at most $1+2R/\ell$ points in
the ball. Their product is
$O(1+R/\ell+R^2/D)$ because $h_0\gg\ell$. Use
$R=\sqrt3Y$ to prove (21).

For its application, fix distinct upper primes with

$$
P_2=P_1+Na,\qquad P_3=P_1+Nb,\qquad
0<a<b,\qquad\gcd(P_1,N)=1.
$$

Let $s,t$ be nonzero distinct integers such that
$\max(|s|,|t|,|s-t|)<\min_iP_i$. Put

$$
g=\gcd(a,b),\qquad
h=\frac{\max(|s|,|t|,|s-t|)}{\gcd(|s|,|t|)},\qquad
P_-=2^{\gamma(K-1)^2}.
$$

The number of integer triples in $[1,Y]^3$ satisfying

$$
(t-s)P_1R_1-tP_2R_2+sP_3R_3=0
\tag{22}
$$

is at most

$$
\ll1+Yh\left(\frac1N+\frac gb\right)
+\frac{Y^2}{P_-h}.
\tag{23}
$$

To prove this, divide $s,t$ by their positive common divisor; the plane
is unchanged. Use the reduced coprime values for the rest of this plane
calculation, so their maximum, including $|s-t|$, is $h$. The normal

$$
c=((t-s)P_1,-tP_2,sP_3)
$$

is primitive. A prime different from all $P_i$ dividing every
coordinate would divide both $s$ and $t$. A prime equal to one of
the $P_i$ cannot divide the other coordinates: those upper primes are
distinct and all three small coefficients are nonzero of magnitude less
than every $P_i$. This excludes every common prime factor. At least
one of $t-s,-t,s$ has magnitude $h$, so $D\ge P_-h$.

For a lattice vector $v$, rewrite its plane equation as

$$
P_1\{(t-s)v_1-tv_2+sv_3\}
+N\{-ta v_2+sb v_3\}=0.
\tag{24}
$$

Coprimality implies that the first integer brace is divisible by $N$.
If $\|v\|_\infty<N/(3h)$, its absolute value is less than $N$,
so both braces vanish. The integer vector
$((t-s)v_1,-tv_2,sv_3)$ then has coordinate sum zero and satisfies
the additional relation $a(-tv_2)+b(sv_3)=0$. Dividing $a,b$ by
$g$ and using coprimality shows it is an integer multiple of

$$
((b-a)/g,-b/g,a/g).
$$

For $v\ne0$ the multiple is nonzero. Its largest coordinate has
magnitude at least $b/g$, whereas every coordinate has magnitude at
most $h\|v\|_\infty$. Therefore every nonzero lattice vector has

$$
\|v\|_\infty\ge
\min\left\{\frac{N}{3h},\frac{b}{gh}\right\}.
\tag{25}
$$

Its Euclidean length is no smaller. Substitute (25) and $D\ge P_-h$
in (21), using the sum of the two reciprocals to bound the reciprocal
of their minimum. This proves (23).

## Conditional averaging, including the line contributions

Fix $K,L$ in (12), and condition on $q_{L+1},\ldots,q_K$. This
fixes $N$. Define the deterministic lower-product envelope and ranges

$$
M_0=2^{L^2},\qquad U=X/N,\qquad Z=XY/M_0.
\tag{26}
$$

Here $Z$ differs from the actual-modulus quantity used in (14).
The lower coordinates remain random; their product $M$ exceeds $M_0$.
Every collision triple has $0<a<b<U$, $0<|s|,|t|<Z$, $s\ne t$.
If $U\le1$ or $Z\le1$ no such triple exists, so assume both
exceed one. All the following enumeration ranges are now fixed under
the conditioning.

Fix an actual prime upper triple, the gap parameters, and $s,t$.
Eliminating $M$ from (13) gives (22). Each integer point
$(R_1,R_2,R_3)$ of this plane in $[1,Y]^3$ permits at most one
value of $M$, namely

$$
M=(P_2R_2-P_1R_1)/s.
\tag{27}
$$

If that value is nonpositive, nonintegral, or not an available product,
its probability is zero. Otherwise (7) bounds its conditional probability
by $M_0^{-1}2^{O(K\log(K+1))}$. Summing these probabilities is
valid even when different plane points determine the same $M$; only
linearity of expectation for their finitely many indicators is used.
We count all lower integer points, which includes the required distinct
lower prime points and may include additional inadmissible points.

The small-coefficient condition for (23) holds uniformly. Indeed,
$|s|,|t|,|s-t|<2Z$, and

$$
\log_2(Z/P_-)=-(1-\gamma)L^2+2\gamma K-\gamma.
\tag{28}
$$

By (12) this has a fixed negative quadratic leading term. Increasing
the deterministic $k_0$ ensures $2Z<P_-$ throughout the band.
Furthermore every upper prime exceeds every auxiliary prime in $N$,
so the required coprimality holds. We apply (23) only to prime upper
triples, then enlarge the parameter ranges when bounding their number.

There are at most $X$ choices for $P_1$ and at most $U^2$ gap
pairs. The sum needed for the second line contribution is

$$
\sum_{0<a<b<U}\frac{\gcd(a,b)}b\ll U(1+\ln U).
\tag{29}
$$

For each $b$, bound $\gcd(a,b)$ by
$\sum_{d\mid a,\ d\mid b}d$. Summing over $1\le a<b$ gives
at most $b\tau(b)$. Also

$$
\sum_{b\le U}\tau(b)
=\sum_{d\le U}\lfloor U/d\rfloor
\le U(1+\ln U),
$$

which proves (29). There are $O(Z^2)$ signed offset pairs. For each,
the reduced height satisfies $1\le h<2Z$. The sums over these
pairs of $1,h,1/h$ are therefore respectively
$O(Z^2)$, $O(Z^3)$, and $O(Z^2)$.

Summing every term of (23), using (27), gives

$$
\begin{aligned}
\mathbb E(T_{K,L}\mid q_{L+1},\ldots,q_K)
\le\frac{2^{O(K\log(K+1))}}{M_0}
\left\{
XU^2Z^2+XYUZ^3+\frac{XYU^2Z^3}{N}+U^2Y^2Z^2
\right\}.
\end{aligned}
\tag{30}
$$

In this order the terms arise from the constant, the $Yhg/b$ line
term, the $Yh/N$ line term, and the area term. For the last term use
$X/P_-=2^{2\gamma K-\gamma}$. The factor $1+\ln U$ in (29)
is $O(K^2)$ since $U\le X$, and is absorbed into the displayed
uniform error. The atom error is also uniform because $L<K$.

Using $N>2^{K^2-L^2}$ and $U=X/N$, the four terms in (30)
have the following exponent coefficients after division by $M_0$:

$$
\begin{array}{c|l}
XU^2Z^2/M_0&5\gamma-2+(2\gamma-1)\lambda\\
XYUZ^3/M_0&5\gamma-1+(4\gamma-3)\lambda\\
XYU^2Z^3/(M_0N)&6\gamma-3+(4\gamma-1)\lambda\\
U^2Y^2Z^2/M_0&4\gamma-2+(4\gamma-1)\lambda.
\end{array}
\tag{31}
$$

The first minus the fourth is $\gamma(1-2\lambda)<0$ on (12).
The third minus the fourth is $2\gamma-1<0$. Define

$$
D_\gamma(\lambda)=4\gamma-2+(4\gamma-1)\lambda,\qquad
H_\gamma(\lambda)=5\gamma-1+(4\gamma-3)\lambda.
$$

The bound is independent of the conditioned outcome. Averaging its finite
conditional expectations proves

$$
\mathbb E T_{K,L}\le2^{O(K\log(K+1))}
\left(2^{D_\gamma(\lambda)K^2}
+2^{H_\gamma(\lambda)K^2}\right)
\tag{32}
$$

uniformly throughout (12).

## Exponent balance and one infinite auxiliary realization

The fixed-modulus coefficient in (14) is
$F_\gamma(\lambda)=5\gamma-3+4\gamma\lambda$. Put

$$
\eta=3-20\gamma/3>0.
$$

For positivity, $\sqrt6<49/20$ follows by squaring, so
$\gamma<9/20$. The lower range $\lambda\le2/3$ satisfies

$$
F_\gamma(\lambda)\le F_\gamma(2/3)
=23\gamma/3-3=\gamma-\eta.
\tag{33}
$$

The error $O(K^2/\log K)$ in (14) is at most $\eta K^2/2$
for all sufficiently large $K$, with a threshold independent of $L$
and the outcome. Thus this entire range has a fixed exponential saving.

For $\lambda\ge2/3$, $H_\gamma$ is decreasing because
$4\gamma-3<0$, and

$$
H_\gamma(\lambda)\le H_\gamma(2/3)=\gamma-\eta.
\tag{34}
$$

Also $4\gamma-1>0$, so $D_\gamma$ is increasing. The upper
endpoint of (12) gives

$$
D_\gamma(\lambda)
\le D_\gamma\left(\frac\gamma{1-\gamma}\right)
=\frac{5\gamma-2}{1-\gamma}=\gamma,
\tag{35}
$$

where the last equality is $\gamma^2+4\gamma-2=0$.

Define $T_K=\sum_{k_0\le L<K}T_{K,L}$. Outside (12) the
summands vanish. Use (14) and (33) on the lower part, and (32),
(34), (35) on the upper part. There are at most $K$ summands.
Consequently there is one deterministic constant $C_4>0$ such that
for all sufficiently large $K$,

$$
\mathbb E T_K\le V_K:=
2^{\gamma K^2+C_4K\log_2(K+1)}.
\tag{36}
$$

Each $T_K$ is a finite-valued function of the first $K$ coordinates
of the product space, hence measurable. Markov's inequality gives

$$
\mathbb P(T_K>2^KV_K)\le2^{-K}.
$$

These probabilities are summable. The first Borel--Cantelli lemma implies
that almost every infinite auxiliary sequence satisfies
$T_K\le2^KV_K$ for every sufficiently large $K$. Explicitly, the
probability of any failure after index $J$ is at most the tail sum
$\sum_{K\ge J}2^{-K}$; letting $J\to\infty$ gives probability
zero for infinitely many failures. No independence of the events is used.

Fix one such outcome once and for all. There is a cutoff depending on
this outcome beyond which

$$
T_K\le2^{\gamma K^2+O(K\log(K+1))}.
\tag{37}
$$

This outcome-dependent cutoff is distinct from the earlier deterministic
$k_0$. We have selected one infinite basis; subsequent shells do not
change any already fixed auxiliary prime.

## Simultaneous selection using every full lower shell

A simple three-uniform hypergraph on $n$ vertices with $m$ edges
has an independent set of size

$$
\gg\frac{n}{\sqrt{1+m/n}}\quad(n>0).
\tag{38}
$$

If $m=0$, take every vertex. Otherwise retain each vertex independently
with probability $p=\min\{1,\sqrt{n/(3m)}\}$. The expected
number of retained vertices minus retained edges is $pn-p^3m$.
Some outcome attains at least its expectation, and deleting one vertex
from each of its remaining edges leaves at least that many vertices in
an independent set. If $m\le n/3$, the difference is at least
$2n/3$. If $m>n/3$, it equals
$2n\sqrt{n/(3m)}/3$. Both cases give (38) with one absolute
constant. This is a finite argument; an empty vertex set can be selected
as empty without invoking (38).

For each upper shell $K$, form a simple three-uniform hypergraph on
the full set $\mathcal P_K$. An upper three-set is an edge whenever
it occurs as the upper coordinates of a fiber triple with any full lower
shell $\mathcal P_L$, $k_0\le L<K$. This definition precedes all
shell selections and includes every lower prime in those shells. Repeated
upper three-sets count as one edge. The number $m_K$ of edges is at
most $T_K$.

By (6), (37), and (38), every sufficiently large shell has an
independent subset $\mathcal I_K$ with

$$
|\mathcal I_K|\ge2^{\gamma K^2-O(K\log(K+1))}.
\tag{39}
$$

For example, (6) gives
$n_K\ge2^{\gamma K^2-C_5\log(K+1)}$, while
$m_K/n_K\le2^{C_6K\log(K+1)}$ after enlarging a fixed constant;
substitution in (38) gives (39). Choose a maximum independent subset
in each finite shell, resolving ties lexicographically in increasing prime
order. This specifies all the choices for the fixed auxiliary sequence.
In the finitely many earlier shells choose the empty set. Define one set

$$
A=\{a_p:p\in\mathcal I_K\text{ for some }K\ge k_0\}.
\tag{40}
$$

Suppose an integer had three distinct unordered representations using
$A$. By (9), all three would use the same shell pair $(K,L)$.
Same-shell uniqueness excludes $K=L$, including diagonals. If $K>L$,
the representations determine three points of one fiber by (11), with
distinct upper and lower coordinates. The upper three-set is therefore
an edge of the shell-$K$ hypergraph and lies in $\mathcal I_K$,
contrary to independence. The edge definition used all lower shells
before selection, so choosing subsets in any other shell cannot create
a collision that this argument missed. Thus

$$
r_A(n)\le2\quad\text{for every integer }n.
\tag{41}
$$

## Every real cutoff and the original loss

For any sufficiently large real $x$, choose the unique $K$ such that
$B_K\le x<B_{K+1}$. Every label selected from shell $K$ is below
$B_K$ by (5), and injectivity and (39) give

$$
\log_2 A(x)\ge\gamma K^2-C_7K\log_2(K+1)
\tag{42}
$$

for a fixed $C_7$ and all sufficiently large such $K$. Put
$t=\log_2x$. By (2),

$$
K^2+2K<t\le(K+1)^2+3(K+1)=K^2+5K+4.
\tag{43}
$$

Equations (42)–(43) imply

$$
\log_2 A(x)\ge\gamma t-C_8\sqrt t\log_2 t
\tag{44}
$$

for all sufficiently large $x$: the change from $\gamma K^2$ to
$\gamma t$ costs at most $\gamma(5K+4)$, while $K<\sqrt t$
and $\log_2(K+1)=O(\log_2t)$. Converting to natural logarithms
and enlarging a fixed constant yields

$$
A(x)\ge x^\gamma
\exp\{-C\sqrt{\ln x}\,\ln\ln x\}
\quad(x\ge x_0)
\tag{45}
$$

for some $C>0$ and $x_0>e$. The selected shell sizes in (39) tend
to infinity, so $A$ is infinite. Dividing the logarithm of (45) by
$\ln x$ proves the limit inferior in L4, because
$\ln\ln x/\sqrt{\ln x}\to0$. For any fixed $\alpha<\gamma$,
eventually $C\ln\ln x/\sqrt{\ln x}\le\gamma-\alpha$, which
proves $A(x)\ge x^\alpha$ for this same $A$. This proves every
clause of the statement with real cutoffs.

## Source record and current verification

The external statements are used at the following exact interfaces:

- P. Erdős, *Beweis eines Satzes von Tschebyschef*,
  *Acta Litt. Sci. Szeged* 5 (1932), 194–198,
  [author-hosted PDF](https://users.renyi.hu/~p_erdos/1932-01.pdf),
  §5, printed pp. 197–198 (PDF pp. 4–5): for every integer $m\ge1$
  there is a prime $q$ with $m<q\le2m$. Apply this with
  $m=2^{2j-1}$ in (1). The upper endpoint is composite for these
  $m\ge2$, so allowing it does not change the prime set.
- Keith Conrad, *Cyclicity of (Z/(p))^×*, undated author exposition,
  [PDF](https://kconrad.math.uconn.edu/blurbs/grouptheory/cyclicmodp.pdf),
  Theorem 2.6, printed/PDF p. 3: the nonzero residue group modulo every
  prime is cyclic. Its order is $q-1$, giving the unique digit in any
  interval of $q-1$ consecutive exponent classes used in (4).
- D. Zagier, *Newman's Short Proof of the Prime Number Theorem*,
  *American Mathematical Monthly* 104(8) (1997), 705–708,
  [PDF](https://people.mpim-bonn.mpg.de/zagier/files/doi/10.2307/2975232/fulltext.pdf),
  the named Prime Number Theorem on printed p. 705 (PDF p. 2):
  $\pi(t)\sim t/\ln t$. This gives (6) and the auxiliary-prime
  count in (7). Both specializations are derived above.
- Rick Durrett, *Probability: Theory and Examples*, Version 5,
  11 January 2019, [PDF](https://sites.math.duke.edu/~rtd/PTE/PTE5_011119.pdf).
  Theorem 2.1.21, printed p. 53 (PDF p. 61), extends consistent finite
  laws on $\mathbb R^n$ to the countable real product. The specialization
  to the finite sets $\mathcal Q_j$ and its conditioning rule are
  justified above. Theorem 1.6.1(a), printed p. 29 (PDF p. 37), gives
  finite expectation linearity, used in (30), (36), and (38).
  Theorem 1.6.4 on the same page, with its naming remark on printed p. 30
  (PDF p. 38), gives the Markov bound for $T\ge0$ and $a>0$,
  $\mathbb P(T\ge a)\le\mathbb ET/a$. This is the specialization
  $\phi(t)=\max(t,0)$ and the target set $[a,\infty)$ of the
  source's general inequality, called Chebyshev there. Theorem 2.3.1,
  printed p. 68 (PDF p. 76), says summable event probabilities give
  probability zero to infinitely many occurrences, with no independence
  hypothesis. It applies to the bad events following (36).

A bounded source check accessed these exact PDFs on 2026-09-09 UTC and
visually checked all the named theorem statements. The three number-theory
proofs were not audited. For Durrett, the limsup-event definitions on
printed p. 67 (PDF p. 75) were also viewed; the short Markov and
Borel--Cantelli proofs were read, while the extension theorem's proof in
Appendix A.3 was not read. The claimed external reading depth is claims
checked, with those limited additional proof readings. This identifies
external premises without claiming a complete local proof of their sources.

For method attribution, Javier Cilleruelo's
[*Infinite Sidon sequences*](../../../../library/additive_bases/cilleruelo_2014_infinite_sidon_sequences/_index.md)
is used in its selected local version, arXiv:1209.0326v2,
15 May 2013. The shifted digits are in §2.1, p. 4; the counting
and shell-recovery arguments are Propositions 1–2, pp. 4–6. Section 3.1,
p. 9, chooses auxiliary primes independently and gives the product
probability estimate of shape $2^{-k^2+O(k\log k)}$. Its prime
intervals are $(2^{2j-1},2^{2j+1}]$, distinct from (1). The digital
construction and random-product mechanism are prior methods, but the
applications needed here, including (7), are proved directly. No density
conclusion of that source supplies L4.

The canonical source digest records its earlier visual reading of
pp. 1–6 for the digital-method locators. The current bounded source check
read pp. 7–10 as extracted text and viewed pp. 1 and 9 visually, confirming
the version and randomization attribution. Neither reading record claims
whole-paper proof acceptance.

This is an author-recorded proof at tier 0. Its symbolic deductions do
not require a mathematical computation or numerical certificate. The
construction gives existence of the favorable auxiliary sequence; no
algorithm for finding it is asserted. Native Lean coverage and independent
whole-claim acceptance are not asserted.

The proof reproduces all needed local arguments rather than relying on
the truth of [L2](../L2_two_representation_exponent/_index.md), whose
related exponent-$3/7$ proof also has tier 0 standing. Its proof sections
"The label set and its digits" and "Recovering the shells and the
congruence fibers" parallel (3)–(13) here; its "A uniform count of
triples in the fibers" contains the related elimination and factorization;
its "Choosing one set through all shells" contains the finite alteration
and cutoff mechanism. All those deductions are rederived above. In
particular, the four size inequalities (17) and the fixed-modulus count
(14) are proved only on $\lambda\le2/3$ at the new $\gamma$.
L2's exponent-$3/7$ range estimates and final theorem are not applied to
the larger collision band (12).

The fixed auxiliary intervals (1), deterministic shells (3), and loss (45)
specify this claim. No optimized-schedule bound is asserted. Independent
acceptance requires scrutiny of these exact mathematical pages and their
external interfaces; no such acceptance is recorded here.

The reported bounded literature checking had partial
API coverage and outstanding MathSciNet review. It did not include a refreshed
Pascadi forward-citation sweep or a separate quantitative-refinement sweep.
Those limitations remain outstanding. No fresh literature census or current
priority verdict is supplied here.
