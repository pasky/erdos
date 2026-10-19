---
name: research/schur_number_growth/evidence
title: Exact checks for the Schur-growth notes
desc: Exact finite checks of sparse Bohr cells, a sixteen-vertex avoidance obstruction, the block composition and a short-prefix witness with rational Bohr frequencies, arc rescaling, signed-cube maps and small colorings, and a twisted-block palette witness.
created: 2026-10-15T23:02:04Z
updated: 2026-10-17T22:11:11Z
---

# Exact checks for the Schur-growth notes

[[research/schur_number_growth/_index|..]]

***

From the repository root run:

```sh
uv run --no-sync python wiki/research/schur_number_growth/evidence/main.py
```

The program uses exact integer and rational arithmetic and checks, for the
refutation of [[theory/ramsey_theory/L261_difference_domain_thinning/_index|L261]],
that every relation among the differences of $\{4^0,\ldots,4^{n-1}\}$ is
an endpoint triangle for $n\le8$; for the refutation of
[[theory/ramsey_theory/L266_bohr_cell_uniform_avoidance/_index|L266]],
that the digit and digit-sum constraints select exactly the powers of $b$
for $1\le n\le5$, $q\in\{3,4,8\}$ and $b=\max(4,n+2,q+1)$, by examining
every integer in $[0,b^n-1]$ (at most 59049 candidates per case); and that
the three-coloring of $K_{16}$ by the cubic-residue classes of
$\mathrm{GF}(16)$ has no monochromatic triangle and every six-vertex
subset has every color. Its transfer to differences of sixteen powers of
18 has 120 differences and 560 Schur triples, none monochromatic. The
three-box argument of L266 makes this a counterexample at $\rho=1/3$;
the huge ambient interval is handled by the written cell and extension
proofs, not enumerated. For the
refutation of [[theory/ramsey_theory/L260_dilated_prefix_color_omission/_index|L260]],
that the block composition is Schur-free with both palettes for every pair
of tripling colorings with at most four colors and for the retained Bohr
coloring, and that one composite of $[1,63239]$ has a longest
color-omitting dilated prefix below the bound of Lemma C; for the
proof of [[theory/ramsey_theory/L262_sum_free_arc_colorings/_index|L262]],
the multiplier of its Lemma 2 on every sum-free arc with endpoints in
$\tfrac1{120}\mathbb Z$, and the sum-free arcs of the tripling colorings
for $k\le7$; and for the
[[research/schur_number_growth/signed_cube_reduction|signed-cube reduction]],
the base-$b$ embedding for $r\le5$, the digit-cube cells for $r\le4$, the
binary-value and support maps for $r\le6$, that $Q_3^+$ has no Schur-free
two-coloring, and the colorings behind $\chi_4\le3$, $\chi_5\le4$,
$\chi_6\le5$ and $\chi_7\le5$; and for the
[[research/schur_number_growth/invariant_palette_rule|palette-rule page]],
that a retained four-coloring of $Q_4^+$ is Schur-free and, with the four
twisted blocks $\{(x_1,x_2,y_1,y_2):x_1+y_1=s_1,\ x_2+y_2=s_2\}$ (sums
mod $2$) and its retained palettes, obeys rule (R), while one block uses
all four colors on its internal pairs and the sum of $2^{|U_B|}$ over the
blocks is $28>2^4$; that coloring is a function neither of the support
nor of the binary value. Controls confirm that the Schur test counts equal
summands, that the prefix statistic sees the late color of a tripling
coloring, and that the rule-(R) test rejects a palette containing an
internal color.

Three inputs are retained. [bohr_psi_m20.json](assets/bohr_psi_m20.json) is
a 20-color coloring of $[1,800]$ whose classes lie in Bohr sets
$\{x:\{\theta_ix\}\in(1/3,2/3)\}$, found by `produce.py bohr 20 800 4`
(seed 4) as in the construction of Lemma B of the refutation of L260.
The twenty frequencies are retained as exact numerator-denominator pairs,
and the checker verifies each element's arc membership using integers.
The discovery sampler uses floating arithmetic, but the retained witness
and its verification do not rely on rounding.
[schur_44.json](assets/schur_44.json) is a coloring of $[1,44]$ by four
colors with no monochromatic $x+y=z$, found by the depth-first search
`produce.py schur 44 4`; composed by Lemma A with one color on $[1,1]$, it
gives the five-coloring of $[1,133]$ behind $\chi_7\le5$. The checker
verifies both inputs exactly and does not rely on either search; rerunning
`produce.py` reproduces both files byte for byte.
[twisted_cube_r4.json](assets/twisted_cube_r4.json) holds the coloring of
the forty vectors of $Q_4^+$ and the four palettes. It was found by a SAT
search (kissat) over colorings and palettes with the twisted blocks fixed,
block $(0,0)$ required to use every color inside and each other block
allowed at most two colors missing from its interior. That search is not
retained; the checker verifies the witness directly.

The largest interval coloring checked has length 63239; the largest
signed cube checked has dimension seven. The program uses the repository's
Python environment, including NumPy, on one thread and below 1 GiB.
Expected runtime is a few seconds. The checks illustrate proved lemmas or
verify finite witnesses, and prove no asymptotic statement. There is no
independent review. The program exits nonzero on any failed check, also
under optimized Python.
