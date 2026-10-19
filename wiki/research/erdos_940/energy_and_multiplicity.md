---
name: research/erdos_940/energy_and_multiplicity
title: Energy, multiplicity, and the cubic quadric fibers
desc: Multiplicity criteria, exact prime scaling, and checked near-neighbor and square-class reductions; the critical cubic count remains open.
tags: []
sources: []
created: 2026-09-22T02:48:33Z
updated: 2026-10-13T05:28:09Z
---


# Energy, multiplicity, and the cubic quadric fibers

***

## Status

The identities, local estimates, and real-volume estimates below are proved.
They isolate sufficient targets for positive density, but no required global
multiplicity or averaged lattice-point bound has been established. The
bounded-ratio estimates and the obstructions to particular parametrizations
do not resolve the density question.

## The cross-coordinate correlation still needed

A direct attempt to keep the binary trace as well as its Eisenstein norm
does not yet close the density argument. For $F=x^3+y^3+cz^3$, $c\in\mathbb N$
fixed, define

$$
C_N(h)=\#\{(x,y,u,v)\in[1,N]^4:
x^3+y^3-u^3-v^3=h\}.
$$

The full box energy is exactly

$$
E_F(N)=N C_N(0)+
\sum_{\substack{1\le z,w\le N\\z\ne w}}
C_N\bigl(c(w^3-z^3)\bigr).
$$

The binary zero-difference term is controlled; the second term is not.
Writing $x^3+y^3=(x+y)(x^2-xy+y^2)$ keeps the trace constraint but
does not bound this shifted correlation. For norms of size $N^2$ with
small common divisor, reduced norm ratios can have height of order $N^2$.
Enumerating the binary quadruples and applying a divisor bound separately
to $w^3-z^3=h$ loses the required average factor of order $1/N$.
No estimate for the full sum, or a sufficient weaker rich-fiber bound,
was obtained. This identity names the remaining count; it is not a
replacement lemma that has been proved.

The zero-difference assertion has a precise form:

$$
C_N(0)=2N^2-N+O_\varepsilon(N^{4/3+\varepsilon}).
\tag{A}
$$

The main term counts the two permutations, with the diagonal corrected once. The
remaining points lie off the rational lines of $x^3+y^3-u^3-v^3=0$, so
[Heath-Brown, Theorem 1](../../../library/diophantine_problems/heath_brown_1997_density_rational_points_cubic_surfaces/_index.md)
applies. The nonsingularity, three coplanar rational lines, and precise
definition of the count off those lines have been checked in the supplied paper.
Thus the uncontrolled cross-coordinate sum would have to be $O_c(N^3)$ for this
energy route to succeed.

There is also an exact entropy formulation. Let $X,Y,Z$ be independent
uniform variables in $\{1,\ldots,N\}$, put $U=X^3+Y^3$ and
$T=U+cZ^3$, and use natural logarithms. Conditional on $T$, the input
is uniform in its fiber, so the chain rule gives

$$
\frac1{N^3}\sum_n R_N(n)\log R_N(n)
=H(Z\mid T)+H(X,Y\mid U).
\tag{B}
$$

Indeed $U$ is determined by $(Z,T)$ and $(X,Y)$ is independent of $Z$.
The binary conditional entropy satisfies

$$
H(X,Y\mid U)=\left(1-\frac1N\right)\log2
+O_\varepsilon(N^{-2/3+\varepsilon}).
\tag{C}
$$

For an input pair let $o=1$ if $X=Y$ and $o=2$ otherwise, and let
$b_N(U)$ be its full binary fiber size. Its excess logarithmic
multiplicity is $\log(b_N(U)/o)\le b_N(U)-o$. Summed over inputs,
the latter counts only nonpermutation binary collisions and is
$O_\varepsilon(N^{4/3+\varepsilon})$ by (A). The average of
$\log o$ is $(1-1/N)\log2$, proving (C).

Consequently, a bounded average logarithmic multiplicity here is equivalent
to a bound for $H(Z\mid T)$. Neither this conditional entropy nor a
weaker bound retaining enough bounded-fiber input mass has been controlled.
The trace--norm reformulation has not supplied the missing estimate.

## A weaker target than the complete second moment

### Inverting a cube difference is already almost unique

There is a precise limitation to replacing the inverse difference-of-cubes
map by a divisor estimate, even when seeking only logarithmic
multiplicity. Put

$$
D_N(h)=\#\{(z,w)\in[1,N]^2:z\ne w,\ w^3-z^3=h\}.
$$

The binary collision bound (A), with its two permutation families
removed, gives

$$
\sum_{h\ne0}D_N(h)(D_N(h)-1)
\ll_\varepsilon N^{4/3+\varepsilon}.                 \tag{D1}
$$

Indeed, equality of two nonzero differences is a binary sum-of-cubes
collision after rearrangement. One permutation family identifies the
two ordered pairs; the other would give zero differences.
Since $\log t\le t-1$ for $t\ge1$,

$$
\frac1{N(N-1)}\sum_{h\ne0}D_N(h)\log D_N(h)
\ll_\varepsilon N^{-2/3+\varepsilon}.                \tag{D2}
$$

Thus inverse difference multiplicity has vanishing average logarithm.

The usual divisor majorant behaves very differently. For a uniform
ordered pair $z\ne w$,

$$
\frac{\omega(|w^3-z^3|)}{\log\log N}\longrightarrow2
\quad\hbox{in probability}.                         \tag{D3}
$$

Here is a short proof. For primes $p>3$, the density of zeros of
$w^3-z^3$ modulo $p$ is

$$
\beta_p=
\begin{cases}
3/p-2/p^2,&p\equiv1\pmod3,\\
1/p,&p\equiv2\pmod3.
\end{cases}
$$

For $d=p$ or $pq$, CRT and residue-box counting give divisibility
probability

$$
\prod_{p\mid d}\beta_p+O(N^{-1}+dN^{-2}).             \tag{D4}
$$

The implicit constant is absolute for these one- and two-prime moduli.
Take $Z=N^{1/4}$ and sum the indicators for $p\le Z$.
The errors in their first and second moments tend to zero: the pair
error is $O(Z^2/N+Z^4/N^2)=o(1)$.
For example, Mertens' estimate and the
[fixed-conductor real-character bound](quadratic_prime_harmonics.md)
applied to the nonprincipal character modulo three give
$\sum_{p\le Z}\beta_p=2\log\log N+O(1)$, while
$\sum_p\beta_p^2<\infty$. Thus the mean and variance of this
small-prime count are both $2\log\log N+O(1)$.
Removing the diagonal $z=w$ changes these moments by $o(1)$,
since its contributions are at most $\pi(Z)/N$ and
$\pi(Z)^2/N$. There are at most twelve prime factors above $Z$
of a nonzero difference of size at most $N^3$.
Chebyshev's inequality proves (D3).

As $\tau(m)\ge2^{\omega(m)}$, it follows that on $1-o(1)$ of all
nonzero pairs,

$$
\log\tau(|w^3-z^3|)
\ge (2\log2-o(1))\log\log N.                         \tag{D5}
$$

The convergence persists under any restrictions retaining a fixed
positive proportion of pairs. Hence the logarithmic divisor majorant
still diverges on every such restriction, although the actual inverse
entropy in (D2) tends to zero.

This is not an estimate for the needed cross-coordinate incidence.
In particular, (D1) does not justify discarding its exceptional
differences after they are weighted by the other coordinates. The
uncontrolled all-nonzero contribution for a diagonal ternary cubic is

$$
\sum_{\substack{h_1h_2h_3\ne0\\
                a_1h_1+a_2h_2+a_3h_3=0}}
 D_N(h_1)D_N(h_2)D_N(h_3).
$$

Neither (D2) nor (D3) bounds that sum.

### The bounded-fiber and entropy criteria

Fix positive integer coefficients $a_1,\ldots,a_r$, and write


$$
F(\mathbf x)=\sum_{i=1}^r a_ix_i^r,\quad
R_N(n)=\#\{\mathbf x\in[1,N]^r:F(\mathbf x)=n\},\quad
V_N=F([1,N]^r).
$$


If $\mathbf X$ is uniform on $[1,N]^r$, then


$$
\mathbb E\frac1{R_N(F(\mathbf X))}
=\frac1{N^r}\sum_{n\in V_N}R_N(n)\frac1{R_N(n)}
=\frac{|V_N|}{N^r}.
\tag{1}
$$


Consequently the positive value set of $F$ has positive upper natural density if
and only if there are constants $K,c>0$ and arbitrarily large $N$ such that


$$
\#\{\mathbf x\in[1,N]^r:R_N(F(\mathbf x))\le K\}\ge cN^r.
\tag{2}
$$


Indeed, (2) makes (1) at least $c/K$. Conversely, if (1) is at least $\delta$,
choose $K\ge2/\delta$. The contribution from tuples over fibers larger than $K$
is at most $1/K$, so at least a $\delta/2$ fraction of tuples lie over fibers of
size at most $K$. To pass between box values and ordinary upper density, use
$F([1,N]^r)\subseteq[1,(\sum_i a_i)N^r]$, and the fact that every positive tuple
representing a value at most $X$ has all coordinates at most
$(X/\min_i a_i)^{1/r}$.

A sufficient, potentially weaker substitute for the usual energy bound is


$$
\frac1{N^r}\sum_n R_N(n)\log R_N(n)\le C
\tag{3}
$$


along an unbounded sequence. Jensen applied to $e^{-t}$ makes (1) at least
$e^{-C}$. In contrast, the full bound $\sum_nR_N(n)^2\ll N^r$ controls
$\mathbb E R_N(F(\mathbf X))$. Condition (3) is sufficient, not claimed
necessary. No unconditional proof of (2) or (3) for a suitable diagonal form was
obtained.

## Good-prime energy factors have no divergent product for $r\ge3$

Consider the collision form


$$
H(\mathbf x,\mathbf y)=\sum_{i=1}^r a_i(x_i^r-y_i^r).
$$


Let $p\nmid r\prod_i a_i$, and let $N_p$ count its zeros in $\mathbb F_p^{2r}$.
For


$$
S_i(b)=\sum_{x\bmod p}e_p(ba_ix^r),
$$


additive orthogonality gives the exact identity


$$
N_p=p^{2r-1}+\frac1p\sum_{b\ne0}\prod_{i=1}^r|S_i(b)|^2.
\tag{4}
$$


The multiplicative-character expansion and ordinary Gauss-sum bound yield
$|S_i(b)|\le(r-1)\sqrt p$ for $b\ne0$. Therefore


$$
0\le N_p-p^{2r-1}\le(r-1)^{2r}p^r.
\tag{5}
$$


Only the zero vector can be singular modulo $p$. Every other root lifts
nonsingularly. When all $2r$ coordinates are divisible by $p$, scaling the
variables contributes $p^{-2r}$ and scaling the degree-$r$ output contributes
$p^r$. Thus the limiting zero density is


$$
\sigma_p:=\lim_{k\to\infty}p^{-k(2r-1)}
\#\{H=0\pmod{p^k}\}
=\frac{N_p-1}{p^{2r-1}(1-p^{-r})}.
\tag{6}
$$


One can derive (6) by decomposing vectors according to their common $p$-adic
valuation; the contribution of valuation $j$ is $p^{-rj}(N_p-1)/p^{2r-1}$, and
the residual all-divisible part tends to zero.

Equations (5)–(6) imply


$$
\sigma_p=1+O_r(p^{1-r}).
\tag{7}
$$


The good-prime product is therefore convergent and positive for every $r\ge3$.
For cubes at $p\equiv2\pmod3$, the cubing map is bijective, so $N_p=p^5$
exactly. This local calculation removes a possible explanation for logarithmic
loss; it does not prove a global energy bound or control multiplicities at
individual integers.

## Cubic collisions as quaternary quadratic equations

For $r=3$, let $h_i=x_i-y_i$ and $u_i=x_i+y_i$. Apart from the diagonal
$\mathbf h=0$, write


$$
\mathbf h=t\mathbf k,\qquad t=\gcd(h_1,h_2,h_3)>0,
$$


where $\mathbf k$ is primitive and may have negative coordinates. The identity


$$
4(x_i^3-y_i^3)=h_i(3u_i^2+h_i^2)
$$


converts a collision into


$$
Q_{\mathbf k}(\mathbf u,t)
:=3\sum_{i=1}^3a_i k_i u_i^2
+t^2\sum_{i=1}^3a_i k_i^3=0.
\tag{8}
$$


There are also the parity conditions $u_i\equiv t k_i\pmod2$, and positivity
bounds inherited from $x_i,y_i$. With $K=\|\mathbf k\|_\infty$, one has
$u_i\ll N$ and $t\ll N/K$. When nonzero, the determinant squareclass of this
quadric is


$$
3a_1a_2a_3 k_1k_2k_3\left(\sum_i a_i k_i^3\right).
\tag{9}
$$


The coefficients and the right side of the associated ternary equation are tied
together; this is not a free coefficient average to which a uniform ternary
bound can be applied without further work.

### Coefficient choice cannot give this generic quadric a rational section

For arbitrary positive rational $a_i$, the generic projective quadric
over $K=\mathbb Q(h_1,h_2,h_3)$ associated with (8) is

$$
3\sum_i a_i h_i u_i^2+F(\mathbf h)w^2=0.
\tag{D}
$$

It has no $K$-point. A rational-function point could be specialized at
positive rational $h_i$, avoiding its finitely many denominators and
preserving a nonzero coordinate. Every coefficient in (D) would then
be positive, a contradiction.

Its determinant squareclass is
$3a_1a_2a_3h_1h_2h_3F(\mathbf h)$, and remains nonsquare over
$\overline{\mathbb Q}(\mathbf h)$. The smooth projective plane cubic
$F=0$ is geometrically irreducible, is distinct from each coordinate
line, and occurs with valuation one in that determinant. Thus changing
the nonzero coefficients cannot turn this generic quadric into a split
quadric or remove the cubic factor of its discriminant.

Over $K(\sqrt{-3})$ there is the explicit point $u_i=(\sqrt{-3}/3)h_i$, $w=1$.
The quadric then becomes rational by projection from a point, but is not split:
its determinant is still nonsquare. This recovers the setting of the
[Eisenstein parametrization](remaining_questions.md#an-eisenstein-height-counting-attempt),
not a way around its integral-height problem. The assertion concerns a generic
rational section; it does not exclude rational points in individual mixed-sign
fibers, whose average remains uncontrolled.

## Real volume is on the correct scale; lattice counts are not controlled

Fix $0<\delta<1$ and restrict all six original variables to $[\delta N,N]$. This
retains a fixed positive proportion of the possible positive triples. On the
corresponding real region, $u_i\ge2\delta N$. Choose $j$ with $|k_j|=K$. Then


$$
\left|\frac{\partial Q_{\mathbf k}}{\partial u_j}\right|
=6a_j|k_j|u_j\gg_{\delta,\mathbf a}KN.
$$


For fixed other coordinates there is at most one positive root in $u_j$.
Integrating the Dirac mass of $Q_{\mathbf k}$ in that coordinate, then over the
two remaining $u$ coordinates and over $t\ll N/K$, gives


$$
\int_{\text{physical region}}\delta_0(Q_{\mathbf k}(\mathbf u,t))\,d\mathbf u\,dt
\ll_{\delta,\mathbf a}\frac{N^2(N/K)}{KN}
=\frac{N^2}{K^2}.
\tag{10}
$$


There are $O(K^3)$ primitive directions in a dyadic shell. Summing (10) for
dyadic $K\ll N$ gives $O(N^3)$, without a logarithm.

However, the corresponding pointwise bound for integer points is false. With
equal coefficients and $k_1+k_2+k_3=0$, take cyclic permutation solutions
$\mathbf y=(x_2,x_3,x_1)$. For a fixed such direction and $t\ll N/K$, the
differences determine $\mathbf x$ up to a common translation. There are $\gg N$
admissible translations and $\gg N/K$ admissible $t$, giving $\gg N^2/K$ points
in that fiber when the ranges are nonempty. These permutation solutions
contribute only $O(N^3)$ in total, but they cannot be bounded pointwise by the
real volume.

**Unresolved step:** an averaged lattice-point estimate at the $O(N^3)$ scale,
separating these accumulating families and controlling the remaining fibers
uniformly. Equations (7) and (10) settle neither that estimate nor the weaker
multiplicity criterion (2). They show exactly why neither a divergent good-prime
product nor a real-volume logarithm supplies the missing argument.

## Distinct cube classes still have split positive fibers

One attempted remedy was to use


$$
F(x_1,x_2,x_3)=x_1^3+2x_2^3+4x_3^3.
$$


This form has no nonzero rational zero. Indeed, the valuations at $2$ of its
nonzero summands lie in distinct residue classes modulo three, so the minimum
valuation occurs uniquely. Consequently $C(\mathbf k)=k_1^3+2k_2^3+4k_3^3$ never
vanishes at a nonzero rational direction. Distinct coefficient cube classes also
remove ordinary coordinate-permutation identities.

They do **not**, however, remove all positive split fibers. There is the exact
identity


$$
\begin{aligned}
F(27m+92s,\ 212m+480s,\ 171m+515s)\\
=F(27m+12s,\ 212m+642s,\ 171m+391s).
\end{aligned}
\tag{11}
$$


All variables are positive for $m,s>0$. For a direct verification, put


$$
\mathbf k=(40,-81,62),\quad
\mathbf v=(27,212,171),\quad
\mathbf w=(104,1122,906),
$$


and $q_{\mathbf k}(\mathbf z)=40z_1^2-162z_2^2+248z_3^2$. Exact arithmetic gives


$$
C(\mathbf k)=-45570,\quad
q_{\mathbf k}(\mathbf v)=0,\quad
\sum_i a_i k_i v_iw_i=0,\quad
q_{\mathbf k}(\mathbf w)=60760.
$$


Therefore $Q_{\mathbf k}(\mathbf u,t)=3q_{\mathbf k}(\mathbf u)-45570t^2$
vanishes on the plane $(\mathbf u,t)=(2m\mathbf v+s\mathbf w,2s)$. Recovering
$\mathbf x=(\mathbf u+t\mathbf k)/2$ and $\mathbf y=(\mathbf u-t\mathbf k)/2$
proves (11). The squareclass expression is in fact a square:


$$
24 k_1k_2k_3 C(\mathbf k)=219698438400=468720^2.
$$


The identity and its three quadratic equalities were also checked by exact
symbolic expansion. This is a counterexample to global nonsplitting for these
coefficients, not evidence against an averaged $O(N^3)$ bound.

## Fixed diagonal points give genus-two direction curves

The same coefficient choice yields a more precise description of the rational
lines through a fixed diagonal point. Fix $\mathbf v\in\mathbb Q^3$ with
$v_1v_2v_3\ne0$ and set


$$
b_i=a_iv_i^3,\qquad \ell_i=a_iv_i^2k_i,
\qquad (a_1,a_2,a_3)=(1,2,4).
$$


A nondegenerate fiber $Q_{\mathbf k}$ contains $(\mathbf v,0)$ exactly when
$\sum_i\ell_i=0$. Given this rational point, it has rational ruling lines
exactly when its determinant is square: split off one hyperbolic plane; the
remaining binary form is hyperbolic precisely under this condition. Its
determinant squareclass is


$$
3\ell_1\ell_2\ell_3
\left(\frac{\ell_1^3}{b_1^2}+
\frac{\ell_2^3}{b_2^2}+
\frac{\ell_3^3}{b_3^2}\right).
$$


Putting $(\ell_1,\ell_2,\ell_3)=(s,t,-s-t)$ identifies these rational directions
with points on the double cover


$$
W^2=-3st(s+t)
\left(\frac{s^3}{b_1^2}+\frac{t^3}{b_2^2}
-\frac{(s+t)^3}{b_3^2}\right).
\tag{12}
$$


The binary sextic has six distinct projective roots. None of the roots of
$st(s+t)$ is a root of the cubic factor, because a coincidence requires
$b_i=\pm b_j$, contrary to the distinct rational cube classes of $1,2,4$. The
discriminant of the cubic factor is


$$
\frac{-27(b_1-b_2-b_3)(b_1-b_2+b_3)
(b_1+b_2-b_3)(b_1+b_2+b_3)}{(b_1b_2b_3)^4}.
\tag{13}
$$


Each numerator factor is nonzero: otherwise some signed choice of the $v_i$
would give a nonzero rational zero of $F$, which the valuation argument
excludes. Formula (13) follows by expanding the usual binary-cubic discriminant.

Thus the smooth projective curve (12) has genus two. By Faltings's theorem it
has finitely many rational points. For each fixed $\mathbf v$ with nonzero
coordinates, there are therefore only finitely many nondegenerate rational
ruling directions through the corresponding diagonal point. Each such direction
gives two lines, neither contained in $t=0$, whose intersection with the quadric
there is a nonsingular conic.

**Remaining gap.** There is no uniform bound for these directions as $\mathbf v$
varies, nor a bound for nonsplit fibers. Fixed-point finiteness does not control
the required growing-height average and supplies no bounded-multiplicity or
positive-density conclusion.

## Subsequent range estimates

The [controlled-range note](cubic_collision_ranges.md) now bounds
coordinate-zero differences, differences of size at most $N^{2/3-\eta}$, and
primitive directions of size at most $N^{1/2-\eta}$ by $O(N^3)$. It supplies the
full coefficient-uniform quadratic argument. For $(1,2,4)$, the remaining energy
problem is entirely in nonsingular fibers with larger primitive directions; in
particular, the shell $\|\mathbf k\|\asymp N$, $t=1$ has not been controlled.
This narrows the outstanding average without proving it.

The [cube-free-output note](cubefree_cubic_values.md) proves that a positive
proportion of inputs for $(1,2,4)$ have cube-free output, and that the average
logarithm of the output's cube part is bounded. However, the explicit split
identity (11) still supplies $\gg N^2$ positive primitive collisions with
cube-free output. A restricted energy or bounded-fiber theorem on that
positive-mass input set remains unproved; deleting common dilations does not
by itself remove the outstanding problem.

## Exact prime-scaling for geometric coefficient tuples

This is a proved, author-recorded normalization, not a multiplicity bound. For
any prime $p$ and integer $r\ge2$, set

$$
F_{p,r}(\mathbf x)=x_1^r+px_2^r+\cdots+p^{r-1}x_r^r,
\qquad
T(\mathbf x)=(px_r,x_1,\ldots,x_{r-1}).
$$

Then $F_{p,r}(T\mathbf x)=pF_{p,r}(\mathbf x)$ and $T^r=pI$. Conversely, if
$p\mid F_{p,r}(\mathbf x)$ for an integral tuple, reduction modulo $p$ forces
$p\mid x_1$. Hence

$$
T^{-1}(\mathbf x)=(x_2,\ldots,x_r,x_1/p)
$$

is integral, positive when $\mathbf x$ is positive, and has value
$F_{p,r}(\mathbf x)/p$. Thus, for the unrestricted positive representation
function $r_{p,r}(n)$, the two maps give a bijection proving

$$
r_{p,r}(pn)=r_{p,r}(n)\qquad(n\ge1).
\tag{14}
$$

In particular $r_F(2n)=r_F(n)$ for $F=x^3+2y^3+4z^3$. This identity is for
all positive representations of a target, not a fixed-box representation
function: the transformation changes the shape of a box.

Let $V(X)$ count distinct positive values of $F_{p,r}$ up to $X$, and $V^*(X)$
count those values not divisible by $p$. Equation (14) gives exactly

$$
V(X)=\sum_{j\ge0}V^*(X/p^j).
\tag{15}
$$

Consequently $V(X)=o(X)$ if and only if $V^*(X)=o(X)$. For the nontrivial
implication, truncate (15) at $j<J$; the tail is at most
$X p^{-J}/(1-p^{-1})$. First let $X\to\infty$, then $J\to\infty$.
Equivalently, positive upper density can be tested just on the $p$-free
targets. For the cubic candidate, this means odd targets. The identity does
not supply control on how many representations those odd targets have.

## A near-neighbor existence criterion

The following is a proved implication with an **unproved hypothesis**. It
records a possible way to avoid bounding all collision pairs, not a solution
of the density problem.

Fix $0<\delta<1$ and positive integer coefficients $a_1,a_2,a_3$. Put
$F(\mathbf x)=\sum_i a_ix_i^3$ and
$\mathcal B_N=[\delta N,N]^3\cap\mathbb Z^3$. Write $R_N^\delta(n)$ for the
number of representations of $n$ in $\mathcal B_N$. Let $B_N(\varepsilon)$
count the points $\mathbf x\in\mathcal B_N$ for which there exists
$\mathbf y\in\mathcal B_N\setminus\{\mathbf x\}$ satisfying

$$
F(\mathbf y)=F(\mathbf x),\qquad
\|\mathbf y-\mathbf x\|_2\le\varepsilon N.
$$

Each input is counted only once, regardless of how many neighbors it has.
If

$$
\lim_{\varepsilon\downarrow0}\limsup_{N\to\infty}
\frac{B_N(\varepsilon)}{N^3}=0,
\tag{16}
$$

then the positive value set of $F$ has positive lower density.

To prove this implication, each level surface in the box is a graph

$$
x_3=\left((n-a_1x_1^3-a_2x_2^3)/a_3\right)^{1/3}.
$$

For any two points of the graph lying in the box, the difference-of-cubes
formula gives a Lipschitz bound for this projection inverse, with constant
depending only on $\delta$ and the coefficients. For example,

$$
|x_3-y_3|\le\frac{a_1|x_1-y_1|+a_2|x_2-y_2|}{a_3\delta^2}.
$$

Thus points that are mutually more than $h$ apart have projections separated
by more than $h/L$, where $L$ is fixed. Packing in $[\delta N,N]^2$ bounds
their number by $C(1+N/h)^2$.

Choose a constant $A$ sufficiently large, depending only on this packing
constant. For all sufficiently large fixed $K$, put $h=AN/\sqrt K$. In a
fiber of size $R>K$, at most $K/2$ points can have no other fiber point within
distance $h$: these isolated points are mutually $h$-separated. At least
$R/2$ points therefore have a neighbor within $h$. Summing over such fibers,

$$
\#\{\mathbf x\in\mathcal B_N:R_N^\delta(F(\mathbf x))>K\}
\le2B_N(A/\sqrt K).
\tag{17}
$$

Under (16), choose a fixed $K$ making the limsup on the right less than half
the asymptotic input mass $(1-\delta)^3N^3$. Then $\gg N^3$ inputs lie in
fibers of size at most $K$, yielding $\gg N^3$ distinct values below
$(a_1+a_2+a_3)N^3$, for every sufficiently large $N$. This proves the claimed
positive lower density.

For pairs with all three coordinate differences nonzero, the
[existing short-difference estimate](cubic_collision_ranges.md) bounds their
number by $O_{\mathbf a,\eta}(N^{1+\eta}H^3)$. The later
[coordinate-zero refinement](cubic_collision_ranges.md) proves that inputs with
a coordinate-sharing near neighbor are $O_{\mathbf a}(\varepsilon N^3)+o(N^3)$,
so their contribution does vanish in the iterated limit in (16). For $(1,2,4)$
even unrestricted off-diagonal coordinate-sharing collisions have a power
saving. The all-nonzero-difference estimate still does not establish (16): the
needed scale is $H=\varepsilon N$ with fixed $\varepsilon$, not
$H\ll N^{2/3-\eta}$. No estimate for the near-neighbor existence count at that
scale has been proved. Bounding all short collision pairs at the $O(N^3)$ scale
would return to the stronger full pair-energy problem in the interior box:
partition it into a fixed number $L=O_\varepsilon(1)$ of smaller boxes of
diameter at most $\varepsilon N$. Cauchy--Schwarz bounds the total energy by $L$
times the sum of their within-box energies, hence by $L$ times the short-pair
energy. The possible advantage in (16) is precisely that it only counts
existence.

### What the available packing estimate actually yields

For $F=x^3+2y^3+4z^3$, combining (17) with the two checked
[short-difference and coordinate-sharing bounds](cubic_collision_ranges.md)
gives, for every fixed $\eta>0$ and all sufficiently large $K$,

$$
\#\{\mathbf x\in\mathcal B_N:R_N^\delta(F(\mathbf x))>K\}
\ll_{\delta,\eta}
N^{4+\eta}K^{-3/2}+N^{1+\sqrt3}(1+\log N)^4.          \tag{17a}
$$

Indeed, in the all-nonzero-difference bound substitute
$H=AN/\sqrt K$, increasing the fixed lower threshold for $K$ so
$H\le N$. The coordinate-sharing contribution is bounded by the
unrestricted off-diagonal count. If $K>N^2$ the left side is zero,
so no smaller-distance convention is needed.

After division by $N^3$, the first term in (17a) still grows for
fixed $K$. It becomes useful only for polynomially growing $K$.
Thus this combination of pointwise quadratic counting and packing
does not prove (16) or bounded average logarithmic multiplicity.
This identifies the loss in the attempted estimate; it does not
exclude a sharper bound for neighbor existence.

## Separated prime-adic coefficients do not give coordinatewise injectivity

This checked obstruction comes from Section 9 of the
[independent record](independent/canonical_decomposition_and_quartic_zero_target.md).
It concerns a proposed congruence proof of injectivity, not the existence of
integral collisions in a growing box.

Let $p\nmid r$ and let two coefficients be $p^{e_0}u_0$ and $p^{e_1}u_1$,
where $u_0,u_1\in\mathbb Z_p^\times$ and $e_1>e_0$. Set all $y_i=1$,
and all but these two $x_i$ equal to $1$. The collision equation becomes

$$
x_0^r=1-p^{e_1-e_0}(u_1/u_0)(x_1^r-1).
$$

For every $x_1\in\mathbb Z_p$, the right side is $1\pmod p$. Hensel's
lemma supplies a unique $x_0\in1+p\mathbb Z_p$. Factoring $x_0^r-1$ shows
that, when $x_1^r-1$ is a unit,

$$
v_p(x_0-1)=e_1-e_0.
$$

For example, take $x_1=p$. A change in the higher-weight coordinate can
therefore be canceled by a sufficiently deep change in the lower-weight
coordinate, however large the fixed exponent spacing. It is invalid to
infer coordinatewise equality by recursively reducing such collision
equations modulo $p$.

These solutions are $p$-adic; they are not asserted to be positive integral
solutions or to lie in any prescribed box. The argument does not refute a
global energy estimate. It also does not conflict with the exact
prime-scaling identity (14), whose reduction modulo $p$ concerns divisibility
of one represented value rather than subtraction of two representations.

## The prime-geometric digit argument leaves a critical carry map

The following exact formulation records why a subsequent digit/entropy
attempt did not establish positive density. Put $F=x^3+2y^3+4z^3$ and
$N=2^k$, $k\ge1$. For each odd $a\in[1,N)$ and each
$(y,z)\in[1,N]^2$, there is exactly one odd $x\in[1,N]$ with

$$
F(x,y,z)\equiv a\pmod N.
$$

Indeed $a-2y^3-4z^3$ is odd and cubing permutes the odd residues modulo
$2^k$. Define

$$
C_{a,k}(y,z)=\frac{F(x,y,z)-a}{N}.
$$

This maps exactly $N^2$ input pairs into the integers in $[0,7N^2]$.
Its fiber at $c$ has size exactly $R_N(a+Nc)$, the original cubic
box-representation count. Low-digit uniformity has therefore only separated
the odd-output problem into critical maps with $N^2$ inputs and $O(N^2)$
possible carries.

If $s_{a,k}(c)$ denotes that fiber size, a bound

$$
\sum_{\substack{1\le a<N\\a\text{ odd}}}\sum_c
s_{a,k}(c)\log s_{a,k}(c)\ll N^3
$$

would imply positive upper density by the logarithmic criterion above,
applied to the $N^3/2$ odd-output inputs. In entropy language, with natural
logarithms and uniform $(y,z)$, the exact identity is

$$
H(C_{a,k})=2\log N-
\frac1{N^2}\sum_c s_{a,k}(c)\log s_{a,k}(c).
$$

The missing estimate is a bounded average entropy deficit for the carries.
Neither Hensel lifting nor $r_F(2n)=r_F(n)$ controls it. Successive digit
steps retain growing polynomial carries rather than a proved finite-state
recursion. No bounded-fiber or logarithmic-moment estimate was obtained.

The subsequent [carry-spectrum calculation](cubic_carry_spectrum.md) gives
the exact dyadic lift and proves that primitive high-conductor carry
characters need not decay: an odd-modulus resonance survives at every
dyadic scale. Thus contracting all such modes is not a valid way to close
the entropy estimate.

The [primitive-fiber note](primitive_cubic_fibers.md) proves that common
dilations cost only bounded entropy, removes low-height projected planes
from the logarithmic moment, and excludes rational lines and conics on
individual output surfaces for $(1,2,4)$. None of these statements controls
the remaining primitive high multiplicity.

## Nearest-neighbor secants need not decrease height

There is an exact normalization for this approach. For a collision
$F(x)=F(x+t k)=n$, with primitive integral $k$, put
$C=F(k)$, $B=\sum_i a_i x_i k_i^2$, and
$A=\sum_i a_i x_i^2k_i$. Assume $C\ne0$, as always holds for the
special form. Expansion gives $3A+3tB+t^2C=0$, and the third secant point is

$$
[C(x-tk)-3Bk:C].
$$

Its integer content is exactly $g=\gcd(C,3B)$: reducing the first three
coordinates modulo $C$ gives $-3Bk_i$, and $k$ is primitive. Thus
$g\mid3A$ as well. The polynomial identity

$$
n k_1k_2k_3
=A\sum_i x_i k_jk_\ell
 -B\sum_i x_jx_\ell k_i+C x_1x_2x_3,
$$

where $\{i,j,\ell\}=\{1,2,3\}$ in each summand, gives
$g\mid3n k_1k_2k_3$. One can verify the identity by applying the cubic
equation with roots $x_i/k_i$ to each root and summing with weights
$a_i k_i^3$; clearing denominators makes it valid also when some $k_i=0$.
These divisibilities alone supply no useful height decrease.

The following checked family defeats a proposed universal descent, not the
near-neighbor existence criterion. Take positive integers $u_j,v_j$ defined by

$$
2v_j+u_j\sqrt{34}=(6+\sqrt{34})(35+6\sqrt{34})^j.
$$

They satisfy $2v_j^2-17u_j^2=1$, tend to infinity, and
$v_j/u_j\to\sqrt{17/2}$. For $j\ge1$, set

$$
P_j=(u_j-1,v_j+1,2u_j-1),\qquad
Q_j=(u_j+1,v_j-1,2u_j+1).
$$

These positive points lie in a fixed interior cone and satisfy

$$
F(P_j)=F(Q_j),\qquad Q_j-P_j=(2,-2,2),
\quad F=x^3+2y^3+4z^3.
$$

For example, with $U=(u,v,2u)$ and $k=(1,-1,1)$,
$F(U+k)-F(U-k)=6(17u^2-2v^2)+6=0$.

Their third secant point on $F=n$, where $n=F(P_j)$, is integral:

$$
T_j=(-8u_j-2v_j,\ 9u_j+3v_j,\ -7u_j-2v_j).
$$

Direct substitution in the cubic on the line gives this formula.
In projective coordinates its last coordinate is one, so its primitive
height is $9u_j+3v_j$. With $N_j=v_j+1$, the maximum endpoint coordinate,

$$
H(T_j)/N_j\longrightarrow3+9\sqrt{2/17}>6.                \tag{18}
$$


Moreover $P_j,Q_j$ are eventually reciprocal unique nearest integer
neighbors on their level surface. To check this, fix $h=(a,b,c)\in\mathbb Z^3$.
After replacing $v_j^2$ by $(17u_j^2+1)/2$, the difference
$F(P_j+h)-F(P_j)$ has $u_j^2,u_j,v_j$ coefficients

$$
3(a+17b+16c),\quad
3(a^2-2a+8c^2-16c),\quad 6b(b+2),
$$

respectively, and a constant term. If it vanished for infinitely many
$j$, division first by $u_j^2$ and then by $u_j$ would force these three
coefficients to be zero, since $\sqrt{17/2}$ is irrational. Thus $b=0$
or $-2$. For $b=0$ one gets $a=-16c$ and $c(33c+2)=0$, hence $h=0$.
For $b=-2$, one gets $a=34-16c$ and
$33c^2-134c+136=0$, whose only integral root is $c=2$; hence
$h=(2,-2,2)$. Both differences also annihilate the constant term.

Every other bounded integer difference therefore occurs only finitely
often. A finite union proves that, for every fixed radius, eventually
there are no other equal-output points in that neighborhood of either
endpoint. In particular nearest-neighbor selection does not repair the
height increase in (18). This is a sparse fixed-direction family already
covered by the controlled-range estimates; it does not obstruct a
statistical descent that discards a negligible set of inputs.

## A binary norm majorant cannot be bounded on positive input mass

This is a limitation of one factorization argument for an equal-coefficient
binary subsum. It is not a bound for actual cubic multiplicity, and does
not exclude a factorization method that retains the trace condition.

Put

$$
Q(x,y)=x^2-xy+y^2,
\qquad \omega_1(m)=\#\{p\mid m:p\equiv1\pmod3\}.
$$

For a uniform pair $(x,y)\in[1,N]^2\cap\mathbb Z^2$,

$$
\frac{\omega_1(Q(x,y))}{\log\log N}\longrightarrow1
\quad\text{in probability}.                             \tag{19}
$$


Here is the second-moment proof. Set $Z=N^{1/4}$ and sum the indicators
$1_{p\mid Q(x,y)}$ over $p\le Z$, $p\equiv1\pmod3$, obtaining $T$.
Over $\mathbb F_p$, $Q=0$ is the union of two distinct lines, so its
root count is $2p-1$ and its normalized density is
$\beta_p=2/p-1/p^2$. For $d=p$ or $pq$ with distinct such primes,
CRT gives a root count $\varrho(d)\le4d$, and residue-box counting gives

$$
\Pr(d\mid Q)=\frac{\varrho(d)}{d^2}
+O(1/N+d/N^2).                                         \tag{20}
$$

The summed single-prime errors are $O(Z/N+Z^2/N^2)$; the summed
two-prime errors are $O(Z^2/N+Z^4/N^2)=o(1)$. The products of
single-prime errors also have total $o(1)$, even after multiplication
by $\sum\beta_p=O(\log\log N)$. The classical Mertens theorem in
arithmetic progressions therefore yields

$$
\mathbb ET=\log\log N+O(1),\qquad
\operatorname{Var}T=\log\log N+O(1).
$$

Chebyshev's inequality proves concentration. Since $Q(x,y)\le N^2$,
at most eight prime divisors exceed $Z$. This proves (19).

Unique factorization in the Eisenstein integers gives, for every
positive integer $m$ represented by $Q$,

$$
r_Q(m):=\#\{(u,v)\in\mathbb Z^2:Q(u,v)=m\}
=6\prod_{p\equiv1\ (3)}(v_p(m)+1)
\ge6\,2^{\omega_1(m)}.                                 \tag{21}
$$

Indeed the six units give the factor six. A split prime of exponent
$e$ can be distributed between its two conjugate prime factors in
$e+1$ ways; an inert prime must have even exponent and contributes one
choice, and the ramified prime contributes one choice.
Equations (19)--(21) show that, on $1-o(1)$ of the input pairs,

$$
\log r_Q(Q(x,y))\ge(\log2-o(1))\log\log N.              \tag{22}
$$

Every restriction retaining a fixed positive proportion of pairs
therefore still has divergent average logarithmic **norm** multiplicity.
The same holds for positive-mass subsets of triples $(x,y,z)$, since
the exceptional pair set times $[1,N]$ has size $o(N^3)$. In particular,
a bounded norm-divisor sieve cannot retain positive input mass.

For the actual cubic $x^3+y^3+cz^3=n$, write $s=x+y$ and $d=x-y$.
The exact factorization requires

$$
4(n-cz^3)=s^3+3sd^2,
\qquad
s\mid n-cz^3,\quad
\frac{4(n-cz^3)/s-s^2}{3}=d^2,                           \tag{23}
$$

with the parity and positivity restrictions on $s,d$. For fixed trace
$s$ and norm $Q(x,y)$ there are at most two pairs $(x,y)$. It is this
compatibility, not the full Eisenstein norm count, that eliminates the
spurious multiplicity in (22). No estimate sufficient for positive
density was obtained while retaining (23).

## A square-class reformulation retains the unknown collision mass

Fix positive integers $a_1,a_2,a_3$, $0<\eta<1$, and $N\ge2$.
Let $\mathcal H=[\eta N,N]\cap\mathbb Z$, and define

$$
b_N(D)=\#\left\{(x_1,y_1,x_2,y_2)\in[1,N]^4\cap\mathbb Z^4:
4\sum_{i=1}^2a_i(x_i^3-y_i^3)=D\right\},
$$


$$
A_N(n)=\sum_{h\in\mathcal H}
b_N\bigl(-a_3h(h^2+n)\bigr),\qquad 1\le n\le12N^2.
$$

For a cubic collision with $h=x_3-y_3\in\mathcal H$ and
$u=x_3+y_3$, the identity

$$
4a_3(x_3^3-y_3^3)=a_3h(h^2+3u^2)
$$

shows that its count is at most

$$
T_N=\sum_{1\le u\le2N}A_N(3u^2).                     \tag{24}
$$

The omitted parity and endpoint conditions only enlarge this count;
given $h,u$, the two third coordinates are uniquely determined.

Two elementary estimates explain the appeal of this reformulation.
For every $\varepsilon>0$,

$$
\sum_n A_N(n)\ll_{\mathbf a,\varepsilon}N^{4+\varepsilon},
\qquad
\sum_n A_N(n)^2
\ll_{\mathbf a,\varepsilon}N^{1+\varepsilon}
\int_0^1|f_N(\alpha)|^8\,d\alpha,                     \tag{25}
$$

where $f_N(\alpha)=\sum_{x=1}^N e(\alpha x^3)$.
Every occurring $D=-a_3h(h^2+n)$ is nonzero and has
$|D|\ll_{\mathbf a}N^3$ when $b_N(D)\ne0$.
Its possible $h$ are divisors of $|D|$, hence number
$O_{\mathbf a,\varepsilon}(N^\varepsilon)$; $D,h$ determine $n$.
Since $\sum_D b_N(D)=N^4$, this proves the first estimate.
Cauchy--Schwarz in $h$ proves

$$
\sum_n A_N(n)^2\ll N^{1+\varepsilon}\sum_D b_N(D)^2.
$$

Finally, orthogonality and Cauchy--Schwarz give

$$
\sum_D b_N(D)^2
=\int_0^1|f_N(4a_1\alpha)|^4|f_N(4a_2\alpha)|^4\,d\alpha
\le\int_0^1|f_N(\alpha)|^8\,d\alpha.
$$

In particular, inserting an eighth-moment bound
$\int|f_N|^8\ll_\varepsilon N^{5+\varepsilon}$ yields, after
renaming $\varepsilon$,
$\sum_n A_N(n)^2\ll_{\mathbf a,\varepsilon}N^{6+\varepsilon}$.
No improvement of that moment is being asserted here.

The square sieve would have to detect that $3n$ is a square.
Writing $n=dv^2$, with $d$ squarefree, gives the masses

$$
B_N(d)=\sum_{v\ge1:\,dv^2\le12N^2}A_N(dv^2),
\qquad B_N(3)=T_N.                                   \tag{26}
$$

For sieve primes greater than $4N$, all these $v$ are coprime
to the primes. Thus quadratic-character grouping is exact, and the
$d=3$ contribution has character value $1$. A quadratic large-sieve
bound using the grouped coefficient norm encounters
$\sum_d B_N(d)^2\ge T_N^2$. It cannot be estimated from
$\sum_n A_N(n)^2$ by pretending that all the $n$ are squarefree.
For smaller sieve primes one must also keep the coprimality factors;
discarding them does not justify that replacement.

Even the bounds $\sum A_N\ll N^4$ and $\sum A_N^2\ll N^6$
alone would not control (24) by $O(N^3)$. On $1\le n\le N^2$,
the abstract nonnegative weights

$$
a(n)=N^2+N^{5/2}\mathbf1_{\{n=3v^2\text{ for some }v\ge1\}}
$$

extended by zero up to $12N^2$, have these two bounds, but their
$3$-square-class mass is
$\asymp N^{7/2}$. These weights are not claimed to arise from
cubic differences. They show exactly why the two moment bounds and
the proposed ungrouped large-sieve step do not prove the desired
collision estimate. A bound exploiting the actual square-class
concentration or a new joint character correlation remains unproved.
