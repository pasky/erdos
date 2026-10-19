---
name: research/erdos_25/prime_filtration
desc: Conditional survivor entropy, a universal singleton prime-stage second moment, and a limited activated arithmetic comparison.
tags: [entropy, prime-filtration, sieve, partial-results]
sources: []
created: 2026-09-22T04:28:00Z
updated: 2026-09-24T22:13:01Z
---


# research/erdos_25/prime_filtration

***

This approach exposes entire prime-adic coordinates rather than
installing congruences in increasing modulus order. The following
estimates are proved, but their transfer to the full activated integer
orbit remains incomplete. All moduli are distinct unless indicated.
The case $q=1$ is trivial and is omitted.

Write $G=\prod_p\mathbb Z_p$, let $S$ be the full Haar survivor set,
and suppose $\mu(S)=\delta>0$. Put $\nu=\delta^{-1}\mathbf1_S\mu$.
For $q=p^e m$ with $P^+(m)<p$, and an earlier-coordinate configuration
$x$, define the forbidden new-coordinate fraction
$$
 \alpha_p(x)=\mu_p\left(
   \bigcup_{\substack{q=p^e m\,:
               x\equiv a_q\pmod m}}[a_q]_{p^e}\right).
 \tag{1}
$$
Use $P^+(1)=1$. This includes every chosen modulus with largest
prime factor $p$, regardless of the size of its smaller-prime part.

## A finite conditional entropy budget

With earlier-coordinate expectation under $\nu$,
$$
 \sum_p\mathbb E_\nu[-\log(1-\alpha_p)]\le\log(1/\delta).
 \tag{2}
$$
In particular $\sum_p\mathbb E_\nu\alpha_p<\infty$.

For a proof, the conditional law $K_p(x,\cdot)$ of the $p$-coordinate
under $\nu$ is supported on a set of $\mu_p$-measure at most
$1-\alpha_p(x)$. Relative entropy therefore satisfies
$$
 D(K_p(x,\cdot)\Vert\mu_p)\ge-\log(1-\alpha_p(x)).
$$
This follows by conditioning Haar on the allowed set and using
nonnegativity of relative entropy. Fibers with $\alpha_p=1$ have
zero earlier marginal under $\nu$.
The chain rule, over finitely many prime coordinates, gives
$$
 \sum_{p\le P}\mathbb E_\nu D(K_p\Vert\mu_p)
 =D(\nu_{\le P}\Vert\mu_{\le P})\le\log(1/\delta).
$$
For completeness, if
$h_P=\mathbb E_\mu(\mathbf1_S\mid\mathcal F_{\le P})$, the right
side equals
$$
 \log(1/\delta)+\delta^{-1}\mathbb E_\mu[h_P\log h_P].
$$
The martingale $h_P$ converges to $\mathbf1_S$; bounded convergence
of $h_P\log h_P$ shows that this expression tends to
$\log(1/\delta)$. Summing the preceding conditional lower bounds
proves (2). This entropy statement itself permits multiple residues.

## A summable Haar second moment using singleton distinctness

The union bound in the new coordinate gives
$$
 \alpha_p(x)\le A_p(x):=
 \sum_{q=p^em}p^{-e}\mathbf1_{[a_q]_m}(x).
$$
Since each $p^em$ occurs at most once, pairwise CRT and enlargement
to all $p$-smooth smaller parts give
$$
 \begin{aligned}
 \mathbb E_\mu\alpha_p^2
 &\le\mathbb E_\mu A_p^2\\
 &\le\frac1{(p-1)^2}
    \sum_{P^+(m),P^+(r)<p}\frac{(m,r)}{mr}\\
 &=U_p:=\frac1{(p-1)^2}
       \prod_{\ell<p}\frac{1+1/\ell}{(1-1/\ell)^2}
 \ll\frac{\log^3(2p)}{p^2}.
 \end{aligned}
 \tag{3}
$$
Indeed the local series is
$\sum_{i,j\ge0}\ell^{-\max(i,j)}
=(1+1/\ell)/(1-1/\ell)^2$.
The product in (3) is at most
$\prod_{\ell<p}(1-1/\ell)^{-3}$, so the already checked elementary
[Euler-product bound](coherent_power_cutoff.md#two-elementary-sieve-ingredients)
applies. Thus $\sum_p\mathbb E_\mu\alpha_p^2<\infty$ universally.
Repeated residues would add multiplicities in this calculation.

## An activated arithmetic second moment

For an integer $n$, truncate using the actual activation condition:
$$
 A_p(n)=\sum_{\substack{q=p^em\le n\,: P^+(m)<p}}
               p^{-e}\mathbf1_{n\equiv a_q\pmod m}.
$$
Then, for $X\ge2$,
$$
 \frac1{H_{\lfloor X\rfloor}}\sum_{n\le X}\frac{A_p(n)^2}{n}
 \le U_p+\frac{2X}{H_{\lfloor X\rfloor}(p^2-1)^2}.
 \tag{4}
$$
For each compatible pair $q=p^em$, $q'=p^fr$, the smaller-coordinate
conditions form one class modulo $[m,r]$, counted only for
$n\ge T=\max(q,q')$. Its harmonic sum is at most
$$
 H_{\lfloor X\rfloor}/[m,r]+1/T.
$$
To check the error, normalize that class modulo $[m,r]$: its only
possible positive root below the modulus contributes at most $1/T$,
and the later terms are bounded by the harmonic progression of zero
residue. The main terms sum to at most $U_p$ as in (3).

For fixed $e,f$, discarding smoothness only increases the error. The
number of pairs with $\max(p^em,p^fr)\le t$ is at most
$t^2/p^{e+f}$. Partial summation therefore bounds the sum of
$1/\max(p^em,p^fr)$ below $X$ by $2X/p^{e+f}$.
Multiplication by $p^{-e-f}$ and summation over $e,f\ge1$ gives
$2X/(p^2-1)^2$, proving (4).

For any fixed threshold $a>0$, Markov's inequality and a union bound
now show that the normalized harmonic mass of integers $n\le X$
with $A_p(n)>a$ for some $p>Y$ is at most
$$
 a^{-2}\left[
 O\left(\frac{\log^3(2Y)}Y\right)
 +O\left(\frac{X}{H_{\lfloor X\rfloor}Y^3}\right)\right].
 \tag{5}
$$
This is useful, for example, at $Y=X^{1/3}$. It bounds large-potential
fibers, not the total number of deletions by those primes. It gives no
vanishing bound for the remaining moving prime range.
In fact, a uniform original-activation second-moment bound for the
uncapped $A_p$ is [false](#a-uniform-original-activation-second-moment-bound-is-false).
The counterexample below does not refute such a bound for the exact
forbidden fraction $\alpha_p$.

## Positive survivor measure gives no pointwise distortion cap

For a prime $p$, use moduli $q_j=pj$, $1\le j<p$, and residues
$$
 a_j\equiv0\pmod j,\qquad a_j\equiv j\pmod p.
$$
These moduli are distinct and all have largest prime factor $p$.
The full survivor density is at least
$1-H_{p-1}/p\to1$. Nevertheless, on the earlier-coordinate fiber
$x\equiv0\pmod L$, where $L=\operatorname{lcm}(1,\ldots,p-1)$,
the stage removes $p-1$ of the $p$ digits. Conditional survival forces
the zero digit, so its density relative to Haar in that coordinate is
$p$. The earlier fiber has positive $\nu$-mass $1/(\delta pL)$.
Thus (2) cannot be replaced by a uniform pointwise bound based on
$\delta$, even when $\delta$ tends to one.

The remaining difficulty is specific: (2) is averaged under the full
survivor law $\nu$, while (4)--(5) sample actual integers. Nonlinear
events determined by earlier prime coordinates can have periods far
larger than $X$, despite individual active moduli being at most $X$.
No transfer estimate connecting these two controls, and no proof of
the required lower logarithmic density, was obtained.

The later [full-survivor trace obstruction](full_survivor_trace_obstruction.md)
shows that directly sampling the canonical earlier-coordinate densities
of this infinite law $\nu$ can in fact give a nonzero signed trace,
even at a fixed prime. Uniform high-prime cancellation also fails for
these weights despite $\delta>1/4$, weights bounded by four, and the
pointwise bound $\alpha_p(n)\le1/p$. The example's actual delayed
sieve has natural density. Thus a viable transfer must retain finite
activation or impose additional arithmetic information; the infinite
conditional marginals themselves are not available arithmetic weights.

## Exact arithmetic moments with stronger power activation

There is a useful exact transfer under a different activation rule. It
does **not** establish density even for that stronger rule; the remaining
conditional-trace obstruction is stated below.

Fix an integer $k\ge2$ and replace activation by $n\ge q^k$. Put
$$
 A_{p,k}(n)=\sum_{\substack{q=p^em,\ P^+(m)<p\\q^k\le n}}
           p^{-e}\mathbf1_{n\equiv a_q\pmod m}.
$$
For every integer $X\ge1$, both natural and harmonic moments obey
$$
 \frac1X\sum_{n\le X}A_{p,k}(n)^k\le U_{p,k},\qquad
 \frac1{H_X}\sum_{n\le X}\frac{A_{p,k}(n)^k}{n}\le U_{p,k},
 \tag{6}
$$
where
$$
 U_{p,k}=\frac1{(p-1)^k}
 \prod_{\ell<p}\left(\sum_{a\ge0}
                  \frac{(a+1)^k-a^k}{\ell^a}\right)
 \ll_k\frac{\log^{2^k-1}(2p)}{p^k}.
 \tag{7}
$$
In particular $U_{p,2}=U_p$: quadratic activation removes the entire
$X$-dependent error from (4).

To prove this, expand the $k$th power. A compatible tuple
$q_j=p^{e_j}m_j$ specifies one residual class modulo
$d=[m_1,\ldots,m_k]$. Every active point in that tuple satisfies
$$
 n\ge\max_jq_j^k\ge\prod_jq_j\ge d.
$$
The exact delayed progression bounds are therefore at most $X/d$ for
counting and $H_X/d$ for harmonic sums. Discarding compatibility and
enlarging the modulus collection increases the resulting positive sum.
Distinctness ensures that each $p^em$ occurs at most once. The sums over
$e_1,\ldots,e_k\ge1$ give $(p-1)^{-k}$; at a smaller prime $\ell$,
the number of exponent tuples with maximum exactly $a$ is
$(a+1)^k-a^k$. This gives the product (7). Its local factor is
$1+(2^k-1)/\ell+O_k(\ell^{-2})$, so the elementary Euler-product
bound proves the last estimate in (7).

Consequently, for $Y\ge2$ and $t>0$, the natural or normalized harmonic
mass below $X$ of
$$
 \{n:\exists p>Y,\ A_{p,k}(n)>t\}
$$
is at most
$$
 C_k t^{-k}\frac{\log^{2^k-1}(2Y)}{Y^{k-1}},
 \tag{8}
$$
uniformly in $X$. This follows from Markov's inequality, a union bound,
and summing (7), even over all integers greater than $Y$.

The missing transfer is still not a moment estimate of this kind.
Haar prime-stage normalization uses cancellation while all earlier
coordinates are fixed. An arithmetic distortion argument would require
control of signed expressions of the form
$$
 \frac1{H_X}\sum_{n\le X}
 \frac{w_{p-}(n)(\mathbf1_{B_p}(n)-\alpha_p(n))}{n},
$$
where $w_{p-}$ is a nonlinear accumulated weight depending on arbitrarily
many earlier congruences. Bounding products of $k$ active congruences
does not bound this trace. Their accumulated CRT conductor can exceed
$n$ despite $q^k\le n$ for every individual active modulus. No arithmetic
conditional cancellation has been proved, so neither (6) nor (8) is a
density theorem for arbitrary residues.

## Removing repeated largest prime factors from the tail

There is a simple exact reduction, valid for arbitrary residues. Put
$$
 \mathcal R=\{q\ge2:P^+(q)^2\mid q\}.
$$
Unique factorization and the established elementary Euler-product bound
give
$$
 \begin{aligned}
 \sum_{q\in\mathcal R}\frac1q
 &=\sum_p\left(\sum_{e\ge2}p^{-e}\right)
          \sum_{P^+(m)<p}\frac1m\\
 &=\sum_p\frac1{p(p-1)}
             \prod_{\ell<p}(1-1/\ell)^{-1}
 \ll\sum_p\frac{\log(2p)}{p^2}<\infty.
 \end{aligned}
 \tag{9}
$$
Here $P^+(1)=1$. Moreover, the portion with $P^+(q)>Y$ is
$O(\log(2Y)/Y)$, by comparison with the corresponding sum over
all integers greater than $Y$.

For each normalized residue, activation gives at most $X/q$ hits
below $X$. Thus moduli from $\mathcal R$ beyond a numerical cutoff
$Q$ have, uniformly in $X$, at most
$$
 X\sum_{\substack{q\in\mathcal R\\q>Q}}\frac1q
$$
hits. Their tails are negligible in upper natural density and hence
in upper logarithmic density. This does not say that deleting the
whole family $\mathcal R$ leaves the density unchanged: its fixed
initial classes can have positive density and must be retained in
finite approximations.

Consequently, to prove finite-congruence logarithmic approximation in
general, it suffices to treat the core
$$
 q=pm,\qquad P^+(m)<p,
$$
and then add back the reciprocal-summable family by the preceding
tail estimate. In this core the prime-stage forbidden fraction is
exactly the number of distinct forbidden $p$-digits represented by
matching smaller-coordinate classes, divided by $p$. This reduction
does not bound that digit count on the activated integer orbit and
does not supply the missing conditional trace estimate.

## A uniform original-activation second-moment bound is false

Despite the summable Haar bound (3), the original-activation arithmetic
second moments of $A_p$ need not be uniformly bounded, even for systems
whose moduli all have total prime-factor rank five and whose largest
prime factor occurs only once.

Let $p$ tend to infinity through primes, put $X=p^5$, and let
$\mathcal D_p$ consist of the products of four distinct primes at most
$p/2$. Unique factorization and Chebyshev's prime-counting bounds give
$$
 M_p:=|\mathcal D_p|
 =\binom{\pi(p/2)}4\asymp \frac{p^4}{(\log p)^4}.
$$
For each $m\in\mathcal D_p$, install the single modulus $q=pm$ with
normalized residue
$$
 a_{pm}=X-pm\left\lfloor\frac{X}{pm}\right\rfloor.
$$
These moduli are distinct, satisfy $q\le p(p/2)^4<X$, and have
$P^+(q)=p$, $v_p(q)=1$, and $\Omega(q)=5$. Thus they already belong
to the core retained in the preceding reduction.

At the integer $n=X$, every smaller-coordinate condition matches:
$X\equiv a_{pm}\pmod m$, and every modulus is active. Hence
$$
 A_p(X)=\frac{M_p}{p},\qquad
 \frac1{H_X}\sum_{n\le X}\frac{A_p(n)^2}{n}
 \ge\frac{M_p^2}{p^2XH_X}
 \gg\frac{p}{(\log p)^9}\longrightarrow\infty.
$$
In particular, for every fixed $Y$, the supremum over finite systems
and cutoffs of
$$
 \sum_{p>Y}\frac1{H_X}\sum_{n\le X}\frac{A_p(n)^2}{n}
$$
is infinite. The natural-average second moment also diverges, since
its corresponding one-point lower bound is
$M_p^2/(p^2X)\gg p/(\log p)^8$.

This construction does **not** produce a large exact forbidden
fraction. Every assigned residue has the same $p$-digit, namely
$a_{pm}\equiv X\equiv0\pmod p$. Consequently $\alpha_p\le1/p$ on
every smaller-coordinate fiber, with equality at $n=X$. The obstruction
is multiplicity in the union-bound potential $A_p$, not a failure of a
uniform estimate for $\alpha_p$. No conclusion about the remaining
conditioned arithmetic trace follows from this example.

## Information as finite congruences activate

The obstruction to infinite-survivor marginals does not invalidate the
following **finite** information identity. It still supplies no arithmetic
trace bound.

For a finite increasing family, let
$$
 S_j=\bigcap_{i\le j}C_i^c,\quad
 \delta_j=\mu(S_j)>0,\quad
 \nu_j=\delta_j^{-1}\mathbf1_{S_j}\mu,
 \quad S_0=G,\quad\delta_0=1.
$$
Work modulo a common finite period, exposing its prime-power coordinates
in increasing prime order. Write $K_p^{(j)}$ for the conditional law
of the coordinate at $p$ under $\nu_j$, given earlier coordinates.
Then
$$
 \sum_{j=1}^J\sum_p\mathbb E_{\nu_j}
   D(K_p^{(j)}\Vert K_p^{(j-1)})
 =\log\frac1{\delta_J}.
 \tag{10}
$$
The expectation is over the earlier-coordinate marginal of $\nu_j$.
Conditional versions on null fibers do not matter, since
$\nu_j\ll\nu_{j-1}$.

Indeed, on $S_j$ the density ratio
$d\nu_j/d\nu_{j-1}$ equals $\delta_{j-1}/\delta_j$, so
$D(\nu_j\Vert\nu_{j-1})=\log(\delta_{j-1}/\delta_j)$.
The finite relative-entropy chain rule, followed by telescoping in
$j$, proves (10). In particular, if the infinite survivor measure
is $\delta>0$, every finite budget is at most $\log(1/\delta)$.
The identity does not use singleton distinctness.

There are also exact projection recursions. Put
$$
 h_{p,j}=\mathbb E_\mu(\mathbf1_{S_j}\mid\mathcal F_{\le p}),
 \qquad w_{p,j}=h_{p,j}/\delta_j,
 \qquad F_j=S_{j-1}\setminus S_j,\quad e_j=\mu(F_j).
$$
Linearity and $\delta_j=\delta_{j-1}-e_j$ give
$$
 h_{p,j}-h_{p,j-1}
 =-\mathbb E_\mu(\mathbf1_{F_j}\mid\mathcal F_{\le p}),
$$
$$
 w_{p,j}-w_{p,j-1}
 =\frac{e_jw_{p,j-1}
       -\mathbb E_\mu(\mathbf1_{F_j}\mid\mathcal F_{\le p})}
       {\delta_j},
 \qquad 0\le w_{p,j}\le1/\delta_J.
 \tag{11}
$$

To retain actual activation, let $S_n$ use exactly the moduli
$q\le n$, with $\delta_n=\mu(S_n)$, and define $h_{p,n}$
accordingly. For each finite cutoff $X$, both telescopes are finite
and yield
$$
 \begin{aligned}
 \sum_{n\le X}\frac{\mathbf1_A(n)-\delta_n}{n}
 &=\sum_p\sum_{n\le X}
        \frac{h_{p,n}(n)-h_{p-,n}(n)}n\\
 &=-\sum_{q\le X}\sum_{q\le n\le X}
        \frac{\mathbf1_{F_q}(n)-e_q}{n}.
 \end{aligned}
 \tag{12}
$$
Here $h_{p-,n}$ fixes primes below $p$, and the initial prime
projection is the constant $\delta_n$. At an active point all
earlier congruences are active, so the full first-kill cells $F_q$
give exactly the second equality.

Thus exchanging the prime and activation sums reproduces the original
first-kill discrepancy. The bounded information in (10) is integrated
under changing Haar-conditioned laws, whereas (12) samples their changing
functions at $x=n$. No estimate transferring the former to this
diagonal trace was obtained. Since
$H_X^{-1}\sum_{n\le X}\delta_n/n\to\delta$, an
$o(\log X)$ bound for (12) is still precisely the required
candidate-density conclusion, not a consequence of the telescoping.
