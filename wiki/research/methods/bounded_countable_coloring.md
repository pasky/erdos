---
name: research/methods/bounded_countable_coloring
title: From bounded countable colorings to cardinal-sized witnesses
desc: A domain bridge for the proposed negative model in Problem 598, with the forcing and positive-in-L imports kept explicit.
created: 2026-10-14T12:38:34Z
updated: 2026-10-14T12:38:34Z
---

***

[[problems/set_theory/E0598/_index|Problem 598]] concerns all countably
infinite subsets and witnesses of a prescribed cardinal size. The Magidor
relation in
[[../library/set_theory/garti_2019_first_omitting_cardinal_magidority/claim_1_10|Garti–Hayut Claim 1.10]]
instead concerns bounded countably infinite subsets of a singular cardinal.
The following author-recorded argument supplies the domain bridge. It does
not independently verify the forcing theorem or the other half of the
proposed independence result.

Let $\operatorname{cf}(\lambda)=\omega$ and let $\kappa<\lambda$ be
uncountable and regular. Suppose
$\lambda\to[\lambda]^{\aleph_0\text{-bd}}_\kappa$; the domain includes
all countable order types. For a coloring
$f:[\lambda]^{\aleph_0}\to\kappa$, restrict to bounded subsets and choose
$A\subseteq\lambda$ of size $\lambda$ and a color $i$ omitted there.
Choose an increasing cofinal sequence $(\lambda_n)_{n<\omega}$ in
$\lambda$. Some $A\cap\lambda_n$ has size at least $\kappa$, since
otherwise its countable union would have size below the uncountable regular
cardinal $\kappa$. Take $X\subseteq A\cap\lambda_n$ of size $\kappa$.
Every countable subset of $X$ is bounded in $\lambda$, so it omits $i$.
Consequently

$$
\lambda\to[\kappa]^{\aleph_0}_\kappa.
$$

Color monotonicity also needs no additional set theory. If the bounded
omitting relation holds with $\rho$ colors and $\rho\le\kappa$, compose
a $\kappa$-coloring with a surjection onto $\rho$. Omitting a
$\rho$-color omits its nonempty fiber of $\kappa$-colors.

In Claim 1.10(a) of arXiv:1801.00239v3, take $\beta=1$. The theorem starts
from I1 and produces a Magidor $\lambda$ with
$\alpha_M(\lambda)=\aleph_2$. Its proof first uses Prikry forcing at a
measurable $\mu<\lambda$, then a countably closed Lévy collapse. Using
the standard facts that these steps add no reals, and the theorem's
preservation of $\lambda$ as a limit cardinal, the final continuum is
below $\lambda$: the unchanged reals inject into the old ordinal
$\mu<\lambda$. Hence the final $\kappa=\mathfrak c^+$ is below
$\lambda$ and at least $\aleph_2$. Monotonicity and the domain bridge
give the desired negative instance at $m=\lambda$. No assumption of CH
is needed for this specialization.

The source introduction and Claim 1.10's proof paragraph supply the domain
convention and the two forcing steps. Preservation of Magidority, the
no-new-reals facts, and the supporting forcing lemmas remain imported
premises, not reconstructed proofs here. The independent scrutiny needed for
the whole conclusion is separate from checking this bridge.

For the positive-in-$L$ half,
[[problems/set_theory/E0598/claims/2026_05_24_wu|Wu's existing claim]]
uses a finite-subset coding and elementary-substructure equivalence followed
by a condensation-to-$0^\sharp$ theorem. Those textbook interfaces are
unverified in this note. Checking their exact hypotheses, and the final
cardinals in the negative model, is the next useful source test. A missing
model-theoretic hypothesis or forcing-preservation clause leaves the whole
independence conclusion conditional on that gap.
