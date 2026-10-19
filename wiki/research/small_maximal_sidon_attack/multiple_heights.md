---
name: research/small_maximal_sidon_attack/multiple_heights
title: Compatible height fibers and concentrated residuals
desc: |
  Disjoint internal height differences characterize compatible fibers
  above a modular Sidon set. Residuals confined to few classes or rows
  admit small completions. Exact finite examples measure the gap between
  these sufficient criteria and the coverage of explicit height systems.
tags: []
sources:
- problems/additive_bases/E0156
problems:
- 156
created: 2026-10-15T23:58:19Z
updated: 2026-10-15T23:58:19Z
---

***

The following elementary arguments and finite observations are
author-recorded by Plasma AI. They address the compatible-completion gap
in the [proof sketch](proof_sketch.md), without establishing the
$O(N^{1/3})$ bound in
[[problems/additive_bases/E0156/_index|Problem 156]]. All Sidon conventions
here include doubles.

## Compatibility of several heights

Let $B=\{b_1,\ldots,b_m\}\subset[0,q)$ be strong Sidon modulo $q$.
For finite nonempty integer sets $H_i$, define

$$
A=\bigcup_{i=1}^m(b_i+qH_i),\qquad
\Delta_i=(H_i-H_i)\cap\mathbb Z_{>0}.
$$

**Fiber criterion.** The integer set $A$ is strong Sidon if and only if
every $H_i$ is strong Sidon and the sets $\Delta_i$ are pairwise disjoint.

*Proof.* Reduce an equality of two unordered pair sums modulo $q$.
The modular Sidon property fixes the unordered pair of fiber indices.
If both indices are $i$, uniqueness is exactly the Sidon property of
$H_i$. For distinct indices $i,j$, an equality has the form
$h_i+h_j=h'_i+h'_j$. A nontrivial equality gives the same positive
difference in $\Delta_i$ and $\Delta_j$, after interchanging the primed
and unprimed pairs if necessary. Conversely, such a common difference
gives a crossed pair-sum collision. Doubles occur in the same-fiber
case, so they are included. $\square$

For example, for $1\le i\le m$ take

$$
H_i=\{0,2i-1,3m+i-1\}.
$$

Its positive differences are $2i-1$, $3m-i$, and $3m+i-1$. As $i$
varies, these occupy respectively the odd numbers in $[1,2m-1]$,
$[2m,3m-1]$, and $[3m,4m-1]$, without repetitions. The resulting
$3m$-point set is therefore strong Sidon and lies in $[0,4mq)$.
With a Singer base, $m=p+1$ and $q=p^2+p+1$, this has cubic-root size.
The criterion establishes compatibility, not maximality.

For a residue $r\in[0,q)$ the exact heights reached by $A+A-A$ are

$$
\bigcup_{b_i+b_j-b_\ell\equiv r\pmod q}
\left(H_i+H_j-H_\ell+
\frac{b_i+b_j-b_\ell-r}{q}\right).
$$

The last term is an integer in $\{-1,0,1\}$. Indices may repeat. A
target outside $A$ in this union is blocked: a cancellation of the
subtracted element with a summand would put the target in $A$.
Midpoint blockers, where $2x\in A+A$, provide an additional possibility.

## Complete vertical differences

Suppose all $H_i\subset[0,M)$ and
$\bigcup_i\Delta_i\supseteq\{1,\ldots,M-1\}$. Every target in
$[0,qM)\setminus A$ sharing a residue class with an element of $A$ is
blocked. Indeed, write $y-x=q\delta$ with $x\in A$ and
$1\le|\delta|\le M-1$. There are $a,a'\in A$ in one fiber with
$a-a'=q\delta$, so $y=x+a-a'$. We have $a'\ne a$; also $a'\ne x$,
since otherwise $y=a\in A$. Thus this is a valid blocker.

A finite system of pairs $a_i,b_i=a_i+i$, $1\le i\le m$, partitioning
$\{1,\ldots,2m\}$ gives such columns:

$$
H_i=\{0,i,b_i+m\},\qquad
\Delta_i=\{i,a_i+m,b_i+m\}.
$$

The differences partition $\{1,\ldots,3m\}$, so $M=3m+1$ works.
Such a pair system is called a Skolem system. This argument is conditional
on the pair system and uses no general existence theorem. The exact
systems used below, for $m\in\{4,8,12,20,24\}$, are retained and
checked in the
[finite inputs](evidence/assets/multiple_height_completions.json).
For example, at $m=4$ the pairs in order of their differences are
$(7,8),(2,4),(3,6),(1,5)$.

## Completion from concentration

Let $A_0\subset[1,N]$ be strong Sidon, and let $R_0$ consist of the
points outside $A_0$ that can individually be added to it. Every greedy
completion adds a set $U\subseteq R_0$ with $A_0\cup U$ strong Sidon.
This follows from heredity: a point addable at a later stage was already
addable at the start. As the interval is finite, a greedy completion
terminates at a maximal set. Any upper bound for the size of a compatible
$U\subseteq R_0$ consequently bounds every such completion.

**Few residue classes.** If $N\le qM$ and $R_0$ lies in at most
$r\ge1$ residue classes modulo $q$, write $u_j$ for the number of
added points in class $j$ and $u=|U|$. Positive same-class differences
are distinct multiples of $q$ in $\{q,\ldots,(M-1)q\}$. Therefore

$$
\sum_j\binom{u_j}{2}\le M-1,\qquad
\frac{u^2}{r}-u\le2(M-1),\qquad
u\le\frac{r+\sqrt{r^2+8r(M-1)}}2
 \le r+\sqrt{2r(M-1)}.
$$

An empty residual requires no additions. In particular, when
$q\asymp p^2$, $M=O(p)$, and $r=O(p)$, completion adds only $O(p)$
points, even if $|R_0|$ has order $p^2$.

**Few short intervals.** If $R_0$ lies in $r$ intervals each containing
at most $q$ consecutive integers, a Sidon subset of each interval has
size at most $(1+\sqrt{8q-7})/2$: its positive differences are distinct
and at most $q-1$. Partitioning $U$ between these intervals gives
$|U|\le r(1+\sqrt{8q-7})/2$. For $q\asymp p^2$ and $r=O(1)$ this
is again $O(p)$. The elementary bound suffices; no sharp interval Sidon
estimate is needed.

**Complete vertical differences.** If $A_0-A_0$ contains
$q,2q,\ldots,(M-1)q$ and $N\le qM$, no compatible $U$ has two points
in one residue class modulo $q$. Their difference would repeat a
difference of $A_0$. Thus in this case at most one added point per
residual class is possible. This conclusion applies to unoccupied as
well as occupied classes.

These are sufficient completion criteria. No construction meeting them
uniformly at cubic scale is supplied here, and a large residual spread
over many classes does not prove a large necessary completion cost.

## Finite multiple-height examples

Use the deterministic Singer representatives returned by
[the evidence program](evidence/main.py), ordered increasingly, and
assign the columns in increasing index order. The domain has $N=qM$
points, written $[0,N)$; translating everything by one gives $[1,N]$.
Here the explicit columns have $M=4m$, the Skolem columns have
$M=3m+1$, and $m=p+1$. Every listed seed is strong Sidon. The retained
additions give a maximal strong Sidon completion, and are not claimed
to be a smallest completion.

| Columns | $p$ | $N$ | Initial misses | Classes with a miss | Added points |
| --- | ---: | ---: | ---: | ---: | ---: |
| Explicit | 3 | 208 | 2 | 2 | 1 |
| Explicit | 5 | 744 | 46 | 22 | 4 |
| Explicit | 7 | 1824 | 131 | 49 | 9 |
| Explicit | 11 | 6384 | 733 | 121 | 16 |
| Explicit | 13 | 10248 | 1222 | 169 | 20 |
| Explicit | 17 | 22104 | 3129 | 289 | 31 |
| Explicit | 19 | 30480 | 4199 | 361 | 34 |
| Explicit | 23 | 53088 | 7887 | 529 | 45 |
| Skolem | 3 | 169 | 0 | 0 | 0 |
| Skolem | 7 | 1425 | 28 | 24 | 5 |
| Skolem | 11 | 4921 | 181 | 104 | 11 |
| Skolem | 19 | 23241 | 1205 | 356 | 26 |
| Skolem | 23 | 40369 | 2401 | 525 | 31 |

The same thirteen cases with decreasing base order are also retained.
All 26 cases have no missed target in an occupied residue class. For
the explicit increasing-order examples with $p\ge7$, misses occur in
every unoccupied class. These finite examples do not provide the desired
class concentration. They neither rule out different column assignments
nor distinguish an eventual $O(p)$ completion bound from a logarithmic
loss.

## Two points in one row

For the same Singer base let $D=B-B$. Take two points $c+qs$ and
$c+\delta+qs$ at a common height $s\ge1$, with
$0\le c<c+\delta<q$. Their main-type triples cover every point of
their row, counting the two selected centers, exactly when

$$
[0,q)\subseteq(c+D)\cup(c+\delta+D).
$$

The two centers count as already selected; other covered points use
nonzero differences of $B$. The following minima count uncovered
residues over all such pairs. No compatibility requirement is imposed
on the pair, so a zero alone supplies no strong Sidon construction.

| $p$ | 5 | 7 | 11 | 13 | 17 | 19 | 23 | 29 | 31 | 37 | 43 |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| Minimum misses | 0 | 0 | 2 | 0 | 10 | 2 | 31 | 12 | 23 | 25 | 109 |

The finite zeros also prevent inferring a universal uniqueness assertion
for the complementary pair at distance $q$. The
[earlier two-translate census](finite_templates.md) instead uses the
closed interval $[0,q]$, allows a center at $q$, and requires the pair's
distance to avoid $D$; those are different domains and conditions.
Positive minima in this table exclude only this two-point, main-type
cover for the specified base. Other blocking triples, more centers,
different bases and asymptotic constructions remain open.

The [evidence instructions](evidence/_index.md) specify every finite
domain and the checks of the retained witnesses. These computations are
author checks, not independent review.
