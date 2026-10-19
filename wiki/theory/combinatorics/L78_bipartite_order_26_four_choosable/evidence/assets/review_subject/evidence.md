[cut]

The [entry point](main.py) checks the finite arithmetic of the
[proof](../_proof.md). It reads the compact weighting in
[`assets/compact_certificate.json`](assets/compact_certificate.json) and
recomputes the six profile multiplicities and eight event-weight rows
displayed there by exact binomial counts. It separately computes the same
event weights over all $2^{17}$ subsets and all 2378 admissible four-subsets
by subset- and superset-sum transforms, without the profile formulas.
The resulting $Z=83424$, $\max\ell=4374$ and $\max r=2664$ give
$(a-2)\max\ell+(26-a)\max r\le82746<Z$ for every $2\le a\le13$.
Naming the smaller side left covers all side splits.

For every ordered split $(a,b)$ with $2\le a\le24$ and
$a+b=26$ it reads the integer weights of
[`assets/certificates.json`](assets/certificates.json), assigns each subset
$T$ of the 17-colour palette meeting $\{0,1,2,3\}$ and $\{4,5,6,7\}$ the
weight of its profile, computes the total weight $Z$ and, by subset- and
superset-sum transforms over all $2^{17}$ subsets, the largest left and
right event weights $\max\ell$ and $\max r$ over all four-subsets other
than the two fixed lists, and checks $(a-2)\max\ell+b\max r<Z$ in exact
integers. It also checks the file's declared domain and that every split
appears exactly once. The helper functions are in
[`util/certificate.py`](util/certificate.py).

The controls use the same functions. The two assignments in
[`assets/controls.json`](assets/controls.json), the $K_{2,4}$ assignment
with 2-lists and an assignment of 18 distinct 3-lists on nine colours found
by a local search, are re-checked bad by exhaustion. After relabelling two
disjoint left lists, every weighting concentrated on a single profile, and
the uniform weighting, gives them event weight at least $Z$, as an actual
bad assignment must. Deleting one right list of the second assignment
leaves a colourable assignment, whose colouring is exhibited and checked;
the uniform weighting does not certify the split $(13,13)$; and malformed
weights and list assignments are refused. A Python-integer bound on the
total weight is checked before conversion to the arrays' 64-bit integers,
so all transform sums are exact. Run from the repository root:

```sh
uv run --no-sync python wiki/theory/combinatorics/L78_bipartite_order_26_four_choosable/evidence/main.py
```

It needs numpy and the root `tools` package, reads only the three assets,
writes nothing, and takes a few seconds; every failed check exits nonzero,
including under `python -O`. The [discovery program](produce.py) solves the
linear program described in the proof for every split and writes the
rounded weights to the ignored `output/` folder; it needs scipy, and its
output is a proposal that the entry point does not read. The program checks
the weighted count only: the reduction to 17 colours, distinct lists and
two disjoint left lists is the argument of the proof.
