---
name: integer_sequences/openai_2026_simultaneous_primitive_roots_conditional_lower_bound_prime_bases/theorem_1_1
title: "Theorem 1.1: under Inputs 3.1, 4.1, 5.1 and 5.2, any fixed finite set of primes are all primitive roots modulo at least c x/(log x)^2 primes in (x,2x)"
desc: |
  The manuscript's main claim, conditional on four inputs it states and takes
  from the companion Artin manuscript: for distinct primes q_1,...,q_k, at
  least c x/(log x)^2 primes p in (x,2x) have every q_i as a primitive root.
  Claims checked only.
created: 2026-10-12T23:13:55Z
updated: 2026-10-12T23:13:55Z
---

***

## Statement

For a prime $p$ and an integer $q$ prime to $p$, $\operatorname{ord}_p(q)$ is
the multiplicative order of $q$ modulo $p$, and $q$ is a primitive root
modulo $p$ when this order is $p-1$ (p. 1). The theorem assumes four
Inputs, which the manuscript takes without proof from its companion, the
manuscript *Primitive roots for every admissible integer base*. They are
stated once here, condensed, for this page and the page of Proposition 2.1.

**Setup for Inputs 4.1 and 5.2** (`sections/04-marked-family.tex` lines
10--71 and 88--89, pp. 6--7). The real variable $x$ tends to infinity, and
each parameter not shown to depend on $x$ is fixed before $x$ grows. Put
$L=\log x$, $W=\exp(L^{0.24})$ and $V(y)=\prod_{p\le y}(1-1/p)$ for $y\ge1$,
with products over primes. Let $P^-(h)$ be the least prime factor of $h$, with
$P^-(1)=\infty$; $h$ is $W$-rough when $P^-(h)>W$. The marks depend on an
integer $K\ge1$ and fixed exponents $0.1<a_1<\cdots<a_K<0.2$. The group
$\mathcal P_i$ consists of the primes in $[\exp(L^{a_i}),\exp(2L^{a_i})]$,
and the group primes are the members of $\mathcal P_1,\dots,\mathcal P_K$.
With $V_i$ the sum of $1/p$ over $\mathcal P_i$ and $\omega_i(h)$ the number
of primes of $\mathcal P_i$ dividing $h$, the mark of $h\ge1$ is
$\mathcal W(h)=2^{K-\sum_i\omega_i(h)}\prod_{i=1}^K\omega_i(h)/V_i$, the
companion's marks with parameter $1/2$. For $w>\gamma>0$ the rough-factor
density is

$$
D_\gamma(w)=\frac1w+\sum_{j\ge2}\frac1{j!}\int_{R_j}
\frac{1}{w-t_1-\cdots-t_{j-1}}\,\frac{dt_1\cdots dt_{j-1}}{t_1\cdots t_{j-1}},
$$

where $R_j$ is the region where every $t_i\ge\gamma$ and
$t_1+\cdots+t_{j-1}\le w-\gamma$.

**Input 3.1** (uniform Hecke zero-free assertion;
`sections/03-splitting.tex` lines 8--15, p. 3). Over every cyclotomic field
$F$ containing the twelfth roots of unity $\mu_{12}$, no finite-order Hecke
$L$-function $L_F(s,\chi)$, continued meromorphically, vanishes in the
half-plane $\operatorname{Re}s>1-10^{-6}$. Here $\chi$ is a continuous
character of $F^\times\backslash\mathbb A_F^\times$ with finite image, and
the principal character's pole at $s=1$ is allowed.

**Input 4.1** (marked Type II estimate; `sections/04-marked-family.tex`
lines 99--151, pp. 7--8). Dirichlet characters here, principal ones
included, vanish on nonunits, and the frequencies $t$ and $v$ are real.
Part (i) is a criterion on the coefficients. Fix $\delta,C,D_*>0$ and scales
$H_m,H_n\ge x^\delta$ with $X=H_mH_n\asymp x$, the comparison constants
fixed. Let $F$ be any function on the positive integers with $|F|\le1$ that
is unchanged when its argument is multiplied by a group prime. Let the
complex coefficients $\alpha_m$ and $\beta_n$ have size at most $L^C$ and be
supported on $W$-rough integers of $[H_m,2H_m]$ and $[H_n,2H_n]$, with
$\alpha$ supported on some interval $I\subseteq[H_m,2H_m]$. Assume that, for
all fixed $A_0,B,A>0$, the averages $H_m^{-1}\sum_m\alpha_m\chi(m)m^{it}$
have size $\ll_AL^{-A}$ for every Dirichlet character $\chi$ of modulus at
most $L^{A_0}$ and every $|t|\le2XL^B$, uniformly in $I$, $\chi$ and $t$;
the constant and threshold may depend on $A_0$, $B$, $A$, the setup and the
fixed parameters behind the coefficients. Then, once $K$ exceeds a bound
that depends on the fixed data but not on the $a_i$,

$$
\Bigl|\sum_{m,n}\alpha_m\beta_nF(mn-1)\mathcal W(mn-1)\Bigr|\ll XL^{-D_*}.
$$

Its constant and threshold may depend on all the fixed data, the $a_i$ and
the assumption's constants and thresholds among them; beyond that the bound
is uniform in $F$, the scales, $I$ and the coefficients. Part (ii) supplies
the assumed cancellation for one coefficient. Keep the conditions of part
(i) on $F$, $\beta$ and the scales, fix $0<\gamma<w_-<w_+<1$, and suppose
that $\log H_m/L$ and $\log(2H_m)/L$ lie in $[w_-,w_+]$. Then for every
interval $I\subseteq[H_m,2H_m]$ and every $|v|\le L^C$, the coefficient
equal to

$$
m^{iv}\Bigl(\mathbf 1_{P^-(m)>x^\gamma}-
\frac{D_\gamma(\log m/L)}{LV(W)}\mathbf 1_{P^-(m)>W}\Bigr)
$$

for $m\in I$, and to $0$ elsewhere, meets the assumption of part (i) for all
fixed $A_0,B,A>0$. It does so uniformly in the scales, $I$, $\chi$, $t$ and
$v$, with constant and threshold depending on the fixed parameters, $\gamma$
and $w_\pm$ among them.

**Input 5.1** (block sieve; `sections/05-prime-reservoir.tex` lines 11--63,
pp. 12--13). Take a finite set $\mathcal A$ with weights $\lambda_\nu\ge0$,
a real $z>1$, a set $\mathcal D$ of primes at most $z$ and, for each
$p\in\mathcal D$, a subset $\mathcal A_p\subseteq\mathcal A$ to be sifted
out. Below, $\ell$ ranges over the squarefree products of primes of
$\mathcal D$, $\ell=1$ included, and $\mathcal A_\ell$ is the intersection
of the $\mathcal A_p$ with $p\mid\ell$, with $\mathcal A_1=\mathcal A$.
Assume that the weight of each $\mathcal A_\ell$ is $Yg(\ell)+R(\ell)$,
where $Y\ge0$ and $g$ is multiplicative on these $\ell$ with $g(1)=1$, and
set $g(p)=0$ for primes outside $\mathcal D$. Assume also, for fixed
$\eta_0>0$ and $C_0<\infty$, that $0\le g(p)\le1-\eta_0$ for every prime $p$
and $\sum_{u<p\le u^2}g(p)\le C_0$ for every $u>1$. Let $S$ be the weight of
the elements of $\mathcal A$ that lie in no $\mathcal A_p$. Then for each
even $H$ beyond a threshold

$$
S=Y\prod_{p\le z}(1-g(p))\bigl(1+O(e^{-H})\bigr)+
O\Bigl(\sum_{\ell\le z^{4H+2}}|R(\ell)|\Bigr),
$$

and for $H=2$ there is the upper bound
$S\ll Y\prod_{p\le z}(1-g(p))+\sum_{\ell\le z^{10}}|R(\ell)|$. The threshold
for $H$ and all the implied constants depend only on $\eta_0$ and $C_0$.

**Input 5.2** (rough-number density; `sections/05-prime-reservoir.tex`
lines 65--78, p. 13). For some absolute constants $b_d,c_d,C_d>0$ and every
fixed $b$ with $0<b<\min(b_d,1/2)$, the density obeys the identity
$\int_b^{1/2}D_t(1-t)\,dt/t=D_b(1)-1$, whatever value the integrand is
given at $t=1/2$, and the bound
$D_b(1)\le e^{-\gamma_E}b^{-1}(1+C_de^{-c_d/b})$, where $\gamma_E$ is
Euler's constant.

**Theorem 1.1.** Suppose Inputs 3.1, 4.1, 5.1 and 5.2 hold, and fix $k\ge1$
distinct positive primes $q_1,\dots,q_k$. Then there are $c_{\mathbf q}>0$
and $x_{\mathbf q}>1$, depending on these primes, such that for each real
$x\ge x_{\mathbf q}$ the interval $(x,2x)$ contains at least

$$
c_{\mathbf q}\,\frac{x}{(\log x)^2}
$$

primes $p\nmid q_1\cdots q_k$ modulo which every $q_i$ is a primitive root,
that is, with $\operatorname{ord}_p(q_i)=p-1$ for $i=1,\dots,k$.

The manuscript calls the theorem "an implication from four statements taken
from the companion manuscript" and says that the Inputs' proofs there "and
its cited companion manuscripts are outside the scope of this paper" (p. 1).
Nothing is claimed without the four Inputs. The bases must be positive
primes; composite bases are not covered. For $k=1$ the conclusion is the
prime-base case of the companion's Theorem 1.1, which the companion claims
without hypotheses.

**Source.** OpenAI, *Simultaneous primitive roots: a conditional lower bound
for prime bases*, release folder
`preprints/Simultaneous-primitive-roots-a-conditional-lower-bound-for-prime-bases-October-4-2026`;
TeX file `build/sections/01-introduction.tex`, label `thm:main` (lines
32--47), PDF p. 1; the proof is in `build/sections/02-reduction.tex` lines
48--119 and closes at lines 113--119, PDF p. 3. Provenance and attestations are
on
[[integer_sequences/openai_2026_simultaneous_primitive_roots_conditional_lower_bound_prime_bases/_index|the card]].

**Read depth.** Claims checked: the statement, the definition of the order,
the four Inputs with the marked setup and density they use, and the
statements of Propositions 2.1 and 2.2 that the proof combines were read
clause by clause in the TeX source. The one-page proof was read for its
structure (below), as were the proofs of the two propositions (Sections 3--5);
no step was checked. Nothing here is independently reviewed.

## Proof pointer

Section 2 (pp. 2--3). Write $\iota_p(q)=(p-1)/\operatorname{ord}_p(q)$ for
the index of a base $q$ modulo $p$; $q$ is a primitive root exactly when the
index is $1$. Let $M$ be the product of the odd $q_i$ ($M=1$ if there are
none), and use the Chinese remainder theorem to choose a class $a$ modulo $M$
that is a quadratic nonresidue modulo every odd $q_i$; then $a$ and $a-1$ are
units modulo $M$. Proposition 2.1
([[integer_sequences/openai_2026_simultaneous_primitive_roots_conditional_lower_bound_prime_bases/proposition_2_1|result page]]),
which assumes Inputs 4.1, 5.1 and 5.2, gives at least $c_{M,a}x/L^2$ primes
$p\in(x,2x)$ with $p\equiv a\pmod M$ and $p-1=4rQ$, where $Q>x^{0.9}$ is
prime and every prime factor of $r$ lies in
$(\exp(L^{0.1}),\exp(L^{0.3}))$. For large $x$ both $r$ and $Q$ are odd, so
$p\equiv5\pmod8$. Quadratic reciprocity then makes every odd $q_i$ a
nonresidue modulo $p$, since $p\equiv a$ modulo $q_i$ and $p\equiv1\pmod4$,
and the supplementary law does the same for $2$. By Euler's criterion each
index $\iota_p(q_i)$ is then odd, so an index above $1$ has an odd prime
divisor $\lambda$, which is $Q$ or divides $r$, and
$q^{(p-1)/\lambda}\equiv1\pmod p$.

Two kinds of exception remain. If $\lambda=Q$, then $p$ divides $q^j-1$ for
some $j=(p-1)/Q<2x^{0.1}$; the product of these numbers has logarithm
$\ll_q x^{0.2}$ and each prime above $x$ contributes more than $L$, so there
are $O_q(x^{0.2}/L)$ such primes. If $\lambda=\ell$ divides $r$, then $\ell$
is in the range of Proposition 2.2, which assumes Input 3.1 and bounds the
primes $p\in(x,2x)$ with $p\equiv1\pmod\ell$ and
$q^{(p-1)/\ell}\equiv1\pmod p$ by $\ll_q x/(\ell(\ell-1)L)+x^{1-\eta}$,
$\eta=10^{-6}$. Summing over the at most $\exp(L^{0.3})$ primes
$\ell>\exp(L^{0.1})$ loses $O_q((x/L)\exp(-L^{0.1})+\exp(L^{0.3})x^{1-\eta})$
primes. Both losses are $o(x/L^2)$ for each of the finitely many bases, so at
least $c_{M,a}x/(2L^2)$ of the primes from Proposition 2.1 have every index
equal to $1$.

Where the propositions come from. Proposition 2.2 is proved in Section 3
(pp. 3--6) from Input 3.1 alone. The Kummer field
$K=\mathbb Q(\mu_\ell,q^{1/\ell})$ has degree $\ell(\ell-1)$ (the polynomial
$T^\ell-q$ is Eisenstein at the primes above $q$) and
$\log|d_K|+[K:\mathbb Q]\ll_q\ell(\ell-1)\log(2\ell)$; the two congruences
say that Frobenius at $p$ is trivial, that is, that $p$ splits completely in
$K$. Placing $K$ under $K\mathbb Q(\mu_{12\ell})$, whose zeta function is a
product of Hecke $L$-functions of the cyclotomic field
$\mathbb Q(\mu_{12\ell})\supseteq\mu_{12}$ and is $\zeta_K$ times entire
nonprincipal Hecke $L$-functions of $K$, gives $\zeta_K(s)\ne0$ for
$\operatorname{Re}s>1-\eta$, $s\ne1$, with the width independent of $\ell$.
A smoothed explicit formula with an error uniform in the field, using a
uniform zero count of Hasanalizade, Shen and Wong, then bounds the smoothed
prime-ideal sum by $\ll x+x^{1-\eta}(\log|d_K|+[K:\mathbb Q])$, and each
completely split prime in $(x,2x)$ contributes at least $[K:\mathbb Q]L$ to
it. Proposition 2.1 is proved in Sections 4--5 (pp. 6--20) from Inputs 4.1,
5.1 and 5.2; its result page summarizes that argument.

## Dependencies

Assumed and not proved in the manuscript: Inputs 3.1, 4.1, 5.1 and 5.2. The
manuscript attributes them to the companion *Primitive roots for every
admissible integer base*
([[integer_sequences/openai_2026_primitive_roots_admissible_integer_base/_index|card]]):
Input 3.1 to its Theorem 1.2
([[integer_sequences/openai_2026_primitive_roots_admissible_integer_base/theorem_1_2|result page]]),
Input 4.1 to the coefficient criterion of its Lemma 10.2 specialized to these
marks and to the cancellation verified in the proof of its Proposition 10.3,
Input 5.1 to its Lemma 11.1 and Input 5.2 to its Lemma 11.2. Proved in the
manuscript from the Inputs: Propositions 2.1 and 2.2. External results cited
at statement level and not checked here: quadratic reciprocity, Euler's
criterion and the Chinese remainder theorem (Section 2); abelian Artin
formalism (Neukirch, Chapter VII, Corollary 10.5 and Theorem 10.6), the
entirety of nonprincipal Hecke $L$-functions (Tate 1967) and the zero count
of Hasanalizade, Shen and Wong (2022, Corollary 1.2) for Proposition 2.2;
the prime number theorem for a fixed modulus, the Bombieri--Vinogradov
theorem (Bombieri 1965, Vinogradov 1965) and Mertens' theorem for
Proposition 2.1.

## Bears on

The manuscript names no Erdős problem; the row below is a background lead
inferred on this page, not stated in the manuscript and unverified here, and
the page's status rests on its own acceptance evidence.

- [[../wiki/problems/integer_sequences/E0985/_index|Problem 985]]: background.
  The corrected question asks whether every prime $p>2$ has a prime
  primitive root $q<p$. Under Inputs 3.1, 4.1, 5.1 and 5.2 the theorem gives,
  for any fixed finite set of primes, infinitely many $p$ at which all of
  them are primitive roots, so each such $p$ has a prime primitive root below
  it; for a single prime base, $2$ for instance, the companion claims this
  without hypotheses, and the manuscript's introduction reads Heath-Brown's
  theorem, cited on the page, as giving it for one of any three distinct
  primes. The theorem says nothing about the "every $p$" quantifier and
  bounds the least prime primitive root of no given $p$; no deduction toward
  the question is known. Unverified.
