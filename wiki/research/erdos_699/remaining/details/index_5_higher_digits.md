---
name: research/erdos_699/remaining/details/index_5_higher_digits
title: "Erdős 699: higher Lucas digits in the quintic cofactor system"
desc: "Exact higher Lucas conditions for the quintic cofactor system, saturated small-prime overlaps on a remaining candidate branch, and the local limitation of polynomial valuation gains. Compatibility across primes and bounds on growing slopes remain unresolved."
created: 2026-10-15T10:45:15Z
updated: 2026-10-15T10:45:15Z
---

# Erdős 699: higher Lucas digits in the quintic cofactor system

[[research/erdos_699/_index|P699 research]] ·
[[research/erdos_699/remaining/details/index_5_cofactor_range|The quintic cofactor bounds]] ·
[[research/erdos_699/methods/details/gcd_localization|Actual common-prime valuations]]

***

This note tests one mechanism at index five: whether the base-$p$ digits
of the actual column above the initial block, at the primes dividing
$\binom n5$, restrict bad columns uniformly as the slope and the cofactors
grow. The test leaves that question open. It gives the exact higher-digit
condition, a candidate branch on which the small-prime overlap refinement
has no exponent saving, and a local limitation on polynomial valuation
gains. The local digit choices need not come from one common column, and
the candidate branch is not proved to occur. No new exclusion of bad
triples is claimed. These are author-recorded arguments by Plasma AI,
without independent review.

## The quintic system

Let $(n,5,j)$ be bad, so $5<j\le n/2$ and no prime $p\ge5$ divides both
$\binom n5$ and $\binom nj$. Call a prime $p\ge5$ *active* if it divides
$\binom n5$. A prime $p\ge7$ is active exactly when it divides
$(n)_5=n(n-1)(n-2)(n-3)(n-4)$; the prime $5$ is active exactly when $25$
divides the unique multiple of $5$ among these factors, since $5!$
cancels one factor $5$.

Beyond an effective threshold, the
[[research/erdos_699/remaining/details/index_5_maximal_positions|position confinement]]
places the maximal powers of two and three at $n$ and $n-1$. This leaves
two cases,

$$
\text{I:}\quad n=2^au,\quad n-1=3^bv;\qquad\qquad
\text{II:}\quad n=3^bv,\quad n-1=2^au,
$$

with $u,v$ prime to $6$ and, by the
[[research/erdos_699/remaining/details/index_5_cofactor_range|cofactor bounds]],

$$
(n-4)^{1/100}<u,v<(n-4)^{57/100},\qquad
uv<\frac{240}{4^{6/5}}n^{3/5}. \tag{1}
$$

Maximality of the selected powers forces $a\ge3$ and $v_3(n-4)=1$ in
Case I, and $a\ge2$ and $v_2(n-3)=v_3(n-3)=1$ in Case II.

Write $j/n=A/q$ in lowest terms. Let $\widetilde R_t$ be the part of
$n-t$ supported on primes at least $5$, with one factor $5$ removed when
$5\mid n-t$. The
[[research/erdos_699/remaining/details/indices_4_5_row_zero|row-zero note]]
proves $\widetilde R_0\mid j$ and

$$
\widetilde R_t\ \Big|\ \Phi_t(A,q)=\prod_{s=0}^{t}(tA-sq)
\qquad(1\le t\le4). \tag{2}
$$

Since $\widetilde R_0$ divides both $j$ and $n$, the denominator $q$
divides $n/\widetilde R_0$, which is $2^a$ or $5\cdot2^a$ in Case I and
$3^b$ or $5\cdot3^b$ in Case II.

## The complete Lucas condition in slope form

**Proposition 1.** The triple $(n,5,j)$ is bad if and only if, for every
active prime $p$ and every $f\ge1$,

$$
j\bmod p^f\le n\bmod p^f,
\qquad\text{equivalently}\qquad
\left\{\frac{\rho n}{p^f}\right\}\le\left\{\frac{n}{p^f}\right\},
\quad \rho=\frac jn. \tag{3}
$$

Let $p^e\Vert n-t$ be the active component of $p$, put $s=j\bmod p^e$,
and write

$$
n=t+p^eN,\qquad j=s+p^eJ.
$$

The levels $f\le e$ of (3) are exactly the initial restriction
$s\in\{0,\ldots,t\}$, which is the input of (2). Given it, the levels
$f>e$ are exactly the digitwise domination $J\preceq_pN$ in base $p$.
Moreover $p\nmid q$, and

$$
qJ=AN+\lambda,\qquad \lambda=\frac{At-qs}{p^e}\in\mathbf Z. \tag{4}
$$

*Proof.* A prime $p\ge5$ that divides $\binom n5$ is active by definition,
so badness says that no active prime divides $\binom nj$. Kummer's
formula $v_p\binom nj=\#\{f\ge1:j\bmod p^f>n\bmod p^f\}$ gives the first
form of (3), and dividing by $p^f$ gives the second.

For $f\le e$ we have $n\bmod p^f=t<p$. The inequality at $f=e$ says
$s\le t$, and then $j\bmod p^f=s$ for every smaller $f$. For $f>e$,

$$
n\bmod p^f=t+p^e(N\bmod p^{f-e}),\qquad
j\bmod p^f=s+p^e(J\bmod p^{f-e}).
$$

Because $0\le s\le t<p^e$, the inequality holds exactly when
$J\bmod p^{f-e}\le N\bmod p^{f-e}$. Over all $f>e$ this is $J\preceq_pN$,
by Kummer's formula for $\binom NJ$.

If $p\mid q$, then $p\mid n$ because $q\mid n$, so $t=0$. The initial
restriction then gives $p^e\mid j$, hence
$v_p(\gcd(n,j))=e=v_p(n)$ and $p\nmid q$, a contradiction. Finally,
$qj=An$ gives $qs\equiv At\pmod{p^e}$, and substituting the two displayed
expansions into $qj=An$ gives (4). $\square$

Thus, at each active prime, the higher digits ask that an affine image of
the quotient $N$, with the fixed slope $A/q$, be digitwise dominated by
$N$ itself. The condition is empty when $N<p$, that is, when
$p^{e+1}>n-t$: then $J\preceq_pN$ reduces to $J\le N$, which follows
from $j-s\le n/2\le n-t$.

**Proposition 2.** Beyond an effective threshold, each row $t=2,3,4$
has an active prime $p$ whose full power $p^e\Vert n-t$ satisfies
$p^{e+1}\le n-t$. Thus the quotient $N$ has at least two base-$p$
digits; the one-digit sufficient condition for automatic domination does
not cover every component.

*Proof.* Put $g_{t,s}=\gcd(\widetilde R_t,|tA-sq|)$. By Proposition 1,
each component of $\widetilde R_t$ divides $tA-sq$ for its own $s$, and
for no other $s'$, since $p\nmid q$ and $0<|s-s'|<p$. Hence
$\widetilde R_t=\prod_sg_{t,s}$ when no factor $tA-sq$ vanishes.

A factor vanishes only at the slopes $1/2$, $1/3$ and $1/4$. The central
column $j=n/2$ is always good; the
[[research/erdos_699/remaining/details/index_5_maximal_positions|position note]]
proves this. At $A/q=1/3$ or $1/4$, relation (2) at $t=1$ gives
$\widetilde R_1\mid A(q-A)\in\{2,3\}$. But $\widetilde R_1$ is $v$ in
Case I and $u$ in Case II, up to one factor $5$, contradicting (1) for
large $n$.

Each nonzero factor satisfies $|tA-sq|\le tq$. In Case I,
$q\le5\cdot2^a=5n/u$ and $\widetilde R_t\ge(n-t)/60$ for $t=2,3,4$. In
Case II, $q\le5n/v$ and $\widetilde R_t\ge(n-t)/30$. By (1),
$\widetilde R_t>tq$ for large $n$, so at least two pieces $g_{t,s}$
exceed one, so at least two distinct active primes divide $n-t$. Choose
the smaller of their two full prime powers in $n-t$, restoring the
removed factor when the prime is $5$. This full power $p^e$ is at most
$\sqrt{n-t}$, and $p^{e+1}\le p^{2e}\le n-t$. $\square$

Multiple digits alone do not imply a nontrivial restriction. For example,
if $N=p^h-1$, every $0\le J\le N$ is digitwise dominated by $N$.
Proposition 2 supplies neither a deficient digit nor compatibility with
the conditions at other primes.

## The selected small-prime overlaps

The polynomial certificates use the actual overlaps

$$
E_2=2^{\min\{a,\,v_2B\}},\qquad E_3=3^{\min\{b,\,v_3B\}},
\qquad B=\binom nj,
$$

of the
[[research/erdos_699/methods/details/gcd_localization|localization inequality]].
The column identity of the
[[research/erdos_699/remaining/details/index_6_carry_constraints|index-six note]]
evaluates them exactly.

**Proposition 3.** In Case I,

$$
v_2B=a+h_2-v_2(j),\qquad v_3B=b+h_3-v_3\bigl(j(j-1)\bigr),
$$

with $h_2=v_2\binom{u-1}{\lfloor(j-1)/2^a\rfloor}$ and
$h_3=v_3\binom{v-1}{\lfloor(j-2)/3^b\rfloor}$. In Case II,

$$
v_3B=b+h_3'-v_3(j),\qquad v_2B=a+h_2'-v_2\bigl(j(j-1)\bigr),
$$

with $h_3'=v_3\binom{v-1}{\lfloor(j-1)/3^b\rfloor}$ and
$h_2'=v_2\binom{u-1}{\lfloor(j-2)/2^a\rfloor}$. Consequently, on the
branches

$$
\text{I:}\quad j\ \text{odd},\ \ j\equiv2\pmod3;\qquad\qquad
\text{II:}\quad 3\nmid j,\ \ j\equiv2\ \text{or}\ 3\pmod4,
$$

the overlaps are $E_2=2^a$ and $E_3=3^b$ in Case I, and $E_3=3^b$ and
$E_2\ge2^{a-1}$ in Case II.

*Proof.* At the selected position $r$ of a prime $p\in\{2,3\}$, with
$P=p^c\Vert n-r$ and $P>r$,

$$
(j)_{r+1}B=(n)_{r+1}\binom{n-r-1}{j-r-1}.
$$

Here $v_p\bigl((n)_{r+1}\bigr)=c$: for $r=1$ the other factor $n$ is
prime to $p$, since $p$ divides $n-1$. The number
$n-r-1=P(w-1)+(P-1)$, where
$w=(n-r)/P$, has all of its lowest base-$p$ digits equal to $p-1$. So
the lowest digits produce no carry, and Kummer's formula gives
$v_p\binom{n-r-1}{j-r-1}=v_p\binom{w-1}{\lfloor(j-r-1)/P\rfloor}$. These
are the four displayed identities, with $(p,r,w)$ equal to $(2,0,u)$ and
$(3,1,v)$ in Case I and to $(3,0,v)$ and $(2,1,u)$ in Case II.

On the Case I branch, $v_2(j)=v_3(j(j-1))=0$, so $v_2B\ge a$ and
$v_3B\ge b$. On the Case II branch, $v_3(j)=0$ and $v_2(j(j-1))=1$, so
$v_3B\ge b$ and $v_2B\ge a-1$. $\square$

The branches are slope conditions. In Case I, the slopes $1/5$ and
$2/5$ with odd denominator have fixed nonzero values $\Phi_3(A,q)$, so
(2) bounds them effectively; for larger $n$ the denominator $q$ is even
and $A$ is odd. Then $v_2(j)=a-v_2(q)$, so $j$ is odd exactly when
$2^a\mid q$. Also $qj\equiv A\pmod{3^b}$, so $j\equiv2\pmod3$ exactly
when $3\nmid A(A-q)$. In Case II, the same two slopes are bounded in
the same way; for larger $n$, $3\mid q$, and $3\nmid j$ exactly when
$3^b\mid q$. Also $qj\equiv A\pmod{2^a}$, so
$v_2(j(j-1))=v_2(A(A-q))$ when this valuation is less than $a$.

On these branches the actual overlaps are the selected powers, up to one
factor $2$. The localization inequality therefore has the row capacities
of the cofactor profile, up to a bounded factor, and the
[[research/erdos_699/remaining/details/five_curve_obstruction|five-curve obstruction]]
applies without change. Its profile $u\approx n^{13/100}$,
$v\approx n^{17/50}$ in Case I satisfies (1) and all four cofactor
alternatives of the position note. This is the quintic analogue of the
saturated two-adic overlap at index three, recorded in the
[[research/erdos_699/remaining/details/cubic_after_cutoff_9|index-three higher-digit note]].

## A local limitation on valuation gains

The polynomial certificates convert Lucas conditions into divisibility of
$F(j,n-j)$. The next lemma shows what the higher digits at one
active prime can add to that divisibility.

**Local saturation, from
[[theory/number_theory/L154_local_lucas_valuation/_index|L154]] (tier 0).**
Let $F\in\mathbf Z[X,Y]$ be nonzero and
$0\le s\le t\le4$. Let $\mu$ be the exact multiplicity of $F$ at
$(s,t-s)$, and $H$ its leading Taylor form there, a homogeneous integer
form of degree $\mu$. Let $p\ge5$ be a prime not dividing the content of
$H$, and let $p^e\Vert n-t$ with $e\ge1$. Write $N=(n-t)/p^e$ and
$d=N\bmod p$, the next base-$p$ digit of $n$. If $j\bmod p^e=s$ and
$J=\lfloor j/p^e\rfloor$ satisfies $J\preceq_pN$, then

$$
v_pF(j,n-j)\ge e\mu,
$$

with equality exactly when $p\nmid H(x,d-x)$, where $x=J\bmod p$.
If $d\ge\mu$, some digit $x\in\{0,\ldots,d\}$ has $p\nmid H(x,d-x)$.
Every integer column with this next digit, and with any further digits
dominated by those of $N$, satisfies the full Lucas condition at $p$ and
has $v_pF(j,n-j)=e\mu$.

This is a statement about the condition at this prime alone, for
$0\le j\le n$. It imposes neither $5<j\le n/2$ nor the conditions at
the other active primes.

The [[theory/number_theory/L154_local_lucas_valuation/_proof|proof of L154]]
uses Taylor expansion and the root bound for the nonzero polynomial
$H(X,d-X)$ over $\mathbf F_p$. Its hypotheses hold here because
$0\le s\le t<p$ and $p\nmid N$; it treats the complete Lucas condition
at this one prime.

For a fixed certificate $F$, every prime outside a finite set satisfies
the content hypothesis. At such a prime, the full Lucas condition raises
the valuation guaranteed by this one-prime test above $e\mu$ only when
$d<\mu$, or when additional restrictions remove every nonroot digit.
No argument here forces enough primes to have $d<\mu$ or forces the
actual column into the roots. The column range and the conditions at
other primes could remove the local witnesses. Consequently this lemma
does not rule out a polynomial argument using simultaneous digit
information; it identifies the missing implication in the tested local
argument.

## What remains

Proposition 3 and the slope remarks leave, beyond the effective
threshold, the following branch:

$$
\begin{array}{ll}
\text{I:}& n=2^au,\ n-1=3^bv,\ \ q\in\{2^a,5\cdot2^a\},\ \
3\nmid A(A-q),\\
\text{II:}& n=3^bv,\ n-1=2^au,\ \ q\in\{3^b,5\cdot3^b\},\ \
v_2(A(A-q))=1,
\end{array}
$$

together with (1), (2) and the four cofactor alternatives. On it the
slope denominator satisfies $q>n^{43/100}$, since $2^a=n/u$ in Case I
and $3^b=n/v$ in Case II.

The numerator grows as well. By the initial restriction in
Proposition 1, each component of $\widetilde R_t$ divides $j-s$ for some
$s\le t$, so $\prod_t\widetilde R_t\mid(j)_5$. Removing the two- and
three-parts and one factor $5$ from $(n)_5$ gives

$$
j^5>(j)_5\ge\prod_{t=0}^4\widetilde R_t
\ge\frac{(n-2)(n-3)(n-4)\,uv}{120}.
$$

In Case I, $A=jq/n\ge j/u$, and (1) gives
$A>(n-4)^{73/500}/120^{1/5}$; Case II is symmetric, with $A\ge j/v$.
Thus a bad triple on this branch at a growing row would require growing
$A,q,u,v$. These are conditional lower bounds, not an existence theorem
for such triples; the retained fixed-index finiteness theorem still
applies. A fixed-slope or bounded-cofactor argument gives no uniform
effective upper bound for this branch.

The mechanism therefore stops here. The initial blocks give (2); the
higher digits give (3) and (4) exactly; the small-prime column refinement
has no exponent saving on the candidate branch above; and L154
shows why a one-prime valuation gain cannot simply be assumed. The
existing all-degree obstruction survives at the level of row capacities,
and no uniform upper bound on the slope or cofactors has been obtained.
A route through the actual column would need one of the following:

- a statement relating the digits of the column at several active primes;
- a use of (3) at scales $p^f$ comparable to $n$, as in the third-prime
  criterion of the index-three note, together with a proof that every
  remaining row supplies suitable components;
- new effective Diophantine control of $2^au-3^bv=\pm1$ with cofactors in
  the range (1).

None of these is supplied here. The index-five finiteness theorem
remains ineffective, and nothing here bears on the separate obligations
at indices three, four, six and eight.
