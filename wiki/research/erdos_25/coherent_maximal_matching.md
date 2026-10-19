---
name: research/erdos_25/coherent_maximal_matching
desc: Maximal matching multiples give a finite first-kill trace bound and a new logarithmic-density criterion in terms of the Haar first-kill tail.
tags: [coherent-residues, harmonic-measure, partial-results]
sources: []
created: 2026-09-22T13:20:00Z
updated: 2026-09-24T22:13:01Z
---


# research/erdos_25/coherent_maximal_matching

***

## A simultaneous finite trace bound

Let $D$ be a finite set of distinct moduli with common profinite
center $\alpha$. Write $E_q$ for the actual delayed first-kill
set and $e_q$ for its Haar first-kill mass. If $J\subseteq D$
and $\tau=\sum_{q\in J}e_q$, then, uniformly in all these data,
$$
 H_{\bigcup_{q\in J}E_q}(X)
 \ll \tau\log(2X)\log(2+\log(2X)).
 \tag{1}
$$
The bound uses one common center simultaneously. It does not sum
separate phase maxima. Its extra $\log\log X$ factor prevents it
from establishing unrestricted coherent tail tightness.
The positive kernel in (2) below already has order
$\log X\log\log X$ for $D=J=\{1\}$. Thus bounding that
kernel using only $G_J$ and its Haar mass cannot remove the loss;
one would have to retain more of the numerical maximality condition.

### Maximal matching multiples and a rough quotient

Choose an integer $b$ realizing $\alpha$ modulo
$\operatorname{lcm}(1,\ldots,\lfloor X\rfloor)$. For each
counted hit $n\le X$, with first modulus $q$, take the largest
integer $m\le n$ satisfying
$$
 q\mid m,\qquad m\mid n-b.
$$
Such an $m$ exists, since $q$ itself is eligible. In the
zero-residue system on $D$, its first dividing generator is
exactly $q$: an earlier generator dividing $m$ would cover
$n$, and would be active there. Consequently
$$
 m\in G_J:=\{m\ge1:\operatorname{first}_D(m)\in J\}.
$$
Maximality also implies that $(n-b)/m$ has no prime divisor
at most $n/m$, since otherwise multiplying $m$ by that prime
would give a larger admissible choice. If $m\le n/2$, this
also excludes the quotient zero. Quotients may be negative; the
upper sieve below applies on arbitrary translated intervals.

On a dyadic interval $(H,2H]$, fix $m$ and put $t=H/m$.
For $t$ larger than a fixed absolute constant, the possible
quotients lie in an interval of length $t$ and avoid every prime
at most $t$. The uniform dimension-one upper sieve established
in [the power-cutoff notes](local_colored_power_cutoff.md#an-elementary-upper-sieve-of-fixed-dimension),
applied at $y=t^{1/B}$ for a sufficiently large fixed $B$,
bounds their number by
$$
 O\bigl(t/\log(2+t)\bigr).
$$
For bounded $t$, use $n\ge m$: the delayed progression
$n\equiv b\pmod m$ has at most $2H/m=2t$ points below
$2H$. Since $m\le2H$, here $t\ge1/2$, and the same
bound holds after enlarging its absolute constant.

Weighting by $1/H$ and summing over possible $m$ therefore gives
$$
 H_{E_J\cap(H,2H]}(X)
 \ll\sum_{\substack{m\le\min(X,2H)\\m\in G_J}}
          \frac1{m\log(2+H/m)}.
$$
For each fixed $m$, summation over dyadic $H$ is a harmonic
sum in the dyadic index. Thus
$$
 H_{E_J}(X)
 \ll \tau+
 \sum_{\substack{m\le X\\m\in G_J}}
       \frac{\log(2+\log(2X/m))}{m}.
 \tag{2}
$$
The possible point $n=1$ costs at most $\tau$, since a hit
there requires the modulus 1 and its full first cell has mass 1.

### Haar control of the matching multiples

The geometric valuation law, as used in
[coherent transport](coherent_annuli_and_shadows.md#simultaneous-transport-across-a-bounded-divisor-gap),
gives
$$
 T(Y):=\sum_{\substack{m\le Y\\m\in G_J}}\frac1m
 \le \tau Z_Y\ll\tau\log(2Y),\qquad
 Z_Y=\prod_{p\le Y}(1-1/p)^{-1}.
 \tag{3}
$$
Only generators at most $Y$ matter in this calculation; their
first-cell masses are unchanged by discarding later generators,
and their selected masses sum to at most $\tau$.

For $K_X(t)=\log(2+\log(2X/t))$, partial summation yields
$$
 \sum_{\substack{m\le X\\m\in G_J}}\frac{K_X(m)}m
 =K_X(X)T(X)+
   \int_1^X\frac{T(t)}{t(2+\log(2X/t))}\,dt.
$$
Use (3) and $\log(2t)\le\log(2X)$ in the integral to obtain
(1). In an infinite coherent system, restricting to moduli $q\le X$
leaves the active first kills and all their first-cell masses unchanged.
Thus (1) applies to any selected tail of the infinite system as well.

## Exact replacement exclusions

There is a stronger, checked formulation of numerical maximality, but
no summation of it removing the logarithmic loss has been obtained.
For the choice of $m$ used above, write
$m=qa$, $t=n/m$, and $h=(n-b)/m$. Its maximality is
equivalent to
$$
 k\nmid h\quad\text{whenever}\quad
 k\ge2,\quad \exists d\mid a:\ (d,k)=1,
                         \quad d<k\le td.
 \tag{7}
$$
Indeed, every competing multiple of $q$ is uniquely of the form
$r=mk/d$, with $d\mid a$ and $(d,k)=1$, after reducing
$r/m$. It divides $n-b=mh$ precisely when $k\mid h$;
the two size conditions say $m<r\le n$.

For an ordered tail there is a still stronger choice. Let
$D_0=D\cap[1,Y]$ and
$G=M(D)\setminus M(D_0)$. At a tail hit choose the largest
$m\le n$ dividing $n-b$ and belonging to $M(D)$, without
requiring divisibility by the original first generator. Then $m\in G$:
an old generator dividing $m$ would cover $n$. This retains
the tail Haar mass $\mu(G)$, although the particular first label
can change. Its exact quotient exclusion family is
$$
 \mathcal K(m,n)=
 \left\{\frac r{(r,m)}:m<r\le n,\ r\in M(D)\right\}.
 \tag{8}
$$
The equivalence follows from
$r\mid mh\iff r/(r,m)\mid h$. This includes replacements by
incomparable generators.

On $H<n\le2H$, fix $m\le H$ and retain only
$\mathcal K(m,H)$. It already contains every integer
$2\le k\le H/m$, by taking $r=mk$. Thus every *additional*
minimal generator of its multiples union exceeds $H/m$ and has no
prime factor at most $H/m$. The quotient interval has length
$H/m$. The new constraints therefore occur beyond that interval's
length; a conventional per-quotient upper sieve using primes below
$(H/m)^{1/B}$ sees no improvement. For $m>H$ the quotient
interval has bounded length and there are no such retained competitors.
These observations do not rule out a simultaneous divisor-switching
argument. No such arithmetic estimate was proved.

## A Haar-tail criterion for original activation

For an infinite coherent family suppose that
$$
 \tau(Y):=\sum_{q>Y}e_q
        =o\!\left(\frac1{\log\log Y}\right).
 \tag{4}
$$
Then its delayed union $B$ has logarithmic density
$\beta=\sum_qe_q$, with finite-periodic approximation in upper
logarithmic density. Its survivor set has logarithmic density
$1-\beta$. No natural-density conclusion is asserted.

Indeed the already-proved power-cutoff theorem gives natural density
$\beta$ for
$$
 B_*:=\{n\in B:q(n)\le\sqrt n\}.
$$
Fix $c>0$. If $X^c<n\le X$ lies in $B\setminus B_*$,
then its first modulus exceeds $X^{c/2}$. By (1), these points
have harmonic mass at most
$$
 O\bigl(\tau(X^{c/2})\log X\log\log X\bigr)=o(\log X).
$$
The remaining points $n\le X^c$ have harmonic mass at most
$c\log X+O(1)$. Divide by $\log X$, take the upper limit,
and let $c\downarrow0$. This proves that $B\setminus B_*$
has logarithmic density zero. Subtracting the asymptotic for any
finite prefix then proves the asserted finite-periodic approximation.

A convenient sufficient condition for (4) is
$$
 \sum_q e_q\log\log(3q)<\infty,
 \tag{5}
$$
because $\tau(Y)\log\log(3Y)$ is bounded by the tail of
this convergent series. Neither (4) nor (5) has been proved for an
arbitrary coherent system. The criterion does not concern arbitrary
incompatible residues, and does not resolve Problem 25.

## Final status of the maximality approach

The continuation tried to retain the numerical maximality of $m$
instead of using only its rough-cofactor consequence. Numerical
maximality also forbids larger matching multiples obtained by replacing
factors, not just by adjoining a prime. No simultaneous estimate for
these additional exclusions was obtained. Thus the logarithmic loss
in (1) has not been removed. The example following (1) rules out
removing it from the positive kernel alone; it does not rule out a
different argument using maximality more fully.

One sufficient estimate considered, but **not proved**, was
$$
 H_B(X)\le\beta_D H_{\lfloor X\rfloor}
          +C\left(1+\sum_{\substack{q\in D\\q\le X}}e_q\log q\right)
 \tag{6}
$$
uniformly over finite coherent families and their common centers,
with an absolute $C$. Here $\beta_D$ is their full Haar union
measure. This is only a possible coherent estimate, not an assertion
for arbitrary residues; the general energy comparison has already
been [refuted](energy_counterexample.md).

For clarity, its sufficiency in the coherent case has no further
analytic gap. For a fixed infinite family, $\sum_q e_q\le1$
implies
$$
 \frac1{\log X}\sum_{q\le X}e_q\log q\longrightarrow0.
$$
For a fixed $M$, the terms $q\le M$ tend to zero after
normalization, and the remaining normalized sum is at most
$\sum_{q>M}e_q$, which tends to zero with $M$.
Apply (6) to the finite truncation $q\le X$, whose active union
agrees with the infinite union below $X$; its Haar mass is at
most the limiting $\beta$. Finite prefixes give the reverse
lower logarithmic bound. Hence (6), if established, would give
logarithmic density $\beta$. No proof of (6), nor a coherent
counterexample to the density statement, was obtained.
