# Erdős Problem 173: statement and context

From the corpus's problem page for Erdős Problem 173, the corpus's claim page for Shader's 1976 theorem, and the library's pages for the 1975 paper of Erdős, Graham, Montgomery, Rothschild, Spencer and Straus, as they stood on 2026-10-19.

## Targets

`challenge.lean` states five theorems. Each is compared against the target named
here.

- `Erdos173.erdos_173`: the Statement, with a triangle read as three
  non-collinear points.
- `Erdos173.erdos_173.variants.right_triangle`: Shader's Theorem 2.
- `Erdos173.erdos_173.variants.equilateral_exception`: the commentary's remark
  that some coloring, the coloring by alternating strips being the example,
  misses an equilateral triangle.
- `Erdos173.erdos_173.variants.non_equilateral`: Conjecture 3 of *Euclidean
  Ramsey Theorems, III*, for nondegenerate triangles, that is, three
  non-collinear points.
- `Erdos173.erdos_173.variants.three_distinct_points`: Conjecture 3, with a
  triangle read as any three distinct points, collinear ones included; and,
  together with `Erdos173.erdos_173`, the Statement when three distinct
  collinear points count as a triangle.

## Statement

**Statement.** In any $2$-colouring of $\mathbb{R}^2$, for all but at most one
triangle $T$, there is a monochromatic congruent copy of $T$.

## The question and its commentary

**The question (erdosproblems.com formulation, page last edited 16 October
2025).** The statement above; OPEN. The commentary, in this page's words: some
colorings force one equilateral triangle to be excluded, the coloring of the
plane by alternating strips being the example, and Shader [Sh76] proved the
statement for any single right triangle. The 1975 colloquium paper of Erdős,
Graham, Montgomery, Rothschild, Spencer and Straus poses the question as its
Conjecture 3, that every non-equilateral triangle has a monochromatic congruent
copy in every two-coloring of the plane, and shows by its Theorem 1 that a
coloring misses a triangle with sides $a$, $b$, $c$ exactly when it misses the
equilateral triangles of all three side lengths; so the question is whether a
two-coloring of the plane can miss equilateral triangles of two different sides.
The discussion on erdosproblems.com held one comment (15 February 2026) citing
that paper, Graham's 2017 survey of Euclidean Ramsey theory, Currier, Moore and
Yip's 2024 paper and the 2025 computational paper of Mundinger and coauthors,
and the proof-claim tab was empty on 6 October 2026.

## Shader's theorem (the claim page for Shader 1976)

**Claim.** L. E. Shader, *All right triangles are Ramsey in $\mathbb{E}^2$!*, J.
Combin. Theory Ser. A 20 (1976), no. 3, 385--389. A triangle is Ramsey in the
plane when every two-coloring of $\mathbb R^2$ contains a monochromatic
congruent copy of it. Theorem 2 states that every right triangle is Ramsey in
this sense; Corollary 4, that every triangle with sides $a$, $b$ and
$\sqrt{b^2+2a^2}$ with $2b>a$ is Ramsey; and Corollary 5, that every triangle
with sides $a$, $b$ and $\sqrt{4b^2-a^2}$ with $\sqrt{3/2}\,b<a<\sqrt{5/2}\,b$
is Ramsey. The engine is Lemma 1: for every real $a>0$ and every two-coloring of
the plane there is a monochromatic equilateral triangle of side $ka$ for some
$k\in\{1,3,5,7\}$, proved by a case analysis on the coloring of a lattice.
Theorem 3 states that every parallelogram has a congruent copy with three
vertices of one color, which decides no triangle. The source is carded at
[[../library/discrete_geometry/shader_1976_all_right_triangles_are_ramsey_e2/_index|shader_1976_all_right_triangles_are_ramsey_e2]].

## Conjectures 2 and 3 of Euclidean Ramsey Theorems, III

From the library's pages
`library/discrete_geometry/erdos_1975_euclidean_ramsey_theorems_iii/conjecture_3.md`,
`library/discrete_geometry/erdos_1975_euclidean_ramsey_theorems_iii/theorem_1.md`
and
`library/discrete_geometry/erdos_1975_euclidean_ramsey_theorems_iii/theorem_9.md`
for P. Erdős, R. L. Graham, P. Montgomery, B. L. Rothschild, J. Spencer and
E. G. Straus, *Euclidean Ramsey Theorems, III*, Infinite and Finite Sets
(Keszthely 1973), Colloq. Math. Soc. János Bolyai 10, North-Holland (1975),
559--583, with one sentence quoted from p. 559 of the paper. Quotations are
marked; the rest is in the library's words.

**Triangles and $R(K)$** (p. 559). The paper considers only the plane, two
colors and three-point sets: "That is if $K$ is a triangle (= a set of three
points) in $E^2$, we consider the following statement: $R(K)$: For any
2-coloring of $E^2$ there is a monochromatic $K'$ congruent to $K$." For a
fixed two-coloring $f$, $R_f(K)$ says that some $K'$ congruent to $K$ is
monochromatic under $f$ (p. 562).

**Conjecture 2** (p. 560), as posed: "If $E^2$ is 2-colored so that there is
no equilateral triangle of side $d$, then there is a monochromatic
equilateral triangle of side $d'$, for $d'\ne d$." The hypothesis is read
with "monochromatic" understood, as the surrounding text and the
reformulation on p. 565 show: the paper restates Conjecture 2 as saying that
$T_f=\{(a,a,a)\}$ for some $a>0$, or $T_f=\emptyset$, so the conclusion
is for every $d'\ne d$.

**Conjecture 3** (p. 560), as posed: "If $K$ is a triangle which is not
equilateral, then $R(K)$ is true."

The paper derives Conjecture 3 from Conjecture 2 through its Theorem 1 and
states that the two are equivalent in view of Theorem 1 (p. 560). It puts
$T=\{(a,b,c):0\le a\le b\le c\le a+b\}$ and, for each two-coloring $f$, lets
$T_f$ be the set of triples $(a,b,c)\in T$ with no monochromatic triangle of
sides $a$, $b$, $c$ (pp. 563--564); it restates Conjecture 3 as
$T_f\subset\{(a,a,a)\mid a>0\}$ for every two-coloring $f$ (p. 564). Its
Theorem 9 (p. 572) states $R(K)$ for several families of triangles $K$, and
the print notes that one of them includes $K=(a,2a,3a)$, three collinear
points.
