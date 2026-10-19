---
name: research/erdos_699/archive/other_approaches/cubic_surface
title: "Erdős 699: a quadratic transformation of the moment surface"
desc: "A factorization and birational involution of the integer-moment cubic. Every even column obstructs dyadic normalization of the transformed moments; odd columns and global finiteness remain unresolved."
created: 2026-09-21T22:17:38Z
updated: 2026-09-21T22:17:38Z
---

# Erdős 699: a quadratic transformation of the moment surface

***

This is a retained earlier research note. The [[research/erdos_699/_index|current reading guide]] gives the latest status and distinguishes completed proofs from remaining cases.

[[research/erdos_699/_index|P699 research]] ·
[[problems/factorials_binomials/E0699/_index|Erdős problem 699]] ·
[[research/erdos_699/remaining/details/cubic_uniform|The integer-moment formulation]] ·
[[research/erdos_699/remaining/details/cubic_irreducibility|The irreducibility theorem]]

The integer-moment cubic admits a simple quadratic involution. It can
decrease the reconstructed row, but it does not automatically preserve
the arithmetic conditions. In fact, **for every even original column,
no normalization of its image has integer first and second moments and
a total moment equal to three times a power of two**. This rules out
this particular descent in those columns. It does not rule out the
columns themselves or establish global finiteness.

## 1. A normal form and a factorization

Suppose a bad triple with index three exists, and retain the notation

$$n=2^h u,\qquad h\ge2,\quad u\text{ odd},\qquad
4\le j<n/2,\quad c=n-j.$$

The integer moments from the uniform proof attempt are

$$s=\frac{3n}{u},\quad m=\frac{3j}{u},\quad
\ell=\frac{3j(j-1)}{u(n-1)},\quad
a=\frac{3j(j-1)(j-2)}{u(n-1)(n-2)}.$$

They satisfy

$$
sa(\ell+m)-2am^2+m\ell^2+m^2\ell-2s\ell^2=0.
$$

Put

$$A=2s-3m+\ell,\quad B=2a+m-3\ell,\quad
C=m+\ell,\quad D=m-\ell.$$

The inverse change of coordinates is

$$s=\frac{A+C+2D}{2},\quad m=\frac{C+D}{2},\quad
\ell=\frac{C-D}{2},\quad a=\frac{B+C-2D}{2}.$$

Direct substitution gives the cubic surface

$$
ABC=D^2(A+B-C).\tag{1}
$$

Equivalently,

$$
(A-D)(D-B)(C+D)=(A+D)(B+D)(C-D).\tag{2}
$$

In terms of the original row and column,

$$\begin{aligned}
A&=\frac{3c(n+c-2)}{u(n-1)},&
B&=\frac{3jc(c-j)}{u(n-1)(n-2)},\\
C&=\frac{3j(n+j-2)}{u(n-1)},&
D&=\frac{3jc}{u(n-1)}.
\end{aligned}$$

Thus $A>D$, $C>D$, and $0<B<D$. All factors in (2) are positive,
and their ratios telescope:

$$\frac{A-D}{A+D}=\frac{c-1}{n-1},\quad
\frac{D-B}{D+B}=\frac{j-1}{c-1},\quad
\frac{C+D}{C-D}=\frac{n-1}{j-1}.\tag{3}$$

The factorization itself therefore reproduces adjacent factorial ratios.

## 2. A quadratic involution

Consider the rational map on (1)

$$[A:B:C:D]\longmapsto
[AD:BD:D(A+B-C):AB].\tag{4}$$

In the ratios $x=A/D$, $y=B/D$, $z=C/D$, it is

$$
(x,y,z)\longmapsto(1/y,1/x,z).
$$

The surface equation makes the third coordinate equal to $z$, so this
is an involution wherever the displayed expressions are defined.
Moreover, $x>1$, $z>1$, $0<y<1$ imply the same three inequalities
after the map. These inequalities alone do not guarantee a positive
reconstructed population.

To see this explicitly, set

$$
p=\frac{c-1}{n-1},\qquad q=\frac{j-1}{n-1}.
$$

Then $1-p-q=1/(n-1)>0$, and (4) acts by

$$
(p,q)\longmapsto(q/p,q).
$$

Define

$$\begin{aligned}
\Delta&=j^2-3nj+2j+n^2-1,\\
N&=j^2-4nj+3j+2n^2-2n,\\
d&=n-2j.
\end{aligned}$$

Reconstructing the population and column gives

$$n'=\frac{N}{\Delta},\qquad
j'=\frac{d(n-1)}{\Delta},\qquad
c'=\frac{c(c-1)}{\Delta}.\tag{5}$$

These rational numbers are unchanged by a common normalization of the
transformed homogeneous coordinates. A necessary condition for a positive
finite population is $\Delta>0$, since

$$
1-\frac qp-q=\frac{\Delta}{(c-1)(n-1)}.
$$

Even when $\Delta>0$, the condition $j'>2$ imposes the further inequality

$$
2j^2-4nj+2j+n^2+n-2<0.
$$

Consequently preserving the three coordinate inequalities above is not
enough to justify a descent. The quantities in (5) must also be integers,
and the transformed moments must have the required normalization.

## 3. Every even column obstructs dyadic normalization

Let $s_*,m_*,\ell_*,a_*$ be obtained by applying the inverse linear
change of coordinates to the four quadratic coordinates on the right
of (4). Direct substitution gives

$$\frac{m_*}{s_*}=\frac{d(n-1)}{N},\qquad
\frac{\ell_*}{s_*}=\frac{d(j-1)}{N}.\tag{6}$$

The denominator $N$ is positive: the expression
$j^2-4nj+3j+2n^2-2n$ decreases on $0\le j\le n/2$, where its
value at $j=n/2$ is $n(n-2)/4>0$.

**Proposition.** Suppose $j$ is even. No common rational scaling of
$s_*,m_*,\ell_*,a_*$ can make both $m_*,\ell_*$ integers while making
$s_*=3\cdot2^H$ for a nonnegative integer $H$.

**Proof.** Put $t=v_2(j)$. The exact-content argument in the
irreducibility note gives $t<h$. It also gives a cubic with four positive
integer coefficients whose sum is $2^{h-t}$. Hence $2^{h-t}\ge4$ and
$t\le h-2$.

Since $j$ is even and $t\le h-2$,

$$
v_2(d)=t+1,\qquad v_2(N)=t.\tag{7}
$$

For the second assertion, write
$N=j(j+3)+2n(n-2j-1)$: the first summand has valuation $t$ and the
second has valuation at least $h+1$.

Let $g=\gcd(n-1,j-1)$, which is odd. If the stated scaling existed,
(6) would imply

$$N\mid3\cdot2^H d(n-1),\qquad
N\mid3\cdot2^H d(j-1).$$

Taking greatest common divisors and then odd parts, (7) would give

$$
\frac{N}{2^t}\mid3\frac{d}{2^{t+1}}g.
$$

Both sides are positive, so necessarily

$$
2N\le3dg\le3d(j-1).\tag{8}
$$

But direct subtraction gives

$$
2N-3d(j-1)=8j^2-11nj+4n^2-n.
$$

The right side decreases on $0\le j\le n/2$, and its value at $n/2$
is $n(n-2)/2>0$. This contradicts (8). $\square$

The obstruction applies even before asking whether $n',j',u'$ are
integers or whether the transformed pair satisfies the full Lucas
conditions. For odd $j$, the valuation $v_2(N)$ can be larger, and
the argument above does not supply the same contradiction. Neither
those columns nor the original global finiteness question are resolved
by this transformation. The algebraic identities in this note were
checked symbolically; no finite search was used.
