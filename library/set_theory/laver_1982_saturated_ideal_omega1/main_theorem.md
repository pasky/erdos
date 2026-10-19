---
name: set_theory/laver_1982_saturated_ideal_omega1/main_theorem
title: "Main theorem (§ 1): from a huge cardinal, a normal (ℵ₂, ℵ₂, ℵ₀)-saturated ideal on ω₁"
desc: |
  Laver's § 1 theorem that the consistency of a huge cardinal gives the
  consistency of a normal (ℵ₂, ℵ₂, ℵ₀)-saturated ideal on ω₁, in a model of
  2^ℵ₀ = ℵ₁ and 2^ℵ₁ = ℵ₂; the paper does not state that GCH holds there.
created: 2026-10-14T22:55:45Z
updated: 2026-10-14T22:55:45Z
---

***

**Source.** Richard Laver, *An $(\aleph_2,\aleph_2,\aleph_0)$-saturated ideal
on $\omega_1$* (1982): the definitions and the statement on p. 173, the
proposition $\Phi$ and Kunen's construction on p. 174, and the proof of § 1 on
pp. 174--176. The edition is identified on the
[[set_theory/laver_1982_saturated_ideal_omega1/_index|source card]].

**Definitions (p. 173).** For a regular uncountable cardinal $\kappa$, a
$\kappa$-ideal is a nontrivial $\kappa$-complete ideal $\mathcal J$ of subsets
of $\kappa$, and $\mathcal J^+$ is the family of subsets of $\kappa$ not in
$\mathcal J$. An $\omega_1$-ideal $\mathcal J$ is
$(\aleph_2,\aleph_2,\aleph_0)$-saturated when every family of $\aleph_2$ sets
in $\mathcal J^+$ has a subfamily of $\aleph_2$ sets in which every countable
subfamily has its intersection in $\mathcal J^+$; the paper takes the notion
from its author's earlier paper (its [10]).

**Statement.** If the existence of a huge cardinal is consistent, then it is
consistent that there is a normal $(\aleph_2,\aleph_2,\aleph_0)$-saturated
$\omega_1$-ideal (p. 173). In detail (pp. 174--175): let $j:V\to M$ witness
that $\kappa$ is huge, with $j(\kappa)=\lambda$. Laver modifies Kunen's forcing
to a two-step forcing $\bar{\mathbb B}=\bar{\mathcal P}\otimes\bar{\mathcal Q}$
after which $\kappa=\omega_1$ and $\lambda=\omega_2$. The extension
$V^{\bar{\mathbb B}}$ is a model of Kunen's proposition $\Phi$ below, with a
stronger form of its clause (2), and in it an ideal $\mathcal J$ on $\kappa$,
defined on p. 175 from an ultrafilter on $\kappa$ in a further extension, is a
normal nontrivial ideal on $\omega_1$ that is
$(\aleph_2,\aleph_2,\aleph_0)$-saturated.

**The proposition $\Phi$ (p. 174).** $\Phi$ says that $2^{\aleph_0}=\aleph_1$,
that $2^{\aleph_1}=\aleph_2$, and that there are a poset $\mathbb C$ and, in
$V^{\mathbb C}$, an elementary embedding $\tilde j:V\to N$ into a transitive
class with $\tilde j(\alpha)=\alpha$ for $\alpha<\omega_1^V$ and
$\tilde j(\omega_1^V)>\omega_1^V$, such that (1) $\mathbb C$ is a two-step
forcing whose first factor has the $\aleph_2$-chain condition and whose second
is $\aleph_2$-closed, and (2) $\{\tilde j(\alpha):\alpha<\omega_2^V\}\in N$ and
$\tilde j(\omega_1^V)=\omega_2^V$. The paper recalls that Kunen proved $\Phi$
consistent relative to a huge cardinal, that clause (1) gives an
$\aleph_2$-saturated ideal on $\omega_1$, and that clause (2) gives Chang's
conjecture.

**What the paper says about GCH in this model.** The paper does not say that
the generalized continuum hypothesis holds in its model. Its statements about
the continuum function there are three. The model satisfies $\Phi$, whose
first two clauses are $2^{\aleph_0}=\aleph_1$ and $2^{\aleph_1}=\aleph_2$
(p. 174: Laver shows "how to modify it to get a model" of $\Phi$). The
introduction says that $2^{\aleph_0}=\aleph_1$ "holds in the model of §1"
(p. 173). The proof uses that $2^\kappa=\lambda$ in $V^{\bar{\mathbb B}}$
(p. 175), that is, $2^{\aleph_1}=\aleph_2$. Nothing is said about
$2^{\aleph_2}$ or larger powers, and the paper names no hypothesis on the
ground model beyond the huge embedding, assuming familiarity with Kunen's
construction (p. 174). The abbreviation GCH occurs only on p. 177, in the
question how strong the two polarized relations of § 2 are "assuming GCH", and
in the remark that, relative to ZFC alone, $2^{\aleph_0}=\aleph_1$ and
$2^{\aleph_1}>\aleph_2$ are consistent with the first of them (start with a
model of GCH and add more than $\aleph_2$ subsets of $\omega_1$ with countable
conditions). Komjáth's survey reports this theorem as making GCH consistent
with an $(\aleph_2,\aleph_2,\aleph_0)$-saturated ideal on $\omega_1$ (Problem
24, p. 431, of
[[set_theory/komjath_2025_erdos_hajnal_problem_list/_index|his problem-list survey]]);
that is the survey's wording, not the paper's.

**Normality.** The ideal is normal: the introduction says so (p. 173), and the
proof states that in $V^{\bar{\mathbb B}}$ the ideal $\mathcal J$ "is a normal
nontrivial ideal on $\omega_1$" (p. 175).

**Proof pointer.** Pages 174--176. Kunen's forcing is a two-step product
$\mathcal P\otimes\mathcal Q$, with $\mathcal P$ of size $\kappa$ and the
$\kappa$-chain condition and $\mathcal Q$ of size $\lambda$ and the
$\lambda$-chain condition, together with a regular embedding of it into
$j(\mathcal P)$ that fixes $\mathcal P$ and has a master code. Laver replaces
$\mathcal P$ by a $\kappa$-stage iteration $\bar{\mathcal P}\subseteq V_\kappa$
of Silver-type collapses with Easton supports, and $\mathcal Q$ by the collapse
$\mathcal E_{\kappa\lambda}$. A $\Delta$-system argument using the Mahloness of
$\kappa$ shows that for every $\beta<\kappa$, every $\kappa$ conditions of
$\bar{\mathcal P}$ include $\kappa$ of which any fewer than $\beta$ have a
common extension (the "$(\kappa,\kappa,<\beta)$-cc", p. 175). The same
argument, applied to $j(\bar{\mathcal P})$ in $M$, yields the
$(\aleph_2,\aleph_2,\aleph_0)$-saturation of $\mathcal J$. Not reconstructed
here.

**Read depth.** Claims checked: the definitions and statements of p. 173, the
proposition $\Phi$ with Kunen's clauses (a)--(c) on p. 174, and the assertions
on p. 175 that $\bar{\mathcal P}$ has the $(\kappa,\kappa,<\beta)$-cc, that
$2^\kappa=\lambda$ in $V^{\bar{\mathbb B}}$ and that $\mathcal J$ is a normal
nontrivial ideal on $\omega_1$, were read clause by clause on the page images.
The proof on pp. 174--176 was looked through on the page images and no step was
checked. Nothing here is independently reviewed.

**Dependencies.** External, and assumed by the proof: Kunen's construction and
his results on $\Phi$ (Saturated ideals, J. Symbolic Logic 43 (1978), 65--76,
the paper's [8]). The saturation notion comes from Laver, A saturation property
on ideals, Compositio Math. 36 (1978), 233--242 (the paper's [10]). Neither
has a card in the library.

**Bears on.**

- [[../wiki/problems/set_theory/E1172/_index|#1172]]: the model has
  $2^{\aleph_0}=\aleph_1$, $2^{\aleph_1}=\aleph_2$ and a normal
  $(\aleph_2,\aleph_2,\aleph_0)$-saturated ideal on $\omega_1$, so by the
  [[set_theory/laver_1982_saturated_ideal_omega1/theorem_p177|§ 3 theorem]] it
  satisfies $\omega_2\to(\omega_1+\omega)^2_2$, a one-line deduction made
  here; the paper does not state that GCH holds in it, which the problem's
  consistency question requires.
- [[../wiki/problems/set_theory/E1170/_index|#1170]]: by the same theorem the
  model satisfies $\omega_2\to(\alpha)^2_2$ for every
  $\alpha\le\omega_1+\omega_1+1$, again a deduction made here; the paper says
  nothing about the larger $\alpha<\omega_2$ that the problem also asks about.
