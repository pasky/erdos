---
name: research/smooth_successor_estimates/evidence/verify/elementary_estimates/weak_steps
title: "Independent derivations of three weak steps"
desc: Independent derivations of interval discrepancy, rough-number density transfer, and candidate mass for the frozen elementary estimates.
created: 2026-10-16T04:10:53Z
updated: 2026-10-16T04:16:14Z
---

# Independent derivations of three weak steps

***

These written keepers accompany the [examination report](report.md). They
concern the frozen text examined on 2026-10-15, identified there and in the
[subject map](subject_map.md). They do not modify the subject. All prime
estimates used below are the explicit classical premises in the report.
There is no numerical computation or executable evidence leg.

## 1. Discrepancy with unrestricted cuts and imprimitive characters

Put $L=\log x$, $T=\log L$, $W=\exp(\sqrt L)$, and
$\Delta=L^{-S}$. Fix $b_1,\kappa,\Gamma,B,S$ as in E2, with
$S\ge2B+2$, and let $a=b_1/4$. The important lower bound is
$Y\ge e^{-\Delta}x^a$ for a cell $C=(Y,e^\Delta Y]$ meeting the ambient
range. The number of cells is at most $L^{S+1}+2$.

For the actual integer counts, the block-sieve argument with cutoff $W>1$,
level $D_W=W^{8\lceil T^2\rceil+2}$, and $O(1)$ divisibility remainders
gives

$$
 R(C)=|C|V(W)(1+O(e^{-2T^2}))+O(D_W),\qquad
 D_W=\exp(O(\sqrt L\,T^2)).
$$

Since $\log D_W=o(L)$, whereas
$|C|V(W)\gg x^a L^{-S-1/2}$, the denominator is positive and asymptotic
to $\Delta YV(W)$, uniformly in these cells. Every selected rough integer
and every selected prime is $W$-rough: $x^{b_1}>W$ and the entire cell
lies above $W$ eventually. Consequently $c_I(C)\in[0,1]$ exactly.
This set inclusion, rather than an asymptotic density ratio, supplies the
coefficient bound. It is valid for every fixed precision and has no dependence
on that precision.

Let $J_0=J\cap K$. It is an interval, regardless of the lengths of the
original intervals. On the support of $I-B_I$, every character modulus
$r\le L^B$ is coprime to the summation variable, because all its prime
divisors are smaller than $W$.

For a principal character the relevant weight is $f(y)=y^{it-1}$.
On a full cell,

$$
 \sum_C(I-B_I)=0,\qquad
 \sup_C|f(y)-f(Y)|\le(1+|t|)(e^\Delta-1)/Y.
$$

The number of integers in the cell is at most $|C|+1$, so its contribution
after subtracting $f(Y)$ is bounded by

$$
 O\bigl((1+|t|)\Delta(\Delta+Y^{-1})\bigr).
$$

Summing first, before taking any limit, gives
$O(L^{B+1-S}+L^{B+1}x^{-a})$. There are at most two cells which meet
$J_0$ without being contained in it; their combined harmonic mass is
$O(\Delta+x^{-a})$. For fixed $S$, the powers of $x^{-a}$ beat all
the displayed powers of $L$. Thus the whole principal sum is
$O(L^{-B-1})$. This proof covers $J_0$ across many dyads; it does not
need the smaller dyadic interval assumed in the original application. A cut
cell is never renormalized.

For a nonprincipal character, first isolate the prime input. Write
$A_\chi(y)=\sum_{p\le y}\chi(p)$. If $y\ge\exp(L^c)$, then
$r\le(\log y)^{B/c}$. Summing the Siegel–Walfisz statement over reduced
classes gives

$$
 |A_\chi(y)|\ll_K L^B y(\log y)^{-K}.
$$

The loss $L^B$ is present here. Orthogonality cancels the common main
term for any nonprincipal character of modulus $r$, not just primitive
ones. A prime dividing $r$ has character value zero. Partial summation
on an arbitrary prime interval with lower endpoint $y_1$ gives

$$
 \left|\sum_{p\in I}\chi(p)p^{it-1}\right|
 \ll_K L^B(\log y_1)^{-K}
       +L^{2B}(\log y_1)^{1-K}.
$$

For the integral estimate take $K>1$; enlarging it until
$c(K-1)\ge A+2B$ gives $O(L^{-A})$, uniformly in both endpoints.
This is an absolute error estimate. It remains valid when the interval has
no primes or is shorter than the typical prime spacing.

The actual roughness test has an exact enumeration, not an independence
heuristic. For each admitted integer, sort its prime factors in
nondecreasing order, with multiplicity. There are at most
$\lfloor1/b_1\rfloor$ factors. On fixing the first $l-1$ and their
product $Q$, the last prime lies in the intersection of three intervals:
the order condition, $p>x^\gamma$, and $Qp\in J_0$. Hence the preceding
prime estimate applies once, with $c=1/2$, to every $Q$.
Only prefixes with a nonempty last-prime interval matter; all their primes
are at most $x$. Their total absolute harmonic weight is at most

$$
 \left(\sum_{x^{b_1}<p\le x}p^{-1}\right)^{l-1}
 \ll_{b_1}1.
$$

Taking $A=B+2$ therefore bounds the actual-test sum by
$O_{b_1}(L^{-B-2})$. Equal primes cause no duplication in the sorted
list. The prime test is the case $l=1$.

For the proxy, do not try to infer a very-short-interval relative prime
asymptotic. For every partial cell interval $H$, CRT and the block sieve
instead give, for each reduced class $a\bmod r$,

$$
 \#\{n\in H:n\equiv a\bmod r,\ P^-(n)>W\}
 =\frac{|H|V(W)}{\varphi(r)}
   +O\left(e^{-2T^2}\frac{|H|V(W)}{\varphi(r)}+D_W\right).
$$

The identity in the main term uses
$r^{-1}\prod_{p\mid r}(1-1/p)^{-1}=\varphi(r)^{-1}$;
it holds for nonsquarefree $r$ too. Applying this to each initial
subinterval of $J_0\cap C$, and summing against $\chi$, bounds its
partial character sums by

$$
 O(e^{-2T^2}\Delta YV(W)+L^BD_W).
$$

Partial summation against $y^{it-1}$ costs at most
$Y^{-1}(1+(1+|t|)(e^\Delta-1))\le2/Y$ eventually.
Multiply by the unchanged full-cell constant $c_I(C)\le1$ and sum.
The resulting bound is

$$
 O\left(e^{-2T^2}LV(W)
       +L^{S+1+B}D_Wx^{-a}\right)=O(L^{-B-2}).
$$

The first term has logarithm $-2T^2+O(T)$; the second has logarithm
$-aL+o(L)+O_{S,B}(T)$. They beat every fixed power of $L$.
The implied constants can depend on the fixed input data; the extra power
saved in all cases absorbs them and gives the literal bound $L^{-B}$.

This checks all interval cuts, every principal or imprimitive character,
and every $|t|\le L^B$ simultaneously. It also explains why selecting
$S$ after the Type II demand $B$ is legitimate: coefficient size and
rough support were established without selecting $S$.

## 2. From prime lists to the density and the subtraction identity

Use the coordinate measure $dt_1\cdots dt_{l-1}$ on
$\sum_{i=1}^lt_i=w$, with $t_l=w-\sum_{i<l}t_i$.
It is not the Euclidean surface measure. For $l\ge2$, set

$$
 T_l(\gamma,w)=\frac1{l!}
 \int_{\substack{t_i\ge\gamma\ (i<l)\\
                 \sum_{i<l}t_i\le w-\gamma}}
       \frac{\prod_{i<l}dt_i/t_i}{w-\sum_{i<l}t_i},
 \qquad T_1(\gamma,w)=1/w.
$$

On a compact set $\gamma\ge b>0$, $w-\gamma\ge\varepsilon>0$,
$w\le w_{\max}$, only boundedly many $l$ occur. Every coordinate
denominator is at least $b$. For a varying $(\gamma,w)$ the integrand
with its indicator converges off finitely many hyperplanes and is bounded
by an integrable constant on a fixed box. This proves joint continuity,
including thresholds $w=l\gamma$ for $l\ge2$, where the integral
shrinks to zero. It asserts no continuity across $w=\gamma$.

For a cell $C=(Y,e^\Delta Y]$, put $w=\log Y/L$.
PNT at accuracy $A=S+2$ gives

$$
 \pi(e^\Delta y)-\pi(y)
 =\frac{\Delta y}{\log y}(1+O(L^{-1}))
 \quad(\log y\ge cL,\ c>0\ \hbox{fixed}).
$$

Indeed the endpoint error is $O(yL^{-S-2})$, compared to a
main term of order $yL^{-S-1}$. The variation of the main integral
and $e^\Delta-1$ gives no larger relative error when $S\ge1$.

The nonsquarefree integers in the cell admitted by the roughness test
are at most

$$
 e^\Delta Y\sum_{n>x^\gamma}n^{-2}
 =O(Yx^{-b})=o(\Delta Y/L).
$$

For squarefree integers, exactly $l!$ ordered prime lists represent an
integer with $l$ prime factors. Dropping the distinctness condition only
increases the ordered-list count. Fix its first $l-1$ primes and let
$Q$ be their product. Existence of a last prime above $x^\gamma$
implies $s=\log Q/L<w-\gamma+\Delta/L$, so
$\log(Y/Q)\ge bL/2$ eventually. Counting all primes in
$(Y/Q,e^\Delta Y/Q]$, even those which might fail the last cutoff,
is a legitimate upper bound.

After the last-prime estimate, the remaining normalized sum is an integral
against the product of the discrete reciprocal-prime measures
$\mu=\sum_{x^\gamma<p\le x^{w_{\max}}}p^{-1}\delta_{\log p/L}$.
For every interval with endpoints between $\gamma$ and $w_{\max}$,

$$
 \mu((a,a'])=\log(a'/a)+O_b(L^{-1}).
$$

For $l\ge2$, every first prime in a nonempty list is below
$e^\Delta x^{w_{\max}-b}<x^{w_{\max}}$ eventually, which justifies
this upper cutoff on $\mu$.

Partition the coordinate box into cubes of fixed side $\eta$.
The error in the mass of each cube is $O_{\eta,b,l}(L^{-1})$;
there are only finitely many cubes at this stage. On a cube away from
the moving cutoff hyperplane, the integrand oscillates by $O(\eta)$.
Cubes touching that hyperplane lie in a slab of thickness $O_l(\eta)$
whose product $dt_i/t_i$ measure is $O_{b,l,w_{\max}}(\eta)$.
The additional strip of thickness $\Delta/L$ has measure
$O(\Delta/L)$. These estimates are uniform in $\gamma,w$ in
the stated compact set. Supremum sums therefore give

$$
 \frac{L\,N_\gamma(C)}{\Delta Y}\le
 D_\gamma(w)+O(\eta)+o_\eta(1),
$$

with the last error uniform in the allowed cells and exponents for
each fixed $\eta$. For any desired error, choose $\eta$ first and
then the threshold for $x$. This proves the asserted uniform $o(1)$
without letting $S$, $\eta$, or the number of prime factors grow with
$x$ after their selection.

For a factor $m=N/n$ with $x\le N\le5x$ and
$a=\log n/L\in(\gamma,\gamma']$, its containing cell satisfies
$w=1-a+O(L^{-1})$. Since
$\gamma'\le1/2-\kappa$,
$w-\gamma\ge2\kappa-O(L^{-1})$; also $w\le1$ eventually.
Thus the compact set $K(b_1,\kappa,1)$ suffices. Divide by the
already established $R(C)\sim\Delta YV(W)$ and use its uniform
continuity to get

$$
 c_\gamma(C)\le
 \frac{\sup_{\gamma\le a\le\gamma'}D_\gamma(1-a)+o(1)}{LV(W)}.
$$

No primality of $n$ is used in this deduction. It covers the source's
factor formulation as well as the reconstruction's stated prime-factor
application. For balanced prime cells $w\ge0.46-o(1)$, the same
normalization gives $c_{\rm pr}=(1+o(1))/(wLV(W))$, so 3 is an
absolute eventual constant. Neither its value nor the compactness
argument requires $S$ to be an early choice.

For the identity, work term by term on the simplex of total sum 1.
The coordinate measure is invariant under permutations: exchanging a
dependent coordinate with an independent one has absolute Jacobian 1.
Almost every point has a unique minimum coordinate. If it is $\alpha$,
there are $l$ choices for its position, and the remaining coordinates
sum to $1-\alpha$ and are all at least $\alpha$. Therefore

$$
 T_l(b_1,1)
 =\int_{b_1}^{1/2}
       T_{l-1}(\alpha,1-\alpha)\,\frac{d\alpha}{\alpha}.
$$

The coefficient is $l/l!=1/(l-1)!$, not $1/l!$.
For $l=2$ the inner integral is simply $1/(1-\alpha)$.
Summing these finite identities and separating $T_1(b_1,1)=1$
proves (7.18). As a direct normalization check, for
$1/3<b_1<1/2$ it reduces to

$$
 D_{b_1}(1)-1
 =\log\frac{1-b_1}{b_1}
 =\int_{b_1}^{1/2}\frac{d\alpha}{\alpha(1-\alpha)}.
$$

This check supplements, rather than replaces, the all-$l$ argument.
The endpoint $\alpha=1/2$ has left-limit density 2 and zero
integration mass.

For the lower ordinary count in $(x,2x]$, an integer with prime
multiplicities $a_p$ receives weight
$(l!/\prod_p a_p!)/l!=1/\prod_p a_p!\le1$ from all ordered lists.
Keeping only prefixes with $s<1-b_1-\eta'$ preserves this inequality
and guarantees that every last prime in $(x/Q,2x/Q]$ is above
$x^{b_1}$. PNT and infimum cube sums give the truncated simplex
integrals as a lower bound for the limit inferior of the scaled count.
Increasing those domains by taking $\eta'\downarrow0$ yields
$D_{b_1}(1)$. The ordinary upper sieve, with
$h=2\lfloor1/(40b_1)\rfloor$, has level at most
$x^{1/5+2b_1}$ and relative error
$c_1e^2e^{-1/(20b_1)}$. For sufficiently small $b_1$ its
remainder is $o(x/L)$ and $h\ge h_0$. Mertens' product formula
then gives (7.19) with absolute constants.

Finally, on the triangular bin domain, uniform continuity bounds the
difference between $D_\gamma(1-a)$ and $D_\alpha(1-\alpha)$ by
$\omega(2\delta_0)$ whenever $a,\alpha$ are in the same bin.
Integrating in $d\alpha/\alpha$ gives total error at most
$\omega(2\delta_0)\log(1/(2b_1))$. The fixed mesh can make this
at most $1/10$. The identity and the two ordinary counts then leave
$1-1/10-O(b_1^{-1}e^{-1/(20b_1)})+o(1)$ in the normalized
preliminary-minus-unbalanced mass, once the consumer's preliminary and
per-prime sieve bounds and conditional Type II proxy replacement are
available. The purely numerical mesh estimate uses no P; its weighted
application inherits the consumer's P hypothesis. The errors are absolute in this
normalization; no exceptional integer set has been discarded without
its weight.

The unused Buchstab cross-check also has a direct verification.
Scaling the coordinates gives $D_\gamma(w)=F(w/\gamma)/\gamma$,
where $F(u)=D_1(u)$ is defined for $u>1$.
Permutation symmetry gives
$uT_l(1,u)=\frac1{(l-1)!}\int_{\sum_{i<l}t_i\le u-1}
\prod_{i<l}dt_i/t_i$. Differentiating this integral away from its
thresholds and extending continuously yields
$(uF(u))'=F(u-1)$ for $u>2$, while $F(u)=1/u$ for
$1<u\le2$. These are the usual defining equations of Buchstab's
function; no property of it is needed for the proof above.

## 3. Local candidate mass without a uniform threshold in the slot index

Let $M_j$ be the harmonic prime mass in band $j$, and $M_*$ the
harmonic mass of the exceptional integers. Expand the ordered slots
before taking any expectation. With each slot independently sampled
proportionally to its reciprocal, their product $V$ satisfies

$$
 \sum_v\frac{a_Q(v)}v f(v)=H_Q\mathbb E f(V),\qquad
 H_Q=\prod_{j\le j_x}\frac{M_j^{r_0}}{r_0!}\frac{M_*}{M_{j_{**}}}.
$$

Different ordered lists with the same product are supposed to add in
this equality. The factorial normalization therefore causes no
probability-model mismatch when primes repeat. Every Q-slot entry is
coprime to every P-prime, including the exceptional integer since
its least prime exceeds $W$. Thus $u=vr$ with $r_*=1$ is
unique as a factorization into the Q-supported part and the P-part.
Independent harmonic sampling of $R$ consequently gives the exact
identity

$$
 X_A=H_QH_P\,\mathbb E[VR\Psi(VR/x)].
$$

For one P-group, sum all powers of a selected prime. Its geometric
mass is $1/(p-1)$; hence, with
$F_g(q)=\prod_{p\in\mathcal P_g}(1+q/(p-1))$,
the marked group sum is $F'_g(q)/V_g$.
It equals

$$
 F_g(q)V_g^{-1}\sum_{p\in\mathcal P_g}(p-1+q)^{-1}.
$$

The second factor is at least 1. Its error from 1, and the error
between $\log F_g(q)$ and $qV_g$, are bounded by constants
times the group's sum of $p^{-2}$. Across all groups these errors
tend to zero, since the groups are disjoint and their primes tend to
infinity. This proves both the asserted asymptotic and the exact
lower product for $H_P$.

For $\xi=L^{-2/5}$, the prime-power mass after tilting is
$(p^{1-\xi}-1)^{-1}\le2e/p$ eventually. This bounds each
tilted marked-group mass by a constant in the fixed group bounds.
There are $O(T)$ groups, so
$\sum_r W_1(r)r^{\xi-1}\le L^{C}$ for a fixed $C$.
It follows that
$\sum_{r>x^\sigma}W_1(r)/r\le e^{-\sigma L^{3/5}}L^C$.
The sampling measure is normalized by $H_P\ge1$, so the same bound
controls its tail probability.

Every $M_j$ lies eventually between two fixed positive constants,
uniformly through $j_x$, since the smallest band logarithm is at
least $20T$. The product of $O(T)$ such factors is bounded above
and below by powers of $L$. For each fixed $j_{**}$, eventually
every prime in its band exceeds $W$. Hence
$M_*\ge M_{j_{**}}$, while $M_*\le L+1$.
The exponent in the resulting bounds for $H_Q$ is independent of
$j_{**}$; the threshold need not be.

Condition on every variable except the first prime $p_0$ in band 0.
This is a pure slot because $j_{**}\ge j_0\ge J_1>0$.
An event $x\le VR\le2x$ restricts $p_0$ to one interval
$[y,2y]$, intersected with its band. When this is nonempty,
$y\ge x^{c_1s'}/2$. Chebyshev gives probability $O(1/L)$
uniformly in the variables conditioned upon, proving the upper mass
comparison.

For a lower comparison let
$\Delta_0=(c_2-c_1)s'L$, and choose the fixed prefix length $J_1$
so that all tail slot logarithms, even if all are maximal, sum to
at most $\Delta_0/24$. The infinite tail midpoints have this bound
as well. For every nonfree slot in the prefix restrict its logarithm
to $m_j\pm\epsilon s_j$, with
$\epsilon\le(c_2-c_1)/(48r_0)$. Its cumulative deviation is at
most

$$
 \epsilon r_0\sum_{j\ge0}s_j
 =2\epsilon r_0s'L\le\Delta_0/24.
$$

This event involves only a fixed number of pure slots and has
probability at least a fixed $c_{\rm pre}>0$, by their harmonic
prime masses. Also impose $\log R\le\Delta_0/12$; its probability
is eventually at least $1/2$, independently of the prefix.
The exceptional slot is in the tail, so only its deterministic range
enters. On this event, subtraction of the infinite midpoint sum $L$
gives

$$
 \log(VR)-L=(\log p_0-m_0)+d,\qquad
 -\Delta_0/12\le d\le\Delta_0/6.
$$

These bounds include the missing bands beyond $j_x$. The interval
where $\Psi$ has its positive lower bound prescribes an interval
of fixed positive logarithmic length $\ell_0$ for $p_0$.
Its left endpoint is $m_0-d+\log\alpha_0$.
Both its endpoints stay at least $\Delta_0/4$ inside band 0
for large $x$. PNT and partial summation give uniformly there

$$
 \sum_{e^A<p\le e^{A+\ell_0}}\frac1p
 =\log(1+\ell_0/A)+O(A^{-2})\gg L^{-1}.
$$

After dividing by $M_0$, the conditional probability is
$\gg L^{-1}$, and on the desired event $VR\Psi(VR/x)\gg x$.
The lower comparison constant is thus a product of fixed positive
constants. It cannot depend on the later fixed $j_{**}$.
Using $H_P\ge1$ and the lower bound for $H_Q$ gives the
claimed fixed power lower bound for $X_A$.

The micro-band comparison is exact before estimating it:

$$
 \frac{H_Q}{H_Q^{\rm mic}}=\prod_{j<j'}\frac{M_j^{r_0}}{r_0!}.
$$

The exceptional factor cancels because $j_{**}\ge j_0\ge j'$.
Only finitely many early bands remain, giving an index-independent
positive lower bound for this ratio.

An attempted disproof that takes $j_{**}=j_x$ as $x$ grows would
make the exceptional range lie below $W$, eventually leaving it
empty. That construction is excluded by the actual quantifiers:
$j_{**}$ is fixed before $x\to\infty$, and its threshold may
depend on it. This failed attack pinpoints a necessary qualification
which the statement retains. The constants used later to choose
$\kappa$ require no uniform threshold in $j_{**}$.
