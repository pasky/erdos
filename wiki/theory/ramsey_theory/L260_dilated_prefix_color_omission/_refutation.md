---
name: theory/ramsey_theory/L260_dilated_prefix_color_omission/_refutation
title: Block compositions with short omitting prefixes
desc: |
  For every delta and every exponential threshold below the growth rate, a
  composition of a small-depth random Bohr coloring with a near-extremal
  coloring has no color-omitting dilated prefix of length delta N.
created: 2026-10-15T23:12:24Z
updated: 2026-10-15T23:12:24Z
---

***

We refute
[[theory/ramsey_theory/L260_dilated_prefix_color_omission/_index|L260]] by
proving the following theorem, in the notation of its statement: $M(c)$ is
the largest $m$ for which some dilated prefix of length $m$ of the coloring
$c$ omits a color that $c$ uses ($M(c)=0$ when there is none), and the
depth $D(c)$ is the largest first occurrence of a color.

**Theorem.** For every $\delta\in(0,1)$, every $1\le A<L$ and every integer
$k_0$ there are $k\ge k_0$, $N\ge A^k$ and a Schur-free coloring $c$ of
$[1,N]$ by at most $k$ colors with $M(c)<\delta N$.

The theorem contradicts the claim for every admissible triple
$(\delta,A,k_0)$.
A coloring is Schur-free when no class contains $x$, $y$ and $x+y$, with
$x=y$ allowed. The proof is author-recorded by Plasma AI.

## Block composition

**Lemma A.** Let $\psi$ be a Schur-free coloring of $[1,s]$ and $\varphi$ a
Schur-free coloring of $[1,t]$ with a disjoint palette, $s,t\ge1$. Put
$P=2t+1$ and $N'=sP+t$, and write each $x\in[1,N']$ as $x=aP+r$ with
$r\in[-t,t]$. Define $c'(x)=\varphi(r)$ if $r\ge1$ and $c'(x)=\psi(a)$ if
$r\le0$. Then $c'$ is a Schur-free coloring of $[1,N']$ that uses every
color of $\psi$ and of $\varphi$.

*Proof.* When $r\le0$, $x\ge1$ forces $a\ge1$ and $x\le sP+t$ forces
$a\le s$. Every color is used: $\varphi(r)$ at $x=r$ and $\psi(a)$ at
$x=aP$. Let $x=aP+r$ and $y=bP+r'$ have the same color, with
$z=x+y\le N'$.

- Both fine ($r,r'\ge1$). If $r+r'\le t$, then $z$ has residue $r+r'$ and is
  fine, and $\varphi(r)=\varphi(r')=\varphi(r+r')$ is impossible. If
  $r+r'\ge t+1$, then $z=(a+b+1)P+(r+r'-P)$ with $r+r'-P\in[-t,-1]$, so $z$
  is coarse.
- Both coarse ($r,r'\le0$). If $r+r'\ge-t$, then $z=(a+b)P+(r+r')$ is
  coarse with block $a+b\le s$, and $\psi(a)=\psi(b)=\psi(a+b)$ is
  impossible. If $r+r'<-t$, then $z=(a+b-1)P+(r+r'+P)$ with
  $r+r'+P\in[1,t]$, so $z$ is fine.

Equal summands are included ($a=b$, $r=r'$). $\square$

Taking $\psi$ and $\varphi$ extremal gives
$S(m+n)\ge S(m)(2S(n)+1)+S(n)$, the composition behind the
Abbott–Hanson inequality that the problem page records second-hand. That
source is not held, and nothing here rests on it.

## Random Bohr colorings of small depth

**Lemma B.** Let $m\ge2$ be an integer and put
$s=\lfloor(3/2)^m/4\rfloor$. Let $X\le s$ be a positive integer with

$$
\frac14+\frac{36m(1+\log X)^2}{X}+m\Bigl(1-\frac1m\Bigr)^{X/6}<1.
$$

Then $[1,s]$ has a Schur-free coloring by $m$ colors in which every color
occurs in $[1,X]$. For every $m\ge40$ the integer $X=m^4$ satisfies these
conditions.

*Proof.* Let $\theta_1,\ldots,\theta_m$ be independent and uniform on
$[0,1)$, write $\{u\}$ for the fractional part, and let
$B_i=\{x\ge1:\{\theta_ix\}\in(1/3,2/3)\}$. Each $B_i$ is sum-free: if
$\{\theta x\},\{\theta y\}\in(1/3,2/3)$, then $\{\theta(x+y)\}$ is congruent
modulo 1 to a number in $(2/3,4/3)$, which misses $(1/3,2/3)$; $x=y$ is
included.

For each integer $x\ge1$, $\theta\mapsto\{\theta x\}$ preserves Lebesgue
measure on $[0,1)$, so $\{\theta_1x\},\ldots,\{\theta_mx\}$ are independent
and uniform. Hence $x$ lies in no $B_i$ with probability $(2/3)^m$, and the
event $E_1$ that every $x\in[1,s]$ lies in some $B_i$ fails with
probability at most $s(2/3)^m\le1/4$.

Let $Z_i=|B_i\cap[1,X]|$, so $\mathbb EZ_i=X/3$. The indicator of
$(1/3,2/3)$ has Fourier coefficients $\hat c_0=1/3$ and
$|\hat c_h|\le1/(\pi|h|)$ for $h\ne0$, so the function
$\theta\mapsto1_{B_i}(x)$ has Fourier coefficient $\hat c_{n/x}$ at each
multiple $n$ of $x$ and $0$ elsewhere. For $x\ne y$ with $g=\gcd(x,y)$,
Parseval's identity for the two functions of $\theta_i$ at $x$ and at $y$
gives

$$
\Bigl|\Pr(x,y\in B_i)-\frac19\Bigr|
=\Bigl|\sum_{l\ne0}\hat c_{ly/g}\,\overline{\hat c_{lx/g}}\Bigr|
\le\sum_{l\ne0}\frac{g^2}{\pi^2l^2xy}=\frac{g^2}{3xy}.
$$

Since

$$
\sum_{x,y\le X}\frac{\gcd(x,y)^2}{xy}
\le\sum_{g\le X}\Bigl(\sum_{j\le X/g}\frac1j\Bigr)^2\le X(1+\log X)^2,
$$

the variance satisfies

$$
\operatorname{Var}Z_i\le\frac29X+\frac13X(1+\log X)^2\le X(1+\log X)^2 .
$$

Chebyshev's inequality gives $\Pr(Z_i<X/6)\le36(1+\log X)^2/X$, so the
event $E_2$ that $Z_i\ge X/6$ for every $i$ fails with probability at most
$36m(1+\log X)^2/X$.

Fix $\theta_1,\ldots,\theta_m$ in $E_1\cap E_2$ and give each $x\in[1,s]$ a
color chosen uniformly from $\{i:x\in B_i\}$, independently over $x$. Each
class lies in some $B_i$, so the coloring is Schur-free. Each $x\in B_i$
receives color $i$ with probability at least $1/m$, so color $i$ is absent
from $[1,X]$ with probability at most $(1-1/m)^{Z_i}\le(1-1/m)^{X/6}$. The
displayed condition makes the total failure probability less than 1.

For $X=m^4$ and $m\ge40$: $1\le\log m$ gives
$36m(1+\log X)^2/X\le900\log^2m/m^3\le0.2$, since $\log^2m/m^3$ decreases
for $m\ge2$ and is below $2.2\cdot10^{-4}$ at $m=40$; the last term is at
most $me^{-m^3/6}<1/4$, since $m^3/6>\log(4m)$ for $m\ge40$.
Thus the sum is below $1/4+0.2+1/4<1$.
Finally $(3/2)^{40}/4>40^4$, and
$(3/2)^m/(4m^4)$ increases for $m\ge40$ because $(41/40)^4<3/2$, so
$m^4\le s$. $\square$

## The composite has a short omitting prefix

**Lemma C.** Let $\delta\in(0,1)$. Let $\psi$ be a Schur-free coloring of
$[1,s]$ all of whose colors occur in $[1,D]$, with $\delta s\ge D+1$. Let
$\varphi$ be a Schur-free coloring of $[1,t]$ with a disjoint palette, such
that $P=2t+1$ is prime and $t+1\ge1/\delta$. Then the composition $c'$ of
Lemma A satisfies $M(c')<\delta N'$.

*Proof.* For $d>1/\delta$, every dilated prefix along $d$ has length at
most $N'/d<\delta N'$. Let $d\le1/\delta$. Then $d\le t+1<P$, so $d$ is
invertible modulo the prime $P$; and $d<s$, since $\delta s\ge D+1\ge2$.

- Fine colors. For each $r\in[1,t]$ some $j\le P-1$ has
  $dj\equiv r\pmod P$. Then $dj<sP\le N'$ and $c'(dj)=\varphi(r)$.
- Coarse colors. For each color of $\psi$ pick $a\le D$ with that color.
  The interval $[aP-t,aP]$ holds $t+1\ge d$ consecutive integers, hence a
  multiple $dj\le aP$, and $c'(dj)=\psi(a)$.

So every prefix along $d$ of length at least $DP$ contains every color, and
a color-omitting prefix along $d$ has length at most
$DP-1<\delta sP\le\delta N'$. $\square$

## Proof of the theorem

Fix $\delta\in(0,1)$ and $1\le A<L$, and choose $A_1$ with $A<A_1<L$.
By Lemma B fix $m\ge40$ with $\delta s\ge m^4+1$ and a Schur-free coloring
$\psi$ of $[1,s]$ by $m$ colors, all occurring in $[1,m^4]$. For large $n$,
$S(n)\ge A_1^n$. By Bertrand's postulate choose a prime $P$ with
$S(n)<P\le2S(n)$, put $t=(P-1)/2\le S(n)$, and let $\varphi$ be the
restriction to $[1,t]$ of a Schur-free coloring of $[1,S(n)]$ by $n$ colors,
with its colors renamed apart from those of $\psi$. For large $n$,
$t+1\ge1/\delta$, and Lemma C gives $M(c')<\delta N'$ for
the composition $c'$, which uses at most $k=m+n$ colors. Finally
$N'>P>S(n)\ge A_1^n\ge A^{m+n}$ for large $n$, because
$(A_1/A)^n\to\infty$; and $k=m+n\ge k_0$ for large $n$. $\square$
