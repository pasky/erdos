---
name: research/leads/balanced_auxiliary_prime_density/loss_refinement
title: Balanced auxiliary primes in the two-representation construction
desc: |
  The full balanced-schedule proof, with its exact reviewed subject and
  qualified independent review and distinct contract-grade records.
created: 2026-09-15T05:31:30Z
updated: 2026-09-15T05:31:30Z
---

***

## Statement and standing

Put $\gamma=\sqrt6-2$. There exist one infinite set
$A\subseteq\mathbb Z_{>0}$ and constants $C>0$ and $x_0>e$ such that

$$
r_A(n):=|\{(a,b)\in A^2:a\le b,\ a+b=n\}|\le2
\quad(n\in\mathbb Z),
$$

and, for every real $x\ge x_0$,

$$
A(x):=|A\cap[1,x]|
\ge x^\gamma\exp\{-C\sqrt{\ln x\,\ln\ln x}\}.
\tag{1}
$$

A diagonal representation is counted once. The original author-recorded
argument received an independent whole-argument
[refutation-failed review](evidence/verify/loss_refinement_review.md), followed
by a [PASS from a distinct contract grader](evidence/verify/loss_refinement_grade.md).
These records concern the exact
[reviewed subject](evidence/assets/loss_refinement_reviewed.txt).

This native text is an author-prepared retention of that proof. The review
and grade do not allocate a claim identity, confer a numerical tier, or
assert native formal verification. Their source-reading and
historical-attribution limits remain in force. In particular, the reviewer
did not authenticate the author's Cilleruelo attribution, L2 standing, or
historical reading assertions.

The result improves the explicit loss in the
[L4 statement](../../../theory/additive_bases/L4_random_modulus_exponent/_index.md),
whose loss is $\exp\{-C\sqrt{\ln x}\ln\ln x\}$. It does not
improve the exponent $\gamma$, assert a current public record or priority,
or resolve the square-root lower-density question in
[Erdős Problem 158](../../../problems/additive_bases/E0158/_index.md).
L4's statement, proof and historical standing are not amended here.

The construction follows the shifted discrete-logarithm method of
Cilleruelo, *Infinite Sidon sequences*, arXiv:1209.0326v2, 15 May 2013,
and the capacity-two collision-plane argument recorded in native L4.
The changed ingredient is the growth of the auxiliary-prime sizes. The
essential arithmetic and selection deductions are supplied below; the L4
density theorem is not being applied to a schedule outside its statement.

All unspecified logarithms in the proof have base two. Natural logarithms
appear as $\ln$. Implied constants are independent of the lower shell,
the auxiliary-prime outcome, and the eventual real cutoff. They may depend
on the fixed number $\gamma$.

## Auxiliary primes and deterministic scales

For $j\ge1$ define

$$
w_j=\lceil j\log_2(j+1)\rceil,\qquad
S_k=\sum_{j=1}^k w_j,\qquad S_0=0,\qquad
R_k=k\log_2(k+1).
$$

The integers $w_j$ strictly increase. For example, the real function
$t\log_2(t+1)$ increases by more than one when an integer $t\ge1$
is increased by one. Its ceiling therefore increases by at least one.
Let $q_j$ be independent and uniform over the finite set of primes

$$
\mathcal Q_j=\{q:2^{w_j}<q\le2^{w_j+1}\}.
\tag{2}
$$

Bertrand's postulate makes every such set nonempty. The intervals in (2)
are disjoint even when successive exponents differ by one, so all selected
primes are distinct. Define

$$
Q_k=\prod_{j\le k}q_j,\qquad b_j=4q_j,\qquad
B_k=\prod_{j\le k}b_j=4^kQ_k,
\qquad Q_0=B_0=1.
$$

For every outcome,

$$
2^{S_k}<Q_k\le2^{S_k+k},\qquad
2^{S_k+2k}<B_k\le2^{S_k+3k}.
\tag{3}
$$

The following growth estimates will control every error term:

$$
S_k\asymp k^2\log_2(k+1),\quad
w_k=O(R_k),\quad R_k=o(S_k),\quad
R_k=O\bigl(\sqrt{S_k\log_2(S_k+2)}\bigr).
\tag{4}
$$

For the first estimate, the upper bound follows by replacing every $j$ by
$k$ in the summands. The last $\lfloor k/2\rfloor$ summands give the
lower bound, since each is at least
$(k/2)\log_2(k/2+1)$. The remaining assertions follow directly; in
particular $R_k^2\ll S_k\log_2(S_k+2)$.

The prime number theorem, specialized to $(2^w,2^{w+1}]$, gives
$|\mathcal Q_j|\gg 2^{w_j}/(w_j+1)$, uniformly after enlarging a
constant to include the finitely many small $j$. Unique factorization and
the disjoint intervals recover the entire tuple from its product.
Consequently, for every integer $m$,

$$
\mathbb P(Q_L=m)
\le2^{-S_L}\prod_{j\le L}C(w_j+1)
\le2^{-S_L+O(R_L)}.
\tag{5}
$$

The last bound uses
$\sum_{j\le L}\log_2(C(w_j+1))=O(L\log_2(L+1))$.
It holds with the same constant after conditioning on any prescribed
values of $q_{L+1},\ldots,q_K$: these coordinates are independent of
the first $L$. A countable product of the finite probability spaces
provides one probability space for all $j$; only finite cylinder
conditioning is used below.

## Source shells and digital properties

Choose one deterministic $k_0$ sufficiently large for all eventual
uniform comparisons below, and in particular for
$\gamma S_{k-1}>w_k+1$ whenever $k\ge k_0$. Define disjoint source
shells and their upper endpoints by

$$
\mathcal P_k=\{p\text{ prime}:2^{\gamma S_{k-1}}<p
\le2^{\gamma S_k}\},\qquad X_k=2^{\gamma S_k}.
\tag{6}
$$

Each such source prime exceeds every $q_j$ with $j\le k$.
The prime number theorem gives

$$
n_k:=|\mathcal P_k|\sim X_k/\ln X_k,
\qquad \log_2n_k=\gamma S_k-O(\log_2(S_k+2)).
\tag{7}
$$

Indeed, the discarded lower interval has at most $X_{k-1}$ integers,
and
$X_{k-1}\ln X_k/X_k=\gamma S_k\ln2\,2^{-\gamma w_k}\to0$.
Thus no short-interval prime theorem is needed. The shells are nonempty
eventually.

Fix a primitive root $g_j$ modulo each selected prime $q_j$. For
$p\in\mathcal P_k$, let $x_j(p)$, for $j\le k$, be the unique
integer in $[q_j+1,2q_j-1]$ with
$g_j^{x_j(p)}\equiv p\pmod{q_j}$, and put $x_j(p)=0$ for $j>k$.
Set

$$
a_p=\sum_{j=1}^k x_j(p)B_{j-1}.
\tag{8}
$$

Cyclicity of the nonzero prime-field residues supplies the digit, since
the interval contains exactly $q_j-1$ consecutive exponent classes.
Mixed-radix uniqueness follows by reduction modulo the first radix,
subtraction, division, and induction. It gives
$1\le a_p<B_k$. The last nonzero digit identifies the shell. Inside
one shell, equal labels imply $Q_k\mid p-p'$, and
$p,p'\le X_k<Q_k$, proving that $p\mapsto a_p$ is injective.

Every sum of two labels has no carries. If its shell indices are $K\ge L$,
its digits lie in the disjoint ranges

$$
\begin{array}{c|c}
j\le L &[2q_j+2,4q_j-2]\\
L<j\le K &[q_j+1,2q_j-1]\\
j>K &\{0\}.
\end{array}
\tag{9}
$$

Thus every representation of a given integer uses the same unordered
shell pair. For a same-shell equality, exponentiating each digit gives
equality of prime products modulo $Q_K$. Both products are at most
$X_K^2<Q_K$ because $2\gamma<1$. They are equal as integers, so
unique factorization identifies the unordered pair, including diagonals.

For unequal shells $K>L$ write

$$
M=Q_L,\quad N=Q_K/Q_L,\quad X=2^{\gamma S_K},\quad
Y=2^{\gamma S_L},\quad \lambda=S_L/S_K.
$$

Equal sums imply equality under the map

$$
\Phi_{K,L}(P,R)=(P\bmod N,PR\bmod M),
\qquad(P,R)\in\mathcal P_K\times\mathcal P_L.
\tag{10}
$$

The upper digits give the first congruence; the lower digits give the
second. The converse is not asserted. Both projections within a fiber
are injective: fix one coordinate, cancel it modulo $M$, and use
$Y<M$; or combine congruences modulo $M$ and $N$ and use $X<MN$.
Cancellations are valid because the source primes exceed all auxiliary
prime factors concerned.

Two distinct points of a fiber have a nonzero upper difference divisible
by $N$ and a nonzero product difference divisible by $M$. The latter
products differ by unique factorization and disjointness of source shells.
Together with (3), these facts force

$$
1-\gamma<\lambda<\frac{\gamma}{1-\gamma}.
\tag{11}
$$

Let $T_{K,L}$ count three-element subsets of a fiber, summed over all
fibers. It vanishes outside (11). Order a triple's upper coordinates as
$P_1<P_2<P_3$, and call their corresponding distinct lower coordinates
$R_1,R_2,R_3$. There are unique integers $a,b,s,t$ with

$$
P_2-P_1=Na,\quad P_3-P_1=Nb,\quad
P_2R_2-P_1R_1=Ms,\quad P_3R_3-P_1R_1=Mt.
\tag{12}
$$

Here $a,b$ are positive with $a<b$, and $s,t$ are nonzero and distinct.
Both signs of $s,t$ must be counted.

## Fixed-modulus estimate in the lower part of the band

For this section put

$$
U=X/N,\qquad Z=XY/M,\qquad W=2XY^2/(MN).
$$

Then $0<a<b<U$ and $0<|s|,|t|<Z$. Elimination in (12) gives

$$
\begin{aligned}
aR_2(R_3-R_1)-bR_3(R_2-R_1)&=dM,\\
s(R_3-R_1)-t(R_2-R_1)&=dN
\end{aligned}
\tag{13}
$$

for an integer $d$ with $|d|<W$; coprimality of $M,N$ justifies
the integer $d$. When $\lambda\le2/3$, all of

$$
U<R_i,\qquad U<P_i,\qquad 2XY<P_2P_3,\qquad WU^3<M
\tag{14}
$$

hold uniformly for sufficiently large $K$. The logarithms of the four
ratios to be made less than one are bounded above, respectively, by

$$
\begin{aligned}
&-(1-\gamma)(S_K-S_L)+\gamma w_L,\\
&-(S_K-S_L)+\gamma w_K,\\
&1-\gamma(S_K-S_L)+2\gamma w_K,\\
&1+(4\gamma-4)S_K+(2\gamma+2)S_L.
\end{aligned}
\tag{15}
$$

The first three have fixed negative multiples of $S_K$ plus
$O(R_K)=o(S_K)$. The fourth is at most
$1+(16\gamma-8)S_K/3$, with negative coefficient. If $d=0$,
the first equation in (13), reduced modulo $R_2$, would imply
$R_2\mid b$, contradicting (14). Thus $0<|d|<W$.

Fix $a,b,s,t,d$ and let $\Delta=at-bs$. If $\Delta\ne0$, put
$\rho=R_2-R_3$ and $\sigma=atR_2-bsR_3$. Direct elimination and
completion of a product give

$$
\begin{aligned}
&(\Delta\rho-dN(b-a))(\Delta\sigma-dNab(s-t))\\
&\hspace{1cm}=d(s-t)\{\Delta^2M+dN^2ab(b-a)\}=:F.
\end{aligned}
\tag{16}
$$

For clarity, (13) first yields
$\rho\sigma=d\{M(s-t)-NaR_2+NbR_3\}$; substitute
$R_2=(\sigma-bs\rho)/\Delta$ and
$R_3=(\sigma-at\rho)/\Delta$ and complete the two factors.
The integer $F$ is nonzero: otherwise the braces vanish, whence
$M\mid dab(b-a)$, contrary to
$0<|dab(b-a)|<WU^3<M$.

Every factor in $F$ has absolute value at most $2^{C S_K}$ for a
fixed constant. The elementary uniform divisor bound

$$
\max_{1\le n\le2^{C S_K}}2\tau(n)
\le2^{O(S_K/\log_2(S_K+2))}
\tag{17}
$$

bounds its ordered signed factor pairs. To obtain (17), set
$u=\ln H$ for $H=2^{C S_K}$. In the prime factorization of
$n\le H$, primes at most $\sqrt u$ contribute at most
$\sqrt u\ln(1+u/\ln2)$ to $\ln\tau(n)$. For larger primes,
the sum of exponents is at most $2u/\ln u$, and
$\ln(e+1)\le e\ln2$. Both contributions are $O(u/\ln u)$.

Each factor pair in (16) determines $\rho,\sigma$, then $R_2,R_3$,
then $R_1$ by the second equation of (13), and finally $P_1,P_2,P_3$
by (12). Every division has a nonzero denominator. Invalid reconstructions
can be discarded.

If $\Delta=0$, write $a=ea'$, $b=eb'$ with
$e=\gcd(a,b)$ and $\gcd(a',b')=1$. Then $s=fa'$, $t=fb'$
for a nonzero integer $f$. Set $C_0=fM-NeR_1$. Equations (12) give

$$
a'C_0=P_2(R_2-R_1),\qquad b'C_0=P_3(R_3-R_1).
$$

By (14), $a'<P_2$ and $b'<P_3$, so the distinct primes $P_2,P_3$
both divide $C_0$. But $|C_0|<2XY<P_2P_3$, forcing $C_0=0$
and hence $R_2=R_1$, a contradiction.

A triple forces $U,Z,W>1$. There are at most $U^2$, $4Z^2$, and
$2W$ possibilities for the gap pair, signed offset pair, and $d$.
Combining these with (17) proves, uniformly when $\lambda\le2/3$,

$$
T_{K,L}\le
2^{[5\gamma-3+4\gamma\lambda]S_K+
O(S_K/\log_2(S_K+2))}.
\tag{18}
$$

The inequality also holds when there are no triples. Its main exponent
comes from $U^2Z^2W=2X^5Y^4/(MN)^3$ and $MN>2^{S_K}$.

## Integer points on a collision plane

We need a lattice estimate with its line term retained. If
$c\in\mathbb Z^3$ is primitive and nonzero, the lattice
$\Lambda=\{v\in\mathbb Z^3:c\cdot v=0\}$ has rank two and
covolume $D=\|c\|_2$. If $\ell$ is its shortest nonzero vector
length, then

$$
|\Lambda\cap[-Y,Y]^3|\ll1+Y/\ell+Y^2/D.
\tag{19}
$$

Here is an elementary justification. If $c_1=c_2=0$, then
$c_3=\pm1$ and the assertion about rank and covolume is immediate.
Otherwise let $d_0=\gcd(c_1,c_2)>0$, choose
$c_1u+c_2v=d_0$, and choose $d_0a+c_3b=1$. The vectors

$$
(c_2/d_0,-c_1/d_0,0),\quad (uc_3,vc_3,-d_0),\quad(ua,va,b)
$$

have determinant one, and the first two have cross product $c$.
They give the stated lattice basis and covolume. A shortest vector has
coprime coordinates in any lattice basis, and thus extends to a basis.
Reduce the other basis vector modulo it until the parallel component has
absolute value at most $\ell/2$. Its perpendicular height $h_0$
then satisfies $h_0\ge\sqrt3\ell/2$ and $D=\ell h_0$.
Counting lattice lines in a ball of radius $\sqrt3Y$, and points per
line, gives $O((1+Y/h_0)(1+Y/\ell))$, which is (19).

For fixed upper primes and offsets in (12), elimination of $M$ gives

$$
(t-s)P_1R_1-tP_2R_2+sP_3R_3=0.
\tag{20}
$$

Let $g=\gcd(a,b)$ and let
$h=\max(|s|,|t|,|s-t|)/\gcd(|s|,|t|)$. Put
$P_-=2^{\gamma S_{K-1}}$. If
$\max(|s|,|t|,|s-t|)<\min_iP_i$, the number of integer points
of (20) in $[1,Y]^3$ is at most

$$
\ll 1+Yh\left(\frac1N+\frac gb\right)
       +\frac{Y^2}{P_-h}.
\tag{21}
$$

To prove this, first divide $s,t$ by their positive greatest common
divisor. The normal vector
$((t-s)P_1,-tP_2,sP_3)$ is primitive: a common prime different from
all $P_i$ would divide both reduced offsets, and a prime equal to one
of the $P_i$ cannot divide the two other, nonzero, smaller coefficients.
Its norm is at least $P_-h$.

For a vector $v$ in its kernel, use $P_2=P_1+Na$, $P_3=P_1+Nb$
to write the equation as

$$
P_1\{(t-s)v_1-tv_2+sv_3\}
 +N\{-ta v_2+sb v_3\}=0.
$$

If $\|v\|_\infty<N/(3h)$, coprimality of $P_1,N$ forces both
braces to vanish. The vector $((t-s)v_1,-tv_2,sv_3)$ is then a
nonzero integer multiple of $((b-a)/g,-b/g,a/g)$ unless $v=0$.
Thus every nonzero kernel vector has norm at least
$\min\{N/(3h),b/(gh)\}$. Substitute this and the determinant
bound into (19) to obtain (21).

## Averaging over the lower modulus

Fix $K,L$ in (11), and condition on $q_{L+1},\ldots,q_K$, fixing
$N$. In this section use the deterministic bounds

$$
M_0=2^{S_L},\qquad U=X/N,\qquad Z=XY/M_0.
\tag{22}
$$

Every actual triple has $0<a<b<U$ and $0<|s|,|t|<Z$, with
$s\ne t$. These ranges are fixed under the conditioning. If $U\le1$
or $Z\le1$ there is no triple. For any fixed actual upper-prime triple,
offset pair, and lower integer point in (20), the only possible value of
$M$ is

$$
M=(P_2R_2-P_1R_1)/s.
$$

If it is not an allowed positive integer product, its probability is zero.
Otherwise (5) bounds its conditional probability by
$M_0^{-1}2^{O(R_K)}$. Summing the point indicators is legitimate even
when different points yield the same product $M$.

The small-coefficient hypothesis of (21) is uniform throughout (11),
because the offsets and their difference have magnitude less than $2Z$,
and

$$
\log_2(Z/P_-)=-(1-\gamma)S_L+\gamma w_K.
\tag{23}
$$

The right side is at most a fixed negative multiple of $S_K$ plus
$O(R_K)$, by (11) and (4). Therefore $2Z<P_-$ once the deterministic
threshold is large enough.

There are at most $X$ first upper primes and at most $U^2$ gap pairs.
We use

$$
\sum_{0<a<b<U}\frac{\gcd(a,b)}b\ll U(1+\ln U).
\tag{24}
$$

Indeed, $\gcd(a,b)\le\sum_{d\mid a,\ d\mid b}d$, so summing in
$a$ gives at most $b\tau(b)$, and
$\sum_{b\le U}\tau(b)\le U(1+\ln U)$.
Over the $O(Z^2)$ signed offset pairs, the sums of $1,h,1/h$ are
at most $O(Z^2),O(Z^3),O(Z^2)$, respectively. The latter intentionally
uses only $h\ge1$; a sharper noncritical estimate is unnecessary.

Summing (21), using (5), (24), and
$X/P_-=2^{\gamma w_K}$, gives

$$
\mathbb E(T_{K,L}\mid q_{L+1},\ldots,q_K)
\le\frac{2^{O(R_K)}}{M_0}
\left\{XU^2Z^2+XYUZ^3+\frac{XYU^2Z^3}{N}
                      +U^2Y^2Z^2\right\}.
\tag{25}
$$

Both $1+\ln U=O(S_K)$ and the source endpoint factor
$2^{\gamma w_K}$ are absorbed into the error $2^{O(R_K)}$.
The four main exponent coefficients, in units of $S_K$, are

$$
\begin{array}{c|l}
1&5\gamma-2+(2\gamma-1)\lambda\\
2&5\gamma-1+(4\gamma-3)\lambda\\
3&6\gamma-3+(4\gamma-1)\lambda\\
4&4\gamma-2+(4\gamma-1)\lambda.
\end{array}
\tag{26}
$$

The first minus the fourth is $\gamma(1-2\lambda)<0$, since
$(11)$ has $\lambda>1-\gamma>1/2$. The third minus the fourth
is $2\gamma-1<0$. Define

$$
D_\gamma(\lambda)=4\gamma-2+(4\gamma-1)\lambda,
\qquad
H_\gamma(\lambda)=5\gamma-1+(4\gamma-3)\lambda.
$$

The bound (25) is uniform in the conditioned outcome. Averaging its
finite conditional expectations proves

$$
\mathbb E T_{K,L}\le2^{O(R_K)}
\left(2^{D_\gamma(\lambda)S_K}
     +2^{H_\gamma(\lambda)S_K}\right).
\tag{27}
$$

## Critical exponent, summability, and simultaneous selection

Put $\eta=3-20\gamma/3>0$. For the sign, $\gamma<9/20$ follows
from $\sqrt6<49/20$, whose square is an exact strict comparison.
On $\lambda\le2/3$, the coefficient in (18) is at most

$$
5\gamma-3+8\gamma/3=\gamma-\eta.
$$

Its divisor error is $o(S_K)$, uniformly in $L$, so this whole range
has an eventual fixed exponential saving, for instance
$T_{K,L}\le2^{(\gamma-\eta/2)S_K}$.

On $\lambda\ge2/3$, the function $H_\gamma$ decreases and is
at most $H_\gamma(2/3)=\gamma-\eta$. The function $D_\gamma$
increases, and throughout the strict band (11) it satisfies

$$
D_\gamma(\lambda)
\le D_\gamma\!\left(\frac\gamma{1-\gamma}\right)
=\frac{5\gamma-2}{1-\gamma}=\gamma.
\tag{28}
$$

The last equality uses $\gamma^2+4\gamma-2=0$. No favorable spacing
between $S_L/S_K$ and the boundary is assumed. In particular (28) covers
shell pairs arbitrarily close to the critical boundary, with the same
constant in the error of (27).

Write $T_K=\sum_{k_0\le L<K}T_{K,L}$. There are fewer than $K$
terms, so (18) and (27) give one deterministic constant $C_1$ such that

$$
\mathbb E T_K\le2^{\gamma S_K+C_1R_K}
\tag{29}
$$

for all sufficiently large $K$. Markov's inequality implies

$$
\mathbb P\left(T_K>2^{\gamma S_K+C_1R_K+K}\right)\le2^{-K}.
$$

The probabilities are summable. The first Borel--Cantelli lemma, or just
the union bound on all failures after $J$ followed by $J\to\infty$,
shows that almost every infinite auxiliary-prime sequence has only
finitely many exceptions. Fix one such sequence. Since $K\le R_K$,

$$
T_K\le2^{\gamma S_K+O(R_K)}
\tag{30}
$$

holds for all sufficiently large $K$ in this one sequence. The threshold
here may depend on the chosen outcome; the constants preceding the
probabilistic choice do not. No event independence is needed in this step.

For each $K$, form a simple three-uniform hypergraph on the full shell
$\mathcal P_K$. An upper three-set is an edge if it occurs in a fiber
triple with any full lower shell $\mathcal P_L$, $k_0\le L<K$.
Its edge count $m_K$ satisfies $m_K\le T_K$. This definition is made
before choosing any shell subsets.

A three-uniform hypergraph on $n>0$ vertices with $m$ edges has an
independent subset of size

$$
\gg n/\sqrt{1+m/n}.
\tag{31}
$$

If $m=0$, retain everything. Otherwise retain each vertex with
probability $p=\min\{1,\sqrt{n/(3m)}\}$. Expected retained vertices
minus retained edges equal $pn-p^3m$. Delete one vertex from every
remaining edge in an outcome attaining at least that expectation. If
$m\le n/3$ the difference is at least $2n/3$; otherwise it is
$2n\sqrt{n/(3m)}/3$. This proves (31).

Equations (7), (30), and (31) supply independent subsets $I_K$ with

$$
|I_K|\ge2^{\gamma S_K-C_2R_K}
\tag{32}
$$

for all sufficiently large $K$, with one constant $C_2$ for the fixed
outcome. Choose, for example, the lexicographically first maximum
independent subset of each finite shell. Choose the empty subset in the
finitely many exceptional earlier shells, and put

$$
A=\{a_p:p\in I_K\text{ for some }K\}.
\tag{33}
$$

This specifies one set. If an integer had three distinct unordered
representations using it, (9) would identify a common shell pair. The
same-shell uniqueness already proved excludes that case, including every
diagonal. Otherwise (10) puts the representations in one fiber with three
distinct upper primes. Those primes form an edge inside $I_K$, a
contradiction. Using full lower shells in the edge definition makes all
choices simultaneous; later shell choices introduce no missed obstruction.
Hence $r_A(n)\le2$ for every integer $n$.

## Every real cutoff and the sharper loss

For sufficiently large real $x$, let $K$ be the unique index with
$B_K\le x<B_{K+1}$ and put $t=\log_2x$. Every selected label from
shell $K$ lies below $B_K$, so injectivity and (32) give

$$
\log_2 A(x)\ge\gamma S_K-C_2R_K.
\tag{34}
$$

Both sides of the physical cutoff comparison are explicit:

$$
S_K+2K<t<S_{K+1}+3(K+1)
=S_K+w_{K+1}+3K+3.
\tag{35}
$$

In particular $t-S_K=O(R_{K+1})=O(R_K)$, and (4) gives
$R_K\ll\sqrt{t\log_2(t+2)}$. Combining (34) and (35), then
enlarging the constant for all sufficiently large $t$, yields

$$
\log_2 A(x)\ge\gamma t-C_3\sqrt{t\log_2 t}.
$$

Conversion to natural logarithms gives (1). The selected shell sizes in
(32) tend to infinity because $R_K=o(S_K)$, so $A$ is infinite.
The argument is uniform over every real cutoff, not just the shell
endpoints. Since the loss is $o(\ln x)$, this same set also satisfies
$A(x)\ge x^\alpha$ eventually for each fixed $\alpha<\gamma$.

## External inputs and reading boundary

The standard external inputs are Bertrand's postulate in the form
``every integer m>=1 has a prime m<q<=2m'', cyclicity of the nonzero
residue group of a prime field, the prime number theorem
$\pi(x)\sim x/\ln x$, and the countable product of finite probability
spaces. Markov and the summable-event argument are used explicitly above.
The precise standard-source locators used in L4 are: Erdős (1932),
*Beweis eines Satzes von Tschebyschef*, §5, printed pp. 197-198;
Conrad, *Cyclicity of (Z/(p))^×*, Theorem 2.6, p. 3;
Zagier (1997), *Newman's Short Proof of the Prime Number Theorem*,
printed p. 705; and Durrett, *Probability: Theory and Examples*,
version 5 dated 11 January 2019, Theorems 2.1.21, 1.6.4, and 2.3.1.
Their theorem interfaces are consumed as standard external results. This
note does not claim a fresh visual or whole-proof audit of those sources.

The original author reported reading the full native L4 and L2 statements
and proofs, whose recorded standing at that reading was tier 0. The author
also reported visually reading the selected Cilleruelo manuscript on
pp. 1, 2, and 9 for its representation convention, Theorem 1.2, and
independent auxiliary-prime/product-probability mechanism. Its density
theorem is background, not a premise of (1). These are retained historical
author assertions, not reading claims made by the independent reviewer or
by this filing operation. The
[canonical source index](../../../../library/additive_bases/cilleruelo_2014_infinite_sidon_sequences/_index.md)
identifies the selected arXiv:1209.0326v2 manuscript, dated 15 May 2013.

No computation, formal verification, or public novelty conclusion is
claimed by this argument. Subsequent independent review is recorded
separately above, with its exact external-source interfaces, artifact
identities, actual reading depth, and distinct grader's scope.
