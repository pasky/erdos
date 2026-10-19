---
name: research/erdos_940/rational_transformations
title: Limits of rational transformations and multiplicative amplification
desc: Fixed rational symmetries act on negligible positive integral input mass unless monomial; linear multiplier classes form a group of order dividing the number of variables.
tags: []
sources: []
created: 2026-09-22T21:15:35Z
updated: 2026-09-22T21:15:35Z
---


# Limits of rational transformations and multiplicative amplification

***

## Status and scope

The statements below are proved limitations of two proposed ways to settle
the density question. They supply no density conclusion for a diagonal
value set or for $S_r$. A family of rational transformations whose
complexity grows with the input scale is not controlled by these bounds.

Throughout, $r\ge3$ and

$$
F(\mathbf x)=\sum_{i=1}^r a_i x_i^r,\qquad a_i\in\mathbb Q_{>0}.
$$


## Summable multiplier sets preserve density zero

Let $A,M\subseteq\mathbb N$, with $1\in M$ and
$S=\sum_{m\in M}1/m<\infty$. Then

$$
\overline d(MA)\le S\,\overline d(A).
\tag{1}
$$

Indeed, for any fixed $K$,

$$
\#(MA\cap[1,X])
\le\sum_{\substack{m\in M\\m\le K}}\#(A\cap[1,X/m])
+X\sum_{\substack{m\in M\\m>K}}\frac1m.
$$

Divide by $X$, take the limsup, and then let $K\to\infty$.
As $A\subseteq MA$, the set $MA$ has density zero if and only if $A$
does. This includes the full set of $r$-powerful multipliers: its
reciprocal sum is at most
$\prod_p(1+p^{-r}/(1-p^{-1}))<\infty$.

Thus multiplicative saturation cannot turn a density-zero value set into
one of positive upper density, even if the original set has a strong
near-linear counting lower bound. This does not decide whether the
original set has density zero.

## Integer inputs of a fixed nonpolynomial rational map

**Lemma.** Let $T\in\mathbb Q(x_1,\ldots,x_r)^s$ have at least one
coordinate which is not a polynomial. For every $\varepsilon>0$,

$$
\#\{\mathbf x\in[1,N]^r\cap\mathbb Z^r:
T\text{ is defined at }\mathbf x,\ T(\mathbf x)\in\mathbb Z^s\}
\ll_{T,\varepsilon}N^{r-1+\varepsilon}.
\tag{2}
$$


Choose a nonpolynomial coordinate $P/Q$ in reduced form with
$P,Q\in\mathbb Z[\mathbf x]$. Let $Q_0$ be a primitive irreducible
nonconstant factor of $Q$, and choose $x_j$ on which $Q_0$ depends.
Over $\mathbb Q(\widehat{\mathbf x})[x_j]$, the polynomials $P,Q_0$
are coprime, by Gauss's lemma. Hence their resultant

$$
R(\widehat{\mathbf x})=\operatorname{Res}_{x_j}(P,Q_0)
$$

is nonzero. The resultant identity, after clearing fixed constants if
necessary, implies that an integral value of $P/Q$ satisfies

$$
Q_0(\mathbf x)\mid cR(\widehat{\mathbf x})
$$

for a fixed nonzero integer $c$.

Discard parameter slices where $R$ or the leading $x_j$-coefficient of
$Q_0$ vanishes. These lie on fixed nonzero polynomial zero sets and
number $O_T(N^{r-2})$; including all $x_j$ costs $O_T(N^{r-1})$.
On any other slice, $|cR|\ll_T N^{O_T(1)}$. There are
$O_{T,\varepsilon}(N^\varepsilon)$ signed divisors of $cR$, and
each equation $Q_0(x_j)=d$ has at most $\deg_{x_j}Q_0$ roots.
There are $O(N^{r-1})$ slices. This proves (2).

## Fixed rational self-maps cannot create typical multiplicity

**Proposition.** Suppose $T\in\mathbb Q(\mathbf x)^r$ satisfies
$F\circ T=F$ identically. Unless $T$ is a positive monomial symmetry
of $F$, only $o_{F,T}(N^r)$ inputs in $[1,N]^r\cap\mathbb Z^r$
have a defined image in $\mathbb N^r$.

If a coordinate is nonpolynomial, apply (2) with $\varepsilon<1$.
Otherwise $T$ is polynomial. At every counted input, positivity and the
identity imply $0<T_i(\mathbf x)\ll_F N$ for each $i$. If some
coordinate has degree $d>1$, with nonzero leading homogeneous part $G$,
then, uniformly for $\mathbf u\in[0,1]^r$,

$$
N^{-d}T_i(N\mathbf u)=G(\mathbf u)+O_T(N^{-1}).
$$

The counted normalized inputs lie in $|G(\mathbf u)|\ll_{F,T}N^{-1}$.
For any fixed $\eta>0$, Riemann sums bound their upper proportion by
the volume of $\{|G|\le\eta\}\cap[0,1]^r$. Letting $\eta\downarrow0$
gives zero, since a nonzero polynomial zero set has measure zero.

It remains to consider $T=A\mathbf x+\mathbf b$. Highest-degree terms
give $F(A\mathbf x)=F(\mathbf x)$. The matrix $A$ is invertible:
a nonzero $v\in\ker A$ would make the directional derivative
$\sum_i r a_i v_i x_i^{r-1}$ identically zero, which is impossible.
The Hessian determinant of $F$ is a nonzero constant times
$(x_1\cdots x_r)^{r-2}$. The transformation rule and unique
factorization force each row of $A$ to be a scalar coordinate form.
Comparing degree-$(r-1)$ terms then gives $\mathbf b=0$.
If any scalar is negative, no positive input has a positive image;
otherwise this is precisely a positive monomial symmetry. This proves
the proposition.

Such symmetries merely permute the actual summands $a_i x_i^r$ and
form a finite group. Consequently no fixed finite list of rational
involutions or self-maps forces unbounded multiplicity on a positive
proportion of inputs. The constants in (2), and the polynomial
small-neighborhood argument, are not uniform over varying maps.

## The multiplier classes of linear similitudes

Let $G=\mathbb Q_{>0}^{\times}/\mathbb Q_{>0}^{\times r}$, and let
$\mathcal A$ be the multiset of classes of $a_1,\ldots,a_r$.
The positive multiplier classes of rational linear similitudes

$$
F(T\mathbf x)=\lambda F(\mathbf x),
\qquad T\in\operatorname{GL}_r(\mathbb Q),\quad\lambda>0,
$$

are exactly

$$
H=\{h\in G:h\mathcal A=\mathcal A\},\qquad |H|\mid r.
\tag{3}
$$

The Hessian argument just given makes $T$ monomial, proving necessity
of multiset stabilization. Conversely, a matching of the coefficient
classes supplies the rational coordinate scalings, which can be chosen
positive. This proves the characterization.

The stabilizer is finite: for a fixed coefficient class $g$, the map
$h\mapsto hg$ injects it into the finite support of $\mathcal A$.
Its action on $G$ is free. Each orbit in the coefficient multiset has
$|H|$ distinct classes with equal multiplicities. Summing their
multiplicities proves $|H|\mid r$.

In particular, two distinct primes cannot both be similitude multipliers:
their classes generate a subgroup of order $r^2$. More generally,
distinct primes with multipliers $p_j^{e_j}$ require
$\prod_j r/\gcd(r,e_j)\mid r$.
Each class in $H$ has a unique positive integer representative $c_h$
with prime exponents in $\{0,\ldots,r-1\}$. Its positive integer
members are exactly $c_h m^r$, $m\ge1$. Thus integer similitude
multipliers have a convergent reciprocal sum. By (1), even allowing
every such output dilation cannot amplify a density-zero set to
positive upper density. Rational coordinate changes may impose further
integrality restrictions; ignoring them only enlarges this saturation.

These results rule out fixed rational amplification and a nonsummable
family of linear dilation symmetries. They do not estimate a family of
transformations of growing complexity, or the actual primitive fibers
of $F$.

## No composition law linear in one input

There is no identity

$$
F(B(\mathbf x,\mathbf y))=F(\mathbf x)F(\mathbf y)
$$

in which $B$ is rational in $\mathbf y$ and linear in $\mathbf x$.
This statement holds for all nonzero rational coefficients, without
positivity, when $r\ge3$.

Indeed, over $K=\mathbb Q(\mathbf y)$ write $B=A\mathbf x$.
The matrix $A$ is invertible: otherwise a kernel vector would give a
nonzero direction along which $F$ has identically zero derivative.
The same Hessian argument over $K$ makes $A$ monomial. Comparing any
one coefficient then gives

$$
F(\mathbf y)=c\,g(\mathbf y)^r,
\qquad c\in\mathbb Q^\times,\quad g\in\mathbb Q(\mathbf y)^\times.
$$

The polynomial $F$ is absolutely irreducible, as proved in the
[fixed-norm argument](finite_core_reduction.md#a-fixed-number-field-norm-cannot-equal-the-diagonal-form).
Taking the valuation at its prime divisor gives $1=r v_F(g)$, a contradiction.

In particular, a reduced-norm construction cannot supply such a
bilinear composition law for a diagonal form. This excludes that
construction, not nonlinear rational composition laws or positive
density of the value set.
