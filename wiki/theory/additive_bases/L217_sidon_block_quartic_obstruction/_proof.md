---
name: theory/additive_bases/L217_sidon_block_quartic_obstruction/_proof
title: "Proof of the quartic obstruction for the block law"
desc: "Cyclic variance identities, a collision coupling, and weighted pair counts obstruct zeroing and uniform renormalization of block laws and their uniform admixtures at every positive excess coefficient."
created: 2026-10-15T20:05:11Z
updated: 2026-10-15T20:05:11Z
---

***

This is a complete author-recorded proof of
[[theory/additive_bases/L217_sidon_block_quartic_obstruction/_index|L217]].
Until the final section, all asymptotic constants are absolute and concern
$s\to\infty$; that section states its additional parameter dependence.
Write $W=s^3-s^2+s$, $N=sW$, $k=s^2$ and $D=W-1$. The probability law
$\mu_s$ is the equal-block law of
[[theory/additive_bases/L216_sidon_linear_capacity_barrier/_index|L216]],
whose difference capacities imply $\mathbb E Q\le D$.

We first prove

$$
\operatorname{Var}_{\mu_s} Q
\le\frac{3+2\sqrt2}{12}s^3+O(s^{5/2}),                 \tag{1}
$$

and

$$
\mathbb E_{\mu_s}\sum_{d=1}^{D}r_A(d)(r_A(d)-1)
=s^3+O(s^2).                                         \tag{2}
$$

The constant in (1) is less than $1/2$, whereas the leading constant in
(2) is one.

## The variance before sampling without replacement

For this calculation allow $s$ independent uniform labeled positions in each
block, with repetitions. Count a pair of coinciding labels once as a pair of
distance zero. Let $C$ count pairs at cyclic distance at most $D$, and let
$Q_*$ count pairs at ordinary distance at most $D$ after an independent
uniform rotation. Then $Q_*=C-Z$, where $Z$ counts the short cyclic pairs
which cross the cut. The comparison with sets will remove all repetitions.

More generally, take $B\ge3$ blocks of length $W$ and $m$ independent points
per block. If $U_b$ denotes their coordinates in $\{0,\ldots,W-1\}$, then

$$
C=B\binom m2+\sum_{b\in\mathbb Z_B}H(U_b,U_{b+1}),\qquad
H(U,V)=\sum_{x\in U,\,y\in V}\mathbf1_{y<x},           \tag{3}
$$

with sums over labels. For independent uniform $X,Y$ in one block, put
$\alpha=(W-1)/(2W)$ and $a(x)=(x-(W-1)/2)/W$. The kernel

$$
g(x,y)=\mathbf1_{y<x}-\alpha-a(x)+a(y)
$$

has zero row and column means, and direct summation gives

$$
\mathbb E g(X,Y)^2=\frac{W^2-1}{12W^2}.               \tag{4}
$$

For example, $\operatorname{Var}(\mathbf1_{Y<X})=(W^2-1)/(4W^2)$
and each of the two orthogonal one-variable projections has variance
$(W^2-1)/(12W^2)$, giving (4) by subtraction.
The one-variable terms in (3) telescope over the cycle. The residuals on
different block boundaries have zero covariance: disjoint ones are independent,
and for adjacent ones conditioning on the common block leaves two independent
variables of conditional mean zero. Inside one boundary sum, distinct label
pairs likewise have zero covariance. Consequently

$$
\operatorname{Var} C
=\frac{B m^2}{12}(1-W^{-2}).                         \tag{5}
$$

## The variance caused by the cut

We show, uniformly for $W\ge m$ and $B\ge4$,

$$
\operatorname{Var} Z\le\frac{m^3}{6}+O(m^2+m^3/W).    \tag{6}
$$

Only the block containing the cut and its two neighbors can contribute to
$Z$. Conditional on the cut, it is a sum of zero-one kernels over pairs of
at most $3m$ independent labeled positions. Decompose each kernel into its
mean, two one-variable projections and a residual with zero conditional mean
in each variable. This is an orthogonal decomposition: residuals on distinct
label pairs have zero covariance, including when they share one label.
Each residual has squared norm at most the squared norm of its original
zero-one kernel, hence at most one. The total residual variance is therefore
$O(m^2)$.

Scale distances from the cut by $W$, and let
$f(x)=(1-|x|)_+$. For a labeled position at $x$, the expected number of its
partners across the cut is

$$
m f(x)-b(x)+O(m/W),\qquad 0\le b(x)\le1.             \tag{7}
$$

The triangular term counts all positions across the cut within distance
$W-1$ at density $m/W$. The term $b$ subtracts the spurious partner label
equal to the chosen label in its own block. The error is uniform: the integer
count of allowed positions differs from $Wf(x)$ by a bounded amount.

Let the cut fall at relative position $a\in[0,1]$ in its block. The three
unit blocks around the cut have integrals of $f$ equal to

$$
\frac{(1-a)^2}{2},\qquad \frac12+a-a^2,
\qquad\frac{a^2}{2}.
$$

Since $\int f^2=2/3$, the sum of its within-block variances is

$$
K(a)=\frac23-\left(\frac{(1-a)^4}{4}
 +\left(\frac12+a-a^2\right)^2+\frac{a^4}{4}\right)
=\frac16-\frac32a^2(1-a)^2\le\frac16.                \tag{8}
$$

For the discrete grid the same sum is at most $1/6+O(1/W)$, uniformly in
$a$: the bounded, piecewise linear functions $f$ and $f^2$ have uniformly
bounded variation, so their left Riemann sums differ from their integrals by
$O(1/W)$. Equations (7)--(8), with $m$ labels in each block, show that the
one-variable part of the conditional variance is at most
$m^3/6+O(m^2+m^3/W)$. Together with the residual bound this proves the same
bound for $\operatorname{Var}(Z\mid\text{cut})$.

Its conditional mean differs by $O(m)$ from the cut-independent value
$m^2D(D+1)/(2W^2)$. Indeed the leading term counts the $D(D+1)/2$ unordered
position pairs across the cut with density $m^2/W^2$. Excluding identical
labels subtracts at most $m$ times a bounded number of normalized
within-block pair counts. Thus the variance of the conditional mean is
$O(m^2)$. The law of total variance proves (6).

Now use $B=m=s$ and $W\asymp s^3$. From (5)--(6) and the triangle
inequality for centered $L^2$ norms,

$$
\sqrt{\operatorname{Var}Q_*}
\le\sqrt{\operatorname{Var}C}+\sqrt{\operatorname{Var}Z},
\qquad
\operatorname{Var}Q_*
\le\frac{(1+\sqrt2)^2}{12}s^3+O(s^2).                 \tag{9}
$$

## Coupling back to genuine sets

Within each block accept the independent positions in label order. If a
position repeats an already accepted one, replace it by a fresh uniform
position outside the accepted set. This yields a uniform sample without
replacement. Keep the same random rotation. If $J$ is the total number of
labels replaced, its conditional replacement probability at the $j$th label
of a block is $(j-1)/W$. Thus

$$
\mathbb E J=\frac{s^2(s-1)}{2W}=O(1),\qquad
\mathbb E J^2=O(1).                                  \tag{10}
$$

For the second assertion, conditional expectations of two distinct
replacement indicators factor: at the later label its conditional
probability is the same deterministic number, regardless of the earlier
history. Hence the second moment is at most
$\mathbb E J+(\mathbb E J)^2$.

Replacing a point inside its block changes the short-pair count by at most
$3s$: only labels in that block and its two neighbors can be involved, before
or after the replacement. Therefore $\|Q-Q_*\|_2=O(s)$. Standard deviation
is $1$-Lipschitz in $L^2$ (it is distance to the constant random variables),
so (9) gives (1). The convention for coincident labels disappears after
this coupling.

## Repeated differences and the cost of renormalization

For any fixed set $T$ of $t\le4$ distinct positions, and any rotation, its
inclusion probability is a product of factors
$(s)_{t_b}/(W)_{t_b}$, where $t_b$ counts its positions in block $b$ and
$(v)_j=v(v-1)\cdots(v-j+1)$. Uniformly in $T$ and the rotation,

$$
p(T)=y^t(1+O(s^{-1})),\qquad y=s/W.                  \tag{11}
$$

For $s\ge4$ these probabilities are positive. In particular the denominators
defining $a_3,a_4$ are positive, since strong Sidon triples and quadruples
exist in the interval.

For $d\le D$, the number of ordered pairs of distinct $d$-edges having
four different endpoints is

$$
(N-d)(N-d-1)-2(N-2d)=N^2(1+O(s^{-1})).
$$

By (11) their contribution to $\mathbb E r_A(d)(r_A(d)-1)$ is
$N^2y^4(1+O(s^{-1}))=1+O(s^{-1})$, uniformly in $d$. The shared-endpoint
terms contribute $O(Ny^3)=O(s^{-2})$. Summing over
$D=s^3+O(s^2)$ proves (2).

There are $O(N^2)$ non-Sidon triples and $O(N^3)$ non-Sidon quadruples:
a triple contains a three-term progression, while a quadruple contains either
such a progression or two different pairs of equal sum. Choosing all but one
position in the relevant equality determines the last one. Thus, for
$t=3,4$, the total moment erased at degree $t$ is at most

$$
O(N^{t-1}y^t)=O(s^{2t-4}).
$$

Before zeroing, the total is exactly $\binom kt\asymp s^{2t}$ because
the law has fixed cardinality. Consequently

$$
a_t=1+O(s^{-4})\quad(t=3,4).                         \tag{12}
$$

Let $\mathcal L_0$ merely erase non-Sidon moments, without renormalizing.
All coefficients of the Boolean-reduced $Q^2$ are nonnegative. Every term
in $\sum_{d\le D}P_d(P_d-1)$, where $P_d=\sum_i z_i z_{i+d}$, has
non-Sidon support and is erased. Hence

$$
\mathcal L_0((Q-\mathbb E Q)^2)
\le\operatorname{Var}_{\mu_s}Q
 -\mathbb E_{\mu_s}\sum_{d\le D}r_A(d)(r_A(d)-1).      \tag{13}
$$

The constant and linear-in-$Q$ terms remain unchanged:
$\mathcal L_0 Q=\mathbb E Q$ and $\mathcal L_0 1=1$. No positivity of
$\mathcal L_0$ is assumed. By (12), the change from $\mathcal L_0 Q^2$ to
$\mathcal L Q^2$ is at most $O(s^{-4})\mathbb E Q^2=O(s^2)$, using
$\mathbb E Q\le D$ and (1). Combining (1)--(2) and (13),

$$
\mathcal L((Q-\mathbb E Q)^2)
\le-\frac{9-2\sqrt2}{12}s^3+O(s^{5/2}).
$$

This is negative for all sufficiently large $s$, proving the claim. The
normalizations give the displayed total moments exactly by their definition;
they do not supply any missing local identity or repair the negative square.

## Admixture with the uniform fixed-size law

Let $\nu_s$ be uniform on all $k$-subsets of the interval, and put
$\rho_s=(1-\alpha_s)\mu_s+\alpha_s\nu_s$, with $0\le\alpha_s\le1$.
Assume only the necessary capacity $\mathbb E_{\rho_s}r_A(1)\le1$.
Writing $b=\mathbb E_{\mu_s}r_A(1)$ and $u=\mathbb E_{\nu_s}r_A(1)$,
the pair formulas give exactly

$$
b=1-\frac{s-1}{W}-\frac{s^2}{W^3},\qquad
u=\frac{s^2-1}{s^2-s+1}
 =1+\frac{s(s-2)}W.
$$

Thus

$$
\alpha_s\le\frac{1-b}{u-b}
=\frac{(s-1)W^2+s^2}{(s^2-s-1)W^2+s^2}
=\frac{1+O(s^{-1})}{s}.                             \tag{14}
$$

The short-pair means differ by $s^2/2+O(s)$. Indeed, set
$T_0=\sum_{d=1}^{W-1}(N-d)=(W-1)(N-W/2)$. The uniform pair moment is
$y^2-y(1-y)/(N-1)$, so (9) in L216 gives

$$
\mathbb E_{\nu_s}Q-\mathbb E_{\mu_s}Q
=y(1-y)\left(\frac N2-\frac{W+1}{6}
             -\frac{T_0}{N-1}\right)
=\frac{s^2}{2}+O(s).                                \tag{15}
$$

We also need $\operatorname{Var}_{\nu_s}Q=O(s^3)$, including the
fixed-cardinality cancellation. View the short pairs as the edges of a graph
on the interval. Let $E$ be its number of edges, $d_i$ its vertex degrees,
$A=\sum_i d_i(d_i-1)$, and $p_j=(k)_j/(N)_j$. Exact counting of two edges
by their intersection gives

$$
\operatorname{Var}_{\nu_s}Q
=E(p_2-p_4)+A(p_3-p_4)+E^2(p_4-p_2^2).              \tag{16}
$$

Here $E=O(ND)$ and $A=4E^2/N+O(D^3+E)$. To see the latter estimate,
all but $2D$ vertices have degree $2D$; the exceptional degrees are between
$D$ and $2D$, and $2E/N=2D-D(D+1)/N$. Consequently
$\sum_i(d_i-2E/N)^2=O(D^3)$.
For the fixed values $j\le4$, with $N\asymp k^2$,

$$
p_j=y^j\left(1-\frac{j(j-1)}{2k}+O(k^{-2})\right),
\qquad p_4-p_2^2=y^4\left(-\frac4k+O(k^{-2})\right).
$$

In (16), the leading terms $4E^2y^3/N$ and $-4E^2y^4/k$ cancel
because $y=k/N$. The remainder is

$$
O\left(Ey^2+D^3y^3+\frac{E^2y^4}{k^2}\right)=O(s^3).
                                                               \tag{17}
$$

The variance formula for a mixture, (1), and (14)--(17) now yield

$$
\begin{aligned}
\operatorname{Var}_{\rho_s}Q
&=(1-\alpha_s)\operatorname{Var}_{\mu_s}Q
  +\alpha_s\operatorname{Var}_{\nu_s}Q
  +\alpha_s(1-\alpha_s)
       (\mathbb E_{\nu_s}Q-\mathbb E_{\mu_s}Q)^2\\
&\le\left(\frac{3+2\sqrt2}{12}+\frac14\right)s^3
      +O(s^{5/2}).                                  \tag{18}
\end{aligned}
$$

For each distinct set $T$ of at most four positions, the mixture still has
inclusion probability $y^{|T|}(1+O(s^{-1}))$, uniformly in $\alpha_s$.
Thus its repeated-difference mass is still $s^3+O(s^2)$, the normalizing
factors are still $1+O(s^{-4})$, and $\mathbb E_{\rho_s}Q^2=O(s^6)$.
The zeroing and renormalization estimates (12)--(13) therefore apply with
$\rho_s$ and its own mean. Combining them with (18) gives

$$
\mathcal L_{\rho_s}((Q-\mathbb E_{\rho_s}Q)^2)
\le-\frac{3-\sqrt2}{6}s^3+O(s^{5/2})<0
$$

for all sufficiently large $s$. This rules out this entire mixture repair
subject to its first difference capacity. It does not rule out a nonuniform
change of the surviving moments.

## A weighted test for every positive excess coefficient

Fix $0<\beta\le1$, let $W=s^3-\beta s^2+O(s)$ be integers at least $s$, and
set $N=sW$, $k=s^2$, $D=W-1$, $y=s/W$. In this section $\mu_s$ samples $s$ points
per $W$-point block and rotates, and $\nu_s$ is uniform on all $k$-subsets.
These parameters have $(k-\sqrt N)/N^{1/4}\to\beta/2$.
Let $\rho_s=(1-\alpha_s)\mu_s+\alpha_s\nu_s$ satisfy
$\mathbb E_{\rho_s}r_A(1)\le1$. The same pair formulas as above give

$$
\mathbb E_{\mu_s}r_A(1)=1+\frac{\beta-1}s+O(s^{-2}),\qquad
\mathbb E_{\nu_s}r_A(1)=1+\frac\beta s+O(s^{-2}),
$$

and therefore $\alpha_s\le1-\beta+O(s^{-1})$.

Put $g(t)=t-1/3$, and use the cyclic quadratic polynomial

$$
F=\sum_{d=1}^{D}g(d/W)C_d,\qquad
C_d=\sum_{i\in\mathbb Z_N}z_i z_{i+d}
    =P_d+P_{N-d}.                                    \tag{19}
$$

Each unordered short cyclic pair is counted once, since $2D<N$.
We will prove

$$
\mathcal L_{\rho_s}((F-\mathbb E_{\rho_s}F)^2)
=-\frac{11}{270}(1-\alpha_s)s^3+O(s^{5/2}).           \tag{20}
$$

All errors are uniform in $\alpha_s\in[0,1]$; their constants may depend on
the fixed $O(s)$ bound in the definition of $W$. Equation (20) and the first
capacity prove the final statement of the claim.

### The two genuine variances and their means

First allow independent labeled samples in each block, counting a coincidence
with weight $g(0)$. On the unit square define

$$
h_0(u,v)=g(|u-v|),\qquad
h_1(u,v)=\mathbf1_{v<u}g(1+v-u).
$$

The first kernel counts within-block pairs, and the second counts adjacent
blocks. Let $h_j^\circ$ denote the kernel after subtracting its two
one-variable projections and adding back its mean. The projections needed
here are

$$
A_0(u)=u^2-u+\frac16,\qquad
H(u)=\int_u^1 g(t)\,dt=\frac16+\frac u3-\frac{u^2}{2}.
$$

The two projections of $h_1$ are $H(1-u)$ and $H(v)$; its mean is $1/6$,
while $h_0$ has mean zero. Direct polynomial integration gives

$$
\int h_0^2=\frac1{18},\quad \int A_0^2=\frac1{180},\quad
\int h_1^2=\frac1{12},\quad \int H^2=\frac{17}{540}.
$$

Consequently

$$
\|h_0^\circ\|_2^2=\frac2{45},\qquad
\|h_1^\circ\|_2^2=\frac{13}{270}.                    \tag{21}
$$

On the discrete $W$-point grid these formulas have errors $O(1/W)$.
This follows by summing the bounded piecewise polynomial kernels on each
side of the diagonal; the diagonal and its adjacent cells have total area
$O(1/W)$. The projection identity is exact on that grid: the sum of the
within-block row and the two adjacent-block rows is constant in the chosen
position. In the full pair statistic their coefficients are $s-1,s,s$,
so its one-variable projection is just the negative of the within-block
projection. Its total variance is $O(s^2)$.

The canonical two-variable terms are orthogonal for different label pairs,
including pairs sharing one label, exactly as in (4)--(5). There are
$s\binom s2$ within-block pairs and $s^3$ adjacent-block pairs. Thus the
labeled statistic has variance

$$
\left(\frac12\frac2{45}+\frac{13}{270}\right)s^3+O(s^2)
=\frac{19}{270}s^3+O(s^2).
$$

The coupling (10) applies because $W\asymp s^3$. Moving one label changes
the weighted statistic by at most $3s$, so the $L^2$ change is $O(s)$.
It follows that

$$
\operatorname{Var}_{\mu_s}F
=\frac{19}{270}s^3+O(s^{5/2}).                       \tag{22}
$$

For the uniform law, view (19) as a weighted graph on the cycle. Write
$S_j=\sum_{d=1}^{D}g(d/W)^j$ for $j=1,2$. The total edge weight is
$M_1=NS_1$, the sum of squared edge weights is $M_2=NS_2$, and every
vertex has weighted degree $2S_1$. The intersection count (16), with
weights, is

$$
\operatorname{Var}_{\nu_s}F
=M_2(p_2-2p_3+p_4)
 +M_1^2\left(\frac4N(p_3-p_4)+p_4-p_2^2\right).
$$

The leading terms in the parentheses cancel as before, leaving $O(s^2)$
after multiplication by $M_1^2$. Also $S_2=W/9+O(1)$ and
$Ny^2W=s^3$. Therefore

$$
\operatorname{Var}_{\nu_s}F=\frac19s^3+O(s^2).        \tag{23}
$$

There is no large mixture-of-means term in this direction. Indeed, the
two exact sums

$$
\sum_{d=1}^{W-1}g(d/W)=\frac{W-1}{6},\qquad
\sum_{d=1}^{W-1}g(d/W)(W-d)=\frac{W-1}{6}
$$

give

$$
\mathbb E_{\nu_s}F-\mathbb E_{\mu_s}F
=\frac{k(1-y)}6\left(\frac1W-\frac{W-1}{N-1}\right)=O(s).
$$

The variance formula for a mixture and (22)--(23) hence give

$$
\operatorname{Var}_{\rho_s}F
=\left((1-\alpha_s)\frac{19}{270}+\frac{\alpha_s}{9}\right)s^3
 +O(s^{5/2}).                                        \tag{24}
$$

### What ordinary Sidon zeroing removes

Every short ordinary repeated-difference term has non-Sidon support.
Its total contribution to $F^2$ is

$$
R=\sum_{d=1}^{D}g(d/W)^2 r_A(d)(r_A(d)-1).
$$

The uniform inclusion estimate (11) holds for the mixture as well. The
count proving (2) therefore gives
$\mathbb E_{\rho_s}R=S_2(1+O(s^{-1}))=s^3/9+O(s^2)$.
All other erased terms contribute only $O(s^2)$ in absolute value, including
terms with negative weights. Here is a count that accounts for those signs.

For fixed short cyclic lengths $d,e$, the corresponding ordinary lengths are
among $d,N-d$ and $e,N-e$. If two disjoint edges have different ordinary
lengths, their union can be non-Sidon only at a bounded number of relative
offsets: a collision of their other pairings determines their relative
starting point, or one of the four triples is a three-term progression and
does the same. There are therefore $O(ND^2)$ such configurations, with
total moment $O(ND^2y^4)=O(s^2)$. Equal ordinary lengths at most $D$ are
already counted in $R$. Equal lengths $N-d$ have at most $d^2$ ordered edge
pairs, giving total $O(D^3y^4)=O(s)$. A forbidden three-point support is a
progression; for two of its edges to have cyclic length at most $D<N/2$,
its ordinary step must be at most $D$. These give $O(ND)$ supports and
total moment $O(NDy^3)=O(s)$. All polynomial coefficients in these estimates
are bounded in absolute value by a universal constant.

Thus zeroing, with no renormalization, gives the equality with error

$$
\mathcal L_0((F-\mathbb E_{\rho_s}F)^2)
=\operatorname{Var}_{\rho_s}F-\frac19s^3+O(s^2).       \tag{25}
$$

As before $a_t=1+O(s^{-4})$. To bound the effect despite the signed
coefficients, replace every edge weight by its absolute value. The square
of that statistic has expectation $O(s^6)$: count two edges with two, three,
or four distinct endpoints and use $p(T)=O(y^{|T|})$. It dominates the
absolute coefficients of $F^2$. Renormalization therefore changes (25) by
only $O(s^2)$. Equations (24)--(25) prove (20).

The mixture class here has capacity-feasible examples at every fixed
$0<\beta<1$. If $0\le\alpha<1-\beta$ is constant, then uniformly for
$d=xW<W$ its difference expectation is at most
$1+(\beta-1+\alpha-\alpha x)/s+O(s^{-2})<1$.
For $d\ge W$ it is at most $(N-W)y^2=1-(1-\beta)/s+O(s^{-2})<1$.
Every sum expectation is at most $Ny^2/2+y=1/2+O(s^{-1})$.
The obstruction is therefore not due to an empty input class. It rules out
the specified zeroing and uniform renormalization throughout that class,
while leaving general nonuniform completions open.
