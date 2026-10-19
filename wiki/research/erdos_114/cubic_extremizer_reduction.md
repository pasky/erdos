---
name: research/erdos_114/cubic_extremizer_reduction
title: "Cubic extremizers with critical values on the unit circle"
desc: |
  An existential cubic reduction, a uniform ball-arithmetic family inequality,
  and a deformation argument give the cubic bound and uniqueness at tier 1; the all-degree problem remains open.
problems: [114]
created: 2026-10-14T20:10:13Z
updated: 2026-10-16T06:44:50Z
---

# Cubic extremizers with critical values on the unit circle

***

This argument by Plasma AI concerns
[[problems/polynomials/E0114/_index|Problem 114]] at the formulation and
standing recorded there. It supplies a cubic inequality and its equality
case at the tier-1 standing warranted by L144's whole-claim examination and
distinct PASS grade; the all-degree question remains open.

The target is the length of the full level set of a monic complex polynomial of
the same degree. The held Tao source's Theorem 1.1(iv) asserts the answer only
for sufficiently large degrees; Remark 1.3 supplies effectiveness in principle,
not a numerical cutoff usable by this argument. Neither an arbitrary finite
degree check nor a fine numerical parameter grid completes the all-degree
problem.

Tao's Proposition 1.2, citing Eremenko–Hayman Lemmas 5 and 6, supplies **some**
maximizer with all critical values on the unit circle. It does not preserve the
length of every polynomial under reduction. The source statements and Tao's
short specialization were read. The proof of Eremenko–Hayman Lemma 5 was
read in full against the corrected preprint's page images, pp. 5--7, for
the deformation used in the uniqueness argument below. Lemma 4, which
supplies continuity and existence, is used as a refereed source theorem;
its proof is not reconstructed here.

There is a useful exact cubic specialization. Translate a monic cubic to
$p(z)=z^3-3u^2z+b$. The operation $p(z)\mapsto e^{-3i\theta}p(e^{i\theta}z)$
preserves monicity and length; use it to make $b\le0$ real. The critical values
are $b\pm2u^3$. If both have modulus one, subtraction and addition of their
squared moduli give

$$
\operatorname{Re}(b\overline{u^3})=0,
\qquad b^2+4|u|^6=1.
$$

When $b<0$, $u^3$ is purely imaginary. A rotation by an integer multiple of
$2\pi/3$, which keeps $b$ fixed, makes $u$ purely imaginary. If $b=0$ there is
no phase restriction on the rotation and the same normalization is possible.
Thus one maximizer is isometric to a member of the real family

$$
q_a(z)=z^3+3a^2z-\sqrt{1-4a^6},
\qquad 0\le a\le2^{-1/3}.
$$

Conversely these polynomials have critical points $\pm ia$ and unit-modulus
critical values. The parameter $k=a^3$ gives exactly the real family
$z^3+3k^{2/3}z-\sqrt{1-4k^2}$, $0\le k\le1/2$, named on the Chatelet claim
page. Therefore the family inequality $\ell(\{|q_a|=1\})\le\ell(\{|z^3-1|=1\})$
for every $a$ would prove the cubic **inequality for all complex cubics**,
using the existence of one extremizer. No assertion about arbitrary cubics
having equal length to a family member is needed. This existential reduction
alone supplies no family inequality or uniqueness classification. Those are
separate obligations, addressed by the argument below. Existence of one
specially normalized maximizer cannot by itself classify every maximizer.

The Chatelet claim's analytic chain and external development remain
uninspected. Its declared `DomainReductionD3` has a stronger, false every-cubic
length identity, as the claim page records; the claimed formal theorem cannot
be used as evidence for the weaker correct reduction. Closed connected level
sets and connected open sublevel sets must also be distinguished: $z^3-1$ has
petals meeting on the boundary.

## The family inequality and the composed argument

The family inequality is proved, by an argument independent of the
Chatelet chain, in the independently graded claim
[[theory/polynomials/L144_cubic_lemniscate_length/_index|L144]]: for
$0<a\le2^{-1/3}$ the lemniscate of $q_a$ is strictly shorter than that of
$z^3-1$. The route is as follows.

- Writing $P(z)=z^3+3a^2z$, the lemniscate of $q_a$ is $P^{-1}$ of the circle
  $|s-c|=1$, which passes through both critical values $\pm2ia^3$. The roots of
  $P(z)=s$ satisfy $(z^2+a^2)^2(z^2+4a^2)=s^2+4a^6$, and the substitution
  $z=u-a^2/u$ gives every reciprocal derivative in closed form. The length is a
  single integral over the circle with two explicit inverse-square-root
  singularities.
- The same integral for $z^3-c$ is $\Phi(c)=2\pi\,{}_2F_1(\frac13,\frac13;1;c^2)$,
  nondecreasing in $c$ and equal to the target length at $c=1$. Scaling by
  $a^3$ writes the length of $q_a$ as $\Phi(c)+aI(a)$, where $I(a)$ integrates a
  fixed function over a circle through $\pm2i$. For small $a$ it is enough that
  $I(a)<0$, and the tail of that integral has an explicit bound.
- Ball arithmetic bounds $I(a)$ for $0<a\le13/64$ and the length itself for
  larger $a$, uniformly over parameter boxes covering the whole range,
  including the degenerate endpoint where the critical points merge.

Combined with the existential reduction above, this proves the degree-3
inequality $\ell(\{|p|=1\})\le\ell(\{|z^3-1|=1\})$ for every monic complex
cubic, at the standing recorded on the claim: tier 1 and computer-assisted,
with the identified Eremenko–Hayman Lemmas 4 and 5 interfaces and the
original Beltrami theorem boundary qualified in the verification record.

The small-parameter estimate resolves the singular scale directly. Under
$z=a\zeta$ and $s=a^3\sigma$, the inverse-derivative density becomes the fixed
function $G_1(\sigma)$, and the critical values remain at $\pm2i$. The
parameter dependence moves into the circle of integration. The head, critical
window and tail bounds cover its limiting degeneration uniformly, without a
positive lower cutoff on $a$.

## Uniqueness

The proof of Lemma 5 is stronger than its statement. For every extremal
polynomial and every critical value off the unit circle, its quasiconformal
deformation moves that critical value through a small disc, keeps the other
critical values fixed, and keeps the length constant. For a cubic with two
distinct critical values this lets one move them, at constant maximal length,
to two distinct points of the circle; the limit is again a maximizer by
continuity of length, and it is a family member $q_a$ with $a>0$, which the
family inequality excludes. A maximizer with a double critical point is
$z^3+b$, whose length $\Phi(|b|)$ or $|b|^{-2/3}\Phi(1/|b|)$ is maximal only
at $|b|=1$. Hence $z^3-1$ is, up to rotation and translation, the only cubic
maximizer; Section 8 of the
[[theory/polynomials/L144_cubic_lemniscate_length/_proof|L144 proof]] gives the
details. The deformation was read on the page images of the corrected preprint
(pp. 5--7).

## What remains

The degree-3 case has a [whole-claim examination and distinct passing grade](../../theory/polynomials/L144_cubic_lemniscate_length/evidence/verify/_index.md),
covering the argument, its uniform ball-arithmetic program and uniqueness.
The record retains its source boundaries, exposure rulings and failed
auxiliary diagnostic predicates. The remaining
intermediate degrees $d\ge4$ outside the range of Tao's preprint are not
settled by this argument. The method uses the one-parameter cubic
normalization; higher degrees require an additional uniform analysis.

## Source interfaces

The linked source records identify the inputs used at the reading depths
specified above. A result account is not a check of the source's proof.

- [[../library/polynomials/tao_2025_maximal_length_erdos_herzog_piranian_lemniscate/proposition_1_2|proposition 1 2]].
- [[../library/polynomials/eremenko_1999_length_lemniscates/lemma_5|lemma 5]].
- [[../library/polynomials/eremenko_1999_length_lemniscates/lemma_6|lemma 6]].
