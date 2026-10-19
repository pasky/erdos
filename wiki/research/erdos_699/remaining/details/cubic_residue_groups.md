---
name: research/erdos_699/remaining/details/cubic_residue_groups
title: "Residue groups required by a cubic counterexample"
desc: "A cubic counterexample needs three groups at (n-2)/2 and two large groups at n-1; bounded groups at (n-2)/2 and columns near the edge or centre are effectively finite."
created: 2026-09-22T23:00:00Z
updated: 2026-10-13T05:28:09Z
---

# Residue groups required by a cubic counterexample

[[research/erdos_699/_index|P699 research]] ·
[[research/erdos_699/remaining/index_three|Index three]]

***

**Theorem.** Suppose that no odd prime divides both $\binom n3$ and
$\binom nj$, where $4\le j\le n/2$. Put $M=(n-2)/2$. For each
$r\in\{0,1,2\}$, let $C_r$ be the product of the full prime-power
components $p^{v_p(M)}$ at which $j\equiv r\pmod{p^{v_p(M)}}$.
Then

$$
C_0>1,\qquad C_1>1,\qquad C_2>1.
$$

In particular,

$$
\omega\!\left(\frac{n-2}{2}\right)\ge3.
$$

These are repository deductions. The proof below is uniform and uses no
new finite search. It excludes entire factorization patterns. Section 7
also proves effective finiteness whenever any one of the three groups is
bounded. Section 8 gives effective finiteness when either $j$ or $n-2j$
is at most a prescribed multiple of $n^{3/4}$. These results do not
establish global finiteness.

## 1. The factorization and the elementary restrictions

The [analytic cubic reductions](../../proofs/details/cutoff_and_cubic.md)
and [endpoint divisibilities](cubic_followup.md) give

$$n=2^h u,\quad u\text{ odd},\quad h\ge2,\quad
3u^3<2^h,\quad4\le j<n/2,\quad u\mid3j.$$

We need only $h\ge5$, and this follows without the retained large finite
computations. If $h\le4$, the displayed inequality forces $u=1$, leaving
$n=4,8,16$. There are no admissible columns for $n=4$. For $n=8$, the
only column in the original range is $j=4$, and seven divides both
binomial coefficients. For $n=16$, seven is a common divisor when
$j=4,5,6$, and five is a common divisor when $j=7,8$. These assertions
follow directly from Lucas's criterion or the binomial values.

Set $c=n-j$, $d=c-j$, and
$t=v_2(j)=v_2(c)<h$. The [integer cubic argument](cubic_irreducibility.md)
proves the assertion about $t$, and the earlier alternating-coefficient
argument gives

$$
d^2>3n-2.
$$

Every full odd prime-power component $p^a\Vert n-r$ satisfies

$$
j\bmod p^a\in\{0,\ldots,r\},\qquad r=0,1,2,
$$

except possibly when $p^a=3$. For $r=2$, the same assertion holds at this
exception automatically. Consequently the three pairwise coprime groups
$C_0,C_1,C_2$ partition $M$.

Write

$$B=C_1,\qquad A=C_0C_2,\qquad M=AB,\qquad
K=\frac{jc}{n-1}.$$

The endpoint divisibilities imply $3K\in\mathbb Z$. Let
$\lambda\in\{1,3\}$ be the reduced denominator of $K$, and put
$\kappa=\lambda K$. If $\lambda=3$, then $v_3(n-1)=1$ and
$3\nmid\kappa nM$: an exponent at least two in $n-1$ would be active,
forcing that full power of three to divide $jc$ and making $K$ integral
at three.

The [factorization argument](../../archive/other_approaches/cubic_factorization.md)
now gives positive integers $r,s$ such that

$$
\kappa=Ar,\qquad \kappa-\lambda=B^2s.\tag{1}
$$

Indeed, components in $C_0$ or $C_2$ divide $jc$, while every component
of $B$ divides both $j-1$ and $c-1$. Use

$$
K-1=\frac{(j-1)(c-1)}{n-1}
$$

and $\gcd(M,\lambda(n-1))=1$. In particular,

$$v_2(r)=2t,\qquad
v_2(s)=v_2\bigl((j-1)(c-1)\bigr).\tag{2}$$

Since $d^2=n^2-4jc>3n-2$, we also have

$$
K<\frac M2,\qquad r<\frac{\lambda B}{2}.\tag{3}
$$

## 2. The middle group cannot be empty

Suppose $B=1$. If $\lambda=1$, (3) leaves no positive integer $r$.
If $\lambda=3$, it forces $r=1$, hence $K=M/3$. Therefore

$$
3d^2=n^2+6n-4.
$$

As $32\mid n$, this would give $d^2\equiv20\pmod{32}$, which is
not a square residue. Thus $C_1=B>1$.

## 3. An empty outer group gives a small square identity

Suppose $C_0=1$ or $C_2=1$. All of $A$ then divides one of $j,c$,
while the other is congruent to two modulo $A$. Choose
$\{x,y\}=\{j,c\}$ and positive integers $a,b$ such that

$$
x=Aa,\qquad y=Ab+2,\qquad a+b=2B.\tag{4}
$$

Positivity of $b$ follows from $y\ge4$. Substituting (4) in
$\lambda jc=(n-1)Ar$ gives

$$
AD=2\lambda a-r,\qquad D=2Br-\lambda ab.\tag{5}
$$

Moreover,

$$
r=\frac{\lambda ay}{n-1}<\lambda a,
$$

so $D$ is a positive integer. Eliminate $A$ between (1) and (5), and
use $ab=B^2-(a-B)^2$. The result is

$$\bigl[r-\lambda(a-B)\bigr]^2
   =(\lambda^2-Ds)B^2.\tag{6}$$

A rational number whose square is an integer is an integer. Hence some
integer $z$ satisfies

$$
r-\lambda(a-B)=zB,\qquad Ds=\lambda^2-z^2,\qquad |z|<\lambda.\tag{7}
$$

Thus $Ds=1$ when $\lambda=1$, and

$$
Ds\in\{9,8,5\}\quad\text{when }\lambda=3.\tag{8}
$$

## 4. Odd columns are impossible in this pattern

If $j$ is odd, then $a,b,r$ are odd. Since $j+c\equiv0\pmod4$,
one of $j-1,c-1$ is divisible by four and the other by two. By (2),

$$
8\mid s.
$$

Also $a+b=2B\equiv2\pmod4$, so $ab\equiv1\pmod4$, and (5) gives

$$
D\equiv2-\lambda\pmod4.
$$

The case $\lambda=1$ contradicts $Ds=1$. For $\lambda=3$, (8) and
$8\mid s$ force $D=1,s=8$, contradicting $D\equiv3\pmod4$.

## 5. Even columns leave one explicit branch

Suppose $j$ is even. From (4), $v_2(a)=t$. If $t=1$, then
$4\mid b$, since $y\equiv2\pmod4$. If $t\ge2$, then $v_2(b)=1$.
In both cases $8\mid ab$. By (2), $8\mid2Br$ as well, so

$$
8\mid D.
$$

Equations (7)--(8) consequently force

$$
\lambda=3,\quad D=8,\quad s=1,\quad z=\pm1.\tag{9}
$$

Now $Ar=B^2+3$. Since $B$ is odd, $v_2(B^2+3)=2$, giving
$t=1$ and $v_2(r)=2$. Combining $8A=6a-r$ with (7) shows that
$z=-1$ would give $r=8(A-B)$, contradicting this valuation. Therefore
$z=1$, and the remaining branch is

$$r=4(2A-B),\qquad a=\frac{2(4A-B)}3,\qquad
8A^2-4AB-B^2=3.\tag{10}$$

## 6. The row label and a quadratic character exclude that branch

Let $\ell$ be an odd prime dividing $\gcd(n,x)$. Since
$n=2AB+2$, it cannot divide $A$. Thus it divides $a$. Also
$\ell\ne3$, because $\lambda=3$ implies $3\nmid n$.
Reducing (10) modulo $\ell$ gives

$$
AB\equiv-1,\qquad B\equiv4A,\qquad4A^2\equiv-1\pmod\ell.
$$

The quadratic equation in (10) then has left side congruent to
$-24A^2\equiv6$, although its right side is three. This forces
$\ell=3$, a contradiction. Hence $\gcd(n,j)=\gcd(n,x)$ is a power
of two. The row-label condition $u\mid3j$ and $3\nmid n$ imply
$u=1$.

We have therefore reduced to $n=2^h$. Since $\lambda=3$, we have
$n\equiv1\pmod3$, so $h$ is even. Every prime divisor $p$ of
$B\mid2^{h-1}-1$ has $2^{h-1}\equiv1\pmod p$ with $h-1$ odd.
The order of two modulo $p$ is odd, so two is a quadratic residue
modulo $p$. Consequently the Jacobi symbol satisfies

$$
\left(\frac2B\right)=1.\tag{11}
$$

On the other hand, $AB=2^{h-1}-1\equiv-1\pmod{16}$. Reducing
the quadratic equation in (10) modulo sixteen gives

$$
8+4-B^2\equiv3\pmod{16},\qquad B^2\equiv9\pmod{16}.
$$

Thus $B\equiv3$ or $5\pmod8$, and the supplementary law for the
Jacobi symbol gives $(2/B)=-1$, contradicting (11).

Both outer groups must therefore be nonempty, completing the proof.

The three groups may still contain arbitrarily many primes and vary with
the row. This restriction does not establish a bound on $h$ or global
finiteness of the remaining bad triples.

## 7. A bounded residue group gives an effective finite set

There is also a uniform effectivity statement.

**Theorem.** Given any positive integer $L$, one can effectively determine
all bad cubic pairs $(n,j)$ for which

$$
\min(C_0,C_1,C_2)\le L.
$$

In particular, every infinite sequence of distinct bad pairs would have
all three $C_r$ tending to infinity. The bound concerns a residue group,
not a prescribed two-adic valuation of $n$.

**Proof.** Put $g=\gcd(u,3)$ and $v=u/g$. The row-label condition gives
$v\mid j,c$, and $\gcd(v,(n-1)(n-2))=1$.

First fix an outer group. Set $C=C_0$ and $x=c$, or $C=C_2$ and $x=j$.
In either case

$$k=\frac{\lambda Cx(x-1)}{(n-1)(n-2)}\in\mathbb Z_{>0},\qquad
k<\lambda C.\tag{12}$$

To see integrality, $n-1$ divides $\lambda x(x-1)$ because
$x(x-1)\equiv-jc\pmod{n-1}$. Moreover $M$ divides $Cx(x-1)$:
the group $C$ supplies the components at which $x\equiv2$, while
every other component divides $x$ or $x-1$. Finally $x(x-1)$ is even
and $n-2=2M$. These three divisors are pairwise coprime. The strict
upper bound follows from $4\le x\le n-4$.

Since $v\mid x$ and $v$ is coprime to the denominator in (12),
$v\mid k$. Thus

$$
u\le3k<3\lambda C.\tag{13}
$$

For a bounded $C$, there are only finitely many possible triples
$(\lambda,k,u)$, and they can be enumerated. Fix one of them and set
$\alpha=k/(\lambda C)\in(0,1)$. Equation (12) becomes

$$
x(x-1)=\alpha(n-1)(n-2).\tag{14}
$$

Split $h$ according to its parity. Write

$$n=\delta X^2,\qquad \delta=\epsilon u,\qquad
\epsilon\in\{1,2\},\qquad X=2^{\lfloor h/2\rfloor}.$$

With $Y=2x-1$, (14) gives the fixed quartic equation

$$
Y^2=4\alpha\delta^2X^4-12\alpha\delta X^2+8\alpha+1.\tag{15}
$$

Its leading and constant coefficients are nonzero, and its discriminant
as a quadratic in $X^2$ is

$$
16\alpha\delta^2(\alpha-1)\ne0.
$$

Consequently the polynomial in $X$ is squarefree, and (15) has geometric
genus one.

Now fix the middle group $B=C_1$. Equations (1) and (3) give

$$
1\le r<\frac{\lambda B}{2},\qquad v^2\mid r.\tag{16}
$$

For the divisibility, $v^2\mid jc$ and $\gcd(v,n-1)=1$ imply
$v^2\mid\kappa=Ar$, while $\gcd(v,A)=1$. Hence

$$
u\le3\sqrt r.
$$

A bounded $B$ again leaves an effectively enumerable finite list of
$(\lambda,r,u)$. Fix one such choice and put
$\alpha=r/(2\lambda B)\in(0,1/4)$. Since $A=(n-2)/(2B)$,
equation (1) now reads

$$
jc=\alpha(n-1)(n-2).
$$

With the same parity split $n=\delta X^2$, the integer $Y=d$ satisfies

$$
Y^2=(1-4\alpha)\delta^2X^4+12\alpha\delta X^2-8\alpha.\tag{17}
$$

Here again the leading and constant coefficients are nonzero, and the
quadratic discriminant is

$$
16\alpha\delta^2(\alpha+2)\ne0.
$$

Thus (17) is another fixed genus-one quartic.

For completeness, both families admit a direct integral map to a
nonsingular Weierstrass equation. Write either as

$$
Y^2=aX^4+bX^2+c
$$

with rational $a,b,c$, where $ac(b^2-4ac)\ne0$. Choose a positive
integer $D$ divisible by their denominators, and put

$$
U=D^2aX^2,\qquad V=D^3aXY.
$$

For integral $X,Y$, these are integers satisfying

$$
V^2=U^3+(D^2b)U^2+(D^4ac)U.\tag{18}
$$

Both coefficients are integers. The cubic is squarefree, since
$ac\ne0$ and $b^2-4ac\ne0$. Thus (18) is a nonsingular elliptic
curve over $\mathbb Q$. The
[Baker–Coates effective theorem for integer points on genus-one curves](https://doi.org/10.1017/S0305004100045904)
provides an algorithm to determine all its integral points. This use of
the theorem does not assume an independently computed Mordell–Weil
basis.

Each integral point of (18) has only finitely many preimages: first solve
$X^2=U/(D^2a)$, then recover $Y$ from $V=D^3aXY$. Our relevant $X$ is
positive, so there is no exceptional zero denominator. Retain only the
preimages with $X$ a power of two and with the required $Y$ and column
conditions. This produces a finite explicit candidate set for each
parameter choice. The full binomial condition decides which candidates
are actually bad. Running this procedure over $C\le L$ or $B\le L$
and the finite parameter lists proves the theorem. $\square$

The algorithm above has not been implemented or evaluated for a particular
$L$. This result still leaves the possibility that all three residue
groups grow without bound. It does not give a uniform stopping bound for
the whole cubic case.

## 8. Effective finiteness near the edge and the center

Two further integer quotients give uniform lower bounds on both the column
$j$ and its doubled distance $d=n-2j$ from the midpoint. They also give
effective finiteness in regions of width $C n^{3/4}$ for every fixed
constant $C$.

**Theorem.** With the preceding notation, every bad pair satisfies

$$
j(j-1)\ge(n-1)\left(1+\sqrt{1+\frac{4M}{\lambda^2}}\right),\tag{19}
$$

and

$$
d^2\ge1+(n-1)\left(1+\frac{\sqrt{M+4\lambda^2}}{\lambda}\right).\tag{20}
$$

For every prescribed positive rational $C$, all bad pairs for which

$$
\min\{j,n-2j\}\le Cn^{3/4}\tag{21}
$$

form an effectively computable finite set. In particular, along any
infinite sequence of distinct bad pairs,

$$\frac{j}{n^{3/4}}\longrightarrow\infty,
\qquad
\frac{n-2j}{n^{3/4}}\longrightarrow\infty.$$

**Proof.** Define

$$x=\frac{\lambda j(j-1)}{2(n-1)},\qquad
m=\frac{\lambda(d^2-1)}{n-1}.$$

Both are integers. For $x$, use
$j(j-1)\equiv-jc\pmod{n-1}$, the integrality of $\lambda jc/(n-1)$,
and the fact that $n-1$ is odd. For $m$, use

$$
m=\lambda(n+1)-4\kappa.
$$

Modulo a full prime-power component of $M$, the three labels
$j\equiv0,1,2$ give respectively

$$x\equiv0,0,\lambda,
\qquad m\equiv3\lambda,-\lambda,3\lambda.$$

Consequently

$$M\mid x(x-\lambda),\qquad
M\mid(m-3\lambda)(m+\lambda).\tag{22}$$

The positive endpoint quotient gives
$j(j-1)(j-2)\ge u(n-1)(n-2)$. Since
$(j-2)/(n-2)<1/2$, it follows that
$j(j-1)>2u(n-1)$, hence $x>\lambda u\ge\lambda$.
Also $m>3\lambda$ follows from $d^2>3n-2$. Thus the integers

$$k=\frac{x(x-\lambda)}M,
\qquad q=\frac{(m-3\lambda)(m+\lambda)}M\tag{23}$$

are positive. Applying $k,q\ge1$ and completing the squares gives
(19)--(20). The first bound can be strengthened by replacing $M$ with
$vM$, where $v=u/\gcd(u,3)$: the row label gives $v\mid x$, and
$\gcd(v,M)=1$, so $v\mid k$.

Now fix $k$ and $\lambda$. Eliminate $M$ from the definition of $x$
and (23), and set $J=2j-1$. The resulting equation is

$$
\lambda kJ^2=16x^3-16\lambda x^2+8kx+\lambda k.\tag{24}
$$

The discriminant of the cubic on the right is

$$
-256k\bigl(128k^2+107\lambda^2k-64\lambda^4\bigr).
$$

It is nonzero for positive integer $k$: the quadratic expression in
$k$ has discriminant $44217\lambda^4$, and $44217$ lies strictly
between $210^2$ and $211^2$. Equation (24) therefore defines a fixed
genus-one curve. The Baker--Coates theorem used in Section 7 effectively
determines all its integer points. Each such point determines at most
one pair under consideration, through

$$
n=2\frac{x(x-\lambda)}k+2,\qquad j=\frac{J+1}2.
$$

Likewise, for fixed $q$ and $\lambda$, elimination gives

$$
\lambda qd^2=(m+\lambda)(2m^2-6\lambda m+q).\tag{25}
$$

Its cubic discriminant is

$$
\bigl(36\lambda^2-8q\bigr)\bigl(8\lambda^2+q\bigr)^2.
$$

This is nonzero because $q>0$ and $\lambda$ is odd, so the only
positive possible zero $q=9\lambda^2/2$ is not an integer. Applying
the same effective theorem gives finitely many integer pairs $(m,d)$,
from which one recovers

$$n=2\frac{(m-3\lambda)(m+\lambda)}q+2,
\qquad j=\frac{n-d}2.$$

It remains to bound the finite lists of parameters. Since $n\ge8$,
we have $n-1\ge7n/8$ and $n-2\ge3n/4$. Thus

$$
k<\frac{\lambda^2j^4}{2(n-1)^2(n-2)}
<\lambda^2\frac{j^4}{n^3},
$$

and

$$
q<\frac{2\lambda^2d^4}{(n-1)^2(n-2)}
<4\lambda^2\frac{d^4}{n^3}.
$$

Therefore $j\le Cn^{3/4}$ forces $k<9C^4$, while
$d\le Cn^{3/4}$ forces $q<36C^4$. Enumerate these parameter lists
with $\lambda\in\{1,3\}$, determine the integer points of
(24)--(25), and test the recovered pairs against the original binomial
condition. This proves effective finiteness in (21). $\square$

These algorithms have not been evaluated for a particular $C$. The
result strengthens the lower bounds by every fixed constant, but does
not improve the exponent $3/4$ or prove global finiteness. Possible bad
pairs with both $j/n^{3/4}$ and $(n-2j)/n^{3/4}$ unbounded remain outside
these finite regions.

## 9. Both labels at n minus one must have large groups

The analogous partition of the active part of $n-1$ gives an elementary
restriction. Let $\mu=3$ if $v_3(n-1)=1$, and $\mu=1$ otherwise,
and write

$$
H=\frac{n-1}{\mu}=D_0D_1,
\qquad
D_r=\prod_{\substack{p^a\Vert H\\j\equiv r\pmod{p^a}}}p^a
\quad(r=0,1).
$$

Here $\mu$ removes the possibly inactive factor three from $n-1$. It
need not equal the reduced denominator $\lambda$ of $K$ used in Sections
1–8: if $v_3(n-1)=1$ but $3\mid jc$, then $\mu=3$ and $\lambda=1$.

Every prime-power component of $H$ is active. Its initial Lucas condition
assigns one of the two labels, so $D_0,D_1$ are coprime and their product
is $H$.

**Theorem.** Every bad cubic pair satisfies

$$
D_0,D_1>1,
\qquad n-2<\frac34(\mu D_0)^3,
\qquad n-2<\frac{4}{3\sqrt3}(\mu D_1)^3.
$$

In particular, $n-1$ has at least two distinct active odd prime factors,
and each label group exceeds $(n-2)^{1/3}/\mu\ge(n-2)^{1/3}/3$.
Together with the theorem above for $M=(n-2)/2$, at least five distinct
odd primes occur across these two coprime factors. At least four are
active. The only possible inactive prime in $M$ is three when
$v_3(M)=1$; the nonemptiness theorem does not exclude a group consisting
solely of this factor. If $M$
has no inactive component, or the group containing that component also
contains an active prime, the count improves to at least five active
primes. The three-group theorem alone does not establish the latter
condition in every row.

**Proof.** Suppose first that one of $D_0,D_1$ is one. Then
$j\equiv0$ or $1\pmod H$. If $\mu=1$, the range
$4\le j<n/2<H$ rules this out. If $\mu=3$, write $n=3H+1$.
The only admissible possibilities are $j=H$ and $j=H+1$.
Put $M=(n-2)/2=(3H-1)/2$. The endpoint divisibility gives
$M\mid j(j-1)(j-2)$, while $M$ is odd and coprime to three.
For $j=H$, the residues of $3j,3(j-1),3(j-2)$ modulo $M$ are
$1,-2,-5$, so $M\mid10$. For $j=H+1$, they are $4,1,-2$,
so $M\mid8$. Both are impossible because the reduction in Section 1
gives $h\ge5$, hence $M\ge15$.

Now $D_0,D_1>1$. Write $j=D_1a+1$ and set $L=\mu D_0$.
The range $j<n/2$ gives $0<a<L/2$. Since
$LD_1=n-1=2M+1$, we have $Lj\equiv a+L\pmod M$.
Multiplying the endpoint divisibility by $L^3$ yields

$$
M\mid a(a+L)(a-L).
$$

This is a nonzero integer of absolute value
$a(L^2-a^2)<3L^3/8$: the function $x(1-x^2)$ is increasing on
$0<x<1/2$ and its endpoint value is $3/8$. Thus
$n-2=2M<3L^3/4$.

Similarly write $j=D_0b$ and set $L=\mu D_1$.
Since $D_0>1$ and $j<n/2$, we have $0<b<L/2$.
Now $Lj\equiv b\pmod M$, so

$$
M\mid b(b-L)(b-2L).
$$

Its absolute value is
$b(L-b)(2L-b)<2L^3/(3\sqrt3)$. Indeed, the maximum of
$x(1-x)(2-x)$ on $0<x<1/2$ is $2/(3\sqrt3)$ at
$x=1-1/\sqrt3$. Since $x=b/L$ is rational, equality is impossible.
Hence $n-2=2M<4L^3/(3\sqrt3)$. $\square$

These bounds exclude unbalanced label splits at $n-1$. They do not
bound either group above or settle the cubic case.
