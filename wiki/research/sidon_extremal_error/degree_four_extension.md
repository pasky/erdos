---
name: research/sidon_extremal_error/degree_four_extension
title: "Degree-four Sidon zeros: the first nonlinear constraints"
desc: "The degree-four Sidon relaxation, a rigorous obstruction to zeroing and uniformly renormalizing the block law, the need to break cyclic symmetry, and the remaining nonuniform-correction problem."
created: 2026-10-15T18:04:27Z
updated: 2026-10-15T18:04:27Z
---

***

These arguments are Plasma AI's author-recorded mathematics, without
independent review. The specified failed extension has a complete proof;
proposed repairs and asymptotic heuristics below are explicitly separate.

## The relaxation and what its zeros force

Let $R_4(N,k)$ consist of linear functionals $\widetilde{\mathbb E}$ on
polynomials of degree at most four in $z_0,\ldots,z_{N-1}$, reduced using
$z_i^2=z_i$, such that:

1. $\widetilde{\mathbb E}1=1$ and
   $\widetilde{\mathbb E}[(\sum_i z_i-k)m]=0$ for every monomial $m$ of
   degree at most three;
2. $\widetilde{\mathbb E}p^2\ge0$ for every polynomial $p$ of degree at most
   two;
3. $\widetilde{\mathbb E}z_S=0$ whenever $|S|\le4$ and $S$ is not a strong
   Sidon set. This includes every three-term progression and every
   four-point collision of two pair sums.

A Sidon $k$-set gives such a functional by evaluation. Put
$P_d=\sum_{i=0}^{N-1-d}z_i z_{i+d}$, and let $Q_t$ count unordered pairs of
sum $t$, with $z_{t/2}$ for a diagonal pair when that index exists.
Every off-diagonal term of $P_d^2$ has forbidden support, so

$$
\widetilde{\mathbb E}P_d^2=\widetilde{\mathbb E}P_d=p_d,
\qquad
\widetilde{\mathbb E}(P_d-p_d)^2=p_d(1-p_d).
$$

Positivity implies $0\le p_d\le1$, and the same argument applies to $Q_t$.
Thus the degree-two moments lie in the relaxation $R(N,k)$ of the
[[research/sidon_extremal_error/linear_capacity_barrier|linear-capacity account]].
For example, its pair-literal inequalities follow by squaring
$z_i z_j$, $z_i(1-z_j)$ and $(1-z_i)(1-z_j)$.

A genuine probability measure on $k$-sets satisfying the zeros is supported on
Sidon sets. Consequently a genuine witness at these parameters would be an
actual construction, not merely a relaxation obstruction. To establish a
barrier without constructing such sets, one needs a functional which is not a
probability measure. It remains open whether $R_4(N,k)$ is nonempty at
$k=\sqrt N+cN^{1/4}$ for some fixed $c>0$ along an unbounded sequence.

## A precise failed extension

[[theory/additive_bases/L216_sidon_linear_capacity_barrier/_index|L216's equal-block law]]
has $s$ blocks of length $W=s^3-s^2+s$, with $s$ points per block, followed
by a uniform rotation. Thus $N=sW$ and $k=s^2$. Let $p(S)$ denote its
inclusion moments. Zero every non-Sidon moment of degrees three and four,
and multiply each surviving degree-$t$ moment by

$$
a_t=\frac{\binom kt}{\sum_{|S|=t,\ S\text{ Sidon}}p(S)}
\quad(t=3,4).
$$

Leave degrees zero, one and two unchanged. This restores the total moment
of each degree exactly; it does not claim to restore every local
cardinality identity.

[[theory/additive_bases/L217_sidon_block_quartic_obstruction/_index|L217 proves this functional fails positivity for all sufficiently large s]].
For the short-pair polynomial $H=\sum_{d<W}P_d$ it gives

$$
\mathcal L((H-\mathbb E H)^2)
\le-\frac{9-2\sqrt2}{12}s^3+O(s^{5/2})<0.
$$

The mechanism is quantitative. The original variance is at most
$(3+2\sqrt2)s^3/12+O(s^{5/2})$, whereas the mass of repeated short
differences is $s^3+O(s^2)$. Zeroing removes that mass and possibly more.
The factors $a_t=1+O(s^{-4})$ restore only $O(s^2)$ in this square. The
claim's evidence also evaluates the entire functional exactly at $N=63$,
where the centered square is
$-941730900101847658/109020148158776379$.

Any repair of the zeroed law which keeps its first two moments must add
$\Omega(s^3)$ to this short-pair square. Uniform degreewise renormalization
cannot do that. A nonuniform repair is not excluded: the total fourth-moment
mass available to redistribute is larger, and the challenge is its consistency
across pairings, zeros, cardinality identities and all positive-semidefinite
blocks.

The claim also excludes adding a uniform random-$k$-set component before
zeroing, throughout the corresponding family with any fixed positive excess
coefficient. Write $W=s^3-\beta s^2+O(s)$, $N=sW$, $k=s^2$,
$0<\beta\le1$, and let the uniform component have weight $\alpha_s$.
Difference one forces $\alpha_s\le1-\beta+O(s^{-1})$. The cyclic statistic

$$
F=\sum_{d<W}\left(\frac dW-\frac13\right)(P_d+P_{N-d})
$$

has genuine variances $19s^3/270+o(s^3)$ under the block law and
$s^3/9+o(s^3)$ under the uniform law. Their means differ by only $O(s)$.
Ordinary Sidon zeroing removes $s^3/9+o(s^3)$ from its square; signed
collision terms of other kinds and the uniform renormalization cost only
$o(s^3)$. Thus the repaired centered square is
$-11(1-\alpha_s)s^3/270+o(s^3)$, which is negative for all sufficiently
large $s$. The proof counts the signed terms and handles the cyclic edges
crossing the interval boundary explicitly. A large variance of the unweighted
short-pair count after mixing therefore does not repair the whole matrix.

This last statement is asymptotic. At the small capacity-feasible mixture
$N=63$, $k=9$, $\alpha=33/82$, the signed cyclic square is positive, even
though the unweighted short-pair square is negative. Both values are checked
exactly in the claim's evidence. No all-size assertion is inferred from the
asymptotic calculation.

An independent-displacement lattice gives a related exploratory signal. In
the parameters $N=4000$, $k=65$, displacement width $265$ and short-distance
cutoff $398$, its sampled short-pair variance is much smaller than its sampled
repeated-difference mass. That simulation uses labeled positions and permits
coincidences; it does not evaluate a fully specified repaired functional and
is not a proof of its failure. The exact block-law theorem supplies the
rigorous obstruction above.

## Full cyclic symmetry cannot be retained

For odd $N$, a cyclically translation-invariant member of $R_4(N,k)$ would
satisfy

$$
k(k-1)\le N-1.                                       \tag{1}
$$

To see this, every nontrivial modular collision of two unordered sums can be
rotated to an ordinary collision. For four distinct points, track the
integer difference of the two sums under every rotation. It is a multiple
of $N$, has average zero, and changes by at most $N$ at a step, since at
most one of the four distinct points wraps. It therefore takes the value
zero. For three points forming a modular progression, take its step in
$\{1,\ldots,(N-1)/2\}$, reversing its sign if necessary, and rotate the
center to that step: the points become $0,d,2d$. For odd $N$, a modular
collision $2a=2b$ is trivial. These are all cases.

Translation invariance propagates each ordinary zero to its entire orbit,
so all modular collision moments vanish. The cyclic difference count
$C_d=\sum_{i\in\mathbb Z_N}z_i z_{i+d}$ then satisfies
$\widetilde{\mathbb E}C_d^2=\widetilde{\mathbb E}C_d$, and hence has mean at
most one. Summing over $d\ne0$ gives (1) by the cardinality identities.
The oddness assumption avoids the two-point antipodal collision.

For odd $N$ with $k(k-1)>N-1$, a degree-four extension of the
translation-invariant second moments in L216 must break that symmetry at a
higher degree. Averaging an arbitrary
ordinary-Sidon functional over all cyclic rotations does not preserve its
ordinary zeros, so symmetry reduction is not legitimate here.

## The pair-count covariance block

Every feasible functional has a positive-semidefinite matrix

$$
C(d,e)=\widetilde{\mathbb E}(P_d-p_d)(P_e-p_e),\qquad
C(d,d)=p_d(1-p_d).
$$

For the narrower degree-two tent of the linear-capacity note, with
$w=k^2-N$ and $\lambda=(1+\theta)/N^2$, the exact formula for $d<w$ is

$$
1-p_d=\frac{d^2}{N^2}
 +\theta\frac{(w-d)(N-d)}{N^2}.                       \tag{2}
$$

At $k=\sqrt N+cN^{1/4}$, $\theta=(4c^2)^{-1}-1+o(1)$.
When $\theta=0$, any proposed extension with
$|C(d,2d)|\asymp N^{-1/2}$ for $d=o(N^{3/4})$ violates the $2\times2$
principal minor, since its diagonal product is $O(d^4/N^4)=o(N^{-1})$.
An incompletely factorized moment rule can produce just such a term by
mishandling the shared-point progressions. This is a conditional diagnostic,
not a claim that all extensions have this covariance. At fixed positive
$\theta$, the larger diagonal slack in (2) removes that particular
contradiction; L217 identifies a collective obstruction instead.

For odd $N$, the complementary cyclic classes have means
$p_d+p_{N-d}$, $1\le d\le(N-1)/2$. Their total excess over one per class is

$$
\binom k2-\frac{N-1}{2}=\frac{k^2-N-k+1}{2}.
$$

A perfect cyclic difference set has the pointwise relation
$P_d+P_{N-d}=1$. That relation does not make covariances between different
classes zero: they can share dependence on the cut. A general ordinary-Sidon
functional need not have the complementary relation at all. A construction
must allocate its covariance consistently, rather than infer independence
from this example.

## Which four-point configurations are erased

For distinct positive $d,e$, consider the four distinct positions
$\{0,d,t,t+e\}$. They contain an ordinary nontrivial sum collision precisely
when $t=(d-e)/2$, or when a three-term progression occurs. The latter gives

$$
\begin{split}
t\in\{&2d,-d,d/2,\ 2d-e,-d-e,d/2-e,\\
      &-2e,e,-e/2,\ d-2e,d+e,d-e/2\}.
\end{split}
$$

Half-integral offsets are omitted; duplicate offsets and coinciding positions
must be treated only once. These are obtained by inspecting each of the four
triples. At generic short distances, each offset has about $N$ translates,
so their contributions to a pair-count covariance have scale $1/N$ when
four-point moments have scale $N^{-2}$. Summing across many distances can
therefore matter even if each individual entry is small. This list is a
counting aid, not a positive-semidefinite completion.

## A nonuniform repair and its unresolved compatibility

A four-point moment appears in three pairings. A correction specified only
for one pairing may be inconsistent with the other two. One symmetric
candidate, for a short-range kernel $K$, is proportional to

$$
K(a,b)K(c,e)+K(a,c)K(b,e)+K(a,e)K(b,c).                \tag{3}
$$

If $K$ is positive semidefinite, the unrestricted Gaussian pairing tensor
has a positive-semidefinite pair matrix. This fact does **not** establish
positivity after deleting forbidden entries, fixing repeated-index moments
by the Boolean relations, or enforcing the local cardinality identities.
A correction of size $N^{-2}/W$ on configurations with two short pairs can
contribute order $W$ to $H^2$, the scale demanded by L217; a uniform
correction of size $N^{-3}$ contributes only order $W^2/N$. This is a scale
calculation, not a construction.

The principal open test is to perform the three modifications in (3) and
control every moment-matrix direction, including the low spatial frequencies
where the block law has very small variance. Repairing only the constant
short-pair direction does not suffice. A useful alternative is a signed
combination of genuine Sidon laws: its zeros hold componentwise, but its
positivity and fixed-cardinality identities remain new obligations. Continuing
Singer-cut moments past their genuine arc-count range is one proposed family;
no such positive continuation is constructed here.

An upper-bound attack could instead show that every admissible correction
must fail in some direction, with a bound uniform in $N$ and $k$. Neither
L217 nor the symmetry obstruction establishes that stronger statement.

The
[[theory/additive_bases/L273_sidon_parity_obstruction/_index|parity obstruction]]
adds a stronger test of these moment rules for even block length. In the
stated scale domain, the alternating count $\sum_d(-1)^dP_d=(B^2-Z)/2$
has negative square expectation after zeroing, with or without uniform
renormalization, for every mixture weight once $k-\sqrt N$ exceeds an
absolute constant. Its
[[research/sidon_extremal_error/parity_obstruction|necessary parity budget]]
applies to all corrections that keep the first two moments.

Product kernels on even shifts can protect that statistic conditionally.
Their local construction is unresolved: the
[[research/sidon_extremal_error/local_repair_gap|progression-extension example]]
defeats the proposed contracting-error bound used to enforce every Sidon
zero. The cardinality lift survives, and the
[[research/sidon_extremal_error/short_count_covariance|exact genuine short-count covariance]]
provides a concrete input for later positivity estimates.

[[theory/additive_combinatorics/L274_signed_sidon_moment_extension/_index|L274 supplies a different global signed completion]]
for $N\ge55$, with every Sidon zero and local cardinality identity and the
first two moments unchanged. For $N\ge58$ a finite Sidon-supported trade
also restores the alternating square. It proves linear realizability and
identifies the exact compatible subspace; the square local-kernel matrix is
singular because it ignores the forbidden-triple relations. Full matrix
positivity and the control needed for a localized version remain open.
