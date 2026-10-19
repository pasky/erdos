---
name: research/erdos_699/remaining/details/cubic_uniform
title: "Erdős 699: a uniform cubic proof attempt"
desc: "Integer moments, an incomplete Vieta argument, and a two-prime full-Lucas criterion excluding rows with suitably sized prime-power factors of n-1 and n-2. Global finiteness remains unproved."
created: 2026-09-21T21:11:29Z
updated: 2026-09-22T01:18:10Z
---

# Erdős 699: a uniform cubic proof attempt

[[research/erdos_699/_index|P699 research]] ·
[[problems/factorials_binomials/E0699/_index|Erdős problem 699]] ·
[[research/erdos_699/remaining/details/cubic_followup|Earlier cubic reductions]]

***

The objective here is to prove that **no** admissible cubic counterexample
exists. This note records a uniform algebraic attempt, without extending any
finite computation. It does **not** complete that proof.

The useful outcome is an exact formulation in integer moments and a specific
obstruction to a Vieta argument: a second rational root is forced into
$(1,2)$, but its integrality does not follow from the argument.
The subsequent [irreducibility theorem](cubic_irreducibility.md)
shows that every hypothetical pair gives an irreducible integer cubic after
removing its exact power-of-two content. A separate
[five-point argument](cubic_weighted.md) rules out improving
the uniform polynomial certificate merely by removing powers of two from $n$.
The [moment surface note](../../archive/other_approaches/cubic_surface.md) analyzes a
quadratic involution and proves that every even column obstructs its
required dyadic normalization.

## 1. A sufficient uniform target

Suppose that no odd prime divides both $\binom n3$ and $\binom nj$, where
$4\le j\le n/2$. The elementary reductions in the earlier notes give

$$
n=2^h u,\qquad h\ge2,\quad u\text{ odd},\qquad j<n/2.
$$

Put $c=n-j$ and

$$
W=\frac{u(n-1)(n-2)}6.
$$

Badness implies the two divisibilities

$$u(n-1)\mid3jc,\qquad
u(n-1)(n-2)\mid j(j-1)(j-2).\tag{1}$$

Equivalently, every coefficient of

$$
P(z)=\frac1W\sum_{r=0}^3\binom j{3-r}\binom cr z^r\tag{2}
$$

is an integer. For completeness, the endpoint criterion from the earlier
note gives the prime-power restrictions
$j\bmod p^a\in\{0,\ldots,t\}$ for each active component
$p^a\Vert n-t$, $t=0,1,2$. Each such restriction makes the $p$-part of
$W$ divide every coefficient in (2), including when $p=3$. Conversely,
integer coefficients include the two endpoint divisibilities, which imply
(1).

Since $P(1)=2^h$, this says that all four probabilities

$$
\frac{\binom j{3-r}\binom cr}{\binom n3},\qquad 0\le r\le3,
$$

are dyadic rationals. They are the probabilities of the four color counts
when drawing three objects without replacement from populations of sizes
$j$ and $c$.

Thus the following statement would suffice to settle the cubic case:

> For $n=2^h u$, $h\ge2$, $u$ odd, and $4\le j<n/2$, the two
> divisibilities (1) cannot both hold.

This is a **stronger sufficient target**, not an established equivalence
with badness. Conditions (1) only retain the initial prime-power blocks of
the Lucas conditions. A pair satisfying them could still have a carry in a
higher base-$p$ digit and therefore be good for the original problem.

## 2. An integer cubic equation retaining the moments

Write $P(z)=p_0+p_1z+p_2z^2+p_3z^3$. Define

$$\begin{aligned}
s&=3\cdot2^h,\\
m&=3p_0+2p_1+p_2=\frac{3j}{u},\\
\ell&=3p_0+p_1=\frac{3j(j-1)}{u(n-1)},\\
a&=3p_0=\frac{3j(j-1)(j-2)}{u(n-1)(n-2)}.
\end{aligned}\tag{3}$$

All four quantities are integers, and $3\mid a$. The factors of three
are necessary: the unscaled first and second moments need not be integers
when the factor $3$ in $\binom n3$ has been canceled.

The parameters satisfy

$$
s>2m>4\ell>8a>0,\tag{4}
$$

and the exact identities

$$\begin{aligned}
u(s\ell-m^2)&=3(\ell-m),\\
u(sa-\ell m)&=6(a-\ell).
\end{aligned}\tag{5}$$

The first identity follows by substituting (3); the second also follows
from $a/\ell=(j-2)/(n-2)$. Eliminating $u$ gives the homogeneous cubic

$$
sa(\ell+m)-2am^2+m\ell^2+m^2\ell-2s\ell^2=0.\tag{6}
$$

Conversely, suppose $s=3\cdot2^h$, $u$ is odd, and integer
$m,\ell,a$ satisfy (5), with $3\mid a$, and with
$j=um/3$ an admissible integer for $n=us/3$.
The two linear equations (5) then give exactly the moment expressions
in (3). The inverse formulas

$$p_0=\frac a3,\quad p_1=\ell-a,\quad
p_2=m-2\ell+a,\quad
p_3=\frac s3-m+\ell-\frac a3\tag{7}$$

show that (2) has integer coefficients. This recovers (1).
Equation (6) on its own is weaker: it must be accompanied by the odd
integer $u$, the identities (5), and the reconstruction of $n,j$.

This reformulation treats every exponent $h$ at once. It supplies no
contradiction merely from the fact that $s/3$ is a power of two.

## 3. A second root strictly between one and two

There is a short Vieta argument that comes close to an integer
contradiction. Put

$$A=p_0=\frac{j(j-1)(j-2)}{u(n-1)(n-2)},\qquad
L=\ell=\frac{3j(j-1)}{u(n-1)}.$$

Both are positive integers. Their defining equations give

$$n-1=\frac{3j(j-1)}{uL},\qquad
n-2=\frac{L(j-2)}{3A}.$$

Subtracting yields

$$
9A j^2-(9A+uL^2)j+2uL^2-3AuL=0.\tag{8}
$$

The other root of this integer quadratic is

$$\begin{aligned}
j^*&=1+\frac{uL^2}{9A}-j\\
&=1+\frac{jc}{(n-1)(j-2)}.
\end{aligned}\tag{9}$$

**Lemma.** Under (1) and the admissibility conditions above,

$$
1<j^*<2.
$$

**Proof.** The lower bound is immediate from (9). Since $A\ge1$,

$$
u(n-1)(n-2)\le j(j-1)(j-2).
$$

As $n>2j$, we have $(j-2)/(n-2)<1/2$. Consequently

$$
2(n-1)\le2u(n-1)<j(j-1).
$$

But direct subtraction in (9) gives

$$2-j^*=
\frac{j(j-1)-2(n-1)}{(n-1)(j-2)}>0.$$

This proves the lemma. $\square$

If $j^*$ were an integer, the proof would be finished. The missing
assertion is precisely

$$
9A\mid uL^2.\tag{10}
$$

Neither having integer coefficients in (8) nor having one integer root
implies (10), since the quadratic is not monic. In fact the lemma shows
that **any** hypothetical solution of (1) must violate (10).
Thus (10) cannot be treated as a routine cancellation step: proving it
from badness would itself complete the contradiction.

The reduced denominator of $j^*$ is exactly

$$\frac{9A}{\gcd(9A,uL^2)}
=\frac{(n-1)(j-2)}{\gcd(jc,(n-1)(j-2))}>1.\tag{11}$$

It divides $3(j-2)$, because $(n-1)\mid3jc$. This identifies where an
attempted integral descent fails. Apart from the prime $3$, its denominator
can contain primes from $j-2$ that need not divide $\binom n3$ at all.
The original no-carry hypothesis gives no direct condition at such primes.
This observation does not prove that the full Lucas conditions are
insufficient; it explains why they cannot simply be cited to justify (10).

Even a prime dividing $\binom n3$ can remain in that denominator while
obeying its full Lucas condition. To see this in an infinite family, let
$p\ge13$ be a prime with $p\equiv1\pmod4$, let $b>a\ge1$, and put

$$
n=5p^b+p^a+2,\qquad j=p^b+2,\qquad c=4p^b+p^a.
$$

Then $4\mid n$, $4\le j<n/2$, and $p^a\Vert n-2$, so $p$ is active.
The nonzero base-$p$ digits of $n$ are $5,1,2$ at positions $b,a,0$,
respectively, while those of $j$ are $1,2$ at positions $b,0$.
Every digit of $j$ is at most the corresponding digit of $n$; Lucas's
theorem therefore gives $p\nmid\binom nj$. Nevertheless,

$$v_p(j-2)=b,\qquad v_p(c)=a,\qquad
v_p(j)=v_p(n-1)=0.$$

Consequently the reduced denominator of the rational expression
$1+jc/[(n-1)(j-2)]$ contains exactly $p^{b-a}$ in its $p$-part.
This family satisfies the full condition at **one** active prime, not the
conditions at every active prime or the two global divisibilities (1).
It is not a family of counterexamples. It shows that a full Lucas
condition at an individual prime does not supply the cancellation needed
in (10), even when that prime divides $\binom n3$.

Clearing the denominator in $0<2-j^*<1$ does yield a positive integer:

$$\begin{aligned}
E&=9A(j+1)-uL^2\\
&=\frac{9j(j-1)\bigl(j(j-1)-2(n-1)\bigr)}
{u(n-1)^2(n-2)}>0.
\end{aligned}\tag{12}$$

However, the range $j<n/2$ does not make $E<1$. For example, with $u=1$
and $j/n$ tending to a fixed $\theta\in(0,1/2)$, the displayed rational
expression is asymptotic to $9\theta^4 n$. Thus merely clearing the
denominator and estimating the resulting integer does not finish the
Vieta argument.

## 4. A row-halving attempt does not yet give a descent

One other transformation can be written particularly simply in the
subcase where

$$M=\frac{j(j-1)}{n-1},\qquad
Q=\frac{j(j-1)(j-2)}{(n-1)(n-2)}$$

are integers. This subcase must not be assumed without proof in the
general cubic problem, because of the possible canceled factor of three.

The equations imply

$$
\frac{M(M-2)}{n-2}=Q(j+1)-M^2\in\mathbb Z.\tag{13}
$$

Since $4\mid n$ and $n-1$ is odd, $M$ is even. Put $x=M/2$ and
$N=n/2$. Equation (13), with $N-1$ odd, implies

$$
N-1\mid x(x-1).\tag{14}
$$

Here $0<x<N/4$, so the transformation does give a smaller integer
parameter. It does **not** reproduce both cubic conditions for $(N,x)$.
The next numerator factor would be $N-2=(n-4)/2$, whose odd primes
are not generally among the primes controlled by the original hypothesis.
The full Lucas hypothesis concerns primes dividing $\binom n3$;
it does not automatically supply a condition at these new primes.
Iteration of (14) is therefore not justified.

Full Lucas conditions also fail to transfer prime by prime under this
map. For example, $(n,j)=(372,106)$ has $M=30$ and gives
$(N,x)=(186,15)$. At the active prime $5\mid n-2$, the original
digits satisfy

$$
n=(2442)_5,\qquad j=(0411)_5,
$$

so the original Lucas test passes. But

$$
N=(1221)_5,\qquad x=(0030)_5,
$$

and the transformed test fails. This pair is not a cubic counterexample;
it shows that any preservation argument would need simultaneous
information from other primes. The solved index-two case alone is
insufficient as well, since its permitted common prime includes two.

## 5. A further restriction from the full Lucas conditions

The initial prime-power blocks used in (1) do not exhaust badness.
Here is one way to retain higher digits. Call an odd prime $p$ active
when $p\mid\binom n3$.

**Lemma.** For any bad triple and any power of an active prime with
$n/2<p^b\le n$, one has

$$
j\le n-p^b.\tag{15}
$$

**Proof.** Since $j<n/2<p^b$, all its base-$p$ digits at positions $b$
and above vanish. Lucas's theorem and $p\nmid\binom nj$ say that
each remaining digit is at most the corresponding digit of $n$.
Consequently $j\le n\bmod p^b$. Since $p^b\le n<2p^b$, this
remainder is $n-p^b$. $\square$

In particular, an active prime power in that interval excludes the entire
row if

$$
(n-p^b)^3\le u(n-1)(n-2).\tag{16}
$$

Indeed, (1), positivity, and (15) would imply

$$u(n-1)(n-2)\le j(j-1)(j-2)<j^3
\le(n-p^b)^3,$$

contradicting (16). This is a uniform sufficient criterion, rather than a
finite computation. To turn it into a proof of finiteness, one would need
to show that every sufficiently large remaining row has such an active
prime power. No argument establishing that assertion is known here.
Prime-power gap estimates alone would not suffice: the base prime must
divide $\binom n3$.

The positions of the permitted residues give a stronger criterion when
two active prime powers are available. It does not require either prime
power to lie within $O(n^{2/3})$ of $n$.

**Two-prime criterion.** Suppose there are powers $P=p^a$ and $Q=q^b$
of active odd primes such that

$$P\mid n-1,\qquad Q\mid n-2,\qquad
P,Q\le\sqrt n,\qquad PQ\ge\frac{2n}{3}.\tag{17}$$

Then the row has no bad column $4\le j<n/2$.

**Proof.** Put $T=PQ$, $R=n-T$, and $U=\max(P,Q)$. Since $P$ and
$Q$ divide consecutive integers, they are coprime and distinct. In
particular, the distinct odd integers $P,Q$ differ by at least two.
We have

$$\frac n2<U^2\le n,\qquad
U^2=T+U|P-Q|.$$

The prime underlying $U$ is active, so (15), applied to its power $U^2$,
gives

$$
j\le M:=n-U^2=R-U|P-Q|<R-1.\tag{18}
$$

Also $R\ge U|P-Q|>2$, since $U^2\le n$. The initial Lucas blocks give

$$j\equiv\varepsilon\pmod P,\quad
j\equiv\delta\pmod Q,\qquad
\varepsilon\in\{0,1\},\quad\delta\in\{0,1,2\}.$$

Their six Chinese remainder classes are represented by
$\delta(n-1)-\varepsilon(n-2)$ modulo $T$. Because
$R\le T/2$, their representatives in $[0,T)$ are exactly

$$
0,\quad1,\quad R-1,\quad R,\quad2R-2,\quad T-R+2.\tag{19}
$$

Every entry other than $0,1$ is at least $R-1$. But (18) gives
$0\le j<R-1<T$. Thus $j\le1$, a contradiction. $\square$

**The adjacent product range leaves two explicit columns.** Retain the
prime-power and divisibility assumptions in (17), but instead suppose

$$
\frac n2<PQ<\frac{2n}{3}.
$$

The same argument still gives (18), since $U^2\ge PQ>n/2$.
Now $T/2<R<T$. The classes $R-1$ and $R$ remain excluded by (18).
The class $2R-2$ can enter the permitted interval only after subtracting
$T$, while $T-R+2$ is already in $[0,T)$. Consequently every hypothetical
bad column must be one of

$$
\boxed{j=2n-3PQ-2\quad\text{or}\quad j=2PQ-n+2.}\tag{20}
$$

A displayed value is retained only if
$4\le j<n/2$ and $j\le n-\max(P^2,Q^2)$; values outside these ranges
are discarded. The two displayed expressions sum to $n-PQ$.
If the unreduced representative $2R-2$ is less than $T$, it exceeds
$R-1$ and contributes no candidate, consistently with its expression
in (20) being negative.

**Completing the adjacent range.** Suppose in addition that $P$ is the
full prime-power component $p^{v_p(n-1)}$. In the range
$n/2<T<2n/3$, the second column in (20) is always excluded. The first is
also excluded unless $v_3(n-1)=1$; in that exceptional case it must satisfy
the additional cofactor equation below. When $n$ is a power of two, the
exceptional case is excluded as well.

Put

$$A=\frac{n-1}{P},\qquad B=\frac{n-2}{Q},\qquad
g=\begin{cases}3,&v_3(n-1)=1,\\1,&v_3(n-1)\ne1.\end{cases}$$

Here $A/g$ is an odd integer: if $g=3$, the active prime underlying $P$
cannot be $3$. Fullness of $P$ gives $\gcd(A,PQ)=1$.
The size assumptions and $R>2$ give

$$
A\ge P,\qquad P<B<2P,\qquad PA-QB=1.\tag{21}
$$

Indeed, $PA=n-1\ge P^2-1$ gives $A\ge P$ by integrality;
$n-2>T$ gives $B>P$; and $n<2T$ gives $B<2P$.
Since $4\mid n$, we also have

$$
A\equiv-P\pmod4,\qquad B\equiv2\pmod4.\tag{22}
$$

First consider $j=2T-n+2$. At each full active component of $A$, the
initial Lucas block requires $j\equiv0$ or $1$. Modulo that component,
$j\equiv2T+1$, and the alternative $2T\equiv0$ is impossible because
the component is odd and coprime to $T$. All those components therefore
divide $2T+1$. Their product is $A/g$, so, using $QB=PA-1$,

$$\frac Ag\mid2T+1
\quad\Longrightarrow\quad
\frac Ag\mid2P-B.$$

But (21) gives $0<2P-B<A$, while (22) gives $4\mid2P-B$.
Since $A/g$ is odd, the positive quotient $(2P-B)/(A/g)$ must be a
multiple of $4$. It is also less than $g\le3$, a contradiction.

Now consider $j=2n-3T-2=2(n-1)-3T$. If $P$ is not a power of $3$
and $v_3(n-1)\ge2$, then $3\nmid T$ and $v_3(j)=1$. This violates
the initial Lucas block at the full active power of $3$ in $n-1$.
Exclude this case first. In every remaining case, the prime-power
components of $A/g$ are coprime to $3T$. At each one,
$j\equiv-3T$ can equal only the Lucas residue $1$, so

$$\frac Ag\mid3T+1
\quad\Longrightarrow\quad
\frac Ag\mid3P-B.$$

Consequently the integer

$$
k=\frac{3P-B}{A/g}
$$

satisfies $0<k<2g$ by (21). Equation (22) gives
$k\equiv-g\pmod4$. If $g=1$, these conditions are inconsistent.
If $g=3$, then $Q\ge5$ because $3\mid n-1$. The inequality
$T<2n/3$ gives $2B+4/Q>3P$. Since $2B$ is even, $3P$ is odd,
and $4/Q<1$, it follows that $B>3P/2$. Thus

$$
0<k=\frac{3(3P-B)}A<\frac{9P}{2A}\le\frac92.
$$

Together with $k\equiv1\pmod4$, this forces $k=1$. The only
remaining possibility in the adjacent range is therefore

$$v_3(n-1)=1,\qquad j=2n-3PQ-2,\qquad
A=3(3P-B).\tag{23}$$

For a pure power $n=2^h$, the condition $v_3(n-1)=1$ forces $h$ even.
Write $n=x^2$, where $x$ is a power of two and $x\ge4$.
Since $PQ>x^2/2$ and $Q\le x$, we have $P>x/2$.
The coprime odd integers $x-1,x+1$ have product $n-1$, so the full
prime-power component $P$ lies entirely in one of them. Its cofactor
there is an odd positive integer less than
$2(x+1)/x<3$, hence equals $1$. The condition $P\le x$ consequently
forces

$$
P=x-1,\qquad A=x+1.
$$

But (23) now gives

$$
B=3P-\frac A3=\frac{8x-10}{3}>2(x-1)=2P,
$$

contradicting (21). This completes the exclusion. $\square$

**Extended two-prime criterion.** The threshold in (17) can therefore be
replaced by $PQ>n/2$, provided $P$ is the full active prime-power
component of $n-1$ and either $v_3(n-1)\ne1$ or $n$ is a power of two.
In particular, for every row $n=2^h$, full $P$ and any $Q$ satisfying
the remaining assumptions exclude every bad column as soon as $PQ>n/2$.

This criterion uses a higher Lucas digit through (18), together with
the positions of the initial residue classes and the remaining active
components of $n-1$. It is a conditional
exclusion of entire rows, not a global finiteness theorem. What remains
missing is a supply of suitable prime powers for all remaining rows, or
a different argument for rows where their cross-products are too small.
No finite search is used in (17)–(23).

A fixed list of small primes cannot cover all the remaining rows, either.
In fact, for every $B\ge3$ there are infinitely many $h$ such that
$\binom{2^h}{3}$ has no odd prime divisor at most $B$. To see this, put

$$
L=\operatorname{lcm}\{p(p-1):3\le p\le B,\ p\text{ prime}\}
$$

and take $h\equiv2\pmod L$, with $h$ arbitrarily large. Euler's theorem
gives $2^h\equiv4\pmod{p^2}$ for every listed prime. For $p\ge5$,
division by $6$ modulo $p$ gives $\binom{2^h}{3}\equiv4\pmod p$.
For $p=3$, the congruence $2^h\equiv4\pmod9$ gives
$v_3(2^h-1)=1$, so the factor $3$ is exactly canceled by $3!$.
Thus all these primes are inactive. A proof using Lucas must therefore
allow its chosen primes to grow with the row.

## 6. Status of the proof attempt

The established statements in this note are the exact reformulations
(2)–(7), the lemma $1<j^*<2$, the denominator formula (11), the identity
(12), the limited transformation (13)–(14), and the full-Lucas restriction
(15)–(16), the two-prime exclusion criterion (17)–(19), the two-column
restriction (20), and its extension through the cofactor restrictions
(21)–(23). The algebraic identities were checked symbolically;
none uses a finite search or a numerical cutoff.

The uniform nonexistence assertion remains unproved. The Vieta route needs
a valid integrality argument for its second root; the row-halving route
needs a proof that the cubic hypotheses are preserved. Neither missing
step is supplied here, and the earlier computational evidence is not used
as a substitute for either one.
