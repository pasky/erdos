---
name: research/erdos_864/established_bounds
desc: Leading bounds, a vector-kernel refinement of the upper secondary term, difference structure, and Fourier stability; the target remains unresolved.
tags: [proved, bounds]
sources: []
created: 2026-09-23T02:15:22Z
updated: 2026-10-13T13:01:33Z
---


# research/erdos_864/established_bounds

***

## Current bounds

The best bounds that follow from published results are

$$
 (2/\sqrt3+o(1))\sqrt N\le M(N)\le(1.863\ldots+o(1))\sqrt N.
$$

All sum conditions include diagonal pairs. The upper bound is Theorem 3 of
Pikhurko (2006), p. 2099,
[source record](../../../library/additive_bases/pikhurko_2006_dense_edge_magic_graphs_thin_additive/theorem_3.md),
a refereed bound of $((1/4+(\pi+2)^{-2})^{-1/2}+o(1))\sqrt N$ on quasi-Sidon
subsets of $[1,N]$, those with $|A+A|=(1+o(1))\binom{|A|}2$. A set counted by
$M(N)$ with $k$ elements is quasi-Sidon: the $r$ representations of its one
repeated sum use disjoint elements, so $r\le\lceil k/2\rceil$ and
$|A+A|=\binom{k+1}2-(r-1)\ge\binom{k+1}2-k/2$. Erdős–Freud (1991) print the
trivial bound $(2+o(1))\sqrt N$ as display (37), p. 204, and state without
proof that the coefficient $2$ can be replaced by $1.98$.

The bounds proved here are

$$
 (2/\sqrt3+o(1))\sqrt N\le M(N)
 \le \sqrt{2N}+O(N^{1/4}).
$$

The refined estimates below are proved directly for the present class. The
final kernel refinement adapts a vector-valued smoothing theorem to the present
class.

A [second-order construction improvement](second_order_construction.md)
gives

$$
 \limsup_{N\to\infty}
 \frac{M(N)-(2/\sqrt3)\sqrt N}{N^{1/4}}
 \ge\frac{2\sqrt2}{9\,3^{1/4}}.
$$

It does not change either leading constant displayed above.

## Lower bound

Put $m=\lfloor N/3\rfloor$, choose an ordinary Sidon set
$B\subset[1,m]$ of size $(1+o(1))\sqrt m$, and put
$A=B\cup(N-B)$. The three kinds of sums lie in

$$
 [2,2m],\qquad[N-m+1,N+m-1],\qquad[2N-2m,2N-2],
$$

respectively. These ranges are disjoint, including when $3\mid N$.
Within either copy, uniqueness follows from the Sidon property. A mixed
sum is $N+b-b'$; every nonzero difference in a Sidon set has a unique
ordered representation. Only the sum $N$ repeats, with $|B|$
representations.

For the reflected construction, see Erdős–Freud (1991),
[source record](../../../library/additive_bases/erdos_freud_1991_sums_sidon_sequence/_index.md),
pp. 203–204. For the ordinary Sidon asymptotic, see Theorem 5 of
[source record](../../../library/additive_bases/obryant_2004_complete_annotated_bibliography_work_related_sidon/_index.md),
pp. 10–11. It can also be obtained from the following standard construction. For
a prime $p$, a primitive root $g$, and $t\in\mathbb Z_{p-1}$, choose
$a_t\in\mathbb Z_{p(p-1)}$ with $a_t\equiv t\pmod{p-1}$ and
$a_t\equiv g^t\pmod p$. The sum of two such residues determines the sum and
product of their second coordinates in $\mathbb F_p$, hence the unordered
pair. This is a modular Sidon set of size $p-1$. Choosing a prime
$p\le\sqrt m$ with $p\sim\sqrt m$ and taking integer representatives gives
the claimed lower bound for all large $m$.

## Difference structure

Suppose $S$ is the exceptional sum. Write

$$
 C=A\cap(S-A),\qquad D=A\setminus C,\qquad k=|A|,
 \quad c=|C|.
$$

The possible element $S/2$ belongs to $C$. For a set $X$, write

$$
 \rho_X(j)=\#\{(x,y)\in X^2:x-y=j\}\qquad(j>0).
$$

If two distinct pairs $(x,y),(u,v)$ have the same positive difference,
then $x+v=y+u$. The unordered representations on the two sides are
distinct: equality of their multisets would force either the original
pairs to coincide or a zero difference. Thus

$$
 x+v=y+u=S,
 \qquad (u,v)=(S-y,S-x).
$$

Every repeated difference therefore has exactly two representations,
both wholly inside $C$. In particular,

$$
 \rho_A(j)\le2,
 \qquad \rho_A(j)-\tfrac12\rho_C(j)\le1. \tag{1}
$$

If there is no exceptional sum, set $C=\varnothing$; the same
inequalities hold, with the stronger $\rho_A(j)\le1$.

## Sliding-window identity and the square-root-two upper bound

For integer $h\ge1$, let
$X_h(t)=|X\cap\{t,\ldots,t+h-1\}|$, with $t\in\mathbb Z$.
Counting the windows containing each ordered pair gives

$$
 \sum_t X_h(t)=h|X|,
 \qquad
 \sum_t X_h(t)^2=h|X|+
 2\sum_{j=1}^{h-1}(h-j)\rho_X(j). \tag{2}
$$

There are at most $N+h-1$ nonempty windows. By $\rho_A(j)\le2$,

$$
 \frac{h^2k^2}{N+h-1}
 \le hk+2h(h-1). \tag{3}
$$

Taking $h=N$ first shows $k=O(\sqrt N)$. Then taking
$h=\lceil N^{3/4}\rceil$ in (3) gives
$k^2\le2N+O(N^{3/4})$, hence

$$
 k\le\sqrt{2N}+O(N^{1/4}).
$$


## A kernel refinement of the secondary upper term

An adaptation of the kernel certificate in Hou--Zhao,
[*An Improved Upper Bound for Finite Sidon Sets via Vector-Valued
Smoothing*, v3](https://arxiv.org/html/2607.01169v3), gives

$$
 M(N)\le\sqrt{2N}+2^{1/4}\gamma_0N^{1/4}+O(1),
 \qquad \gamma_0=0.9434925907135450\ldots.                       \tag{3a}
$$

This changes only the secondary term. We use the feasible certificate
asserted in Lemma 4.1 of that version. The smoothing argument is Theorem
2.1 of the same paper.

Here is the needed extension. For nonnegative weights $w_a$, put
$W=\sum_aw_a$, $Q=\sum_aw_a^2$, and assume
$\sum_{a-b=d}w_aw_b\le1$ for each $d>0$. For any nonnegative
probability kernel $K$, its even autocorrelation $C_K$ satisfies
$\sum_dC_K(d)=1$. Thus

$$
 \left\|\sum_aw_aK(\cdot-a)\right\|_2^2
 \le Q C_K(0)+2\sum_{d>0}C_K(d)
 =1+(Q-1)\|K\|_2^2.
$$

For the paper's certificate, let $\lambda_r,K_r,Z_r$ denote its
mixing weights, probability kernels, and boundary functions. Their
pointwise covering inequality and norm identities are

$$
 \sum_r\lambda_r\sum_tK_r(t)Z_r(a+t)\ge1,
 \quad \sum_r\lambda_r\|K_r\|_2^2=\alpha/H,
 \quad \sum_r\lambda_r\|Z_r\|_2^2=N+\beta H-1,
$$

where $\alpha,\beta>0$ are fixed and
$\sqrt{\alpha\beta}=\gamma_0$. These hold for the certificate's
allowed integer scales $H$, with $H=o(N)$. Multiplication of
the covering inequality by $w_a$, summation, and direct-sum
Cauchy--Schwarz give the weighted extension

$$
 W^2\le(N+\beta H-1)\left(1+\frac{\alpha(Q-1)}H\right).         \tag{3b}
$$


For our sets choose $w_a=1/\sqrt2$ for every element. The
difference multiplicity bound proves the hypothesis; then
$W=k/\sqrt2$, $Q=k/2$. Choose an allowed scale

$$
 H=\sqrt{\frac{\alpha}{\sqrt2\beta}}\,N^{3/4}+O(1).
$$

Using the already proved $k\le\sqrt{2N}+O(N^{1/4})$, expansion
of (3b) yields

$$
 k^2/2\le N+2^{3/4}\gamma_0N^{3/4}+O(N^{1/2}),
$$

and taking square roots proves (3a). The paired-core weights in the
next section also satisfy (3b), but do not change the leading constant.

## Weighted paired-core bound

Give elements of $C$ weight $1/\sqrt2$ and elements of $D$
weight $1$. For each positive difference, the sum of the products of
its endpoint weights is at most one: a repeated difference contributes
$1/2+1/2$, and a unique difference contributes at most one.
Put

$$
 W=k-(1-1/\sqrt2)c,\qquad Q=k-c/2.
$$

The weighted version of (2) and Cauchy–Schwarz give, for every $h\ge1$,

$$
 W^2\le\frac{N+h-1}{h}(h-1+Q). \tag{4}
$$

Consequently,

$$
 k-(1-1/\sqrt2)c\le\sqrt N+O(N^{1/4}). \tag{5}
$$

Thus the proposed bound already holds for families with

$$
 \frac c k\le
 \frac{1-\sqrt3/2}{1-1/\sqrt2}+o(1).
$$

This is only a partial case; a large paired core remains possible.

## Retaining the cross terms

Subtract half the core identity in (2) from the identity for $A$,
and use (1). This gives the inequality

$$
 \sum_t\bigl(\tfrac12 C_h(t)^2+2C_h(t)D_h(t)+D_h(t)^2\bigr)
 \le h(h-1)+h(k-c/2). \tag{6}
$$

Remove $S/2$, if present, for a loss of at most one element, and now
use $A,C,k,c$ for the reduced sets and their sizes; $D$ is unchanged. Let
$B=C\cap(-\infty,S/2)$, $b=|B|$, $d=|D|$, and
$L=\operatorname{diam}B$. Then $C=B\sqcup(S-B)$, and reflection
preserves the sum of the squares of window counts. Hence
$\frac12\sum C_h^2\ge\sum B_h^2$. For nonempty $B$, (6) gives

$$
 \frac{b^2}{L+h}+\frac{d^2}{N+h-1}
 +\frac2{h^2}\sum_t C_h(t)D_h(t)
 \le1+\frac{b+d-1}{h}. \tag{7}
$$

In particular, if $L\asymp N$,

$$
 \frac{b^2}{L}+\frac{d^2}{N}\le1+O(N^{-1/4}). \tag{8}
$$

If additionally $b=(1+o(1))\sqrt L$, this proves
$d=o(\sqrt N)$. A reflected near-maximal Sidon set on a span comparable
to $N$ cannot be supplemented by a positive multiple of $\sqrt N$
unpaired elements.

Neither (6) nor Cauchy–Schwarz implies
$k^2-c^2/2\le N+o(N)$. The subtracted quadratic has the wrong
convexity for that inference.

## Off-center exceptional sums

The core lies in

$$
 J=[1,N]\cap[S-N,S-1],\qquad
 \ell=\operatorname{diam}J=\min(S-2,2N-S).
$$

There are at most $\ell+h$ windows meeting $J$, and at most
$N+h-1$ windows meeting $[1,N]$. In (6), equivalently
$\sum(A_h^2-C_h^2/2)$, the summand is at least $A_h^2/2$ on
the former windows and at least $A_h^2$ elsewhere. Weighted
Cauchy–Schwarz yields

$$
 h^2k^2\le (N+\ell+2h-1)
 \bigl(h(h-1)+h(k-c/2)\bigr).
$$

Thus

$$
 k\le\sqrt{N+\ell}+O(N^{1/4}). \tag{9}
$$

The requested constant follows if $\ell\le N/3+o(N)$. Again,
the centered case is not settled.

## Remaining obstacle

No established argument here bounds a fully symmetric example by the
desired constant. Even proving that bound for the symmetric subclass
would leave the reduction from arbitrary sets to that subclass to check.
See [symmetric reformulations](symmetric_reformulations.md) and
[obstructions](obstructions.md).

## A conditional symmetric bound from residue concentration

Let $B\subset[1,L]$ be ordinary Sidon, put $m=|B|$, and let

$$
 c_r=|B\cap(r\bmod q)|,\qquad H=\lceil L/q\rceil.
$$

For every positive integer $h$,

$$
 \sum_{r\bmod q}c_r^2
 \le(H+h-1)\left(1+\frac{m-1}{h}\right). \tag{10}
$$

To prove this, divide each residue fiber by $q$, after subtracting
its residue, and translate it into an interval of $H$ integers.
The nonzero positive difference sets of all these scaled fibers are
pairwise disjoint: a repeated difference $j$ would repeat the
original difference $qj$ in $B$. Summing their sliding-window
identities therefore gives an upper bound $hm+h(h-1)$ for the sum
of window-count squares. Cauchy--Schwarz in each fiber gives the
lower bound $h^2\sum_r c_r^2/(H+h-1)$, proving (10).

For $q=o(\sqrt L)$, take $h\asymp\sqrt{Hm}$, using the ordinary
Sidon bound $m=O(\sqrt L)$. More quantitatively, this yields

$$
 q\sum_r c_r^2
 \le L+O\!\left(q^{1/2}L^{3/4}+q\sqrt L\right)=L+o(L). \tag{11}
$$

If $B$ occupies at most $(2/3+o(1))q$ residue classes, another
application of Cauchy--Schwarz gives

$$
 m^2\le(2/3+o(1))L.
$$

This proves the desired bound for symmetric examples whose positive
half has this residue-concentration property, regardless of how the
set was constructed. It does not address sets equidistributed modulo
small moduli; no implication from $B\cap3B=\varnothing$ to the
required concentration was established.

## Uniform Fourier stability for near-maximal ordinary Sidon sets

The following statement applies to ordinary Sidon sets. It does not
assume $B\cap3B=\varnothing$, and supplies no improvement of the
leading upper-bound constant for that subclass.

Let $L$ be a positive integer and let
$B\subset[1,L]\cap\mathbb Z$ be Sidon, with

$$
 \tfrac12\sqrt L\le m=|B|\le2\sqrt L.
$$

Write $e(x)=\exp(2\pi i x)$, and put

$$
 F(\theta)=\sum_{b\in B}e(b\theta),\qquad
 D_L(\theta)=\sum_{j=1}^{L}e(j\theta).
$$

Then, with an absolute implied constant,

$$
 \sup_{\theta\in\mathbb R}
 \left|\frac{F(\theta)}m-\frac{D_L(\theta)}L\right|
 \ll \sqrt{(1-m^2/L)_+}+L^{-1/8}. \tag{12}
$$

Here $x_+=\max(x,0)$. In particular, if $m^2/L\to1$, the
normalized Fourier transform is uniformly approximated by that of
the uniform probability measure on the interval, at all frequencies
simultaneously.

**Proof.** Set $H=\lceil L^{3/4}\rceil$ and $K=L+H-1$. For any
nonempty $T\subset\{0,\ldots,H-1\}$, write $t=|T|$,

$$
 F_T(\theta)=\sum_{a\in T}e(a\theta),\qquad
 g=1_B*1_T.
$$

The function $g$ is supported on $\{1,\ldots,K\}$, and
$\sum_xg(x)=mt$. Every nonzero ordered difference of $B$ occurs
at most once. On expanding the square of the convolution, the terms
with equal elements of $T$ therefore contribute $mt$, and each
of the $t(t-1)$ remaining ordered pairs contributes at most one.
Thus

$$
 \sum_xg(x)^2\le mt+t(t-1).
$$

Subtracting the squared mean gives

$$
 \left\|g-\frac{mt}{K}1_{\{1,\ldots,K\}}\right\|_2^2
 \le t^2\left(1-\frac{m^2}{K}+\frac mt\right).
$$

Taking the Fourier transform at a specified frequency and applying
Cauchy--Schwarz over the $K$ possible values of $x$, we obtain

$$
 \left|F(\theta)F_T(\theta)-\frac{mt}{K}D_K(\theta)\right|
 \le t\sqrt{K-m^2+\frac{Km}{t}}. \tag{13}
$$


Put

$$
 \eta=\sqrt{(1-m^2/L)_+}+L^{-1/8}.
$$

Whenever $t\ge H/6$, the assumptions on $m$ imply

$$
 K-m^2+\frac{Km}{t}
 \le (L-m^2)_++H+\frac{6Km}{H}
 \ll L(1-m^2/L)_++L^{3/4},
$$

and hence the square root in (13), divided by $m$, is $O(\eta)$.

First suppose $\|\theta\|\ge L^{-7/8}$, where
$\|\theta\|$ is the distance to the nearest integer. Partition the
unit circle into six arcs of angular length $\pi/3$, and choose
$T$ to consist of those integers $a\in\{0,\ldots,H-1\}$ whose
phases $e(a\theta)$ lie in a largest arc. Then $t\ge H/6$.
After rotating the midpoint of this arc to $1$, every phase has
real part at least $\cos(\pi/6)$; consequently

$$
 |F_T(\theta)|\ge(\sqrt3/2)t.
$$

Dividing (13) by $m|F_T(\theta)|$ gives

$$
 \frac{|F(\theta)|}{m}
 \ll \frac{|D_K(\theta)|}{K}+\eta.
$$

The geometric-series estimate

$$
 |D_J(\theta)|\le\frac1{2\|\theta\|}
$$

shows that both $|D_K(\theta)|/K$ and
$|D_L(\theta)|/L$ are $O(L^{-1/8})$ in this range.
The triangle inequality proves (12) here.

For $\|\theta\|<L^{-7/8}$, choose the representative of $\theta$
in $[-1/2,1/2]$ and instead take $T=\{0,\ldots,H-1\}$.
Then

$$
 \frac{F_T(\theta)}H=1+O(H|\theta|)
 =1+O(L^{-1/8}).
$$

Dividing (13) by $mH$, and using $|F(\theta)|/m\le1$, yields

$$
 \left|\frac{F(\theta)}m-\frac{D_K(\theta)}K\right|
 \ll\eta.
$$

Finally,

$$
 \left|\frac{D_K(\theta)}K-\frac{D_L(\theta)}L\right|
 \le \frac{2(K-L)}K\ll L^{-1/4}.
$$

This proves (12) in the remaining range. $\square$

The bound is a Fourier stability statement, not a four-variable counting
theorem. In particular, an $o(m)$ uniform Fourier error does not by itself
give an $o(m^4/L)$ error when counting $x+y+z=w$ at the critical scale
$m\asymp\sqrt L$. See the
Fourier-transfer counterexample
for the scope of this obstruction. No leading gap below $\sqrt L$ for Sidon,
$(3,1)$-sum-free sets is claimed here.

### A one-frequency moment relaxation also remains feasible

Even assuming hypothetically that $m^2/L\to1$ and
$B\cap3B=\varnothing$, the preceding approximation and fourth
moments alone give no contradiction. Remove the arc
$\|\theta\|\le A_L/L$, where $A_L\to\infty$ sufficiently slowly,
and put $Z=F(\theta)/\sqrt m$ on its complement. Expectations in
this paragraph mean normalized Lebesgue integration on that
complement. The necessary limiting moments are

$$
 \mathbb E|Z|^2=1,\qquad
 \mathbb E|Z|^4=\frac43,\qquad
 \mathbb E(Z^3\overline Z)=-\frac16,\qquad
 \mathbb EZ^4=0.                                               \tag{14}
$$

Indeed, on the full circle the second and fourth absolute moments
are $1$ and $2-1/m$, while the two displayed unbalanced fourth
moments vanish. On putting
$\Phi(u)=\int_0^1 e(ut)\,dt$, the removed arc contributes

$$
 \int_{\mathbb R}|\Phi|^4=\frac23,\qquad
 \int_{\mathbb R}\Phi^3\overline\Phi=\frac16,\qquad
 \int_{\mathbb R}\Phi^4=0
$$

to these fourth moments and $o(1)$ to the second moment.
These integrals are respectively the additive energy of
$1_{[0,1]}$, the volume of $t_1+t_2+t_3\le1$, and its
fourfold convolution at zero. Uniform approximation on every fixed
rescaled arc, followed by a sufficiently slow diagonal choice of
$A_L$, justifies the subtractions.

The moments (14) are consistent with a bounded complex random
variable. If $U$ is uniform on the unit circle, take

$$
 Z=\begin{cases}
 U,&\text{with probability }1/3,\\
 (U-U^3)/\sqrt2,&\text{with probability }2/3.
 \end{cases}
$$

In the second case, the second and fourth absolute moments are
$1,3/2$, and $\mathbb E(Z^3\overline Z)=-1/4$.
All analytic moments $\mathbb EZ^j$, $j\ge1$, vanish in both
cases. This proves compatibility with (14); it does not construct
Fourier transforms of admissible sets. An argument using arithmetic
relations between different frequencies, or further information
beyond these moments, remains open.
