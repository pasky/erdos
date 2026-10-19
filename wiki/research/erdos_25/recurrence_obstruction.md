---
name: research/erdos_25/recurrence_obstruction
desc: Near-density-one finite-return obstructions, with bounded-density limiting residue laws and a positive-measure affine-ideal boundary.
tags: [endpoints, recurrence, obstructions]
sources: []
created: 2026-09-22T02:51:13Z
updated: 2026-09-24T22:13:01Z
---


# research/erdos_25/recurrence_obstruction

***

An attempted new route was additive recurrence: an endpoint set with
positive logarithmic density should return along its assigned arithmetic
progressions. The following construction shows why finite-return versions
of this idea fail, even under much stronger density hypotheses.

## A growing-horizon obstruction: proved

**Theorem.** For every $0<\varepsilon<1$ there are a set $E\subseteq
\mathbb N$ of natural density $\delta>1-\varepsilon$ and an injective
assignment $r\mapsto q(r)$ such that
$$
 q(r)\le r<2q(r),\qquad
 0\le r-q(r)\ll_\varepsilon
 r\left(\frac{\log\log r}{\log r}\right)^2,
$$
and, for all sufficiently large $r\in E$,
$$
 E\cap\{r+kq(r):k\in\mathbb Z,\ k\le
             c_\varepsilon\log r/\log\log r\}
 =\{r\}.
 \tag{1}
$$
Nevertheless, each assigned progression returns to $E$ with asymptotic
frequency at least $\delta$:
$$
 \lim_{Y\to\infty}\frac1Y
 \#\{1\le k\le Y:r+kq(r)\in E\}\ge\delta.
 \tag{2}
$$
In particular this is **not** a globally private endpoint family, and is
not a counterexample to Problem 25.
After ordering the distinct moduli, it also fails the full first-kill
condition: every assigned class contains infinitely many endpoints with
larger assigned moduli, by (2) and $q(s)>s/2$.

### Construction

Write $\pi_m$ for the $m$th prime. Choose an integer
$A>\zeta(2)/\varepsilon$ and set
$$
 p_k=\pi_{A(k+1)^2}\qquad(k\ge0).
$$
These are distinct, $p_k>k$, and
$\sum_k1/p_k\le\zeta(2)/A<\varepsilon$.
We use the elementary bound $\pi_m\ll m\log(m+1)$.
Indeed Legendre's formula gives
$v_p\binom{2h}{h}\le\lfloor\log_p(2h)\rfloor$, whence
$$
 \log\binom{2h}{h}\le\#\{p\le2h\}\log(2h).
$$
Together with $\binom{2h}{h}\ge4^h/(2h+1)$ this gives
$\#\{p\le x\}\gg x/\log x$ and, on inversion, the stated bound.
In particular $\log p_k\ll_\varepsilon\log(k+2)$.
For $j\ge1$, put
$$
 M_j=\prod_{k=0}^jp_k,\qquad R_j=(j+1)^2M_j.
$$
Choose a unit $c_j\pmod{M_j}$ by CRT such that
$$
 c_j\equiv1\pmod{p_0},\qquad
 c_j\equiv-k^{-1}\pmod{p_k}\quad(1\le k\le j).
$$

The set
$$
 E_0=\{n\ge1:p_k\nmid n\text{ for every }k\ge0\}
$$
has natural density
$$
 \delta=\prod_{k\ge0}(1-1/p_k)
 \ge1-\sum_{k\ge0}1/p_k>1-\varepsilon.
$$
This follows from finite CRT and the uniform tail count
$X\sum_{k>m}1/p_k$. Remove the initial segment below $R_1$ and the
boundary bands
$$
 G_j=[R_j,R_j+M_j)\cap\mathbb N
$$
from $E_0$, obtaining $E$. The bands have natural density zero: when
$R_j\le X<R_{j+1}$,
$$
 \left|[1,X]\cap\bigcup_iG_i\right|
 \le\sum_{i\le j}M_i\le2M_j\le\frac{2X}{(j+1)^2}.
$$
Hence $d(E)=\delta$.

For $r\in E\cap[R_j+M_j,R_{j+1})$, define
$$
 a_r=((1-c_j)r\bmod M_j)\in[0,M_j),\qquad q(r)=r-a_r.
$$
Then $R_j<q(r)<R_{j+1}$ and
$q(r)/r\ge1-1/(j+1)^2>1/2$. Within a stage, equality $q(r)=q(s)$
implies $c_jr\equiv c_js\pmod{M_j}$. Since $c_j$ is a unit,
$r\equiv s\pmod{M_j}$, then $a_r=a_s$ and $r=s$. Different stages
have disjoint modulus ranges. Thus the assignment is globally injective.

The negative step $r-q(r)=a_r$ is divisible by $p_0$, so is outside
$E$. All further negative steps are negative. For $1\le k\le j$,
$$
 r+kq(r)\equiv r(1+kc_j)\equiv0\pmod{p_k},
$$
so the first $j$ positive steps also miss $E$.

Finally $\log R_{j+1}\ll_\varepsilon(j+2)\log(j+3)$.
Since $r<R_{j+1}$, monotonic inversion gives
$j\gg_\varepsilon\log r/\log\log r$ for large $r$, proving (1).
Moreover
$$
 0\le r-q(r)<M_j\le\frac r{(j+1)^2}
 \ll_\varepsilon r\left(\frac{\log\log r}{\log r}\right)^2.
$$

### Eventual returns remain abundant

For any fixed $r\in E$ and any $q\ge1$, finite CRT and the summable
prime tail give
$$
 d\{k\ge1:r+kq\in E_0\}
 =\prod_{\substack{p\in\{p_0,p_1,\ldots\}\\p\nmid q}}(1-1/p)
 \ge\delta.
 \tag{3}
$$
A selected prime dividing $q$ never divides $r+kq$, since it does not divide
$r$. Every other prime forbids exactly one residue of $k$. To justify
the infinite tail uniformly before taking limits, its number of hits
among $k\le Y$ is at most
$$
 (r+qY)\sum_{p\text{ in the omitted tail}}1/p.
$$
Divide by $Y$, first let $Y\to\infty$, and then truncate farther.
Removing a density-zero set of integers changes the density along any
fixed progression by zero. Thus (3) holds with $E$ in place of $E_0$,
proving (2).

## What the failed recurrence route teaches

Let $E_K$ consist of endpoints whose assigned progression has no other
$E$-point through its first $K$ positive steps. Every $E_K$ contains all
but finitely many points of $E$, so
$$
 d(E_K)=\delta\quad\text{for every fixed }K,
 \qquad \bigcap_{K\ge1}E_K=\varnothing.
$$
Thus neither a uniform bounded-return theorem nor interchanging the
return-horizon limit with logarithmic density is legitimate. Even a
return horizon of order $\log r/\log\log r$ can miss almost all the
eventual recurrence.

The [private-endpoint target](unresolved_estimates.md#private-witness-reduction-for-endpoints)
requires avoidance of **all** other endpoints along the whole progression.
This construction does not have that property. It rules out fixed
return horizons and the indicated growing horizon, not every larger
endpoint-dependent finite horizon. A recurrence proof needs additional
information beyond these weaker conditions; passing from them to full
privacy by continuity of logarithmic density is invalid.

## The scale of this CRT mechanism is optimal

Suppose a finite prime pool $P$, of reciprocal sum at most
$\varepsilon<1$, excludes every $r+kq$ with $1\le k\le K$, where
$r$ is coprime to every pool prime. Each prime excludes at most
$K/p+1$ values of $k$ (and none if it divides $q$). Thus
$|P|\ge(1-\varepsilon)K$. If the enforcing product
$M=\prod_{p\in P}p$ is at most $r$, then
$$
 \log r\ge\log M\ge\log((|P|+1)!)
 \ge(1-\varepsilon)K\log K-O_\varepsilon(K).
$$
Consequently this particular method cannot exceed a horizon of order
$\log r/\log\log r$. This is not a bound for other recurrence
constructions.

## Every residue assignment on these moduli gives density one

There is a stronger obstruction to converting this construction into
a counterexample: its modulus set alone forces full deletion density.

**Lemma.** Suppose $D$ has natural density $\delta>0$, and for integers
$M_J$ all sufficiently large members of $D$ are coprime to $M_J$, with
$\varphi(M_J)/M_J\to\delta$. Then every singleton-residue assignment
on $D$ has delayed excluded union of natural density one.

**Proof.** Let $D_J$ be a cofinite subset coprime to $M_J$, and put
$\beta_J=\mu(\bigcup_{q\in D_J}q\widehat{\mathbb Z})$.
Finite unions of these multiples are independent of the units modulo
$M_J$. The multiples theorem and its finite-periodic logarithmic
approximation therefore give
$$
 \operatorname{ld}\bigl(M(D_J)\cap\{n:(n,M_J)=1\}\bigr)
 =\beta_J\frac{\varphi(M_J)}{M_J}.
$$
The set on the left contains $D_J$, which has density $\delta$.
Hence $\beta_J\ge\delta/(\varphi(M_J)/M_J)\to1$.
Finite union compression, followed by increasing finite unions, gives
the same lower bound for the Haar union of any chosen residue classes
on $D$. That union has measure one. Every finite delayed prefix has
its periodic density, so the entire delayed excluded union has natural
density one by squeezing. $\square$

For the construction above, injectivity and $q(r)=r-o(r)$ imply
$d(\{q(r):r\in E\})=\delta$. To check this directly, for every fixed
$h>0$, all sufficiently large endpoints satisfy
$(1-h)r\le q(r)\le r$, which squeezes the counting functions.
For each fixed $J$, later stages give
$q(r)\equiv c_jr\pmod{M_J}$; both factors are units. Also
$$
 \frac{\varphi(M_J)}{M_J}
 =\prod_{k\le J}(1-1/p_k)\longrightarrow\delta.
$$
The lemma applies. Thus changing the residues while retaining these
moduli cannot repair the construction: every such system has survivor
set of natural, and therefore logarithmic, density zero.

## The limiting residue law is absolutely continuous

The same construction has a stronger distributional property. It defeats
an attempted extension of the
[nonatomic-residue necessary condition](profinite_residue_endpoints.md)
using only limiting marginals and fixed affine returns.

On $G=\widehat{\mathbb Z}$ set
$$
 S=\{x:p_k\nmid x\text{ for every }k\ge0\},\qquad
 A=\{a:p_0\mid a,\ p_k\nmid a\text{ for every }k\ge1\}.
$$
Then $\mu(S)=\delta$ and $\mu(A)=\delta/(p_0-1)$. For the actual
endpoints and assignments constructed above, the logarithmic empirical
measures satisfy
$$
 \begin{aligned}
 \frac1{\log X}\sum_{\substack{r\le X\\r\in E}}\frac{\delta_r}{r}
     &\Longrightarrow\mathbf1_S\mu,\\
 \frac1{\log X}\sum_{\substack{r\le X\\r\in E}}\frac{\delta_{q(r)}}r
     &\Longrightarrow\mathbf1_S\mu,\\
 \frac1{\log X}\sum_{\substack{r\le X\\r\in E}}\frac{\delta_{a_r}}r
     &\Longrightarrow(p_0-1)\mathbf1_A\mu.
 \end{aligned}
 \tag{4}
$$
In particular, all three limiting marginals are absolutely continuous
with bounded density, not just nonatomic.

For the new third assertion, at stage $j$ the map
$$
 r\bmod M_j\longmapsto (1-c_j)r\bmod M_j
$$
takes the units onto
$$
 A_j=\{0\le a<M_j:p_0\mid a,\ (a,M_j/p_0)=1\}
$$
with constant multiplicity $p_0-1$. Indeed $1-c_j=0\pmod{p_0}$,
whereas $1-c_j=(k+1)/k\ne0\pmod{p_k}$ for $1\le k\le j$.
The constructed primes satisfy $p_k>k+1$.

Fix a residue $b\pmod h$. Inclusion--exclusion gives
$$
 |A_j\cap[b]_h|
 =M_j\mu(\widehat A_j\cap[b]_h)+O_h(2^j),
$$
where $\widehat A_j$ imposes the same finite prime conditions on $G$.
Since $2^j/M_j\to0$ and $\widehat A_j\downarrow A$, the corresponding
periodic stage frequency tends to
$(p_0-1)\mu(A\cap[b]_h)$. Each partial stage incurs counting error
$O(M_j)$. Up to a point $X$ in stage $j$, the sum of these errors is
$O(M_j)=o(X)$ because $X\ge R_j=(j+1)^2M_j$.

Replacing the finite unit condition at stage $j\ge J$ by membership in
$E_0$ costs at most $X\sum_{k>J}1/p_k$: a discrepancy must be divisible
by an omitted prime. Let $J\to\infty$. The discarded boundary bands
also have density zero. This proves the claimed natural counting
frequency for $a_r\pmod h$, and partial summation gives its logarithmic
version. Residue cylinders determine weak convergence on $G$.

The first assertion of (4) follows directly from the density-zero
difference between $E$ and $E_0$. For the second, let $D=\{q(r):r\in E\}$.
As proved above, $d(D)=\delta$ and $D$ is eventually coprime to every
fixed $M_J$. The set $D\setminus E_0$ has upper natural density at most
$\sum_{k>J}1/p_k$; hence $D$ differs from $E_0$ by a density-zero set.
Its residue frequencies are therefore those of $S$. Finally,
$q(r)/r\to1$ transfers these frequencies and harmonic weights to the
cutoff and weights in (4).

Every weak joint limit of $(r,q(r),a_r)$ is supported on
$$
 r+kq\equiv0\pmod{p_k}\quad(k\ge1),\qquad
 r-q\equiv0\pmod{p_0}.
$$
Each fixed constraint holds at all sufficiently late stages and is
clopen, so it passes to the limit. Thus every fixed positive affine
return, and the one possibly nonnegative backward return, lies outside
$S$. Nevertheless the actual progressions return to $E$ abundantly,
as (2) proves. Bounded-density marginals and all these fixed-time limit
constraints therefore do not establish global privacy or its negation.

## A positive-measure boundary for affine ideals

For the same $S$, define
$$
 F_S=\{(q,a)\in G^2:(a+qG)\cap S\ne\varnothing\}.
$$
Then
$$
 (q,a)\in F_S
 \quad\Longleftrightarrow\quad
 \text{no }p_k\text{ divides both }q\text{ and }a.
$$
Necessity is immediate. For sufficiency, choose the coordinates of a
point in $a+qG$ independently: if $p_k\mid q$, its $a$-coordinate is
already a unit; if $p_k\nmid q$, one can choose a unit in that affine
fiber. Consequently
$$
 \mu^{\otimes2}(F_S)=\prod_{k\ge0}(1-p_k^{-2})>0.
$$
Yet $F_S$ is closed and nowhere dense. Any basic open neighborhood
leaves a fresh selected prime unconstrained, and has a sub-neighborhood
where that prime divides both coordinates. Thus the open set of affine
ideals entirely contained in $G\setminus S$ has positive-measure boundary.
An attempted joint-measure argument cannot assume that this boundary is
Haar-null, even under absolute continuity. This is an obstruction to
that intermediate argument, not a private-endpoint construction.
