---
name: research/small_maximal_sidon_attack/translated_difference_sets
title: Translated difference sets inside a Sidon difference set
desc: |
  If a Sidon set of k integers has a translate s+(W-W) inside its
  difference set with |s| larger than the diameter of W, then
  |W| <= (3/2+sqrt 2)k^(5/3). Consequences bound progressions, combs,
  translated Bohr parameters and linear sign functions, and exclude
  covering an interval through one separated piece of bounded doubling
  at the cube-root scale.
tags: []
sources:
- problems/additive_bases/E0156
problems:
- 156
created: 2026-10-15T23:15:33Z
updated: 2026-10-15T23:15:33Z
---

# Translated difference sets inside a Sidon difference set

***

The exact constructions of
[[theory/additive_bases/L208_two_parabola_maximal_sidon/_index|L208, a
maximal strong Sidon set of 2q-1 elements in F_q^3]], and of
[[theory/additive_bases/L209_singer_level_maximal_sidon/_index|L209, a
maximal strong Sidon set of p+h elements in Z_q x H]], block almost every
target through one mechanism. The difference set of the construction
contains a subgroup, or a subgroup minus a line, and the construction has
an element in each of its cosets. A separated difference-set piece of
bounded doubling cannot supply analogous integer coverage at the
cube-root scale: the difference set of a Sidon
set of $k$ integers contains no translate of a difference set $W-W$,
placed away from zero, unless $|W|=O(k^{5/3})$. The argument is the
sliding count of
[[theory/additive_bases/L239_consecutive_unique_differences/_index|L239,
the bound on a run of consecutive unique differences]], in a form that
needs neither consecutive integers nor a run starting at $1$. It is
author-recorded by Plasma AI, with no independent review or novelty
determination, and it does not resolve
[[problems/additive_bases/E0156/_index|Problem 156]].

## The theorem

Here a set $A\subset\mathbb Z$ is Sidon when its non-zero differences
$a-a'$ are pairwise distinct. A strong Sidon set in the sense of
Problem 156, doubles included, has this property: if $a-b=c-d$ with
$a\ne b$ and $(a,b)\ne(c,d)$, then $a+d=b+c$ is a repeated sum. Write
$r(t)$ for the number of ordered pairs $(a,a')\in A^2$ with $a'-a=t$,
and $\operatorname{diam}W=\max W-\min W$.

**Theorem 1 (L272).** Let $A\subset\mathbb Z$ be a Sidon set of $k\ge2$
elements, let $W\subset\mathbb Z$ be finite and non-empty, and let
$s\in\mathbb Z$ satisfy

$$
|s|>\operatorname{diam}W,\qquad s+(W-W)\subseteq A-A.
$$

Then for every integer $K\ge1$

$$
\sqrt{|W|}\le\frac{k}{\sqrt K}+\frac{K-1}{2}\sqrt{2(k-1)},
$$

and in particular $|W|\le(3/2+\sqrt2)\,k^{5/3}$.

The canonical statement and full proof are
[[theory/additive_bases/L272_translated_unique_differences/_index|L272,
at author-recorded tier 0]] and its
[[theory/additive_bases/L272_translated_unique_differences/_proof|sliding-count
proof]]. The extensions below use its finitely supported count
$F(j)=|A\cap(j+W)|$, with norm and inner product in
$\ell^2(\mathbb Z)$, and the identities

$$
\|F\|^2\le k|W|+|W|^2-|W|,\qquad
\langle F,F(\cdot+s)\rangle=|W|^2,\qquad
\|F-F(\cdot+s)\|^2\le2|W|(k-1).
$$

The hypothesis $|s|>\operatorname{diam}W$ is where the integers enter:
the multiples of $s$ leave $W-W$ and never return to it. The proof uses
nothing else about $\mathbb Z$. In any abelian group, if $A$ has $k$
elements and distinct non-zero differences, $s+(W-W)\subseteq A-A$, and
$js\notin W-W$ for $1\le j<\max(K,2)$, the same argument gives the
same inequality. In a finite group the multiples of $s$ can return to
$W-W$, so the bound need not hold without that avoidance condition.
The difference set of the L208 set in $\mathbb F_q^3$ contains every
$(x,y,0)$ with $x\ne0$. For prime $q\ge5$, take
$W=\{(x,y,0):0\le x<\lfloor q/4\rfloor,\ y\in\mathbb F_q\}$ and
$s=(\lfloor q/2\rfloor,0,0)$, interpreting the displayed integers as
field elements. Every element of $s+(W-W)$ has nonzero first coordinate,
so this translate lies in the difference set. Here
$|W|=q\lfloor q/4\rfloor$ and $k=2q-1$. This gives counterexamples to
an unrestricted finite-group bound along arbitrarily large primes.
In L209 the subgroup $\mathbb Z_q\times\{0\}$ likewise allows large
translated difference sets without the avoidance condition.

The proof uses $r(t)\le1$ only for $t\in(W-W)\setminus\{0\}$, and
$r(s+t)=1$ only for $t\in W-W$. Under the hypothesis of L239, that every
$1\le d\le L$ has exactly one representation $d=b'-b$, take
$u=\lfloor(L+1)/2\rfloor$, $W=\{0,\dots,u-1\}$ and $s=u$. Then
$s+(W-W)=\{1,\dots,2u-1\}$, and the theorem gives
$L\le2u\le(3+2\sqrt2)k^{5/3}$, the leading term of the bound of L239.
This comparison uses the proof's restricted uniqueness conditions, not a
global Sidon hypothesis absent from L239. The case $L=0$ is immediate.

## Progressions and combs

**Corollary 2.** Let $A$ be a Sidon set of $k\ge2$ integers. If $A-A$
contains an arithmetic progression $x,x+\delta,\dots,x+(\ell-1)\delta$
of positive integers, with integers $\delta,\ell\ge1$, then
$\ell\le(3+2\sqrt2)k^{5/3}$.
In particular every interval of positive integers inside $A-A$ has at
most $(3+2\sqrt2)k^{5/3}$ elements.

*Proof.* Put $u=\lfloor(\ell+1)/2\rfloor$,
$W=\{0,\delta,\dots,(u-1)\delta\}$ and $s=x+(u-1)\delta$. Then
$s+(W-W)$ is the progression $x,\dots,x+(2u-2)\delta$, which lies in the
given one, and $s\ge1+(u-1)\delta>\operatorname{diam}W$. Theorem 1 gives
$u\le(3/2+\sqrt2)k^{5/3}$, and $\ell\le2u$. $\square$

Since $A-A=-(A-A)$, the same bound holds for progressions of negative
integers.

**Corollary 3.** Let $L\ge u\ge1$ and $w\ge1$ be integers. If $A-A$
contains every $\sigma L+\varepsilon$ with $1\le\sigma\le2w-1$ and
$|\varepsilon|\le u-1$, then $wu\le(3/2+\sqrt2)k^{5/3}$.

*Proof.* Take
$W=\{\sigma L+\varepsilon:0\le\sigma<w,\ 0\le\varepsilon<u\}$, which has
$wu$ elements because $L\ge u$, and $s=wL$. Then $W-W$ consists of the
$\sigma L+\varepsilon$ with $|\sigma|\le w-1$ and $|\varepsilon|\le u-1$,
so $s+(W-W)$ is the given set, and
$\operatorname{diam}W=(w-1)L+u-1<wL$. $\square$

The set of Corollary 3 is a comb: $2w-1$ teeth of $2u-1$ consecutive
integers with period $L$. It is the integer form of a two-dimensional
progression, the nearest integer analogue of a subgroup with its cosets.
Its size is $O(k^{5/3})$ whatever the period.

## Bohr sets and linear sign functions

For $\alpha\in\mathbb R$, $\eta\in(0,1]$ and $X\ge1$, let
$B(\alpha;\eta,X)$ be the set of integers $t$ with $|t|<X$ and
$\operatorname{dist}(t\alpha,\mathbb Z)<\eta$.

**Corollary 4.** If $s+B(\alpha;\eta,X)\subseteq A-A$ and $|s|\ge X$,
then $\eta X\le(9+6\sqrt2)k^{5/3}$.

*Proof.* Split $[0,1)$ into $\lceil2/\eta\rceil\le3/\eta$ arcs of length
at most $\eta/2$. One arc contains the fractional part of $n\alpha$ for
at least $\eta X/6$ of the integers $0\le n<X/2$; let $W$ be the set of
these $n$. Every $t\in W-W$ has $|t|<X/2$ and
$\operatorname{dist}(t\alpha,\mathbb Z)<\eta/2$, so
$W-W\subseteq B(\alpha;\eta,X)$, and $\operatorname{diam}W<X/2<|s|$.
Theorem 1 gives $\eta X/6\le|W|\le(3/2+\sqrt2)k^{5/3}$. $\square$

Now let $B\subset[0,q)$ be a set of $k\ge2$ integers whose residues form
a perfect difference set modulo $q=k^2-k+1$, and let $D=B-B$. By the
[half-set lemma](integer_transfer.md), for every integer $0<\rho<q$
exactly one of $\rho$ and $\rho-q$ lies in $D$. The sign $[\rho\in D]$
decides every carry of the anchored lifts in the
[integer transfer analysis](integer_transfer.md).

A run of consecutive $\rho$ in $(0,q)$ on which the sign is constant has
at most $(3+2\sqrt2)k^{5/3}$ elements. A run inside $D$ is an interval
of positive integers in $D$. For a run outside $D$, the half-set lemma
and $D=-D$ put the integers $q-\rho$ in $D$. Corollary 2 applies in both
cases.

**Corollary 5.** If $k>2\cdot10^8$, there are no real $\alpha,\beta$ with

$$
D\cap(0,q)=\{\rho\in(0,q):\{\rho\alpha+\beta\}<1/2\}.
$$

*Proof.* Suppose such $\alpha,\beta$ exist and write
$\varphi(\rho)=\{\rho\alpha+\beta\}$. Let $I$ be the set of integers in
$[3q/8,5q/8]$, so $|I|\ge q/4-1$.

First suppose some $\rho_0\in I$ has $\varphi(\rho_0)\in[1/8,3/8]$.
Among the integers $0\le n<q/8$, at least $q/128$ have $\{n\alpha\}$ in
one of the sixteen arcs $[i/16,(i+1)/16)$; let $W$ be the set of them.
For $t\in W-W$, the integer $\rho_0+t$ lies in $(q/4,3q/4)$ and
$\varphi(\rho_0+t)$ lies in $(1/16,7/16)$, so $\rho_0+t\in D$. As
$\rho_0\ge3q/8>\operatorname{diam}W$, Theorem 1 gives
$q/128\le(3/2+\sqrt2)k^{5/3}$.

Otherwise $\varphi$ avoids $[1/8,3/8]$ on $I$. Two of the fractional
parts of $j\alpha$, $0\le j\le8$, lie in one arc $[i/8,(i+1)/8)$, so
some $1\le h\le8$ has $h\alpha=m+\theta$ with $m\in\mathbb Z$ and
$|\theta|<1/8$. Fix a residue class modulo $h$ and let $P$ be its
elements in $I$, so that $|P|\ge q/32-9/8$. Along $P$ the phase changes
by $\theta$ modulo $1$ at each step. Lift it to real numbers changing by
$\theta$ at each step. A step is shorter than the gaps
$[1/8,3/8]+\mathbb Z$, which the lifted phase never meets, so the lifted
phase stays in one interval $(3/8+n,9/8+n)$. There the sign
$[\varphi<1/2]$ changes only at $1/2+n$ and at $1+n$, and the lifted
phase is monotone. So $P$ splits into at most three runs of constant
sign, and some run is a progression with difference $h$ and at least
$q/96-3/8$ terms. If its terms lie in $D$, Corollary 2 applies to it.
If not, the half-set lemma and $D=-D$ put the progression of the
$q-\rho$ in $D$, and Corollary 2 applies to that. Either way
$q/96-3/8\le(3+2\sqrt2)k^{5/3}$.

In both cases $q\le560k^{5/3}+36$. With $q=k^2-k+1$ this fails for
$k>2\cdot10^8$. $\square$

So no perfect difference set of large order has a sign function decided
by a linear form in this way. The constants are not optimized.

## Several translates

Translates of one difference set at many places are bounded jointly,
and the places need only be separated.

**Lemma.** Let $X,Y\subset\mathbb Z$ be finite and non-empty and let
$\delta\ge0$. If consecutive elements of $X$ differ by more than
$\delta$, and so do consecutive elements of $Y$, then $X+Y$ contains
$|X|+|Y|-1$ elements whose consecutive differences all exceed $\delta$.

*Proof.* With $x_1<\dots<x_n$ and $y_1<\dots<y_m$, the chain
$x_1+y_1<x_1+y_2<\dots<x_1+y_m<x_2+y_m<\dots<x_n+y_m$ has every step
equal to some $y_{j+1}-y_j$ or some $x_{i+1}-x_i$. $\square$

By induction on $m$, if $S$ has $\lambda$ elements whose consecutive
differences exceed $\delta$, then the sums of $m$ elements of $S$,
repetition allowed, include $m(\lambda-1)+1$ integers whose pairwise
differences exceed $\delta$.

**Proposition 6.** Let $A$ be a Sidon set of $k\ge2$ integers and let
$W$ be finite and non-empty. Let $s_1<\dots<s_\lambda$ be integers with
$s_1>\operatorname{diam}W$, $s_{i+1}-s_i>\operatorname{diam}W$ and
$s_i+(W-W)\subseteq A-A$ for every $i$. Then for every integer $m\ge1$

$$
\sqrt{|W|}\le\frac{k}{\sqrt{m(\lambda-1)+1}}+m\sqrt{2(k-1)}.
$$

*Proof.* As in the proof of Theorem 1, $\|F\|\ge|W|$ and
$\|F-F(\cdot+s_i)\|^2\le2|W|(k-1)$ for every $i$. By the lemma, the sums
of $m$ of the $s_i$ include a set $\Sigma$ of $m(\lambda-1)+1$ integers
whose pairwise differences exceed $\operatorname{diam}W$, so they lie
outside $W-W$. Telescoping gives $\|F-F(\cdot+\tau)\|\le m\sqrt{2|W|(k-1)}$
for each $\tau\in\Sigma$. The windows $j+\tau+W$, $\tau\in\Sigma$, are
pairwise disjoint, so the average $g$ of the $F(\cdot+\tau)$ satisfies
$0\le g\le k/|\Sigma|$ and $\|g\|^2\le k^2|W|/|\Sigma|$, while
$\|F-g\|\le m\sqrt{2|W|(k-1)}$. The triangle inequality finishes the
proof. $\square$

**Corollary 7.** Let $u\ge8k$. If $A-A$ contains $\lambda$ pairwise
disjoint intervals, each of $2u-1$ positive integers, then
$\lambda\le1+113k^{5/2}u^{-3/2}$. Hence the positive elements of $A-A$
lying in runs of at least $2u-1$ consecutive integers number at most
$4u+452k^{5/2}u^{-1/2}$.

*Proof.* Take $W=\{0,\dots,u-1\}$ and let $s_i$ be the centres of the
intervals. Then $s_i+(W-W)$ is the $i$-th interval,
$s_1\ge u>\operatorname{diam}W$, and consecutive centres differ by at
least $2u-1$. For $\lambda\ge2$ apply Proposition 6 with
$m=\lceil k^{1/3}(\lambda-1)^{-1/3}\rceil$. The right side is at most
$(1+\sqrt2)k^{5/6}(\lambda-1)^{-1/3}+\sqrt{2k}$, and
$\sqrt{2k}\le\sqrt u/2$, so
$\sqrt u\le2(1+\sqrt2)k^{5/6}(\lambda-1)^{-1/3}$; this gives the first
claim. A run of $L\ge2u-1$ consecutive integers contains at least
$L/(4u)$ disjoint intervals of $2u-1$ integers, which gives the second.
$\square$

For fixed $0<\varepsilon\le2/3$ and sufficiently large $k$, apply this
with $u_0=\lceil k^{1+\varepsilon}\rceil\ge8k$. Since
$1+\varepsilon\le2-\varepsilon/2$, runs of length at least $2u_0-1$
carry $O(k^{2-\varepsilon/2})$ positive differences. The same bound
holds for any larger threshold, and symmetry gives the bound for both
signs.

If the positions have no small linear relations, the bound per
translate improves.

**Proposition 8.** Let $A$ be a Sidon set of $k\ge2$ integers, let $W$
be finite and non-empty, and let $d\ge1$ and $s_1,\dots,s_d$ be integers with
$s_i+(W-W)\subseteq A-A$ for every $i$. Let $m\ge1$, and suppose that
$\sum_ib_is_i\notin W-W$ for every non-zero $b\in\mathbb Z^d$ with
$\sum_i|b_i|\le m$. Then

$$
\sqrt{|W|}\le k\Bigl(\frac{d}{m}\Bigr)^{d/2}+m\sqrt{2(k-1)}.
$$

*Proof.* The case $b=e_i$ of the hypothesis gives $s_i\notin W-W$, so
the first part of the proof of Theorem 1 applies to each $s_i$:
$\|F-F(\cdot+s_i)\|^2\le2|W|(k-1)$ and $\|F\|\ge|W|$. Let $Q$ be the set
of $b\in\mathbb Z^d$ with $0\le b_i\le\lfloor m/d\rfloor$, so
$|Q|\ge(m/d)^d$, and put $\tau_b=\sum_ib_is_i$. Each $\tau_b$ is a sum of
at most $m$ of the $s_i$, so $\|F-F(\cdot+\tau_b)\|\le m\sqrt{2|W|(k-1)}$.
For $b\ne b'$ in $Q$ we have $0<\sum_i|b_i-b'_i|\le m$, so
$\tau_b-\tau_{b'}$ is not in $W-W$. Hence the average $g$ of the
$F(\cdot+\tau_b)$, $b\in Q$, satisfies $0\le g\le k/|Q|$, so
$\|g\|^2\le k^2|W|/|Q|$, and $\|F-g\|\le m\sqrt{2|W|(k-1)}$. The
triangle inequality $\|F\|\le\|g\|+\|F-g\|$ finishes the proof.
$\square$

If the nonrelation hypothesis holds for an integer $m$ of order
$k^{1/(d+2)}$, this gives $|W|=O_d(k^{(d+4)/(d+2)})$. For instance,
two translates give $|W|=O(k^{3/2})$ when the stated nonrelation
condition holds through $m\asymp k^{1/4}$.

## Incomplete translates

**Proposition 9.** Let $A$ be a Sidon set of $k\ge2$ integers, let $W$
be finite and non-empty, let $|s|>\operatorname{diam}W$, and let
$0\le\varepsilon<1$. Suppose that $s+w'-w\in A-A$ for all but at most
$\varepsilon|W|^2$ pairs $(w,w')\in W^2$. Then for every integer $K\ge1$

$$
\sqrt{(1-\varepsilon)|W|}\le\frac{k}{\sqrt K}
 +\frac{K-1}{2}\sqrt{2k+2\varepsilon|W|}.
$$

*Proof.* In the proof of Theorem 1 the inner product is now
$\langle F,F(\cdot+s)\rangle\ge(1-\varepsilon)|W|^2$. So
$\|F\|^2\ge(1-\varepsilon)|W|^2$ and
$\|F-F(\cdot+s)\|^2\le2k|W|+2\varepsilon|W|^2$, and the rest is
unchanged. $\square$

Let $\varepsilon\le1/64$. If $\varepsilon|W|\le k$, take
$K=\lceil k^{1/3}\rceil$; the right side is at most $2k^{5/6}$. If
$\varepsilon|W|>k$, take $K=\lceil1/(4\sqrt\varepsilon)\rceil$; then
$k/\sqrt K\le2k\varepsilon^{1/4}$ and the second term is at most
$\sqrt{|W|}/4$. The two cases give

$$
|W|\le\max\bigl(5k^{5/3},\,8\sqrt\varepsilon\,k^2\bigr).
$$

Thus if $|W|=\beta k^2>5k^{5/3}$ and at most an $\varepsilon$
proportion of the pairs $(w,w')\in W^2$ have
$s+w'-w\notin A-A$, then $\varepsilon\ge\min(1,\beta^2)/64$.
The missing proportion counts pairs, with their multiplicities, rather
than distinct elements of $s+(W-W)$. This extends the
stability estimate of the
[consecutive-difference note](consecutive_differences.md) from initial
intervals to translated difference sets.

## Bearing on Problem 156

Suppose that $A\subset[1,N]$ is strong Sidon with $k$ elements, that
$T\subseteq A$, and that $P=s+(W-W)\subseteq A-A$ with
$|s|>\operatorname{diam}W$ and $|W-W|\le\mu|W|$. If $T+P$ contains
every target outside $A$, then $|T||P|\ge N-k$ and Theorem 1 gives

$$
k^{8/3}\ge\frac{N-k}{(3/2+\sqrt2)\mu}.
$$

Intervals, progressions and the combs of Corollary 3 have $\mu\le4$.
So, for fixed $\mu$, a construction satisfying this particular coverage
hypothesis has at least $c_\mu N^{3/8}$ elements. This excludes the
stated imitation of the group constructions at the cube-root scale.
It is not a bound for constructions using several pieces or other
blocking triples. The same cardinality argument allows $O(k^2)$ targets
to be handled separately, including all midpoint blockers: replace
$N-k$ by $N-k-O(k^2)$ in the displayed inequality. It still contradicts
$k=O(N^{1/3})$ for fixed $\mu$.

The theorem leaves open the following.

- **Unseparated translates.** If $|s|\le\operatorname{diam}W$, the
  averaging proof no longer guarantees that its windows are disjoint or
  that every required difference is nonzero. No conclusion for that
  case is established here. The trivial example $s=0$, $W=A$ gives
  $W-W\subseteq A-A$; it is not a counterexample to the theorem's bound.
- **Dense pieces.** For a Singer base, $D\cap(0,q)$ has $(q-1)/2$
  elements. Theorem 1 bounds only the
  translated difference sets inside such a piece, not the piece, and
  Proposition 9 shows that when $|W|\asymp k^2$, the separated translate
  misses differences from a positive proportion of pairs in $W^2$.
  Blocking through a dense piece fails exactly at its holes. The only
  uniform complementarity mechanism supplied by this account is the pair
  at distance $q$ of the coherence lemma in the
  [integer transfer analysis](integer_transfer.md), which a strong Sidon
  set can use once.
- **Many pieces.** Proposition 6 and Corollary 7 bound translates of one
  $W$ at separated positions; for $0<\varepsilon\le2/3$, runs of length
  at least $2\lceil k^{1+\varepsilon}\rceil-1$ carry only
  $O(k^{2-\varepsilon/2})$ differences in all. Pieces of unrelated
  shapes are not bounded by these arguments.

The [proof sketch](proof_sketch.md) records how this changes the
remaining gap.
