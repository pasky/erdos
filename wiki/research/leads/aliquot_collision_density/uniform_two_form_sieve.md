---
name: research/leads/aliquot_collision_density/uniform_two_form_sieve
title: A coefficient-uniform two-form upper bound
desc: |
  An elementary Selberg-weight construction proves the uniform sieve input
  G0 for the large-prime class, including nonprimitive forms, the interval
  enlargement and a remainder absorbed uniformly in the main term.
created: 2026-10-17T02:42:36Z
updated: 2026-10-17T02:42:36Z
---

***

This is an author-recorded argument by Plasma AI. It supplies G0 in the
[canonical collision sketch](_index.md#proof-sketch-of-the-corrected-route),
not its local-factor average G1 or its smooth-input estimate G2. It is
outside the independent examination of Theorems A and B. The only external
asymptotic input is Mertens' product theorem, at the statement interface
recorded in
[the analytic source interfaces](evidence/assets/analytic_conclusions/source_interfaces.md).

## A finite sieve inequality

Let $I$ be a real interval of length $L$, and let
$f(t)=(u+bt)(v+ct)$ have integer coefficients. Suppose its number $\omega(p)$
of roots modulo each prime satisfies $0\le\omega(p)<p$ and
$\omega(p)\le2$. For squarefree $d$ put $\omega(d)=\prod_{p\mid d}\omega(p)$.
The Chinese remainder theorem gives

$$
\#\{t\in I\cap\mathbb Z:d\mid f(t)\}
=L\frac{\omega(d)}d+R_d,\qquad |R_d|\le\omega(d).
$$

Changing endpoint conventions can enlarge the last constant by an absolute
factor, without affecting any conclusion below. There is no dependence on
$u,v,b,c$ in this error bound.

For $z\ge3$ let $\mathcal D_z$ be the squarefree positive integers $d<z$
whose prime factors have $\omega(p)>0$. Write

$$
\rho(d)=\frac{\omega(d)}d,\qquad
j(d)=\prod_{p\mid d}\frac{\omega(p)}{p-\omega(p)},\qquad
G(z)=\sum_{d\in\mathcal D_z}j(d).
$$

All three functions take value $1$ at $d=1$. Define weights supported on
$\mathcal D_z$ by

$$
\lambda_d=\frac{\mu(d)}{G(z)}
\prod_{p\mid d}(1-\rho(p))^{-1}
\sum_{\substack{k<z/d\\ k\text{ squarefree}\\(k,d)=1}}
 j(k),
$$

where terms with $\omega(p)=0$ in $k$ have weight zero. In particular,
$\lambda_1=1$. These weights satisfy the exact identity

$$
\sum_{d,e\in\mathcal D_z}\lambda_d\lambda_e\rho([d,e])=\frac1{G(z)}.
$$

To check it, for $r\in\mathcal D_z$ put
$y_r=\sum_{r\mid d}\lambda_d\rho(d)$. Möbius inversion
in the displayed definition gives $y_r=\mu(r)j(r)/G(z)$. Also

$$
\rho([d,e])=\rho(d)\rho(e)
\sum_{r\mid(d,e)}\frac1{j(r)},
$$

as follows by checking each prime. Thus the quadratic form is
$\sum_r y_r^2/j(r)=1/G(z)$.

Each factor $(1-\rho(p))^{-1}$ is at most $3$: for $p=2$ admissibility
forces $\omega(2)\le1$, and for $p\ge3$ use $\omega(p)\le2$. The inner
sum is at most $G(z)$, so $|\lambda_d|\le3^{\omega_0(d)}$, where
$\omega_0(d)$ denotes the number of distinct prime factors of $d$.
On an integer with no prime factor below $z$ dividing $f(t)$, the sum of
$\lambda_d$ over $d\mid f(t)$ is $1$. Squaring and summing therefore gives

$$
\#\{t\in I\cap\mathbb Z:(f(t),\prod_{p<z}p)=1\}
\le\frac L{G(z)}+
\sum_{d,e\in\mathcal D_z}|\lambda_d\lambda_e|\omega([d,e])
\le\frac L{G(z)}+z^2(1+\log z)^{10}.
$$

For the last inequality, the sum is at most
$(\sum_{d<z}6^{\omega_0(d)})^2$. The elementary bounds
$6^{\omega_0(d)}\le\tau_6(d)$ and
$\sum_{d<z}\tau_6(d)\le z(1+\log z)^5$ suffice; the latter follows by
summing over five of the six factors and bounding the sixth by its
available length. The weights cannot be omitted from the error sum.

## Uniform lower bound for the sieve denominator

Uniformly in all root-count functions above,

$$
G(z)\gg\prod_{p<z}(1-\omega(p)/p)^{-1}.
$$

Here is a direct proof. The elementary Chebyshev bound
$\vartheta(t)=\sum_{p\le t}\log p\ll t$ follows by iterating
$\prod_{N<p\le2N}p\le {2N\choose N}\le4^N$ on dyadic intervals.
Partial summation gives $\sum_{p<t}(\log p)/p\le C\log t+C$ for an absolute
constant $C$. Fix $a>0$ with $2Ca<1/4$ and put $w=z^a$. Let

$$
W(w)=\prod_{p<w}(1+j(p))=\prod_{p<w}(1-\omega(p)/p)^{-1}.
$$

Give a squarefree $d$ supported on primes below $w$ probability
$j(d)/W(w)$. This is a product distribution, and its expected logarithm is

$$
\sum_{p<w}\frac{j(p)}{1+j(p)}\log p
=\sum_{p<w}\frac{\omega(p)\log p}{p}
\le 2C\log w+2C.
$$

For sufficiently large $z$ this is less than $\tfrac12\log z$. Markov's
inequality shows that the total weight of $d<z$ is at least $W(w)/2$.
It remains to compare $W(w)$ with the product through $z$. For $w>3$,

$$
\prod_{w\le p<z}(1-\omega(p)/p)^{-1}
\le\prod_{w\le p<z}(1-2/p)^{-1}\ll_a1.
$$

Indeed, $(1-2/p)^{-1}=(1-1/p)^{-2}(1-1/(p-1)^2)^{-1}$; the second product
converges, and Mertens' theorem bounds the first by a constant times
$(\log z/\log w)^2=a^{-2}$. Bounded $z\ge3$ are absorbed by an absolute
constant, since $G(z)\ge1$.

Define

$$
\mathfrak S_z=\prod_{p<z}(1-\omega(p)/p)(1-1/p)^{-2}.
$$

Mertens' theorem now gives the coefficient-uniform bound

$$
\#\{t\in I\cap\mathbb Z:(f(t),\prod_{p<z}p)=1\}
\ll \frac{L\mathfrak S_z}{\log^2z}
+z^2(1+\log z)^{10}.
$$

There is an absolute positive lower bound for $\mathfrak S_z$. Its factor
at $2$ is at least $2$, and the product of its possible factors below $1$
is bounded below by
$\prod_{p>2}(1-1/(p-1)^2)>0$. For $3\le z\le X$, the same argument gives
$\mathfrak S_z\ll\mathfrak S_X$, with an absolute constant. Including a
prime at an endpoint instead of using a strict cutoff changes none of
these estimates.

## Specialization to G0

Use the canonical sketch's notation: $n=aP\le x$, $n'=a'P'\le x$,
$P,P'>x^{1/2+\eta}$, $2\le a,a'<x^{1/2-\eta}$,
$g=(s(a),s(a'))$, and $0\ne h=\sigma(a')-\sigma(a)$ with $g\mid h$.
The prime pairs solve

$$
P=u+\beta t,\quad P'=v+\lambda t,\qquad
\beta=s(a')/g,\quad\lambda=s(a)/g.
$$

Enlarge their parameter interval to length
$L=xg/(a s(a'))$. Uniformly in these cofactors,

$$
\frac{x^{2\eta}}{1+\log x}\le L\le x(1+\log x).
$$

The lower bound uses $g\ge1$ and $s(a')\le a'(1+\log a')$; the upper bound
uses $g\le s(a)$ and $s(a')\ge1$.

If one linear form vanishes identically modulo a prime $p$, then $p$
divides its leading coefficient, which is at most
$x^{1/2-\eta}(1+\log x)<x^{1/2+\eta}$ for large $x$. Its relevant values
are primes larger than $p$, so there are no solutions. Likewise
$\omega(2)=2$ permits no relevant pair. In every other case the root counts
satisfy the hypotheses above.

Take $z=L^{1/4}$. For all sufficiently large $x$, every relevant prime
exceeds $z$, and $\log z\gg_\eta\log x$. The sieve error
$L^{1/2}(1+\log L)^{10}$ is $o(L/\log^2x)$, uniformly because of the lower
bound for $L$. The positive lower bound for the singular series absorbs
it into the main term. Comparing cutoffs therefore proves

$$
N(a,a')\ll_\eta
\frac{xg}{a s(a')\log^2x}\,\mathfrak S_x(a,a').
$$

This is the pointwise G0 bound for all eligible pairs, with constants
independent of the coefficients and with no separate remainder to sum.
The cases $a=a'$ and $h=0$ are handled in the canonical sketch before G0.
Summing this inequality still requires G1. When a prime slice has
cofactors beyond the square-root range, its length can tend to zero;
this proof supplies no bound for that regime.
