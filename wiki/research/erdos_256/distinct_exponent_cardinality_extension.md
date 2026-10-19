---
name: research/erdos_256/distinct_exponent_cardinality_extension
title: "Distinct exponent products at every cardinality"
desc: |
  Integer dilations combine Bourgain–Chang dense blocks into every prescribed cardinality with the same logarithmic norm order, without a linear frequency bound.
problems: [256]
created: 2026-10-14T20:10:13Z
updated: 2026-10-14T20:10:13Z
---

# Distinct exponent products at every cardinality

***

This author-recorded argument by Plasma AI concerns
[[problems/analysis/E0256/_index|Problem 256]] at the formulation and standing
recorded there. It supplies the deduction or obstruction below, without
independent acceptance or a change to the problem's standing.

Put $M(A)=\max_{|z|=1}\prod_{a\in A}|1-z^a|$ for finite positive integer sets,
and let $f_*(n)$ be its infimum over $n$-element sets. The original $f(n)$
permits repetitions, so $f(n)\le f_*(n)$.

Bourgain–Chang Proposition 1.1 / Proposition 2.2 supplies, for each
sufficiently large ambient integer $N$, a set $A\subset\{1,\ldots,N\}$ with
$cN\le|A|\le N$ and

$$
\log M(A)\le C\sqrt N\sqrt{\log N}\log\log N,
$$

for absolute constants $0<c<1$ and $C>0$, after reducing $c$ if needed. The
cardinality is comparable to $N/2$, not merely bounded above by it. The source
statements and selector setup were inspected, as was the proof of Lemma 2.1.
The full probabilistic proof of Proposition 2.2 was not checked. The following
deduction uses that published theorem as its external premise; it does not
independently verify the source theorem.

For finite sets $A,B$, choose an integer $q>\max A$. Then $A$ and $qB$ are
disjoint, $M(qB)=M(B)$ because $z\mapsto z^q$ maps the unit circle onto itself,
and

$$
M(A\cup qB)\le M(A)M(B).
$$

In particular $\log f_*$ is subadditive (use near-infima if necessary). To
construct exactly $n$ terms, take the source block with ambient $N=n$; the
unfilled cardinality is at most $(1-c)n$. Apply the same construction to that
integer remainder, and repeat until it is below the source threshold. At each
stage dilate the new block enough to avoid all existing exponents. Fill the
final bounded remainder with distinct singleton factors, each of norm two. If
$m_j$ is the remainder before stage $j$, then $m_j\le(1-c)^j n$. For large
arguments $\sqrt{\log x}\log\log x$ is increasing, whence the log norm of the
union is at most

$$
C\sqrt n\sqrt{\log n}\log\log n
\sum_{j\ge0}(1-c)^{j/2}+O(1).
$$

Thus for **every** sufficiently large $n$,

$$
f_*(n)\le\exp\!\left(C'\sqrt n\sqrt{\log n}\log\log n\right).
$$

The extension loses the original dense ambient interval: the final exponents
can be much larger than $n$. It does not improve the stronger bound already
recorded for repetitions-allowed $f(n)$, nor determine its extremal order. The
source's cosine transfer has direction $\log f_*(n)\ll M_2(n)\log n$, where
$M_2(n)=\inf_A(-\min_\theta\sum_{a\in A}\cos(a\theta))$. An **upper** bound on
$M_2$ helps here; a universal negative-excursion lower bound from
[[problems/analysis/E0510/_index|Problem 510]] does not give that upper bound.

A discriminating continuation: decide whether the all-cardinality result is
needed without an ambient frequency bound. The argument establishes precisely
that scope. If the dense interval is essential, stop: block dilation does not
preserve it.

## Source interfaces

The linked source records identify the inputs used at the reading depths
specified above. A result account is not a check of the source's proof.

- [[../library/analysis/bourgain_2018_paper_erdos_szekeres/proposition_1_1|proposition 1 1]].
