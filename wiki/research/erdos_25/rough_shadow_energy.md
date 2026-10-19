---
name: research/erdos_25/rough_shadow_energy
desc: Globally private canonical endpoints can have bounded total rough-shadow measure but unbounded second moment, ruling out a uniform quadratic shadow charge.
tags: [endpoints, obstructions, second-moments]
sources: []
created: 2026-09-22T12:05:00Z
updated: 2026-09-24T22:13:01Z
---


# research/erdos_25/rough_shadow_energy

***

A different attempted proof attached a rough-quotient shadow to each
private endpoint and sought an averaged packing estimate. The
[earlier obstruction](unresolved_estimates.md#affine-rough-shadows-can-overlap-with-arbitrarily-large-multiplicity)
rules out bounded pointwise overlap. The construction below also rules
out a uniform second-moment substitute, even with globally private
positive witnesses and bounded total shadow measure.

## Statement

There are finite distinct-modulus singleton families with globally
private endpoints $r_q\in[q,2q)$ for which the rough shadows
$$
 S_q=\{a_q+qt:t\ge1,\ P^-(t)>q\},\qquad P^-(1)=\infty,
$$
obey
$$
 \sum_q d(S_q)\le C,
 \qquad
 \int\left(\sum_q\mathbf1_{S_q}\right)^2\,d\mu\longrightarrow\infty.
 \tag{1}
$$
In the integral, each shadow denotes its full periodic congruence
version; its natural density and pair intersection densities are
unchanged by discarding the finite inactive part. Thus a uniform bound
$\int Z^2\le C\int Z$, or even a uniform bound on $\int Z^2$ when
$\int Z$ is bounded, is false for this proposed shadow assignment.

## A private fixed-rank family

Let $\mathcal P$ be the odd primes at most $y$, and put
$\lambda=\sum_{p\in\mathcal P}1/p$. For an integer $k\ge1$, let
$D_k$ be all products of exactly $k$ distinct primes of $\mathcal P$.
Use $a_q=q-1$ and $r_q=2q-1$.

Every $q$ is odd, and $D_k$ is primitive. If $r_p$ belongs to the
$q$-cylinder, then $q\mid2p$, hence $q\mid p$. Equal squarefree
rank forces $p=q$. The witnesses are therefore globally private,
not just private relative to earlier moduli. Activation is exact at
$r_q=2q-1$.

One shadow has density
$$
 d(S_q)=\frac1q\prod_{p\le q}(1-1/p)\asymp\frac1{q\log q}.
 \tag{2}
$$
The constants follow from the
[elementary Euler-product bounds](coprime_entropy.md#elementary-prime-estimates).

Uniformly in $k$ and $y$,
$$
 \sum_{q\in D_k}\frac1{q\log q}\le3.
 \tag{3}
$$
Indeed, write $A(t)=\sum_{p\ge3}p^{-1-t}$ for $t>0$ and use
$1/(q\log q)=\int_0^\infty q^{-1-t}\,dt$. The elementary
symmetric sum is at most $A(t)^k/k!$. For $0<t\le1$,
$$
 A(t)\le\log\zeta(1+t)\le\log(1+1/t)\le\log(1/t)+\log2.
$$
Substitution $u=\log(1/t)$ bounds its integral by
$$
 \frac1{k!}\int_0^\infty(u+\log2)^k e^{-u}\,du\le2.
$$
For $t\ge1$, put $C_0=\sum_{n\ge3}n^{-2}<1$; then
$A(t)\le C_0 3^{1-t}$, whose $k$th power divided by $k!$
has integral $C_0^k/(k!k\log3)<1$. This proves (3), and hence
the bounded mean in (1).

## Pair intersections remain large

Let $g=(q,p)$, $q=gu$, $p=gv$, and $L=\operatorname{lcm}(q,p)$.
The two cylinders require $n+1=Lz$. Their quotient variables in
the shadows are respectively $vz-1$ and $uz-1$.
At the prime $2$, both leading coefficients are odd, so the two
forbidden roots coincide. At an odd prime at most $\min(q,p)$,
at most two roots are forbidden; at primes between the two cutoffs,
at most one is forbidden. A zero leading coefficient gives the
constant $-1$, and excludes nothing. CRT therefore yields
$$
 \mu(S_q\cap S_p)
 \ge\frac{c}{L\log q\log p}.
 \tag{4}
$$
For detail, the conditional probability given $n+1\in L\widehat{\mathbb Z}$
is bounded below by
$$
 \frac12\prod_{3\le\ell\le\min(q,p)}(1-2/\ell)
 \prod_{\min(q,p)<\ell\le\max(q,p)}(1-1/\ell),
$$
where the products are over primes. The first product is bounded below
by an absolute positive constant times the square of
$\prod_{\ell\le\min(q,p)}(1-1/\ell)$, since the correction
ratios form a convergent positive product. The displayed quantity is
therefore $\gg1/(\log q\log p)$, proving (4).

## Selecting a rank with large gcd energy

Over all pairs of squarefree products of primes from $\mathcal P$,
the sum of $1/\operatorname{lcm}(q,p)$ is
$$
 Z=\prod_{\ell\in\mathcal P}(1+3/\ell)
   \asymp(\log y)^3.
$$
Normalize these weights to a probability law. At each prime the four
states (neither product, first only, second only, both) have weights
$1,1/\ell,1/\ell,1/\ell$, independently between primes.
If $K_1,K_2$ are the two ranks, their difference has independent
symmetric increments, with probabilities $1/(\ell+3)$ each for
$+1$ and $-1$. Its characteristic function is
$$
 \varphi(t)=\prod_{\ell\in\mathcal P}
       \left(1-\frac{2(1-\cos t)}{\ell+3}\right).
$$
Every factor is positive for real $t$. For $|t|\le\lambda^{-1/2}$
and large $\lambda$, the product is at least an absolute positive
constant. Fourier inversion consequently gives
$$
 \Pr(K_1=K_2)\ge c/\sqrt\lambda.
$$
Also $\mathbb E K_i\le2\lambda$, and the exponential-moment bound
at parameter $\log2$ gives
$$
 \Pr(K_i>4\lambda)\le\exp(-(4\log2-2)\lambda).
$$
The probability of rank zero for both products is $1/Z$, also
negligible. Pigeonholing among the at most $4\lambda$ positive
ranks up to $4\lambda$ supplies one $k$ with
$$
 1\le k\le4\lambda,
 \qquad
 \sum_{q,p\in D_k}\frac1{\operatorname{lcm}(q,p)}
 \ge\frac{cZ}{\lambda^{3/2}}.
 \tag{5}
$$
Every member of $D_k$ satisfies $\log q\le k\log y$.
Equations (4)--(5) now give
$$
 \int\left(\sum_{q\in D_k}\mathbf1_{S_q}\right)^2d\mu
 \ge\frac{cZ}{\lambda^{3/2}k^2(\log y)^2}
 \gg\frac{\log y}{(\log\log y)^{7/2}}\longrightarrow\infty.
$$
Together with (2)--(3), this proves (1).

The residues are all the fixed signed center $-1$, a solved logarithmic
density regime. The construction refutes this specific quadratic
shadow charge; it does not refute endpoint nullity, the primitive-type
reciprocal sum target, or a different fractional allocation of shadows.
