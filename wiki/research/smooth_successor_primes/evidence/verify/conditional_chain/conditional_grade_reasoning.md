---
name: research/smooth_successor_primes/evidence/verify/conditional_chain/conditional_grade_reasoning
desc: Grading reproduction of the conditional examination's signed, extraction and counting keepers, preserving their exact adverse and surviving scopes.
created: 2026-10-16T04:55:23Z
updated: 2026-10-16T04:55:23Z
---

# research/smooth_successor_primes/evidence/verify/conditional_chain/conditional_grade_reasoning

***

On 2026-10-16 UTC the grader assessed the complete original
[signed keeper](signed_keeper.md),
[extraction keeper](extraction_keeper.md) and
[counting keeper](counting_keeper.md), together with
[the premise account](premises.md) and their unchanged
inputs. The calculations below reproduce those existing derivations for
grading. They add no new premise, proof repair or replacement examination.
The source method is OpenAI's unrefereed manuscript *Weighted dilation graphs,
smooth shifted primes and totient fibers*, 24 September 2026 release.
Original project exposition and parameter checks are credited to Plasma AI.

## Signed deduction: weakest analytic bridge

The notation and quantifiers are those of the complete premise account.
In particular $L=\log x$, $T=\log L$, $W=e^{\sqrt L}$;
group marks count distinct primes and band slots permit repetitions.
The exceptional slot is an integer rough above $W$.

The original keeper does not begin by assuming the post-Cauchy expression.
It bounds the discarded group part by
$xL^{O(1)}\exp(-b_*L^{1-d}/4+O(\sqrt L))$.
Because $d<0.47<1/2$, this is smaller than every required logarithmic
saving. The Euler factors used in the marked tail retain prime powers.

In the finite allocation, $E=UL^{-K_0}$ and the final allocated product
satisfies $EL^{-C_s}\le e\le E$. The residual invariant is checked at each
slot: nonzero weights imply enough residual capacity to reach the cutoff.
The exceptional integer and group factors stay on the other side.
The list has $O(T)$ slots; there is no assumption that an infinite procedure
terminates. The pre-Cauchy expansion uses a product of one-dimensional
Fourier norms with fixed per-slot cost, hence
$(2C_F)^{O(T)}=L^{O(1)}$. It does not apply a fixed-dimensional constant
uniformly in an increasing dimension. Its total cost, residual coefficient
bound and tail precision are fixed before $K_0$.

The Cauchy diagonal satisfies

$$
\sum_{e\mid(mn+1)/2}\tau((mn+1)/(2e))^2
\le \tau(mn+1)^3,
\qquad
\mathcal N_{\rm diag}
\ll L^{O(1)}\sum_{v\ll x}\tau(v)\tau(v+1)^3
\ll xL^{C_5}.
$$

The last step uses Cauchy–Schwarz and the ordinary second and sixth moments;
no shifted-divisor asymptotic is imported. Since $EV\asymp xL^{-K_0}$,
choosing
$K_0\ge C_3+C_5+2C_f+2D_*+2$
pays the diagonal and the already fixed pre-Cauchy Fourier mass.

For the off-diagonal, starting from
$mn=2eh-1$, $m'n=2eh'-1$, define $k=(m-m')/(2e)$. The identities are

$$
m'-m=-2ek,\qquad h'-h=-kn,\qquad mh'-m'h=k,
\qquad z=m'h,\quad z+k=mh'.
$$

The first equation gives $(n,2e)=1$, so the divisibility defining $k$ is
valid. In the converse, $m'\equiv m\pmod{2|k|}$ makes $e$ integral and
the cutoff imposes $e>0$. The equation
$m(h'-h)=-k(2eh-1)$ and $(m,k)=1$ imply integral
$n=(2eh-1)/m>0$. Roughness gives $(m,k)=1$ because $0<|k|<W$.
Substitution recovers the original equations uniquely.
Thus the correspondence is an actual bijection, with both signs of $k$,
rather than an uncontrolled enlargement of the signed sum.

The character modulus is $2|k|$. Both $m,m'$ are units, so orthogonality
imposes precisely their congruence. The pulled-back second cutoff is

$$
n=\frac{(m-m')z}{kmm'}-\frac1m.
$$

Its negative last term and the positivity cutoff matter. In logarithmic
coordinates for $m,m',z$, derivatives of $e/E$ and $n/V$ are polynomial
in $L$ after $K_0$ is fixed. Three-dimensional separation is now a legitimate
fixed-dimensional application. Absolute endpoint bounds
$L^{O(1)}\tau(z_*)^2$, the fourth moment and Cauchy–Schwarz pay all tails.

The separated endpoints in the original keeper are exactly

$$
F_0(v)=\sum_{mpr=v_*}
\alpha_m\chi(m)m^{i(\varrho-\xi_2)}
\mathbf1_{p\in I_{**},\,P^-(p)>W}p^{-i\sigma}\overline{c_r},
$$

$$
G_0(v)=\sum_{mpr=v_*}
\alpha_m\chi(m)m^{i(\xi_1+\varrho)}
\mathbf1_{p\in I_{**},\,P^-(p)>W}p^{-i\sigma}\overline{c_r}.
$$

Expanding $\overline{F_0(z)}G_0(z+k)$ verifies each conjugation.
The outer factors $z^{i(\varrho+\xi_3)}(z+k)^{-i\varrho}$
restore the powers on $h,h'$ and the separated $z$ variable.
Roughness makes $m,m'$ group-free, giving
$z_*=m'h_*$ and $W_\ell(z)=W_\ell(h)$, and the analogous identities
at $z+k$. The discrepancy-bearing coefficient is the original restricted
$\alpha$, with the new character and powers explicit in P's endpoint.
There is no unexplained discrepancy transfer to a new sequence.
The integer slot, unrestricted $c_r$, modulus, frequencies and positive
power range all meet P. If the balanced factor range is nonempty then
$b_*\le1/2$, so $\eta_*<b_*/4\le1/8<1/4$.

For $\widetilde\psi(t)=t\psi_Z(t)$,
$Z\widetilde\psi(z/Z)/z=\psi_Z(z/Z)$. The unweighted correlation is
therefore $Z$ times P's harmonic sum. This is the indispensable scale
factor; P gives $O(ZL^{-D_0})$, not $O(L^{-D_0})$ for that sum.
The fixed post-Cauchy costs precede $D_0$ and then P's $B$.
The keeper's bound
$D_0\ge C_3+C_9-K_0+2C_f+2D_*+2$, with $D_0>0$,
pays the off-diagonal after Cauchy and all Fourier variation.
The signed result is thus supported by the existing proof under P and the
stated elementary/classical inputs. No source Section 6 equivalence is
needed or certified by this grading.

## Extraction: every consumed sieve range

The original extraction keeper derives Type I, rather than assuming it as
an additional theorem. It uses the positive inverse-of-2 residue class,
the primitive conductor decomposition, the large-sieve factor $1/R$ and
Siegel–Walfisz for small conductors. The principal-character error is kept.
The resulting modulus-sum estimate is

$$
\sum_{\substack{d\le x^\vartheta\\d\ {\rm odd,\ squarefree}}}|r(d)|
\ll xL^{-D}+X_A L^{-18}
\quad(\vartheta<1/2,\ D>0\text{ fixed}).
$$

This matches the surviving E5 conclusion. It is not a pointwise assertion
for individual moduli. Full-cell proxies and actual interval cuts match E2;
$S>2B+3$ is stronger than the threshold accepted in E's grade.
The tests lie in the rough support, so the coefficient bound is 1
independently of $S$.

The odd-prime normalization is exact:

$$
\frac{1-1/(p-1)}{1-1/p}=1-\frac1{(p-1)^2}\quad(p\ge3),
\qquad
\frac{V_1(y)}{V(y)}\longrightarrow
\mathfrak S=2\prod_{p\ge3}\left(1-\frac1{(p-1)^2}\right)>0.
$$

For the preliminary cutoff $x^{b_1}$, the stated small fixed $b_1$ and
even $h$ put the sieve level within Type I's exponent.
For the individual large-prime sieve at $W$, the products $pd$ are all
distinct: $p$ is their unique prime factor exceeding $W$.
Their size is at most $x^{1/2-\kappa+o(1)}$.
Thus summing remainders does not silently incur a divisor multiplicity.

The cofactor density transfer uses only
$\log(2u-1)/L=1+O(1/L)$ and the compact gap
$w-\gamma\ge2\kappa+o(1)$. It imports no theorem about shifted primes.
The finite-simplex identity supplies
$\int_{b_1}^{1/2}D_\alpha(1-\alpha)\,d\alpha/\alpha=D_{b_1}(1)-1$;
the removed one-prime contribution is exactly 1.
The finite mesh is fixed before $x$, using joint continuity.
PNT and partial summation give the reciprocal prime interval limit
$\log(\gamma'/\gamma)$; subtracting two bare Mertens $O(1)$ errors would
not suffice. Strict least-prime bins and repetitions are both retained.
These operations leave at least $\mathfrak S X_A/(2L)$ on primes and
balanced composites.

Every remaining composite has two prime factors counted with multiplicity,
both in $[x^{1/2-2\kappa},x^{1/2+2\kappa}]$ for large $x$.
Two Type II replacements are legitimate: after the first, its proxy is
an arbitrary coefficient bounded by 1 for the second. Squares are included
and ordering can only overcount.

The full balanced proof is present in the original keeper. Its assignment
integer $D_1$ contains the entire exceptional integer and prime-power
multiplicities. With early choices of $j',\theta,j_0$,

$$
D_1\le x^{1/20},\qquad
\sum\lambda/D_1=H_Q^{\rm mic},\qquad
\sum\lambda\le x^{1/20}H_Q^{\rm mic}\ll x^{1/20}H_Q.
$$

One distinct marked prime per group accounts for the mark normalization.
The permission-mask expectation supplies exactly the remaining
$q^{\omega-s}$ damping. The residual macro-list multiplicity factor is at
most 1, giving a pointwise upper bound. No squarefreeness of $D_1$ is assumed.

For each assignment, $mn=-1\pmod{D_1}$ has exactly $\varphi(D_1)$
solutions, including nonsquarefree $D_1$. At an odd prime $l\nmid D_1$,
the two disjoint failures $mn=0$ and $mn=-1$ occupy $2l-1$ and $l-1$
residue pairs. Hence the sieve density is at most $3/l$ and its maximum
is $7/9$ at 3. CRT gives the box remainder, summed to
$D=x^{10\theta}\le x^{1/20}$, as

$$
L^C\{(M_1+M_2)D+D_1D^2\}.
$$

Here $M_i\ll x^{0.54}$ is essential. Summing the assignment weights gives
at most $x^{0.64}L^C H_Q^{\rm mic}$, negligible against
$X_AV(W)^2\asymp xH_QH_P/L^2$. The Euler main term is bounded by

$$
xV(W)^2V(x^\theta)H_Q^{\rm mic}H_P
\ll X_AV(W)^2.
$$

The finite compensation product over primes dividing $D_1$ is bounded
because those primes are at least $L^{20}$; the mask compensation uses
the already derived exact inequality
$H_P\ge\prod_{p\ {\rm in\ groups}}(1+q/(p-1))\ge1$.
All constants used here precede $\kappa,b_1,j_{**},S$.
There are $O(\kappa L+1)$ balanced dyads. After the proxy factor the
composite cost is
$C_{\rm bal}(\kappa+L^{-1})X_A/L+o(X_A/L)$.

The choice order is early geometry and $C_{\rm bal}$, then $\kappa$,
then $b_1,j_{**}$ and the finite mesh, then Type II saving,
$K_0,D_0,B$, and finally $S$. The bound 1 for proxies prevents feedback
from $S$ to $B$. The original proof yields prime weight at least
$\mathfrak S X_A/(5L)$. Candidate mass and the maximum weight
$\exp(C_w\sqrt L)$ therefore give at least

$$
c\,xL^{-C_A-1}\exp(-C_w\sqrt L)
$$

distinct primes $p=2u-1\in[2x-1,4x-1]$ with
$P^+(p+1)\le x^\delta$. The extra factor 2 in $p+1=2u$ is harmless
eventually. Setting $x=y$ and comparing logarithms gives A+ for every
sufficiently large real $y$, for each fixed $\delta,\eta>0$.

## Strongest successful attack: unrestricted dyads

The isolated dyadic assertion states only $M_1M_2\asymp x$.
At $x=2^j$, choose $m\in[1,2)$, $n\in[2x,4x)$.
Then $m=1$ is rough under the stated convention.
Smooth compact support gives $\Psi(1)=\Psi(2)=0$,
so every nonzero summand corresponds exactly to $x<u<2x$ and
$n=2u-1$. Its sum is

$$
S_W=\sum_{P^-(2u-1)>W}A(u)\Psi(u/x).
$$

Type I and the operative E1 sieve at $W$ with
$h=2\lceil T^2\rceil$ give
$S_W\sim\mathfrak S X_AV(W)$.
The level is $x^{o(1)}$ and
$xL^{-D}+X_AL^{-18}=o(X_AV(W))$ once $D>C_A+10$.
Since $V(W)\sim e^{-\gamma_E}/\sqrt L$,

$$
\frac{S_W}{X_AV(W)^2}
\sim \mathfrak S e^{\gamma_E}\sqrt L\longrightarrow\infty.
$$

This reproduces the original asymptotic witness under the same classical
and elementary premises. It uses neither P nor experimental prime counts.
The omitted factor balance cannot be supplied by a product-size condition.
The witness lies outside the actual balanced specialization; that restriction
and its proof were already present in the frozen examination.
No repair was introduced in grading.

## Counting: weakest terminal bridge

For $0<\epsilon<1$, the original keeper fixes
$B\ge8/\epsilon$, $\eta=\epsilon/16$, $\delta=1/(2B)$,
$y=(\log x)^B$ and
$k=\lfloor\log x/\log(5y+1)\rfloor$.
A+ supplies $M\ge(\log x)^{B(1-\eta)}$ primes, eventually $M>2k$.
Their $k$-subset products are squarefree and strictly less than $x$.
Writing $L=\log x$ and $N=\binom Mk$,

$$
\log N\ge k(\log M-\log k)
\ge(1-\eta-1/B)L-o(L).
$$

Each divisor sum is a product of $k$ terms $p+1\le5y+1$,
hence at most $x$, with prime factors at most $\sqrt L$.
The number of possible values is bounded by
$U=(1+L/\log2)^{\sqrt L}$, so $\log U=o(L)$.
Cauchy's inequality gives at least $N^2/U$ ordered equal-value pairs.

For $t=\lceil\eta k\rceil$, pairs sharing at least $t$ selected primes
are at most $N\binom kt\binom M{k-t}$.
Their fraction among all pairs is at most
$2^k(2k/M)^t$. Indeed $M>2k$ bounds the ratio of binomial coefficients,
and

$$
\log\!\left(2U\,2^k(2k/M)^t\right)
=-\eta(1-\eta-1/B)L+o(L)\longrightarrow-\infty.
$$

At least $N^2/(2U)$ equal-value ordered pairs remain.
The diagonal is deleted since it shares all $k$ primes.
Writing $a=gu,b=gv$, squarefreeness makes $g,u,v$ pairwise coprime.
Thus $\sigma(g)>0$ cancels from
$\sigma(g)\sigma(u)=\sigma(g)\sigma(v)$.
It would be invalid to use this multiplicative cancellation for arbitrary
nonsquarefree products; here the constructed products supply the hypothesis.

There are fewer than $\eta k$ common primes, so $g<x^\eta$.
For a fixed unordered reduced pair and fixed $g$, there are at most two
ordered preimages. Therefore the entire fiber is at most $2x^\eta$, and

$$
h_{\rm sf}(x)\ge\frac{N^2}{4Ux^\eta},\qquad
\log h_{\rm sf}(x)\ge(2-3\eta-2/B)L-o(L).
$$

The two factors 2 respectively pay deletion and ordering.
Since $3\eta+2/B\le7\epsilon/16<\epsilon$, the strict desired inequality
holds eventually. The products and reduced pairs satisfy the strict endpoint
for real $x$, including integer $x$. Also $b<x$ iff $b<\lceil x\rceil$
for integer $b$, so the supplied ceiling identity is correct.
Larger $\epsilon$ follow from a smaller fixed loss.
The count is of actual pairs, not of values of $\sigma$ or collision events.
Together with $h(x)<x^2$, the eventual inequalities give the catalog exponent
interpretation. No uniform threshold as $\epsilon$ tends to zero is used.

## Reproduction and limits

Read the unchanged original package in its stated order and recompute the
identities and inequalities above, with the original keepers supplying the
full intermediate derivations. The failure inputs are exact mathematical
ones: the degenerate dyad above, and, in E's separate grade, the empty-prime
example at $z=1/2$. No numerical computation bears either verdict.

All consumed Section 2 and Section 7 interfaces match the separately graded
E fragments. P is assumed throughout the signed and extraction implications.
The original classical proofs, PDFs, source Section 6 equivalence, and any
acceptance of P remain outside the grading warrant.
