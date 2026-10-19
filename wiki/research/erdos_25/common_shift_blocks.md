---
name: research/erdos_25/common_shift_blocks
desc: Uniform interval and harmonic bounds for coherently shifted dyadic blocks.
tags: [coherent-residues, obstructions, partial-results]
sources: []
created: 2026-09-22T02:34:17Z
updated: 2026-09-24T22:13:01Z
---


# research/erdos_25/common_shift_blocks

***

Checking Section 5 of the [[research/erdos_25/independent/harmonic_bounds_and_common_shifts|independent input]]
gives the following new obstruction. The proof below makes its local
estimate finite and also controls all quotient ranges in a single block.
It does not settle the unrestricted coherent-residue problem.

The later [weighted prime-residue estimate](weighted_prime_residue_windows.md)
allows growing numbers of local residues and gives a uniform harmonic
bound from their weighted support sizes. Its
[single-residue specialization](weighted_prime_residue_windows.md#power-law-interval-bound-with-one-residue-at-each-prime)
also verifies the quantitative rate
$T(\log Q)^{-0.086071\ldots+o(1)}$ on intervals of length
$T\ge Q^{1+\varepsilon}$. The qualitative interval range in (1)
below is wider, so neither formulation is discarded.

## Uniform interval bound: proved

For integers $Q\ge2$ and $b$, put
$$
 U_Q(b)=\bigcup_{Q\le q\le2Q}(b+q\mathbb Z).
$$
Uniformly in $b$ and in intervals $I$ of length $H$,
$$
 \frac{|U_Q(b)\cap I|}{H}\longrightarrow0
 \quad\text{as }Q\to\infty\text{ and }H/Q\to\infty.
 \tag{1}
$$
There is no restriction on the location of the interval or on the size
of the common shift.

**Finite estimate.** For squarefree $P\le Q$, define
$$
 A(P)=\sqrt3\prod_{p\mid P}
 \left(\frac{\sqrt{2-1/p}}p+(1-1/p)^{3/2}\right).
$$
Then
$$
 \frac{|U_Q(b)\cap I|}{H}\le A(P)+\frac{2PQ}{H}.
 \tag{2}
$$

**Proof.** On a residue $r\pmod P$, the incidence sum is
$$
 S_Q(r)=\sum_{Q\le q\le2Q}\frac{(q,P)}q
                  \mathbf1_{(q,P)\mid r-b}.
$$
For fixed $t\pmod P$, the nonnegative periodic function
$f_t(q)=(q,P)\mathbf1_{(q,P)\mid t}$ has mean
$$
 W_P(t)=
 \prod_{\substack{p\mid P\\p\mid t}}(2-1/p)
 \prod_{\substack{p\mid P\\p\nmid t}}(1-1/p).
 \tag{3}
$$
Indeed the residues with $(q,P)=d$ have proportion
$\varphi(P/d)/P$; summing $d\varphi(P/d)/P$ over $d\mid(P,t)$
factors as (3). Splitting $[Q,2Q]$ into periods of length $P$ and
using $1/q\le1/Q$ gives $S_Q(r)\le3W_P(r-b)$ when $P\le Q$.

CRT and the elementary count in one progression give
$$
 |U_Q(b)\cap I\cap(r+P\mathbb Z)|
 \le \frac HP S_Q(r)+2Q.
$$
The trivial bound in the same residue class is $H/P+1$. Taking the
smaller bound and summing over $r$ yields
$$
 \frac{|U_Q(b)\cap I|}{H}
 \le\frac1P\sum_{r\bmod P}\min(1,S_Q(r))+\frac{2PQ}{H}.
$$
Since $\min(1,x)\le\sqrt x$ for $x\ge0$, the first term is at most
$\sqrt3\,\mathbb E_{t\bmod P}\sqrt{W_P(t)}=A(P)$. The product
formula for this expectation follows from CRT independence. This proves
(2).

For $P$ the product of successively more primes,
$$
 A(P)=\exp\left[-(3/2-\sqrt2)\sum_{p\mid P}\frac1p+O(1)\right]
 \longrightarrow0.
$$
Here $3/2-\sqrt2>0$ and the prime reciprocal sum diverges. The latter
also follows directly because the Euler product over $p\le z$ dominates
$H_{\lfloor z\rfloor}$, while its logarithm is
$\sum_{p\le z}1/p+O(1)$. In (2), first fix such a $P$, then let
$Q,H/Q\to\infty$, and finally increase $P$. This proves (1).
$\square$

The same bounds apply to any coherent subfamily with moduli in
$[Q,2Q]$: finite CRT supplies a common integer shift, even when the
residues originally come from an arbitrary profinite center. Both the
center and the subfamily may vary with $Q$. Delayed activation only
reduces the counted set.

## Uniform harmonic bound for one block: proved

Let $B_Q$ be any delayed coherent singleton union with moduli in
$[Q,2Q]$. Then
$$
 \sup_{B_Q}\sup_{X\ge2}
 \frac{H_{B_Q}(X)}{H_{\lfloor X\rfloor}}\longrightarrow0
 \qquad(Q\to\infty).
 \tag{4}
$$
Thus a single coherently shifted dyadic block cannot retain positive
normalized harmonic deletion by moving its hits to arbitrarily large
quotients.

For a proof, write $N_Q(t)=|B_Q\cap[1,t]|$. It vanishes for $t<Q$,
and (2), applied to $(0,t]$, gives
$N_Q(t)\le A(P)t+2PQ$. Partial summation, for $X\ge Q$, gives
$$
 H_{B_Q}(X)
 \le A(P)(1+\log(X/Q))+2P.
$$
Consequently, for $Q\ge\max(P,3)$,
$$
 \sup_{B_Q,X\ge2}\frac{H_{B_Q}(X)}{H_{\lfloor X\rfloor}}
 \le A(P)+\frac{2P}{\log Q}.
 \tag{5}
$$
First let $Q\to\infty$ and then increase the primorial $P$.
This proves (4).

## Scope and limitations

The condition $H/Q\to\infty$ in (1) cannot simply be removed.
For $b=Q$, every integer in $[2Q,3Q]$ is an active hit, witnessed
by $q=n-Q\in[Q,2Q]$. Such natural-density spikes therefore remain
possible, although (4) shows their uniformly vanishing normalized
harmonic effect.

An unbounded number of dyadic blocks need not obey a summable version of
(4). Neither this result nor the earlier
[bounded-quotient compression bound](compression_and_blocks.md#uniform-bound-for-bounded-quotient-deletion-proved)
controls a general conditioned tail. The
[unrestricted coherent case](structured_residues.md#coherent-profinite-residues-only-a-partial-reduction)
is still unresolved.

## Coherence is essential for the long-interval conclusion

For arbitrary singleton residues the interval assertion (1) is false,
even when the Haar footprint tends to zero and $H/Q\to\infty$.
This is a **natural-counting** obstruction, not a logarithmic-density
counterexample.

Let $L\ge12$ be divisible by $12$, and choose $Q>L$, $Q\ge12$.
Independently color each integer $q\in[Q,2Q]$ uniformly by
$j_q\in\{1,\ldots,L\}$ and use the class $j_q\pmod q$.
Write $b_Q=\mu(\bigcup_{Q\le q\le2Q}q\widehat{\mathbb Z})$.
For every coloring its Haar union has measure at most $Lb_Q$, since it
is contained in the union of $L$ common translates of this multiples
window. The proved bound (2) implies $b_Q\to0$.

Fix an integer $n\in I=[3LQ/4,LQ]$. For each integer
$L/2\le k\le2L/3$, choose $j\in[1,L]$ with $j\equiv n\pmod k$.
Such a $j$ exists because $k\le L$. Then
$$
 q=(n-j)/k\in[Q,2Q]:\qquad
 q\ge9Q/8-3/2\ge Q,\quad q\le2Q.
$$
Different chosen pairs give different moduli: if
$n=kq+j=k'q+j'$, then $q|j-j'$, and $|j-j'|<L<Q\le q$
forces $j=j'$ and $k=k'$. Thus at least $L/6$ independent colors
can delete $n$, each with probability $1/L$. Consequently
$$
 \Pr(n\text{ is deleted})\ge1-e^{-1/6}.
$$
Averaging over $n$ supplies a coloring deleting at least this fraction
of the integer points of $I$. All these hits are active, since $n>q$.

For each increasing $L$, choose $Q$ so large that $Lb_Q\le1/L$.
Then the Haar footprint tends to zero, whereas the interval length is
$H=LQ/4$ and its deleted proportion stays bounded away from zero.
The moduli are distinct and all lie in a single dyadic window.

### Why the consecutive-shift container does not amplify harmonically

Let
$$
 V=\bigcup_{1\le j\le K}\bigcup_{Q\le q\le2Q}[j]_q,
 \qquad 1\le K<Q.
$$
Writing $s=\sum_{Q\le q\le2Q}1/q\ge1/2$, its full incidence count
$F$ has mean $Ks$. For $d=(q,r)$, at most $K^2/d+K$ pairs
$(j,\ell)\in[1,K]^2$ satisfy $j\equiv\ell\pmod d$. Therefore
$$
 \mathbb EF^2\le K^2s^2+K G_Q,
 \qquad G_Q=\sum_{Q\le q,r\le2Q}\frac{(q,r)}{qr}
 \le4(1+\log(2Q)).
$$
The last bound follows from $(q,r)=\sum_{d\mid q,r}\varphi(d)$.
Cauchy--Schwarz gives
$$
 \mu(V)\ge\frac{Ks^2}{Ks^2+G_Q}
 \ge\frac{K}{K+16(1+\log(2Q))}.
$$
Thus making this entire container's footprint tend to zero requires
$K=o(\log Q)$. Even the full range $[Q,KQ]$ contributes only
$O(1+\log K)=o(\log Q)$ harmonic mass, not a positive normalized
harmonic anomaly. This does not give a lower bound for every colored
subunion, whose measure can be much smaller than that of its container.
