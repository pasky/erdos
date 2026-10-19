---
name: research/erdos_699/remaining/details/cubic_abc
title: "Finitely many bad cubic triples assuming rational abc"
desc: "Ordinary abc implies cubic finiteness. A single abc exponent 10/9 suffices; a specified constant K gives n < 10^263 K^69. No Hall–Lang assumption is needed."
created: 2026-09-23T14:52:00Z
updated: 2026-09-23T19:29:43Z
---

# Finitely many bad cubic triples assuming rational abc

[[research/erdos_699/_index|P699 research]] ·
[[research/erdos_699/remaining/index_three|The cubic case]]

***

**Theorem.** Assuming the ordinary abc conjecture over $\mathbb Q$,
there are only finitely many bad triples $(n,3,j)$ in Erdős problem 699.
Neither Hall–Lang nor an abc conjecture over varying number fields is
needed. The odd part of $n$, the valuation of $j$, the auxiliary fields,
and the elliptic ranks may all vary.

This is a repository deduction from the established cubic factorization.
It does not prove that the finite exceptional set is empty. Section 4
makes the stopping bound explicit in one abc constant: if $K\ge1$
is valid at $\epsilon=1/9$, then every bad row satisfies
$n<10^{263}K^{69}$. Ordinary abc asserts the existence of such a
constant but does not supply its value. Unconditional finiteness at
$i=3$ remains open.

Together with the [completed indices](../../proofs/_index.md) and the
unconditional fixed-index finiteness results at $4,5,6,8$, this also
implies that **ordinary rational abc makes the set of all bad triples
in P699 finite**.

We use abc in the form

$$\max(|a|,|b|,|c|)\le K_\epsilon
\operatorname{rad}(abc)^{1+\epsilon},\qquad a+b=c,$$

for nonzero coprime integers. Signs cause no problem: rearrange the
equation to put its two positive terms on one side. Two fixed choices
of $\epsilon$ suffice below.

## 1. The factorization and the first abc inequality

For a bad triple, put

$$n=2^h u,\quad u\text{ odd},\quad c=n-j,\quad
t=v_2(j),\quad g=\gcd(u,3),\quad v=u/g,\quad m=h-t.$$

The [cubic factorization](cubic_abc_factorization.md)
supplies positive integers $A,B,r,s,f$, and $\lambda\in\{1,3\}$,
with

$$M=(n-2)/2=AB,\quad B=C_1,\quad
w=2^{2t}v^2,\quad L=2^tvB,\quad K=\frac{jc}{n-1},$$

and

$$\begin{aligned}
wAr&=\lambda K,& B^2s&=\lambda(K-1),\\
A^3r-\lambda f^2&=2^{2m-2}g^2s,&
f&=\frac{n-2j}{2L}.
\end{aligned}$$

Here $A,r,f$ are odd, $\gcd(Ar,s)=1$, $K<M/2$, and
$wr<\lambda B/2$. All this is unconditional.

For completeness, apply abc to

$$X=A^3r=Y+Z,\qquad Y=\lambda f^2,\quad
Z=2^{2m-2}g^2s.$$

Their common gcd divides nine: every common prime divides $g$, and
if three divides $X$ when $g=3$, then $3\nmid s$ and $v_3(Z)=2$.
The radical of the primitive triple is at most $6Arfs$. Moreover,

$$\frac{6Arfs}{X}
=\frac{3\lambda(n-2j)(K-1)}{LM^2}<\frac{12}{L},
\qquad X=\frac{\lambda M^2K}{L^2}<\frac{3n^3}{16L^2}.$$

Consequently,

$$
\boxed{L^{1+3\epsilon}\ll_\epsilon n^{3\epsilon}.}\tag{1}
$$

In particular $L=n^{o(1)}$ along any unbounded bad sequence. This is the first abc step of the height argument.

## 2. A rational parametrization with a useful fourth-degree identity

Put

$$T=n/2,\qquad q=\lambda B,\qquad R=wr,\qquad
F=Lf=(n-2j)/2.$$

The same factorization gives the conic

$$
\boxed{qF^2=(q-2R)T^2+3RT-R,\qquad 0<R<q/2.}\tag{2}
$$

In particular $q,R,T,F$ are positive integers. Also
$T=2^{h-1}u$, $q=\lambda B$, $u=gv$, and $Bv\le L$.
Thus $q,u\ll L$ and $\operatorname{rad}(T)\le2u$.

The rational parameter has a direct expression in the row and column:

$$\boxed{x=-\frac{j(n-j)}{(n-2)(j-1)}=\frac ab,}
\qquad \gcd(a,b)=1,\quad b>0.$$

In particular $x<0$, while

$$
x+2=\frac{(j-2)(n+j-2)}{(n-2)(j-1)}>0.
$$

Thus $a,b,a+2b$ are all nonzero. This is the conic parametrization

$$
x=\frac{R(q(T-1)+Y)}{2q(q+R-RT)},\qquad Y=qF.
$$

Indeed $R/q=K/M$, $T=M+1$, and
$K-1=(j-1)(c-1)/(n-1)$ simplify it to the displayed formula.
Its denominator cannot vanish: $K=jc/(n-1)>j/2\ge2$.
Define the integral binary quadratic forms

$$\begin{aligned}
p&=2qa^2+2qab+Rb^2,\\
V&=4q(q+R)a^2+4qRab+R^2b^2.
\end{aligned}$$

Substituting (2) into the expression for $x$ gives

$$
\boxed{V=2RTp,\qquad p^2-b^2V=4q^2a^3(a+2b).}\tag{3}
$$

The second identity is a polynomial identity, independent of (2).
The first follows equivalently by observing that the discriminant in
$x$ of $V(x,1)-2RTp(x,1)$ is $16R^2Y^2$.

The form $V$ is positive definite:

$$V=4q(q+R)\left(a+\frac{Rb}{2(q+R)}\right)^2
+\frac{R^3}{q+R}b^2>0.$$

Therefore $p>0$. The resultant is

$$\mathcal R:=\operatorname{Res}(p(X,1),V(X,1))
=4q^2R^3(R+4q)\le20q^6.\tag{4}$$

For primitive $(a,b)$, $\gcd(p,V)$ divides this binary resultant.
Indeed the integral resultant identities express both
$\mathcal R a^3$ and $\mathcal R b^3$ as integral combinations of
$p,V$; use $\gcd(a,b)=1$. Since $T$ is an integer, (3) also gives
$p\mid V$. Hence

$$
\boxed{p\mid\mathcal R,\qquad 1\le p\le20q^6.}\tag{5}
$$

Every prime dividing $pV$ thus divides $2qR(R+4q)u$.
This is the crucial arithmetic consequence of the parametrization.

All three terms in the second identity of (3) are nonzero, by the
signs already established.

## 3. The second abc inequality bounds n by a power of L

Write $H_x=\max(|a|,b)$. We first have the elementary lower bound

$$
\max(p^2,b^2V)\ge\frac{H_x^4}{24q}.\tag{6}
$$

If $b\ge H_x/2$, positive definiteness gives
$b^2V\ge R^3b^4/(q+R)\ge H_x^4/(24q)$, since $R\ge1$ and
$q+R<3q/2$. Otherwise $|a|=H_x$ and $|a+b|>H_x/2$, with
$a(a+b)>0$; thus $p=2qa(a+b)+Rb^2>qH_x^2$.

Let $D=\gcd(p^2,b^2V)$, also the common gcd of the three terms
in (3). By (5), $D\le p^2\le400q^{12}$. After division by $D$,
the abc triple therefore has height at least

$$
\frac{H_x^4}{9600q^{13}}.\tag{7}
$$

Its radical is at most

$$\begin{aligned}
\operatorname{rad}\bigl(2q\,pV\,ab(a+2b)\bigr)
&\le2qR(R+4q)u\,|ab(a+2b)|\\
&\le30q^3uH_x^3.
\end{aligned}\tag{8}$$

Applying ordinary rational abc with $\epsilon=1/6$ to (3), (7)
and (8) give

$$\frac{H_x^4}{9600q^{13}}
\ll(q^3uH_x^3)^{7/6},\qquad
H_x\ll q^{33}u^{7/3}.\tag{9}$$

On the other hand, $V\le9q^2H_x^2$ and $Rp\ge1$, so

$$n=2T=\frac{V}{Rp}\le9q^2H_x^2
\ll q^{68}u^{14/3}.$$

Using $q=\lambda B$, $u=gv$, $\lambda,g\le3$, and $Bv\le L$
now yields the uniform bound

$$
\boxed{n\ll L^{68}.}\tag{10}
$$

Finally choose $\epsilon=1/204$ in (1). This gives
$L\ll n^{1/69}$. Combining with (10),

$$
n\ll n^{68/69},
$$

which bounds $n$. There are only finitely many admissible columns in
each bounded row. This proves the theorem. $\square$

## 4. A fixed abc exponent suffices, with an explicit stopping bound

Here "rational abc" means the usual abc conjecture, over $\mathbb Q$.
We need considerably less than its assertion for every positive
$\epsilon$. The paired factorization strengthens the second step.

**Theorem.** Suppose that, for one fixed

$$
0<\epsilon<\frac{\sqrt{30}-3}{21}=0.117963\ldots,
$$

there is a constant $\mathcal K\ge1$ such that every nonzero primitive
integer triple $a+b=c$ satisfies

$$\max(|a|,|b|,|c|)
\le\mathcal K\operatorname{rad}(abc)^{1+\epsilon}.\tag{11}$$

Then there are only finitely many bad cubic triples. In particular,
the single exponent $1+\epsilon=10/9$ suffices. If a valid numerical
constant $\mathcal K$ for this exponent is supplied, then

$$
\boxed{n<10^{263}\mathcal K^{69}.}\tag{12}
$$

The proof only uses (11) on the two families of primitive triples
specified below. Consequently that restricted assertion, with one
uniform constant, also suffices. It is not necessary to assume (11)
for unrelated abc triples.

### Keeping the constant in the first application

The common gcd in Section 1 is at most nine, so the first application
with the specified constant gives

$$\frac X9\le\mathcal K
\left(\frac{12X}{L}\right)^{1+\epsilon}.$$

Substituting $X<3n^3/(16L^2)$ yields

$$\boxed{L^{1+3\epsilon}
\le108\mathcal K(9/4)^\epsilon n^{3\epsilon}.}\tag{13}$$

This uses abc only on the primitive reductions of
$A^3r=\lambda f^2+2^{2m-2}g^2s$.

### The paired identity and its common divisor

Choose an orientation $(J,C)=(j,n-j)$ or $(n-j,j)$, to be specified
below. Both entries are at least four. Write $U,V$ for the groups of
$(n-2)/2$ assigned labels zero and two for $J$, and keep $B=C_1$.
The [paired factorization](cubic_abc_factorization.md#3-paired-factors-at-n-minus-one-and-n-minus-two)
gives positive integers

$$\begin{gathered}
n-1=\lambda D_0D_1,\qquad UVB=(n-2)/2,\\
\alpha=\frac{J}{D_0U},\quad
\beta=\frac{C}{D_1V},\quad
\kappa=\frac{n+J-2}{D_1U},\quad
\ell=\frac{n+C-2}{D_0V},\\
X_1=\frac{J-1}{BD_1},\qquad Z_1=\frac{J-2}{V},\\
\alpha\beta=R,\qquad \kappa\ell=R+4q,\qquad q=\lambda B,
\end{gathered}$$

and the exact identity

$$\boxed{\lambda^2\alpha D_0^3Z_1+\beta\kappa
=4B^3T X_1^2.}\tag{14}$$

Put $a_0=2^tv$, so $R=a_0^2r$ and $L=a_0B$. Also put
$k_2=2^{v_2(\kappa)}$ and

$$
\delta=\gcd(\lambda^2\alpha D_0^3Z_1,\beta\kappa).
$$

Then

$$
\boxed{\delta\le9a_0k_2.}\tag{15}
$$

Here are the needed cancellations. First,
$\gcd(D_0,\beta\kappa)=1$: a prime dividing $D_0$ divides $J$
and $n-1$, while $C$ and $n+J-2$ are respectively $1$ and $-1$
modulo that prime. Also $\gcd(\lambda,\beta\kappa)=1$, since
$\lambda=3$ implies $3\nmid R(R+4q)$.

The odd parts of $\gcd(\beta,Z_1)$ and
$\gcd(\kappa,\alpha)$ are one. For example, a common odd prime
of $\beta$ and $Z_1$ would divide $n-2$; after removing its full
component from $C$ and $J-2$, the two quotients cannot both retain
that prime, because $C+(J-2)=n-2$. The argument for $\kappa,\alpha$
uses $(n+J-2)-J=n-2$ in the same way.
The odd part of $\gcd(\kappa,Z_1)$ divides
$\gcd(u,J-2)$, which divides three because $u\mid3J$.
Finally the odd part of $\gcd(\alpha,\beta)$ divides $u$.
Thus the odd part of $\delta$ is at most $3u$.
At two, $v_2(\alpha)=v_2(\beta)=t$, so the two-part of
$\delta$ is at most $2^tk_2$. Since $u=gv$, $g\le3$, this proves
(15).

### Repeated factors reduce the radical

Let $\mathscr R$ be the radical of the primitive triple obtained
from (14). Every prime of $T=2^{h-1}u$ lies in $6R$, because
$u=gv$ and $v^2\mid R$. Moreover
$\operatorname{rad}(R)\le R/a_0$ and the odd prime support of
$\kappa$ is bounded by $\kappa/k_2$. Therefore

$$\boxed{\mathscr R
\le6\lambda B\frac{R}{a_0}\frac{\kappa}{k_2}D_0X_1Z_1.}\tag{16}$$

In particular the odd part of the row is not an additional radical
factor. This is stronger than estimating the support in Section 3
without using the paired factors.

Write $Q=4B^3T X_1^2$ and $x=J/n\in(0,1)$. Direct substitution gives

$$2\lambda B R\kappa D_0X_1Z_1
=\frac{2R\beta\kappa(n-1)(J-1)(J-2)}{D_1C}
\le\sqrt2 R\beta\kappa\sqrt{\frac nB}\frac JC\sqrt Q.$$

Also $\ell D_0-\beta D_1=2BU>0$, so

$$D_1^2<\frac{(n-1)\ell}{\lambda\beta},\qquad
Q=\frac{2Bn(J-1)^2}{D_1^2}>\frac{B\beta J^2}{\ell}.$$

The last inequality uses $J\ge4$. Apply (11) to (14), after
primitive reduction, using height $Q/\delta$. Combining these
inequalities and (15)--(16) yields

$$\begin{aligned}
n^{(1-3\epsilon)/2}
&\le9\,3^{1+\epsilon}2^{(1+\epsilon)/2}\mathcal K\,
 B^{-1}R^{1+\epsilon}(\beta\kappa)^{(1+3\epsilon)/2}
 (R+4q)^{(1-\epsilon)/2}
 \frac{x^{2\epsilon}}{(1-x)^{1+\epsilon}}.
\end{aligned}\tag{17}$$

In this calculation the contribution of the common divisor is
$\delta/(a_0k_2)^{1+\epsilon}\le9$; it cancels the factors which
would otherwise cause a large height loss.

Reflection exchanges $\beta\kappa$ and $\alpha\ell$, whose
product is $R(R+4q)$. Choose the orientation with
$\beta\kappa\le\sqrt{R(R+4q)}$. The exact identity

$$
x(1-x)=\frac{R(n-1)(n-2)}{2qn^2}\ge\frac{R}{4q}
$$

then bounds the last factor in (17) by $(4q/R)^{1+\epsilon}$.
Use $R<q/2$, $R+4q<9q/2$, and $q\le3B$. For
$0<\epsilon\le1/8$ this gives the simple explicit estimate

$$\boxed{n^{(1-3\epsilon)/2}
\le10^5\mathcal K B^{1+2\epsilon}
\le10^5\mathcal K L^{1+2\epsilon}.}\tag{18}$$

For completeness, a bound on its numerical coefficient is
$9\cdot4\cdot2\cdot5\cdot(9/2)\cdot27=43740<10^5$.
No implicit height constant has been used.

### Combining the two estimates

Square (18), raise it to $1+3\epsilon$, and apply (13). The result is

$$\boxed{n^{1-6\epsilon-21\epsilon^2}
\le10^{10(1+3\epsilon)}
\bigl(108(9/4)^\epsilon\bigr)^{2+4\epsilon}
\mathcal K^{4+10\epsilon}.}\tag{19}$$

The exponent on the left is positive precisely in the stated range.
This proves finiteness from a single fixed abc exponent.

For $\epsilon=1/9$, (13) and (18) simplify to

$$L^{4/3}\le216\mathcal K n^{1/3},\qquad
n^{1/3}\le10^5\mathcal K L^{11/9}.$$

Eliminating $L$ gives

$$n\le10^{180}216^{33}\mathcal K^{69}
<10^{263}\mathcal K^{69},$$

where $216^2<10^5$ proves the last numerical inequality. This is
(12). $\square$

### Computing the exceptional set once the constant is given

For a specified valid $\mathcal K$, take
$N=\lceil10^{263}\mathcal K^{69}\rceil$. Enumerate the rows
$n=2^hu\le N$ with $u$ odd, $h\ge49$, and $3u^3<2^h$.
Factor the endpoint integers, intersect their prime-power residue
conditions, and apply full Lucas at every active odd prime to the
remaining columns. The earlier certified computation covers $h\le48$.
Direct binomial gcds give a slower elementary finite algorithm without
any need for a factorization oracle.

Thus the proof has explicit dependence on its abc constant. Ordinary
abc asserts that a valid constant exists, but does not supply its value
or an algorithm for finding one. Checking abc up to a finite height
cannot certify a constant for all heights. There is no further
ineffective application of Siegel, Roth, Faltings, or Hall--Lang here.

This effective statement concerns $i=3$. It neither proves that the
computed set would be empty nor makes the separate unconditional
finiteness arguments at $i=4,5,6,8$ effective.
