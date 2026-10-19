---
name: research/erdos_25/rational_phase_overlap
desc: Uniform cross-phase overlap and conditional negative correlation for rational residue patterns; the arithmetic endpoint transfer remains open.
tags: [rational-slopes, endpoints, partial-results]
sources: []
created: 2026-09-22T06:10:00Z
updated: 2026-09-24T22:13:01Z
---


# research/erdos_25/rational_phase_overlap

***

These lemmas isolate where the second-moment argument for long rational
approximation epochs loses control. They do not prove logarithmic
endpoint nullity for arbitrary irrational slopes.

## Cross-phase second moments

Let $(A,b)=1$, $b\ge1$, and put
$$
 a_q=\lfloor Aq/b\rfloor,\qquad
 u_q=Aq-ba_q\in\{0,\ldots,b-1\},\qquad C_q=[a_q]_q.
$$
For every $D\subseteq[Q,2Q)\cap\mathbb N$, with integer $Q\ge2$,
$$
 \sum_{\substack{q,r\in D\\u_q\ne u_r}}
                    \mu(C_q\cap C_r)
 \ll1+\frac{b\log(2b)}Q.
 \tag{1}
$$
Thus, when $Q$ is large compared with $b\log b$, large second moments
can arise only within individual phases.

For a compatible pair write $g=(q,r)$. The identity
$$
 b(a_q-a_r)=A(q-r)-(u_q-u_r)
$$
implies $g\mid u_q-u_r$; different phases therefore require $g<b$.
Set $k=|q-r|/g$. Compatibility also gives
$$
 k<Q/g,\qquad \|Ak/b\|<1/g.
$$
One period modulo $b$ contains at most $3b/g$ qualifying residues,
because $A$ is invertible modulo $b$. Hence at most
$3Q/g^2+3b/g$ values of $k\le Q/g$ qualify. Each pair $(g,k)$ gives
at most $4Q/g$ ordered pairs, each of intersection measure at most
$g/Q^2$. Summation bounds (1) by
$$
 \frac4Q\sum_{g<b}\left(\frac{3Q}{g^2}+\frac{3b}{g}\right)
 \le2\pi^2+\frac{12b(1+\log b)}Q.
$$
For $b=1$ the cross-phase sum is empty.

## Negative correlation after exposing small primes

For $0\le u<b$, let $U_u$ be a finite or countable union of cylinders
satisfying
$$
 ba\equiv-u\pmod q.
$$
Repeated moduli are permitted in this lemma. Expose all $p$-adic
coordinates with $p\le b$, writing their sigma-algebra as $\mathcal F_b$.
Set
$$
 \beta_u=\Pr(U_u\mid\mathcal F_b),\qquad M=\sum_{u<b}\beta_u.
$$
Then, almost surely,
$$
 \Pr(U_u\cap U_v\mid\mathcal F_b)\le\beta_u\beta_v
       \quad(u\ne v),
 \tag{2}
$$
and
$$
 \sum_{u<b}\min(\beta_u,1/b)
 \le2\Pr\left(\bigcup_{u<b}U_u\mid\mathcal F_b\right).
 \tag{3}
$$

Fix the exposed coordinates. At a prime $p>b$, the phase centers
$-u/b\in\mathbb Z_p$ are distinct modulo $p$. For a Haar coordinate
$X_p$, at most one of the matching depths
$T_{p,u}=v_p(X_p+u/b)$ is positive. For increasing functions $f,g$
of the depths in two different phases, write
$f=f(0)+f_+$ and $g=g(0)+g_+$. Their nonnegative remainders satisfy
$f_+g_+=0$. This proves their negative correlation in one coordinate.
Induction over independent prime coordinates extends it to increasing
functions of the two depth vectors. The conditional phase-union events
are increasing functions of precisely those vectors. This proves (2)
for finite unions; monotone convergence handles countable unions.

For $Z=\sum_u\mathbf1_{U_u}$, (2) gives, conditionally,
$\mathbb EZ=M$ and $\mathbb EZ^2\le M+M^2$. Cauchy--Schwarz yields
$$
 \Pr(Z>0\mid\mathcal F_b)\ge M/(1+M).
$$
Finally $\sum_u\min(\beta_u,1/b)\le\min(M,1)\le2M/(1+M)$,
proving (3).

If an old survivor set $S$ has a period whose prime factors are all at
most $b$, it is $\mathcal F_b$-measurable. Thus
$$
 \int_S\sum_{u<b}\min(\beta_u(x),1/b)\,d\mu(x)
 \le2\mu\left(S\cap\bigcup_{u<b}U_u\right).
 \tag{4}
$$
The constant is independent of the period, and no coprimality with $b$
is needed.

## The unresolved arithmetic step

For a fixed endpoint quotient $\ell\ge1$, the rational phase relation is
$$
 r_q=\ell q+a_q=\frac{(\ell b+A)q-u_q}{b}.
$$
To exploit (4), one would need a uniform bound transferring the harmonic
mass of selected endpoints $r_q\in S$ into those capped conditional
Haar masses. No such bound was proved. The affine transformation of
the old survivor set cannot be ignored, and unconditioned phase bounds
do not automatically apply inside each small-prime fiber. In particular,
(1)--(4) do not bridge the gap left by the
[Brjuno theorem](irrational_slope_endpoints.md#why-the-remaining-irrational-logarithmic-case-is-not-settled).
