---
name: research/sidon_extremal_error/linear_capacity_barrier
title: "Linear-capacity barrier for finite Sidon sets"
desc: "A genuine fixed-size block-sampling law satisfies every Sidon capacity in expectation up to sqrt(N)+N^(1/4)/2-O(1), obstructing single linear-capacity certificates below exponent 1/4; adaptive and nonlinear arguments remain outside this conclusion."
created: 2026-10-15T18:04:27Z
updated: 2026-10-15T18:04:27Z
---

***

The distributions, the pseudo-moment family and the inequalities below are
Plasma AI's author-recorded mathematics. They are not independently reviewed,
and they bound classes of arguments, not the extremal function itself.

## Setting

Let $h(N)$ be the largest size of a Sidon set in $\{0,\ldots,N-1\}$, a
translate of the interval of
[[problems/additive_bases/E0030/_index|Problem 30]]: a set in which
$a+b=c+e$ forces $\{a,b\}=\{c,e\}$, repetitions included. For any set
$A\subset\{0,\ldots,N-1\}$ write

$$
r_A(d)=\#\{a\in A:\ a+d\in A\},\qquad
\sigma_A(s)=\#\{(a,b)\in A^2:\ a\le b,\ a+b=s\}.
$$

A set is Sidon exactly when $r_A(d)\le1$ for every $d\ge1$, and exactly when
$\sigma_A(s)\le1$ for every $s$.

A *linear capacity certificate* at size $k$ consists of a real function $\Psi$
on the $k$-element subsets, numbers $\alpha_d\ge0$ ($1\le d\le N-1$) and
$\beta_s\ge0$ ($0\le s\le2N-2$), and a real $\gamma$, such that for every
$k$-element subset $A$, Sidon or not,

$$
\Psi(A)\le\sum_d\alpha_d\,r_A(d)+\sum_s\beta_s\,\sigma_A(s)+\gamma
\qquad\text{and}\qquad
\Psi(A)>\sum_d\alpha_d+\sum_s\beta_s+\gamma .
$$

Such a certificate proves $h(N)<k$: a Sidon set would satisfy the first
inequality with every multiplicity at most $1$, contradicting the second. In
such a proof the Sidon hypothesis enters only through nonnegative combinations
of the inequalities $r_A(d)\le1$ and $\sigma_A(s)\le1$, while the universally
valid inequality may use anything true of all $k$-sets: integrality of counts,
positivity of every degree, convexity, combinatorial structure.

The sliding-window argument behind
[[../library/additive_bases/erdos_1941_problem_sidon_additive_number_theory_related/theorem_p212_upper_bound|Erdős and Turán's classical bound n^(1/2)+O(n^(1/4))]]
is one. For $1\le T\le N$ let $c_t=|A\cap[t-T+1,t]|$ for
$0\le t\le N+T-2$. Every $k$-set satisfies
$\sum_tc_t^2=kT+2\sum_{d<T}(T-d)\,r_A(d)$ and, by Cauchy–Schwarz,
$\sum_tc_t^2\ge(kT)^2/(N+T-1)$. With $\Psi=(kT)^2/(N+T-1)-kT$,
$\alpha_d=2(T-d)$ for $d<T$ and all other coefficients $0$, the certificate
applies whenever $k^2T>(N+T-1)(k+T-1)$, and $T=\lceil N^{3/4}\rceil$ gives
$h(N)\le\sqrt N+N^{1/4}+O(1)$.

## A distribution that defeats every linear certificate

[[theory/additive_bases/L216_sidon_linear_capacity_barrier/_index|L216 proves the following explicit barrier]]:
for every $N\ge2^{20}$ and every positive integer

$$
k\le\sqrt N+\frac12N^{1/4}-10,
$$

there is a probability measure on the $k$-subsets with
$\mathbb E r_A(d)\le1$ for every ordinary difference and
$\mathbb E\sigma_A(s)\le1$ for every sum, diagonal pairs included. Its proof
partitions the cycle into nearly equal blocks, samples nearly equal fixed
numbers of points independently in the blocks, and rotates the union. The
pair probabilities are obtained by elementary counting. The result is
proved at tier 0, without independent review.

A particularly simple exact family has $s$ blocks of length
$W=s^3-s^2+s$, each containing a uniform $s$-subset. Here
$N=s^4-s^3+s^2$, $k=s^2$ and the pair moments are a cyclic tent of width $W$.
The excess divided by $N^{1/4}$ tends to $1/2$.

**Certificate consequence.** Averaging the first certificate inequality over
this measure gives
$\mathbb E\Psi\le\sum\alpha_d+\sum\beta_s+\gamma$, contradicting the second
inequality. Thus this certificate class cannot prove an upper error
$O(N^\alpha)$ for any $\alpha<1/4$. The law need not be supported on Sidon
sets: it satisfies their capacities only after averaging. The statement
includes every universal inequality on $k$-sets, even of higher degree; its
restriction is the linear use of the capacities with coefficients independent
of the set.

## An alternative realization by independent displacement

The following complete author argument gives the same asymptotic obstruction
through a different distribution. For every fixed $\eta\in(0,1/2)$, it works
for all sufficiently large $N$ and
$\sqrt N\le k\le\sqrt N+(1/2-\eta)N^{1/4}$. Its conditioning and error
estimates are unnecessary for the block construction, but describe the
perturbed-lattice model used in a separate exploratory fourth-moment probe.

**Construction.** Let $s=N/k$, $L_m=\lfloor mN/k\rfloor$ for $m\in\mathbb Z$,
$w=k^2-N$ and $W=w+\lceil N^{2/3}\rceil$. Take $R$ uniform on
$\mathbb Z_N$ and $U_0,\ldots,U_{k-1}$ uniform on $\{0,\ldots,W-1\}$, all
independent, and put $P_m=(R+L_m+U_m)\bmod N$. Let $\mu$ be the law of
$\{P_0,\ldots,P_{k-1}\}$, read in $\{0,\ldots,N-1\}$, conditioned on the event
$\mathrm{NC}$ that the $P_m$ are distinct. It is a lattice of spacing about
$\sqrt N$, each point displaced by up to $W$, about $N^{3/4}$, and rotated at
random.

**Proof.** *Tent law.* For $m\ne m'$, $U_{m'}-U_m$ has the law
$\tau(t)=(W-|t|)_+/W^2$ on the integers. The function $\tau$ on $\mathbb R$ is
$1/W^2$-Lipschitz and has Fourier transform
$\hat\tau(\xi)=\bigl(\sin(\pi W\xi)/(\pi W\xi)\bigr)^2$.

*Lattice sums.* For an integer $x$ let $G(x)=\sum_{m\in\mathbb Z}\tau(x-L_m)$.
Since $|L_m-ms|<1$, at most $2W/s+2$ terms are nonzero and each moves by at
most $1/W^2$ when $L_m$ is replaced by $ms$. Poisson summation gives
$\sum_m\tau(x-ms)=s^{-1}\sum_{\ell}\hat\tau(\ell/s)e(\ell x/s)$, and
$\sum_{\ell\ne0}\hat\tau(\ell/s)\le\frac{2s^2}{\pi^2W^2}\cdot\frac{\pi^2}6$.
Hence

$$
\Bigl|G(x)-\frac1s\Bigr|\le\frac\varepsilon s,\qquad
\varepsilon=\frac{s^2}{3W^2}+\frac2W+\frac{2s}{W^2}
\le\left(\frac13+o(1)\right)N^{-1/3}.
$$

*Cyclic pair counts.* Because $2W<N$, a residue $d$ has at most one
representative $\tilde d$ in $(-W,W)$; set $\tau(\tilde d)=0$ when it has none.
Since $L_{m+k}=L_m+N$,

$$
\Gamma(d):=\sum_{m\ne m'}\Pr\bigl(P_{m'}-P_m\equiv d\bigr)
=\sum_{m=0}^{k-1}G(d+L_m)-k\,\tau(\tilde d)
\le\frac{k^2}N(1+\varepsilon)-k\,\tau(\tilde d).
$$

*Interval counts.* Let $\tilde r(d)$ count the index pairs with
$P_{m'}=P_m+d$ as integers. Given the $U_m$, each $P_m$ is uniform because $R$
is, so a pair with $P_{m'}-P_m\equiv d$ satisfies $P_{m'}=P_m+d$ with
probability $(N-d)/N$. Thus
$\mathbb E\,\tilde r(d)=\frac{N-d}N\Gamma(d)$, and the event $\mathrm{NC}$ does
not involve $R$.

*Conditioning.* Fix a pair $(m,m')$ and let $\mathrm{NC}'$ be the event that
the other $k-2$ points are distinct. It is independent of $U_m$, $U_{m'}$ and
$R$, contains $\mathrm{NC}$, and differs from it only on an event of
probability at most $\sum_{b}\bigl(\Pr(P_b=P_m)+\Pr(P_b=P_{m'})\bigr)
\le2(1+\varepsilon)/s$. Hence

$$
\mathbb E[\tilde r(d)\mid\mathrm{NC}]\le\phi\,\mathbb E\,\tilde r(d),\qquad
\phi=1+\frac{2(1+\varepsilon)}{s\Pr(\mathrm{NC})},
$$

and $\Pr(\mathrm{NC})\ge1-\frac12\Gamma(0)\ge1-\frac{k^2}{2N}(1+\varepsilon)$,
which tends to $1/2$. So $\phi=1+O(N^{-1/2})$. On $\mathrm{NC}$,
$r_A(d)=\tilde r(d)$.

*Capacity.* Write $\delta=k-\sqrt N$, so $w=2\delta\sqrt N+\delta^2\le
(1-2\eta+o(1))N^{3/4}$. For $d>N/2$,
$\mathbb E\,\tilde r(d)\le\frac{k^2}{2N}(1+\varepsilon)$, which tends to
$1/2$. For $1\le d\le N/2$, using $(N-d)(N+w)\le N^2+N(w-d)$,

$$
\mathbb E\,\tilde r(d)\le\Bigl(1+\frac{w-d}N\Bigr)(1+\varepsilon)
-\Bigl(1-\frac WN\Bigr)\frac{k\,(W-d)_+}{W^2}.
$$

For $d\ge W$ the right side is at most
$(1-N^{-1/3})(1+\varepsilon)=1-\Omega(N^{-1/3})$. For $d<W$ it is linear in
$d$, so it suffices to check $d=W$, done, and $d=0$, where it equals
$1+w/N-k/W+O(N^{-1/3})$. Since $k\ge\sqrt N$ and
$w(w+\lceil N^{2/3}\rceil)\le(1-2\eta+o(1))^2N^{3/2}$, one has
$k/W-w/N\ge(4\eta-4\eta^2+o(1))N^{-1/4}/(1-2\eta)$, so the value at $d=0$ is
$1-\Omega(\eta N^{-1/4})$. Multiplying by $\phi=1+O(N^{-1/2})$ keeps every
bound below $1$ for $N\ge N_0(\eta)$.

*Sums.* At most $N/2$ pairs $a<b$ have $a+b=s$, each with
$\Pr(a,b\in A)\le\phi\,\Gamma(b-a)/N\le\phi\frac{k^2}{N^2}(1+\varepsilon)$, and
$\Pr(s/2\in A)\le k/(N\Pr(\mathrm{NC}))$. So
$\mathbb E_\mu\sigma_A(s)\le\frac12+o(1)$. $\square$

The expectations $\mathbb E\,\tilde r(d)$ of the unconditioned process are
integers divided by $W^2N$ and come from one cyclic convolution, so the
conditions can be checked exactly for given $N$ and $k$. With the parameters of
the construction and the factor $\phi$ above, $\max_d\phi\,\mathbb E\,\tilde
r(d)$ is about $0.9974$ at $(N,k)=(16000000,4024)$, and about
$1.0011$ at $(N,k)=(16000000,4028)$. The approach to $1/2$ is slow, through
error terms of relative size $N^{-1/12}$ and $N^{-1/4}$.

## Exact pseudo-moments at the same threshold

The degree-two moment relaxation $R(N,k)$ is the set of real pairs $(x,X)$, $X$
symmetric with indices $0,\ldots,N-1$, satisfying:

1. cardinality: $\sum_ix_i=k$, $X_{ii}=x_i$ and $\sum_jX_{ij}=kx_i$;
2. positivity: the matrix with rows $(1,x^{\mathsf T})$ and $(x,X)$ is positive
   semidefinite;
3. pair literals: for $i\ne j$, $X_{ij}\ge0$, $X_{ij}\le x_i$, $X_{ij}\le x_j$
   and $1-x_i-x_j+X_{ij}\ge0$;
4. difference capacity: $\sum_{i=0}^{N-1-d}X_{i,i+d}\le1$ for
   $1\le d\le N-1$;
5. sum capacity: $\sum_{i<j,\ i+j=s}X_{ij}+[s\text{ even}]\,x_{s/2}\le1$ for
   $0\le s\le2N-2$, the last term present when $s/2\le N-1$.

The indicator $z$ of a Sidon $k$-set gives the point $x=z$, $X=zz^{\mathsf T}$.
Constraints 1–3 hold for every $k$-set. A separation certificate obtained
by a nonnegative linear combination of constraints 1–5 is covered by the
barrier, and the moments of each constructed measure lie in $R(N,k)$. The next theorem gives an explicit rational point, exactly and
for every $N\ge48$.

**Theorem 2.** For every $N\ge48$ and every integer $k$ with

$$
\sqrt N+1\le k\le\sqrt N+\tfrac12N^{1/4}-\tfrac14,
$$

$R(N,k)$ contains the point $x_i=y$, $X_{ii}=y$ and $X_{ij}=y^2-f_{r(i,j)}$ for
$i\ne j$, where

$$
w=k^2-N,\qquad y=\frac kN,\qquad
\lambda=\frac{y-y^2}{w(w-1)},\qquad
f_r=\lambda\max(w-r,0),
$$

and $r(i,j)=\min(|i-j|,N-|i-j|)$ is the cyclic distance. For $N\ge411$ the
interval contains an integer, so the largest $k_R(N)$ with $R(N,k)$ nonempty
satisfies

$$
\sqrt N+\tfrac12N^{1/4}-\tfrac54<k_R(N)\le\sqrt N+N^{1/4}+O(1),
$$

the upper bound by the window certificate above.

**Proof.** Put $s=\sqrt N$, $u=N^{1/4}$ and $\delta=k-s$, so
$1\le\delta\le u/2-1/4$ and $w=2\delta s+\delta^2$. Four parameter facts come
first.

- (a) $2\le w\le N/2$. Indeed $w\ge 2s+1$, and $w\le us+s/4=N^{3/4}+N^{1/2}/4$,
  which is at most $N/2$ for $N\ge48$.
- (b) $k(w+1)\ge N$, since $k\ge s$ and $w+1>s$.
- (c) $w^2\le N(k-1)$. Write $t=u/2-\delta$, so $1/4\le t\le u/2-1$. Then
  $4\delta^2N=N^{3/2}-4tN^{5/4}+4t^2N$, $4\delta^3s\le N^{5/4}/2$ and
  $\delta^4\le N/16$, so
  $w^2\le N^{3/2}-(4t-\frac12)N^{5/4}+(4t^2+\frac1{16})N$, while
  $N(k-1)\ge N^{3/2}$ because $\delta\ge1$. It suffices that
  $g(t)=(4t-\frac12)u-4t^2-\frac1{16}\ge0$. The function $g$ is concave,
  $g(1/4)=u/2-5/16>0$, and $g(u/2-1)=u^2-u/2-65/16\ge0$ for $u\ge2.3$, which
  holds for $N\ge48$.
- (d) $y\le1/2$, since $k\le s+u/2\le N/2$ for $N\ge48$.

*Row identity and positivity.* By (a), every cyclic distance
$r\in\{1,\ldots,w-1\}$ is below $N/2$, so it occurs exactly twice among the
$j\ne i$. Hence

$$
\sum_{j\ne i}f_{r(i,j)}=2\lambda\sum_{r=1}^{w-1}(w-r)=\lambda w(w-1)=y-y^2 .
$$

The matrix $C=X-y^2J$ therefore has diagonal entries
$y-y^2=\sum_{j\ne i}f_{r(i,j)}$ and off-diagonal entries $-f_{r(i,j)}\le0$: it
is the Laplacian of the weights $f$, so
$v^{\mathsf T}Cv=\sum_{i<j}f_{r(i,j)}(v_i-v_j)^2\ge0$ and $C\mathbf 1=0$. This
gives $X\mathbf 1=Ny^2\mathbf 1=kx$ and $\sum_ix_i=Ny=k$, which is constraint
1, and constraint 2 because the Schur complement $X-xx^{\mathsf T}$ equals $C$.

*Pair literals.* By (b), $f_r\le\lambda(w-1)=(y-y^2)/w\le y^2$, so
$0\le X_{ij}\le y^2\le y$, and $1-2y+X_{ij}\ge0$ by (d).

*Difference capacity.* The matrix depends only on cyclic distance, so the sum
in constraint 4 equals $(N-d)(y^2-f_{r(d)})$ with $r(d)=\min(d,N-d)$. By (c),
$\lambda=(N(k-1)-w)/(N^2w(w-1))\ge1/N^2$. For $1\le d<w$ one has $r(d)=d$ and
$y^2-f_d\le(N+w)/N^2-(w-d)/N^2=(N+d)/N^2$, so the sum is at most
$1-d^2/N^2<1$. For $w\le d\le N-w$ the sum is
$(N-d)(N+w)/N^2\le1-w^2/N^2<1$. For $d>N-w$ it is less than
$w(N+w)/N^2\le3/4$.

*Sum capacity.* At most $N/2$ pairs $i<j$ have $i+j=s$, so the left side of
constraint 5 is at most $k^2/(2N)+k/N$, which is at most $1$ when
$(k+1)^2\le2N+1$; this holds for $N\ge48$ because $k\le s+u/2$. $\square$

Condition (c) is the binding one: $(2\delta s)^2\le w^2\le N(k-1)$ forces
$\delta\le(\frac12+o(1))N^{1/4}$, so this family reaches exactly the
coefficient $1/2$. If in addition the first moments are uniform, $x_i=k/N$,
the window means are known exactly near the ends,
$\sum_t\mathbb E(c_t)^2=y^2\bigl((N-T+1)T^2+(T-1)T(2T-1)/3\bigr)$, and the
window chain gives $wT/N\le k-1+(1+w/N)T^2/(3N)$; the choice
$T=\sqrt{3Nk}$ yields $k\le\sqrt N+(3^{-1/2}+o(1))N^{1/4}$. For uniform first
moments the threshold coefficient of $R$ therefore lies between $1/2$ and
$3^{-1/2}=0.577\ldots$; in general it lies between $1/2$ and $1$.

An auxiliary program over circulant pseudo-moments, those with $X_{ij}$
depending only on the cyclic distance, omits the sum capacities. The remaining
constraints form a linear program: the row identity, the difference capacities
and the pair literals are linear, and positivity is the nonnegativity of each
Fourier mode. Solved in floating point with bisection on a real $k$, it gives
threshold coefficients about $0.602$, $0.590$, $0.589$ and $0.585$ at
$N=200$, $500$, $1000$ and $2000$, where the tent family itself reaches about
$0.49$ at $N=2000$ and the finite-$N$ uniform-moment window cap is $0.624$. At
the solver's threshold point almost every difference capacity is tight, the
pair moments exceed $y^2$ at long distances, and a few distances are fully
depleted, so the reported moments use each difference about once on average
at every scale. These figures are uncertified and do not assert feasibility
of the full relaxation $R$. The asymptotic threshold, if it exists, lies in
$[1/2,3^{-1/2}]$ for the auxiliary class and is not determined here.

## What the barrier covers and what it leaves open

L216 restricts single linear-capacity certificates. Its distribution
is a genuine random $k$-set, so every inequality true of all $k$-sets holds
for it, at every degree and with all integrality. It differs from a Sidon set
only in that its multiplicities $r_A(d)$ are small on average rather than $0$
or $1$ in every realization. A proof outside this certificate class may
use the Sidon property nonlinearly, for instance through $r_A(d)^2=r_A(d)$,
through the additive energy identity $\sum_x r_{A-A}(x)^2=2k^2-k$, through the
absence of three-term progressions in every realization, or through the
structure of the set of missing differences. Heuristically the pair counts
under $\mu$ behave like Poisson variables, so its expected energy is near
$2k^2+2N/3$ rather than the Sidon value $2k^2-k$.

Whether the published refinements of the $N^{1/4}$ coefficient (Lindström's
bound, and those of Balogh–Füredi–Roy, O'Bryant, Carter–Hunter–O'Bryant,
Hou–Zhao and Chen recorded on the problem page) are linear capacity
certificates has not been checked against their proofs. O'Bryant's window
identity is linear in the multiplicities $r_A(d)$, but a proof built on it may
also use a nonlinear consequence of the Sidon property. That assessment needs
proof-level reading of each source.

A proof can also escape the corollary without any nonlinear use, by splitting
into cases according to statistics of the set. Carter–Hunter–O'Bryant's
Section 2, read for this purpose, uses the window identity at two lengths
$T'<T$ with only $S\ge0$ from the Sidon property, but bounds the variance
from below through the end profile of the window counts and chooses which
window gives the contradiction according to that profile. Such a disjunction
of restricted inequalities is not itself a certificate of the specified form:
conditioning the measure on one case need not preserve its capacities.
Concentration of the splitting statistics might allow an extension of the
barrier, but would need quantitative margins and control of conditional
capacities. Concentration alone is not asserted to defeat a case split, and no
such extension is proved here.

The
[[research/sidon_extremal_error/degree_four_extension|degree-four account records the first nonlinear constraints and the exact failure of zeroing followed by uniform renormalization for the block law]].
In the cyclic group the same linear constraints already give $k(k-1)\le N-1$,
so the excess $\frac12N^{1/4}$ is an interval boundary effect: the ordinary
difference $d$ has only $N-d$ slots, and the depletion of short-range pairs is
paid by the zero variance of the cardinality.

A search on 2026-10-15 for semidefinite, Lasserre, sum-of-squares or
Lovász-theta treatments of finite Sidon sets or Golomb rulers found none. The
search was not exhaustive, and no novelty is claimed.
