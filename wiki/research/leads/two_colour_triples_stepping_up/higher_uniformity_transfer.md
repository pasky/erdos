---
name: research/leads/two_colour_triples_stepping_up/higher_uniformity_transfer
title: The conditional two-colour transfer from triples to higher uniformity
desc: |
  A complete two-colour stepping-up argument for k >= 3, with vertex order
  2^N and forbidden size 2n+k-4, and its conditional implication from a
  double-exponential triple bound to every fixed higher uniformity.
tags: []
sources: []
created: 2026-10-16T15:39:01Z
updated: 2026-10-16T15:39:01Z
---

# The conditional two-colour transfer from triples to higher uniformity

***

This page supplies the higher-uniformity link in the
[[research/leads/two_colour_triples_stepping_up/_index|two-colour triple sketch]].
It does not supply the missing triple construction. The lemma is the
classical Erdős--Hajnal stepping-up lemma, stated with this range and
constant in the abstract of Conlon, Fox and Sudakov,
[*An improved bound for the stepping-up lemma*, arXiv:0907.0283v1](https://arxiv.org/abs/0907.0283v1).
Only that abstract was consulted here. The elementary two-colour proof
below is an author-recorded derivation by Plasma AI, not a reconstruction
or independent review of that paper's proof. It avoids relying on the
ambiguous range printed in the 1965 source discussed on the problem page.

## Exact transfer

**Lemma.** Let $n\ge k\ge3$. If $\varphi:\binom{[N]}k\to\{0,1\}$ has
no monochromatic $n$-set, there is a colouring of the $(k+1)$-sets of
$\{0,1\}^N$ with exactly the same two available colours and no
monochromatic $(2n+k-4)$-set.

Relabel the seed vertices by positions $0,\ldots,N-1$ and order the binary
words as integers. For two distinct words define
$\delta$ to be the largest differing position. Two basic facts follow
directly from binary order: adjacent deltas in an increasing list differ,
and the delta of its endpoints is the maximum of its consecutive deltas.
For the first fact, two consecutive crossings of the same highest bit
would require the middle word's bit to be both one and zero. For the
second, split at the largest position that varies in the list: all zeros
at that position precede all ones, and that unique crossing is its largest
consecutive delta.

For $x_1<\cdots<x_{k+1}$ write $d_i=\delta(x_i,x_{i+1})$. If the $k$
deltas are monotone, give this $(k+1)$-set colour
$\varphi(\{d_1,\ldots,d_k\})$. Otherwise find its first local extremum:
give a local maximum colour zero and a local minimum colour one. This is
defined because adjacent deltas differ and a nonmonotone finite sequence
with that property has a local extremum. No additional colour is used.

Suppose $x_1<\cdots<x_m$ is monochromatic, where $m=2n+k-4$, and put
$d_i=\delta(x_i,x_{i+1})$ for $1\le i<m$. Any local extremum at an index
$2\le i\le m-k+1$ must have the type of this monochromatic colour: take
the four consecutive words $x_{i-1},x_i,x_{i+1},x_{i+2}$ and append any
$k-3$ later words. There are enough later words because
$m-(i+2)\ge k-3$. The resulting delta list has its first local extremum
at its second position, of precisely the original type.

Consecutive local extrema of a sequence with unequal neighbours alternate
between maxima and minima. Consequently the prefix
$d_1,\ldots,d_{m-k+2}$ has at most one local extremum. Its length is
$2n-2$. If it is monotone, it contains $n$ monotone deltas. If it has one
extremum, its two monotone runs overlap at that entry and their lengths sum
to $2n-1$, so one again has at least $n$ entries.

Any $k$ selected values from that monotone run occur as the consecutive
deltas of a $(k+1)$-subset of its words. In an increasing run, select its
first word and the right endpoints of the selected deltas; every interval
maximum is its last delta. In a decreasing run, select the left endpoints
of the selected deltas and the final run word; every interval maximum is
its first delta. Thus every $k$-subset of these $n$ delta values has the
same $\varphi$-colour as the lifted monochromatic set. This contradicts
the seed hypothesis and proves the lemma. $\square$

In Ramsey forcing-number notation the conclusion is

$$
R_{k+1}(2n+k-4)\ge2^{R_k(n)-1}+1.
$$

The minus one comes from taking a colouring on $R_k(n)-1$ vertices; it
cannot be silently omitted. The lemma starts at $k=3$. It gives no graph
to triple lift: with only two deltas there is no local extremum to use in
the nonmonotone clause.

## Composition with a hypothetical triple construction

Define $\operatorname{twr}_1(x)=x$ and
$\operatorname{twr}_{j+1}(x)=2^{\operatorname{twr}_j(x)}$.
Suppose for all sufficiently large $t$ there are two-colour triple
colourings of orders $N_3(t)\ge\operatorname{twr}_3(a t)$ with no
monochromatic $t$-set, for some $a>0$. Set

$$
n_3(t)=t,\qquad n_{k+1}(t)=2n_k(t)+k-4,
\qquad N_{k+1}(t)=2^{N_k(t)}.
$$

Repeated application of the lemma gives two-colour $k$-uniform examples
of order $N_k(t)\ge\operatorname{twr}_k(a t)$ with forbidden size

$$
n_k(t)=2^{k-3}t-k+3.
$$

The formula follows directly by induction, including its negative additive
term. For each fixed $k$, take
$t=\lfloor(n+k-3)/2^{k-3}\rfloor$. Then $n_k(t)\le n$ and eventually
$t\ge n/2^{k-2}$. Monotonicity yields
$R_k(n)>\operatorname{twr}_k(a n/2^{k-2})$ for all sufficiently large $n$.

A lower bound on $R_3(t)$ alone also supplies the assumed examples after
decreasing $a$: the available order is $R_3(t)-1$, and for any fixed
$0<a<c$ one has
$\operatorname{twr}_3(ct)-1\ge\operatorname{twr}_3(at)$ eventually.
Uniformity two has the elementary random graph bound
$R_2(n)>\lfloor2^{n/4}\rfloor$ for $n\ge4$, hence the required
height-two bound after reducing its constant. For $r\ge3$, combine the
lower bound with the classical upper bound
$R_r(n)\le\operatorname{twr}_r(O_r(n))$, stated in
[[../library/ramsey_theory/erdos_1965_partition_relations_cardinal_numbers/statement_16_3|Erdős--Hajnal--Rado, statement 16.3]],
which credits Erdős and Rado. That upper bound is used as a literature
statement; the 1965 text omits its proof and no proof of the upper bound is
reconstructed here. The combination gives
$\log_{r-1}R_r(n)\asymp_r n$, the full asymptotic conclusion of
[[problems/ramsey_theory/E0562/_index|Problem 562]]. All transfers use two
colours. The triple premise is the unresolved research premise in this
composition, and remains unresolved here.
