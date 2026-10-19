---
name: research/erdos_25/rank_and_moment_obstructions
desc: Rank and moment obstructions, sharp nonempty first-kill cell bounds, and unresolved entropy and additive-error targets.
tags: [open-questions, obstructions]
sources: []
created: 2026-09-22T00:05:00Z
updated: 2026-10-14T00:26:52Z
---


# research/erdos_25/rank_and_moment_obstructions

***

The [overlapping entropy obstruction](overlapping_entropy_obstruction.md)
strengthens the higher-moment failures below: overlapping first-kill
potentials need not be uniformly integrable, even for zero residues.
It does not refute the disjoint first-kill entropy bound.

These are bounds and counterexamples concerning intermediate estimates,
**not** a resolution of Problem 25. The first two obstructions use zero
residues; later constructions have the residues specified in their proofs.

## All individual divisor-face capacities still miss the difficulty

The finite proof in [bounded prime rank](bounded_prime_rank.md) uses the
constraints
$$
 \sum_{q:d\mid q,\ a_q\equiv b\ (d)}c_q\le\frac1d.
 \tag{1}
$$
For actual normalized first-kill harmonic masses these sharpen to
$$
 \sum_{q:d\mid q,\ a_q\equiv b\ (d)}c_q
 \le\frac{H_{\lfloor X/d\rfloor}}{dH_X}.
 \tag{2}
$$
Neither the full collection (2), nor primitivity and distinctness of the
moduli together with (2), implies a rank-independent small-footprint bound.

Choose disjoint finite prime groups $P_1,\ldots,P_r$ such that
$$
 1<c_j:=\sum_{p\in P_j}\frac1p\le2.
$$
They may all lie above any prescribed bound: take successive primes until
each reciprocal sum first exceeds $1$, using divergence of the prime
reciprocal sum. Let $D$ consist of all products selecting exactly one
prime from each group, with residue zero. These are distinct squarefree
moduli and form a primitive set. Their periodic union has density
$$
 \beta_r=\prod_{j=1}^r
 \left(1-\prod_{p\in P_j}(1-1/p)\right)
 \le(1-e^{-4})^r\longrightarrow0.
 \tag{3}
$$
Indeed $\log(1-1/p)\ge-2/p$ for every prime.

Nevertheless the weights
$$
 \lambda_q=\frac{1/q}{\prod_jc_j}
$$
have total mass $1$ and satisfy (1). If $d$ selects primes from the groups
indexed by $J$, direct factorization gives
$$
 \sum_{q:d\mid q}\lambda_q
 =\frac1d\prod_{j\in J}c_j^{-1}\le\frac1d.
$$
Other nonempty faces have zero mass. Put $Q=\max D$, $X=Q^3$, and
$c_q=\lambda_q/2$. For each relevant $d\le Q$,
$$
 \frac{H_{\lfloor X/d\rfloor}}{H_X}
 \ge\frac{\log(X/d)}{1+\log X}
 \ge\frac{2\log Q}{1+3\log Q}>\frac12
 \qquad(Q\ge3).
$$
Thus all the stronger capacities (2) hold, while $\sum_qc_q=1/2$ and
$\beta_r\to0$. These weights have **not** been realized as actual
first-kill masses. That missing realization is precisely why this is
not a counterexample to Problem 25.

The later [product-capacity obstruction](product_capacity_obstruction.md)
strengthens this failure: exact harmonic face capacities admit positive
abstract mass on vanishing-footprint families even with distinct primitive
moduli satisfying $\omega(q)\le3$. Large prime-power exponents replace
the increasing distinct-prime rank used above. These weights, too, are
not established as actual first-kill masses.

## Uniform higher moments of the natural first-kill potential fail

For a finite family, write
$$
 c_q(X)=\frac{H_{E_q}(X)}{H_X},\qquad
 Z_X(\omega)=\sum_q q c_q(X)\mathbf1_{[a_q]_q}(\omega).
$$
Its mean is $H_B(X)/H_X$ and its support has Haar measure $\beta$.
A uniform $L^2$ bound would give a square-root small-footprint estimate
by Cauchy--Schwarz. In fact there is no uniform $L^p$ bound for **any**
fixed $p>1$.

Here is an explicit sequence disproving such bounds. For an integer
$k\to\infty$, take successive primes greater than $k^3$, stopping when
their reciprocal sum first reaches $k$. Denote the resulting finite pool
by $P$, and put
$$
 L=\prod_{p\in P}p,\qquad
 D=\left\{\prod_{p\in S}p:S\subset P,\ |S|=k\right\},
 \qquad X=L^2.
$$
Use zero residues. Let $e_q=d(E_q)$ and
$P_0=\prod_{p\in P}(1-1/p)$, and let $N(\omega)$ count the primes of
$P$ dividing a Haar-random integer. Since
$$
 \sum_{p\in P}1/p=k+O(k^{-3}),\qquad
 \sum_{p\in P}1/p^2=O(k^{-2}),
$$
we have $P_0=e^{-k}(1+O(k^{-2}))$.

The event that exactly the $k$ primes constituting $q$ divide $\omega$
has $q$ as its unique divisor from $D$. It lies in the first-kill set
for $q$, regardless of the ordering. Therefore $qe_q\ge P_0$.
Each $E_q$ is exactly $L$-periodic on the positive integers; activation
causes no exception for zero residues. Summing over the $L$ blocks of
length $L$ up to $L^2$ gives
$$
 H_{E_q}(L^2)\ge e_qH_L,
 \qquad H_{L^2}\le2H_L.
$$
Consequently
$$
 Z_X\ge\frac{P_0}{2}\binom Nk.
 \tag{4}
$$

The probability needed to use (4) has an elementary estimate. Put
$y_p=1/(p-1)$ and $T=\sum_{p\in P}y_p=k+O(k^{-2})$.
For $m=k$ or $2k$,
$$
 \Pr(N=m)=P_0 e_m((y_p)_{p\in P})
 =(1+O(k^{-2}))e^{-k}\frac{k^m}{m!}.
 \tag{5}
$$
Indeed $m!e_m(y)/T^m$ is the probability that $m$ independent draws
with probabilities $y_p/T$ are all distinct. Its complement is at most
$\binom m2\max_p(y_p/T)=O(k^{-2})$.

On $N=2k$, (4), (5), and Stirling's formula yield
$$
 \mathbb E Z_X^2
 \ge(1+o(1))\frac{(4/e)^k}{8\pi^{3/2}k^{3/2}}
 \longrightarrow\infty.
$$
More generally, for each fixed $p>1$,
$$
 \mathbb E Z_X^p\gg_p
 \frac{(4/e)^{(p-1)k}}{k^{(p+1)/2}}\longrightarrow\infty.
$$
Thus fixed-exponent Hölder estimates cannot repair this particular
first-kill potential. Likewise
$\sum_q\kappa(q)c_q(X)$ is unbounded: here
$\kappa(q)=(1+o(1))2^k$ uniformly, while
$\sum_qc_q(X)\ge\Pr(N\ge k)/2\ge\Pr(N=k)/2$.

The exact zero-residue inequality $H_B(X)\le\beta H_X$ remains true
for every family in this example. Large moments of this potential do
not themselves indicate an actual harmonic-density anomaly.

### A four-prime certificate against the sharper second-moment charge

Section 9 of the [[research/erdos_25/independent/harmonic_capacity_and_narrow_windows|fourth independent record]]
gives a small exact example of the same overlapping-potential obstruction.
Put $h_q=H_{E_q}(X)$ and
$$
 V(\omega)=\sum_q qh_q\mathbf1_{[a_q]_q}(\omega).
$$
CRT gives
$$
 \mathbb EV=\sum_qh_q,\qquad
 \mathbb EV^2=\sum_{q,r}(q,r)
 \mathbf1_{a_q\equiv a_r\pmod{(q,r)}}h_qh_r.
$$
The proposed bound $\mathbb EV^2\le H_X\sum_qh_q$ would imply
the sharp harmonic inequality by Cauchy--Schwarz on the full union.
It fails already for zero residues at $2,3,5,7$, with $X=10$:
$$
 (h_2,h_3,h_5,h_7)
 =\left(\frac{137}{120},\frac49,\frac15,\frac17\right),
 \qquad \sum_qh_q=\frac{4861}{2520},\quad H_{10}=\frac{7381}{2520}.
$$
Here the first-kill sets are respectively
$\{2,4,6,8,10\},\{3,9\},\{5\},\{7\}$, so all coefficients
come directly from the exact activation rule. Since the primes are
distinct,
$$
 \mathbb EV^2
 =\left(\sum_qh_q\right)^2+\sum_q(q-1)h_q^2
 =\frac{862117}{151200},
 \qquad
 \mathbb EV^2-H_{10}\sum_qh_q
 =\frac{329873}{6350400}>0.
$$
This finite certificate was checked by rational arithmetic; the displayed
sets and identities also give a direct verification. It is a failure of
this charge, not of harmonic domination for zero residues. The preceding
construction already proves the stronger absence of any uniform
higher-moment bound for this potential.

## Disjoint first-kill potentials also have no uniform higher moment

Replacing the overlapping potential $Z_X$ by a disjoint one does not fix
the moment method. Let $F_q=C_q\setminus\bigcup_{r<q}C_r$ be the full
first-kill regions, with densities $e_q$, and consider
$$
 W_X=\sum_{e_q>0}\frac{c_q(X)}{e_q}\mathbf1_{F_q}.
$$
For every fixed $s>1$, $\mathbb E W_X^s$ is unbounded over finite
distinct-modulus singleton systems. The following construction is explicit.

Fix an integer $M\ge2$ and set $N=M^2$. For each prime $p$ and integer
$e\ge1$ with $p^e(p-1)\le N$, install all the classes
$$
 j p^{e-1}\pmod{j p^e},\qquad 1\le j\le p-1.
 \tag{6}
$$
All their moduli are at most $N$ and are distinct: their largest prime
factor is $p$, its exponent is $e$, and the remaining factor is $j<p$.
The full survivor set is exactly $L_N\mathbb Z$, where
$$
 L_N=\prod_{p(p-1)\le N}
 p^{\lfloor\log_p(N/(p-1))\rfloor}.
 \tag{7}
$$

To prove (7), analyze the classes by increasing $p$, and for a fixed $p$
by increasing $e$; this is only a proof ordering, not a change to the
eventual increasing-modulus enumeration. Earlier primes already force
divisibility by every $j<p$: if $\ell^v\mid j$, then
$\ell^v(\ell-1)\le(p-1)(p-2)<p(p-1)\le N$.
At the $e$th stage survivors are divisible by $p^{e-1}$. Their next
nonzero $p$-adic digit $j\in\{1,\ldots,p-1\}$ places them in precisely
the corresponding class (6), since they are also divisible by $j$.
The zero next digit avoids all these classes. This proves (7).

Now set $Q=N+1$, translate every old residue by $Q$, and append the class
$0\pmod Q$. The old full survivor set is $Q\pmod{L_N}$. All old moduli
are below $Q$, so every old congruence is active at the new endpoint $Q$,
which survives them all. At $X=Q$ the appended class has first-kill set
$\{Q\}$, hence $c_Q=1/(QH_Q)$. If $g=\gcd(Q,L_N)$, its full first-kill
density is $e_Q=g/(QL_N)$. Thus
$$
 \mathbb E W_Q^s
 \ge\frac{c_Q^s}{e_Q^{s-1}}
 =\frac{L_N^{s-1}}{Q g^{s-1}H_Q^s}
 \ge\frac{L_N^{s-1}}{Q^sH_Q^s}.
 \tag{8}
$$

Every prime power at most $M$ divides $L_N$, so
$L_N\ge\operatorname{lcm}(1,\ldots,M)\ge2^M/(M+1)$.
For the last elementary inequality, each $\binom Mk$ divides the lcm:
Legendre's valuation formula has at most $\lfloor\log_p M\rfloor$
nonzero summands, each at most one. The largest binomial coefficient is
at least $2^M/(M+1)$. Consequently (8) tends to infinity for every
$s>1$ while $Q=M^2+1$.

Again this is not a counterexample to Problem 25. It rules out uniform
fixed-exponent moment control even for a potential supported on disjoint
Haar first-kill regions. The substantial density cost of the old sieve
has not been converted into a logarithmic-density anomaly.

## A rank-sensitive additive target: now refuted

Distinctness gives a useful uniform truncation in total prime-factor rank.
For a finite singleton system, let $B_{>r}$ use only moduli with
$\Omega(q)>r$. Then
$$
\begin{aligned}
 H_{B_{>r}}(X)
 &\le H_{\lfloor X\rfloor}
       \sum_{\substack{q\le X\\\Omega(q)>r}}\frac1q\\
 &\le(3/2)^{-r}H_{\lfloor X\rfloor}
       \prod_{p\le X}(1-3/(2p))^{-1}
 \ll(3/2)^{-r}(\log(3X))^{5/2}.
\end{aligned}
\tag{9}
$$
The Euler-product estimate follows from
$(1-3/(2p))^{-1}(1-1/p)^{3/2}=1+O(p^{-2})$ and the already checked
Mertens product bound. With $r=\lceil8\log\log(3X)\rceil$, (9) is $O(1)$.

Consequently a uniform finite estimate
$$
 H_B(X)\le\beta H_{\lfloor X\rfloor}+C_r,
 \qquad \Omega(q)\le r,
 \qquad C_r=\exp(o(r)),
 \tag{10}
$$
would prove the full problem: apply it to the low-rank part, whose Haar
union has density at most $\beta$, and use (9) for the rest. Its total
error would be $o(\log X)$, uniformly over finite systems, permitting the
usual finite-truncation squeeze. A linear bound $C_r=O(r)$ would give
the stronger uniform error $O(\log\log X)$.

Estimate (10) is **refuted** by the
[energy counterexample](energy_counterexample.md#consequence-for-the-rank-sensitive-target).
That construction has harmonic excess
$\asymp(\log Q)^{1/21}$. Removing all moduli with
$\Omega(q)>r=\lceil8\log\log(3Q)\rceil$ loses only $O(1)$ harmonic
mass by (9), and can only decrease its Haar union measure. Thus any
universal additive constants for rank at most $r$ must satisfy
$$
 C_r\ge\exp\bigl((1/168+o(1))r\bigr)
$$
along the resulting sequence. In particular neither
$C_r=\exp(o(r))$ nor a uniform $O(\log\log X)$ additive error is
possible. The bounded-rank natural-density theorem makes no such
quantitative assertion and remains valid. A uniform additive
$o(\log X)$ comparison remains open.

## Entropy of the disjoint potential: an unresolved stronger target

The failure of every fixed $L^p$ bound does not rule out
$$
 \sum_i c_i(X)\log_+\frac{c_i(X)}{e_i}\le C
 \tag{11}
$$
with an absolute constant. No proof or counterexample to (11) was found.
It would settle the full problem: for a tail with Haar mass
$\eta=\sum_{i>k}e_i$ and harmonic mass $\alpha=\sum_{i>k}c_i(X)$,
the log-sum inequality gives
$$
 \alpha\log(\alpha/\eta)
 \le\sum_{i>k}c_i(X)\log\frac{c_i(X)}{e_i}\le C.
$$
As $\eta\to0$, this forces $\alpha\to0$ uniformly in $X$. Here zero-density
finite periodic first-kill cells are empty, so they never have positive
$c_i$. This is a conditional implication, not an estimate proved for
arbitrary residues.

### Averaging in harmonic time does not weaken the entropy target

Let $u=H_N$, and interpolate each first-kill harmonic sum linearly
between successive harmonic times. Denote it by $F_i(u)$, and put
$$
 c_i(u)=F_i(u)/u,\qquad
 K(u)=\sum_i c_i(u)\log_+\frac{c_i(u)}{e_i}.
$$
Terms with $e_i=0$ have $F_i=0$ and are omitted. The functions
$F_i$ are nondecreasing and $\sum_i c_i(u)\le1$. Thus, for
$v\ge u$, $c_i(v)\ge(u/v)c_i(u)$. Using monotonicity of
$x\log_+(x/e_i)$ and
$$
 \lambda x\log_+\frac{\lambda x}{e_i}
 \ge\lambda x\log_+\frac{x}{e_i}+\lambda x\log\lambda
 \quad(0<\lambda\le1),
$$
we obtain
$$
 K(v)\ge\frac uvK(u)-\frac uv\log\frac vu.
$$
For every $\Lambda>1$, integration gives the exact lower bound
$$
 \int_u^{\Lambda u}K(v)\,dv
 \ge u(\log\Lambda)K(u)-\frac u2(\log\Lambda)^2.
$$
Consequently an absolute averaged estimate
$\int_1^T K(v)\,dv\le CT+O(1)$ would imply
$$
 K(u)\le\frac{C\Lambda}{\log\Lambda}
                    +\tfrac12\log\Lambda+o(1).
$$
A constant pointwise bound trivially implies an averaged one. The two
targets are therefore equivalent up to constants: scale-averaging this
nonnegative information does not bypass the unproved constant entropy
estimate. No estimate for a different signed quantity was obtained.

### Valuation-measurable systems: a proved uniform bound

Suppose each full cylinder $C_i$ is determined by prime valuations.
This includes $a_i=0$ and, for even $q_i$, $a_i=q_i/2$, in any mixture.
For these systems,
$$
 W_X\le\frac{Z_X}{H_{\lfloor X\rfloor}},\qquad
 Z_X=\prod_{p\le X}(1-1/p)^{-1}.
 \tag{12}
$$
Restrict to the prefix $q_i\le X$, which does not change any earlier
first-kill cell. The independent geometric valuation model on primes
$p\le X$ assigns every $X$-smooth integer $n$ probability $1/(Z_Xn)$.
Because $F_i$ is valuation-measurable, its probability in this model is
exactly its Haar measure $e_i$. Since $E_i\subseteq F_i$,
$$
 H_{E_i}(X)\le Z_X\Pr(N\le X,\ N\in F_i)\le Z_Xe_i.
$$
This proves (12). The Euler-product estimate $Z_X\ll\log(2X)$, checked
in the Davenport--Erdős 1951 source as recorded above, makes (12) a
uniform $L^\infty$ bound. In particular (11) holds in these special
cases. The translated digit-sieve construction giving (8) is not
valuation-measurable.

### Removing $c_i$ from the logarithm destroys the target

The superficially stronger information estimate
$\sum_i c_i(X)\log(1/(q_i e_i))=O(1)$ is false even for zero residues.
Here is a finite construction with unbounded limiting value.

Choose primes $P$, all greater than $k^3$, whose reciprocal sum is
$2k+O(k^{-3})$, and take all products of $k$ distinct primes of $P$ as
zero-residue moduli. Let $P_0$ be an initial segment of $P$ with
reciprocal sum $k/2+O(k^{-3})$. The least active product dividing a Haar
integer is the product $q$ of its $k$ smallest dividing primes of $P$.
Consequently
$$
 q e_q=\prod_{\substack{p\in P,\ p<\max(q)\\p\nmid q}}(1-1/p).
$$
The independent prime-divisibility counts have variances at most their
means. Chebyshev therefore shows that, with probability $1-O(1/k)$,
fewer than $k$ primes of $P_0$ but at least $k$ primes of $P$ divide the
integer. On this event, $\max(q)$ is beyond $P_0$ and
$$
 \log\frac1{q e_q}
 \ge\sum_{\substack{p\in P_0\\p\nmid q}}\frac1p
 \ge k/2-O(k^{-2}),
$$
because at most $k$ selected primes were removed from that sum and
each exceeds $k^3$. Hence
$$
 \sum_q e_q\log\frac1{q e_q}\ge k/2-O(1).
$$
For each fixed finite system $c_q(X)\to e_q$, giving the asserted
counterexample to the stronger information estimate. It does not
contradict (11); in fact (12) applies to every one of these systems.

### Sharp growth of the Haar-weighted information

The preceding quantity has a sharp asymptotic maximum. For a finite
distinct-modulus singleton family with all $q\le Q$, put
$$
 I=\sum_q e_q\log\frac1{qe_q},
$$
with zero summands when $e_q=0$. Then, as $Q\to\infty$,
$$
 \log\log Q-O((\log\log Q)^{2/3})
 \le \sup I\le \log H_{\lfloor Q\rfloor}+1/e.
 \tag{H}
$$
Thus $\sup I=(1+o(1))\log\log Q$. The lower bound already uses
zero residues. This is a statement about Haar masses $e_q$, not the
arithmetic masses $c_q(X)$ in the unresolved target (11).

For the upper bound let $\beta=\sum_qe_q\le1$. If $\beta>0$, the
log-sum inequality and distinctness give
$$
 I\le\beta\log\frac{\sum_q1/q}{\beta}
 \le\beta\log H_{\lfloor Q\rfloor}-\beta\log\beta
 \le\log H_{\lfloor Q\rfloor}+1/e.
$$
The case $\beta=0$ is immediate.

For the lower bound put
$$
 L=\log\log Q,\qquad
 k=\lfloor L-2L^{2/3}\rfloor,\qquad z=Q^{1/k},
$$
and use every product of $k$ distinct primes from
$P=\{p:k^3<p\le z\}$, with residue zero. These moduli are distinct
and at most $Q$. The elementary prime reciprocal estimates already
used in these notes give
$$
 \lambda:=\sum_{p\in P}\frac1p
 =L-\log k-\log(3\log k)+O(1)
 \ge k+k^{2/3}
$$
for sufficiently large $Q$. Choose an initial prime segment
$P_0\subset P$ with reciprocal sum
$k-k^{2/3}+O(k^{-3})$. Under Haar measure, prime divisibility is
independent and each count has variance at most its mean.
Chebyshev's inequality shows that, with probability
$1-O(k^{-1/3})$, fewer than $k$ primes of $P_0$ but at least
$k$ primes of $P$ divide the sampled point.

Its first-kill modulus $q$ is then the product of its $k$ smallest
dividing primes of $P$. Writing $P^+(q)$ for the largest prime
factor, its exact first-kill mass satisfies
$$
 qe_q=\prod_{\substack{p\in P,\ p<P^+(q)\\p\nmid q}}(1-1/p).
$$
On the indicated event $P^+(q)$ exceeds every prime of $P_0$.
At most $k$ primes of $P_0$ divide $q$, each greater than $k^3$.
Consequently
$$
 \log\frac1{qe_q}
 \ge\sum_{\substack{p\in P_0\\p\nmid q}}\frac1p
 \ge k-k^{2/3}-O(k^{-2}).
$$
The logarithm is nonnegative on every other first-kill cell. Integrating
therefore gives $I\ge k-O(k^{2/3})=L-O(L^{2/3})$, proving (H).
Zero residues make activation exact: every positive multiple of $q$
is already at least $q$.

This rules out a constant Haar-information bound and identifies its
correct growth. Its universal $o(\log Q)$ bound does not establish
an $o(\log X)$ arithmetic excess, or resolve (11).

### Coherence does not give a uniform bound for the disjoint potential

There is no absolute $L^\infty$ bound for $W_X$, even for coherent
prime-modulus systems. This does not refute a uniform finite-$L^p$
bound restricted to coherent systems, or the entropy target (11).

Choose a finite admissible $S\subseteq[1,T]$ with
$H_S=\sum_{s\in S}1/s$ arbitrarily large. The elementary construction
of such sets is proved in
[finite sharp counterexamples](finite_sharp_counterexamples.md#admissible-sets-with-large-harmonic-weight).
Choose a prime $q>T$. For every prime $p<q$, let $r_p$ be a residue
omitted by $S\bmod p$, and choose a common center by CRT with
$$
 \alpha\equiv qr_p\pmod p\quad(p<q),\qquad
 \alpha\equiv0\pmod q.
$$
Install all prime moduli up to $q$. Every $qs$, $s\in S$, is first
killed by $q$: it avoids each earlier prime class because $q$ is
invertible modulo that prime. All these hits are active.
For $X=qT$,
$$
 c_q(X)\ge\frac{H_S}{qH_{qT}},\qquad
 e_q=\frac1{qZ_{q^-}},\qquad
 Z_{q^-}=\prod_{p<q}(1-1/p)^{-1}\ge H_{q-1}.
$$
The last bound follows by expanding the Euler product: every integer
at most $q-1$ occurs. Since $T<q$ and $H_{q^2}\le2H_q$,
$$
 \frac{c_q(X)}{e_q}\ge\frac{H_S}{4}.
$$
The nonempty $q$th first-kill cell has positive Haar measure, so this
proves the asserted failure of uniform $L^\infty$ control. Its small
measure prevents this calculation from establishing a moment or
entropy obstruction.

## Size of a nonempty first-kill cell

**Proved.** There is an absolute constant $C$ such that every nonempty
full first-kill cell at modulus $q$ in a distinct-modulus singleton
system satisfies
$$
 q e_q\ge \exp(-C\sqrt q).
 \tag{13}
$$
The exponent order $\sqrt q$ is sharp. This is a pointwise size bound,
not a summable entropy or activated trace estimate.

First consider any nonempty survivor set formed by singleton moduli at
most $N$. Set
$$
 y=2\sqrt N,\qquad
 L=\prod_{p\le y}p^{\lfloor\log_pN\rfloor}.
$$
The elementary prime-counting bound gives
$\log L\le\pi(y)\log N=O(\sqrt N)$, with bounded $N$ absorbed in
the constant. Fix the residue modulo $L$ of one surviving point.
All conditions at moduli supported on primes at most $y$ are now
avoided. Every other modulus is $pm$ for a unique prime $p>y$, with
$m\le N/p<y$. Its small-prime part is fixed, so it either imposes
no condition or excludes one digit modulo $p$.

Distinctness allows at most $\lfloor N/p\rfloor$ such excluded
digits. Different large prime coordinates are independent. Since
$N/p^2<1/4$, the full surviving Haar measure is at least
$$
 \frac1L\prod_{y<p\le N}(1-N/p^2)
 \ge\frac1L\exp\left(-\frac43N\sum_{n>y}\frac1{n^2}\right)
 \ge\exp(-C\sqrt N).
 \tag{14}
$$
This proves the corresponding lower bound for any nonempty survivor set.

For a nonempty $F_q$, run the same argument with $N=q$ inside
$C_q=[a_q]_q$, choosing a point of $F_q$ to fix the small-prime
digits. The chosen fiber has conditional measure at least $1/L$.
Any large prime dividing $q$ is already fixed; all earlier conditions
at that prime are avoided, since the chosen point survives them.
The remaining large primes obey the same product bound. The resulting
conditional survival probability is $qe_q$, proving (13).

For sharpness, the translated digit sieve proved above has
$q=M^2+1$ and
$$
 qe_q=\frac{\gcd(q,L_{M^2})}{L_{M^2}}
 \le q(M+1)2^{-M}\le\exp(-c\sqrt q)
$$
for all sufficiently large $M$, with an absolute $c>0$.
Thus a uniformly better exponent order is impossible. Summing the
pointwise consequence $\log(1/(qe_q))\ll\sqrt q$ gives no useful
uniform bound on the actual first-kill entropy; that global question
remains open.

## A small exponential rank error: later refuted

**Superseded target.** The [prime-only amplification](prime_additive_excess.md)
proves that the additive excess is unbounded even for $\Omega(q)=1$.
Thus no finite rank-only additive error exists, irrespective of its
growth with rank. The sufficiency calculation below is logically correct but has
a false hypothesis; it records an approach that this obstruction rules out, not
an open target.

Before the prime-only strengthening, the subexponential obstruction
left the following possibility. For fixed $1<z<2$, the proof of (9)
gives the valid, more flexible truncation bound
$$
 H_{B_{>r}}(X)
 \ll_z z^{-r}(\log(3X))^{z+1}.
 \tag{15}
$$
Indeed $\sum_{q\le X}z^{\Omega(q)}/q$ is at most
$\prod_{p\le X}(1-z/p)^{-1}\ll_z(\log(3X))^z$; comparison
of local factors with $(1-1/p)^{-z}$ proves the final estimate.

Consequently the following **now-refuted** finite additive bound
$$
 H_B(X)\le\beta H_{\lfloor X\rfloor}+O(e^{cr})
 \quad\text{when }\Omega(q)\le r,
 \qquad 0<c<\tfrac12\log2,
 \tag{16}
$$
would settle the full problem if true with an implied constant
independent of $r$, $X$, and the family. Choose $z<2$ sufficiently close
to $2$ that $c<\log z/z$, then choose
$z/\log z<a<1/c$ and take $r=\lceil a\log\log(3X)\rceil$.
Equation (15) is $o(\log X)$ because $a\log z>z$, and the error
in (16) is $o(\log X)$ because $ac<1$. The low-rank Haar footprint
is no larger than the whole footprint, so finite approximation gives
the conditional conclusion.

This identifies a range not excluded by the lower bound
$C_r\ge\exp((1/168+o(1))r)$. The prime-only construction excludes that entire
range: even the rank-one additive constant is infinite.
The constant coprime entropy theorem is a different statement and
remains valid.
