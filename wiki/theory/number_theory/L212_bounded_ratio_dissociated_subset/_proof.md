---
name: theory/number_theory/L212_bounded_ratio_dissociated_subset/_proof
title: Multiscale averaging with deficient pivots
desc: A discrete Kraft deficiency estimate bounds a positive set in terms of its aspect ratio and the least possible nonzero coefficient sum of a relation. It gives the sharp positive bound at ratio 4/3 and the factor 3 at ratio 2.
created: 2026-10-15T18:14:21Z
updated: 2026-10-15T22:09:18Z
---

# Multiscale averaging with deficient pivots

***

This proves
[[theory/number_theory/L212_bounded_ratio_dissociated_subset/_index|L212]].
Throughout, $d(X)$ is the largest size of a dissociated subset of a finite
set $X$, $v_2(z)$ is the exponent of $2$ in a nonzero integer $z$, and
$t_+=\max(t,0)$. For a finite set $S$ of integers and $a\in S$ put

$$
m_S(a)=\bigl|\{v_2(x-a):x\in S\setminus\{a\}\}\bigr|,
$$

the number of distinct 2-adic valuations of differences from $a$.

## Step 1: integer model

Choose a basis of the $\mathbb Q$-span of $P$ in $\mathbb R$ and write each
element by its rational coordinate vector; evaluation of coordinate vectors
is $\mathbb Q$-linear and injective. Replace it by a rational linear
functional close enough that every nonzero value among the finitely many
combinations $\sum_{x\in P}\varepsilon_xx$ with $\varepsilon_x\in\{-1,0,1\}$
keeps its sign, and clear denominators. Every rational linear relation
that held originally still holds. The nonzero ternary combinations were
also preserved, so the zero ternary combinations and the dissociated
subsets are the same as before. Positivity
and the order are preserved, and so is any specified rational ratio bound
$\max P\le R\min P$: strict inequality survives a small perturbation, and
equality is the rational relation $R\min P-\max P=0$. Hence it suffices
to prove the claim for a set $P$ of positive integers.

## Step 2: the pivot budget

**Lemma A.** Let $P$ be a finite set of positive integers, and let
$q\ge1$ be an integer such that every ternary relation on $P$ has
coefficient sum either zero or of absolute value at least $q$. Suppose
$a\in P$ and $b_1,\ldots,b_k\in P\setminus\{a\}$ have pairwise distinct
valuations $v_2(b_i-a)$ and

$$
\sum_{i=1}^k|b_i-a|<qa.
$$

Then $\{a,b_1,\ldots,b_k\}$ is dissociated.

*Proof.* Put $\delta_i=b_i-a$. A ternary relation reads
$sa+\sum_i\varepsilon_i\delta_i=0$, where
$s=\varepsilon_0+\sum_i\varepsilon_i$. If $s\ne0$, then the hypothesis gives
$|sa|\ge qa>\sum_i|\delta_i|\ge|\sum_i\varepsilon_i\delta_i|$, a
contradiction. If $s=0$, a nonzero term of least valuation is unique,
so every $\varepsilon_i$ vanishes; then $\varepsilon_0=0$. $\square$

The choice $q=1$ is always available. If all elements are odd, reduction
modulo two gives $q=2$. More generally, a unit class modulo an integer
$q$ satisfies the stated condition.

## Step 3: Kraft equality and integer deficiency

**Lemma B.** For every nonempty finite set $S$ of integers,

$$
\sum_{a\in S}2^{-m_S(a)}=1.
$$

*Proof.* For $|S|=1$ this is $2^0=1$. Otherwise let $j$ be the least
valuation of a difference of two elements of $S$. All elements agree
modulo $2^j$, and $S$ splits into two nonempty classes $S',S''$ modulo
$2^{j+1}$. For $a\in S'$, differences to $S''$ have valuation $j$ and
differences within $S'$ have larger valuation. Hence
$m_S(a)=m_{S'}(a)+1$, and similarly on $S''$. Induction gives
$\tfrac12+\tfrac12=1$. $\square$

This is the Kraft equality of the binary residue tree underlying
[[theory/number_theory/L22_near_logarithmic_dissociated_subset/_index|L22]].
It is proved directly here; L22 is not a premise.

We shall also use the elementary inequality

$$
t_+\le s-1+2^{t-s}\qquad(t\in\mathbb Z,\ s\in\mathbb Z_{\ge1}).
\tag{1}
$$

For $t\le0$ the right side is positive. For $t>0$, put $u=t-s$;
(1) is $u+1\le2^u$, valid for every integer $u$. For $u\le-1$ its
left side is nonpositive; for $u=0,1$ there is equality; and induction
proves it for $u\ge2$.

## Step 4: the aspect-ratio bound

**Lemma C.** Let $P$ satisfy the hypotheses of Lemma A, with at least two
elements. Put $A=\min P$, $L=\max P-\min P$, $k=d(P)$, and $b=qA/L$.
If $b>1$, then

$$
|P|<\frac{b+1}{2(b-1)}\,2^k.
\tag{2}
$$

Put $n=|P|$ and $\alpha=2^k/n$.

For each pivot $a\in P$ and each difference level $j$, let $c_j(a)$ be
the least $|x-a|$ over $x\in P$ with $v_2(x-a)=j$. Let $N_a(r)$ count
the levels with $c_j(a)\le r$, and define the truncated cost

$$
F(a)=\int_0^L\bigl(k-N_a(r)\bigr)_+\,dr.
$$

If $m_P(a)\ge k$, this is exactly the sum $K(a)$ of the $k$ smallest
level costs. Indeed, the usual layer-cake formula for an ordered finite
list gives $K(a)=\int_0^\infty(k-N_a(r))_+\,dr$, and the integrand
vanishes for $r\ge L$. Choosing one element attaining each of these
costs would give $k+1$ dissociated elements by Lemma A if $K(a)<qa$.
By the definition of $k$, therefore,

$$
m_P(a)\ge k\quad\Longrightarrow\quad F(a)=K(a)\ge qa\ge bL.
$$

For a deficient pivot put $h=k-m_P(a)\ge1$. Since
$N_a(r)\le m_P(a)$, we have $F(a)\ge hL$. For every integer $h\ge1$,

$$
b-h\le(b-1)2^{h-1}:
$$

if the left side is positive, it is at most $b-1$, and otherwise the
inequality is immediate. Thus deficient pivots satisfy
$F(a)/L\ge b-(b-1)2^{k-m_P(a)-1}$. Summing over all pivots and applying
Lemma B to the deficient pivots' part of the Kraft sum gives

$$
\frac{\mathbb E F(a)}L
\ge b-\frac{b-1}{2n}
 \sum_{a:\ m_P(a)<k}2^{k-m_P(a)}
\ge b-\frac{b-1}{2}\alpha.
\tag{3}
$$

Pivots with too few levels have been included in (3), not discarded.

For the upper bound, partition $[A,A+L]$ into $2^s$ consecutive intervals
of length $L2^{-s}$, for each $s\ge1$, assigning endpoints consistently.
Write $I_s(a)$ for the interval containing $a$, and put

$$
D_s(a)=\bigl(k-m_{P\cap I_s(a)}(a)\bigr)_+.
$$

For $L2^{-s}\le r<L2^{1-s}$, every point in $P\cap I_s(a)$ is within
distance $r$ of $a$. Hence $N_a(r)\ge m_{P\cap I_s(a)}(a)$ and

$$
F(a)\le L\sum_{s\ge1}2^{-s}D_s(a).
\tag{4}
$$

This inequality holds for every pivot, including those with fewer than
$k$ total levels. Applying (1) with $t=k-m_{P\cap I_s(a)}(a)$, summing
over the points in each nonempty interval, and using Lemma B there gives

$$
\begin{aligned}
\mathbb E D_s(a)
&\le s-1+
 \frac{2^{k-s}}n
 \sum_{I:\ P\cap I\ne\varnothing}
 \sum_{a\in P\cap I}2^{-m_{P\cap I}(a)}\\
&\le s-1+\frac{2^{k-s}}n\,2^s
 =s-1+\alpha.
\end{aligned}
\tag{5}
$$

Also $D_s(a)\le k$. Therefore (4)--(5) give the strict bound

$$
\frac{\mathbb E F(a)}L
<\sum_{s\ge1}2^{-s}(s-1+\alpha)
=1+\alpha.
\tag{6}
$$

Strictness follows, for example, at every $s\ge k+1$, where
$s-1+\alpha>k\ge\mathbb E D_s(a)$. All the series converge, so this
strict improvement at one term suffices.

Combining (3) and (6) yields
$b-(b-1)\alpha/2<1+\alpha$, hence
$\alpha>2(b-1)/(b+1)$. This is (2). $\square$

If $\max P\le(1+\theta)\min P$ with rational $0<\theta<q$, then
$b\ge q/\theta$. The function $(b+1)/(2(b-1))$ is decreasing, so

$$
|P|<\frac{q+\theta}{2(q-\theta)}\,2^{d(P)}.
\tag{7}
$$

The singleton case satisfies (7) directly. The integer model preserves
the rational ratio bound, every ternary relation and its coefficient sum,
so (7) holds for positive real sets under the same relation hypothesis.

In particular, choosing $q=1$ and $\theta=1/3$ gives
$|P|<2^{d(P)}$ whenever $\max P\le\tfrac43\min P$. Choosing $q=2$ and
$\theta=1$ gives $|O|<3\,2^{d(O)-1}$ for positive odd sets of ratio at
most two. A unit class modulo $q$ satisfies the sharp positive bound
whenever its ratio is at most $1+q/3$.

## Step 5: summing valuation layers

Now assume $\max P\le2\min P$. Apply the integer model from Step 1 and
write the nonempty valuation
layers of $P$ in increasing order as $P_1,\ldots,P_r$, with
$d_i=d(P_i)$ and $d=d(P)$.

A dissociated subset of $P_i$ can be adjoined to one element from every
lower layer. In a relation using any of these lower representatives,
the used element of least valuation is unique and cannot cancel; the
remaining relation lies in the dissociated subset of $P_i$. Thus

$$
d_i+i-1\le d,\qquad r\le d.
$$

Dividing the $i$-th layer by its common power of two produces a positive
odd set with the same ratio and dissociation number. Equation (7) gives

$$
|P_i|<3\,2^{d_i-1}\le3\,2^{d-i}.
$$

Consequently

$$
|P|<3\sum_{i=1}^r2^{d-i}<3\,2^d.
$$

In fact, integrality gives
$|P_i|\le3\,2^{d-i}-1$, and therefore
$|P|\le3(2^d-2^{d-r})-r\le3\,2^d-d-3$.
Only the simpler strict bound is claimed. Since
$3\,2^d<2^{d+2}$, it also gives
$d(P)\ge\lfloor\log_2|P|\rfloor-1$. $\square$

## Scope and a regular-tree special case

The proof controls both the cost of valid pivots and the contribution
of deficient pivots. Its interval hypothesis enters (3) through $b=qA/L$.
Different scales are combined in
[[theory/number_theory/L213_triple_log_dissociated_subset/_index|L213]].

There is a stronger extraction when the residue tree has no shallow
leaves. Let $O$ be a finite set of positive odd integers of ratio at
most two, let $k\ge1$ be an integer, and suppose $n=|O|\ge2^k$ and
$m_O(a)\ge k$ for every $a\in O$. Use the same $F$ with this $k$, without
assuming $k=d(O)$. Every $F(a)$ is now a genuine $k$-companion cost.
Equations (4)--(6) give
$\mathbb E F/L<1+2^k/n\le2$, so some $F(a)<2L\le2a$. Lemma A supplies
$k+1$ dissociated elements. This proves the sharp positive extraction
in this regular-tree regime.

The parity restriction can be removed from this special case. Let $P$
be a finite nonempty set of positive integers of ratio at most two, let
$k\ge1$, and suppose $m_P(a)\ge k$ for every $a\in P$.
Let $Q$ be the highest nonempty valuation layer,
with $h$ nonempty layers below it. If $h\ge k$, one representative
from each layer already gives $k+1$ dissociated elements. Otherwise

$$
m_P(a)=h+m_Q(a)\quad(a\in Q),
$$

so every leaf of $Q$ has depth at least $k-h$. Kraft equality implies
$|Q|\ge2^{k-h}$. Dividing $Q$ by its common power of two, the odd case
just proved gives $k-h+1$ dissociated elements in $Q$. Adjoin one
representative from every lower layer, as in Step 5, to obtain $k+1$
elements of $P$. Thus any such set whose residue tree has minimum
leaf depth $k$ has the sharp extraction of $k+1$ elements. The general
case still has shallow leaves; the main argument bounds their
contribution but does not remove it.
