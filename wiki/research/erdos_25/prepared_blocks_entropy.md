---
name: research/erdos_25/prepared_blocks_entropy
desc: Period-independent entropy and square-root bounds for prepared small-center blocks, without coprimality, and limits on disjoint amplification.
tags: [entropy, partial-results, obstructions]
sources: []
created: 2026-09-22T06:10:00Z
updated: 2026-09-24T22:13:01Z
---


# research/erdos_25/prepared_blocks_entropy

***

These results control an entire class of preparations, rather than an
individual unusually small first-kill cell. They do not prove the general
first-kill entropy conjecture.

Write $H_X=H_{\lfloor X\rfloor}$ and
$c_i(X)=H_{E_i}(X)/H_X$, where $E_i$ is the actual delayed first-kill
set and $e_i$ the full first-kill Haar measure. We use the established
valuation-model bound: for a zero-residue first-kill cell $F_i^0$,
$$
 H_{F_i^0}(X)\le Z_X\mu(F_i^0),\qquad
 Z_X=\prod_{p\le X}(1-1/p)^{-1}\le C H_X.
 \tag{1}
$$
This follows because the geometric valuation model assigns each
$X$-smooth integer $n$ probability $1/(Z_Xn)$; the cell is determined
by valuations. Only active moduli $q\le X$ need be retained.

## A period barrier for a prepared block

Let a finite preparatory sieve have period $P$ and full survivor density
$\delta>0$. Append distinct moduli $q>P$, all coprime to $P$, and give
them one common normalized integer residue
$$
 0\le\alpha<\min q.
$$
Then, uniformly in the appended family and $X\ge2$,
$$
 \sum_{i\text{ appended}}c_i(X)\log_+\frac{c_i(X)}{e_i}
 \le\delta\log\frac C\delta.
 \tag{2}
$$
The appended family may be finite or infinite. Its moduli are still
installed in increasing numerical order.

Let $e_i^0$ be the first-kill density in the zero-residue system formed
by the appended moduli alone. Their prime coordinates are disjoint from
those of $P$, so translation and independence give
$e_i=\delta e_i^0$. If $n$ is an actual appended first kill, then
$m=n-\alpha=tq_i\ge q_i$ lies in its corresponding zero-residue
first-kill cell: otherwise an earlier appended class would cover $n$.
Also $m\le n\le X$ and $1/n\le1/m$. Thus (1) gives
$$
 c_i(X)\le C e_i^0,\qquad c_i(X)/e_i\le C/\delta.
 \tag{3}
$$
All appended hits occur beyond $P$, where every preparatory class is
active. There are $\delta P$ surviving residues modulo $P$. The exact
delayed harmonic progression bound on each of them gives
$$
 \sum_{i\text{ appended}}c_i(X)
 \le \frac{\delta P}{P H_X}H_{\lfloor X/P\rfloor}\le\delta.
$$
Together with (3), this proves (2).

For the [energy construction](energy_counterexample.md), $P=L$ and
$\delta=1/L$. Its old full cylinders are disjoint, so their $e_i=1/q_i$
and $c_i\le1/q_i$ make their positive entropy terms zero. Consequently
its entire normalized entropy is at most $\log(CL)/L$. The lower bound
already proved there is $\gg(\log L)/L$, so its order is exactly
$\Theta((\log L)/L)$. Changing the cutoff or the sparse residue channel
within this mechanism cannot refute constant normalized entropy.

The hypotheses matter. The argument does not handle appended moduli
smaller than the preparatory period or arbitrary moving centers. The
shared-prime restriction can now be removed, as proved next. Neither
version applies to every conditioned block.

## Removing coprimality by exact gcd strata

**Theorem.** Let $S$ be any $P$-periodic set of density $\delta$.
Append a family of moduli $q>P$ with one common normalized integer
center $0\le\alpha<\min q$. Write
$$
 U=\bigcup_q[\alpha]_q,\qquad
 \tau=\mu(S\cap U),\qquad
 T=S\cap\bigcup_q\{\alpha+tq:t\ge1\}.
$$
There is an absolute $C\ge1$ such that, with
$A_X=H_{\lfloor X/P\rfloor}/H_{\lfloor X\rfloor}$ and $H_0=0$,
$$
 \left(\frac{H_T(X)}{H_{\lfloor X\rfloor}}\right)^2
 \le C A_X\tau.
 \tag{5}
$$
If $S$ is the survivor set of a finite preparatory sieve, its appended
first-kill masses also satisfy
$$
 \sum_{i\text{ appended}}c_i(X)\log_+\frac{c_i(X)}{e_i}
 \le A_X\delta\log\frac C\delta.
 \tag{6}
$$
Interpret the right side as zero when $\delta=0$. No coprimality with
$P$ is assumed. The constants do not depend on $P$ or the center.

**Proof.** If $X\le P$ there are no hits. Otherwise discard appended
moduli greater than $X$, which does not change the trace or any active
first-kill cell. This can only decrease $\tau$, so it suffices to prove
the assertions for the retained finite family.

For an actual hit put $m=n-\alpha>0$, $g=(m,P)$, $R=P/g$, and
$m=gu$, so $(u,R)=1$. For a modulus $q$, let $h=(q,P)$. It can
divide $m$ only if $h\mid g$. When $h\mid g$,
$$
 q\mid gu\quad\Longleftrightarrow\quad r:=q/h\mid u,
 \qquad (r,R)=1,\qquad r>P/h\ge R.
 \tag{7}
$$
Indeed $(q/h,P/h)=1$ and $g/h\mid P/h$. Let $D_g$ be the set
of effective moduli $r$ arising in this way, and put
$$
 \beta_g=\mu(M(D_g)),\qquad
 S_g=\{u:(u,R)=1,\ \alpha+gu\in S\},\qquad
 \delta_g=d(S_g),\qquad c_R=\varphi(R)/R.
$$
The set $S_g$ is $R$-periodic. Every generator of $M(D_g)$ is
coprime to $R$, so CRT independence gives the Haar contribution of
this stratum as
$$
 \tau_g=\delta_g\beta_g/g,\qquad \sum_{g\mid P}\tau_g=\tau.
 \tag{8}
$$

Every actual hit in the stratum has $u\ge r>R$. Also
$1/n\le1/(gu)$ and $u\le X/g$. Summing the exact delayed
progression bound over the $\delta_gR$ residues of $S_g$ gives
$$
 h_g:=\frac{H_{T_g}(X)}{H_{\lfloor X\rfloor}}
 \le A_X\delta_g/g.
 \tag{9}
$$
For a second bound, use the geometric valuation model on primes at
most the **global cutoff** $X$, omitting primes dividing $R$.
Its normalizing product is
$$
 Z_X^{(R)}=c_R Z_X\le Cc_RH_{\lfloor X\rfloor},
$$
since all primes dividing $R$ are at most $P<X$. Every sampled
$u\le X/g$ with $(u,R)=1$ is an atom of this model. The probability
of $M(D_g)$ is exactly $\beta_g$, since its retained generators are
coprime to $R$ and at most $X$. Dropping the restriction $u\in S_g$
therefore gives $h_g\le Cc_R\beta_g/g$. Combining this with (9),
$$
 h_g^2\le CA_Xw_g\tau_g,
 \qquad w_g=c_R/g=\varphi(P/g)/P,
 \qquad\sum_{g\mid P}w_g=1.
$$
Cauchy--Schwarz and (8) prove (5).

For (6), retain the original ordering of appended moduli. In a fixed
$g$-stratum the effective zero classes have first-kill measures
$e^0_{i,g}$; incompatible classes contribute zero, and repeated
effective moduli have empty later cells. The order of the effective
moduli need not be increasing. Independence from the $R$-coordinates
gives
$$
 e_{i,g}=\delta_g e^0_{i,g}/g.
$$
The same rough valuation model, now applied to a zero-residue
first-kill cell, gives $c_{i,g}\le Cc_Re^0_{i,g}/g$. All relevant
effective generators are at most $X$, so their cell probabilities
are their Haar measures. Put $\theta_g=\delta_g/c_R\in[0,1]$.
For nonzero terms,
$$
 c_{i,g}/e_{i,g}\le C/\theta_g,\qquad
 \sum_i c_{i,g}\le A_X w_g\theta_g.
$$
The convex log-sum inequality for $t\log_+t$ permits passage from
these joint $(i,g)$ masses to their $i$-marginals. Concavity of
$\theta\log(C/\theta)$ then yields
$$
 \sum_i c_i\log_+(c_i/e_i)
 \le A_X\sum_gw_g\theta_g\log(C/\theta_g)
 \le A_X\delta\log(C/\delta),
$$
because $\sum_gw_g\theta_g=\sum_g\delta_g/g=\delta$.
Every preparatory congruence is active at an appended hit, since
$q>P$. This checks that the arithmetic cells used are the actual
first kills and completes the proof. $\square$

### Disjoint copies cannot amplify these blocks

Embed a block by $n=a+Rt$, $0\le a<R$, in a parent cylinder of
measure $w=1/R$. A base class $(q,b)$ becomes $(Rq,a+Rb)$,
with activation preserved exactly. The harmonic image mass is at most
$1/R$ times the base mass, while the incremental Haar mass is divided
by $R$. Consequently (5) gives
$$
 h_{\rm copy}^2\le Cw\tau_{\rm copy}.
$$
For any finite collection of copies in pairwise disjoint parent
cylinders, $\sum w\le1$, and hence
$$
 h_{\rm total}^2\le C\Bigl(\sum w\Bigr)
                         \Bigl(\sum\tau_{\rm copy}\Bigr)
 \le C\tau_{\rm total}.
$$
Thus changing preparation systems, sharing primes within a block, or
using arbitrarily many disjoint localized copies does not create a
fixed harmonic deletion with vanishing incremental footprint in this
construction. The argument does not handle overlapping parent regions,
moving centers within a block, or appended moduli below its preparatory
period. No counterexample meeting those remaining requirements was found.

There is also a separate obstruction to assigning divergent entropy to
disjoint selector cylinders with distinct moduli. Croot's corollary gives
$$
 f(x)\le x\exp\left(-(1/6-o(1))\sqrt{\log x\log\log x}\right)
$$
for their maximal number with moduli at most $x$; the hypotheses and
corollary were checked on pages 1--2 of
[Croot, *On Non-intersecting Arithmetic Progressions*](https://arxiv.org/pdf/math/0208236).
For any fixed $A\ge0$, summing over $e^j\le q<e^{j+1}$ therefore gives
$$
 \sum_i\frac{(\log q_i)^A}{q_i}\le C_A,
$$
because each sufficiently late block contributes at most
$O_A((j+1)^A\exp(-c\sqrt{j\log j}))$. In particular their Shannon
energy is uniformly bounded. This theorem concerns disjoint **full
cylinders**, not disjoint first-kill regions inside overlapping cylinders.

Moreover, affine disjoint copies multiply both $c_i$ and $e_i$ by
the parent weight (with an additional factor at most one on $c_i$
from the harmonic cutoff). The weight cancels inside $\log(c_i/e_i)$.
Thus these direct sums yield a weighted average of internal entropies,
not an extra logarithm of the reciprocal parent weight. Neither this
construction nor the selector argument refutes the constant global
first-kill entropy target.

## A prime-power preparation can be reduced to small full footprint

There is a separate reduction for a preparation whose survivor set
$S$ is periodic modulo $L=p^k$. It permits arbitrary appended
residues and overlap, but assumes all appended moduli satisfy $q\ge L$.
Let $U$ be their full union, $B$ their originally activated
union, and $\tau=\mu(S\cap U)$. For every $0<\eta\le1$
there is an appended subfamily with unions $U_\eta,B_\eta$ satisfying
$$
 \mu(U_\eta)\le\tau/\eta,\qquad
 H_{B_\eta}(X)\ge H_{S\cap B}(X)-4\eta H_{\lfloor X\rfloor}.
 \tag{11}
$$
This is a proved reduction, not a small-full-footprint theorem for
arbitrary singleton families.

Separate the $p$-adic coordinate of each full cylinder, writing it
$I_q\times J_q$, and retain the class when
$s_q:=\mu_p(S\mid I_q)\ge\eta$. For fixed other coordinates,
the retained $p$-adic cylinders are nested or disjoint. Their union
is a disjoint union of maximal retained cylinders, each having
$S$-relative measure at least $\eta$. Integration over the other
coordinates proves
$\mu(S\cap U_\eta)\ge\eta\mu(U_\eta)$.

Let $V$ be the union of all $p$-adic cylinders with
$S$-relative measure below $\eta$. Its maximal cylinders are
disjoint, so $\mu(S\cap V)\le\eta$. Moreover
$E=S\cap V$ is $L$-periodic: a cylinder deeper than level
$k$ either lies in $S$, with relative measure one, or misses
$S$ entirely. For $t\ge L$, periodic counting gives
$$
 |E\cap[L,t]|\le\mu(E)(t+L)\le2\eta t.
$$
Every discarded active hit lies in $E$ and is at least $L$.
Partial summation bounds their harmonic mass by
$4\eta H_{\lfloor X\rfloor}$, proving (11).

For appended hits admitting a witnessing modulus with
$q\le n\le Kq$, this gives the explicit bound
$$
 \frac{H_{S\cap B_K}(X)}{H_{\lfloor X\rfloor}}
 \le\min\left(1,\,4\sqrt{H_{\lfloor K\rfloor}\tau}\right).
 \tag{12}
$$
Indeed their retained part has mass at most
$H_{\lfloor K\rfloor}\sum_{q\le X,q\text{ retained}}1/q$.
Distinctness, the exact multiples inequality, and finite union
compression bound this by
$H_{\lfloor K\rfloor}\mu(U_\eta)H_{\lfloor X\rfloor}$.
Add the discarded mass from (11) and optimize
$H_{\lfloor K\rfloor}\tau/\eta+4\eta$; when its optimizer is
larger than one, the trivial bound suffices. If $\tau=0$, take
$\eta\downarrow0$.

Thus overlapping binary selector fibers cannot amplify the earlier
energy gadgets through bounded-quotient endpoints. For unrestricted
quotients, (11) reduces such an attempted construction to one with
small *full* footprint; it does not exclude that remaining possibility.
The argument uses laminarity of one prime's cylinders and supplies no
corresponding uniform theorem for a general multi-prime preparation.

## Independent prime-support blocks

The [bounded-prime-overlap theorem](bounded_prime_overlap_blocks.md)
extends the density conclusion below to blocks such that each prime
occurs in at most a fixed number of block supports. Its proof uses
product-space Hölder and the exact whole-block harmonic bound; it does
not assert the first-kill entropy estimate (10) for overlapping blocks.

**Theorem.** Partition a strictly increasing singleton modulus family
into blocks $D_j$ whose prime supports are pairwise disjoint. Within
block $j$, use one integer center
$$
 0\le\alpha_j<\min D_j.
$$
The blocks and their prime ranks may be unbounded, and the centers need
not remain bounded. The delayed survivor set has logarithmic density
equal to its finite-prefix candidate.

If that candidate is $\delta=0$, finite prefixes already give natural
density zero. Suppose $\delta>0$. For a modulus $q_i\in D_j$, let
$e_i^{(j)}$ denote its first-kill Haar mass among earlier moduli of its
own block only. Independence of prime supports gives
$$
 e_i=\delta_{i-}^{\rm other}\,e_i^{(j)}
       \ge\delta e_i^{(j)}.
$$
The substitution $m=n-\alpha_j$ maps each actual first kill into the
zero-residue version of that within-block cell. The same argument as
(3) yields $c_i(X)\le C e_i^{(j)}$. Therefore
$$
 \sum_i c_i(X)\log_+\frac{c_i(X)}{e_i}
 \le\log(C/\delta)\sum_i c_i(X)\le\log(C/\delta).
 \tag{10}
$$
This is uniform in $X$ for the given infinite system.

For a prefix of length $k$, put
$\tau_k=\sum_{i>k}e_i\to0$ and
$\rho_k(X)=\sum_{i>k}c_i(X)$. Log-sum and (4) give
$$
 \rho_k(X)\log\frac{\rho_k(X)}{\tau_k}\le\log(C/\delta).
$$
It follows that $\sup_X\rho_k(X)\to0$. This is precisely finite-periodic
approximation in upper logarithmic density. Finite prefixes supply the
claimed density. No natural-density assertion is made when $\delta>0$.

The proof respects activation: normalized positive centers ensure
$n-\alpha_j\ge q_i$, not an omitted root below its modulus. Disjoint
prime supports supply independence only between blocks; no coprimality
or bounded rank is assumed inside a block.
