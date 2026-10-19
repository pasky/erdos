---
name: research/erdos_25/curved_residue_profiles
desc: Curved real residue profiles give natural nullity of bounded-quotient first kills for every slope; a fixed flat profile shows the limit of natural-density conclusions.
tags: [endpoints, real-geometry, partial-results, obstructions]
sources: []
created: 2026-09-22T12:05:00Z
updated: 2026-09-24T22:13:01Z
---


# research/erdos_25/curved_residue_profiles

***

This approach uses the real graph of the residue function. Curvature
controls compatibility between congruences, without imposing coherence
or restricting the prime factors of the moduli. It supplies a new
endpoint theorem, not a solution of the full delayed-union problem.

## Curved perturbations of every slope

**Theorem.** Fix $0<\alpha<1$ and $\theta\in[0,1)$, and set
$$
 a_q=\lfloor\theta q+q^\alpha\rfloor.
 \tag{1}
$$
These residues satisfy $0\le a_q<q$ for all sufficiently large $q$.
Let $D$ be a set of distinct moduli, and fix an integer $\ell\ge1$.
Suppose the points $r_q=\ell q+a_q$ satisfy
$$
 r_q\not\equiv a_p\pmod p
 \qquad(p,q\in D,\ p<q).
 \tag{2}
$$
Then $D$ and $\{r_q:q\in D\}$ have natural density zero.

Consequently, in every singleton system with residues (1), all first
kills with bounded quotient $(n-a_q)/q$ form a naturally null set.
The same assertion allows arbitrary uniformly bounded integer errors
in (1). There is no Diophantine condition on $\theta$.

The earlier [slope theorem](irrational_slope_endpoints.md) required a
Brjuno hypothesis for natural endpoint nullity and admitted a Liouville
obstruction without that hypothesis. Here the sublinear curved term
removes that restriction. Neither theorem controls unbounded quotients.

## Curvature bounds the dyadic second moment

On Haar space let
$$
 Y_Q=\sum_{Q\le q<2Q}\mathbf1_{[a_q]_q}.
$$
We prove, uniformly in $Q\ge2$ and $\theta$,
$$
 \mathbb E Y_Q^2\le M_\alpha<\infty.
 \tag{3}
$$
The finitely many initially unnormalized residues cause no difficulty
for this full-cylinder assertion.

Consider compatible distinct $q<r$ in the dyadic block and write
$$
 g=(q,r),\quad q=gu,\quad r=g(u+k),\quad T=Q/g,
 \quad 1\le k<T.
$$
Compatibility and the error of less than one in a difference of floors
give
$$
 \left\|\theta k+\Phi_{g,k}(u)\right\|<1/g,
 \qquad
 \Phi_{g,k}(u)=\frac{(g(u+k))^\alpha-(gu)^\alpha}{g}.
 \tag{4}
$$
Put $w=Q^{\alpha-1}$. Since $F(x)=x^\alpha$ has second derivative
of constant sign, with $|F''(x)|\asymp_\alpha w/Q$ on $[Q,2Q]$,
$$
 |\Phi'_{g,k}(u)|\asymp_\alpha kw/T.
 \tag{5}
$$
The allowed interval of $u$ has length at most $T$, and its image has
length $O_\alpha(kw)$. Thus (4) is the union of at most
$O_\alpha(kw+1)$ intervals, each of length at most
$O_\alpha(T/(gkw))$. Its number of integer points is at most
$$
 O_\alpha\left((kw+1)\left(\frac{T}{gkw}+1\right)\right).
 \tag{6}
$$
This estimate is uniform in the phase $\theta k$.

Summing (6) over $1\le k<T$ bounds the number of candidate pairs
for a fixed $g$ by
$$
 O_\alpha\left(\frac{T^2}{g}
       +\frac{T\log(2T)}{gw}+wT^2+T\right).
$$
Dropping the coprimality condition on $u,u+k$ only increases this
count. Every pair of exact gcd $g$ contributes $g/(qr)\le g/Q^2$
to the Haar second moment. Such distinct pairs have $g<Q$.
After summing over $g$, including both orders, and adding the diagonal,
$$
 \mathbb E Y_Q^2
 \ll_\alpha 1+w\log(2Q)+\frac{\log^2(2Q)}{Qw}.
 \tag{7}
$$
For example the first term uses $\sum_g g^{-2}<\infty$, and the
third uses $\sum_{g\le Q}\log(2Q/g)/g\ll\log^2(2Q)$.
Since $Qw=Q^\alpha$ and $w=Q^{\alpha-1}$, the right side is
bounded in $Q$. This proves (3).

## The two residue coordinates become uniform

For every fixed integer $P\ge1$ and residues $t,b\pmod P$,
$$
 \#\{Q\le q<2Q:q\equiv t\pmod P,\ a_q\equiv b\pmod P\}
 =Q/P^2+o_{\alpha,\theta,P}(Q).
 \tag{8}
$$

If $\theta$ is irrational, write $q=t+Pm$ and
$y_m=(\theta q+q^\alpha)/P$. For every nonzero integer $h$,
$$
 e(hy_m)=e(h\theta t/P)e(h\theta m)e(hq^\alpha/P),
 \qquad e(x)=\exp(2\pi i x).
$$
The partial sums of $e(h\theta m)$ are bounded. The last factor
has total variation $O_{h,P}(Q^\alpha)$, so Abel summation bounds
the exponential sum by $O_{h,\theta,P}(1+Q^\alpha)=o(Q)$.
Trigonometric approximation therefore makes $y_m\bmod1$ uniform.
The condition $a_q\equiv b\pmod P$ is precisely
$\{y_m\}\in[b/P,(b+1)/P)$, proving (8).

If $\theta=A/d$ is rational, refine to $q\equiv r\pmod{dP}$.
On this progression, $a_q\bmod P$ equals
$\lfloor q^\alpha+Ar/d\rfloor\bmod P$.
For fixed $L,M,\kappa$, the inverse-level intervals for
$x^\alpha+\kappa$ on $[Q,2Q)$ number $O(Q^\alpha)$, each has
length $O(Q^{1-\alpha})$, and the full interval lengths are
increasing by convexity of $x^{1/\alpha}$.
Abel summation against the mean-zero periodic sequence
$\mathbf1_{j\equiv b\ (M)}-1/M$ consequently shows that the
levels with index $j\equiv b\pmod M$ have total length
$Q/M+O(Q^{1-\alpha})$. The two possibly clipped end intervals
have the same error bound. Counting $q\equiv r\pmod L$ on each
level incurs a total error $O(Q^\alpha)$. Hence
$$
 \#\{Q\le q<2Q:q\equiv r\pmod L,
                    \lfloor q^\alpha+\kappa\rfloor\equiv b\pmod M\}
 =\frac{Q}{LM}+O_{\alpha,L,M,\kappa}(Q^\alpha+Q^{1-\alpha}).
$$
Take $L=dP,M=P$ and sum over the $d$ possible $r$ to prove (8).

## Transfer through an arbitrary old survivor set

Let $C_q=[a_q]_q$, $U=\bigcup_{q\in D}C_q$, and take a finite
prefix $D_0\subset D$. Write
$$
 U_0=\bigcup_{q\in D_0}C_q,\qquad
 S=\widehat{\mathbb Z}\setminus U_0,\qquad
 \tau=\mu(U\setminus U_0).
$$
Let $P$ be an old period and identify $S$ with its surviving residues
modulo $P$. If $S$ is empty, (2) allows no later selected endpoints.
Otherwise, for $q>\max D_0$, define
$$
 d=(q,P),\qquad f(q)=\frac{|S\cap[a_q]_d|}{P/d}.
$$
Here $f(q)>0$ for selected $q$, by (2), and CRT gives
$\mu(C_q\cap S)=f(q)/q$.

For fixed $t=q\bmod P$, put $d=(t,P)$ and define $f(t,b)$ in
the same way. Translation by $\ell t$ preserves every fiber modulo
$d$, so exact counting gives
$$
 \sum_{\substack{b\bmod P\\b+\ell t\in S}}\frac1{f(t,b)}
 =\frac Pd\,\#\{\text{nonempty }S\text{-fibers modulo }d\}
 \le P.
 \tag{9}
$$
Equation (8), with this fixed period, therefore implies
$$
 \sum_{\substack{Q\le q<2Q\\a_q+\ell q\bmod P\in S}}\frac1{f(q)}
 \le Q+o(Q).
 \tag{10}
$$

Put $m_Q=|D\cap[Q,2Q)|$ and
$Z_Q=\sum_{q\in D\cap[Q,2Q)}\mathbf1_{C_q\cap S}$.
Its support has measure at most $\tau$, and (3) gives
$\mathbb E Z_Q^2\le M_\alpha$. Twice applying Cauchy--Schwarz yields
$$
 \begin{aligned}
 m_Q^2
 &\le\left(\sum_{q\in D\cap[Q,2Q)}f(q)\right)(Q+o(Q))\\
 &\le2Q(Q+o(Q))\,\mathbb E Z_Q\\
 &\le2Q(Q+o(Q))\sqrt{M_\alpha\tau}.
 \end{aligned}
$$
Thus
$$
 \limsup_{Q\to\infty}\frac{m_Q}{Q}
 \le\sqrt2\,M_\alpha^{1/4}\tau^{1/4}.
$$
Exhausting $D$ by finite prefixes makes $\tau\to0$. Dyadic summation
proves $d(D)=0$. Since $r_q\ge q$, the endpoint set is naturally null
as well. The constant in this conclusion does not grow with the old
period; the limit in $Q$ was taken while that period was fixed.

For actual bounded-quotient first kills, partition by the finitely many
values of $\ell=(n-a_q)/q$. At each such point all earlier moduli
are active, so (2) holds. A fixed integer shift of all the residues
changes neither the compatibility proof nor uniformity in (8).
Partitioning by the finitely many error values proves the stated
bounded-perturbation extension.

## A fixed flat profile can have large natural endpoint spikes

The curved theorem cannot be replaced by an assertion for every smooth
increasing sublinear profile. In fact the fixed choice
$$
 a_q=\lfloor\log\log q\rfloor
 \tag{11}
$$
admits a globally private endpoint family of positive upper natural
density. Its full delayed union can fail to have natural density,
although it has logarithmic density. All selected moduli below are
large enough for (11) to be normalized.

Fix $0<\varepsilon<1/3$. At stage $j$, choose an integer $c_j$
exceeding every earlier endpoint, and put
$$
 Q_j=\left\lfloor\exp(\exp(c_j+1/2))\right\rfloor.
$$
Writing $P_{\mathrm{old}}$ for the old period, choose $c_j$ so large
that $P_{\mathrm{old}}/Q_j\le2^{-j}$ and
$$
 \mu(M([Q_j,2Q_j)\cap\mathbb N))\le\varepsilon2^{-j}.
 \tag{12}
$$
This is possible by the uniform
[multiples-window limit](common_shift_blocks.md). Throughout the
block, $\lfloor\log\log q\rfloor=c_j$ for large $c_j$.
Retain those $q\in[Q_j,2Q_j)$ for which $q+c_j$ avoids the earlier
full union. Its Haar measure is at most $\varepsilon$, so periodic
counting retains at least $(1-\varepsilon-o(1))Q_j$ moduli.

The new endpoints have pairwise differences less than $Q_j$, so are
private within their block. They avoid earlier cylinders by selection.
Every earlier endpoint is less than $c_j$, the least positive
representative of each new cylinder, so the reverse privacy holds too.
Also $q\le q+c_j<2q$. Consequently the full endpoint set $R$ satisfies
$$
 \overline d(R)\ge(1-\varepsilon)/2.
 \tag{13}
$$

Let $D_j$ be the retained moduli and $B_j$ their delayed union.
It is exactly $c_j+M(D_j)$. Positive translation and the exact
multiples harmonic inequality give, for every $X$,
$$
 H_{B_j}(X)\le H_{M(D_j)}(X)
 \le\varepsilon2^{-j}H_{\lfloor X\rfloor}.
$$
Thus finite-block approximation proves logarithmic density
$\beta=\mu(\bigcup_j[c_j]_{D_j})\le\varepsilon$ for
$B=\bigcup_jB_j$, where $[c_j]_{D_j}$ denotes the full block union.
But $B$ contains $R$, so its upper natural density is greater than
$\beta$ by (13). It has no natural density. Its lower natural density
is $\beta$: finite prefixes give the lower bound, and logarithmic
density gives the reverse inequality for the lower natural density.

The endpoint set $R$ itself has logarithmic density zero by the
[summable-footprint endpoint bound](compression_and_blocks.md#summable-footprints-and-selected-endpoints-proved).
The independent [ordered-run criterion](ordered_coherent_runs.md)
also gives logarithmic endpoint nullity for every system with (11).
This example is not a counterexample to Problem 25.

## The remaining gap

Even in the curved class, its full arithmetic cylinder trace cannot
replace its delayed union. For $\theta=0$, $\alpha=1/2$, select
$q=m^2$, $m\ge M\ge2$. The canonical residue is $m$, so the full
cylinders cover every integer at least $M$ through an inactive root.
Their delayed union, however, has natural density at most
$\sum_{m\ge M}m^{-2}\le1/(M-1)$, by the summable-moduli theorem.
Thus full-trace regularity cannot be assumed in a dynamical argument
for these profiles.

The curved theorem proves natural nullity of every fixed quotient range,
not tightness uniformly as the quotient bound tends to infinity.
It therefore supplies no density theorem for the entire curved-profile
union. The flat example shows why natural-density claims require care,
while the run criterion gives a different logarithmic endpoint regime.
No general endpoint theorem or control of unbounded-quotient first kills
has resulted from this approach.
