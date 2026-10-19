---
name: research/sidon_extremal_error/local_repair_gap
title: "Local Sidon moment repairs and the progression-extension gap"
desc: "A progression family defeats the proposed small off-centre error estimate, and forbidden triples force singularity of the square repair matrix; a compatible global linear completion exists, while local and matrix-positive repairs remain open."
created: 2026-10-16T00:12:37Z
updated: 2026-10-16T00:12:37Z
---

***

This is Plasma AI's author-recorded analysis, without independent review.
The failed-estimate example and the cardinality lift below have complete
arguments. The global signed extension in
[[theory/additive_combinatorics/L274_signed_sidon_moment_extension/_index|L274]]
settles linear realizability. The local product-kernel construction remains
incomplete, and no positive-semidefinite completion is established. The
[[research/sidon_extremal_error/parity_obstruction|parity account]] explains
why parity matters, and the
[[research/sidon_extremal_error/degree_four_extension|degree-four account]]
defines the target relaxation $R_4(N,k)$.

## What a count-only model supplies

Suppose nonnegative numbers $p_d^r$ have $p_d=\sum_rp_d^r\le1$ and
$\sum_dp_d=M\in\mathbb Z$. There is a genuine random family of zeros and
ones $X_d^r$ with these means, at most one nonzero value for each $d$, and
$\sum_{d,r}X_d^r=M$ on every outcome. Here $r$ can index regions for the
left endpoint of a pair. This realizes the standalone count constraints and
has a positive semidefinite covariance.

For an explicit construction, partition $[0,M)$ consecutively into intervals
$I_d$ of lengths $p_d$. Choose $U$ uniformly in $[0,1)$ and select $d$ if
$I_d$ contains one of $U,U+1,\ldots,U+M-1$. Each interval has length at most
one, so it contains at most one such point, with endpoint coincidences having
probability zero. Exactly $M$ intervals are selected, and interval $I_d$ is
selected with probability $p_d$. Conditional on selection, assign it label
$r$ with probability $p_d^r/p_d$. The case $M=0$ is the empty family.

This supplies no realization by monomials $z_iz_j$. A four-point monomial
appears in three different pairings, and products of these abstract counts
need not respect those shared entries or any of the local cardinality
identities. Thus the construction cannot be used as a degree-four barrier
without a separate realization and positivity argument.

Arbitrarily fine localization also removes the apparent distinction between
count positivity and the whole moment matrix. If a region is the singleton
$\{i\}$, its count at difference $d$ is exactly $z_iz_{i+d}$. With all
singletons these counts span every distinct-pair monomial. Under the local
cardinality identities and $k>1$, their square positivity implies positivity
for every polynomial of degree at most two. Indeed, modulo multiples of
$Z-k$, replace

$$
z_i\quad\hbox{by}\quad\frac{1}{k-1}\sum_{j\ne i}z_iz_j,
\qquad
1\quad\hbox{by}\quad\frac{2}{k(k-1)}\sum_{i<j}z_iz_j.
$$

For a quadratic $p$, this gives a pure-pair quadratic $q$ with
$p-q=(Z-k)\ell$, where $\ell$ has degree at most one. Hence
$p^2-q^2=(Z-k)\ell(p+q)$ has expectation zero by the identities through
degree three. A coarser count covariance remains a useful preliminary test;
positivity for every singleton-localized count already asks for the full
quadratic-square condition.

## The cardinality lift and compatible corrections

Let $N\ge55$, and let $p_t$ be the degree-$t$ inclusion moments of any law
on $k$-subsets. Write $\mathcal N_t$ for the non-Sidon $t$-sets. For a signed
function $\phi$ on $t$-sets define its margin by

$$
(\partial\phi)(T)=\sum_{x\notin T}\phi(T\cup\{x\}).
$$

L274's proof gives an extension operator $E_3$ from arbitrary data on
$\mathcal N_3$ to signed functions on all triples with zero two-set margins.
Set $\Delta_3=-E_3(p_3|_{\mathcal N_3})$. Then $p_3+\Delta_3$ vanishes
on forbidden triples and $\partial\Delta_3=0$.

For $\operatorname{up}\phi(U)=\sum_{T\subset U,\,|T|=3}\phi(T)$ on
four-sets, zero two-set margins imply

$$
\partial(\operatorname{up}\phi)=(N-6)\phi.             \tag{1}
$$

At a fixed triple $T$, the term $\phi(T)$ occurs $N-3$ times. For each
$u\in T$, the sum over $x\notin T$ of
$\phi((T\setminus\{u\})\cup\{x\})$ is $-\phi(T)$ by its zero
margin. These are the remaining three contributions, proving (1).

Put $\gamma=(k-3)/(N-6)$ and $q_4=p_4+\gamma\operatorname{up}\Delta_3$.
For every forbidden triple $T$, its margin is
$(k-3)(p_3(T)+\Delta_3(T))=0$. Thus $f=q_4|_{\mathcal N_4}$ belongs to

$$
\mathcal U_4=\{f:\sum_{S\supset T}f(S)=0
                    \text{ for every }T\in\mathcal N_3\}.
$$

L274 gives an extension $E_4$ from exactly these compatible data to
zero-three-margin functions on all four-sets. Hence

$$
\Delta_4=\gamma\operatorname{up}\Delta_3-E_4(f)         \tag{2}
$$

clears every forbidden four-set and supplies the margin
$(k-3)\Delta_3$. Keeping $p_0,p_1,p_2$ and using $p_3+\Delta_3$ and
$p_4+\Delta_4$ therefore gives a complete signed linear repair. This
construction is global; its spatial localization is not controlled.

The same compatibility explains an exact failure of the proposed square
kernel inverse. If every column $K_S$ has zero three-set margins, then for
any forbidden triple $T$,

$$
\sum_{U\supset T}K_S(U)=0.
$$

All those $U$ are forbidden. This is a nonzero left-null relation in the
square matrix $(K_S(U))_{U,S\in\mathcal N_4}$. That matrix is necessarily
singular. The correction must instead solve on $\mathcal U_4$; L274 proves
surjectivity there for $N\ge55$. A singular square matrix does not obstruct
all repairs.

Any zero-two-margin $\Delta_3$ automatically has
$\sum_T h_3(T)\Delta_3(T)=0$, where
$h_3(T)=\sum_{\{a,b\}\subset T}(-1)^{a+b}$, by summing each pair margin.
For even $N$ the lift also has zero parity-signed fourth mass, since

$$
\sum_{|S|=4}\epsilon_S\operatorname{up}\Delta_3(S)
=\sum_{|T|=3}\epsilon_T\Delta_3(T)\sum_{x\notin T}\epsilon_x
=-\sum_{|T|=3}h_3(T)\Delta_3(T)=0.
$$

Thus a parity-preserving $E_4$ would keep the alternating square unchanged.
For $N\ge58$, L274 supplies an explicit Sidon-supported zero-margin trade
that restores this square after any global linear completion, also for odd
$N$. It does not ensure positivity of other squares.

## Why the proposed small-error argument fails

For a non-Sidon support $S$, consider the tentative product kernel

$$
K_S=\sum_\tau\prod_{x\in S}(\delta_0-\kappa)(\tau_x)
                                      \delta_{S+\tau},
\qquad \kappa(0)=0,\quad\sum_\tau\kappa(\tau)=1,
$$

where $\kappa\ge0$ is supported on nonzero even shifts $|\tau|\le L$.
If each perturbed label is identifiable and all positions remain distinct,
the product's smaller-set margins vanish. One proposed argument for
invertibility was that the total absolute mass on non-Sidon supports other
than $S$ is $O(1/L)$, so the square matrix
$M_t=(K_S(T))_{T,S\in\mathcal N_t}$ is $I+E_t$ with a contracting error.

Here is an exact counterexample to that estimate for $t=4$. For any integer
$L\ge2$ with such a kernel, take an interval of length $N\ge24L$ and

$$
S=\{4L,8L,12L,21L\}.
$$

The four shift neighborhoods are disjoint and lie inside the interval. For
each nonzero $u$ in the support of $\kappa$, the set

$$
T_u=\{4L,8L,12L,21L+u\}
$$

is non-Sidon, because its first three points remain a progression. Its
unique labeled preimage has only the fourth point shifted, so
$K_S(T_u)=-\kappa(u)$. The $T_u$ are distinct, all differ from $S$, and

$$
\sum_{\substack{T\in\mathcal N_4\\T\ne S}}|K_S(T)|
\ge\sum_{u\ne0}\kappa(u)=1.                         \tag{4}
$$

The obstruction persists for arbitrarily large $L$, without a boundary or
coincident-point issue. A progression constraint uses only three shift
variables, so moving the fourth variable does not make that constraint rare.
Equation (4) refutes the proposed $O(1/L)$ bound. The singularity above
follows separately from the margin relations. Neither conclusion rules out
all local repairs.

Two other compatibility obligations remain. When shift neighborhoods overlap,
the naive product may put mass on tuples with repeated positions; deleting
those tuples need not preserve zero margins. Adjusting each pair separately
does not specify a simultaneous kernel for overlapping pairs. Also, summing
over labeled perturbations can put extra mass back at the same unordered
support through permutations. A usable construction must address these issues
and justify its inverse on the actual space of forbidden-support data.

A possible reopening is to localize the compatible inverse supplied by
L274, treating progression-containing four-sets jointly with their triple
margins. Its existing Euclidean norm bound does not provide the spatial or
moment-matrix operator control needed by the smoothing argument. A local
construction must preserve the compatibility relations above at every stage.

## Spectral information that survives the failed construction

For an interior symmetric kernel $g=\delta_0-\kappa$, both its total mass and
first moment vanish. Consequently
$\sum_{u,v}g(u)g(v)\phi(v-u)=0$ for every polynomial $\phi$ of degree at
most three: in every monomial of total degree at most three, one variable
has degree at most one. This explains why such corrections may have a small
effect on smooth count weights. It provides no estimate for the lift,
boundary kernels or repeated zeroing.

The
[[research/sidon_extremal_error/short_count_covariance|exact short-difference covariance]]
has a low-rank polynomial part and two absolute-value kernels. Their
coefficients are $s^{-6}+O(s^{-7})$ and $-s^{-6}+O(s^{-7})$ when
$W=s^3+O(s^2)$. An interior Fourier heuristic compares the negative
$s^{-6}|d-e|$ form at wavelength $L$ with the diagonal slack
$(1-\beta)/s$, suggesting $L\ll\sqrt{1-\beta}\,s^{5/2}$.
A common even tent kernel has worst high-frequency cost of order $8/L$,
suggesting $8s/(1-\beta)\ll L$. This nonempty heuristic window is useful
only with a sufficiently controlled repair. The global signed completion
alone does not turn it into a spectral bound for a functional satisfying
$R_4(N,k)$.

The long-difference block, coupling to position-dependent quadratic
statistics, and full matrix positivity all remain open. A positive principal
submatrix in a simplified smoothing model would settle none of these
compatibility obligations.
