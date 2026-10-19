---
name: set_theory/laver_1982_saturated_ideal_omega1/theorem_p177
title: "Theorem (p. 177): CH and a normal (ℵ₂, ℵ₂, ℵ₀)-saturated ideal on ω₁ give ω₂ → (ω₁ + ω₁ + 1, α)² for every α < ω₂"
desc: |
  Laver's § 3 theorem, proved in sketch, that 2^ℵ₀ = ℵ₁ and a normal
  (ℵ₂, ℵ₂, ℵ₀)-saturated ideal on ω₁ give ω₂ → (ω₁ + ω₁ + 1, α)^2 for every
  α < ω₂, so the model of § 1 satisfies ω₂ → (ω₁ + ω)^2_2.
created: 2026-10-14T22:55:45Z
updated: 2026-10-14T22:55:45Z
---

***

**Source.** Richard Laver, *An $(\aleph_2,\aleph_2,\aleph_0)$-saturated ideal
on $\omega_1$* (1982), § 3: the statement on p. 177, its announcement on
p. 173, and the sketch of proof on pp. 177--178. The edition is identified on
the [[set_theory/laver_1982_saturated_ideal_omega1/_index|source card]].

**Statement.** Assume $2^{\aleph_0}=\aleph_1$ and that there is a normal
$(\aleph_2,\aleph_2,\aleph_0)$-saturated $\omega_1$-ideal, in the sense defined
on [[set_theory/laver_1982_saturated_ideal_omega1/main_theorem|the main theorem's page]].
Then $\omega_2\to(\omega_1+\omega_1+1,\alpha)^2$ for every $\alpha<\omega_2$:
for every partition $[\omega_2]^2=R\cup G$ there is a set of order type
$\omega_1+\omega_1+1$ all of whose pairs lie in $R$, or a set of order type
$\alpha$ all of whose pairs lie in $G$.

The introduction's announcement (p. 173) omits the word normal; the statement
of § 3 (p. 177) has it, and the ideal built in § 1 is normal. The paper writes
$\omega_1+\omega_1+1$; Komjáth's survey and Problem 1172's page write
$\omega_1 2+1$, the same ordinal.

**Consequences.** With $\alpha=\omega_1+\omega$ the theorem gives
$\omega_2\to(\omega_1+\omega)^2_2$, since a set of order type
$\omega_1+\omega_1+1$ contains one of order type $\omega_1+\omega$; with
$\alpha=\omega_1+\omega_1+1$ it gives $\omega_2\to(\alpha)^2_2$ for every
$\alpha\le\omega_1+\omega_1+1$. The model of § 1 satisfies
$2^{\aleph_0}=\aleph_1$ (p. 173) and has a normal such ideal, so both relations
hold there, relative to the consistency of a huge cardinal. The introduction
places § 3 after recalling the question of Erdős and Hajnal (the paper's [3],
their 1971 problem list) whether $\omega_2\to(\omega_1+\omega)^2_2$ is
consistent (p. 173), but the paper does not state these consequences in words;
they are one-line deductions made here.

**Proof pointer.** Pages 177--178; the paper says "We just give a sketch
modulo familiar arguments". Fix $[\omega_2]^2=R\cup G$, and for a set
$B\subseteq\omega_2$ of order type $\omega_1$ copy the ideal to $B$ through the
order isomorphism with $\omega_1$. The cases are whether there are $\aleph_2$
sets $B_\alpha$ of order type $\omega_1$, placed one above another, with all
pairs inside each $B_\alpha$ in $R$, and such that for $\alpha<\beta$ a set in
the dual filter on $B_\alpha$ has all its pairs with $B_\beta$ in $G$. If there
are, a ramification argument builds, for each $\alpha<\omega_2$, a set of order
type $\alpha$ with all pairs in $G$. If not, the failed step of the
construction gives a set $B_\alpha$ of order type $\omega_1$ with all pairs in
$R$ and $\aleph_2$ points each joined in $R$ to a positive part of $B_\alpha$;
$(\aleph_2,\aleph_2,\aleph_0)$-saturation makes the countable intersections of
these parts positive, and a ramification argument extends $B_\alpha$ to a set
of order type $\omega_1+\omega_1+1$ with all pairs in $R$. Building the
$B_\alpha$ uses a ramification argument in the manner of Kurepa and of Erdős
and Rado, and a generalization of an argument of Galvin (credited to the
paper's [1], Baumgartner, Hajnal and Máté) that under $2^{\aleph_0}=\aleph_1$,
among any $\aleph_2$ sets in a normal filter on $\omega_1$ there are $\aleph_1$
whose intersection is in the filter. The paper adds that a forthcoming paper of
Kanamori will give a similar proof that
$\kappa^+\to(\kappa+\kappa+1,(\kappa:\kappa^+))^2$ for weakly compact
$\kappa$. Not reconstructed here.

**Read depth.** Claims checked: the statement on p. 177 and its announcement
on p. 173 were read clause by clause on the page images. The sketch on
pp. 177--178 was read on the page images and no step was checked; the sketch
itself leaves its ramification arguments to the reader. Nothing here is
independently reviewed.

**Dependencies.** For the consequences in a model:
[[set_theory/laver_1982_saturated_ideal_omega1/main_theorem|the main theorem]].
External: the Galvin argument as given by Baumgartner, Hajnal and Máté, Weak
saturation properties of ideals (Colloq. Math. Soc. János Bolyai 10, 1975,
137--158, the paper's [1]), and the ramification method of Kurepa (1952, [9])
and of Erdős and Rado
([[set_theory/erdos_1956_partition_calculus_set_theory/_index|A partition calculus in set theory]],
1956, [2]). The first two have no card in the library.

**Bears on.**

- [[../wiki/problems/set_theory/E1172/_index|#1172]]: in the model of § 1 the
  theorem gives $\omega_2\to(\omega_1+\omega)^2_2$ relative to a huge
  cardinal; that model satisfies $2^{\aleph_0}=\aleph_1$ and
  $2^{\aleph_1}=\aleph_2$, and the paper does not state that it satisfies GCH,
  which the problem's consistency question requires (see the main theorem's
  page).
- [[../wiki/problems/set_theory/E1170/_index|#1170]]: in the same model it
  gives $\omega_2\to(\alpha)^2_2$ for every $\alpha\le\omega_1+\omega_1+1$; the
  problem asks for every $\alpha<\omega_2$, which the paper does not address.
