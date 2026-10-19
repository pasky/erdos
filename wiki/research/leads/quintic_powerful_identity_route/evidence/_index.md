---
name: research/leads/quintic_powerful_identity_route/evidence
title: Evidence
desc: |
  Two exploratory scripts searching numerically for four-term identities of
  fifth powers of binary forms; no entry point, no checks, and no evidence
  for any claim.
tags: []
sources: []
created: 2026-09-28T08:31:48Z
updated: 2026-09-28T08:31:48Z
---

# Evidence

[[research/leads/quintic_powerful_identity_route/_index|..]]

***

The retained scripts
[`quintic_identity_search.py`](util/quintic_identity_search.py) and
[`trace_search.py`](util/trace_search.py) are exploratory computations, not
evidence for any claim: the first searches by Levenberg–Marquardt from random
starts for identities $Q_1^5+Q_2^5+Q_3^5+Q_4^5=0$ among binary forms of one
degree over $\mathbb C$ or $\mathbb R$, and the second searches the cyclic
shape $\sum_{k=0}^{2}(Q\circ M^k)^5=I^5$ that [the lead](../_index.md)
describes. There is no entry point and nothing is checked, so a run certifies
nothing. Both need `numpy`, which the repository environment does not hold,
so run them from the repository root with it added for the run:

```sh
uv run --no-sync --with numpy python wiki/research/leads/quintic_powerful_identity_route/evidence/util/quintic_identity_search.py complex 2 2000
uv run --no-sync --with numpy python wiki/research/leads/quintic_powerful_identity_route/evidence/util/trace_search.py complex 2 300
```

The arguments are the field, the degree and the number of starts, with an
optional seed after them.
