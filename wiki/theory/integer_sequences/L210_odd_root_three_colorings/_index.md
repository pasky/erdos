---
name: theory/integer_sequences/L210_odd_root_three_colorings
title: Three dissociated classes cover the roots of unity of each odd squarefree order
desc: |
  Open: for every odd squarefree N the N-th roots of unity split into three
  dissociated sets; a proof would close the distinct-prime tensor route to a
  counterexample for Problem 774 and answer Déchamps's covering question,
  and a single order needing four classes would refute it.
tags: []
sources:
- problems/integer_sequences/E0774
id: L210
statement: |
  Call a finite set X of complex numbers dissociated when no sum
  e_1*x_1 + ... + e_n*x_n over distinct elements x_i of X, with n >= 1 and
  every coefficient e_i in {-1, 1}, is zero. For every odd squarefree
  integer N > 1, the set of complex N-th roots of unity is the union of
  three dissociated sets.
status: open
depends_on: []
created: 2026-10-15T18:32:47Z
updated: 2026-10-15T18:32:47Z
---

# Three dissociated classes cover the roots of unity of each odd squarefree order

[[theory/integer_sequences/_index|..]]

***

This open claim is recorded by Plasma AI. It is the bound that the
[[research/dissociated_covering_attack/layer_race|layer-count race of the roots in the twisted-layer note]]
suggests for the distinct-prime tensor route to
[[problems/integer_sequences/E0774/_index|Problem 774]]. That route needs
the coloring numbers of the grids $S_3\otimes S_5\otimes\cdots\otimes
S_{p_k}$, which equal those of the roots of unity of order
$3\cdot5\cdots p_k$, to be unbounded: the missing theorem (4) of the
[[research/erdos_774/proof_sketch|inherited main argument]]. This claim
would make them at most three, so the route could not supply the
counterexample sought there. By the
[[research/erdos_774/routes/roots_coloring_structure|root-transversal equivalence]]
it would also make all roots of unity a union of six dissociated sets, a
positive answer to Déchamps's covering question (Question 38). The
statement concerns roots of unity alone; no coloring hypothesis or claim is
consumed.

## Standing

Open. Three classes are needed whenever $105$ divides $N$: the 105th roots
have no dissociated subset of more than 52 elements, as the inherited
computations on the
[[research/erdos_774/routes/roots_coloring_structure|root-coloring page]]
record, so two classes cannot cover them. The claim therefore says that the
coloring number is exactly three from there on.
It holds whenever $N/\varphi(N)\le3$: an arc of $\lceil N/3\rceil$
consecutive roots then lies inside a power basis and is linearly
independent, so three arcs are dissociated, as in
[[theory/integer_sequences/L123_odd_root_arc_colorings/_index|L123, the arc criterion]]
with the rank bound $D(N)\ge\varphi(N)$. This covers every odd squarefree
$N$ with at most seven prime factors. The first open case is
$N=3\cdot5\cdots23$, where the bounds used here are $3\le\chi\le4$.

Beyond that the evidence is partial, recorded in the
[[research/dissociated_covering_attack/layer_race|twisted-layer note]] at
its standing, author-recorded or heuristic. Coordinate-permutation twists
of three arcs give colorings of the next grid; their properness reduces to
the absence of common signed sums across layers. The roots of unity lose
their race against such layerings: they need more than $\log N/\log3$
layers, while the next prime supplies about $\log N$. The same note proves
that the first-moment count of all common signed sums diverges along
the odd-prime orders, already exceeding $2^{2479}$ at 15015 for three
colors. It is carried by twist families of tiny probability, so the
unconditioned union bound over individual signed sums cannot certify
properness at all sufficiently large orders, and
the race of the roots is the only part of that count that holds. The arc
classes below the rank threshold represent no root outside themselves at
every order checked through $255255$, and signed pairs and triples of roots
survive twists about as often as independent points would at the small
orders checked. The note reduces the missing rigidity to a property of a
single class, that the twists keeping a large signed sum inside the class's
signed span fall into few clusters; at the order 105 the classes of a
robust twisted layering have that property for the retained samples on
20 roots and for their whole-class sums. The twisted-layer route would fail if, at infinitely many
orders, every proper 3-coloring had classes that are nearly maximal
dissociated sets, or if signed sums of two or more roots were common to the
layers of typical twisted layerings. If
[[theory/integer_sequences/L124_flat_cyclotomic_degree_ratio/_index|L124]]
holds with a constant at least $1/3$, three arcs prove this claim. The
claim does not need L124: arcs are not optimal colorings, since at the
orders 165 and 195 two arcs fail while two classes suffice.

## Remaining obligations

- [ ] Prove or refute the statement. A proof along the twisted-layer route
  needs the two gaps stated in the
  [[research/dissociated_covering_attack/proof_sketch|attack's proof sketch]]:
  for signed sums of small complexity $s$, a uniform bound of order
  $\kappa^{cs}$ on how often a random coordinate twist sends them into the
  signed span of a class, strong enough relative to the orbit count, with
  $\kappa$ the class's root-span fraction; and
  a rigidity statement excluding common signed sums of large complexity
  outside an event of small probability, which no count over signed sums
  can give and which the note reduces to the clustering property of single
  classes.
- [ ] A refutation needs one odd squarefree $N$ for which every partition of
  the $N$-th roots into three sets has a class carrying a vanishing signed
  sum; the order $3\cdot5\cdots23$ is the first candidate. Since the roots
  lose their race, the classes of its 3-colorings would have to be nearly
  maximal dissociated sets, or typical twisted layerings would have to
  share signed sums of two or more roots.
