---
name: research/erdos_25/coherent_annuli_and_shadows
desc: Power-annulus, prime-shadow, and simultaneous bounded-divisor-gap transport bounds; separate phase maxima cannot be summed.
tags: [coherent-residues, sieve, partial-results]
sources: []
created: 2026-09-22T06:10:00Z
updated: 2026-09-24T22:13:01Z
---


# research/erdos_25/coherent_annuli_and_shadows

***

The following finite estimates are proved. They do not control the union
of all arbitrarily thin power bands adjacent to the activation boundary.

## A finite relative-power annulus estimate

Consider a coherent family, and selected full first-kill cells $J$ of
total Haar mass $\tau$. Let $q(n)$ denote the least full covering modulus.
For $0<\eta\le1/4$, put
$$
 E_{\eta,J}=\{n:q(n)\in J,\ n^{1-2\eta}<q(n)\le n^{1-\eta}\}.
$$
Uniformly in finite families, centers, $X\ge2$, and $0<\varepsilon\le1/10$,
$$
 H_{E_{\eta,J}}(X)
 \ll\left(\varepsilon+\frac\tau\varepsilon\right)\log(2X)
       +\frac{1+\tau\log\log(3X)}{\varepsilon\eta}.
 \tag{1}
$$
The same statement follows for infinite families by retaining the
finitely many moduli that can be active below $X$.

Here is the additional summation argument, using the already proved
[coherent smooth-factor sieve](coherent_power_cutoff.md). Work on
$I_H=(H,2H]$ for dyadic $H$, omitting the initial range
$\log H<C/(\varepsilon\eta)$; its total harmonic weight is
$O(1/(\varepsilon\eta))$. Set $y=H^{c\varepsilon\eta}$ with a small
absolute $c$. The shifted smooth-part estimate excludes at most
$O(\varepsilon+H^{-c'\eta})H$ points. At a remaining point write
$n-b=qsh$, where $s$ is the $y$-smooth part of $(n-b)/q$, $h$ is
$y$-rough, and $b$ is an integer realizing the finite center residues.
We have $s\le H^{\eta/2}$. For the retained annulus,
$$
 H^{1-2\eta}<q\le2H^{1-\eta},\qquad
 H^{1-2\eta}<m:=qs\le2H^{1-\eta/2}.
$$
The quotient interval has length $H/m\ge H^{\eta/2}/2$, sufficient
for the elementary rough-number upper sieve. Moreover $q$ is the first
generator dividing $m$ in the corresponding zero-residue system.
Retaining this size information in that sieve gives
$$
 \frac{\#\{\text{good hits in }I_H\}}H
 \ll\frac1{\varepsilon\eta\log H}
 \sum_{\substack{\operatorname{first}_D(m)\in J\\
          H^{1-2\eta}<m\le2H^{1-\eta/2}}}\frac1m.
 \tag{2}
$$
All constants remain absolute; the discarded initial range absorbs the
fixed factors two in the cutoffs.

For fixed $m$, the dyadic sum of $1/\log H$ over the displayed range
is $O(\eta+1/\log m)$. This follows by placing $\log H$ between
$(\log m-\log2)/(1-\eta/2)$ and $\log m/(1-2\eta)$ and comparing the
sum with the integral of $dt/t$. Also, the geometric valuation model gives
$$
 T(Y):=\sum_{\substack{m\le Y\\\operatorname{first}_D(m)\in J}}
             \frac1m\le Z_Y\tau\ll\tau\log(2Y).
 \tag{3}
$$
Partial summation of (3) yields
$$
 \sum_{\substack{2\le m\le Y\\\operatorname{first}_D(m)\in J}}
             \frac1{m\log m}
 \ll\tau(1+\log\log(3Y)).
$$
Multiply (2) by the harmonic bound $1/H$ per point and sum the dyadic
intervals. Equations (2)--(3) give the $\tau/\varepsilon$ main term
and the stated $\tau\log\log X/(\varepsilon\eta)$ error. The excluded
fractions give $O(\varepsilon\log X+1/\eta)$, completing (1).

For fixed $\eta$, the infinite-family annulus was already naturally
null: it is the difference of two power-delayed unions with the same
density. The new content of (1) is its **finite uniformity** and explicit
error, allowing $\eta$ to decrease with $X$. Summing all decreasing
deficit bands still incurs an unbounded loss. The argument does not
justify interchanging that infinite sum with logarithmic density.

## A weighted one-prime-shadow bound

Let $P$ be a finite primitive set. For $q\in P$, define
$$
 A_q=\{p\text{ prime}:\exists r\in P,\ r<q,\ r\mid qp\},
 \qquad s_q=\sum_{p\in A_q}\frac1p.
$$
Then
$$
 \sum_{\substack{q\in P\\q\le X}}
          \frac{\omega(q)e^{-s_q}}q\le2H_{\lfloor X\rfloor}.
 \tag{4}
$$
For each prime $p\mid q$, assign the face $d=q/p$. For fixed $d$,
order its prime children $dp\in P$ increasingly. Every earlier child
$d\ell$ divides $(dp)\ell$, so
$$
 s_{dp}\ge\sum_{\substack{\ell<p\\d\ell\in P}}\frac1\ell.
$$
If the child weights are $w_j=1/p_j\le1/2$, the inequality
$w_j\le2(1-e^{-w_j})$ and telescoping imply
$$
 \sum_j w_j\exp\left(-\sum_{h<j}w_h\right)\le2.
$$
Thus each face contributes at most $2/d$. Summing over $d\le X/2$
proves (4); each $q$ is counted exactly $\omega(q)$ times.

An actual coherent first-kill quotient cannot be divisible by any prime
in $A_q$: otherwise a smaller generator would divide $n-b$. This is
additional information beyond primitive-modulus counting. However, no
simultaneous upper sieve has been proved that converts (4) into the
required harmonic bound. In particular, predecessor primes larger than
the relevant quotient interval cannot simply be treated as independent
arithmetic exclusions.

The [primitive atom obstruction](prime_block_obstructions.md#primitive-small-footprint-families-with-a-large-atom-kernel)
shows why the unsieved term $m=q$ cannot instead be bounded using only
primitivity and the full Haar footprint. A weighted shadow/sieve argument
is a provisional possibility, not an established next step.

## Separate phase maxima cannot be summed

There is a stronger obstruction to replacing the simultaneous problem
by individual quotient-sieve estimates. There are finite primitive
modulus sets $D$ with $\beta_D\to0$ and cutoffs $X$ for which
$$
 \frac1{\log X}\sum_{q\in D}
       \sup_{\alpha\in\widehat{\mathbb Z}}H_{E_q^\alpha}(X)
 \longrightarrow\infty.
 \tag{5}
$$
Here $E_q^\alpha$ is the actual first-kill set at $q$ in the coherent
system on $D$. The supremum may use a **different center for each
modulus**. Equation (5) is not a single-system harmonic anomaly.

Use the [prime-block construction](prime_block_obstructions.md#primitive-small-footprint-families-with-a-large-atom-kernel).
With $Y\to\infty$, set
$$
 L=\log\log Y,\qquad \mathcal P=\{p:L^3<p\le Y\},
 \qquad\lambda=\sum_{p\in\mathcal P}1/p,
 \qquad r=\left\lceil\lambda+\tfrac12\sqrt{\lambda\log\lambda}\right\rceil.
$$
For a sufficiently large fixed $C$, take **all** products of $r$
distinct pool primes that are at most $Y^C$, and set $X=Y^{2C}$.
The reciprocal-weight and upper-cutoff estimates proved in that note
give
$$
 \beta_D\ll1/\log\lambda\longrightarrow0,
 \qquad\sum_{q\in D}\frac1q
 \gg\frac{\log Y}{\log L\,L^{5/8}}.
 \tag{6}
$$
No lower cutoff is imposed on $D$; this ensures that every smaller
rank-$r$ product used next is still a generator.

Fix $q\in D$ and put
$$
 A_q=\{p\in\mathcal P:p\nmid q,\ p<P^+(q)\}.
$$
Choose $\alpha\equiv0\pmod q$. For $n=qt$, the earlier coherent
classes are avoided exactly when
$$
 t\not\equiv\alpha q^{-1}\pmod p\quad(p\in A_q).
 \tag{7}
$$
To prove necessity, for each $p\in A_q$ the generator
$q'=qp/P^+(q)$ is smaller than $q$. Matching its $p$-coordinate,
together with $\alpha\equiv0\pmod q$, makes $q'$ divide $qt-\alpha$.
Conversely, any earlier rank-$r$ generator introduces a prime
$p\not\mid q$ smaller than $P^+(q)$: otherwise replacing its removed
prime factors of $q$ by the introduced ones would increase the product.
If that generator divides $qt-\alpha$, this $p$ violates (7).

Independently choose the forbidden quotient residue at each $p\in A_q$
uniformly from $\{\lceil\sqrt p\rceil,\ldots,p-1\}$. CRT realizes
these choices by an integer center satisfying $\alpha\equiv0\pmod q$.
For $L^4\le t\le\sqrt Y$, primes $p>t^2$ cannot remove $t$.
For the remaining primes the hitting probability is at most
$1/(p-\lceil\sqrt p\rceil)$. The convergent correction product in
the [admissible-set argument](finite_sharp_counterexamples.md#admissible-sets-with-large-harmonic-weight)
and the elementary Euler-product bounds therefore imply
$$
 \Pr(qt\in E_q^\alpha)
 \gg\prod_{L^3<p\le t^2}(1-1/p)
 \gg\frac{\log L}{\log t}.
$$
All these hits are active, every predecessor is active there, and
$qt\le Y^{C+1/2}\le X$. Averaging over the choices gives
$$
 \sup_\alpha H_{E_q^\alpha}(X)
 \gg\frac{\log L}{q}
       \sum_{L^4\le t\le\sqrt Y}\frac1{t\log t}
 \gg\frac{L\log L}{q}.
$$
Summing and applying (6) proves (5), with a lower bound
$\gg L^{3/8}$.

Thus even optimal separate first-kill bounds, uniform in the coherent
center, cannot be summed to obtain the desired small-footprint result.
In this example the complete predecessor conditions already reduce to
the prime exclusions (7), so merely retaining composite predecessors
does not repair that particular strategy. A successful replacement
would have to use the common center simultaneously across moduli.
Neither such an estimate nor a synchronized counterexample was obtained.

## Simultaneous transport across a bounded divisor gap

The following bound uses one common center simultaneously, rather than
summing separate phase maxima. It applies directly to selected
first-kill cells and has no preparatory-period constant.

Let $D$ be finite, with coherent center $\alpha$, and let
$q(n)$ be the least covering modulus of an activated hit $n$.
Select cells $J\subseteq D$ of total Haar mass
$\tau=\sum_{q\in J}e_q$. For an integer $K\ge2$, set
$$
 T_{J,K}=\{n\in B:q(n)\in J,\ \exists m\ge1:
 q(n)\mid m,\ n/K\le m\le Kn,\ n\equiv\alpha\pmod m\}.
$$
Then, for integers $N\ge1$,
$$
 H_{T_{J,K}}(N)
 \le\tau\bigl(H_KZ_N+KZ_{KN}\bigr)
 \ll\tau K(1+\log K)H_N,
 \tag{8}
$$
where $Z_Y=\prod_{p\le Y}(1-1/p)^{-1}$.

**Proof.** Put
$$
 G_J=\{m\ge1:\operatorname{first}_D(m)\in J\},
$$
where the first generator is taken in the zero-residue multiples
system on $D$. The geometric valuation distribution gives
$$
 \sum_{\substack{m\le Y\\m\in G_J}}\frac1m\le Z_Y\tau.
 \tag{9}
$$
For this calculation retain the generators at most $Y$; their
selected first-kill masses sum to at most $\tau$. All their prime
supports are at most $Y$, so the smooth-integer law has exactly
their Haar divisibility probabilities.

Any witnessing $m$ belongs to $G_J$, with first generator exactly
$q(n)$. An earlier generator dividing $m$ would also cover $n$;
it would be active since it is smaller than $q(n)\le n$.

For witnesses $m\le n\le Km$, the sum of the weights of the positive
delayed progression points at a fixed $m$ is at most $H_K/m$.
Summing over $m\le N$ gives $H_KZ_N\tau$ by (9).
For witnesses $n<m\le Kn$, select one $m$ per $n$. This selection
is injective: a fixed $m$ has at most one positive root $n<m$
congruent to $\alpha$. Since $1/n\le K/m$, the second contribution
is at most $KZ_{KN}\tau$. The established estimate
$Z_Y\ll\log(2Y)$ completes (8). $\square$

For all cells together, one may allow **any** matching
$m\in M(D)$ in $[n/K,Kn]$, not necessarily a multiple of the
actual first-kill modulus. The exact multiples inequality gives
$$
 H_T(N)\le\beta\bigl(H_KH_N+KH_{KN}\bigr)
 \le\beta[H_K+K(1+\log K)]H_N,
 \tag{10}
$$
where $\beta=\mu(M(D))$. Use
$\sum_{m\in M(D),m\le Y}1/m\le\beta H_Y$ in the same two counts.

Taking $K\asymp\tau^{-1/2}$ in (8) shows that outside normalized
harmonic mass $O(\sqrt\tau\log(1/\tau))$, any selected-cell anomaly
has no matching multiple of its first-kill modulus within factor
$K$ of the sampled integer. Equivalently, all ordinary divisors
of the profinite cofactor $(n-\alpha)/q(n)$ avoid
$[n/(Kq(n)),Kn/q(n)]$. This is a necessary divisor-gap condition,
not a bound for the remaining points. It does not prove the coherent
small-footprint estimate or logarithmic density.
