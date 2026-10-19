---
name: research/leads/aliquot_collision_density/large_prime_class_average
title: The gcd-weighted average for the large-prime class
desc: |
  Exact local factors and a Brun–Titchmarsh compatibility argument bound the
  averaged sieve input G1 of the large-prime class, after removing few
  inputs, except for common divisors of s(a) and s(a') that divide a'-a and
  exceed every prime factor of both cofactors by a fixed power; that core
  is open.
created: 2026-10-17T04:12:41Z
updated: 2026-10-17T04:12:41Z
---

***

This is an author-recorded argument by Plasma AI for the gap G1 of the
[canonical collision sketch](_index.md#proof-sketch-of-the-corrected-route).
It is outside the independent examination of Theorems A and B. It computes
the local factors of the large-prime class exactly and bounds every part of
the G1 average except one regime of large common divisors, which it states
as an open estimate. Constants are not computed explicitly; the section
"Standing" lists exactly what is proved and what is open.

The external inputs are the Brun–Titchmarsh inequality, used in the form of
[[../library/primes/montgomery_vaughan_2006_multiplicative_number_theory_i/theorem_3_9|Montgomery and Vaughan's Theorem 3.9 with its error-free sharpening, valid for intervals of length at least twice the modulus]]
and read at statement depth; Mertens' theorems; and, in Lemma 0, the prime
number theorem for progressions to moduli at most $\log\log y$, in its
Siegel–Walfisz form. The latter is used as stated in
[Exercise 64 of Tao's 2014 Notes 2](https://terrytao.wordpress.com/2014/12/09/254a-notes-2-complex-analytic-multiplicative-number-theory/):
for each fixed $A>0$, the von Mangoldt sum in a reduced class modulo
$q\le\log^A t$ is $t/\varphi(q)+O(t\exp(-c_A\sqrt{\log t}))$.
This statement was read; its proof was not re-examined here. No numerical
effectivity of its constants is required.

## Setting

Use the notation of the canonical sketch. Fix $\delta>0$ and
$0<\eta<1/4$, put $y=x^{1/2-\eta}$, and consider cofactors $2\le a<y$, so
that every member of $S_1(x)$ is $aP$ with a prime $P>x^{1/2+\eta}$. For large
$x$ each such cofactor has $s(a)\ge\delta a/2$. For $a\ne a'$ write

$$
g=(s(a),s(a')),\qquad h=\sigma(a')-\sigma(a),\qquad
\beta=s(a')/g,\qquad \lambda=s(a)/g .
$$

The pair is *eligible* if $h\ne0$, $g\mid h$, both forms $P=u+\beta t$,
$P'=v+\lambda t$ are primitive, and $\omega(2)\le1$. The
[uniform sieve argument](uniform_two_form_sieve.md) gives
$N(a,a')\ll_\eta xg\,\mathfrak S_x(a,a')/(a\,s(a')\log^2x)$ for eligible
pairs and shows that the other pairs with $a\ne a'$ have no solutions.

This page works with a trimmed form of G1. A set $\mathcal B$ of cofactors
is removed first. The inputs $aP\le x$ with $a\in\mathcal B$ number at most
$(4x/\log x)\sum_{a\in\mathcal B,\,a<y}1/a$ for large $x$, because
$x/a>x^{1/2}$ and $\pi(t)\le2t/\log t$ for large $t$. So a set with
$\sum_{a\in\mathcal B,\,a<y}1/a\le\varepsilon'\log y$ removes at most
$2\varepsilon'x$ inputs. This suffices for statement 3 of Theorem B and
for the large-prime conclusion below. It does not prove G1 as stated for
every cofactor.

## Exact local factors

**Lemma 1.** Let $(a,a')$ be eligible and let $p$ be a prime. Put
$e_1=v_p(s(a))$, $e_2=v_p(s(a'))$, $e=\min(e_1,e_2)=v_p(g)$ and
$f=v_p(h)\ge e$. Then $e_1\ne e_2$ forces $f=e$, and the factor of
$g\,\mathfrak S_x(a,a')$ at $p\le x$ is

- $p^e\,p/(p-1)$ if $e_1\ne e_2$;
- $p^e\bigl(1-(p-1)^{-2}\bigr)$ if $e_1=e_2$ and $f=e$, which needs $p>2$;
- $p^e\,p/(p-1)$ if $e_1=e_2$ and $f>e$.

Conversely, a pair with $h\ne0$ and $g\mid h$ is ineligible exactly when some
prime has $e_1\ne e_2$ and $f>e$, or when $p=2$ has $e_1=e_2$ and $f=e$.

*Proof.* The forms satisfy $\lambda u-\beta v=h/g$, and
$v_p(\beta)=e_2-e$, $v_p(\lambda)=e_1-e$. If $e_1<e_2$, then $p\mid\beta$
and $p\nmid\lambda$, so $u+\beta t\equiv u$ and $\lambda u\equiv h/g$
modulo $p$. When $f>e$ this gives $p\mid u$, so every value of the first
form is divisible by $p$; it is not primitive, and since
$p\le\beta<x^{1/2+\eta}$ it has no prime value in range. When $f=e$ the
first form never vanishes modulo $p$ and the second has one root, so
$\omega(p)=1$ and the factor is $(1-1/p)(1-1/p)^{-2}=p/(p-1)$. The case
$e_1>e_2$ is symmetric. If $e_1=e_2$, then $p\nmid\beta\lambda$ and the two
roots $-u/\beta$, $-v/\lambda$ coincide modulo $p$ exactly when
$p\mid\lambda u-\beta v=h/g$, that is, when $f>e$. So $\omega(p)=1$ if
$f>e$ and $\omega(p)=2$ if $f=e$; the latter is the inadmissible case at
$p=2$. $\square$

Thus $g\,\mathfrak S_x(a,a')\le g\prod_{p\in T}p/(p-1)$, where $T$ is the
set of primes at which the third or first case occurs. Every prime of $T$
divides $\beta\lambda\,(h/g)$.

**Lemma 2.** If $v_p(\sigma(a))>v_p(a)$ and $v_p(\sigma(a'))>v_p(a')$, then
$e_1=v_p(a)$, $e_2=v_p(a')$ and $f>e$. Hence an eligible pair has
$v_p(a)=v_p(a')$, and its factor at $p$ is exactly $p^{v_p(a)}p/(p-1)$.

*Proof.* $v_p(s(a))=v_p(\sigma(a)-a)=v_p(a)$, and
$f\ge\min(v_p(\sigma(a)),v_p(\sigma(a')))\ge e+1$. Lemma 1 excludes
$e_1\ne e_2$ and gives the third case. $\square$

## Good cofactors

Let $L=\log\log y$ and $W=L/(4\log L)$, and fix $0<\nu<1/10$. For a cofactor
$a$ put $Q=P(a)$, $c=a/Q$, $Q_2=P(c)$ and $c_2=c/Q_2$, and write
$W(a)=\prod_{p\le W}p^{v_p(a)}$. Call $a$ *good* if

1. $Q>y^\nu$, $Q_2>y^\nu$, $Q\nmid c$ and $Q_2\nmid c_2$;
2. $v_p(\sigma(c))>v_p(c)$ for every prime $p\le W$;
3. $(a,\sigma(a))$ has no prime factor larger than $W$.

Then $a=c_2Q_2Q$ with pairwise coprime factors, and condition 2 implies
$v_p(\sigma(a))>v_p(a)$ for $p\le W$, since $\sigma(a)=\sigma(c)(Q+1)$ and
$v_p(a)=v_p(c)$. Condition 3 has two consequences used below. If $p>W$
divides $s(a)$, then $p\nmid a$ and $p\nmid\sigma(a)$; and $p\nmid s(c)$,
since otherwise $p\mid\sigma(c)$ by $s(a)=s(c)Q+\sigma(c)$, hence $p\mid c$,
and $p$ would divide both $a$ and $\sigma(a)$.

**Lemma 0 (density of good cofactors).** As $y\to\infty$, the cofactors
$2\le a<y$ that are not good satisfy
$\sum1/a\le\bigl(e^\gamma\nu(1+\log(1/\nu))+o(1)\bigr)\log y$.

*Proof.* Write $\mu(S)=\sum_{a\in S,\,a<y}1/a$, and use Euler products
throughout: for a nonnegative multiplicative $f$,
$\sum_{n<y}f(n)/n\le\prod_{q<y}\sum_{j\ge0}f(q^j)q^{-j}$.

Condition 1. The $a$ with $P(a)\le y^\nu$ have
$\mu\le\prod_{q\le y^\nu}(1-1/q)^{-1}=e^\gamma\nu\log y\,(1+o(1))$ by
Mertens' product theorem. Those with exactly one prime factor $q>y^\nu$
are $q^jm$ with $P(m)\le y^\nu$, so
$\mu\le\sum_{y^\nu<q\le y,\,j\ge1}q^{-j}\cdot e^\gamma\nu\log y\,(1+o(1))
=e^\gamma\nu(\log(1/\nu)+o(1))\log y$. Those divisible by $q^2$ for some
prime $q>y^\nu$ have $\mu\le(1+\log y)\sum_{q>y^\nu}q^{-2}=o(1)$. Every
remaining $a$ satisfies condition 1.

Condition 3. The $a$ divisible by a prime $p\in(W,L]$ have
$\mu\le(1+\log y)\sum_{W<p\le L}1/p=o(\log y)$, because
$\log W=\log L-\log(4\log L)$. For a prime $p>L$ with $p\mid a$ and
$p\mid\sigma(a)$, either $p^2\mid a$, costing $(1+\log y)/p^2$, or
$p\,\|\,a$ and some prime power $q^j\,\|\,a/p$ has $p\mid\sigma(q^j)$,
costing at most $(1+\log y)p^{-1}\sum_{q^j<y,\,p\mid\sigma(q^j)}q^{-j}$.
The terms with $j\ge2$ have $q^j\ge p/2$ and sum to $O(p^{-1/2})$. The
terms with $j=1$ have $q\equiv-1\pmod p$ and $q\ge2p-1$; the cited
Brun–Titchmarsh inequality and partial summation give
$\sum_{q<y,\,q\equiv-1\ (p)}1/q\le(2L+3)/(p-1)$. Summing over $p>L$ gives
$(1+\log y)\cdot O(1/\log L+L^{-1/2})=o(\log y)$.

Condition 2. For $a$ satisfying condition 1, the $a$ with a given $c$ have
weight $c^{-1}\sum_{P(c)<Q\le y/c}1/Q\le(\log(1/\nu)+o(1))/c$, since
$P(c)>y^\nu$. So it suffices to show that the $c<y$ violating condition 2
have $\sum1/c=o(\log y)$. Fix a prime $p\le W$, let $\mathcal P_p$ be the
primes $q\equiv-1\pmod p$ in $(W,y^\nu]$, and let $\omega_1(n)$ count the
primes of $\mathcal P_p$ dividing $n$ exactly once. Each of them contributes
at least $1$ to $v_p(\sigma(n))$. So if $c=p^kc_0$ with $p\nmid c_0$
violates the condition at $p$, then $\omega_1(c_0)\le k$. With
$z=1/2$, the Euler product bound and Mertens' product theorem give
$\sum_{n<y}z^{\omega_1(n)}/n\le e^\gamma\log y\,
\exp(-E_p/2+O(1/W))(1+o(1))$, where $E_p=\sum_{q\in\mathcal P_p}1/q$,
because each $q\in\mathcal P_p$ changes its Euler factor by the factor
$1-1/(2q)+O(q^{-2})$. Hence the violations with $v_p(c)=k$ have
$\sum1/c\le p^{-k}2^ke^\gamma\log y\,e^{-E_p/2}(1+o(1))$, and those with
$v_p(c)>k_0$ have $\sum1/c\le2(1+\log y)p^{-k_0-1}$. By the prime number
theorem for progressions to moduli at most $\log\log y$,
$E_p\ge(1-o(1))L/(p-1)\ge(4-o(1))\log L$ for $p\le W$. Take
the lower part of this estimate only from primes above $T_0=\exp(L^2)$:
partial summation of Siegel–Walfisz on $[T_0,y^\nu]$ gives
$(L-2\log L+\log\nu)/(p-1)+O(\exp(-cL))$, uniformly for $p\le W$,
which justifies the stated lower bound. Take
$k_0=\lceil2\log L\rceil$. For $p=2$ the first bound sums over $k\le k_0$
to $(k_0+1)e^{-E_2/2}\log y\,O(1)$, with $E_2\ge(1-o(1))L$; for $p\ge3$ it
sums to at most $3e^\gamma e^{-E_p/2}\log y\,(1+o(1))$. Summing over
$p\le W$ gives
$\bigl(k_0e^{-L/3}+\pi(W)L^{-2+o(1)}+2^{-k_0}\bigr)O(\log y)=o(\log y)$.
$\square$

## Compatibility

For an eligible pair of good cofactors, Lemma 2 forces $W(a)=W(a')$, and
then

$$
g\,\mathfrak S_x(a,a')\le W(a)\prod_{p\le W}\frac p{p-1}\cdot g'\cdot F,
\qquad
F=\prod_{\substack{p>W\\ p\mid\beta\lambda(h/g)}}\frac p{p-1},
$$

where $g'$ is the part of $g$ composed of primes above $W$.

**Lemma 3.** Let $(a,a')$ be an eligible pair of good cofactors and let
$d\ge1$ divide $g'$. Then:

1. $(s(c),d)=(c,d)=1$, and $Q\equiv q_c(d)\pmod d$, where
   $q_c(d)\equiv-\sigma(c)\,s(c)^{-1}\pmod d$; likewise for $a'$.
2. $d\mid a'-a$.
3. $d$ divides $\Delta'(c;a')=a'\,s(c)+c\,\sigma(c)$.
4. The polynomial $F_{c_2,a'}(t)=c_2\sigma(c_2)t^2+(c_2\sigma(c_2)+a's(c_2))t
   +a'\sigma(c_2)$ satisfies $F_{c_2,a'}(Q_2)=\Delta'(c;a')$, and it is
   nonzero modulo every prime $p\mid d$. Hence $Q_2$ lies in at most
   $2^{\omega(d)}$ residue classes modulo the radical of $d$.

*Proof.* Every prime of $d$ exceeds $W$ and divides $s(a)$, so the
consequences of condition 3 give the coprimality, and
$d\mid s(a)=s(c)Q+\sigma(c)$ gives the class of $Q$. Item 2 follows from
$s(a)-s(a')+h=a'-a$ and $d\mid g\mid h$. Then
$a'\equiv a=cQ\equiv-c\,\sigma(c)s(c)^{-1}\pmod d$, which is item 3. For
item 4, substitute $c=c_2t$, $\sigma(c)=\sigma(c_2)(t+1)$ and
$s(c)=s(c_2)t+\sigma(c_2)$. If all three coefficients vanished modulo $p$,
then $p\mid a's(c_2)$. If $p\mid a'$, then $p\mid\sigma(a')$ because
$p\mid s(a')$, against condition 3 for $a'$. Otherwise $p\mid s(c_2)$ and
$p\mid\sigma(c_2)$, so $p$ divides $c_2\mid a$ and
$\sigma(c_2)\mid\sigma(a)$, against condition 3 for $a$. A nonzero
polynomial of degree at most two has at most two roots modulo $p$, and
$Q_2$ is a root modulo each $p\mid d$ by item 3. $\square$

The point of item 4 is that the congruence $a\equiv a'\pmod d$ costs a
second prime of $a$, not only its largest one. The largest prime supplies
$d\mid s(a)$ and the second supplies the compatibility with $a'$.

**Lemma 6 (simple roots after a negligible removal).** Among good
cofactors, the ones for which some prime $p>W$ divides both $s(a)$ and
$Q-Q_2$ have total reciprocal weight

$$
\ll_\nu \frac{\log y}{W}
       +y^{-\nu/2}(1+\log y)^3=o(\log y).
$$

Call a good cofactor *separated* if it survives this removal. For an
eligible pair of separated good cofactors and every $d\mid g'$, the
admissible values of $Q_2$ lie in at most $2^{\omega(d)}$ classes modulo
$d$, not merely modulo its radical.

*Proof of the removal bound.* Put $c=a/Q$, so $c<y^{1-\nu}$, and let
$Q_2=P(c)$. A prime counted in the removal satisfies

$$
p\mid T(c):=s(c)Q_2+\sigma(c),\qquad Q\equiv Q_2\pmod p.
$$

The positive integer $T(c)$ is at most $2y^2(1+\log y)$ and has
$O(1+\log y)$ distinct prime factors. For $p>y^{\nu/2}$, a single
residue class modulo $p$, restricted to integers above $y^\nu$ and at
most $y$, has reciprocal sum at most
$y^{-\nu}+(1+\log y)/p$. Summing this bound over $p\mid T(c)$ and then
over $c$ with weight $1/c$ gives the second term of the assertion.
Primality is not needed for this part.

For $W<p\le y^{\nu/2}$ write $c=c_2Q_2$. Multiplicativity gives

$$
T(c)=s(c_2)Q_2^2+2\sigma(c_2)Q_2+\sigma(c_2).
$$

Since $p\mid s(a)$ and $a$ is good, $p\nmid a\sigma(a)$, and therefore
$p\nmid c_2\sigma(c_2)$. The displayed polynomial is nonzero modulo $p$
and has at most two roots. For fixed $c_2,p$, Brun–Titchmarsh and partial
summation bound the reciprocal sum over the allowed $Q_2>y^\nu$ by
$O_\nu(1/(p-1))$. For each such $Q_2$ the same bound applies to
$Q>y^\nu$ in its class modulo $p$. Both uses have
$p\le y^{\nu/2}$; the prime parameters are larger than $p^2$.
Dropping ordering and product restrictions only increases these positive
sums. The resulting bound is

$$
O_\nu(1+\log y)\sum_{p>W}\frac1{(p-1)^2}
\ll_\nu \frac{\log y}{W}.
$$

*Proof of the prime-power root bound.* Write $A=c_2$ and
$F(t)=F_{A,a'}(t)$ as in Lemma 3. The identities
$a'\equiv A Q_2Q\pmod d$ and

$$
s(a)=s(A)Q_2Q+\sigma(A)(Q_2+Q+1)\equiv0\pmod d
$$

give

$$
F'(Q_2)\equiv A\sigma(A)(Q_2-Q)\pmod d.
$$

Every factor on the right is a unit modulo $d$: the first two by
goodness, and the last by separation. Thus every root that can represent
a retained cofactor is simple modulo each prime dividing $d$. A simple
root modulo $p^j$ has exactly one lift modulo $p^{j+1}$, since
$F(t+p^j u)\equiv F(t)+p^j u F'(t)\pmod{p^{j+1}}$. There are at most two
simple roots modulo each $p$, and the Chinese remainder theorem gives
at most $2^{\omega(d)}$ classes modulo $d$. $\square$

The extra removal costs $o(x)$ inputs in $S_1(x)$ by the reciprocal-weight
estimate in "Setting". It does not assume that the large-prime part of
$s(a)$ is squarefree or cubefree. Proposition 4 below holds for all good
cofactors; the subsequent reductions of its remaining core use the
separated subset.

## The accessible divisors

Fix $0<\kappa<\nu/3$. Since $g'=\sum_{d\mid g'}\varphi(d)$, the G1 sum over
eligible pairs of good cofactors is at most

$$
\sum_{(a,a')}\frac{W(a)\prod_{p\le W}\frac p{p-1}\,F}{aa'}
\sum_{d\mid g'}\varphi(d).
$$

Call a divisor $d$ of $g'$ *accessible* for the pair if
$\max(P(a),P(a'))>d^{1/(1-\kappa)}$, and write $\Lambda_{\rm acc}$ and
$\Lambda_{\rm core}$ for the parts of this sum over accessible and
inaccessible $d$.

**Proposition 4.** $\Lambda_{\rm acc}\ll_{\nu,\kappa}\log^2y$.

*Main estimate.* Consider the divisors with $P(a)>d^{1/(1-\kappa)}$; the
case $P(a')>d^{1/(1-\kappa)}$ is symmetric. Fix a good $a'$ and $d\mid
s(a')$ composed of primes above $W$. By Lemma 3, the good $a=c_2Q_2Q$ with
$d\mid s(a)$, $a\equiv a'\pmod d$ and $Q>d^{1/(1-\kappa)}$ satisfy

$$
\sum\frac1a\le\sum_{c_2\le y}\frac1{c_2}
\sum_{\substack{Q_2>y^\nu\\ F_{c_2,a'}(Q_2)\equiv0\ (\mathrm{rad}\,d)}}
\frac1{Q_2}
\sum_{\substack{d^{1/(1-\kappa)}<Q\le y\\ Q\equiv q_c(d)\ (d)}}\frac1Q .
$$

If $(q_c(d),d)>1$, a prime $p\mid d$ divides $\sigma(c)$, and
$d\mid s(a)$ forces $Q=p<d^{1/(1-\kappa)}$; so the inner class is reduced
whenever it is nonempty. For $t\ge\max(y^\nu,d^{1/(1-\kappa)})$ we have
$t\ge2d$ for large $y$ and $\log(t/d)\ge\kappa\log t$, and the cited
Brun–Titchmarsh inequality gives
$\pi(t;d,b)\le2t/(\kappa\varphi(d)\log t)$. Partial summation from
$z\ge y^\nu$ to $Z\le y$ bounds the inner sum by $K_1/\varphi(d)$, with
$K_1=2(1+\log(1/\nu))/\kappa$.

Put $r=\mathrm{rad}\,d$. The $Q_2>r^{1/(1-\kappa)}$ in the at most
$2^{\omega(d)}$ classes contribute at most $2^{\omega(d)}K_1/\varphi(r)$ in
the same way; a class containing a multiple of a prime $p\mid r$ contains no
such prime. Each class contains at most $2r^{2\kappa}$ integers up to
$r^{1/(1-\kappa)}$, each above $y^\nu$. Therefore the $a$-sum is at most

$$
(1+\log y)\,2^{\omega(d)}
\Bigl(\frac{K_1}{\varphi(r)}+\frac{2r^{2\kappa}}{y^\nu}\Bigr)
\frac{K_1}{\varphi(d)} .
$$

Multiply by $\varphi(d)$, sum over $d\mid s(a')$ and then over $a'$ with
weight $1/a'$. The second term contributes at most
$y^{2\kappa-\nu+o(1)}$, because $d\le y\log y$ and
$\sum_{a'<y}\tau(s(a'))^2/a'\le y^{o(1)}$. The first term contributes
$K_1^2(1+\log y)\sum_{a'}\Phi(s(a'))/a'$, where

$$
\Phi(N)=\sum_{\substack{d\mid N\\ p\mid d\Rightarrow p>W}}
\frac{2^{\omega(d)}}{\varphi(\mathrm{rad}\,d)}
=\prod_{\substack{p^k\|N\\ p>W}}\Bigl(1+\frac{2k}{p-1}\Bigr)
=\sum_{e\mid N}\psi(e),
$$

with $\psi$ multiplicative, supported on integers whose primes exceed $W$,
and $\psi(p^j)=2/(p-1)$ for $j\ge1$. Swap the sums. For $e\le y^{\nu/2}$,
the good $a'=c'Q'$ with $e\mid s(a')$ have $Q'$ in one class modulo $e$,
reduced because otherwise $Q'$ would be a prime factor of $e$, and
$Q'>y^\nu\ge e^2$, so their weight is at most
$(1+\log y)K_1'/\varphi(e)$ with $K_1'$ depending only on $\nu$; and
$\sum_e\psi(e)/\varphi(e)\le\prod_{p>W}(1+O(p^{-2}))$. For $e>y^{\nu/2}$,
the primes $Q'>y^\nu$ of one residue class modulo $e$ have reciprocal sum
at most $y^{-\nu}+(1+\log y)/e$, because after the first of them the class
has one element in each interval of length $e$; so the weight is at most
$(1+\log y)(y^{-\nu}+(1+\log y)/e)$. Since
$\sum_{e\le y\log y}\psi(e)=y^{o(1)}$ and
$\sum_e\psi(e)e^{-1/2}\ll1$, these $e$ contribute $o(1)$. Hence
$\sum_{a'}\Phi(s(a'))/a'\ll\log y$, and the divisors with
$P(a)>d^{1/(1-\kappa)}$ contribute $O(\log^2y)$ before the weights
$W(a)\prod_{p\le W}p/(p-1)$ and $F$ are restored.

*Restoring the small-prime weight.* Restrict $c_2$ and $a'$ to
$W(c_2)=W(a')=w$; this is forced, because $W(a)=W(c_2)$ when $Q,Q_2>W$.
Writing $c_2=wm$ with $m$ free of primes up to $W$, the Euler product and
Mertens' product theorem give
$\sum_{c_2<y,\,W(c_2)=w}1/c_2\le w^{-1}\prod_{W<q<y}(1-1/q)^{-1}
=w^{-1}e^\gamma\log y\prod_{p\le W}(1-1/p)\,(1+o(1))$. The bounds for
$Q_2$ and $Q$ do not depend on $w$, and the same factor appears for $a'$
in every step of the $\Phi$ estimate. So the weight
$w\prod_{p\le W}p/(p-1)$ times the two factors $w^{-1}\prod_{p\le W}(1-1/p)$,
summed over $W$-smooth $w$, gives
$\prod_{p\le W}(1-1/p)\sum_w1/w=1$ times the unweighted bound.

*The singular-series weight.* Pointwise, $F\ll\log\log y$: the integer
$\beta\lambda h/g<y^4$ has $O(\log y)$ prime factors, and the product of
$p/(p-1)$ over the first $O(\log y)$ primes above $W$ is
$O(\log\log y/\log W)$. This suffices wherever a power saving is
available, in particular for the reductions of the core below. In the main
term $F$ must be averaged, as follows.

Put $Z_0=(\log y)^2$. Primes of $T$ above $Z_0$ contribute a factor
$1+o(1)$, since there are $O(\log y)$ of them. For $W<p\le Z_0$ let
$h_3(p)=(p/(p-1))^3-1\le7/p$. Every such prime of $T$ divides $s(a)$, or
$s(a')$, or $h$ while dividing neither $s(a)$ nor $s(a')$. By the
arithmetic–geometric mean inequality,

$$
F\le(1+o(1))\,\tfrac13\bigl(A(a)^3+A(a')^3+H^3\bigr),
$$

where $A(n)=\prod_{p\mid s(n),\,W<p\le Z_0}p/(p-1)$ and
$H=\prod_{p\mid h,\ p\nmid s(a)s(a'),\ W<p\le Z_0}p/(p-1)$. Expand each cube
as $\sum_eh_3(e)$ over squarefree $e$ with the indicated prime factors.

For $A(a')^3$: $\Phi(N)A(N)^3=\sum_{e\mid N}\psi_3(e)$ with $\psi_3$
multiplicative and $\psi_3(p^j)\ll1/p$, and the $\Phi$ estimate applies
unchanged.

For $A(a)^3$: a prime $p\mid e$ with $p\nmid d$ puts $Q$ in one class
modulo $p$, because $p\nmid s(c)$, and $p\mid\sigma(c)$ would force
$Q=p\le Z_0$. For $e\le E_0=y^{\kappa\nu/16}$, $Q$ then lies in one class
modulo $de$, and $\log E_0\le(\kappa/4)\log Q$ lets Brun–Titchmarsh give
$K_2/(\varphi(d)\varphi(e))$ in place of $K_1/\varphi(d)$, with $K_2$
depending on $\kappa,\nu$; and $\sum_eh_3(e)/\varphi(e)\ll1$. Primes
$p\mid e$ that divide $d$ impose nothing new and contribute
$\prod_{p\mid d}(1+7/p)$, which joins $\Phi$. For $e>E_0$, Rankin's trick
gives $\sum_{e\mid s(a),\,e>E_0}h_3(e)\le E_0^{-1/2}\prod_{p\le
Z_0}(1+7p^{-1/2})=y^{-\kappa\nu/32+o(1)}$.

For $H^3$: a prime $p\mid e$ divides $\sigma(a')-\sigma(a)$ but neither
$s(a)$ nor $s(a')$, so $p\nmid d$. If $p\nmid\sigma(c)$, then
$Q\equiv\sigma(a')\sigma(c)^{-1}-1\pmod p$, one class, handled as for
$A(a)^3$. If $p\mid\sigma(c)$, then $p\mid\sigma(a)$, so
$p\mid\sigma(a')=\sigma(c')(Q'+1)$. If moreover $p\nmid\sigma(c')$, then
$Q'\equiv-1\pmod p$, one class, absorbed by the Brun–Titchmarsh step for
$Q'$ in the $\Phi$ estimate. The remaining primes divide both
$\sigma(c)$ and $\sigma(c')$, and their factors multiply to at most
$G(c)G(c')$, where $G(n)=\prod_{p\mid\sigma(n),\,W<p\le Z_0}(1+7/p)^{1/2}$.

The weight $G$ has bounded mean. Since $\sigma(c)=\sigma(c_2)(Q_2+1)$,
$G(c)\le G(c_2)\prod_{p\mid Q_2+1,\,W<p\le Z_0}(1+7/p)^{1/2}$, and the
second factor expands into conditions $Q_2\equiv-1\pmod f$, absorbed by the
Brun–Titchmarsh step for $Q_2$.

Here the simultaneous congruences can be kept throughout the sums. A
prime dividing $d$ divides neither $\sigma(a)$ nor $\sigma(a')$ on the
good set. Thus the new moduli from $H$ and from $Q_2+1$ are coprime to
$d$. On the long $Q_2$ range in the main estimate, a modulus $f\le E_0$
therefore changes its root-class bound to
$O_{\nu,\kappa}(2^{\omega(d)}/(\varphi(r)\varphi(f)))$.
Indeed
$rf\le Q_2^{1-\kappa}y^{\kappa\nu/16}
\le Q_2^{1-15\kappa/16}$, and the Chinese remainder theorem combines
the polynomial roots modulo $r$ with the class $-1$ modulo $f$.
The short $Q_2$ range is already a power-saving error and can use the
pointwise polylogarithmic bound for $F$.

The primes assigned to a congruence on $Q$ multiply its original
modulus $d$ by at most $E_0$, with the same margin. The primes assigned
to $Q'\equiv-1$ multiply the small modulus
$e\le y^{\nu/2}$ in the $\Phi$ calculation by at most $E_0$.
These two moduli on $Q'$ are coprime: a common prime would divide both
$s(a')$ and $\sigma(a')$, contradicting goodness. Their product is at
most $Q'^{1/2+\kappa/16}$. All reciprocal prime sums consequently keep
their uniform Brun–Titchmarsh bounds, with the additional factors
$1/\varphi(f)$ for the added moduli. Summing their nonnegative expansion
coefficients converges, since each new prime contributes $O(p^{-2})$.
For any added modulus above $E_0$, the same Rankin bound as for
$A(a)^3$ is a negative power of $y$ times $y^{o(1)}$; pointwise
polylogarithmic bounds handle the other weights. This also covers the
large-$e$ remainder of the $\Phi$ calculation.

For $c_2=wm$ with $m$ free of primes up to
$W$, $G(c_2)\le G(w)G(m)$, and the Euler product gives
$\sum_{m<y}G(m)/m\le\prod_{W<q<y}(1-1/q)^{-1}
\exp\bigl(\sum_q(g(q)-1)/q+O(1/W)\bigr)$ with
$g(q)=\prod_{p\mid q+1,\,W<p\le Z_0}(1+7/p)^{1/2}=\sum_{f\mid q+1}\xi(f)$,
where $\xi$ is multiplicative on squarefree $f$ with primes in $(W,Z_0]$
and $\xi(p)\le4/p$. The partial summation of Lemma 0 gives
$\sum_{q<y,\,q\equiv-1\ (f)}1/q\le(2L+5)/\varphi(f)$ for $f\le y^{1/2}$,
and the trivial bound $2\log y/f$ holds for larger $f$. Hence
$\sum_q(g(q)-1)/q\le(2L+5)\sum_{f>1}\xi(f)/\varphi(f)+o(1)
=O(L/(W\log W))=O(1)$. The same applies to $c'$ on the $a'$-side. Finally
$\sum_wG(w)^2/w\le(1+o(1))\prod_{p\le W}(1-1/p)^{-1}$ over $W$-smooth $w$,
because $\sigma(p^k)<p^{k+1}$ has at most $(k+1)\log p/\log W$ prime factors
above $W$. So the factors $G(w)^2$ cost $1+o(1)$ against $\sum_w1/w$.
Large moduli $e$ and $f$ are removed by Rankin's trick as above. Hence the
main estimate holds with the weight $F$, up to a constant factor depending
on $\nu$ and $\kappa$. $\square$

## The open core

The remaining part is

$$
\Lambda_{\rm core}
=\sum_{(a,a')}\frac{W(a)\prod_{p\le W}\frac p{p-1}\,F}{aa'}
\sum_{\substack{d\mid g'\\ d^{1/(1-\kappa)}\ge\max(P(a),P(a'))}}
\varphi(d),
$$

Here and throughout this section the sum is restricted to eligible pairs
of separated good cofactors. The discarded reciprocal weight is still
at most the bound in Lemma 0 plus $o(\log y)$.
We have $d>y^{\nu(1-\kappa)}$, and
$d\le\min(|a'-a|,s(a),s(a'))<y$. When $d>P(a)$, item 1 of Lemma 3 pins the
largest prime of $a$:

$$
P(a)\ \text{is the least positive residue of}\ -\sigma(c)\,s(c)^{-1}
\pmod d ,
$$

and likewise for $a'$. So the core counts pairs of cofactors whose values
of $s$ share a divisor that also divides their difference and is nearly as
large as every prime factor of either cofactor; when it exceeds them, each
largest prime is a least residue of a modular fraction formed from the rest
of its cofactor.

**A narrower core.** Fix $\kappa''>0$ with $2\kappa+\kappa''<\nu$.
Fix $a'$ and $d\mid s(a')$. Lemma 6 puts $Q_2$ in at most
$2^{\omega(d)}$ classes modulo $d$, and the primes above $y^\nu$ in one
class have reciprocal sum at most $y^{-\nu}+(1+\log y)/d$.

If $Q=P(a)\ge d^{1-\kappa''}$, then $Q\le d^{1/(1-\kappa)}$ lies in one
class modulo $d$, so at most $2d^{2\kappa}$ values occur, each with
$1/Q\le d^{\kappa''-1}$. After the factor $\varphi(d)\le d$ and the sum over
$c_2$, the $a$-sum is at most
$(1+\log y)2^{\omega(d)+1}d^{2\kappa+\kappa''}
(y^{-\nu}+(1+\log y)d^{-1})$.
Since $y^{\nu(1-\kappa)}\le d\le y\log y$, summing over $d\mid s(a')$ and
over $a'$ gives $y^{-c+o(1)}$ for some $c=c(\nu,\kappa,\kappa'')>0$.

**Lemma 5.** Let $c,c'\ge2$ satisfy $v_p(\sigma(c))>v_p(c)$ and
$v_p(\sigma(c'))>v_p(c')$ for every prime $p\le W$, let $(c,\sigma(c))$ and
$(c',\sigma(c'))$ have no prime factor above $W$, and let $W(c)=W(c')$. If
$c\ne c'$, then $\Delta(c,c')=c\,\sigma(c)s(c')-c'\sigma(c')s(c)\ne0$. The
hypotheses hold for $c=a/P(a)$ and $c'=a'/P(a')$ when $a,a'$ are good and
$W(a)=W(a')$.

*Proof.* $\Delta(c,c')=0$ means $c+c^2/s(c)=c'+c'^2/s(c')$. The first
hypothesis gives $v_p(s(c))=v_p(c)$ for $p\le W$, and by the second no prime
above $W$ divides both $c$ and $s(c)$. So $(c^2,s(c))=W(c)$, and
$(c^2/W(c))/(s(c)/W(c))$ is $c^2/s(c)$ in lowest terms. Two rationals that
differ by an integer have the same reduced denominator, so
$s(c)/W(c)=s(c')/W(c')$, and $W(c)=W(a)=W(a')=W(c')$ gives $s(c)=s(c')$.
Since $t\mapsto t+t^2/s$ is increasing for $s>0$, $c=c'$. For good
cofactors, condition 2 is the first hypothesis, condition 3 gives the
second because $c\mid a$ and $\sigma(c)\mid\sigma(a)$, and $W(c)=W(a)$
because $P(a)>W$. $\square$

**Both largest primes below $d$.** If $P(a),P(a')<d$, then each is the
least positive residue of its class, so $c\ne c'$ (otherwise $a=a'$), the
pair is determined by $(c,c',d)$, and $d\mid\Delta(c,c')$, which follows
from item 3 of Lemma 3 after multiplying by $s(c')$. Lemma 5 makes
$\Delta(c,c')$ a nonzero integer of size $y^{O(1)}$, so it has $y^{o(1)}$
divisors. Hence the pairs with $P(a)P(a')\ge d^{1+\epsilon}$ contribute at
most $\sum_{c,c'}(cc')^{-1}\sum_{d\mid\Delta(c,c')}d^{-\epsilon}$ over
$d\ge y^{\nu(1-\kappa)}$, which is $y^{-c+o(1)}$. Since
$P(a)P(a')>y^{2\nu}$, this covers every such pair with
$d\le y^{2\nu/(1+\epsilon)}$.

**Two large primes on one side.** If $P(a)<d$ and
$P(a)P_2(a)\ge d^{1+\epsilon}$, fix $a'$
and $d\mid s(a')$ and restrict $Q$ and $Q_2$ to dyadic ranges $[R,2R)$ and
$[R_2,2R_2)$ with $RR_2\ge d^{1+\epsilon}/4$. Then $Q$ is determined by
$(c_2,Q_2)$, and $Q_2$ takes at most $2^{\omega(d)}(R_2/d+1)$ values, so
$\sum1/(QQ_2)\le2^{\omega(d)}(1/(dR)+1/(RR_2))\le2^{\omega(d)+3}
d^{-1-\epsilon/2}$, using $R\ge(RR_2/2)^{1/2}$. After the factor $\varphi(d)$,
the sums over $c_2$, the dyadic ranges, $d\mid s(a')$ and $a'$ give
$y^{-c+o(1)}$. The same holds with $a$ and $a'$ exchanged.

These parts contribute $o(1)$, also with the weights restored: the
small-prime weight as in Proposition 4, and $F$ through its pointwise bound
$F\ll\log\log y$ against the power savings. What remains consists of
divisors exceeding $P(a)^{1/(1-\kappa'')}$ and
$P(a')^{1/(1-\kappa'')}$, for which the two largest of
$P(a),P_2(a),P(a'),P_2(a')$ have product below $d^{1+\epsilon}$.
Necessarily $d>y^{2\nu/(1+\epsilon)}$. Both largest primes are least
residues of their classes, determined by the rest of their cofactors.
There is no restriction on the radical of $d$: Lemma 6 supplies the
prime-power root count for all retained pairs.

**Gap G1-core.** Prove $\Lambda_{\rm core}\ll\log^2y$ for fixed small
$\nu$ and $\kappa$. By the reductions above it suffices to bound the
remaining regime, with its weights. In a model where $s(a)$ and $s(a')$ are independent of
$a$ and $a'$ modulo large $d$, the inner condition has probability about
$d^{-3}$, and the core is $O(y^{-\nu/2}\log^2y)$. No such independence is
proved. The estimate is therefore expected but unknown: it is supported only
by that model, and no source read here supplies it.

The tools above stop exactly here. Brun–Titchmarsh needs a free prime whose
range exceeds the modulus $d$, and in the core no prime of either cofactor
has that range. Enumerating $d$ as a divisor of one value of $s$ and
bounding the progression $a'\equiv a\pmod d$ trivially loses the factor
$d$ that the condition $d\mid s(a')$ should supply; the result is too large
by about the average number of divisors of $s(a)$ above $y^{\nu/2}$. The
two-dimensional large sieve bounds the
total variance of $(a,\sigma(a))$ over all residue pairs modulo $d$, but
that variance may sit on the diagonal residues $a\equiv\sigma(a)$ counted
here, and it reaches only $d$ up to about $y^{1/2}$. A proof must show
that these least residues fall in short initial intervals no more often
than their length predicts, on average over the pairs.

**Lemma 7 (separation of bounded reduced ratios).** Put
$\Pi_W=\prod_{p\le W}p$ and $C_\delta=1+2/\delta$. For an eligible pair of
good cofactors in $\mathcal A_\delta(y)$, let
$u=s(a)/g$, $v=s(a')/g$ and $H=h/g$. Then

$$
\Pi_W\mid H,\qquad
0<|H|<C_\delta\max(u,v),\qquad
(uv,\Pi_W)=1.
$$

In particular $\max(u,v)>\Pi_W/C_\delta$. For every fixed $K$, no such
pair has $\max(u,v)\le K$ for sufficiently large $y$. This includes
$s(a)=s(a')$, for which $u=v=1$.

*Proof.* At every $p\le W$, Lemma 2 gives
$v_p(s(a))=v_p(s(a'))=v_p(g)$ and $v_p(h)>v_p(g)$. This proves the
divisibility and coprimality. Also
$\sigma(a)\le C_\delta s(a)$ and
$\sigma(a')\le C_\delta s(a')$, while both divisor sums are positive.
Consequently
$0<|h|<\max(\sigma(a),\sigma(a'))\le
C_\delta g\max(u,v)$. Finally $W\to\infty$, so $\Pi_W\to\infty$.
$\square$

The core is a scaled collision problem at the cofactor scale. For a core divisor
$d$ put $\lambda=s(a)/d$ and $\lambda'=s(a')/d$. Then

$$
\lambda'\,s(a)=\lambda\,s(a'),\qquad a'\equiv a\pmod{s(a)/\lambda},\qquad
\lambda\le\frac{s(a)}{P(a)^{1-\kappa}}\le\frac{(1+\log y)\,a}{P(a)^{1-\kappa}},
$$

and likewise for $\lambda'$. These coefficients have size at most
$y^{1-\nu/2}$ for large $y$. Lemma 7 excludes bounded coefficients after
their common factor is cancelled; in particular ordinary cofactor
collisions contribute no eligible pair once $y$ is large. An induction
using only ordinary fiber sizes therefore has no supplied bridge to this
core. It needs a bound for the displayed weighted scaled collisions with
unbounded reduced coefficients and with the extra congruence retained.

Removing the largest prime does not close that induction by itself:
substitution of $a=cQ$ and $a'=c'Q'$ changes the scaled equality to

$$
\lambda'(Q+1)s(c)-\lambda(Q'+1)s(c')
=\lambda c'-\lambda'c.
$$

The right side need not vanish, and the new coefficients depend on the
removed primes. Thus the zero-right-side scaled equality alone is not an
invariant induction hypothesis. A successful descent must control these
affine equations, their congruence constraints and their summed weights;
no contracting recurrence is established here.

Luca and Pomerance avoid this regime in the proof of their
[[../library/arithmetic_functions/luca_pomerance_2015_range_sum_of_proper_divisors_function/theorem_1|positive-density range theorem]]
(15-page preprint, Section 3.1). Their cofactors are $m=q\ell$ with
$\ell\le x^{1/10}$, and a common divisor $h$ of $s(m)$ and $s(m')$ divides
$\ell\sigma(\ell)s(\ell')-\ell'\sigma(\ell')s(\ell)$, the analogue of
$\Delta'$ with both cofactors decomposed. That integer is smaller than
$2x^{3/10}$ in absolute value, so a divisor $h>x^{1/3}$ forces it to
vanish, and the gcd properties of their Lemma 1 then force $\ell=\ell'$.
For general cofactors the analogous integer has size up to about $y^3$,
and no such forcing occurs.

## Consequence for the large-prime class

G0, Proposition 4 and the core estimate together give, for each
$\varepsilon>0$ and the corresponding removal of at most $\varepsilon x$
inputs, $C_{S_1}(x)\ll_{\delta,\eta,\varepsilon}x$ for the remaining
inputs. With the truncation argument of Theorem B this would show that for
every set $A$ of density zero, the $n\le x$ with $s(n)\in A$ and
$P(n)>x^{1/2+\eta}$ number $o(x)$, and hence that $s^{-1}(A)$ has upper
density at most $1-\log2$. This conclusion is conditional on Gap
G1-core; it is not proved here.

## Standing

Proved here, author-recorded: Lemmas 0, 1, 2, 3, 5, 6 and 7; Proposition 4,
including both weights; and the stated reductions of the core on
separated good cofactors. Constants were not computed explicitly; each step records the
inequality it uses.

Open: Gap G1-core in the remaining large-modulus regime. Nothing on this page is
independently reviewed, and the trimmed estimate it targets is not G1 as
stated for every cofactor.
