---
name: research/erdos_774/evidence/tensor_boundary
title: Exact boundary certificate for the 3-by-4-by-3 tensor
desc: A checked twelve-coloring certificate shows the boundary tensor S_3 x S_4 x S_3 has no universal three-color anchor, before or after exact scalar encoding.
tags: [E0774, computational, proved, tensor]
sources: []
created: 2026-09-24T23:30:00Z
updated: 2026-09-24T23:30:00Z
---

# Exact boundary certificate for the 3-by-4-by-3 tensor

[[research/erdos_774/evidence/_index|..]]

***

## Purpose and conclusion

This certificate supplies the boundary case of the
[root-coverage recurrence](../../routes/tensor_holes.md): for the base
$S_3\otimes S_4$ with one further factor $S_3$, the universal signed-span
set of three colors is $U_3=\{0\}$, and the same holds after every exact
ternary-relation-preserving linear encoding. The mathematical argument
that turns the checked facts into that conclusion, a disjointness-connected
hyperplane argument, is on the route page; the same argument is used by the
[Grow boundary certificate](../boundary_anchor/_index.md).

## What is checked

Run, from the repository root,

```sh
uv run --no-sync python wiki/research/erdos_774/evidence/tensor_boundary/main.py
```

The [checker](main.py) uses the standard library and the shared root
`tools` checker, performs no search, and finishes in under a second. Its
named checks are:

- the fixed three-layer coloring of the twelve base columns of
  $S_3\otimes S_4$ has, for each of its three colors, four columns per
  $S_3$ layer with 81 distinct signed sums, and successive signed-span
  intersection sizes $81,7,1$, $81,7,1$ and $81,17,1$, so each color is
  dissociated;
- the three tensor color classes have twelve columns each, and the third
  lies in the rational hyperplane with normal
  $(0,0,0,0,0,0,0,0,1,-1,-1,1)$;
- for each of twelve automorphic colorings, given by a permutation of each
  factor and a color relabeling, the image of one specified color class is
  disjoint from a specified class of the original coloring, and the image
  of the third class lies in the transported hyperplane;
- the twelve transported hyperplane normals have rational rank twelve.

Nine base layers with $3^4=81$ signed sums each are enumerated; no
enumeration of $3^{36}$ tensor coefficients is used. A failed clause exits
nonzero.

## Discovery of the certificate

The certificate was found by bounded exact enumeration, which is not part
of the normal run. For $S_3\otimes S_4$, all $6^4=1296$ column-permutation
colorings were enumerated, retaining 216 whose colorwise row counts permute
$(2,1,1)$; their 36 four-point classes were checked by 81 ternary sums each.
With seed 3774 and a cap of 50,000 triples, the first triple, indices
$[96,70,44]$, gave the proper boundary coloring, with exact ranks
$12,12,11$. A contemplated $3^{12}$ enumeration was not performed. All 864
coordinate automorphisms were checked for disjoint-class connectivity and
normal rank; a refinement to neighbors of the original coloring stopped
after 332 permutations, including 43 qualifying neighbors, and produced
the twelve-coloring certificate. A weighted-span diagnostic with the
pattern $(123),(231),(312),(123)$, all 144 automorphisms, three classes,
and 81 sums per class (34,992 occurrences) found, among 1,134 nonzero
vectors, a largest membership count of 144, attained by the 24 signed
roots, with all other counts at most 84; this was not used to claim a
general weighted separation theorem.
