---
name: research/erdos_25/overlapping_parent_preparations
desc: Positive-measure singleton preparations with moduli at most z and harmonic traces from z squared; the arithmetic refinement remains open.
tags: [constructions, conditioned-tails, partial-results]
sources: []
created: 2026-09-22T09:25:34Z
updated: 2026-09-24T22:13:01Z
---


# research/erdos_25/overlapping_parent_preparations

***

## A finite preparation lemma: proved

Let $\mathcal P$ be the odd primes at most $z$, and put
$$
 \lambda=\sum_{p\in\mathcal P}\frac1p,\qquad
 k=\lfloor\lambda\rfloor,\qquad
 r=\lfloor2\lambda-2\sqrt\lambda\rfloor.
$$
As $z\to\infty$, there is a finite singleton sieve whose distinct
moduli are squarefree products of $k$ primes of $\mathcal P$, with
full survivor set $S$, and a measurable set $G\subseteq S$ such that
$$
 \mu(G)\ge\tfrac12-o(1).
 \tag{1}
$$
Each $x\in G$ belongs to a parent cylinder $C(x)$ whose modulus is
a product of $r$ primes of $\mathcal P$, and
$$
 \frac{\mu(S\cap C(x))}{\mu(C(x))}\le e^{-3\lambda/2}.
 \tag{2}
$$

The parents are auxiliary cylinders, not installed congruences. They
can overlap and can have the same modulus with different residues.
The actual preparatory sieve uses at most one residue per modulus.
Thus (1)--(2) establish a concrete heavily overlapping preparation,
outside the disjoint-parent bounds in
[prepared-block entropy](prepared_blocks_entropy.md).
They do **not** construct the later singleton congruences needed for a
counterexample.

## Random singleton preparation

Define
$$
 R(x)=\#\{p\in\mathcal P:x\bmod p\in\{0,1\}\},\qquad
 T=\{|R-2\lambda|\le2\sqrt\lambda\}.
$$
Haar independence gives $\mathbb ER=2\lambda$ and
$\operatorname{Var}R\le2\lambda$, so $\mu(T)\ge1/2$.
Put
$$
 b=\lceil2\lambda+4\sqrt\lambda\rceil,\qquad
 B=\binom bk.
$$
For each $k$-element subset $J\subseteq\mathcal P$, independently
install its product modulus with probability $2^k/B$, and, if
installed, choose its CRT digits independently and uniformly in
$\{0,1\}$ at the primes of $J$. Since $b\ge2k$,
$\binom bk\ge2^k$, so this is a valid probability.

For a fixed $x$, precisely $\binom{R(x)}k$ subsets could hit it.
Each hits with probability $1/B$, independently over subsets.
Therefore the exact probability of surviving the random preparation is
$$
 f(R(x))=\left(1-\frac1B\right)^{\binom{R(x)}k}.
 \tag{3}
$$
On $T$,
$$
 1-f(R(x))
 \le\frac{\binom{R(x)}k}{B}
 \le(3/4)^{2\sqrt\lambda-1}=o(1)
 \tag{4}
$$
for sufficiently large $\lambda$. For the last bound, increase the
upper binomial argument from $R(x)$ to $b$ one step at a time:
each reverse ratio is at most $3/4$, and there are at least
$2\sqrt\lambda-1$ steps.

## Conditional survival in every parent

A parent $C$ fixes $r$ success coordinates and their $0/1$
values. Under Haar law conditioned on $C$,
$$
 R=r+V,\qquad
 \mathbb EV=2\lambda-O(\log\lambda),
 \tag{5}
$$
uniformly over the parent. Indeed the removed reciprocal sum is at
most $H_{r+2}$, even if the chosen primes are the smallest available.

The elementary exponential-moment bound for this sum of independent
Bernoulli variables gives
$$
 \Pr(V<12\sqrt\lambda)
 \le\exp\{-2\lambda+O(\sqrt\lambda\log\lambda)\}.
 \tag{6}
$$
For example use
$\Pr(V<t)\le u^{-t}\mathbb E u^V
\le u^{-t}\exp(-(1-u)\mathbb EV)$, with
$u=\lambda^{-1/2}$ and $t=\lceil12\sqrt\lambda\rceil$.
Above that cutoff, $r+V$ exceeds $b$ by at least
$5\sqrt\lambda$, for large $\lambda$. In the first that many
binomial-ratio steps each ratio is at least $4/3$. Thus
$$
 \frac{\binom{r+V}k}{B}\ge(4/3)^{5\sqrt\lambda},
 \qquad
 f(r+V)\le\exp\{-(4/3)^{5\sqrt\lambda}\}.
$$
Integrating (3) over the parent, and using (6), proves
$$
 \mathbb E_{\rm sieve}
     \frac{\mu(S\cap C)}{\mu(C)}
 \le\eta_\lambda
 :=\exp\{-2\lambda+O(\sqrt\lambda\log\lambda)\},
 \tag{7}
$$
uniformly over all parents.

For each $x\in T$, choose $C(x)$ deterministically before sampling
the sieve, for example by taking its $r$ smallest success primes.
Markov's inequality and (7) give
$$
 \mathbb E_{\rm sieve}\mu\left\{x\in T:
       \frac{\mu(S\cap C(x))}{\mu(C(x))}>e^{-3\lambda/2}\right\}
 \le\eta_\lambda e^{3\lambda/2}=o(1).
 \tag{8}
$$
Equation (4) also gives
$\mathbb E_{\rm sieve}\mu(T\setminus S)=o(1)$.
Choose a realization with the sum of these two defects at most its
expectation. The remaining part of $T$ is the claimed $G$.
In particular, no union bound over the very numerous parents is used.

## Activated arithmetic version

Fix integers $X\ge2Q$ and $Q\ge z^{r+1}$ before sampling the sieve.
The realization can be chosen to satisfy (1)--(2) and additionally
$$
 \frac{\sum_{n\in G\cap[Q,X]}1/n}{\sum_{Q\le n\le X}1/n}
 \ge\tfrac12-o(1).
 \tag{9}
$$

To verify this, set $s=|\mathcal P|$. Direct CRT counting of the
one-prime and two-prime conditions gives, for every $Y\ge1$,
$$
 \sum_{n\le Y}(R(n)-2\lambda)^2
 =Y\sum_{p\in\mathcal P}(2/p-4/p^2)+O(s^2).
 \tag{10}
$$
The mean-count error contributes $O(\lambda s)$, which is included
in $O(s^2)$. Partial summation on $[Q,X]$ and Chebyshev put at
least $1/2-o(1)$ of its normalized harmonic measure on $T$:
the normalized error is
$O(s^2/(\lambda Q\sum_{Q\le n\le X}1/n))=o(1)$.

The estimates (4) and (7)--(8) hold after replacing Haar sampling of
$x$ by any fixed probability measure, because the conditional-parent
expectation is uniform and $C(x)$ is fixed in advance. Apply them
simultaneously to Haar measure and to this normalized harmonic
measure, then choose a realization whose sum of all four bad masses
is at most its expectation. This proves (9).

All installed moduli are at most $z^k<Q$, and all parent moduli are
at most $z^r<Q$, for large $z$. Hence every preparatory class is
active at all integers counted in (9). The installed distinct moduli
can be ordered strictly increasingly. The realization may depend on
$Q,X$; no simultaneous-in-$X$ assertion is made.

## A quantified obstruction to the missing refinement

Any appended modulus refining a parent has at least $r$ distinct
prime factors from $\mathcal P$. Let
$$
 D_r=\{q:\omega_{\mathcal P}(q)\ge r\},\qquad
 \beta_r=\Pr\left(\sum_{p\in\mathcal P}
                     {\rm Bernoulli}(1/p)\ge r\right).
$$
The full multiples union generated by $D_r$ has measure $\beta_r$.
Chernoff's inequality at the parameter $\log2$ gives
$$
 \beta_r\le2^{-r}\prod_{p\in\mathcal P}(1+1/p)
 \le\exp\{-(2\log2-1)\lambda+O(\sqrt\lambda)\}.
 \tag{11}
$$
For arbitrary singleton appended residues, distinctness and the
exact multiples harmonic inequality imply
$$
 \frac{H_{\text{hits with positive quotient }t\le K}(X)}{H_X}
 \le H_{\lfloor K\rfloor}
       \frac{\sum_{q\le X,\ q\in D_r}1/q}{H_X}
 \le H_{\lfloor K\rfloor}\beta_r.
 \tag{12}
$$
Consequently a fixed positive harmonic deletion cannot be obtained
from bounded quotients, or even from quotient ranges with
$$
 \log K\le
 \exp\{(2\log2-1-\varepsilon)\lambda\}
$$
for a fixed $\varepsilon>0$ and large $\lambda$.

The open step is to choose distinct appended moduli whose many active
progression points remain in the protected arithmetic survivors,
while their total additional conditional Haar footprint tends to
zero. The preparation lemma proves neither that step nor a logarithmic
density counterexample. It shows why restricting to disjoint parents
does not exhaust possible preparations.

## Product truncation lowers the preparatory activation scale

The preparation can be strengthened: all installed moduli may be at most
$z$, all parents have modulus below $z^2$, and (9) already holds on
$[Q,X]$ for $Q=\lceil z^2\rceil$ and any chosen $X\ge2Q$.
The realization may depend on $X$. Replace the parameters by
$$
 k=\lfloor\lambda\rfloor,\quad y=z^{1/k},\quad
 r=\lfloor2\lambda-6\sqrt\lambda\rfloor,
 \quad b=\lceil2\lambda+4\sqrt\lambda\rceil,\quad B=\binom bk.
 \tag{13}
$$
Take $z$ large enough that $k,r>0$. Independently install each
$k$-element prime subset $J$ **only when**
$\prod_{p\in J}p\le z$, with the same probability $2^k/B$
and uniform $0/1$ CRT digits. An eligible subset hits a compatible
point with probability $1/B$.

Write $R_I(x)$ for its number of success primes in $I$, and set
$$
 T_0=\{|R_{[3,z]}-2\lambda|\le2\sqrt\lambda,\
                          R_{(y,z]}\le\sqrt\lambda\}.
 \tag{14}
$$
The elementary prime-counting upper bound and partial summation give
$$
 \sum_{y<p\le z}\frac1p
 \ll1+\log\frac{\log z}{\log y}
 =O(\log(2k))=O(\log\lambda).
 \tag{15}
$$
Haar Chebyshev for the first condition and Markov for the second give
$\mu(T_0)\ge\tfrac12-o(1)$.

The same holds for normalized harmonic measure $\nu$ on $[Q,X]$.
With $s=\#\mathcal P$, the CRT identity (10) and partial summation give
$$
 \mathbb E_\nu(R_{[3,z]}-2\lambda)^2
 \le2\lambda+O\!\left(\frac{s^2}{QH_{[Q,X]}}\right)
 =2\lambda+O(1),
$$
where $H_{[Q,X]}=\sum_{Q\le n\le X}1/n\gg1$. Similarly,
$$
 \mathbb E_\nu R_{(y,z]}
 =2\sum_{y<p\le z}\frac1p+
                    O\!\left(\frac{s}{QH_{[Q,X]}}\right)
 =O(\log\lambda).
$$
Thus $\nu(T_0)\ge\tfrac12-o(1)$.

Every $x\in T_0$ has at least $2\lambda-3\sqrt\lambda$ success
primes at most $y$. Choose $r$ of them deterministically as its
parent $C(x)$, before sampling the sieve. Its modulus satisfies
$$
 d\le y^r=z^{r/k}<z^2.
 \tag{16}
$$
Product truncation only decreases the old deletion bound:
$$
 \Pr(x\notin S)\le\frac{\binom{R_{[3,z]}(x)}k}{B}
 \le(3/4)^{2\sqrt\lambda-O(1)}=o(1)
 \qquad(x\in T_0).
 \tag{17}
$$

Conditioned on any such low-prime parent,
$$
 R_{[3,y]}=r+V,\qquad
 \mathbb EV=2\lambda-O(\log\lambda).
 \tag{18}
$$
Here (15) accounts for the omitted large primes, while the reciprocal
sum of the $r$ fixed primes is $O(\log(r+2))$.
The exponential-moment argument in (6), now with cutoff
$15\sqrt\lambda$, gives
$$
 \Pr(V<15\sqrt\lambda)
 \le\exp\{-2\lambda+O(\sqrt\lambda\log\lambda)\}.
 \tag{19}
$$
Above that cutoff, $r+V$ exceeds $b$ by at least
$5\sqrt\lambda-O(1)$. Every $k$-subset of these low successes
is eligible, since its product is at most $y^k=z$. Independence
and the binomial-ratio estimate therefore give
$$
 \mathbb E_{\rm sieve}\mathbf1_S(x)
 \le\left(1-\frac1B\right)^{\binom{r+V}k}
 \le\exp\{-(4/3)^{5\sqrt\lambda-O(1)}\}.
 \tag{20}
$$
Integrating over the parent and using (19) proves the uniform bound
$$
 \mathbb E_{\rm sieve}\frac{\mu(S\cap C)}{\mu(C)}
 \le\exp\{-2\lambda+O(\sqrt\lambda\log\lambda)\}.
 \tag{21}
$$

Apply Markov at threshold $e^{-3\lambda/2}$ in (21), and integrate
over the predetermined parents $C(x)$, separately against Haar
measure and $\nu$. Together with (17), the sum of all four expected
bad masses is $o(1)$. Choose a realization with that sum at most its
expectation and retain
$$
 G=\{x\in T_0\cap S:
          \mu(S\cap C(x))/\mu(C(x))\le e^{-3\lambda/2}\}.
$$
Then
$$
 \mu(G)\ge\tfrac12-o(1),\qquad \nu(G)\ge\tfrac12-o(1).
 \tag{22}
$$
This proves the strengthened preparation.

Every installed modulus is a distinct squarefree $k$-fold prime
product at most $z$, so all preparatory congruences are active on
$[Q,X]$ and can be ordered strictly increasingly. The parents remain
auxiliary, potentially overlapping cylinders, not repeated installed
congruences. A distinct appended refinement giving a fixed positive
normalized harmonic anomaly has still not been constructed.

The later [bounded-overlap refinement theorem](parent_refinement_overlap.md)
rules out this missing step at every cutoff if the appended refinements
have subexponential overlap within each parent and exponentially small
incremental footprint. Its low-success-count comparison with the actual
preparatory survivors requires no overlap assumption. The unresolved
case is the conversion of a raw sum of conditional cylinder masses to
their union measure when in-parent overlap is unrestricted.

## Lower-rank parents: another proved preparation

The choice of parent rank near $2\lambda$ is not forced. There
is a weaker conditional-survival estimate with parents of rank
$k=\lfloor\lambda\rfloor$, which avoids the exponentially
sparse modulus-support condition of the rank-$2\lambda$ version.
It is still only a preparation, not a counterexample.

Keep the product-truncated random sieve and the parameters $k,y,b,B$
from (13), but choose a parent using exactly $k$ success primes
at most $y$, rather than $r$ of them. Every point of $T_0$
has enough such primes, and this parent has modulus at most
$y^k=z$. Uniformly over all these parents,
$$
 \mathbb E_{\rm sieve}\frac{\mu(S\cap C)}{\mu(C)}
 \le\exp\{-(1-\log2)\lambda+O(\sqrt\lambda)\}.
 \tag{23}
$$
Indeed, conditioned on the parent, the number of low-prime successes
is $k+V$, with $\mathbb EV=2\lambda-O(\log\lambda)$.
The Bernoulli exponential-moment bound gives, for a fixed sufficiently
large absolute $A$,
$$
 \Pr(V\le\lambda+A\sqrt\lambda)
 \le2^{\lambda+A\sqrt\lambda}\mathbb E2^{-V}
 \le\exp\{-(1-\log2)\lambda+O(\sqrt\lambda)\}.
$$
Above this cutoff, $k+V$ exceeds the binomial threshold $b$
by at least $5\sqrt\lambda$, after increasing $A$.
All $k$-subsets of these low-prime successes have product at most
$z$, so the same binomial-ratio calculation as (20) makes the
conditional random-survival probability at most
$\exp\{-(4/3)^{5\sqrt\lambda-O(1)}\}$. Integrating proves (23).

For each point of $T_0$, fix its parent before sampling the sieve
by taking its $k$ smallest success primes at most $y$, with
their actual 0/1 digits. This is a finite-coordinate measurable rule.
Markov's inequality at threshold
$\exp(-(1-\log2)\lambda/2)$, together with (17), gives a
realization with a set $G\subseteq S\cap T_0$ satisfying
$$
 \mu(G)\ge\tfrac12-o(1),\qquad
 \nu(G)\ge\tfrac12-o(1),\qquad
 \frac{\mu(S\cap C(x))}{\mu(C(x))}
 \le e^{-(1-\log2)\lambda/2}\quad(x\in G),
 \tag{24}
$$
where $\nu$ is the chosen harmonic measure on $[z^2,X]$
from the product-truncation argument. Its uniform expectation proof
allows Haar and $\nu$ to be imposed simultaneously exactly as
before. All actual preparatory moduli remain distinct and at most
$z$; the parents are auxiliary and may overlap.

The rank threshold $k\approx\lambda$ no longer supplies an
exponentially small Chernoff bound for the reciprocal support of
possible refined moduli. Also a typical point can lie in roughly
$\binom{2\lambda}{\lambda}$ parents, rather than the
subexponential number in the rank-$2\lambda$ construction. Thus
the [new weighted and overlap obstructions](weighted_divisibility_moments.md)
do not apply with their vanishing errors unchanged. No distinct
refinements with a fixed harmonic anomaly and small incremental
union footprint have been obtained from (24). The difficulty is
controlling the union over a full logarithmic epoch, not merely
finding one parent of small conditional survivor measure.

### Status of mixed-root and coding attempts

The last construction attempts used the lower-rank parents above,
and also intermediate parent ranks between $\lambda$ and
$2\lambda$. No assignment of distinct appended moduli was found
that both removes a fixed positive normalized harmonic mass over an
epoch and has vanishing incremental Haar **union** measure. The
proved single-parent rarity estimates do not supply that union
estimate. This is a missing step, not an impossibility theorem for
these lower-rank constructions.

For mixed 0/1 residues, the exact identity available at any hit is
$$
 a_q^2\equiv a_q\pmod q,\quad n\equiv a_q\pmod q
 \quad\Longrightarrow\quad q\mid n(n-1).
$$
This permits attempts to encode choices among divisors of
$n(n-1)$. But separating codes for divisibility-comparable
moduli does not exclude a different, incomparable divisor from
covering the same integer. Neither a bound for these cross-scale
collisions nor a private canonical witness construction was proved.
Also, the size of $n(n-1)/q$ does not by itself control its number
of old prime factors: selecting idempotent roots can bias that
cofactor. No typical-prime-factor heuristic for it is used in
(23)--(24) or in any claimed theorem.

## Limits of endpoint accounting and asymmetric colors

The subsequent construction attempt did not produce the missing
overlapping refinements. Two precise restrictions on its proposed
accounting can be retained.

First, if one selected integer $n_q\ge q$ is assigned to each
distinct modulus, and the selected endpoints have harmonic mass at least
$cH_X$, then
$$
 \sum_{q\le X}\frac1q
 \ge\sum_{n_q\le X}\frac1{n_q}\ge cH_X.
 \tag{25}
$$
Thus an upper certificate using only
$\mu(S\cap C_q)\le\eta/q$ and then summing these bounds cannot
tend to zero unless $\eta H_X\to0$. This is a limitation of that
certificate, **not** a lower bound for the actual incremental union.
The lower-rank preparation's available exponent in (24) does not meet
this requirement over an epoch starting at $z^2$. Smaller actual
cell masses or coordinated overlap could still change the situation.

Second, consider a finite pool of odd primes, with allowed success digits
$E_p=\{0\}$ or $\{0,1\}$. Suppose every preparatory modulus is
squarefree and its prescribed digits belong to these sets. Let a parent
$C$ fix success digits at a subset $J$ of the pool. If
$S\cap C\ne\varnothing$, then
$$
 \mu(S\mid C)\ge
       \prod_{p\notin J}(1-|E_p|/p).
 \tag{26}
$$
Indeed, points in $C$ with nonsuccess digits at every pool prime
outside $J$ avoid all preparatory classes using such a prime. Any
remaining preparatory class hitting such a point would use only primes
in $J$, and would then contain the whole parent, contrary to its
nonempty intersection with $S$. Independence proves (26).

Writing $\lambda=\sum_p1/p$ and
$\lambda_1=\sum_{p:E_p=\{0,1\}}1/p$, the convergent quadratic
error in the logarithm of this product gives the weaker uniform bound
$$
 \mu(S\mid C)\ge\exp(-\lambda-\lambda_1-O(1)).
$$
This does not control unions of overlapping parents. The attempted
asymmetric-color variation supplied no rigorous improvement of their
total incremental footprint; heuristic exponent balances are not used
as an impossibility theorem here.

Simply enlarging polynomial epochs also did not evade the existing
[weighted bound](weighted_divisibility_moments.md): for the rank
$2\lambda-o(\lambda)$ parents, it already extends to
$\log X\le\exp((1+2\log2-\varepsilon)\lambda)$.
No new counterexample mechanism or general exclusion was proved.
