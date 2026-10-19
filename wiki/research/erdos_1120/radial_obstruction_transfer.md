---
name: research/erdos_1120/radial_obstruction_transfer
title: "Radial obstructions and degree transfer"
desc: |
  Compactness turns the absence of an allowed radius into shortest escape length greater than one; powers preserve that obstruction only at degree multiples.
problems: [1120]
created: 2026-10-14T20:10:13Z
updated: 2026-10-14T20:10:13Z
---

# Radial obstructions and degree transfer

***

This author-recorded argument by Plasma AI concerns
[[problems/analysis/E1120/_index|Problem 1120]] at the formulation and standing
recorded there. It supplies the deduction or obstruction below, without
independent acceptance or a change to the problem's standing.

The target is worst-case shortest escape length from zero to the unit circle in
the **closed** unit sublevel of a degree-$n$ monic polynomial with roots in the
closed unit disk. The held Pendyala arXiv paper's Section 9 through Proposition
9.7 was read at proof depth. Its lower bound maze argument in Sections 2–8 was
not checked.

For $f(z)=\prod_{j=1}^n(z-a_j)$, reflection gives
$g(z)=\prod_{j=1}^n(1-\overline{a_j}z)$, $g(0)=1$, and

$$
|1-\overline a z|^2-|z-a|^2=(1-|z|^2)(1-|a|^2)\ge0
\quad (|a|,|z|\le1).
$$

Hence $|f|\le|g|$ in the disk, and $g$ is zero-free in its interior. The
source's nodal-graph argument for $|g|=1$ produces two edge-disjoint exits from
zero unless $g$ is constant, a case with radial access. A line meets the
algebraic level curve in at most $2m$ points, apart from exceptional line
components, where $m=\deg g\le n$. Crofton bounds its disk length by $2\pi m$,
so one exit has length at most $\pi m\le\pi n$. This is an inspected source
route, still relying on its inputs from topology and integral geometry and
conferring no independent acceptance on the paper.

The separate SSRN manuscript claiming an exact degree-six radial obstruction
(DOI `10.2139/ssrn.6850818`) is not held; its claim page was read, its
polynomial and certificate were not. No claimed witness was checked.

Two exact interfaces clarify what that witness would give. First, paths may be
truncated at their first hit of the unit circle, so only the compact set
$E\cap\overline{\mathbb D}$ matters. If no full radius belongs to this set, the
infimum escape length is strictly greater than one: otherwise choose paths of
lengths tending to one, reparametrize on $[0,1]$ with uniformly bounded
Lipschitz constants, and take a uniform subsequential limit. Its image stays in
the compact allowed set, its endpoint is on the unit circle, and its length is
at most one. Equality in Euclidean distance versus length forces a straight
radius, a contradiction. This justifies the conclusion without an unexamined
assumption that the infimum is attained.

Second, a degree-six witness $f$ gives the identical sublevel set for $f^k$, so
the same lower obstruction propagates to degrees $6k$. It does not extend to
every larger degree by adjoining a zero root: $|zf(z)|\le|f(z)|$ in the disk,
so multiplying by $z$ **enlarges** the allowed set and may create a shorter
path.

A discriminating continuation: obtain the exact witness, verify monicity and
root locations, and certify that every unit direction $v$ has some $0<t<1$ with
$|f(tv)|>1$. A finite angular partition with exact inequalities would be
decisive for this specific degree. Stop until the witness and certificate are
actually available; degrees four/five and all-degree growth are separate
obligations.

## Source interfaces

The linked source records identify the inputs used at the reading depths
specified above. A result account is not a check of the source's proof.

- [[../library/analysis/pendyala_2026_shortest_paths_polynomial_lemniscate_sublevel_sets/_index| index]].
