---
name: research/erdos_25/capped_prime_fractions
desc: Optimized arithmetic square-tail bounds for exact prime-stage forbidden fractions, with an enlarged small-prime range and an unresolved middle range.
tags: [prime-filtration, sieve, partial-results]
sources: []
created: 2026-09-22T14:20:00Z
updated: 2026-09-24T22:13:01Z
---


# research/erdos_25/capped_prime_fractions

***

This continues [prime filtration](prime_filtration.md), using the exact
forbidden fraction rather than its possibly very large union-bound
potential. The result controls two prime ranges uniformly for arbitrary
singleton residues. It does not establish logarithmic density: an
intermediate range and the conditioned arithmetic digit transfer both
remain unresolved.

## Definitions and theorem

Let $\mathcal F$ be a finite family of distinct moduli $q>1$, with
one residue $a_q$ for each. Write a modulus whose largest prime factor
is $p$ uniquely as $q=p^e m$, where $e\ge1$ and
$P^+(m)<p$; take $P^+(1)=1$. For an integer $n$, define
$$
 \alpha_p(n)=\mu_p\!\left(
   \bigcup_{\substack{q=p^em\in\mathcal F,\ q\le n\\
                     n\equiv a_q\ (m)}}[a_q]_{p^e}
                    \right),
 \tag{1}
$$
where $\mu_p$ is Haar probability on $\mathbb Z_p$. Thus
$0\le\alpha_p(n)\le1$, and $\alpha_p(n)=0$ for $p>n$.
The condition $q\le n$ is the original activation, not a power delay.

Put
$$
 U_p=\frac1{(p-1)^2}
       \prod_{\ell<p}\frac{1+1/\ell}{(1-1/\ell)^2}
       \ll\frac{\log^3(2p)}{p^2},
 \qquad T_K=\sum_{p>K}U_p.
 \tag{2}
$$
Products and sums indexed by $p,\ell$ are over primes. In particular
$T_K\to0$.

For all sufficiently large $n$, set
$$
 y(n)=\exp\!\left(\frac{\log n}{8\log\log n}\right),
$$
and set $y(n)=1$ on the remaining finite initial segment. Then
$$
 \limsup_{X\to\infty}\ \sup_{\mathcal F}
 \frac1{H_{\lfloor X\rfloor}}
 \sum_{n\le X}\frac1n
 \sum_{\substack{p>K\\p\le y(n)\ \text{or}\ p>n^{1/3}}}
          \alpha_p(n)^2
 \le \frac{T_K}{\log2}
 \qquad(K\ge60).
 \tag{3}
$$
The supremum can depend on $X$. Consequently the left side tends to
zero as $K\to\infty$. The same assertion applies to infinite
singleton systems, since only finitely many moduli are active below any
fixed cutoff.

The [optimized refinement below](#an-optimized-small-prime-cutoff) replaces
$y(n)$ by
$\exp(c\log n\,\log\log\log n/\log\log n)$ for every fixed
$0<c<1/2$, and improves the right side of (3) to $T_K$.

## Truncating the smaller part

Average over $I_N=\{N+1,\ldots,2N\}$. For $M\ge1$, let
$$
 A_{p,M}(n)=
 \sum_{\substack{q=p^em\in\mathcal F\\m\le M}}
       p^{-e}\mathbf1_{n\equiv a_q\ (m)},
 \qquad
 R_{p,M}(n)=
 \sum_{\substack{q=p^em\in\mathcal F\\m>M,\ q\le n}}
       p^{-e}\mathbf1_{n\equiv a_q\ (m)}.
$$
The small-part potential deliberately omits activation. The large-part
potential retains it. Since
$\alpha_p\le\min(1,A_{p,M}+R_{p,M})$, the elementary inequality
$$
 \min(1,A+R)^2\le A^2+2R\qquad(A,R\ge0)
 \tag{4}
$$
gives a useful capped estimate. To check (4), it is immediate for
$A\ge1$; for $A<1$, the capped square increases with $R$
at rate at most two.

Two compatible smaller-part congruences form one class modulo
$[m,r]$, and hence have at most $N/[m,r]+1$ simultaneous
solutions in $I_N$. There is at most one original congruence at each
$p^em$. Therefore
$$
 \mathbb E_{I_N}A_{p,M}^2
 \le U_p+\frac{M^2}{N(p-1)^2}.
 \tag{5}
$$
For the main term, enlarge to all smaller parts supported on primes
below $p$ and use
$$
 \sum_{P^+(m),P^+(r)<p}\frac1{[m,r]}
 =\prod_{\ell<p}\sum_{i,j\ge0}\ell^{-\max(i,j)}
 =\prod_{\ell<p}\frac{1+1/\ell}{(1-1/\ell)^2}.
$$
For the error, the sum of the coefficients of all small-part terms is
at most $M\sum_{e\ge1}p^{-e}=M/(p-1)$.

For a term of $R_{p,M}$, normalize $a_q\bmod m$ as
$c\in[0,m)$. Writing $n=c+km$, activation is exactly
$k\ge p^e$. Its active count up to $2N$ is therefore at most
$2N/m$, with no extra root error. It follows that
$$
 \mathbb E_{I_N}R_{p,M}
 \le \frac2{p-1}
       \sum_{\substack{m>M\\P^+(m)<p}}\frac1m.
$$
Combining this with (4)--(5) proves
$$
 \mathbb E_{I_N}\alpha_p^2
 \le U_p+\frac{M^2}{N(p-1)^2}
       +\frac4{p-1}
          \sum_{\substack{m>M\\P^+(m)<p}}\frac1m.
 \tag{6}
$$

## The small-prime range

For $p\ge60$, Rankin's inequality with
$\theta=1/\log p\le1/4$ gives
$$
 \sum_{\substack{m>M\\P^+(m)<p}}\frac1m
 \le M^{-\theta}
       \prod_{\ell<p}(1-\ell^{-1+\theta})^{-1}
 \ll (\log p)\exp\!\left(-\frac{\log M}{\log p}\right).
 \tag{7}
$$
Here the product is $O(\log p)$ uniformly in $p$. Indeed,
its logarithmic difference from
$\prod_{\ell<p}(1-1/\ell)^{-1}$ has first-power contribution
$$
 \sum_{\ell<p}\frac{\ell^\theta-1}{\ell}
 \le e\theta\sum_{\ell<p}\frac{\log\ell}{\ell}=O(1),
$$
and higher-power contribution bounded by
$O(\sum_{\ell}\ell^{-3/2})=O(1)$. The elementary prime-product
and prime-log-sum estimates used here are proved in
[the coherent power-cutoff notes](coherent_power_cutoff.md#two-elementary-sieve-ingredients).

Summing (6)--(7), and using
$\sum_{p\le Y}(\log p)/(p-1)\ll\log Y$, gives
$$
 \mathbb E_{I_N}\sum_{K<p\le Y}\alpha_p^2
 \le T_K+\frac{CM^2}{NK}
       +C\log Y\exp\!\left(-\frac{\log M}{\log Y}\right)
 \qquad(60\le K<Y).
 \tag{8}
$$
Take
$$
 M=N^{1/3},\qquad
 Y(N)=\exp\!\left(\frac{\log N}{6\log\log N}\right).
$$
For sufficiently large $N$, (8) becomes
$$
 \mathbb E_{I_N}\sum_{K<p\le Y(N)}\alpha_p^2
 \le T_K+\frac{C N^{-1/3}}K
             +\frac{C}{\log N\log\log N}.
 \tag{9}
$$
If $Y(N)\le K$, the sum is empty and the same upper bound is harmless.

## The large-prime range

Let $A_p(n)$ be the full union-bound potential, including activation
in every term. Then $\alpha_p^2\le A_p^2$. For a point of
$I_N$, any active modulus $p^em$ has $m\le2N/p^e$.
Counting compatible pairs on $[1,2N]$, rather than $I_N$, gives
$$
 \mathbb E_{I_N} A_p^2
 \le 2U_p+\frac1N
       \left(\sum_{e\ge1}p^{-e}\lfloor2N/p^e\rfloor\right)^2
 \le 2U_p+\frac{4N}{(p^2-1)^2}.
 \tag{10}
$$
Chebyshev's prime-counting upper bound and partial summation imply
$$
 \sum_{p>Z}(p^2-1)^{-2}\ll\frac1{Z^3\log(2Z)}.
$$
Consequently
$$
 \mathbb E_{I_N}\sum_{p>N^{1/3}}\alpha_p^2
 \ll \frac{(\log N)^3}{N^{1/3}}+\frac1{\log N}=o(1),
 \tag{11}
$$
uniformly in the family.

## Harmonic summation and the remaining gaps

For $N<n\le2N$, eventually $y(n)\le Y(N)$. Also
$p>n^{1/3}$ implies $p>N^{1/3}$. Thus (9)--(11) bound the
ordinary average on $I_N$ of the inner sum in (3) by
$T_K+o_N(1)$, with a uniform error. Multiplication by $1/n\le1/N$
shows that its harmonic mass on that interval has the same upper bound.
Sum over $N=2^j$; a final partial interval can be enlarged to the
whole interval. The number of intervals is $(\log X)/\log2+O(1)$,
and their uniform error has vanishing Cesàro average. Finitely many small
integers contribute a family-independent bounded amount, since
$\alpha_p(n)=0$ for $p>n$. Division by $H_X\sim\log X$
proves (3).

The preceding proof leaves the prime interval
$$
 n^{1/(8\log\log n)}<p\le n^{1/3}
$$
untreated. The optimized refinement below shortens this interval but
does not eliminate it. More fundamentally,
$\alpha_p(n)$ averages over a $p$-adic fiber, whereas the integer
$n$ uses one possibly correlated digit in that fiber. Even a bound
for the omitted squared fractions would not by itself identify their
sum with actual deletions. An arithmetic transfer retaining the old
survivor condition is still required. No such transfer, general
logarithmic-density theorem, or counterexample is asserted here.

The [bounded-height center theorem](bounded_height_prime_centers.md)
now controls this middle range when each prime's smaller-part residues
admit moderately many integer centers of bounded height. It gives full
arithmetic square tails for that subclass, with arbitrary new-prime
digits. The unrestricted middle range remains open. Furthermore,
[bounded full-survivor conditional weights](full_survivor_trace_obstruction.md)
do not turn even pointwise square tails into signed arithmetic
cancellation; that specific infinite-marginal transfer is false.

## The cap, rather than the distribution of digits, is the extra input

In the squarefree-largest-prime subfamily $q=pm$, a uniform bound
for the exact squared fractions is equivalent up to an absolute
constant to a bound for the squared capped union-bound potential.
This concerns unconditioned nonnegative averages, not the missing
survivor-conditioned digit transfer.

Fix arbitrary smaller-part residues $c_{p,m}\pmod m$. Independently
choose a uniform residue $b_{p,m}\pmod p$ and use CRT to install
one class modulo $pm$ with these two projections. Moduli are still
globally distinct, since $P^+(m)<p$. At a fixed $n$, let
$$
 C_p(n)=\#\{m:pm\text{ is selected},\ pm\le n,
                              \ n\equiv c_{p,m}\pmod m\},
 \qquad A_p(n)=C_p(n)/p.
$$
The exact forbidden fraction is the fraction of the $p$ digits
occupied by $C_p(n)$ independent uniform choices. Hence
$$
 \mathbb E\alpha_p(n)
 =1-(1-1/p)^{C_p(n)}
 \ge(1-e^{-1})\min(1,A_p(n)).
$$
Jensen gives
$$
 \mathbb E\alpha_p(n)^2
 \ge(1-e^{-1})^2\min(1,A_p(n))^2.
 \tag{12}
$$
Conversely $\alpha_p(n)\le\min(1,A_p(n))$ for every assignment.
After any finite nonnegative weighted summation in $n,p$, some
deterministic digit assignment attains at least the expectation in
(12). Thus one cannot resolve the uniform intermediate-prime square
estimate merely by seeking additional cancellation between its
forbidden digits. A bound for the high multiplicities of the
smaller-part congruences, with their activation retained, is needed.

## An optimized small-prime cutoff

**Theorem.** Fix $0<c<1/2$ and $K\ge60$, and for sufficiently
large $n$ put
$$
 y_c(n)=\exp\!\left(
 c\,\frac{\log n\,\log\log\log n}{\log\log n}\right);
$$
set $y_c(n)=1$ on the finite initial segment. Then
$$
 \limsup_{X\to\infty}\sup_{\mathcal F}
 \frac1{H_{\lfloor X\rfloor}}
 \sum_{n\le X}\frac1n
 \sum_{\substack{p>K\\p\le y_c(n)\ \mathrm{or}\ p>n^{1/3}}}
       \alpha_p(n)^2
 \le T_K.
 \tag{13}
$$
All exponents $e\ge1$, arbitrary singleton residues, and original
activation are retained. In particular the remaining middle range is
$y_c(n)<p\le n^{1/3}$, not the larger range left by (3).

### A uniform tilted Euler product

For $0<\theta\le1/4$, $p\le Y$, and $s=\theta\log Y$,
$$
 \prod_{\ell<p}(1-\ell^{-1+\theta})^{-1}
 \ll \log(2p)\exp(Cse^s).
 \tag{14}
$$
Indeed, relative to the product at $\theta=0$, the first-power
logarithmic contribution is at most
$$
 \sum_{\ell<p}\frac{\ell^\theta-1}{\ell}
 \le \theta Y^\theta
            \sum_{\ell<p}\frac{\log\ell}{\ell}
 \ll se^s.
$$
All higher powers contribute $O(1)$, uniformly, since their sum
is bounded by $C\sum_\ell\ell^{-3/2}$. The elementary product and
prime-log-sum estimates already used in (7) complete the proof.
Thus, with
$S_p(M)=\sum_{m>M,\ P^+(m)<p}1/m$, Rankin's inequality gives
$$
 S_p(M)\ll\log(2p)
                 \exp(-\theta\log M+Cse^s).
 \tag{15}
$$

A useful specialization, also used in
[the very-smooth modulus reduction](smooth_largest_prime_reduction.md),
is $M=p^u$, $s=\log u-2\log\log u$. Whenever $u$ is
sufficiently large and $0<s/\log p\le1/4$, it gives
$$
 S_p(p^u)\ll\log(2p)
 \exp\!\left(-u\log u+2u\log\log u
                      +O\!\left(\frac{u}{\log u}\right)\right).
 \tag{16}
$$
No asymptotic theorem for smooth numbers is required.

### Harmonic truncation with its exact main coefficient

For any residue class modulo $d$, discrete partial summation gives
$$
 \sum_{\substack{N<n\le2N\\n\equiv b\ (d)}}\frac1n
 \le \frac{H_{2N}-H_N}{d}+\frac1N.
 \tag{17}
$$
The counting discrepancy on each initial subinterval of
$\{N+1,\ldots,2N\}$ has absolute value at most one; its weighted
discrepancy is therefore at most $1/(N+1)$.

Use the same $A_{p,M},R_{p,M}$ as above. Pairwise CRT in (17)
and the coefficient sum $M/(p-1)$ imply
$$
 \sum_{N<n\le2N}\frac{A_{p,M}(n)^2}{n}
 \le (H_{2N}-H_N)U_p+\frac{M^2}{N(p-1)^2}.
$$
Activation gives the unchanged remainder estimate
$$
 \sum_{N<n\le2N}\frac{R_{p,M}(n)}n
 \le\frac2{p-1}S_p(M).
$$
Consequently the capped inequality (4) yields
$$
 \sum_{N<n\le2N}\frac1n\sum_{K<p\le Y}\alpha_p(n)^2
 \le (H_{2N}-H_N)T_K+\frac{CM^2}{NK}
                     +4\sum_{p\le Y}\frac{S_p(M)}{p-1}.
 \tag{18}
$$

Take
$$
 M=\frac{\sqrt N}{\log N},\qquad Y=y_c(2N),\qquad
 u=\frac{\log M}{\log Y}.
$$
Then
$$
 u\log u=\left(\frac1{2c}+o(1)\right)\log\log N.
$$
Choose a fixed $a$ with $2c<a<1$, set $s=a\log u$, and
take $\theta=s/\log Y$. Formula (15), uniformly over $p\le Y$,
gives
$$
 S_p(M)\ll\log(2p)
 \exp\!\left(-a u\log u+Cau^a\log u\right)
 =\log(2p)(\log N)^{-a/(2c)+o(1)}.
$$
Using $\sum_{p\le Y}\log(2p)/(p-1)\ll\log Y\ll\log N$,
the final term in (18) is
$(\log N)^{1-a/(2c)+o(1)}=o(1)$.
The other error is $O(1/(K(\log N)^2))$.
The function $y_c$ is eventually increasing, so
$p\le y_c(n)$ implies $p\le Y$ on this interval.

The already proved large-prime estimate (11) contributes $o(1)$
in harmonic mass on the same interval. For $c=1/4$, one may take
$a=3/4$, and the combined error is $O((\log N)^{-1/4})$.
For every fixed $c<1/2$, it is still a uniform vanishing error.

Finally sum (18) over $N=2^j$, enlarging the last partial interval.
The main terms telescope; the final dyadic endpoint changes $H_X$
by only $O(1)$. The errors have vanishing Cesàro average, and the
finite initial segment is uniformly bounded since
$\alpha_p(n)=0$ for $p>n$. This proves (13).

The sharper cutoff does not address the survivor-conditioned digit
transfer. Even a proof for all omitted primes would leave that
separate arithmetic step unresolved.
