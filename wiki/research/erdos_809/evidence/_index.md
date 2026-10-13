---
name: research/erdos_809/evidence
desc: |
  Retained publication files of the Erdős 809 formalization: the Mathlib-only
  challenge statement, the solution module, the comparator configuration, the
  registry entry (PALOMAR-2026-09-30-000004) and the write-up, kept as assets
  beside the research folder.
tags: []
sources: []
created: 2026-09-25T01:21:28Z
updated: 2026-10-08T01:29:59Z
---

# research/erdos_809/evidence

[[research/erdos_809/_index|..]]

***

The folder `assets/publication/` retains the files the formalization's
standalone project publishes: `Challenge.lean`, the statement of the result
over Mathlib alone with a deliberate `sorry` in place of the proof;
`Solution.lean`, which supplies the same theorem from the proof development;
`comparator.json`, which names the compared theorem and the permitted axioms;
`formalization.yaml`, the registry entry (PALOMAR-2026-09-30-000004); the
project's README and lake files with their own Lean and Mathlib pins; and,
under `paper/`, the write-up of the seven-cycle proof with further bounds at
higher edge densities, `c7_threshold.tex` and its compiled `c7_threshold.pdf`,
under the project's Apache License 2.0 (`LICENSE`). They are retained bytes,
not pages, and are not built here: a `sorry` cannot live in the accepted Lean
closure, and the proof development itself is ported under
`lean/Erdos/Library/Problem809/` as the [formalization
account](../formalization.md) describes.

The files are those of the project's repository,
<https://github.com/plasma-ai/erdos-809>, at commit `f2ad237` of 8 October
2026, compared on 2026-10-13. The Lean, comparator, registry and lake files are
unchanged there since commit `ed2155f`, the one the port is of. The README is
the version at `f2ad237`, which since the port has gained the registry entry
and a link to the write-up. The write-up is current at commit `eb385a8` of 29
September 2026, the last commit touching either of its files. After `0f27743`,
the commit the registry entry pins, the repository's commits changed only the
write-up's author line, one broken citation in it and the README.

The README's "to our knowledge" novelty sentence reflects the project's search
of 24 September 2026 and is retained as written; Asad Shahab's independent proof
claim, a proof of the seven-cycle case with a Lean development whose headline
theorem covers every odd cycle $C_{2k+1}$ with $k\ge3$, was filed on the site
first (proof claim 358, before the project's 367, both on 27 September 2026;
preprint arXiv:2609.38286, 29 September 2026), and this corpus built that
development at its pinned commit and audited its statement on 2026-10-08, as
[[problems/ramsey_theory/E0809/_index|the problem page]] records.
