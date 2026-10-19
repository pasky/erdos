---
name: problems/distance_problems/E0097/claims/evidence/verify/deduction_review
title: Review of the deduction of Problem 97 from Problem 96
desc: |
  Retains the fresh-context adversarial review of 2026-10-14, which found the
  project's deduction of a counterexample to Problem 97 from the accepted
  disproof of Problem 96 correct and complete.
created: 2026-10-14T01:24:27Z
updated: 2026-10-14T01:24:27Z
---

***

## Record, attribution and exact subject

**PASS.** The deduction on
[[problems/distance_problems/E0097/claims/2026_10_14_plasma_ai|the project's claim page on Problem 97]]
is correct and complete as a proof, from the accepted result recorded on
[[problems/distance_problems/E0096/claims/2026_09_10_kruer_kohlmeyer|the claim page on Problem 96]],
that the answer to Problem 97 is no and that the general form, in which a fixed
$k$ replaces four, fails for every $k\ge2$. Reviewed on 2026-10-14 (UTC).

Reviewer: a fresh-context adversarial reviewer (Opus 5.5) at Plasma AI, run as
an isolated assignment distinct from the author of the deduction; it had not
built on the subject before the review. Its charge was to try to break the
deduction and to return PASS or FAIL with reasons. It was given only the four
files below, read each in full, used no network and edited nothing. No distinct
grader is recorded, so no numerical tier is assigned.

The four files, numbered as the report numbers them:

1. `wiki/problems/distance_problems/E0097/claims/2026_10_14_plasma_ai.md`, the
   subject;
2. `wiki/problems/distance_problems/E0096/claims/2026_09_10_kruer_kohlmeyer.md`,
   the accepted claim on Problem 96;
3. `wiki/problems/distance_problems/E0097/claims/2026_09_13_kruer_kohlmeyer_price.md`,
   the claim page of Kruer, Kohlmeyer and Price;
4. `wiki/problems/distance_problems/E0097/_index.md`, the problem page and its
   Statement.

The subject is file 1 as first written on 2026-10-14. After the review the
page was changed as the report asks: the Claim's first sentence (D1); the
paragraph on the sources, which now calls the deduction the contrapositive of
the site's remark (D2) and attributes to Lemma 4.1 and Remark 4.5 only what
file 3 records (D3); and the desc and the wording the report lists (D4). File
2 now takes $d=4k-3$ for the general form (D5). The page's link now names the
accepted Lean solution of Problem 96, and its Standing paragraph became the
Acceptance paragraph. No step of the proof changed. The exact reviewed text is
not retained in this repository.

This record was filed from the reviewer's report, which is retained below in
full. The filing rewrapped the report to 80 columns and added this section; it
changes no path, scope, date or verdict.

## Retained report

VERDICT: PASS

The deduction is correct and complete. Take Theorem 1.1 of the accepted Problem
96 claim as given, with d=13 (or the accepted negation of O(n) with constant 3).
The page then proves that some convex polygon has every vertex with at least
four other vertices at distance 1, which answers the Statement "no". It also
proves the fixed-k form false for every k ≥ 2. The defects below are about
wording and how the page relates itself to its sources. None of them affects the
proof.

**Checks**

1. **Input: pass.**
   - File 2 records Theorem 1.1 as giving, for every integer d ≥ 2, a set V_d in
     strictly convex position with |V_d| = N_d = 2d^d·2^{d^{d+1}} and u(V_d) ≥
     (d/4)N_d. Step 1 quotes this exactly.
   - With d=13 and N_13 > 0, u ≥ (13/4)N_13 > 3N_13, so φ(V_0) > 0 strictly, as
     the deletion needs.
   - The page defines u (unordered pairs at distance exactly 1) and strictly
     convex position (no point in the convex hull of the others) the same way
     file 2 does.
   - N_13 = 2·13^13·2^{13^14} is the correct value of the formula.
   - The alternative route is valid. The accepted Lean file proves ¬(f =O[atTop]
     n), where f(n) is the supremum of unit-pair counts over n-point sets in
     strict convex position. Not big-O with constant 3 means f(n) > 3n for
     infinitely many n. That supremum is over a nonempty set (n points on a
     circle qualify) of naturals bounded by C(n,2). So it is attained, or at
     least exceeded only by real sets, and some n-point strictly convex set has
     more than 3n unit pairs.
   - The page's phrase "since that maximum is taken over counts at most C(n,2)"
     covers this, though briefly.
   - One assumption is left unstated: that the Lean predicate "strict convex
     position" equals "no point in the convex hull of the others". File 2 says
     so only in words (see caveat 2).

2. **Deletion: pass.**
   - Removing p from V_i removes exactly the deg_{V_i}(p) unit pairs that
     contain p, so u(V_{i+1}) = u(V_i) − deg ≥ u(V_i) − 3 and |V_{i+1}| = |V_i|
     − 1. Hence φ = u − 3|S| never decreases.
   - By induction φ(V_i) > 0 at every step, and the process stops within |V|
     steps because each step removes a point.
   - At the end, u(W) > 3|W| ≥ 0 gives u(W) ≥ 1, so W is nonempty. The stopping
     rule gives deg_W(p) ≥ 4 for every p in W, so |W| ≥ 5.
   - Which removable point is chosen at each step does not matter. Everything
     checks.

3. **Convex position and the polygon: pass.**
   - Heredity holds: W\{p} ⊆ V\{p}, so conv(W\{p}) ⊆ conv(V\{p}).
   - No three points of W are collinear, since the middle one would lie on the
     segment between the other two. With |W| ≥ 5 and no three collinear, P =
     conv(W) has nonempty interior.
   - The corners of the convex hull of a finite set are points of that set. A
     point of W that is not a corner is a convex combination of the corners,
     which are other points of W; that would contradict strict convexity.
   - So the vertices of P are exactly W: at least 5 of them, none missing, none
     extra, and no straight-angle vertices.
   - The page uses these standard convexity facts without proving them, which is
     acceptable.

4. **Conclusion against the Statement: pass.**
   - The Statement asks for every convex polygon to have a vertex with no 4
     other vertices equidistant from it. Its negation is: some convex polygon
     has, at every vertex, 4 other vertices at a common distance. P satisfies
     this with distance 1, using any four of the at-least-four unit neighbours.
   - "At least four" is the right reading. Having five at one distance includes
     four. The problem page's falsifiability note says the same thing ("every
     vertex has four other vertices at a common distance"), and Danzer's
     three-neighbour nonagon is read the same way.
   - An "exactly four" reading would not be refuted directly, but that reading
     is unnatural (caveat 3).
   - Step 4 states the conclusion correctly. Its remark that the common distance
     happens to be 1 at every vertex, which the question does not require, is
     accurate.

5. **General form: pass.**
   - For k ≥ 2, d = 4k−3 ≥ 5 ≥ 2 is allowed, and (4k−3)/4 = k − 3/4 > k−1.
   - Deleting points of degree at most k−1 with φ = u − (k−1)|S| works exactly
     as before. The surviving W has every degree ≥ k, so |W| ≥ k+1 ≥ 3, and it
     is strictly convex, so it is a nondegenerate polygon.
   - k=4 gives d=13, which matches the main case. (k=1 is trivially false for
     any polygon and needs no argument.)
   - The formal route also extends to general k by using the constant k−1,
     though the page claims it only for k=4.

6. **Overstatements and source relations: mixed.** The proof's dependence is
   stated accurately: it uses only Theorem 1.1 (or the accepted negation) plus
   elementary convexity. The size bound N_13 follows correctly from W ⊆ V_13.
   The Standing section rightly says the certified Lean object is only the
   negation of O(n). Three issues are listed below as defects D1 to D3.

**Defects**

- **D1 (needs a fix): one sentence of the Claim paragraph is false as written.**
  Lines 26–28: "...at least four other vertices at distance exactly 1 from it,
  so no vertex has four other vertices equidistant from it in the sense the
  question excludes."
  - Read literally, "no vertex has four other vertices equidistant from it" says
    the opposite of what is proved. The trailing qualifier does not repair it.
  - It should say something like: "so every vertex has four other vertices
    equidistant from it, and no vertex is of the kind the question asks for."
    Step 4 already says this correctly.

- **D2 (needs a fix): the page gets the logical relation to the site's remark
  wrong.**
  - "Relation to the sources" says: "a positive answer to this problem would
    give a linear bound for Problem 96. The deduction here runs the other way
    and needs only one direction..."
  - The site's remark is: a yes to Problem 97 means at most 3n unit pairs in
    every convex set. Its contrapositive is: a convex set with more than 3n unit
    pairs gives a no to Problem 97. That contrapositive is exactly this page's
    deduction, and the site's induction is the deletion step run backwards.
  - So the deduction runs in the same direction as the site's remark, not the
    other way. Together with the accepted Theorem 1.1, it is a one-line
    consequence of a remark the site already published.
  - The reason given ("since this problem lets the common distance vary")
    explains why the converse fails. It does not explain what the deduction
    "needs". The sentence is muddled.
  - This also weakens the originality framing ("so the claim is the project's").
    The written-out proof is the project's, and it adds a few small things: P is
    an explicit subset of V_13, the common distance is 1 at every vertex, and it
    gives the N_13 bound. The page should say plainly that the core disproof is
    the contrapositive of the site's remark applied to the accepted theorem.
  - File 2 uses the same "In the other direction" wording.

- **D3 (needs a fix): the cited page does not support what the page attributes
  to Lemma 4.1 and Remark 4.5.**
  - The page says these results "state that strictly convex sets with
    arbitrarily large minimum unit-distance degree exist exactly when the ratio
    of unit pairs to points is unbounded over strictly convex sets."
  - The page it links (file 3) records only that Lemma 4.1 and Remark 4.5 state
    the deletion step "in general". The "exactly when" equivalence appears on
    files 2 and 4, not on file 3.
  - The equivalence is true: the reverse direction is u ≥ δ·n/2. But from the
    read set I cannot confirm that it is what those two results say. Either
    record their content on the KKP claim page or soften the attribution.

- **D4 (cosmetic): small wording problems.**
  - The desc says "with 13/4 unit pairs per point" and "four others at distance
    one". These should say "at least 13/4" and "at least four".
  - "whose Theorem 1.1 of Kruer and Kohlmeyer supplies" is ungrammatical.
  - "this page rests on neither" has an unclear antecedent: neither the
    manuscript's lemma nor its disproof?
  - "published in general form" is loose for an unrefereed GitHub manuscript.
  - "a point of W that were not a vertex" is awkward.

- **D5 (cosmetic): the two pages pick different d for the general form.** File 2
  uses d = 4k and file 1 uses d = 4k−3. Both are valid, but the pages disagree.

**Caveats**

1. **The N_13 bound rests on the paper's Theorem 1.1, not on the certified
   object.** The step-1 route and the N_13 bound depend on Theorem 1.1's exact
   form (|V_d| = N_d, constant d/4). The Lean certification covers only the
   negation of O(n), as the page itself says, and the corpus has not built that
   proof. The disproof itself survives through the formal route, but the size
   bound N_13 does not follow from that route. I took Theorem 1.1 as given, as
   instructed.
2. **The formal route assumes the Lean predicate is strict convexity.** It
   relies on "strict convex position" in the formal-conjectures statement
   meaning "no point in the convex hull of the others". If it meant weak convex
   position, the surviving set could have points sitting on the polygon's edges,
   and step 3 would need adjusting. The step-1 route does not depend on this.
3. **The reading of "4 vertices equidistant".** The pass assumes it means "four
   other vertices at a common distance", that is, at least four. That is the
   standard reading and the corpus's own reading.
4. **What I read.** I read only the four assigned files. I did not check the
   content of the Kruer and Kohlmeyer explanation, the Lean files, or the KKP
   manuscript.
