---
name: research/erdos_774/routes/axis_line_extraction
title: Uniform extraction from axis lines with linearly growing sides
desc: Target-independent root-polygon rounding gives a direct uniform Sidon estimate for full axis-line indicators, including sides d_i=i+2; this does not inherit extraction from a full simplex tensor or prove unbounded coloring.
tags: [E0774, proved, construction, extraction, incomplete]
sources: []
created: 2026-09-18T18:54:49Z
updated: 2026-09-18T18:54:49Z
---


# Uniform extraction from axis lines with linearly growing sides

***

## Theorem and scope

For integers $d_i\geq3$, put
$$
X_t=\prod_{i=1}^t[d_i],\qquad N_t=|X_t|,
$$
and let $L_t\subset\mathbb Z^{X_t}$ consist of the indicator vectors
of all full axis-parallel lines. Thus an $i$-line has $d_i$ entries
equal to one. Different lines give distinct, nonzero, non-antipodal vectors.

Write $\rho(L_t)$ for the positive-real Sidon parameter: for every
complex coefficient family $(c_\ell)_{\ell\in L_t}$,
$$
\max_{z\in\mathbb T^{X_t}}
\operatorname{Re}\sum_{\ell\in L_t}c_\ell\prod_{x\in\ell}z_x
\ \geq\ \rho(L_t)\sum_{\ell\in L_t}|c_\ell|.
\tag{1}
$$

The direct finite estimate is
$$
\boxed{\displaystyle
\rho(L_t)\geq
\min_{1\leq i\leq t}
\prod_{j=i+1}^t\cos(\pi/d_j)^{d_i}.}
\tag{2}
$$
In particular, if
$$
M=\sup_{i\geq1}d_i\sum_{j>i}d_j^{-2}<\infty,
\tag{3}
$$
then every $L_t$ has positive-real Sidon parameter at least
$2^{-9M}$, and there is **one** $\delta>0$ such that every
subset of every $L_t$ contains a dissociated subset of relative size
at least $\delta$.

This includes the dense linear schedule $d_i=i+2$, with $M\leq1$.
A sharper elementary estimate below gives
$\rho(L_t)\geq\exp(-\pi^2/2)$. More generally, for
$d_i=a+b(i-1)$, integers $a\geq3,b\geq1$, one has
$M\leq1/b$ and $\rho(L_t)\geq\exp(-\pi^2/(2b))$.

This is a new direct estimate for the **line subfamily**. It does not assert
proportional dissociation of the full simplex tensors at a linear schedule,
which the [full-tensor entropy obstruction](tensor_schedule_constraints.md)
rules out. It also does **not** prove that the coloring numbers $\chi_1(L_t)$
are unbounded. The proof below is self-contained until its final application of
the supplied Pisier theorem. Independent internal review checked the finite
induction, constants, embeddings, and exact Pisier hypotheses; no defect was
found.

## 1. A target-independent root-polygon rounding lemma

For every integer $d\geq3$ and $u\in\mathbb T$, there is a
finite random variable $Y\in\mathbb T$ satisfying
$$
Y^d=u\quad\hbox{surely},\qquad
\mathbb EY=a_d:=\cos(\pi/d)>0.
\tag{4}
$$
Indeed the $d$-th roots of $u$ are the vertices of a rotated
regular $d$-gon. Its convex hull contains the closed disk centered at
zero of radius $\cos(\pi/d)$. The positive real number $a_d$
therefore is a convex combination of those vertices. Use the combination's
weights as probabilities.

The distribution may depend on $u$, but its expectation does not.
Independent copies of (4), with possibly different prescribed targets,
therefore satisfy
$$
\mathbb E\prod_{x\in F}Y_x=a_d^{|F|}
\tag{5}
$$
for every finite set $F$ of distinct indices. No uniform choice of the
whole distribution, and no measurable choice in the target, is required:
only finitely many targets occur in a given step.

## 2. Directional induction

For a polynomial on $L_t$, denote its total coefficient magnitude in
direction $i$ by $W_i$. We prove the stronger directional assertion
$$
\max_z\operatorname{Re}P(z)
\geq\sum_{i=1}^t r_{i,t}W_i,
\qquad
r_{i,t}=\prod_{j=i+1}^t a_{d_j}^{d_i}.
\tag{6}
$$
For $t=1$, the family has a single line, whose character can be assigned
any unit value, so $r_{1,1}=1$ works.

Suppose the assertion holds through $t-1$, and put $d=d_t$.
Decompose the point variables into layers
$z^{(s)}=(z_{x,s})_{x\in X_{t-1}}$, $s\in[d]$.
An arbitrary polynomial on $L_t$ has the form
$$
P(z)=\sum_{s=1}^d P_s(z^{(s)})
       +\sum_{x\in X_{t-1}}b_x\prod_{s=1}^d z_{x,s},
\tag{7}
$$
where each $P_s$ uses precisely the old line directions.

In each $P_s$, multiply every direction-$i$ coefficient by
$a_d^{d_i}$, obtaining $\widetilde P_s$. Choose the layers
$z^{(s)}$ independently using the induction hypothesis for these
**rescaled** polynomials. Their total real value satisfies
$$
\sum_s\operatorname{Re}\widetilde P_s(z^{(s)})
\geq\sum_{i<t}r_{i,t-1}a_d^{d_i}W_i.
\tag{8}
$$
All layer choices are now fixed.

For each $x$, if $b_x\ne0$, prescribe
$$
u_x=
\frac{\overline b_x}{|b_x|}
\left(\prod_s z_{x,s}\right)^{-1};
\tag{9}
$$
if $b_x=0$, choose any $u_x\in\mathbb T$. Choose independent
random variables $Y_x$ from (4), with targets $u_x$, and replace
every layer coordinate by
$$
z'_{x,s}=z_{x,s}Y_x.
\tag{10}
$$
Every new-axis term then equals $|b_x|$ deterministically, since
$Y_x^d=u_x$. An old $i$-line character, in any layer, is multiplied
by the product of $Y_x$ over its $d_i$ distinct base points.
By (5), its expected multiplier is exactly $a_d^{d_i}$. Consequently
$$
\begin{aligned}
\mathbb E\operatorname{Re}P(z')
&=\sum_s\operatorname{Re}\widetilde P_s(z^{(s)})+W_t\\
&\geq\sum_{i<t}r_{i,t-1}a_d^{d_i}W_i+W_t.
\end{aligned}
\tag{11}
$$
The random choice has finite support, so one outcome attains at least this
expectation. This proves (6), with
$r_{i,t}=r_{i,t-1}a_{d_t}^{d_i}$ and $r_{t,t}=1$, hence (2).

Rescaling before optimization is essential: no sign or phase of an old
individual term is assumed favorable. The target-dependent distributions
are selected only after the old layers are fixed. Independence is required
across base points, not across layers; the same $Y_x$ is deliberately
used in all layers so that (9) is solved exactly.

## 3. Uniform constants and dense schedules

For $d\geq3$,
$$
-\log\cos(\pi/d)\leq\frac{9\log2}{d^2}.
\tag{12}
$$
One elementary proof observes that
$F(x)=-\log\cos x\,/x^2$ is nondecreasing on $(0,\pi/3]$.
The sign of its derivative is the sign of
$h(x)=x\tan x+2\log\cos x$. Here $h(0)=0$, and
$$
h'(x)=x\sec^2x-\tan x
      =\frac{x-\sin x\cos x}{\cos^2x}\geq0.
$$
Thus $F(x)\leq F(\pi/3)=9\log2/\pi^2$, giving (12).
Combining (12) with (3) gives
$$
r_{i,t}\geq
\exp\left(-9\log2\,d_i\sum_{j>i}d_j^{-2}\right)
\geq2^{-9M}.
\tag{13}
$$

For the arithmetic schedule $d_i=a+b(i-1)$, monotonicity and an
integral comparison give
$$
\sum_{j>i}d_j^{-2}
\leq\int_0^\infty(d_i+bu)^{-2}\,du
=\frac1{bd_i}.
\tag{14}
$$
For these increasing arithmetic schedules, improve (12) to
$$
-\log\cos(\pi/n)\leq\frac{\pi^2}{2n(n-1)},\qquad n\geq4.
\tag{14a}
$$
For $n\geq5$, set $u=\pi^2/(2n^2)$. The elementary inequalities
$\cos(\pi/n)\geq1-u$ and
$-\log(1-u)\leq u/(1-u)$ show that the left side of (14a) is at
most $\pi^2/(2n^2-\pi^2)$, which is at most its right side because
$\pi^2<10\leq2n$. For $n=4$, the left side is
$(\log2)/2<3/8<\pi^2/24$, using $\log2<3/4$ and $\pi>3$.
Every future side $d_j$, $j>i$, is at least four, and
$$
\begin{aligned}
d_i\sum_{j=i+1}^t-\log\cos(\pi/d_j)
&\leq\frac{\pi^2d_i}{2}
       \sum_{j=i+1}^t\frac1{d_jd_{j-1}}\\
&=\frac{\pi^2d_i}{2b}
       \left(\frac1{d_i}-\frac1{d_t}\right)
\leq\frac{\pi^2}{2b}.
\end{aligned}
\tag{14b}
$$
Here $d_j-1\geq d_{j-1}$, so (14a) justifies the first inequality.
Consequently:

- $d_i=i+2$ has $\rho(L_t)\geq\exp(-\pi^2/2)$.
- $d_i=10i$ has $\rho(L_t)\geq\exp(-\pi^2/20)$.
- A dyadic block schedule in which side $2^m$ is repeated $2^m$
  times, for $m\geq2$, has $M\leq2$: from any point in its block,
  the remaining same-block contribution to $d_i\sum_{j>i}d_j^{-2}$
  is less than one, and all later blocks contribute exactly one. Hence it
  has the uniform bound $\rho(L_t)\geq2^{-18}$.

The number of columns is
$$
|L_t|=N_t\sum_{i\leq t}\frac1{d_i},
\tag{15}
$$
so the arithmetic and displayed repeated-dyadic schedules have an unbounded
line-to-point ratio. Equation (15) alone is not a chromatic lower bound:
dissociated classes may have rational dependencies.

## 4. Independent additive-loss version

There is also a simpler, weaker directional estimate
$$
\rho(L_t)\geq
\min_{i\leq t}\left(1-
\frac{\pi^2d_i}{2}\sum_{j=i+1}^t d_j^{-2}\right).
\tag{16}
$$
For each prescribed target $u_x=e^{i\theta_x}$, choose a finite
random real lift $X_x$ with $e^{iX_x}=u_x$, mean zero, and
$\mathbb EX_x^2\leq\pi^2$: take the two adjacent lifts surrounding
zero with their mean-zero probabilities. Use independent lifts across base
points. Replace all $z_{x,s}$ by $z_{x,s}e^{iX_x/d}$.
New terms again align exactly, while the phase correction on an old
$i$-line has mean zero and variance at most $\pi^2d_i/d^2$.
The inequality
$$
\operatorname{Re}(we^{iv})
\geq\operatorname{Re}w-v\operatorname{Im}w-\tfrac12|w|v^2
$$
therefore bounds its expected loss by
$\pi^2d_i|w|/(2d^2)$. This time optimize the unscaled old layer
polynomials and induct with an additive loss for each direction, yielding
(16). For $d_i=10i$, it gives the independent explicit bound
$\rho(L_t)\geq1-\pi^2/20>1/2$.

The multiplicative root-polygon argument is stronger because its expectation
is exactly real and target-independent; unlike the accumulated additive
estimate, it remains positive for $d_i=i+2$.

## 5. One full-dissociation extraction constant

Embed $H_t=\mathbb Z^{X_t}$ into $H_{t+1}$ by
$e_x\mapsto e_{(x,1)}$. This is a primitive direct-summand embedding,
and takes every old axis line to a line in the fixed new-coordinate slice.
Consequently the $L_t$ are nested in the direct-limit free abelian
group $H$. Every character of $H_t$ extends to $H$.

Under (3), every finite polynomial supported on
$L=\bigcup_tL_t\subset H$ therefore satisfies the ordinary Sidon
estimate with constant at most $2^{9M}$, by (13). Apply Pisier's
Theorem 2 **once** to this one infinite set in the dual of the compact
abelian group $\widehat H$. It gives one integer $k$ such that
every finite subset of $L$ has a dissociated subset of size at least
its cardinality divided by $k$. Set $\delta=1/k$.

The exact theorem statement was checked in the supplied
[full source](../../../../library/analysis/pisier_1983_arithmetic_characterizations_sidon_sets/_index.md),
Theorem 2 on reading-copy page 3, after reading its digest. The source does not
provide an explicit dependence of $k$ on the Sidon constant, so no numerical
extraction constant is asserted. The analytic constants above are explicit.

The carry-free integer realization and separated-block assembly already
available in the wiki apply to these finite $0,1$-column families.
They do not settle the remaining obligation
$$
\sup_t\chi_1(L_t)=\infty
$$
for any of these schedules. No completion claim follows from this extraction
theorem alone.
