---
name: research/erdos_1145
title: Balanced additive complements
desc: "Restrictions and construction attempts for balanced additive complements; existence remains open."
tags: []
sources: []
created: 2026-09-22T18:09:09Z
updated: 2026-10-19T04:19:07Z
---

# Balanced additive complements

[[research/_index|..]]

[[research/erdos_1145/collision_density|collision_density]]: Finite-bin difference counting forces a quantitative collision density.

[[research/erdos_1145/counting_regularity|counting_regularity]]: Elementary consequences of termwise balance and bounded cross representations.

[[research/erdos_1145/monotone_path_shells|monotone_path_shells]]: Flexible path shells give balanced cofinite complements and uniform bounds for every block pair, but only a logarithmic bound for the full unions.

[[research/erdos_1145/nonconstant_representations|nonconstant_representations]]: Every bounded representation function of a balanced pair differs from each nonzero periodic pattern on a set of positive lower density.

[[research/erdos_1145/prefix_resonance|prefix_resonance]]: An arbitrary large path can be matched by admissible smaller paths so
that one target has logarithmically many distinct representations.
The all-prefix estimate needs coordination across scales; the local
increment restrictions and pairwise bounds do not supply it.

***

This folder's notes that cite no source are author-recorded research, not
claims.

The linked notes are retained here; the notes for the routes
named without links are not part of this repository, so their results are
recorded here without proofs.

## Where things stand

**Unresolved.** No complete proof or counterexample to Problem 1145 is
established. The target is [[problems/additive_bases/E1145/_index|Problem 1145]],
whose Current assessment records the status search this folder
attacks. A positive answer includes the diagonal Erdős–Turán problem. No
retained construction has both proved cofinite coverage and a uniform full
representation bound. Every theorem in this folder is author-recorded; none
has an independent verification record.

### Necessary conditions on a counterexample

A hypothetical bounded counterexample has
$A(x),B(x)=\Theta(\sqrt x)$, $A(x)-B(x)=o(\sqrt x)$, and
square-root local continuity ([counting regularity](counting_regularity.md)).
Repeated sums have positive lower density
([collision density](collision_density.md)), and the representation
function differs from every fixed nonzero periodic pattern on a set of
positive lower density
([nonconstant representations](nonconstant_representations.md)).
These restrictions do not exclude a bounded, persistently varying function.

- **Both unphased parity-cover routes are excluded.**
  Initial births
  force logarithmically growing allocation discrepancy.
  Terminal births
  also exclude a full forward odd list: its endpoint $t_{2q}-1$
  accumulates in one residue class of later prefixes. Even alternating
  the full forward parity cannot avoid the fixed residue-capacity bound.
  The unphased asymmetric-cover route assumed that a full odd-row list
  stays available; the terminal-birth residue-capacity bound shows that it
  cannot.
- **Two generic integer-code repairs fail under explicit hypotheses.**
  For integer-carry encodings, an injective
  $(\mathbb Z/p\mathbb Z)^d$-encoding with $K$ ambient additive defects
  satisfies $p^d\le\binom{K+p-2}{p-1}$; a fixed list of global carry
  offsets is impossible for fixed $p$ as $d\to\infty$.
  Carry-free radix padding instead loses square-root lower density.
  These restrictions do not exclude selected-pair or branch-dependent
  corrections. The tested
  polynomial encodings already fail
  through imbalance, gaps, or same-shell carry collisions.
- **Zero microscopic variance has strong, but still conditional, consequences.**
  Marked-fiber localization forces a purely
  singular common measure, integer conditional sum and difference fibers,
  and even limiting sum multiplicities. It excludes the deterministic
  relational pattern, not all equality-case
  measures. The
  topological check
  concerns unique geometric sums only: conditional counts do not provide
  the needed bound on every support representation.

### Useful approaches and their exact gaps

[Nonlinear path shells](monotone_path_shells.md) have termwise balance,
cofinite coverage, and $r(n)=O(\log n)$. The missing condition is a
uniform convolution bound against the **entire** opposite old prefix.
The [exact-resonance construction](prefix_resonance.md), recorded in
[[theory/additive_bases/L126_path_shell_resonance/_index|L126 at tier 0]],
shows that admissible paths can realize logarithmic peaks, even with the
large path prescribed. Thus local increment restrictions alone cannot
provide that uniform estimate; coordinated choices remain open.
The stated affine, shared-prefix, and independent-path subclasses are
excluded; arbitrary coordinated nonlinear paths are not. The
scale-gap formulation
states a sufficient bounded-overlap invariant, but its geometric size
budget is not a Cartesian construction or a carry-correct decoder.

Residue routing and
controlled parity allocation preserve
balance, residue margins, and uniform bounds for individual shell pairs.
Ordered-routing lemmas give conditional cyclic
coverage from full row-class lists or constant allocation discrepancy;
neither premise can persist for unphased forward parity sorting. Moving
rank phases, or a four-class rule with an interior forward class full,
evade the stated endpoint obstructions. No compatible indefinite
allocation, ordinary covering lift, or whole-prefix bound is known.
Fractional routing does bound whole-prefix
convolutions, but constant-loss integral rounding and a covering invariant
are missing.

Cyclic-prefix covers and
clone extensions have finite witnesses and specific
dead ends, not an infinite extension theorem. Any retained-prefix example
needs persistent branching irregularity;
eventually subcritical child products are excluded by a supermartingale
argument. The randomized relational relaxation still lacks consistent
shared-vertex choices.

Finite-field blocks solve local covering
problems, not infinite gluing. The specified
partial-mirror offsets are excluded, but
arbitrary length-dependent offsets remain outside that proof; no
carry-correct scale-tag decoder has been established.
The existing energy and
row-profile relaxations remain feasible at fixed
bounds. No argument forces their microscopic variance to vanish.

**Provisional directions:** phased or interior-class routing still needs
an actual extension theorem. Scale-gap coding would have to realize the
bounded-overlap invariant with exact integer carries while retaining
coverage and balance. Neither is established as a feasible route.
