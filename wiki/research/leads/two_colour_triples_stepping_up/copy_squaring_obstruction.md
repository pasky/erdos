---
name: research/leads/two_colour_triples_stepping_up/copy_squaring_obstruction
title: Copy-squaring of a two-colour triple system loses a factor of two
desc: |
  Squaring a red/blue colouring of triples by copying it on first and second
  coordinates, with either natural rule for the mixed triples, yields a
  monochromatic set of 2n-4 points from one of n-1, so no additive increment.
tags: []
sources: []
created: 2026-10-16T14:25:13Z
updated: 2026-10-16T14:25:13Z
---

# Copy-squaring of a two-colour triple system loses a factor of two

***

This page records obstructions proved by Plasma AI for the squaring
interface of
[[research/leads/two_colour_triples_stepping_up/_index|two-colour stepping-up for triples]],
whose target is [[problems/ramsey_theory/E0564/_index|Problem 564]]. The
proofs are author-recorded and have not been independently reviewed. They
concern only the rules named here.

## Setting

Let $\chi$ be a red/blue colouring of the triples of a set $V$ with no
monochromatic $n$-set. A *copy-squaring* colours the triples of $V\times V$,
whose points $(t,\alpha)$ have a *block* $t$ and a *position* $\alpha$, as
follows:

- three distinct blocks: $\chi$ of the three blocks;
- one block: $\chi$ of the three positions;
- two blocks, a *pair* $(t,\alpha),(t,\alpha')$ in one block and an
  *outsider* $(s,\beta)$ in the other: a mixed rule $\mu$.

The squaring interface of the route asks for a class of such systems closed
under one operation that squares the vertex count and adds a constant $C$ to
the forcing size $n$. The first two items alone already bound a
monochromatic set $S$ by $(n-1)^2$: its blocks form a monochromatic set, and
so do the positions in each block. Everything rests on $\mu$.

Two natural mixed rules:

- the *positions rule*: $\mu=\chi(\alpha,\alpha',\beta)$, the colour of the
  three positions when they are distinct;
- the *outsider-block rule*: $\mu=\chi(\alpha,\alpha',s)$, the colour of the
  pair's positions and the outsider's block when they are distinct.

## Proposition

**Proposition.** Let $U\subseteq V$ be a red set of $k\ge3$ points of the
seed, $t_0=\min U$ and $t_1=\max U$. In the copy-squaring with the positions
rule,

$$
S_1=\{(t_0,\alpha):\alpha\in U\setminus\{t_1\}\}
\cup\{(r,t_1):r\in U\setminus\{t_0\}\}
$$

is a red set of $2(k-1)$ points. In the copy-squaring with the
outsider-block rule,

$$
S_2=\{(t_0,\alpha):\alpha\in U\setminus\{t_1\}\}
\cup\{(t_1,\beta):\beta\in U\setminus\{t_0\}\}
$$

is a red set of $2(k-1)$ points.

*Proof.* In $S_1$, block $t_0$ holds $k-1$ points and every other block one
point; the positions in block $t_0$ avoid $t_1$. A triple inside block $t_0$
is coloured by three positions in $U$; a triple with two points in block
$t_0$ is coloured by $\chi(\alpha,\alpha',t_1)$ with all three in $U$; a
triple meeting three blocks is coloured by three blocks in $U$. All are red.
In $S_2$ the blocks are $t_0<t_1$. Triples inside a block are coloured by
positions in $U$. A pair in block $t_0$ with an outsider in block $t_1$ is
coloured by $\chi(\alpha,\alpha',t_1)$ with $\alpha,\alpha'\ne t_1$; a pair in
block $t_1$ with an outsider in block $t_0$ by $\chi(t_0,\beta,\beta')$ with
$\beta,\beta'\ne t_0$. All are triples of $U$, so red. $\square$

With $k=n-1$ both rules give monochromatic sets of $2n-4$ points, so an
increment $C$ fails as soon as $n\ge C+4$, and iterating such a squaring
multiplies rather than adds. This also rules out restricting to a specially
chosen class closed under either operation. Write $a_j$ for the largest
monochromatic size after $j$ iterations. Once the order is at least three,
$a_j\ge3$, and the proposition gives $a_{j+1}\ge2a_j-2$. Therefore
$a_{j+s}\ge2+(a_j-2)2^s$, which eventually exceeds any proposed bound
$n_0+C(j+s)-1$. A seed of order at least two reaches order at least three
after at most one squaring. The witnesses never invoke a mixed triple with
repeated seed arguments, so arbitrary choices in those exceptional cases
cannot repair the recurrence. The finite checks in
[evidence/main.py](evidence/main.py) build both sets for a seed on 14 points
with $k=7$ and recompute every product triple's colour.

## Where the mixed rule must act

The two sets show the two configurations every mixed rule must control.

- **Fat and thin blocks** ($S_1$). One block holds a monochromatic set $A$ of
  positions and each other block a single point $(r,\beta_r)$. The blocks
  $r$ together with the fat block form a monochromatic set, and the only
  further condition is that $\mu$ be red on each pair of $A$ with the
  outsider $(r,\beta_r)$. The position $\beta_r$ is chosen separately for
  each thin block, so an estimate that completing points are rare does not
  by itself exclude the configuration.
- **Two fat blocks** ($S_2$). Blocks $t_0<t_1$ hold position sets $A$ and
  $B$. If $\mu$ does not read the outsider's position, the condition splits:
  $A$ must be red under $\chi$ and a red clique of the pair colouring
  $\mu(t_0,t_1;\cdot,\cdot)$ on lower-block pairs, and $B$ likewise for
  upper-block pairs, independently. An increment $C$ then needs, for every
  $t_0<t_1$, the two largest such sets to have total size at most $n+C-1$,
  which neither natural rule provides.

No mixed rule controlling both configurations is supplied here. A rule
depending only on blocks and on the pair's positions, as in the second item, reduces the
question to a property of pair colourings attached to the seed, which the
inductive hypothesis (no monochromatic $n$-set) does not supply; the class of
admitted systems would have to carry it as an extra invariant and reproduce
it after squaring.
