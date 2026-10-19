---
name: research/erdos_25/finite_sharp_counterexamples
desc: Sharp finite harmonic and Dirichlet counterexamples, a positive two-class boundary, and obstructions to recentering harmonic constants.
tags: [obstructions, sieve, finite-counterexamples]
sources: []
created: 2026-09-22T01:15:00Z
updated: 2026-10-14T00:26:52Z
---


# research/erdos_25/finite_sharp_counterexamples

***

## Scope and status

The two proposed inequalities
$$
 H_B(X)\le\beta H_{\lfloor X\rfloor},\qquad
 D_B(s)\le\beta\zeta(s)\quad(s>1)
 \tag{1}
$$
are false, even for finite families of distinct **prime** moduli.
Here $B$ is the delayed excluded union, $\beta$ is its full periodic
density, and $D_B(s)=\sum_{n\in B}n^{-s}$.

The existence proof below invokes the finite-complexity prime linear-forms
theorem of Green--Tao--Ziegler. It produces finite counterexamples by a
negative-expectation argument, not an extracted numerical certificate.
It does **not** refute Problem 25: each resulting family is finite, and
prime-modulus infinite families have natural density by the established
pairwise-coprime case. Nor does it refute a uniform sublogarithmic
*additive error* in the harmonic comparison.

### External theorem used

We use the prime asymptotic for any fixed system of integer linear forms
with pairwise nonproportional linear parts, on bounded convex dilates
where all forms are positive. Fixed smooth weights on such regions are
permitted by partial summation. The asymptotic is the real volume times
the product of local densities, with the appropriate prime logarithms.

The relevant full-source passages were checked during this work:
[Green--Tao, *Linear equations in primes*](https://annals.math.princeton.edu/wp-content/uploads/annals-v171-n3-p08-p.pdf),
Lemma 1.6, printed p. 1761, and Main Theorem, printed p. 1763;
[Green--Tao--Ziegler, *An inverse theorem for the Gowers
$U^{s+1}[N]$-norm*](https://annals.math.princeton.edu/wp-content/uploads/annals-v176-n2-p11-p.pdf),
Theorem 1.3 and the following application paragraph, printed p. 1235.
The latter completes the hypotheses needed for the prime asymptotic.
All coefficients below, however large, are fixed before the scale tends
to infinity. No uniformity in the number of forms is invoked.

## Admissible sets with large harmonic weight

A finite set $S\subset\mathbb N$ is admissible if it omits some residue
modulo every prime. Such sets have unbounded harmonic sums.

Here is the already established construction in a form sufficient here.
For primes $p\le Y$, independently choose a forbidden residue, uniformly
over all residues for $p=2,3$, and uniformly in
$\{\lceil\sqrt p\rceil,\ldots,p-1\}$ for $p\ge5$. Let $S$ be the
integers at most $Y$ avoiding them. It is admissible: primes above $Y$
cannot be fully represented by a set of size at most $Y$.
For fixed $t$, primes above $t^2$ cannot remove it; the other primes have
hitting probability at most $1/(p-\lceil\sqrt p\rceil)$.
Comparison with $\prod_{p\le t^2}(1-1/p)$ gives
$\Pr(t\in S)\gg1/\log(t+2)$, because the product of the correction
ratios is positive. Hence $\mathbb E H_S(Y)\gg\log\log Y$.

It follows that
$$
 L:=\sum_{t\in S}\log(1+1/t)
$$
can be made arbitrarily large, since its difference from
$\sum_{t\in S}1/t$ is bounded absolutely. Fix such an $S$, and write
$k=|S|$, $T=\max S$, $\nu_\ell=|S\bmod\ell|$, and
$$
 c=\prod_\ell\frac{1-\nu_\ell/\ell}{(1-1/\ell)^k}>0.
$$
The product converges: beyond all differences between members of $S$,
$\nu_\ell=k$ and each factor is $1+O_S(\ell^{-2})$.

## Two prime moment calculations

For a prime $q$, let
$$
 A(q)=\#\{0\le a<q:\ a+tq\text{ is prime for all }t\in S\},
 \qquad b_q=\frac{A(q)(\log q)^k}{cq}.
$$
The prime linear-forms theorem gives, for $j=1,2$,
$$
 \frac1{\pi(2R)-\pi(R)}
 \sum_{\substack{R<q\le2R\\q\ {
m prime}}}b_q^j\longrightarrow1.
 \tag{2}
$$
For $j=1$ the forms are $q,a+tq$; for $j=2$ they are
$q,a+tq,b+tq$, retaining the common $q$ only once.
The domains are $R<q\le2R$, $0\le a,b<q$.
Conditional on $q\not\equiv0\pmod\ell$, a shift variable has exactly
$\ell-\nu_\ell$ allowable residues. The singular series are therefore
$c$ and $c^2$. Weighting by $q^{-j}(\log q)^{jk}$ cancels the
$q^j$ shift volume and the corresponding prime logarithms, yielding (2).
All listed forms are pairwise nonproportional. The diagonals in the
second moment have lower dimension and do not affect the asymptotic.
In particular the prime average of $(b_q-1)^2$ tends to zero.

Call $q$ good if $1/2\le b_q\le2$. Bad primes have relative density
$o(1)$ on every growing dyadic interval, and their average $b_q$-mass
is $o(1)$, by Cauchy--Schwarz and (2).

For a target prime $p$, define
$$
 J(p)=\sum_{t\in S}
 \sum_{\substack{p/(t+1)<q\le p/t\\q\ {
m prime}}}
 \frac{(\log q)^k}{cq}
 \mathbf1_{\{p+(s-t)q\ {
m prime}\ \forall s\in S\setminus\{t\}\}}.
$$
The analogous first and second moment asymptotics are
$$
 \mathbb E_{\substack{R<p\le2R\\p\ {
m prime}}}J(p)\to L,
 \qquad
 \mathbb E_{\substack{R<p\le2R\\p\ {
m prime}}}J(p)^2\to L^2.
 \tag{3}
$$
For a first-moment summand the forms are
$p,q,p+(s-t)q$ for $s\ne t$. For a second-moment summand use a common
$p$ and the two corresponding collections with independent $q_1,q_2$.
These forms are again pairwise nonproportional. Conditional on
$p\not\equiv0\pmod\ell$, the forbidden residues of $q$ consist of zero
and one value for each nonzero residue represented by $S-t$; their
number is $\nu_\ell$. Thus the singular series are again $c,c^2$.
The weighted real integral for the $t$-summand is
$$
 \int_{p/(t+1)}^{p/t}\frac{dq}{q}=\log(1+1/t).
$$
The second-moment integral is the product of the two such integrals.
On these convex wedges all forms are positive and comparable with $R$,
with constants depending only on the fixed $S$. This proves (3).

Let $J_{\rm good}$ omit the bad $q$. Then $J_{\rm good}(p)\to L$
in prime-average $L^1$. To justify this removal, exchange the incidence
sums over $p,q$. A fixed good shift for $q$ supplies at most $k$ target
primes, so
$$
 \sum_{\substack{R<p\le2R\\p\ {
m prime}}}(J(p)-J_{\rm good}(p))
 \le k\sum_{\substack{R/(T+1)<q\le2R\\q\ {
m bad}}}b_q
 =o(R/\log R).
 \tag{4}
$$
The $q$-range is covered by finitely many dyadic intervals because $T$
is fixed. This also supplies the uniformity needed when dyadic intervals
are later summed over $N\le p\le N^C$.

## Random covering of the old prime survivors

Fix $1<C<2$, $0<\varepsilon<1$, and $X=N^C$. First install the zero
classes at every prime at most $N$. Independently select each good prime
$q\in(N,X]$ with probability $\varepsilon$. For a selected $q$, choose
its residue uniformly among the $A(q)$ good shifts.

This is a finite singleton system with distinct prime moduli. For a
target prime $p>(T+1)N$, every $q$ appearing in $J(p)$ belongs to $(N,X]$.
For given $p,q$, at most one $t$ gives $0\le p-tq<q$. Whenever this shift
is good, its selection probability is $\varepsilon/A(q)$. Moreover
$$
 \frac1{A(q)}\ge\frac{(\log q)^k}{2cq}
 \qquad(q\text{ good}).
$$
Independence over $q$ therefore bounds the probability that $p$ survives by
$\exp(-\varepsilon J_{\rm good}(p)/2)$.
All hits used here are active: $p=a+tq$ with $t\ge1$ and $0\le a<q$
implies $p\ge q$.

Since the exponential on the nonnegative half-line is Lipschitz, (3)--(4)
give mean survival at most $e^{-\varepsilon L/2}+o(1)$ on each growing
dyadic prime interval. Weighted summation gives
$$
 \mathbb E H_A(X)\le1+e^{-\varepsilon L/2}\log C+o(1).
 \tag{5}
$$
Indeed the old survivors below $X<N^2$ are exactly $1$ and primes above
$N$. The boundary primes up to $(T+1)N$ have harmonic mass $o(1)$.
For each dyadic interval the weighted error is $o(1/\log R)$ uniformly
as its lower endpoint tends to infinity; summing from $N$ to $N^C$
keeps the total error $o(1)$.

Let $\delta$ be the final periodic survivor density. It depends only on
which prime moduli were selected, not on their residues. Exactly,
$$
 \mathbb E\delta=
 \prod_{p\le N}(1-1/p)
 \prod_{\substack{N<q\le N^C\\q\ {
m good}}}(1-\varepsilon/q).
$$
The omitted bad primes have reciprocal sum $o(1)$ on this range by (2).
Mertens' product asymptotic and prime reciprocal summation imply
$$
 \mathbb E[\delta H_{\lfloor X\rfloor}]
 \longrightarrow e^{-\gamma}C^{1-\varepsilon}.
 \tag{6}
$$

Choose $e^\gamma<C<2$ and
$0<\varepsilon<1-\gamma/\log C$. The limit in (6) is greater than one.
Then choose the fixed admissible $S$ with $L$ so large that
$$
 1+e^{-\varepsilon L/2}\log C<e^{-\gamma}C^{1-\varepsilon}.
$$
For all sufficiently large $N$, (5)--(6) make the expectation of
$H_A(X)-\delta H_{\lfloor X\rfloor}$ negative. Some finite realization
therefore refutes the harmonic inequality in (1).

## The Dirichlet comparison also fails near $s=1$

Fix $t>0$ and let $s_N=1+t/\log N$. For the old zero sieve,
$$
 D_{A_{\rm old}}(s_N)=\prod_{p>N}(1-p^{-s_N})^{-1}
 \longrightarrow e^{E_1(t)}
 =\frac{e^{-\gamma}}t e^{J_0(t)},
$$
where
$$
 E_1(t)=\int_1^\infty e^{-tv}\frac{dv}{v},\qquad
 J_0(t)=\int_0^1(1-e^{-tv})\frac{dv}{v}=t+O(t^2).
$$
The Euler-product limit follows by taking logarithms: the prime-power
terms of degree at least two are $o(1)$, and partial summation using the
prime number theorem gives the displayed integral for the degree-one
terms. Also $E_1(t)=-\gamma-\log t+J_0(t)$.

The same random covering removes expected Dirichlet mass at least
$$
 (1-e^{-\varepsilon L/2})\int_1^C e^{-tv}\frac{dv}{v}+o(1)
$$
from the primes in $(N,N^C]$. Any additional deletions only improve this
upper bound on $D_A(s_N)$. On the other hand,
$$
 \mathbb E[\delta\zeta(s_N)]\longrightarrow
 \frac{e^{-\gamma}}t C^{-\varepsilon}.
$$
Thus the limiting expected excess is at most
$$
 \frac{e^{-\gamma}}t\bigl(e^{J_0(t)}-C^{-\varepsilon}\bigr)
 -(1-e^{-\varepsilon L/2})\int_1^C e^{-tv}\frac{dv}{v}.
 \tag{7}
$$
Choose $C<2$ with $\log C>e^{-\gamma}$, and $a>0$ sufficiently small
that $e^{-\gamma}(1+a\log C)<\log C$. Set $\varepsilon=at$.
With perfect covering, expression (7) tends as $t\downarrow0$ to
$e^{-\gamma}(1+a\log C)-\log C<0$.
First fix sufficiently small $t$, then choose fixed admissible $S$ so
that its finite $L$ makes (7) negative, and only then let $N\to\infty$.
Negative expectation supplies finite realizations with
$$
 D_B(s_N)>(1-\delta)\zeta(s_N),\qquad s_N\downarrow1.
$$
There is no interchange of limits in $S,t,N$ here.

## What remains

The later [prime-template amplification](prime_additive_excess.md)
strengthens the finite harmonic conclusion to **unbounded** additive
excess with prime moduli. It still gives no fixed positive normalized
excess and is not an infinite counterexample.

These constructions defeat the exact finite comparisons proposed as sufficient
routes. The excess obtained is bounded on the
harmonic scale used in the earlier construction above, not a positive
multiple of $\log X$.
No iteration preserving a positive limiting periodic survivor density
and producing logarithmic oscillation has been proved. The uniform
sublogarithmic-error target remains open.

## Two classes satisfy the sharp comparisons

Section 5 of the [[research/erdos_25/independent/harmonic_capacity_and_narrow_windows|fourth independent record]]
correctly proves the Dirichlet comparison for two classes. Its loss
argument also proves the harmonic comparison, despite the counterexamples
above for larger families.

**Proposition.** For a delayed union $B$ of at most two singleton
classes at distinct moduli, of full periodic density $\beta$,
$$
 H_B(X)\le\beta H_{\lfloor X\rfloor},\qquad
 D_B(s)\le\beta\zeta(s)\quad(s>1).
$$
If the two classes are compatible, a stronger comparison holds: their
delayed union has no greater weight than the all-zero union for every
nonnegative, nonincreasing, summable weight $w:\mathbb N\to\mathbb R$.
Finitely supported decreasing weights are included.

**Proof.** Write the distinct moduli as $m<n$, with normalized
residues $a_m,a_n$. Put
$$
 W_q(a)=\sum_{t\ge1}w(qt+a),\qquad
 \ell_w(q,a)=W_q(0)-W_q(a)\ge0.
$$
For compatible classes, let $L=\operatorname{lcm}(m,n)$ and let
$b\in[0,L)$ be their common CRT representative. If $b=0$, their
delayed intersection has weight $W_L(0)$. If $b\ge n$, its weight is
$\sum_{t\ge0}w(b+tL)\ge W_L(0)$, because $b<L$.
In either case inclusion--exclusion and $W_q(a)\le W_q(0)$
give the claimed comparison with the zero union.

If $0<b<n$, then $b=a_n$, and the delayed intersection has
weight $W_L(b)=W_L(0)-\ell_w(L,b)$. Since $n\mid L$,
$$
 \ell_w(L,b)
 =\sum_{k\ge1}\bigl(w(Lk)-w(Lk+b)\bigr)
 \le\sum_{t\ge1}\bigl(w(nt)-w(nt+b)\bigr)
 =\ell_w(n,b).
$$
The left side is a sub-sum of the nonnegative terms on the right.
Thus the intersection loss is absorbed by the $n$-class loss,
and inclusion--exclusion again proves weighted comparison with the
zero union. No convexity of $w$ is needed.

Compatible classes have the same union density
$\beta=1/m+1/n-1/L$ as the zero classes. Apply the
[multiples inequalities](basic_reductions.md) with
$w(j)=j^{-1}\mathbf1_{j\le X}$ or $w(j)=j^{-s}$ to obtain
the two asserted bounds. If the classes are incompatible, their
density is $1/m+1/n$, and the separate single-class bounds suffice.
One class is handled by the same single-class comparison. $\square$

The density-normalized conclusion does not hold for arbitrary
decreasing weights. For instance, the zero classes
modulo $2,3$ cover three integers up to $4$, exceeding
$(2/3)\cdot4$. Also, the already checked
[$(2,3,5)$ example](unresolved_estimates.md#further-checks-after-renewed-work)
shows that comparison with the zero union fails for three compatible
classes. The proposition therefore does not repair the false
many-class sharp bounds.

## Fixed-template affine amplification fails

Here are precise additional limitations on amplifying a finite anomaly.
Let $B$ be any fixed finite delayed union of full density $\beta>0$, and
put
$$
 M=\max\left(0,\sup_{X\ge1}
           (H_B(X)-\beta H_{\lfloor X\rfloor})\right)<\infty.
$$
Finiteness follows from eventual periodicity. For integers $m\ge1$ and
$0\le b<m$, replacing $(q,a)$ by $(mq,ma+b)$ gives exactly the affine
image $mB+b$, with activation preserved and density $\beta/m$.
For $N=\lfloor X\rfloor\ge m$,
$$
 H_{mB+b}(X)\le m^{-1}H_B(\lfloor N/m\rfloor),\qquad
 H_N-H_{\lfloor N/m\rfloor}\ge\log(m/2).
$$
Consequently
$$
 H_{mB+b}(X)-(\beta/m)H_N
 \le\frac{M-\beta\log(m/2)}m.
 \tag{8}
$$
For $X<m$ there are no image points. Thus $m\ge2e^{M/\beta}$ eliminates
every individual positive harmonic anomaly of this fixed template.

Partial summation also gives
$$
 D_B(s)-\beta\zeta(s)
 =(s-1)\int_1^\infty
   (H_B(x)-\beta H_{\lfloor x\rfloor})x^{-s}\,dx\le M.
$$
Since $D_{mB+b}(s)\le m^{-s}D_B(s)$ and
$\zeta(s)\ge1/(s-1)$,
$$
 \frac{D_{mB+b}(s)}{(\beta/m)\zeta(s)}
 \le e^{-(s-1)\log m}\bigl(1+(M/\beta)(s-1)\bigr).
$$
Hence $m\ge e^{M/\beta}$ eliminates every Dirichlet anomaly,
simultaneously for all $s>1$. Choosing $s$ closer to one does not allow
arbitrarily large dilations of one fixed anomalous system.

Finally, literal iteration of affine maps $t\mapsto qt+a$ from a finite
alphabet produces only moduli supported on the alphabet's finite prime
set $P$. After enforcing singleton distinctness, their reciprocal sum is
at most $\prod_{p\in P}(1-1/p)^{-1}<\infty$, so natural density exists.
Adding fresh prime tags to a bounded-branching fixed-alphabet tree does
not repair this: if child moduli are $M_{vi}=M_vr_vq_i$ and the tags
$r_v$ escape every bounded set, then with $W=\sum_i1/q_i$ the reciprocal
mass at consecutive sufficiently deep levels contracts by
$W/r_v\le1/2$. Its total reciprocal sum again converges.

These facts concern fixed templates and direct compositions. They do
not rule out increasingly complex conditioned constructions.

## An elementary recentering obstruction for harmonic constants

Section 6 of the [[research/erdos_25/independent/bounded_quotient_blocks_and_recentering|second independent record]]
supplies a correct, small example strengthening the already recorded
[finite-prefix recentering failure](unresolved_estimates.md#further-checks-after-renewed-work).
It also gives a simpler proof of failure of Dirichlet compression to
the zero-residue system, without a prime-distribution theorem.

Let $B_0$ use the zero residues at $2,3,35$, and let $B_2$ instead
use residues $(0,0,2)$, always with activation at the modulus. The
latter system has common phase $72\pmod{210}$. Pairwise coprimality
gives both full unions density
$$
 \beta=1-\frac12\frac23\frac{34}{35}=\frac{71}{105}.
$$
After removing multiples of $2$ and $3$, the additional deletions are
exactly
$$
 E_0=\{210k+35,210k+175:k\ge0\},\qquad
 E_2=\{210k+37,210k+107:k\ge0\}.
$$
The positive root $2$ of the translated class is inactive there, but
already removed by the modulus $2$; all listed points are active.
Consequently
$$
 \lim_{X\to\infty}\bigl(H_{B_2}(X)-H_{B_0}(X)\bigr)
 =\Lambda:=\sum_{k\ge0}
 \left(\frac1{210k+37}+\frac1{210k+107}
       -\frac1{210k+35}-\frac1{210k+175}\right)>0.
 \tag{9}
$$
For $x=210k$, a summand equals
$$
 \frac{68}{(x+107)(x+175)}-
 \frac2{(x+35)(x+37)}.
$$
Its numerator over the common positive denominator is
$2(33x^2+2166x+25305)>0$. Each summand is $O((k+1)^{-2})$,
proving convergence; an incomplete last period has weight $O(1/X)$.
Thus the asymptotic harmonic constant is larger for $B_2$.

The same pairing gives
$$
 \lim_{s\downarrow1}\bigl(D_{B_2}(s)-D_{B_0}(s)\bigr)=\Lambda>0.
 \tag{10}
$$
Indeed, for $1\le s\le2$, the mean value theorem bounds the paired
differences by a summable constant multiple of $(k+1)^{-2}$.
Dominated convergence applies. Since both densities equal $\beta$,
this disproves additive and ratio comparisons to the zero-residue
system for all sufficiently small positive $s-1$.

It does **not** violate the raw comparison $D_{B_2}(s)\le\beta\zeta(s)$
near $1$. To check this without numerical constants, put
$$
 P(s)=1-(1-2^{-s})(1-3^{-s})(1-35^{-s}).
$$
Then $D_{B_0}(s)=\zeta(s)P(s)$ and
$$
 \lim_{s\downarrow1}(D_{B_0}(s)-\beta\zeta(s))
 =P'(1)
 =-\frac{34}{105}
   \left(\log2+\frac{\log3}{2}+\frac{\log35}{34}\right).
$$
Also $0<\Lambda<1/107$: discard the negative pair in each summand
of (9), and bound the remaining differences by the telescoping
series with offsets $107$ and $317$. Since $\log2\ge1/2$,
$P'(1)+\Lambda<-17/105+1/107<0$.
The raw Dirichlet inequality is refuted by the separate construction
above, not by this three-modulus example. The changing-family
violations there do not by themselves produce a fixed family whose
asymptotic harmonic constant exceeds $\beta\gamma$.

### An all-prime three-modulus variant

Section 7.2 of the [[research/erdos_25/independent/profinite_shifts_and_long_windows|third independent record]]
gives a smaller recentering example in which all three moduli are prime.
Use $(2,3,23)$, with residues $(0,0,0)$ or $(0,0,2)$. Both full unions
have density $47/69$, and the second has common phase $48$.
Their additional active points outside the first two classes are
$$
 \{138j+23,138j+115:j\ge0\},\qquad
 \{138j+25,138j+71:j\ge0\},
$$
respectively. As $s\downarrow1$, their paired Dirichlet-series difference
has limit
$$
\Lambda_{23}=\sum_{j\ge0}
 \left[\frac{44}{(138j+71)(138j+115)}
             -\frac2{(138j+23)(138j+25)}\right]>0.
$$
For $x\ge0$, positivity follows from
$$
 22(x+23)(x+25)-(x+71)(x+115)
 =21x^2+870x+4485>0.
$$
The summands are $O((j+1)^{-2})$. The same paired mean-value bound
holds uniformly for powers $n^{-s}$, $1\le s\le2$, so the difference
remains positive for $s>1$ sufficiently close to $1$. This verifies the
input's failure of weighted recentering, now with prime moduli only.

As with the $35$-example, it does not violate the raw Dirichlet
inequality (1) for $s>1$ sufficiently close to $1$.
Dropping the negative pair and telescoping with offsets $71$ and $209$
gives $0<\Lambda_{23}<1/71$. With
$P_{23}(s)=1-(1-2^{-s})(1-3^{-s})(1-23^{-s})$,
$$
 P_{23}'(1)
 =-\frac{22}{69}\left(\log2+\frac{\log3}{2}
                                    +\frac{\log23}{22}\right).
$$
Thus $P_{23}'(1)+\Lambda_{23}<-11/69+1/71<0$.
The independent note's separate suggestion that the raw inequality
could still be true is superseded by the counterexamples above.

### The stopped-coordinate model does not dominate the actual trace

Section 8.4 of the independent input correctly proves the auxiliary
inequality
$$
 P_{\mathcal C}(s):=
 \sum_{\substack{\varnothing\ne J\subseteq\mathcal C\\
                  J\text{ compatible}}}
 (-1)^{|J|+1}\operatorname{lcm}(q_j:j\in J)^{-s}
 \le P_{\mathcal C}(1)=\mu\left(\bigcup_{C\in\mathcal C}C\right).
 \tag{11}
$$
Here $\mathcal C$ is a finite congruence family. Independently at each
prime choose a Haar digit sequence and an independent retained depth
$L_p$, with $\Pr(L_p\ge e)=p^{-e(s-1)}$. A prime-power condition is
met only if its digits match and its entire required depth is retained.
An intersection has probability zero if incompatible, and otherwise
has probability $\operatorname{lcm}(q_j:j\in J)^{-s}$. Inclusion--
exclusion gives $P_{\mathcal C}(s)$. Removing the depth restrictions
gives (11); coupling the depths also makes it nonincreasing in $s$.

The missing domination
$D_B(s)\le\zeta(s)P_{\mathcal C}(s)$ is false. For the coherent
three-modulus system above, all intersections are compatible, so
$P_{\mathcal C}(s)=P(s)$, while (10) gives
$D_{B_2}(s)>\zeta(s)P(s)$ near $1$.
Thus this valid probabilistic model cannot replace the activated
integer trace. Neither example is an infinite density counterexample.
