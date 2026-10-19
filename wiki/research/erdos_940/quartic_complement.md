---
name: research/erdos_940/quartic_complement
title: Positive lower density of the quartic complement
desc: Author-recorded argument for positive lower density of the quartic complement; no whole-conclusion review of the prose is filed.
tags: []
sources: []
created: 2026-09-22T02:24:55Z
updated: 2026-10-19T04:18:52Z
---

# Positive lower density of the quartic complement

***

## Status and statement

The argument below proposes positive lower density of the complement for $r=4$.
Its algebraic, analytic, and truncation steps have been checked separately, but
an independent whole-conclusion review of this prose has not been filed. The
argument does not address the density-zero question.

**Theorem.** For every $\varepsilon>0$, there are integers $M,a$, with
$a\equiv8\pmod{16}$, such that


$$
\limsup_{X\to\infty}\frac M X
\#\{n\le X:n\in S_4,\ n\equiv a\pmod M\}<\varepsilon.
\tag{1}
$$


Consequently $\underline d(\mathbb N\setminus S_4)>0$.

The proof uses Hilbert reciprocity, Chebotarev in multiquadratic fields, and
quartic Gauss sums. Its coefficient-uniform analytic estimate is proved in
[the Euler-product note](quartic_euler_majorant.md).

## 1. Canonical coefficients and summable weights

Let


$$
\mathcal C=\left\{\prod_p p^{e_p}:e_p\in\{0,5,6,7\},\text{ finitely many }e_p\ne0\right\}.
$$


Every positive 4-powerful integer is uniquely $dx^4$, with $d\in\mathcal C$,
$x\ge1$. This is the checked canonical decomposition in
[Beyer de Ryke, Section 6](../../../library/diophantine_problems/beyer_de_ryke_2026_density_deficit_cube_full_sums/_index.md).

For $\mathbf d=(d_1,d_2,d_3,d_4)\in\mathcal C^4$, write


$$
D=d_1d_2d_3d_4,\qquad
w(\mathbf d)=D^{-1/4},\qquad
h(\mathbf d)=4^{\omega(D)},\qquad
F_{\mathbf d}(\mathbf x)=\sum_i d_ix_i^4.
$$


Euler products give


$$
\sum_{\mathbf d\in\mathcal C^4}w(\mathbf d)h(\mathbf d)D^\eta<\infty
\qquad(0\le\eta<1/20).
\tag{2}
$$


Indeed, the local factor is $1+O_\eta(p^{-5/4+5\eta})$: the least decaying term
has a positive exponent in just one coefficient. The other finitely many local
terms decay faster. In particular, every fixed logarithmic power can replace
$D^\eta$ in (2). Also


$$
\sum_{\substack{\mathbf d\in\mathcal C^4\\\exists p>B:\ p\mid D}}
w(\mathbf d)h(\mathbf d)\ll B^{-1/4}.
\tag{3}
$$


To see (3), use a union bound over $p>B$ in the convergent Euler product and
$\sum_{n>B}n^{-5/4}\ll B^{-1/4}$.

For a modulus $L$, set


$$
\rho_L(b;\mathbf d)=L^{-3}\#\{\mathbf x\bmod L:F_{\mathbf d}(\mathbf x)\equiv b\pmod L\}.
$$


CRT makes these factors multiplicative in $L$. Positive lattice-point counting,
for fixed $L,\mathbf d$, gives


$$
\#\{\mathbf x\in\mathbb N^4:F_{\mathbf d}(\mathbf x)\le X,
 F_{\mathbf d}(\mathbf x)\equiv b\pmod L\}
=\frac{VX}{L}w(\mathbf d)\rho_L(b;\mathbf d)+o_{L,\mathbf d}(X),
\tag{4}
$$


where $V=\Gamma(5/4)^4$. The box bound for this count is $Xw(\mathbf d)$.
Therefore, for each fixed $L,b$, dominated convergence gives the ordered
representation first moment


$$
\lim_{X\to\infty}\frac L X R_4(X;b,L)
=V\sum_{\mathbf d\in\mathcal C^4}w(\mathbf d)\rho_L(b;\mathbf d).
\tag{5}
$$


Here $R_4$ counts ordered sums of exactly four positive 4-powerful integers. The
dominating summable function is $Lw(\mathbf d)$; $L$ is fixed before taking this
limit. Equivalently, truncate once more after choosing $L$, then use the
absolute $w$-tail. No uniform lattice error in the coefficients is asserted.

## 2. Elimination of the principal-character cases

Call a tuple *exceptional for this proof* if either


$$
D\in\mathbb Q^{\times2},
\quad\text{or}\quad
ab^3c^2d^2\in4\mathbb Q^{\times4}
\tag{6}
$$


for some permutation $(a,b,c,d)$ of its coefficients. This is a larger class
than Ghidelli's exceptional forms. Call the other tuples *regular*.

For $B\ge3$, put


$$
M_0=16\prod_{\substack{p\le B\\p\text{ odd}}}p^2,
\qquad
a_0\equiv8\pmod{16},\quad a_0\equiv p\pmod{p^2}\ (2<p\le B).
\tag{7}
$$


**Elimination lemma.** If a tuple satisfies (6) and every prime dividing its
coefficients is at most $B$, then


$$
\rho_{M_0}(a_0;\mathbf d)=0.
\tag{8}
$$


We use a standard consequence of Hilbert reciprocity: a positive definite
rational quaternary quadratic form of square determinant cannot be isotropic at
every finite place. Such a form is similar to $\langle1,u,v,uv\rangle$, $u,v>0$,
the norm form of the quaternion algebra $(-u,-v)$. This algebra ramifies at
infinity and must ramify at another place. The reciprocity assertion is [Voight,
Chapter 14, Proposition 14.2.1 and Corollary
14.2.3](https://link.springer.com/chapter/10.1007/978-3-030-56694-4_14), whose
passage has been checked.

Suppose first that $D$ is square, and consider $Q(\mathbf y)=\sum_i d_i y_i^2$.
A putative congruence solution to (7) gives
$n=F_{\mathbf d}(\mathbf x)\equiv8\pmod{16}$. At least one coefficient and
corresponding variable are odd; otherwise every fourth-power term is divisible
by 16, by 4-powerfulness. At $y_i=x_i^2$, the value of $Q$ has 2-adic valuation
3, and the derivative in an odd coefficient/variable coordinate has valuation 1.
Hensel's criterion $3>2\cdot1$ gives a nonzero zero of $Q$ over $\mathbb Q_2$.

At an odd coefficient prime $p$, the condition $v_p(n)=1$ forces a unit
coefficient with a unit variable: otherwise the unit-coefficient terms are
divisible by $p^4$, and all nonunit coefficients are divisible by $p^4$. Thus
$F_{\mathbf d}=0\pmod p$ has a nonsingular point. Hensel lifts it to a nonzero
zero over $\mathbb Q_p$; squaring the coordinates gives a nonzero zero of $Q$.
At all other odd primes, $Q$ has four unit coefficients, so finite-field
isotropy and Hensel again give local isotropy. This contradicts reciprocity.

For the second condition in (6), (ab) is a square. Write


$$
a=As^2,\quad b=At^2,
$$


where $A$ is positive squarefree and $s,t$ are positive integers. The condition
in (6) implies that (2stcd) is a rational square. The identity


$$
ax^4+by^4+cz^4+dw^4
=A(sx^2-ty^2)^2+c(z^2)^2+d(w^2)^2+2Ast(xy)^2
\tag{9}
$$


maps the quartic to the positive quadratic form


$$
Q_+=\langle A,c,d,2Ast\rangle,
$$


whose determinant is square. The map in (9) has no nonzero base point over a
characteristic-zero field: $z=w=xy=0$ and $sx^2-ty^2=0$ force all four original
variables to vanish.

The same nonsingular quartic lifting argument gives isotropy of $Q_+$ at odd
coefficient primes. At the remaining odd primes its coefficients are units. At
(2), at least one of $cz^4,dw^4$ must be odd: otherwise those terms are
divisible by 16, while the only possible odd terms are $ax^4,by^4$. Both must be
odd, but then


$$
ax^4+by^4\equiv A(s^2+t^2)\equiv2A\not\equiv0\pmod8,
$$


a contradiction. Thus (9) has an odd coefficient/variable coordinate and value
of valuation 3; quadratic Hensel proves isotropy at (2). Reciprocity again gives
a contradiction, proving (8).

## 3. Uniform local bounds

For an odd prime $p\nmid D$, quartic Gauss sums give


$$
\rho_p(0;\mathbf d)=1+\frac{p-1}{p^2}t_p(\mathbf d),\qquad |t_p(\mathbf d)|\le21.
\tag{10}
$$


If $p\equiv3\pmod4$, fourth powers and squares have the same fiber cardinalities
over each target, and


$$
t_p(\mathbf d)=\left(\frac Dp\right).
\tag{11}
$$


For a **regular** tuple, the
[uniform Euler-product lemma](quartic_euler_majorant.md) proves


$$
\prod_{\substack{2<p\le B\\p\nmid D}}\rho_p(0;\mathbf d)
\ll (\log(2D))^{11},
\tag{12}
$$


uniformly in $B$ and the coefficients. Briefly, the 21 Gauss-sum terms group
into one quadratic Dirichlet character and ten Gaussian Hecke characters. Every
constituent is nonprincipal precisely after excluding the possibilities (6). The
infinity types are fixed. Their moduli are polynomially bounded in $D$, and an
elementary Gaussian lattice estimate bounds each $L(\sigma,\psi)$ by a constant
times the logarithm of its modulus, uniformly for real $\sigma>1$. Comparing
Euler sums at $\sigma=1+1/\log B$ proves (12). The linked note supplies the
expansion, character classification, and uniform estimates.

For any canonical coefficient tuple, a solution of $F=p\pmod{p^2}$ has a
unit-coefficient unit variable. It is nonsingular modulo $p$. If $p\nmid D$,
precisely the zero vector among the roots modulo $p$ fails to lift to this
target, so


$$
\rho_{p^2}(p;\mathbf d)=\rho_p(0;\mathbf d)-p^{-3}.
\tag{13}
$$


If $p\mid D$, either no solutions exist, or a unit coefficient allows the crude
bound $4p^3$ for the number of roots modulo $p$; hence


$$
\rho_{p^2}(p;\mathbf d)\le4.
\tag{14}
$$


The modulus-16 factor is at most (16). Equations (12)–(14) give, for regular
tuples,


$$
\rho_{M_0}(a_0;\mathbf d)
\le C h(\mathbf d)(\log(2D))^{11},
\tag{15}
$$


with $C$ independent of $B,\mathbf d$. For every tuple, (10), (14), and the
usual upper bound for $\sum_{p\le B}1/p$ give


$$
\rho_{M_0}(a_0;\mathbf d)
\le C h(\mathbf d)(\log(2B))^{21}.
\tag{16}
$$


## 4. A character distribution with a bounded total prime budget

Fix positive constants $c_m$, indexed by squarefree integers $m>1$, with
$\sum_m c_m\le1/2$; for instance $c_m=2^{-m}$.

Let $E\subset\mathcal C$ be finite. Put


$$
K_E=\mathbb Q(\sqrt d:d\in E),\quad G=\operatorname{Gal}(K_E/\mathbb Q),
$$


and identify its character group with the positive rational squareclasses
generated by $E$. Represent these squareclasses by squarefree positive integers.
Define


$$
f(g)=1-\sum_{\substack{m\in\widehat G\\m\ne1}}c_m\chi_m(g).
\tag{17}
$$


Orthogonality gives


$$
f(g)\ge\tfrac12,\quad
\frac1{|G|}\sum_g f(g)=1,\quad
\frac1{|G|}\sum_g f(g)\chi_m(g)=-c_m\quad(m\ne1).
\tag{18}
$$


Since $K_E$ is totally real, it is disjoint from $\mathbb Q(i)$. For every
$g\in G$, Chebotarev gives a positive-density set of primes $q\equiv3\pmod4$
with Frobenius $g$, whose reciprocal sum diverges.

Given $T>0$, select finitely many such primes for each $g$, with reciprocal sum
in


$$
\left[\frac{Tf(g)}{|G|},\frac{Tf(g)}{|G|}+\frac1{|G|}\right].
$$


Require all primes to exceed $B$, every coefficient prime in $E$, $T+1$, and
(|G|). Let $\mathcal Q$ be their union. Then


$$
\sum_{q\in\mathcal Q}\frac1q\le T+1,\qquad
\sum_{q\in\mathcal Q}\frac1{q^2}\le1.
\tag{19}
$$


If $\mathbf d\in E^4$ has nonsquare product of squareclass $m$, equations
(18)–(19) imply


$$
\sum_{q\in\mathcal Q}\frac{(D/q)}q\le-Tc_m+1.
$$


At every selected prime impose the target $q\pmod{q^2}$. By (11), (13), and
$\log(1+u)\le u$,


$$
\prod_{q\in\mathcal Q}\rho_{q^2}(q;\mathbf d)
\le\exp(-Tc_m+2).
\tag{20}
$$


The total reciprocal-prime budget in (19) is independent of the size of $E$ and
the rank of $G$. The rates $c_m$ can be extremely small, but they are strictly
positive and were fixed before choosing $E$.

For uncontrolled coefficient tuples, use (11) and (13) when $q\nmid D$, giving
at most (1+1/q), and (14) when $q\mid D$. Since the primes of $M_0$ and
$\mathcal Q$ are disjoint, each coefficient-dividing prime costs at most a
single factor (4). For


$$
M=M_0\prod_{q\in\mathcal Q}q^2,
\quad a\equiv a_0\pmod{M_0},\quad a\equiv q\pmod{q^2},
$$


we therefore have the universal bound


$$
\rho_M(a;\mathbf d)
\le C e^{T+1}(\log(2B))^{21}h(\mathbf d).
\tag{21}
$$


Using valuation-one targets at the selected primes is essential for this simple
bound: with target zero merely modulo $q$, four coefficients divisible by $q$
would produce a factor $q$.

## 5. Parameter order and completion

Fix a small $\delta>0$. All constants below can absorb $V$ and the fixed factors
in the preceding bounds.

First choose $T$ so large that


$$
CVe^2\sum_{\mathbf d\text{ regular}}
w(\mathbf d)h(\mathbf d)(\log(2D))^{11}
e^{-Tc_{\operatorname{sf}(D)}}<\delta.
\tag{22}
$$


This follows by dominated convergence from (2): every regular tuple has
nonsquare $D$, and every $c_m$ is positive.

Next choose $B$ so large that


$$
CVe^{T+1}(\log(2B))^{21}
\sum_{\substack{\mathbf d\\\exists p>B:\p\mid D}}w(\mathbf d)h(\mathbf d)<\delta.
\tag{23}
$$


This is possible by (3). Every exceptional tuple not contributing to this tail
is eliminated by (8).

Now choose a finite $E\subset\mathcal C$, containing (1), such that


$$
CVe^{T+1}(\log(2B))^{21}
\sum_{\mathbf d\notin E^4}w(\mathbf d)h(\mathbf d)<\delta.
\tag{24}
$$


Construct the prime sets and $M,a$ of Section 4 for this $E,T,B$.

Partition the complete coefficient sum in (5). Regular tuples in $E^4$
contribute less than $\delta$ by (15), (20), and (22). Exceptional tuples
supported on primes at most $B$ contribute zero. All other exceptional tuples
contribute less than $\delta$ by (21), (23). Finally the remaining regular
tuples outside $E^4$ contribute less than $\delta$ by (21), (24). Consequently


$$
V\sum_{\mathbf d\in\mathcal C^4}w(\mathbf d)\rho_M(a;\mathbf d)<3\delta.
$$


Equation (5) bounds the upper relative density of the exactly-four-summand value
set by this number. The number of 4-powerful integers up to $X$ is $O(X^{1/4})$,
so one-, two-, and three-summand representations contribute only $O(X^{3/4})$
values. Since $M$ is fixed, these do not affect the relative density. Choose
$3\delta<\varepsilon$ to prove (1).

With $\varepsilon=1/2$, the class $a\pmod M$ alone supplies


$$
\underline d(\mathbb N\setminus S_4)\ge\frac1{2M}>0.
$$


## Exact scope

The argument has no conjectural hypotheses, but the whole conclusion still
awaits independent review. It neither proves $d(S_4)=0$ nor proves positive
upper density of $S_4$. It gives no conclusion about the complement for $r\ge5$.
The latter exponents have a [uniform positive lower bound for progression
representation first moments](local_first_moments.md), so the arbitrarily small
first-moment conclusion used here cannot extend unchanged.

## Checked alternative from the later independent record

The [random omission proof](quartic_random_omission.md), checked from
[second independent record](independent/quartic_pattern_elimination_and_random_omission.md),
proves the same theorem with a different completion mechanism. It replaces the
finite Chebotarev distribution of Section 4 by a small infinite
quadratic-character bias in prime omission probabilities. Its extra input is a
[two-sided uniform prime-harmonic bound](quadratic_prime_harmonics.md); the
existing proof above needs no such lower $L$-bound.

The independent record also gives a convenient alternative to the local
lifting step in Section 2. If $Q(\mathbf z)=n$ and $a_jz_j^2$ is a
$p$-adic unit, replace

$$
z_j\quad\text{by}\quad
z_j\sqrt{1-n/(a_jz_j^2)}.
$$

This produces a nonzero zero of $Q$ whenever $p\mid n$ for odd $p$,
or $8\mid n$ at $2$: the square-root argument is in
$1+p\mathbb Z_p$ or $1+8\mathbb Z_2$, respectively.
For the mixed form (9), if neither unchanged original term is a unit
at an odd coefficient prime, both paired original terms must be units;
otherwise their sum is a unit or every original term is divisible by
$p^4$, contradicting $v_p(n)=1$. The cross term $2Ast(xy)^2$ is then
a unit. At $2$, the unchanged odd term was already forced in Section 2.
Thus this perturbation proves the same finite-place isotropy directly,
without passing through a quartic zero and checking the map's base points.
The exceptional family and reciprocity obstruction are unchanged.
