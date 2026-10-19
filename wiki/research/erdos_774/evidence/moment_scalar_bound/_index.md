---
name: research/erdos_774/evidence/moment_scalar_bound
title: A candidate scalar determinant bound on ten moment-lattice pairs
desc: An exact scan of 16,694 degree patterns on ten pairs finds no violation of a candidate scalar lower bound for moment-lattice covolumes; the expression is a diagnostic, not a theorem.
tags: [E0774, computational, Boolean-moments, finite]
sources: []
created: 2026-09-24T23:30:00Z
updated: 2026-09-24T23:30:00Z
---

# A candidate scalar determinant bound on ten moment-lattice pairs

[[research/erdos_774/evidence/_index|..]]

***

## The tested expression

A candidate closed-form lower bound for the normalized covolume of the
sublattices spanned by a degree pattern was tested on exactly ten
prescribed pairs $(d,\ell)$ and all nonempty degree unions. For
$A\subseteq\{0,\ldots,\ell\}$, set $h_j=\binom dj-\binom d{j-1}$,
$A_j=A\cap[j,d-j]$, $N_j=|A_j|$, and

$$
\nu_j=\sum_{s<t\in A_j}v_2(t-s)
      -\sum_{a=0}^{N_j-1}\sum_{b=1}^a v_2(b).
$$

The computed expression was

$$
\frac{\sum_jh_j[(d/2-j)N_j-N_j(N_j-1)/2-\nu_j]}
     {\sum_jh_jN_j}.
$$

This expression is not used as a theorem; its proposed ballot-basis proof
is unnecessary for the independent
[compression argument](../../lemmas/moment_lattice_stability.md), which
supersedes the diagnostic.

| $d,\ell$ | Patterns | Minimum expression $=$ full normalized covolume |
|---|---:|---:|
| 8,5 | 63 | 28/73 |
| 8,6 | 127 | 28/247 |
| 10,6 | 127 | 105/212 |
| 10,7 | 255 | 45/242 |
| 12,7 | 255 | 990/1651 |
| 12,8 | 511 | 990/3797 |
| 16,9 | 1023 | 40040/50643 |
| 16,10 | 2047 | 24024/58651 |
| 20,11 | 4095 | 125970/130771 |
| 20,12 | 8191 | 41990/75883 |

There are 16,694 patterns in total and zero violations of the tested
comparison. Full prefixes attain each displayed minimum; uniqueness of the
minimizer was not tested or asserted. The diagnostic ends at its finite
bound.

## What is checked

Run, from the repository root,

```sh
uv run --no-sync python wiki/research/erdos_774/evidence/moment_scalar_bound/main.py
```

The [checker](main.py) rescans every pattern of every pair with exact
rational arithmetic in the standard library and the shared root `tools`
checker; it performs no search and finishes in a few seconds. Its named
checks are that no pattern falls below the full normalized covolume
$(d-\ell)\binom d\ell/(2\sum_{s\le\ell}\binom ds)$, that the full prefix
attains the recorded minimum for each pair, and that 16,694 patterns are
scanned. A failed clause exits nonzero.
