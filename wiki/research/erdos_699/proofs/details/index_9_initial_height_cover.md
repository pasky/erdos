---
name: research/erdos_699/proofs/details/index_9_initial_height_cover
title: "Erdős 699: all initial index-nine sources at the polynomial height"
desc: "Complete boxed Padé interval chains establish all eleven initial pair sources and four ordinary AP sources from h=10^241547627."
created: 2026-09-22T00:00:00Z
updated: 2026-10-14T00:26:52Z
---

# Erdős 699: all initial index-nine sources at the polynomial height

[[research/erdos_699/_index|P699 research]] ·
[[research/erdos_699/methods/details/pade_block_adjustment|Choosing the Padé index]] ·
[[research/erdos_699/archive/previous_bounds/index_9_numerical_tail|The earlier numerical stopping bound]]

***

All eleven pair sources and four ordinary arithmetic-progression sources
in the relaxed index-nine proof hold for

$$
h=n-8\ge10^{241547627}.\tag{1}
$$

The [checker](../../computations/erdos_699_index_9_initial_height_cover.py)
and [complete interval chains](../../computations/erdos_699_index_9_initial_height_cover.json.gz)
establish these fifteen target-box exclusions. The pair sources imply
the nineteen weakened baseline alternatives. This addresses the initial
sources; the 790 further joint clauses and the whole-index coverage are
separate ingredients.

**Complete result.** The [combined proof](index_9_complete.md)
excludes every admissible bad triple at nine. The estimates below
are retained as components of that proof.

## Fixed-index inequalities

The argument uses the
[boxed sparse-witness lemma](index_7_initial_height_cover.md).
Under upper bounds $u_p\le h^{e_p}$, the cost of clearing residual
denominators at a fixed integer Padé index $m$ is at most

$$D(x)=\sum_p\bigl(L_{s(p)}a_p\log(p)\,m
                         -b_p(1-e_p)x\bigr)_+,
\qquad x=\log h.$$

Each logarithmic coefficient is rounded upwards. The first term of the
integer estimate decreases with $x$. The second term is the maximum of
affine functions indexed by all subsets of the prime components. Exact
rational endpoint inequalities therefore prove the estimate throughout
an interval of real logarithmic heights.

Every source starts at the integer 556183965, strictly below
$241547627\log10$. Accepted intervals have adjoining endpoints and
continue beyond the source's previously established numerical tail.
The symmetric $(3,7)$ pair already has a smaller tail threshold and
needs no additional interval.

## The arithmetic-progression families

For the ordinary AP sources, the sparse argument uses newly specified
off-diagonal families. If the old seed record is $(P,Q,a,b,c,d)$, the
directions are $(d,c-d,d)$, with adjacent rectangles

$$\bigl(dm,(c-d)m-1,dm\bigr),\qquad
\bigl(dm+1,(c-d)m-2,dm+1\bigr).$$

The [source preparation](../../computations/erdos_699_index_9_boxed_sources.py)
verifies their polynomial constants independently. The old AP
coefficient-gcd bounds are not transferred to these new rectangles:
each sparse witness receives its own pointwise bound. Both methods
exclude the same target box, so the existing AP tail remains applicable.

| Seed | Directions | Sparse witnesses |
| --- | --- | ---: |
| $16-15=1$ | $(8,3,8)$ | 348 |
| $81-80=1$ | $(4,1,4)$ | 411 |
| $25-24=1$ | $(3,1,3)$ | 408 |
| $245-243=2$ | $(39,8,39)$ | 2852 |

The pair gap is at most eight. Each AP has position step of absolute
value at most four, so its product gap is at most sixteen. All factors
lie in $[h,h+8]$.

## Retained certificate

The fifteen sources use twelve distinct direction triples. The complete
certificate contains 299324 interval witnesses. Each records the Padé
index, right logarithmic endpoint, coefficient-gcd lower bound on the
$2^{-32}$ grid, and number of BFT intervals used. The source identities,
targets, arithmetic hypotheses, and numerical tail bounds are retained
with them.

The calculation reuses the read-only prime-log prefix through $10^9$
and proper prime powers through $10^{14}$. Every accepted witness was
checked during construction. The serialized-chain verifier also checks
every interval inequality and endpoint, all prepared constants, and
the presence of every named input. No interpolation rank or binomial row
was recomputed.

Run the serialized-chain checks with:

```sh
.venv/bin/python wiki/research/erdos_699/computations/erdos_699_index_9_initial_height_cover.py
```

The optional `--replay-gcd` flag independently recomputes every
pointwise coefficient-gcd bound using the shared prime cache. A combined
proof wrapper can call `check(data, replay_gcd=False)`; the default
performs all source-binding and rational interval checks.
