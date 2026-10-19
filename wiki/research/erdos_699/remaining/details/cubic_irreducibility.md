---
name: research/erdos_699/remaining/details/cubic_irreducibility
title: "Erdős 699: a hypothetical cubic counterexample gives an irreducible cubic"
desc: "Every bad triple gives an irreducible integer cubic with roots in (-1,0), and an associated monic integral depressed cubic. Global finiteness remains unproved."
created: 2026-09-21T21:52:28Z
updated: 2026-09-22T19:12:28Z
---

# Erdős 699: a hypothetical cubic counterexample gives an irreducible cubic

[[research/erdos_699/_index|P699 research]] ·
[[problems/factorials_binomials/E0699/_index|Erdős problem 699]] ·
[[research/erdos_699/remaining/details/cubic_uniform|The uniform proof attempt]]

***

This note proves a uniform restriction on a hypothetical counterexample
with index three. After removing its exact power-of-two content, the
associated cubic is **irreducible over the rationals**. The proof uses no
finite search. It does not yet prove nonexistence or global finiteness of
the counterexamples.

The subsequent [elliptic-curve note](cubic_elliptic.md)
proves that a specified twist of $y^2=P(z)$ has a point of infinite order,
and explains why the change to the monic cubic gives an elliptic quartic.

## 1. The integer cubic supplied by badness

Suppose that no odd prime divides both $\binom n3$ and $\binom nj$, with
$4\le j\le n/2$. The
[[research/erdos_699/remaining/details/cubic_followup|earlier cubic reductions]]
give

$$
n=2^h u,\qquad h\ge2,\qquad u\text{ odd},\qquad j<n/2.
$$

Put $c=n-j$ and

$$
W=\frac{u(n-1)(n-2)}6=\frac{\binom n3}{2^h}.
$$

Then $W$ is an odd positive integer. Badness implies that $W$ divides
every coefficient of

$$
R(z)=\sum_{r=0}^3\binom j{3-r}\binom cr z^r.\tag{1}
$$

All four coefficients are positive, and Vandermonde's identity gives

$$
R(1)=\binom n3=2^h W.\tag{2}
$$

We will only use this coefficient divisibility, so the result also applies
to any admissible pair satisfying the necessary endpoint divisibilities
from the uniform proof attempt.

## 2. The column has smaller two-adic valuation than the row

**Lemma.** One has $t:=v_2(j)<h$, and $v_2(c)=t$.

**Proof.** Suppose instead that $2^h\mid j$. Then $2^h\mid c$ as well.
For an integer $x$ divisible by four,

$$v_2\!\binom x3=v_2(x),\qquad
v_2\!\binom x2=v_2(x)-1.$$

Consequently the two endpoint coefficients in (1) are divisible by $2^h$.
Each middle coefficient has valuation
$v_2(j)+v_2(c)-1\ge2h-1\ge h$. Thus every coefficient of $R$ is
divisible by $2^hW$. Since all four are positive, this contradicts (2).
Therefore $t<h$. The equality $v_2(c)=t$ now follows from $c=n-j$.
$\square$

**Lemma.** The largest power of two dividing every coefficient of $R$
is exactly $2^t$.

**Proof.** There is nothing to prove for the lower bound when $t=0$.
For $t\ge1$, the middle coefficients have valuation $2t-1\ge t$.
For $x=j,c$, the endpoint valuation is

$$
v_2\!\binom x3=t+v_2(x-2)-1\ge t.
$$

Thus $2^t$ divides all coefficients. On the other hand,

$$R'(1)=c\binom{n-1}{2}
=\frac{c(n-1)(n-2)}2$$

has valuation exactly $t$. If every coefficient had valuation greater
than $t$, its derivative at one would too. This proves exactness, including
when $t=0$. $\square$

Define

$$
P(z)=\frac{R(z)}{2^tW}\in\mathbb Z[z].\tag{3}
$$

It follows that

$$P(1)=2^{h-t},\qquad
P'(1)=\frac{3c}{2^t u}\text{ is an odd integer}.\tag{4}$$

The integrality of the derivative follows from (3); its oddness follows
either from the exact valuation of $R'(1)$ or directly from the displayed
quotient. Thus the reduction of $P$ modulo two has a **simple root at one**.
Moreover, $P$ is primitive: any common divisor of its coefficients divides
$P(1)$, hence is a power of two, and the exact-content lemma excludes two.

## 3. All three roots are negative and real

For completeness, this needs no general theorem about Jacobi polynomials.
Expansion of the cubic discriminant gives

$$\operatorname{Disc}R
=\frac{j^2c^2(j-1)(c-1)(n-1)(n-2)^2}{12}>0.\tag{5}$$

This is also the cubic specialization of the discriminant identity in the
[[research/erdos_699/proofs/details/cutoff_and_cubic|cutoff and cubic note]].
A real cubic with positive discriminant has three distinct real roots.
The positive coefficients of $R$ exclude nonnegative roots. Therefore all
three roots of $R$, and hence of $P$, are strictly negative.

They in fact all lie in $(-1,0)$. Write $d=c-j$. The earlier alternating
coefficient argument gives $d^2>3n-2$, so

$$\begin{aligned}
R(-1)&=-d(d^2-3n+2)/6<0,\\
R'(-1)&=\frac c2\bigl((d-1)^2-(n-1)\bigr)>0,\\
R''(-1)&=c(c-1)(2-d)<0.
\end{aligned}$$

For the middle inequality, $d^2-2d-n+2>2(n-d)>0$.
Also $R'''(-1)>0$. Consequently every coefficient of $-R(-1-z)$
is positive, excluding any root of $R$ at or below $-1$.

## 4. A general irreducibility observation

**Lemma.** Let $F\in\mathbb Z[z]$ be primitive, with positive leading
coefficient and all roots strictly negative and real. If $F(1)$ is a power
of a prime $p$ and $p\nmid F'(1)$, then $F$ is irreducible over
$\mathbb Q$.

**Proof.** Otherwise Gauss's lemma supplies a factorization $F=AB$ into
nonconstant integer polynomials with positive leading coefficients. Every
root of either factor is negative and real, so every coefficient of either
factor is strictly positive. Hence $A(1),B(1)\ge2$. Their product is the
power $F(1)$ of $p$, so both are divisible by $p$. But then

$$
F'(1)=A'(1)B(1)+A(1)B'(1)\equiv0\pmod p,
$$

a contradiction. $\square$

Applying this lemma with $p=2$ and using (4) proves:

**Theorem.** Every hypothetical bad triple with index three gives a
primitive irreducible cubic $P$ as in (3), with three distinct negative
real roots in $(-1,0)$, $P(1)=2^{h-t}$, and $P'(1)$ odd.

The same conclusion holds under the necessary endpoint divisibilities
alone; the higher Lucas digit conditions have not been used.

## 5. An associated monic integer cubic

The same hypotheses also give a monic irreducible cubic

$$H(y)=y^3-ky+2q,\qquad
k=\frac{3jc}{2^{2t}(n-1)},\quad
q=\frac{jcd}{2^{3t}(n-1)(n-2)},\tag{6}$$

where $k,q$ are positive odd integers. Here is an integrality argument
that also covers the possible canceled factor of three.
The unnormalized integer moments from the uniform note are

$$m=\frac{3j}{u},\qquad
\ell=\frac{3j(j-1)}{u(n-1)},\qquad
a=\frac{3j(j-1)(j-2)}{u(n-1)(n-2)},\qquad 3\mid a.$$

Thus

$$K:=\frac{3jc}{n-1}=u(m-\ell)\in\mathbb Z,\qquad
B:=\frac{2jcd}{(n-1)(n-2)}
=\frac{2u}{3}(2a+m-3\ell)\in\mathbb Z.$$

The latter is integral because $um=3j$ and $3\mid a$.
The four positive integer coefficients of $P$ sum to $2^{h-t}$,
so $t\le h-2$. It follows that $v_2(d)=t+1$ and hence

$$
v_2(K)=2t,\qquad v_2(B)=3t+1.
$$

Dividing $K$ by $2^{2t}$ and $B$ by $2^{3t}$ proves the assertions
about $k,q$. The exact change of variable is

$$P(z)=\frac{2^{2t}(1-z)^3}{u n^2}
H\!\left(\frac{j+cz}{2^t(1-z)}\right).\tag{7}$$

This invertible rational change proves that $H$ is irreducible and has
three real roots. Its discriminant satisfies

$$k^3-27q^2
=2^{2(h-t)-2}u^6\operatorname{Disc}P>0.$$

This gives a monic formulation of the simultaneous real and two-adic
restrictions. It is still a necessary condition: arbitrary odd $k,q$
satisfying a discriminant congruence need not reconstruct admissible
integers $n,j,u$.

## 6. What this settles, and what it leaves open

This excludes every hypothetical pair for which the associated cubic has
a rational root, or any other rational factorization. It also identifies
a totally real cubic field associated with every remaining pair. The
simple root at one modulo two is compatible with irreducibility over the
rationals, so it is not itself a contradiction.

For reference, the exact discriminant after normalization is

$$\operatorname{Disc}P
=\frac{108\,j^2c^2(j-1)(c-1)}
{2^{4t}u^4(n-1)^3(n-2)^2}.\tag{8}$$

Its positivity and integrality can sharpen necessary size inequalities.
They do not supply an upper bound on $h$: when $t$ and $u$ are fixed and
$j/n$ stays inside $(0,1/2)$, the displayed expression grows proportionally
to $n$. Thus neither the elementary discriminant lower bound nor
irreducibility alone completes a finiteness argument.

There is also a direct way to see the limitation of rational approximation.
Homogenize with the orientation

$$
F(x,y)=x^3P(y/x),\qquad r=jx+cy,\quad s=x-y.
$$

Expansion gives the exact identity

$$F(x,y)=\frac{1}{2^t u n^2}\left(
r^3-\frac{3jc}{n-1}rs^2
+\frac{2jc(c-j)}{(n-1)(n-2)}s^3\right).\tag{9}$$

The integer pairs $(r,s)$ form a lattice of determinant $n$, since
$r=ny+js$. Dirichlet approximation, with $Q=\lfloor n^{1/4}\rfloor$,
gives integers $s,y$ with $1\le |s|\le Q$ and
$|ny+js|\le n/(Q+1)$. Set $x=y+s$. Since $n>2j\ge8$,
the two coefficients inside (9) satisfy

$$\frac{3jc}{n-1}\le n,\qquad
\frac{2jc(c-j)}{(n-1)(n-2)}\le n.$$

Thus (9) yields a nonzero integer value with

$$1\le |F(x,y)|\le
\frac{2n^{1/4}+n^{-1/4}}{2^t u}.\tag{10}$$

Nonvanishing follows from irreducibility and $(x,y)\ne(0,0)$.
The numerator scale in (10) still grows when $u,t$ are fixed. Moreover,
the distinguished value $F(1,1)=2^{h-t}$ does not imply that the new value
$F(x,y)$ is a power of two. This approximation therefore does not give a
descent preserving the original hypotheses. Identities (5), (7), and (9), and
the derivative identity used above, were checked symbolically.

The unresolved objective remains to rule out these irreducible cubics,
or to prove that only finitely many can arise from bad triples. Even the
infinite subfamily $u=1$ is not settled by the arguments in these notes.
