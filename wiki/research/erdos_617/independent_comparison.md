---
name: research/erdos_617/independent_comparison
desc: Audits of four isolated inputs, including full-cap boundary sharpness, superseded claims, and precise limits of the arguments.
tags: [graph-theory, audit]
sources: []
created: 2026-09-22T04:18:35Z
updated: 2026-10-14T00:26:52Z
---


# research/erdos_617/independent_comparison

***

The [isolated input](independent/small_independence_and_packing_obstructions.md)
was treated as unverified, then compared with all topical notes linked by the
research index. Its assertions of prior checking were not accepted as evidence.
The checks below used the displayed arguments, independent reconstructions, and
the relevant primary-source passages. The original input is retained as an
archive, not as an alternative entry point into current progress.

**The full problem remains unresolved.** None of the verified
additions excludes the surviving least-budget minimal-ratio core
or the all-deficient two-supported core.

The later [quadratic completion](hereditary_span_bound.md) improves both
the span and equality thresholds to $r\ge64a^2$. The fourth-power
comparisons below describe the earlier audited state.

## Verified additions

The independent maximum-degree induction proves exactly the finite
partition theorem used in [Hereditary span](hereditary_span_bound.md).
It is written there, making that part of the existing proof
self-contained without changing its $64a^4$ threshold.

The nonpartite Turán gap in equation (6) is true, but its claimed
linked proof is absent from the input bundle. A complete
single-vertex-cloning proof was reconstructed and is in
[Packing tools](packing_tools.md). It agrees with the applicable
branch of Kang--Pikhurko Theorem 1, checked in the supplied full
source after reading its digest. The same note includes the stronger
matching-transversal classification: the failed system
on $k$ parts of size $k-1$ is $k-1$ disjoint transversal $K_k$'s,
not just a collection of pairwise perfect matchings.

The exact equality classification in Appendix E is valid for unequal
nonempty parts as well as equal ones. It is preserved with a full
proof and conditional clique-merging consequence in
[Transversal equality](transversal_equality.md). Neither this result
nor the present global stability bounds prove a near-equality
completion theorem. The statement that the relevant weights are
“near” one is not a quantified conclusion of those bounds.

Appendix C provides a useful complementary relaxation counterexample:
all hereditary caps and $\alpha=\omega=r$ can hold while the
least-color budget fails. Its proof was checked and extends from
primes to prime powers. The construction and exact excess
$r(r-1)(r-2)/2$ are recorded in
[Local-cap obstructions](local_cap_obstruction.md).

The affine edit-distance bounds in Section 5 also survive checking.
Their missing equality classification was reconstructed in full in
[Affine edit obstruction](affine_edit_obstruction.md). An extension
would need at least $2(r-1)^2$ old-edge recolorings, or
$(r-1)(2r-1)$ for $r\ge5$. These improve the requirement to alter every
singleton-direction class. They give
no reduction of arbitrary colorings to affine constructions.

## Valid arguments already matched or surpassed

Section 1 repeats [Reductions](reductions.md).
The two small-independence span claims in Section 2 follow from
the reconstructed gap, with excess

$$
\frac{-a^2+3a+2}{2}r-2a.
$$

They give $a=2$ for $r\ge3$ and $a=3$ for $r\ge7$ by an
elementary color-coupling argument, recorded in
[Cross-color cores](cross_color_cores.md). They do not improve that
note's existing localized-inequality exclusions. Nor do they
replace the exact-order structure in the
[two-row](two_row_structure.md) and
[three-row](three_row_structure.md) notes. The gap argument uses
clique restrictions in the other colors, not just one-color caps.

The quantitative proofs in Section 3 and Appendix A check, including
the extracted clique sizes, exceptional-vertex counts, the
dependency degree in the finite probability lemma, and the final
constants. Under full hereditary caps, both $r<256a^6$ and
$r<4096a^5$ are weaker than the existing $r<64a^4$ condition.
The sixth-power theorem nevertheless retains a distinct scope:
it uses only

$$
|H|=ar+1,\quad \alpha(H)\le a,\quad
e(H)\le D_r(ar+1),
$$

and the caps on $(r+1)$-sets. Its proof does not need caps on
all intermediate subsets. The fifth-power argument uses the
two-clique cap to bound their cross edges by $2r$; the present
fourth-power proof instead includes the exceptional vertex in
the capped set, obtaining the stronger estimate
$c_{ij}\le m_i+m_j+d_id_j$. This explains the improved threshold.

Section 4's full-resolution exclusion is already in Packing tools.
Appendix B's nonuniform pentagon blow-up supplies the same
local-only obstruction as the first family in Local-cap obstructions,
at parameters $r=5k$ rather than $r=5k+2$. Its exceptional
component violates the full cap by

$$
e(H)-D_r(2r+1)=5k^2+k-2>0.
$$

Its claimed local minimum $2k^2$ is attained by occupancies
$(2k+1,2k,0,0,k)$ in the input's cyclic labeling; the phrase
“next small class” should not be read as selecting bag 2 instead
of bag 4. No new coloring counterexample results.

Appendix D's private-clique construction, pairwise-disjoint exception
classes, full-clique absorption, and support-component independence
bounds are correct and already present in
[Two-supported private cliques](two_supported_private_cliques.md).
Its concern about iterating after absorption is legitimate, but
the established [Full-row deletion](full_row_deletion.md)
handles the initial independence drop when at least three full
rows occur, and then justifies subsequent deletion and absorption.
Its “another color has a full clique” conclusion is weaker than
the existing $\Omega(\sqrt r)$-color conclusion. None of these
arguments removes the all-deficient remainder.

## Disagreements and failed inferences

The averaged independence bound left undecided in Appendix F is already an
established input in Packing tools. Rechecking [Abiad--Kumar--Pragada, Theorems
2.2 and 3.1](https://arxiv.org/html/2609.00210v1#S2) confirms the localized
inequality; Jensen gives the averaged version. This uses that theorem, not an
unjustified replacement of maximum degree by average degree.

Appendix E's warning about inheriting the original minority budget
is correct. The present [potential reduction](minimal_ratio_potential.md)
does not inherit an average-degree upper bound of $r$; it proves
$2e(H)\le r|H|+r(r-a)$. A concrete nonregular minimal core inside
a graph satisfying the global budget, but failing the local cap,
is recorded there to isolate the failed inference.

Appendix F's additive exception charge has no injective charging
rule: several exceptions can share the same obstruction edges.
The limitation is retained in Transversal equality. Optimizing a
stability partition by local moves is still only a suggestion;
no additional completion result follows from the input.

The support-component deletion in Appendix D preserves the
one-color independence bound, but should not be conflated with
a simultaneous component decomposition in all colors. More
generally, actual color components and edge-disjoint spanning
witnesses with leftover edges are different hypotheses.

## Claims without enough supplied proof

Section 6 lists further assertions whose linked topical files
are not included in the independent input. Its no-packing claim
for $r$ spanning witnesses, each made of $r-2$ cliques of order
$r$ and a $(2r+1)$-vertex independence-two component, does follow
from the checked small-independence exclusion: color each witness
with its own color and assign leftover edges arbitrarily.
Every color still has independence at most $r$, while the
exceptional component still has target independence at most two.
The color-coupling span bound gives a contradiction.

The more specific exact-component inequality

$$
r^2-(a^2-3a+1)r-4a+2\le0
$$

was not reconstructed in the first audit. The second audit below supplies its
proof in [Cross-color cores](cross_color_cores.md).
The unspecified longer bounded-template assertions still have no
supplied proof and remain unverified.

## Second independent input: checked comparison

The [second isolated input](independent/clique_residue_and_affine_repair.md)
was read as unverified mathematical input and compared with every
topical note linked by the root index. Its named supporting companion
files are not retained. The conclusions recorded here
come from checking its displayed proofs or reconstructing those
missing arguments, not accepting its claims of prior checking.
The archived body is retained unchanged.

### Additions and stronger deductions

**Affine repairs.** Section 5's local perturbation proof is valid:
for an arbitrary old partition into $r$ sets of order $r$,
independence at most $r$ and the local $(r+1)$-set cap force
$t\ge r^{4/3}/4-r/2$ crossing edges, with asymptotic constant
$4^{-2/3}$. Its pentagon example, local cap, old partition, exact
edit counts, and change of distinguished vertex were reconstructed
and checked. They are recorded in
[Local-cap obstructions](local_cap_obstruction.md). The example
violates the full hereditary cap, so its claimed sharp exponent
applies only to the weaker one-graph hypotheses.

The decisive comparison is to count defective **rows**, not high
cross-degree vertices. There are at most $2rt/(r^2-t)$ defective
rows. Matching-transversal rigidity controls the intact rows, and
the established quadratic hereditary span theorem excludes the
remaining small-independence core. The complete checked proof in
[Affine edit obstruction](affine_edit_obstruction.md) gives

$$
t>\frac{r^2}{16\sqrt r+1},\qquad
M>\frac{(r-1)r^2}{16\sqrt r+1}
=\left(\frac1{16}-o(1)\right)r^{5/2}.
$$

This improves both the input's $r^{7/3}$ repair bound and the
previous quadratic bounds asymptotically, not necessarily at every
small parameter. Its separate finite quadratic assertion is already
weaker than the earlier checked bound and was not needed.

**Incident palettes.** Section 6's minimum-degree block accounting
and square-root palette estimate check. Applying that accounting
with all other colors' independence bounds, rather than only the
local cap, gives a stronger result. If $q$ colors are absent at
a vertex, then

$$
q(5r^2-3r+4-2q)\le r^2(r-1),
\qquad q<r/5.
$$

Thus every vertex sees more than $4r/5$ colors. The convex
block-cost proof, including its harmless $r=3$ rounding exception,
is in [Palette and cut bounds](palette_and_cut_bounds.md).
That note also proves both supplied cut inequalities and records
an additional parity-rounding improvement.

**Packing and components.** Section 3's transversal classification
is already in [Packing tools](packing_tools.md), but its forced
independent-set-to-block charge was missing from one existing
packing bound. It can be added simultaneously with the residual's
Turán edge lower bound. The same note records the resulting
formula and the checked exclusion of $r-1$ disjoint full cliques
in a minority graph for $r\ge5$.

Section 4's component and leakage identities are correct, including
the correction for uncolored pairs. They are in
[Cross-color cores](cross_color_cores.md). Applying the established
nonpartite Turán gap to foreign colors on every independence-$s$
component residue gives the stronger necessary inequality

$$
r^2-(s^2-3s+1)r-4s+2\le0.
$$

This supplies a full proof of the unverified formula
from the first independent input. It still requires the stated
simultaneous component decompositions; pruning colors independently
does not supply them while retaining edge coverage.

**Failures of local-only stability.** Section 7.1 validly extends the
existing equal-bag pentagon family to every $r\ge11$. The more
substantial Section 7.2 gives $r-\Theta(\sqrt r)$ full cliques,
not $r-O(1)$, even with the minority budget, minimum degree
$r-1$, local caps, and independence-criticality. Its full
capped-simplex proof is in Local-cap obstructions. Every
pentagon component already violates a full hereditary cap,
with explicit positive excess. These are rigorous failures of
weaker proposed lemmas, not coloring counterexamples.

### Superseded claims and precise limits

Section 2's singleton-clique count, elementary high-minimum-degree
partiteness lemma, deletion argument, and numerical threshold all
check. The random-completion expectation should be described as
**at most** $M/\min_i|N(v)\cap A_i|^2$; this is strictly less
than one when $M>0$, while $M=0$ gives expectation zero directly.
This is a wording correction, not a substantive gap.

In an actual coloring, that theorem is superseded by
[Hereditary span](hereditary_span_bound.md): the same $sr+1$
residue is impossible for $r\ge64s^2$, without an external
monochromatic $K_r$. Its fixed-$s$ clique-packing consequence
can likewise use this stronger threshold.

The independent statement that existence of a suitable minority
$K_r$ is unproved describes only its isolated investigation.
[Packing tools](packing_tools.md) already forces full cliques
in a least color using the checked localized independence bound.
It does **not** force a clique-rich near-resolution, which remains
the relevant gap.

Section 7.3's critical-edge witness is correct; its disconnected
independence-$r$ consequence is made explicit in
[Minimal-core structure](minimal_core_structure.md). It does not
exclude connected independence-$r$ graphs, and the surviving
minimal-ratio core is already $K_r$-free without that argument.

Section 8's color-preserving transitive exclusion is weaker than
[Symmetry obstructions](symmetry_obstructions.md), which permits
the action to permute colors. Its tensor failure and warnings
about simultaneous repairs agree with the retained construction
notes. The cut statement about balanced sets means a balanced
bipartition of the whole vertex set, not any two small equal sets.

**The unrestricted problem remains unresolved.** No result from this
comparison excludes either surviving core in its full parameter
range or constructs a counterexample.

## Third independent input: checked comparison

The [third isolated input](independent/uniform_capacity_and_clique_packings.md)
was read as unverified and compared with all topical notes linked by the root
index. Its supporting `notes/` files are absent. Claims of prior auditing were
not treated as evidence; the useful proofs were checked from the displayed
arguments or reconstructed independently. The archived body is preserved,
including its explicit unresolved status.

### Additions and stronger deductions

**Small-independence graphs.** Section 3's two-slot argument works under
the one-graph hereditary caps, not only in an actual coloring. It gives
capacity $|H|\le2r$ for $r\ge3$, improving the earlier cap-only threshold
$r\ge4$. Its shortest-odd-cycle degree argument gives a much shorter
proof of the existing two-row equality theorem for $r\ge6$. Both are
in [Two-row structure](two_row_structure.md).

The independence-three proof also checks and can be shortened further:
an overloaded $3r+1$-set cannot contain $K_r$, because deleting it would
leave an overloaded independence-two set. Every nonneighborhood then
has at most $2r-1$ vertices by two-row equality. The complement-degree
upper bound contradicts the inherited lower edge bound by $(r-5)/2$.
This gives cap-only span for $r\ge6$, recorded in
[Three-row structure](three_row_structure.md), improving its previous
threshold $12$ for span alone. Equality rigidity at order $3r$ remains
proved only for $r\ge12$. These improvements do not establish new cases
of the original coloring problem.

**Packing in every color.** Sections 5.3--5.5 survive checking. In particular
the triangle-support lemma is valid:
symmetrize vertices outside the triangle support using maximum
**total** degree, and handle an empty first neighbor part separately.
The resulting bound is sharp. The matching-transversal attachments,
duplicate-color propagation, and both budget polynomials check. The
omitted $r=3,4$ cases of $p\le r-2$ were reconstructed, rather than
accepted from the unavailable scratch link.

There is a stronger conclusion after comparison. The established
private-row excess in [Cross-color cores](cross_color_cores.md) changes
the fiber bound to

$$
t_i(A)\le(r-1)(p-1-e(r))+1,
\qquad e(r)=\left\lceil\frac{\sqrt{8r-7}-5}{2}\right\rceil.
$$

If $p=r-a$ and the residue contains an independent $(a+1)$-set,
transversal rigidity gives $t_i(A)\ge(p-1)^2+a+1$. The exact difference
of these bounds is $a(p-2)-(r-1)e(r)$. Combining this with the checked
small-independence and quadratic span theorems yields

$$
\boxed{p\le r-\max\{3,\lfloor\sqrt r/8\rfloor\}-1\quad(r\ge8).}
$$

The complete elementary input proof and the stronger deduction are in
[Global clique packing](global_clique_packing.md). This is an upper
bound on disjoint full cliques in every color, not a bound on their
total number and not a lower bound supplying a contradiction. It does
not validate the separate unaudited total-clique-count draft in
[Private-clique approach](private_clique_approach.md).

**Concentrated affine repairs.** Section 6's vertex-cover bound is valid:
with $q=\min\{d\ge1:\binom{d+1}{2}\ge r-1\}$, replacing $k$ old points
by $k+1$ arbitrary vertices requires

$$
k\ge\left\lceil\frac{(r-1)q^2}{r+q-2}\right\rceil
=2r-O(\sqrt r).
$$

The proof, including empty residual lines, is in
[Affine edit obstruction](affine_edit_obstruction.md). Applied to a
vertex cover of the changed-old-edge graph, it bounds edit concentration.
The existing order-$r^{5/2}$ edit-count bound alone gives only an
order-$\sqrt r$ cover bound, so this addition has distinct content.
The weaker assertion $M\ge(r-1)^2+1$ is already superseded even by
the earlier quadratic bound $M\ge2(r-1)^2$; its longer equality
analysis was not needed or incorporated.

**A growing-independence barrier.** Section 7.2's cycle blowup checks,
including its exact local nonedge minimum, criticality, proper-induced
minimality, and surplus formula. It gives more than the input states:
heavy-bag anchors furnish two-support with $b<r$ and satisfy the desired
light-set bound. Thus the least-core budget, local cap, two-support,
bounded exceptions, criticality, and induced minimality can hold
simultaneously while the overloaded independence number is unbounded.

The full proof is in
[Growing-independence barrier](growing_independence_barrier.md). The same note
gives a simpler exact rejection than the input's asymptotic warning: a
light--heavy--light union has only $t^2$ nonedges, less than the required
$(r-1)(t-g)$, for every stated parameter. This is a failure of weaker proposed
arguments, not a graph meeting the full core hypotheses and not a compatible
family of color graphs.

### Superseded results and useful limitations

Sections 1--2 agree with the existing reductions and stability induction.
The $r\ge256a^6$ proof checks, including empty cores, full-part random
choices, and the final constants. Under all hereditary caps it is weaker
than $r\ge64a^2$. As in the first comparison, its narrower assumptions
remain distinct: whole-set density and $(r+1)$-set caps suffice for
that sixth-power proof. It does not require every intermediate cap.

Section 4 gives a minimal overloaded induced subgraph in **every color**.
The current [least-color potential reduction](minimal_ratio_potential.md)
also retains the budget, and its [structure](minimal_core_structure.md)
gives further restrictions. Those stronger budget conclusions must not
be assigned to every color's independently extracted core. Neither
version proves that the core lies in the small-independence range.

Section 5.1's lower bound $e(G_i)\ge T+r-1$ is already established by
both the nonpartite gap and [Palette and cut bounds](palette_and_cut_bounds.md).
Its batchwise local-cap refinement is weaker than the latter note's
full-cap charge $(r-1)p_r(b)$. The fiber construction is the existing
[two-supported private-clique](two_supported_private_cliques.md)
mechanism; it does not close the clique-safe assignment, deletion,
or all-deficient normalization gaps. The matching-transversal extremizer
also differs from the weight-one extremizer in
[Transversal equality](transversal_equality.md); it supplies no missing
near-equality completion theorem.

Section 7.1's pentagon constructions reiterate the distinction between
local and hereditary caps in [Local-cap obstructions](local_cap_obstruction.md).
The weighted family's displayed counts and local minimum check, but the
claimed model-specific sharp lower bound has no supplied proof and is
not adopted. Its $r^{4/3}$ scale already occurs in the retained local-only
examples. All the cycle blowups are line graphs of multicycles, so the
established [line-graph span](line_graph_obstruction.md) and
[subdivision-network](clique_path_networks.md) results reject them under
full caps, without any bounded-independence assumption. The final
provisional weighted-cycle calculation is not needed, and its unavailable
precise inequality remains unverified.

The regular-color observation in Section 7.3 is superseded by
[Symmetry obstructions](symmetry_obstructions.md), which allow permuted
colors and also exclude general one-point transitivity for $r\ge100$.
The compatibility warnings remain correct: completing edge-disjoint
witnesses preserves independence bounds, but need not preserve their
components. Partial-net incidences, proper-subset marginal consistency,
or counts of near-full clusters do not force the required full-clique
packing. The index's separate budgeted and bounded-exception cores
remain separate under their full hypotheses.

**Unresolved.** No checked claim from this input excludes the surviving
cores for all parameters or constructs a counterexample.

## Fourth independent input: checked comparison

The [fourth isolated input](independent/growing_local_independence_range.md) was
read as unverified, then compared with the root index and all its linked topical
notes. Its supporting `notes/` files are unavailable. The checks used its
displayed arguments and the established proofs, not its claims of prior
auditing. The archived body is preserved unchanged.

### A useful boundary example, with stronger verification

Section 7's graph
$H=\overline{C_5(r-2,r-2,1,1,1)}$ has the stated order $2r-1$,
independence two, clique number $r-1$, and edge count $D_r(2r-1)-1$.
It actually satisfies **all hereditary caps** for every $r\ge3$.
Its complement has maximum degree $r-1$ and $(r-1)^2+1$ edges;
deleting vertices gives

$$
e(\overline H[W])\ge(r-1)(|W|-r)+1
\quad(r\le|W|\le2r-1).
$$

The complete proof is in [Two-row structure](two_row_structure.md).
This makes explicit the sharpness of the $K_r$-free order bound and
the failure of a naive boundary induction. It is not a new obstruction
to the actual surviving cores: the family is among the existing odd-core
structures, and [Unit-deficit propagation](unit_deficit_propagation.md)
already has locally colored, cap-saturating examples at this order for
$r\ge4$. The separate suppression counterexample in
[Local-cap obstructions](local_cap_obstruction.md) has the same order
but different private-row behavior.

### Valid results already matched or surpassed

**Local independence.** Sections 1--3 check, including the exact
$2r$ rigidity proof, the degree-$r$ step for $P_3$ when $r\ge6$,
and the harmonic greedy clique construction in Theorem 4. In that
construction the accumulated complement deficit is at most $2k^2H_k$;
the exceptional partition, strict random-transversal bound, and final
$3r/8+r/8$ estimate are valid. These give alternative proofs, not better
conclusions than the established [two-row](two_row_structure.md) and
[three-row](three_row_structure.md) results or
[Hereditary span](hereditary_span_bound.md). The latter replaces

$$
r\ge256k^6(1+\log k)^3
\quad\text{by}\quad r\ge64k^2
$$

under the hereditary hypotheses available in a coloring, and also proves
equality rigidity at order $kr$. Thus the input's statement that no
general boundary theorem was proved describes only its isolated
investigation. The overloaded-component consequence likewise improves
to independence greater than $\sqrt r/8$; this still leaves an unbounded
range, not a contradiction.

**Full-clique packings.** Theorem 5 is valid, including its
matching-transversal classification and maximum-degree equality fact.
Its direct grid argument is an alternative to the full-resolution
obstruction already in [Packing tools](packing_tools.md). Section 7's
conditional edge charge and polynomial $D(r,h)$ also check. They omit
the additional residual contribution $p_r(hr+1)$ retained in equation
(P) of that note. More decisively,
[Global clique packing](global_clique_packing.md) already proves

$$
p\le r-\max\{3,\lfloor\sqrt r/8\rfloor\}-1\qquad(r\ge8)
$$

in every color, stronger than the input's minority-only $p\le r-3$.
Neither upper bound forces a large packing to exist.

**Double-neighbor exceptions.** The private-fiber identities and
inequalities (16)--(17) are valid. One omitted case should be explicit:
a double cannot have two full supporting fibers. Its $r-1$ nonneighbors
in each would have to be completely joined, contradicting the external
degree-one bound into a full clique. This also excludes the
$d=1$, no-deficient-fiber case before applying the $sr+1$ edge budget.
With one full support the double is complete to its deficient support;
with two deficient supports the square-root assignment works as stated.

The resulting fourth-root lower bound is weaker than the existing
[cross-color excess-deficit bound](cross_color_cores.md), which applies
to every foreign color without assuming $d\le r$. Writing $s$ for the
number of deficient fibers and $E=\sum_{t_a>0}(t_a-1)$ gives

$$
d=E+s+1\ge
\left\lceil\frac{\sqrt{8r-7}-5}{2}\right\rceil+2
\qquad(r\ge7).
$$

No upper bound on exceptions, clique-safe completion, or least-color
budget follows from the independent lower bound.

**Single-color obstructions.** The near-equal pentagon construction for
every $r\ge11$, its edge budget, and its small-set optimization check.
They already appear with additional properties in
[Local-cap obstructions](local_cap_obstruction.md). The exceptional
$2r+1$-vertex core violates the full hereditary cap and is excluded by
$P_2$. These examples refute a proof from the minority budget and local
caps alone, not one using every inherited cap or the actual coloring.
The input's unsupported links to further scratch constructions add no
independently checked claim beyond the displayed arguments.

### Resolved auxiliary uncertainty and failures that remain useful

Section 7 leaves the averaged inequality

$$
\alpha(G)\ge\frac{2|G|}{\overline d(G)+\omega(G)+1}
$$

unproved. It is already established in [Packing tools](packing_tools.md):
the localized bound of
[Abiad--Kumar--Pragada, Theorem 3.1](https://arxiv.org/html/2609.00210v1#S3),
followed by Jensen and $c(v)\le\omega(G)$, gives exactly this inequality.
Theorem 2.2's inequality proof and Theorem 3.1 were rechecked in the
primary source for this audit. The input's minimum-degree reduction is
therefore not a remaining research gap. Its warning against replacing
the mean degree on a maximum independent set by the graph's mean is
nevertheless correct; the stronger
[degree-balancing counterexamples](light_independent_set_obstruction.md)
show why that substitution cannot justify the theorem. The averaged
inequality forces a least-color $K_r$, not a near-complete resolution or
a solution of the light-set problem.

The exact-component versus spanning-template warning also remains
correct. Adding leftover edges preserves independence upper bounds but
may destroy components. In the particular $(r-2)K_r$ plus
independence-two-core template, $P_2$ excludes the spanning core itself,
so that obstruction survives completion. It does not justify arbitrary
component incidence arguments after independently pruning colors.

**Research status unchanged.** No checked claim combines the separate
budgeted and bounded-exception normalizations, excludes the surviving
core range, or supplies a counterexample coloring.
