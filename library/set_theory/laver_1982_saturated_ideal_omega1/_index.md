---
name: set_theory/laver_1982_saturated_ideal_omega1
title: "Laver: An (ℵ₂, ℵ₂, ℵ₀)-saturated ideal on ω₁"
desc: |
  Laver's 1982 paper building, from a huge cardinal, a model of 2^ℵ₀ = ℵ₁ and
  2^ℵ₁ = ℵ₂ with a normal (ℵ₂, ℵ₂, ℵ₀)-saturated ideal on ω₁, and showing that
  CH with such an ideal gives a polarized relation for ω₂ × ω₁ and, for a
  normal ideal, ω₂ → (ω₁ + ω₁ + 1, α)^2 for every α < ω₂; the paper does not
  state that GCH holds in its model.
license: reserved
created: 2026-10-14T22:55:45Z
updated: 2026-10-14T23:06:55Z
---

# Laver: An (ℵ₂, ℵ₂, ℵ₀)-saturated ideal on ω₁

[[set_theory/_index|..]]

[[set_theory/laver_1982_saturated_ideal_omega1/main_theorem|main_theorem]]: Laver's § 1 theorem that the consistency of a huge cardinal gives the
consistency of a normal (ℵ₂, ℵ₂, ℵ₀)-saturated ideal on ω₁, in a model of
2^ℵ₀ = ℵ₁ and 2^ℵ₁ = ℵ₂; the paper does not state that GCH holds there.

[[set_theory/laver_1982_saturated_ideal_omega1/theorem_p177|theorem_p177]]: Laver's § 3 theorem, proved in sketch, that 2^ℵ₀ = ℵ₁ and a normal
(ℵ₂, ℵ₂, ℵ₀)-saturated ideal on ω₁ give ω₂ → (ω₁ + ω₁ + 1, α)^2 for every
α < ω₂, so the model of § 1 satisfies ω₂ → (ω₁ + ω)^2_2.

***

Richard Laver, *An $(\aleph_2,\aleph_2,\aleph_0)$-saturated ideal on
$\omega_1$*, in D. van Dalen, D. Lascar and J. Smiley (eds.), *Logic
Colloquium '80*, Studies in Logic and the Foundations of Mathematics **108**,
North-Holland, 1982, pp. 173--180, doi:10.1016/S0049-237X(09)70510-5; the
author at the University of Colorado, Boulder. Cited as [La82] on Problem
1170's page and as [120] in Komjáth's survey of the Erdős–Hajnal problem list.

The copy read for this card is the publisher's PDF from ScienceDirect: 8
pages, printed pp. 173--180 = PDF pp. 1--8 (printed p. $n$ is PDF p.
$n-172$), a scan of the printed chapter with an OCR text layer that garbles
most of the mathematics, so the statements below were read on rendered page
images. The file prints "© North-Holland Publishing Company, 1982" in the
header of its first page (p. 173). The Crossref record
(<https://api.crossref.org/works/10.1016/S0049-237X(09)70510-5>, read
2026-10-14) names Elsevier as publisher and lists only text-and-data-mining
licenses, with no Creative Commons license: every other right reserved.

**What the paper proves.** Kunen had obtained an $\aleph_2$-saturated ideal on
$\omega_1$ from a huge cardinal, and Magidor from an almost huge one (p. 173).
§ 1 modifies Kunen's construction to obtain, from a huge cardinal, a normal
$(\aleph_2,\aleph_2,\aleph_0)$-saturated ideal on $\omega_1$: every $\aleph_2$
positive sets include $\aleph_2$ of which every countably many have positive
intersection
([[set_theory/laver_1982_saturated_ideal_omega1/main_theorem|main theorem]]).
§ 2 shows that $2^{\aleph_0}=\aleph_1$ and an
$(\aleph_2,\aleph_2,\aleph_0)$-saturated $\omega_1$-ideal give the polarized
relation
$\binom{\aleph_2}{\aleph_1}\to\binom{\aleph_1}{\aleph_1}^{1,1}_{\aleph_0}$: for
every $f:\omega_2\times\omega_1\to\omega$ there are sets $A\subseteq\omega_2$
and $B\subseteq\omega_1$ of size $\aleph_1$ with $f$ constant on $A\times B$
(p. 176). The paper recalls that its [3], the Erdős–Hajnal problem list of
1971, asked whether the weaker
$\binom{\aleph_2}{\aleph_1}\to\binom{\aleph_0}{\aleph_1}^{1,1}_2$ is consistent
with $2^{\aleph_0}=\aleph_1$, and it reports Galvin's extension of § 2 to
$\binom{\omega_2}{\omega_1}\to\binom{\alpha}{\omega_1}^{1,1}_{\aleph_0}$ for
every $\alpha<\omega_2$. § 3 proves, in sketch, that $2^{\aleph_0}=\aleph_1$
and a normal such ideal give $\omega_2\to(\omega_1+\omega_1+1,\alpha)^2$ for
every $\alpha<\omega_2$
([[set_theory/laver_1982_saturated_ideal_omega1/theorem_p177|theorem of p. 177]]),
after recalling that [3] asked whether $\omega_2\to(\omega_1+\omega)^2_2$ is
consistent. § 4 strengthens the saturation in the model of § 1, adding a normal
ideal on $\omega_2$ with a countably closed dense set, and shows that the
variant model in which $\kappa$ becomes $\aleph_2$ and $\lambda$ becomes
$\aleph_3$ satisfies the Chang-type relation
$\aleph_3\to(\aleph_2)^{\aleph_0}_{\aleph_2/\aleph_1}$. By p. 173, every result
except that last one has an analogue with $\omega_1$ replaced by the successor
of an arbitrary regular cardinal.

**GCH.** The paper does not state that GCH holds in its model. The model of
§ 1 satisfies the proposition $\Phi$, whose first clauses are
$2^{\aleph_0}=\aleph_1$ and $2^{\aleph_1}=\aleph_2$ (p. 174, with pp. 173 and
175); the paper says nothing about $2^{\aleph_2}$ or larger powers, or about
the ground model's continuum function, and mentions GCH only on p. 177, as the
hypothesis of a question about the polarized relations of § 2. The
[[set_theory/laver_1982_saturated_ideal_omega1/main_theorem|main theorem's page]]
gives the passages. Komjáth's survey reports the result as the consistency of
GCH with such an ideal (Problem 24, p. 431, of
[[set_theory/komjath_2025_erdos_hajnal_problem_list/_index|the survey]]); that
is the survey's wording, not the paper's. The ideal of § 1 is normal (pp. 173
and 175).

Read status: claims checked. The definitions and announcements of p. 173, the
remark on Woodin's dense ideal on p. 174, the proposition $\Phi$ with Kunen's
clauses (a)--(c) on p. 174, the assertions of p. 175 that the new iteration has
the $(\kappa,\kappa,<\beta)$-cc, that $2^\kappa=\lambda$ in the final model and
that the ideal is normal and nontrivial, the § 2 statement and Galvin's
extension on p. 176, the GCH question, the remark on consistency relative to
ZFC and the § 3 statement on p. 177, the § 4 statements on pp. 178--179, and
the reference list (pp. 179--180) were read clause by clause on the page
images. The proofs of §§ 1--4 were looked through on the page images and no
proof step was checked; the proof of § 3 is itself a sketch. Nothing here is
independently reviewed.

**Bears on.** [[../wiki/problems/set_theory/E1172/_index|#1172]]: the model of
§ 1 satisfies $2^{\aleph_0}=\aleph_1$ and has a normal
$(\aleph_2,\aleph_2,\aleph_0)$-saturated ideal on $\omega_1$, so by the § 3
theorem it satisfies $\omega_2\to(\omega_1+\omega)^2_2$, relative to a huge
cardinal (a one-line deduction made here). The ideal is normal, but the paper
states only $2^{\aleph_0}=\aleph_1$ and $2^{\aleph_1}=\aleph_2$ in that model,
not GCH, which the problem's consistency question requires.
[[../wiki/problems/set_theory/E1170/_index|#1170]]: in the same model
$\omega_2\to(\alpha)^2_2$ holds for every $\alpha\le\omega_1+\omega_1+1$, a
partial instance of the problem; the paper says nothing about larger
$\alpha<\omega_2$.

**Results.**

- [[set_theory/laver_1982_saturated_ideal_omega1/main_theorem|Main theorem]]
  (§ 1, pp. 173--176): from a huge cardinal, a normal
  $(\aleph_2,\aleph_2,\aleph_0)$-saturated ideal on $\omega_1$, with what the
  paper says about the continuum function of its model.
- [[set_theory/laver_1982_saturated_ideal_omega1/theorem_p177|Theorem of p. 177]]
  (§ 3, pp. 177--178): $\omega_2\to(\omega_1+\omega_1+1,\alpha)^2$ for every
  $\alpha<\omega_2$, from $2^{\aleph_0}=\aleph_1$ and a normal such ideal.

No file of this source is held: no license on record permits its redistribution,
and the card cites the edition it names above.
