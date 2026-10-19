---
name: research/erdos_699/remaining/details/cubic_abc_factorization
title: "The integer factorization used in the cubic abc proof"
desc: "The endpoint conditions give coprime factors, the conic, and the paired identities used by the cubic abc proof."
created: 2026-09-23T21:45:28Z
updated: 2026-09-24T03:19:37Z
---

# The integer factorization used in the cubic abc proof

[[research/erdos_699/_index|P699 research]] ·
[[research/erdos_699/remaining/details/cubic_abc|The cubic abc proof]]

***

This note collects the unconditional algebra needed in Sections 1 and 4
of the cubic abc proof. Its input is the
[endpoint reduction](cubic_followup.md#1-the-remaining-problem-as-two-divisibilities).
These are necessary conditions for badness, not a converse: the higher
Lucas digits are not imposed by the factorization.

## 1. The factorization for all hypothetical bad triples

For a bad triple write

$$n=2^hu,\quad c=n-j,\quad d=c-j>0,\quad
t=v_2(j),\quad g=\gcd(u,3),\quad v=u/g,$$

where $u$ is odd, $h\ge2$, $4\le j<n/2$, and $3u^3<2^h$.
The endpoint conditions give

$$u(n-1)\mid3jc,\qquad
u(n-1)(n-2)\mid j(j-1)(j-2),$$

and the corresponding condition for $c$. At each active odd component
$p^a\Vert n-i$, they give $j\bmod p^a\in\{0,\ldots,i\}$.
Only a component $3^1$ can be inactive. We also use the proved
[alternating-coefficient inequality](cubic_followup.md#3-alternating-coefficients-exclude-an-infinite-family-of-columns)
$d^2>3n-2$.

The normalization gives $m:=h-t\ge2$, $v_2(c)=t$, and $v_2(d)=t+1$.
Here is a short justification. Put $W=u(n-1)(n-2)/6$.
The four coefficients $\binom j{3-i}\binom ci/W$, $0\le i\le3$,
are positive integers and sum to $2^h$. If $t\ge h$, all four are
divisible by $2^h$, which is impossible. For $t<h$ their exact common
two-part is $2^t$: each is divisible by $2^t$, and their derivative
sum is $3c/u$, of valuation $t$. Dividing by $2^t$ proves $m\ge2$.
The assertions about $c,d$ follow. These coefficient divisibilities
also follow directly from the residue labels at each active prime.

Set

$$K=\frac{jc}{n-1},\qquad M=\frac{n-2}{2},\qquad
\lambda=\operatorname{den}(K)\in\{1,3\},\qquad k=\lambda K.$$

The denominator is in lowest terms. If $\lambda=3$, then
$3\mid n-1$ and $3\nmid k u M$; hence in all cases
$\gcd(k,k-\lambda)=\gcd(\lambda,M)=1$.
Partition the full prime-power factors of $M$ by their labels
$j\equiv0,1,2$, and call their products $U,B,V$, respectively.
Thus $U=C_0$, $B=C_1$, and $V=C_2$ in residue-group notation.
The component $3^1$, if present, also has one of these three labels.
Thus $M=UBV$, with $U,B,V$ pairwise coprime. Put $A=UV$.
The labels and

$$
K-1=\frac{(j-1)(c-1)}{n-1}
$$

give $A\mid k$ and $B^2\mid k-\lambda$. Define positive integers
$R,s$ by

$$
AR=k,\qquad B^2s=k-\lambda.\tag{1}
$$

In particular $\gcd(AR,Bs)=1$ and $\gcd(\lambda,s)=1$.
The label-zero conditions at the active components of $u$ give
$v\mid j,c,d/2$; removing $g$ accounts for its possibly inactive
single factor three. Since $\gcd(v,A(n-1))=1$, we have $v^2\mid R$.
Also $v_2(R)=2t$. Define

$$
w=2^{2t}v^2,\qquad R=wr,\qquad L=2^tvB.
$$

Then $r$ is a positive odd integer. To define the remaining parameter,
put $e=d/2$. The middle label gives $B\mid j-1$, so the identity

$$
e=M-(j-1)=AB-(j-1)
$$

proves $B\mid e$ without assuming any auxiliary quotient integral.
As $\gcd(B,v)=1$, the preceding divisibilities and $v_2(e)=t$ give
the positive odd integer $f=e/L$.

We have obtained

$$\boxed{\begin{aligned}
AB+1&=2^{h-1}u,\\
wAr-B^2s&=\lambda,\\
\lambda w f^2&=\lambda A^2-s(2AB+1),\\
A^3r-\lambda f^2&=2^{2m-2}g^2s.
\end{aligned}}\tag{2}$$

For the third identity use $e^2=(M+1)^2-K(2M+1)$, then substitute
(1) and $e=Lf$. For the fourth, subtract the third from
$A^2(wAr-B^2s)=\lambda A^2$ and use
$(AB+1)^2/w=2^{2m-2}g^2$.

The coprimalities needed below are

$$
\gcd(Ar,s)=\gcd(B,r)=\gcd(A,f)=\gcd(s,f)=1.\tag{3}
$$

The first two follow from (1). At a prime of $A$, the outer label
makes $e\equiv1$ or $-1$ modulo that prime, proving the third.
The third identity of (2), together with $\gcd(\lambda A,s)=1$,
proves the fourth. The last identity of (2) also shows that a common
prime of $r,f$ can only be three. Finally $d^2>3n-2$ gives

$$
K<M/2,\qquad R<\lambda B/2.\tag{4}
$$

For the first abc application, the three terms
$A^3r$, $\lambda f^2$, and $2^{2m-2}g^2s$ have common gcd at most
nine. Indeed, (3) forces a common prime to divide $g$; if it is
three, then $3\nmid s$ and the last term has valuation two.

## 2. The conic and parameter sizes

Put

$$
T=n/2=AB+1,\qquad q=\lambda B,\qquad F=Lf=d/2.
$$

The notation separates the full coefficient $R=wr$ from its odd
factor $r$; $q$ is the middle-group coefficient, while $L$ contains
the column's two-part, $v$, and the middle group $B$.
Since $K/M=R/q$ and $F^2=T^2-K(2T-1)$, we obtain

$$
\boxed{qF^2=(q-2R)T^2+3RT-R,\qquad 0<R<q/2.}\tag{5}
$$

All four parameters are positive integers. Also $\gcd(q,R)=1$,
because $\gcd(B,R)=1$ and $\lambda=3$ implies $3\nmid R$.
The elementary size and support relations used in the abc proof are

$$Bv\le L,\qquad q\le3L,\qquad u\le3L,\qquad
\operatorname{rad}(T)\le2u.$$

## 3. Paired factors at n minus one and n minus two

Choose either orientation $(J,C)=(j,c)$ or $(c,j)$. Reassign $U,V$
to the zero and two labels of $J$; reflection exchanges them and
leaves $A,B,R,q$ unchanged. Partition

$$
\frac{n-1}{\lambda}=D_0D_1,\qquad D_0\mid J,\quad D_1\mid C.
$$

These factors are coprime and contain the full components with labels
zero and one, respectively. When $\lambda=1$, integrality of $K$
also supplies the label at a possibly inactive component three.
When $\lambda=3$, that component is removed; an active component
at three would already force $K$ integral.
All factors of $D_0D_1$ are coprime to $UBV$. Define

$$\alpha=\frac{J}{D_0U},\quad
\beta=\frac{C}{D_1V},\quad
\kappa=\frac{n+J-2}{D_1U},\quad
\ell=\frac{n+C-2}{D_0V}.\tag{6}$$

The labels prove that these are positive integers, for even as well
as odd columns. Their products and linear relations are

$$\boxed{\begin{gathered}
\alpha\beta=R,\qquad \kappa\ell=R+4q,\\
\kappa U+\beta V=2\lambda D_0,\qquad
\alpha U+\ell V=2\lambda D_1,\\
\ell D_0-\beta D_1=2BU,\qquad
\kappa D_1-\alpha D_0=2BV.
\end{gathered}}\tag{7}$$

These follow by multiplying or adding (6); for the second product use
$(n+J-2)(n+C-2)=JC+2(n-1)(n-2)$.
Moreover $v_2(\alpha)=v_2(\beta)=t$, and
$\gcd(\lambda,R(R+4q))=1$. Reflection interchanges
$\alpha\leftrightarrow\beta$ and $\kappa\leftrightarrow\ell$.

## 4. The paired abc identity

The same labels give positive integers

$$
X_1=\frac{J-1}{BD_1},\qquad Z_1=\frac{J-2}{V}.
$$

They satisfy the identity used in the second abc application:

$$\boxed{\lambda^2\alpha D_0^3Z_1+\beta\kappa
=4B^3T X_1^2.}\tag{8}$$

To prove it, multiply by $D_1^2UV$ and substitute (6),
$\lambda D_0D_1=n-1$, and $2BUV=n-2$. The result is

$$
(n-1)^2J(J-2)+C(n+J-2)=n(n-2)(J-1)^2,
$$

which follows from
$(n-1)^2-(J-1)^2=C(n+J-2)$. Every term in (8) is positive.
The [abc proof](cubic_abc.md#the-paired-identity-and-its-common-divisor)
controls the common divisor and radical before applying abc.

The identities here are repository deductions, extracted from the
[earlier factorization calculations](../../archive/other_approaches/cubic_factorization.md).
No elliptic-curve or number-field assumption is used in this note.
