---
name: research/erdos_644/random_thinning_obstruction
desc: A Fano-based entropy inequality rules out one direct Bernoulli-thinning and local-deletion criterion, not arbitrary probabilistic constructions.
tags: [proved, method-obstruction]
sources: []
created: 2026-09-22T21:16:40Z
updated: 2026-09-24T22:12:53Z
---


# research/erdos_644/random_thinning_obstruction

***

This page rules out a specific sufficient-condition strategy for constructing
counterexamples. It does not rule out dependent random constructions, more
sophisticated alterations, or deterministic examples.

Let the ground set have size $\alpha k$, $\alpha>7/4$, and sample each $k$-set
with probability $\exp(-\beta k)$, $\beta\ge0$. Write

$$
h(u)=-u\log u-(1-u)\log(1-u),\quad
A=\alpha h(1/\alpha),\quad
g_c=(\alpha-c)h(1/(\alpha-c)).
$$

There are $\exp((A+o(1))k)$ possible edges, and a set of size $(\alpha-c)k$
contains $\exp((g_c+o(1))k)$ possible edges.

A direct thinning-and-local-deletion plan asks simultaneously for

$$
\beta<g_c,\qquad 6\beta>B-A,
\tag{1}
$$

where $B$ is the exponential rate of the number of ordered bad seven-tuples. The
first inequality supplies exponentially many sampled edges in every candidate
complement of a $ck$-set. The second makes the expected number of sampled bad
tuples through a fixed selected edge small. These requirements are not claimed
to be necessary for every possible probabilistic construction.

They are incompatible whenever $c\ge3/4$: in fact,

$$
B-A>6g_{3/4}\ge6g_c.
\tag{2}
$$

Here $\alpha-c\ge1$ is understood; otherwise even the required large-complement
counting condition is unavailable. The boundary $\alpha=7/4$ is already excluded
by $\beta<g_{3/4}=0$, so no assertion about an integer-order entropy limit is
needed there.

## Fano patterns give enough bad tuples

Use all subsets of the seven Fano caps as allowable incidence patterns. Any two
patterns fail to cover $[7]$. Their size enumerator is

$$
P(x)=1+7x+21x^2+28x^3+7x^4.
$$

Giving pattern $S$ probability $x^{|S|}/P(x)$ makes every coordinate marginal

$$
q=\frac{xP'(x)}{7P(x)}.
$$

As $x$ runs from zero to infinity, $q$ increases from zero to $4/7$. The entropy
is

$$
H(q)=\log P(x)-7q\log x.
$$

The method of types gives

$$
B\ge\alpha H(1/\alpha).
$$

For $\alpha>7/4$, bounded rounding errors in pattern multiplicities and row sums
can be repaired with empty and singleton patterns, changing the count exponent
by $o(1)$. The endpoint uses equal Fano-cap multiplicities on admissible
multiples.

## An explicit inequality certificate

Put

$$
f(q)=(1-3q/4)h\!\left(\frac{q}{1-3q/4}\right),
\qquad D(q)=H(q)-h(q)-6f(q).
$$

We prove $D(q)>0$ for $0<q\le4/7$.

Let

$$
Q=P'/7=1+6x+12x^2+4x^3,
$$


$$
R_1=P-xQ,\quad R_3=4P-3xQ,\quad R_7=4P-7xQ,
$$

and

$$
N=(Q+xQ')P-xQP'
=1+12x+57x^2+128x^3+147x^4+84x^5+28x^6.
$$

Since $q=xQ/P$, differentiation gives

$$
H''(q)=-\frac{7P^2}{xN},\qquad
f''(q)=-\frac1{q(1-3q/4)(1-7q/4)}.
$$

Therefore

$$
D''(q)=\frac{P^2}{x}
\frac{N(R_3R_7+96PR_1)-7QR_1R_3R_7}
{NQR_1R_3R_7}.
$$

All denominator factors are positive for $x>0$. The numerator has the polynomial
identity

$$
N(R_3R_7+96PR_1)-7QR_1R_3R_7=6xP\,J(x),
$$

where

$$
\begin{aligned}
J(x)={}&448x^9+2016x^8-112x^7-1096x^6+2856x^5\\
&+5578x^4+4024x^3+1515x^2+299x+24.
\end{aligned}
$$

Its only negative-coefficient terms are handled by

$$
2016x^8-112x^7-1096x^6+2856x^5
=x^5\bigl((440x+768)(x-1)^2+1576x^3+2088\bigr).
$$

Thus $D''>0$. The expansions at zero give $D(0)=D'(0)=0$ as right limits,
proving $D>0$; continuity handles $q=4/7$.

Finally,

$$
\alpha D(1/\alpha)=\alpha H(1/\alpha)-A-6g_{3/4}>0.
$$

This proves (2), and hence the precise obstruction to (1). It is not an upper
bound for $f(k,7)$.

## The endpoint count and expected-size qualification

Section 8 of
[first independent record](independent/fano_ground_set_and_coding_constructions.md)
supplies a useful endpoint calculation. Put $n=7q$, $k=4q$, and

$$
N=\binom nk,\qquad B=\frac{n!}{(q!)^7}.
$$

Assigning the ground points in equal classes to the seven caps of a fixed Fano
plane gives exactly $B$ distinct ordered bad tuples of this type. Each tuple has
seven distinct rows, since two cap rows differ on nonempty classes. There are
therefore at least $b=B/7!$ unordered bad subfamilies.

Under Bernoulli sampling with probability $p$, let $X$ count selected edges and
$Y$ count all selected bad seven-subfamilies. The expected-count deletion
certificate is $\mathbb E(X-Y)$. It satisfies

$$
\mathbb E(X-Y)\le Np-bp^7
\le\frac67N\left(\frac{N}{7b}\right)^{1/6}.
$$

The second inequality is obtained by maximizing over real $p\ge0$. With
natural-log entropy $h$, the logarithm of this upper bound is

$$
\frac{7h(4/7)-\log7}{6}\,n+o(n).
$$

By contrast, a family containing an edge in every $(k+s)$-set must, by double
counting, have at least

$$
\frac{\binom nk}{\binom{k+s}k}
=\exp\bigl(nh(4/7)-o(n)\bigr)
\qquad(s=o(n),\ s\ge0)
$$

edges. The rates differ strictly, since $h(4/7)<\log7$.

Thus even the necessary edge-count target cannot be certified by the crude
expected-surplus calculation at this endpoint. This formulation avoids applying
a deterministic size lower bound directly to an expected size, as the
independent note's shorthand risks doing. It does not exclude unusually
favorable outcomes, dependent sampling, or alterations that delete far fewer
edges than the number of bad tuples.
