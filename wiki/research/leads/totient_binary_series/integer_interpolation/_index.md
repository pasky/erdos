---
name: research/leads/totient_binary_series/integer_interpolation
title: Integer Interpolation of Shifted Totients
desc: |
  Normalized shifted-totient vectors span the full integer lattice beyond
  every cutoff, giving finite two-sided gap multipliers at every order;
  a weighted coefficient bound for their complete tails remains open.
sources: []
problems:
- 249
research_state: ready
review_status: unreviewed
created: 2026-09-17T07:59:31Z
updated: 2026-10-14T00:26:52Z
---

# Integer Interpolation of Shifted Totients

[[research/leads/totient_binary_series/_index|..]]

[[research/leads/totient_binary_series/integer_interpolation/carry_criterion|carry_criterion]]: Two carry conditions retain complete-tail control and admit small finite
witnesses; positivity refutes the proposed uniform character bound, while
separate tail and residue depths leave a less restrictive construction.

[[research/leads/totient_binary_series/integer_interpolation/computation|computation]]: Exact finite certificates for the first full shifted-totient integer image
and weighted costs of specified inhomogeneous solutions.

[[research/leads/totient_binary_series/integer_interpolation/evidence/_index|evidence/]]: Exact right inverses, predecessor obstructions, and weighted target
solutions for nine finite shifted-totient interpolation systems, and
exact witnesses of the aggregated carry criterion through order 384,
and an exact exercise of the shadow bridge at four depths.

[[research/leads/totient_binary_series/integer_interpolation/geometry|geometry]]: Progression means control real solutions; Linnik's theorem gives an
effective integer cost exp(O(k^2 log k)), still above the required scale.

[[research/leads/totient_binary_series/integer_interpolation/phase_localization|phase_localization]]: Multiplicative relations inside the short window localize every small
phase near a dyadic phase with a controlled odd numerator, yielding
a subsequence equivalence and a finite exact separation test.

[[research/leads/totient_binary_series/integer_interpolation/phase_transference|phase_transference]]: A Gaussian comparison gives a quantitative converse to the odd-kernel
phase obstruction; the totient recurrence reduces the relevant quotient
to two dimensions and removes the polynomial loss from the asymptotic
phase criterion on linearly growing supports.

[[research/leads/totient_binary_series/integer_interpolation/shadows|shadows]]: Two exact kernel vectors with non-proportional shadows exclude every
denominator below 2^J over their cost; a rational value makes every large
depth flat, an irrational value leaves infinitely many depths non-flat, and
rounding turns two shadows and an odd starting vector into a cheap odd
kernel vector.

[[research/leads/totient_binary_series/integer_interpolation/two_depth_carries|two_depth_carries]]: Separate-depth carry and homogeneous scalar-kernel criteria control the
full binary tail; odd pairing is feasible, while its uniform weighted cost
remains open and does not follow from generic short kernel vectors.

***

The [[research/leads/totient_binary_series/_index|binary totient argument]]
needs an arithmetic construction as well as tail control. This page proves
integer solvability of one growing family of finite interpolation problems. It
does not bound the size of the solutions as their order increases. All arguments
are author-recorded and unreviewed; they do not resolve
[[problems/irrationality/E0249/_index|Problem 249]].

The external theorem used below is Dirichlet's infinitude of primes in
every reduced arithmetic progression. Its statement was inspected on
p. 1 of [Dirichlet's 1837 paper, translated by Ralf Stephan,
arXiv:0808.1408v2, 24 November 2014](https://arxiv.org/pdf/0808.1408v2).
The analytic proof is not reconstructed here. The other ingredients are
the Chinese remainder theorem, elementary totient divisibility, and
integer linear algebra. No native L-claim or numerical experiment is
needed for the proof.

The fresh-prime separation mechanism has a closely related antecedent in [Will
Cook's Plectis note, “A Basis for the 2-Kernel of Euler's Totient,” the
evaluation-matrix
section](https://wcook04.github.io/plectis/maths/problems/erdos_249.html). That
section's displayed proof was inspected on 2026-09-17: it suppresses other
affine forms modulo a chosen prime to prove rational independence. Here the
slopes are all one, normalization by two permits separation modulo every prime,
and the conclusion is the full integer image of the evaluation vectors. No
literature novelty claim is made. The rest of that source's proofs and its
reported formal checks are not dependencies or independently verified here.

## The integer span

For distinct integers $s_1,\ldots,s_r$, $r\ge1$, fix an integer $B$ such
that $B+s_j\ge3$ for every $j$. Set

$$
v(n)=\left(\frac{\varphi(n+s_1)}2,\ldots,
           \frac{\varphi(n+s_r)}2\right)\in\mathbb Z^r,
\qquad n\ge B.
$$

**Theorem 1.** The integer span of these vectors is all of $\mathbb Z^r$.
In particular, every prescribed integer vector is a finite integer
linear combination of shifted-totient vectors with indices beyond $B$.
The lower cutoff is arbitrary; the coefficients and selected indices
can depend on it and on every shift.

*Proof.* Fix any prime $p$ and any coordinate $j_*$. For each $j\ne j_*$,
choose a distinct prime $q_j\equiv1\pmod{2p}$ larger than $2p$ and every
$|s_i-s_{j_*}|$. Dirichlet supplies these finitely many primes. Prescribe
a prime parameter $t$ by

$$
t\equiv-1\pmod{2p},\qquad
 t\equiv s_{j_*}-s_j\pmod{q_j}\quad(j\ne j_*).
$$

The moduli are pairwise coprime, and every prescribed residue is a
unit: the shift differences are nonzero and smaller in magnitude than
the corresponding $q_j$. Thus the combined class is reduced. Dirichlet
gives arbitrarily large primes $t$ in it. Put $n=t-s_{j_*}\ge B$.
At the selected coordinate,

$$
\frac{\varphi(n+s_{j_*})}{2}=\frac{t-1}{2}
 \equiv-1\pmod p.
$$

This includes $p=2$, when $t\equiv3\pmod4$. At every other coordinate,
$q_j\mid n+s_j$, hence $q_j-1\mid\varphi(n+s_j)$. Since
$2p\mid q_j-1$, that normalized coordinate is zero modulo $p$.
Consequently the vectors $v(n)$ generate every coordinate direction
modulo every prime $p$.

Let $L$ be their integer span. The vectors just found for $p=2$ contain
$r$ linearly independent vectors over $\mathbb Q$, because their
reductions modulo two are independent. Hence $L$ has finite index in
$\mathbb Z^r$. If this index exceeded one, choose a prime dividing it.
An integer basis of $L$ has determinant divisible by that prime, so its
image modulo that prime is a proper subspace. This contradicts the
coordinate directions already constructed. Thus $L=\mathbb Z^r$.
$\square$

This is integral solvability, stronger than full rank over $\mathbb Q$.
It implies that some finite interval already generates the full lattice,
but gives no explicit bound for its endpoint or any estimate uniform in
the number of shifts. Each vector in the integer span uses only finitely
many generators by definition.

There is a terminating, unquantified search for any fixed instance:
enumerate the vectors in increasing $n$, maintain their integer span,
and stop when it is $\mathbb Z^r$. The theorem guarantees eventual
termination. An integer normal-form algorithm then expresses the
requested target. No running-time or coefficient-height estimate is
asserted by this description.

## Exact cancellation of a finite interval

Write $A(x)=\sum_{n\ge1}\varphi(n)x^n$. Fix any integer $k\ge3$ and any
$B\ge k+2$. Apply Theorem 1 to the $2k$ shifts

$$
-k+1,-k+2,\ldots,0,1,\ldots,k
$$

and target vector equal to zero at nonpositive shifts and $-\varphi(s)$
at positive shift $s$. There are finitely supported integers $y_n$,
$n\ge B$, such that

$$
\sum_n y_n\varphi(n+s)=
\begin{cases}
0,&-k<s\le0,\\
-2\varphi(s),&1\le s\le k.
\end{cases}
\tag{1}
$$

The vector $y$ is not zero, because the target at $s=1$ is nonzero.
Let $N=\max\{n:y_n\ne0\}$ and define

$$
P(x)=2x^N+\sum_n y_nx^{N-n}\in\mathbb Z[x].
$$

Then $P$ has leading coefficient two and no other terms in degrees
$N-k,\ldots,N-1$. Moreover

$$
[x^{N+s}](PA)=0\qquad(-k<s\le k).
\tag{2}
$$

Indeed the contribution from $2x^N A$ is zero for $s\le0$ and
$2\varphi(s)$ for $s>0$; equation (1) cancels it. In particular the
central coefficient is zero, as well as both adjacent gaps.
Thus such normalized integer polynomials exist at every order $k$.
Their degrees and coefficient sizes remain uncontrolled.

The normalization two is minimal among positive integer leading
coefficients with these following gaps. Modulo two,
$A(x)\equiv x+x^2$. Vanishing at degrees $N+1,N+2$ forces first
$p_N+p_{N-1}\equiv0$ and then $p_N\equiv0$. No odd leading
coefficient is possible.

## The complete tail in the same parameters

Put $S=A(1/2)$ and retain the exact tails
$T_n=2^nS-\Phi_n$, where
$\Phi_n=\sum_{r\le n}\varphi(r)2^{n-r}$. For any solution of (1), set

$$
\Lambda_k=2S+\sum_n y_nT_n=uS-v,
\qquad
u=2+\sum_n y_n2^n,\quad v=\sum_n y_n\Phi_n,
$$

and define the positive integer cost

$$
C_k(y)=2(k+2)+\sum_n|y_n|(n+k+2).
\tag{3}
$$

The sum over $n$ is finite. The following hold for this same $k$ and $y$:

$$
u\equiv2\pmod{2^k},\qquad v\equiv0\pmod{2^k},\qquad
|\Lambda_k|\le 2^{-k}C_k(y).
\tag{4}
$$

For the first congruence use $n\ge B\ge k+2$. For the second expand
$\Phi_n\equiv\sum_{r=0}^{k-1}2^r\varphi(n-r)\pmod{2^k}$ and apply
the nonpositive-shift equations in (1). For the bound, absolute
convergence and the positive-shift equations give

$$
\Lambda_k=\sum_{j>k}
 \left(2\varphi(j)+\sum_n y_n\varphi(n+j)\right)2^{-j}.
$$

Use $\varphi(t)\le t$ and the exact sums
$\sum_{j>k}2^{-j}=2^{-k}$ and
$\sum_{j>k}j2^{-j}=(k+2)2^{-k}$. This bounds the entire infinite
remainder and gives exactly (3)-(4); no moving-kernel limit is used.

**Proposition 2.** A solution of (1) excludes every rational value
$S=a/b$, $a,b\in\mathbb Z$, $b\ge1$, with

$$
bC_k(y)<2^k.
\tag{5}
$$

*Proof.* Under that rationality assumption $b\Lambda_k=au-bv$ is an
integer, and (4)-(5) make its magnitude less than one. It would therefore
be zero. But (4) makes it congruent to $2a$ modulo $2^k$. Since
$0<S<2$, we have $0<2a<4b$. Also $C_k(y)\ge2(k+2)>4$, so
$2a<4b<bC_k(y)<2^k$. The residue is nonzero, a contradiction.
$\square$

Consequently an infinite sequence of solutions, with $k\to\infty$ and
$C_k(y)/2^k\to0$, would prove irrationality of $S$. This is a
sufficient condition, with no necessity claim. Theorem 1 supplies
solutions of (1) for each fixed $k$, but supplies no such estimate.

## The remaining construction

For $B=k+2$, let $\Gamma_k$ be the minimum of (3) over all finitely
supported integer solutions of (1). Theorem 1 and the well-ordering of
positive integers show that $\Gamma_k$ is finite and attained for every
$k\ge3$. The still-open useful bound is

$$
\liminf_{k\to\infty}\frac{\Gamma_k}{2^k}=0.
\tag{6}
$$

The
[[research/leads/totient_binary_series/integer_interpolation/geometry|effective
integer bound]], Proposition 4, uses Linnik's theorem and the polynomial
real-rank prefix to prove $\Gamma_k\le\exp(O(k^2\log(k+2)))$, with effective
constants and a support endpoint of the same order. This is an unconditional
quantitative upper bound, but it is too large to establish (6). Its proof
controls both the support and the coefficients; it does not identify the
minimum.

This formulation removes an unknown integrality obstruction: the affine
system is solvable at every order, even after any prescribed lower
cutoff. It does not remove the size obligation. The retained
[[research/leads/totient_binary_series/integer_interpolation/computation|finite
certificates]] give integer right inverses and proper-image obstructions
at the preceding endpoint for $k=3,4,8,12,16,24,32,48,64$. They certify
the least full-image prefixes for these orders, and separately give
36 feasible target solutions. Neither a rank calculation nor this
finite table establishes (6).

For example, at $k=64$ the least full-image endpoint is $R=194$.
A target solution using the larger support interval $66\le n\le386$
has 284 nonzero coefficients, maximum magnitude 314, and cost
$C_{64}=2433103$. Hence $\Gamma_{64}\le2433103$, and (5) excludes
$b\le7581571381774$. This finite exclusion is much weaker than the
continued-fraction exclusion in the main research account; the purpose
here is to measure a constructive interpolation cost. The reported costs
are upper bounds, not minima. All retained solutions impose central
cancellation; they also satisfy the relaxed system below, but no
separate central-free search or minimum is claimed.

Possible next improvements include an explicit arithmetic basis with
controlled coefficients, an estimate for this particular inhomogeneous
integer system, or a different normalization with a smaller full-tail
cost. A homogeneous short vector with the leading coefficient zero
does not provide the prescribed solution. A scalar-kernel vector with
an additional odd prefix pairing can instead serve a different linear
form, as described below. The fresh-prime proof above
uses primes in fixed progressions after fixing all shifts; it cannot be
read as a uniform small-prime construction as $k$ grows.


## The central cancellation can be omitted

For finding a small cost it can be useful to impose only the $2k-1$
conditions

$$
\sum_ny_n\varphi(n+s)=0\quad(-k<s<0),\qquad
\sum_ny_n\varphi(n+s)=-2\varphi(s)\quad(1\le s\le k),
\tag{7}
$$

still with finite integer support $n\ge k+2$. Put
$c_0=\sum_ny_n\varphi(n)$, with no constraint that $c_0=0$.
Theorem 1 also supplies solutions of (7) at every order, by omitting
shift zero. The same definitions of $\Lambda_k,u,v,C_k(y)$ give

$$
u\equiv2\pmod{2^k},\qquad v\equiv c_0\pmod{2^k},\qquad
|\Lambda_k|\le C_k(y)2^{-k}.
\tag{8}
$$

The tail estimate uses only the positive-shift cancellations, so its proof
is unchanged. The backward cancellations at shifts $-1,\ldots,-k+1$
give the new congruence for $v$.

**Proposition 3.** The same condition $bC_k(y)<2^k$ excludes a rational
value $S=a/b$ for a solution of (7), even without central cancellation.

*Proof.* The first three terms of $S$ sum to one and the remaining terms
are positive; also $S<\sum n2^{-n}=2$. Thus $1<S<2$.
Each $\varphi(n)$ in $c_0$ is even, so $c_0$ is even. The integer
$2a-bc_0$ cannot vanish: that would make $S=c_0/2$ an integer in $(1,2)$.
Moreover

$$
0<|2a-bc_0|<b(4+|c_0|)<bC_k(y)<2^k,
$$

since $|c_0|\le\sum_n|y_n|n$ and $C_k(y)\ge2(k+2)+\sum_n|y_n|n$.
But rationality and (8) make $b\Lambda_k$ an integer of magnitude
less than one, hence zero, while its residue modulo $2^k$ is the
nonzero $2a-bc_0$. This is a contradiction. $\square$

Let $\widetilde\Gamma_k$ be the minimum of the same cost over solutions
of (7). Then it is finite and attained, and
$\widetilde\Gamma_k\le\Gamma_k$. A family with
$\liminf_k\widetilde\Gamma_k/2^k=0$ is therefore a weaker sufficient
size requirement. The cost already controls the central coefficient, so
no separate estimate for it is needed for this criterion. The two
interpolation systems should remain distinguished in finite comparisons;
neither minimum has a proved useful asymptotic bound.

## Relation to finite polynomial multipliers

The
[[research/leads/totient_binary_series/sparse_transforms/gap_multipliers|gap-multiplier
criterion]] uses $P(x)=\sum_{i=0}^Np_ix^i$ with $p_N=2$, the preceding
coefficient gap, and the two product gaps flanking $b_N=[x^N]PA$. For a solution
of (7), the exact identification is

$$
p_{N-n}=y_n,\qquad p_N=2,\qquad b_N=c_0,\qquad
\Lambda(P)=\Lambda_k,\qquad E_0(P)=C_k(y)2^{-k}.
$$

Thus Theorem 1 settles qualitative solvability of that affine system at
every order, even with support restricted to $n\ge k+2$. It does not
give its proposed height bound $HN^2/2^k\to0$. The exact weighted
bound above can be smaller than the estimate using maximum height and
all possible coefficients, so the minima in (6) and in Proposition 3
retain the actual support and coefficient weights.

The
[[research/leads/totient_binary_series/sparse_transforms/evidence/_index|five
retained polynomial witnesses]] are finite instances of the product criterion.
Four also meet this page's stricter cutoff and bound $\widetilde\Gamma_k$ at
their particular orders. The $(N,k)=(100,20)$ instance has a reversed
coefficient at $n=k$; it remains valid for the product criterion but does not
bound the minimum defined here. No finite instance supplies an asymptotic
estimate or a claim of optimal height.

The
[[research/leads/totient_binary_series/integer_interpolation/geometry|geometric
sufficient bound]] makes a possible next construction precise. It controls the
weighted cost by the least-norm real solution for this target and the
orthogonalized lengths of an integer kernel basis. These are separate
obligations: bounded kernel geometry alone does not control the target's real
component in a general integer matrix. For these totient matrices, Proposition 2
of that page uses finite progression means to give a singular-value lower
bound on prefixes of length $O(k^3\log k)$ and a specified family of all larger
lengths. The real contribution to the weighted cost is then less than $512k^3$,
uniformly as those prefixes grow. Integral target membership is reached
eventually by Theorem 1, without a quantitative endpoint. Choosing an endpoint
and controlling the weighted cost of integer rounding remain the open
quantitative obligations in this particular construction.

The
[[research/leads/totient_binary_series/integer_interpolation/carry_criterion|aggregated
carry criterion]] weakens the hypothesis of Propositions 2 and 3. The residue
argument uses only $v\bmod2^k$, and the tail bound uses only the single integer
$\sum_{j\le k}2^{k-j}b_{N+j}$, so it suffices that these two aggregates vanish
rather than all $2k$ gap coefficients; the leading coefficient may then be any
nonzero integer. The corresponding minimum $\Gamma^*_k$ satisfies
$\Gamma^*_k\le\Gamma_k$, and its retained exact witnesses at sampled orders
through $k=384$ cost about $2k^2$, against the retained exact-gap costs above. A
proposed uniform character bound on that page is refuted by an unavoidable
scalar character; it supplies no live proof target. The
[[research/leads/totient_binary_series/integer_interpolation/two_depth_carries|two-depth
version]] allows the residue depth to grow slowly while a longer
truncation controls the tail. Leading coefficient one is qualitatively
feasible at every pair of depths. Its exact-slice counting identity
isolates the remaining bounded-coefficient construction without assuming
independence after the scalar equation has been imposed.

The same page's homogeneous criterion is the less restrictive
construction target. For support $n\ge B\ge4$, one needs
$\sum_nz_nU_J(n)=0$ and $\sum_nz_n\Phi_n/2$ odd. Its full-tail bound
is $C/2^J$, where $C=\sum_n|z_n|(n+J+2)$. The valuation gap excludes
every fixed rational denominator along a family with $B\to\infty$ and
$C=o(2^J)$. It needs neither a prescribed nonzero target nor a
residue-repair multiplier. At $B=J\ge4$, the finite sufficient bound
is $bC<2^{J+1}$.

Using the prime number theorem for the fixed modulus 20, an odd
kernel vector on $[J,2J]$ is feasible for every sufficiently large
$J$ with $5\nmid J$, including the subsequence $J=2^m$. The displayed
two-term vector can have cost of order $J^2 2^J$, so this support
result does not supply the needed estimate. A positive-row comparison
family with many short even relations but only expensive odd relations
rules out that generic shortcut. Arithmetic control of the actual
totient row's odd-kernel minimum remains open.

The
[[research/leads/totient_binary_series/integer_interpolation/shadows|shadows page]]
gives a second sufficient construction. Two exact kernel vectors with
non-proportional integer shadows $(u,v)$ exclude every denominator below
$2^J$ divided by their larger cost, without a parity condition. Given
an odd kernel vector, rounding against explicit vectors with zero
shadow also yields an odd vector at polynomial extra cost. With
$B_J=\max(4,\lfloor\log_2(J+1)\rfloor)$, the existence of an odd
$o(2^J)$ family on $[B_J,3J]$ is equivalent to irrationality; the reverse
implication supplies $O(J^4)$ cost along a subsequence. This construction
gives neither an all-depth bound nor an equivalence on $[J,2J]$.

The
[[research/leads/totient_binary_series/integer_interpolation/phase_transference|phase
comparison]] instead bounds the minimum odd cost in terms of the best weighted
alignment of $U_J/2$ with the half-integer phase $\Phi/4$. Explicit vectors with
zero shadow reduce the relevant quotient to two dimensions. On the permitted
linearly growing supports, cost $o(2^J)$ is equivalent to phase error times
$2^J$ tending to infinity. Proving that arithmetic estimate, or constructing the
vectors directly, remains open; neither equivalence retires a method that might
do so.

The
[[research/leads/totient_binary_series/integer_interpolation/phase_localization|arithmetic
localization]] supplies the separate short-support reverse argument. An aligning
phase small enough in terms of $J$ forces a dyadic phase with a bounded odd
numerator; the complete tail gives rational approximants whose common dyadic
factors permit chaining. Consequently $S$ is irrational if and only if
$\epsilon_J2^J$ is unbounded along powers of two, equivalently a short-support
odd $o(2^J)$ family exists along a subsequence. This gives an exact finite
sufficient test over $O(MJ)$ odd numerators for $\epsilon_J>M2^{-J}$, with
explicit structural and size conditions. No unbounded successful family or
all-depth growth estimate has been established.
