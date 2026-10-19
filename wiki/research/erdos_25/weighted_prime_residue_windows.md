---
name: research/erdos_25/weighted_prime_residue_windows
desc: A uniform harmonic bound for one dyadic block from weighted prime-residue support, allowing unboundedly many local colors.
tags: [coherent-residues, partial-results, prime-coordinates]
sources: []
created: 2026-09-22T11:00:00Z
updated: 2026-09-24T22:13:01Z
---


# research/erdos_25/weighted_prime_residue_windows

***

The weighted-coherence sketch in Section 5 of
the [[research/erdos_25/independent/profinite_shifts_and_long_windows|third independent record]]
can be made rigorous and gives the following one-block estimate.
It assumes only control of residue supports modulo primes, not common
prime-power centers or a bounded number of global profiles. It does not
control an arbitrary conditioned tail or an unbounded number of blocks.

## Uniform harmonic theorem

Let $Q\ge2$ be an integer, let $D\subseteq[Q,2Q]\cap\mathbb N$, and
choose one normalized residue $a_q$ for each distinct $q\in D$. Put
$$
 B=\bigcup_{q\in D}\{a_q+tq:t\ge1\}.
$$
For every prime $p$ dividing some selected modulus, define
$$
 R_p=\{a_q\bmod p:q\in D,\ p\mid q\},\qquad r_p=|R_p|,
 \qquad \mathcal H=\sum_{p:r_p>0}\frac1{p r_p}.
$$
If $D$ is nonempty, there is an absolute constant $C$ such that
$$
 \sup_{X\ge2}\frac{H_B(X)}{H_{\lfloor X\rfloor}}
 \le \min\{1,C/\mathcal H\}.
 \tag{1}
$$
In particular, any sequence of such blocks with $\mathcal H\to\infty$
has uniformly vanishing normalized harmonic mass, even at unbounded
quotients. The empty family is trivial.

More generally, (1) holds for any chosen set of primes at most $2Q$
and nonempty sets $R_p$ containing all required residues at those primes.
One may therefore adjoin missing primes with arbitrary singleton supports.
If every actual support size is at most $R$, this gives the corollary
$$
 \sup_{X\ge2}\frac{H_B(X)}{H_{\lfloor X\rfloor}}
 \ll\min\{1,R/\log\log(3Q)\}.
 \tag{1a}
$$
Here $R$ may grow with $Q$. This uses only prime-level support bounds.

## A finite interval estimate

First use any finite set $\mathcal P$ of primes with nonempty supports
$R_p$ satisfying the same containment condition; it is permissible to
enlarge a support. Write
$$
 m=|\mathcal P|,\qquad h=\sum_{p\in\mathcal P}\frac1{p r_p}>0,
 \qquad \ell=\sum_{p\in\mathcal P}\frac1p.
$$
For an interval $I$ of $T\ge Q$ consecutive integers, the full union
$U=\bigcup_{q\in D}[a_q]_q$ obeys
$$
 |U\cap I|\ll \frac{T}{h}
       +\left(\frac{T}{Q}+Q\right)\frac{m^2}{h^2}.
 \tag{2}
$$
All constants are absolute, including with arbitrarily large $T$.

Define the prime score and the extra score forced by a modulus by
$$
 K(n)=\sum_{p\in\mathcal P}\frac1{r_p}
                   \mathbf1_{n\bmod p\in R_p},\qquad
 c_p=\frac1{r_p}-\frac1p\ge0,\qquad
 G(q)=\sum_{p\mid q,\ p\in\mathcal P}c_p.
$$
Under uniform residue sampling their means are respectively $\ell$ and
$$
 v=\sum_{p\in\mathcal P}\frac{c_p}{p}
   =h-\sum_{p\in\mathcal P}\frac1{p^2},
 \qquad h-1<v\le h.
$$
The variance of $K$ is exactly $v$; that of $G$ is at most $h$.

For any interval $J$ of $S$ consecutive integers, counting single and
double prime congruences by CRT gives
$$
 \sum_{n\in J}(K(n)-\ell)^2\ll Sh+m^2,
 \qquad
 \sum_{q\in J}(G(q)-v)^2\ll Sh+m^2.
 \tag{3}
$$
Here the counting error for one residue is at most one. In the first
identity, a prime pair has $r_pr_{p'}$ residue choices but coefficient
$1/(r_pr_{p'})$, so its error is $O(1)$; the total is $O(m^2)$.
The mean-count error is at most $m$, and multiplication by
$\ell\le m/2$ preserves this bound. The second identity is the same
calculation with the single zero residue at each prime and coefficients
$0\le c_p\le1$. These observations also cover the diagonal terms.

It suffices to prove (2) for $h\ge8$, since otherwise $|U\cap I|\le T$
proves it after adjusting the constant. By (3), at most
$$
 O(Q/h+m^2/h^2)
 \tag{4}
$$
integers $q\in[Q,2Q]$ have $G(q)<h/2$. Each selected exceptional
modulus contributes at most $T/Q+1$ points of $I$.

For any remaining selected $q$, parametrize its points in $I$ as
$n=a_q+qt$, with $t$ in an interval of $T_q\le T/q+1$ integers.
Primes dividing $q$ force membership in $R_p$. At primes not dividing
$q$, the allowed residues of $t$ again form sets of size $r_p$.
The mean of $K(a_q+qt)$ in this residue model is therefore exactly
$$
 \sum_{p\mid q}\frac1{r_p}
       +\sum_{p\nmid q}\frac1p=\ell+G(q)\ge\ell+h/2.
$$
The same CRT variance bound shows that at most
$O(T_q/h+m^2/h^2)$ of these points have $K(n)<\ell+h/4$.
Summing over the at most $Q+1$ distinct selected moduli costs
$O(T/h+Qm^2/h^2)$, since $\sum_qT_q=O(T+Q)=O(T)$.
The remaining covered points belong to $K(n)\ge\ell+h/4$, whose
count in $I$ is $O(T/h+m^2/h^2)$ by (3). Combining these estimates
with (4) proves (2).

The term $Tm^2/(Qh^2)$ must be retained before imposing a size
condition on $m$. Discarding a modulus-window error before multiplying
by $T/Q+1$ would not be uniform in the length of the interval.
Also, using $c_p=1/r_p-1/p$ avoids subtracting a possibly larger
$O(\log\log\log Q)$ loss from a slowly growing $h$.

## Passing to harmonic measure

Assume $m^2\le Qh$, and put $Y=Q\max(1,m^2/h)$. Equation (2)
implies $|B\cap[1,t]|\ll t/h$ for $t\ge Y$ (integer rounding
only changes the absolute constants). There are no active points below
$Q$. Below $Y$, use the trivial harmonic bound
$1+\log(Y/Q)$; above $Y$, use partial summation with this counting
estimate. Uniformly for $X\ge2$, this gives
$$
 \frac{H_B(X)}{H_{\lfloor X\rfloor}}
 \ll \frac1h+
       \frac{1+\log^+(m^2/h)}{\log Q}.
 \tag{5}
$$
For $X<Y$, apply the trivial estimate directly up to $X$; for
$X\ge Y$ the remaining contribution is
$O(h^{-1}(1+\log(X/Y)))$. Thus (5) also covers every cutoff
within the initially uncontrolled range.

To deduce (1), use the full support parameter $\mathcal H$. The
[elementary Euler-product estimates](coprime_entropy.md#elementary-prime-estimates)
imply, uniformly for $2\le y\le2Q$,
$$
 \sum_{y<p\le2Q}\frac1p
 \le\log\frac{\log(2Q)}{\log y}+C_0,
 \qquad \mathcal H\le\log\log(2Q)+C_0.
 \tag{6}
$$
Indeed the logarithm of the finite Euler product differs from the
prime reciprocal sum by $O(1)$, while that product is bounded above
and below by absolute multiples of $\log y$.

For $\mathcal H$ larger than a fixed absolute constant choose
$$
 y=Q^{\exp(-\mathcal H/2)},\qquad
 \mathcal P=\{p\le y:r_p>0\}.
$$
The second bound in (6) ensures $y\ge2$ in this range. The first
ensures
$$
 h\ge\mathcal H/2-O(1)\ge\mathcal H/4.
$$
Also $m^2\le y^2\le Q\le Qh$. Applying (5) gives
$$
 \frac{H_B(X)}{H_{\lfloor X\rfloor}}
 \ll \frac1{\mathcal H}+\frac{1+2\log y}{\log Q}
 \ll \frac1{\mathcal H},
$$
since $\log y/\log Q=e^{-\mathcal H/2}$ and
$\mathcal H\ll\log Q$. Bounded $\mathcal H$ is handled by the
trivial bound one. This proves (1).

## Comparison and limits

For the full coherent dyadic family all $r_p=1$, so
$\mathcal H\asymp\log\log Q$ and (1) supplies an explicit harmonic
rate. The [common-shift interval theorem](common_shift_blocks.md)
has the stronger qualitative length range $T/Q\to\infty$;
(2) instead gives a quantitative estimate with finitely many prime
coordinates. Under $\mathcal P\subseteq[2,z]$ and $z^2\le Qh$,
it implies the input's bound $O(T/h+Qz^2/h^2)$.

The parameter can tend to infinity even with unbounded $r_p$;
prime-power coherence is unnecessary. Conversely, small periodic
footprint alone has not been related to this parameter in a way that
controls the general problem. No summation over arbitrarily many
windows or localization to a first-kill tail is justified by (1).
The power-law assertion mentioned separately in the input also admits
a complete proof, given next; none of its unavailable companion files
is needed.

## Power-law interval bound with one residue at each prime

Suppose that, for each prime $p$, all selected moduli divisible by $p$
have the same residue $\alpha_p\pmod p$. There need not be coherence
at higher prime powers. For each fixed $\varepsilon>0$, uniformly over
these families and intervals $I$ of $T\ge Q^{1+\varepsilon}$
consecutive integers,
$$
 |U\cap I|\le T(\log Q)^{-\delta_*+o_\varepsilon(1)},\qquad
 \delta_*=1-\frac{1+\log\log2}{\log2}=0.086071\ldots.
 \tag{7}
$$
Unrepresented primes may receive arbitrary $\alpha_p$.

We first record the finite truncation estimate used in the proof.
For any prime subset of $[2,z]$, coefficients $0\le d_p\le1$, one
residue $b_p$ at each prime, and an even integer $k$, Bonferroni and
CRT imply on any interval $J$ of $S$ integers
$$
 \sum_{t\in J}\prod_p(1-d_p\mathbf1_{t\equiv b_p\ (p)})
 \le S\left(\prod_p(1-d_p/p)+E\right)+z^k,
 \qquad E=\frac{L^{k+1}}{(k+1)!},\quad
 L=\sum_{p\le z}\frac1p.
 \tag{8}
$$
Indeed the even inclusion--exclusion truncation is an upper bound.
Its Haar excess above the full product is at most the next elementary
symmetric sum, bounded by $E$. There are at most $z^k$ squarefree
products of at most $k$ primes at most $z$, each giving a counting
error at most one. This proves (8), including its uniformity in $S$.

Fix $1<b<2$, set $s=b/2$ and $a=1-s$, and put
$K(n)=\sum_{p\le z}\mathbf1_{n\equiv\alpha_p\ (p)}$.
Choose $k$ to be the least even integer at least $20L$; then
$E\le e^{-30L}$ for large $L$. On the progression for a selected $q$,
primes dividing $q$ force $A(q):=\omega_z(q)$ matches. Applying (8)
to the other primes gives
$$
 \sum_{n\in I\cap[a_q]_q}s^{K(n)}
 \le T_q F(q)+T_qE+z^k,\qquad
 F(q)=s^{A(q)}\prod_{\substack{p\le z\\p\nmid q}}(1-a/p),
 \tag{9}
$$
where $T_q\le T/q+1$. To average over $q$, write
$$
 F(q)=P_s\prod_{p\le z}(1-d_p\mathbf1_{p\mid q}),\quad
 P_s=\prod_{p\le z}(1-a/p),\quad
 d_p=1-\frac{s}{1-a/p}\in[0,1].
$$
A second application of (8), now on $[Q,2Q]$, yields
$$
 \sum_{Q\le q\le2Q}F(q)
 \le(Q+1)(D_s+E)+z^k,\quad
 D_s=\prod_{p\le z}(1-2a/p+a/p^2)
     =\exp(-2aL+O_b(1)).
 \tag{10}
$$
Using $T_q\le T/Q+1$ and $\sum_qT_q=O(T)$ in (9)--(10),
and allowing incidence overcounting, bounds the covered points with
$K(n)\le bL$ by
$$
 O_b\!\left(T e^{-I_2(b)L}+T s^{-bL}E
             +s^{-bL}(T/Q+Q)z^k\right),\quad
 I_2(b)=2-b+b\log(b/2).
 \tag{11}
$$
The factor $s^{-bL}$ is valid since $s^{K(n)}\ge s^{bL}$ on
these points. In particular the $Tz^k/Q$ error from averaging the
moduli has not been dropped.

For the remaining points, put $B_0=\lceil bL\rceil$ and
$j=\lfloor(b-1)L\rfloor$. CRT counting of the factorial moment gives
$$
 \#\{n\in I:K(n)\ge bL\}
 \le\frac{T L^j/j!+z^j}{\binom{B_0}{j}}
 \le T\exp(-I_1(b)L+O_b(\log L))+z^k,
 \quad I_1(b)=b\log b-b+1.
 \tag{12}
$$
The last exponent follows by Stirling's formula from
$B_0-j=L+O(1)$. We work with large $Q$, so $j\ge1$; smaller
values can be absorbed in the constants.

Finally choose
$$
 z=Q^{\min(\varepsilon,1)/(1000\log\log Q)}.
$$
The elementary prime estimates give
$L=\log\log Q-\log\log\log Q+O_\varepsilon(1)$, and
$z^k\le Q^{\min(\varepsilon,1)/40}$ for sufficiently large $Q$.
All CRT errors in (11)--(12), divided by $T$, are at most
$$
 (\log Q)^{O_b(1)}
 \left(Q^{-1+\min(\varepsilon,1)/40}
       +Q^{-\varepsilon+\min(\varepsilon,1)/40}\right).
$$
They decay as a fixed negative power of $Q$, uniformly for every
$T\ge Q^{1+\varepsilon}$. The term $s^{-bL}E$ is also negligible.
Taking $b=1/\log2$ makes $I_1(b)=I_2(b)=\delta_*$ and proves (7).

This verifies the independent note's quantitative exponent and slightly
weakens its coherence hypothesis. The estimate remains a one-window
bound; it provides neither the missing inverse structural theorem nor
a summable estimate for all windows of a general system.
