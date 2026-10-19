---
name: research/sharp_dissociated_subset/evidence
title: Evidence
desc: Exact checks of odd-progression dissociation numbers, limits of fixed-pivot and freely centered certificates, and explicit certificates separating these models, run by one entry point.
tags: []
sources: []
created: 2026-10-15T18:14:21Z
updated: 2026-10-15T18:14:21Z
---

# Evidence

[[research/sharp_dissociated_subset/_index|..]]

***

The [entry point](main.py) checks in exact integer arithmetic the finite
facts stated in
[[research/sharp_dissociated_subset/pivot_certificates|the certificate note]]:

- the odd progressions $O_k=\{1,3,\ldots,2^{k+1}-1\}$ have dissociation
  numbers $2,3,5,6,7$ for $k=1,\ldots,5$, each with a retained witness and
  an exhaustive search for a larger dissociated subset;
- the set $\{1,3,5,7,13\}$ has dissociation number $4$, its largest
  graded-pivot certificate has $2$ companions, and the dependent set
  $\{13;7,1,5\}$ meets the lemma's strict budget with equality;
- the set $\{3,14,17,24,41,43,58,107,289\}$ has dissociation number $7$
  and largest graded-pivot certificate $2$, while the lattice form with
  modulus $107$ certifies its dissociated subset $\{3,14,24,107,289\}$;
- a set of $32$ positive integers with largest element below twice the
  smallest has largest dominant-pivot certificate $4$, below
  $\lfloor\log_232\rfloor=5$, while a retained graded certificate has $8$
  companions and a retained $6$-element subset is dissociated;
- a set of $9$ odd integers with largest element below twice the smallest
  has dissociation number $8$ and largest graded-pivot certificate $3$;
- in a set of $8$ integers every pivot with at least three levels pays
  more than the diameter for its three cheapest levels.
- three explicit certificates using free centers, which the original
  graded predicate rejects, together with a dependent negative control;
- a set of $32$ positive integers whose minimum total centered cost over
  all five-companion stars is $512668211$, exceeding its diameter
  $512000052$, although the minimizing six-point star is dissociated;
- a set of $65$ odd integers of ratio below two whose seven-companion
  stars all fail even the freely centered budget with multiplier two,
  with minimum defect $892$, together with an eight-element dissociated
  subset, a seven-element graded certificate, and a passing comparison.

The small graded-certificate searches enumerate every pivot, every set
of levels and every choice of companions. The dominant-pivot and
centered-budget checks instead minimize the exact cost independently
at each difference level. Centers among the ambient elements suffice:
the objective for a fixed selected set is piecewise linear with a
minimum at one of its elements. The program uses
the standard library and the shared failure harness, reads no input files
and writes no output. It runs in a few seconds from the repository
root:

```sh
uv run --no-sync python wiki/research/sharp_dissociated_subset/evidence/main.py
```

These checks concern the listed finite sets only. They support the
corrected orientation and the recorded limits of single-pivot certificates
in the [proof sketch](../proof_sketch.md), and prove nothing about
Problem 963 in general.

The split-tree instance is also part of
[[theory/number_theory/L270_recentered_pivot_obstruction/_index|L270, the obstruction to the stronger odd certificate at every fixed ratio above one]].
Its proof gives the general construction and the finite instance's
exact minimum symbolically. The checks here do not establish the
universal quantifier over ratios.
