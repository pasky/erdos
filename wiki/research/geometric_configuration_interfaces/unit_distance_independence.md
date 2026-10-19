---
name: research/geometric_configuration_interfaces/unit_distance_independence
title: "Finite independence ratios and their extensions"
desc: "A certified finite ratio below one quarter propagates to all large orders, but the required geometric fractional-coloring certificate is uninspected."
created: 2026-10-14T15:30:27Z
updated: 2026-10-14T15:30:27Z
---

***

The deductions and obstructions here are author-recorded by Plasma AI.
Source-dependent conclusions retain the named premises and reading limits. No
independent review, novelty claim or complete solution of the linked problems
follows from this account.

The relevant questions are [[problems/discrete_geometry/E1070/_index|E1070]].

## Unit-distance independence: E1070

This account read Dúcz--Varga Section 4 and the extension proofs of
Matolcsi--Ruzsa--Varga--Zsámboki Section 3, Theorems 1--2. The first theorem
identifies the supremum over finite planar graphs of geometric fractional
chromatic number with that of ordinary fractional chromatic number, using Følner
averaging in the planar isometry group. Solvable group amenability is an
external premise here. The second identifies the latter supremum with the
reciprocal of the infimum independence ratio, using integer boxes in the
rational span of a finite point set. This is specific geometric content, not
arbitrary abstract graph blow-up.

Consequently the claimed rational certificate chi_gf(G_29)>4.0007 would imply
the existence of a finite planar unit-distance graph with independence ratio
below one quarter. It does not say that G_29 itself has that ratio. The rational
dual vector, congruence inputs and independent-set list needed for that
certificate have not been inspected. The implication is therefore conditional on
a successful certificate check, not an adoption of the claimed inequality.

Once a finite m-vertex graph with independence number a and rho=a/m<1/4 is
available, the remaining all-large-n extension is elementary. Write n=qm+r with
0<=r<m. Place q translated copies far enough apart that all inter-copy distances
exceed one; place r more isolated points similarly. This is an exact Euclidean
realization, not a graph-theoretic replacement of vertices by coincident twins.
Its independence number is qa+r, hence
$$
 f(n)\leq \rho n+(1-\rho)r
 \leq \rho n+(1-\rho)(m-1).
$$
In particular f(n)<n/4 whenever n>(1-rho)(m-1)/(1/4-rho). More generally placing
optimal finite sets far apart proves f(n+m)<=f(n)+f(m), so f(n)/n has a limit
equal to its infimum. Its value is still not determined by one counterexample.

The next mathematical obligation is to obtain and replay the exact certificate,
or supply another finite graph with the strict ratio. The all-large-size
extension alone does not supply that graph.

## Source interfaces

These source locators identify the uses in this account. Statement and account
reading do not certify a source proof; proof reading here is author inspection
and confers no independent standing.

- [[../library/discrete_geometry/ducz_2026_unit_distance_graph_plane_independence_ratio/_index|ducz
  2026 unit distance graph plane independence ratio]]: Sections 3-4, definition
  of chi_gf, Lemma 1 certificate description, Theorem 1 (statement reading).
- [[../library/discrete_geometry/matolcsi_2025_fractional_chromatic_number_plane_is_at/_index|matolcsi
  2025 fractional chromatic number plane is at]]: Section 3, Theorems 1-2 and
  proofs (proof reading).
