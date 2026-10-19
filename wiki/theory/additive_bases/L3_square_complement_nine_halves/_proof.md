---
name: theory/additive_bases/L3_square_complement_nine_halves/_proof
title: Proof of the annular square-complement limits
desc: |
  Elementary root lifting proves positive-target coverage; disjoint cycles
  give a uniform counting error and exact limits 3 sqrt(2) and 9/2.
tags: []
sources: []
created: 2026-09-09T00:57:37Z
updated: 2026-09-09T01:21:03Z
---

***

We prove [L3](_index.md) for its displayed set $A$. Throughout, a power
$q$ means $3^k$ with integer $k\ge0$. Membership in $R_M$ means
positive-integer membership in one of the residue classes $0,1,2$ modulo
$M$, with repetitions removed. Counting functions use the closed real
cutoff convention $A(X)=|A\cap[1,X]|$.

## Bounded square roots

Fix an integer $u\equiv1\pmod3$. For each power $q$, there is a root
$m_q$ with

$$
0\le m_q\le q,\qquad m_q^2\equiv u\pmod{2q}.
\tag{6}
$$

At adjacent powers $q$ and $Q=3q$, the bounded roots satisfy

$$
m_Q\in\{m_q,\ 2q-m_q,\ 2q+m_q\}.
\tag{7}
$$

Here are complete elementary justifications. Modulo $3$, the roots of
$u$ are exactly $1$ and $-1$. Suppose $q=3^k$ with $k\ge1$, and $z$
is a root modulo $q$. Write $z^2-u=dq$. The three possible lifts of
its residue class modulo $3q$ are $z+hq$ for $h=0,1,2$. Their square
congruence is equivalent to

$$
d+2zh\equiv0\pmod3,
$$

because $3\mid q$. Since $z^2\equiv1\pmod3$, the coefficient $2z$
is nonzero modulo $3$. Exactly one $h$ solves the displayed congruence.
Every root modulo $3q$ reduces to a root modulo $q$. Induction therefore
gives exactly two roots modulo every $q\ge3$. They are distinct sign
classes: a root is not divisible by $3$, so it cannot equal its negative
modulo $q$.

For any root class modulo the odd integer $q$, the two classes above it
modulo $2q$ have opposite parity. Choose the one with parity $u$. Its
square is then congruent to $u$ modulo both $q$ and $2$, hence modulo
$2q$: if an integer is divisible by $q$ and by $2$, it is divisible by
$2q$ because $q$ is odd. Conversely every root modulo $2q$ arises this
way. Thus for $q\ge3$ there are exactly two sign classes modulo $2q$.
Neither is represented by $0$ or $q$, since those integers are divisible
by $3$. For either root representative $z\in[0,2q)$, the smaller of
$z$ and $2q-z$ is the unique root $m_q$ with $0<m_q<q$.

A root $m_Q\in[0,3q]$ reduces modulo $2q$ to $m_q$ or $-m_q$.
For $0<m_q<q$, all representatives of these classes in $[0,3q]$ are
exactly $m_q,2q-m_q,2q+m_q$. This proves (7) when $q\ge3$.

For $q=1$, put $m_1=0$ if $u$ is even and $m_1=1$ if $u$ is odd.
These are precisely the bounded roots modulo $2$. An even $u\equiv1
\pmod3$ is $4$ modulo $6$ and has bounded root $m_3=2$; an odd such
$u$ is $1$ modulo $6$ and has bounded root $m_3=1$. Each belongs to
the set on the right of (7). This supplies the first transition as well
as the starting case of (6).

## Catching a positive residual

If $a$ is an integer, $r\in\{0,1,2\}$, and

$$
0<a\le4q^2,\qquad a\equiv r\pmod{2q},
\tag{8}
$$

then $a\in A$. To see this, list the closed outer intervals at scales
$1,3,\ldots,q$. The upper endpoint $4s^2$ at scale $s$ equals the
lower endpoint $4(3s)^2/9$ at scale $3s$. Their union is
$[4/9,4q^2]$, which contains every positive integer at most $4q^2$.
Choose a scale $s\le q$ whose interval contains $a$. Since $2s$ divides
$2q$, congruence (8) implies $a\equiv r\pmod{2s}$. The outer annulus
at $s$ contains $a$. This argument includes shared endpoints and $s=1$.

## Coverage of every positive target

At scale $q=1$, $R_2$ contains every positive integer and the outer
interval contains $1,2,3,4$. Thus these four targets have the form
$0^2+a$, and $5=1^2+4$.

Fix an integer $t\ge6$. Choose the unique $r\in\{0,1,2\}$ with
$r\equiv t-1\pmod3$, and put $u=t-r$. Apply (6) and (7) to this
$u$, and write

$$
a_q=t-m_q^2.
\tag{9}
$$

Each $a_q$ is an integer congruent to $r$ modulo $2q$. If any $a_q$
lies in $[4q^2/9,4q^2]$, it belongs to the outer annulus at $q$ and
represents $t$. We may therefore assume that no $a_q$ lies in that
closed interval, and produce another representation.

Since $m_1\in\{0,1\}$, we have $a_1\ge5>4$. Also $a_s\le t$ for
every scale $s$. There is consequently a least power $Q>1$ such that
$a_Q\le4Q^2$. Put $Q=3q$. Minimality gives $a_q>4q^2$. At scale $Q$
the residual is at most the outer upper endpoint, and by assumption it
is outside the closed outer interval. Hence it lies strictly below the
lower endpoint:

$$
a_q>4q^2,\qquad a_Q<\frac{4Q^2}{9}=4q^2.
\tag{10}
$$

If $a_Q>0$, it satisfies (8) at scale $q$, because its congruence modulo
$2Q$ descends modulo $2q$. It then belongs to $A$ and represents $t$.
We may thus assume $a_Q\le0$, including the possibility $a_Q=0$.

Write $m=m_q$ and $M=m_Q$. Formula (7) lists all possibilities for $M$.
The choice $M=m$ contradicts (10). The choice $M=2q-m$ would imply

$$
a_Q=a_q-4q^2+4qm>0,
$$

contrary to $a_Q\le0$. Therefore $M=2q+m$. Define the alternative
residual

$$
e=t-(2q-m)^2=a_q-4q^2+4qm>0.
\tag{11}
$$

The integer $2q-m$ is a root of $u$ modulo $2q$, so
$e\equiv r\pmod{2q}$. If $e\le4q^2$, (8) gives $e\in A$ and
$t=(2q-m)^2+e$. It remains to treat $e>4q^2$.

Set

$$
b=t-(q-m)^2=a_q+2qm-q^2.
\tag{12}
$$

Because $q-m=Q-M$ and $M^2\equiv u\pmod Q$, we have
$b\equiv r\pmod Q$. Moreover (10) and (11) give

$$
b=\frac{a_q+e}{2}+q^2>5q^2.
\tag{13}
$$

The inequality $a_Q=a_q-4q^2-4qm\le0$ gives the upper bound

$$
b\le3q^2+6qm\le9q^2,
\tag{14}
$$

where the last step uses $m\le q$. Thus

$$
b\in R_Q\cap\left[\frac{5Q^2}{9},Q^2\right]\subseteq A.
$$

Finally $q-m\ge0$, so (12) is a representation by a nonnegative square
and an element of $A$. The argument allowed equality in (14), and allowed
$a_Q=0$ throughout its final branch. Together with the five initial
targets, it proves positive-target coverage.

## Exact cycles and their endpoint conventions

For each power $q$, let

$$
C_q=(L_q,U_q]\cap\mathbb Z_{>0},\qquad
L_q=\frac{4q^2}{9},\qquad U_q=4q^2.
\tag{15}
$$

The cycles are pairwise disjoint and partition the positive integers:
$U_q=L_{3q}$, their union as real intervals is $(4/9,\infty)$, and
every positive integer exceeds $4/9$. The first cycle is
$C_1=\{1,2,3,4\}$, all of which belong to $A$.

Fix $q\ge3$. An outer annulus from a smaller scale has upper endpoint
at most $L_q$ and cannot meet $C_q$. An outer annulus from a larger
scale has lower endpoint at least $U_q$; only the next scale can meet
$C_q$, and only at $U_q$. That endpoint already lies in the outer
annulus at $q$, because $U_q=4q^2\equiv0\pmod{2q}$. It introduces
no extra member. Every inner annulus from a smaller scale ends at most
at $q^2/9<L_q$. Every inner annulus from a larger scale starts at least
at $5q^2>U_q$. Thus on $C_q$ the literal union defining $A$ has
exactly the membership given by its two annuli at scale $q$.

Put $B_q=5q^2/9$ and $D_q=q^2$. These are integers for $q\ge3$.
Since $R_{2q}\subseteq R_q$, we obtain the following disjoint
description, including all internal endpoints:

$$
\begin{aligned}
A\cap C_q={}&
\bigl(R_{2q}\cap(L_q,B_q)\bigr)\\
&\mathbin{\dot\cup}
\bigl(R_q\cap[B_q,D_q]\bigr)\\
&\mathbin{\dot\cup}
\bigl(R_{2q}\cap(D_q,U_q]\bigr).
\end{aligned}
\tag{16}
$$

The point $L_q$ belongs to the preceding cycle and is deliberately
excluded from (16). For instance, at $q=3$ it is $4\in A$, although
$4\notin R_6$. Its contribution is retained in the prefix count below.
For integer endpoints $L<U$, the corresponding half-open prefix identity
would be

$$
A\cap[0,U)
=(A\cap[0,L))\mathbin{\dot\cup}(A\cap\{L\})
\mathbin{\dot\cup}(A\cap(L,U-1]).
$$

Replacing its final piece by $A\cap(L,U]$ changes the right endpoint.
Below we use closed prefixes throughout, so the exact new piece is
$A\cap(L_q,X]$, and it is the full cycle only when $X=U_q$.

## Periodic counts with a uniform error

For a residue $r$ modulo an integer $M\ge1$ and real $a\le b$, the
number of integers congruent to $r$ in $(a,b]$ is exactly

$$
\left\lfloor\frac{b-r}{M}\right\rfloor
-\left\lfloor\frac{a-r}{M}\right\rfloor.
\tag{17}
$$

It differs from $(b-a)/M$ by at most $1$. When $M\ge3$, the three
residues defining $R_M$ are distinct. Summing (17) shows that their
count in a positive interval $(a,b]$ differs from $3(b-a)/M$ by at
most $3$. Changing either endpoint's inclusion alters the count by at
most one. Consequently, for any choices of open or closed endpoints in
a positive interval of length $\ell$, the count from $R_M$ differs
from $3\ell/M$ by at most $6$. This also covers a singleton interval,
an empty interval, and an interval whose endpoints coincide. This bound
does not depend on $M$, the endpoint values, or the translation of the
interval.

For $q\ge3$, both moduli in (16) are at least $3$. Apply this estimate
to the three intervals there. Their lengths are $q^2/9$, $4q^2/9$,
and $3q^2$, respectively. Therefore

$$
|A\cap C_q|=6q+\varepsilon_q,\qquad
|\varepsilon_q|\le18,
\tag{18}
$$

since

$$
\frac{3}{2q}\frac{q^2}{9}
+\frac3q\frac{4q^2}{9}
+\frac{3}{2q}(3q^2)=6q.
$$

Now let $q=3^k$ with $k\ge1$. The cycles preceding $C_q$ are
$C_1,C_3,\ldots,C_{q/3}$ and partition all positive integers at most
$L_q$. The exact first-cycle count is four. Summing (18) for the
remaining $k-1$ preceding cycles gives

$$
\begin{aligned}
A(L_q)
&=4+\sum_{j=1}^{k-1}(6\cdot3^j+\varepsilon_{3^j})\\
&=3q-5+\sum_{j=1}^{k-1}\varepsilon_{3^j}.
\end{aligned}
\tag{19}
$$

The sum is empty when $k=1$. In particular,

$$
|A(L_q)-3q|\le5+18(k-1).
\tag{20}
$$

For an arbitrary real $X\in[L_q,U_q]$, intersect each interval in
(16) with $(-\infty,X]$. The resulting lengths are

$$
\begin{aligned}
\ell_1(X)&=\max\{0,\min\{X,B_q\}-L_q\},\\
\ell_2(X)&=\max\{0,\min\{X,D_q\}-B_q\},\\
\ell_3(X)&=\max\{0,X-D_q\}.
\end{aligned}
$$

Each nonempty intersection is an interval with its actual endpoint
conventions. Applying the same bound, including degenerate cases at the
breakpoints, proves

$$
\left|
|A\cap(L_q,X]|-T_q(X)
\right|\le18,
\qquad
T_q(X)=\frac{3\ell_1(X)}{2q}
+\frac{3\ell_2(X)}q+\frac{3\ell_3(X)}{2q}.
\tag{21}
$$

The equality $A(X)=A(L_q)+|A\cap(L_q,X]|$ is exact. Combining
(20) and (21) yields

$$
|A(X)-(3q+T_q(X))|\le18k+5.
\tag{22}
$$

On putting $x=X/q^2$, direct substitution of the three lengths gives
$3q+T_q(X)=qF(x)$, with $F$ as in the statement. For example, its
three normalized expressions are

$$
3+\frac32\left(x-\frac49\right),\qquad
3+\frac16+3\left(x-\frac59\right),\qquad
3+\frac16+\frac43+\frac32(x-1).
$$

They simplify to the three formulas for $F$. This proves the asserted
uniform estimate, including both ends of every cycle. It also explains
why using a count only at the cycle endpoints would be insufficient.

## Both exact extremal limits

Set $H(x)=F(x)/\sqrt x$ for $4/9\le x\le4$. For every real cutoff
in (22), $\sqrt X=q\sqrt x\ge2q/3$, so

$$
\left|\frac{A(X)}{\sqrt X}-H(X/q^2)\right|
\le\frac{3(18k+5)}{2\cdot3^k}.
\tag{23}
$$

The right-hand side tends to zero as $k\to\infty$. For example,
$k\le2^k$ for $k\ge1$, by induction, and hence
$k/3^k\le(2/3)^k\to0$. Every real $X\ge4$ lies in one of the
intervals $[4q^2/9,4q^2)$ with $q=3^k$, $k\ge1$, and the selected
$k$ tends to infinity with $X$. Thus (23) is an error tending to zero
uniformly over all sufficiently large real cutoffs, including seams.

To locate the extrema, for positive constants $a,b$ differentiate

$$
\frac{a}{\sqrt x}+b\sqrt x:
\qquad
\frac{d}{dx}\left(\frac{a}{\sqrt x}+b\sqrt x\right)
=\frac{bx-a}{2x^{3/2}}.
$$

On the first interval $[4/9,5/9]$, the values $a=7/3$, $b=3/2$
make this derivative negative. The profile decreases from $9/2$ to
$19/(2\sqrt5)$. On $[5/9,1]$, the values $a=3/2$, $b=3$ make
the derivative positive, so the profile increases from
$19/(2\sqrt5)$ to $9/2$. The common minimum of these two pieces
exceeds $3\sqrt2$, because both are positive and

$$
\left(\frac{19}{2\sqrt5}\right)^2
=\frac{361}{20}>18=(3\sqrt2)^2.
$$

On $[1,4]$, the profile is $3/\sqrt x+(3/2)\sqrt x$. Its derivative
is negative for $x<2$, zero at $2$, and positive for $x>2$. It has
value $9/2$ at both endpoints and minimum $3\sqrt2$ at $x=2$.
Consequently

$$
3\sqrt2\le H(x)\le\frac92
\quad\left(\frac49\le x\le4\right).
\tag{24}
$$

The uniform error (23) and (24) give

$$
\liminf_{X\to\infty}\frac{A(X)}{\sqrt X}\ge3\sqrt2,
\qquad
\limsup_{X\to\infty}\frac{A(X)}{\sqrt X}\le\frac92.
$$

For $X_k=q^2=3^{2k}$ the normalized argument is $1$ and
$H(1)=9/2$. Equation (23) therefore shows
$A(X_k)/\sqrt{X_k}\to9/2$. For $Y_k=2q^2=2\cdot3^{2k}$ it
shows $A(Y_k)/\sqrt{Y_k}\to3\sqrt2$, because $H(2)=3\sqrt2$.
Both sequences tend to infinity. They supply the reverse inequalities
for the upper and lower limits, proving both equalities in the statement.

## Dependencies

All essential deductions are given above using elementary integer and
real arithmetic. The argument uses no external theorem, no native
L-claim, and no computational premise. Its current verification standing
is recorded on the [claim page](_index.md).
