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

For a prime $p$ and an integer $q$ with $p\nmid q$, $\operatorname{ord}_p(q)$
is the multiplicative order of $q$ in $\mathbb F_p^\times$, and $q$ is a
primitive root modulo $p$ when $\operatorname{ord}_p(q)=p-1$ (p. 1). The
theorem assumes four statements that the manuscript calls Inputs, takes from
its companion *Primitive roots for every admissible integer base*, and does
not prove. They are stated here exactly, in the corpus's words, after the
setup two of them use.

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

**Input 3.1** (uniform Hecke zero-free assertion;
`sections/03-splitting.tex` lines 8--15, p. 3). For every cyclotomic number
field $F$ containing the group $\mu_{12}$ of twelfth roots of unity and every
finite-order Hecke character $\chi$ of $F$ (a continuous character of
$F^\times\backslash\mathbb A_F^\times$ with finite image), the meromorphic
continuation of $L_F(s,\chi)$ has no zero in $\operatorname{Re}s>1-10^{-6}$.
The text adds that the principal character's pole at $s=1$ is permitted.

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

**Theorem 1.1.** Assume Inputs 3.1, 4.1, 5.1 and 5.2. Let $k\ge1$ and let
$q_1,\dots,q_k$ be distinct positive primes. Then there are constants
$c_{\mathbf q}>0$ and $x_{\mathbf q}>1$, depending on the set, such that for
every real $x\ge x_{\mathbf q}$ at least

$$
c_{\mathbf q}\,\frac{x}{(\log x)^2}
$$

primes $p\in(x,2x)$ satisfy $p\nmid q_1\cdots q_k$ and
$\operatorname{ord}_p(q_i)=p-1$ for every $1\le i\le k$.

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
48--119 and closes at lines 113--119, PDF p. 3. Read 2026-10-12. Provenance
and attestations are on
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
