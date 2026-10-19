---
name: research/erdos_25/squarefull_kernel_truncation
desc: Natural density for singleton systems with a bounded number of prime factors occurring to exponent one, including arbitrary bounded distinct-prime rank.
tags: [density, prime-rank, squarefull-kernels, partial-results]
sources: []
created: 2026-09-22T09:44:27Z
updated: 2026-09-24T22:13:01Z
---


# research/erdos_25/squarefull_kernel_truncation

***

## Theorem: proved

For a positive integer $q$, write
$$
 \lambda(q)=\#\{p:v_p(q)=1\}.
$$
Consider a family of distinct moduli $q$, with one arbitrary normalized
residue $a_q$ at each modulus, and let
$$
 C_q=[a_q]_q,\qquad
 U=\bigcup_q C_q\subseteq\widehat{\mathbb Z},\qquad
 B=\{n\ge1:\exists q\le n,\ n\equiv a_q\pmod q\}.
$$
If $\lambda(q)\le r$ throughout the family, for some fixed integer
$r\ge0$, then $B$ has finite-periodic approximation in upper natural
density. Its natural density is $\mu(U)$, and the survivor set has
natural and logarithmic density $1-\mu(U)$.

In particular, **arbitrary singleton residues with bounded
$\omega(q)$ have natural density**, without any restriction on
exponents or coherence. The theorem is stronger: the number of distinct
prime factors occurring to exponent at least two need not be bounded.

The proof uses the finite counting inequality from
[bounded prime rank](bounded_prime_rank.md), which permits multiple
residues at a modulus:
$$
 \Omega(d_i)\le r
 \quad\Longrightarrow\quad
 \left|\bigcup_i\{k\ge d_i:k\equiv c_i\pmod{d_i}\}
                  \cap[1,T]\right|
 \le 2^r T\,
       \mu\left(\bigcup_i[c_i]_{d_i}\right).
 \tag{1}
$$
This is a finite inequality, uniform in the moduli and residues. It does
not require the already established density theorem for bounded
$\Omega$.

## Two elementary estimates

Call $m$ powerful, or squarefull, if every prime divisor of $m$
occurs to exponent at least two; include $1$. Let $\mathcal P$
denote the set of powerful integers. Every $m\in\mathcal P$ has a
unique representation $m=a^2b^3$ with $b$ squarefree. Therefore
$$
 \#\{m\in\mathcal P:m\le T\}
 \le \sqrt T\sum_{b\ge1}b^{-3/2}\ll\sqrt T.
 \tag{2}
$$
Dyadic summation gives
$$
 S:=\sum_{m\in\mathcal P}\frac1m<\infty,\qquad
 \sum_{\substack{m\in\mathcal P\\m>M}}\frac1m\ll M^{-1/2}.
 \tag{3}
$$
If
$$
 L_0(M)=\operatorname{lcm}\{m\le M:m\in\mathcal P\},
$$
then the product bound for an lcm and (2) give
$$
 \log L_0(M)
 \le\sum_{\substack{m\in\mathcal P\\m\le M}}\log m
 \ll\sqrt M\log(2M).
 \tag{4}
$$

Write $\mathcal T_r$ for the squarefree integers with at most $r$
prime factors, including $1$. The elementary prime reciprocal bound
$\sum_{p\le T}1/p\ll\log\log(3T)$ implies
$$
 R_r(T):=\sum_{\substack{t\le T\\t\in\mathcal T_r}}\frac1t
 \ll_r\bigl(\log\log(3T)\bigr)^r.
 \tag{5}
$$
Indeed, for each number of factors, enlarge the sum to ordered tuples
of primes at most $T$.

We will also use the following consequence, proved here to avoid
invoking an almost-prime asymptotic. For $r\ge1$, put
$A_r(T)=\#(\mathcal T_r\cap[1,T])$. Chebyshev's elementary estimate
$\vartheta(y)=\sum_{p\le y}\log p\ll y$ gives
$$
\begin{aligned}
 \sum_{\substack{t\le T\\t\in\mathcal T_r}}\log t
 &=\sum_{\substack{t\le T\\t\in\mathcal T_r}}\sum_{p\mid t}\log p\\
 &\le\sum_{\substack{m\le T\\m\in\mathcal T_{r-1}}}
              \vartheta(T/m)
 \ll T R_{r-1}(T).
\end{aligned}
$$
The terms $t>\sqrt T$ each have $\log t>\frac12\log T$;
there are at most $\sqrt T$ smaller integers. Thus, for large $T$,
$$
 A_r(T)\ll_r
 \frac{T}{\log T}\bigl(\log\log(3T)\bigr)^{r-1}.
 \tag{6}
$$
For $X^{1/2}\le Y<X$, partial summation consequently yields
$$
 \sum_{\substack{Y<t\le X\\t\in\mathcal T_r}}\frac1t
 \ll_r
 \bigl(\log\log(3X)\bigr)^{r-1}
 \left(\frac1{\log X}+
       \frac{\log(X/Y)}{\log Y}\right).
 \tag{7}
$$
Here the negative lower endpoint in partial summation was discarded.
For $r=0$, the left side is zero as soon as $Y\ge1$.

## A conditioned asymptotic counting bound

We prove the following stronger intermediate assertion. Let $W$ be
any periodic set, viewed both as a union of integer residue classes and
as a clopen subset of $\widehat{\mathbb Z}$. Then
$$
 \overline d(B\cap W)\le 2^r\mu(U\cap W).
 \tag{8}
$$
The conditioning period of $W$ is fixed when the natural-density
limit is taken.

Let $K$ be such a period. Every modulus in the family has a unique
factorization
$$
 q=mt,\qquad
 m\in\mathcal P,\quad t\in\mathcal T_r,\quad (m,t)=1:
 \tag{9}
$$
put in $m$ precisely the prime powers with exponent at least two,
and in $t$ the primes with exponent exactly one.

For a sufficiently large counting cutoff $X$, choose
$$
 M=\lfloor\log X\rfloor,\qquad
 L=\operatorname{lcm}(K,L_0(M)),\qquad
 \eta=\frac1{\log X}.
 \tag{10}
$$
By (4),
$$
 \log L\le\log K+O(\sqrt{\log X}\log\log X)=o_K(\log X).
 \tag{11}
$$
Although $L$ grows with $X$, all ensuing finite bounds are uniform
in $L$.

### Large powerful kernels

Since a single delayed class modulo $q$ has at most $X/q$ points
below $X$, the union coming from $m>M$ has at most
$$
\begin{aligned}
 X\sum_{\substack{m\in\mathcal P\\m>M}}\frac1m
       \sum_{\substack{t\le X\\t\in\mathcal T_r}}\frac1t
 &\ll_r
 X\frac{(\log\log(3X))^r}{\sqrt{\log X}}
 =o_r(X)
\end{aligned}
\tag{12}
$$
points. We enlarged the set of coprime pairs in (9), which only
increases the positive sum. Distinctness of the original moduli is
used here.

### Refining the small kernels

For $m\le M$, we have $m\mid L$. As $t$ is squarefree and
coprime to $m$, set
$$
 u=\frac{t}{(t,L)},\qquad
 D=\operatorname{lcm}(L,q)=Lu.
 \tag{13}
$$
In particular, $\Omega(u)\le r$, $q\mid D$, and $D\le Lt$.

Refine $C_q$ into residue classes modulo $D$, but activate these
refined classes only at $n\ge D$. Call the union of the resulting
delayed sets $B_X^*$; this construction uses only the classes with
small powerful kernel $m\le M$. It is a subset of $B$.

On a fiber $n=b+Lk$, $0\le b<L$, a nonempty refinement is one
residue class for $k$ modulo $u$. The activation condition is
exactly
$$
 b+Lk\ge Lu\quad\Longleftrightarrow\quad k\ge u.
 \tag{14}
$$
The quotient family on that fiber can have several residues at a
modulus, which is permitted in (1).

Because $K\mid L$, each fiber lies wholly in $W$ or wholly outside
it. Let $\beta_b$ be the conditional Haar measure, on the fiber
$[b]_L$, of the full union of all the small-kernel classes. Apply
(1) to the finitely many refined classes active below $X$.
Their Haar union is no larger than $\beta_b$; the quotient cutoff
is at most $X/L$. Summing over the fibers belonging to $W$ gives
$$
\begin{aligned}
 |B_X^*\cap W\cap[1,X]|
 &\le 2^r\frac XL
          \sum_{\substack{0\le b<L\\ {}[b]_L\subseteq W}}\beta_b\\
 &=2^r X\,\mu(U_{\le M}\cap W)
 \le2^r X\,\mu(U\cap W),
\end{aligned}
\tag{15}
$$
where $U_{\le M}$ is the full small-kernel union. Classes with
$u=1$, including those with $q\mid L$, present no exception:
their quotient activation is $k\ge1$.

### The extra activation delay costs $o(X)$

Any point counted by a small-kernel class at the original activation
but not at the stronger one satisfies, for some such class,
$$
 q\le n<D\le Lt.
 \tag{16}
$$
There are at most $\eta X$ positive integers with $n\le\eta X$.
For every other point in (16),
$$
 t>Y:=\frac{\eta X}{L}.
 \tag{17}
$$
Since $q\le n\le X$, also $t\le X$.
Another application of the individual delayed progression bound
therefore gives at most
$$
 \eta X+
 X\left(\sum_{m\in\mathcal P}\frac1m\right)
      \sum_{\substack{Y<t\le X\\t\in\mathcal T_r}}\frac1t
 \tag{18}
$$
extra points. This is the second place where singleton distinctness
is used.

By (10)--(11),
$$
 \log(X/Y)=\log L+\log\log X
 =O_K(\sqrt{\log X}\log\log X),
 \qquad
 \log Y\sim\log X.
 \tag{19}
$$
In particular $X^{1/2}\le Y<X$ eventually. Equations (3), (7),
and (19) show that (18) is $o_{r,K}(X)$.
Combining (12), (15), and (18) proves (8).

The proof in fact supplies a family-independent error for each fixed
$r$ and $K$; no rate of convergence for the full Haar union is
assumed.

## Finite-periodic approximation

Let $F$ be a finite subfamily, and write $U_F$ for its full
periodic union and $B_F$ for its delayed union. They differ on only
finitely many positive integers. Thus
$$
 B\setminus B_F
 \quad\hbox{and}\quad
 B\cap(\widehat{\mathbb Z}\setminus U_F)\cap\mathbb N
$$
differ on only finitely many integers. Apply (8) with
$W=\widehat{\mathbb Z}\setminus U_F$:
$$
 \overline d(B\setminus B_F)
 \le 2^r\mu(U\setminus U_F).
 \tag{20}
$$
As finite subfamilies exhaust the family, the right side tends to
zero by continuity of Haar measure from below. This is the claimed
finite-periodic approximation. Since $d(B_F)=\mu(U_F)$, it also
proves $d(B)=\mu(U)$. Complementation and partial summation yield
the corresponding natural and logarithmic survivor densities.

The case $r=0$ is included; it also follows directly from (3),
because all original moduli are powerful.

## Scope and the earlier product obstruction

The argument establishes arbitrary bounded-$\omega$ density, but
does not settle unrestricted Problem 25: $\lambda(q)$ can be
unbounded. Its two elementary tail estimates rely on fixed $r$;
the finite bound (1) also has the factor $2^r$.

The [three-prime product-capacity obstruction](product_capacity_obstruction.md)
does not contradict this result. Its abstract masses satisfy
individual divisor-face capacities, but the present proof uses
singleton arithmetic union bounds, a cutoff-dependent lcm refinement,
and an asymptotically negligible activation discrepancy. It does not
deduce a uniform finite bound solely from those capacities.

The same proof permits a uniformly bounded number of residues per
original modulus: only (12) and (18) change, by that fixed
multiplicity factor, and their errors still tend to zero. No
unbounded-multiplicity version is claimed.

## A growing-rank cutoff and its limitation

For every fixed real $z>1$,
$$
 \sum_{q\le X}\frac{z^{\lambda(q)}}q
 \le\prod_{p\le X}\left(1+\frac zp+\frac1{p(p-1)}\right)
 \ll_z(\log(3X))^z.
 \tag{21}
$$
Each local factor is
$(1-1/p)^{-z}(1+O_z(p^{-2}))$, so the previously used
Euler-product bound proves the last estimate. Unlike the analogous
generating function for $\Omega(q)$, this one has no restriction
$z<2$: exponents at least two contribute the unweighted geometric
tail $1/(p(p-1))$.

Write $B_{>r}$ for the delayed union using moduli with
$\lambda(q)>r$. Singleton distinctness and the exact individual
counting and harmonic bounds give, uniformly in the residues,
$$
 \frac{|B_{>r}\cap[1,X]|}{X},\quad
 \frac{H_{B_{>r}}(X)}{H_{\lfloor X\rfloor}}
 \ll_z z^{-r}(\log(3X))^z.
 \tag{22}
$$
Taking $z=e$ and
$r=\lceil(e+\varepsilon)\log\log X\rceil$ makes both omitted
proportions $O_\varepsilon((\log X)^{-\varepsilon})$.
This does **not** extend the fixed-rank density theorem: the retained
rank grows, and its comparison constant $2^r$ is unbounded.

There is also a precise obstruction to using a fixed rank and only
reciprocal counting. The powerful-kernel decomposition (9) gives
$$
 \sum_{\substack{q\le X\\\lambda(q)\le r}}\frac1q
 \ll_r(\log\log(3X))^r=o(\log X).
$$
Thus high-rank moduli carry asymptotically all unrestricted reciprocal
mass. They also carry its leading raw harmonic-progression budget:
$$
 \sum_{\substack{q\le X\\\lambda(q)>r}}
       \frac{H_{\lfloor X/q\rfloor}}q
 =\left(\frac12+o(1)\right)(\log X)^2
 \qquad(r\text{ fixed}).
 \tag{23}
$$
The unrestricted double sum is
$\frac12(\log X)^2+O(\log X)$, by summing
$q^{-1}(\log(X/q)+O(1))$; the low-rank part is
$O_r(\log X(\log\log(3X))^r)$. A footprint- or first-kill-sensitive
comparison remains necessary.
