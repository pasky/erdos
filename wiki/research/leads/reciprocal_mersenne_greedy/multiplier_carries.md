---
name: research/leads/reciprocal_mersenne_greedy/multiplier_carries
title: Half Expansions with Finitely Many Multipliers
desc: |
  Half expansions for at most four geometric multipliers containing 1,
  an exact seed criterion and doubling extension, and the residual bounds
  needed to exclude a seed's first failure. Mixed carries of a half-target
  two-cycle force a borrow block but do not splice the ordinary carries.
  Full-weight doubling blocks reduce exactly to the gap test and require
  variable terminal carries. Seeds for unbounded initial segments, which would
  give the full Mersenne half expansion, are unproved.
tags: []
sources: []
problems:
- 257
created: 2026-10-17T00:00:00Z
updated: 2026-10-17T00:00:00Z
---

# Half Expansions with Finitely Many Multipliers

***

The arguments below, except where a source is named, are Plasma AI's,
credited to Plasma AI. They are author-recorded and unreviewed. This page
supports the [[research/leads/reciprocal_mersenne_greedy/proof_sketch|canonical sketch]];
it proves no rational membership for the full Mersenne weights.

## The multiplier reduction

For a finite set $C\subseteq\mathbb N$ containing $1$, put

$$
v_n(C)=\sum_{a\in C}2^{-an},\qquad
U_n(C)=\sum_{k>n}v_k(C)
=\sum_{a\in C}\frac{2^{-an}}{2^a-1}.
$$

If $C\ne\{1\}$, then $v_n(C)>U_n(C)$: the terms for $a=1$ agree and
every other weight term is larger than its tail term. Thus any representation
of $1/2$ by these weights has the same digits as their actual greedy
expansion. Its first digit is zero, since $v_1(C)>1/2$. Throughout, including
the separate case $C=\{1\}$, the desired support is in $\{2,3,\ldots\}$.

Write $C=\{1\}\cup B$, set $\epsilon_1=0$, and define

$$
f_n=\sum_{\substack{a\in B\\a\mid n}}\epsilon_{n/a}.
$$

The coefficient of $2^{-n}$ in the expanded sum is
$\epsilon_n+f_n$. It therefore suffices to construct digits
$\epsilon_n\in\{0,1\}$ and integers $c_n$ with

$$
c_1=1,\qquad
\epsilon_n+f_n=2c_{n-1}-c_n\quad(n\ge2),\qquad
2^{-n}c_n\longrightarrow0.\tag{1}
$$

Indeed, telescoping gives
$\sum_{n=2}^N(\epsilon_n+f_n)2^{-n}=1/2-2^{-N}c_N$.
Nonnegative rearrangement then gives
$\sum_{n\ge2}\epsilon_nv_n(C)=1/2$. Conversely a representation supplies
these integer carries by the recurrence, and

$$
c_n=\sum_{r\ge1}(\epsilon_{n+r}+f_{n+r})2^{-r}
\quad\hbox{so that}\quad 0<c_n\le |C|.
$$

Here the strict lower bound follows from infinite support. No finite support
can represent $1/2$: if its largest element is $m\ge2$ and $J=\max C$,
multiplication by $2^{Jm}$ makes the left side odd, since only the term
with $(a,n)=(J,m)$ contributes an odd integer, and makes $1/2$ even.
This parity argument also covers $C=\{1\}$.

## A construction with at most three additional multipliers

**Proposition.** For every finite $B\subseteq\{2,3,\ldots\}$ with
$|B|\le3$, there is an infinite $A\subseteq\{2,3,\ldots\}$ such that

$$
\sum_{n\in A}\left(2^{-n}+\sum_{a\in B}2^{-an}\right)=\frac12.
$$

There is an explicit recursive construction with $c_n\in\{1,2\}$.
For nonempty $B$ its digits are the unique greedy digits for these weights.

*Proof.* Suppose the digits below $n\ge2$ have been chosen. Every $f_m$ for
$n\le m<2n$ is already determined: each summand uses $m/a<n$.
Bertrand's postulate supplies a prime $p$ with $n<p<2n$. At such a prime
$f_p=0$, since the only possible multiplier is $a=p$ and its digit is
$\epsilon_1=0$. Thus the least integer

$$
k(n)>n\quad\hbox{such that}\quad f_{k(n)}\ne1
$$

exists below $2n$ and can be found without choosing any further digit. Put

$$
h_1=0,\qquad
h_n=\begin{cases}
0,&f_{k(n)}=0,\\
1,&f_{k(n)}\ge2,
\end{cases}
\qquad
c_n=1+h_n,\qquad
\epsilon_n=1+2h_{n-1}-h_n-f_n.\tag{2}
$$

The calculation of $k(n)$ uses only already fixed digits, so a forecast made
at an earlier stage does not change when more digits are chosen. The four
possibilities for $f_n$ verify that $\epsilon_n$ is a bit:

| $f_n$ | Consequence for the states | $\epsilon_n$ |
| --- | --- | --- |
| $0$ | $h_{n-1}=0$ | $1-h_n$ |
| $1$ | $h_{n-1}=h_n$ | $h_n$ |
| $2$ | $h_{n-1}=1$ | $1-h_n$ |
| $3$ | $h_{n-1}=1$ and $h_n=0$ | $0$ |

For $n=2$, the first row applies because $f_2=0$ and $h_1=0$.
For $n>2$, if $f_n\ne1$, then $k(n-1)=n$, giving the indicated preceding
state. If $f_n=1$, then $k(n-1)=k(n)$, giving equal states. Finally, if
$f_n=3$, all three distinct multipliers in $B$ divide $n$. None divides
$n+1$, so $f_{n+1}=0$, $k(n)=n+1$ and $h_n=0$.

Equation (2) is exactly (1), and $1\le c_n\le2$ proves the required limit.
The parity argument proves infinite support. Strict domination of every tail
proves greedy agreement when $B$ is nonempty. For $B=\varnothing$, the
construction simply selects every $n\ge2$. $\square$

Bertrand's postulate is the only external theorem used in this construction;
its classical proof is not reproduced here. The prime need not be computed:
one can scan the already determined $f_m$ until its value is not $1$.

## Where this rule stops

The last row of the table uses $|B|\le3$. With four additional multipliers the
same rule can give a negative digit. For
$C=\{1,2,3,4,6\}$, the rule reaches $n=108$ with
$f_{108}=4$, $c_{107}=2$ and proposed $c_{108}=1$, hence proposes
$\epsilon_{108}=-1$. This refutes that extension of (2), not half membership
for these weights. The exact greedy prefix for this same $C$ instead has

| $n$ | $f_n$ | $c_{n-1}$ | $\epsilon_n$ | $c_n$ |
| --- | --- | --- | --- | --- |
| $106$ | $0$ | $1$ | $0$ | $2$ |
| $107$ | $0$ | $2$ | $1$ | $3$ |
| $108$ | $4$ | $3$ | $1$ | $1$ |

These are different prefixes from step 106 onward. The
[[research/leads/reciprocal_mersenne_greedy/evidence/_index|evidence entry point]]
reproduces both calculations in exact arithmetic. A rule allowing
larger carries must anticipate this kind of forcing before the final
preceding step and prove that its later choices remain compatible. The
window rule of Lemma 12 of the canonical sketch does anticipate it: with
these multipliers it uses the carries $1,2,3,1$ at steps $105$ to $108$, the
actual truncated greedy carries.

## An exact finite seed and a doubling extension

The bounded carries of a finite multiplier set give a constructive finite
criterion. This criterion does not prove that its seed exists for every
set of multipliers.

**Proposition.** Let $C$ be finite with $1\in C$, and let $M\ge2$ be a
common multiple of its elements. Put

$$
Q_C(M,d)=\sum_{\substack{a\in C\\ad\le M}}2^{M-ad}
\qquad(2\le d\le M).
$$

A half representation for $v_n(C)$ with support omitting $1$ exists if and
only if there is a set $D\subseteq\{2,\ldots,M\}$ with

$$
\sum_{d\in D}Q_C(M,d)=2^{M-1}-1.\tag{3}
$$

There is at most one such seed $D$. Given it, the following backward
recurrence constructs an infinite half representation while retaining all
proper-divisor contributions of its earlier digits.

*Proof.* Write $B=C\setminus\{1\}$ and $K=|B|$. First note the elementary
bound

$$
\sum_{a\in B}\frac1{2^a-1}
\le\sum_{a\ge2}\frac1{2^a-1}<\frac23,
$$

obtained by bounding each summand by $\frac43 2^{-a}$, with strict inequality
when $a>2$. If a half representation exists, its carry at the common
multiple $M$ is a positive integer by (1) and the infinite-support argument.
The contribution of the $a=1$ channel to its future coefficient tail is at
most $1$. For each $a\in B$, divisibility $a\mid M$ gives

$$
\sum_{d>M/a}\epsilon_d2^{M-ad}\le\frac1{2^a-1}.
$$

Hence $0<c_M<1+\frac23<2$, so $c_M=1$. Telescoping (1) through $M$
gives (3), with $D$ the support through $M$.

Conversely, a Boolean seed satisfying (3) has integer forward carries with
$c_1=c_M=1$. Reading the recurrence backward as
$c_{m-1}=(\epsilon_m+f_m+c_m)/2$ shows that these carries are positive and
at most $|C|$: each coefficient $\epsilon_m+f_m$ is between $0$ and $|C|$.

Suppose a prefix through $H=2^jM$ has been constructed and ends at $c_H=1$.
Every $f_m$ for $H<m\le2H$ is already determined by that prefix, because
$m/a\le H$ for $a\ge2$. Set $c_{2H}=1$, and for $m=2H,\ldots,H+1$ define

$$
c_{m-1}=\left\lceil\frac{f_m+c_m}{2}\right\rceil,
\qquad
\epsilon_m=2c_{m-1}-f_m-c_m\in\{0,1\}.\tag{4}
$$

These new digits affect forcing only at positions beyond $2H$, so they do
not change any $f_m$ used in this block. Repeatedly using
$\lceil(b+\lceil x\rceil)/2\rceil=\lceil(b+x)/2\rceil$ for integer $b$
shows that the carry calculated at the beginning of the block is

$$
\left\lceil\sum_{m=H+1}^{2H}f_m2^{H-m}+2^{-H}\right\rceil.
$$

Since every $a\in B$ divides $H$, the expression inside the ceiling is
positive and less than $\frac23+2^{-H}\le\frac{11}{12}<1$. Its ceiling is
therefore $1$, as required by the preceding prefix. Backward induction in
(4) gives $1\le c_m\le\max(1,K)$ throughout every new block. Iterating the
construction doubles the known prefix each time and keeps all carries
bounded. Equation (1) then telescopes to a half representation. The parity
argument already given makes its support infinite.

Finally the integer row is strictly superincreasing. The $a=1$ contribution
to $Q_C(M,d)-\sum_{k>d}Q_C(M,k)$ is $1$. Every $a\ge2$ contributes either
zero, when $ad>M$, or a positive number, since
$\sum_{k>d}2^{-ak}<2^{-ad}$. Thus two distinct subsets cannot have the same
row sum, and decreasing greedy on the integer weights decides (3).
$\square$

For example, $C=\{1,2,3,4,6\}$ and $M=12$ have the exact seed
$D=\{2,3,6,7,10\}$. The row sum is
$1361+585+65+32+4=2048-1$. Its doubling extension passes the carry-$3$
transition at steps $106$--$108$ where the earlier two-state rule fails.
Check 7 of the [[research/leads/reciprocal_mersenne_greedy/evidence/_index|evidence]]
reconstructs this seed and checks the extension, including every earlier
divisor contribution. It also checks other stated finite sets; none of those
checks supplies seeds for unbounded initial segments.

**Adjoining a common multiple.** If $C$ has a half representation and
$b\ge2$ is a multiple of every element of $C$, then $C\cup\{b\}$ has one
too. Use $M=b$: the old representation has carry $1$ at $b$, and the added
multiplier contributes nothing to $Q_C(b,d)$ for $d\ge2$. The same seed
therefore works in (3). This gives a uniform extension along divisibility
chains. Such a chain does not eventually contain every positive integer,
so it does not supply the approximation to all Mersenne multipliers.

**The full weights at doubling boundaries.** The doubling blocks have an
exact counterpart for the full weights $w_n=\frac1{2^n-1}$ of the
[[research/leads/reciprocal_mersenne_greedy/proof_sketch|canonical sketch]],
but the construction from $H=2$ cannot keep every boundary carry at $1$.
Let $H\ge2$ and $N=2H$, and suppose the greedy expansion of $\frac12$
has passed step $H$, so that its scaled residual
$s_H=2^Hr_H$ lies in $(0,\sigma_H]$ (Lemmas 4, 5 and 7 there). Encode digits
$\epsilon_{H+1},\ldots,\epsilon_N$ by the integer
$W=\sum_{d=H+1}^N\epsilon_d2^{N-d}$, and let
$G(W)=\sum_{d=H+1}^N\epsilon_d2^{N-d}w_d$ be the scaled mass that these
digits place beyond $N$. Because $2^Nw_d=2^{N-d}(1+w_d)$,

$$
s_N=2^Hs_H-W-G(W).
$$

By Lemma 4 of the sketch these digits are the greedy digits exactly when
$0\le s_N\le\sigma_N$, and $s_N\ne0$ because $\frac12$ is not a finite
subsum. Since $0\le G(W)<\frac8{21}$, each $w_d$ with $d\ge3$ being
at most $\frac87 2^{-d}$, and $\sigma_N<\frac{10}9$, an admissible word
satisfies $0<2^Hs_H-W<\frac32$, so at most two adjacent words qualify. If
$W\ge1$ and $k$ is the position of its last one, then $W-1$ replaces that one
by a zero and the following zeros by ones. Expanding
$2^Ng_k=2^Nw_k-2^N\sum_{d>k}w_d$ in the same way gives

$$
1+G(W)-G(W-1)-\sigma_N=2^Ng_k .
$$

The values of $2^Hs_H$ admissible for $W-1$ and for $W$ are therefore
separated by an open interval of length exactly $2^Ng_k$: the level-$k$ gap
of Lemma 2 of the sketch, scaled by $2^N$. Choosing between the two words is
Lemma 4 applied to the whole block. A rule that provably leaves an admissible
word at every doubling boundary is equivalent to Step 4 of the sketch, not a
weaker input, and the residual $s_H$ already holds everything that the choice
uses.

The carries give an explicit choice between the two words while retaining
the old prefix. For the target $\frac12$, Lemma 6 of the sketch gives
$c_N=P_N+s_N$, where $P_N$ is the pending contribution of the digits
through $N$. It splits as $P_N=E_H+G(W)$, with

$$
E_H=\sum_{\substack{d\le H\\\epsilon_d=1}}\frac{2^{N\bmod d}}{2^d-1}
$$

the part from the digits through $H$. Define

$$
K_H=2^Nr_H+E_H
   =2^{N-1}-\sum_{\substack{d\le H\\\epsilon_d=1}}
                  \left\lfloor\frac{2^N}{2^d-1}\right\rfloor,
\qquad u_H=\lfloor E_H\rfloor+1,
\qquad \rho_H=u_H-E_H.
$$

Thus $K_H$ is an integer, $0<\rho_H\le1$, and $c_N=K_H-W$.
An admissible block has
$E_H<c_N=E_H+G(W)+s_N<E_H+2$, because
$G(W)<8/21$ and $\sigma_N<10/9$. The only possible terminal carries
are therefore $u_H,u_H+1$, and the corresponding words are

$$
W_H=K_H-u_H,\qquad W_H-1.
$$

The word bounds and the endpoint cases are automatic. Indeed,
$W_H=2^Hs_H-\rho_H>-1$ and
$2^H(\sigma_H-1)<2/3$, so its integrality gives
$0\le W_H\le2^H$. If $W_H=0$, the zero block leaves scaled residual
$\rho_H\in(0,1]$. If $W_H=2^H$, choose the all-ones block $W_H-1$:
its scaled residual is $1+\rho_H-G(W_H-1)>0$, and its upper tail
bound follows by subtracting all weights in $(H,N]$ from
$r_H\le T_H$.

For an interior word $1\le W_H<2^H$, the two residuals are

$$
s_N(u_H)=\rho_H-G(W_H),\qquad
s_N(u_H+1)=1+\rho_H-G(W_H-1).
$$

The first is always at most $1$, and the second is always positive.
Consequently both candidates fail exactly when

$$
G(W_H-1)+(\sigma_N-1)<\rho_H<G(W_H).
$$

Equality at the left endpoint is admissible. Equality at the right
endpoint would give a finite half representation and is impossible by
Lemma 7 of the sketch. By the preceding separation identity the open
interval has length $2^Ng_k$, where $k$ is the last one of $W_H$.
This is a complete candidate-selection test, not a proof that one
candidate passes. Starting at $H=2$ with the selected index $2$, a proof
that this interval is avoided at every doubling boundary would construct
the full half representation. The unknown statement concerns these
half-rooted states, not arbitrary positive integer carries.
For another nonintegral dyadic target $q$ with $2^Nq$ integral, the same
formulas hold after replacing $2^{N-1}$ by $2^Nq$ in $K_H$, provided the
given prefix is admissible. They do not guarantee its later survival.

At the half target the same calculation applies to a fixed finite
multiplier set $C$:
replace $E_H$ and $G(W)$ by their sums over $a\in C$ with $ad>N$,
and replace $\sigma_n$ by $2^nU_n(C)$. The displayed full-weight bounds
still majorize the terms. At common-multiple boundaries the earlier seed
theorem proves the needed selection; it does not construct its starting
seed. Equivalence with the greedy test does not rule out proving a
selection invariant in these variables.

Since $c_N>E_H$, the half construction starting at $H=2$ cannot fix every
doubling-boundary carry at $1$. For a finite multiplier set at a common
multiple, the corresponding
pending mass is below $\frac23$, which is why the proposition above
restarts every block at carry $1$. No such bound holds for the full
weights. The greedy prefix of $\frac12$ through step $16$
is $\{2,3,6,7,14\}$ (Lemma 10 of the sketch), and

$$
E_{16}=\frac13+\frac47+\frac4{63}+\frac{16}{127}+\frac{16}{16383}
=\frac{376801}{344043}>1,
$$

so $c_{32}\ge2$. Check 10 of the
[[research/leads/reciprocal_mersenne_greedy/evidence/_index|evidence]]
checks the exact candidate carries and residuals along the certified half
prefix. Choosing the smaller candidate at every boundary also fails for
this same half orbit: at $H=32$ its old pending mass satisfies $E_{32}<1$,
but $c_{64}=2$, so the second candidate is required. Its different-target
control has both candidates fail: a
surviving dyadic prefix and an integer carry are insufficient hypotheses
for the missing uniform selection theorem.

## Transferring a seed to a larger multiplier set

An unchanged seed cannot usually be transferred when a multiplier is added.
This is an obstruction to that transfer rule, not to the existence of a
new seed.

Suppose $C$ has a half representation, $b\ge2$ is not in $C$, and $M$ is a
common multiple of $C\cup\{b\}$. Let $D$ be the seed for $C$ at $M$.
Every half representation omitting $1$ contains $2$. Indeed, for $n\ge3$,
$v_n(C)\le(2^n-1)^{-1}\le\frac87 2^{-n}$, so a support omitting both
$1$ and $2$ has sum at most $2/7<1/2$. Consequently

$$
\sum_{d\in D}Q_{C\cup\{b\}}(M,d)
=2^{M-1}-1+\sum_{\substack{d\in D\\bd\le M}}2^{M-bd}.
$$

If $M\ge2b$, the extra sum is at least $2^{M-2b}$, from $d=2$.
If $M=b$, the extra sum is zero. Since $b\mid M$, these are the only
possibilities. Thus reuse of the same seed at a common boundary is possible
exactly when $M=b$, the common-multiple adjoining case above. When $b$ is
not a common multiple of $C$, a proof must construct the changed seed or use
a boundary condition other than this carry-$1$ equation.

Even equality of the forcing coefficients up to a position does not
preserve the digits up to that position. At $M=6$ the sets

$$
C=\{1,2\},\quad D=\{2,3,5\},\qquad
C'=\{1,2,3\},\quad D'=\{2,3,6\}
$$

satisfy their respective seed equations:

$$
20+9+2=31,\qquad 21+9+1=31.
$$

The proved doubling extension supplies an infinite half representation in
each case, and uniqueness fixes these prefixes. Both have
$(f_2,f_3,f_4,f_5)=(0,0,1,0)$, but their digit and carry pairs at position
$5$ are $(\epsilon_5,c_5)=(1,1)$ for $C$ and $(0,2)$ for $C'$.
The new multiplier first contributes at position $6$, where the forcing
changes from $1$ to $2$. Its effect on the carry changes an earlier digit.
This refutes an extension rule that preserves the prefix below $2b$ merely
because the new multiplier contributes no coefficient there. It does not
refute the window rule, which already looks beyond the current position.

There is also an obstruction to replacing Boolean multiplier coefficients
by a continuous interpolation. Put

$$
v_n^{(\lambda)}=2^{-n}+\lambda4^{-n},\qquad
U_n^{(\lambda)}=2^{-n}+\frac\lambda3 4^{-n},
\qquad 0\le\lambda\le1.
$$

The endpoints $\lambda=0$ and $\lambda=1$ have half representations with
support omitting $1$, by the constructions for $C=\{1\}$ and $C=\{1,2\}$.
For $\lambda>0$, each weight strictly exceeds its tail, so a gap after
any prefix excludes half membership. The prefix $\{2,3\}$ has residual
$r=1/8-5\lambda/64$. At position $4$ it is a gap exactly when

$$
U_4^{(\lambda)}<r<v_4^{(\lambda)}
\quad\Longleftrightarrow\quad
\frac{16}{21}<\lambda<\frac{48}{61}.
$$

For the explicit value $\lambda=7/9$, this is

$$
U_4^{(7/9)}=\frac{439}{6912}
<r=\frac{444}{6912}
<v_4^{(7/9)}=\frac{453}{6912}.
$$

Thus solvability at the two Boolean endpoints does not persist throughout
their convex interpolation. An argument passing through fractional
multiplier coefficients must address these gaps; it cannot infer membership
from continuity or convexity alone. This example has a fractional
coefficient, so it neither disproves half membership for a Boolean
multiplier set nor resolves Problem 257.

## Adjoining the next multiplier

There is a necessary early interface for an induction on
$C_b=\{1,\ldots,b\}$. It does not assert that either of its prefixes has an
infinite continuation.

**Proposition.** Let $b\ge3$. Suppose $\epsilon$ represents $1/2$ for
$C_{b-1}$ and $\epsilon'$ represents $1/2$ for $C_b$. Put $N=2b-1$ and

$$
A_a(\epsilon)=\sum_{n\ge2}\epsilon_n2^{-an},\qquad
P_m(\epsilon)=\sum_{n=2}^m\epsilon_n2^{m-n}.
$$

The two supports agree through $b-1$. For their carries in (1), their
prefixes and carries at $N$ satisfy exactly one of

$$
\bigl(P_N(\epsilon'),c'_N\bigr)
=\bigl(P_N(\epsilon),c_N\bigr)
\quad\hbox{or}\quad
\bigl(P_N(\epsilon)-1,c_N+1\bigr).\tag{5}
$$

The second prefix is obtained by binary subtraction of one. If $k$ is the
last selected position of $\epsilon$ at or before $N$, it changes the digit
at $k$ from $1$ to $0$ and changes the following zeros through $N$ to ones.
This case requires $k\ge b$.

*Proof.* Write $F_C(\eta)=\sum_{a\in C}A_a(\eta)$. Then

$$
F_{C_{b-1}}(\epsilon)-F_{C_{b-1}}(\epsilon')
=A_b(\epsilon')>0.
$$

Strict domination of the weight tails makes $\epsilon$ lexicographically
larger. Each $A_a$ for $a\ge2$ is strictly increasing in that order, and
$A_1$ is nondecreasing. Equality of the two $A_1$ values would require the
larger word to terminate at the first differing digit; this is impossible
by the infinite-support parity argument. Thus, writing
$x=A_1(\epsilon)$ and $x'=A_1(\epsilon')$,

$$
0<x-x'\le A_b(\epsilon')\le\frac{4^{-b}}{1-2^{-b}},\qquad
0<2^N(x-x')\le\frac1{2(1-2^{-b})}<1.\tag{6}
$$

Let $k$ be the first differing position. If $k<b$, strict tail domination
and the multiplier $2\in C_{b-1}$ would give

$$
A_b(\epsilon')
\ge v_k(C_{b-1})-U_k(C_{b-1})
\ge\frac23\,4^{-k}
\ge\frac83\,4^{-b},
$$

contradicting $A_b(\epsilon')\le\frac87 4^{-b}$ from $b\ge3$. Hence the
supports agree through $b-1$.

To handle both binary expansions of dyadic values without choosing a new
convention, put
$\rho_N(\eta)=\sum_{j\ge1}\eta_{N+j}2^{-j}$. Infinite support gives
$0<\rho_N(\eta)\le1$ for both supports. By (6),

$$
0\le P_N(\epsilon)-P_N(\epsilon')
=2^N(x-x')-\rho_N(\epsilon)+\rho_N(\epsilon')<2.
$$

This integer is therefore $0$ or $1$. For $n\le N$, the new multiplier
$b$ contributes only $\epsilon'_1=0$, if it contributes at all. Every
proper multiplier in $C_{b-1}$ reads an index at most $b-1$, where the
supports agree. Their proper forcing is equal through $N$, so subtracting
(1) gives
$c'_n-c_n=P_n(\epsilon)-P_n(\epsilon')$ there. This proves (5).
Binary subtraction and the already proved agreement through $b-1$ give
the last assertion. $\square$

Conversely, both prefixes in (5), with the second discarded when its borrow
starts below $b$, satisfy the finite coefficient recurrence through $N$.
In the second case the carries equal the old carries before $k$ and are one
larger from $k$ to $N$. They lie in $[1,b]$, since the old carries lie in
$[1,b-1]$. This is only coefficient compatibility, not a tail bound for
the weighted residual and not extendibility. Already for $b=3$, the old
$C_2$ prefix $\{2,3,5\}$ has $c_5=1$. Keeping it would give, at the common
boundary $M=6$, $f'_6=2$ and
$\epsilon'_6=2c'_5-c'_6-f'_6=-1$ if $c'_6=1$. The decremented prefix
$\{2,3\}$ instead has $c'_5=2$ and extends by $\epsilon'_6=1$ to the
$C_3$ seed $\{2,3,6\}$.

### The signed repair equation

Fix $M=\operatorname{lcm}(1,\ldots,b)$ and let $\epsilon$ be the old seed
through $M$, supplied by its half representation. Set
$\delta_n=\epsilon'_n-\epsilon_n$ and $z_n=c'_n-c_n$. The exact repair
requires integer $\delta_n$ with
$-\epsilon_n\le\delta_n\le1-\epsilon_n$, and obeys

$$
\delta_n+
\sum_{\substack{2\le a<b\\a\mid n}}\delta_{n/a}
+\mathbf1_{b\mid n}(\epsilon_{n/b}+\delta_{n/b})
=2z_{n-1}-z_n,\qquad z_1=z_M=0.\tag{7}
$$

Here $\delta_1=0$, and the last summand is zero when $b\nmid n$.
Equivalently, the finite seed equation is

$$
\sum_{n=2}^M\delta_n Q_{C_b}(M,n)
=-\sum_{2\le n\le M/b}\epsilon_n2^{M-bn}.\tag{8}
$$

Equation (8) with the Boolean bounds on $\delta$ is necessary and
sufficient for a new seed: it subtracts the old row equation from the new
one, including exactly the excess of the added channel. By the proved seed
theorem, such a seed extends to an infinite half representation. Its
prefix must then be one of (5), and its integer carries automatically lie
in $[1,b]$. Thus (5) restricts the finite construction without proving
feasibility of (7) or (8). In particular, divisor contributions after the
first changed digit cannot be held fixed.

The carry changes cannot be required to stay nonnegative. At $M=60$ the
following are seeds for $C_4$ and $C_5$, respectively:

$$
\begin{aligned}
D_4={}&\{2,3,6,7,10,12,13,15,16,17,19,22,24,25,27,30,31,33,\\
&35,37,41,42,43,46,49,53,55,56,58,60\},\\
D_5={}&\{2,3,6,7,12,13,16,17,19,20,22,24,25,27,29,31,33,37,\\
&41,42,43,45,46,49,53,55,56,60\}.
\end{aligned}
$$

For each $j\in\{4,5\}$, their exact row sums are

$$
\sum_{n\in D_j}\sum_{\substack{1\le a\le j\\an\le60}}2^{60-an}
=576460752303423487=2^{59}-1.
$$

They therefore extend to the unique half representations of the seed
theorem. The finite carries computed from (1) include

| $n$ | $\epsilon_n$ for $C_4$ | $\epsilon'_n$ for $C_5$ | $c_n$ | $c'_n$ | $f_n$ | $f'_n$ |
| --- | --- | --- | --- | --- | --- | --- |
| 28 | 0 | 0 | 1 | 1 | 1 | 1 |
| 29 | 0 | 1 | 2 | 1 | 0 | 0 |
| 30 | 1 | 0 | 1 | 1 | 2 | 1 |

In particular $z_{29}=-1$. The change of forcing at $30$ is explicit:
for $C_4$ it reads the selected indices $15$ and $10$, whereas for $C_5$
those indices are absent and the new multiplier reads the selected index
$6$. Check 8 of the
[[research/leads/reciprocal_mersenne_greedy/evidence/_index|evidence]]
verifies the two row identities, all their finite carries and this table.
It refutes a nonnegative-carry repair invariant, not the existence of a
Boolean repair. The two-prefix proposition concerns only the early window
$n\le2b-1$ and is consistent with this later negative change.

An induction proving that at least one prefix in (5) has a completion
satisfying (8), for every $b\ge3$, would give all the initial segments
needed below. Its successive supports would also agree through $b-1$,
so every coordinate would eventually stabilize. The existence of those
completions remains unproved. A rule that permits signed carry changes and
controls their later divisor contributions is still needed; the finite
compatibility and the displayed successful seeds supply no such rule.

## The exact first failure of a seed

For the finite row in (3), abbreviate $Q_n=Q_C(M,n)$ and put
$T=2^{M-1}-1$. The remaining capacity after position $n$ is

$$
B_n=\sum_{d=n+1}^M Q_d
=\sum_{\substack{a\in C\\an\le M}}
  \frac{2^{M-an}-1}{2^a-1}.\tag{9}
$$

Indeed, $a\mid M$, so the last term of the geometric progression in
$d$ has exponent zero. The summand in (9) is zero when $an=M$.
Consequently the strict superincreasing margin is the integer

$$
Q_n-B_n
=1+\sum_{\substack{a\in C,\ a\ge2\\an\le M}}
  \frac{(2^a-2)2^{M-an}+1}{2^a-1}>0.\tag{10}
$$

Run decreasing greedy on this row, with $r_1=T$. At position $n$, select
$n$ exactly when $r_{n-1}\ge Q_n$, and subtract $Q_n$ if selected.
Initially $0\le T\le Q_2+B_2$, because the $a=1$ contributions alone sum
to $T$. If all preceding choices have left enough capacity, then
$0\le r_{n-1}\le Q_n+B_n$. Selecting $n$ leaves a remainder in
$[0,B_n]$. Skipping it leaves enough capacity exactly when
$r_{n-1}\le B_n$. Thus the first failure is precisely

$$
B_n+1\le r_{n-1}\le Q_n-1.\tag{11}
$$

Strict superincrease forces these greedy decisions in every possible
seed, so no alternative earlier Boolean choice repairs such a failure.
Conversely, if (11) never occurs, the last remainder lies in
$[0,B_M]=\{0\}$ and the seed is complete. For $n>M/2$ all proper
multipliers disappear, giving $Q_n=2^{M-n}$ and $B_n=Q_n-1$; (11) is
then empty. A first failure must therefore occur at $n\le M/2$.

There is an exact interface to the coefficient carries. For any Boolean
prefix $\eta_2,\ldots,\eta_n$, define its carries by (1), with
$\eta_1=0$, and retain its pending contribution beyond coefficient
position $n$:

$$
E_n=\sum_{d=2}^n\eta_d
       \sum_{\substack{a\in C\\n<ad\le M}}2^{M-ad}.
$$

Telescoping (1) through $n$ accounts for all contributions at positions
at most $n$. The other contributions of the selected prefix are exactly
$E_n$. Its row remainder therefore satisfies

$$
r_n=T-\sum_{d=2}^n\eta_dQ_d
    =2^{M-n}c_n-1-E_n.\tag{12}
$$

In particular, enough remaining capacity is equivalent to the two bounds

$$
1+E_n\le 2^{M-n}c_n\le1+E_n+B_n.\tag{13}
$$

A positive bounded coefficient carry alone does not imply these bounds:
the old $\{2,3,5\}$ prefix for the $C_3$, $M=6$ row, discussed above,
has $c_5=1$ and $E_5=2$, hence $r_5=-1$. It is not a valid prefix of
that row's greedy seed.

For $C_b=\{1,\ldots,b\}$, proving that the actual residual never enters
(11), for $2\le n\le M/2$ and unbounded $b$, would finish the seed route.
Equations (12)--(13) retain all later multiplier contributions, but do not
prove this avoidance. They expose the exact missing bound; no uniform
first-failure exclusion is established here.

## A whole-word iteration and its limitation

One alternative construction updates the entire binary word. For an
integer $0\le x\le T$, write

$$
x=\sum_{d=2}^M\eta_d(x)2^{M-d},\qquad
H_C(x)=\sum_{a\in C\setminus\{1\}}
       \sum_{2\le d\le M/a}\eta_d(x)2^{M-ad}.
$$

The seed equation is exactly $x+H_C(x)=T$, or the fixed-point equation
$x=\mathcal A(x)$ for $\mathcal A(x)=T-H_C(x)$. Each individual digit
expansion in $H_C$ is nondecreasing in $x$: at the first differing digit
its weight exceeds the sum of the later weights. Thus $H_C$ is
nondecreasing and $\mathcal A$ is nonincreasing. Moreover

$$
0\le H_C(T)
\le 2^M\sum_{a\ge2}\frac{4^{-a}}{1-2^{-a}}
\le\frac{2^M}{9}<T
$$

for $M\ge2$, so $\mathcal A$ maps the integer interval $[0,T]$ into itself.
Starting with $(\ell_0,u_0)=(0,T)$, define

$$
\ell_{j+1}=\mathcal A(u_j),\qquad
u_{j+1}=\mathcal A(\ell_j).\tag{14}
$$

These integer intervals are nested: the first is contained in $[0,T]$,
and antitonicity preserves containment at each subsequent step. Every
fixed point belongs to all of them. Eventually the interval stabilizes,
but the resulting equalities are only

$$
\ell=\mathcal A(u),\qquad u=\mathcal A(\ell).
$$

If $\ell=u$, its binary word is the required seed. If $\ell<u$, these
bounds form a two-cycle; nesting alone does not supply a fixed point or
exclude one between them.

This distinction matters even for this digit-expansion operator. Retain
$C=\{1,2\}$ and $M=12$, but replace the half-target row value $2047$ by
$t=1281$. Define $\mathcal A_t(x)=t-H_C(x)$ on $[0,t]$. Here

$$
H_C(x)=256\eta_2(x)+64\eta_3(x)+16\eta_4(x)
       +4\eta_5(x)+\eta_6(x).
$$

The exact values are

| $x$ | $H_C(x)$ |
| --- | --- |
| $0$ | $0$ |
| $1281$ | $272$ |
| $1009$ | $85$ |
| $1196$ | $260$ |
| $1021$ | $85$ |
| $1025$ | $256$ |

Iteration (14), with $t$ in place of $T$, gives

$$
(0,1281),\quad(1009,1281),\quad(1009,1196),\quad
(1021,1196),\quad(1021,1196),\ldots .
$$

Nevertheless $1025=1024+1$ is a fixed point. Its support $\{2,12\}$
has exact row sum

$$
Q_C(12,2)+Q_C(12,12)=(1024+256)+1=1281.
$$

Thus even a unique valid Boolean solution need not be obtained by the
extremal iteration. This example changes the target integer. It refutes
an argument based only on antitonicity, nesting and existence of a seed;
it does not refute collapse for $T=2^{M-1}-1$ or half membership.

A proof that (14) collapses for the half target and unbounded initial
segments $C_b$ would supply the missing seeds. That statement is unproved.
A nontrivial stabilized pair with first differing digit $k$ must satisfy

$$
0<u-\ell=H_C(u)-H_C(\ell)
\le \sum_{\substack{a\in C,\ a\ge2\\ak\le M}}
       \frac{2^{M-ak}}{1-2^{-a}}
\le\frac{16}{9}\,2^{M-2k}.\tag{15}
$$

For the first inequality, bound each differing expanded word by all its
terms from position $k$ onward; for the second, use $k\ge2$ and sum the
geometric series over $a$. The same computation bounds the change of the
expanded words caused by digits at positions $d\ge j$ alone by
$\frac{16}{9}2^{M-2j}$, for every $j\ge2$.

**Proposition (stable pairs).** Suppose (14) stabilizes at $\ell<u$. Let
$k$ be the first position at which their words differ, and let $Y$ be the
integer whose word agrees with that of $u$ through position $k$ and is zero
after it. Then $2k\le M$, and:

1. the words of $u$ and $Y$ agree through position $2k-1$, and so do the
   words of $\ell$ and $Y-1$;
2. if a seed $x$ exists, then $\ell\le x\le u$ and
   $|x-Y|\le\frac{16}{9}2^{M-4k}$. Hence either $x\ge Y$, the digit of $x$
   at $k$ is $1$ and its digits at $k+1,\ldots,\min(4k-1,M)$ are $0$, or
   $x<Y$, $4k\le M$, the digit of $x$ at $k$ is $0$ and its digits at
   $k+1,\ldots,4k-1$ are $1$;
3. if no seed exists, (14) stabilizes at a pair with $\ell<u$.

*Proof.* The stabilized equalities give $u-\ell=H_C(u)-H_C(\ell)$. If
$2k>M$, no expanded word reads a digit at a position $d\ge k$, so this
difference is $0$; hence $2k\le M$. By (15), $u-\ell<2^{M-2k+1}$. The word
of $\ell$ has $0$ at position $k$, so $\ell<Y\le u$, and both $u-Y$ and
$Y-\ell$ are less than $2^{M-(2k-1)}$. As $Y$ is a multiple of $2^{M-k}$,
this proves the first assertion.

Every integer in $[Y,u]$ therefore has the word of $Y$ through position
$2k-1$, and its expanded words exceed those of $Y$ only through digits at
positions $d\ge2k$; this excess is at most $\frac{16}{9}2^{M-4k}$. As
$\mathcal A$ is nonincreasing and $\mathcal A(u)=\ell$, it maps $[Y,u]$
into $[\ell,\ell+\frac{16}{9}2^{M-4k}]$. In the same way every integer in
$[\ell,Y-1]$ has the word of $Y-1$ through position $2k-1$, so
$\mathcal A$ maps $[\ell,Y-1]$ into $[u-\frac{16}{9}2^{M-4k},u]$. Every
fixed point lies in each interval of (14), so $\ell\le x\le u$. If $x\ge Y$,
then $x=\mathcal A(x)$ lies in the first image interval and $\ell<Y\le x$;
if $x<Y$, it lies in the second and $x<Y\le u$. Either way
$|x-Y|\le\frac{16}{9}2^{M-4k}<2^{M-(4k-1)}$. In the first case $x-Y$ is
therefore an integer in $[0,2^{M-(4k-1)})$, which gives the stated digits.
In the second case $Y-x$ is a positive integer below $2^{M-(4k-1)}$, so
$4k\le M$, and $x$ has the digits of $Y-1$ through position $4k-1$.
Finally, an iteration that stabilizes at $\ell=u$ yields a fixed point,
that is, a seed. $\square$

Besides the digit-expansion bounds, the proof uses that $\mathcal A$ is
nonincreasing and maps the starting interval into itself, not the value
of the target. It therefore applies unchanged to $\mathcal A_t$ for any
target $0\le t<2^{M-1}$. Indeed, each selected position $d\ge2$ contributes
at most $2^{M-d}/(2^d-1)\le2^{M-d}/3$ to $H_C(x)$, so
$0\le H_C(x)\le x/3$ and $\mathcal A_t$ maps $[0,t]$ into itself.

Thus the extremal iteration constructs the seed exactly when it collapses,
and it fails to collapse in two situations only: no seed exists, so that
the first failure (11) occurs, or a seed exists whose word has, right after
the first differing position $k\le M/2$ of the stabilized pair, a run of
at least $\min(3k-1,M-k)$ digits all different from its digit at $k$.
Conversely, a seed with no such run after any position $2\le k\le M/2$
forces collapse. A proof that (14) collapses for unbounded $C_b$ would
therefore prove that their seeds exist. The stable-pair restrictions do not
prove this collapse, but neither do they rule out obtaining it from the
special half target. In the
different-target example, $k=2$, $Y=1024$ and the seed $1025$ has zeros at
positions $3$ to $7$, as the proposition requires. Check 9 of the
[[research/leads/reciprocal_mersenne_greedy/evidence/_index|evidence]]
tests the first two assertions at every target below $2^{11}$ for
$C=\{1,2,3,4,6\}$ and $M=12$: 427 targets give a stable pair with
$\ell<u$, and 16 of them also have a seed. The same check finds that (14)
collapses at the half target for every $C$ with
$C\setminus\{1\}\subseteq\{2,\ldots,12\}$ and $\operatorname{lcm}(C)\le2520$.
Neither finite observation proves collapse for an unbounded family.

### Mixed carries at the half target

The all-ones value $T=2^{M-1}-1$ gives more than antitonicity. Suppose
$\ell<u$ is a stabilized pair, and write
$\alpha_d=\eta_d(\ell)$, $\beta_d=\eta_d(u)$, with
$\alpha_1=\beta_1=0$. Put
$f^-_n=\sum_{a\in C\setminus\{1\},\,a\mid n}\alpha_{n/a}$ and define
$f^+_n$ with $\beta$ in place of $\alpha$. The two mixed carries are

$$
p_1=q_1=1,\qquad
p_n=2p_{n-1}-\alpha_n-f^+_n,\qquad
q_n=2q_{n-1}-\beta_n-f^-_n.\tag{16}
$$

The crossed row equations $\ell+H_C(u)=u+H_C(\ell)=T$ give
$p_M=q_M=1$. Reading (16) backward proves that both carries are positive
integers. If $K=|C|-1>0$, their future-tail formulas give the bounds

$$
1\le p_n,q_n\le\lceil\mu_C(n)\rceil
\le\lfloor K/2\rfloor+1,\qquad
\mu_C(n)=\sum_{a\in C\setminus\{1\}}
               \frac{2^{n\bmod a}}{2^a-1}.\tag{17}
$$

For example,

$$
p_n=2^{n-M}+\sum_{n<d\le M}\alpha_d2^{n-d}
 +\sum_{\substack{a\in C\setminus\{1\}\\n<ad\le M}}
      \beta_d2^{n-ad}.
$$

The first two terms sum to at most $1$, and the proper-channel terms are
strictly below $\mu_C(n)$. Thus $p_n<1+\mu_C(n)$, which proves the first
integer upper bound. Each summand in $\mu_C(n)$ is at most
$\frac12+1/(2(2^a-1))$. The bound
$\sum_{a\ge2}(2^a-1)^{-1}<2/3$ proves the second upper bound after taking
integers. The same argument applies to $q_n$. If $C=\{1\}$, the map is
constant and has no nontrivial pair.

Let $k$ be the first differing digit, and set
$\delta_n=\beta_n-\alpha_n$, $z_n=p_n-q_n$ and
$h_n=f^+_n-f^-_n$. Then

$$
z_n=2z_{n-1}+\delta_n-h_n,\qquad
h_n=\sum_{\substack{a\in C\setminus\{1\}\\a\mid n}}\delta_{n/a},
\qquad z_1=z_M=0.\tag{18}
$$

Here $2k\le M$ by the stable-pair proposition. For $k\le n<2k$ one has
$h_n=0$, because all its quotients are below $k$. In this window,
$z_n$ is the positive binary-prefix difference. To bound it from above,
retain the proper future contribution $P(n,k)$ of the common digits
$d<k$, namely
$P(n,k)=\sum_{d=2}^{k-1}\alpha_d
\sum_{a\in C\setminus\{1\},\,n<ad\le M}2^{n-ad}$.
The contribution of all digits $d\ge k$ is at most

$$
D(n,k)=\sum_{a\in C\setminus\{1\}}
          \sum_{k\le d\le M/a}2^{n-ad}
\le\frac{16}{9}2^{n-2k}<1.
$$

Both mixed carries lie in $(P(n,k),P(n,k)+1+D(n,k)]$. This interval has
length less than $2$, so two integer carries in it differ by at most one.
Consequently

$$
z_n=1\quad(k\le n<2k),\qquad
\delta_k=1,\qquad \delta_n=-1\quad(k<n<2k).\tag{19}
$$

If $2\in C$, $M$ is even and $k\ge3$, one further step is forced:

$$
\delta_{2k}=-1,\qquad p_{2k}=q_{2k}.\tag{20}
$$

Indeed, $h_{2k}=\delta_k=1$, so (18) gives
$z_{2k}=1+\delta_{2k}\ge0$. If $M=2k$, the terminal equality proves
$z_{2k}=0$. Otherwise $M\ge2k+2$. In the difference of the proper future
tails at position $2k$, the known digit $\delta_{k+1}=-1$ contributes
$-1/4$ in channel $2$. The positive digit at $k$ contributes at most
$1/(2^k-1)$ through channels at least $3$, and all unknown digits
$d\ge2k$ contribute at most $\frac{16}{9}4^{-k}$. Discarding the other
negative contributions gives an upper bound
$-1/4+1/(2^k-1)+\frac{16}{9}4^{-k}<0$ for $k\ge3$.
The difference of the primary future tails is strictly less than $1$.
Subtracting the tail formulas for $p_{2k}$ and $q_{2k}$ therefore gives
$z_{2k}<1$. Its nonnegative integrality proves (20). For $C_b$ with
$b\ge4$, the first interval of (14) lies above $3\cdot2^{M-3}$, using
$H_C(T)\le2^M/9$ and $M\ge12$. Both words therefore begin with digits
$\alpha_2=\beta_2=\alpha_3=\beta_3=1$, so any first disagreement has
$k\ge4$ and (20) applies.

These conditions recover collapse when $K\le3$. In that case (17) gives
$p_n,q_n\le2$. Bertrand's postulate supplies a prime $k<r<2k$, which lies
within the row. At $r-1$, (19) and positivity give $p_{r-1}\ge2$.
At the prime $r$ the proper forcing vanishes, and hence
$p_r=2p_{r-1}-\alpha_r\ge3$, a contradiction. This is an alternative
proof for the already constructed small multiplier sets, with the same
classical external theorem. For $K\ge4$, the value $3$ is allowed by
(17); this contradiction does not extend uniformly.

### Why the carry rejoin is not a splice

Assume the hypotheses of (20). Let $c^-_n,c^+_n$ be the ordinary carries
(1) of the two Boolean prefixes, each using its own proper forcing.
Below $2k$ their forcing agrees, so $c^-_n=p_n$ and $c^+_n=q_n$.
At $2k$ it differs by one. Writing $p_{2k}=q_{2k}=r$, one obtains

$$
c^-_{2k}=r+1,\qquad c^+_{2k}=r-1.\tag{21}
$$

Thus equal mixed carries leave ordinary boundary carries two apart. A
continuation beginning with carry $r$ splices to neither ordinary prefix.
Strict positivity of $c^+_{2k}$ requires $r\ge2$; mixed positivity alone
only gives $r\ge1$.

There is an explicit continuing discrepancy. If $\{1,2,3,4\}\subseteq C$,
in particular for $C_b$ with $b\ge4$,
and $2k<n\le\min(4k,M)$, equations (19)--(20) determine all proper
quotients in (18), giving

$$
h_n=-\mathbf1_{2\mid n}+\mathbf1_{n=3k}
    -\mathbf1_{3\mid n,\,n>3k}+\mathbf1_{n=4k}.\tag{22}
$$

In particular $h_{2k+2}=-1$ when that position is in the row. Setting both
$z$ and $\delta$ to zero after the rejoin violates (18) there. This
identifies a failed continuation rule, not a counterexample to the half
target or to some more elaborate repair.

The next block also retains the common forcing. Let $f^0_n$ be the proper
contribution of the common digits below $k$, put $m_n=p_n+q_n$, and put
$s_n=\alpha_n+\beta_n$. On the same block,

$$
\begin{aligned}
f^+_n+f^-_n
 &=2f^0_n+\mathbf1_{2\mid n}
   +\mathbf1_{3\mid n,\,n\ge3k}+\mathbf1_{n=4k},\\
m_n&=2m_{n-1}-s_n-f^+_n-f^-_n,\\
(s_n,\delta_n)&\in\{(0,0),(1,-1),(1,1),(2,0)\},\\
2+|z_n|&\le m_n\le2\lceil\mu_C(n)\rceil-|z_n|,
\qquad m_n\equiv z_n\pmod2.
\end{aligned}\tag{23}
$$

Equations (18), (22) and (23) give a precise continuation problem; the
boundary offsets (21) and the pending contributions (12)--(13) must also
be retained in any construction of an ordinary seed. No inequality or
decreasing integer quantity is proved here that excludes all nontrivial
half-target pairs for unbounded $b$, and no repair satisfying every later
Boolean constraint is constructed. The next required input is such an
all-parameter continuation or exclusion theorem. The block identities
alone are necessary conditions, not that theorem.

The mixed recurrence, the rejoin (20), the offsets (21), and the next-block
forcing are tested in check 9 on the 169 nontrivial pairs with $k\ge3$ in
its different-target $M=12$ enumeration. For a target $t$ the terminal
mixed carries are $2^{M-1}-t$, so those examples test the algebra but not
the half-target bound (17). The proofs above, rather than that finite
enumeration, supply the stated conditional identities.

## The half target across multiplier sets

The full target needs seeds only for initial segments, but a uniform
question over all finite sets of multipliers is consistent with every
finite case examined here:

> Does every finite $C\subseteq\mathbb N$ with $1\in C$ give a half
> representation with support omitting $1$, that is, a seed (3) at
> $M=\max(2,\operatorname{lcm}(C))$?

A positive answer contains the seeds for every $C_b$, and hence the full
Mersenne half representation below. Because it quantifies over all sets,
it also allows an induction that adjoins one new multiplier at a time, in
any order, through the analogue of the signed repair (7)--(8). The question
is open here. Check 9 of the evidence finds the seed for all 2048 sets with
$C\setminus\{1\}\subseteq\{2,\ldots,12\}$; this is a finite census, not an
induction.

Two exact examples show what a proof of this question must use. Each changes
the weights, so neither refutes the question or half membership for any set
of multipliers.

First, allowing repeated multipliers can lose the half target. The weights
$\omega_n=2^{-n}+4^{-n}+3\cdot8^{-n}$ have integer coefficients, so their
carries obey (1); they dominate their tails strictly,
$\omega_n-\sum_{m>n}\omega_m=\frac23 4^{-n}+\frac{18}7 8^{-n}$; and
$\frac13+\frac37<1$, so the carry at a common multiple of $2$ and $3$ is
again $1$. A half representation omits $1$, because $\omega_1>\frac12$,
and contains $2$, because
$\sum_{m\ge3}\omega_m=\frac14+\frac1{48}+\frac3{448}<\frac12$. It then
meets a gap at step 3:

$$
\sum_{m\ge4}\omega_m=\frac{1409}{10752}
<\frac12-\omega_2=\frac{1512}{10752}
<\omega_3=\frac{1575}{10752}.
$$

Bounding only the total multiplier mass does not prevent a gap. The
multiplicities
$\lambda_3=3$, $\lambda_4=2$, $\lambda_5=1$ beside the unit channel have
$\sum_{a\ge2}\lambda_a/(2^a-1)=\frac37+\frac2{15}+\frac1{31}$, which is below
$\sum_{a\ge2}(2^a-1)^{-1}$, yet the forced greedy prefix $\{2,3\}$ meets a
gap at step $4$. Both gaps are checked in exact rationals by check 9.

Second, allowing the multiplier set to vary with the index can also lose
the half target. For $m\le9$ put
$v_m=2^{-m}+\sum_{a\in B_m}2^{-am}$ with

| $m$ | $B_m$ |
| --- | --- |
| $2$ | $\{6,7,8,9\}$ |
| $3$ | $\{4,5,6,8,9,10\}$ |
| $4$ | $\{3,4,8,10\}$ |
| $5$ | $\{2,3,4,6,7,9,10\}$ |
| $6$ | $\{3,4,6,8\}$ |
| $7$ | $\{2,3,4,5,6,8\}$ |
| $8$ | $\{2,5,7,9\}$ |
| $9$ | $\{2,\ldots,10\}$ |

and $v_m=2^{-m}$ for $m>9$. The sums of distinct $v_m$ with $m>9$ are
exactly the numbers in $[0,2^{-9}]$, so $\frac12$ is a sum of distinct
$v_m$ with $m\ge2$ exactly when some $F\subseteq\{2,\ldots,9\}$ leaves
$\frac12-\sum_{m\in F}v_m$ in $[0,2^{-9}]$. Check 9 enumerates all $2^8$
sets $F$ and finds none. Index-dependent multiplier sets inside
$\{2,\ldots,10\}$ can thus lose the half target, whereas no fixed set $C$
with $1\in C\subseteq\{1,\ldots,12\}$ does. An argument that applies
equally to integer multiplicities, or to multiplier sets chosen separately
at each index, cannot prove the question. The coefficient
$\epsilon_n+f_n$ of (1), with $f_n=\sum_{a\in B,\,a\mid n}\epsilon_{n/a}$,
is the Dirichlet convolution of $\epsilon$ with the indicator of $C$; a
proof must use that structure. The full Mersenne weights have it, with
every multiplier once at every index.

## What would reach the full weights

Put $C_J=\{1,\ldots,J\}$. If representations of $1/2$ can be constructed
for unbounded $J$, compactness gives a full Mersenne representation. In fact,
uniformly over $A\subseteq\{2,3,\ldots\}$,

$$
0\le\sum_{n\in A}\bigl(w_n-v_n(C_J)\bigr)
\le\sum_{a>J}\frac{2^{-2a}}{1-2^{-a}}
\le\frac23\,4^{-J}.
$$

Choose a coordinatewise convergent subsequence of the supports. Uniform
summability of $w_n$ makes its limiting sum $1/2$. The full-weight support
is infinite by the odd-denominator argument in the canonical sketch, and
uniqueness identifies it with the actual full-weight greedy support.
This would discharge Step 4 of that sketch, including every later gap test.
It does not require a uniform bound on the carries as $J$ grows.

Cook's [geometric-truncation note](https://github.com/wcook04/plectis-erdos/blob/69e50fe6bc41322323dd213f96b626ab8f50106b/research/experiments/erdos257/notes/truncation-rung-ladder-2026-07-24.md)
also gives this transfer and a finite test for each fixed $J\ge3$. Its
Theorems 3 and 6 use
$\mu_J(M)=\sum_{a=2}^J2^{M\bmod a}/(2^a-1)$: if some
$M\in[n,2n-2]$ has $\mu_J(M)\le11/15$, no Boolean prefix for the target
$1/2$ can meet a gap at step $n\ge4$. Taking a multiple of
$\operatorname{lcm}(2,\ldots,J)$ covers all
sufficiently large steps for that fixed $J$. The note reports completed
finite certificates for $3\le J\le22$. Its written argument has been read;
those source programs and certificate files have not been replayed here,
and the reported certificates are not premises of the proposition.

The missing input is a construction satisfying (1) for unbounded $J$. The
two-state proposition supplies only $J\le4$. The seed proposition supplies
a complete extension for any fixed $J$ once its finite seed exists. Allowing
three arbitrarily large additional multipliers does not approximate the full
series: the sets must
eventually contain every fixed multiplier. The failure at 108 rules out only
the displayed two-state rule. Neither the proposition nor finitely many
successful values of $J$ supply the unbounded family. This input is unproved
here, not refuted.

## Relation to the full gap test

Three observations locate the missing input of the truncation route. They
do not rule out using its bounded carries or its finite seed equation to
construct the required half representations.

First, each fixed multiplier set admits rational sums over infinite supports
trivially. For a periodic support the sum
$\sum_{a\in C}\sum_{n\equiv r\ (\mathrm{mod}\ M)}2^{-an}$ is a finite sum of
geometric series. The transfer needs the one target $\frac12$ for an
unbounded set of $J$; a rational value for each $J$ separately gives nothing.

Second, membership for the truncated weights persists only together with
the full gaps. Let $J\ge2$, $n\ge2$, $F\subseteq\{2,\ldots,n-1\}$ and
$S^{(J)}_F=\sum_{k\in F}v_k(C_J)$. Since $v_n(C_J)>U_n(C_J)$, the argument
of Lemma 2 of the sketch shows that the interval
$\bigl(S^{(J)}_F+U_n(C_J),\,S^{(J)}_F+v_n(C_J)\bigr)$ contains no sum of
distinct $v_k(C_J)$. Its left end is at most $S_F+T_n$, since
$S^{(J)}_F\le S_F$ and $U_n(C_J)\le T_n$ termwise. By the
displayed bound applied to $F\cup\{n\}$, its right end is at least
$S_F+w_n-\frac23 4^{-J}$. A half representation for $C_J$ therefore puts
$\frac12$ outside $\bigl(S_F+T_n,\,S_F+w_n-\frac23 4^{-J}\bigr)$. That is the
whole corresponding gap of $\Sigma$ except a strip at its right end, and it is
nonempty whenever $n\le J$, since the gap has length above $\frac23 4^{-n}$.
As $\frac12$ is not the finite sum $S_F+w_n$, it lies at positive distance
from every such right end. Half representations along an unbounded set of
$J$ thus put $\frac12$ outside every gap of $\Sigma$, which is half membership
by Lemma 4 of the sketch, without compactness.

Third, for the same digits the truncated and full forcing values agree at
every position $m\le2J+1$, since a multiplier $a$ with $a\mid m$ and
$m/a\ge2$ is at most $m/2$. On the steps $n\le J$, whose known windows lie
below $2J$, the truncated weights therefore present exactly the full
forcing values, and these are the steps that the second observation ties to
the full gaps. The fixed-$J$ witness of Cook's note gives
nothing on the steps $4\le n\le J$, whose witness positions satisfy
$M\le2n-2<2J$. For $J\ge8$ every $M$ with $2\le M<2J$ has
$\mu_J(M)>\frac{11}{15}$. If $M<J$, the terms of $\mu_J(M)$ with $a=2$ and
$a=M+1$ already exceed $\frac13+\frac12$. If $J\le M<2J$, the terms with
$a=2,3,4$ and with the least $a>M/2$ exceed
$\frac13+\frac17+\frac1{15}+\frac14$, since that least $a$ is at least 5
and $2a-M\le2$.

A construction for unbounded $J$ would therefore prove Step 4 for the actual
orbit of $\frac12$. These comparisons explain why bounded values of $J$
alone are insufficient. They do not show that a proof using bounded carries
for each $C_J$ is impossible or no simpler than a direct orbit invariant.
Equation (3) and the doubling extension give one precise construction task:
produce the unique finite seed at $M=\operatorname{lcm}(1,\ldots,J)$ for an
unbounded set of $J$. No uniform seed construction is supplied here.

A rule allowing the larger carries exists. It is the window rule of Lemma 12
of the canonical sketch, with $f_m$ counting only multipliers in $C$. It
determines each digit from already fixed digits, keeps its carries at most
$\max(1,|C|-1)$, and agrees with the truncated greedy digits for
$C=\{1,2,3,4,6\}$ and $C=\{1,\ldots,8\}$ through step 400
([[research/leads/reciprocal_mersenne_greedy/evidence/_index|check 6]]). Its
digits are bits away from the coincidences of that lemma. Proving their
Booleanity for unbounded initial segments is one possible completion; a
construction of the seeds in (3), which uses a different extension rule, is
another. The next discriminating test is a proposed uniform construction of
those seeds, or an invariant proving that the window rule never fails. The
finite seed checks do not settle this. For the full weights, literal carries
are necessarily unbounded, as Lemma 6 of the canonical sketch proves, whereas
the doubling extension permits a carry bound depending on the finite set $C$.
