---
name: research/erdos_25/conditioned_endpoint_blocks
desc: Dense finite endpoint blocks have tiny conditioned Haar mass, but independent Bernoulli protection cannot extend them to polynomial-length epochs.
tags: [endpoints, obstructions, finite-sieves, probability]
sources: []
created: 2026-09-22T04:10:00Z
updated: 2026-09-24T22:13:01Z
---


# research/erdos_25/conditioned_endpoint_blocks

***

This is a finite obstruction, **not** a counterexample to Problem 25.
It defeats a proposed scale-by-scale charging inequality. An amortized
argument would have to account for the earlier sieve which prepares each
block, not only the new endpoints and their incremental Haar measure.

## Statement

For each fixed integer $k\ge1$, put $L=2^k$. For arbitrarily large
multiples $Q$ of $4L$, there is a finite distinct-modulus singleton sieve
using only moduli below $2Q$, with at least $Q/(4L)$ first-kill endpoints
$n=q\in[Q,2Q)$. The sum $\tau$ of the full first-kill densities of
these new endpoint classes satisfies
$$
 \tau\ll_L(\log Q)^{-(1+k/2)}.
 \tag{1}
$$
Consequently there are no absolute $C$ and positive function $f$ for
which every such block satisfies
$$
 \tau\ge\frac{f(\alpha)}{(\log Q)^C},
 \qquad\#\{\text{new endpoints in }[Q,2Q)\}\ge\alpha Q.
 \tag{2}
$$
Choose $k$ with $1+k/2>C$ and fix $\alpha=1/(4L)$.

The earlier congruences need not themselves have private endpoints.
Thus this does not disprove a version of (2) imposing that additional
condition on the entire earlier family.

## Preparing a protected set with uniformly distributed empty residues

Fix $c=1/1000$ and set
$$
 H=Q/L,\quad J=[Q/L,2Q/L)\cap\mathbb Z,\quad
 N=\left\lceil\frac{Q}{c\log Q}\right\rceil.
$$
We take $Q$ sufficiently large in terms of $L$, so $L<N<Q$.
Install the $k$ classes
$$
 2^{j-1}\pmod{2^j},\qquad1\le j\le k.
$$
Their full survivor set is exactly $L\mathbb Z$.
For each future modulus $N\le q<Q$, write
$$
 g_q=(q,L),\qquad r_q=q/g_q.
$$
Every effective modulus satisfies
$r_q\ge N/L\gg_L Q/\log Q$, and a given $r$ arises from at most
$k+1$ original moduli. Indeed $q=2^e r$ with $0\le e\le k$.

Select $S\subseteq J$ by retaining each integer independently with
probability $1/2$. For each distinct effective modulus $r$, let
$$
 E_r=\{b\bmod r:S\cap[b]_r=\varnothing\},\qquad m_r=|E_r|.
$$
The indicators of $b\in E_r$ are independent as $b$ varies with $r$
fixed, since their sets of sampled integers are disjoint. If
$\ell_{r,b}=|J\cap[b]_r|$, their means are $2^{-\ell_{r,b}}$.
We have
$$
 \ell_{r,b}\le H/r+1\le c\log Q+1,
$$
so all these means are at least $\rho:=Q^{-1/100}$ for large $Q$.

Put $G=Q^{1/4}$ and $\epsilon=Q^{-1/10}$. With probability tending
to one, simultaneously for all the effective $r$, all $d\mid r$ with
$d\le G$, and all $u\bmod d$,
$$
 m_r\ge\tfrac12r\rho,
 \qquad
 \frac{|E_r\cap[u]_d|}{m_r}
 =\frac{1+O(\epsilon)}d.
 \tag{3}
$$
Here and below the absolute constants in this $O$-notation can be fixed
independently of $r,d,u$.

To verify the expectation in (3), the row lengths $\ell_{r,b}$ have
only two consecutive values. The longer rows form a cyclic interval of
residues modulo $r$. Its intersection counts in classes modulo $d$
differ by at most one. Thus if $\mu_r=\mathbb E m_r$, then
$$
 \left|\mathbb E|E_r\cap[u]_d|-\mu_r/d\right|\le1,
 \qquad
 \mu_r/d\gg_L Q^{3/4-1/100}/\log Q.
$$
For a sum $Y$ of independent Bernoulli variables, the exponential-moment
bound gives
$\Pr(|Y-\mathbb EY|>\epsilon\mathbb EY)
\le2\exp(-\epsilon^2\mathbb EY/3)$ for $0<\epsilon<1$.
Apply this to all these counts and to $m_r$. There are at most $Q^3$
counts, while each error probability is exponentially small in a
positive power of $Q$. The expectation error of at most one is also
negligible relative to $\epsilon\mu_r/d$. This proves (3) by a union
bound. The same inequality gives $|S|\ge H/4$ with probability tending
to one. Fix an $S$ with all these properties.

## Making the full survivor measure small

Independently for each original modulus $q\in[N,Q)$, choose a uniform
$b_q\in E_{r_q}$ and install
$$
 a_q\equiv Lb_q\pmod q.
 \tag{4}
$$
For $n=Lt$, condition (4) is equivalent to
$t\equiv b_q\pmod{r_q}$, because $(L/g_q,r_q)=1$.
Every point of $LS$ avoids all these classes and the earlier digit
classes.

Let $t$ be Haar-random and write
$$
 X_r(t)=\frac{\mathbf1_{E_r}(t\bmod r)}{m_r},\qquad
 Z(t)=\sum_{N\le q<Q}X_{r_q}(t),\qquad
 M=\mathbb EZ=\sum_{N\le q<Q}\frac1{r_q}.
$$
We claim
$$
 \operatorname{Var}Z\ll_L Q^{-1/20}.
 \tag{5}
$$
If $d=(r,s)\le G$, CRT and (3) give
$$
 \mathbb E X_rX_s
 =\frac{d}{rs\,m_rm_s}
   \sum_{u\bmod d}|E_r\cap[u]_d|\,|E_s\cap[u]_d|
 =\frac{1+O(\epsilon)}{rs}.
$$
The total contribution of these covariances is $O(\epsilon M^2)$.
The number of ordered original pairs with $(r_q,r_{q'})>G$ is at most
$$
 (k+1)^2\sum_{d>G}^{Q}\lfloor Q/d\rfloor^2
 \ll_L Q^2/G.
$$
For such a pair, (3) bounds the joint expectation by
$$
 \mathbb E X_rX_s\le\frac1{m_rm_s}
 \ll_L\frac{Q^{2/100}(\log Q)^2}{Q^2}.
$$
For an upper variance bound its covariance is no larger than this.
Therefore
$$
 \operatorname{Var}Z
 \ll\epsilon M^2+O_L\bigl(Q^{2/100}(\log Q)^2/G\bigr),
$$
which implies (5), since $M=O_L(\log\log Q)$.

The mean is more precisely
$$
 \begin{aligned}
 M&=\sum_{N\le q<Q}\frac{(q,L)}q\\
  &=\left(\sum_{d\mid L}\frac{\varphi(d)}d\right)
                    \log(Q/N)+O_L(1/N)\\
  &=(1+k/2)\log\log Q+O_L(1).
 \end{aligned}
 \tag{6}
$$
This follows by expanding $(q,L)=\sum_{d\mid(q,L)}\varphi(d)$ and
using harmonic sums in the resulting divisibility classes.

Conditional on $t$, independent choices in (4) leave it uncovered with
probability $\prod_q(1-X_{r_q}(t))\le e^{-Z(t)}$.
Consequently the expected full periodic survivor density of the old
sieve (the digit classes and (4)) is at most
$$
 \frac1L\mathbb E e^{-Z}
 \le\frac1L\bigl(e^{1-M}+\Pr(Z<M-1)\bigr)
 \le\frac1L\bigl(e^{1-M}+\operatorname{Var}Z\bigr).
$$
By (5)--(6), some finite choice of the residues therefore has full
survivor density
$$
 \delta_{\rm old}\ll_L(\log Q)^{-(1+k/2)}.
 \tag{7}
$$
It still preserves every point of $LS$.

## Appending the endpoint block and checking activation

Choose exactly $Q/(4L)$ points from $LS\subseteq[Q,2Q)$, and for each
chosen $n$ append the zero class modulo $n$.
Every appended modulus exceeds every old modulus, and they are all
distinct. The endpoint $n$ avoids every old full class by construction.
It also avoids every other appended class of smaller modulus: two
distinct integers in $[Q,2Q)$ cannot divide one another. Thus it is
first killed by its own congruence, active exactly at $n=q$.

There are exactly $Q/(4L)$ such endpoints. The full first-kill
cells of the appended classes are disjoint subsets of the old full
survivor set. Their total Haar mass is consequently at most
$\delta_{\rm old}$, proving (1).

One can also keep the **global** survivor density at least $1/2$:
replace every pair $(q,a)$ in this finite construction by $(2q,2a)$.
This confines all deletions to the even integers, preserves activation
exactly, and halves both the endpoint block fraction and the selected
Haar mass. Thus a positive global survivor density does not repair (2).

The construction does not arrange infinitely many such preparations at
bounded total Haar cost while preserving positive logarithmic endpoint
mass. Nor do its individual endpoint windows have positive normalized
logarithmic weight as $Q\to\infty$. These are the missing requirements
for a counterexample to the original problem.

## Why independent protection does not extend to a logarithmic epoch

The last continuation tested replacing the dyadic protected window by
an interval $[Q,Q^K]$, with fixed $K>1$. For independent
positive-density protection, there is a precise obstruction.

Let $Q\ge1$ be an integer, $X\ge Q$, and $0<\theta<1$. Retain
each integer of $I=[Q,X]\cap\mathbb Z$ independently with
probability $\theta$, obtaining $S$. If
$T=|I|=\lfloor X\rfloor-Q+1$, then
$$
 \Pr\{\exists q\le Q,\ a\bmod q:\ S\cap[a]_q=\varnothing\}
 \le Q^2(1-\theta)^{\lfloor T/Q\rfloor}
 \le Q^2e^{-\theta\lfloor T/Q\rfloor}.
 \tag{8}
$$
Indeed, each residue class modulo $q\le Q$ contains at least
$\lfloor T/q\rfloor\ge\lfloor T/Q\rfloor$ points of $I$.
The probability all are omitted is at most the indicated power of
$1-\theta$. There are $\sum_{q\le Q}q\le Q^2$ possible classes,
so the union bound proves (8).

For $X=Q^K$, the right side tends to zero. With probability tending
to one, **every** class at every preparatory modulus $q\le Q$
therefore meets $S$. All those congruences would be active at the
intersecting points, because the protected interval starts at $Q$.
Consequently no such class can be installed while preserving all of
$S$. This prevents the direct Bernoulli empty-residue construction
from protecting a fixed positive density across a polynomial epoch.

The same obstruction applies inside the fixed fiber $L\mathbb Z$
used above. Select quotient integers independently on
$[\lceil Q/L\rceil,\lfloor X/L\rfloor]$. Every class modulo
$q\le Q$ compatible with $L\mathbb Z$ induces one quotient
class modulo $q/(q,L)\le Q$. Repeating the proof bounds the
probability of any compatible empty class by
$$
 Q^2\exp\!\left(
 -\theta\left\lfloor
 \frac{\lfloor X/L\rfloor-\lceil Q/L\rceil+1}{Q}
 \right\rfloor\right).
 \tag{9}
$$
For fixed $L$ and $X=Q^K$, this also tends to zero.
Incompatible classes can be installed but remove no part of the
fiber and so cannot supply the intended preparation within it.

Equations (8)--(9) concern independent sampling at a fixed positive
retention probability. They do not rule out a correlated protected
set, a growing preparatory fiber, or interleaved preparation using
moduli larger than $Q$. The overlapping-parent preparation still
lacks distinct appended congruences with sufficiently long protected
active traces. Its pointwise conditional Haar estimates do not
establish the required trace statement.
