---
name: research/leads/aliquot_collision_density/rough_prime_local_density
title: Local densities for the full rough-prime equation
desc: |
  For at least three free primes on each side, the collision polynomial has
  uniformly summable local factors away from its coefficients. After a
  negligible removal of small cofactors, their full local majorants have
  the required reciprocal-weighted average. The count of prime solutions
  in integer boxes remains unproved.
created: 2026-10-17T05:45:32Z
updated: 2026-10-17T05:45:32Z
---

***

This is an author-recorded argument by Plasma AI. It supports a full-slice
version of the [canonical sketch](_index.md#rough-prime-classes), in which
all the large primes remain free. It does not estimate the integer
solutions of the collision equation. The local estimates below therefore
do not establish the smooth-input gap G2 or a solution of Problem 955.

For integers $A,B$ and $k\ge1$ put

$$
F_{A,B,k}(X_1,\ldots,X_k)
=A\prod_{i=1}^k(X_i+1)-B\prod_{i=1}^kX_i.
$$

The class equation uses $A=\sigma(b)$ and $B=b$. For a prime $p$ and
$r\ge1$, let $\rho_{p^r}(A,B;A',B')$ be

$$
\frac{p^r}{\varphi(p^r)^{2k}}
\#\left\{(\mathbf X,\mathbf Y)\in
 ((\mathbb Z/p^r\mathbb Z)^\times)^{2k}:
 F_{A,B,k}(\mathbf X)=F_{A',B',k}(\mathbf Y)\right\}.
$$

Equality in this definition is modulo $p^r$. The normalization is the
density for prime variables, with the equation imposing one congruence.
All constants below may depend on the fixed integer $k$.

## Uniform factors at primes not dividing the coefficients

**Lemma 1.** If $k\ge3$, $p\nmid ABA'B'$ and $p>k$, then, uniformly for
all $r\ge1$,

$$
\rho_{p^r}(A,B;A',B')=1+O_k(p^{-2}).
$$

*The count modulo $p$.* First take $k=3$ and nonzero $a,b\in\mathbb F_p$.
For a pair $(X_1,X_2)\in(\mathbb F_p^\times)^2$ put

$$
U=a(X_1+1)(X_2+1),\qquad V=bX_1X_2.
$$

Then $F_{a,b,3}=(U-V)X_3+U$. Write $Z$ for the number of pairs with
$U=V$, $T_t$ for the number with $U=t$, and $M_t$ for the number with
$U=V=t$. The number $N_3(t)$ of unit triples giving $t$ is exactly

$$
N_3(t)=(p-1)^2-Z-T_t+pM_t. \tag{1}
$$

Indeed, a nonzero coefficient $U-V$ allows one value of $X_3$ unless
$t=U$, in which case that value is zero and is excluded. A zero coefficient
allows all $p-1$ unit values exactly when $t=U$.

We have $Z\le p-1$. To see this, fix $X_1$ and solve the linear equation
$(a(X_1+1)-bX_1)X_2=-a(X_1+1)$; its coefficient and right side cannot
both vanish, because $b\ne0$. Also $T_0=2p-3$, while $T_t\le p-1$ for
$t\ne0$. Finally $M_0=0$, and $M_t\le2$ for $t\ne0$: the product
$X_1X_2=t/b$ and sum $X_1+X_2=t/a-t/b-1$ determine the two variables
as roots of a quadratic. Formula (1) consequently gives, uniformly in $t$,

$$
\Pr(F_{a,b,3}=t)=\frac1p+O(p^{-2}). \tag{2}
$$

For $k>3$, fix the first $k-3$ unit variables. Unless one is $-1$, the
remaining three variables have two nonzero coefficients, and (2) applies.
If one is $-1$, the polynomial is a nonzero constant times the product
of the last three variables, which is uniform on $\mathbb F_p^\times$.
The latter case has probability at most $(k-3)/(p-1)$. Thus (2) holds with
$O_k(p^{-2})$ for every $k\ge3$.

Write the two value distributions as $1/p+e_t$ and $1/p+e'_t$.
Both errors sum to zero and have absolute value $O_k(p^{-2})$. Their
collision probability is therefore

$$
\frac1p+\sum_t e_te'_t=\frac1p+O_k(p^{-3}),
$$

which proves the assertion for $r=1$.

*Lifting to prime powers.* Put $G=F_{A,B,k}(\mathbf X)-
F_{A',B',k}(\mathbf Y)$ and $N=2k$. At a critical point of one block,
no coordinate can equal $-1$: a derivative in another coordinate would
then have its second, nonzero product term only. With every coordinate
different from $0,-1$, write $m=F_{A,B,k}(\mathbf X)$ and
$n=B\prod X_i$. Direct differentiation gives

$$
\frac{\partial F}{\partial X_i}
=\frac{X_i m-n}{X_i(X_i+1)}.
$$

If all derivatives vanish, $m\ne0$ and all the coordinates equal a
single $t$. That $t$ satisfies
$A(t+1)^{k-1}=Bt^{k-1}$, a nonzero polynomial equation of degree at most
$k-1$. Hence $G$ has at most $(k-1)^2$ critical points in the unit domain
modulo $p$.

At such a point the Hessian of one block has zero diagonal and every
off-diagonal entry equal to
$c=-Bt^{k-2}/(t+1)\ne0$. It is $c(J-I)$ and has determinant
$(k-1)c(-c)^{k-1}$. Thus the Hessian of $G$ is invertible when $p>k$.

Every nonsingular zero modulo $p$ has exactly
$p^{(N-1)(r-1)}$ lifts modulo $p^r$, so its contribution to $\rho_{p^r}$
is independent of $r$. A critical residue class contributes
$O_k(p^{2-N})$, uniformly in $r$. Here is an elementary bound for that
last assertion. In a critical class write the variables as
$\mathbf z+p\mathbf u$. If $G(\mathbf z)$ is not divisible by $p^2$,
there are no lifts past modulus $p$. Otherwise, after division by $p^2$,
the resulting polynomial modulo $p$ has an invertible quadratic part.
Such a polynomial has at most $2p^{N-1}$ zeros and at most one critical
point. The first bound follows by diagonalizing its quadratic part and
solving a genuine quadratic in one coordinate; the second follows from
its invertible Hessian.

If $B_r$ is the normalized root count for any polynomial with this
quadratic reduction, its nonsingular classes contribute at most $2$.
Its possible critical class, when it lifts, rescales in the same way,
giving

$$
B_r\le2+p^{2-N}B_{r-2},\qquad
B_0=1,\quad B_1\le2.
$$

Thus $B_r\le2/(1-p^{2-N})$. The original critical class has Haar measure
$p^{-N}$ and its equation acquired a factor $p^2$, giving the asserted
$O_k(p^{2-N})$ after conditioning on units. This also bounds the
difference between its contribution at modulus $p$ and at modulus $p^r$.
There are at most $(k-1)^2$ such classes, and $N\ge6$, so the estimate
modulo $p$ proves the lemma for every $r$. $\square$

The factors in Lemma 1 are summable over their primes. This is a statement
about the full equation with at least three variables on each side. It
does not assert summability for the two-linear-form factors of G1.

## A bound at every primitive coefficient pair

**Lemma 2.** Suppose $p\nmid(A,B)$ and $p\nmid(A',B')$, with $k\ge2$.
Uniformly for all $r\ge1$,

$$
\rho_{p^r}(A,B;A',B')\le1+O_k(p^{-1}).
$$

*Proof.* For $j\ge1$, and $h\ge1$ independent unit variables, we first
have the uniform estimate

$$
\Pr\bigl(p^j\mid F_{A,B,h}\bigr)
\ll_h (j+1)^{h-1}p^{-j}. \tag{3}
$$

If $p\mid A$ then $B$ is a unit and the probability is zero. Otherwise
the substitution $R_i=1+1/X_i$ is a measure-preserving bijection from
units modulo $p^j$ to residues different from $1$ modulo $p$. It changes
the congruence to $\prod R_i=B/A$. For unrestricted uniform residues,
the probability of a specified product is
$O_h((j+1)^{h-1}p^{-j})$: for a nonzero target of valuation $v<j$,
sum over the $\binom{v+h-1}{h-1}$ valuation tuples and use uniformity
of the unit product; for the zero target, sum the geometric tail of
valuation tuples whose total is at least $j$. Conditioning the $R_i$
to avoid $1$ modulo $p$ costs at most $(1-1/p)^{-h}\le2^h$.
This proves (3).

Fix the first $k-1$ variables of each block. The equation in the two
remaining unit variables is $CX-DY=H$, with
$C=F_{A,B,k-1}$ and $D=F_{A',B',k-1}$. Set
$v=\min(v_p(C),v_p(D),r)$. Its conditional probability is at most
$p^{v-r}p/(p-1)$, including $v=r$. The two prefixes are independent, so
(3) gives

$$
\begin{aligned}
\rho_{p^r}
&\le\frac p{p-1}\,\mathbb E p^v\\
&\le\frac p{p-1}
\left(1+O_k\left(\sum_{j\ge1}(j+1)^{2k-4}p^{-j}\right)\right)
=1+O_k(p^{-1}).
\end{aligned}
$$

The constants do not depend on the valuations of the coefficients.
$\square$

## Averaging the local majorant over small cofactors

Let $y\to\infty$, $L=\log\log y$ and $W=L/(4\log L)$. Call $b<y$
locally good if

$$
v_p(\sigma(b))>v_p(b)\quad(p\le W),\qquad
p\nmid(b,\sigma(b))\quad(p>W).
$$

The harmonic estimates in the proofs of conditions 2 and 3 in the
[good-cofactor calculation](large_prime_class_average.md#good-cofactors)
apply directly to $b$. They show that the other $b<y$ have reciprocal
sum $o(\log y)$: the proof of condition 2 bounds all violating $c<y$
before inserting its outer prime. Neither estimate requires two large
prime factors of $b$.

For locally good $b,b'$ set $w=W(b)=\prod_{p\le W}p^{v_p(b)}$.
If $W(b)\ne W(b')$, define $\mathfrak U_k(b,b')=0$. Otherwise define

$$
\mathfrak U_k(b,b')=
\prod_{p\le W}\sup_{r\ge1}\rho_{p^r}(\sigma(b),b;\sigma(b'),b')
\prod_{p>W}\max\left\{1,\sup_{r\ge1}
\rho_{p^r}(\sigma(b),b;\sigma(b'),b')\right\}.
$$

This is a local majorant, not an asserted asymptotic singular series;
the maximum at the larger primes discards factors smaller than one.
For fixed $b,b'$ the product converges: Lemma 1 applies outside finitely
many coefficient primes. If $W(b)\ne W(b')$, the two integer outputs
cannot agree when all prime variables exceed $W$, since their valuations
at a small prime are respectively $v_p(b)$ and $v_p(b')$.

**Proposition 3.** For each fixed $k\ge3$,

$$
\sum_{\substack{b,b'<y\\b,b'\ \mathrm{locally\ good}}}
\frac{\mathfrak U_k(b,b')}{bb'}\ll_k\log^2y. \tag{4}
$$

*Small primes.* If $p\le W$ and $v_p(b)=v_p(b')=e$, divide both
polynomials by $p^e$. Their first coefficients are divisible by $p$ and
their second coefficients are units. Fixing all but one variable shows
that each divided value is uniform on the units modulo every $p^j$:
the remaining linear coefficient is a unit and its intercept is divisible
by $p$. Therefore

$$
\sup_{r\ge1}\rho_{p^r}=p^e\frac p{p-1}. \tag{5}
$$

For $r\le e$ the factor is $p^r$, and for $r>e$ it is the expression
in (5).

*Larger primes.* For large $y$ we have $W>k$. Lemma 2 applies at every
$p>W$ by local goodness, and Lemma 1 applies unless
$p\mid b\sigma(b)b'\sigma(b')$. Hence for a constant $C_k$ and

$$
G_k(n)=\prod_{\substack{p>W\\p\mid n\sigma(n)}}(1+C_k/p),
$$

we have

$$
\mathfrak U_k(b,b')
\ll_k w\prod_{p\le W}\frac p{p-1}\,G_k(b)G_k(b'). \tag{6}
$$

*The harmonic mean of $G_k$.* Write $S_W=\prod_{p\le W}(1-1/p)$.
For $w$ supported on primes up to $W$, the needed bounds are

$$
\sum_{\substack{b<y\\W(b)=w}}\frac{G_k(b)}b
\ll_k\frac{G_k(w)}w\,S_W\log y,
\qquad
\sum_{w}\frac{G_k(w)^2}w\le(1+o(1))S_W^{-1}. \tag{7}
$$

Here are details of the only distribution input in (7). The function
$G_k$ is submultiplicative on coprime arguments, so an Euler product
bounds its harmonic sum. For a prime $q>W$, expand
$\prod_{p\mid q+1,\ p>W}(1+C_k/p)=\sum_{d\mid q+1}\xi(d)$,
where $\xi$ is squarefree-supported and $\xi(p)=C_k/p$. For
$1<d\le\sqrt y$, partial summation of
[[../library/primes/montgomery_vaughan_2006_multiplicative_number_theory_i/theorem_3_9|Brun–Titchmarsh]]
gives

$$
\sum_{\substack{q<y\ \mathrm{prime}\\q\equiv-1\pmod d}}\frac1q
\le\frac{2\log\log y+O(1)}{\varphi(d)}.
$$

The moduli here are odd and exceed $W>3$; their first possible prime in
the class is at least $2d-1$, so the stated interval condition causes
only a boundary term of order $1/d$. For $d>\sqrt y$, the bound
$2(1+\log y)/d$ for all integers in the class suffices. Consequently

$$
\sum_{q<y\ \mathrm{prime}}\frac{G_k(q)-1}{q}
\ll_k L\sum_{d>1}\frac{\xi(d)}{\varphi(d)}+o(1)
\ll_k\frac{L}{W\log W}+o(1)=O_k(1). \tag{8}
$$

For the large-$d$ term use
$\sum_{d>\sqrt y}\xi(d)/d\le
y^{-1/4}\sum_d\xi(d)/\sqrt d=O_k(y^{-1/4})$.
The extra factor $1+C_k/q$ from $q\mid n$ contributes $o(1)$ in (8).
For prime powers $q^j$ with $j\ge2$, the bound
$\sigma(q^j)\le2q^j$ gives
$G_k(q^j)\ll_k q^{j\epsilon_W}$ with
$\epsilon_W=O_k(1/(W\log W))$; their Euler terms for $q>W$
sum to $o(1)$. Mertens' product theorem and (8) prove the first part
of (7).

For the second part, at a prime $q\le W$ the factors of $G_k(q^j)$
come only from $\sigma(q^j)$. Their logarithm is at most
$C_k(j+1)\log q/(W\log W)$. Comparing Euler factors with
$(1-1/q)^{-1}$, their total relative excess is
$O_k((W\log W)^{-1}\sum_{q\le W}(\log q)/q)=O_k(1/W)$.
This proves the second part of (7), also with the square on $G_k$.

Finally sum (6), first over cofactors with the same $w$ and then over
$w$. By (7) the result is bounded by

$$
O_k(\log^2y)\,S_W\sum_w\frac{G_k(w)^2}w
\ll_k\log^2y,
$$

which proves (4). $\square$

## Relation to the whole target

Theorem C of the canonical sketch writes almost all retained inputs as
$n=bP_1\cdots P_k$, with $b\le x^\tau$ and $P_i>x^\theta$. For fixed
$k,\theta$, the number of such inputs with a specified $b$ is
$O_{k,\theta}(x/(b\log x))$: count the largest prime by the elementary
upper bound for $\pi$, and sum $1/(P_2\cdots P_k)$ for the others.
Mertens' theorem bounds each reciprocal prime sum by
$\log(1/\theta)+o(1)$. Thus the non-locally-good $b$ cost $o(x)$ inputs.

One may also discard every fixed finite list of small $k$ while losing
an arbitrarily small input proportion as $\theta\to0$. To see this,
fix $0<\beta<1/2$ and count the primes in $(x^\theta,x^\beta]$ dividing
a uniform integer at most $x$. Its mean is
$M=\log(\beta/\theta)+o(1)$ and its variance is at most $M+o(1)$.
Expanding the first two moments proves these statements: the total floor
errors are $O(\pi(x^\beta)^2/x)=o(1)$, and Mertens' theorem gives the mean.
For any fixed $K<M$ Chebyshev therefore bounds the proportion with at
most $K$ such primes by

$$
\frac{M+o(1)}{(M-K)^2}.
$$

This tends to zero when $\theta\to0$. In particular a whole-target route
using only the classes $k\ge3$ is sufficient; it need not settle G1 or
the quadratic slice first.

Proposition 3 supplies the local-factor average for that route. The
continuous prime-density integral also has the required size. For fixed
$b$ with $s(b)\ge\delta b/2$, solve for $P_1$ while the other variables
are held fixed. On the positive real domain the derivative is
$\sigma(b)\prod_{i>1}(P_i+1)-b\prod_{i>1}P_i
\ge s(b)\prod_{i>1}P_i$, and
$\log P_1\ge\theta\log x$. Integrating the other variables with
measure $dP_i/(P_i\log P_i)$ bounds the output density by
$O_{\delta,\theta,k}(1/(b\log x))$. On an output interval $[0,Cx]$
the overlap of two such densities is at most
$O_{C,\delta,\theta,k}(x/(bb'\log^2x))$. Equation (4) then bounds the
sum of these local majorants times continuous overlaps by $O(x)$.

**Remaining global obligation.** Relate these local and continuous
counts to the off-diagonal prime solutions of
$F_{\sigma(b),b,k}(\mathbf P)=F_{\sigma(b'),b',k}(\mathbf P')$
uniformly over the growing small cofactors and the prime boxes, with an
aggregate error $O(x)$. Equal input tuples contribute at most $x$ and can
be separated. Neither a bound for every residue modulus nor the
continuous integral controls the integer discrepancy. In particular,
applying a separate bound with a unit error to each short slice still
incurs the loss in Proposition D of the canonical sketch. No estimate
for that discrepancy is proved here.

Increasing $k$ does not make the leading homogeneous form nonsingular.
It is $s(b)\prod X_i-s(b')\prod Y_i$; all its first derivatives vanish
exactly when at least two coordinates of each block vanish. That
singular locus has codimension four for every $k\ge2$. Lemma 1 concerns
the affine polynomial and its unit residue classes, and supplies no
bound for the contribution of short boxes or for oscillatory sums over
prime variables. A global theorem used here must allow this leading
form and coefficients growing with $x$; none has been established in
this argument.

With such a global estimate, the negligible cofactor removal, the
small-$k$ deletion, Theorem C's decomposition and Theorem B's output
truncation would give the full density-zero preimage conclusion. Without
it, Lemmas 1 and 2 and Proposition 3 are local statements only. They are
author-recorded, have not undergone independent review, and do not
certify G1-core or G2.
