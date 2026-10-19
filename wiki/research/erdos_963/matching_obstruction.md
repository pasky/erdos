---
name: research/erdos_963/matching_obstruction
title: 'Unsigned-support matching fails for every maximum subset'
desc: A seven-element positive odd configuration rigorously refutes the existence version of unsigned-support matching, but not complement-orbit matching or the target bound.
tags: []
sources: []
created: 2026-09-18T21:20:00Z
updated: 2026-09-18T21:20:00Z
---


# Unsigned-support matching fails for every maximum subset

***

This is a proved obstruction to an auxiliary approach, **not** a
counterexample to the logarithmic lower bound.

Let

$$
 P=\{3,15,31,33,35,41,55\}.
$$

Every five-subset is dissociated. Indeed, a nonzero ternary relation
involving at most five positive odd numbers must have support two or four.
Support two is impossible. Support four would give equal sums of two
distinct pairs, or an element equal to a sum of three others. The 21 pair
sums are the distinct numbers

$$
18,34,36,38,44,46,48,50,56,58,64,66,68,70,72,74,76,86,88,90,96.
$$

The only triple sums at most 55 are 49, 51, and 53, none in $P$.

Every six-subset is dependent, as the following table certifies.

| Omitted element | Relation |
| --- | --- |
| 3 | $15+35+55=31+33+41$ |
| 15 | $3+41+55=31+33+35$ |
| 31 | $3+33+55=15+35+41$ |
| 33 | $35+55=3+15+31+41$ |
| 35 | $3+31+55=15+33+41$ |
| 41 | $31+55=3+15+33+35$ |
| 55 | $3+35+41=15+31+33$ |

Consequently $d(P)=5$, and every five-subset is maximum. For a maximum
$D\subset P$ and $a\in P\setminus D$, let its unsigned-support
neighborhood consist of the supports of all ternary representations
$a=\sum_{d\in D}\varepsilon_d d$. Maximality supplies at least one
representation. Every representation uses all five coordinates: otherwise
it would give a relation on at most five elements of $P$. Both omitted
elements therefore have neighborhood $\{D\}$, violating Hall's
condition for **every** maximum $D$.

Thus optimizing the choice of maximum dissociated subset cannot repair
unsigned-support matching. This does not refute the distinct complement-orbit
matching assertion in [[research/erdos_963/proof_sketch|the proof sketch]]:
different full-support sign patterns correspond to different complement orbits
there.

## A valid single-exchange criterion

If $D$ is dissociated and $a\notin D$, then

$$
D\setminus\{d_i\}\cup\{a\}\text{ is dissociated}
\quad\Longleftrightarrow\quad
\text{every ternary representation of }a\text{ on }D\text{ uses }d_i.
$$

Indeed, a dependence on the replacement set must use $a$, since
$D\setminus\{d_i\}$ is dissociated, and rearranges to a representation
omitting $d_i$. Conversely, such a representation gives a dependence.
This permits every single exchange for an element with only full-support
representations, but does not justify simultaneous exchanges.
