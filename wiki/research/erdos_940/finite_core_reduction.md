---
name: research/erdos_940/finite_core_reduction
title: Finite-core reduction of the density question
desc: Quantitative canonical-core approximation, fixed-form equivalence, and checked homogeneity and polynomial-construction limitations.
tags: []
sources: []
created: 2026-09-22T02:24:55Z
updated: 2026-09-22T23:09:46Z
---


# Finite-core reduction of the density question

***

## Status

The statements below are proved. They reduce the question but do not resolve it.

## Canonical cores and a quantitative tail

Fix $r\ge3$. Write $\mathcal P_r$ for the positive $r$-powerful integers and


$$
\mathcal C_r=\left\{\prod_{s=1}^{r-1}b_s^{r+s}:b_1\cdots b_{r-1}\text{ squarefree}\right\}.
$$


Every $n\in\mathcal P_r$ is uniquely $dx^r$, with $d\in\mathcal C_r$ and
$x\ge1$. For each prime exponent, subtract the unique exponent in
$\{0,r+1,\ldots,2r-1\}$ in its residue class modulo $r$. The remaining exponent
is a nonnegative multiple of $r$. This is the decomposition in
[Beyer de Ryke, Section 6, (16)–(17)](../../../library/diophantine_problems/beyer_de_ryke_2026_density_deficit_cube_full_sums/_index.md),
whose full passage has been checked.

Its weight is finite:


$$
W_r=\sum_{d\in\mathcal C_r}d^{-1/r}
=\prod_p\left(1+\sum_{s=1}^{r-1}p^{-1-s/r}\right)<\infty.
$$


For $Y\ge1$, ignoring squarefreeness and coprimality gives


$$
\#(\mathcal C_r\cap[1,Y])
\le Y^{1/(r+1)}\prod_{s=2}^{r-1}\zeta\left(\frac{r+s}{r+1}\right).
$$


Indeed, fix $b_2,\ldots,b_{r-1}$, bound the number of $b_1$ by


$$
Y^{1/(r+1)}\prod_{s=2}^{r-1}b_s^{-(r+s)/(r+1)},
$$


and sum. Dyadic decomposition consequently shows


$$
T_r(Y):=\sum_{\substack{d\in\mathcal C_r\\d>Y}}d^{-1/r}
\ll_r Y^{-1/(r(r+1))}.
$$


The bound $\#(\mathcal P_r\cap[1,X])\le W_rX^{1/r}$ also follows immediately.

## Uniform approximation of the sumset

Let $A_{r,Y}$ be the union of the positive value sets


$$
\{d_1x_1^r+\cdots+d_rx_r^r:x_1,\ldots,x_r\ge1\},
\qquad d_1,\ldots,d_r\in\mathcal C_r\cap[1,Y].
$$


Then, uniformly for $X,Y\ge1$,


$$
0\le\#(S_r\cap[1,X])-\#(A_{r,Y}\cap[1,X])
\ll_r X^{1-1/r}+XY^{-1/(r(r+1))}.
\tag{1}
$$


Representations with fewer than $r$ summands account for $O_r(X^{1-1/r})$
tuples. For fixed cores, the number of $r$-tuples whose sum is at most $X$ is
bounded by


$$
X\prod_{i=1}^r d_i^{-1/r}.
$$


Thus the tuples having at least one core larger than $Y$ are at most


$$
X\bigl(W_r^r-(W_r-T_r(Y))^r\bigr)
\le rXW_r^{r-1}T_r(Y),
$$


which proves (1). Overcounting values causes no problem for this upper bound.

## Equivalence with fixed diagonal forms

The following are equivalent:

1. $S_r$ has natural density zero.
2. Every positive diagonal form $d_1x_1^r+\cdots+d_rx_r^r$ with canonical
   coefficients has a density-zero positive value set.
3. Every positive integral diagonal form $a_1x_1^r+\cdots+a_rx_r^r$ has a
   density-zero positive value set.

The implication $3\Rightarrow2$ is immediate. For $2\Rightarrow1$, fix $Y$; the
finite union $A_{r,Y}$ has density zero. Divide (1) by $X$, let $X\to\infty$,
and then $Y\to\infty$.

For $1\Rightarrow3$, let $R=\operatorname{rad}(a_1\cdots a_r)$ and $L=R^r$.
Every $La_i$ is $r$-powerful, as is $La_i x_i^r$ for every positive $x_i$. If
$V$ is the positive value set of the form with coefficients $a_i$, then
$LV\subseteq S_r$. Moreover


$$
\overline d(LV)=L^{-1}\overline d(V).
$$


Hence $\overline d(S_r)=0$ implies $\overline d(V)=0$.

In particular, $S_r$ has positive upper density if and only if at least one
fixed positive integral diagonal form of degree $r$ in $r$ variables does.
Allowing canonical coefficients to grow with the target cannot avoid this
fixed-form requirement.

**Lower-density qualification.** Positive lower density of $S_r$ implies, by
(1), positive lower density of some finite union $A_{r,Y}$. This argument does
not imply positive lower density of an individual member of that finite union.

### Homogeneity does not repair the lower-density inference

The following counterexample from the
[independent record](independent/canonical_decomposition_and_quartic_zero_target.md),
Section 2, has been checked. Choose integers $1=M_0<M_1<\cdots$ with
$M_j/M_{j+1}^{1-1/r}\to0$. Partition $\mathbb N$ into the alternating unions
$B_0,B_1$ of the bands $[M_j,M_{j+1})$, and put

$$
A_i=\{bk^r:b\in B_i,\ k\ge1\}\qquad(i=0,1).
$$

Both sets are closed under multiplication by positive $r$th powers, and
$A_0\cup A_1=\mathbb N$. If band $j$ belongs to $B_{1-i}$, then at
$X_j=M_{j+1}-1$ every base contributing to $A_i\cap[1,X_j]$ is below $M_j$.
Consequently

$$
\#(A_i\cap[1,X_j])\le M_jX_j^{1/r}=o(X_j).
$$

Thus both $A_i$ have lower density zero. These are abstract homogeneous sets,
not diagonal-form images; the example excludes only an inference from
homogeneity and finite union alone.

## Independent polynomial summands still reduce to fixed forms

The following additional limitation, proposed in Section 9 of the
[independent record](independent/canonical_decomposition_and_quartic_zero_target.md),
is proved here.

**Proposition.** Let $f\in\mathbb Z[T]$ be nonconstant, eventually positive,
and $r$-powerful at every sufficiently large integer input. Every nonconstant
irreducible factor of $f$ over $\mathbb Q$ has multiplicity at least $r$.
In particular $\deg f\ge r$. If $\deg f=r$, then

$$
f(T)=c(aT+b)^r,
\qquad a,b,c\in\mathbb Z,\quad a>0,\quad\gcd(a,b)=1,
$$

where $c$ is positive and $r$-powerful.

**Proof.** By Gauss's lemma write
$f=c\prod_j g_j^{m_j}$ with $c\ne0$ integral and distinct primitive
irreducible $g_j\in\mathbb Z[T]$. A nonconstant integer polynomial $g$ has
infinitely many prime divisors of its nonzero values. Here is the elementary
argument. If these primes formed a finite set $P$, choose $n_0$ with
$A=g(n_0)\ne0$ and let $D$ be the product of $P$ (or $1$ if $P$ is empty).
Then

$$
\frac{g(n_0+ADt)}A=1+DtH(t),\qquad H\in\mathbb Z[t],
$$

is a nonconstant integer polynomial, congruent to $1$ at every prime in $P$.
A value of absolute value greater than $1$ has a prime divisor outside $P$,
contradicting the assumption.

Fix $g_j$. Choose such a prime $p$ outside the finite set dividing $c$, the
leading coefficients and discriminants of the $g_i$, or their pairwise
resultants. A root $n_0$ of $g_j$ modulo $p$ is simple and is not a root of
any other $g_i$. Of its $p$ lifts modulo $p^2$, exactly one remains a root;
choose a different lift. On this residue class modulo $p^2$,

$$
v_p(f(n))=m_j.
$$

There are arbitrarily large positive $n$ in the class, so $m_j\ge r$.

If the total degree is $r$, there is just one factor, primitive and linear,
with multiplicity $r$. Choose its leading coefficient positive; eventual
positivity gives $c>0$. For any $p\mid c$, primitivity of $aT+b$ allows an
arbitrarily large input with $p\nmid an+b$. Hence $v_p(c)\ge r$, as claimed.
$\square$

For at most $r$ fixed univariate polynomial summands with independent positive
integer inputs and the above hypotheses, let the nonconstant degrees be
$d_1,\ldots,d_j$. Eventual positivity gives only

$$
O\left(X^{\sum_{i=1}^j1/d_i}\right)
$$

candidate tuples with sum at most $X$. Constants and finitely many initial
inputs do not affect this bound. It is $o(X)$ unless $j=r$ and all $d_i=r$.
In that remaining case the construction is a single fixed positive integral
diagonal form $\sum_i c_i x_i^r$, with each root variable restricted to an
arithmetic progression. Thus this polynomial construction does not bypass
the fixed-form density problem. No claim is made about coupled multivariate
parametrizations or families varying with $X$.

## Polynomial identities on a missing ray

The preceding polynomial-factor lemma also restricts coupled
one-parameter constructions. Fix $r\ge3$ and $t\in\mathbb N\setminus S_r$.
Suppose

$$
\sum_{i=1}^j f_i(u)=t(au+b)^r,\qquad
1\le j\le r,\quad a,b\in\mathbb Z,\quad a>0,           \tag{P}
$$

where each $f_i\in\mathbb Z[u]$ is positive and $r$-powerful at
**every sufficiently large integer** $u$. Set $g=\gcd(a,b)>0$.
Then $g\ge2$, there are no constant summands, and

$$
f_i(u)=c_i\left(\frac{au+b}{g}\right)^r,\qquad
c_i\in\mathcal P_r,\qquad \sum_i c_i=tg^r.            \tag{P1}
$$


Indeed, positivity prevents cancellation of the highest degrees,
so every $f_i$ has degree at most $r$. The polynomial-factor lemma
makes each nonconstant term $c_i(A_i u+B_i)^r$, where $c_i$ is
positive and $r$-powerful, $A_i>0$, and $\gcd(A_i,B_i)=1$.
Put $w_i=c_iA_i^r$, $s_i=B_i/A_i$, and $s=b/a$. Comparing the
coefficients of $u^r,u^{r-1},u^{r-2}$ in (P) gives

$$
\sum_iw_i=ta^r,\qquad
\sum_iw_is_i=ta^rs,\qquad
\sum_iw_is_i^2=ta^rs^2.
$$

Constants contribute to none of these coefficients, since $r\ge3$.
Thus $\sum_iw_i(s_i-s)^2=0$. Positivity of every $w_i$ implies
$s_i=s$, and primitivity identifies $A_i u+B_i=(au+b)/g$.
Leading coefficients now give $\sum_i c_i=tg^r$. Subtracting (P1)
from (P) rules out positive constant summands. Finally $g=1$
would represent $t$ using at most $r$ powerful terms.

Consequently any **fixed finite list** of identities

$$
\sum_i f_{\nu,i}(u)=t\,m_\nu(u)^r
$$

with $m_\nu\in\mathbb Z[u]$ eventually positive and with the same
eventual-all-input hypotheses produces only $O(M^{1/2})$ distinct
prime denominator values $m_\nu(u)\le M$. A denominator of degree
at least two has $O(M^{1/2})$ relevant integer inputs; a linear
one has fixed content $g\ge2$ and can take at most one distinct
prime value. Constant denominators contribute finitely many values.

This applies, for example, to $t=r+1$, which is not in $S_r$ because
the least powerful integer other than $1$ is $2^r>r+1$.
If $S_r$ were cofinite, representations of $(r+1)p^r$ would therefore
lie outside each prescribed finite list of these constructions for
almost every prime $p$. This does not rule out varying families,
multivariable parametrizations, rational parameters, or arbitrary
representations on that ray.

## A fixed number-field norm cannot equal the diagonal form

This rules out a specific norm-identity construction; it is not a density
theorem. Let $r\ge3$, $a_i\in\mathbb Q^\times$, and
$F=\sum_{i=1}^r a_i x_i^r$. For any number field $L/\mathbb Q$ of degree
$d>1$, any $c\in\mathbb Q^\times$, and any nonzero rational function
$G\in L(x_1,\ldots,x_r)$, one has

$$
cF\ne N_{L(\mathbf x)/\mathbb Q(\mathbf x)}(G).              \tag{2}
$$


Indeed the projective hypersurface $F=0$ is smooth over
$\overline{\mathbb Q}$. If its equation had two nonconstant homogeneous
factors, their hypersurfaces would intersect in $\mathbb P^{r-1}$,
because $r-1\ge2$, and every intersection point would be singular.
Thus $F$ is absolutely irreducible. The prime divisor $(F)$ remains
prime under the constant-field extension to $L$, with ramification
index one and residue degree $d$. Equivalently, its residue function
field tensored with $L$ is a field of degree $d$ over the original
residue field. The norm valuation formula consequently gives

$$
v_F\bigl(N(G)\bigr)=d\,v_{F,L}(G)\in d\mathbb Z,
$$

whereas $v_F(cF)=1$. This proves (2), even with arbitrary denominators
in $G$. Positivity of the coefficients is unnecessary.

The same argument works for any absolutely irreducible polynomial.
It does not apply to reduced norms of central simple algebras, or to
extensions depending on the variables: for
$K=\mathbb Q(\mathbf x)$, the quadratic extension $K(\sqrt{-F})/K$
has $N(\sqrt{-F})=F$. Thus a varying-field method is not excluded.

## Unrestricted tuple counting has a growing constant

The ordered representation asymptotic in
[Beyer de Ryke, Proposition 6.1](../../../library/diophantine_problems/beyer_de_ryke_2026_density_deficit_cube_full_sums/_index.md)
has been checked in the full supplied paper:

$$
\#\{(n_1,\ldots,n_r)\in\mathcal P_r^r:\textstyle\sum_i n_i\le X\}
\sim\Gamma(1+1/r)^rW_r^rX.
$$

For a fixed canonical tuple the lattice volume is
$\Gamma(1+1/r)^rX\prod_i d_i^{-1/r}$, and the box bound
$X\prod_i d_i^{-1/r}$ is summable over the tuples. Dominated
convergence proves the asymptotic. Tuples with repeated actual summands
number $O_r(X^{1-1/r})$, so the unordered constant is

$$
C_r=\frac{\Gamma(1+1/r)^rW_r^r}{r!}.
$$


Section 9 of
[second independent record](independent/quartic_pattern_elimination_and_random_omission.md)
adds the following correct elementary warning: $C_r$ does not eventually become
less than one. The two Euler factors at $2,3$ give

$$
W_r\ge\left(1+\frac{r-1}{4}\right)
       \left(1+\frac{r-1}{9}\right)\ge\frac{r^2}{36}.
$$

Also $\Gamma(1+1/r)=\int_0^\infty t^{1/r}e^{-t}\,dt\ge e^{-1}$
by restricting the integral to $t\ge1$, and $r!\le r^r$. Hence

$$
C_r\ge\left(\frac{r}{36e}\right)^r\longrightarrow\infty.
$$

This rules out an eventual deficit by unrestricted tuple counting alone.
It gives no lower bound for distinct values, since growing multiplicity
can coexist with a density-zero support. The independent fixed-form
equivalence agrees with the one above; its strict-exponent coefficient
tail is weaker than the endpoint $Y^{-1/[r(r+1)]}$ already proved here.

## Mixing the canonical cores costs bounded entropy

This is a proved multiplicity comparison, not a density theorem.
For $\mathbf d\in\mathcal C_r^r$, let $R_{\mathbf d}(n)$ count
positive ordered root tuples representing $n$ by
$F_{\mathbf d}=\sum_i d_i x_i^r$, and let
$R(n)=\sum_{\mathbf d}R_{\mathbf d}(n)$.

Choose uniformly an ordered $r$-tuple of $r$-powerful integers
whose sum is at most $X$. Let $Y$ be its sum and $\mathbf D$ its
canonical core tuple. Then, uniformly for sufficiently large $X$,

$$
\mathbb E\log\frac{R(Y)}{R_{\mathbf D}(Y)}
=H(\mathbf D\mid Y)\le L_r.                            \tag{6}
$$

In particular,

$$
\Pr\{R(Y)>e^K R_{\mathbf D}(Y)\}\le L_r/K
\qquad(K>0).                                          \tag{7}
$$


Here is the entropy bound with the domination step explicit. The
canonical tail proved above implies

$$
\sum_{d\in\mathcal C_r}d^{-1/r}\log d<\infty.
$$

Define the probability law
$\mu(\mathbf d)=W_r^{-r}\prod_i d_i^{-1/r}$. Its entropy
is finite. The total number of inputs is $\gg_r X$, whereas the
number with core $\mathbf d$ is at most
$X\prod_i d_i^{-1/r}$. Consequently
$\Pr(\mathbf D=\mathbf d)\le B_r\mu(\mathbf d)$.
Nonnegativity of relative entropy gives

$$
H(\mathbf D)
\le\mathbb E\log\frac1{\mu(\mathbf D)}
\le B_r\sum_{\mathbf d}\mu(\mathbf d)\log\frac1{\mu(\mathbf d)}
<\infty.
$$

The distribution of $\mathbf D$ has finite support at each $X$,
so this use of relative entropy requires no limiting interchange.
Finally, conditional on $Y=n$,

$$
\Pr(\mathbf D=\mathbf d\mid Y=n)
=R_{\mathbf d}(n)/R(n),
$$

which proves (6); Markov's inequality proves (7).

Equivalently, with $T(X)=\sum_{n\le X}R(n)$ and $0\log0=0$,
one has the exact identity

$$
\sum_{n\le X}R(n)\log R(n)
-\sum_{\mathbf d}\sum_{n\le X}
 R_{\mathbf d}(n)\log R_{\mathbf d}(n)
=T(X)H(\mathbf D\mid Y)=O_r(X).                         \tag{8}
$$

Thus the entropy contributed by competition between different
cores is bounded on the input probability space. The unresolved
self-fiber multiplicities of the fixed forms remain: neither (6)
nor (8) bounds their weighted logarithmic moment. Averaging over
growing coefficients has not supplied a positive-density input
family, since its canonical tail has vanishing mass.
