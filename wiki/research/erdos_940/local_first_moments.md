---
name: research/erdos_940/local_first_moments
title: Local information and representation first moments
desc: Residue surjectivity and a uniform positive progression first moment for exponents at least five.
tags: []
sources: []
created: 2026-09-22T02:24:55Z
updated: 2026-10-14T00:26:52Z
---


# Local information and representation first moments

***

## Status

The lemmas and theorem in this note are proved. They describe limitations of
local first-moment arguments, not solutions of the density or infinitude
questions.

## Every residue contains two powerful summands

For every $r\ge1$, every modulus $M\ge1$, and every residue $a\pmod M$, there
are infinitely many sums of exactly two positive $r$-powerful integers in that
residue.

For each prime power $p^k\parallel M$, write $a=b_p+c_p$, with each summand
either a unit or zero modulo $p^k$. For $p\ge3$, choose $b_p\bmod p$ outside
$\{0,a\}$, so both summands are units. At $p=2$, use two odd summands when $a$
is even, and (0+a) when $a$ is odd. CRT gives positive representatives $b,c$.
Choose $E\ge r$ with $E\equiv1\pmod{\varphi(M)}$. Then


$$
b^E+c^E\equiv a\pmod M.
$$


Both summands are $r$-powerful. Replacing $b$ by $b+tM$ yields infinitely many
distinct values. The case $M=1$ is immediate.

For $r\ge3$, the two-summand set nevertheless has density zero, by the bound
$O_r(X^{2/r})$ for its candidate tuples. Thus surjectivity modulo every integer
is far weaker than positive density.

## Large good primes cannot produce arbitrary savings when $r\ge5$

For $F(\mathbf x)=\sum_{i=1}^r d_i x_i^r$, define


$$
\rho_{p^k}(a;F)=p^{-k(r-1)}\#\{\mathbf x\bmod p^k:F(\mathbf x)\equiv a\pmod{p^k}\}.
$$


If $p\nmid r\prod_i d_i$, then, uniformly in $a,k$,


$$
\rho_{p^k}(a;F)\ge
1-(r-1)^r p^{1-r/2}-p^{1-r}.
\tag{1}
$$


For $h\ne0\pmod p$, expansion into multiplicative characters gives


$$
\left|\sum_{x\bmod p}e_p(hd_i x^r)\right|\le(r-1)\sqrt p.
$$


Additive orthogonality therefore bounds the deviation of the number of solutions
modulo $p$ from $p^{r-1}$ by $(r-1)^r p^{r/2}$. The only possibly singular
solution is the zero vector. Remove it, and lift each nonsingular solution to
exactly $p^{(k-1)(r-1)}$ solutions modulo $p^k$. This proves (1).

When $r\ge5$, the errors in (1) are summable over primes. For sufficiently large
$P$, products of these lower bounds over any set of primes greater than $P$ are
bounded below by a positive constant tending to (1) as $P\to\infty$. Allowing
high prime powers or highly divisible targets does not alter this conclusion.

### Nonzero good-prime targets: a sharper bound

The distinction in Section 4 of the
[independent record](independent/canonical_decomposition_and_quartic_zero_target.md)
is also valid: for unit coefficients and $a\not\equiv0\pmod p$,

$$
|\rho_p(a;F)-1|\le(r-1)^r p^{-(r-1)/2}.
\tag{1a}
$$

Indeed, put $g=\gcd(r,p-1)$. Each nonzero-frequency power sum expands into
$g-1$ Gauss sums of absolute value $\sqrt p$. Expanding the product over
the $r$ coordinates leaves at most $(g-1)^r$ terms. The remaining frequency
sum is a multiplicative Gauss sum twisted by the nonzero target: its
absolute value is $\sqrt p$ for a nonprincipal character and $1$ for the
principal character. Division by the orthogonality factor $p$ and by the
normalizing factor $p^{r-1}$ proves (1a). At target zero that frequency sum
can instead have magnitude $p-1$, giving the weaker bound used in (1).

If also $p\nmid r$, every solution at a nonzero target is nonsingular, so
$\rho_{p^k}(a;F)=\rho_p(a;F)$ whenever $p\nmid a$. Thus for a fixed form,
using only sufficiently large good primes with nonzero targets cannot make
the product arbitrarily small already for $r\ge4$. The successful quartic
proof uses targets $p\pmod{p^2}$, which are **zero modulo $p$**, and is not
subject to this sharper summability obstruction.

## Uniform lower bound for all progression first moments, $r\ge5$

Let


$$
R_r(X;a,M)=\#\{(n_1,\ldots,n_r)\in\mathcal P_r^r:
\textstyle\sum_i n_i\le X,\ \sum_i n_i\equiv a\pmod M\}.
$$


**Theorem.** For every $r\ge5$, there is $c_r>0$, independent of $a,M$, such
that


$$
\liminf_{X\to\infty}\frac{M}{X}R_r(X;a,M)\ge c_r.
\tag{2}
$$


The limit here is taken for each fixed $a,M$.

### A finite family handles all small-prime targets

Choose $B\ge r$ so large that, for every prime $p>B$, both


$$
\gamma_p=1-(r-1)^r p^{1-r/2}-p^{1-r},\qquad
\gamma'_p=1-(r-1)^{r-1}p^{(3-r)/2}-p^{2-r}
$$


exceed (1/2). Put


$$
h_p=2v_p(r)+1,\qquad Q=\prod_{p\le B}p^{h_p}.
$$


Consider the finite family


$$
F_u(\mathbf x)=u^{r+1}x_1^r+x_2^r+\cdots+x_r^r,
\qquad 1\le u\le Q,\quad (u,Q)=1.
$$


All positive summands of every $F_u$ are $r$-powerful.

Given an integer $a$, choose $t\pmod Q$ that is $0\pmod{p^{h_p}}$ if $p\nmid a$,
and $1\pmod{p^{h_p}}$ otherwise. Then $a-t^r$ is a unit modulo $Q$. Take its
representative $u\in[1,Q]$, and let $v\equiv u^{-1}\pmod Q$. We have


$$
F_u(v,t,0,\ldots,0)\equiv a\pmod Q.
$$


At every $p\le B$, the derivative with respect to $x_1$ has valuation $v_p(r)$.
For $k\ge h_p$, fix the other coordinates modulo $p^{h_p}$, and vary them modulo
$p^k$. Each of the $p^{(k-h_p)(r-1)}$ choices admits a lift of $x_1$, by the
Hensel criterion $h_p>2v_p(r)$. For $k<h_p$, reduction gives at least one
solution. In either case,


$$
\rho_{p^k}(a;F_u)\ge p^{-h_p(r-1)}.
\tag{3}
$$


### Large primes and the uniform product

For $p>B$ not dividing $u$, (1) gives the lower bound $\gamma_p$. If $p\mid u$,
use only the remaining $r-1$ unit-coefficient variables. Their nonsingular
solution count, normalized by $p^{r-2}$, is at least $\gamma'_p$, by the same
Gauss-sum proof with $r-1$ variables. The free first coordinate and nonsingular
lifting give


$$
\rho_{p^k}(a;F_u)\ge\gamma'_p.
$$


Every prime dividing $u$ is at most $Q$. As $r\ge5$, $\prod_{p>B}\gamma_p>0$.
Since all the factors below lie in ((0,1]), equations (1) and (3) imply


$$
\prod_{p^k\parallel M}\rho_{p^k}(a;F_u)\ge\eta_r>0,
$$


where one may take


$$
\eta_r=
\prod_{p\le B}p^{-h_p(r-1)}
\prod_{p>B}\gamma_p
\prod_{B<p\le Q}\gamma'_p.
$$


### Lattice counting

For fixed $M,u$, counting positive lattice points in the region
$F_u(\mathbf x)\le X$, residue class by residue class, gives


$$
\#\{\mathbf x\in\mathbb N^r:F_u(\mathbf x)\le X, F_u(\mathbf x)\equiv a\pmod M\}
=\frac{\Gamma(1+1/r)^r X}{M u^{(r+1)/r}}
\prod_{p^k\parallel M}\rho_{p^k}(a;F_u)
+O_{M,u,r}(X^{1-1/r}).
$$


The map to the ordered summand tuple $(u^{r+1}x_1^r,x_2^r,\ldots,x_r^r)$ is
injective. Taking $u\le Q$ proves (2), with


$$
c_r=\Gamma(1+1/r)^r Q^{-(r+1)/r}\eta_r.
$$


**Scope.** This theorem rules out extending the cubic proof by making ordered
representation first moments arbitrarily small on progressions. By itself it
does not exclude a useful fixed saving, and it gives no density bound for
distinct values. The subsequent
[quintic finite-certificate argument](quintic_first_moment_barrier.md),
extended at the prime five, proves the stronger lower bound
$385732347/156250000>2.468$ for the **unordered** first moment when $r=5$,
ruling out a deficit below one in that case.

## A single locally universal core for the fifth powers

For $r=5$, the same uniform positive lower bound already holds for the single
form


$$
F_5=x_1^5+\cdots+x_5^5.
$$


Here is a direct proof. For a prime $p\ne5$, let $A=\{x^5:x\in\mathbb F_p\}$.
Then


$$
|A|=1+\frac{p-1}{\gcd(5,p-1)},\qquad |5A|\ge\min\{p,5|A|-4\}=p
$$


by Cauchy–Davenport. Every nonzero target has a primitive solution. For zero,
use $(1,-1,0,0,0)$. Nonsingular lifting gives $\rho_{p^k}(a;F_5)\ge p^{-4}$ for
every $k,a$.

At $p=5$, the fifth-power residues modulo $25$ are $0,\pm1,\pm7$. Every centered
residue from $-12$ to $12$ is a sum of at most five of these, with a nonzero
term: use $0=1-1$; ones for $1,\ldots,5$; $6=7-1$; $7$ plus zero through four
ones for $7,\ldots,11$; and $12=7+7-1-1$, then negate. Pad with zeros to five
terms.

Choose corresponding input residues $u_i\pmod5$, with $u_1\ne0$. For $k\ge2$,
every choice $x_i\equiv u_i\pmod5$ for $i=2,\ldots,5$ leaves the required first
fifth power in the correct residue class modulo $25$. The map


$$
\{x\bmod5^k:x\equiv u_1\pmod5\}\longrightarrow
\{y\bmod5^k:y\equiv u_1^5\pmod{25}\},\qquad x\mapsto x^5,
$$


is exactly five-to-one: after writing $x=u_1+5t$, the integer polynomial
$((u_1+5t)^5-u_1^5)/25$ has derivative $u_1^4\pmod5$ and is bijective modulo
every power of $5$. Consequently


$$
\rho_{5^k}(a;F_5)\ge5^{-3}\quad(k\ge2),
$$


while the modulus-$5$ density is $1$.

For $p>256$, use the stronger good-prime bound


$$
\rho_{p^k}(a;F_5)\ge1-1024p^{-3/2}-p^{-4}=\gamma_p>\tfrac12.
$$


The product of these $\gamma_p$ is positive. Combining the finitely many other
primes gives $\eta_5>0$ with $\rho_M(a;F_5)\ge\eta_5$ for every $M,a$. Lattice
counting therefore gives a normalized progression first moment at least
$\Gamma(6/5)^5\eta_5$ for this one core alone. This is a local-distribution
result, not positive density of its distinct values.

## Many denominator primes do not force a proper zero subsum locally

One attempted descent on targets $tm^r$ was to force a proper collection
of summands to add to zero at a prime dividing $m$, and then seek a shorter
powerful relation. Congruences alone do not force that first step, even
for a fixed coefficient tuple.

Fix $r\ge3$ and $F=\sum_i d_i x_i^r$. For $p\nmid r\prod_i d_i$, at least

$$
p^{r-1}-(r-1)^r p^{r/2}-(2^r-2)r^2p^{r-2}                 \tag{4}
$$

roots of $F=0\pmod p$ have no vanishing nonempty proper subsum.
The power-sum estimate above gives the first two terms. For a fixed
proper subset $I$, a root with its $I$-subsum zero also has its complementary
subsum zero. Fixing all but one variable in each block bounds the number
of such roots by $r^2p^{r-2}$. Union over the $2^r-2$ subsets proves (4).

For sufficiently large $p$ this lower bound is positive. Each surviving
root has every coordinate nonzero, since singleton subsums are nonzero.
It is nonsingular and lifts to every $p^k$, including to any prescribed
target divisible by $p$, while retaining the proper-subsum condition
modulo $p$. CRT combines such roots at arbitrarily many sufficiently large
denominator primes avoiding the coefficients.

For canonical $d_i$, the resulting positive root representatives do give
$r$-powerful summands satisfying these congruences. Their exact sum need
not be the prescribed target, and their sizes are uncontrolled. Thus this
excludes only the proposed **local** forcing of a shorter relation; an
argument using exact equality and $d_i x_i^r\le tm^r$ is not ruled out.
