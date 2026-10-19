---
name: discrete_geometry/plasma_ai_2026_monochromatic_triangles_two_colorings_plane/evidence/verify/statement_fidelity/report
title: "Whole-statement fidelity audit: Lean challenge file for Erdős Problem 173"
desc: |
  Fresh-context refutation-charge audit, on 2026-10-19, of the definition and
  five statements of the Problem 173 formalization's challenge file against
  the problem's Statement under both readings of a triangle, Shader's theorem,
  the remark on the exception and Conjecture 3: all faithful, the Statement
  covered whole, the claim partly.
created: 2026-10-18T02:18:16Z
updated: 2026-10-19T02:49:23Z
---

***

# Whole-statement fidelity audit: Lean challenge file for Erdős Problem 173

## Subject

Role: independent fresh-context reviewer under a refutation charge. The task is
to find any defect in the fidelity of the Lean challenge file for Erdős Problem
173 to the mathematical statements it formalizes. I wrote none of the material
under audit.

- Examination date (UTC): 2026-10-19.
- Freeze date of the extraction: 2026-10-19.
- Files read, each in full, all in the extraction folder `extraction/` beside
  this report: `assignment.md`, `problem_statement.md`, `claim_statement.md`,
  `challenge.lean`, `fc_173.lean`, `fc_2d.lean`.
- Scope: the definition `Erdos173.HasMonochromaticCopy` and the five theorems
  `Erdos173.erdos_173`, `Erdos173.erdos_173.variants.right_triangle`,
  `Erdos173.erdos_173.variants.equilateral_exception`,
  `Erdos173.erdos_173.variants.non_equilateral` and
  `Erdos173.erdos_173.variants.three_distinct_points` of `challenge.lean`, each
  against the target named in `problem_statement.md` "Targets"; the bridge
  between the two notions of a copy and the two readings of the Statement
  (assignment item 6); the colorings (item 7); the copy claim against
  `fc_173.lean`, with `fc_2d.lean` as supporting definitions, and every
  docstring assertion (item 8); and coverage of the Statement and of the Claim
  and Covers paragraphs of `claim_statement.md` (item 9). The truth of the
  statements and their proofs are out of scope.
- I did not compile or run the Lean file. Where a finding depends on how Lean 4
  or Mathlib defines, parses or elaborates something, it rests on my general
  knowledge and is marked "(general knowledge)".

## Independence

I was given the path of the assignment and the path of this report, with the
instruction to read only the extraction folder. I had no part in the
formalization, the claim, the extraction or any earlier review, and I was shown
no earlier review. I read the six files above and no other. I ran no command,
searched no filesystem, consulted no version history and used no web source.

Exposure outside the read set, at the point it happened:

- Before I opened any file, the environment that launched this review placed
  the organization's and the repository's general agent-instruction text in my
  context. It states working conventions (verification tiers, page rules,
  citation by path and date) and says nothing about Problem 173, its claim or
  this formalization. No finding relies on it.
- The same launch context showed directory names, among them the name of the
  library folder that holds this report. They carry no mathematical content.
- `problem_statement.md` names three library page paths and a wiki link target
  for the 1976 source. I saw these names in that file and did not open them.
- `fc_173.lean` imports `FormalConjecturesUtil`, and `fc_2d.lean` imports three
  `FormalConjecturesForMathlib` files. I did not read them. Item 8 below
  accounts for this.

## (a) Restatement

### Targets

- **Statement** (target of `erdos_173`, with a triangle read as three
  non-collinear points; with `three_distinct_points`, also under the reading in
  which any three distinct points form a triangle). For every coloring of the
  plane with two colors, the triangles with no congruent copy whose three
  vertices share a color fall into at most one congruence class.
- **[Sh76] Theorem 2** (target of `right_triangle`). For every right triangle
  and every two-coloring of the plane, some congruent copy of the triangle has
  its three vertices of one color. The claim page defines "Ramsey in the
  plane" as exactly this two-coloring property.
- **The commentary's remark** (target of `equilateral_exception`). Some
  two-coloring of the plane has no monochromatic congruent copy of some
  equilateral triangle; the coloring by alternating strips is the example.
- **Conjecture 3, nondegenerate** (target of `non_equilateral`). For every
  triangle with three non-collinear vertices that is not equilateral, every
  two-coloring of the plane has a monochromatic congruent copy of it: $R(K)$.
- **Conjecture 3, as posed** (target of `three_distinct_points`). The same for
  every "triangle (= a set of three points)": three distinct points, collinear
  ones included, that are not equilateral.

### Lean statements

- **`HasMonochromaticCopy c T`.** Some triangle `T'` (three affinely
  independent labelled points of the plane) has, label by label, the same
  pairwise distances as `T`, and its three vertices all receive one color
  under `c`.
- **`erdos_173`.** For every coloring `c` and triangles `T₁`, `T₂`: if neither
  has a monochromatic copy, then some relabelling of the vertices of `T₁` has,
  label by label, the pairwise distances of `T₂`.
- **`right_triangle`.** For every coloring `c` and every triangle `T` whose
  unoriented angle at vertex `1` is $\pi/2$, `T` has a monochromatic copy.
- **`equilateral_exception`.** There are a coloring `c` and a triangle `T`
  with all three sides equal such that `T` has no monochromatic copy under `c`.
- **`non_equilateral`.** For every coloring `c` and every triangle `T` whose
  three sides are not all equal, `T` has a monochromatic copy.
- **`three_distinct_points`.** For every coloring `c` and every three pairwise
  distinct points `p 0`, `p 1`, `p 2` of the plane, collinear or not, whose
  three pairwise distances are not all equal, there are three points `q 0`,
  `q 1`, `q 2` with the same pairwise distances label by label, all of one
  color.

## (b) Clause-by-clause comparison

### Definitions unfolded

| Object | Unfolding | Verdict |
| --- | --- | --- |
| `ℝ²` | Local notation for `EuclideanSpace ℝ (Fin 2)`, that is `PiLp 2 (fun _ : Fin 2 => ℝ)`, whose `dist` is the Euclidean distance (general knowledge). `fc_2d.lean` declares the same expansion as `scoped[EuclideanGeometry] notation`. | The Euclidean plane. Faithful. |
| `Triangle ℝ ℝ²` | Under `open Affine`, `Affine.Triangle ℝ ℝ² = Affine.Simplex ℝ ℝ² 2`: a structure with `points : Fin 3 → ℝ²` and `independent : AffineIndependent ℝ points` (general knowledge). In the plane: three pairwise distinct, non-collinear, labelled points. | A nondegenerate triangle, as in reading (a). |
| `≅` | `Congruent v₁ v₂ := ∀ i₁ i₂, edist (v₁ i₁) (v₁ i₂) = edist (v₂ i₁) (v₂ i₂)`, notation scoped in `Congruent` and opened by `open scoped Congruent`, `infixl:25` (general knowledge). In a metric space `edist` is `ENNReal.ofReal dist`, so this is equality of all pairwise distances, index by index. The rival `≅` of category theory is a `Type`, not a `Prop`, so it cannot elaborate in any of the five positions (under `∧` or as the body of `∃`). | Label-by-label equality of distances. |
| `c : ℝ² → Fin 2` | An arbitrary function into a two-element type. | A two-coloring. |
| `Equiv.Perm (Fin 3)`, `T₁.points ∘ σ` | `σ` is a bijection of the labels, coerced to a function; `(T₁.points ∘ σ) i = T₁.points (σ i)`. `∘` (`infixr:90`) binds tighter than `≅` (`25`), so the conclusion parses as `(T₁.points ∘ σ) ≅ T₂.points` (general knowledge). | A relabelling of `T₁`. |
| `∠ a b c` | `EuclideanGeometry.angle a b c = InnerProductGeometry.angle (a -ᵥ b) (c -ᵥ b)`, the unoriented angle at the middle point, in $[0,\pi]$; its junk value is $\pi/2$ when `a = b` or `c = b` (general knowledge). | The angle at vertex `1`. |
| `dist` | The Euclidean distance. | — |
| `Function.Injective p` on `Fin 3 → ℝ²` | `∀ a b, p a = p b → a = b`: the three points are pairwise distinct. It says nothing about collinearity. | Three distinct points, collinear ones allowed. |

**`HasMonochromaticCopy c T`** unfolds to
`∃ T' : Triangle ℝ ℝ², (T'.points ≅ T.points) ∧ ∃ i, ∀ j, c (T'.points j) = i`,
with `i : Fin 2` and `j : Fin 3`.

- Copy. `T'` is any triangle with the distances of `T` label by label. In a
  Euclidean space a distance-preserving correspondence between finite
  configurations extends to an isometry of the whole space (general
  knowledge), so the `T'` are exactly the images of `T` under isometries of
  the plane, orientation-reversing ones included. Reflections are allowed.
  Rescaling is not, since distances are equal, not proportional.
- Relabelling. `T'` is existential and the color condition does not depend on
  labels, so any three-point set congruent to the vertex set of `T`, under any
  correspondence, can be labelled to serve as `T'`.
- The requirement that `T'` be a `Triangle` removes no copy: a configuration
  with the distances of an affinely independent `T` is itself affinely
  independent (the bridge, below).
- Monochromatic. `∃ i, ∀ j, c (T'.points j) = i` says all three vertices share
  one color.
- Verdict: faithful to "a monochromatic congruent copy", with congruence read
  as an isometric image. The Statement and the 1975 paper read congruence the
  same way. The paper parametrizes triangles by their side lengths alone ($T_f$
  is a set of triples $(a,b,c)$; Theorem 1 speaks of "a triangle with sides
  $a$, $b$, $c$"), and side lengths do not distinguish a triangle from its
  mirror image. That congruence includes reflections is also the standard
  convention of Euclidean Ramsey theory (general knowledge).

### `erdos_173` against the Statement

- Coloring: `∀ c`, with no hypothesis. Matches "in any 2-colouring of
  $\mathbb R^2$".
- Triangles: `Triangle ℝ ℝ²`, three non-collinear points. Matches reading (a),
  which the Targets section fixes for this theorem.
- "At most one, up to congruence." The exceptions (triangles with no
  monochromatic copy) are closed under congruence and relabelling, since a copy
  of one is a copy of the other. So the Statement's "at most one" can only mean
  at most one congruence class: read literally as at most one point set, it
  would forbid any exception, because an exception has infinitely many
  congruent copies. "At most one class" is the same as "any two exceptions are
  congruent", which is the Lean conclusion. The count is not changed to "none"
  and not taken up to labelling.
- Role of `σ`. `≅` compares vertices with equal labels, so a scalene triangle
  `T` and its relabelling `T ∘ (0 1)` are not `≅` to each other, though both
  are exceptions whenever one is. Without `σ` the statement would fail whenever
  any scalene exception existed. With `σ`, `∃ σ, T₁.points ∘ σ ≅ T₂.points`
  says exactly that the vertex sets are congruent: given an isometry `φ` with
  `φ {T₁ vertices} = {T₂ vertices}`, take `σ i` to be the label of the
  `T₁`-vertex that `φ` sends to `T₂.points i`; conversely the distance equality
  extends to an isometry. The congruence allows reflections, as the Statement's
  congruence does.
- Strength: an exception set contained in one congruence class gives the Lean
  conclusion for every pair, and the Lean conclusion for every pair puts all
  exceptions in one class. Neither stronger nor weaker.
- Not vacuous: `T₁ = T₂` is allowed, and the hypotheses are satisfiable by any
  coloring and equilateral triangle that witness `equilateral_exception`.
- Verdict: faithful.

### `right_triangle` against [Sh76] Theorem 2

- Every right triangle is covered. A right triangle `R` has its right angle at
  some vertex `k`. Reindexing `R` by the transposition `τ` of `1` and `k` gives
  a triangle `T` with `T.points = R.points ∘ τ` and the right angle at vertex
  `1`. `HasMonochromaticCopy` is invariant under relabelling: if `T'` witnesses
  it for `T`, then `T'.points ∘ τ⁻¹` is affinely independent, monochromatic and
  `≅ R.points`, because `≅` is preserved by reindexing both sides alike. So the
  theorem for vertex `1` gives the theorem for every right triangle.
- Junk value: `∠` is $\pi/2$ when two of its points coincide, but the vertices
  of a `Triangle` are distinct, so no degenerate configuration satisfies `hT`
  vacuously.
- Nothing beyond the target is assumed: `c` and `T` are arbitrary.
- Conclusion: a monochromatic congruent copy, reflections allowed, as above.
  The target's "Ramsey in the plane" is the two-coloring property defined on
  the claim page, not the higher-dimensional notion of a Ramsey set.
- Verdict: faithful.

### `equilateral_exception` against the commentary

- `∃ c ∃ T`: some coloring and some triangle. Matches "some coloring misses
  some equilateral triangle".
- `dist (T.points 0) (T.points 1) = dist (T.points 1) (T.points 2) ∧
  dist (T.points 1) (T.points 2) = dist (T.points 2) (T.points 0)` makes all
  three sides equal. `T` is affinely independent, so its side is positive and
  `T` is a genuine equilateral triangle.
- `¬ HasMonochromaticCopy c T`: no congruent copy of `T` is monochromatic.
  Allowing reflections changes nothing for an equilateral triangle.
- Not trivially true. The witness `T` cannot be degenerate. A constant coloring
  fails, since `T` itself is then a monochromatic copy, so the witness needs a
  coloring that genuinely misses an equilateral triangle. One exists, as a
  check on non-vacuity (my own argument): color by alternating half-open
  horizontal strips $[kh,(k+1)h)$ with $h=\tfrac{\sqrt3}{2}s$. An equilateral
  triangle of side $s$ has vertical extent between $h$ and $s<2h$, so it does
  not fit in one strip and a monochromatic copy would need vertices in strips
  $k$ and $k+2$, two of them in one strip. The third vertex lies at vertical
  distance at most $h$ from the midpoint of the other two, which sits in their
  strip, so it cannot reach the strip two away.
- The Lean statement does not name the strips coloring. The target is the
  existence remark, with the strips as its example, so the existential form is
  the right strength.
- Verdict: faithful.

### `non_equilateral` against Conjecture 3, nondegenerate

- `hT : ¬ (d01 = d12 ∧ d12 = d20)` holds exactly when the three sides are not
  all equal, that is, when `T` is not equilateral. There is no further
  restriction beyond `T` being a `Triangle`, which the target ("for
  nondegenerate triangles") fixes.
- Conclusion: `c` is a free parameter, so the theorem says `HasMonochromaticCopy
  c T` for every two-coloring `c`. For each `c` that is $R_c(K)$ for the vertex
  set $K$ of `T`; over all `c` it is $R(K)$.
- Nothing beyond the target is assumed.
- What the restriction to `Affine.Triangle` leaves out of Conjecture 3: the
  sets of three distinct collinear points, with sides $(a,b,a+b)$, such as the
  paper's $(a,2a,3a)$ in Theorem 9. Triples with coincident points are not
  sets of three points and are not part of Conjecture 3. `three_distinct_points`
  supplies the collinear sets.
- Not vacuous: the 3-4-5 triangle with vertices $(0,0)$, $(3,0)$, $(0,4)$
  satisfies `hT`, and the conclusion requires a genuine monochromatic copy.
- Verdict: faithful.

### `three_distinct_points` against Conjecture 3, and against the Statement read with collinear triangles

- `hp : Function.Injective p` says exactly that the three points are pairwise
  distinct and puts no condition on collinearity.
- `he` says the three pairwise distances are not all equal. For three distinct
  points, equal pairwise distances $s>0$ means exactly that they are the
  vertices of an equilateral triangle. Three distinct collinear points are
  never equilateral: one lies between the other two, so the outer distance is
  the sum of two positive distances and exceeds each. Hence every collinear
  triple of distinct points satisfies `he` and falls under the theorem, and
  `he` says exactly "not equilateral".
- Conclusion `∃ q, (q ≅ p) ∧ ∃ i, ∀ j, c (q j) = i`. `q ≅ p` gives `q` the
  distances of `p` label by label. Since `p` is injective, its distances
  between distinct labels are positive, so `q` is injective too: three distinct
  points. `q` is any isometric image of `p`, reflections included, and is
  existential, so relabelled copies are allowed. Rescaling is excluded. The
  color clause is the same as in `HasMonochromaticCopy`. This is a
  monochromatic congruent copy of `p`.
- The paper's "triangle (= a set of three points)" is a set with three
  elements: three distinct points, with no non-collinearity condition. Its
  Theorem 9, which includes $K=(a,2a,3a)$, confirms that collinear sets count.
- Coincident points: a triple with a repeated point is not a set of three
  points, so it is not in Conjecture 3 and not a triangle under either reading
  of the Statement. The paper's reformulation over
  $T=\{(a,b,c):0\le a\le b\le c\le a+b\}$ formally admits $a=0$, that is the
  triples $(0,b,b)$ and $(0,0,0)$, but none of them is ever in $T_f$: two of
  the three vertices of an equilateral triangle of side $b$ share a color,
  which gives a monochromatic pair at distance $b$, and a single point is
  monochromatic. Excluding coincident triples therefore drops nothing of
  substance.
- Not vacuous and not trivially true. For `p` $=(0,0),(1,0),(2,0)$, the points
  are distinct with distances $1,1,2$, so `he` holds; the conclusion then asks
  for three collinear, equally spaced points at spacing $1$ of one color.
  Nondegenerate instances (the 3-4-5 triangle) also satisfy the hypotheses.
  `q` is a plain function with every distance fixed by `q ≅ p`, so there is no
  junk value to exploit.
- Verdict: faithful.

### The bridge and the two readings (item 6)

**Bridge.** For an affinely independent `p` and the triangle `T` with
`T.points = p`: some `q` with `q ≅ p` and `∃ i, ∀ j, c (q j) = i` exists exactly
when `HasMonochromaticCopy c T`.

- (⇐) A witness `T'` of `HasMonochromaticCopy c T` gives `q := T'.points`.
  Immediate.
- (⇒) Put $u=q_1-q_0$, $v=q_2-q_0$. The Gram entries are determined by the
  pairwise distances: $\|u\|^2=d_{01}^2$, $\|v\|^2=d_{02}^2$ and
  $\langle u,v\rangle=\tfrac12(d_{01}^2+d_{02}^2-d_{12}^2)$. So `q` and `p` have
  equal Gram determinants. Three points are affinely independent exactly when
  $u$, $v$ are linearly independent (general knowledge for the Mathlib
  characterization), that is, when the Gram determinant is nonzero. So `q` is
  affinely independent, `⟨q, _⟩` is a `Triangle`, and it witnesses
  `HasMonochromaticCopy c T`.
- Verdict: the bridge holds in both directions.

**Reading (a)**, a triangle is three non-collinear points. The Statement is
exactly `erdos_173`, as shown above. Whole.

**Reading (b)**, a triangle is any three distinct points. An exception is an
injective `p` with no monochromatic `q ≅ p`. Let `p₁`, `p₂` be exceptions.

1. By the contrapositive of `three_distinct_points` (with `hp`), each `pᵢ` has
   all three distances equal, to some $s_i>0$.
2. Three distinct points with all distances equal to $s$ have Gram determinant
   $s^4-s^4/4=\tfrac34 s^4\ne0$, so each `pᵢ` is affinely independent and
   forms a triangle `Tᵢ`.
3. By the easy direction (⇐) of the bridge, `HasMonochromaticCopy c Tᵢ` would
   give a `q` for `pᵢ`, so `¬ HasMonochromaticCopy c Tᵢ`.
4. `erdos_173` gives `σ` with `p₁ ∘ σ ≅ p₂`.

So any two exceptions under reading (b) are congruent up to relabelling. The
conclusion uses `erdos_173`, `three_distinct_points`, the Gram fact of step 2
and the easy bridge direction; it does not use `non_equilateral`. The hard
direction (⇒) shows that the two notions of exception agree on non-collinear
triples, and it is needed to transfer `equilateral_exception` to reading (b)
(item 9). Under reading (b) too, the Statement is covered whole.

### The colorings (item 7)

`c : ℝ² → Fin 2` is an arbitrary function in all five theorems. In
`erdos_173`, `right_triangle`, `non_equilateral` and `three_distinct_points`
it is universally quantified with no hypothesis; in `equilateral_exception` it
is existential over all functions, which matches the target's "some coloring"
(the strips coloring is moreover measurable). No measurability or other
regularity is assumed anywhere. `Fin 2` has exactly two elements, so it matches
"2-colouring"; the claim's $\{-1,1\}$ is in bijection with it. Verdict:
faithful.

### The copy claim and the docstrings (item 8)

**Differences between `challenge.lean` and `fc_173.lean`**, found by a
line-by-line comparison:

1. `fc_173.lean` opens with an Apache 2.0 licence comment, "Copyright 2026 The
   Formal Conjectures Authors". `challenge.lean` has no such comment and names
   the copyright and licence in its module docstring.
2. Imports: `fc_173.lean` has `public import FormalConjecturesUtil`;
   `challenge.lean` has four Mathlib imports (`PiL2`, unoriented angles,
   simplices, congruence).
3. The module docstrings differ entirely. Among other things, `fc_173.lean`'s
   [Sh76] reference omits the volume, while `challenge.lean`'s has "20".
4. `challenge.lean` adds `/-- The Euclidean plane, as in formal-conjectures. -/
   local notation "ℝ²" => EuclideanSpace ℝ (Fin 2)` inside the namespace.
   `fc_173.lean` gets `ℝ²` from `fc_2d.lean`'s scoped notation with the same
   expansion, activated by `open scoped ... EuclideanGeometry`.
5. Removed attribute lists: `@[category research open, question, AMS 5 51]` on
   `erdos_173`, and `@[category research solved, AMS 5 51]` on
   `right_triangle` and `equilateral_exception`.
6. `challenge.lean` adds `non_equilateral` and `three_distinct_points` with
   their docstrings.

Everything else is identical: `module`, `@[expose] public section`,
`open Affine`, `open scoped Congruent EuclideanGeometry`, `namespace Erdos173`,
the definition with its docstring, the three theorem docstrings and
statements, and `end Erdos173`.

The differing imports do not change the meaning of the copied text. The
statements use only `Affine.Triangle`, `Congruent`, `dist`, the unoriented `∠`
and the canonical metric and torsor structure of `EuclideanSpace ℝ (Fin 2)`.
The instances that `fc_2d.lean` adds (an orientation and
`Fact (finrank = 2)`) bear on none of them. I could not read
`FormalConjecturesUtil` or the `FormalConjecturesForMathlib` files; that they
do not replace the metric on `EuclideanSpace ℝ (Fin 2)` is an assumption, not
a finding.

The copy claim holds. One point of wording: the removed attribute lists hold
`question` and `AMS 5 51` besides `category ...`. These are classification
attributes with no logical content, so "apart from their category attributes"
is accurate if it means the whole classification list, and slightly
understates the removal if read narrowly. The commit `7db2ea3b91` and the path
`FormalConjectures/ErdosProblems/173.lean` agree with the assignment's
description of `fc_173.lean`; the file itself prints neither.

**Docstring assertions.**

| Assertion | Where | Carried by | Holds? |
| --- | --- | --- | --- |
| The 1975 paper conjectured that every triangle except possibly one equilateral triangle has a monochromatic congruent copy. | Module, first paragraph | Prose. Its content is that of `erdos_173` with `three_distinct_points`. | Yes. Conjecture 3 gives the non-equilateral part, and Conjecture 2, restated as $T_f=\{(a,a,a)\}$ or $\emptyset$, gives "at most one"; the paper calls them equivalent. |
| The catalog's maintainer catalogs the question as Problem 173. | Module, first paragraph | Prose. | Not checkable in the read set; consistent with general knowledge. |
| Any two triangles without a monochromatic congruent copy are congruent. | Module, Claim | `erdos_173` | Yes. |
| Any three distinct non-equilateral points, collinear included, have a monochromatic congruent copy. | Module, Claim | `three_distinct_points` | Yes. |
| "and so the exceptional triangle, if there is one, is equilateral" | Module, Claim | Follows by contraposition from `non_equilateral` (triangles) and `three_distinct_points` (triples). | Yes. |
| Some coloring has such an exception. | Module, Claim | `equilateral_exception` | Yes. |
| Alternating half-open strips of suitable width miss some equilateral triangle. | Module, Claim; `equilateral_exception` docstring | Prose only. | Yes (strip argument above). |
| The definition and first three theorems are copied verbatim apart from category attributes, with `ℝ²` declared locally. | Module, third paragraph | Prose. | Yes, with the attribute wording point above. |
| `non_equilateral` and `three_distinct_points` are not from formal-conjectures. | Module, third paragraph | Prose. | Yes: `fc_173.lean` contains neither. |
| They state Conjecture 3. | Module, third paragraph | Both theorems. | Yes; `non_equilateral` for nondegenerate triangles, `three_distinct_points` as posed. |
| A triangle in the first four theorems is `Affine.Triangle`, so collinear triples are not covered there. | Module, third paragraph | The types of those four theorems (and of the definition). | Yes. |
| `three_distinct_points` is stated for any three distinct points. | Module, third paragraph | `three_distinct_points` (`hp` only). | Yes. |
| Conjecture 3 counts three distinct collinear points as a triangle. | Module, third paragraph | Prose. | Yes: "a set of three points" (p. 559) and Theorem 9's $(a,2a,3a)$. |
| In every statement a copy may be reflected and relabelled. | Module, third paragraph | `HasMonochromaticCopy` (existential `T'`), `three_distinct_points` (existential `q`), `erdos_173` (`σ` and `≅`). | Yes. |
| [Sh76] reference. | Module | Prose. | Matches `problem_statement.md`. |
| The five theorems have deliberate proof holes; another file proves them and a checker compares them. | Module, last paragraph | Five `sorry`s are visible. | Holes: yes. The rest is not checkable in the read set. |
| Relabellings and reflections allowed, rescaling not. | `HasMonochromaticCopy` and `three_distinct_points` docstrings | The definition and the theorem. | Yes. |
| All but at most one triangle up to congruence; `≅` compares equal labels, so `σ` is needed; no measurability. | `erdos_173` docstring | `erdos_173` | Yes. |
| [Sh76] proved every right-angled triangle has a monochromatic copy. | `right_triangle` docstring | `right_triangle`, through relabelling invariance. | Yes. |
| Every non-equilateral triangle has a copy; Conjecture 3 for nondegenerate triangles. | `non_equilateral` docstring | `non_equilateral` | Yes. |
| Three distinct collinear points never have equal pairwise distances. | `three_distinct_points` docstring | Prose only; no Lean statement asserts it. | Yes (betweenness argument above). |
| "so every collinear triple is covered" | `three_distinct_points` docstring | Implicit in the theorem: `he` holds for every collinear distinct triple. | Yes. |

No docstring assertion is false. A cosmetic difference: the module docstring
writes *Euclidean Ramsey theorems, III*, while `problem_statement.md` writes
*Euclidean Ramsey Theorems, III*.

### Coverage (item 9)

**The Statement.** Under reading (a), `erdos_173` alone covers it whole. Under
reading (b), `erdos_173` and `three_distinct_points` cover it whole through the
four steps of item 6. `right_triangle`, `equilateral_exception` and
`non_equilateral` are not needed for it. As a cross-check,
`three_distinct_points` implies `non_equilateral` (hard bridge direction), and
`non_equilateral` implies `right_triangle` (by Pythagoras the hypotenuse is the
longest side, so a right triangle is never equilateral).

**The claim of `claim_statement.md`.**

| Claim assertion | Status | How |
| --- | --- | --- |
| Colorings $c:\mathbb R^2\to\{-1,1\}$ with no measurability or regularity. | Covered | `c : ℝ² → Fin 2` is arbitrary in all five. |
| At most one positive length $r$ with no monochromatic equilateral triangle of side $r$. | Follows, not stated | Apply `erdos_173` to equilateral triangles of sides $r_1$, $r_2$, which then lack monochromatic copies; congruence forces $r_1=r_2$. |
| Equivalently, for $x>0$, $x\ne1$, every coloring has a monochromatic equilateral triangle of side $1$ or $x$. | Follows, not stated | Immediate from the previous line. The stated equivalence also holds: the converse uses rescaling the coloring by $r_1$. |
| Every non-equilateral set of three distinct points, collinear triples included, has a monochromatic congruent copy. | Covered (stated) | `three_distinct_points`. |
| That copy is obtained by a translation and a rotation. | Not covered | Every copy in the five statements may be reflected. For a scalene, non-collinear triangle a reflected copy is not a rotated and translated copy: a proper motion carrying the set onto its mirror image would match the vertices as the reflection does, and two isometries agreeing on three non-collinear points are equal. Nothing in the five statements turns a monochromatic reflected copy into a monochromatic direct one. (For collinear and isosceles triples the two notions agree, by the reflection in their line or axis.) |
| Hence for all but at most one triangle $T$ there is a monochromatic congruent copy. | Covered | `erdos_173` (reading (a)); with `three_distinct_points` and the bridge (reading (b)). |
| An exceptional $T$ is equilateral. | Follows by contraposition | `non_equilateral` for triangles, `three_distinct_points` for distinct triples. |
| Its side depends on the coloring. | Follows, not stated | `erdos_173` makes the missed side a function of the coloring. That it varies follows from `equilateral_exception` and an elementary rescaling: if `c` misses side $s$, then $z\mapsto c(z/\lambda)$ misses side $\lambda s$. |
| Covers: the whole Statement, whether or not collinear triples count. | Covered | Item 6, both readings. |
| The one exception is needed. | Covered | `equilateral_exception`. Under reading (b) the hard bridge direction shows the same triple has no monochromatic `q`. |
| The alternating-strips coloring is that exception. | Not covered by a Lean statement | Prose in two docstrings. The claim attributes it to the problem page. |
| The claim does not classify the colorings that miss a side. | Nothing to cover | Not an assertion. |

## (c) Checklist

- **"Almost all" or "at most one" quietly changed.** Applicable to `erdos_173`.
  Not changed: "at most one up to congruence" is rendered as "any two
  exceptions are congruent up to relabelling", neither "none" nor "at most one
  labelled triangle". Not applicable to the other four, which are universal or
  existential as their targets are.
- **Degenerate cases.** Applicable. Collinear triples are excluded by
  `Affine.Triangle` in four theorems and the definition, as their targets fix;
  they are included in `three_distinct_points`, where `he` holds for all of
  them. Coincident points are excluded everywhere (affine independence, `hp`),
  and belong to no target; the paper's zero-side triples are trivially never
  exceptions. Vacuity: every hypothesis is satisfiable (3-4-5 triangle,
  $(0,0),(1,0),(2,0)$, the strips witness), and every conclusion requires a
  genuine monochromatic configuration or its absence.
- **Consequence sentences as claim surfaces.** Applicable. "and so the
  exceptional triangle ... is equilateral" (module): valid by contraposition.
  "so collinear triples are not covered there" (module): valid. "so the
  conclusion allows a relabelling `σ`" (`erdos_173` docstring): valid. "so every
  collinear triple is covered" (`three_distinct_points` docstring): valid.
  "Since `T'`/`q` is arbitrary, relabellings and reflections ... are allowed":
  valid. Claim "Equivalently": valid by rescaling. Claim "Hence for all but at
  most one triangle": valid, and covered directly by `erdos_173`. The target's
  "so the question is whether a two-coloring of the plane can miss equilateral
  triangles of two different sides" is target text, consistent with Theorem 1
  as reported, and no finding relies on it. No "in particular" occurs.
- **Junk values and edge cases.** Applicable. `∠` returns $\pi/2$ at coincident
  points, but triangle vertices are distinct. `≅` uses `edist`, which is finite
  in a metric space and agrees with `dist`. `Fin 3` literals `0`, `1`, `2` name
  the three labels. No division, coercion or default value enters any
  statement.
- **Convention drift.** Applicable. Labelling: handled by `σ` in `erdos_173`,
  the existential `T'` and `q`, and relabelling invariance for the right angle
  at vertex `1`. Orientation: `∠` is unoriented, and `≅` ignores orientation.
  Reflection: allowed throughout, matching the targets' congruence; this
  departs from the claim's "translation and a rotation", recorded under
  coverage. Scaling: excluded throughout, as the targets require.

## (d) Strongest attack

The strongest attempt targeted the reflection convention. If "congruent copy"
in the Statement, in Conjecture 3 and in [Sh76] meant a copy by a translation
and a rotation only, then `HasMonochromaticCopy` and the conclusion of
`three_distinct_points`, which accept reflected copies, would be weaker than
their targets. `right_triangle`, `non_equilateral` and `three_distinct_points`
would then assert less than the targets. `erdos_173` would also be weaker,
because fewer triangles would count as exceptions.

The attack fails against the targets. The 1975 paper identifies a triangle with
its side lengths $(a,b,c)$ in $T_f$, in Theorem 1 and in the restatement of
Conjecture 3, and side lengths cannot tell a triangle from its mirror image; so
its congruence includes reflections. That is also the standard convention of
Euclidean Ramsey theory (general knowledge), and the Statement uses the same
words. For equilateral triangles, which carry the exception, the two
conventions agree.

The attack does land on the claim, not on the formalization: `claim_statement.md`
asserts copies "obtained by a translation and a rotation", which no Lean
statement carries for scalene non-collinear triangles. It is a coverage gap,
not a fidelity defect.

Other attempts that failed: dropping `σ` (shown necessary and sufficient); a
mismatch between the two notions of exception under reading (b) (closed by the
Gram-determinant bridge); collinear triples escaping `he` (impossible by
betweenness); a vacuous or degenerate witness for `equilateral_exception`
(excluded by affine independence and by the constant-coloring check); and the
`∠` junk value (unreachable).

## Verdict

- `HasMonochromaticCopy`: faithful.
- `erdos_173`: faithful.
- `erdos_173.variants.right_triangle`: faithful.
- `erdos_173.variants.equilateral_exception`: faithful.
- `erdos_173.variants.non_equilateral`: faithful.
- `erdos_173.variants.three_distinct_points`: faithful.
- Copy claim: holds. The definition and the first three statements, with their
  docstrings, are identical to `fc_173.lean`. The only removals are the
  attribute lists, which hold `question` and `AMS 5 51` besides `category`, and
  the only addition to the copied part is the local `ℝ²` notation with its
  docstring.
- Coverage of the Statement, reading (a), triangles as three non-collinear
  points: whole, by `erdos_173` alone.
- Coverage of the Statement, reading (b), triangles as any three distinct
  points: whole, by `erdos_173` with `three_distinct_points` through the
  bridge.
- Coverage of the claim: partial. Not covered: the requirement that the copy be
  obtained by a translation and a rotation alone, since every statement allows
  reflected copies; and the identification of the strips coloring, which is
  prose only. Follows without being stated: the single missed side length and
  its $x\ne1$ form, that an exceptional triangle is equilateral, that its side
  depends on the coloring (with an elementary rescaling), and the Statement
  under reading (b). Stated: the monochromatic copy of every non-equilateral
  set of three distinct points, collinear triples included (reflections
  allowed); "all but at most one triangle" under reading (a); that one
  exception is needed; and the absence of any regularity assumption on the
  coloring.
