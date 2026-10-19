# wiki/research/leads/equilateral_two_scale/_index.md

[cut]

By Lemma 1.3 and Corollary 1.4 of
[[../library/discrete_geometry/jelinek_2009_monochromatic_triangles_two_colored_plane/corollary_1_4|Jelínek, Kynčl, Stolař and Valla]],
which they take from Erdős, Graham, Montgomery, Rothschild, Spencer and
Straus, a coloring that contains a monochromatic equilateral triangle of
side $a$ contains every triangle with a side $a$, and a coloring that
contains a monochromatic triangle with sides $a,b,c$ contains a monochromatic
equilateral triangle of one of those sides. Hence the problem is equivalent
to this two-scale question, the target of the lead: for which $x>0$, $x\ne1$,
does every two-coloring of the plane contain a monochromatic equilateral
triangle of side $1$ or of side $x$? A full solution answers it for every
such $x$, or exhibits a coloring missing two sides. The question is symmetric
under $x\mapsto1/x$, and copies may be taken by translations and rotations
alone, since equilateral triangles are symmetric under reflection.



[cut]

**Candidate conclusion.** Every two-coloring of the whole plane contains a
monochromatic congruent copy of every non-equilateral triangle, including
every collinear triple of distinct points, and misses at most one
equilateral side length. Thus it misses at most one triangle congruence
class, which, if present, is equilateral.



[cut]

1. **Finite forcing.** Lemma 1.3 and Corollary 1.4 of Jelínek et al. reduce
   the question to simultaneous avoidance of equilateral sides $1$ and
   $x\ne1$. The eight-point configuration is reconstructed in coordinates
   on the [[research/leads/equilateral_two_scale/circle_exclusion|circle
   account]], including its orientation-preserving maps and its
   positive-measure version. No picture is needed for this interface.
2. **Carrier.** Given $x>0$, use $L=F_x(i)$, where $F_x$ is the real
   closure of $\mathbb Q(x)$ inside $\mathbb R$, and its unit group $K_x$.
   This is a countable dense carrier containing both equilateral
   triangles. Proposition 3 of the
   [[research/leads/equilateral_two_scale/transcendental_scales|carrier
   account]] also proves its exact equivalence to the whole-plane
   avoidance question by finite compactness and real-closed transfer.
3. **Unit template.** At transcendental $x$, Theorem 1 of the
   [[research/leads/equilateral_two_scale/unit_templates|finite-cover
   account]] rules out a finite cover of $K_x$ by the kernels
   $u\mapsto\lambda(q_j u)$ of an $E$-linear functional with
   $\lambda(1)=1$, where $E$ is the algebraic numbers. It reduces such a
   cover to a finite function field, forces rational Cauchy transforms,
   and factors the functional through a finite-dimensional algebra where
   Cayley transforms contradict the cover. Propositions 6--8 of the
   carrier account turn this into the rational unit-vector template
   required by the rigidity proof. At algebraic $x$, the original
   number-field selection has its stated hypotheses.
4. **Haar rigidity.** Theorem 2 of the
   [[research/leads/equilateral_two_scale/rigidity_extension|rigidity
   extension]] applies the template to the wild-character proof in
   Sections 2 and 3 of the OpenAI plane-coloring manuscript. Its other
   field inputs are countability, density, real closedness and divisibility
   of $K_x$, all discharged there. The source's relative-singularity,
   compact-tower and multiple-average arguments supply the radial
   identities; the template replaces the number-field step. Every wild
   invariant character law on $L$ is therefore Haar, 

[cut]


5. **Binary transfer.** In an invariant law on an avoiding coloring,
   projection of the origin sign onto continuous vectors is conditional
   expectation. Corollary 3 of the rigidity extension preserves every
   nonzero pair correlation. The identity
   $Q(a,b,c)=1+ab+ac+bc\ge0$ on $[-1,1]^3$, with equality only when both
   endpoint signs occur, gives a Borel weakly avoiding coloring by joint
   sampling and thresholding. The
   [[research/leads/equilateral_two_scale/binary_transfer|binary account]]
   supplies this argument; it applies on $L$ to both scales for every
   real $x>0$.
6. **Measurable exclusion.** Theorem 4 of the circle account excludes
   weak measurable avoidance at two unequal scales. A Bessel bound treats
   $x\ge3/2$ and $x\le2/3$. Inside that window a boundary point would
   force alternation under a sixty-degree rotation and invariance under
   an irrational rotation on one of its two circles, unless the circle
   contains a positive-length part of the null boundary. The two-step
   circle map rules out a nonempty null set with that property. Empty
   measure-theoretic boundary makes a color null or conull, contradicting
   avoidance. This argument needs no classification of measurable
   single-scale avoiders.
7. **Whole conclusion.** If an arbitrary coloring missed equilateral
   sides $a<b$, rescale to $1,x=b/a$. Step 5 would give a weak measurable
   avoider, contradicting step 6. Thus at most one equilateral side is
   missed. Step 1 gives every non-equilateral triangle, and hence the
   stated at-most-one-congruence-class conclusion.



[cut]
