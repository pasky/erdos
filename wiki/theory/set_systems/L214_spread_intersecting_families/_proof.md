---
name: theory/set_systems/L214_spread_intersecting_families/_proof
title: Proof that intersecting families can be arbitrarily spread
desc: |
  Substitution powers have an exactly computable spread; the two-star block
  family with m = rho^rho halves the excess at every level, and a random
  subfamily turns the normalized spread into the absolute form.
created: 2026-10-15T17:54:12Z
updated: 2026-10-15T17:54:12Z
---

***

## Conventions

Families, the subfamily $\mathcal F_T$ of members containing $T$, intersecting
families, the block family $B(\rho,m)$ and the substitution $G[H]$ are as in the
[[theory/set_systems/L214_spread_intersecting_families/_index|statement of L214]].
The families used below are nonempty, and their uniformities are positive.
For a family $\mathcal F$, $S$ denotes a uniformly random member, so that
$\Pr[T\subseteq S]=|\mathcal F_T|/|\mathcal F|$. For a real $R>0$ the
**excess** of $\mathcal F$ at $R$ is

$$
E_{\mathcal F}(R)=\max_{T\neq\varnothing}\Pr[T\subseteq S]\,R^{|T|},
$$

the maximum over nonempty subsets $T$ of the ground set; it is positive and
attained. Call $\mathcal F$ **normalized $R$-spread** when
$E_{\mathcal F}(R)\le1$, that is, when $|\mathcal F_T|\le R^{-|T|}|\mathcal F|$
for every nonempty $T$. If $\mathcal F$ consists of $n$-sets, taking $T$ to be a
member gives $|\mathcal F|\ge R^n$. The **absolute** form used by
Bell–Chueluecha–Warnke and by Rao asks instead $|\mathcal F_T|\le R^{n-|T|}$.

For an $a$-uniform family $G$ on $V$ and a real $E>0$ put

$$
\psi_G(E)=\max_{\varnothing\neq I\subseteq V}\Pr[I\subseteq A]\,E^{|I|},
$$

where $A$ is a uniformly random member of $G$. Thus $\psi_G(R)=E_G(R)$, and
$\psi_G$ is nondecreasing.

## Substitution

**Lemma 1.** Let $G$ be an $a$-uniform family on $V$ and $H$ a $b$-uniform
family on $U$. The map sending $A\in G$ and $(S_i)_{i\in A}$ with $S_i\in H$ to
$\bigcup_{i\in A}\{i\}\times S_i$ is a bijection onto $G[H]$. Hence $G[H]$ is
$ab$-uniform with $|G[H]|=|G|\,|H|^a$, and a uniformly random member of $G[H]$
is obtained from a uniformly random $A\in G$ and independent uniformly random
$S_i\in H$. If $G$ and $H$ are intersecting, so is $G[H]$.

*Proof.* A member determines $A$ as its projection to $V$ and $S_i$ as its fiber
over $i\in A$, so the map is injective; the other assertions follow, since the
fibers are disjoint $b$-sets and every $A$ has $|H|^a$ preimage tuples. If two
members have root sets $A,A'$, pick $i\in A\cap A'$; their fibers over $i$ are
members of $H$ and share a point $u$, so both members contain $(i,u)$. $\square$

For $a\ge2$, iterating gives an $a^h$-uniform family $G^h$ with
$|G^h|=|G|^{(a^h-1)/(a-1)}$, from $|G^{h+1}|=|G|\,|G^h|^a$, and it is
intersecting when $G$ is.

**Lemma 2 (exact spread recursion).** For $G$ and $H$ as in Lemma 1 and every
$R>0$,

$$
E_{G[H]}(R)=\psi_G\bigl(E_H(R)\bigr).
$$

Consequently $E_{G^h}(R)=\psi_G^{(h)}(R)$, the $h$-fold iterate of $\psi_G$.

*Proof.* Let $T\subseteq V\times U$ be nonempty, let $I$ be its projection to
$V$ and, for $i\in I$, let $T_i\ne\varnothing$ be its fiber over $i$. A member
$\bigcup_{i\in A}\{i\}\times S_i$ contains $T$ exactly when $I\subseteq A$ and
$T_i\subseteq S_i$ for every $i\in I$. By the independence in Lemma 1,

$$
\Pr[T\subseteq S]\,R^{|T|}
=\Pr[I\subseteq A]\prod_{i\in I}\Bigl(\Pr[T_i\subseteq S_i]\,R^{|T_i|}\Bigr)
\le\Pr[I\subseteq A]\,E_H(R)^{|I|}\le\psi_G\bigl(E_H(R)\bigr).
$$

Conversely, choose $I$ attaining the maximum in $\psi_G(E_H(R))$ and, for each
$i\in I$, a set $T_i$ attaining $E_H(R)$; the set
$T=\bigcup_{i\in I}\{i\}\times T_i$ gives equality throughout. For the
consequence, $E_{G^1}(R)=E_G(R)=\psi_G(R)$ and $G^{h+1}=G[G^h]$. $\square$

## The block family

**Lemma 3.** Let $\rho\ge2$ and $m\ge\rho$ be integers, $B=B(\rho,m)$,
$\kappa=m\rho^{-\rho}$ and $\varphi=\max(1,\kappa)/(1+\kappa)$. Then $B$ is an
intersecting family of $(m+1)$-sets with $|B|=\rho^m(1+\kappa)$, and for every
nonempty set $I$,

$$
\Pr[I\subseteq A]\le\varphi\,\rho^{1-|I|},
$$

with equality for $I=\{x\}$ when $\kappa\le1$ and for $I=\{z\}$ when
$\kappa\ge1$. Hence $\psi_B(E)\le\varphi E$ for $0<E\le\rho$.

*Proof.* Call the members $\{x\}\cup T$ of the first kind and the members
$\{z\}\cup Y_i\cup W$ of the second kind; there are $\rho^m$ and
$m\rho^{m-\rho}=\kappa\rho^m$ of them. Each has $m+1$ points. Two members of the
first kind share $x$, two of the second kind share $z$, and $\{x\}\cup T$ meets
$\{z\}\cup Y_i\cup W$ in the point of $T$ on $Y_i$; so $B$ is intersecting. Let
$I$ be nonempty and contained in some member, since otherwise the probability
is $0$, and divide the counts below by $|B|=\rho^m(1+\kappa)$.

*$I$ lies in a member of the first kind.* Then $I\setminus\{x\}$ meets each
$Y_i$ in at most one point. If $x\in I$, exactly $\rho^{m-|I|+1}$ members
contain $I$, all of the first kind, and the probability is
$\rho^{1-|I|}/(1+\kappa)$. If $x\notin I$, then $\rho^{m-|I|}$ members of the
first kind contain $I$; a member of the second kind contains $I$ only if
$I\subseteq Y_i$ for some $i$, which here forces $|I|=1$, and then
$\rho^{m-\rho}$ of them do. The probability is $\rho^{-|I|}/(1+\kappa)$ when
$|I|\ge2$ and $(\rho^{-1}+\rho^{-\rho})/(1+\kappa)<1/(1+\kappa)$ when $|I|=1$.

*$I$ lies only in members of the second kind.* Write
$I=I_z\cup I_Y\cup I_W$ with $I_z\subseteq\{z\}$, $I_Y\subseteq Y_i$ for a
single $i$ and $I_W$ meeting each $Y'_j$ in at most one point. If
$I_Y\ne\varnothing$, the members containing $I$ are those with this $i$ and
$W\supseteq I_W$, so the probability is $\rho^{-\rho-|I_W|}/(1+\kappa)$; as
$|I|\le1+\rho+|I_W|$, this is at most $\rho^{1-|I|}/(1+\kappa)$. If
$I_Y=\varnothing$, any $i$ is allowed and the probability is
$\kappa\rho^{-|I_W|}/(1+\kappa)$; as $|I_W|\ge|I|-1$, this is at most
$\kappa\rho^{1-|I|}/(1+\kappa)$.

In every case the probability is at most $\varphi\rho^{1-|I|}$. The singletons
$\{x\}$ and $\{z\}$ have probabilities $1/(1+\kappa)$ and $\kappa/(1+\kappa)$,
which gives the equality cases. Finally, for $0<E\le\rho$,

$$
\psi_B(E)\le\max_{t\ge1}\varphi\rho^{1-t}E^t
=\varphi E\max_{t\ge1}\Bigl(\frac E\rho\Bigr)^{t-1}=\varphi E.
\qquad\square
$$

## Proof of the first part

Take $m=\rho^\rho$, so $\kappa=1$ and $\varphi=1/2$, and let
$h=\lceil\log_2\rho\rceil$. By Lemma 3, $\psi_B(E)\le E/2$ for $0<E\le\rho$, and
the values stay in that range, so by Lemma 2

$$
E_{B^h}(\rho)=\psi_B^{(h)}(\rho)\le2^{-h}\rho\le1 .
$$

Thus $\mathcal F=B(\rho,\rho^\rho)^h$ satisfies
$|\mathcal F_T|\le\rho^{-|T|}|\mathcal F|$ for every nonempty $T$, and
$|\mathcal F|\ge\rho^n$. It is an intersecting family of $n$-sets with
$n=(\rho^\rho+1)^h$ by Lemmas 1 and 3; in particular no two of its members are
disjoint.

The same argument proves the general form: if $m\ge\rho$ and
$\varphi(\rho,m)^h\rho\le1$, then $B(\rho,m)^h$ is normalized $\rho$-spread. For
example $B(2,2)^2$, with $\varphi=2/3$, is normalized $2$-spread.

## Random thinning: proof of the second part

**Lemma 4.** Let $n\ge2$, let $\mathcal F$ be a normalized $\rho$-spread
family of $n$-sets with $|\mathcal F|\le(2\rho)^n$, and let $r$ be a real
number with $16\le r\le\rho/16$ and $r\ge2\ln(4\rho)+2$. Then $\mathcal F$ has
a subfamily $\mathcal F'$ with $|\mathcal F'|>r^n$ and
$|\mathcal F'_T|\le r^{n-|T|}$ for every nonempty set $T$.

*Proof.* Since $|\mathcal F|\ge\rho^n\ge16^nr^n$, the number
$q=2r^n/|\mathcal F|$ lies in $(0,1)$. Keep each member of $\mathcal F$
independently with probability $q$, and call the result $\mathcal F'$.

The size $|\mathcal F'|$ is binomial with mean $2r^n$, so by the Chernoff bound
$\Pr[|\mathcal F'|\le r^n]\le e^{-r^n/4}<1/2$.

Fix $T$ with $1\le t=|T|\le n-1$ and $\mathcal F_T\ne\varnothing$. Then
$X=|\mathcal F'_T|$ is binomial with mean $\mu=q|\mathcal F_T|\le2r^n\rho^{-t}$.
Let $\ell=\lfloor r^{n-t}\rfloor+1$, the least integer exceeding $r^{n-t}$. By
the union bound over $\ell$-subsets of $\mathcal F_T$,

$$
\Pr[X>r^{n-t}]=\Pr[X\ge\ell]\le\binom{|\mathcal F_T|}{\ell}q^\ell
\le\Bigl(\frac{e\mu}{\ell}\Bigr)^\ell
\le\bigl(2e(r/\rho)^t\bigr)^\ell\le\bigl(2e\cdot16^{-t}\bigr)^\ell
\le\Bigl(\frac{2e}{16}\Bigr)^{t\ell},
$$

using $\ell>r^{n-t}$ in the third step and $2e\le(2e)^t$ in the last. Put
$c_0=\ln(8/e)>1.079$, so the bound is $e^{-c_0t\ell}$. Since $\ell\ge r^{n-t}$
and $t\,r^{n-t}\ge(t+1)\,r^{n-t-1}$ for $r\ge2$, the product $t\ell$ is at least
$(n-1)r$. A set $T$ with $\mathcal F_T\ne\varnothing$ lies in a member, so at
most $|\mathcal F|\,2^n\le(4\rho)^n$ sets $T$ of these sizes occur. Every other
nonempty $T$ is harmless: $|\mathcal F'_T|\le1=r^0$ when $|T|=n$, and
$\mathcal F'_T=\varnothing$ when $\mathcal F_T=\varnothing$. Hence, using
$n-1\ge n/2$,

$$
\Pr\bigl[\exists T:\ |\mathcal F'_T|>r^{n-|T|}\bigr]
\le(4\rho)^n e^{-c_0(n-1)r}
\le\exp\Bigl(-n\Bigl(\frac{c_0r}{2}-\ln(4\rho)\Bigr)\Bigr)\le e^{-n}<\frac12,
$$

because $c_0r/2>r/2\cdot1.079\ge\ln(4\rho)+1$ when $r\ge2\ln(4\rho)+2$. With
positive probability neither bad event occurs. $\square$

Now let $r\ge16$ and $\rho=\lceil16r\rceil$, so $\rho\ge256$ and
$r\le\rho/16$. The function $r-2\ln(64r+4)-2$ is increasing for $r\ge16$ and
positive at $r=16$, where it equals $16-2\ln1028-2>0.12$; since
$4\rho\le64r+4$, this gives $r\ge2\ln(4\rho)+2$. The family $\mathcal F$ of the
first part for this $\rho$ is normalized $\rho$-spread, and with $m=\rho^\rho$,
$|\mathcal F|=(2\rho^m)^{(n-1)/m}=2^{(n-1)/m}\rho^{n-1}\le(2\rho)^n$. Lemma 4
gives the required $\mathcal F'$, which is intersecting as a subfamily of an
intersecting family. $\square$

## Remarks on the parameters

With $\rho=2$ the family is $B(2,4)$ itself: $32=2^5$ sets of size $5$, every
nonempty $T$ in at most $2^{5-|T|}$ of them. With $\rho=3$ it is
$B(3,27)^2$, of uniformity $784$. In general

$$
\log_2n=\lceil\log_2\rho\rceil\log_2(\rho^\rho+1)=(1+o(1))\,\rho(\log_2\rho)^2,
$$

so along these $n$ the spread is $\rho=(1+o(1))\log_2n/(\log_2\log_2n)^2$ in the
normalized form, and $r=\rho/16$ up to rounding in the absolute form. The
excess halves at each level because both centers $x$ and $z$ lie in exactly half
of the members; the number $m=\rho^\rho$ of blocks is what makes a whole block
$Y_i$, which a member of the second kind must contain, as rare as $\rho$-spread
requires.
