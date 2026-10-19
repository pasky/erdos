---
name: research/erdos_25/probabilistic_smoothing
desc: Exact convergence for exponential-clock smoothing, and obstructions to random thinning and random-order charges.
tags: [probability, obstructions, partial-results]
sources: []
created: 2026-09-22T02:51:13Z
updated: 2026-09-24T22:13:01Z
---


# research/erdos_25/probabilistic_smoothing

***

This approach randomizes the sieve rather than estimating its original
first-kill cells. Smoothing gives a strong convergence theorem, but the
passage back to the unsmoothed union remains unproved. Two explicit
obstructions explain why basic thinning and random reordering do not
remove the difficulty.

## Summable clocks: proved convergence

For the full cylinders $C_q=[a_q]_q$, choose positive rates such that
$$
 S=\sum_q\lambda_q/q<\infty.
$$
Distinctness permits the universal choice
$\lambda_q=(1+\log q)^{-2}$. For a common translation $z\in G=
\widehat{\mathbb Z}$, define
$$
 W_n(z)=\sum_{q\le n}\lambda_q\mathbf1_{C_q}(n-z),\qquad
 W(\omega)=\sum_q\lambda_q\mathbf1_{C_q}(\omega).
$$
The Haar random variable $W$ is integrable, with mean $S$.

**Theorem.** The law of $W_n(z)$ under harmonic sampling
$\Pr(n)=1/(nH_N)$, $1\le n\le N$, converges to the Haar law of $W$
in $1$-Wasserstein distance, uniformly in $z$. The same assertion holds
for uniform sampling on $[1,N]$.

**Proof.** Truncate both potentials to $q\le K$. On the integer side,
the harmonic $L^1$ error is at most
$$
 \frac1{H_N}\sum_{q>K}\lambda_q H_{B_{q,z}}(N)
 \le\sum_{q>K}\lambda_q/q,
$$
because $H_{B_{q,z}}(N)\le H_{\lfloor N/q\rfloor}/q$. The Haar $L^1$
error is exactly the same tail sum. These bounds are uniform in $z$.
The truncated integer potential is eventually periodic. Its distribution
converges to its Haar distribution uniformly over the finitely many
possible translations modulo the fixed common period. The triangle
inequality for $1$-Wasserstein distance proves the result. Equivalently,
apply the same estimates to every $1$-Lipschitz test function.
The uniform-sampling version uses $|B_{q,z}\cap[1,N]|\le N/q$.
$\square$

In particular, for every fixed $t\ge0$,
$$
 \frac1{H_N}\sum_{n\le N}\frac{1-e^{-tW_n(z)}}n
 \longrightarrow\int_G(1-e^{-tW})\,d\mu,
 \tag{1}
$$
uniformly in the common translation.

This has an exact clock interpretation: independently retain class $q$
when an exponential clock of rate $\lambda_q$ rings before $t$.
An integer with active potential $W_n(z)$ is deleted with probability
$1-e^{-tW_n(z)}$. For fixed $t$, the expected reciprocal sum of retained
moduli is at most $tS$, hence that sum is finite almost surely. Every
fixed-time random sieve therefore has natural density by the summable
case.

### The unresolved limit is an atom, not a convergence theorem for the clocks

Let $\beta=\mu(\bigcup_qC_q)$. Positivity of all rates gives
$$
 \mu(W=0)=1-\beta,\qquad
 \mathbf1_{B_z}(n)=\mathbf1_{\{W_n(z)>0\}}.
$$
Thus taking $t\to\infty$ in (1) asks for convergence at the possible
atom $0$ of the limiting distribution. Wasserstein convergence does not
control this: the constants $1/N$ converge to $0$ in that distance,
although their probabilities of being positive are all one.

For fixed $t$ the exact omitted mass is
$$
 \frac1{H_N}\sum_{\substack{n\le N\\W_n(z)>0}}
             \frac{e^{-tW_n(z)}}n.
$$
The required estimate, for each fixed $z$, is
$$
 \lim_{t\to\infty}\limsup_{N\to\infty}
 \frac1{H_N}\sum_{\substack{n\le N\\W_n(z)>0}}
                  \frac{e^{-tW_n(z)}}n=0.
$$
It has not been established. This is the remaining small-positive-potential
problem, not a consequence of dominated convergence.

The proof even permits repeated moduli if summable rates are assigned
to the individual congruence pairs. It cannot, by itself, distinguish
Problem 25 from the multi-residue setting. Summable rates regularize
each finite time precisely by suppressing remote moduli.

## Fixed-probability thinning preserves hypothetical anomalous blocks

Let a finite singleton family have all $q\ge Q>1$, full footprint
$\beta$, and normalized harmonic deletion $\alpha$ at $N$. Retain each
class independently with fixed probability $p>0$, obtaining
$\alpha_p,\beta_p$. Then
$$
 \mathbb E\alpha_p\ge p\alpha,\qquad \beta_p\le\beta.
 \tag{2}
$$
Each originally deleted integer survives the thinning as a deletion with
probability at least $p$, which proves the first inequality.

Changing the retention of class $q$ changes $\alpha_p$ by at most $1/q$.
The elementary product variance bound therefore gives
$$
 \operatorname{Var}(\alpha_p)
 \le p(1-p)\sum_q q^{-2}\le\frac{p(1-p)}{Q-1}.
$$
For completeness, reveal the independent retention bits in order. The
corresponding martingale differences have squared means at most
$p(1-p)/q^2$, because the two conditional expectations differ by at most
$1/q$. Orthogonality and summation give the variance bound. Chebyshev
then yields
$$
 \Pr\{\alpha_p<p\alpha-\eta\}
 \le\frac{p(1-p)}{\eta^2(Q-1)}.
 \tag{3}
$$
Hence hypothetical late blocks with fixed positive deletion and vanishing
footprint retain positive deletion with probability tending to one after
every fixed-probability thinning. Such thinning is not a mechanism for
destroying the counterexample obstruction.

## Random-order charges can escape to wholly redundant classes

For a finite family, let $M(\omega)$ count full hits and $m(n)$ count
active hits. Averaging a uniform random order gives symmetric allocations
$$
 e_q=\int_{C_q}\frac1{M(\omega)}\,d\mu,
 \qquad
 c_q(N)=\frac1{H_N}\sum_{\substack{n\le N\\n\in B_q}}
                       \frac1{n\,m(n)}.
$$
Their totals are $\beta$ and the actual normalized harmonic deletion.
They are not consistent as the finite family grows.

Take zero residues at $2$ and at $2p$ for every odd prime $p$. All later
classes lie inside $C_2$, so every genuine increasing-order tail increment
is zero. On $C_2$, however, infinitely many odd primes divide a Haar
integer almost surely. Indeed the probability of avoiding all sufficiently
large primes is zero by CRT and divergence of their reciprocal sum.
Thus $M\to\infty$ on $C_2$, and dominated convergence gives
$e_q\to0$ for every fixed $q$, while $\sum_qe_q=1/2$ throughout.
For every fixed cutoff $K$,
$$
 \sum_{q>K}e_q\longrightarrow\frac12.
$$
All allocation mass escapes to late classes that add no footprint at all.
Keeping an old prefix first avoids this defect but restores the original
conditioned-survivor difficulty.

### A weaker entropy bound does hold for the symmetric allocation

If all moduli are at most $N$, then
$$
 \sum_q c_q(N)\log_+\frac{c_q(N)}{e_q}\ll\log\log(3N).
 \tag{4}
$$
To check this, conditional Jensen gives
$$
 e_q\ge\frac1{qD_q},\qquad
 D_q:=\mathbb E(M\mid C_q)
 =\sum_{\substack{r\\C_q\cap C_r\ne\varnothing}}\frac{(q,r)}r
 \le H_N\sum_{d\mid q}\frac{\varphi(d)}d
 \le H_N2^{\Omega(q)}.
$$
Since $qc_q(N)\le1$,
$\log_+(c_q/e_q)\le\log H_N+\Omega(q)\log2$.
Distinctness and the established
[prime-rank generating bound](rank_and_moment_obstructions.md#a-rank-sensitive-additive-target-now-refuted)
give
$$
 \sum_{\Omega(q)>r}c_q(N)
 \le\min\{1,C(3/2)^{-r}(\log(3N))^{3/2}\}.
$$
Summing this tail bound over $r\ge0$ proves
$\sum_q\Omega(q)c_q(N)\ll\log\log(3N)$ and hence (4).

This growing bound and the allocation escape above prevent it from
replacing the unresolved constant entropy bound for the original disjoint
first-kill potential. No conclusion about the full logarithmic density
has been obtained from these probabilistic regularizations.
