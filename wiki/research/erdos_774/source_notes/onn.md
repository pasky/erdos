---
name: research/erdos_774/source_notes/onn
title: "Onn: convex discrete optimization"
desc: "Source notes for Problem 774: Onn: convex discrete optimization."
tags: []
sources: []
created: 2026-09-24T22:18:19Z
updated: 2026-10-13T04:56:43Z
---

# Onn: convex discrete optimization

***

[Library card](../../../../library/additive_combinatorics/onn_2007_convex_discrete_optimization/_index.md),
focusing on circuits, Graver bases, and augmentation.

Shmuel Onn, "Convex discrete optimization," in *Encyclopedia of
Optimization* (2009), 513--550.

Onn develops convex integer optimization through finite universal test sets,
especially Graver bases.  A Graver basis consists of conformally minimal
integer kernel vectors; every integer dependence can be decomposed into such
primitive sign-compatible moves (Lemma 4.2, p. 29).  Circuits are the
primitive integer kernel vectors of minimal support; every circuit lies in the
Graver basis, the two sets coincide when the matrix is totally unimodular, and
in general the Graver basis is much larger (p. 29).

For E0774 this language can organize the signed-relation hypergraph of an
integer encoding.  If all primitive kernel moves of a proposed block can be
classified and their coefficients controlled, dissociation becomes a finite
condition: since a conformal summand of a relation with coefficients in
$\{0,\pm1\}$ again has such coefficients, a subset is dissociated exactly
when it contains the support of no Graver element with entries in
$\{0,\pm1\}$.  Circuits alone do not suffice: for the block $\{1,2,3\}$ the
relation $1+2-3=0$ has such coefficients while no circuit does.  The chief
caveat is coefficient size: Graver elements and circuits need not lie in
$\{0,\pm1\}$, while E0774 ignores dependencies with larger coefficients.
