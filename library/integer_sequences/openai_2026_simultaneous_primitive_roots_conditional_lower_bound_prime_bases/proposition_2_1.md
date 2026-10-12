---
name: integer_sequences/openai_2026_simultaneous_primitive_roots_conditional_lower_bound_prime_bases/proposition_2_1
title: "Proposition 2.1: under Inputs 4.1, 5.1 and 5.2, at least c x/(log x)^2 primes p = 4rQ+1 in (x,2x) in a fixed odd progression, with Q > x^0.9 prime and r built from primes in (exp(L^0.1), exp(L^0.3))"
desc: |
  The manuscript's prime reservoir, conditional on three inputs it takes
  from the companion Artin manuscript: many primes p in (x,2x) in a
  fixed progression with p-1 = 4rQ, Q > x^0.9 prime and r composed of
  primes in a controlled range. Claims checked only.
created: 2026-10-12T23:13:55Z
updated: 2026-10-12T23:13:55Z
---

***

## Statement

The proposition assumes three statements that the manuscript calls Inputs,
takes from its companion *Primitive roots for every admissible integer
base*, and does not prove. They are stated here exactly, in the corpus's
words, after the setup they use.

**The marked setup** (`sections/04-marked-family.tex` lines 10--71 and
88--89, pp. 6--7). Throughout, $x$ is real and tends to infinity, $L=\log x$,
$W=\exp(L^{0.24})$ and $V(y)=\prod_{p\le y}(1-1/p)$ for $y\ge1$, with
products over primes. $P^-(h)$ is the least prime factor of $h>1$,
$P^-(1)=\infty$, and $h$ is $W$-rough when $P^-(h)>W$. Every parameter not
displayed as depending on $x$ is fixed before $x$ grows. For an integer
$K\ge1$ and fixed exponents $0.1<a_1<\cdots<a_K<0.2$, the prime groups are
$\mathcal P_i=\{p\ \text{prime}:\exp(L^{a_i})\le p\le\exp(2L^{a_i})\}$, with
$V_i=\sum_{p\in\mathcal P_i}1/p$; their members are the group primes. For
$h\ge1$, $\omega_i(h)$ is the number of primes of $\mathcal P_i$ dividing
$h$, and the marks (the companion's, with mark parameter $1/2$) are

$$
\mathcal W(h)=2^{K-\sum_i\omega_i(h)}\prod_{i=1}^K\frac{\omega_i(h)}{V_i}.
$$

For $w>\gamma>0$ the rough-factor density is

$$
D_\gamma(w)=\frac1w+\sum_{j\ge2}\frac1{j!}
\int\limits_{\substack{t_i\ge\gamma\ (1\le i<j)\\ \sum_{i<j}t_i\le w-\gamma}}
\frac{1}{w-\sum_{i<j}t_i}\prod_{i<j}\frac{dt_i}{t_i}.
$$

Dirichlet characters, principal ones included, are extended by zero on
nonunits, and frequencies are real.

**Input 4.1** (marked Type II estimate; `sections/04-marked-family.tex`
lines 99--151, pp. 7--8). Part (i), the coefficient criterion. Fix
$\delta,C,D_*>0$. Let $H_m,H_n\ge x^\delta$ with $X=H_mH_n\asymp x$, the
comparison constants fixed. Let $F:\mathbb Z_{>0}\to\mathbb C$ satisfy
$|F(h)|\le1$ and $F(ph)=F(h)$ for every group prime $p$ and every $h\ge1$.
Let $(\alpha_m)$ and $(\beta_n)$ be complex sequences supported on $W$-rough
integers of $[H_m,2H_m]$ and $[H_n,2H_n]$ respectively, with $\alpha$
supported on some interval $I\subseteq[H_m,2H_m]$ and
$|\alpha_m|,|\beta_n|\le L^C$. Suppose that for all fixed $A_0,B,A>0$, every
Dirichlet character $\chi$ of modulus $k\le L^{A_0}$ and every real
$|t|\le2XL^B$,

$$
\Bigl|\frac1{H_m}\sum_m\alpha_m\chi(m)m^{it}\Bigr|\ll_A L^{-A},
$$

uniformly in the interval, the character and the frequency, the constant and
threshold being allowed to depend on $A_0,B,A$, the fixed setup and the fixed
parameters defining the coefficients. Then

$$
\Bigl|\sum_{m,n}\alpha_m\beta_nF(mn-1)\mathcal W(mn-1)\Bigr|\ll XL^{-D_*}
$$

once $K$ is large enough in terms of the fixed data, how large not depending
on the particular $a_i$. The implied constant and threshold may depend on all
fixed data, the $a_i$ and the constants and thresholds of the hypothesis
included; with those fixed, the bound is uniform over the admissible $F$,
dyads, intervals and coefficients. Part (ii), rough coefficient
cancellation. Keep the marked data and the conditions on $F$, $\beta$,
$H_m$ and $H_n$, with no $\alpha$ chosen in advance. Fix
$0<\gamma<w_-<w_+<1$ and suppose
$[\log H_m/L,\log(2H_m)/L]\subseteq[w_-,w_+]$. Then for every interval
$I\subseteq[H_m,2H_m]$ and every real $|v|\le L^C$ the coefficient

$$
\alpha^{(0)}_m=m^{iv}\Bigl(\mathbf 1_{P^-(m)>x^\gamma}-
\frac{D_\gamma(\log m/L)}{LV(W)}\mathbf 1_{P^-(m)>W}\Bigr)
\qquad(m\in I),
$$

set to zero outside $I$, satisfies the cancellation hypothesis of part (i)
for all fixed $A_0,B,A>0$, uniformly in the dyads, the interval, the
character, $t$ and $v$; its constant and threshold may depend on the fixed
parameters, $\gamma$, $w_-$ and $w_+$ among them.

**Input 5.1** (block sieve; `sections/05-prime-reservoir.tex` lines 11--63,
pp. 12--13). Let $z>1$, let $\mathcal A$ be a finite set with weights
$\lambda_\nu\ge0$, let $\mathcal D$ be a set of primes at most $z$, and for
each $p\in\mathcal D$ let $\mathcal A_p\subseteq\mathcal A$ (its bad
condition). For a squarefree product $\ell$ of primes of $\mathcal D$ put
$\mathcal A_\ell=\bigcap_{p\mid\ell}\mathcal A_p$, with
$\mathcal A_1=\mathcal A$. Suppose that for every such $\ell$, $\ell=1$
included, $\sum_{\nu\in\mathcal A_\ell}\lambda_\nu=Yg(\ell)+R(\ell)$ with
$Y\ge0$, where $g$ is multiplicative on these products, $g(1)=1$, and
$g(p)=0$ for primes $p\notin\mathcal D$; and that for fixed $\eta_0>0$ and
$C_0<\infty$, $0\le g(p)\le1-\eta_0$ for every $p$ and
$\sum_{u<p\le u^2}g(p)\le C_0$ for every $u>1$. Let $S$ be the total weight
of $\mathcal A\setminus\bigcup_{p\in\mathcal D}\mathcal A_p$. Then for every
sufficiently large even integer $H$,

$$
S=Y\prod_{p\le z}(1-g(p))\bigl(1+O(e^{-H})\bigr)+
O\Bigl(\sum_{\ell\le z^{4H+2}}|R(\ell)|\Bigr),
$$

the sum over squarefree $\ell$ composed of primes of $\mathcal D$ ($\ell=1$
included), where the threshold for $H$ and the implied constants depend only
on $\eta_0$ and $C_0$; and for $H=2$,
$S\ll_{\eta_0,C_0}Y\prod_{p\le z}(1-g(p))+\sum_{\ell\le z^{10}}|R(\ell)|$,
over the same kind of $\ell$.

**Input 5.2** (rough-number density; `sections/05-prime-reservoir.tex` lines
65--78, p. 13). There are absolute constants $b_d,c_d,C_d>0$ such that, for
every fixed $0<b<\min(b_d,1/2)$,

$$
\int_b^{1/2}D_t(1-t)\,\frac{dt}{t}=D_b(1)-1,
\qquad
D_b(1)\le\frac{e^{-\gamma_E}}{b}\bigl(1+C_de^{-c_d/b}\bigr),
$$

with $\gamma_E$ Euler's constant; the integrand's value at $t=1/2$ does not
matter.

**Proposition 2.1** (a prime reservoir in a fixed progression). Assume Inputs
4.1, 5.1 and 5.2. Let $M\ge1$ be odd and squarefree, $M=1$ included, and let
$a$ be a residue class modulo $M$ with $\gcd(a(a-1),M)=1$. Then there are
constants $c_{M,a}>0$ and $x_{M,a}>1$ such that for every real
$x\ge x_{M,a}$, with $L=\log x$, at least $c_{M,a}x/L^2$ primes $p$ satisfy

$$
x<p<2x,\qquad p\equiv a\pmod M,\qquad p=4rQ+1,
$$

where $r$ is a positive integer, $Q>x^{0.9}$ is prime, and every prime
$\ell$ dividing $r$ satisfies $\exp(L^{0.1})<\ell<\exp(L^{0.3})$.

For these primes $Q$ is the largest prime factor of $p-1$ and the cofactor
$4r=(p-1)/Q$ is below $2x^{0.1}$. The statement does not exclude $r=1$, but
it does not promise that case either: the construction's marks
$\mathcal W(r)$ vanish unless $r$ has a prime factor in every group, so
$r=1$ carries no weight. For large $x$, $r$ and $Q$ are odd and every such
$p$ is $5$ modulo $8$. Nothing is claimed without the three Inputs; Input
3.1 is not used.

Read against its statement only, the companion's own Proposition 2.1, which
allows a progression modulo any positive multiple of $8$, appears to contain
this one: take there the modulus $8M$, $c=4$ and a class $u$ with
$u\equiv5\pmod8$ and $u\equiv a\pmod M$. This comparison is made on this
page and is unverified. The manuscript does not make it: it derives the
proposition from the three Inputs instead of citing the companion's, and
its introduction presents Sections 4--5 as extending the companion's
Section 12 construction to a fixed progression.

**Source.** OpenAI, *Simultaneous primitive roots: a conditional lower bound
for prime bases*, release folder
`preprints/Simultaneous-primitive-roots-a-conditional-lower-bound-for-prime-bases-October-4-2026`;
TeX file `build/sections/02-reduction.tex`, label `prop:reservoir` (lines
11--28), PDF p. 2; the proof occupies Sections 4 and 5
(`build/sections/04-marked-family.tex` and
`build/sections/05-prime-reservoir.tex`, PDF pp. 6--20) and closes at
`05-prime-reservoir.tex` lines 596--610, PDF p. 20. Read 2026-10-12.
Provenance and attestations are on
[[integer_sequences/openai_2026_simultaneous_primitive_roots_conditional_lower_bound_prime_bases/_index|the card]].

**Read depth.** Claims checked: the statement, Inputs 4.1, 5.1 and 5.2 and
the marked setup and density they use were read clause by clause in the TeX
source, together with the statements of Lemmas 4.2--4.4. The fifteen-page
proof was read for its structure only (below); no step was checked and the
numerical exponent margins were not recomputed. Nothing here is
independently reviewed.

## Proof pointer

Section 4 (pp. 6--12) builds a weighted family. Fix a smooth $\Psi$
supported in $(1,2)$ with $0\le\Psi\le1$, let $h_{\mathcal P}$ be the part of
$h$ composed of group primes, and let $F(h)$ be the indicator that
$h/h_{\mathcal P}=4Q$ for a prime $Q>x^{0.9}$; this $F$ is invariant under
multiplication by group primes, as Input 4.1 requires. The weight of
$d\ge2$ is $w(d)=\mathbf 1_{d\equiv a\,(M)}\Psi(d/x)F(d-1)\mathcal W(d-1)$
(4.15). A supported $d$ is uniquely $4rQ+1$ with $r$ a product of group
primes, so every supported prime has the shape the proposition asks for,
and the bound on the marks gives $0\le w\le B_K=(2/\log2)^K$. Lemma 4.3
shows by the prime number theorem modulo the fixed $M$ that the total weight
$X_0$ is of order $xJ_0/L$, where
$J_0=\sum_r\mathcal W(r)/r$ lies between $1$ and a constant depending on
$K$, and that large $r$ contribute negligibly. Lemma 4.4 bounds the sieve
remainders, on average over $r\le x^\epsilon$ and over moduli up to
$D_0=x^{1/2-\kappa/2}$, by the Bombieri--Vinogradov theorem. Lemma 4.2
twists Input 4.1 by a character $\chi_0$ modulo $M$: Input 4.1(ii) applied to
the product characters $\chi_0\chi$, of modulus at most $L^{A_0+1}$,
supplies the cancellation hypothesis of Input 4.1(i).

Section 5 (pp. 12--20) extracts primes. A lower-bound sieve (Input 5.1 at
depth $H_b=2\lfloor1/(40b)\rfloor$) removes the prime factors up to $x^b$
and leaves weight at least
$e^{-\gamma_E}b^{-1}(1-C_se^{-c_s/b})+o(1)$ in units of
$\mathfrak S_MX_0/L$, where $\mathfrak S_M>0$ is a constant fixed by $M$
(5.5). Composites whose least prime factor $n$ lies in $(x^b,x^{1/2-\kappa}]$
are removed bin by bin over a fixed partition of $[b,1/2-\kappa]$. In each
bin the weight of $d=mn$ with $P^-(m)>x^\gamma$ is replaced, at cost
$o(X_0/L)$, by a count of $W$-rough $m$ weighted by
$D_\gamma(\log m/L)/(LV(W))$; this uses Lemma 4.2 after separating
$\Psi(mn/x)$ by Fourier inversion and the progression by characters
modulo $M$ (5.8). A sieve conditioned on $n\mid d$ evaluates the replaced
count (5.6), and Input 5.2 bounds the total over the bins by
$D_b(1)-1+1/8$ in the same units (5.12)--(5.13). The remaining composites
are products of two primes above $x^{1/2-\kappa}$. For each $r$ separately,
an upper-bound sieve on pairs $(m,n)$ with $mn\equiv1\pmod{4r}$ (Input 5.1
with $H=2$) bounds their weight by $C_2(\kappa+L^{-1})X_0/L$, with $C_2$
independent of $\kappa$, $b$ and $K$ (5.20). The parameters are chosen in
the order $\kappa$, $\epsilon$, $b$, the partition, $K$, the $a_i$, and
finally $x$, so that each of the three fixed losses is at most $1/8$. The
primes then carry weight at least $\mathfrak S_MX_0/(2L)\gg x/L^2$ (5.21),
and dividing by $B_K$ counts distinct primes.

## Dependencies

Assumed and not proved in the manuscript: Inputs 4.1, 5.1 and 5.2, which it
attributes to the companion *Primitive roots for every admissible integer
base*
([[integer_sequences/openai_2026_primitive_roots_admissible_integer_base/_index|card]]):
Input 4.1 to the coefficient criterion of its Lemma 10.2 specialized to
these marks and to the cancellation verified in the proof of its
Proposition 10.3, Input 5.1 to its Lemma 11.1 and Input 5.2 to its Lemma
11.2. Proved in the manuscript: Lemmas 4.2--4.4. External results cited at
statement level and not checked here: the prime number theorem for a fixed
modulus, the Bombieri--Vinogradov theorem (Bombieri 1965, Vinogradov 1965),
Mertens' theorem and Fourier inversion.

## Bears on

The manuscript names no Erdős problem, and no problem page is identified as
using this proposition; the card says why Problem 1065 is not listed.
