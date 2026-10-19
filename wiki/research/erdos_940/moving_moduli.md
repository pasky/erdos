---
name: research/erdos_940/moving_moduli
title: Uniform lattice counting and moving-modulus quintic means
desc: Quintic first-moment bounds for moving moduli and intervals, and equidistribution under fixed continuous root-phase weights.
tags: []
sources: []
created: 2026-09-22T03:06:14Z
updated: 2026-09-22T03:06:14Z
---


# Uniform lattice counting and moving-modulus quintic means

***

## Status

The exact inequalities below are proved and author-recorded. They extend the
[fixed-progression quintic theorem](quintic_first_moment_barrier.md) to moving
moduli and intervals. They remain statements about **representation counts**,
not distinct represented values, and do not decide either unresolved question
for $S_5$.

## An exact lattice bound

Let $r\ge1$ be an integer, let $d_i>0$ be integers, and put


$$
F_{\mathbf d}(\mathbf x)=\sum_{i=1}^r d_i x_i^r,\qquad
V_{\mathbf d}=\Gamma(1+1/r)^r\prod_i d_i^{-1/r},\qquad
\kappa_{\mathbf d}=\left(\sum_i d_i\right)^{1/r}.
$$


For $M\ge1$ and an integer $a$, write


$$
\rho_M(a;\mathbf d)=M^{1-r}
\#\{\mathbf b\bmod M:F_{\mathbf d}(\mathbf b)\equiv a\pmod M\},
$$


and let $R_{\mathbf d}(X;a,M)$ count positive integral $\mathbf x$ with
$F_{\mathbf d}(\mathbf x)\le X$ in this target class. For every real $X\ge0$,


$$
\frac{\rho_M V_{\mathbf d}}M
\bigl(X^{1/r}-\kappa_{\mathbf d}M\bigr)_+^r
\le R_{\mathbf d}(X;a,M)
\le\frac{\rho_M V_{\mathbf d}}M
\bigl(X^{1/r}+\kappa_{\mathbf d}M\bigr)^r.
\tag{1}
$$


**Proof.** Use the weighted norm
$\|\mathbf z\|_{\mathbf d}=(\sum_i d_i|z_i|^r)^{1/r}$. The volume of its
radius-$t$ ball in the positive orthant is $V_{\mathbf d}t^r$.

Fix one admissible residue vector. Attach the disjoint cubes $\mathbf q+[0,M)^r$
to its positive lattice points $\mathbf q$ of norm at most $t=X^{1/r}$. Every
such cube lies in the positive ball of radius $t+\kappa_{\mathbf d}M$, proving
the upper bound for this residue vector.

For the lower bound, take any positive real vector of norm at most
$(t-\kappa_{\mathbf d}M)_+$ and round each coordinate upwards to the least
positive integer in the prescribed residue class. The resulting lattice point
has norm at most $t$. Each lattice point has preimage volume at most $M^r$. Thus
the number of counted points is at least
$V_{\mathbf d}(t-\kappa_{\mathbf d}M)_+^r/M^r$. Summing over the
$\rho_M M^{r-1}$ admissible residue vectors proves (1).

No constants in (1) depend implicitly on $a$ or $M$.

## Consequence for the finite quintic certificate family

Use the finite set $\mathcal E$ and canonical family $\mathcal C$ of the
[quintic first-moment proof](quintic_first_moment_barrier.md):


$$
\mathcal E=\{p\le1000:p\text{ prime},\ p\ne5,\ p\not\equiv1\pmod5\},
$$


and each prime exponent in a member of $\mathcal C$ is $0,6,7,8$, or $9$. That
proof establishes the finite coefficient inequality


$$
\frac1{120}\sum_{\mathbf d\in\mathcal C^5}
V_{\mathbf d}\rho_M(a;\mathbf d)>\Lambda:=\frac{429}{400}
\tag{2}
$$


for **every** $M,a$, not merely after taking a fixed-modulus limit. Its finite
certificate is used as established here, without a new computation.

Put


$$
\kappa=5^{1/5}\prod_{p\in\mathcal E}p^{9/5}.
$$


Then $\kappa_{\mathbf d}\le\kappa$ for all tuples in this family. Canonical
uniqueness and the upper bound $120$ on the number of orderings of a
five-element multiset give


$$
U_5(X;a,M)\ge
\Lambda\frac XM
\left(1-\frac{\kappa M}{X^{1/5}}\right)_+^5.
\tag{3}
$$


The inequality is strict whenever the bracket is positive. Hence uniformly for
any moving moduli $M=o(X^{1/5})$ and residues $a$,


$$
\liminf\frac M X U_5(X;a,M)\ge\frac{429}{400}>1.
\tag{4}
$$


In fact a below-one first moment remains impossible for all $M\le cX^{1/5}$ with
any fixed


$$
0<c<\kappa^{-1}\left(1-\left(\frac{400}{429}\right)^{1/5}\right).
$$


The constant is extremely small but positive and independent of $X,a,M$.

## Moving intervals

Let $0\le A<B$ and $H=B-A$. Subtract the upper bound (1) at $A$ from the lower
bound at $B$, using the same finite coefficient family. This gives


$$
U_5((A,B];a,M)\ge\frac\Lambda M
\left[\bigl(B^{1/5}-\kappa M\bigr)_+^5
-\bigl(A^{1/5}+\kappa M\bigr)^5\right]_+.
\tag{5}
$$


Again it is strict if the displayed bracket is positive. Write $h=\kappa M$ and
suppose $h\le B^{1/5}$. The mean-value theorem gives


$$
B-(B^{1/5}-h)^5\le5hB^{4/5},
\qquad
(A^{1/5}+h)^5-A\le80hB^{4/5}.
$$


Thus the inner difference in (5) is at least $H-85\kappa M B^{4/5}$. In
particular,


$$
H\ge3400\kappa M B^{4/5}
\quad\Longrightarrow\quad
U_5((A,B];a,M)>
\frac{16731}{16000}\frac HM>\frac HM.
\tag{6}
$$


The hypothesis implies $h\le B^{1/5}/3400$, so the preceding bound is
applicable. More generally the liminf in (4), with $X$ replaced by the interval
length $H$, is at least $429/400$ whenever $H/(MB^{4/5})\to\infty$.

These estimates exclude a below-one first-moment argument throughout these
ranges. They say nothing comparable when $M$ is larger than the coordinate scale
or the interval is shorter than the boundary error, and they do not rule out
arguments exploiting repeated representations.

## Aligning finitely many axis intercepts does not force a gap

A different proposed gap construction was to make all fractional parts
$(n/d)^{1/5}$, for a finite collection of cores, approach integers from a
prescribed side. The following exact statement shows why qualitative alignment
alone cannot work.

**Proposition.** For any finite set $D$ of canonical fifth-power cores, there is
a positive integer $q=b^5+4$ such that


$$
\left(\left\{(qm^5/d)^{1/5}\right\}\right)_{d\in D},\qquad m\ge1,
\tag{7}
$$


is equidistributed in the $|D|$-dimensional unit torus. Nevertheless every
target $qm^5$ is a sum of five positive fifth powers.

**Proof.** Let $P_D$ denote the primes supporting $D$ and let


$$
K=\mathbb Q(p^{1/5}:p\in P_D).
$$


The monomials $\prod_{p\in P_D}p^{j_p/5}$, $0\le j_p<5$, form a basis over
$\mathbb Q$. To check the degree, adjoin $5^{1/5}$ first if needed, then the
remaining prime radicals one at a time. Before adjoining $p^{1/5}$, the
preceding field is unramified at the fresh prime $p$: the discriminants of the
previous defining polynomials are supported on $5$ and their respective defining
primes, and composita of unramified extensions remain unramified. Therefore
$T^5-p$ is Eisenstein at any prime above $p$, and each adjunction has degree
five. The first adjunction is ordinary Eisenstein over $\mathbb Q$.

For a canonical core the exponents are $0,6,7,8,9$, giving distinct residues
modulo five. Thus distinct $d^{-1/5}$, $d\in D$, are nonzero rational multiples
of distinct basis monomials, and are linearly independent over $\mathbb Q$.

Set $P=\prod_{p\in P_D\cup\{2,5\}}p$ and $b_0=2P$. Choose a prime
$\ell\mid 8P^5+1$. Then $\ell\nmid5P$ and $\ell\mid b_0^5+4$. The derivative of
$f(T)=T^5+4$ at $b_0$ is a unit modulo $\ell$. If $v_\ell(f(b_0))=1$, take
$b=b_0$; otherwise take $b=b_0+\ell$. Expansion modulo $\ell^2$ gives
$v_\ell(q)=1$ for $q=b^5+4$ in either case.

The field $K$ is unramified at $\ell$, so $q^{1/5}\notin K$, by valuation.
Consequently


$$
1,\quad (q/d)^{1/5}\quad(d\in D)
$$


are linearly independent over $\mathbb Q$: a relation with nonzero constant term
would put $q^{1/5}$ in $K$, whereas a relation with zero constant term
contradicts the independence of the core radicals. The geometric-series formula
for each nontrivial integer Fourier character, followed by Fourier
approximation, proves equidistribution of (7).

Finally,


$$
qm^5=(bm)^5+m^5+m^5+m^5+m^5.
$$


All five summands are positive, completing the proof.

For example, for every fixed $0<\varepsilon<1$, a proportion $\varepsilon^{|D|}$
of the parameters $m$ make all the roots lie within $\varepsilon$ of integers
from below. More generally, every nonempty open pattern occurs among represented
targets. Thus no exclusion criterion can depend solely on membership of these
finitely many fractional parts in a fixed nonempty open region. This statement
does not cover shrinking tolerances depending on $n$, extra arithmetic
conditions, or control of the full curved lattice shell.

## Representation-weighted root phases

There is a stronger quantitative statement for fixed continuous root-phase
filters. It is proved here independently of the particular represented ray
above.

**Lemma.** Fix $r\ge2$, positive integral coefficients $a_1,\ldots,a_r$, and
integers $M\ge1,b$. Put $F(\mathbf x)=\sum_i a_ix_i^r$. For every fixed real
$\lambda\ne0$,

$$
\sum_{\substack{\mathbf x\in\mathbb N^r\\F(\mathbf x)\le X\\
F(\mathbf x)\equiv b\pmod M}}
e\bigl(\lambda F(\mathbf x)^{1/r}\bigr)=o(X),
\tag{8}
$$

where $e(t)=\exp(2\pi it)$.

**Proof.** Let $N=X^{1/r}$ and fix $\delta>0$. Tuples with some
$x_i<\delta N$ contribute $O_{F,r}(\delta N^r)$. For the other tuples, fix
$x_2,\ldots,x_r$, set $B=\sum_{i>1}a_ix_i^r$, and split $x_1$ into residue
classes modulo $M$. The congruence in (8) either holds on an entire such class
or nowhere on that class; the size restrictions give one interval. The phase
$f(x_1)=\lambda(a_1x_1^r+B)^{1/r}$ has

$$
f''(x_1)=\lambda(r-1)a_1B x_1^{r-2}
(a_1x_1^r+B)^{1/r-2}.
$$

On the retained interval, $B\asymp_{F,\delta}N^r$ and
$x_1\asymp_{F,\delta}N$, so $|f''|\asymp_{F,\delta}|\lambda|/N$.
The standard second-derivative estimate for exponential sums on an interval,
$\sum e(f(n))\ll L\sqrt\eta+\eta^{-1/2}$ when
$\eta\le |f''|\ll\eta$, applies after parameterizing the residue class.
It gives $O_{F,\delta,M,\lambda}(N^{1/2})$ per fiber. Thus the left side of
(8) is

$$
O_{F,r}(\delta N^r)+O_{F,\delta,M,\lambda}(N^{r-1/2}).
$$

Let $N\to\infty$ and then $\delta\to0$. This proves (8).

For clarity, this argument also gives the following dependence on a nonzero
varying frequency:

$$
\frac{|S_F(X;\lambda)|}{X}
\ll_{F,r}\delta+C_{F,\delta,M}
\left(\sqrt{\frac{|\lambda|}{N}}
+\frac1{\sqrt{N|\lambda|}}\right).
\tag{9}
$$

It does not give a useful relative error for every shrinking phase set.

### Continuous weights have the same limiting mean

Fix positive real numbers $\alpha_1,\ldots,\alpha_k$, and let $H$ be the
closure in $\mathbb T^k$ of the continuous line
$\{t(\alpha_1,\ldots,\alpha_k):t\in\mathbb R\}$. Write $\mu_H$ for Haar
probability measure. For any continuous $\psi:\mathbb T^k\to\mathbb C$, put

$$
w(n)=\psi(\alpha_1n^{1/r},\ldots,\alpha_kn^{1/r}),\qquad
\bar w=\int_H\psi\,d\mu_H.
$$

Fourier approximation and (8) give

$$
\sum_{\substack{\mathbf x\in\mathbb N^r\\F(\mathbf x)\le X\\
F(\mathbf x)\equiv b\pmod M}}w(F(\mathbf x))
=\bar w\,R_F(X;b,M)+o(X),
\tag{10}
$$

where $R_F$ is the unweighted tuple count. Indeed, a Fourier character indexed
by $\mathbf h\in\mathbb Z^k$ is constant one precisely when
$\sum_j h_j\alpha_j=0$; every other character is covered by (8).

Ordinary target counting has the identical mean:

$$
\sum_{\substack{n\le X\\n\equiv b\pmod M}}w(n)
=\bar w\,\frac X M+o(X).
\tag{11}
$$

For a nonzero Fourier frequency $\lambda$, comparison with the integral gives
an error $O_{M,\lambda}(1+X^{1/r})$ for the exponential sum in (11).
Substitution $u=t^{1/r}$ and integration by parts bound the integral by
$O_{M,\lambda}(1+X^{1-1/r})$. Both are $o(X)$. Fourier approximation proves
(11), including the case of rational dependencies among the $\alpha_j$.

Take $r=5$, $\alpha_j=d_j^{-1/5}$ for any fixed finite list of cores, and
$\psi\ge0$. Apply (10) to the finite canonical family used in the
[quintic certificate](quintic_first_moment_barrier.md), and divide its ordered
counts by $5!$. Every unordered representation has at most $5!$ orderings, so
nonnegative weighting preserves this lower bound. If $U_5(n)$ is the number
of unordered representations of $n$ by exactly five positive $5$-powerful
integers, the certificate and (11) imply

$$
\liminf_{X\to\infty}\frac M X
\sum_{\substack{n\le X\\n\equiv b\pmod M}}U_5(n)w(n)
\ge\frac{429}{400}\bar w.
\tag{12}
$$

The normalized weighted target count tends to $\bar w$. Thus adding a fixed
nonnegative continuous root-phase filter with positive mean cannot turn that
first-moment method into a deficit below one. The same conclusion permits
any fixed nonnegative periodic target weight, by summing residue classes.
This is a limitation of those fixed filters, not a statement about distinct
values, shrinking-target filters, or infinitude of the complement.
