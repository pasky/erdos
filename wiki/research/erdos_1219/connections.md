---
name: research/erdos_1219/connections
title: "Connections: what the canonization proofs give elsewhere"
desc: |
  Assesses, target by target, what the reconstructed Canonization Lemma and
  the block-to-cofinality reduction of Theorem 1.2 give for other
  erdosproblems.com problems: the exact dividing line behind Problem 1219, the
  strong-limit transfer and the type-count obstruction for Problem 1220, the
  reduction of Hajnal's triple conjecture to a canonization statement with its
  gaps, and the reasons the mechanism does not reach Problems 1218 and 1167.
created: 2026-09-28T08:01:38Z
updated: 2026-10-19T04:19:07Z
---

[[research/erdos_1219/_index|..]]

***

**Standings of two targets.** Two passages below differ from the standings that
the problem pages record. The section on Problem 1220 treats the problem as open
and leaves the
reported counterexample of Shelah and Stanley [170] to a status search; the
problem page reads their Theorem 3, a consistent failure of the relation at
$\aleph_{\mathfrak c^+}$, which meets both hypotheses in ZFC, accepts it as
[[problems/set_theory/E1220/claims/1987_01_01_shelah_stanley|the not-provable side]]
and, with the positive answer of Erdős, Hajnal and Rado under GCH as the
not-disprovable side, records the problem as independent; the strong-limit
transfer and the type-count obstruction of that section are unaffected. The
paragraph on the two wordings in the section on Problem 1218 takes the page's
statement to be the earlier wording, with first target $\aleph_{\beta+1}$; the
problem page states the corrected relation, with first target $\aleph_\beta$,
which erdosproblems.com adopted on 7 September 2026 to fix a transcription
error, and rejects [[problems/set_theory/E1218/claims/2026_09_02_li|Li's claim]]
because it answers only the earlier wording, whose relation is a theorem of
Erdős, Hajnal and Rado. The implication from Problem 1167 recorded in that
section concerns the corrected relation and stands.

**Scope.** This page carries the mechanism reconstructed in
[[research/erdos_1219/lemma_1_1_reconstruction|Lemma 1.1]] (canonization by
types on fast-growing blocks) and
[[research/erdos_1219/theorem_1_2_reconstruction|Theorem 1.2]] (the reduction
of a coloring of pairs on $\sum_{\mu<\lambda}2^\mu$ to a coloring of pairs on
$\operatorname{cf}\lambda$), specialized in
[[research/erdos_1219/corollary_1_3_reconstruction|Corollary 1.3]] to
Problem 1219, to the other problems that use the same objects, and records
for each what the transfer gives, what it does not give, and why. Every
statement here is author-recorded, no problem status changes, and no tier is
assigned. The statements
were independently reviewed as they stood on 2026-09-28T13:50:48Z
by seven focused reviews graded in
[[research/erdos_1219/evidence/verify/connections_grade|the connections grade]],
which passes all seven and accepts fourteen corrections, since applied. Since
the review, the Target paragraph of the Problem 1219 section and the Conjecture
1A section's reference to the problem page's search were restated against the
current problem page without dates; this touches no examined statement, proof,
code or input. Sources are cited at the standing their library pages record; the
survey of
[[../library/set_theory/komjath_2025_erdos_hajnal_problem_list/_index|Komjáth 2025]]
is read from its held conversion, and reading outside the held corpus is
limited to the erdosproblems.com pages named in each section.
Notation is that of the theorem page: $\theta\to(\mu_0,\ldots,\mu_{k-1})^r$
for cardinals, $(\rho)_\gamma$ for $\gamma$ repetitions of the target
$\rho$, and $\chi=\sum_{\mu<\lambda}2^\mu$. A *block decomposition* of a set
$X$ is a partition $X=\bigsqcup_{i<\kappa}X_i$ into $\kappa$ pieces.

## Tools

Three facts are used below. The first restates what Theorem 1.2's proof
consumes from the lemma, so that later sections can apply it without
repeating the verification; the other two are recorded here with their
proofs.

**(T1) The lemma's interface.** Let $\kappa$ be an infinite regular
cardinal, let $\mu(i)$ ($i<\kappa$) be infinite cardinals, strictly
increasing, with $\mu(0)\ge\kappa$ and $2^{\mu(i)}$ strictly increasing, let
$\lambda_i=(2^{\mu(i)})^+$, let $A_i$ be pairwise disjoint sets with
$|A_i|=\lambda_i$, and let $F:A^n\to2$ be a function of finitely many places
on $A=\bigcup_iA_i$. Then Lemma 1.1 applies with its $\chi=2$,
$F_0=F_1=F$, these $\lambda_i$, $\mu(i)$ and $A_i$, and any properties
$P_\alpha$ satisfying its realizability hypothesis (H): Step 2(a) and Step 5
of the theorem page verify the regularity and monotonicity of the
$\lambda_i$, the growth condition and $2^{2+\kappa}<\lambda_0$ from exactly
these assumptions (Step 5 uses $\mu(0)\ge\kappa$, $|j|\le\mu(j)$, the strict
increase of the powers and the infinitude of each $\mu(i)$, and nothing
about $\lambda$). Its conclusion gives $a^*_i\in A_i$ and $B_i\subseteq A_i$
with $|B_i|\le\mu(i)$, clauses (1A), (1B) and (2), and for two-place $F$ the
canonical form $F(b,c)=F(b',c')$ for $b,b'\in B_\alpha$, $c,c'\in B_\beta$,
$\alpha<\beta$, as in Step 6.

**(T2) Composition with a witness at the cofinality.** Let $\lambda$ be a
singular cardinal, $\kappa=\operatorname{cf}\lambda$, $\gamma\ge1$, and let
$\rho_\nu\ge2$ ($\nu<\gamma$) be cardinals with
$\kappa\not\to(\kappa,(\rho_\nu)_{\nu<\gamma})^2$. Then
$\lambda\not\to(\lambda,(\rho_\nu)_{\nu<\gamma})^2$.

*Proof.* Fix a witness $c:[\kappa]^2\to1+\gamma$ and a block decomposition
$\lambda=\bigsqcup_{i<\kappa}X_i$ with $|X_i|<\lambda$. Color a pair inside
one $X_i$ with $0$ and a pair $\{x,y\}$ with $x\in X_i$, $y\in X_j$, $i\ne j$,
with $c(\{i,j\})$. Let $H$ be homogeneous in color $0$ with $|H|=\lambda$ and
$J=\{i:H\cap X_i\ne\emptyset\}$. If $|J|<\kappa$ then $J$ is bounded in the
regular $\kappa$, so $H$ lies in fewer than $\operatorname{cf}\lambda$ sets
of size less than $\lambda$ and $|H|<\lambda$; hence $|J|=\kappa$, and $J$ is
$c$-homogeneous in color $0$, a contradiction. Let $H$ be homogeneous in a
color $1+\nu$ with $|H|=\rho_\nu$. Pairs inside a block have color $0$, so
$H$ meets each block in at most one point, $|J|=\rho_\nu$, and $J$ is
$c$-homogeneous in color $1+\nu$, a contradiction. $\square$

The case $\gamma=1$, $\rho_0=\aleph_1$ is the necessity remark Komjáth
prints under Problem 4 (p. 419); the case $\gamma=\aleph_0$, $\rho_\nu=3$ is
used for Problem 1218 below.

**(T3) The converse of Theorem 1.2 at the cofinality.** Let $\lambda$ be
singular with $\kappa=\operatorname{cf}\lambda$, suppose
$\langle2^\mu:\mu<\lambda\rangle$ is not eventually constant, and suppose
$\kappa\not\to(\kappa)^2_2$. Then $\chi\not\to(\lambda)^2_2$.

*Proof.* Choose cardinals $\mu(i)<\lambda$ ($i<\kappa$), strictly increasing and
cofinal in $\lambda$, with $2^{\mu(i)}$ strictly increasing; Step 1 of the
theorem page does this from the non-constancy alone, the bound $\mu_0$ being
unnecessary here. Since $2^\mu\ge\mu^+$, the powers are cofinal in $\lambda$, so
$\sup_{\mu<\lambda}2^\mu\ge\lambda$ and, by the sum formula of the theorem page,
$\chi=\sup_{\mu<\lambda}2^\mu=\sup_i2^{\mu(i)}=\sum_{i<\kappa}2^{\mu(i)}$, the
last step because the sum has $\kappa$ terms with supremum at least $\kappa$.
Take a block decomposition $\chi=\bigsqcup_{i<\kappa}X_i$ with
$|X_i|=2^{\mu(i)}$, on each $X_i$ a Sierpiński coloring $e_i$ of $[X_i]^2$ with
no homogeneous set of size $\mu(i)^+$ ((S) on the theorem page), and a witness
$c$ for $\kappa\not\to(\kappa)^2_2$; color a pair inside $X_i$ by $e_i$ and a
pair across blocks $i\ne j$ by $c(\{i,j\})$. Let $H$ be homogeneous in a color
$\nu$ with $|H|=\lambda$, and $J$ as before. Each $H\cap X_i$ is
$e_i$-homogeneous, so $|H\cap X_i|\le\mu(i)$. If $|J|<\kappa$, then $J$ is
bounded by some $i_0<\kappa$ and
$|H|\le\sum_{i<i_0}\mu(i)\le|i_0|\cdot\mu(i_0)<\lambda$, since $\lambda$ is a
limit cardinal; so $|J|=\kappa$, and choosing one point of $H$ in each block of
$J$ shows that $J$ is $c$-homogeneous in color $\nu$, a contradiction. $\square$

## Problem 1219 beyond the catalog question

**Target.** [[problems/set_theory/E1219/_index|Problem 1219]] (status `solved`,
claim `proved`; its Current assessment rests on Corollary 1.3, with Komjáth's
survey as the acceptance record). Its Known Results record, from
erdosproblems.com and not from a held source, that with $\aleph_\kappa$ in place
of $\aleph_\omega$ the answer is yes for $\kappa<\omega$ and no for
$\kappa>\omega$; and they record Hajnal's Conjecture 1A as a separate open
question, treated in its own section below.

**What transfers.** Theorem 1.2 is already the general form, and (T3) is
its converse at the cofinality. Together with two classical facts they give
the exact dividing line (author-recorded): *for a singular cardinal
$\lambda$,*

$$
\sum_{\mu<\lambda}2^\mu\to(\lambda)^2_2
\iff
\begin{cases}
2^\mu\ge\lambda\text{ for some }\mu<\lambda,\\
\langle2^\mu:\mu<\lambda\rangle\text{ is not eventually constant, and}\\
\operatorname{cf}\lambda\to(\operatorname{cf}\lambda)^2_2 .
\end{cases}
$$

The direction from right to left is Theorem 1.2: the first condition is
"eventually $\ge\lambda$", since $\mu\mapsto2^\mu$ is nondecreasing. For the
other direction: if $2^\mu<\lambda$ for every $\mu<\lambda$, then
$\chi=\lambda$ by the sum formula, and $\lambda\not\to(\lambda)^2_2$ for
every singular $\lambda$ (color a pair by whether its points lie in the
same piece of a block decomposition into $\operatorname{cf}\lambda$ pieces
of size below $\lambda$, the coloring on
[[../library/set_theory/shelah_1975_notes_partition_calculus/theorem_1_2|the theorem's result page]]);
if the powers are eventually constant with value $2^{\mu_0}\ge\lambda$,
then $\chi=2^{\mu_0}$ and Sierpiński's $2^{\mu_0}\not\to(\mu_0^+)^2_2$ with
$\mu_0^+\le\lambda$ gives $\chi\not\to(\lambda)^2_2$; and if the first two
conditions hold but the third fails, (T3) applies. Since an uncountable
regular $\kappa$ satisfies $\kappa\to(\kappa)^2_2$ exactly when it is
weakly compact, the third condition says that $\operatorname{cf}\lambda$ is
$\omega$ or weakly compact. In particular
$\sum_{\mu<\aleph_{\omega_1}}2^\mu\not\to(\aleph_{\omega_1})^2_2$ in ZFC,
whatever the powers do, while for $\lambda=\aleph_{\omega+\omega}$, of
countable cofinality, the relation holds exactly when the sequence
$\langle2^{\aleph_{\omega+n}}:n<\omega\rangle$ is not eventually constant and
some $2^{\aleph_{\omega+n}}$ is at least $\lambda$ (then above it, since
$\operatorname{cf}2^\mu>\mu\ge\aleph_0=\operatorname{cf}\lambda$); in the form
Bloom's catalog prints the problem, with $\aleph_\kappa$ in place of
$\aleph_\omega$, the sum $\sum_k2^{\aleph_{n_k}}$ keeps its integer indices and
the erdosproblems.com bullet is a theorem of ZFC on both sides: for
$\kappa>\omega$, blocks of size $2^{\aleph_{n_k}}$ carrying Sierpiński
colorings, with one color across blocks, admit no homogeneous set of size
$\aleph_{\omega+1}$ (a homogeneous set in the across-block color meets each
block in at most $\aleph_{n_k}$ points, so has size at most $\aleph_\omega$; one
in the other color lies inside one block), so
$\sum_k2^{\aleph_{n_k}}\not\to(\aleph_{\omega+1})^2_2$ whatever the powers are;
for $\kappa<\omega$, the relation (ER) of the theorem page at a block with
$n_k\ge\kappa$ gives $(2^{\aleph_{n_k}})^+\to(\aleph_{n_k+1})^2_2$ with
$\aleph_{n_k+1}>\aleph_\kappa$ and
$(2^{\aleph_{n_k}})^+\le\sum_k2^{\aleph_{n_k}}$. The characterization above
concerns the different sum $\sum_{\mu<\aleph_\kappa}2^\mu$, for which the answer
at $\kappa=\omega+\omega$ is yes under consistent cardinal arithmetic (for
instance $2^{\aleph_{\omega+n}}=\aleph_{\omega+\omega+n+1}$ for $1\le n<\omega$,
an Easton pattern) and no in ZFC at $\kappa=\omega_1$; the source
erdosproblems.com attributes the bullet to ([ErHa71], p. 20, not held) should be
read before the bullet is recorded in either form.

**Falsification checks.** (T3) carries the non-constancy hypothesis only to
match Theorem 1.2's: its proof takes the $\mu(i)$ from Step 1 but uses nothing
about the powers beyond $\sum_{i<\kappa}2^{\mu(i)}=\chi$, which the sum formula
gives for any strictly increasing cofinal $\langle\mu(i)\rangle$ of infinite
cardinals, since $\sup_i2^{\mu(i)}=\sup_{\mu<\lambda}2^\mu=\chi>\kappa$; so its
conclusion holds for every singular $\lambda$ with
$\operatorname{cf}\lambda\not\to(\operatorname{cf}\lambda)^2_2$, and when the
powers are eventually constant it also comes from Sierpiński alone, so the case
split loses nothing. The Sierpiński colorings are used at $\mu(i)^+\le\lambda$,
where they exclude homogeneous sets of size $\lambda$ inside a block, which is
the only place the argument differs from (T2). The regular case is outside this
page: for uncountable regular $\lambda$ the relation reduces to $\lambda$ weakly
compact (at $\lambda=\omega$ it is Ramsey's theorem) and is not touched by the
mechanism.

**Outcome.** Transfers, as a by-product: the converse (T3) and the
characterization above; no lead, since Problem 1219 is proved and the
characterization has no open case.

## Problem 1220: the singular unbalanced relation

**Target.** [[problems/set_theory/E1220/_index|Problem 1220]] (status `open`, no
compiled assessment) asks whether $\lambda\to(\lambda,\aleph_1)^2$ for every
singular $\lambda$ such that $\lambda$ and $\operatorname{cf}\lambda$ are
both $\aleph_0$-inaccessible, that is, $\mu^{\aleph_0}<\lambda$ for
$\mu<\lambda$ and likewise for $\operatorname{cf}\lambda$. It is Problem 4
of the Erdős--Hajnal list. Komjáth's commentary (pp. 419--420, read in the held
conversion) records: the hypotheses are necessary, by
$\tau^{\aleph_0}\not\to(\tau^+,\aleph_1)^2$ and by (T2); the simplest case is
$\lambda=\aleph_{\mathfrak c^+}$, where the hypothesis on
$\operatorname{cf}\lambda=\mathfrak c^+$ implies the one on $\lambda$ by a
theorem of Shelah, so that this $\lambda$ satisfies the hypotheses in ZFC; an
Erdős--Rado theorem ([45, Theorem 35.4] in the survey's numbering) gives the
positive relation when $\aleph_{\mathfrak c^+}$ is strong limit; Shelah and
Stanley ([170]) constructed a forcing that adds a counterexample to
$\aleph_{\mathfrak c^+}\to(\aleph_{\mathfrak c^+},\aleph_1)^2$ while preserving
the powers below a prescribed $\mu<\aleph_{\mathfrak c^+}$; and ([171]) from
$\mathfrak c^+$ measurable cardinals they obtained a model where
$\aleph_{\mathfrak c^+}$ is not strong limit and the relation holds. None of
[45], [170], [171] is held. If the summary of [170] is accurate, the universal
question, read as a question of ZFC, has a consistent negative answer at
$\lambda=\aleph_{\mathfrak c^+}$, and the erdosproblems.com label `open` should
be re-examined by a status search before anything is recorded on the problem
page. The erdosproblems.com page (accessed 2026-09-28; last edited 1 September
2026) states the problem, the necessity of the conditions and the simplest case,
and lists one proof claim in its forum, not read here.

**What transfers: the strong-limit case.** The mechanism reduces the
relation to its cofinality exactly when $\lambda$ is strong limit. The
transfer lemma (author-recorded):

*Let $\lambda$ be a singular strong limit cardinal,
$\kappa=\operatorname{cf}\lambda$, and $\theta\le\kappa$ a cardinal with
$\kappa\to(\kappa,\theta)^2$. Then $\lambda\to(\lambda,\theta)^2$.*

*Proof.* Let $f:[\lambda]^2\to2$ and suppose $f$ has no homogeneous set of
size $\theta$ in color $1$; a homogeneous set of size $\lambda$ in color
$0$ is to be found. Since $2^\mu\ge\mu^+$ for $\mu<\lambda$, the powers
below $\lambda$ are not eventually constant, so Step 1 of the theorem page,
run without its bound $\mu_0$, gives infinite cardinals $\mu(i)<\lambda$
($i<\kappa$), strictly increasing and cofinal in $\lambda$, with
$\mu(0)\ge\kappa$ and $2^{\mu(i)}$ strictly increasing. Put
$\lambda_i=(2^{\mu(i)})^+$; as $\lambda$ is strong limit, $\lambda_i<\lambda$,
and $\sum_{i<\kappa}\lambda_i=\lambda$ by the sum formula, so $\lambda$ has
a block decomposition $\bigsqcup_{i<\kappa}A_i$ with $|A_i|=\lambda_i$. For
$\alpha<\kappa$ let $P_\alpha$ say that $B_\alpha$ is homogeneous in color
$0$ with $|B_\alpha|=\mu(\alpha)$. (H) holds: for $C\subseteq A_\alpha$ with
$|C|=\lambda_\alpha$, the relation (ER) of the theorem page with
$\mu=\mu(\alpha)$, transported to $C$, gives a homogeneous set of size
$\lambda_\alpha$ in color $0$ or one of size $\mu(\alpha)^+\ge\kappa\ge\theta$
in color $1$; the second is excluded, and a subset of the first of size
$\mu(\alpha)$ serves. By (T1) with the two-place $\tilde f$ of Step 5, the
lemma gives $B_\alpha\subseteq A_\alpha$ with $|B_\alpha|=\mu(\alpha)$,
homogeneous in color $0$, and a well-defined $g:[\kappa]^2\to2$ with
$g(\{\alpha,\beta\})=f(\{b,c\})$ for $b\in B_\alpha$, $c\in B_\beta$,
$\alpha<\beta$. Apply $\kappa\to(\kappa,\theta)^2$ to $g$. If $I\subseteq\kappa$
with $|I|=\kappa$ is $g$-homogeneous in color $0$, then
$B=\bigcup_{\alpha\in I}B_\alpha$ is $f$-homogeneous in color $0$, by the
argument of Step 7, and $|B|=\sum_{\alpha\in I}\mu(\alpha)=\lambda$, as
there. If $J\subseteq\kappa$ with $|J|=\theta$ is $g$-homogeneous in color
$1$, choose $b_\alpha\in B_\alpha$ for $\alpha\in J$; distinct
$b_\alpha,b_\beta$ lie in distinct blocks and
$f(\{b_\alpha,b_\beta\})=g(\{\alpha,\beta\})=1$, so $\{b_\alpha:\alpha\in J\}$
is homogeneous in color $1$ of size $\theta$, which was excluded. $\square$

With $\theta=\aleph_1$: *if $\lambda$ is singular strong limit and
$\operatorname{cf}\lambda\to(\operatorname{cf}\lambda,\aleph_1)^2$, then
$\lambda\to(\lambda,\aleph_1)^2$*, and with (T2) the two relations are
equivalent for strong limit $\lambda$. For a regular $\aleph_0$-inaccessible
$\kappa$ the hypothesis $\kappa\to(\kappa,\aleph_1)^2$ is the Erdős--Rado
theorem for pairs (for successor $\kappa=a^+$ it is Theorem 7(i) of the held
[[../library/set_theory/erdos_1956_partition_calculus_set_theory/_index|Erdős and Rado (1956)]],
printed p. 432, PDF p. 6: $a^+\to(b,a^+)^2$ for the least $b$ with $a^b>a$, and
$a^{\aleph_0}=a$ forces $b\ge\aleph_1$; the regular limit case is not held; the
regular case is not what the problem asks), so the transfer lemma proves the
strong-limit case of the problem, whose instance
$\lambda=\aleph_{\mathfrak c^+}$ Komjáth attributes to [45, Theorem 35.4]; [45]
is not held, so how much of the case its theorem covers is not checked here, and
nothing new is claimed.

**What does not transfer, and why.** For $\lambda$ that is
$\aleph_0$-inaccessible but not strong limit, the mechanism is blocked at
its type count. The sets $B_i$ must have sizes $\mu(i)$ cofinal in
$\lambda$, so the parameter sets $E_\alpha=\bigcup_{i<\alpha}B_i$ have
sizes cofinal in $\lambda$; the number of types over $E_\alpha$ is
$2^{|E_\alpha|}$ in general (bound (A) on the lemma page), and the second
thinning needs it below the block size $\lambda_\alpha<\lambda$. If
$2^\mu\ge\lambda$ for some $\mu<\lambda$, then $2^{|E_\alpha|}\ge\lambda$
for every $\alpha$ with $|E_\alpha|\ge\mu$, and the count that the second
thinning of the lemma page uses no longer yields a fiber of size
$\lambda_\alpha$. Choosing the $\mu(i)$ below the least such $\mu$ keeps the
count but bounds $\sup_i\mu(i)<\lambda$, so the final set is too small. This is
an obstruction to the counting of Lemma 1.1 over full parameter sets, not to
canonization as such and not a proof of the negative relation; the consistent
counterexample of [170] and the consistent positive answer of [171] at a
non-strong-limit $\aleph_{\mathfrak c^+}$, both as reported by Komjáth, show
that the open part is not decided by cardinal arithmetic of this kind, and any
proof must use the $\aleph_0$-inaccessibility of $\lambda$ in a way that does
not pass through $2^{|E_\alpha|}$. The finite-color variant
$\lambda\to(\lambda,(\aleph_1)_k)^2$ would follow from a positive answer by the
color-merging induction of
[[research/erdos_1171/connections|the Problem 1171 connections page]], as that
page notes; it is not a route.

**Next investigation.** (i) Acquire Shelah and Stanley [170] and [171] and
record on the problem page what is proved: whether the model of [170]
keeps both $\aleph_0$-inaccessibility hypotheses, which decides whether the
universal question is independent of ZFC, and what [171] assumes. (ii) If
the question survives as a ZFC question for some class of $\lambda$, the
obstruction above says the proof cannot canonize over parameter sets of
size $\mu$ with $2^\mu\ge\lambda$; a positive outcome would need a
canonization that uses only countable parameter sets, which
$\aleph_0$-inaccessibility can count, and a negative outcome is a
counterexample of the [170] kind.

**Outcome.** Transfers to the strong-limit case, proved through the lemma from
the Erdős--Rado theorem for pairs at the cofinality; fails beyond it, with the
type-count obstruction; no lead, since the open part is exactly where the
mechanism is blocked and its status needs a source-level search first.

## Hajnal's Conjecture 1A: triples

**Target.** The stronger question recorded on Problem 1219's page and on
the paper's
[[../library/set_theory/shelah_1975_notes_partition_calculus/conjecture_1a|Conjecture 1A page]]:
under $\aleph_\omega<2^{\aleph_{n(0)}}<2^{\aleph_{n(1)}}<\cdots$,

$$
\chi=\sum_{n<\omega}2^{\aleph_n}\to(\aleph_\omega,4)^3 ,
$$

that is, every $f:[\chi]^3\to2$ has a homogeneous set of size
$\aleph_\omega$ in color $0$ or a homogeneous $4$-element set in color $1$.
Shelah's Remark (p. 1261) asserts $\chi\not\to(\aleph_\omega,5)^3$ without
proof; Komjáth (p. 419) records the conjecture as unproven; the search recorded
on the problem page found nothing later. It is not an
erdosproblems.com problem, and its status is not tracked by a problem page.

**What transfers: the endgame.** Keep the blocks $A_i$ ($i<\omega$) of
Step 2 of the theorem page for $\lambda=\aleph_\omega$, with
$|A_i|=\lambda_i=(2^{\mu(i)})^+$ and the $\mu(i)$ of Step 1, so that
$\chi=\bigsqcup_iA_i$. For a triple $\{x,y,z\}$ meeting the blocks
$i\le j\le k$ call $(i,j,k)$ its pattern. The mechanism's final step, the
Ramsey argument on canonical values, survives the passage to triples in the
following form. Say that $f$ satisfies the *canonization statement* (C)
when there are sets $S_i,T_i\subseteq A_i$ ($i<\omega$) with
$|S_i|=\mu(i)$, $f$ constantly $0$ on $[S_i]^3$, $T_i$ a triple with
$f(T_i)=1$, such that with $B_i=S_i\cup T_i$:

- (P1) for $i<j<k$, $f(\{a,b,c\})$ takes one value $g(i,j,k)$ for all
  $a\in S_i$, $b\in S_j$, $c\in S_k$;
- (P2) for $i<j$, $f(\{a,a',b\})$ takes one value $h_2(i,j)$ for all
  $\{a,a'\}\in[B_i]^2$ and $b\in B_j$;
- (P3) for $i<j$, $f(\{a,b,b'\})$ takes one value $h_1(i,j)$ for all $a\in S_i$
  and $\{b,b'\}\in[B_j]^2$.

*Endgame lemma* (author-recorded). *Suppose every $f:[\chi]^3\to2$ that
has no homogeneous $4$-set in color $1$ and no homogeneous set of size
$\aleph_\omega$ in color $0$ inside a single block satisfies (C). Then
Conjecture 1A holds.*

*Proof.* Let $f:[\chi]^3\to2$. If $f$ has a homogeneous $4$-set in color
$1$, or a block contains a homogeneous set of size $\aleph_\omega$ in color
$0$, there is nothing to prove; otherwise take $S_i,T_i,g,h_1,h_2$ from
(C). Ramsey's theorem for triples, $\omega\to(\omega)^3_2$, gives an
infinite $I\subseteq\omega$ on which $g$ is constant, say $\varepsilon$, and
Ramsey's theorem for pairs, applied twice, an infinite $I'\subseteq I$ on
which $h_1$ and $h_2$ are constant, say $\eta_1$ and $\eta_2$. Five cases,
the second of which is covered by the first and third.
If $\varepsilon=1$: one point of $S_i$ for each of four indices $i\in I'$
gives a $4$-set all of whose triples have pattern $(i,j,k)$ with $i<j<k$
and color $1$. If $\eta_1=\eta_2=1$: for $i<j$ in $I'$, two points of
$S_i$ and two of $S_j$ give a $4$-set whose triples have patterns $(i,i,j)$
and $(i,j,j)$, all of color $1$. If $\eta_2=1$ and $\varepsilon=0$: for
$i<j$ in $I'$, $T_i$ together with one point of $B_j$ is a $4$-set, its
triple $T_i$ of color $1$ and its other three triples of pattern $(i,i,j)$
and color $h_2(i,j)=1$. If $\eta_1=1$ and $\varepsilon=0$: one point of $S_i$
together with $T_j$, by (P3) at the pairs of $T_j$. In the remaining case
$\varepsilon=\eta_1=\eta_2=0$, and $B=\bigcup_{i\in I'}S_i$ is homogeneous in
color $0$: a triple inside one $S_i$ has color $0$ by the choice of $S_i$, and
the other triples have patterns $(i,i,j)$, $(i,j,j)$ or $(i,j,k)$ with values
$\eta_2$, $\eta_1$, $\varepsilon$. As $I'$ is infinite,
$|B|=\sum_{i\in I'}\mu(i)=\aleph_\omega$ as in Step 7. $\square$

The triples $T_i$ enter only through the two mixed cases; they are what
the hypothesis "no color-$0$ set of size $\aleph_\omega$ inside a block"
buys, since under it every subset of $A_i$ of size $\lambda_i>\aleph_\omega$
contains a triple of color $1$. The coloring that gives color $1$ exactly
to the triples of pattern $(i,i,j)$, $i<j$, has no homogeneous $4$-set in
color $1$, and its homogeneous sets of size $\aleph_\omega$ in color $0$
lie, up to finitely many points, inside a single block; it shows that the
case $\eta_2=1$, $\varepsilon=0$ cannot be handled without the $T_i$.

**What the lemma gives toward (C).** Apply (T1) with the three-place
$\tilde f$ extending $f$ symmetrically (and by $0$ on tuples with a
repeated entry), with properties $P_i$ that realize $S_i$ and $T_i$
inside every full-size subset of $A_i$, as (H) realizes the two
homogeneous sets for pairs, with $(2^\mu)^+\to(\mu^+,4)^3$ in place of
(ER), together with whatever (P2) turns out to need. Then:

- (P1) up to its lowest point. By (1B) with $\bar a=(a)$, for $i<j<k$,
  $a\in B_i$, $b,b'\in B_j$, $c,c'\in B_k$: $f(\{a,b,c\})=f(\{a,b',c'\})$.
  The dependence on $a$ is what clause (3) removes, by passing to a fiber of
  $a\mapsto\langle f(\{a,b,c\}):i<j<k\rangle$ inside $S_i$, a map with at
  most $2^{\aleph_0}$ values; the fiber has size $\mu(i)$ when
  $2^{\aleph_0}<\mu(i)$, the reading of the hypothesis
  $2^{\chi+\kappa}<\operatorname{cf}\mu(i)$ here. That can be arranged, by
  starting Step 1 above $2^{\aleph_0}$, exactly when
  $2^{\aleph_0}<\aleph_\omega$;
  the conjecture's hypothesis allows $2^{\aleph_0}>\aleph_\omega$, and then
  the fiber argument fails. Clause (3)'s heredity hypothesis fails for the
  property with $T_i$, since a same-size subset of $B_i$ may omit the
  triple; its fiber argument applies to $S_i$ alone, with $T_i$ kept, since
  (P1) is asked on the $S_i$.
- (P2) up to the pair. By (1A) at $j$ with $\bar a=(a,a')$ and the first
  thinning of the lemma page, which gives $b$ and $a^*_j$ the same type over
  $E_j$, $f(\{a,a',b\})=f(\{a,a',a^*_j\})$ for $b\in B_j$; so (P2)
  says that $c_i(\{a,a'\})=\langle f(\{a,a',a^*_j\}):j>i\rangle$, a
  coloring of $[B_i]^2$ with at most $2^{\aleph_0}$ colors, is constant on
  $[B_i]^2$. The lemma's thinnings fix the types of single elements over
  $D_i$ and never look at two elements of one block, so this must be built
  into $P_i$ and realized inside every $C\subseteq A_i$ of size
  $\lambda_i$. The Erdős--Rado relation $(2^\mu)^+\to(\mu^+)^2_\mu$
  (Theorem 39(i) of the held Erdős and Rado (1956) with $r=1$) gives, when
  $2^{\aleph_0}\le\mu(i)$, a $c_i$-homogeneous
  $C'\subseteq C$ of size $\mu(i)^+$, inside which the relation
  $(2^\mu)^+\to(\mu^+,4)^3$ helps no further (it applies only when
  $\mu(i)=2^\nu$ for some $\nu$, and then $2^\nu<\aleph_\omega\le2^{\mu_0}$
  gives $\nu^+\le\mu_0<\mu(i)$, so it yields a color-$0$ set of size
  $\nu^+<\mu(i)$ only), and inside which a color-$1$ triple is not guaranteed,
  because $|C'|<\lambda_i$; a $c_i$-homogeneous set of size $\lambda_i$ cannot
  be asked, as $\lambda_i$ is a successor cardinal. So (P2) needs a block
  statement of its own: in every $C\subseteq A_i$ of size $\lambda_i$, for the
  coloring $c_i$ induced by $f$ against any choice of higher points, jointly
  with the coloring $d_i$ of the (P3) bullet, a set $S\cup T$ as in (C) on
  which that coloring is constant, or a homogeneous $4$-set of $f$ in
  color $1$. Open here.
- (P3) not at all. With $\{b,b'\}\subseteq B_j$ and $a\in E_j$, neither
  $b$ nor $b'$ is a parameter of the other's type, and no clause of the
  lemma relates $f(\{a,b,b'\})$ to anything. (P3) implies that the
  restriction of $d_j(\{b,b'\})=\langle f(\{a,b,b'\}):a\in E_j\rangle$, a
  coloring of $[B_j]^2$ with at most $2^{|E_j|}=2^{\mu(j-1)}$ colors, to the
  coordinates $a\in\bigcup_{i<j}S_i$ is constant, and asks in addition that
  its common value $v_j$ be constant on each $S_i$, $i<j$; the route needs
  the converse direction, constancy of all of $d_j$, which is what the
  lemma's property must realize.
  Constancy of $d_j$ alone does not give this: if $f(\{a,b,b'\})=\varphi(a)$ on
  every triple of pattern $(i,j,j)$ with $\varphi$ not constant on $S_i$, then
  $d_j$ is constant for every choice of $B_j$ while (P3) fails. Once every $d_j$
  is constant, the second demand follows by thinning each $S_i$ to a fiber of
  $a\mapsto\langle v_j(a):j>i\rangle$, a map with at most $2^{\aleph_0}$ values,
  taken jointly with the fiber of (P1) under the same hypothesis
  $2^{\aleph_0}<\mu(i)$; the values $v_j(a)$ do not change when the $S_j$ are
  thinned later. Here $2^{\mu(j-1)}\ge2^{\aleph_{n(0)}}>\aleph_\omega>\mu(j)$
  for every $j\ge1$, so the number of colors exceeds the target, and Erdős--Rado
  at the block size $\lambda_j=(2^{\mu(j)})^+$ would need
  $2^{\mu(j)}\ge2^{2^{\mu(j-1)}}$, a double-exponential growth the hypothesis
  does not supply; when $2^{\mu(j)}<2^{2^{\mu(j-1)}}$ there are colorings of
  $[\lambda_j]^2$ with $2^{\mu(j-1)}$ colors and no homogeneous triple
  ($2^\theta\not\to(3)^2_\theta$, as Komjáth notes under Problem 5). Making the
  earlier blocks smaller does not help, because the $\mu(i)$ must be cofinal in
  $\aleph_\omega$ while every $2^{\mu(i)}$ with $\mu(i)\ge\aleph_{n(0)}$ exceeds
  $\aleph_\omega$. Whether the particular $d_j$ induced by an $f$ without
  color-$1$ $4$-sets admits a homogeneous $S_j\cup T_j$ is the consequential
  gap.

**Falsification checks.** The endgame uses only the values on the $B_i$
and the two Ramsey theorems; its four cases are exhaustive, since
$(\varepsilon,\eta_1,\eta_2)\in\{0,1\}^3$ and every triple with a $1$ is
covered. The block sizes are those of Theorem 1.2, so (T1) applies
verbatim; the printed Remark after Lemma 1.1, that the lemma could be
refined along the lines of the paper's [7], § 5, may bear on (P3) and was
not read. The three-color form of Theorem 1.2 says nothing here: it adds a
color with target $\omega$ to pairs, while the conjecture raises the
exponent.

**Next investigation.** Attack (P3) first, since (P1) and (P2) reduce to
cardinal arithmetic under $2^{\aleph_0}<\aleph_\omega$ and a block
statement of Erdős--Rado type, while (P3) has no such reduction: decide
whether an $f$ without homogeneous $4$-sets in color $1$ forces the induced
pair colorings $d_j$ to have homogeneous sets of size $\mu(j)$ containing a
color-$1$ triple, in blocks of size $(2^{\mu(j)})^+$. A positive outcome for
the joint block statement, realizing inside every full-size subset of $A_j$ a
set $S_j\cup T_j$ on which both $d_j$ and the (P2) coloring $c_j$ are
constant, with the fiber step of the (P3) bullet that makes the common value
of each $d_j$ constant on the lower $S_i$, proves the conjecture under
$2^{\aleph_0}<\aleph_\omega$ by the endgame lemma; a negative outcome, a
coloring $f$ defeating (P3) in every choice of the sets $S_i,T_i$ in all of
the blocks, shows that (C) fails for this $f$ on these blocks, so the route
as formulated is closed, while a weaker canonical form or another
decomposition is not excluded;
its $f$ is a candidate for a counterexample to be tested against the conjecture
directly. In either case the imported inputs $(2^\mu)^+\to(\mu^+,4)^3$ and
$\omega\to(\omega)^3_2$ (Ramsey; Erdős, Hajnal and Rado 1965, neither held)
should be located on their pages before the route is built on.

**Outcome.** Transfers conditionally: the endgame lemma reduces the
conjecture to the canonization statement (C), of which the lemma supplies
(P1) under $2^{\aleph_0}<\aleph_\omega$ and half of (P2), and nothing of
(P3). Filed as the lead
triple canonization for Hajnal's conjecture.

## Problem 1218: the negative triple relation under GCH

**Target.** [[problems/set_theory/E1218/_index|Problem 1218]] (status `open`, no
compiled assessment) asks, under GCH and with $\beta=\omega_{\omega+1}$,
whether $\aleph_{\beta+1}\not\to(\aleph_{\beta+1},(4)_{\aleph_0})^3$; this
is the erdosproblems.com wording of 2026-09-04, which the page carries, and it
agrees with Komjáth's Problem 1 (p. 419),
$\lambda=\kappa_0=\aleph_{\omega_{\omega+1}+1}$. The erdosproblems.com page
(accessed 2026-09-28; last edited 7 September 2026) now prints
$\aleph_{\beta+1}\not\to(\aleph_\beta,(4)_{\aleph_0})^3$, with the first target
$\aleph_\beta$ rather than $\aleph_{\beta+1}$, states the general
Erdős--Hajnal--Rado conjecture

$$
\aleph_{\beta+1}\not\to(\aleph_\beta,(4)_{\aleph_{\operatorname{cr}(\beta)}})^3
$$

for ordinals $\beta$ with
$\beta>\operatorname{cf}\beta>\operatorname{cf}\beta-1>\operatorname{cr}\beta$,
with $\beta=\omega_{\omega+1}$ the least such ordinal (the page does not
define $\operatorname{cr}$), cites [EHR65, p. 131], and lists one comment
and one proof claim in its forum, not read here. The
two wordings are different relations: erdosproblems.com's current one is the
stronger negative statement, and it implies the page's by weakening the
first target. Which one the sources state is for the problem page's
status search to settle; both are addressed below.

**Why the mechanism fails.** The mechanism builds positive relations from
positive relations on blocks; the problem asks for a negative one. Even
for the positive relation that would refute it, the resource
$\aleph_{\beta+1}$ is a regular cardinal, so any block decomposition into
fewer than $\aleph_{\beta+1}$ pieces has a piece of full size, and the
block-to-cofinality reduction has nothing to reduce to; and Theorem 1.2's
$\chi$ at $\lambda=\aleph_\beta$ is, under GCH,
$\sum_{\gamma<\beta}\aleph_{\gamma+1}=\aleph_\beta$,
not $\aleph_{\beta+1}$, and its hypothesis "eventually $\ge\lambda$" fails.
The composition (T2) produces negative relations for pairs on singular
resources, which is the wrong exponent and the wrong resource. Nothing
here bears on the problem.

**Context recorded: the stepping-up instance.** Under GCH,
$\aleph_{\beta+1}=2^{\aleph_\beta}$, and the erdosproblems.com form of the
problem is the case $r=2$, $\lambda=\kappa_0=\aleph_\beta$, $\kappa_n=3$
($1\le n<\omega$) of the negative stepping-up implication that
[[problems/set_theory/E1167/_index|Problem 1167]] asks about, applied to the
relation $\aleph_\beta\not\to(\aleph_\beta,(3)_{\aleph_0})^2$. That relation
holds under GCH (author-recorded):
$\operatorname{cf}\aleph_\beta=\aleph_{\omega+1}$, and Komjáth's commentary on
Problem 5 (p. 420) records the theorem of [45, Section 20] that
$2^\lambda=\lambda^+$ implies
$\lambda^+\not\to(\lambda^+,(3)_{\operatorname{cf}\lambda})^2$ for singular
$\lambda$, which at $\lambda=\aleph_\omega$ gives
$\aleph_{\omega+1}\not\to(\aleph_{\omega+1},(3)_{\aleph_0})^2$ under GCH (the
GCH case of [[problems/set_theory/E1168/_index|Problem 1168]]); (T2) with
$\gamma=\aleph_0$ and $\rho_\nu=3$ lifts it to $\aleph_\beta$. So a positive
answer to Problem 1167 in its case $r=2$ with one singular target and the others
finite, the case its authors could not settle even under GCH per the
erdosproblems.com page of Problem 1167, would prove Problem 1218 in the
erdosproblems.com form and hence in the page's form; and a model of GCH in which
Problem 1218 fails in the erdosproblems.com form would refute Problem 1167. This
is a connection between two problems recorded from the survey, not a product of
the mechanism.

**Outcome.** Fails, with the regular-resource obstruction; the implication
from Problem 1167 is recorded for both problem pages; no lead.

## Problem 1167: the negative stepping-up lemma

**Target.** [[problems/set_theory/E1167/_index|Problem 1167]] (status `open`,
claim `none`; its current assessment judges the statement with the
conditions $\gamma\ge2$ and $\kappa_\alpha>r$ of the Erdős--Hajnal list) asks
whether $2^\lambda\to(\kappa_\alpha+1)^{r+1}_{\alpha<\gamma}$
implies $\lambda\to(\kappa_\alpha)^r_{\alpha<\gamma}$; the erdosproblems.com
page (accessed 2026-09-28; last edited 1 September 2026) lists the proved cases
from [EHMR84] and names $r=2$ with one singular $\kappa_\alpha$ and the others
finite as the difficult case. Komjáth prints it as Problem 2 with the same case
list (p. 419).

**What transfers.** Nothing. The mechanism proves positive relations on a
sum of powers from positive relations at the cofinality and on blocks of
size $(2^\mu)^+$; the stepping-up lemma relates a relation on $\lambda$ to
one on $2^\lambda$ with the exponent raised, and neither Theorem 1.2 nor
(T2) or (T3) changes the exponent. Two remarks locate the mechanism's
results relative to the problem. First, Theorem 1.2 and Hajnal's
conjecture sit next to the difficult case: for $\lambda=\aleph_n$ the
relation $\aleph_n\not\to(\aleph_\omega,3)^2$ is trivial, so the implication
asked would give $2^{\aleph_n}\not\to(\aleph_\omega,4)^3$ for every $n$; that
relation holds outright, from $2^{\aleph_n}\not\to(\aleph_{n+1},4)^3$
(author-recorded; a theorem of Erdős, Hajnal and Rado 1965, not held: order
${}^{\aleph_n}2$ lexicographically, fix a well-order of it, and color a triple
$1$ exactly when its lexicographic middle element is the well-order-least of the
three; in a color-$1$ four-element set the two middle elements would each
precede the other, and in a color-$0$ set of size $\aleph_{n+1}$ the elements
with at most $\aleph_n$ elements of the set below them, and likewise above,
number at most $\aleph_n$ each, since the lexicographic order carries no
monotone sequence of length $\aleph_{n+1}$, so the well-order-least of the
remaining elements has elements of the set on both sides; the derivation is
written out as Lemma B of
[[research/erdos_1219/evidence/verify/connections_problem_1167_the_negative_stepping_up_lemma_review|the section's review]]),
so this instance of the implication is settled, while Conjecture 1A asserts the
positive relation for the sum $\chi$ of these powers; the two are compatible, as
Sierpiński's $2^{\aleph_n}\not\to(\aleph_{n+1})^2_2$ is compatible with Shelah's
$\chi\to(\aleph_\omega)^2_2$, and a proof of the conjecture would show that the
sum of the powers behaves differently from each summand at exponent $3$ as well.
Second, the instance of the difficult case that is itself an erdosproblems.com
problem is Problem 1218, as the previous section records.

**Outcome.** Not applicable; the Problem 1218 instance is recorded; no
lead.

## Other relations in the set-theory folder

The mechanism needs a resource that is a union of $\operatorname{cf}\lambda$
blocks of regular sizes $(2^{\mu(i)})^+$ growing to the resource, a
coloring of pairs (or, with the gaps above, triples), and a positive
relation at the cofinality. It does not apply to
[[problems/set_theory/E1168/_index|Problem 1168]], a negative relation on the
regular cardinal $\aleph_{\omega+1}$, beyond the GCH remark in the Problem
1218 section, which uses (T2) at the singular $\aleph_\beta$ and not at
$\aleph_{\omega+1}$; nor to [[problems/set_theory/E0070/_index|Problem 70]], a relation
for triples with an ordinal target on the reals: (T1) passes to the lemma the
hypothesis $2^{\chi+\kappa}<\lambda_0\le|A|$, which puts every domain of the
lemma above $2^{\aleph_0}=|\mathbb R|$, and Theorem 1.2's resource exceeds
$2^{\mu(0)}\ge2^{\aleph_0}$, so no coloring of a set of size continuum is in the
mechanism's scope, while (T2) and (T3) produce negative relations for pairs and
bear on no positive relation for triples; nor to
[[problems/set_theory/E1170/_index|Problem 1170]] and
[[problems/set_theory/E1172/_index|Problem 1172]], balanced or ordinal-target relations
on the regular cardinals $\omega_2$ and $\omega_3$; nor to
[[problems/set_theory/E0598/_index|Problem 598]], which colors countable subsets rather
than finite tuples. The set mappings of
[[problems/set_theory/E0623/_index|Problem 623]] and
[[problems/set_theory/E1173/_index|Problem 1173]] live at $\aleph_\omega$ and
$\aleph_{\omega+1}$, but a free set is not a homogeneous set, and the type
canonization has no clause for them; their obstructions are on
the Problem 501 connections page. In the
other direction,
[[research/erdos_1171/connections|the Problem 1171 connections page]] records
that its color-merging induction does not apply to Problem 1219, a balanced
cardinal relation; the mechanism here is the one that proves that relation, and
the two are disjoint in what they consume.

## Outcomes

- Problem 1219: transfers, as by-products. The converse (T3) and the
  characterization: for singular $\lambda$,
  $\sum_{\mu<\lambda}2^\mu\to(\lambda)^2_2$ holds
  exactly when some $2^\mu\ge\lambda$, the powers are not eventually
  constant, and $\operatorname{cf}\lambda$ is $\omega$ or weakly compact.
- Problem 1220: transfers to the strong-limit case, proved from the Erdős--Rado
  theorem for pairs at the cofinality (the transfer lemma: strong limit singular
  $\lambda$ and $\operatorname{cf}\lambda\to(\operatorname{cf}\lambda,\theta)^2$
  with $\theta\le\operatorname{cf}\lambda$ give $\lambda\to(\lambda,\theta)^2$);
  fails for non-strong-limit $\lambda$, with the type-count obstruction; the
  survey's report of a consistent counterexample at $\aleph_{\mathfrak c^+}$ is
  flagged for the problem page's status search.
- Hajnal's Conjecture 1A (on Problem 1219's page): transfers
  conditionally. The endgame lemma reduces it to the canonization statement
  (C); the lemma gives (P1) under $2^{\aleph_0}<\aleph_\omega$ and half of
  (P2); (P3) is the gap. Lead filed.
- Problem 1218: fails, regular resource and wrong direction; the implication
  from the difficult case of Problem 1167 is recorded, with the GCH premise
  proved by (T2); the two erdosproblems.com wordings are flagged.
- Problem 1167: not applicable; the Problem 1218 instance is recorded.
- Problems 1168, 70, 1170, 1172, 598, 623 and 1173: not applicable.
