---
name: research/erdos_699/archive/other_approaches/cubic_nested_heights
title: "Why endpoint weights do not close the surface approximation argument"
desc: "A Bezout argument rules out the required strict inequality for every big divisor with arbitrary endpoint weights when log j / log n tends to one; earlier explicit symmetric calculations are retained."
created: 2026-09-22T00:16:49Z
updated: 2026-09-22T20:30:39Z
---

# Why endpoint weights do not close the surface approximation argument

***

This is a retained earlier research note. The [[research/erdos_699/_index|current reading guide]] gives the latest status and distinguishes completed proofs from remaining cases.

[[research/erdos_699/_index|P699 research]] ·
[[problems/factorials_binomials/E0699/_index|Erdős problem 699]] ·
[[research/erdos_699/remaining/details/cubic_uniform|The uniform cubic attempt]]

This note tests a Diophantine approximation theorem against the remaining
cubic case. **Arbitrary weights at the five endpoint points cannot give the
strict height inequality needed in the range $\log j/\log n\to1$.**
Section 4 proves this for every big rational divisor on the indicated
surface, without assuming symmetry or nefness. Thus the fact that all
three residue groups must grow does not repair this application of the
theorem. This is an obstruction to a proposed proof, not a proof of
nonexistence or finiteness of bad triples.

Sections 1--3 retain the earlier exact calculations for symmetric nef
divisors. They illustrate the failure numerically; the argument in
Section 4 explains why nonsymmetric choices fail as well.

## 1. The surface and the inequality needed

Start with $n=2^h$ and the necessary odd-prime endpoint conditions. Let
$X$ be the blowup of $\mathbf P^1_n\times\mathbf P^1_j$ at

$$
(1,0),(1,1),(2,0),(2,1),(2,2).
$$

Write $F$ for a fiber of the $n$ projection and $H$ for a fiber of the
$j$ projection, and write $E_{rs}$ for the exceptional divisor above
$(r,s)$. Thus $H^2=F^2=0$ and $H.F=1$. Put $Q=(\infty,\infty)$.
Consider

$$
L=aH+bF-x(E_{10}+E_{11})-y(E_{20}+E_{21}+E_{22}),\tag{1}
$$

where $a,b,x,y>0$ are rational and

$$
a\ge2x,\qquad a\ge3y,\qquad b\ge x+y.\tag{2}
$$

These conditions make $L$ nef. For a curve other than a vertical fiber,
the sums of its multiplicities on each of the two rows are at most its
intersection with a vertical fiber; this proves nonnegative intersection
with (1). The two special vertical fibers give the first two inequalities
in (2). Moreover

$$
V:=L^2=2ab-S>0,\qquad S:=2x^2+3y^2.
$$

For a closed subscheme $Y$, use

$$\beta(L,Y)=\liminf_{m\to\infty}
\frac{\sum_{r\ge1}h^0(X,mL\otimes\mathcal I_Y^r)}
{m h^0(X,mL)}.$$

The main theorem of
Huang–Levin–Xiao
permits a divisor and a point on it as a nested regular chain. Applied to
$F_\infty\supset Q$ at infinity
and $F_0$ at $2$, it gives the relevant inequality with contributions
$\beta(L,Q)\log n$ and $\beta(L,F)\log n$ when
$\log j/\log n\to1$. The endpoint gcds give

$$
h_L(n,j)=(a+b-x-y)\log n+o(\log n).
$$

Consequently, to exclude this remaining range by this application, one
would need

$$
\beta(L,Q)+\beta(L,F)>a+b-x-y.\tag{3}
$$

At the finite place one may complete $F_0$ to a regular chain with an
arbitrary point on it and discard the additional nonnegative term. For
fixed odd $u$ in $n=u2^h$, enlarging the fixed set of places gives the
same asymptotic test. The theorem's exceptional algebraic curves do not
repair failure of the strict numerical inequality.

## 2. Exact beta constants

Put $z=(2x+y-a)_+$, where $t_+=\max(t,0)$, and define

$$C_F=
\begin{cases}
\dfrac23x^3+2xy^2+\dfrac13y^3+\dfrac16z^3,&x\ge y,\\[3pt]
y^3+2x^2y+\dfrac16z^3,&x\le y,
\end{cases}$$

$$T=
\begin{cases}
2x^3+3xy^2+\dfrac52y^3,&2x\ge3y,\\[3pt]
\dfrac{14}{9}x^3+2x^2y+4y^3,&2x\le3y.
\end{cases}$$

Then

$$
V\beta(L,F)=ab^2-Sb+C_F,\tag{4}
$$
$$
V\beta(L,Q)=ab^2+(a^2-S)b-aS+T.\tag{5}
$$

Here are derivations which also specify the geometry behind the formulas.

For (4), fix a sufficiently divisible $m$. At $n=1$, the Taylor
coefficient of order $r$ belongs to the subspace of polynomials in $j$
divisible by $[j(j-1)]^{(xm-r)_+}$; at $n=2$, the corresponding condition
is divisibility by $[j(j-1)(j-2)]^{(ym-s)_+}$. These are two filtrations
of $k[j]_{\le am}$, so they admit a simultaneous constant basis $e_i(j)$.
The section module has basis

$$
e_i(j)(n-1)^{r_i}(n-2)^{s_i}.
$$

Thus its dimension at $n$-degree at most $bm$ is
$\sum_i(bm-r_i-s_i+1)_+$. The intersection of the two filtration spaces
has dimension

$$
[am-2\max((xm-r)_+,(ym-s)_+)-(ym-s)_++1]_+.
$$

After scaling, the first moment of the total cost $r_i+s_i$ is $S/2$,
and its second moment is $C_F$. Integrating
$\sum_i(b-t-r_i-s_i)_+$ over $t$ gives (4). In particular, the mixed
second moment follows by integrating the joint tail

$$2\min(p,q)+(2p+q-a)_+,
\qquad 0\le p\le x,\quad0\le q\le y.$$

For (5), blow up $Q$ as well and denote its exceptional divisor by
$E_Q$. Put $A_1=a-2x$, $A_2=a-3y$, and $\tau=a+b-x-y$. For
$0\le t\le\tau$, the negative part of $L-tE_Q$ is supported on the
strict transforms of $F_\infty,H_\infty,F_1,F_2$. Its coefficients are

$$\delta=(t-a)_+,\quad \gamma,\quad
r_1=\frac{(\gamma-A_1)_+}{2},\quad
r_2=\frac{(\gamma-A_2)_+}{3},$$

where $\gamma-r_1-r_2=(t-b)_+$. These are obtained by setting the
intersections of the remaining divisor with the active curves to zero.
The remainder is nef and becomes zero at $t=\tau$. One can check
nefness on the exceptional curves, the vertical and horizontal fibers
through the six points, and the four diagonal curves through $Q$ and
an unequal-$j$ pair from the two rows. These are all the negative curves:
the row and fiber intersection bounds, combined with adjunction, force
any other negative nonfiber curve to have bidegree $(1,1)$; the indicated
four are exactly those possibilities.

Writing

$$s(\gamma)=\gamma-\frac{(\gamma-A_1)_+}{2}
-\frac{(\gamma-A_2)_+}{3},$$

integration of this Zariski decomposition gives

$$V\beta(L,Q)=ab^2+(a^2-S)b-\frac{a^3}{3}
+\int_0^a s(\gamma)^2\,d\gamma.$$

The elementary integral is $a^3/3-aS+T$, proving (5).

## 3. The strict inequality always has the wrong sign

Write $p=x+y$. Multiplying the difference between the two sides of (3)
by $V$ gives

$$
G(b)=-[a^2-2ap+S]b+C_F+T-Sp.
$$

Its coefficient of $b$ is negative, since

$$a^2-2a(x+y)+2x^2+3y^2
=2(x-a/2)^2+3(y-a/3)^2+a^2/6>0.$$

Thus $G$ is largest at $b=p$. There it equals

$$
G(p)=C_F+T-p(a^2-2ap+2S).
$$

Its derivative with respect to $a$ is

$$
2p(p-a)-\frac12(2x+y-a)_+^2<0,
$$

because (2) implies $p\le5a/6$. It therefore suffices to set
$a=\max(2x,3y)$. The resulting expressions are

$$G=
\begin{cases}
-\dfrac43x^3+3xy^2-3y^3,&2x\ge3y,\\[3pt]
-\dfrac{22}{9}x^3+6x^2y-3xy^2-4y^3,&x\le y,\ 2x\le3y,\\[3pt]
-\dfrac49x^3+3xy^2-6y^3,&y\le x\le3y/2.
\end{cases}$$

All three are negative. In the first case, putting $r=y/x\le2/3$
gives $G/x^3=-4/3+3r^2-3r^3\le-8/9$. In the second case, putting
$r=x/y\le1$ and using $6r^2\le6r$ gives $G/y^3\le-1$. In the last
case, $x/y\le3/2$ gives $G/y^3\le-3/2$.

We have proved, throughout (2),

$$
\boxed{\beta(L,Q)+\beta(L,F)<a+b-x-y.}
$$

For example, on the entire boundary family
$L=6H+bF-3(E_{10}+E_{11})-2(E_{20}+E_{21}+E_{22})$, $b\ge5$,
the difference is exactly $-(b-1)/(2b-5)$.

## 4. Arbitrary endpoint weights still cannot give strictness

Suppose $(n,j)$ runs through an unbounded sequence of bad cubic pairs
with $\log j/\log n\to1$. Let

$$
D_i=\gcd(n-1,j-i)\quad(i=0,1),
$$

and let $C_0,C_1,C_2$ be the
[three residue groups at $n-2$](../../remaining/details/cubic_residue_groups.md).
Then

$$
D_0D_1=(n-1)/\lambda,\qquad C_0C_1C_2=(n-2)/2,
$$

where $\lambda\in\{1,3\}$. Pass to a subsequence on which the five
normalized logarithms converge, and write their limits as

$$\alpha_i=\lim\frac{\log D_i}{\log n},\qquad
\gamma_r=\lim\frac{\log C_r}{\log n}.$$

All five numbers are nonnegative, and

$$\alpha_0+\alpha_1=1,\qquad
\gamma_0+\gamma_1+\gamma_2=1.\tag{6}$$

For each pair $(i,r)$, the coprime integers $D_i,C_r$ both divide

$$
j-(r-i)n-(2i-r).
$$

This affine expression is nonzero in $4\le j<n/2$, and its absolute
value is less than $2n$. Hence

$$\alpha_i+\gamma_r\le1
\qquad(i=0,1;\ r=0,1,2).\tag{7}$$

The polytope defined by (6)--(7) has exactly five vertices:

$$
\begin{aligned}
&(\alpha_0,\alpha_1)=(1/3,2/3)\text{ or }(2/3,1/3),
&& (\gamma_0,\gamma_1,\gamma_2)=(1/3,1/3,1/3),\\
&(\alpha_0,\alpha_1)=(1/2,1/2),
&& (\gamma_0,\gamma_1,\gamma_2)
   \text{ is a permutation of }(1/2,1/2,0).
\end{aligned}\tag{8}
$$

For verification, put $m=\min(\alpha_0,\alpha_1)$. The inequalities
say $1/3\le m\le1/2$ and $0\le\gamma_r\le m$. At fixed $m$, the
vertices of the latter triangle are the permutations of
$(m,m,1-2m)$. Each lies on a segment between the corresponding two
points in (8). This proves the assertion about the whole polytope.

### A weighted Bezout inequality

For any nonzero affine polynomial $f(n,j)$ of total degree $d$, we have

$$\alpha_0\operatorname{mult}_{(1,0)}f
 +\alpha_1\operatorname{mult}_{(1,1)}f
 +\sum_{r=0}^2\gamma_r\operatorname{mult}_{(2,r)}f
 \le d.\tag{9}$$

It is enough to check an irreducible factor and the five mass vectors
in (8). If that factor is one of the lines $n=1$ or $n=2$, its weighted
multiplicity sum is exactly one, equal to its degree. Otherwise Bezout
with those two lines gives

$$
m_{10}+m_{11}\le d,\qquad m_{20}+m_{21}+m_{22}\le d,
$$

and each individual multiplicity is at most $d$. At a vertex with all
nonzero masses equal to $1/2$, average the two row inequalities and
discard the unselected multiplicity in the second row. At a vertex
with one $\alpha_i=2/3$, average the two row inequalities and the bound
$m_{1i}\le d$, with coefficient $1/3$ on each. These are exactly (9)
at the five vertices. Convexity and additivity over factors prove (9)
in general. This argument also shows that the divisor consisting of a
line minus these five weighted exceptional divisors is nef on the
blowup of $\mathbf P^2$ at the endpoint points.

### The resulting upper bound for both beta constants

Return to the surface $X$ of Section 1 and take any big rational divisor

$$
L=aH+bF-x_0E_{10}-x_1E_{11}-\sum_{r=0}^2y_rE_{2r}.
$$

Symmetry and nefness are not assumed. A section of $mL$, for sufficiently
divisible $m$, is represented by a polynomial of degree at most $mb$ in
$n$ and at most $ma$ in $j$, with the required endpoint multiplicities.
Write this polynomial as $n^k g(n,j)$, where $n\nmid g$. Its vanishing
order along $F_0$ is $k$. At $Q=(\infty,\infty)$ its vanishing order is

$$
m(a+b)-\deg(n^kg)=m(a+b)-k-\deg g.
$$

The factor $n^k$ is a unit at all five endpoint points. Apply (9) to
$g$, using the multiplicities required by $mL$. Every nonzero section
therefore satisfies

$$\operatorname{ord}_{F_0}(s)+\operatorname{ord}_{Q}(s)
\le m\left(a+b-x_0\alpha_0-x_1\alpha_1
                    -\sum_{r=0}^2y_r\gamma_r\right).\tag{10}$$

The two filtrations of $H^0(X,mL)$ by vanishing at $F_0$ and at $Q$
admit a common adapted basis. Sum (10) over that basis, divide by
$m h^0(X,mL)$, and let $m$ tend to infinity. By the definition of beta,

$$\boxed{
\beta(L,F_0)+\beta(L,Q)
\le a+b-x_0\alpha_0-x_1\alpha_1
                -\sum_{r=0}^2y_r\gamma_r.}\tag{11}$$

For the bad pairs in question, the right side of (11) is precisely
$h_L(n,j)/\log n+o(1)$. At infinity the nested chain
$F_\infty\supset Q$ contributes $\beta(L,Q)\log n+o(\log n)$.
At two the single divisor $F_0$ contributes at most
$\beta(L,F_0)\log n+O(1)$, with equality to leading order for fixed
odd part of $n$. Thus (11) prevents this application of the theorem
from exceeding the available height. Allowing the odd part of $n$ to
vary cannot improve the inequality.

This conclusion concerns this choice of approximation data: the chain
at infinity and the divisor $F_0$ at two, with arbitrary weights at the
five endpoint points. It does not rule out using additional information
at two, other subschemes, or a different Diophantine theorem. Nor does it
cover a sequence with $\log j/\log n$ bounded away from one. Finally,
$C_r\to\infty$ does not imply $\gamma_r>0$; even positivity of all
three limiting masses would not turn (11) into the required strict
inequality.

## Source and provenance

Keping Huang, Aaron Levin and Zheng Xiao,
[*A New Diophantine Approximation Inequality on Surfaces and Its
Applications*](https://arxiv.org/abs/2406.18879), arXiv:2406.18879v1
(2024), Theorem 1.4 and Definition 2.14. The theorem was checked in the
primary TeX source `Surface_20240510.tex`, at the theorem labeled
`BetaMain` and the definition labeled `regulardef`.

The calculations (1)–(5) and the general obstruction (6)–(11) are
deductions here, not claims made in that paper.
