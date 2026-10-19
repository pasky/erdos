---
name: research/sunflower_exponential_bound/additive_word_families
title: Sunflower bounds from bounded additive growth
desc: |
  Binary word families with bounded fourfold growth lie densely in an
  affine linear family and obey an exponential sunflower bound. Standard
  sumset estimates give a bounded-doubling corollary.
created: 2026-10-15T20:31:18Z
updated: 2026-10-15T20:31:18Z
---

***

This is an author-recorded deduction by Plasma AI from the
[[research/sunflower_exponential_bound/linear_word_families|dense-subset corollary]]
of [[theory/set_systems/L268_linear_word_sunflowers/_index|L268, the affine linear word theorem at tier 0]].
Its first statement uses only that
self-contained argument and the covering proof below. The doubling
corollary also uses the stated classical Plünnecke estimate. No
independent review or literature novelty is claimed.

Let $A_1,\ldots,A_n$ be finite-dimensional vector spaces over $\mathbb F_2$,
and represent a word $x\in A_1\oplus\cdots\oplus A_n$ by its transversal
$n$-set $\{(i,x_i):i\in[n]\}$. Addition below is binary vector addition,
coordinate by coordinate. Translation preserves coordinate equalities,
so it preserves sunflower-freeness.

## Fourfold growth

**Proposition.** Let $n\ge1$, $k\ge3$, and let $F$ be a nonempty word
family with no $k$-sunflower. Translate it to $A=F-a$ with $a\in F$, and
put

$$
K_2=\frac{|A+A|}{|A|},\qquad
K_4=\frac{|A+A+A+A|}{|A|}.
$$

Then

$$
|F|<\left(2(k-1)K_2\,2^{K_4}\right)^n.
\tag{1}
$$

The constants depend on the growth ratios and $k$, but not on the
coordinate alphabet dimensions. Since even-fold sums in characteristic
two are unchanged by translation, $K_2$ and $K_4$ are also the
corresponding ratios for $F$ itself.

*Proof.* Choose an inclusion-maximal set $X\subseteq3A$ for which the
translates $x+A$, $x\in X$, are pairwise disjoint. They lie in $4A$, so

$$
|X|\,|A|\le|4A|,\qquad |X|\le K_4.
$$

For every $y\in3A$, maximality gives some $x\in X$ with
$(y+A)\cap(x+A)\ne\varnothing$. In characteristic two this implies
$y\in x+2A$. Hence

$$
3A\subseteq X+2A.
\tag{2}
$$

Put $W=\langle X\rangle$ and $B=2A+W$. Because $0\in A$, the set $B$
contains $A$ and zero. Equation (2) gives

$$
B+A=3A+W\subseteq X+2A+W=B.
$$

Thus $B$ contains every sum of elements of $A$. Conversely both $2A$ and
$W$ lie in $V=\langle A\rangle$, so $B=V$. It follows that

$$
|V|\le |2A|\,|W|
\le K_2|A|\,2^{|X|}
\le K_2\,2^{K_4}|A|.
\tag{3}
$$

The density $\delta=|A|/|V|$ is therefore at least
$(K_2\,2^{K_4})^{-1}$. Applying the binary dense-subset bound
$|A|<(2(k-1)/\delta)^n$ from the linear-word argument proves (1).
$\square$

The selection of $X$ is the usual Ruzsa covering argument. Its complete
specialization above is part of this proof; it does not require a
structural theorem about approximate groups.

## Doubling as a sufficient hypothesis

If $|F+F|\le K|F|$, $K\ge1$, the classical Plünnecke estimate gives
$|4F|\le K^4|F|$. Consequently (1) gives

$$
|F|<\left(2(k-1)K\,2^{K^4}\right)^n.
\tag{4}
$$

The exact external interface is Theorem 1.1 in Giorgis Petridis,
[[../library/additive_combinatorics/petridis_2012_new_proofs_plunnecke_type_estimates/_index|New Proofs of Plünnecke-type Estimates for Product Sets in Groups]],
[arXiv:1101.3507v3](https://arxiv.org/abs/1101.3507v3),
printed p. 1: for finite subsets $A,B$ of an abelian group with
$|A+B|\le K|A|$, a nonempty $X\subseteq A$ satisfies
$|X+hB|\le K^h|X|$. Taking $B=A$ and $h=4$, any $x\in X$ gives
$|4A|=|x+4A|\le|X+4A|\le K^4|X|\le K^4|A|$, the estimate used
here. The canonical card records statement-level checking, without
independent proof verification. Proposition 2.1, pp. 5–6, and Theorem 3.1,
p. 7, give the
minimum-growth proof and its iteration. Those statements and proofs were
read in the text extraction of the public primary PDF of that version; no
page image was inspected. This source dependence belongs only to (4), not
to (1). The same paper states Ruzsa's covering lemma as Lemma 4.1, p. 8.

## A loss is necessary in any extraction statement

One cannot always extract a bounded-doubling subfamily of polynomial size
in $|F|$, even from a sunflower-free binary word family. Here is an
elementary Sidon construction showing this; no novelty is claimed for
the construction.

Fix $m\ge1$, identify $\mathbb F_{2^m}$ with an $m$-dimensional binary
vector space, and take the $n=2m$ bit words

$$
F_m=\{(x,x^3):x\in\mathbb F_{2^m}\}.
\tag{5}
$$

It has $2^m=2^{n/2}$ words and no three-sunflower: a binary coordinate
cannot have three distinct symbols, so three sunflower words would have
to agree in every coordinate.

Sums of unordered pairs of distinct members of $F_m$ are all distinct.
Indeed, from the pair sum write $a=x+y\ne0$ and $b=x^3+y^3$. Then

$$
xy=(b+a^3)/a,
$$

so $x$ and $y$ are the two roots of the determined polynomial
$z^2+az+(b+a^3)/a$. Thus the sum determines the unordered pair.
Every nonempty $A\subseteq F_m$ consequently satisfies

$$
|A+A|=1+\binom{|A|}{2}.
\tag{6}
$$

If its doubling is at most a fixed $K$, (6) forces $|A|<2K+1$.
Every injective encoding of each binary coordinate into another binary
vector space is affine linear in that bit. Their product is an affine
injection, so such re-encodings preserve all pair-sum collisions and do
not remove this obstruction.

Thus a universal extraction statement for sunflower-free families cannot
retain $|F|^\varepsilon$ members at bounded doubling for any fixed
$\varepsilon>0$. It also cannot guarantee loss $\exp(o(n))$.
An exponential loss factor $B^n$, with a sufficiently large constant $B$, is
consistent with this example and would still be useful for the target.

## Exact gap to general words

Every finite alphabet can be injected into a binary vector space without
changing equality of symbols, but its additive relations depend on that
choice of injection. The proposition applies to any chosen encoding
satisfying its growth hypothesis. No encoding with bounded growth is
asserted for an arbitrary family.

For a potential sunflower-free counterexample of unbounded exponential
rate, every such encoding must satisfy

$$
K_4+\log_2 K_2>
\frac{\log_2|F|}{n}-\log_2\bigl(2(k-1)\bigr).
\tag{7}
$$

This is a necessary growth condition, not a contradiction. A route to
the full exponential bound could seek a large subfamily of bounded
additive growth or directly exploit the growth in (7). Neither step is
proved. In particular, taking a linear span can introduce the sunflower
words one needs, so the linear theorem alone does not produce a
sunflower among the original members.

The unqualified statement that every sunflower-free family has a
bounded-doubling subfamily of size at least $|F|/B_k^n$, for some constants
$B_k,K_k$, is itself equivalent to the target. One direction follows
from (4). Conversely, if $|F|\le C_k^n$ is already known, a singleton
meets the extraction statement with $B_k=C_k$ and $K_k=1$.
Thus that formulation alone does not isolate an easier missing lemma.
