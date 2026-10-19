---
name: research/erdos_699/proofs/details/index_7_effective
title: "Erdős 699: index 7 is effective"
desc: "Joint cofactor inequalities from unequal Padé blocks, integer polynomial certificates, and exact rational separation give an effective bound for every bad triple at index seven."
created: 2026-09-22T07:15:20Z
updated: 2026-10-14T00:26:52Z
---

# Erdős 699: index 7 is effective

[[research/erdos_699/_index|P699 research]] ·
[[problems/factorials_binomials/E0699/_index|Erdős problem 699]]

***

**Theorem.** There is an effectively computable integer $N_7$ such that
no bad triple $(n,7,j)$ has $n\ge N_7$, for the original threshold
$p\ge7$.

The [checker](../../computations/erdos_699_index_7_effective.py) and
[certificate](../../computations/erdos_699_index_7_effective.json)
retain a complete finite proof. Its coefficient and Padé thresholds are
effective. The [subsequent numerical proof](../../archive/previous_bounds/index_7_numerical_tail.md)
gives $N_7=10^{3906174477003}$, and a separate
[finite certificate](index_7_finite.md) excludes a lower
range. The new interval covers now join these ranges and give complete exclusion.

The retained proof uses $49$ polynomial certificates and $258$ joint
source inequalities. Its $540$ initial cases have $4,294$ tree nodes and
$3,356$ exact rational infeasibility certificates. The largest jet matrix
has $9,792$ rows.

The main change is to use joint restrictions on the three cofactors.
Replacing every analytic estimate by a separate alternative between two
individual cofactor bounds discards information needed at this index.

**Complete result.** The [combined proof](index_7_complete.md)
excludes every admissible bad triple at seven. The source and
polynomial estimates below are retained as components of that proof.

## Reducing the positions

For $p\in\{2,3,5\}$ choose $r_p\in\{0,\ldots,6\}$ maximizing
$v_p(n-r_p)$, and put

$$n-r_p=P_pu_p,\qquad P_p=p^{v_p(n-r_p)},\qquad
h=n-6,\qquad e_p=\frac{\log u_p}{\log h}.$$

Every admissible row has $n\ge16$. Since each small prime occurs among
the seven numerator factors, $P_p\ge p\ge2$. Hence
$1\le u_p\le n/2<h$ and $0\le e_p<1$.

The [fixed-slope proposition](../../archive/other_approaches/low_crt_row_zero.md) shows
that every bad triple satisfies

$$v_2(n)-v_2(j)\ge3\quad\text{or}\quad
v_3(n)-v_3(j)\ge2\quad\text{or}\quad
v_5(n)-v_5(j)\ge2.$$

In particular, at least one selected position is zero. The main checker
repeats that proposition's 780 exact slope-and-residue cases.

Coincident selected positions are handled by one polynomial certificate:
the product of the selected prime powers at a common position divides
$n-r$, so the whole group has capacity one. With three primes and a
coincidence, there are at most two such capacities. Rearrangement and
nonincreasing row multiplicities cover every repeated-position assignment.

For distinct positions, there are $90$ assignments containing zero. The
five retained old pair alternatives have six componentwise minimal
witness vectors:

$$
\begin{gathered}
(.2679,.2921,0),\quad(0,.2921,.2711),\quad
(.2921,.2916,0),\\
(.3296,.2562,0),\quad(.3296,0,.3774),\quad
(.2676,.2921,.2679).
\end{gathered}
$$

At least one vector gives coordinatewise lower bounds for $(e_2,e_3,e_5)$.
The exact proof covers all $90\cdot6=540$ resulting cases.

## The central column and polynomial factors

The central column is always good at index seven. Suppose $n$ is even.
The three odd integers $n-1,n-3,n-5$ are pairwise coprime and exceed seven.
If one has a prime factor at least eleven, that prime is active in
$\binom n7$. Otherwise one of the three integers is a power $7^a$ with
$a\ge2$, so seven is active. In either case, for an odd offset
$r\in\{1,3,5\}$ and an active prime power $p^a\mid n-r$,

$$
\frac n2\bmod p^a=\frac{r+p^a}{2}>r.
$$

Kummer therefore supplies a common prime at the central column.
Thus a bad triple has $j<n/2$.

This permits coordinate factors, row factors, and a diagonal factor in
the interpolation certificates:

$$
H(X,Y)=\prod_{a=0}^{6}((X-a)(Y-a))^{h_a}
       \prod_{t=0}^{6}(X+Y-t)^{\ell_t}(X-Y)^k.
$$

All are nonzero at $(j,n-j)$ in the remaining domain. The residual
multiplicity at a grid point $x+y<7$ is

$$
R_{xy}=\max\{0,m_{x+y}-h_x-h_y-\ell_{x+y}-k\mathbf1_{x=y}\}.
$$

Each retained symmetric jet matrix has full row rank modulo $251$.
The [nonvanishing lemma](../../methods/details/jet_nonvanishing.md) then gives
an integer polynomial family, of the stated degree, with the prescribed
row multiplicities and at least one nonzero value at $(j,n-j)$.
One certificate uses two coprime degree-$D$ kernel polynomials to save
the extra degree in the general nonvanishing construction. Their full
row rank, two actual modular kernel vectors, bivariate gcd equal to one,
and a full-degree member are all checked. The
[coprime-kernel lemma](../../methods/details/coprime_kernels.md) lifts them to
coprime integer polynomials and bounds their common zeros. For this
certificate, every common zero has $X+Y<10^{775\,415\,594}$.

Factoring the row and diagonal lines is useful here: some otherwise
plausible degree counts have forced line factors and do not give
surjective jet maps.

## Joint Padé inequalities

The source estimates come from the
[unequal-block Padé construction](../../methods/details/off_diagonal_pade.md).
For a selected seed and positive integer directions $(A,B,C)$, let
$c_0,k_0$ be its two certified decay rates. A positive rational parameter
$t$ chooses the common approximation index $m\sim t\log h$.

For a prime component of seed exponent $a_p$, multiplicity $w_p$, and
block length $L_p$, the denominator-clearing cost is

$$
\left(tL_pa_p\log p-w_p(1-e_p)\right)_+.
$$

The integer Padé inequality implies that, above an effective height,

$$
\sum_p\left(tL_pa_p\log p-w_p(1-e_p)\right)_+
\ge \min\{tc_0,tk_0-\nu\}-\epsilon,
\tag{1}
$$

where $\nu=1$ for two individual factors and $\nu=2$ for an AP product
identity. The latter is used only when the actual selected positions
satisfy $r_a+r_b=2r_c$; its nonzero product gap is at most $36$.

Every source uses a finite rational prime-interval sum with a strictly
smaller rational coefficient-gcd rate. Directed interval arithmetic then
rounds the positive-part intercepts upward and the right side of (1)
downward, retaining a positive margin. Consequently the proof uses only
rational inequalities

$$
\sum_p(g_p+w_pe_p)_+\ge T,\qquad T>0. \tag{2}
$$

The [source-clause helper](../../computations/erdos_699_off_diagonal_clauses.py)
recomputes these rational bounds. All analytic approximations have already
been removed before the final linear-algebra verification.

## Exact polynomial cuts and finite separation

Let $F$ be a nonvanishing polynomial supplied by a retained certificate,
with total degree $D$ and row multiplicities $m_0,\ldots,m_6$. Badness,
Kummer localization, and the selected cofactor bounds give

$$
h^{\sum_{t\notin\{r_2,r_3,r_5\}}m_t-D+
            \sum_{p\in\{2,3,5\}}m_{r_p}e_p}
\le C_F. \tag{3}
$$

Here $C_F$ is explicitly computable. One may take

$$
C_F=2^{D+3\max m_t}\|F\|_1(7!)^{\max m_t}.
$$

The factorial accounts for the small-prime factors away from their
selected positions and for the possible cancellation of one factor of
seven in $7!$. The coefficient norm is bounded effectively by maximal
minors of the verified jet matrix.

Fix the exact slack $\delta=1/10000$. Beyond the computable height
$C_F^{1/\delta}$, (3) gives the necessary rational linear inequality

$$\sum_pm_{r_p}e_p
\le D-\sum_{t\notin\{r_2,r_3,r_5\}}m_t+\delta. \tag{4}$$

The proof includes the positive slack in every polynomial cut. It never
replaces the limiting inequality by an unjustified strict boundary.

For each of the 540 initial cases, the certificate gives a finite tree.
An internal node selects an applicable instance of (2) and branches over
all nonempty sign sets. In each branch the signs and (2) become ordinary
rational linear inequalities. At a leaf, the
[exact Farkas checker](../../computations/erdos_699_rational_farkas.py)
verifies positive rational weights $\lambda_s$ such that

$$\sum_s\lambda_s a_s=0,\qquad
  \sum_s\lambda_s b_s<0$$

for the leaf's inequalities $a_s\cdot e\le b_s$. Their weighted sum is
impossible. Every leaf uses at most four inequalities.

Every child of every branch is present, all source position conditions
are checked, and every initial position-and-vector case occurs exactly
once. The coefficient and common-zero bounds together give the evaluated
polynomial height threshold $h\ge10^{19\,813\,540\,001}$. This original proof
left some source thresholds unevaluated; the linked numerical follow-up
evaluates all of them using relaxed clauses and sharper polynomial bounds.
Taking the maximum of the source and polynomial thresholds proves the theorem. Numerical
optimization was used to discover the certificate; no numerical optimizer
is used to verify its rational separation argument.
