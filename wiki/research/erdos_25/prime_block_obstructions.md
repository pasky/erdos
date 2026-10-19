---
name: research/erdos_25/prime_block_obstructions
desc: Prime-block obstructions to conditional coupling, primitive-kernel control, tautification, and profinite fiber returns.
tags: [obstructions, endpoints, density, prime-coordinates]
sources: []
created: 2026-09-22T03:58:00Z
updated: 2026-09-24T22:13:01Z
---


# research/erdos_25/prime_block_obstructions

***

The constructions here defeat proposed intermediate lemmas.
Neither gives private positive integer endpoints or a counterexample to
Problem 25.

## Positive density does not yield a scaled Behrend subfamily

Call $B$ Behrend when its full multiples union has Haar measure one;
by the established multiples theorem this is equivalent to logarithmic
density one for that union.

**Theorem.** For every $0<\eta<1$ there is a set $D$ of natural density
greater than $1-\eta$ such that, for every integer $d\ge1$, the set
$$
 B_d=\{b\ge2:db\in D\}
$$
is not Behrend. In particular no subfamily of $D$ of the form $dB$,
with $1\notin B$, can have $B$ Behrend.

**Proof.** Choose disjoint finite prime blocks $P_j$ such that
$$
 \varepsilon_j=\prod_{p\in P_j}(1-1/p)>0,
 \qquad\sum_j\varepsilon_j<\eta.
$$
Successive finite blocks exist by divergence of the prime reciprocal
sum. Put $L_j=\prod_{p\in P_j}p$ and choose increasing integers
$N_j\ge L_j/\varepsilon_j$. Define
$$
 D=\{n\ge N_1:(n,L_j)>1\text{ whenever }N_j\le n\}.
$$
Let $S_k$ be the periodic set satisfying the first $k$ block conditions.
CRT gives $d(S_k)=\delta_k=\prod_{j\le k}(1-\varepsilon_j)$, and
$D$ is eventually contained in $S_k$. If $X\ge N_j$, the number of
integers at most $X$ failing block $j$ is at most
$$
 \varepsilon_jX+L_j\le2\varepsilon_jX.
$$
Thus
$$
 \underline d(D)\ge\delta_k-2\sum_{j>k}\varepsilon_j,
 \qquad\overline d(D)\le\delta_k.
$$
Letting $k\to\infty$ proves
$d(D)=\delta=\prod_j(1-\varepsilon_j)>1-\eta$.

Fix $d$ and choose a block $j$ with $(d,L_j)=1$. The exceptional set
$$
 F=\{b\in B_d:(b,L_j)=1\}
$$
is finite, because every member has $db<N_j$. It excludes $1$, so
$\mu(M(F))<1$: integers coprime to the finitely many prime factors of
$F$ avoid $M(F)$. Every other member of $B_d$ has a prime factor in
$P_j$. Consequently
$$
 M(B_d)\subseteq M(F)\cup M(P_j).
$$
The two sets on the right depend on disjoint prime coordinates, since
each member of $F$ is coprime to $L_j$. Their union has measure
$$
 1-(1-\mu(M(F)))\varepsilon_j<1.
$$
This proves the theorem. $\square$

### A positive-measure tail need not contain a divisibility cylinder

The thresholds may also be chosen so that
$N_{j+1}>\prod_{i\le j}\max P_i$. Then
$$
 \bigcap_{Y\ge1}\bigcup_{q\in D,\ q>Y}q\widehat{\mathbb Z}
 =F_\infty:=\{z:\text{each }P_j\text{ contains a prime dividing }z\}.
$$
One inclusion follows from the eventual block requirements on $D$.
For the other, choose a dividing prime $p_i\in P_i$ for each $i$ and
put $d_j=\prod_{i\le j}p_i$. These grow without bound, satisfy
$d_j<N_{j+1}$, and eventually belong to $D$, since every condition
active at $d_j$ has index at most $j$. They all divide $z$.
The event $F_\infty$ has measure $\delta>0$, but for any $d$ a fresh
block coprime to $d$ has positive conditional probability of being missed
on $d\widehat{\mathbb Z}$. Thus no divisibility cylinder is contained
in $F_\infty$, even up to a null set.

## Marginal bounds do not control conditional survivor fractions

A proposed endpoint estimate used a finite period $P$, a survivor set
$S\subseteq\mathbb Z/P\mathbb Z$, and
$$
 f(q,n)=\frac{|S\cap[n]_{(q,P)}|}{P/(q,P)}.
$$
Even if a measure $\gamma$ on pairs $(q,n)$ has both marginals bounded
by uniform measure, has fixed mass $1/2$, and is supported on $n\in S$
with $|S|/P=1/2$, the integral $\int f\,d\gamma$ can tend to zero.

Take $P$ to be the product of the primes up to a growing bound. Write
$$
 K(n)=|\{p\mid P:p\mid n\}|,\qquad
 \mu=\sum_{p\mid P}\frac1p\to\infty,\qquad
 C=\sum_{p\mid P}\frac1{p^2}<1.
$$
For uniform $n\bmod P$, $\mathbb EK=\mu$ and
$\operatorname{Var}K\le\mu$. Chebyshev shows that at least half the
residues have $K(n)\le t:=\mu+\sqrt{2\mu}$. Choose exactly $P/2$ of
these residues as $S$, and set
$$
 \gamma=\frac1P\sum_{n\in S}\delta_{(n,n)}.
$$
Its mass and marginals have the claimed properties.

Generate $n$ uniformly, then generate $m$ uniformly in the residue class
$[n]_{(n,P)}$. The prime coordinates of $m$ are independent and
$$
 \Pr(p\mid m)=\frac2p-\frac1{p^2}.
$$
Indeed a zero coordinate of $n$ forces a zero coordinate of $m$;
otherwise the latter is uniform. Hence
$$
 \int f\,d\gamma
 =\Pr(n\in S,m\in S)
 \le\Pr(K(m)\le t)
 \le\frac{2\mu}{(\mu-C-\sqrt{2\mu})^2}\longrightarrow0.
$$
The last inequality applies once $\mu-C-\sqrt{2\mu}>0$.
A Chernoff bound with parameter $1/2$ gives the stronger bound
$$
 \int f\,d\gamma
 \le\exp\bigl(-(1-\log2)\mu+\sqrt{2\mu}\log2+C/2\bigr).
$$
This is only a finite coupling obstruction. Such a coupling is not a
construction of actual first-kill masses, and it does not account for
the integer sizes needed to realize many logarithmic scales.

## Primitive small-footprint families with a large atom kernel

There are finite primitive squarefree families $D$ with full multiples
footprints $\beta_D\to0$, and cutoffs $X\to\infty$, for which
$$
 \frac1{\log X}\sum_{q\in D}\frac{\log\log q}{q}\longrightarrow\infty.
 \tag{4}
$$
Thus the atom kernel arising when the
[coherent annulus estimate](coherent_annuli_and_shadows.md) is summed
over many bands cannot be controlled solely by primitivity and footprint.

Let $Y\to\infty$, put $L=\log\log Y$, and take the prime pool
$\mathcal P=\{p:L^3<p\le Y\}$. Write
$$
 \lambda=\sum_{p\in\mathcal P}\frac1p
 =L-\log\log L+O(1),\qquad
 r=\left\lceil\lambda+\tfrac12\sqrt{\lambda\log\lambda}\right\rceil.
$$
The reciprocal weight of all products of $r$ distinct pool primes is
$$
 S=\sum_{|A|=r}\frac1{\prod_{p\in A}p}
 =(1+o(1))\frac{\lambda^r}{r!}
 \asymp e^\lambda\lambda^{-5/8}.
 \tag{5}
$$
Indeed, normalize the weights $1/p$ to sample $r$ primes independently.
The collision probability is at most
$\binom r2/(\lambda L^3)=O(L^{-2})$. Stirling's formula, with
$r-\lambda=\tfrac12\sqrt{\lambda\log\lambda}+O(1)$, proves (5).
The elementary Euler-product bounds already established in the wiki give
$e^\lambda\asymp\log Y/\log L$.

For a Haar integer, let $N$ count the pool primes that divide it.
Its mean is $\lambda$ and variance at most $\lambda$. Thus the full
footprint of all these products is
$$
 \Pr(N\ge r)\le\frac{4}{\log\lambda}\longrightarrow0.
 \tag{6}
$$

Restrict the products to $Y^a\le q\le Y^C$, where $a>0$ is a sufficiently
small fixed constant and $C$ a sufficiently large fixed constant.
This retains at least half of $S$. For the upper cutoff, the mean of
$\log q$ under normalized reciprocal weights is at most
$$
 (1+o(1))\frac r\lambda
               \sum_{p\in\mathcal P}\frac{\log p}{p}\ll\log Y,
$$
using the elementary Chebyshev prime-sum bound. Markov's inequality
therefore discards at most $S/4$ when $C$ is large. For the lower cutoff,
a product below $Y^a$ uses only primes below $Y^a$. Their reciprocal sum
is at most $\lambda-c$, with arbitrarily large fixed $c$ available by
taking $a$ small, since
$\sum_{Y^a<p\le Y}1/p=\log(1/a)+O(1)$. Its total weight relative to
$S$ is at most $(1+o(1))(1-c/\lambda)^r$, and is less than $1/4$
for an appropriate fixed $c$.

Let $D$ be the retained products and $X=Y^C$. The family is primitive
because all its squarefree members have the same number $r$ of prime
factors. Equation (6) still bounds its footprint. Since
$\log\log q=L+O_{a,C}(1)$ throughout the retained range, (5) gives
$$
 \frac1{\log X}\sum_{q\in D}\frac{\log\log q}{q}
 \gg\frac{L^{3/8}}{\log L}\longrightarrow\infty,
$$
proving (4).

### Tautness does not imply the weighted reciprocal criterion

These finite blocks can be concatenated into an infinite primitive
**taut** set with arbitrarily small full footprint and unbounded
$W_P(X)/\log X$. Here taut means that deleting any one generator
strictly decreases the full multiples-union measure.

Choose successive $Y_j$ so large that the prime pools
$((\log\log Y_j)^3,Y_j]$ are disjoint and ordered, their trimmed
modulus ranges are also ordered, and their footprints have sum less
than a prescribed $\varepsilon<1$. Let $P$ be the union of the
corresponding finite blocks. Disjoint prime supports and equal rank
within each block make $P$ primitive. Its full footprint is at most
$\varepsilon$. For any generator $q$ in block $j$, the event that
exactly its $r_j$ pool primes divide a Haar integer has positive
probability and makes $q$ the unique certificate in its block.
Independently avoiding the other blocks has positive probability
$\prod_{i\ne j}(1-\beta_i)>0$. Thus $q$ has a positive private Haar
region, proving tautness.

At $X_j=Y_j^C$, the $j$th block alone gives
$$
 \frac{W_P(X_j)}{\log X_j}
 \ge\frac aC\sum_{q\in D_j}\frac1q\longrightarrow\infty
$$
by (5). This refutes the proposed route from tautification to the
[weighted logarithmic criterion](coherent_logarithmic_criterion.md).
It does not supply a coherent logarithmic-density anomaly.

## Even diagonal profinite fibers need not return in Haar measure

For every $\varepsilon>0$ there is a compact
$S\subseteq G=\widehat{\mathbb Z}$, with $\mu(S)>1-\varepsilon$,
such that for Haar-almost every $r\in S$,
$$
 m_{rG}(S)=0.
 \tag{7}
$$
Here $m_{rG}$ is normalized Haar measure on the closed subgroup $rG$,
not a ratio of ambient Haar measures; that subgroup may have ambient
measure zero.

Let $R,U$ be independent Haar points and put
$L(y)=\sum_{p\le y}1/p$. Independence across primes gives
$$
 \frac{\#\{p\le y:p\mid R\}}{L(y)}\longrightarrow1
 \quad\text{almost surely}.
$$
For the product $RU$, the prime-divisibility indicators are also
independent, now with probabilities $2/p-1/p^2$. Consequently their
normalized count tends almost surely to $2$. Both assertions follow
directly from Chebyshev and Borel--Cantelli along cutoffs with
$L(y_k)=k^2+O(1)$: the variances are $O(L(y_k))$, so the relative
error probabilities are summable. Monotonicity of the counts and
$L(y_{k+1})/L(y_k)\to1$ interpolate between cutoffs.

Thus the law of $RU$ is singular to Haar measure. The Borel set where
the displayed limit is $1$ has full Haar measure and zero product-law
measure. Inner regularity supplies a compact subset $S$ of that set
with $\mu(S)>1-\varepsilon$. Hence
$$
 0=\Pr(RU\in S)=\int_G m_{rG}(S)\,d\mu(r),
$$
because multiplication by $r$ pushes Haar measure onto Haar measure
of its compact image $rG$. Nonnegativity proves (7).

For example, the diagonal measure obtained by sending
$\mathbf1_S\mu$ under $r\mapsto(q,n)=(r,r)$ has two marginals
bounded by Haar measure and lies on $n\in S$. Nevertheless almost
every corresponding affine ideal $n+qG=rG$ has zero normalized
Haar intersection with $S$. This defeats a proposed positive-fiber
return argument based only on those marginals, even for $q=n$.
It constructs no positive integer private endpoints: a typical
profinite $r$ has infinitely many prime divisors, and no comparison
between a numerical modulus and an integer witness is supplied.
