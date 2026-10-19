---
name: theory/integer_sequences/L251_averaged_near_square_smooth_blocks/_proof
title: Proof of the averaged near-square construction
desc: |
  Count pairs (c, q) with C < c <= 2C and cq^2 in a window of length about
  K^2/C above m; Vaaler's inequality and the third-derivative test bound the
  error by about C^(4/7) K^(1/7), below the main term K/C when C is at most
  K^(6/11)/1024, and one adjustment lands within K of m.
tags: []
sources:
- theory/integer_sequences/L251_averaged_near_square_smooth_blocks/_index
created: 2026-10-15T22:27:51Z
updated: 2026-10-15T22:27:51Z
---

# Proof of the averaged near-square construction

***

This proves the whole statement of
[[theory/integer_sequences/L251_averaged_near_square_smooth_blocks/_index|L251]].
Throughout, $\log$ is the natural logarithm, $e(u):=e^{2\pi iu}$, and

$$
\psi(u):=u-\lfloor u\rfloor-\tfrac12 .
$$

For an integer $C\ge1$ and a real $X\ge0$ put

$$
S_C(X):=\sum_{C<c\le2C}\psi\Bigl(\sqrt{X/c}\Bigr),\qquad
Y_X:=\sqrt{X/C}.
$$

## 1. Two elementary lemmas

**Lemma 1 (adjustment).** Let $c\ge1$, $q\ge1$ and $m\ge0$ be integers with
$D:=cq^2-m>0$, and let $t$ be the largest integer $t\ge0$ with $ct^2<D$.
Then $N:=c(q-t)(q+t)$ satisfies $0<N-m\le c(2t+1)$, $0\le t<q$ and
$t<\sqrt{D/c}$.

*Proof.* As in the proof of
[[theory/integer_sequences/L250_explicit_near_square_smooth_blocks/_proof|L250]]:
$t$ exists because $c\cdot0^2<D$ and $ct^2<D$ bounds $t$; then
$N-m=D-ct^2>0$, maximality gives $c(t+1)^2\ge D$ and hence
$N-m\le c(2t+1)$, and $ct^2<D\le cq^2$ gives $t<q$ and $t<\sqrt{D/c}$.
$\square$

**Lemma 2 (count).** Let $C\ge1$ be an integer and $0\le x<x'$ real. The
number of integer pairs $(c,q)$ with $C<c\le2C$, $q\ge1$ and
$x<cq^2\le x'$ equals

$$
\sum_{C<c\le2C}\Bigl(\sqrt{x'/c}-\sqrt{x/c}\Bigr)-S_C(x')+S_C(x).
$$

*Proof.* For fixed $c$ the admissible $q$ are the integers in
$(\sqrt{x/c},\sqrt{x'/c}]$, all positive because $\sqrt{x/c}\ge0$. Their
number is $\lfloor\sqrt{x'/c}\rfloor-\lfloor\sqrt{x/c}\rfloor$, and
$\lfloor u\rfloor=u-\psi(u)-\frac12$. Sum over $c$. $\square$

## 2. The two analytic inputs

**Vaaler's inequality.** Lemma 7.1 of Granville and Ramaré (Mathematika 43
(1996), 73--107), from Vaaler (Bull. Amer. Math. Soc. 12 (1985), 183--216),
states for every integer $R\ge1$

$$
\pm\psi_0(t)\le\frac1{2R+2}+\sum_{0<|r|\le R}a_r^{\pm}e(rt),
\qquad
a_r^{\pm}=i\alpha_r\pm\beta_r,
$$

where $\psi_0$ is their sawtooth function ($\psi_0=\psi$ off the integers
and $\psi_0=0$ at the integers), and

$$
\alpha_r=\frac{1}{2\pi(R+1)}\Bigl(\pi\Bigl(1-\frac{|r|}{R+1}\Bigr)
\cot\frac{\pi r}{R+1}+\frac{|r|}{r}\Bigr),\qquad
\beta_r=\frac{1}{2R+2}\Bigl(1-\frac{|r|}{R+1}\Bigr).
$$

These are the held statement as printed (read on the page image of p. 27 of
the held preprint, whose labels the library card follows). The upper sign
gives

$$
\psi_0(t)\le\frac1{2R+2}+\sum_{0<|r|\le R}(i\alpha_r+\beta_r)e(rt).
\tag{V+}
$$

As printed, the lower sign is a misprint: as $t\to0^+$ its left side tends
to $\frac12$, while its right side tends to
$\frac1{2R+2}-\sum_{0<|r|\le R}\beta_r=\frac{1-R}{2R+2}\le0$, because the
$\alpha_r$ are odd in $r$ and cancel. The correct lower inequality follows
from (V+): $\psi_0$ is odd, $\alpha_{-r}=-\alpha_r$ and $\beta_{-r}=\beta_r$,
so (V+) at $-t$, reindexed by $r\mapsto-r$, reads

$$
-\psi_0(t)\le\frac1{2R+2}+\sum_{0<|r|\le R}(-i\alpha_r+\beta_r)e(rt).
\tag{V-}
$$

Both (V+) and (V-) also hold with $\psi$ in place of $\psi_0$: the two
functions differ only at integers $t$, where both right sides equal
$\frac1{2R+2}+2\sum_{r=1}^R\beta_r=\frac12=|\psi(t)|$.

For the moduli, put $x=r/(R+1)\in(0,1)$ for $1\le r\le R$. Then
$0\le\pi(1-x)\cot(\pi x)+1\le1/x$: the upper bound is
$\pi x\cot(\pi x)\le1$, and the lower bound is trivial for $x\le\frac12$
and, for $x>\frac12$, is $\pi y\cot(\pi y)\le1$ with $y=1-x$. Hence
$0\le\alpha_r\le1/(2\pi r)$, and $0\le\beta_r\le1/(2R+2)$, so

$$
|\pm i\alpha_r+\beta_r|=\sqrt{\alpha_r^2+\beta_r^2}
\le\frac1{2\pi|r|}+\frac1{2R+2}\qquad(0<|r|\le R).
$$

**The third-derivative test.** Lemma 8.6 of the same paper, with $k=2$
(statement read on the page image of p. 30 of the held preprint): suppose
that on
$[A,B]$ the function $f$ is four times differentiable with $f'''$ monotonic
and

$$
0<m_2\le f'''(t)\le\frac{1}{2Q^{3/2}}
$$

for some integer $Q\in[4,N]$, where $N$ is an integer and $]A,B]$ contains at
most $N$ integers. Then

$$
\Bigl|\frac1{8N}\sum_{A<n\le B}e(\pm f(n))\Bigr|^4
<\frac1{8Q}+\frac{3\log^2Q}{4\pi m_2NQ^{3/2}} .
$$

(The printed factor is $3k^{-k/2}/(2\pi m_kN)$ times
$\log^kQ/Q^{2-2^{-k+1}}$, which is the displayed term at $k=2$.)

## 3. The multiplier sum

**Lemma 3.** Let $C\ge4$ be an integer and $X>0$ real with

$$
C^{3/2}\le Y_X\le C^3/120 .
$$

Then

$$
|S_C(X)|\le60\,C^{4/7}Y_X^{1/7}+40\,C^{3/4}(\log C)^{3/2}.
$$

*Proof.* Write $Y=Y_X$. For an integer $R\ge1$ and $1\le r\le R$ put

$$
T_r:=\sum_{C<c\le2C}e\Bigl(r\sqrt{X/c}\Bigr),
$$

so that $T_{-r}=\overline{T_r}$ for the sums with negative frequency.

*Step 1 (Vaaler).* Sum (V+) and (V-) for $\psi$ over the points
$t=\sqrt{X/c}$. Since $S_C(X)$ is real,

$$
\pm S_C(X)\le\frac{C}{2R+2}+\sum_{0<|r|\le R}|\pm i\alpha_r+\beta_r|\,|T_r|,
$$

and the bound on the moduli, with $|T_{-r}|=|T_r|$ and $1/(R+1)<1/r$ for
$r\le R$, gives

$$
|S_C(X)|\le\frac{C}{2R+2}+\Bigl(1+\frac1\pi\Bigr)\sum_{r=1}^{R}\frac{|T_r|}{r}.
\tag{1}
$$

*Step 2 (one frequency).* Fix $r\ge1$ with $rY/C^3\le1/30$. Put
$h(u):=-r\sqrt X\,u^{-1/2}$, so that $e(r\sqrt{X/c})=e(-h(c))$ and

$$
h'''(u)=\tfrac{15}{8}\,r\sqrt X\,u^{-7/2}>0 ,
$$

which decreases on $[C,2C]$. Since $\sqrt X=Y\sqrt C$, its maximum and
minimum there are

$$
M_2=h'''(C)=\tfrac{15}{8}\,\frac{rY}{C^3},\qquad
m_2=h'''(2C)=2^{-7/2}M_2 .
$$

Let $Z:=(2M_2)^{-2/3}$ and $Q:=\lfloor Z\rfloor$. The condition
$rY/C^3\le1/30$ gives $2M_2\le\frac18$, so $Z\ge4$ and $Q\ge4$; also
$Q\ge Z-1\ge\frac34Z$. The condition $Y\ge C^{3/2}$ gives
$2M_2\ge C^{-3/2}$, so $Q\le Z\le C$. From $Q\le Z$ we get
$h'''\le M_2\le1/(2Q^{3/2})$. So the third-derivative test applies with
$[A,B]=[C,2C]$, $N=C$ (the interval $]C,2C]$ contains exactly $C$ integers)
and the lower sign, and $(a+b)^{1/4}\le a^{1/4}+b^{1/4}$ gives

$$
|T_r|<8^{3/4}CQ^{-1/4}
+8\Bigl(\frac{3}{4\pi}\Bigr)^{1/4}C^{3/4}(\log Q)^{1/2}\,m_2^{-1/4}Q^{-3/8}.
$$

Now $Q^{-1/4}\le(4/3)^{1/4}(2M_2)^{1/6}$ and
$Q^{-3/8}\le(4/3)^{3/8}(2M_2)^{1/4}$, while $2M_2/m_2=2^{9/2}$ and
$\log Q\le\log C$. Hence

$$
|T_r|\le\kappa_1\,C\Bigl(\frac{rY}{C^3}\Bigr)^{1/6}
+\kappa_2\,C^{3/4}(\log C)^{1/2},
$$

with
$\kappa_1=8^{3/4}(4/3)^{1/4}(15/4)^{1/6}=6.371\ldots<6.4$ and
$\kappa_2=8(3/(4\pi))^{1/4}(4/3)^{3/8}2^{9/8}=13.58\ldots<13.6$.

*Step 3 (choice of $R$).* Let $R:=\lceil C^{3/7}Y^{-1/7}\rceil$. Since
$Y\le C^3$, the number $C^{3/7}Y^{-1/7}$ is at least $1$, so
$C^{3/7}Y^{-1/7}\le R\le2C^{3/7}Y^{-1/7}$. Every $r\le R$ satisfies

$$
\frac{rY}{C^3}\le\frac{2Y^{6/7}}{C^{18/7}}\le\frac1{30},
$$

because $Y\le C^3/120$ and $60^{7/6}=118.7\ldots<120$; so Step 2 applies to
every $r\le R$. Using $\sum_{r\le R}r^{-5/6}\le1+6(R^{1/6}-1)\le6R^{1/6}$
and $\sum_{r\le R}r^{-1}\le1+\log R$ in (1),

$$
|S_C(X)|\le\frac{C}{2R}
+6\kappa_1\Bigl(1+\frac1\pi\Bigr)C^{1/2}Y^{1/6}R^{1/6}
+\kappa_2\Bigl(1+\frac1\pi\Bigr)C^{3/4}(\log C)^{1/2}(1+\log R).
$$

The first term is at most $\frac12C^{4/7}Y^{1/7}$. In the second,
$R^{1/6}\le2^{1/6}C^{1/14}Y^{-1/42}$, so the term is at most
$6\cdot6.4\cdot1.3184\cdot1.1225\,C^{4/7}Y^{1/7}<56.9\,C^{4/7}Y^{1/7}$. In
the third, $R\le2C^{3/7}$ and $C\ge4$ give
$1+\log R\le1+\log2+\frac37\log C\le2\log C$, so the term is at most
$2\cdot13.6\cdot1.3184\,C^{3/4}(\log C)^{3/2}<35.9\,C^{3/4}(\log C)^{3/2}$.
Adding the three bounds proves the lemma. $\square$

## 4. Proof of the statement

Let $K\ge64$ and $0\le m\le2^{-15}K^{28/11}$ be integers. If
$m\le K^{5/2}/128$, then
[[theory/integer_sequences/L250_explicit_near_square_smooth_blocks/_index|L250]]
supplies the required integer. Assume from now on that
$K^{5/2}/128<m\le2^{-15}K^{28/11}$. This range is nonempty only if
$K^{1/22}>2^{15}/128=2^8$, so

$$
K>2^{176},\qquad \log K>176\log2>121.9 .
$$

Put

$$
C:=\Bigl\lceil\frac{16m}{K^2}\Bigr\rceil,\qquad
E:=\Bigl\lfloor\frac{K^2}{128C}\Bigr\rfloor,\qquad
Y:=Y_m=\sqrt{m/C}.
$$

**(F1) Size of $C$.** $C\ge16m/K^2>\sqrt K/8>2^{85}$. Also
$C<16m/K^2+1\le2^{-11}K^{6/11}+1\le2^{-10}K^{6/11}$, since
$2^{-11}K^{6/11}>2^{-11}2^{96}\ge1$.

**(F2) Size of $Y$.** $C\ge16m/K^2$ gives $Y\le K/4$. Since $K\ge64$,
$m>K^{5/2}/128\ge K^2/16$, so $16m+K^2\le32m$ and
$m/C>m/(16m/K^2+1)=mK^2/(16m+K^2)\ge K^2/32$; thus $Y>K/(4\sqrt2)$.

**(F3) Size of $E$.** $E\le K^2/(128C)<K^2/16\le m$, and
$E\ge K^2/(128C)-1\ge K^2/(256C)$ because $C\le K\le K^2/256$.

So for $X\in\{m,m+E\}$ we have $m\le X\le2m$ and
$K/(4\sqrt2)<Y_X\le\sqrt2\,Y\le K/(2\sqrt2)$.

**Lemma 3 applies to $X=m$ and $X=m+E$.** $C\ge4$ by (F1). By (F1),
$C^{3/2}\le2^{-15}K^{9/11}<K/(4\sqrt2)<Y_X$. By (F1),
$C^3>K^{3/2}/512$, and $K^{1/2}>2^{88}$ gives
$K^{3/2}/(512\cdot120)\ge K/(2\sqrt2)\ge Y_X$, so $Y_X\le C^3/120$.
Since $Y_X^{1/7}\le(K/(2\sqrt2))^{1/7}<0.863\,K^{1/7}$,

$$
|S_C(m)|+|S_C(m+E)|\le103.6\,C^{4/7}K^{1/7}+80\,C^{3/4}(\log C)^{3/2}.
\tag{2}
$$

**The main term.** For $C<c\le2C$,

$$
\sqrt{\frac{m+E}{c}}-\sqrt{\frac mc}
=\frac{E}{\sqrt c\,(\sqrt{m+E}+\sqrt m)}
\ge\frac{E}{\sqrt{2C}\,(\sqrt2+1)\sqrt m},
$$

using $c\le2C$ and $E\le m$. There are exactly $C$ such $c$, so the sum in
Lemma 2 (with $x=m$, $x'=m+E$) is at least

$$
\frac{E\sqrt C}{(2+\sqrt2)\sqrt m}=\frac{E}{(2+\sqrt2)\,Y}
\ge\frac{K^2/(256C)}{(2+\sqrt2)K/4}=\frac{K}{64(2+\sqrt2)\,C}>\frac{K}{219\,C}.
\tag{3}
$$

**The error is smaller.** Each term of (2) is below $K/(438C)$.

- First term. By (F1), $C\le2^{-10}K^{6/11}$, so
  $C^{11/7}\le2^{-110/7}K^{6/7}$. Since
  $2^{110/7}=5.37\ldots\times10^4>438\cdot103.6=45376.8$, this gives
  $103.6\,C^{4/7}K^{1/7}=103.6\,C^{11/7}K^{1/7}/C<K/(438C)$.
- Second term. By (F1), $C^{7/4}\le2^{-35/2}K^{21/22}$ and
  $\log C<\frac6{11}\log K$. So
  $80\cdot438\,C^{7/4}(\log C)^{3/2}\le35040\cdot2^{-35/2}
  (6/11)^{3/2}K^{21/22}(\log K)^{3/2}<0.077\,K^{21/22}(\log K)^{3/2}$.
  The function $(\log K)^{3/2}K^{-1/22}$ decreases for $\log K>33$, and at
  $K=2^{176}$ it equals $1347.6\ldots/256<5.3$; so
  $0.077(\log K)^{3/2}<0.41\,K^{1/22}<K^{1/22}$, and
  $80\,C^{3/4}(\log C)^{3/2}<K/(438C)$.

By Lemma 2, (2) and (3), the number of pairs $(c,q)$ with $C<c\le2C$,
$q\ge1$ and $m<cq^2\le m+E$ exceeds $K/(219C)-2K/(438C)=0$; being an
integer, it is at least $1$. Take such a pair, and apply Lemma 1 with
$D=cq^2-m\in(0,E]$. It gives $t$ with $t<\sqrt{E/c}$ and
$N=c(q-t)(q+t)$ with

$$
0<N-m\le c(2t+1)<2\sqrt{cE}+c\le2\sqrt{2C\cdot\frac{K^2}{128C}}+2C
=\frac K4+2C\le K,
$$

since $C\le2^{-10}K^{6/11}\le3K/8$. The three factors are positive integers
at most $K$:

- $1\le c\le2C\le K$;
- $q-t\ge1$, because $t<q$;
- $q\le\sqrt{(m+E)/c}<Y_{m+E}\le K/(2\sqrt2)<0.36K$ and
  $t<\sqrt{E/C}\le K/(8\sqrt2\,C)<0.09K$, so $q+t<K$.

So $N\in(m,m+K]$ is a product of three positive integers at most $K$, and
each prime factor of $N$ is at most $K$. This proves the first sentence of
the statement.

**The bound for $k(n)$.** Let $n\ge1$ and
$K:=\max(64,\lceil(2^{15}n)^{11/28}\rceil)$, so that
$n\le2^{-15}K^{28/11}$. If $k(n)\ge K$, some integers $0\le m\le n$ and
$k\ge K$ have each of $m+1,\ldots,m+k$ divisible by a prime greater than
$k$; then each of $m+1,\ldots,m+K$ has a prime factor greater than $K$,
contradicting the first part. Hence
$k(n)\le K-1<\max(64,(2^{15}n)^{11/28})$. The argument uses only $m\ge0$,
so it applies unchanged when $m$ is required to be positive. For the last
sentence, let $k\ge64$: by the first part, for every integer
$0\le n\le2^{-15}k^{28/11}$ the block $n+1,\ldots,n+k$ contains an integer
with no prime factor greater than $k$, so $n_k>2^{-15}k^{28/11}$. $\square$

## Where the exponent comes from

The proof uses the third-derivative test only through Lemma 3. With
$Y\asymp K$ fixed by the requirement $q+t\le K$, the main term is of order
$K/C$ and Lemma 3's leading error is of order $C^{4/7}K^{1/7}$; they balance
at $C\asymp K^{6/11}$, which gives $m\asymp CK^2\asymp K^{28/11}$. The
second error term, of order $C^{3/4}(\log C)^{3/2}$, is smaller by a power
of $K$ in that range, but only by $K^{1/22}$ against $(\log K)^{3/2}$, so it
needs $K$ large. The first error term forces a small constant such as
$2^{-15}$; with it the averaged range is nonempty only for $K>2^{176}$, where
both error terms are under control, and below that L250 alone covers the
statement.
