---
name: research/smooth_successor_estimates/evidence/verify/elementary_estimates/elementary_grade_reasoning
desc: Grading reproduction of the elementary examination's existing keepers, with exact witnesses, parameter losses and restricted consumer interfaces.
created: 2026-10-16T04:55:23Z
updated: 2026-10-16T04:55:23Z
---

# research/smooth_successor_estimates/evidence/verify/elementary_estimates/elementary_grade_reasoning

***

This account accompanies the elementary grade.
On 2026-10-16 UTC the grader reproduced the indispensable reasoning in the
original [weak-step keeper](weak_steps.md) and
[proof-coverage keeper](proof_coverage.md), against the
unchanged inputs named in the [subject map](subject_map.md).
It is an assessment of those derivations, not a new proof offered to rescue
them. All classical premises and reading limits in the grade apply.

The source method is OpenAI's unrefereed manuscript *Weighted dilation graphs,
smooth shifted primes and totient fibers*, 24 September 2026 release.
Original project reconstruction and parameter checks are credited to Plasma AI.

## E1: witness, polynomial construction and five instances

The literal witness has one object of weight 1, no bad primes, $z=1/2$,
$X=0$, $g(1)=1$, $r(1)=1$. The empty intersection condition holds; the prime
density assumptions are vacuous. The avoiding mass is 1. Every asserted
remainder level is less than 1 and therefore contributes zero. A supported
polynomial in no variables has no permitted constant monomial, so also cannot
majorize 1. This reproduces the report's disproof without an unspecified
constant or asymptotic computation.

For $z>1$, the blocks $(z^{2^{-j-1}},z^{2^{-j}}]$ partition the indicated
prime set. With even $h_j=(j+1)h$ and $t$ present bad indicators in a block,
the alternating sum through degree $h_j$ is 1 for $t=0$ and
$\binom{t-1}{h_j}$ otherwise. Thus $U_j\ge I_j\ge0$ and
$U_j-I_j\le E_j$, the sum of degree-$h_j+1$ monomials.
Telescoping proves

$$
0\le U-\prod I_j\le
\sum_j E_j\prod_{k\ne j}U_k=U-V.
$$

Each correction has exactly one block beyond its upper truncation. These
supports are mutually disjoint and disjoint from $U$'s support, giving
coefficients in $\{-1,0,1\}$ for all three polynomials. The exponent sum is
$h\sum(j+1)2^{-j}=4h$; a correction adds at most 1.
Support is at most $z^{4h+1}$, hence at most the asserted remainder level
$z^{4h+2}$. For $z=1$, the prime set is empty and the constant polynomials
give the same restricted conclusion with the retained $r(1)$.

Under the auxiliary independent Bernoulli law,
$a_j\ge e^{-C/\eta_0}$ and
$e_j\le C^{h_j+1}/(h_j+1)!$. For sufficiently large $h$, factorial decay
bounds $\sum_j e_j/a_j$ by a constant times $e^{-h}$ uniformly in the number
of blocks. At $h=2$ the corresponding odd factorial series is bounded.
Consequently $\mathbb EU/G-1$ and $(G-\mathbb EV)/G$ have the required
bounds. This independence is used only to evaluate monomial main terms.
In the actual population each polynomial's error is bounded by the single
sum of absolute remainders, because its coefficients have magnitude at most
1. No independence of actual events or unproved probability approximation
enters.

The five instance checks survive separately:

1. For integers in an arbitrary interval and a reduced class modulo
   $r\le L^B<W$, omit primes dividing $r$. CRT counts have error at most 1;
   the main term is length times $V(W)/\varphi(r)$.
2. In a per-prime sieve, $p>W$ and squarefree $d$ has all primes below $W$.
   Thus $pd$ has exactly one large prime and different pairs give different
   products. The total error is bounded by the Type I sum without extra
   divisor multiplicity.
3. The preliminary sieve has density $1/(p-1)$ on odd primes and
   $b_1(4h+2)\le1/5+2b_1<1/2-\kappa/2$ for sufficiently small fixed $b_1$.
4. The ordinary rough count has density $1/p$, the same level and
   $O(1)$ remainders. Its error is $o(x/L)$.
5. In balanced boxes, $g(l)\le(3l-2)/l^2\le7/9$ for odd primes, uniformly
   over assignments and masks. The fixed-$h=2$ upper bound applies at
   level $x^{10\theta}$.

The literal $z<1$ defect reaches none of these instances.

## E2: restrictions, characters and the last choice of precision

Write $a=b_1/4$, $\Delta=L^{-S}$.
A full cell meeting the ambient range has lower endpoint at least
$e^{-\Delta}x^a$; there are $O(L^{S+1})$ cells.
The ordinary sieve gives

$$
R(C)=|C|V(W)(1+O(e^{-2T^2}))+O(D_W),
\qquad D_W=\exp(O(\sqrt L\,T^2))=x^{o(1)}.
$$

For each fixed $S$, this is positive and asymptotic to $\Delta YV(W)$.
Each actual test selects a subset of the $W$-rough integers of the full cell.
Hence $0\le c_I,B_I\le1$ exactly, before any restriction or choice of $B$.

A principal character modulo $r\le L^B$ equals 1 on the support.
On a full cell, unweighted cancellation is exact. The variation of
$m^{it-1}$ is $O((1+|t|)\Delta/Y)$. Summing the keeper's cell bounds yields
$O(L^{B+1-S}+L^{B+1}x^{-a})$; at most two partial cells add
$O(\Delta+x^{-a})$. For $S\ge2B+2$ this is $o(L^{-B})$.

For a nonprincipal character, the quoted SW theorem gives
$A_\chi(y)\ll L^B y(\log y)^{-K}$ at $y\ge e^{L^c}$, after summing reduced
classes. Partial summation gives

$$
\sum_{p\in I}\frac{\chi(p)p^{it}}p
\ll L^B(\log y_1)^{-K}
   +L^{2B}(\log y_1)^{1-K}.
$$

Taking $c(K-1)\ge A+2B$ supplies arbitrary fixed accuracy. It is an absolute
bound on every interval, not a relative short-prime asymptotic.
For a rough integer, sort all its prime factors, including repetitions.
There are boundedly many factors. Once the prefix is fixed, order, roughness
and product restrictions leave a single last-prime interval. The total
reciprocal prefix mass is bounded in terms of $b_1$. Thus the same cancellation
holds for the actual test, including induced nonprincipal characters.

For the proxy, the reduced-class sieve on each partial cell has main term
$|J'|V(W)/\varphi(r)$ and errors
$O(e^{-2T^2}|J'|V(W)/\varphi(r)+D_W)$.
Summing against the character cancels the common main term. Partial summation
and all cells give

$$
O\!\left(e^{-2T^2}LV(W)+L^{S+1+B}D_Wx^{-a}\right)=o(L^{-B}).
$$

These estimates retain the class-count, twist and cell-count losses.
All coefficients remain bounded by 1 while $S$ is chosen after P's $B$.
The strongest interval/imprimitive-character attack therefore fails on the
actual quantitative claim.

## E3: densities, normalization and mesh

The density uses coordinate measure on the simplex, not Euclidean surface
measure. On the stated fixed compact, denominators are at least $b$ and only
boundedly many terms occur. Dominated convergence proves continuity;
at $w=l\gamma$, $l\ge2$, the integration domain shrinks to zero measure.
No continuity across $w=\gamma$ is asserted.

PNT accuracy $A=S+2$ gives relative error $O(L^{-1})$ in a logarithmic
cell. Prime-square contributions are $O(Yx^{-b})=o(\Delta Y/L)$.
Squarefree products have exactly $l!$ ordered lists; dropping distinctness
only increases the upper count. Fixing the first $l-1$ primes leaves a
last-prime interval with logarithmic lower size at least $bL/2$.
Mertens' reciprocal-prime measure has interval error $O_b(1/L)$.
A fixed cube mesh gives the limiting integral with error
$O(\eta)+o_\eta(1)$; hyperplane slabs have measure $O(\eta)$ and the shifted
cutoff strip has measure $O(\Delta/L)$. Choose $\eta$ first, then $x$.
This establishes the claimed uniformity without exchanging limits.

Balanced cells have $w\ge0.46-o(1)$, hence
$c_{\rm pr}=(1+o(1))/(wLV(W))\le3/(LV(W))$ eventually.
For an unbalanced cofactor, $w=1-a+O(1/L)$ and
$w-\gamma\ge2\kappa-O(1/L)$; the compact $K(b_1,\kappa,1)$ suffices.
This uses the factor's size only, so the report correctly distinguishes the
source's nonprime wording from the narrower stated application.

Permutation of simplex coordinates has absolute Jacobian 1. Choosing the
unique minimum coordinate in $l$ ways changes $1/l!$ to $1/(l-1)!$.
Therefore

$$
T_l(b_1,1)=\int_{b_1}^{1/2}
T_{l-1}(\alpha,1-\alpha)\,\frac{d\alpha}{\alpha}.
$$

Summing and removing $T_1(b_1,1)=1$ proves the identity. For
$1/3<b_1<1/2$ both sides reduce to $\log((1-b_1)/b_1)$, checking the
normalization without substituting a special case for the proof.
The endpoint density has left limit 2 and zero integration mass.

For the ordinary lower count, an integer with multiplicities $a_p$ receives
weight $1/\prod a_p!\le1$ from all its ordered lists. Restricting prefixes
to $s<1-b_1-\eta'$ keeps the last prime above the cutoff. PNT followed by
$\eta'\downarrow0$ gives $D_{b_1}(1)\le\liminf L\Phi(x)/x$.
The ordinary E1 upper sieve and Mertens bound the limsup by
$(e^{-\gamma_E}/b_1)(1+c'e^{-1/(20b_1)})$.
The directions of both limits are correct.

Uniform continuity makes the total bin-supremum error at most
$\omega(2\delta_0)\log(1/(2b_1))$, chosen below $1/10$ at a fixed mesh.
The weighted residual
$1-1/10-O(b_1^{-1}e^{-1/(20b_1)})+o(1)$ additionally uses the consumer's
conditional replacement and sieve bounds. The keeper states this dependency.
Its optional Buchstab cross-check follows by scaling and
$(uD_1(u))'=D_1(u-1)$ for $u>2$, with $D_1(u)=1/u$ on $1<u\le2$.

## E4: exact mass law and exceptional-slot quantifiers

Expanding ordered lists, including repeated primes, gives the exact law

$$
H_Q=\prod_{j\le j_x}\frac{M_j^{r_0}}{r_0!}
       \frac{M_{\rm rough}}{M_{j_{**}}},
\qquad
X_A=H_QH_P\,\mathbb E[VR\Psi(VR/x)].
$$

The exceptional integer is free of group primes because it is $W$-rough;
all group primes are below $W$. Unique separation of the P-part justifies
the second equality. No approximate independence is assumed.

For each fixed later slot, its band's primes eventually exceed $W$, so
$M_{\rm rough}\ge M_{j_{**}}$, while $M_{\rm rough}\le L+1$.
Uniform positive bounds for the $M_j$ and $O(T)$ bands give fixed polynomial
bounds for $H_Q$. Fixing the exceptional divisor leaves at most the band
permutations, giving $a_Q\le\tau$. On $u\le2x$ it has only
$O(\sqrt L)$ prime factors above $W$, so its divisor choices give the
subexponential pointwise bound. The support restrictions give
$L^{20}\le p\le x^\delta$.

For a group, the marked harmonic mass is
$F'_g(q)/V_g=F_g(q)V_g^{-1}\sum(p-1+q)^{-1}$.
The second factor is at least 1. Summable $p^{-2}$ errors give the claimed
asymptotic and exact lower product. Tilting by $\xi=L^{-2/5}$ keeps each
group's tilted mass bounded, since $p^\xi\le e$. The product of $O(T)$
bounds is $L^{O(1)}$, proving the stated tail.

Conditioning on all but a pure slot of band 0 yields the upper probability
$O(1/L)$ by Chebyshev. For the lower bound, the keeper fixes a finite prefix
before the exceptional slot, controls its deviation by $\Delta_0/24$,
and bounds both the actual and nominal tails by $\Delta_0/24$.
The P-part is at most $\Delta_0/12$ with probability eventually at least
$1/2$. Thus the remaining deviation is in
$[-\Delta_0/12,\Delta_0/6]$.
The desired fixed logarithmic interval for the free prime lies at least
$\Delta_0/4$ inside its band. PNT gives probability $\gg1/L$.
This proves both local comparisons with constants independent of the later
fixed exceptional index. Finally

$$
H_Q/H_Q^{\rm mic}=\prod_{j<j'}M_j^{r_0}/r_0!
$$

cancels the exceptional factor exactly. The attempted moving-index
counterexample is outside the quantified assertion.

## E5 and the balanced interface

For real fixed $k\ge0$, the local divisor series is
$1+2^k/p+O_k(p^{-2})$. Positivity and Mertens give the stated moments.
A fixed $b$-fold convolution is bounded by a logarithmic factor times
$\tau(n)^{b-1}$; its square sum and reciprocal-index variant follow.
Cauchy–Schwarz supplies the mixed and shifted moments actually consumed.

Integration by parts in fixed dimension gives
$|\widehat F(\xi)|\ll_j L^{C(j+1)}(1+|\xi|)^{-j}$.
Integrated mass is $O(L^{C(b+2)})$ and the tail beyond $L^{2C}$ is
$O_j(L^{-Cj+C(2b+1)})$. The frequency exponent is fixed before accuracy.
For the separate $O(T)$ transition factors, total variation is
$(2C_F)^{N_s}=L^{O(1)}$, the union bound pays $N_s$ tail errors, and
$\sum_i1/s_{j(i)}\ll1/T$ bounds retained twists by $O(L/T)$.
The two arguments are not conflated.

The elementary bounds are
$\sum_{d\le y}\mu^2(d)/\varphi(d)\ll\log(2y)$ and
$\sum_{n\le D}3^{\omega(n)}\le\sum_{n\le D}d_3(n)\le D(1+\log D)^2$.

For Type I, extracting a pure band-0 prime gives $b(r)\le L^{c_b}\tau(r)$,
$PU\asymp x$, and $P,U\gg x^{a_0}$. Write an induced character's squarefree
odd modulus as $hf$ with primitive conductor $f>1$ and $(h,f)=1$.
The large-conductor bound after Cauchy–Schwarz and the large sieve is

$$
xL^{c'/2}(R^{-1}+P^{-1/2}+U^{-1/2}+R/\sqrt x).
$$

Dyadic and squarefree-$h$ sums cost at most $L^4$. Choose
$C'\ge D+c'/2+4$. For small conductors, SW includes the residue-class loss;
after all sums the bound is
$xL^{c'+C'+3-K}+x^{1-a_0}L^{c'+C'+3}$.
Choose $K\ge D+c'+C'+3$ afterwards.
The principal coprimality error is
$X_A\,O((L/\log L)L^{-20}L)=O(X_AL^{-18})$.
These are the existing keeper's estimates and use no P.

In the balanced interface the whole exceptional integer remains in $D_1$;
its possible repeated prime factors do not change the count
$\varphi(D_1)$ of unit solutions to $mn\equiv-1\pmod{D_1}$.
For each odd sieve prime, the disjoint bad sets have $2l-1$ and $l-1$
pairs. CRT and the elementary sums give error
$O(L^{O(1)}((M_1+M_2)D+D_1D^2))$ per assignment.
The assignment identities
$D_1\le x^{1/20}$,
$\sum\lambda/D_1=H_Q^{\rm mic}$ and
$\sum\lambda\le x^{1/20}H_Q^{\rm mic}$
then give $x^{0.64}L^{O(1)}H_Q^{\rm mic}$ when $M_i\ll x^{0.54}$.
The Euler main term is bounded by
$xV(W)^2V(x^\theta)H_Q^{\rm mic}H_P$.
E4 makes this $O(X_AV(W)^2)$ with constants fixed before the later gap.
Masks reproduce damping by distinct additional group primes, not by
multiplicity. After the two prime proxies and $O(\kappa L+1)$ dyads the
bound is $C_{\rm bal}(\kappa+L^{-1})X_A/L+o(X_A/L)$.

This final calculation depends on balance. It supplies no unrestricted
dyadic theorem. All preceding reproductions preserve the original
classical-source and P qualifications and add no new mathematical premise.
