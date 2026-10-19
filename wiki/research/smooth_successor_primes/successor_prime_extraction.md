---
name: research/smooth_successor_primes/successor_prime_extraction
title: Primes 2u-1 with smooth u
desc: "The independently graded conditional extraction of primes p=2u-1 with smooth p+1, using the proved balanced dyadic scope and exact P and classical premises; the unrestricted dyadic claim is refuted."
created: 2026-10-15T07:33:49Z
updated: 2026-10-15T07:33:49Z
---

# Primes 2u-1 with smooth u

***

This page carries the second link of the
[[research/smooth_successor_primes/_index|smooth-successor route]]: from the
[[research/smooth_successor_primes/signed_type_ii|Type II estimate for factorizations of 2u-1]]
to a count of primes $p$ with $P^+(p+1)\le x^\delta$, and from it to Hypothesis
$\mathrm A^+$. The extraction is OpenAI's, from Section 7 of the
[[../library/arithmetic_functions/openai_2026_weighted_dilation_graphs_smooth_shifted_primes_totient_fibers/_index|weighted-dilation manuscript]];
running it on primes $2u-1$ is Shisheng Li and Zhong Zhuang's proposal; the
derivation and checks below are Plasma AI's.
The
[[research/smooth_successor_primes/evidence/verify/conditional_chain/_index|conditional-chain examination]]
of 2026-10-15 has a [distinct passing grade](evidence/verify/conditional_chain/grade.md),
examined on 2026-10-16 UTC, for the frozen balanced extraction conditional
on exact P and the stated classical premises. The unrestricted dyadic
assertion remains **refuted-as-stated**.

Besides the signed Type II estimate, which assumes premise (P), the argument
uses the following source results. Together with the Section 2 estimates they
are premise (E) of the combined sketch. They concern $u$ or ordinary factor
tests; the only occurrence of $N_u$ is a size relation in (7.17).

- **Proposition 7.1** (candidate mass) concerns $A$, $X_A$ and the prime
  factors of $u$ only.
- **Lemma 7.3** (proxy discrepancy) concerns the factor tests and their proxies
  only.
- **Lemma 7.4** (proxy density bounds and the Buchstab identity). Its bound
  (7.17) is stated for factorizations $mn=N_u$; its proof uses $N_u$ only
  through $N_u\asymp x$, which holds for $N_u=2u-1$.

It also uses the block sieve (the manuscript's Lemma 2.9), the
Siegel–Walfisz theorem, the multiplicative large sieve and Mertens' estimates.
The [[research/smooth_successor_estimates/_index|written reconstruction of E]]
supplies these estimates at precisely the restrictions and parameter order
used below. Its [separate passing grade](../smooth_successor_estimates/evidence/verify/elementary_estimates/grade.md)
accepts the operative sieve fragment and exact E2–E5 scopes relative to
their stated classical premises. The [graded comparison](evidence/verify/conditional_chain/interface_disposition.md)
checks the actual interfaces; it supplies no P acceptance.
In particular, its interval-restricted proxy discrepancy is for the same
original $\alpha$ required by the signed Type II estimate.

## The candidate

Fix $0<\delta<1/4$. Notation is that of the
[[research/smooth_successor_primes/signed_type_ii|Type II page]]. Fix a
nonnegative smooth $\Psi$ supported in $[1,2]$ and bounded below by a positive
constant on a closed subinterval of $(1,2)$ of positive length. Take $q=1/2$,
$\ell=1$, $\lambda=2$,

$$
c_1=1,\quad c_2=\tfrac65,\quad c_3=\tfrac32,\quad c_4=\tfrac95,\qquad
s'=\frac1{r_0(c_1+c_2)},\qquad s_j=s'2^{-j}L,
$$

with $r_0$ a fixed integer such that $c_2s'<\delta$ and $(r_0-1)c_1/2\ge
c_2+1$. Let $j_x$ be the largest $j$ with $c_1s_j\ge20T$ and
$\mathcal Q_j=\{p:c_1s_j\le\log p\le c_2s_j\}$. At each scale $j$ for which
$[c_3s_j,c_4s_j]$ lies inside $[L^{1/10},L^{1/5}]$ or inside
$[L^{3/10},L^{2/5}]$, the primes with logarithm in $[c_3s_j,c_4s_j]$ form a
small or a big group. By the prime number theorem their harmonic masses lie
between fixed positive bounds and each kind has a number of groups comparable
to $T$, so they meet the hypotheses of the Type II page with
$(a,b,c,d)=(1/10,1/5,3/10,2/5)$; they avoid the bands because
$c_2<c_3<c_4<2c_1$, and the bands meet its hypotheses with $\lambda=2$ and
$20T/c_1\le s_{j_x}<40T/c_1$. The exceptional slot of band $j_{**}\ge j_0$
holds an integer $v$ with $e^{c_1s_{j_{**}}}\le v\le e^{c_2s_{j_{**}}}$ and
$P^-(v)>W$, where $j_0$ is a fixed lower bound depending only on the candidate
geometry. Then

$$
A(u)=a_Q(u_*)W_1(u),\qquad X_A=\sum_uA(u)\Psi(u/x),\qquad N_u=2u-1 .
$$

These are the manuscript's choices; only $N_u$ changes. By Proposition 7.1,
for constants $C,C_A,C_w$ depending only on the early choices and for large
$x$,

$$
A(u)\le L^C\tau(u_*),\qquad A(u)\le\exp(C_w\sqrt L)\ (u\asymp x),\qquad
X_A\asymp\frac xLH_QH_P\gg xL^{-C_A},
$$

where $H_Q=\sum_va_Q(v)/v$ and $H_P=\sum_{r_*=1}W_1(r)/r$; the comparison
constants do not depend on $j_{**}\ge j_0$; and on the support of
$A(u)\Psi(u/x)$ every prime factor of $u$ lies in $[L^{20},x^\delta]$. The upper
end uses $c_2s'<\delta$: the band primes are at most $x^{c_2s'}$, the
exceptional integer is at most $x^{c_2s'}$, and the group primes are below $W$.

## Type I distribution in the class of 1/2

For odd squarefree $d$ put

$$
r(d)=\sum_{d\mid2u-1}A(u)\Psi(u/x)-\frac{X_A}{\varphi(d)} .
$$

**Proposition (Type I).** For every fixed $\vartheta<1/2$ and $D>0$,

$$
\sum_{\substack{d\le x^\vartheta\\ d\text{ odd, squarefree}}}|r(d)|
\ll xL^{-D}+X_AL^{-18}.
$$

*Proof.* If a prime $l$ divides both $d$ and $u$, then $2u-1\equiv-1\pmod l$,
so $d\nmid2u-1$. For $(u,d)=1$, $d\mid2u-1$ holds exactly when
$u\equiv\bar2\pmod d$, where $\bar2=(d+1)/2$ is the inverse of $2$, a unit
class. By orthogonality,

$$
\sum_{d\mid2u-1}A(u)\Psi(u/x)
=\frac1{\varphi(d)}\sum_{\chi\bmod d}\overline{\chi(\bar2)}
\sum_uA(u)\Psi(u/x)\chi(u).
$$

The principal character gives $\varphi(d)^{-1}\sum_{(u,d)=1}A(u)\Psi(u/x)$.
Replacing it by $X_A/\varphi(d)$ costs in total at most

$$
\sum_uA(u)\Psi(u/x)\sum_{\substack{d\le x^\vartheta\\(d,u)>1}}
\frac{\mu^2(d)}{\varphi(d)}
\le X_A\max_u\sum_{l\mid u}\frac1{l-1}
\sum_{d'\le x}\frac{\mu^2(d')}{\varphi(d')}
\ll X_AL^{-18},
$$

because every prime factor of a supported $u$ is at least $L^{20}$, there are
$O(L/\log L)$ of them, and the last sum is $O(L)$.

The nonprincipal characters contribute at most
$\varphi(d)^{-1}\sum_{\chi\ne\chi_0}|\sum_uA(u)\Psi(u/x)\chi(u)|$, since
$|\chi(\bar2)|=1$; this quantity does not involve the unit class. Extract one
pure slot of band $0$ to write $A(u)=\sum_{pr=u,\ p\in\mathcal Q_0}b(r)$ with
$0\le b(r)\le L^{O(1)}\tau(r)$; the extracted prime is not a group prime, so
$W_1(u)=W_1(r)$. Split $p$ and $r$ into dyads $P,U$ with $PU\asymp x$; for a
fixed $a_0>0$ every contributing dyad has $x^{a_0}\ll P,U\ll x^{1-a_0}$. A
nonprincipal $\chi\bmod d$ is induced by a primitive $\chi^*$ modulo some
$f>1$ with $d=hf$ and $(h,f)=1$, acting as $\chi^*$ together with
$(p,h)=(r,h)=1$. For conductors $f\asymp R>L^{C'}$, separate $\Psi(pr/x)$ by
Mellin inversion at bounded integrated cost; the multiplicative large sieve and
Cauchy's inequality give

$$
\sum_{f\asymp R}\frac1{\varphi(f)}\sum_{\chi^*\bmod f}^{*}
\Bigl|\sum_{p\asymp P}a_p\chi^*(p)\Bigr|\Bigl|\sum_{r\asymp U}b_r\chi^*(r)\Bigr|
\ll xL^{O(1)}\Bigl(\frac1R+\frac1{\sqrt P}+\frac1{\sqrt U}
+\frac R{\sqrt x}\Bigr),
$$

which, summed over dyads, over $h$ with weight $1/\varphi(h)$ and over $R\le
x^\vartheta$, saves any fixed power of $L$ once $C'$ is large. For $1<f\le
2L^{C'}$, fix $r$ and apply the Siegel–Walfisz theorem with partial summation
to the sum over $p$ with the cutoff $\Psi(pr/x)$, which saves any fixed power of
$L$; the primes $p\mid h$ are $O(1)$ in number, since they exceed $x^{a_0}$ and
$h\le x^\vartheta$, and cost $x^{1-a_0}L^{O(1)}$ in total. $\square$

This is the manuscript's Proposition 7.2 with the unit class $-\bar2$ replaced
by $\bar2$; every estimate after orthogonality is in absolute value.

## The preliminary sieve

Write $V(y)=\prod_{p\le y}(1-1/p)$, $V_1(y)=\prod_{3\le p\le y}(1-1/(p-1))$ and
$\mathfrak S=2\prod_{p\ge3}(1-(p-1)^{-2})>0$, so that $V(y)\sim
e^{-\gamma_E}/\log y$ and $V_1(y)\sim\mathfrak SV(y)$. Fix $0<\kappa<1/50$ and
then a small fixed $b_1>0$; put $b_*=b_1/3$, choose $j_{**}\ge j_0$ with
$c_2s'2^{-j_{**}}<b_*/4$ (so that $\eta_*<b_*/4$), and take
$h=2\lfloor1/(40b_1)\rfloor$ and $\vartheta=1/2-\kappa/2$. For small $b_1$, $h$
is large enough for the block sieve and $b_1(4h+2)<\vartheta$.

Every $N_u=2u-1$ is odd. Apply the block sieve to the integers $u$ with weight
$A(u)\Psi(u/x)$, with the bad conditions $p\mid2u-1$ for the odd primes $p\le
x^{b_1}$. For squarefree odd $d$ the weight on which all conditions at $p\mid d$
hold is $X_A/\varphi(d)+r(d)$, so the density is $g(p)=1/(p-1)$, which satisfies
$g(3)=1/2$ and $\sum_{w<p\le w^2}g(p)\ll1$. With the Type I bound at level
$x^\vartheta$ and $D>C_A+10$,

$$
\sum_{P^-(2u-1)>x^{b_1}}A(u)\Psi(u/x)
\ge\frac{\mathfrak SX_A}L\Bigl\{\frac{e^{-\gamma_E}}{b_1}
\bigl(1-O(e^{-c/b_1})\bigr)+o(1)\Bigr\},
$$

with constants uniform for small $b_1$ and $0<\kappa<1/50$. This is the
manuscript's (7.11); the density $1/(p-1)$ is the same for both signs, because
$2u\pm1\equiv0\pmod p$ each fix one unit class of $u$.

## Composites away from balance

Fix a finite mesh of bins $(\gamma,\gamma']$ partitioning $(b_1,1/2-\kappa]$,
chosen below. Write $I_\gamma(m)=\mathbf 1_{P^-(m)>x^\gamma}$ and
$I_{\rm pr}(m)=\mathbf 1_{m\text{ prime}}$, and let $B_\gamma$, $B_{\rm pr}$ be
their cell proxies at precision $\Delta_L=L^{-S}$: on a cell
$C_Y=(Y,e^{\Delta_L}Y]$ the proxy of a test $I$ is
$c_I(C_Y)\mathbf 1_{P^-(m)>W}$, where $c_I(C_Y)$ is the number of $m\in C_Y$
with $I(m)=1$ divided by the number of $W$-rough $m\in C_Y$. By Lemma 7.3,
$0\le B_I\le1$, and for any fixed $B$ the restricted differences
$(I-B_I)\mathbf 1_K$ satisfy $(\mathrm D_B)$ once $S>2B+3$, uniformly for
intervals $K$ inside dyads of $[x^{b_1/4},x^{1-b_1/4}]$.

A composite $2u-1$ counted above whose least prime factor $p$ lies in the bin
$(x^\gamma,x^{\gamma'}]$ has $m=(2u-1)/p$ with $P^-(m)>x^\gamma$, so the
composites of this bin contribute at most

$$
\sum_{\substack{mp=2u-1\\ x^\gamma<p\le x^{\gamma'}\text{ prime}}}
A(u)\Psi(u/x)\,I_\gamma(m).
$$

All contributing dyads of $m$ and $p$ lie in $[x^{b_*},x^{1-b_*}]$. Apply the
signed Type II estimate with $\alpha=(I_\gamma-B_\gamma)\mathbf 1_K$, $K$ the
cofactor range within a dyad, and $\beta$ the prime indicator of the bin within
a dyad: replacing $I_\gamma$ by $B_\gamma$ costs $o(X_A/L)$ in total. By the
bound (7.17) of Lemma 7.4,

$$
c_\gamma(m)\le\frac{\sup_{\gamma\le a\le\gamma'}D_\gamma(1-a)+o(1)}{LV(W)},
$$

where $D_\gamma$ is the Buchstab density (7.15) of the manuscript. For a prime
$p>W$, $P^-((2u-1)/p)>W$ if and only if $P^-(2u-1)>W$, so the bin contributes at
most that constant over $LV(W)$ times

$$
\sum_{x^\gamma<p\le x^{\gamma'}}\ \sum_{\substack{p\mid2u-1\\ P^-(2u-1)>W}}
A(u)\Psi(u/x).
$$

For each $p$, sieve the odd primes up to $W$ with base mass $X_A/(p-1)$,
density $1/(l-1)$, remainders $r(pd)$ and $h=2\lceil T^2\rceil$. All products
$pd$ are at most $x^{1/2-\kappa+o(1)}<x^\vartheta$, and distinct pairs $(p,d)$
give distinct products, $p$ being their only prime factor above $W$. The Type I
bound therefore gives

$$
\sum_{x^\gamma<p\le x^{\gamma'}}\ \sum_{\substack{p\mid2u-1\\ P^-(2u-1)>W}}
A(u)\Psi(u/x)=X_AV_1(W)\sum_{x^\gamma<p\le x^{\gamma'}}\frac1{p-1}
+o(X_AV(W)),
$$

and since the reciprocal sum tends to $\log(\gamma'/\gamma)$, the bin
contributes at most

$$
\frac{\mathfrak SX_A}L\Bigl\{\sup_{\gamma\le a\le\gamma'}D_\gamma(1-a)
\log(\gamma'/\gamma)+o(1)\Bigr\}.
$$

By the joint continuity in Lemma 7.4, a fine enough fixed mesh makes the sum of
these constants at most
$\int_{b_1}^{1/2-\kappa}D_\alpha(1-\alpha)\,d\alpha/\alpha+1/10$. The identity
(7.18), $\int_{b_1}^{1/2}D_\alpha(1-\alpha)\,d\alpha/\alpha=D_{b_1}(1)-1$, and
the bound (7.19), $D_{b_1}(1)\le e^{-\gamma_E}b_1^{-1}(1+O(e^{-c/b_1}))$, then
leave

$$
\sum_{\substack{2u-1\text{ prime, or}\\ P^-(2u-1)>x^{1/2-\kappa}}}A(u)\Psi(u/x)
\ge\frac{\mathfrak SX_A}L\Bigl\{1-\frac1{10}-O(b_1^{-1}e^{-c/b_1})+o(1)\Bigr\}
\ge\frac{\mathfrak SX_A}{2L}
$$

once $b_1$ is small enough.

## Balanced composites

A composite $2u-1\ll x$ with $P^-(2u-1)>x^{1/2-\kappa}$ has exactly two prime
factors, as $3(1/2-\kappa)>1$, and both lie in
$\mathcal B_\kappa=[x^{1/2-2\kappa},x^{1/2+2\kappa}]$ for large $x$. Overcount
by ordered pairs of primes $m,n\in\mathcal B_\kappa$ with $mn=2u-1$. Replace
$I_{\rm pr}(m)$ by $B_{\rm pr}(m)$ with the signed Type II estimate, then
$I_{\rm pr}(n)$ by $B_{\rm pr}(n)$ with the roles of the two factors exchanged,
the remaining coefficient $B_{\rm pr}(m)$ being bounded by one. Since
$B_{\rm pr}\le C/(LV(W))$ on $\mathcal B_\kappa$ by (7.16), with $C$ absolute
for $0<\kappa<1/50$, the balanced composites contribute $o(X_A/L)$ plus

$$
\frac C{L^2V(W)^2}\sum_{\substack{m,n\in\mathcal B_\kappa,\ mn=2u-1\\
P^-(m)>W,\ P^-(n)>W}}A(u)\Psi(u/x).
$$

**Balanced dyadic bound.** For dyads $m\asymp M_1$ and $n\asymp M_2$
intersecting $\mathcal B_\kappa$, with $M_1M_2\asymp x$ and
$0<\kappa<1/50$,

$$
\sum_{\substack{m,n\in\mathcal B_\kappa,\ m\asymp M_1,\ n\asymp M_2,\ mn=2u-1\\ P^-(m)>W,\ P^-(n)>W}}
A(u)\Psi(u/x)\ll X_AV(W)^2,
$$

with a constant depending only on $\delta,r_0,\Psi$, the group geometry and the
fixed $j',\theta$ below, not on $\kappa$, $b_1$, $j_{**}$, $S$ or the analytic
parameters.

The balance restriction supplies $M_i\ll x^{0.54}$, which is used in the
box-error estimate below. A product-size condition alone is not asserted
to imply this bound.

The conditional-chain examination records **refuted-as-stated** for the
frozen isolated formulation without the balanced range, using $m=1$ to
lose one roughness factor. It records **refutation-failed** for the balanced
specialization consumed here. The explicit balanced-range statement and
box-error qualification above differ from the frozen wording; its exact
subject and witness are retained with the examination.

*Proof.* Choose a large fixed $j'$ and $\theta$ with

$$
c_2s'2^{-j'}<\theta<c_1s'2^{-j'+1},\qquad 10\theta\le\frac1{20},\qquad
\sum_{j\ge j'}r_0c_2s'2^{-j}\le\frac1{25},
$$

possible because $c_2<2c_1$, and enlarge $j_0$ so that $j_0\ge j'$; the
*micro* bands are those with $j\ge j'$, and their harmonic mass $H_Q^{\rm mic}$
satisfies $H_Q^{\rm mic}\ll H_Q$. An *assignment* consists of complete ordered
lists in the micro bands, the exceptional slot included, and one marked prime
in each group, with weight
$\lambda=\prod_{j\ge j'}(1/r_0!)\prod_g(1/V_g)$; let $D_1$ be the product of
its entries. Then

$$
D_1\le x^{1/20},\qquad
\sum_{\rm assgn}\frac\lambda{D_1}=H_Q^{\rm mic},\qquad
\sum_{\rm assgn}\lambda\le x^{1/20}H_Q^{\rm mic}.
$$

Write $s=|\mathcal S|+|\mathcal B|$ and $\omega(u)=\sum_g\omega_g(u)$.
For each assignment, ban every odd prime $l\le x^\theta$ that is not a group
prime and does not divide $D_1$, and ban each group prime not dividing $D_1$
independently with probability $1-q$. Expanding $A(u)$ into lists and marks,
every non-group prime factor of $u$ below $x^\theta$ divides $D_1$: the
omitted bands contain only pure primes above $x^\theta$, and the entire
exceptional integer is in $D_1$. Its prime divisors need not lie in any prime
band. The group part of $D_1$ consists of exactly one mark per group, so the
expected value of the permissions is the damping $q^{\omega(u)-s}$ of $W_1$.
For a fixed residual product the normalized number of omitted pure-prime lists
is at most one, since its contribution in each band is a product of
reciprocal multiplicity factorials. Dropping those residual restrictions gives
the majorant

$$
A(u)\le\sum_{\rm assgn}\lambda\,\mathbf 1_{D_1\mid u}\,
\mathbb E_{\rm mask}\mathbf 1_{\{l\nmid u\text{ for every banned }l\}},
$$

which concerns $u$ alone and is the manuscript's (7.27).

Fix an assignment and a mask. The integer $D_1$ is odd, because its entries are
primes at least $L^{20}$ and the exceptional integer, all of whose prime
factors exceed $W$. So $D_1\mid u$ and $mn=2u-1$ give

$$
mn\equiv-1\pmod{D_1}.
$$

For an odd prime $l\le x^\theta$ with $l\nmid D_1$ the bad events are
$mn\equiv0\pmod l$ when $l\le W$ (roughness of $m$ and $n$), and
$mn\equiv-1\pmod l$ when $l$ is banned, which is $l\mid u$ because $l$ is odd.
These residue sets are disjoint and contain $2l-1$ and $l-1$ pairs. Put
$\nu(l)=(2l-1)\mathbf 1_{l\le W}+(l-1)\mathbf 1_{l\text{ banned}}$ and
$g(l)=\nu(l)/l^2\le3/l$, bounded away from one for $l\ge3$. For a squarefree
product $d$ of these primes, the congruence modulo $D_1$ leaves, for each unit
$m\bmod D_1$, exactly one $n\bmod D_1$, also when $D_1$ has square factors; with
the Chinese remainder theorem there are exactly $\varphi(D_1)\nu(d)$ admissible
residue pairs modulo $D_1d$. Each pair has lattice count in the box equal to its
area term with error $O(1+(M_1+M_2)/(D_1d))$, so the remainders up to
$D=x^{10\theta}$ sum to

$$
\ll L^{O(1)}\bigl((M_1+M_2)D+D_1D^2\bigr)
\le L^{O(1)}\bigl((M_1+M_2)x^{1/20}+D_1x^{1/10}\bigr).
$$

The upper-bound block sieve with $h=2$ gives the main term
$\ll M_1M_2\,\varphi(D_1)D_1^{-2}\prod_l(1-g(l))$, the product over the odd
primes $l\le x^\theta$ not dividing $D_1$. A banned prime below $W$ has factor
$(1-1/l)(1-2/l)$ and a banned prime above $W$ has factor $1-1/l+1/l^2$, each at
most $(1-1/l)^{1+2\mathbf 1_{l\le W}}(1+O(l^{-2}))$; an allowed group prime
has factor $(1-1/l)^2$. Hence

$$
\prod_{\substack{3\le l\le x^\theta\\ l\nmid D_1}}(1-g(l))
\le CV(W)^2V(x^\theta)\prod_{l\mid D_1}(1-1/l)^{-3}
\prod_{\substack{p\text{ allowed}\\ p\nmid D_1}}(1-1/p)^{-1}.
$$

The product over $l\mid D_1$ is bounded, since those primes are at least
$L^{20}$ and $D_1\le x^{1/20}$, and the mask expectation of the last product is
$\prod_{p\nmid D_1}(1+q/(p-1))\le H_P$, the product over group primes, by the
manuscript's (7.6). Summing the main terms over assignments with
$\varphi(D_1)D_1^{-2}\le D_1^{-1}$ gives $\ll xV(W)^2V(x^\theta)H_Q^{\rm
mic}H_P\ll X_AV(W)^2$, and the remainders give $\ll x^{0.64}L^{O(1)}H_Q^{\rm
mic}=o(X_AV(W)^2)$, using $M_i\ll x^{0.54}$ and
$X_AV(W)^2\asymp xH_QH_P/L^2$. $\square$

There are $O(\kappa L+1)$ dyads for $m$ in $\mathcal B_\kappa$ and $O(1)$ for
$n$ given $m$, so the balanced composites contribute at most

$$
C_{\rm bal}(\kappa+L^{-1})\frac{X_A}L+o(X_A/L),
$$

with $C_{\rm bal}$ depending only on $\delta,r_0,\Psi,j',\theta$ and the group
geometry. The residue counts are those of the manuscript's (7.30)–(7.31): there
the congruences read $mn\equiv1$ modulo $D_1$ and modulo each banned prime, with
the same numbers of residue pairs.

## The count and Hypothesis A+

The choices are made in the manuscript's order.

1. Fix $\delta$, $\Psi$, $r_0$ and the band and group geometry; the finite
   prefix of bands used for the lower bound of $X_A$; then $j'$ and $\theta$;
   and $j_0$ covering both.
2. Fix $\kappa\in(0,1/50)$ with $C_{\rm bal}\kappa<\mathfrak S/4$, possible
   because $C_{\rm bal}$ does not depend on $\kappa$.
3. Fix $b_1$ small enough for the preliminary sieve and for the subtraction
   above; set $b_*=b_1/3$; fix $j_{**}$ with $c_2s'2^{-j_{**}}<b_*/4$; fix the
   bin mesh.
4. Fix the Type II saving $D_*$ so that every replacement error, after the
   dyadic sums, is $o(X_A/L)$. The Type II proof then fixes $K_0$, $D_0$ and,
   through (P), the discrepancy exponent $B$.
5. Fix $S>2B+3$ in Lemma 7.3 and the prime-number-theorem accuracies, and let
   $x\to\infty$.

The coefficient bound of the proxies does not depend on $S$, so step 5 does not
feed back into step 4. For all large real $x$,

$$
\sum_{2u-1\text{ prime}}A(u)\Psi(u/x)\ge\frac{\mathfrak SX_A}{2L}
-C_{\rm bal}\Bigl(\kappa+\frac1L\Bigr)\frac{X_A}L-o\Bigl(\frac{X_A}L\Bigr)
\ge\frac{\mathfrak SX_A}{5L}.
$$

After enlarging $C_w$ to absorb the fixed bound on $\Psi$, each summand is
at most $\exp(C_w\sqrt L)$. Since $X_A\ge c_AxL^{-C_A}$ and
$u\mapsto2u-1$ is injective, at least
$(\mathfrak Sc_A/5)\,xL^{-C_A-1}\exp(-C_w\sqrt L)$ distinct primes $p=2u-1$
occur. As $\Psi(u/x)\ne0$ forces $x\le u\le2x$, they satisfy $2x-1\le p\le4x-1$,
and $p+1=2u$ with every prime factor of $u$ at most $x^\delta$, so
$P^+(p+1)=\max(2,P^+(u))\le x^\delta$. This proves:

**Successor count**, assuming (P) and (E). For every fixed $0<\delta<1/4$
there are $c,C_A,C_w>0$ such that for all sufficiently large real $x$

$$
\#\{p\text{ prime}:\ 2x-1\le p\le4x-1,\ P^+(p+1)\le x^\delta\}
\ge c\,x(\log x)^{-C_A-1}\exp\bigl(-C_w\sqrt{\log x}\bigr).
$$

**Hypothesis A+**, assuming (P) and (E). Given $0<\delta<1/4$ and $\eta>0$, the
quantity $\eta L-(C_A+1)\log L-C_w\sqrt L+\log c$ tends to infinity, so the
successor count at $x=y$ gives at least $y^{1-\eta}$ primes $p\le4y-1<5y$ with
$P^+(p+1)\le y^\delta$, for every real $y$ beyond a threshold depending on
$\delta$ and $\eta$. No uniformity as $\delta\to0$ and no effective threshold
is claimed, and none is needed.

The counted primes lie inside the range $2x-2<p\le5x$ of Li and Zhuang's
Theorem 1.4, which states this count under the assumption that the manuscript's
argument is correct.
