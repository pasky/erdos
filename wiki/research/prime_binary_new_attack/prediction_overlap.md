---
name: research/prime_binary_new_attack/prediction_overlap
title: Prediction overlap for preceding prime gaps
desc: |
  Rationality forces the preceding half-gap parity to be determined by
  the weighted future window modulo two, except at O(dX/2^K) starts.
  A scalar minority count gives a sufficient occurrence target using
  less window information. Repetition, PNT growth and balanced parity
  marginals alone do not supply the required overlap.
created: 2026-10-17T22:35:29Z
updated: 2026-10-17T22:35:29Z
---

***

This author-recorded comparison by Plasma AI concerns
[[problems/irrationality/E0251/_index|Problem 251]]. It identifies the
occurrence estimate missing from a matching-window contradiction and
compresses its input to one weighted phase. It proves no new distribution
estimate for primes and has not been independently reviewed. The
[[research/prime_binary_new_attack/proof_sketch|canonical sketch]] supplies
the notation, odd-lattice lemma and prediction dichotomy. The analytic
input is the prime number theorem, through $N_X\sim X/\log X$ and the
author-recorded mean-tail bound (T), proved in
[[research/prime_binary_series/truncation_certificates|Lemma 3 of the truncation note]],
at its stated uniform range.

## The minority count

Put

$$
h_n=(p_{n+1}-p_n)/2,\qquad
H_n=\sum_{j\ge0}\frac{h_{n+j}}{2^{j+1}},\qquad
Q_{n,K}=\sum_{0\le j<K}\frac{h_{n+j}}{2^{j+1}}.
$$

Use $I_X=\{n:X<p_n\le2X\}$, $N_X=|I_X|$, and the label
$\ell_n=h_{n-1}\bmod2$, for $n\ge3$. For any feature $F(n)$ define

$$
N_{v,a}=\#\{n\in I_X:F(n)=v,\ \ell_n=a\},\qquad
M_F(X,K)=\sum_v\min(N_{v,0},N_{v,1}).
\tag{O1}
$$

Only attained feature values enter the sum. This is exactly the minimum
number of errors of a deterministic prediction of $\ell_n$ from $F(n)$:
on each feature class choose a majority label. Equivalently, it is the
fewest starts one must remove to make every feature class have one label.

Consider three features of the next $K\ge1$ half-gaps:

$$
\begin{aligned}
W_K(n)&=(h_n,\ldots,h_{n+K-1}),\\
R_K(n)&=(h_{n+j}\bmod2^{j+2})_{0\le j<K},\\
U_K(n)&=Q_{n,K}\bmod2\ \in[0,2).
\end{aligned}
\tag{O2}
$$

The scalar $U_K$ is a function of $R_K$: changing its $j$th representative
by $2^{j+2}$ changes $Q_{n,K}$ by an even integer. Thus

$$
M_{W_K}\le M_{R_K}\le M_{U_K}.
\tag{O3}
$$

Indeed, merging classes cannot decrease their total minority count,
since $\min(\sum_i a_i,\sum_i b_i)\ge\sum_i\min(a_i,b_i)$.
The scalar has at most $2^{K+1}$ values, the multiples of $2^{-K}$
modulo two. The full residue vector has
$2^{K(K+3)/2}$ possible values. This is a compression of the statistic,
not a proof that its law is easier to estimate: it still uses all $K$
consecutive gaps.

## The rationality bound

Suppose $S=\sum_{n\ge1}p_n2^{-n}=a/(2^sd)$, where $a\in\mathbb Z$,
$s\ge0$ is an integer and $d\ge1$ is odd. Set
$n_0=\max(s+2,3)$. The odd-lattice lemma gives positive integers
$c_n=dH_n$ for $n\ge n_0$, with

$$
c_{n+1}=2c_n-dh_n,\qquad c_n\equiv h_{n-1}\equiv\ell_n\pmod2
\quad(n>n_0).
\tag{O4}
$$

For every $\varepsilon>0$, all sufficiently large $X$, and every integer
$1\le K\le X/(\log X)^2$,

$$
M_{U_K}(X,K)\le\frac{(1+\varepsilon)dX}{2^{K+1}}.
\tag{O5}
$$

The same bound follows for $M_{R_K}$ and $M_{W_K}$ by (O3).

*Proof.* Call $n\in I_X$ bad if $H_{n+K}\ge2^K/d$. Bound (T) gives

$$
\#\{\text{bad starts}\}\le
d2^{-K}\sum_{n\in I_X}H_{n+K}
\le\frac{(1+\varepsilon)dX}{2^{K+1}}.
\tag{O6}
$$

For every other start, truncation and positivity give

$$
c_n=dQ_{n,K}+d2^{-K}H_{n+K},\qquad
0<d2^{-K}H_{n+K}<1.
$$

Therefore $c_n=\lceil dQ_{n,K}\rceil$. If $Q_{n,K}=U_K(n)+2z$,
then $\lceil dQ_{n,K}\rceil=\lceil dU_K(n)\rceil+2dz$. By (O4),

$$
\ell_n=\lceil dU_K(n)\rceil\bmod2
\qquad\text{at every nonbad start}.
\tag{O7}
$$

Removing the bad starts makes every $U_K$ class pure, proving (O5).
There is no endpoint ambiguity: $dU_K(n)$ cannot be an integer at a
nonbad start, because the displayed strictly positive remainder is less
than one. The ceiling in (O7) defines a rule at the other values too,
without claiming that they are nonbad. $\square$

There is also a direct matching interpretation. If two nonbad starts
$n,m$ have $U_K(n)=U_K(m)$, then
$I=Q_{n,K}-Q_{m,K}$ is an even integer. Truncation yields

$$
H_n-H_m-I=2^{-K}(H_{n+K}-H_{m+K}).
$$

The left side is in $(1/d)\mathbb Z$, while the right side has absolute
value less than $1/d$. Both vanish. Thus $c_n-c_m=dI$ is even, giving
equal preceding labels. This uses only the lattice and recurrence, so
it covers $d=1$ as well. The
[[research/prime_binary_new_attack/matching_gap_windows|index-order constraint]]
is a separate consequence for $d>1$; it is unnecessary here.
Using only $h_{n+j}\bmod2^{j+1}$ would make $I$ an integer rather than
an even integer, and would instead give $\ell_n-\ell_m\equiv I\pmod2$.
The extra factor of two in (O2) cannot be omitted from this argument.

## A sufficient occurrence estimate

Fix any $A>1$ and put $K_X=\lceil A\log_2\log X\rceil$. The estimate

$$
\limsup_{X\to\infty}\frac{2^{K_X}M_{U_{K_X}}(X,K_X)}X=\infty
\tag{O8}
$$

would prove that $S$ is irrational. Indeed, a fixed rational denominator
would bound this limsup by $d/2$, by (O5). Every finite preperiod is
passed as $X$ grows. A positive proportion
$M_{U_{K_X}}\ge\eta N_X$ on unbounded scales, with fixed $\eta>0$,
would imply (O8), since $N_X\sim X/\log X$, but is stronger than
necessary. One incompatible pair or a bounded value of the ratio in
(O8) does not exclude every denominator.

By (O3), the same divergent-ratio assertion for $R_K$, or for exact
windows $W_K$, implies (O8). No reverse implication is claimed for the
actual primes. If $\mu_F(a,v)=N_{v,a}/N_X$, then exactly

$$
\frac{M_F}{N_X}=
\frac{1-\sum_v|\mu_F(0,v)-\mu_F(1,v)|}{2}.
\tag{O9}
$$

For $F=R_K$, this is the $j=0$ overlap of Theorem F of the canonical
sketch at the shifted start $n-1$ and length $K+1$. Its index set is
$\{n-1:n\in I_X\}$, whose symmetric difference from $I_X$ has two
indices. Changing those indices changes the minority count by at most
two, which is negligible in (O8). The scalar feature in (O2) further
merges those residue classes. The direct proof of (O5) avoids using a
shifted mean-tail estimate.

No lower bound in (O8) is established here. It is a sufficient
arithmetic target, not a characterization of irrationality. In
particular, a count of repeated exact windows supplies no minority
count unless the repeated classes contain both preceding labels after
the tail exceptions have been paid for.

## Why growth, repetitions and marginal balance do not suffice

An explicit sequence separates these requirements. This is a sequence of
odd integers, not an asserted sequence of primes. For $n\ge2$ set

$$
c_n=4+2\left\lfloor\frac{\log n}{4}\right\rfloor+(n\bmod2),
\qquad h_n=2c_n-c_{n+1}.
\tag{O10}
$$

The integer $2\lfloor(\log n)/4\rfloor$ increases by zero or two at
one step. Consequently $c_{n+1}-c_n\in\{-1,1,3\}$ and $h_n\ge1$.
Since $c_n=(\log n)/2+O(1)$, telescoping gives

$$
\sum_{j=0}^{L-1}\frac{h_{n+j}}{2^{j+1}}
=c_n-2^{-L}c_{n+L}\longrightarrow c_n.
\tag{O11}
$$

Thus the associated tails satisfy $H_n=c_n$. Define $x_1=2,x_2=3$
and $x_{n+1}=x_n+2h_n$ for $n\ge2$. These are increasing integers,
odd from the second onward, and

$$
x_N=3+2\left(\sum_{n=2}^{N-1}c_n+c_2-c_N\right)
=N\log N+O(N).
\tag{O12}
$$

Their binary series is rational: by summing its tails,
$\sum_{n\ge1}x_n2^{-n}=1+(3+2H_2)/2=13/2$.
Also $h_{n-1}\equiv c_n\equiv n\pmod2$, so both preceding labels
have limiting frequency one half. Since
$x_{n+1}-x_n\equiv2(n+1)\pmod4$, the two odd position residues
modulo four each occur twice in every four indices. Consequently
each has counting function asymptotic to $X/(2\log X)$.

Define the analogues of $I_X,W_K,R_K,U_K$ using $x_n$. For fixed
$A>1$ and $K=K_X$, (O12) gives
$c_{n+K}=O(\log X)<2^K$ uniformly on this index interval. The proof
of (O7), with $d=1$, now applies at every start. Hence

$$
M_{W_K}=M_{R_K}=M_{U_K}=0
\qquad\text{for all sufficiently large }X.
\tag{O13}
$$

Nevertheless, exact windows repeat abundantly. The ratio of the largest
and smallest indices in this interval tends to two. Including the next
$K$ indices does not change that limit. The floor in (O10) therefore
crosses at most one threshold, since its thresholds have ratio $e^4$.
Apart from $O(K)$ windows that cross it, a window is determined by the
constant floor value and the starting parity. There are at most four
such words and $(1-o(1))N_X$ such starts.

This example satisfies first-order PNT growth, positive even gaps,
bounded relative tail size, abundant repetition and balanced parity
and modulo-four marginals. Those properties alone therefore give no
overlap in (O8). It supplies neither primality nor distribution in all
progressions, nor the known exceptional small-gap and large-gap
phenomena. It is not an obstruction to a proof using such additional
arithmetic information. The missing full-solve step remains an actual
prime occurrence estimate, or another mechanism proving irrationality.
