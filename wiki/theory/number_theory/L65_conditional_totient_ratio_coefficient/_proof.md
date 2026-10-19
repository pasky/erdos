---
name: theory/number_theory/L65_conditional_totient_ratio_coefficient/_proof
title: The reciprocal least-preimage weight and its phase limit
desc: |
  A conditional extension of the manuscript's prime count, followed by a
  uniform tail argument and an exact-phase criterion for convergence.
created: 2026-10-14T08:41:00Z
updated: 2026-10-14T08:41:00Z
---

***

We prove [[theory/number_theory/L65_conditional_totient_ratio_coefficient/_index|L65]].
All manuscript results invoked below are conditional premises from the
[[../library/arithmetic_functions/openai_2026_asymptotic_formula_number_totients/_index|unrefereed source]].
This proof checks their composition, not their underlying number-theoretic
proofs.

## Notation and source interface

Write $\mathcal V$ for the positive totients and
$\ell(v)=\min\{n:\varphi(n)=v\}$. Then

$$
V(x)=\#(\mathcal V\cap[1,x]),\qquad
V'(x)=\#\{v\in\mathcal V:\ell(v)\le x\}.
$$

The latter set is contained in the former, since $v\le\ell(v)$. Use natural
logarithms throughout this proof. In the manuscript's notation,

$$
B=\log\log x,\quad
m=\left\lfloor\frac{\log B-\log\log B}{\lambda}\right\rfloor,
\quad
\theta(x)=\frac{\log B-\log\log B}{\lambda}-m,
\quad Z(x)=\frac{xG_m}{\log x},
$$

where $\lambda>0$ and $G_m$ are defined in its Equations (2.1)–(2.4).
Its Theorem 2.1 supplies

$$
V(x)=Z(x)\bigl(A(1;\theta(x))+o(1)\bigr),\qquad
0<c_-\le A(1;s)\le c_+<\infty,                         \tag{1}
$$

and $V(cx)/V(x)\to c$ for every fixed $c>0$.

For each sufficiently large fixed cut $H$, the manuscript counts distinct
data $(d,p_1,\ldots,p_R)$, where $R=m-H$, rather than their possibly many
tail witnesses. Its Equation (6.1) defines

$$
M_f(x;H)=\sum_{(d,p_1,\ldots,p_R)}
 \frac{f(\ell(d)/d)}{d\prod_{i=1}^R(p_i-1)}.
$$

The needed source estimates are these. Proposition 5.3 gives, outside
$o_H(1)Z(x)+o_{x;H}(Z(x))$ exceptional values and tuples, a unique tuple
$(p_0,\ldots,p_R,d)$ for each value $v$, with

$$
v=d\prod_{i=0}^R(p_i-1),\qquad
\ell(v)=\ell(d)\prod_{i=0}^R p_i.                     \tag{2}
$$

The identity for $\ell(v)$ uses its assertion about **every** preimage.
Sections 6.1 and 7.1 give, uniformly in the remaining data,

$$
\begin{gathered}
D=d\prod_{i=1}^R(p_i-1)\le\exp((\log x)^{0.8}),\qquad
M_1(x;H)\ll K_HG_m,\quad K_H=H^{o(1)},\\
\sum_{i=1}^R\frac1{p_i}\ll\exp(-cH\rho^{-H}),
\end{gathered}                                                     \tag{3}
$$

where $c>0$, $0<\rho<1$. Each fixed $H$ bounds the tail witnesses, hence
$\ell(d)/d$, independently of $x$. The admissible remaining data do not
change when the largest prime $p_0\ge x^{0.9}$ varies. Proposition 6.5
approximates $M_f/G_m$ by the finite coefficient $A_H(f;\theta)$ with an
error tending to zero as $H\to\infty$, for every $0\le f\le1$.

## Count the preimages at most x

Set $f_0(r)=1/r$. For fixed remaining data put

$$
r=\ell(d)/d,\quad q=\prod_{i=1}^R(1-1/p_i),\quad
T=x/D,\quad U=\frac{x}{\ell(d)\prod_{i=1}^R p_i}
 =Tq/r.
$$

The conditions $\ell(v)\le x$ and $v\le x$ are exactly
$p_0\le U$ and $p_0\le T+1$. Since $r\ge1$ and $q\le1$, the first
already implies the second. We must therefore count

$$
x^{0.9}\le p_0\le U.                                  \tag{4}
$$

For each fixed $H$, (3) and the boundedness of $r$ give
$T,U=x^{1-o(1)}$ uniformly in the data; $q$ is bounded away from zero.
The prime number theorem applied to $U$ gives
$\pi(U)=(U/\log x)(1+o_{x;H}(1))$. The lower cutoff in (4) costs at most
$x^{0.9}$ primes, which is $o(T/\log x)$ uniformly. Also

$$
\left|\frac q r-\frac1r\right|
\le1-q\le\sum_{i=1}^R\frac1{p_i}.
$$

Thus (4) has

$$
\frac{T}{\log x}
\left(f_0(r)+O\left(\sum_{i=1}^R\frac1{p_i}\right)
       +o_{x;H}(1)\right)                              \tag{5}
$$

prime solutions. This is an additive estimate, and requires no prime theorem
for short intervals. Summing (5), using (3), and removing the exceptional
values and tuples in Proposition 5.3 yields

$$
\limsup_{x\to\infty}
\left|\frac{V'(x)}{Z(x)}-\frac{M_{f_0}(x;H)}{G_m}\right|
\le\eta_H,\qquad \eta_H\longrightarrow0.              \tag{6}
$$

In particular the extra error in (5) is
$O(K_H\exp(-cH\rho^{-H}))$, which tends to zero.

Apply the manuscript's Lemma 6.6 to the comparison quantity
$C_{f_0}(x)=V'(x)/Z(x)$, independent of $H$. It proves uniform existence of
$A(f_0;s)$ and

$$
V'(x)=Z(x)\bigl(A(f_0;\theta(x))+o(1)\bigr).           \tag{7}
$$

For clarity, uniformity does not require continuity of $A_H$ in $s$. For
any fixed $s\in[0,1)$ the increasing continuous function
$\psi(B)=(\log B-\log\log B)/\lambda$ assumes $n+s$ at some $B_n\to\infty$.
Then $x_n=\exp(\exp B_n)$ has $\theta(x_n)=s$ exactly. Comparing any two
cut indices on this sequence bounds their coefficients' difference by their
uniform comparison errors. This is the uniform Cauchy argument of Lemma 6.6.

## Positivity and the tail of the least-preimage intervals

Lemma 7.3 of the manuscript says that $\ell(v)/v$ is tight when distinct
totients $v\le x$ receive equal weight: for every $\varepsilon>0$ some
constant $C$ bounds the ratio outside at most $\varepsilon V(x)$ values,
for all sufficiently large $x$. Take $\varepsilon=1/2$. At least
$V(x/C)/2$ values $v\le x/C$ satisfy $\ell(v)\le Cv\le x$. Hence

$$
V'(x)\ge\tfrac12 V(x/C),\qquad
\liminf_{x\to\infty}\frac{V'(x)}{V(x)}\ge\frac1{2C}>0, \tag{8}
$$

using fixed dilation from (1). Equations (1), (7), (8), and the exact-phase
sequences bound $A(f_0;s)$ away from zero uniformly in $s$. The upper bound
follows from $V'\le V$.

For $k\ge1$ let $N_k(x)$ and $f_k$ be as in the manuscript's Equation (2.9).
The intervals partition the values with $\ell(v)>x$, so

$$
V(x)-V'(x)=\sum_{k\ge1}N_k(x),\qquad
\sum_{k>K}N_k(x)
 \le\#\{v\le x:v\in\mathcal V,\ \ell(v)/v>K+1\}.     \tag{9}
$$

Lemma 7.3 makes the right-hand side at most $\varepsilon V(x)$ for all
large $x$ once $K$ is sufficiently large. Now assume the manuscript's
Theorem 2.2 as well. For a fixed finite $K$, substitute its asymptotics and
(1), (7) in (9), and take an exact-phase sequence. For every $s$ this gives

$$
0\le A(1;s)-A(f_0;s)-\sum_{k=1}^K A(f_k;s)
 \le\varepsilon A(1;s)\le\varepsilon c_+.
$$

The choice of $K$ is independent of $s$, proving the stated identity and
uniform convergence of the series. No interchange of the cut limit and an
uncontrolled infinite sum has been used.

## The remaining phase question

Write $\Phi(s)=A(1;s)/A(f_0;s)$. Its denominator has a uniform positive
lower bound, so (1) and (7) imply

$$
\frac{V(x)}{V'(x)}=\Phi(\theta(x))+o(1).                \tag{10}
$$

If $\Phi$ is constant, (10) proves convergence. Conversely, every phase
has an exact sequence tending to infinity, so convergence forces the same
value at every $s$. This is equivalent to constancy of its reciprocal.

For completeness the set of subsequential limits is an interval. For integer
$n$, each of $V(n)$ and $V'(n)$ increases by at most one at the next integer,
$V(n)\le n$, and $V'(n)\ge\pi(n)$, since the distinct values $p-1$ have
preimages $p\le n$. Consequently

$$
\left|\frac{V(n+1)}{V'(n+1)}-\frac{V(n)}{V'(n)}\right|
\le\frac1{\pi(n)}+\frac n{\pi(n)^2}\longrightarrow0.
$$

The ratio is bounded by (8). A bounded real sequence with successive
differences tending to zero has as its cluster set the closed interval
between its liminf and limsup: every intermediate value is approached during
arbitrarily late crossings. The real-variable ratio is constant between
consecutive integers. If $\Phi$ is nonconstant, two exact-phase sequences
give different limits, so this interval is nondegenerate and has continuum
many points. This also recovers the relevant consequence of
[[research/erdos_416/connections|Proposition 417.2]].

The remaining question is a property of the finite arithmetic coefficient,
not a missing tail interchange. With $p_{H,s}(d)$ denoting the union
probability in the manuscript's Equation (2.7), its common prefactor cancels:

$$
\frac{A_H(f_0;s)}{A_H(1;s)}
=\frac{\sum_d p_{H,s}(d)/\ell(d)}{\sum_d p_{H,s}(d)/d}.
                                                               \tag{11}
$$

The sums range over distinct tail totients having a witness. For large $H$
the denominator is uniformly positive, and (11) converges uniformly to
$A(f_0;s)/A(1;s)$. The witness sets and their union probabilities depend on
$s$; $\ell(d)$ is the least preimage among all preimages of $d$. Neither
deduplication nor minimization can be replaced by a sum over independent
witnesses. No phase independence or phase dependence of (11) is proved here.
