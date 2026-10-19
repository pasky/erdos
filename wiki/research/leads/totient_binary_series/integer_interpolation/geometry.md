---
name: research/leads/totient_binary_series/integer_interpolation/geometry
title: Two Quantitative Obligations for Integer Interpolation
desc: |
  Progression means control real solutions; Linnik's theorem gives an
  effective integer cost exp(O(k^2 log k)), still above the required scale.
problems:
- 249
research_state: ready
review_status: unreviewed
created: 2026-09-17T09:20:00Z
updated: 2026-10-14T00:37:26Z
---

***

The [[research/leads/totient_binary_series/integer_interpolation/_index|integer
span theorem]] supplies exact finite solutions, but does not bound their
weighted cost. This page gives an elementary sufficient estimate with
both of its quantitative requirements visible. It is an author-recorded,
unreviewed argument. Proposition 2 below controls the real-solution term
uniformly on sufficiently long prefixes, using finite progression means.
Proposition 4 makes integer solvability effective, with cost at most
$\exp(O(k^2\log(k+2)))$. This bound is too large for the complete-tail
criterion; the required $o(2^k)$ integer cost remains open.

## Projection and rounding in the same finite system

Let $A\in\mathbb Z^{r\times M}$ have row rank $r$, let
$t\in A\mathbb Z^M$, and put

$$
E=\ker_{\mathbb R}A,\qquad
L=E\cap\mathbb Z^M,\qquad d=M-r.
$$

Choose an integer basis $b_1,\ldots,b_d$ of $L$, and let
$b_1^*,\ldots,b_d^*$ be its orthogonal Gram--Schmidt vectors.
When $d=0$ the corresponding sums below are zero. The least Euclidean
norm real solution is

$$
x_0=A^{\mathsf T}(AA^{\mathsf T})^{-1}t\in E^\perp.
\tag{1}
$$

**Proposition 1.** There is $y\in\mathbb Z^M$ with $Ay=t$ and

$$
\|y\|_2^2\le
\|x_0\|_2^2+\frac14\sum_{j=1}^d\|b_j^*\|_2^2.
\tag{2}
$$

For any positive weights $w_1,\ldots,w_M$ and $c\ge0$, this solution
satisfies

$$
c+\sum_iw_i|y_i|
\le c+\|w\|_2
 \left(\|x_0\|_2^2+\frac14\sum_{j=1}^d\|b_j^*\|_2^2\right)^{1/2}.
\tag{3}
$$

*Proof.* Take any integer solution $y^{(0)}$. Its difference from
$x_0$ belongs to $E$. Starting at $j=d$ and proceeding down to 1,
subtract an integer multiple of $b_j$ so that the coefficient of
$b_j^*$ in the residual difference lies in $[-1/2,1/2]$. This is
possible by rounding that real coefficient to a nearest integer.
Since $b_j$ is $b_j^*$ plus a combination of the earlier orthogonal
vectors, the step changes no coefficient already treated. The final
vector $y$ is still an integer solution, and

$$
y-x_0=\sum_{j=1}^d\theta_jb_j^*,\qquad |\theta_j|\le\tfrac12.
$$

The displayed vectors are mutually orthogonal and also orthogonal to
$x_0$. Pythagoras proves (2). Cauchy--Schwarz proves (3). $\square$

This argument is about the prescribed coset, not a nonzero homogeneous
solution. A convenient basis can improve its upper bound; no claim is
made that the bound equals the minimum cost.

## Specialization to shifted totients

For the central-free system fix $k\ge3$, $B=k+2$, $R\ge B$ and let
the columns run through $B\le n\le R$. Thus $M=R-k-1$. The rows are
the $r=2k-1$ shifts $-k<s<0$ and $1\le s\le k$. Set

$$
A_{s,n}=\frac{\varphi(n+s)}2,\qquad
t_s=\begin{cases}0,&s<0,\\-\varphi(s),&s>0.\end{cases}
\tag{4}
$$

All entries are integral. Suppose this finite matrix has full row
rank and $t\in A\mathbb Z^M$. Full integer image $A\mathbb Z^M=\mathbb Z^r$
is a stronger sufficient hypothesis; the integer span theorem guarantees
it at some finite $R$ for each fixed $k$, without an endpoint estimate.

Use $c=2(k+2)$ and weights $w_n=n+k+2$ in (3). Then the resulting
integer solution has the same cost $C_k(y)$ as the
[[research/leads/totient_binary_series/integer_interpolation/_index|complete-tail
criterion]], and

$$
C_k(y)\le 2(k+2)+(R+k+2)\sqrt M
 \left(\|x_0\|_2^2+\frac14\sum_{j=1}^d\|b_j^*\|_2^2\right)^{1/2}.
\tag{5}
$$

Hence a sequence of finite matrices satisfying these hypotheses and
making the right side of (5) equal to $o(2^k)$ would prove the desired
irrationality. This is a sufficient conditional reduction, not a
uniform estimate.

For example, it would suffice to prove, along an unbounded sequence
of $k$, that $R=O(k)$, the least positive singular value of $A$ is
at least $k^{-a}$, and a kernel basis has
$\|b_j^*\|_2\le k^b$ for fixed $a,b\ge0$, in addition to finite
row rank and integral target membership. Indeed
$\|t\|_2\le k^{3/2}$ and
$\|x_0\|_2\le\|t\|_2/\sigma_{\min}(A)$; (5) then gives

$$
C_k(y)=O\!\left(k^{\max(a+3,b+2)}\right)=o(2^k).
$$

No such collection of bounds on prefixes of length $O(k)$ has been
proved here. Proposition 2 instead controls the real contribution on
prefixes of length $O(k^3\log k)$ and uniformly on a specified family
of longer prefixes. The integral membership and rounding cost still
need control at a useful endpoint. Different arithmetic constructions
can also bound $C_k$ without passing through (5).

## Why one geometric bound is insufficient

Both terms in (2) matter, even for integer matrices of full integer
image whose entries have absolute value at most two.

First let $U_r$ be the upper bidiagonal matrix with 1 on its diagonal
and $-2$ immediately above, and take

$$
A=[\,U_r\ \ 0\,],\qquad t=e_r.
\tag{6}
$$

The determinant of $U_r$ is one, so the image is all of $\mathbb Z^r$.
The integer kernel is the last coordinate copy of $\mathbb Z$.
It has covolume one, a unit basis vector, and shortest nonzero dual
vector of length one, with the dual taken in its real span. However
every real solution has first $r$ coordinates

$$
(2^{r-1},2^{r-2},\ldots,2,1).
$$

Thus $\|x_0\|_2\ge2^{r-1}$. Even perfect control of the kernel and
its dual leaves an exponentially large prescribed solution.

For a separate obstruction, let $A$ be the $r\times(r+1)$ matrix
defined by $(Ax)_i=x_i-2x_{i+1}$ and again take $t=e_r$.
Its first $r$ columns are $U_r$, so it also has full integer image.
The real vector $(0,\ldots,0,-1/2)$ is a solution, giving
$\|x_0\|_2\le1/2$. Every integer solution nevertheless has

$$
x_i=2^{r-i}(1+2u)\quad(1\le i\le r),\qquad x_{r+1}=u\in\mathbb Z,
$$

and hence $|x_1|\ge2^{r-1}$. Here the kernel is generated by
$(2^r,2^{r-1},\ldots,2,1)$, and rounding to the integer coset is
the large term. Neither example concerns a totient matrix. They
disprove a general inference from only one of the two estimates.

## Covolume and the limits of finite diagnostics

For full row rank, let
$\Delta=[\mathbb Z^r:A\mathbb Z^M]$. The exact covolume relation is

$$
\det L=\frac{\sqrt{\det(AA^{\mathsf T})}}{\Delta}.
\tag{7}
$$

To see this, extend an integer basis of $L$ to a basis of $\mathbb Z^M$
by lifting a basis of the free group $A\mathbb Z^M$. Orthogonal
projection of these lifts to $E^\perp$ has volume $1/\det L$,
because the whole integer basis has volume one. The restriction of
$A$ to $E^\perp$ scales volume by $\sqrt{\det(AA^{\mathsf T})}$,
while its image basis has volume $\Delta$. This proves (7).

For (4), Hadamard's inequality gives

$$
\det L\le\left(\frac{\sqrt M(R+k)}2\right)^r.
$$

For the unnormalized matrix $G=2A$, the corresponding image index is
$2^r\Delta$; it cannot be dropped in an estimate uniform in $r$.
A determinant bound controls a product of lengths, not every direction
or the distance of the prescribed coset from zero. When $R=4k$ in
the central-free system, $M=3k-1$ and $d=k$; the displayed
determinant bound to the power $1/d$ has order at most $k^3$ up to
a constant factor, rather than $k^2$. This observation still supplies
no covering estimate.

Finite reductions give upper bounds for feasible inhomogeneous costs
and, if separately retained, for nonzero homogeneous vectors. The ratio
of two upper bounds need not bound the ratio of the two minima.
Even an actual ratio growing geometrically would not alone contradict
$C_k/2^k\to0$: growth with a base below two can satisfy this criterion.
Conversely a lower bound on a fixed finite support does not bound the
minimum over all finite supports. The research decision must therefore
keep the exact support, target, arithmetic membership and type of bound
visible. No finite table settles the remaining asymptotic estimate.

## Uniform control of the real contribution on long prefixes

The [[research/leads/totient_binary_series/progression_means|explicit
progression-mean bound]], Lemma 2a, gives a quantitative result for these
particular matrices. Only its finite-window estimate and the exact mean
formula are used. There is no exchange of limits in growing parameters.
Write $\kappa=1/\zeta(2)$ and use natural logarithms. In particular
$\kappa>1/2$, since $\sum_{n\ge2}n^{-2}<\int_1^\infty x^{-2}\,dx=1$.

**Proposition 2.** Fix integers $k\ge3$ and $1\le r\le2k$, and distinct
integer shifts $-k<s_1,\ldots,s_r\le k$. Choose a prime
$2k<\ell<4k$, which exists by Bertrand's postulate. For every integer

$$
X\ge\left\lceil4096k^2\log(k+2)\right\rceil,
\qquad R=2\ell X+\ell+k-1,
$$

let $A$ have entries $A_{j,n}=\varphi(n+s_j)/2$ for
$k+2\le n\le R$. Then $A$ has full real row rank and

$$
\sigma_{\min}(A)\ge\frac{\kappa X^{3/2}}4.
\tag{8}
$$

*Proof.* Fix any $c\in\mathbb R^r$ with $\|c\|_2=1$, set
$D=\sum_jc_j$ and $u_j=s_j+k\in\{1,\ldots,2k\}$. Define
$F(n)=\sum_jc_j\rho(n+s_j)$, where $\rho(m)=\varphi(m)/m$.
For $0\le b<\ell$, let $d_b=c_j$ if $u_j\equiv-b\pmod\ell$
and $d_b=0$ otherwise. There is at most one such $j$, since
$\ell>2k$. The exact mean on $n-k\equiv b\pmod\ell$ is

$$
M_b=\frac{\kappa}{1-\ell^{-2}}
       \left(D-\frac{d_b}{\ell}\right).
$$

Since $\sum_bd_b=D$ and $\sum_bd_b^2=1$, all $\ell$ classes together
give the exact identity

$$
\frac1\ell\sum_{b=0}^{\ell-1}M_b^2
=\frac{\kappa^2}{(1-\ell^{-2})^2}
  \left((1-2\ell^{-2})D^2+\ell^{-3}\right)
\ge\frac{\kappa^2}{\ell^3}.
\tag{9}
$$

For each class use the same $X$ samples
$n=b+\ell(X+t)+k$, $1\le t\le X$. Lemma 2a, with modulus
$\ell$, starting index $T=X$, cutoff $H=2k$, and the kernel at
$u_j$, bounds the error between the sample mean of $F$ and $M_b$ by

$$
E_1=\frac{\sqrt r\,[2+\log(\ell(2X+1)+2k)]}{X}.
$$

This is uniform in $c$ and $b$, because $\sum_j|c_j|\le\sqrt r$.
Put $G(n)=\sum_jc_j\varphi(n+s_j)/n$. At these samples,

$$
|G(n)-F(n)|
=\left|\frac1n\sum_jc_js_j\rho(n+s_j)\right|
\le\frac{k\sqrt r}{\ell X}=:E_2.
$$

The stated threshold makes each $E_i$ less than
$\kappa/(4\ell^{3/2})$. Here are explicit estimates for all growing
parameters. Write $L=\log(k+2)>1$ and $X_0=4096k^2L$.
The function $[2+\log(14kx)]/x$ decreases for $x\ge1$; also
$\ell(2X+1)+2k\le14kX$. Using $\sqrt r\le\sqrt{2k}$ and

$$
2+\log(14kX_0)
=2+\log(14\cdot4096)+3\log k+\log L<22L
$$

therefore gives

$$
E_1<\frac{22\sqrt2}{4096k^{3/2}}
    <\frac1{64k^{3/2}},\qquad
E_2\le\frac{\sqrt2}{8192k^{3/2}L}
    <\frac1{64k^{3/2}}
    <\frac{\kappa}{4\ell^{3/2}}.
$$

For the logarithmic estimate use $14\cdot4096<2^{16}$,
$\log2<1$, $\log k<L$, and $\log L\le L$.
The same last comparison applies to $E_1$.

Let $\overline G_b$ denote the sample mean of $G$ on class $b$.
The triangle inequality for the normalized Euclidean norm over the
$\ell$ classes, (9), and the two error bounds imply

$$
\left(\frac1\ell\sum_b\overline G_b^2\right)^{1/2}
\ge\frac{\kappa}{2\ell^{3/2}}.
$$

By the elementary mean-square inequality on each class,

$$
\sum_{b,t}G\bigl(b+\ell(X+t)+k\bigr)^2
\ge X\sum_b\overline G_b^2
\ge\frac{\kappa^2X}{4\ell^2}.
$$

These $\ell X$ samples are distinct columns of $A$. Their indices
range from $\ell(X+1)+k$ to $R$, and all are at least $\ell X$.
At column $n$, $(A^{\mathsf T}c)_n=nG(n)/2$. Thus

$$
\|A^{\mathsf T}c\|_2^2
\ge\frac{(\ell X)^2}{4}\sum_{b,t}G(n)^2
\ge\frac{\kappa^2X^3}{16}.
$$

This holds for every unit real $c$ at the same $k,\ell,X,R$,
proving full row rank and (8). $\square$

**Corollary 3.** For the central-free target (4), and also for the
central-zero target with shift zero added, the least-norm real solution
at every endpoint of Proposition 2 satisfies

$$
\|x_0\|_2\le\frac{4k^{3/2}}{\kappa X^{3/2}},\qquad
(R+k+2)\sqrt M\,\|x_0\|_2
\le\frac{256}{\kappa}k^3<512k^3,
\quad M=R-k-1.
\tag{10}
$$

Indeed $\|t\|_2\le k^{3/2}$. Also $2k+1\le\ell$ and $X\ge1$
give $R+k+2\le4\ell X$ and $M\le4\ell X$. Combining these
with (8) and $\ell<4k$ proves (10). The constant is independent
of how far $X$ is increased.

The integer span theorem guarantees that, for each fixed $k$, the
full integer image is eventually reached as $X$ increases. Every larger
prefix retains it. Thus one can also choose such an $X$ with
$t\in A\mathbb Z^M$, while retaining the uniform bound (10).
No quantitative endpoint for that integer image follows from the real
singular-value estimate.

For any such $X$ and any integer kernel basis, Proposition 1 and
$\sqrt{a+b}\le\sqrt a+\sqrt b$ supply an integer solution with

$$
C_k(y)\le2(k+2)+512k^3+
 \frac{(R+k+2)\sqrt M}{2}
 \left(\sum_{j=1}^{M-r}\|b_j^*\|_2^2\right)^{1/2}.
\tag{11}
$$

Consequently this particular route now asks for endpoints and kernel
bases, along unbounded $k$, satisfying the integral membership condition
and making the last term $o(2^k)$. Selecting an endpoint with useful
weighted rounding cost is part of that obligation. The real contribution
in (11) already has a uniform polynomial bound. A full-rank real matrix,
or even its eventual full integer image, does not supply the remaining
estimate. No irrationality conclusion is drawn without it.

## An effective integer bound above the required scale

The qualitative prime construction can be made quantitative. The external input
here is Linnik's theorem: there are effective absolute constants $c,L\ge1$ such
that every reduced class modulo $m\ge2$ contains a prime at most $cm^L$. Its
statement was checked in [Xylouris, *On the least prime in an arithmetic
progression and estimates for the zeros of Dirichlet L-functions*, Acta
Arithmetica 150 (2011), pp. 65--66, Theorem
1.1](https://www.impan.pl/shop/en/publication/transaction/download/product/83078);
that paper gives $L=5.18$. Only the existence of effective
absolute constants is used, and the analytic proof is not reconstructed. The
following argument also uses Proposition 2 and elementary integer linear
algebra. It remains author-recorded and unreviewed.

**Lemma 4a (bounded separation modulo a prime).** Let $k\ge3$, let
$-k<s_1,\ldots,s_r\le k$ be distinct integers with $1\le r\le2k$,
and put $v(n)=(\varphi(n+s_j)/2)_{j=1}^r$. There is an effective
absolute constant $C_0$ such that, for every prime $p$ and each $i$,
one can choose an integer

$$
k+2\le n_i\le \exp\bigl(C_0k\log(pk+2)\bigr),
\qquad v(n_i)\equiv-e_i\pmod p.
\tag{12}
$$

*Proof.* Choose a prime $4k<\ell<16k$ different from $p$.
Bertrand's postulate supplies primes in both $(4k,8k)$ and
$(8k,16k)$, so at least one is available. For $1\le j\le r$,
apply Linnik's theorem to

$$
q_j\equiv1\pmod{2p},\qquad q_j\equiv2k+j\pmod\ell.
$$

These classes are reduced. The primes $q_j$ are distinct, exceed
$2k$, differ from $\ell$, and satisfy
$q_j\le c(2p\ell)^L$. For a fixed $i$, prescribe a prime $t_i$ by

$$
t_i\equiv-1\pmod{2p},\qquad
t_i\equiv3k+1\pmod\ell,
\qquad
t_i\equiv s_i-s_j\pmod{q_j}\quad(j\ne i).
$$

The moduli are pairwise coprime. Each shift difference is nonzero
and has absolute value less than $2k<q_j$, so this is again a
reduced class. Its modulus is

$$
m_i=2p\ell\prod_{j\ne i}q_j,
\qquad
\log m_i=O\bigl(r\log(pk+2)\bigr).
$$

Linnik gives $t_i\le cm_i^L$. Its residue modulo $\ell$ also
gives $t_i\ge3k+1$. Set $n_i=t_i-s_i$; then
$n_i\ge2k+1\ge k+2$, with the bound in (12) after enlarging an
absolute constant. At coordinate $i$,
$\varphi(t_i)/2=(t_i-1)/2\equiv-1\pmod p$. At any other
coordinate, $q_j\mid n_i+s_j$, so
$q_j-1\mid\varphi(n_i+s_j)$ and $p\mid\varphi(n_i+s_j)/2$.
This proves (12), including $p=2$. $\square$

**Proposition 4 (effective endpoints and coefficients).** There is
an effective absolute constant $C$ such that for every $k\ge3$ the
central-zero interpolation system (1) on the parent page has an
integer solution supported on $k+2\le n\le R$ with

$$
R\le\exp\bigl(Ck^2\log(k+2)\bigr),\qquad
\sum_n|y_n|\le\exp\bigl(Ck^2\log(k+2)\bigr).
\tag{13}
$$

After enlarging $C$, its weighted cost and associated polynomial
multiplier, of degree $N$ and height $H$, consequently satisfy

$$
\Gamma_k\le C_k(y)\le\exp\bigl(Ck^2\log(k+2)\bigr),
\qquad HN^2\le\exp\bigl(Ck^2\log(k+2)\bigr).
\tag{14}
$$

*Proof.* Take the $r=2k$ shifts $-k+1,\ldots,0,1,\ldots,k$.
Proposition 2 gives full real row rank on a prefix ending at
$R_0=O(k^3\log(k+2))$. Choose $r$ independent columns from this
prefix and let $M_0$ be their square integer matrix. Put

$$
D=|\det M_0|\ge1,\qquad T_0=(R_0+k)/2.
$$

Every entry of $M_0$ has absolute value at most $T_0$.
Hadamard's inequality gives

$$
D\le(\sqrt r\,T_0)^r,\qquad \log D=O(k\log(k+2)).
\tag{15}
$$

For every prime $p\mid D$, adjoin the $r$ columns from Lemma 4a.
Since $p\le D$, all these columns occur before an endpoint
$R\le\exp(O(k^2\log(k+2)))$, enlarged to include $R_0$.
If $D=1$, no columns need be adjoined and take $R=R_0$.
The integer span of the selected columns is all of $\mathbb Z^r$:
its index divides $D$, while for each prime dividing $D$ the added
columns span all of $\mathbb F_p^r$.

It remains to bound the coefficients, not just the indices.
Write $t_s=0$ for $s\le0$ and $t_s=-\varphi(s)$ for $s>0$;
thus $\|t\|_\infty\le k$. The classes of the added columns
generate the group $G=\mathbb Z^r/M_0\mathbb Z^r$ of order $D$.
In its Cayley graph using these classes and their negatives, a
shortest path from zero to the class of $t$ has length at most
$D-1$. Therefore some integer coefficients $a_j$ on the added
columns $v_j$ satisfy

$$
\sum_j|a_j|\le D-1,\qquad
h=t-\sum_j a_jv_j\in M_0\mathbb Z^r.
$$

Put $T_1=(R+k)/2$ and
$A_0=(\sqrt{r-1}\,T_0)^{r-1}$. Every cofactor of $M_0$
has absolute value at most $A_0$, and
$\|h\|_\infty\le k+DT_1$. Hence the integer vector
$b=M_0^{-1}h$ satisfies

$$
\|b\|_1\le r^2A_0\left(\frac{k}{D}+T_1\right),
\qquad
\sum_n|y_n|\le D-1+r^2A_0\left(\frac{k}{D}+T_1\right).
\tag{16}
$$

Combine coefficients when a selected index occurs more than once;
this cannot increase the displayed bound. Now
$\log A_0=O(k\log(k+2))$ and
$\log(T_1+1)=O(k^2\log(k+2))$, proving (13). The complete-tail
cost obeys

$$
C_k(y)\le2(k+2)+(R+k+2)\sum_n|y_n|.
$$

For the polynomial $Q(x)=2x^N+\sum_n y_nx^{N-n}$, take
$N=\max\{n:y_n\ne0\}\le R$. Then
$H\le\max(2,\sum_n|y_n|)$. These facts give (14).
The normalized matrix equation is
$\sum_ny_n\varphi(n+s)/2=t_s$, exactly the central-zero system
after multiplication by two. $\square$

This makes qualitative solvability effective, but does not reach the
irrationality threshold. The bound in (14) divided by $2^k$ grows;
it gives no upper bound tending to zero for the actual minimum's ratio.
Nor is it a lower bound on that minimum.

The quantitative loss can be located in this construction. For a prime
dividing the seed determinant, the CRT modulus has $2k-1$ distinct
auxiliary primes, each larger than $2k$. Its logarithm is at least
$(2k-1)\log(2k)$, and the upper bound used here is
$O(k\log(pk+2))$. Applying a fixed-power least-prime bound to this
modulus therefore supplies no subexponential endpoint guarantee, even
when $p$ is fixed. Improving only Linnik's exponent would not give the
required estimate through these same bounds. A different construction
or a stronger estimate for these particular congruence classes remains
necessary; large moduli alone do not prove that their actual least
solutions, or other interpolation solutions, must be large.
