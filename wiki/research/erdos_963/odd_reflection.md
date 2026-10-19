---
name: research/erdos_963/odd_reflection
title: 'Dimension increase in odd reflected configurations'
desc: Odd reflection increases dimension through seven differences; a general increase by two is false, while an affine single-valuation-layer version is proved.
tags: []
sources: []
created: 2026-09-19T03:50:00Z
updated: 2026-09-19T03:52:14Z
---


# Dimension increase in odd reflected configurations

***

These are special augmentation results, not a proof of the target.
They differ from the refuted assertion in
[[research/erdos_963/reflection_obstruction|the reflection obstruction]]: here the center
itself, not twice the center, is included, and all points are odd.

Let $c$ be a positive odd integer and let $X$ be a dissociated set of
distinct positive even integers smaller than $c$. Write

$$
Q=\{c\}\cup\{c-x,c+x:x\in X\}.
$$


## A proved orientation for at most seven differences

**Theorem.** If $|X|\le7$, there are signs $\sigma_x$ such that

$$
\{c\}\cup\{c+\sigma_xx:x\in X\}
$$

is dissociated. In particular $d(Q)\ge |X|+1$.

A balanced relation among any oriented selection gives a ternary
relation on $X$, so is impossible. For the all-upper selection,
every point is in $[c,2c)$. Odd parity requires even relation support.
An unbalanced relation supported on at most six points has at least
four terms against at most two, or at least three against one;
the interval bounds rule it out. This proves the theorem for
$|X|\le6$.

Let $|X|=7$. If the all-upper selection is dependent, its relation
must use all eight points and have five terms against three. The
pivot $c$ lies on the five-term side: if it lay on the three-term
side, that side would be less than $5c$, whereas the other side
would be at least $5c$. We therefore have a partition

$$
X=A\sqcup B,\qquad |A|=3,\quad |B|=4,\qquad
\sum A-\sum B=2c.
$$

Put $S=\sum B$. Since the three members of $A$ are less than $c$,
we have $S<c$, and every $a\in A$ exceeds $S$.

Flip only $b=\min B$: set $\sigma_b=-1$ and all other signs to
$1$. Suppose the resulting selection has a relation. Write it as

$$
sc+\sum_{x\in X}r_xx=0,
\qquad s=\alpha_0+\sum_xr_x\sigma_x,
$$

where $r_x,\alpha_0\in\{-1,0,1\}$. Oddness makes $s$ even;
$s=0$ is excluded by dissociation of $X$. Also
$\sum X=2c+2S<4c$. Reversing the relation if needed gives

$$
\sum_xr_xx=2c,
\qquad \sum_xr_x\sigma_x\in\{-3,-2,-1\}.              \tag{1}
$$


At least two members of $A$ have coefficient $+1$, since one of
them together with all of $B$ has sum less than $c+S<2c$.
If all three do, every $B$-coefficient must be $-1$. The signed
coefficient sum in (1) is then $1$, impossible. If two do and the
third $a$ has coefficient $-1$, the total is at most
$2c+2S-2a<2c$. Hence precisely two have coefficient $+1$ and
the third $a$ is omitted. The equation becomes

$$
a=S+\sum_{u\in B}r_u u>S.                              \tag{2}
$$


Let $u,v$ be the numbers of positive and negative coefficients on
$B$. There is at least one positive coefficient. If $r_b\le0$,
counting the other three coefficients gives
$\sum_xr_x\sigma_x\ge1$, contrary to (1). If $r_b=1$, that
sum equals $u-v$. To be negative, with $u+v\le4$, requires
$(u,v)=(1,2)$ or $(1,3)$. Equation (2) then gives, respectively,
$a=2b+q$ for the omitted $q\in B\setminus\{b\}$, or $a=2b$.
Both are less than $S$, since $b$ is the smallest of four distinct
positive numbers. This contradicts $a>S$ and proves the theorem.

Thus a centrally symmetric odd set containing its odd center has
dimension at least $d(X)+1$ whenever its positive difference set
has dimension at most seven. The unrestricted version is unproved.

## Increasing dimension by two is false in general

Take $X=\{2,4,8,16\}$ and $c=17$. The set $X$ is dissociated,
but

$$
Q=\{1,9,13,15,17,19,21,25,33\},\qquad d(Q)=5.
$$

Thus the tempting stronger bound $d(Q)\ge d(X)+2$ is false.

The five-set $\{1,9,13,15,17\}$ is dissociated: its ten pair
sums are distinct, and its smallest triple sum exceeds $17$.
Parity excludes every relation except a two-term equality, a
pair-sum equality, or a triple equaling a singleton.

Every six-subset of $Q$ containing two complete reflected pairs
is dependent, since both pairs sum to $34$. Otherwise it consists
of $c$, one complete pair $\{c-x,c+x\}$, and one point from each
other pair. If $x\in\{2,4,8\}$, then $2x\in X$, and the selected
point $c\pm2x$, together with the complete pair and $c$, gives a
balanced four-term relation.

It remains to consider the complete pair $\{1,33\}$. The other
three choices are $a\in\{15,19\}$, $b\in\{13,21\}$ and
$z\in\{9,25\}$. If $a=15$, use $1+15+17=33$; if $a=19,b=13$,
use $1+13+19=33$. In the remaining cases use

$$
1+17+19+21=25+33,\qquad
1+9+19+21=17+33.
$$

This covers every six-subset and proves the claimed dimension.

The obstruction persists in every dimension $k\ge4$. Set

$$
X_k=\{2,4,\ldots,2^k\},\quad c=2^k+1,\quad
Q_k=\{c\}\cup(c+X_k)\cup(c-X_k).
$$

Then $d(Q_k)=k+1$. The all-upper selection with $c$ is
dissociated: in a relation its coefficient sum at $c$ is even,
whereas $\sum X_k=2^{k+1}-2<2c$, so it must be balanced and
then trivial. To exclude $(k+2)$-subsets, two complete pairs give
an immediate relation; otherwise the set has the center, one
complete pair and one choice from every other pair. Any nonlargest
pair is blocked by its doubled offset. For the largest pair
$\{1,2c-1\}$, choices at offsets $2,4,8$ suffice. Successively
according to those choices, use

$$
\begin{split}
1+(c-2)+c&=2c-1,\\
1+(c+2)+(c-4)&=2c-1,\\
1+(c+2)+(c+4)+(c-8)&=c+(2c-1),\\
1+c+(c+2)+(c+4)&=(c+8)+(2c-1).
\end{split}
$$

Thus a general reflection theorem could guarantee at most one
additional dimension.

## A two-dimension increase in an affine special case

Call a set affinely dissociated if its only balanced ternary relation
is trivial. If a dissociated integer set $X$ has all elements of
the same $2$-adic valuation, then

$$
\{0\}\cup X\cup(-X)
\quad\hbox{contains an affinely dissociated }(|X|+2)\hbox{-set}.
                                                               \tag{3}
$$

Scale so the entries are odd, fix a pivot $x_j$, and, for $i\ne j$,
choose $\sigma_i\in\{\pm1\}$ with $\sigma_i\equiv x_i\pmod4$.
Use

$$
Y=\{0,-x_j,x_j\}\cup\{\sigma_i x_i:i\ne j\}.
$$

A balanced ternary relation not assigning opposite nonzero
coefficients to $-x_j,x_j$ reduces to a ternary relation on $X$.
If those two coefficients are equal, cancellation in $X$ would
instead require a coefficient of absolute value two at $0$;
this is also impossible. The only remaining possibility would give

$$
2x_j=\sum_{i\ne j}\varepsilon_i x_i,
\qquad \left|\sum_{i\ne j}\varepsilon_i\sigma_i\right|\le1.
$$

But the latter sum is $2x_j\equiv2\pmod4$, a contradiction.
This proves (3).

For the odd reflected configuration above, (3) gives an actual
dissociated $(|X|+2)$-subset if, additionally,

$$
2c>\sum X+\max X.
$$

Indeed, every relation on the translated selection has an even
coefficient sum at $c$. Its offset part has absolute value at most
$\sum X+\max X$, so the displayed inequality forces balance.

Statement (3) for mixed valuation layers remains unproved. The
counterexample above concerns actual, not affine, dissociation and
does not refute it. It does refute a two-dimension increase for
arbitrary $c>\max X$.

There is also a valuation-free small affine case: (3) holds for
every positive dissociated $X$ with $|X|\le5$, using
$Y=\{0,-M,M\}\cup(X\setminus\{M\})$ and $M=\max X$.
The only possible affine relation would give
$2M=\sum_{x\ne M}\varepsilon_xx$ with
$|\sum\varepsilon_x|\le1$. Among at most four other coordinates
this permits at most two positive coefficients, whose weighted
sum is strictly less than $2M$. This is impossible.

Neither an unrestricted largest-pivot rule nor a largest-valuation
rule can extend this proof. The dissociated set $\{1,2,8,15\}$
has its maximum-valuation pivot $8$ blocked by
$16=1+15=-1+2+15$: avoiding a signed coefficient sum of zero in
the first representation forces the signs on $1,15$ to agree,
and the second then has coefficient sum $\pm1$.

The largest pivot is blocked in
$X=\{8,20,36,40,42,45\}$ by

$$
90=40+42+8=36+42+20-8=36+40+42-8-20.
$$

The first representation forces the signs on $40,42,8$ to agree;
the second then forces those on $36,20$ to agree; the last has
signed coefficient sum $\pm1$. This $X$ is dissociated: successive
valuation arguments eliminate $45$ and $42$, leaving four times
the dissociated set $\{2,5,9,10\}$, whose subset sums are
$0,2,5,7,9,10,11,12,14,15,16,17,19,21,24,26$.
These examples leave free choice of the pivot open.
