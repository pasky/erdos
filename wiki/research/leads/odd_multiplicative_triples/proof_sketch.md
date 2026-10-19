---
name: research/leads/odd_multiplicative_triples/proof_sketch
title: "Three consecutive ones for odd-order multiplicative functions"
desc: |
  An end-to-end sketch for the odd-k triple question: realization and sieve
  arguments, the unresolved aggregate cofactor estimate, scoped tests of
  statistical and finite-sums mechanisms, and a conditional spectral route
  for every odd order using an explicit quotient by the bounded-distance core.
problems:
- 436
review_status: unreviewed
created: 2026-10-16T15:00:01Z
updated: 2026-10-16T15:00:01Z
---

***

This page's results that are not drawn from a cited source are Plasma AI's,
credited to Plasma AI.

## Target and conventions

Throughout, $k\ge1$ is odd, $\zeta=e^{2\pi i/k}$ and
$\mu_k=\{z\in\mathbb C:z^k=1\}$. A function $f:\mathbb N\to\mu_k$ is
completely multiplicative when $f(mn)=f(m)f(n)$ for all $m,n\ge1$; its values
at the primes are arbitrary and determine it. Put

$$
T_f=\{n\ge1:\ f(n)=f(n+1)=f(n+2)=1\},\qquad N(f)=\min T_f ,
$$

with $N(f)=\infty$ when $T_f$ is empty. The target is the statement

**T(k).** Every completely multiplicative $f:\mathbb N\to\mu_k$ has
$T_f\neq\emptyset$,

for every odd $k$, or a counterexample for one odd $k$. Section 1 proves that
T(k) is equivalent to the finiteness of $\Lambda(k,3)$, the second question
of [[problems/integer_sequences/E0436/_index|Problem 436]] for this $k$, and
that $\Lambda(k,3)=\sup_f N(f)$. The growth question of Problem 436 is not
addressed.

For $1$-bounded multiplicative $f,g$ the pretentious distance is

$$
\mathbb D(f,g;x)^2=\sum_{p\le x}
\frac{1-\operatorname{Re} f(p)\overline{g(p)}}{p}.
$$

It is nondecreasing in $x$. Say that $f$ pretends to a Dirichlet character
$\chi$ at bounded distance when $\sup_x\mathbb D(f,\chi;x)<\infty$, and that
$f$ weakly pretends to $\chi$ when $\mathbb D(f,\chi;x)^2=o(\log\log x)$,
the definition used by Tao and Teräväinen. The triangle inequality
$\mathbb D(f_1f_2,g_1g_2;x)\le\mathbb D(f_1,g_1;x)+\mathbb D(f_2,g_2;x)$
holds for $1$-bounded functions. Logarithmic averages are
$\mathbb E^{\log}_{n\le X}a(n)=\sum_{n\le X}a(n)/n\big/\sum_{n\le X}1/n$, and
a set has positive upper logarithmic density when the averages of its
indicator do not tend to $0$.

## Standing

Everything below is author-recorded and unreviewed; no claim card has been
made. Sections 1, 2 and 4 give author-recorded arguments from the explicitly
stated classical inputs and the cited accepted claim. Section 5 and Section 6
reduce the remaining cases using a source theorem held only at statement
standing. Section 7 is conditional on an open conjecture. Section 8 proves
statements about stochastic models, not about multiplicative functions.
Section 11 studies sufficient cofactor estimates, the same models, and
finite-sums arguments. Its arithmetic construction refutes a proposed
reflection constraint, not T(k); no remaining case of the target is settled.
Section 12 gives a conditional spectral route for every odd order. It removes
the bounded-distance core by an explicit pointwise section and uses the
quotient's exact invariance under multiplication by $k$th powers. The required
spectral assertion (QSP) is unproved. A simpler multiplicative factorization
works for squarefree orders, but its character-root condition can fail.

- **Proved here.** The bridge $\Lambda(k,3)=\sup_fN(f)$ (Section 1); T(3)
  with $N(f)\le23532$ for every $f$, from the accepted cubic machine proof
  (Section 2); triples with positive upper logarithmic and natural densities
  for every $f$ that weakly pretends to some Dirichlet character (Section 4).
- **Reduced, not proved.** When no nontrivial power of $f$ weakly pretends to a
  Dirichlet character, $T_f$ has positive upper logarithmic density exactly
  when the monochromatic triples $f(n)=f(n+1)=f(n+2)$ do (Section 5). The
  mixed case of composite $k$ reduces likewise (Section 6).
- **Conditional.** T(k) holds for every odd $k$ if the three-point
  logarithmically averaged Elliott conjecture holds (Section 7). For an odd
  prime $k$, T(k) also holds if every function in Case C has a logarithmic
  Furstenberg system without nonzero rational eigenvalues (Section 12).
  The hypothesis (SP) there, for functions with trivial bounded-distance
  subgroup, suffices for every squarefree odd $k$ by a character-root split.
  The hypothesis (QSP) for the specified, generally nonmultiplicative
  quotient suffices for every odd $k$. These spectral inputs are unproved.
- **Open.** Positivity of the zero-sum three-point statistic in Section 5
  and its relative form in Section 6. This is the missing sufficient density
  statement for the all-odd target; existence alone is weaker.
- **Obstructions to a mechanism.** A twisted Bohr process satisfies every
  proved averaged correlation and dilation property used in Sections 5 and 6,
  yet has no monochromatic consecutive triple, for every $k\ge5$; it violates
  exact multiplicativity at the prime $5$. A digit-twisted process satisfies
  all of these and exact self-similarity at every prime as well, with no
  monochromatic consecutive triple for every odd $k\ge7$ (Section 8). So for
  $k\ge7$ the gap cannot be closed from these logarithmic statistics alone;
  for $k=5$ that question is open. The digit-twisted process has the rational
  eigenvalue $1/3$. Section 12 proves that a process with a Haar position and
  conditional self-similarity can avoid these triples only if its colour
  process has a nonzero rational eigenvalue: without one, Furstenberg
  recurrence forces them.
- **Limits of the proposed inputs.** The conditional cofactor expansion
  of Lemma S retains the three-point problem. The independence assertion (CI)
  is a stronger sufficient condition, not a necessary condition for (AC).
  The digit-twisted process satisfies the label law and the listed stationary
  identities but not the desired cancellation; its formal cofactor variables
  are not values of a completely multiplicative function. Every polynomial
  family of consecutive values built from products of affine forms depends
  on a single affine form, so it
  is a local pattern; for odd $k\ge7$ the digit-twisted process gives
  probability zero to every family with two factors per value, and for
  odd $k\ge9$ with three.
  Hildebrand's shifted special sets cannot produce triples from first moments.
  Even an exact monochromatic finite-sums sequence can have an arbitrary
  odd-order predecessor value after normalization, even in Case C, as the
  arithmetic construction in Section 11 shows.

The full target is unresolved.

## 1. The exact bridge to Problem 436

### Realization of prime values

**Lemma R.** Let $q_1,\dots,q_r$ be distinct primes and
$\varepsilon_1,\dots,\varepsilon_r\in\mu_k$. There are infinitely many primes
$p\equiv1\pmod k$ carrying a Dirichlet character $\chi$ modulo $p$ of order
$k$ whose kernel is the group of nonzero $k$th power residues modulo $p$ and
with $\chi(q_i)=\varepsilon_i$ for every $i$.

*Proof.* Let $K=\mathbb Q(\zeta_k)$, embedded in $\mathbb C$.

Kummer independence. Let $a=\prod_iq_i^{e_i}$ with $0\le e_i<k$, and suppose
$a$ is a $k$th power in $K$. Take an odd prime $\ell$ with $\ell^m\| k$, so
$a=\beta^{\ell^m}$ with $\beta\in K$. If $a$ were not an $\ell$th power in
$\mathbb Q$, then $x^\ell-a$ would be irreducible over $\mathbb Q$:
a proper monic rational factor of degree $j<\ell$ has constant term equal,
up to sign, to $a^{j/\ell}$ times an $\ell$th root of unity, so its
$\ell$th power forces $\ell\mid jv_r(a)$ for every rational prime $r$.
Since $(j,\ell)=1$, that would make $a$ an $\ell$th power. Thus
$\mathbb Q(\beta^{\ell^{m-1}})$ would have degree $\ell$. That field is
Galois over $\mathbb Q$, since $K/\mathbb Q$ is abelian, so it would contain
the ratio $\zeta_\ell$ of two roots of $x^\ell-a$, whose degree $\ell-1\ge2$
does not divide $\ell$. Hence $a=c^\ell$ with $c>0$ rational. Then
$c=\eta\beta^{\ell^{m-1}}$ for some $\eta\in\mu_\ell$, and
$\eta=\eta'^{\ell^{m-1}}$ for some $\eta'\in\mu_{\ell^m}\subset K$, so $c$ is
an $\ell^{m-1}$th power in $K$. Induction on $m$ makes $a$ an $\ell^m$th power
in $\mathbb Q$. Over all prime powers exactly dividing $k$ this gives
$k\mid e_i$, so every $e_i=0$. Oddness of $k$ is used here.

Let $L=K(q_1^{1/k},\dots,q_r^{1/k})$. This is a finite Galois extension
of $K$, and $\sigma\mapsto(\sigma(q_i^{1/k})/q_i^{1/k})_i$ embeds its Galois
group in $\mu_k^r$. If the image were proper, a nontrivial character of
$\mu_k^r$ annihilating it would give exponents $0\le e_i<k$, not all zero,
for which $\prod_iq_i^{e_i/k}$ is fixed by the Galois group, hence lies in
$K$. Its $k$th power contradicts the independence just proved. Thus the
embedding is onto. Let $\sigma$ map to
$(\varepsilon_i)$. By the Chebotarev density theorem there are infinitely many
primes $\mathfrak p$ of $K$ of degree one, prime to $kq_1\cdots q_r$, with
Frobenius $\sigma$. Here Chebotarev gives positive density among all prime
ideals of $K$, while those of residue degree at least two have counting
function $O_K(\sqrt x)$; hence degree-one primes suffice. Their rational
norms $p$ take infinitely many values and satisfy $p\equiv1\pmod k$. The
Frobenius congruence $\sigma(x)\equiv x^p$ modulo a prime of $L$ above
$\mathfrak p$, applied to $x=q_i^{1/k}$, gives
$\varepsilon_i\equiv q_i^{(p-1)/k}$ modulo
$\mathfrak p$. Let $\chi(n)$ be the $k$th power residue symbol
$(n/\mathfrak p)_k$, the element of $\mu_k$ congruent to $n^{(p-1)/k}$ modulo
$\mathfrak p$; it is well defined because distinct $k$th roots of unity stay
distinct modulo $\mathfrak p$. It is a character modulo $p$ of order $k$,
its kernel is the set of $k$th power residues, and $\chi(q_i)=\varepsilon_i$.
$\square$

### The proposition

**Proposition B.** For odd $k$, $\Lambda(k,3)=\sup_fN(f)$, the supremum over
all completely multiplicative $f:\mathbb N\to\mu_k$, as an element of
$\mathbb N\cup\{\infty\}$. In particular $\Lambda(k,3)<\infty$ if and only if
T(k) holds.

*Proof.* Three steps.

Compactness. Identify such functions with points of
$\Omega=\mu_k^{\mathcal P}$, $\mathcal P$ the primes, a compact product space.
The set $\{f:N(f)\le M\}$ depends only on the values at primes up to $M+2$,
so it is open. If T(k) holds these sets cover $\Omega$, so one of them is all
of $\Omega$, and $C(k):=\sup_fN(f)$ is finite.

Lower bound. Let $f$ be given, and let $M=N(f)$ if $N(f)$ is finite and $M$ be
any positive integer otherwise. Lemma R, applied to the primes up to $M+2$
with $\varepsilon_i=f(q_i)$, gives infinitely many primes $p>M+2$ whose
character $\chi$ agrees with $f$ on $[1,M+2]$, since both are completely
multiplicative there and $p$ divides none of these integers. A triple of
$k$th power residues modulo $p$ starting at $r\le M$ is then a triple of ones
of $f$. If $N(f)$ is finite, the first such triple starts at $N(f)$, so
$r(k,3,p)=N(f)$ for infinitely many $p$. If $T_f$ is empty, $r(k,3,p)>M$ for
infinitely many $p$, for every $M$. Hence $\Lambda(k,3)\ge N(f)$ for every
$f$, and $\Lambda(k,3)=\infty$ if some $T_f$ is empty.

Upper bound. Suppose T(k), so $C(k)<\infty$. Let $p>C(k)+2$ be prime and
$d=\gcd(k,p-1)$. The $k$th power residues modulo $p$ are the $d$th power
residues, the image of $x\mapsto x^k$ on the cyclic group
$(\mathbb Z/p\mathbb Z)^\times$. If $d=1$ every integer prime to $p$ is a
residue and $r(k,3,p)=1$. Otherwise let $\psi$ be a character modulo $p$ of
order $d$; its values lie in $\mu_d\subset\mu_k$ and its kernel is the set of
residues. Let $f_p$ be completely multiplicative with $f_p(q)=\psi(q)$ for
primes $q\ne p$ and $f_p(p)=1$. Then $n=N(f_p)\le C(k)$, the integers
$n,n+1,n+2$ are below $p$, and $\psi=f_p=1$ there. So $r(k,3,p)\le C(k)$ and
$\Lambda(k,3)\le C(k)$. With the lower bound, $\Lambda(k,3)=C(k)$. $\square$

The upper bound does not use oddness. The realization lemma does, and this is
the only point where the bridge itself depends on $k$ being odd. For even $k$,
T(k) fails: let $f(q)=(q/3)$ for primes $q\ne3$ and $f(3)=1$; any three
consecutive integers contain one congruent to $2$ modulo $3$, where $f=-1$.
This matches Lehmer and Lehmer's $\Lambda(k,3)=\infty$ for even $k$, recorded
on the problem page.

## 2. The case k = 3

**Corollary 3.** Every completely multiplicative $f:\mathbb N\to\mu_3$ has
$N(f)\le23532$, and equality holds for some $f$.

*Proof.* The accepted
[[problems/integer_sequences/E0436/claims/1962_01_01_lehmer_lehmer_mills_selfridge|Lehmer, Lehmer, Mills and Selfridge claim]]
gives that every prime outside a list of thirteen has three consecutive cubic
residues starting at or below $23532$, and that infinitely many primes have
that triple as their first. For a given $f$, Lemma R gives infinitely many
primes $p>23534$ whose cubic character agrees with $f$ on $[1,23534]$, so the
triple of residues below $23534$ is a triple of ones of $f$. Proposition B
turns the attained value into a function with $N(f)=23532$. $\square$

This inherits the standing of the source: a refereed publication whose machine
case analysis carries no independent review in this corpus. It shows that the
function formulation has no exceptional cases for $k=3$; the thirteen
exceptional primes of the source are small primes, not exceptional functions.

## 3. The case split

Let $H(f)$ be the set of residues $j$ modulo $k$ for which $f^j$ weakly
pretends to some Dirichlet character. It contains $0$, is closed under
negation by complex conjugation, and is closed under addition by the triangle
inequality, because $(a+b)^2\le2a^2+2b^2$ keeps the bound $o(\log\log x)$.
So $H(f)=d\mathbb Z/k\mathbb Z$ for a unique divisor $d$ of $k$.

- **Case A, $d=1$.** $f$ weakly pretends to a character. Section 4 proves
  $T_f$ infinite.
- **Case C, $d=k$.** No power $f^j$ with $k\nmid j$ weakly pretends to any
  character. Section 5 reduces T(k) to monochromatic triples.
- **Case B, $1<d<k$.** Possible only for composite $k$, such as $k=9$ or
  $15$. Section 6.

For prime $k$ only Cases A and C occur.

## 4. Case A: weakly pretentious functions

**Theorem W.** Let $f:\mathbb N\to\mu_k$ be completely multiplicative, $k$
odd, and suppose that $f$ weakly pretends to a Dirichlet character $\chi$
modulo $q$. Then $T_f$ has positive upper natural density and positive upper
logarithmic density. If the pretentious distance is bounded, both lower
densities are positive.

The case $k=1$ is immediate; assume $k\ge3$ throughout the proof. The sieve
input below is a standard theorem. Its application to the three forms,
including the sum of all remainders, is derived here.

### A finite-prime probability model

Fix $P_0\ge5$, larger than every prime divisor of $q$, and set

$$
Q=\left(q\prod_{p\le P_0}p\right)^k,\qquad
B=q\prod_{p\le P_0,\ p\nmid q}p,\qquad
c_0=\frac1q\prod_{p\le P_0,\ p\nmid q}(1-1/p).
$$

The conditions $m\equiv1\pmod q$ and $(m,Q)=1$ select a fixed set of
$Bc_0$ residue classes modulo $B$. Put
$L_1(m)=Qm-1$, $L_2(m)=m$, and $L_3(m)=Qm+1$.
For these $m$, all three forms are prime to $Q$ and pairwise coprime.
For each $p>P_0$ their three zeros modulo $p$ are distinct.

For $y=x^\varepsilon$, let $V_p(m)=i$ if $p\mid L_i(m)$, and let
$V_p(m)=0$ otherwise, for $P_0<p\le y$. Compare this vector, with $m$
uniform among the selected integers up to $x$, with independent variables
$V_p^*$ satisfying

$$
\Pr(V_p^*=i)=1/p\quad(1\le i\le3),\qquad
\Pr(V_p^*=0)=1-3/p.
$$

**Lemma S.** For every sufficiently small fixed $\varepsilon>0$, the total
variation distance between these two vector laws is at most
$C\varepsilon+r(1/(4\varepsilon))+o_{Q,B}(1)$ as $x\to\infty$, where
$C$ is absolute and $r(s)\to0$ as $s\to\infty$. In particular the bound is
uniform over all functions of the vector with absolute value at most one.
The last assertion allows a harmless factor two in the bound.

*Proof.* A vector is specified by a squarefree product $d$ of the primes
with nonzero labels and a choice of one of three labels for each $p\mid d$.
Write $D(m)=\prod_{V_p(m)\ne0}p$ and define $D^*$ in the independent model.
Chinese remaindering gives

$$
\mathbb E\log D(m)
 \le 3\sum_{p\le y}\frac{\log p}{p}+o(\log x)
 \ll\varepsilon\log x+o(\log x),
$$

because each divisibility count is $3c_0x/p+O_B(1)$ and the sum of its
errors is $O_B(y\log y)$. The same bound holds for $D^*$. Markov's
inequality shows that both laws give mass $O(\varepsilon)+o(1)$ to
$d>x^{1/4}$.

For a specified labelled $d\le x^{1/4}$, its positive divisibility conditions
select one class modulo $d$, independently of the classes modulo $B$. Sift
out all primes in $(P_0,y]$ not dividing $d$ from $L_1L_2L_3$. For a
squarefree product $e$ of those primes, the relevant count is

$$
\frac{c_0x}{d}\frac{3^{\omega(e)}}e+O_B(3^{\omega(e)}).
$$

Use the fundamental lemma in dimension three with level
$D_0=x^{1/2}/d$. More explicitly, the input is Theorem 18.11(a) of
Koukoulopoulos, *The Distribution of Prime Numbers*, author's preliminary
version, p. 190, proved from Theorem 19.1 on pp. 195--199. For sieve density
$\nu(p)=3$ and $s=\log D_0/\log y$, it estimates the sifted count by its
Euler product with relative error $O(s^{-s/2})$, plus the sum of the absolute
divisibility remainders for $e\le D_0$. Its dimension hypothesis holds
uniformly after any primes are deleted, since
$\prod_{w<p\le z}(1-3/p)^{-1}\le(\log z/\log w)^3(1+C_1/\log w)$ for
$p>5$, by the Mertens product estimate. Here $s\ge1/(4\varepsilon)$.
Consequently the number of $m$ realizing this entire vector is

$$
\frac{c_0x}{d}\prod_{\substack{P_0<p\le y\\p\nmid d}}(1-3/p)
 \big(1+O(r(1/(4\varepsilon)))\big)
 +O_B\big((x^{1/2}/d)(\log x)^2\big).
$$

The main term divided by $c_0x$ is exactly the independent probability of
this labelled vector. There are $3^{\omega(d)}$ labelings for each $d$.
Summing the absolute remainders over all $d\le x^{1/4}$ costs at most

$$
O_B\left(x^{1/2}(\log x)^2
       \sum_{d\le x^{1/4}}\frac{3^{\omega(d)}}d\right)
 =O_B(x^{1/2}(\log x)^5)=o(x).
$$

The estimates used here follow from $3^{\omega(e)}\le\tau_3(e)$ and the
three-divisor convolution. The relative main-term errors sum to at most a
constant times $r(1/(4\varepsilon))$, since the model probabilities sum to
one. Adding the two large-$d$ tails and normalizing by
$\#\{m\le x:m\equiv1\pmod q,(m,Q)=1\}=c_0x+O_B(1)$ proves the lemma.
$\square$

### Application to the weakly pretentious function

(W0) The character has order dividing $k$. Indeed,
$\mathbb D(1,\chi^k;x)\le k\mathbb D(f,\chi;x)
=o(\sqrt{\log\log x})$. For every nonprincipal Dirichlet character $\psi$,
$\mathbb D(1,\psi;x)^2=\log\log x+O_\psi(1)$, by the prime number theorem
in fixed arithmetic progressions. Therefore $\chi^k$ is principal and
$\chi(-1)=1$, since $k$ is odd.

(W1) Put $u(p)=f(p)\overline{\chi(p)}\in\mu_k$ for $p\nmid q$, and extend
$u$ completely multiplicatively on integers prime to $q$. With
$E=\{p\nmid q:u(p)\ne1\}$, weak pretence and the positive minimum of
$1-\operatorname{Re}z$ over $z\in\mu_k\setminus\{1\}$ give

$$
H_E(x):=\sum_{p\in E,\ p\le x}\frac1p=o(\log\log x).
$$

(W2) Let $G$ be the least subgroup of $\mu_k$ for which
$\sum_{u(p)\notin G}1/p<\infty$. Such a least subgroup exists: the family
is nonempty and closed under intersections. Write $g=|G|$,
$E_1=\{p\in E:u(p)\notin G\}$, and $E_2=E\setminus E_1$.
For every nontrivial character $\psi$ of $G$, minimality implies

$$
\sum_{p\in E_2}\frac{1-\operatorname{Re}\psi(u(p))}{p}=\infty.
$$

Otherwise $\ker\psi$ would be a smaller allowable subgroup; the positive
minimum of $1-\operatorname{Re}\psi(z)$ outside that kernel justifies this
implication.

(W3) Use the forms of Lemma S. Since $f(Q)=1$,
$\chi(Qm\pm1)=\chi(\pm1)=1$, and $\chi(m)=1$, their simultaneous values
$u(L_1)=u(L_2)=u(L_3)=1$ give the required triple starting at $Qm-1$.

(W4) For each of the three forms, discard a value of $m$ if a prime in
$E_1$ above $y$, or in $E_2\cap(y,Qx+1]$, divides that form, or if a prime
$p>P_0$ divides it to exponent at least two. The number discarded is at most

$$
3x\sum_{p\in E_1,\ p>y}\frac1p+
3x\sigma(x)+O(x/P_0)+o_Q(x),\qquad
\sigma(x)=\sum_{p\in E_2,\ x^\varepsilon<p\le Qx+1}\frac1p.
$$

This bound is over all $m\le x$, so also holds on the selected classes.
For a prime or prime square coprime to $Q$, each form has one zero class;
summing the $O(1)$ counting errors gives
$O_Q(\pi(Qx)+\pi(\sqrt{Qx+1}))=o_Q(x)$. The square contribution uses
$\sum_{p>P_0}p^{-2}\ll1/P_0$. No prime divisor of $Q$ occurs in a form.

(W5) In the finite-prime model, require no prime in $E_1$ to have a nonzero
label and require that the products of the $u(p)$ assigned to each of the
three forms are all $1$. Fourier expansion on $G^3$ gives its probability
as $g^{-3}$ times the sum, over $\psi_1,\psi_2,\psi_3\in\widehat G$, of

$$
\prod_{P_0<p\le y}
 \left(1+\frac{\sum_{i=1}^3(\Phi_i(p)-1)}p\right),\qquad
\Phi_i(p)=
\begin{cases}
0,&p\in E_1,\\
\psi_i(u(p)),&p\notin E_1.
\end{cases}
$$

When all characters are trivial the product tends to
$\kappa:=\prod_{p\in E_1,\ p>P_0}(1-3/p)>0$.
Otherwise choose a nontrivial $\psi_j$. The modulus of the product is at
most

$$
\exp\left(-\sum_{\substack{p\in E_2\\P_0<p\le y}}
 \frac{1-\operatorname{Re}\psi_j(u(p))}{p}+O(1)\right)=o(1),
$$

using $|1+z|\le\exp(\operatorname{Re}z+|z|^2/2)$ and
$\sum_p p^{-2}<\infty$. Thus the independent probability tends to
$\kappa/g^3$. Lemma S gives the same probability for the selected $m$ up
to an error that can be made arbitrarily small by choosing $\varepsilon$
small, then $x$ large. On removing the exceptional $m$ of (W4), the
finite-prime products are their actual values $u(L_i(m))$.

(W6) There are arbitrarily large $X$ with

$$
\sum_{\substack{p\in E_2\\X^{\varepsilon^2}<p\le QX+1}}\frac1p\le\delta
$$

for any fixed $\varepsilon,\delta>0$. If every sufficiently large $X$
violated this, choose $X_{j+1}=X_j^{2/\varepsilon^2}$ starting sufficiently
large. The windows are disjoint, each carries mass greater than $\delta$,
and $\log\log X_j=O(j)$. This contradicts $H_E(x)=o(\log\log x)$.
For such an $X$, the bound $\sigma(x)\le\delta$ holds simultaneously for
all $X^\varepsilon\le x\le X$.

(W7) Choose $P_0$ sufficiently large that the $O(1/P_0)$ term in (W4) is
small compared with $c_0\kappa/g^3$. This is possible: as $P_0\to\infty$,
$\kappa\to1$ and $c_0\asymp_q1/\log P_0$. Fix this $P_0$ and hence $Q,B$.
Choose $\varepsilon$ small enough for the error in Lemma S, then $\delta$
small enough in (W6). For all large good $X$, (W4)--(W6) show, uniformly
for $X^\varepsilon\le x\le X$, that

$$
\#\{m\le x:\ m\equiv1\pmod q,\ (m,Q)=1,\ u(L_1)=u(L_2)=u(L_3)=1\}
 \ge a x
$$

with some fixed $a>0$, for example any sufficiently small constant below
$c_0\kappa/g^3$. Consequently $A(t):=|T_f\cap[1,t]|\ge(a/Q)t$ for
$QX^\varepsilon\le t\le QX$. This proves positive upper natural density.
Partial summation also gives

$$
\sum_{n\le QX}\frac{\mathbf1_{T_f}(n)}n
 \ge\int_{QX^\varepsilon}^{QX}\frac{A(t)}{t^2}\,dt
 \ge\frac aQ(1-\varepsilon)\log X.
$$

Thus the upper logarithmic density is positive as well. If the pretentious
distance is bounded, then $\sum_{p\in E}1/p<\infty$ and $G=\{1\}$.
In that case $\sigma(x)\to0$ at every large $x$, so the same proof gives
$A(t)\gg_f t$ for every sufficiently large $t$, proving both lower-density
assertions. $\square$

**Scope of the sieve mechanism.** It randomizes a sparse exceptional set of
primes at well chosen scales. Sifting out all exceptional primes is not an
adequate substitute when their reciprocal sum diverges: the sifted density
can tend to zero. Nor does a fixed positive upper natural density alone
imply a positive upper logarithmic density; the full intervals of good
scales in (W6) supply the additional argument.

## 5. Case C: reduction to monochromatic triples

For every $n$,

$$
\mathbf 1_{T_f}(n)=k^{-3}\sum_{a,b,c\in\mathbb Z/k\mathbb Z}
f(n)^af(n+1)^bf(n+2)^c,
\qquad
\sum_{a+b+c\equiv0}x^ay^bz^c=k^2\,\mathbf 1[x=y=z]\quad(x,y,z\in\mu_k).
$$

Corollary 1.6 of Tao and Teräväinen's Duke paper, quoted as Theorem 1.5 in
[[../library/arithmetic_functions/tao_2019_structure_correlations_multiplicative_functions_at_almost/_index|their 2019 structure paper]],
states: if $1$-bounded multiplicative $g_1,\dots,g_r$ have a product that does
not weakly pretend to any Dirichlet character, then
$\mathbb E^{\log}_{n\le X}g_1(n+h_1)\cdots g_r(n+h_r)\to0$ for all integers
$h_i$. The term $(a,b,c)$ has product $f^{a+b+c}$.

**Proposition N.** In Case C,
$\mathbb E^{\log}_{n\le X}\mathbf 1_{T_f}(n)=\frac1k\,\mathbb E^{\log}_{n\le X}
\mathbf 1[f(n)=f(n+1)=f(n+2)]+o(1)$.

*Proof.* The terms with $a+b+c\not\equiv0$ have products $f^{a+b+c}$ that do
not weakly pretend, so they tend to $0$; the remaining terms sum to
$k^2\mathbf 1[f(n)=f(n+1)=f(n+2)]$. $\square$

So in Case C the set $T_f$ has positive upper logarithmic density exactly when
the monochromatic consecutive triples do. The open statement is:

**(Z).** For every $f$ in Case C, the set of $n$ with $f(n)=f(n+1)=f(n+2)$
has positive upper logarithmic density.

(Z) is stronger than what T(k) needs, which is one triple. With Theorem W and
Proposition N, (Z) for prime $k$ gives T(k).

**The zero-sum statistics.** Tao's logarithmically averaged two-point Elliott
theorem, as stated in the 2019 paper (Conjecture 1.3(ii) with $k=2$, proved
in Tao's 2016 paper), kills $\mathbb E^{\log}f^a(n)\overline{f^a(n+h)}$ for
$h\ne0$ once $f^a$ satisfies the uniform hypothesis (1) of that paper, which
Lemma U of Section 7 supplies in Case C. Hence

$$
\mathbb E^{\log}_{n\le X}\mathbf 1[f(n)=f(n+1)=f(n+2)]
=k^{-2}\Big(1+\sum_{(a,b,c)\in Z_k}
\mathbb E^{\log}_{n\le X}f(n)^af(n+1)^bf(n+2)^c\Big)+o(1),
$$

where $Z_k$ is the set of $(a,b,c)$ with $a,b,c\not\equiv0$ and
$a+b+c\equiv0\pmod k$, of size $(k-1)(k-2)$. These are the zero-sum
three-point statistics; their products are identically $1$, so no
product-based cancellation reaches them, and they are the analogue of
even-order Chowla correlations. (Z) fails exactly when their sum tends to
$-1$. For $k=3$, $Z_3=\{(1,1,1),(2,2,2)\}$ and (Z) fails exactly when
$f(n)f(n+1)f(n+2)\ne1$ on a set of logarithmic density one. Corollary 3
supplies existence, not this stronger density assertion.

The structure theorem quoted as Theorem 1.6 in the same paper (Theorem 1.1 of
the Duke paper) says that each zero-sum correlation sequence
$F(a)=\lim^*\mathbb E^{\log}f^{e_1}(n)f^{e_2}(n+a)f^{e_3}(n+2a)$, taken along a
generalised limit, is a uniform limit of periodic functions $F_i$ with
$F_i(ab)=F_i(a)$ for $b$ prime to the period. It is used here only for
$a\ne0$. Read literally at $a=0$ it would already fail for two functions: for
$f^a$ and its conjugate with shifts $0,1$ the sequence is $1$ at $a=0$ and $0$
elsewhere by the two-point theorem, which is not a uniform limit of periodic
functions. Section 8 shows that this isotypy, with the other averaged
constraints, still does not force (Z).

## 6. Case B: composite k

Let $1<d<k$ with $H(f)=d\,\mathbb Z/k\mathbb Z$. Terms with
$a+b+c\notin d\,\mathbb Z$ vanish by the same theorem, and
$\sum_{a+b+c\equiv0\,(d)}x^ay^bz^c=(k^3/d)\,\mathbf 1[x=y=z\in\mu_d]$, so

$$
\mathbb E^{\log}_{n\le X}\mathbf 1_{T_f}(n)=\frac1d\,\mathbb E^{\log}_{n\le X}
\mathbf 1\big[f(n)=f(n+1)=f(n+2),\ f(n)^d=1\big]+o(1).
$$

Theorem W applied to $f^d$, which weakly pretends to a character, gives a
positive upper logarithmic density of $n$ with $f(n),f(n+1),f(n+2)\in\mu_d$. The
remaining requirement, equality of the three values inside $\mu_d$ on that
structured set, is the zero-sum difficulty of Section 5 relative to $f^d$.

## 7. Conditional completion

**Lemma U.** Let $g$ be completely multiplicative with $g(p)\in\mu_k$ for
every prime, and suppose $\mathbb D(g,\chi;X)\to\infty$ for every Dirichlet
character $\chi$. Then $\inf_{|t|\le X}\mathbb D(g,\chi(n)n^{it};X)\to\infty$
for every $\chi$.

*Proof.* Suppose $\mathbb D(g,\chi n^{it_j};X_j)\le B$ along $X_j\to\infty$
with $|t_j|\le X_j$, and pass to a subsequence on which $|t_j|\log X_j$ either
stays bounded or tends to infinity. In the first case
$\mathbb D(n^{it_j},1;X_j)=O(1)$, so $\mathbb D(g,\chi;X_j)$ is bounded,
which is impossible. In the second, the triangle inequality and $g^k=1$ give
$\mathbb D(1,\chi^kn^{ikt_j};X_j)\le kB$. For fixed $\psi=\chi^k$ and
$1/\log X\le|\tau|\le kX$ one has
$\mathbb D(1,\psi n^{i\tau};X)^2
=\log\log X-\log|L(1+1/\log X+i\tau,\overline\psi)|+O_\psi(1)$.
Indeed the Euler product differs from the prime sum truncated at $X$ by
$O(1)$ uniformly in $\tau$; the omitted prime powers and the absolutely
weighted prime tail have bounded sums. The following bounds apply to
$\overline\psi$ as well as to $\psi$. For $|\tau|\le1$ the logarithm of
the $L$-value is at most
$\log\min(\log X,1/|\tau|)+O(1)$, and for $|\tau|\ge1$ the
fixed-modulus consequence of the Vinogradov--Korobov bound
$|L(1+1/\log X+i\tau,\psi)|\ll_\psi
(\log(|\tau|+3))^{3/4}$ makes it at most
$\frac34\log\log X+O_{\psi,k}(1)$. The exponent $3/4$ absorbs the usual
$\log\log$ factor in the sharper $2/3$ estimate. Either way
$\mathbb D(1,\psi n^{i\tau};X)\to\infty$, a contradiction. $\square$

**Theorem C (conditional).** Assume the three-function case of the
logarithmically averaged Elliott conjecture, Conjecture 1.3(ii) of the 2019
paper with $k=3$: if one of three $1$-bounded multiplicative functions
satisfies the uniform hypothesis (1), then
$\mathbb E^{\log}_{n\le X}g_1(n)g_2(n+1)g_3(n+2)\to0$. Then T(k) holds for
every odd $k$, so $\Lambda(k,3)<\infty$ for every odd $k$.

*Proof.* Let $H_B$ be the set of $j$ for which $f^j$ pretends to some
character at bounded distance; it is a subgroup $d'\mathbb Z/k\mathbb Z$ by the
triangle inequality. For $j\notin H_B$ and every $\chi$,
$\mathbb D(f^j,\chi;X)$ is unbounded and nondecreasing, so it tends to
infinity, and Lemma U gives hypothesis (1) for $f^j$. Every term
$f^a(n)f^b(n+1)f^c(n+2)$ with an exponent outside $H_B$ then tends to $0$. The
terms with $a,b,c\in H_B$ sum to $(k/d')^3\mathbf 1[f^{d'}(n)=f^{d'}(n+1)=
f^{d'}(n+2)=1]$. The function $f^{d'}$ maps into $\mu_{k/d'}$, with $k/d'$
odd, and pretends to a character at bounded distance, so by the bounded-distance
form of Theorem W the set of its triples of ones has positive lower density.
The retained part of the indicator is exactly $d'^{-3}$ times that
quotient triple indicator. Hence $T_f$ has positive lower logarithmic
density. $\square$

Theorem C uses only Section 1, Lemma U and the bounded-distance sieve.
For the unconditional route of Sections 4 to 6, positivity of the residual
diagonal mass remains. Full three-point Elliott cancellation is a stronger
sufficient input; the precise aggregate alternative is in Section 10.

## 8. Twisted Bohr processes

This section concerns stationary stochastic processes, not multiplicative
functions. The first shows that the averaged constraints used above cannot by
themselves prove (Z) for any $k\ge5$; the second adds exact self-similarity at
every prime and still has no triples for $k\ge7$.

**The process.** Let $\beta,\gamma$ be uniform on $\mathbb T=\mathbb
R/\mathbb Z$, $\sigma$ uniform on $\{\pm1\}$ and $R$ uniform on $\mathbb
Z/5\mathbb Z$, all independent. For $h\in\mathbb Z$ put

$$
Y_h=\gamma+\sigma\Big(h\beta+\frac{(R+h)^2}{5}\Big)\in\mathbb T,
\qquad X_h=\zeta^{\lfloor kY_h\rfloor},
$$

so $X_h=\zeta^c$ exactly when $Y_h$ lies in the arc
$I_c=[c/k,(c+1)/k)$. Shifting $h$ by one replaces $(\gamma,R)$ by
$(\gamma+\sigma\beta,\,R+1)$, which has the same joint law with
$(\beta,\sigma)$, so $(X_h)$ is stationary. For fixed irrational $\beta$ and
fixed $\sigma$ the process is a rotation by $(\sigma\beta,1)$ of
$\mathbb T\times\mathbb Z/5\mathbb Z$, which is ergodic.

**Properties.** Each is checked directly.

- (M1) Rotation. Replacing $\gamma$ by $\gamma+1/k$ multiplies every $X_h$ by
  $\zeta$, so every correlation $\mathbb E\prod_jX_{h_j}^{a_j}$ with
  $\sum_ja_j\not\equiv0\pmod k$ vanishes, as Theorem 1.5 requires in Case C.
- (M2) Pairs. For $h\ne0$, $Y_h-Y_0=\sigma(h\beta+(2Rh+h^2)/5)$ is uniform and
  independent of $Y_0=\gamma+\sigma R^2/5$, so $(X_0,X_h)$ is uniform on
  $\mu_k^2$, as the two-point theorem requires.
- (M3) Dilations. For $b$ prime to $5$, the law of $(Y_{abh_j})_j$ equals the
  law of $(Y_{ah_j})_j$ for all integers $a,h_j$: write $R=bR'$ and use
  $b^2\equiv\pm1\pmod5$, which turns the quadratic part into
  $\pm(R'+ah_j)^2/5$, absorbed by replacing $(\sigma,\beta)$ with
  $(\pm\sigma,\pm b\beta)$. Every correlation sequence $F(a)$ is therefore
  constant on the integers prime to $5$. For $5\mid a$ the quadratic part is
  the constant $R^2/5$ and $5\beta$ is uniform, so $F$ is constant there too.
  So $F$ is exactly $5$-periodic on $a\ne0$ and isotypic for the principal
  character, the structure Theorem 1.6 prescribes. The same computation gives
  the dilation invariance $(X_{ph})_h\overset{d}{=}(\varepsilon X_h)_h$ for
  every prime $p\ne5$ and every $\varepsilon\in\mu_k$, the form of Tao's
  entropy-decrement identity for most primes.
- (M4) No monochromatic three-term progression with difference prime to $5$.
  The second difference $Y_0-2Y_d+Y_{2d}$ equals $2\sigma d^2/5$, which is
  $\pm2/5$ modulo $1$ when $5\nmid d$. If $X_0=X_d=X_{2d}=\zeta^c$, write the
  three points as $c/k+\alpha_1$, $c/k+\alpha_2$, $c/k+\alpha_3$ with
  $\alpha_i\in[0,1/k)$; then $\alpha_1-2\alpha_2+\alpha_3\in(-2/k,2/k)$, while
  it must be congruent to $\pm2/5$ modulo $1$. For $k\ge5$ this is impossible.
  In particular $X_0=X_1=X_2$ never happens, so the analogue of $T_f$ is empty.

So for every $k\ge5$ the process has all the averaged properties that the
proved theorems cited in Sections 5 and 6 give: vanishing for nonzero total
exponents, pair uniformity, isotypy of every
nonzero-dilation correlation sequence, and dilation invariance
for every prime other than $5$. Yet (Z) fails for it. Its zero-sum
correlations do not all vanish. That is a failure of the
additional statistical conclusion sought from Elliott for multiplicative
functions, not a disproof of that conjecture. Any proof of (Z) must use more
than these listed identities. For $k=3$ the bound $2/5<2/3$ allows monochromatic
triples, and more generally a twist whose second differences have norm at
least $2/k$ needs $2/k\le1/2$, so no such arc model exists for $k=3$. This
matches the threshold in Tao and Teräväinen's value-pattern theorems (Section
9, item 4) and the machine-proved case $k=3$.

**Where the model fails.** Exact multiplicativity gives an identity at each
single prime $p$, not only on average over primes: among $n$ divisible by $p$,
the triple $(f(n),f(n+p),f(n+2p))$ equals $f(p)(f(m),f(m+1),f(m+2))$ with
$m=n/p$. So the probability that $(X_n,X_{n+p},X_{n+2p})$ is monochromatic,
conditioned on $p\mid n$, must equal the probability that
$(X_0,X_1,X_2)$ is, which is $0$ in the model. For $p=5$ the model's step-$5$
triples are exact progressions $Y_0,Y_0+5\sigma\beta,Y_0+10\sigma\beta$, and
they are monochromatic with positive probability. In an ergodic component
of the underlying rotation, a joining with the
position $n\bmod5$ is a mixture of identifications with $R$ plus a constant;
conditional on $R$, $Y_0$ is uniform. A joining of the colour factor lifts to
this underlying system by conditional disintegration. So the conditioned
probability is positive under every joining with the position, and the model
is not the logarithmic statistics of any completely multiplicative function.
For $k=5$ a proof of (Z) can act here, through the self-similarity at the
specific primes where a rational twist lives. For $k\ge7$ the next process
shows that self-similarity is not enough either.

### A self-similar digit-twisted process for k at least 7

Let $\Pi$ be Haar-distributed on $\widehat{\mathbb Z}$, independent of
$\beta,\gamma,\sigma$. For $x\in\widehat{\mathbb Z}$ with nonzero $3$-adic
component let $u(x)\in\{1,2\}$ be the last nonzero digit of that component in
base $3$, and put $\phi(x)=0$ if $u(x)=1$ and $\phi(x)=1/3$ if $u(x)=2$. Let

$$
Y_n=\gamma+\sigma\big(n\beta+\phi(\Pi+n)\big),
\qquad X_n=\zeta^{\lfloor kY_n\rfloor},
$$

jointly with the position $\Pi+n$. Shifting $n$ replaces $(\gamma,\Pi)$ by
$(\gamma+\sigma\beta,\Pi+1)$, so the joint process is stationary.

- (D1) Consecutive triples. Of $y,y+1,y+2$ exactly one is divisible by $3$;
  the other two have last digits fixed by their residues, and the multiple of
  $3$ has a free digit $s\in\{1,2\}$. In all six cases
  $\phi(y)-2\phi(y+1)+\phi(y+2)\equiv\pm1/3\pmod1$. As in (M4), three points
  in one arc of length $1/k$ have second difference of absolute value below
  $2/k\le1/3$ when $k\ge6$, so $X_n=X_{n+1}=X_{n+2}$ never happens for odd
  $k\ge7$.
- (D2) Exact self-similarity at every prime. Conditioned on $p\mid\Pi$, write
  $\Pi=p\Pi'$, with $\Pi'$ Haar-distributed. Since $u(3x)=u(x)$, and
  $u(px)\equiv p\,u(x)\pmod3$ for $p\ne3$, one has $\phi(3x)=\phi(x)$,
  $\phi(px)=\phi(x)$ for $p\equiv1\pmod3$ and $\phi(px)=1/3-\phi(x)$ for
  $p\equiv2\pmod3$. So $(Y_{ph})_h$ is the same construction driven by
  $(\gamma,\sigma,p\beta,\Pi')$, or by $(\gamma+\sigma/3,-\sigma,-p\beta,\Pi')$
  when $p\equiv2\pmod3$, and these have the original joint law. Hence the law
  of $((X_{ph})_h,\Pi/p)$ given $p\mid\Pi$ is the law of $((X_h)_h,\Pi)$.
- (D3) The averaged properties. Rotation invariance comes from $\gamma$, and
  pair uniformity, jointly with the position, from $\beta$. The law of
  $(Y_{ah_j})_j$ depends only on $v_3(a)$, by the substitution of (M3) in
  $\mathbb Z_3$, and it converges as $v_3(a)\to\infty$, because with
  probability $1-3^{-v_3(a)}$ all the digits $u(\Pi+ah_j)$ equal $u(\Pi)$.
  So on nonzero dilations every correlation sequence is a uniform limit of
  $3^{i+1}$-periodic functions isotypic for the principal character, and the
  unconditioned law is dilation invariant at every prime other than $3$.

So for odd $k\ge7$ a process can have every property of the logarithmic
statistics of a function in Case C used on this page, exact self-similarity at
each prime included, and still have no monochromatic consecutive triple. No
argument that uses only these properties can prove (Z) for $k\ge7$. The
process has a nontrivial local linear-phase component. For example,
on the class $\Pi+n\equiv1\pmod3$ its twist is zero. The function
$t\mapsto\zeta^{\lfloor kt\rfloor}$ has a nonzero Fourier coefficient at
frequency one, so a typical ergodic component has a nonvanishing correlation
with a suitable linear phase on that class. Additional local Fourier
uniformity would exclude this example. So would the absence of rational
eigenvalues, which by Section 12 suffices for (Z) by itself; the colour
process here has the eigenvalue $1/3$. This is an obstruction to arguments
using the listed identities, not to every possible statistical argument, and
it is not a counterexample to an Elliott statement about actual
multiplicative functions.

### Rigidity of the arc model for k = 5

The ternary twist does not exclude triples for $k=5$, since $1/3<2/5$.
There is a sharper obstruction to repairing it within the arc construction.

**Proposition A.** Suppose a stationary process joined with a Haar profinite
position $\Pi$ has a representation

$$
X_h=\zeta^{\lfloor5Y_h\rfloor},\qquad
Y_h=\gamma+h\beta+\phi_h\pmod1,
$$

where $\beta,\gamma$ are independent Haar variables, independent of the
entire twist sequence $(\phi_h)$ and $\Pi$. If the joint process obeys the
conditional self-similarity identity at the primes $2$ and $5$, then
$\Pr(X_0=X_1=X_2)>0$. The twist sequence need not be a function of $\Pi$,
and no closure assumption on a family of twists is needed.

*Proof.* Suppose the consecutive monochromatic probability is zero.
Conditioned on the twists and position, $(Y_h,Y_{h+1})$ is Haar on
$\mathbb T^2$. A third point with fixed second difference $\delta$ can lie
with them in one arc of length $1/5$ on a set of positive measure precisely
when $\delta$ has a representative in $(-2/5,2/5)$. Hence, almost surely,
every consecutive twist second difference has its representative

$$
\delta_h=\phi_h-2\phi_{h+1}+\phi_{h+2}\pmod1
 \quad\hbox{in }[2/5,3/5].
$$

Self-similarity at $2$ says that, conditioned on $2\mid\Pi+h$, the
step-two triple starting at $h$ is also never monochromatic. Its phase
second difference is congruent to
$\delta_h+2\delta_{h+1}+\delta_{h+2}$. This real sum lies in $[8/5,12/5]$.
The only points of that interval whose fractional part belongs to
$[2/5,3/5]$ are its endpoints. Thus all three participating $\delta$'s are
$2/5$, or all are $3/5$. Stationarity gives this at each index of the
appropriate parity. The length-three blocks overlap and cover the integers,
so all $\delta_h$ are the same, either $2/5$ or $3/5$.

The step-five second difference is therefore $25\delta_0=0\pmod1$.
Given the twists and $5\mid\Pi$, the step-five phases form an arithmetic
progression, with first term and difference independently Haar. They have
positive probability of lying in one arc: for example first term in
$[1/20,1/10]$ and difference in $[0,1/40]$ gives probability $1/800$.
This contradicts self-similarity at $5$, which would transfer zero
monochromatic probability from step one. $\square$

This proposition concerns this phase representation with independent Haar
parameters. An arbitrary stationary process with uniform pairs need not
have such a representation. General colourings of the phase circle,
dependence of the phase parameters on the twist, and other stationary
processes are not covered. Thus the proposition does not prove T(5).

## 9. Failed or insufficient mechanisms

1. **Non-pretentiousness of $f$ alone.** A power $f^j$ can still pretend
   (Case B), and the zero-sum terms, such as the exponents $(1,1,k-2)$, have
   trivial product, so no product-based cancellation applies to them.
2. **Fixed-scale sieving in Case A.** See the remark after Theorem W. Replaced
   by good scales and randomization by $E_2$.
3. **Pair theorems.** Hildebrand's bounded first pair and Tao's two-point
   theorem do not give triples. The dilation $(2n,2n+1,2n+2)$ turns a triple
   into the pair $f(n)=f(n+1)=\overline{f(2)}$ plus the fresh value $f(2n+1)$,
   whose joint law with the pair is again a zero-sum-type three-point
   statistic. Hildebrand's theorem is not used anywhere on this page.
4. **Value-pattern theorems.** Tao and Teräväinen, *Value patterns of
   multiplicative functions and related sequences* (Forum Math. Sigma 7
   (2019), e33; arXiv:1904.05096), prove positive lower density of
   $n+1\in A_1$, $n+2\in A_2$, $n+3\in A_3$ for weakly stable sets uniformly
   distributed in short intervals with $\delta_1+\delta_2+\delta_3>1$, treat
   the critical sum $1$, and deduce that $\omega(n)\bmod3$ takes all $27$
   patterns of length three. For a general $f$, multiplication by a prime
   permutes its level sets
   by the value $f(p)$; the common companion-set hypothesis in that paper
   has not been established here. It does hold for the constant-on-primes
   example. Even there, for $k\ge5$ the densities sum to $3/k<1$. The authors
   state that below the critical sum the sets could
   behave like local Bohr sets and that excluding this needs local Fourier
   uniformity, an open problem. Section 8 is a version of that obstruction
   adapted to the full set of averaged constraints.
5. **Isotypy plus recurrence.** Furstenberg's multiple recurrence gives
   monochromatic three-term progressions on average over all differences, but
   isotypy transfers only differences prime to the period, and the model shows
   that restriction can defeat recurrence. Exact self-similarity transfers
   every difference $d$, but only for starting points divisible by $d$, and
   for $k\ge7$ the digit-twisted process defeats that as well.
6. **Spectral arguments.** Pair uniformity makes every $X_0^a$ with
   $a\not\equiv0$ have Lebesgue spectral type, so its projection to the
   rational eigenfunctions of every ergodic component vanishes. The model's
   components are rotations of $\mathbb Z/5\times\mathbb T$ whose irrational
   eigenvalues vary with $\beta$ and do not glue to global eigenfunctions, and
   the colours on the five rational cosets are translated arcs. Rational
   spectrum alone does not decide (Z).
7. **Rational triples and denominators.** Extend $f$ to positive rationals
   by $f(a/b)=f(a)/f(b)$. A monochromatic progression
   $a,a+d,a+2d$ with $f(a)=f(d)$ gives a triple of ones at the rational
   inputs $a/d,a/d+1,a/d+2$. It gives an integer triple only if $d\mid a$.
   Clearing denominators restores step $d$, not step one. For the even-order
   counterexample in Section 1, $1/3,4/3,7/3$ all have value one although
   no three consecutive integers do. This does not refute an odd-order
   denominator-removal lemma, but such a lemma is missing; rational
   recurrence by itself is insufficient.
8. **Repeated squaring at a kernel value.** If $a>1$ and $f(a)=1$, put
   $n_j=a^{2^j}$, $A_j=f(n_j-1)$, and $B_j=f(n_j+1)$. Factoring
   $n_j^2-1$ gives $A_{j+1}=A_jB_j$. A triple centred at $n_j$ needs
   $A_j=B_j=1$. The recurrence alone does not force this: the abstract
   values $A_j=\zeta^j$, $B_j=\zeta$ obey it and avoid that pair for every
   $k>1$. This is not a construction of a completely multiplicative
   counterexample. It shows that a power-centre argument needs additional
   relations between the neighbouring factorizations.
9. **Finite computation.** A Lehmer–Mills style case analysis settles one $k$
   at a time. For $k=5$ a pending author report, not verified here, claims
   $\Lambda(5,3)\ge37{,}329{,}226$, so an enumeration that searches every
   triple below a universal bound
   would need an endpoint beyond that range if the report is correct.
   This does not imply that its prime support must extend beyond that
   range. A separate finite calculation for one $k$ does not settle all
   odd $k$. There cannot be a bound independent of $k$: for any fixed
   $M$, choose an odd $k>\log_2(M+2)$ and set $f(p)=\zeta$ for every prime.
   Then $f(n)=\zeta^{\Omega(n)}\ne1$ for $2\le n\le M+2$, so there is no
   triple starting at or below $M$.
10. **Spectral recurrence and removal of the core.** Lemma E and Proposition
    D in Section 12 transfer recurrence when the relevant position condition
    is independent of the colours. The spectral assertions (SP) and (QSP)
    are unproved; uniform one-point means on progressions do not establish
    independence for a three-point event or for an entire process.
    Lemma J and Proposition V do compose the route with a pretentious
    multiplier, including every squarefree odd order conditionally on (SP).
    But a universal Dirichlet-root split is false: the order-nine function
    over a cubic character modulo seven supplies an arithmetic example.
    Proposition QD bypasses that algebraic failure with a pointwise quotient
    invariant under multiplication by $k$th powers. Its missing input is
    (QSP), a spectral assertion about this actual quotient. Proving it, or
    enough independence to transfer recurrence and combine it with the core,
    would finish the route. The root failure does not obstruct (AC).

## 10. Exact remaining obligations and a discriminating test

The unconditional route covers the entire odd-order target as follows.
The trivial case $k=1$ and the accepted case $k=3$ are settled. For each odd
$k\ge5$, let the weak-pretence subgroup be $H(f)=d\mathbb Z/k\mathbb Z$.
If $d=1$, Theorem W supplies triples. Otherwise the missing input is

$$
\limsup_{X\to\infty}\mathbb E^{\log}_{n\le X}
 \mathbf1[f(n)=f(n+1)=f(n+2)\in\mu_d]>0. \tag{R}
$$

The precise quantifiers are: for every odd $k\ge5$, every divisor $d>1$ of
$k$, and every completely multiplicative $f:\mathbb N\to\mu_k$ whose
weak-pretence subgroup is exactly $d\mathbb Z/k\mathbb Z$, (R) holds.
Sections 5 and 6 then give positive upper logarithmic density of $T_f$;
Section 1 supplies a uniform finite bound for each fixed $k$ and the bridge
to $\Lambda(k,3)$. The bound need not be effective or uniform in $k$.
(R) is a sufficient density statement, stronger than the requested existence
statement. Its truth is unknown here, not refuted by a stochastic model.

For prime $k$, Section 12 gives a qualitative sufficient condition for (R)
with $d=k$: for every completely multiplicative $f:\mathbb N\to\mu_k$ in Case
C, at least one logarithmic Furstenberg system of $f$ has no rational
eigenvalue other than $0$. Weaker still, it suffices that for one such
system, one joint limit with the position and one step $r$ at which a
monochromatic three-term progression has positive measure, the colour
sequence is independent of the position modulo $r$. Section 12 also gives
the precise hypothesis (SP) for functions with trivial bounded-distance
subgroup. Splitting off a pretentious multiplier extends that conditional
route to every squarefree odd $k$, and to other functions whose core
character has a suitable Dirichlet root. The root condition can fail for
repeated-prime orders. Proposition QD instead uses a specified pointwise
quotient of $f$ by its bounded-distance core: the precise spectral hypothesis
(QSP) for this quotient suffices for every odd $k$. These spectral hypotheses
remain unproved. They yield positive triple mass, not the cancellation
assertion (AC) below.

A more analytic test that could complete the route in one argument is the
following **aggregate cofactor estimate**. Let
$H_B(f)=d_B\mathbb Z/k\mathbb Z$ be the bounded-distance subgroup from
Section 7, and define

$$
R_f(n)=\sum_{\substack{a,b,c\bmod k\\
                  (a,b,c)\notin H_B(f)^3}}
 f(n)^a f(n+1)^b f(n+2)^c.
$$

Can one prove, for every odd $k$ and every such $f$, that there is a sequence
$X_j\to\infty$ with

$$
\mathbb E^{\log}_{n\le X_j} R_f(n)\longrightarrow0? \tag{AC}
$$

This asks for one aggregate estimate along some scales, not separate
cancellation of every correlation at every scale. Its implication is exact:

$$
\mathbb E^{\log}_{n\le X}\mathbf1_{T_f}(n)
 =d_B^{-3}\mathbb E^{\log}_{n\le X}
   \mathbf1[f^{d_B}(n)=f^{d_B}(n+1)=f^{d_B}(n+2)=1]
  +k^{-3}\mathbb E^{\log}_{n\le X}R_f(n).
$$

The first term has a positive lower limit by the bounded-distance part of
Theorem W. Thus (AC) would settle every odd $k$, including composite orders.
The full three-point Elliott conjecture implies (AC), but this page does
not prove that the aggregate estimate is strictly weaker.

A natural place to attack (AC) is the passage from the finite-prime vector
of Lemma S to the remaining cofactors of the three forms. Lemma S controls
*only* the primes up to $x^\varepsilon$. In Theorem W, sparse exceptional
primes and the good windows make the omitted factors harmless. For a function
outside the bounded-distance core, those factors cannot be discarded by that
argument, and an extension must bound their **joint**, character-weighted
contribution after the small prime conditions are imposed. Section 11 gives
the exact aggregate conditional expression and its summed error. Independence
(CI) would suffice, but (AC) does not require
independence from the full label vector, or separate cancellation at every
scale. The digit-twisted process shows that the label law and the listed
stationary identities alone do not give the estimate. It supplies no
arithmetic cofactor law, so this obstruction does not close the cofactor
route. Marginal equidistribution, a pair theorem, or independent reference
cofactors cannot replace the missing joint estimate.

There is also a concrete test of the model obstruction for $k=5$, relevant
to judging the statistical route rather than to replacing the all-odd target.
Proposition A rules out the independent linear-phase model with arc colours
using only dilations by $2$ and $5$. The next model question is whether the
same conclusion holds for a general measurable rotation-equivariant
colouring of the phase circle. The exact ternary-twist version asks whether a
measurable set $A\subset\mathbb T$ whose five translates by $j/5$ partition
$\mathbb T$ up to null sets can have zero measure of triples in $A^3$ with
$a-2b+c=\pm1/3\pmod1$, for both signs. The measure here is Haar in
$(a,b)$, with $c=\pm1/3-a+2b$; both nonnegative masses must vanish. A
positive answer to existence of such a set gives another
obstruction; a uniform positive lower bound excludes that model only.
Neither outcome by itself settles arbitrary multiplicative functions.

For clarity, the log-limit processes arising from Case C do obey the
identities used in the model tests. Choose a common subsequence along which
all cylinder averages of $((f(n+h))_h,n\in\widehat{\mathbb Z})$ converge.
Translation changes normalized logarithmic averages by $o(1)$, residue
classes have their usual uniform densities, and the two-point theorem with
Lemma U gives uniform pairs. Theorem 1.5 also gives colour-rotation
invariance jointly with the position. Indeed, to restrict a correlation to
$n\equiv r\pmod q$, insert
$\mathbf1_{n\equiv r\,(q)}=\varphi(q)^{-1}\sum_{\chi\bmod q}\chi(n+1-r)$.
If its total colour exponent is $e\not\equiv0\pmod k$, the unshifted
product becomes $f^e\chi$, which still cannot weakly pretend to a character
in Case C. Apply Theorem 1.5 to the extra shifted character factor; the
finitely many nonpositive inputs do not affect the limit. Fourier expansion
of colour cylinders and residue classes proves the claimed joint invariance.
On $p\mid n$, put $n=pm$: the weights satisfy $1/n=1/(pm)$,
the cutoff changes from $X$ to $X/p$ by an $o(1)$ normalized error, and
$f(p(m+h))=f(p)f(m+h)$. This gives the conditional law of
$((f(p)X_h)_h,\Pi)$, including the divided profinite position; joint
colour-rotation invariance removes the common factor $f(p)$. Thus the
conditional identity tested in Section 8 does hold. These facts justify
testing those identities; they do not assert that every process satisfying
them is realizable by a completely multiplicative function.

## 11. The cofactor interface and tests of further mechanisms

This section records the conditional expansion proposed in Section 10 and
tests of further mechanisms. The arguments are author-recorded and unreviewed.
The model obstructions concern only their listed inputs; the finite-sums
construction is an actual multiplicative function but not a counterexample
to T(k). Neither (AC) nor the full target is proved or refuted.

### The conditional expansion and its aggregate error

Fix $q$ to be the modulus of a character to which $f^{d_B}$ pretends at
bounded distance. Choose $P_0\ge5$, exceeding every prime divisor of $q$,
sufficiently large for the bounded-distance argument of Theorem W, and
keep $q,P_0,Q,B$ fixed throughout the limits in $\varepsilon$ and $x$ below.
Use the population and labels of Lemma S: the selected $m\le x$ satisfy
$m\equiv1\pmod q$ and $(m,Q)=1$, the forms are $L_1=Qm-1$, $L_2=m$,
$L_3=Qm+1$, and $V(m)=(V_p(m))_{P_0<p\le y}$ with $y=x^\varepsilon$.
Since $f(Q)=1$, the triple $(f(L_1),f(L_2),f(L_3))$ is the value triple of
$f$ at $n=Qm-1$,
$n+1$, $n+2$. For $e\in(\mathbb Z/k\mathbb Z)^3$ put
$C_e(x)=\mathbb E_m\prod_if(L_i(m))^{e_i}$. For a labelled vector $v$ let
$D_i(v)$ be the product of the primes with label $i$, and put

$$
S_e(v)=\prod_if(D_i(v))^{e_i},\qquad
\Gamma_e(v)=\mathbb E\Big[\prod_if(L_i)^{e_i}\,\Big|\,V=v\Big],\qquad
M_e(v)=\mathbb E\Big[\prod_if\big(L_i/D_i(v)\big)^{e_i}\,\Big|\,V=v\Big],
$$

the conditional expectations being over the selected $m\le x$, and $0$ when no
selected $m$ has $V(m)=v$. Complete multiplicativity gives exactly

$$
\Gamma_e(v)=S_e(v)M_e(v),\qquad C_e(x)=\sum_v\Pr(V=v)\,\Gamma_e(v),
$$

and Lemma S gives $C_e(x)=\sum_vP^*(v)\Gamma_e(v)+O(\eta)$, where $P^*$ is the
independent reference law and $\eta$ is twice the total-variation bound of
Lemma S.

**The aggregate interface.** Write $d=d_B$, $h=|H_B(f)|=k/d$,
$\mathcal E=(\mathbb Z/k\mathbb Z)^3\setminus H_B(f)^3$ and
$J=|\mathcal E|=k^3-h^3$. Define

$$
\Theta_f(x,\varepsilon)
 =\sum_vP^*(v)\sum_{e\in\mathcal E}S_e(v)M_e(v).
$$

The actual conditional expectations $M_e$ must be used in this expression.
Writing $\eta_0(\varepsilon)=2C\varepsilon+
2r(1/(4\varepsilon))$, the triangle inequality and Lemma S give

$$
\left|\sum_{e\in\mathcal E} C_e(x)
             -\Theta_f(x,\varepsilon)\right|
 \le J\eta_0(\varepsilon)+o_{Q,B,k,\varepsilon}(1). \tag{CE}
$$

Indeed each $|\Gamma_e(v)|\le1$, so the sum of the errors over all $J$
characters is at most $J$ times the bound for one. Conjugate exponents occur
in pairs, so both aggregate quantities are real. No independence of the
cofactors is used in (CE).

In particular, the sufficient condition

$$
\liminf_{\varepsilon\downarrow0}\ \liminf_{x\to\infty}
 |\Theta_f(x,\varepsilon)|=0 \tag{CF}
$$

gives one sequence $x_j\to\infty$ on which
$\sum_{e\in\mathcal E}C_e(x_j)\to0$: first choose fixed
$\varepsilon_j\downarrow0$ making the inner lower limits tend to zero,
then choose $x_j$ successively large enough for that estimate and the error
in (CE). This is the aggregate cofactor question on the selected population,
not a proof of it and not (AC) for all starting integers. It would nevertheless
finish T(k) directly. With the fixed choices of $q$ and $P_0$ above, the
bounded-distance proof of Theorem W applies to $f^d$ with this $k$th-power
choice of $Q$ and gives

$$
c_*:=\liminf_{x\to\infty}\mathbb E_m
 \mathbf1[f^d(L_1)=f^d(L_2)=f^d(L_3)=1]>0,
$$

on these same selected $m$. Fourier inversion there is exactly

$$
\mathbb E_m\mathbf1_{T_f}(Qm-1)
 =d^{-3}\mathbb E_m
   \mathbf1[f^d(L_1)=f^d(L_2)=f^d(L_3)=1]
  +k^{-3}\sum_{e\in\mathcal E}C_e(x).
$$

Thus (CF) would give a positive lower bound along its common sequence. Even
a one-sided estimate suffices: for one fixed small $\varepsilon$, it is
enough that $\limsup_x\Theta_f(x,\varepsilon)$ exceed
$-k^3d^{-3}c_*+J\eta_0(\varepsilon)$. The strict inequality leaves room for
the vanishing error and for the lower-limit approximation to the core.
Neither this one-sided bound nor (CF) is established here.

**A stronger sufficient estimate.** Fix $e$ such that some $f^{e_j}$ is at
unbounded distance from $1$; every $e\notin H_B(f)^3$ qualifies. Suppose the
cofactor term is asymptotically independent of the labels:

$$
\sum_vP^*(v)\,\big|M_e(v)-\mu_e(x)\big|\longrightarrow0
\quad(x\to\infty)\ \hbox{ for some }|\mu_e(x)|\le1. \tag{CI}
$$

Since $P^*$ is a product law,
$\sum_vP^*(v)S_e(v)=\prod_{P_0<p\le y}\big(1+\sum_i(f(p)^{e_i}-1)/p\big)$,
whose modulus is at most
$\exp\big(-\sum_{P_0<p\le y}(1-\operatorname{Re}f(p)^{e_j})/p+O(1)\big)$ by
$|1+z|\le\exp(\operatorname{Re}z+|z|^2/2)$; this tends to $0$ as
$y\to\infty$. For each fixed $\varepsilon$ satisfying (CI), this gives
$\limsup_x|C_e(x)|\le\eta_0(\varepsilon)$. If (CI) holds for every
sufficiently small $\varepsilon$, letting $\varepsilon\downarrow0$ gives
$C_e(x)\to0$. For all $e\notin H_B(f)^3$ together, this is the analogue of
(AC) on the selected population. When $q$ is the modulus of a character to
which $f^{d_B}$ pretends at bounded distance, the core term on the same
population has a positive lower limit by the proof of Theorem W, and $T_f$
would be nonempty. This proves sufficiency of (CI), not its necessity. The
weighted aggregate in (CF), or its one-sided positivity bound, is the actual
remaining interface; neither requires $M_e$ to approach a constant in
absolute mean.

Unwinding the definitions shows what (CI) asks. Given $V=v$, $m$ runs over
the residue classes fixed by the labels, minus the classes of the unlabelled
primes, and $L_i/D_i(v)$ are linear forms in the new variable. So $M_e(v)$ is
again a correlation of $f$ at three linear forms, with the same exponent
vector $e$, and it is zero-sum whenever $e$ is. The expansion relocates the
three-point problem; it does not reduce it. The next proposition shows that
the data the conditioning uses cannot decide (CI).

**Proposition O.** Let $k\ge7$ be odd, and take the digit-twisted process of
Section 8 with its Haar position $\Pi$. Condition on the population event
that $\Pi+1=Qm'$ with $m'\equiv1\pmod q$ and $m'$ a unit at every prime
$p\le P_0$. Put $V_p=i$ when $p\mid\Pi+i-1$, for $P_0<p\le y$ and
$i=1,2,3$. Prescribe any values $f(p)\in\mu_k$ for $P_0<p\le y$, define
$S_e$ and $\Gamma_e$ as above with $X_0,X_1,X_2$ in place of
$f(L_1),f(L_2),f(L_3)$, and put $M_e=\overline{S_e}\,\Gamma_e$. Then:

1. $V$ has exactly the law $P^*$;
2. $\Gamma_e(v)=c_e$ for every $v$, where
   $c_e=\mathbb E[X_0^{e_1}X_1^{e_2}X_2^{e_3}]$ under the population event;
3. $M_e(v)=c_e\overline{S_e(v)}$, so
   $\sum_vP^*(v)S_e(v)M_e(v)=c_e$ exactly;
4. $\sum_{e\ne0}c_e=-1$.

The process also has every property listed in Section 8: rotation
invariance, uniform pairs jointly with the position, isotypy of nonzero
dilations, and the conditional self-similarity at every prime. The last holds
with any prescribed values $f(p)$, because multiplying every colour by
$f(p)$ amounts to translating the independent uniform variable $\gamma$.

*Proof.* Under Haar measure the components of $\Pi$ at distinct primes are
independent and uniform. The population event is a product of conditions on
the components at the primes $p\le P_0$, and $V$ is a function of the
components at the primes in $(P_0,y]$, each label having probability $1/p$.
This gives 1. Given $(\gamma,\beta,\sigma)$, which are independent of $\Pi$,
the window $X_0,X_1,X_2$ is a function of the $3$-adic component of $\Pi$.
Since $3\le P_0$, that component is independent of $V$ under the population
event, which gives 2; 3 follows by definition. By (D1) the event
$X_0=X_1=X_2=1$ is empty at every position, so Fourier inversion gives
$k^{-3}\sum_ec_e=0$, and $c_0=1$. $\square$

Thus the exact label law and the identities of Section 8 hold for this
process, with any prescribed small-prime values. The formal variables $M_e$
also satisfy $\Gamma_e=S_eM_e$ by definition. They have not been realized as
conditional expectations of one arithmetic function at the cofactor inputs;
the proposition supplies none of those additional multiplicative relations.
Its cofactor term is the conjugate small-prime
character times a constant, and the aggregate of all nonzero terms is $-1$,
whereas (AC) asks for $0$ when $H_B$ is trivial. (CI) fails whenever
$c_e\ne0$ and some prescribed $f^{e_j}$ is at unbounded distance from $1$ as
$y$ grows: the computation above would then make
$\sum_vP^*(v)S_e(v)M_e(v)$ tend to $0$, while it equals $c_e$. No argument
whose inputs are the label law of Lemma S and the identities of Section 8 can
prove (CI) or (AC) for odd $k\ge7$. For $k=5$ the twisted Bohr process gives
the same conclusion for arguments that do not use the self-similarity at the
prime $5$. That process is taken independent of $\Pi$, so 1 to 4 hold with
$c_e$ its own correlations; its dilation invariance gives the conditional
self-similarity at every prime other than $5$; and the prime $5$ carries no
label. This does not refute (AC) for any completely multiplicative function.

### Polynomial families of consecutive values are one-dimensional

A different way to escape the identities of Section 8 is to use non-linear
multiplicative identities, which relate the value triple at a large integer
to values near a much smaller one. The relation $t(6t+7)+1=(t+1)(6t+1)$,
$t(6t+7)+2=(2t+1)(3t+2)$ is an example: it puts a triple of ones at
$t(6t+7)$ whenever the three pair products $f(t)f(6t+7)$, $f(t+1)f(6t+1)$
and $f(2t+1)f(3t+2)$ equal $1$. The next lemma shows that every such family
is a fixed finite window around one integer.

**Lemma P.** Let $d\ge1$ and let $A,B\in\mathbb Q[t_1,\dots,t_d]$ each be a
nonzero constant times a product of nonconstant affine-linear factors, with
$B-A=c$ a nonzero constant. Then the linear parts of all these factors are
proportional, so $A$ and $B$ are polynomials in a single affine form.

*Proof.* If $A$ is constant, so is $B$, and the conclusion is immediate.
For $d=1$ there is also nothing to prove. Let $d\ge2$ and let $L$ be a
factor of $A$. On the hyperplane $L=0$ the polynomial $B$ equals the nonzero
constant $c$. The polynomial ring of the hyperplane is a domain, so every
factor of $B$ restricts to a constant there, and an affine function is
constant on $\{L=0\}$ only if its linear part is proportional to that of
$L$. So every factor of $B$ is parallel to every factor of $A$. Since $B$ has
a factor, all factors of $A$ are parallel to it, and so are all factors of
$B$. $\square$

Applied to $N$ and $N+1$, the lemma shows that a family of consecutive
triples $N,N+1,N+2$ given by products of affine forms, in any number of
parameters, factors through one affine form $\ell$. After the substitution
$n=M\ell$, with $M$ clearing denominators, each $f(N+j)$ is a fixed constant
times a product of values $f(n+h)$ for fixed integer shifts $h$, on a fixed
residue class of $n$. Every such family is therefore a local pattern of the
log-limit process with its position, subject to the constraints of Section
8. In particular no such family expresses $f(N),f(N+1),f(N+2)$ through three
pairwise non-proportional affine forms in two parameters, an average to which
exponential-sum bounds over the whole range, rather than local uniformity,
would apply.

In degree two the lemma gives all families explicitly. If
$N_j=A(t+a_j)(t+b_j)$ with $N_j=N_0+j$, then $a_j+b_j=s$ does not depend on
$j$, and with $c=t+s/2$ and $u_j=(a_j-b_j)/2$,

$$
N_j=A(c^2-u_j^2),\qquad u_j^2=u_0^2-j/A .
$$

So the family is three pairs placed symmetrically about one centre, with the
squares of the half-gaps in arithmetic progression. The example above is
$A=6$, $s=7/6$, $u_j=7/12,5/12,1/12$.

In general, after Lemma P and the substitution $n=M\ell$, a family with $r$
factors per value is given by three multisets $H_0,H_1,H_2$ of $r$ integers
such that the monic polynomials $P_j(n)=\prod_{h\in H_j}(n+h)$ satisfy
$P_j=P_0+j\Delta$ for an integer $\Delta\ne0$. For the following identity
with $f$, take $\Delta>0$ and positive arguments $n+h$. On the residue
classes where $\Delta\mid P_0(n)$, the values $N+j=P_j(n)/\Delta$ are
consecutive integers
and $f(N+j)=\overline{f(\Delta)}\prod_{h\in H_j}f(n+h)$. A function with no
triple of ones therefore never has all three products
$\prod_{h\in H_j}f(n+h)$ equal to $f(\Delta)$ on those classes, once $N\ge1$.
The degree-two families have $H_j=\{x-w_j,x+w_j\}$ for a centre $x$ and
half-gaps $w_j$ whose squares are in arithmetic progression.

**Proposition Q.** Let $r\in\{2,3\}$ and let $k\ge3r$ be odd. Let
$H_0,H_1,H_2$ be multisets of $r$ integers with
$\prod_{h\in H_j}(n+h)=P_0(n)+j\Delta$ identically, $\Delta\ne0$, and put
$z_j=\prod_{h\in H_j}(\Pi+h)$. In the digit-twisted process, the event that
$\Delta$ divides $z_0$ and the three products $\prod_{h\in H_j}X_h$ are equal
has probability zero.

So for odd $k\ge7$ the digit-twisted process satisfies the constraint that
every family with two factors per value imposes on a function with no triple
of ones; for odd $k\ge9$ it also satisfies every such three-factor constraint.

*Proof.* Write $\psi(y)\in\{\pm1\}$ for the last nonzero ternary digit of the
$3$-adic component of $y$, read as $\pm1$. It is completely multiplicative,
and the twist of Section 8 is $\phi=(1-\psi)/6$. Let $c_j$ be the number of
$h\in H_j$ with $\psi(\Pi+h)=-1$. The sum $\sum_{h\in H_j}h$ is the
coefficient of $n^{r-1}$, so it does not depend on $j$, and the sum $S_j$ of
the $Y_h$ over $h\in H_j$ satisfies
$S_j-S_{j'}\equiv\sigma(c_j-c_{j'})/3\pmod1$. For
$a_1,\dots,a_r\in[0,1)$, $\sum_i\lfloor ka_i\rfloor$ is congruent modulo $k$
to $\lfloor k\{\sum_ia_i\}\rfloor$ minus an integer in $[0,r-1]$. Hence if
$c_j\not\equiv c_{j'}\pmod3$, the colour exponents of the two products differ
modulo $k$ by an integer in $(k\theta-r,k\theta+r)$ for some
$\theta\in\{\pm1/3,\pm2/3\}$. That interval contains no multiple of $k$ when
$k\ge3r$, and the products differ. It remains to show that, almost surely
when $\Delta\mid z_0$, the $c_j$ are not all congruent modulo $3$.

Since $z_j=z_0+j\Delta$ and $\Delta\mid z_0$, the numbers $z_j/\Delta$ are
three consecutive elements of $\widehat{\mathbb Z}$; the two prime to $3$
have $\psi$-values $+1$ and $-1$. So
$(-1)^{c_j}=\psi(z_j)=\psi(\Delta)\psi(z_j/\Delta)$ takes both signs, almost
surely, and the $c_j$ do not all have the same parity. For $r=2$,
$c_j\in\{0,1,2\}$, and two such values of different parity differ by $1$.

For $r=3$, first $3\mid\Delta$. Otherwise reduction modulo $3$ gives cubics
$g+c$ over $\mathbb F_3$ for all three constants $c$ with a fixed $g$, each
splitting completely. Listing the multisets of three residues shows that this
forces $g=x^3$ up to an additive constant, so each $H_j$ lies in one residue
class, the three classes
distinct. Writing $h=\rho+3a$ with $\rho\in\{0,1,2\}$, a group with sum $s$
has sum of squares congruent to $2\rho s-3\rho^2$ modulo $9$. The groups have
equal sums and equal sums of squares, which for $\rho=0,1,2$ needs
$2s\equiv3$ and $4s\equiv3\pmod9$, and these are incompatible. So the $H_j$
have the same residues modulo $3$, and the positions prime to $3$ contribute
the same count to every $c_j$. Let $\mu$ be the number of $h\in H_j$ with
$3\mid\Pi+h$, the same for each $j$; $\mu\ge1$ when $\Delta\mid z_0$, because
$3\mid\Delta$. If $\mu\le2$, the contributions of the multiples of $3$ lie in
$\{0,1,2\}$ and do not all have the same parity, so two of them differ by
$1$. If $\mu=3$, all shifts are congruent modulo $3$. After translating the
base position, which preserves the law of the process with its position, all
shifts and $\Pi$ are multiples of $3$. Since $\psi(3y)=\psi(y)$, the counts
$c_j$ are those of the family $H_j/3$ at $\Pi/3$, which is Haar distributed
given $3\mid\Pi$, and whose difference is $\Delta/27$. As $|\Delta|$ cannot
decrease forever, this case reduces to $\mu\le2$. $\square$

For $k=5$ the interval in the proof can contain $0$, and for $r=3$ with $k=7$
the floors leave too much slack. Whether some family with at least four
factors per value, or with three when $k=7$, receives positive probability in
the digit-twisted process is open here. A positive answer would show that
this process is not the log-limit of any function without triples. It would
not by itself prove T(k).

### Shifted special sets need more than first moments

Hildebrand's proof of the pair theorem uses special sets: finite sets in
which the difference of any two elements divides both. Two elements of a
special set, divided by their difference, are consecutive integers. Using
Ramsey's theorem, he makes the colours of all elements and of all pairwise
greatest common divisors constant. He then moves every element along one
progression, $n_i\mapsto n_i+tP$, which keeps every difference and multiplies
$n_i$ by $1+tP/n_i$. A first-moment count over $t$, which needs only the
distribution of $f$ in residue classes, finds a $t$ at which two elements
receive the required colour together. All the shifted elements lie in a
window of fixed length around $tP$, so this too is a local pattern.

For triples the relevant configurations are three elements
$a<a+d<a+2d$ with $d\mid a$, which give the triple $a/d,a/d+1,a/d+2$. Every
three-term progression in a special set is of this form.

**Lemma H.** Let $g$ be the completely multiplicative function with $g(3)=1$
and $g(p)=(p/3)$ for $p\ne3$, the even-order example of Section 1. For every
finite set $S$ of positive integers, neither class $S\cap\{g=1\}$ nor
$S\cap\{g=-1\}$ contains $a<a+d<a+2d$ with $d\mid a$. One of the two classes
has at least $|S|/2$ elements.

*Proof.* Such a configuration in the class $\epsilon$ gives
$g(a/d)=g(a/d+1)=g(a/d+2)=\epsilon g(d)$. Of three consecutive integers, the
two prime to $3$ are congruent to $1$ and $2$ modulo $3$, with $g$-values $1$
and $-1$. $\square$

So the set of good indices produced at the best $t$ must exceed half of $S$
before a configuration is forced, while a first-moment count gives only about
a fraction $1/k\le1/3$. The scheme needs joint information on three shifted
elements. Pair statistics are not enough either. A configuration is fixed by
two of its elements up to three choices, so a good pair cannot be completed
in many ways. In the digit-twisted process read at the shifted elements, with
the base position divisible by $P$, the level sets have uniform pairs and, by
(D1) and (D2), contain no configuration.

### Exact finite-sums pairs do not force reflection symmetry

Dietzel's Theorem 4, *On a theorem of Hildebrand*, strengthens the pair
theorem: if $A$ is a finite-index subgroup of $\mathbb Q^+$, then
$\{n\in\mathbb N:n,n+1\in A\}$ contains all nonempty finite sums of some
infinite sequence. Its proof applies Hindman's finite-unions theorem to a
sequence whose earlier block sums divide later terms. Dividing the resulting
monochromatic finite-sums sequence by its first term gives
$\operatorname{FS}(1,a_2,a_3,\ldots)\subset A$.

This suggests a direct attack on T(k). After a further Ramsey refinement,
the values on differences of two block terms can be made constant. For
terms $b_i<b_j$ with $b_i\mid b_j$ and
$f(b_i)=f(b_j)=f(b_i+b_j)=c$, the integer $n=b_j/b_i$ satisfies
$f(n)=f(n+1)=1$, while $f(n-1)=f(b_j-b_i)/c$. A proof that one can select
such a refinement with this last value of order at most two would finish
the odd-order target. The following construction rules out imposing that
constraint on every homogeneous sequence, even for a function with bounded
distance from $1$. A variant below also lies in Case C.

**Proposition F.** Let $k\ge3$ be odd and let $\rho\in\mu_k\setminus\{1\}$.
There exist a completely multiplicative $f:\mathbb N\to\mu_k$ and an
increasing sequence $b_1=1,b_2,\ldots$ such that:

- $f$ is at bounded pretentious distance from $1$;
- every earlier nonempty finite sum of the $b_i$ divides every later term;
- $f(\sum_{i\in I}b_i)=1$ for every finite nonempty $I$;
- $f(b_j-b_i)=\rho$ for every $i<j$.

In particular every quotient $n=b_j/b_i$ has value pattern
$(f(n-1),f(n),f(n+1))=(\rho,1,1)$. This is not a counterexample to T(k):
the construction has $f(1)=f(2)=f(3)=1$.

*Proof.* Construct the terms and distinct primes $p_{ij}$, $i<j$,
recursively. At stage $j\ge2$, let $B_j=\sum_{i<j}b_i$ and let $L_j$ be
the least common multiple of its nonempty subset sums. Choose new primes

$$
p_{ij}>\max(3,2B_j,2^{i+j})\qquad(1\le i<j).
$$

Choose $b_j>2B_j$ subject to $L_j\mid b_j$ and

$$
b_j\equiv b_i+p_{ij}\pmod {p_{ij}^2}\qquad(i<j).
$$

For every previously chosen prime $q$, also prescribe $v_q(b_j)$ to be a
multiple of $k$ strictly greater than both $v_q(L_j)$ and all previous
$v_q(b_i)$. These conditions are compatible: a new prime exceeds every
subset sum entering $L_j$, and at an old prime the prescribed valuation
exceeds the divisibility requirement. The Chinese remainder theorem gives
arbitrarily large positive choices of $b_j$.

Set $f(p_{ij})=\rho$ and $f(p)=1$ at every other prime. The support has
finite reciprocal sum, since $\sum_{i<j}2^{-i-j}<\infty$, so
$\mathbb D(f,1;\infty)^2=(1-\operatorname{Re}\rho)\sum_{i<j}1/p_{ij}<\infty$.
All selected primes exceed $3$.

Fix $q=p_{uv}$. The terms before $b_v$ are positive and their sum is
$B_v<q/2$, while $b_v\equiv b_u\pmod q$. Any nonempty subset of the first
$v$ terms therefore has residue represented by an integer in $(0,2B_v]$,
which is below $q$. Every later term is divisible by $q$, with strictly
increasing valuations that are multiples of $k$. Consequently a nonempty
finite sum has $q$-valuation zero if it uses one of the first $v$ terms;
otherwise its valuation is that of its earliest term, a multiple of $k$.
This holds for every selected prime, proving the assertion about finite sums.

For $b_j-b_i$, the prime $p_{ij}$ has valuation exactly one. A selected prime
$p_{uv}$ with $v>j$ exceeds the difference. If $v=j$ and $u\ne i$, its
residue is $b_u-b_i\ne0\pmod {p_{uv}}$. If $i\le v<j$, the term $b_j$ is
divisible by $p_{uv}$ and $b_i$ is not. Finally, if $v<i<j$, the difference
has the smaller of two distinct valuations, both multiples of $k$. Thus every
selected prime other than $p_{ij}$ contributes a multiple of $k$, and
$f(b_j-b_i)=\rho$. The divisibility assertion follows from $L_j\mid b_j$.
Dividing $b_j-b_i,b_j,b_j+b_i$ by $b_i$, whose value is $1$, gives the stated
pattern. $\square$

**Variant in Case C.** The last three assertions of Proposition F can instead
be realized with $H(f)=H_B(f)=\{0\}$, still with $f(2)=f(3)=1$. After choosing
$b_j$, insert an additional finite block of primes $U_j<p\le Y_j$, where
$U_j>\max(3,2\sum_{i\le j}b_i)$ exceeds all previously selected primes and
endpoints, and choose $Y_j$ with
$\log\log U_j\le j^{-1}\log\log Y_j$. Give every prime
in this block the value of the fixed primitive root $\zeta$. All later
designated primes are chosen above $Y_j$, and all later terms have strictly
increasing valuations divisible by $k$ at these additional primes as well.
This adds only finitely many compatible conditions at each stage.

At an additional prime, a finite sum using one of the terms up to $b_j$ is
nonzero modulo that prime; a sum using only later terms has the valuation of
its earliest term, a multiple of $k$. Differences have valuation zero or a
multiple of $k$ by the same argument. Thus the finite-sums and difference
identities are unchanged. For any fixed Dirichlet character $\chi$ and any
$a\not\equiv0\pmod k$, the prime number theorem in its residue classes gives

$$
\begin{aligned}
\mathbb D(f^a,\chi;Y_j)^2
&\ge\sum_{U_j<p\le Y_j}
       \frac{1-\operatorname{Re}(\zeta^a\overline{\chi(p)})}{p}\\
&=\bigl(1-\mathbf1[\chi\text{ principal}]
                    \operatorname{Re}\zeta^a\bigr)\log\log Y_j
  +O_\chi(\log\log U_j+1).
\end{aligned}
$$

The leading coefficient is positive. Hence $f^a$ weakly pretends to no
character; bounded-distance pretence is excluded as well. This proves the
variant. It still has the triple starting at $1$.

The failed step is the proposed order-two restriction on the predecessor
colour of an arbitrary homogeneous refinement: Proposition F disproves it
within the arithmetic class itself. A successful selection argument would
have to produce a favorable refinement using further information about $f$;
neither the finite-sums theorem nor complete multiplicativity on these
displayed inputs supplies that selection. The construction deliberately
chooses its quotients, and gives no way to control every prescribed integer
start, so it cannot be extended to a target counterexample by the argument
given here. In particular it does not refute a future lemma that uses the
global hypothesis $T_f=\varnothing$, which neither constructed function
satisfies.

### The constant-on-primes case

Let $f_1(p)=\zeta$ for every prime, so $f_1(n)=\zeta^{\Omega(n)}$. For every
$j\not\equiv0$ and every character $\chi$,
$\mathbb D(f_1^j,\chi;x)^2\gg_{k,\chi}\log\log x$, by the prime number
theorem in arithmetic progressions to the modulus of $\chi$. So
$H(f_1)=H_B(f_1)=\{0\}$ for every odd $k$, and $T_{f_1}\neq\emptyset$ says
that three consecutive integers all have $\Omega\equiv0\pmod k$. The identity
of Section 10 has core term $k^{-3}$ for $f_1$. (AC) for $f_1$ asks that the
logarithmic density of
$\{n:\Omega(n)\equiv\Omega(n+1)\equiv\Omega(n+2)\equiv0\pmod k\}$ tend to
$k^{-3}$ along some scales. After the product-based cancellation of Section
5, only zero-sum terms remain. For each fixed $k$ a triple, once found, is a
finite certificate, but nothing on this page proves existence for every odd
$k\ge5$ at once. Any complete solution must. This is the most specific test
of a proposed full route. Recent work on prime factors of consecutive
integers, described in Source uses, rests on two-point correlation estimates
and on upper bounds for $\Omega$ at many shifts; its abstract claims no
condition on three consecutive values modulo $k$.

### What a complete route needs

The averaging mechanisms examined here involve local statistics of $f$:
the conditioning of Lemma S, every polynomial family of consecutive values
(Lemma P), and Hildebrand's shifted special sets. For odd $k\ge7$ the
digit-twisted process satisfies every identity these mechanisms were found to
use, including all families with two factors per value, and has no triple;
for $k\ge9$ it also satisfies all families with three. A complete route needs
information beyond those established inputs. Possible additions include the
following; they are not an exhaustive list of ways to prove the target:

- a property of the local statistics of completely multiplicative
  $\mu_k$-valued functions that the digit-twisted process violates. One such
  property is the absence of correlation between $X_0^a$, for
  $a\notin H_B$, and linear phases within ergodic components. This is a form
  of local Fourier uniformity at slowly growing scales, the input that Tao
  and Teräväinen's value-pattern paper names for excluding local Bohr sets.
  Section 12 shows that a different property suffices by itself in Case C:
  the absence of nonzero rational eigenvalues in one logarithmic
  Furstenberg system;
- a family with at least four factors per value, or three when $k=7$, that
  the digit-twisted process violates, followed by a proof that every function
  with no triple violates it as well;
- an argument that is not an average over a local pattern.

The stated local-uniformity input is not established here. Pilatte's
Theorem 1.2 gives local Fourier uniformity for the Liouville function when
$H\ge\exp((\log X)^{2/5+\varepsilon})$; Theorem 1.3 gives a quantitative
inverse statement for general bounded multiplicative functions. A direct
passage to a fixed Furstenberg limit would need control with each fixed $H$
before $H$ tends to infinity. These growing-interval estimates do not supply
that interchange of limits. Section 1.2 of the paper describes a possible
transfer through higher-point decoupling, whose required extension is still
an additional input. Walsh's cited abstract gives a smaller growing-interval
range under the generalised Riemann hypothesis, not the desired fixed-scale
conclusion. Neither result is used as a premise here.

Renard's preprint does state higher-point estimates, not merely a pair
theorem. Its Theorem 1.2 applies to non-pretentious functions for which
$\{p:f(p)\ne1\}$ has relative density zero among the primes. The mixed-function
estimate quoted as Theorem 3.4 additionally requires every factor to be
close to a fixed twisted character on $[x^\varepsilon,x]$. These hypotheses
do not hold for the constant-on-primes test $f(p)=\zeta\ne1$: its
distance to $1$ on that interval has squared size
$(1-\operatorname{Re}\zeta)\log(1/\varepsilon)+o(1)$ for fixed $\varepsilon$.
For a fixed nonprincipal character, or any nonzero fixed Archimedean twist,
it has squared size $\log(1/\varepsilon)+o(1)$, by the fixed-modulus prime
number theorem.
Thus the quoted small-distance hypothesis fails as $\varepsilon$ decreases.
This restricted class does not supply a bound for the joint cofactor law of
an arbitrary $f$. The preprint is context only; its result is not a premise
here.

The aggregate cofactor estimate remains open at the arithmetic interface
(CE)--(CF). Proposition O prevents deriving it from the label law and the
listed stationary identities alone; it does not prove that local Fourier
uniformity is necessary. The finite-sums alternative has its separate
selection gap above, with the universal reflection shortcut refuted by
Proposition F. Neither failure is a disproof of T(k).
Section 12 gives a qualitative sufficient property that the digit-twisted
process lacks.

## 12. Rational eigenvalues and the statistical route

Section 8 shows that the averaged identities used on this page do not force
(Z) for $k\ge7$. This section locates the feature of the digit-twisted
process that is responsible: its colour process has a nonzero rational
eigenvalue.
Without one, Furstenberg's multiple recurrence theorem and the conditional
self-similarity of Section 10 force monochromatic consecutive triples. The
arguments are author-recorded and unreviewed. They prove conditional
statements; no universal spectral assertion is established here. A further
composition below handles a nontrivial bounded-distance core by a character
root when one exists. An explicit pointwise quotient then removes that
algebraic restriction, giving the all-order sufficient assertion (QSP).

### Logarithmic Furstenberg systems

Extend $f$ to $\mathbb Z$ arbitrarily and regard it as a point of
$\Omega=\mu_k^{\mathbb Z}$, with the shift $(Tx)_h=x_{h+1}$. A
*logarithmic Furstenberg system* of $f$ is a weak-star limit

$$
\mu=\lim_{j\to\infty}\mathbb E^{\log}_{n\le N_j}\delta_{T^nf}
$$

along some $N_j\to\infty$. Every sequence tending to infinity has a
subsequence along which this limit exists. The limit is $T$-invariant, since
a shift changes a normalized logarithmic average by $o(1)$, and it gives each
cylinder the limiting logarithmic density of the corresponding pattern; for
example
$\mu(x_0=x_r=x_{2r})=\lim_j\mathbb E^{\log}_{n\le N_j}
\mathbf1[f(n)=f(n+r)=f(n+2r)]$.

The *spectrum* of $(\Omega,\mu,T)$ is the set of $\alpha\in\mathbb T$ for
which $g\circ T=e(\alpha)g$ has a nonzero solution $g\in L^2(\mu)$. It is
closed under multiplication by integers: $|g|$ is invariant, so the bounded
truncation $g\mathbf1[|g|\le M]$ is a nonzero solution for large $M$, and its
$m$th power is a solution for $m\alpha$ when $m\ge1$. Complex conjugation
handles negative multipliers, and the constant function handles zero.
Let $S(\mu)$ be the set of primes
$p$ with $1/p$ in the spectrum. If a reduced fraction $a/b$ with $b>1$ is in
the spectrum and $p\mid b$, then $(b/p)(a/b)=a/p$ is in it, and multiplying by
an inverse of $a$ modulo $p$ puts $1/p$ in it. So the system has *trivial
rational spectrum*, meaning no rational $\alpha\ne0$ in its spectrum, exactly
when $S(\mu)=\varnothing$.

Section 10 passes to a further subsequence along which the joint averages
with the profinite position converge. This gives a probability measure
$\rho$ on $\Omega\times\widehat{\mathbb Z}$, invariant under
$T\times(+1)$, whose marginals are $\mu$ and Haar measure; write $(X,\Pi)$
for its coordinates and call $\rho$ a *joint limit* of $\mu$. Under $\rho$,
conditional self-similarity holds at every prime $p$: given $p\mid\Pi$, the
pair $((X_{ph})_h,\Pi/p)$ has the law of $((f(p)X_h)_h,\Pi)$. For $r=pr'$,
conditioning first on $p\mid\Pi$ and then on $r'\mid\Pi/p$ shows by induction
on the number of prime factors that, given $r\mid\Pi$, the pair
$((X_{rh})_h,\Pi/r)$ has the law of $((f(r)X_h)_h,\Pi)$, for every $r\ge1$.

**Lemma E.** Let $\rho$ be a joint limit of $\mu$, and let $r\ge1$ have no
prime factor in $S(\mu)$. Then under $\rho$ the residue of $\Pi$ modulo $r$
is independent of $X$.

*Proof.* For $0<j<r$ put $h_j=\mathbb E_\rho[e(j\Pi/r)\mid X]$, a function in
$L^2(\mu)$. For every bounded measurable $G$ on $\Omega$,

$$
\int G\,(h_j\circ T)\,d\mu=\int (G\circ T^{-1})\,h_j\,d\mu
 =\int G(T^{-1}x)\,e(j\pi/r)\,d\rho(x,\pi)
 =e(j/r)\int G\,h_j\,d\mu .
$$

The first equality is the invariance of $\mu$, and the last substitutes
$(x,\pi)\mapsto(Tx,\pi+1)$, which preserves $\rho$. Hence
$h_j\circ T=e(j/r)h_j$. If $h_j\ne0$, then $j/r$ is in the spectrum; written
in lowest terms its denominator $b>1$ divides $r$, and the previous paragraph
puts $1/p$ in the spectrum for every prime $p\mid b$, contrary to the
hypothesis. So every $h_j$ vanishes. These are the nontrivial Fourier
coefficients of the conditional law of $\Pi\bmod r$ given $X$, which is
therefore uniform. $\square$

**Proposition D.** Let $k$ be odd, let $f$ be in Case C, let $\mu$ be a
logarithmic Furstenberg system of $f$ along $N_j$, and let $\rho$ be a joint
limit of $\mu$.

1. If $r\ge1$ satisfies $\mu(x_0=x_r=x_{2r})>0$ and, under $\rho$, $X$ is
   independent of $\Pi\bmod r$, then
   $\mu(x_0=x_1=x_2)=\mu(x_0=x_r=x_{2r})$, and $T_f$ has positive upper
   logarithmic density. By Lemma E the independence holds whenever $r$ has no
   prime factor in $S(\mu)$.
2. If $\mu$ has trivial rational spectrum, then some $r\ge1$ satisfies the
   hypotheses of part 1.
3. Part 2 has a form that does not need Case C. For any $k\ge1$, any
   completely multiplicative $f:\mathbb N\to\mu_k$, and $\mu$, $\rho$ as
   above: if $\mu$ has trivial rational spectrum and $\mu(x_0=1)>0$, then
   $\mu(x_0=x_1=x_2=1)>0$, so $T_f$ has positive upper logarithmic density.
   If $H_B(f)=\{0\}$, then $\mu(x_0=1)=1/k$; this includes Case C.

*Proof.* The event $\{X_0=X_r=X_{2r}\}$ is unchanged when every colour is
multiplied by $f(r)$. Conditional self-similarity at $r$ therefore gives
$\rho(X_0=X_r=X_{2r}\mid r\mid\Pi)=\mu(x_0=x_1=x_2)$. The independence makes
the left side equal to $\mu(x_0=x_r=x_{2r})$, which proves the identity. Its
left side is the limit along $N_j$ of the logarithmic density of
monochromatic consecutive triples, so by Proposition N

$$
\limsup_{X\to\infty}\mathbb E^{\log}_{n\le X}\mathbf1_{T_f}(n)
 \ge k^{-1}\mu(x_0=x_r=x_{2r})>0 .
$$

For part 2, choose $c\in\mu_k$ with $\mu(x_0=c)>0$. Furstenberg's multiple
recurrence theorem for the invertible measure-preserving system
$(\Omega,\mu,T)$ gives $r\ge1$ with $\mu(x_0=x_r=x_{2r}=c)>0$. When
$S(\mu)=\varnothing$, Lemma E applies to every $r$.

For part 3, the Bergelson--Leibman polynomial recurrence theorem, applied to
the set $\{x_0=1\}$ with the polynomials $m^k$ and $2m^k$, gives $m\ge1$
with $\mu(x_0=x_r=x_{2r}=1)>0$ for $r=m^k$. Then $f(r)=f(m)^k=1$, so
conditional self-similarity at $r$ gives
$\rho(X_0=X_r=X_{2r}=1\mid r\mid\Pi)=\mu(x_0=x_1=x_2=1)$, and Lemma E
makes the left side equal to $\mu(x_0=x_r=x_{2r}=1)>0$. If $H_B(f)=\{0\}$,
Lemma U and Halász's mean value theorem give $\sum_{n\le x}f^a(n)=o(x)$
for every $a\not\equiv0\pmod k$, hence logarithmic mean $0$ by partial
summation, and
$\mu(x_0=1)=k^{-1}\sum_a\lim_j\mathbb E^{\log}_{n\le N_j}f^a(n)=1/k$.
$\square$

Part 3 does not use Proposition N or the correlation theorem quoted in
Section 5. Its inputs are Lemma E, the joint limit of Section 10 with its
conditional self-similarity in the form carrying the factor $f(r)$ (the
colour-rotation invariance used there is not needed), Lemma U, the
polynomial recurrence theorem and Halász's theorem.

**Corollary D.** (a) For an odd prime $k$, T(k) holds, and so
$\Lambda(k,3)<\infty$ by Proposition B, provided every completely
multiplicative $f:\mathbb N\to\mu_k$ in Case C has at least one logarithmic
Furstenberg system with trivial rational spectrum. Case A is covered by
Theorem W, and prime $k$ has no Case B. By part 3, for every odd $k$, each
function with $H_B(f)=\{0\}$ and such a system has triples of ones of
positive upper logarithmic density. This includes functions in weak Case B
whose bounded-distance subgroup is trivial; $H(f)$ and $H_B(f)$ must not be
identified. A nontrivial bounded-distance core is treated conditionally
below, first by a character root and then by a pointwise quotient.

(b) Let $k$ be odd and let $f$ be in Case C with $T_f=\varnothing$. Then for
every logarithmic Furstenberg system $\mu$ of $f$ and every joint limit
$\rho$, the colour sequence is dependent on $\Pi\bmod r$ for every $r$ with
$\mu(x_0=x_r=x_{2r})>0$, and every such $r$ has a prime factor in $S(\mu)$.
By the averaged form of Furstenberg's theorem these $r$ form a set of
positive lower density; in particular $S(\mu)\ne\varnothing$.

Frantzikinakis, Lemańczyk and de la Rue prove that a logarithmic Furstenberg
system of a bounded multiplicative function has trivial rational spectrum if
and only if it is strongly stationary, that is, preserved by every dilation
$x\mapsto(x_{rh})_h$ (their Theorem 2.4). Strong stationarity and
Furstenberg's theorem give part 2 directly, without the position; the proof
above does not use their theorem. They also prove, for a completely
multiplicative function without zeros, that if $1/p$ is in the spectrum of
such a system then so is every $q/p^s$ (their Corollary 2.3). With part (b),
this says that every logarithmic Furstenberg system of a Case C function
without triples of ones would contain all the fractions with denominator a
power of some prime $p$ in its spectrum. They also record that it is not
known whether every Furstenberg system of the Liouville function has trivial
rational spectrum.

### The digit-twisted process has the eigenvalue one third

Lemma E and part 1 of Proposition D use only the stationarity of the joint
law, the Haar position and the conditional self-similarity of monochromatic
events. They therefore apply to the digit-twisted process of Section 8 with
its position $\Pi$, where (D1) gives $\Pr(X_0=X_1=X_2)=0$ for odd $k\ge7$.
Its step-three triples are monochromatic with positive probability. When
$3\nmid\Pi$, the integers $\Pi$, $\Pi+3$ and $\Pi+6$ have the same last
nonzero ternary digit, so $Y_0$, $Y_3$, $Y_6$ form an exact progression whose
first term $\gamma+\sigma\phi(\Pi)$ and difference $3\sigma\beta$ are
independent and uniform. All three lie in one arc of length $1/k$ when the
first term lies in the first half of an arc and the difference lies in
$[0,1/(4k))$, so

$$
\Pr(X_0=X_3=X_6)\ge\frac23\cdot\frac12\cdot\frac1{4k}>0 .
$$

If the colour process were independent of $\Pi\bmod3$, the argument of part
1 with $r=3$ would make the two probabilities equal. So it is not, and Lemma
E puts $3$ in its set of spectral primes. The computation also shows that its
unconditioned law is not invariant under dilation by $3$, the one prime
excluded in (D3). The process evades Proposition D only through this rational
eigenvalue, not through its local linear phase: by the proof of part 2, any
stationary process jointly with a Haar position, obeying the conditional
self-similarity of monochromatic events and having no nonzero rational
eigenvalue has monochromatic consecutive triples with positive probability,
whatever its local phases.

### Splitting off a bounded-distance core

The spectral condition can be applied after removing a pretentious
multiplier. The following composition is useful because the positive
lower-density input and the chosen spectral limit then use the same scales.

**Lemma J.** Let $g:\mathbb N\to\mu_d$ and $h:\mathbb N\to\mu_k$ be
completely multiplicative, with $d\mid k$ and $k$ odd. Suppose that $h$ is at
bounded distance from a Dirichlet character, and that $g$ has a logarithmic
Furstenberg system $\mu_g$ with trivial rational spectrum and
$\mu_g(x_0=1)>0$. Then $T_{gh}$ has positive upper logarithmic density.

*Proof.* First, the entire process of $h$ is a measurable function of the
profinite position in any joint logarithmic limit. Here is the approximation
that justifies this assertion. Let $\eta$ modulo $q$ be a character at
bounded distance from $h$. As in (W0), its order divides $k$. Therefore

$$
E=\{p\nmid q:h(p)\ne\eta(p)\},\qquad \sum_{p\in E}\frac1p<\infty.
$$

Fix $P$ exceeding every prime divisor of $q$. Replace $h(p)$ by $\eta(p)$
at primes $p>P$, obtaining $h_P$. The logarithmic upper density of
$\{n:h(n)\ne h_P(n)\}$ is at most $\sum_{p\in E,\ p>P}1/p$:
the two functions agree unless such a prime divides $n$, and the normalized
logarithmic mass of multiples of $p$ is at most $1/p$.

For fixed $P$ and $L$, $h_P(n)$ is determined by
$n\bmod q\prod_{p\le P}p^L$ whenever every $v_p(n)<L$ for $p\le P$.
Indeed those valuations and the remaining unit part modulo $q$ are then
determined by that residue. Assign value $1$ on the other residue classes to
obtain a periodic $\mu_k$-valued function $b_{P,L}$. The logarithmic upper
density of disagreement with $h$ is at most

$$
\sum_{p\in E,\ p>P}\frac1p+\sum_{p\le P}p^{-L}. \tag{PA}
$$

Taking $P$ large and then $L$ large makes this arbitrarily small. The same
holds at each fixed shift, by translation invariance of logarithmic limits.
The periodic functions, read on Haar $\widehat{\mathbb Z}$, are Cauchy in
measure: their disagreement probability equals its logarithmic density
and is bounded by the sum of their errors in (PA). Along a subsequence they
converge almost surely to a measurable $H:\widehat{\mathbb Z}\to\mu_k$.
In every joint limit the $h$-coordinates are therefore $H(\Pi+i)$,
simultaneously for all integer $i$. This proves the assertion without an
assumption of independence.

Now use scales defining $\mu_g$ and pass to a joint limit of the $g$- and
$h$-processes with the position. Lemma E applies to every modulus, so the
entire $g$-process is independent of $\Pi$, hence of the $h$-process. By
Proposition D, part 3, $\delta_g:=\mu_g(x_0=x_1=x_2=1)>0$. By Theorem W
and the approximation above, the $h$-triple has a limiting logarithmic
probability $\delta_h>0$. Independence gives

$$
\limsup_{X\to\infty}\mathbb E^{\log}_{n\le X}\mathbf1_{T_{gh}}(n)
 \ge \delta_g\delta_h>0,
$$

because simultaneous triples of ones for $g$ and $h$ are a triple of ones
for their product. Only the sequence chosen for $g$ was selected; the
positive lower limit for $h$ holds on it. $\square$

**Proposition V.** Let $H_B(f)=d\mathbb Z/k\mathbb Z$, put $e=k/d$, and
let $\chi$ be a Dirichlet character at bounded distance from $f^d$.
Suppose that there is a Dirichlet character $\eta$, of order dividing $k$,
with $\eta^d=\chi$ on the integers prime to both moduli. Then there is a
factorization $f=gh$ in which $g:\mathbb N\to\mu_d$ has
$H_B(g)=\{0\}$ relative to $\mathbb Z/d\mathbb Z$, and $h:\mathbb N\to\mu_k$
is at bounded distance from $\eta$. If this $g$ has a logarithmic
Furstenberg system with trivial rational spectrum, then $T_f$ has positive
upper logarithmic density.

*Proof.* Outside the primes dividing the two moduli, the set
$E=\{p:f(p)^d\ne\chi(p)\}$ has finite reciprocal sum. At those exceptional
primes and at the primes dividing either modulus set $h(p)=f(p)$ and
$g(p)=1$. At all other primes set $h(p)=\eta(p)$ and
$g(p)=f(p)/\eta(p)$. Then $g(p)^d=1$ everywhere and $h$ is at bounded
distance from $\eta$.

If some $g^a$ with $1\le a<d$ were at bounded distance from a character
$\psi$, then $f^a=g^ah^a$ would be at bounded distance from
$\psi\eta^a$. This would put $a$ in $H_B(f)=d\mathbb Z/k\mathbb Z$,
a contradiction. Thus $H_B(g)=\{0\}$. For $d>1$, Lemma U and Halász's
theorem give $\mu_g(x_0=1)=1/d$ in every logarithmic Furstenberg system;
for $d=1$ it is $1$. Lemma J now gives the last assertion. $\square$

The root hypothesis holds whenever $\gcd(d,e)=1$: $\chi$ has order dividing
$e$, so take $\eta=\chi^b$ with $bd\equiv1\pmod e$. It also holds if the
order of $\chi$, though $e$ need not be, is coprime to $d$.

In particular consider the precise spectral assertion

**(SP).** For every odd $d>1$ and every completely multiplicative
$g:\mathbb N\to\mu_d$ with $H_B(g)=\{0\}$, at least one logarithmic
Furstenberg system of $g$ has trivial rational spectrum.

If (SP) holds, then T(k) holds for every squarefree odd $k$. For such $k$,
every divisor $d$ is coprime to $k/d$, so Proposition V applies. Proposition
B gives the finite bound for each such $k$ and its equality with
$\Lambda(k,3)$. For a fixed squarefree $k$, only the instances of (SP) with
$d\mid k$ are needed. This is a conditional conclusion, not a proof of (SP)
or of the full every-odd-$k$ target. It yields positivity, not (AC).

**The root need not exist.** Let $k=9$, and let $\chi$ modulo $7$ have
order $3$. For every prime $p\ne7$ choose $f(p)\in\mu_9$ with
$f(p)^3=\chi(p)$, and put $f(7)=1$. Then $H_B(f)=3\mathbb Z/9\mathbb Z$,
but no Dirichlet character $\eta$ of order dividing $9$ has
$\eta^3=\chi$ away from the moduli.

To see the root failure, enlarge the modulus of a proposed $\eta$ to
include $7$. Its restriction to the $7$-primary unit factor has order
dividing both $9$ and $\varphi(7^s)=6\cdot7^{s-1}$, hence dividing $3$.
Its cube is trivial on that factor, whereas $\chi$ is not. The Chinese
remainder theorem prevents factors at other primes from changing this
restriction. Since $f^3$ is at bounded distance from $\chi$, the subgroup
$H_B(f)$ contains $3\mathbb Z/9\mathbb Z$. If any exponent outside that
subgroup were in $H_B(f)$, it would generate $\mathbb Z/9\mathbb Z$ and
put $f$ at bounded distance from a character $\eta$. By (W0) the order of
$\eta$ would divide $9$, and character separation would give
$\eta^3=\chi$ away from the moduli, contradicting what was just proved.
This proves the asserted bounded-distance subgroup.

Thus a general factorization into a $\mu_d$-valued function and a
bounded-distance pretentious multiplier cannot be assumed: any such
factorization would itself supply the forbidden character root. This is an
arithmetic failure of this particular splitting step. No triple-free
property is claimed for the displayed $f$, and it is not a counterexample
to T(9), (AC), or (SP).

### A quotient with exact power-dilation symmetry

There is a relative spectral formulation that covers every odd order
without a Dirichlet root. Its quotient is an explicit sequence obtained
from $f$, not an independently sampled reference process. It is generally
not multiplicative, so (SP) does not assert its spectral property.

Fix $f:\mathbb N\to\mu_k$, let $H_B(f)=d\mathbb Z/k\mathbb Z$ and put
$e=k/d$. Define the section

$$
s_e(\exp(2\pi i j/e))=\exp(2\pi i j/k)\quad(0\le j<e),
\qquad
b_f(n)=s_e(f(n)^d),\qquad u_f(n)=f(n)/b_f(n).
$$

For $e=1$ set $s_1(1)=1$. Then $b_f(n)^d=f(n)^d$ and $u_f(n)\in\mu_d$.
Although the section need not be a homomorphism, for every $m,n\ge1$
complete multiplicativity and $f(m^k)=1$ give

$$
b_f(m^k n)=b_f(n),\qquad u_f(m^k n)=u_f(n). \tag{PD}
$$

The core $f^d$ is at bounded distance from a character. The approximation
(PA), applied to $f^d$ and then to the finite map $s_e$, shows that the
$b_f$-process is a measurable function of the profinite position in any
joint logarithmic limit. Moreover $b_f(n)=1$ exactly when $f(n)^d=1$.
Consequently Theorem W gives a positive lower logarithmic density for
$b_f(n)=b_f(n+1)=b_f(n+2)=1$.

The quotient has a uniform one-point marginal. For $1\le a<d$, expand the
function $z\mapsto s_e(z)^{-a}$ in characters of $\mu_e$:

$$
s_e(z)^{-a}=\sum_{j=0}^{e-1}c_{a,j}z^j,
\qquad u_f(n)^a=\sum_{j=0}^{e-1}c_{a,j}f(n)^{a+dj}.
$$

Every exponent $a+dj$ is outside $H_B(f)$. Lemma U and Halász's theorem
therefore give mean zero for each summand, including on every fixed
arithmetic progression. For the last statement, remove the fixed greatest
common divisor of the progression's residue and modulus, then expand its
coprime residue condition in Dirichlet characters. Thus in every joint
logarithmic limit the coordinate $U_0$ of the quotient process is uniform on
$\mu_d$ and independent of the profinite position. In particular every
logarithmic Furstenberg system $\mu_u$ of this sequence has
$\mu_u(x_0=1)=1/d$.
For $d=1$ the same assertion holds because $u_f=1$.

This is only one-point independence. It does not establish independence of
the entire quotient process, or of its three-point events, from the
position.

**Proposition QD (conditional).** For the fixed $f$ above, suppose that
$u_f$ has at least one logarithmic Furstenberg system with trivial rational
spectrum. Then $T_f$ has positive upper logarithmic density.

*Proof.* Let $\mu_u$ be such a system. Take the defining scales and pass to
a joint limit of the $u_f$- and $b_f$-processes and the profinite position.
Lemma E uses only stationarity and the Haar position, so it applies here
even though $u_f$ may not be multiplicative. It makes the entire
$u_f$-process independent of the position, and hence of the $b_f$-process.

Apply polynomial multiple recurrence to $A=\{x_0=1\}$, of measure $1/d$,
with the polynomials $m^k$ and $2m^k$. It gives a fixed $m\ge1$, with
$r=m^k$, for which $\mu_u(x_0=x_r=x_{2r}=1)>0$. By (PD), changing
variables $n=r\ell$ in the logarithmic averages gives

$$
\Pr(U_0=U_r=U_{2r}=1\mid r\mid\Pi)
 =\mu_u(x_0=x_1=x_2=1).
$$

The cutoffs $N_j/r$ give the same logarithmic limit as $N_j$, since their
logarithmic difference has bounded mass for this fixed $r$. Independence
from $\Pi\bmod r$ makes the left side
$\mu_u(x_0=x_r=x_{2r}=1)>0$. Put
$\delta_u=\mu_u(x_0=x_1=x_2=1)>0$. The $b_f$-triple probability
$\delta_b$ in the same limit is positive by the core lower-density bound.
The two processes are independent, so the simultaneous triple has
probability $\delta_u\delta_b>0$. Since $f=u_f b_f$, it is a triple of ones
for $f$. This proves the asserted positive upper logarithmic density along
the one sequence defining $\mu_u$. $\square$

Here is the full quantifier statement of this alternative sufficient input:

**(QSP).** For every odd $k\ge1$ and every completely multiplicative
$f:\mathbb N\to\mu_k$, form $d,e,s_e,u_f$ exactly as above using $H_B(f)$.
At least one logarithmic Furstenberg system of $u_f$ has no nonzero rational
eigenvalue.

Proposition QD and Proposition B show that (QSP) implies T(k) and
$\Lambda(k,3)<\infty$ for every odd $k$. This implication uses neither the
product-cancellation theorem of Section 5 nor a Dirichlet root of the core.
When $H_B(f)=\{0\}$, $u_f=f$, so the unsolved constant-on-primes test is
still present. When the core does not split, the new hypothesis concerns
the explicit nonmultiplicative sequence $u_f$; it does not follow from (SP)
as stated. This is a conditional route to the whole target, not a proof of
(QSP), a cancellation estimate, or a claim that (QSP) is necessary.

### What the reduction leaves open

Neither the universal hypothesis of Corollary D(a), (SP), nor (QSP) is
proved here.
The Liouville remark above identifies a related open spectral question; it
does not imply that the property is unknown for every individual function
in Case C. Under the logarithmically averaged Elliott conjecture at every
number of points, Lemma U gives the uniform Bernoulli system for a function
with $H_B=\{0\}$, which would imply (SP). No implication from the
three-point conjecture alone to (SP) is established on this page.

The prime-order route needs less than trivial rational spectrum: for one
joint limit, the colour sequence may instead be independent of the position
modulo a single step carrying positive monochromatic triple mass. No such
step is produced here for arbitrary functions in Case C, including the
constant-on-primes test. Marginal uniformity on residue classes supplies no
independence for this three-point event.

The factorization route handles bounded-distance cores only under the
character-root condition of Proposition V. The order-nine example shows
that the condition cannot be dropped as an algebraic convenience.
Proposition QD avoids this step by using the actual quotient's power-dilation
symmetry. Its missing input is (QSP), not the one-point independence already
proved for that quotient. No argument here eliminates rational eigenvalues
detected by longer quotient patterns. Thus the spectral route reaches the
full target conditionally, with a precisely defined sequence, but leaves its
central arithmetic assertion open. The quantitative alternatives (AC), (CF),
and the one-sided bound of Section 11 also remain unproved at the actual joint
cofactor estimate.

## Source uses and reading limits

- Lehmer, Lehmer, Mills and Selfridge 1962, through the accepted claim page
  linked in Section 2: statement standing, refereed, machine case analysis not
  independently reviewed here. Used in Corollary 3 only.
- [[../library/integer_sequences/lehmer_1963_pairs_consecutive_power_residues/_index|Lehmer, Lehmer and Mills 1963]],
  read in full in its transcription: its realization step cites a theorem of
  an earlier paper with parity conditions that it does not print. Lemma R is
  proved here independently and does not rely on that citation.
- Tao and Teräväinen 2019 (Algebra Number Theory), held as arXiv:1809.02518v2:
  definitions of pretentious distance and weak pretence, Conjecture 1.3,
  Theorems 1.5 and 1.6 quoted there from the authors' Duke paper, and the
  statement that the two-function case of Conjecture 1.3(ii) is proved in
  Tao's 2016 paper. The Duke paper's proofs and Tao's 2016 paper are not held
  and were not read; their theorems are used at the statement standing of
  these quotations.
- Tao and Teräväinen, *Value patterns of multiplicative functions and related
  sequences*, arXiv:1904.05096v2: the abstract and Section 1 through Theorem
  1.14, including Definitions 1.4, 1.6 and 1.7, Conjecture 1.5, Theorems 1.8
  to 1.10 and the discussion of local Bohr sets, were read; the proofs were
  not. Not held; used as context for item 4 of Section 9 and for Section 11,
  not as a premise.
- [[../library/integer_sequences/hildebrand_1991_consecutive_kth_power_residues_ii/_index|Hildebrand 1991]]
  (Michigan Math. J.): the article was read in full, Sections 1 to 4 with
  their proofs, for the account of its special-set method in Section 11. Its
  Theorem 2 is not a premise of any argument here.
- C. Dietzel, *On a theorem of Hildebrand*, Moscow J. Comb. Number Th. 8
  (2019), 189--191, [arXiv:1810.01518v1](https://arxiv.org/html/1810.01518v1):
  the full argument, including Theorems 3--4, Lemma 1, and Comment 1, was
  read in the public HTML. Theorem 4 supplies the finite-sums
  pair interface in Section 11; Comment 1 explicitly leaves odd-index
  triples unresolved. No PDF proof audit was made for this argument.
  Proposition F is proved independently above, without using that theorem.
- M. N. Walsh, *Stability under scaling in the local phases of multiplicative
  functions*, [arXiv:2310.07873v1](https://arxiv.org/abs/2310.07873v1):
  abstract only. Not held; context for Section 11, not a premise.
- C. Pilatte, *Improved bounds for the Fourier uniformity conjecture*,
  [arXiv:2604.26564v1](https://arxiv.org/abs/2604.26564v1): the abstract and
  Sections 1.1--1.3, including the statements of Theorems 1.2 and 1.3 and
  the discussion of the missing higher-point decoupling step, were read in
  the public HTML. The proofs were not read. Not held; context for the
  scale restriction in Section 11, not a premise.
- T. Renard, *Truncated pretentious distances of multiplicative arithmetic
  functions*, [arXiv:2609.37332v1](https://arxiv.org/abs/2609.37332v1):
  Sections 1--2 and Section 3 through the proof of Theorem 1.2 were read in
  the public HTML, including the mixed-function estimate quoted there as
  Theorem 3.4 from Klurman, Mangerel and Teräväinen. That quoted theorem's
  proof was not read. The sparse-prime hypothesis is used only to delimit
  the source's scope in Section 11. Not held; no result of the preprint is
  a premise of the argument.
- T. Tao and J. Teräväinen, *Quantitative correlations and some problems on
  prime factors of consecutive integers*,
  [arXiv:2512.01739v2](https://arxiv.org/abs/2512.01739v2): abstract only.
  It states an asymptotic, for almost all $x$, for the
  number of $n\le x$ with $\omega(n)=\omega(n+1)$, with similar results for
  $\Omega$ and $\tau$, from a two-point correlation estimate, and the
  existence of infinitely many $n$ with $\Omega(n+k)\ll k$ for every $k$. Not
  held; context for the constant-on-primes case of Section 11, not a
  premise.
- Koukoulopoulos, *The Distribution of Prime Numbers*, author's preliminary
  version, [author-hosted PDF](https://dms.umontreal.ca/~koukoulo/documents/publications/primes.pdf),
  accessed 2026-10-16:
  Axioms 1 and 2 and Theorem 18.11(a), pp. 185--190, supply the sieve
  input in Lemma S. Theorem 19.1 and its proof on pp. 192--199 were read;
  the statements on pp. 190 and 195 were also checked on the page images.
  Only the asymptotic part is used, not the numerical lower-bound constants.
  The multiform probability model is derived in Lemma S, rather than imported
  as an unspecified Kubilius theorem.
- N. Frantzikinakis, M. Lemańczyk and T. de la Rue, *Furstenberg systems of
  pretentious and MRT multiplicative functions*,
  [arXiv:2304.03121v4](https://arxiv.org/abs/2304.03121v4), whose arXiv
  comments say it is to appear in Ergodic Theory Dynam. Systems: the abstract,
  Section 2.1, the definitions of Section 3.4 and the proof of Theorem 2.4 in
  Section 4.2 were read in the public HTML. Theorem 2.4 and the Liouville
  remark supply the comparisons in Section 12; Corollary 2.3 supplies the
  stated spectral consequence after Corollary D. These uses retain statement
  standing. Lemma E and Proposition D are proved without these results.
  Not held.
- Standard external inputs: Chebotarev for a finite Galois extension of a
  number field (Lemma R), the fixed-modulus prime number theorem in arithmetic
  progressions and Mertens estimates (Theorem W), the fixed-modulus
  Vinogradov--Korobov estimate, used only with exponent $3/4$ (Lemma U), and,
  in Section 12, Furstenberg's multiple recurrence theorem for three-term
  progressions with its averaged form, the Bergelson--Leibman polynomial
  multiple recurrence theorem (J. Amer. Math. Soc. 9 (1996)), and Halász's
  mean value theorem. Their proofs were not reconstructed here. The Kummer
  independence and the surjectivity of the radical Galois action in Lemma R
  are derived on this page.
- The [author report for Problem 436](https://www.erdosproblemaday.com/report/436)
  dated 2026-07-28
  claims a lower bound for $\Lambda(5,3)$; it is pending and unverified, and
  is mentioned only in Section 9, item 9.
