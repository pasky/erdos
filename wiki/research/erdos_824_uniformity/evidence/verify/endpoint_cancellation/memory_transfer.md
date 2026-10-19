---
name: research/erdos_824_uniformity/evidence/verify/endpoint_cancellation/memory_transfer
title: "Dilation memory and the collision attack"
desc: Independent reconstruction and collision attacks for the dilation-memory transfer used in endpoint cancellation.
created: 2026-10-16T04:10:53Z
updated: 2026-10-16T04:16:14Z
---

# Dilation memory and the collision attack

***

This calculation examines Section 3 of the
[preserved source](../../assets/endpoint_cancellation_subject/source_sections_2_to_5.md.txt), in the positive-mark
case $\ell\ge1$ consumed by P. Source mathematics is attributed to OpenAI;
the independent examination and its derivations are prepared for Plasma AI.
The notation $B_{\rm mem}$ below distinguishes the memory cutoff from the
endpoint discrepancy exponent. All parameters other than $x$ are fixed in
the order specified in the report.

## A prime pays for one residue, not for every return

Fix an expanded path of $N$ edges, with offsets $h_i$ and active label sets
$\Lambda_i$ at its $N+1$ visits. Put $q_0=q_N=\sqrt q$, $q_i=q$ at the
other visits, and $\eta_i=1-q_i$.

For a prime $p$ that is active, compatibility requires all active offsets
to have one residue $c$ modulo $p$. Conditioning the root on that residue
has probability $1/p$. If $a,z$ are its first and last active visits, its
remaining factor is

$$
\frac1p\prod_{i:\,p\notin\Lambda_i}
 (1-\eta_i\mathbf1_{h_i\equiv c\pmod p}).
\tag{M1}
$$

Expand the product before $a$ by its earliest selected index and the product
after $z$ by its latest selected index. Equivalently, subtract successive
partial products. A chosen earlier or later endpoint contributes
$-\eta_i$ and requires the same residue $c$; intervening inactive hits
contribute $q_i$. There is no condition outside the resulting interval.

For a never-active prime, expand its entire product and group every subset
of size at least two by its first and last indices. The empty and singleton
subsets contribute

$$
b_p=1-\frac1p\sum_i\eta_i.
$$

The contribution with endpoints $j<i$ is

$$
\frac{\eta_j\eta_i}{p}\,
\mathbf1_{h_j\equiv h_i\pmod p}
\prod_{j<t<i}(1-\eta_t\mathbf1_{h_t\equiv h_j\pmod p}).
\tag{M2}
$$

Thus, after extracting $\prod_{p\ {\rm big}}b_p$, each represented prime
has one interval of existence, possibly with no active visit. Repeated
inactive hits are retained in its product; they are not independent draws.
For large $x$, $p\ge P_*:=\exp(L^c)\gg N$, so $b_p>0$.

In a physical path, a prime active on both ends of an edge divides $kD$.
All group primes exceed $|k|$. The free-label ban and the distinctness of
each physical list force that prime to be one of the prescribed shared
labels. A prime entering or leaving unshared cannot divide $D$. Hence each
maximal active run has exactly one factor $V_g^{-1}$. A prime with $r$
active runs therefore has required total factor

$$
\frac{V_g^{-r}}{p b_p}.
\tag{M3}
$$

This argument is unchanged for negative $k$.

Use $\nu_g(p)=(V_g p b_p)^{-1}$ for an active birth and
$\lambda_g(p,r)=\nu_g(p)$ with **counting** measure on residues. An active
birth followed by $r-1$ promotions supplies (M3). A ghost birth supplies
$V_g\nu_g(p)$ and $r$ promotions supply $V_g^{-r}$, again giving (M3).
Prescribing a later zero residue costs one point of counting measure, not
another $1/p$.

Choose $\rho$ with $\sqrt q<\rho^2<1$. At an inactive internal hit the
incoming edge, visit, and outgoing edge give
$\rho(q_i/\rho^2)\rho=q_i$. A ghost endpoint gives
$\rho(-\eta_i/\rho)=-\eta_i$ in the appropriate order. Promotion precedes
the visit operation and storage follows it, so active visits acquire none
of these inactive-hit factors. Empty initial and terminal memories account
for the boundary visits with $q_0=q_N=\sqrt q$.

Under distinct birth values, the active visits and the two optional ghost
endpoints determine every storage, promotion, and death. Conversely these
operations recover precisely one term of (M1) or (M2). The $1/b!$ for an
unordered ghost batch removes its orderings. This establishes the exact
memory identity rather than a probabilistic analogy.

## Factorial adjoints, including numerical coincidences

Consider a ghost operation in one group. Write
$A=q_i/\rho^2$, $D=-\eta_i/\rho$, and $C=V_gD$. Suppose a row deletes
$t$ zero particles, keeps $k$, and creates $b$. In its inner product the
factorial measure and deletion choice combine as

$$
\frac1{(k+t)!}\binom{k+t}{t}\frac1{b!}
=\frac1{k!t!b!}.
\tag{M4}
$$

The joint integral consequently has factor
$A^{z(u)}D^tC^b$ against $\lambda_g^k\nu_g^t\nu_g^b$. Swapping the
deleted and created variables proves that the adjoint interchanges $C,D$.
No reciprocal-prime factor appears. This remains true on numerical
diagonals: selections are of particle indices, and symmetric integration
retains their multiplicities.

For the Schur weight $w=v^j$, the absolute row ratio is

$$
\exp(|C|v\nu_g(\mathcal P_g))
       (A+|D|/v)^{z},
\tag{M5}
$$

and the column ratio interchanges $C,D$. Choose fixed $v$ sufficiently
large that

$$
\frac{q_i}{\rho^2}+
\frac{2\max(1,v_+)\eta_i}{\rho v}<1
$$

for both possible $q_i$. This also covers doubling every ghost-birth
coefficient. Since $\nu_g(\mathcal P_g)=1+O(N/P_*)$, the cost is a
constant per group, hence $L^{C_v}$ overall. Crucially, $C_v$ does not
depend on $J$, the probes, or the comparison coefficient exponent.

For an edge, let $a$ target slots be promoted from memory and $b$ source
slots be stored. If the input memory has size $j$, selecting its ordered
promotion indices leaves measure

$$
\frac{(j)_a}{j!}=\frac1{(j-a)!}
=\frac{(j-a+b)_b}{(j-a+b)!}.
\tag{M6}
$$

The second expression is the reversed retrieval of the original stores.
The old residues of promoted particles are $-\Delta$ and the new residues
of stored particles are $\Delta$, where $\Delta=\pm kD$. They are
nonzero because these particles cannot divide $D$. Translation preserves
counting measure. In the reversed row convention the additional scalar
is $V_g^{b-a}$, bounded per group because $a,b\le\ell+m$.

The number of ordered promotions from $z$ eligible pending particles is
controlled together with their unused output damping:

$$
(z)_a\rho^{z-a}\le \sup_{t\ge a}(t)_a\rho^{t-a}<\infty.
\tag{M7}
$$

Storage choices, the factors $v^{b-a}V_g^{-a}$, and fresh integrations
have bounded cost per group. Reversal gives the column estimate. Thus the
absolute edge bounds are $L^{C_a}$, with $C_a$ independent of $J$.
Arbitrary local multipliers of modulus at most one preserve these bounds.

Set $B_{\rm mem}=\lceil L^2\rceil$. At most
$(\ell+m)|\mathcal B|N$ particles can enter memory by storage. Exceeding
the cutoff therefore requires at least
$B_{\rm mem}-O((\ell+m)sN)$ ghost births. Doubling those births in the
absolute evolution gives an omitted mass at most

$$
2^{-B_{\rm mem}+O((\ell+m)sN)}L^{O(N)}
=\exp(-\Omega(L^2)).
\tag{M8}
$$

The initial and terminal empty-memory vectors have bounded norm. For the
small part this is the normalized distinct-list harmonic sum, at most one;
for the big part it is
$\prod_g\nu_g(\mathcal P_g)^M=1+o(1)$.

## Why dirty edges are rare and clean edges use the ideal norm

Fix a source state, all big choices, and the free labels. In each small
group the source symmetrization omits a uniform $\ell$-subset of its $M$
distinct primes. If $F$ is the full small-label product and $U$ the omitted
product, the small part of the step is $F/U$. There are

$$
\mathcal D=\binom{J+\ell}{\ell}^{|\mathcal S|}
$$

distinct possible positive integers $U$, each at most
$\exp(O(TL^b))<P_*$. For an eligible pending particle $(p,r)$,

$$
r\pm kD_{\mathcal B}F/U\equiv0\pmod p
\tag{M9}
$$

has at most one of these solutions: its nonzero factors are units modulo
$p$, and the $U$ are distinct modulo $p$. If $r=0$ there is no solution.
At most $B_{\rm mem}$ omission choices can enable any promotion. The
coefficient depends only on big labels, so conditioning has not biased the
small omission law. Combining the improved row bound with the unrestricted
column bound gives $L^{C_a}\sqrt{B_{\rm mem}/\mathcal D}$. Reversal
applies the same argument to stores. The total dirty norm is at most twice
that quantity.

On a clean edge no particle enters or leaves memory. Absorb the two
pending-zero damping multipliers and memory projections into the endpoint
test vectors. They are contractions and commute with active-list
symmetrization. Fix the $J$ shared labels in each small group. Summing the
remaining $\ell$ small slots with half of the joint normalization at each
endpoint gives maps $P_{\mathbf d}$ satisfying

$$
\sum_{\mathbf d}\|P_{\mathbf d}w\|^2
\le L^{C_s}\|w\|^2.
\tag{M10}
$$

To check the exponent, the one-group multiplier relative to the original
state measure is bounded by

$$
\sup_{z\ge M}q^{z-M}
                 (z-M+\ell)_\ell/V_g^\ell,
$$

a constant independent of $J$ and of the comparison family. Fourier
transformation on the unrestricted small residues and the pending residues
turns translation into $e(\pm\Theta D_{\mathcal B})$. Fixing pending
prime lists makes $\Theta$ independent of the active big labels, including
when an active value happens to equal a pending one.

The remaining big-label operator is the ideal operator or its adjoint.
Changing $\mu_g$ to $\nu_g$ changes its norm by at most
$O_J(L^{C_1}sN/P_*)$ under the square-root-density identification.
Forbidding free/active coincidences costs at most
$O_{J,m}(L^{C_1}s/P_*)$ by row and column estimates: a free draw has atom
$O(P_*^{-1})$ and there are only $O_{J,m}(s)$ relevant comparisons.
Both errors beat every fixed negative logarithmic power. Together with
(M10), the clean norm is at most $2L^{-E_{\rm id}+C_s}$.

Choose $G>E+C_v+3$ and $E_{\rm id}>G+C_s+2$ first. After the comparison
family has fixed $C_a$, choose $J$ so that

$$
\frac{c_0}{2}\log\binom{J+\ell}{\ell}>C_a+G+3.
$$

Then each signed truncated edge has norm at most $L^{-G}$. The exponents
that determine the ideal target do not depend on the later choice of $J$.

## Strongest collision attack

A single absolute collision estimate would fail. Its factor $P_*^{-1}$
would have to absorb a possible $L^{CN}$ absolute path cost, whereas
$\log P_*=L^c=o(N\log L)$. This remains a threat when an early prime is
dropped and a much later fresh birth is forced to equal it: the ordinary
state no longer remembers the early value.

Let potential birth addresses include initial slots, fresh target slots,
and ordered ghost-batch coordinates. There are $A_*=L^{O(1)}$ addresses
under the memory cutoff. For disjoint blocks of addresses of size at least
two, assign coefficient
$\prod_B(-1)^{|B|-1}(|B|-1)!$ and require all their addresses to occur and
to have equal values within each block. The signed sum is exactly the
distinctness indicator. Indeed it is the sign sum of permutations preserving
each numerical-value class, which vanishes on a class of size at least two
by multiplication by a transposition.

If $r=\sum_B(|B|-1)$, there are at most $2r$ affected addresses, and
the total absolute coefficient at rank $r$ is at most $A_*^{2r}$.
This follows, for example, by taking the coefficient of $t^r$ in
$\prod_{j=0}^{A_*-1}(1+jt)$ and bounding it by
$(\sum_jj)^r/r!$.

For large rank, condition on the chronologically first value in each block.
Every subsequent constrained birth is a genuinely fresh integration with
atom $O(P_*^{-1})$. In an edge its step and promotion choices were already
fixed before fresh target values were integrated. In a ghost operation the
ordered batch still has its factorial divisor. Retaining pivot values in
the conditioning even after their particles die allows backward induction
using the uniform row bounds. The fixed-block contribution is bounded by

$$
L^{C_h(N+1)}(C/P_*)^r.
\tag{M11}
$$

For small rank, encode an equality with a dead pivot at its two births:

$$
\mathbf1_{p_1=p_0}=
\int_0^1 e(t p_1)e(-t p_0)\,dt.
\tag{M12}
$$

No value must then travel in the state after the pivot dies. For a larger
block use one such phase for each nonpivot. At fixed Fourier parameters,
only the birth operations in that block change. At most $2r$ edges lose
their signed estimate; all other edges keep their whole pattern sum and
symmetrizations. Initial-birth phases preserve the boundary norm. An
ordered ghost-batch multiplier can be averaged over its permutations,
since the remaining integrand is symmetric; its modulus stays at most one
and (M4) still supplies its adjoint bound. Thus this route gives

$$
O\left(L^{(-G+C_v)N+C_v+2r(G+C_a)}\right).
\tag{M13}
$$

Split the rank sum at
$r_0=\lceil C''N\log L/L^c\rceil$. Summing (M11) with the coefficient
bound gives $o(L^{-EN})$ when $C''$ is large enough. Since $r_0/N=o(1)$,
summing (M13) below $r_0$ gives
$L^{(-G+C_v+o(1))N}=o(L^{-EN})$. This defeats the dead-pivot attack
without replacing signed contraction by one absolute collision estimate.

## Return to integer roots and endpoint pairings

The product of distinct active primes has logarithm
$O_J(NTL^d)=o(L)$ because $0.52+d<1$. Factor out all deterministic
damping belonging to these primes before approximating any average. For
the remaining primes write the damping as $\prod_p(1-X_p)$ with
$0\le X_p\le1$. The sum of independent expectations is $O(NT)$.
Consecutive Bonferroni truncations at degree $h\asymp NT$ have expectation
gap at most $\lambda^h/h!$. Choosing its constant large yields any required
$\exp(-A NT)$ relative precision.

The number of residue terms is $\exp(O(h(L^d+\log N+\log s)))=\exp(o(L))$.
Their CRT counting errors on $[X,2X)$, $X\ge x^\gamma$, total
$\exp(-\gamma L+o(L))$, negligible relative to
$Q_{\rm act}^{-1}\exp(-O(NT))$. The possibly much smaller deterministic
damping has already been factored identically in the two models. Absolute
path mass is $L^{O(N)}$ by the physical row bound and initial normalized
list mass at most one, so the relative errors can be summed. The exact
return condition is the integral of $e(\theta h_N)$ over $[0,1]$.
Restoring this condition, the memory tail, and the residue error gives the
root moment used in Theorem 3.5.

Finally, set $B_0=\mathcal A\mathcal A^*$. On a position block $I_j$ of
length comparable to the maximum step $H$, the matrix
$G_{nm}=\langle u_n,B_0^Ru_m\rangle$ is positive semidefinite. Its
largest eigenvalue is at most its trace. Mark independence gives
$f_j=\sum_{n\in I_j}f_nu_n$ and hence

$$
\langle f_j,B_0^Rf_j\rangle
\le \Bigl(\sum_{n\in I_j}|f_n|^2\Bigr)
       \sum_{n\in I_j}\langle u_n,B_0^Ru_n\rangle.
\tag{M14}
$$

This uses the coefficient norm in the $u_n$ expansion; it does not assume
equal norms for the $u_n$. Spectral Hölder bounds the pairing by
$\|g_j\|\|f_j\|^{1-1/R}$ times the $1/(2R)$ power of (M14).
Since $\log H=O_J(TL^d)$ and $\sup|f_n|\le\exp(O(\sqrt L))$,

$$
(O(H)\sup|f_n|^2)^{1/(2R)}=O(1).
$$

The $H$-neighborhoods used to restrict $g$ have bounded overlap. Hölder
over blocks with exponents $2$, $2R/(R-1)$ and $2R$, followed by the root
moment, gives $|\langle f,\mathcal Ag\rangle|\ll XL^{-E+2C_3}$.
The unnormalized mark fibers and either shift sign are therefore covered.

No computation or finite sampling is used in this derivation.
