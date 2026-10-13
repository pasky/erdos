---
name: diophantine_problems/openai_2026_hilberts_tenth_problem_rational_numbers
desc: |
  A 62-page release manuscript claiming a negative answer to Hilbert's tenth
  problem over Q: no algorithm decides whether an integer polynomial has a
  rational zero, with the number of variables part of the input, and the
  problem has Turing degree 0' even in degree at most four. It reduces integer
  solvability to finite rational tests through a rank-one elliptic curve and
  a five-point height bound, and names no Erdős problem.
license: Apache-2.0
created: 2026-10-12T23:13:55Z
updated: 2026-10-12T23:13:55Z
---

# diophantine_problems/openai_2026_hilberts_tenth_problem_rational_numbers

[[diophantine_problems/_index|..]]

[[diophantine_problems/openai_2026_hilberts_tenth_problem_rational_numbers/corollary_7_1|corollary_7_1]]: The manuscript's consequence of Theorem 1.1: rational solvability of
integer polynomials has the degree of the halting problem, and stays
undecidable for total degree at most four and for sums of squares of
quadratics. Claims checked only.

[[diophantine_problems/openai_2026_hilberts_tenth_problem_rational_numbers/theorem_1_1|theorem_1_1]]: The manuscript's main claim: Hilbert's tenth problem over Q has a negative
answer, by a Turing reduction of integer solvability to rational
solvability. Claims checked only.

[[diophantine_problems/openai_2026_hilberts_tenth_problem_rational_numbers/theorem_2_4|theorem_2_4]]: The manuscript's five-point height estimate: the Weil height of a rational
point of P^1 off five fixed rational points is at most H M^c, where M is the
product of the primes outside a fixed finite set at which the point meets
one of the five to odd order. Claims checked only.

***

OpenAI, *Hilbert's tenth problem over the rational numbers*, OpenAI Math Release
preprint, October 6, 2026. Released under the Apache License 2.0 at
<https://github.com/openai/math> (revision fd4aeeb2e), folder
`preprints/Hilberts-tenth-problem-over-the-rational-numbers-October-6-2026`; the
held PDF, `main.pdf` in the release, is retained as
[openai_2026_hilberts_tenth_problem_rational_numbers.pdf](openai_2026_hilberts_tenth_problem_rational_numbers.pdf),
and the release's TeX bundle in that folder (under `build/`) is the TeX source
cited on this card. The license term was read in the release's root `LICENSE`
file at that revision on 2026-10-12.

```bibtex
@misc{OAI:Hilberts-tenth-problem-over-the-rational-numbers-October-6-2026,
  author = {{OpenAI}},
  title = {{Hilbert's tenth problem over the rational numbers}},
  howpublished = {OpenAI Math Release preprint
                  \href{https://github.com/openai/math/blob/main/preprints/Hilberts-tenth-problem-over-the-rational-numbers-October-6-2026/main.pdf}{OAI:Hilberts-tenth-problem-over-the-rational-numbers-October-6-2026}},
  year = {2026}
}
```

The held PDF has 62 A4 pages with a text layer; its title page is dated
October 6, 2026. Its metadata records the title and the author "OpenAI" but
no creation date, since the TeX source suppresses it (`\pdfinfoomitdate=1`).
The TeX source is `build/main.tex` (81 lines), which inputs seven section
files under `build/sections/` (4,184 lines in all: `01-introduction.tex` 250,
`02-reduction.tex` 888, `03-parity.tex` 718, `04-height.tex` 1,326,
`05-elliptic.tex` 189, `06-primes.tex` 705, `07-consequences.tex` 108), the
figure file `build/figures/reduction-overview.tex` (60 lines) and the
bibliography `build/references/references.bib` (86 entries, of which the PDF
prints the 74 cited).

**Attestation.** The release README at this revision says the repository
holds manuscripts "produced by an internal OpenAI model", that "Some outputs
build upon earlier results produced by the models", that the collection
"includes results at different stages of verification", that "Not all have
accompanying Lean formalizations" and that "Some of the unformalized results
could have issues". Its account of the method says that "The vast majority of
results were obtained with the same procedure using an unreleased internal
OpenAI model"; the exceptions it names concern a zero-free region for the
Riemann zeta function and the Hodge conjecture for CM abelian varieties, and
it does not say whether any other manuscript is an exception. The
manuscript's own README carries the title, the author line "OpenAI", the date
and the citation block, with a version note saying that this version "updates
citations to revised manuscripts in this collection"; it adds no sentence
about authorship or assistance. The title page names OpenAI as the sole
author, and the TeX source carries no statement on how the manuscript was
produced. These are the source's own statements, recorded as attestations and
not as this corpus's review. No refereed publication, arXiv version or
independent review of the manuscript is recorded here, and nothing on this
card is independently reviewed.

**Formalization.** The release's Lean catalog (`lean/formalization.yaml`) at
revision fd4aeeb2e lists no formalization of this manuscript, and its family
has no page under `lean/docs/`; nothing here is a formal proof of any
statement.

**Companions.** The release pairs this manuscript with *A
pointwise 2-converse for elliptic curves with rational two-torsion* (October 7,
2026, with an earlier dated version of September 24, 2026), whose abstract
claims that an elliptic curve over $\mathbb Q$ with a nonzero rational
two-torsion point and $2^\infty$-Selmer corank $0$ or $1$ has analytic and
Mordell--Weil rank equal to that corank and a finite Tate--Shafarevich group;
its finiteness statement is the input to Lemma 3.4 here. It is not held in this
library, so it is not linked. The release also holds an earlier dated
version of this manuscript, *Hilbert's tenth problem over the rational
numbers* (September 24, 2026, folder
`preprints/Hilberts-tenth-problem-over-the-rational-numbers-September-24-2026`,
62 pages); a comparison of the two TeX bundles at the release revision shows
that they differ only in the title-page date and in three bibliography links,
which the earlier version points at the earlier dated versions of the three
cited release manuscripts, so labels, statements and proofs agree. Outside the
family, the modularity step of Section 4 cites Theorem 1.1 of the release
manuscript *Fontaine--Mazur modularity at the prime 2* (October 6, 2026), filed
at
[[number_theory/openai_2026_fontaine_mazur_modularity_prime_2/_index|the Fontaine--Mazur card]],
and Remark 3.5 names Theorem 1.1 of *Goldfeld's analytic density conjecture and
the 2-converse for elliptic curves* (October 7, 2026) as an alternative input to
Lemma 3.4; that manuscript is not held here. The companions' arguments were not
read for this card.

Read status: claims checked for Theorem 1.1
(`build/sections/01-introduction.tex`, label `thm:main`, lines 7--11),
Theorem 2.4 with Corollary 2.5
(`build/sections/02-reduction.tex`, labels `hei:height`, lines 232--248, and
`hei:enlarge-exceptions`, lines 270--279) and Corollary 7.1
(`build/sections/07-consequences.tex`, label `thm:degree-normal-form`, lines
8--23), together with the statements of Propositions 2.1 and 2.2, Lemma
2.3, Corollary 2.6, Lemma 2.7, Proposition 2.8, Lemmas 2.9 and 2.10 and
Propositions 2.11 and 2.12 (`02-reduction.tex` lines 27--34, 109--127,
143--175, 294--322, 435--438, 477--486, 545--553, 643--654, 722--733 and
755--759, in that order), Lemmas 3.3--3.4 (`03-parity.tex` lines
300--315 and 464--468) and Lemma 6.1 (`06-primes.tex` lines 21--40), read
clause by clause on 2026-10-12. The proofs were read for their structure
only and no step was checked; nothing here is independently reviewed.

## Contents

Within each section all numbered statements, remarks included, share one
counter; the numbers below are the PDF's, and its printed page numbers agree
with the PDF page numbers.

- Section 1, Introduction (pp. 3--6; `01-introduction.tex`). States
  [[diophantine_problems/openai_2026_hilberts_tenth_problem_rational_numbers/theorem_1_1|Theorem 1.1]]
  (p. 3). The historical setting (pp. 3--5) recalls Hilbert's problem, the
  Davis--Putnam--Robinson--Matiyasevich theorem, and two sufficient routes to
  undecidability over $\mathbb Q$ that the manuscript says it does not need:
  an existential definition of $\mathbb Z$ in $\mathbb Q$, and a Diophantine
  model of integer arithmetic (Cornelissen and Zahidi 2000). It reviews
  Julia Robinson's first-order definition (1949), Poonen's definition with
  two universal and then seven existential quantifiers (2009) and
  Koenigsmann's universal one (2016); Mazur's conjecture on the topology of
  rational points (1995), which would rule out such definitions and models
  but, the text says, not undecidability itself;
  Poonen's large subrings $\mathbb Z[S^{-1}]$ (2003) and the Turing
  equivalences of Eisenträger, Miller, Park and Shlapentokh (2017); Poonen's
  rank-one transfer between rings of integers (2002), the route of Mazur and
  Rubin conditional on the conjectured evenness of
  $\dim_{\mathbb F_2}\mathrm{Sha}[2]$ (2010), and the unconditional
  results for rings of integers of number fields of Koymans and Pagano (2026)
  and of Alpöge, Bhargava, Ho and Shnidman (2026), which the text notes
  concern finitely generated $\mathbb Z$-algebras and not $\mathbb Q$; the
  elliptic divisibility approach of Cornelissen and Zahidi (2007), and the
  undecidability of Garcia-Fritz, Pasten and Vidaux (2025) in a language
  enlarged by height comparisons. The proof strategy (pp. 5--6) sketches
  the argument outlined on the Theorem 1.1 page and names the two release
  manuscripts used: the pointwise 2-converse in Section 3 and the
  Fontaine--Mazur theorem at $2$ in Section 4.
- Section 2, Finite rational tests for integer solvability (pp. 6--17;
  `02-reduction.tex`). Fixes $F=\mathbb Q(\sqrt2)$, $d=75-53\sqrt2$ and
  $E:y^2=x^3-d^2x$. Proposition 2.1 (p. 7): $E(F)$ has rank one, so
  $mE(F)=\mathbb ZP$ for some $m\ge1$ and a nontorsion $P$. For a
  characteristic-zero domain $R$ with $\sqrt2\notin\operatorname{Frac}R$ it
  states the point axioms ($T_0=O$, $T_1=P$, $T_{a+a'}=T_a+T_{a'}$,
  $T_a\in mE(F_R)$, and $T_a$ finite with $xy\ne0$ for $a\ne0$) and, inside
  an elementary extension of the many-sorted structure carrying $\mathbb Q$,
  $\mathbb Z$, $\mathbb R$, $F$, valuations, heights and elliptic multiples,
  defines the index map $\eta$ by $\widetilde T_a=\eta(a)P$, which is
  additive and injective but not assumed multiplicative. With $z=-x/y$ and
  the truncated formal logarithm $\ell_K$, Proposition 2.2 (p. 8) gives a
  finite set $S_E$ outside which $z$-valuations read off index ratios and
  truncated-logarithm ratios approximate integral index ratios to order $K$,
  on $E$ and on its conjugate $E^\sigma$. Lemma 2.3 (local comparison, p. 8):
  at an ambient prime $q\notin S_E$, $q>K+1$, a primary test on $E$ and an
  alternate test on $E^\sigma$, with auxiliary $h,j_0$ fixed for all $a$,
  force every embedded $\widetilde a$ to be $q$-integral with
  $\widetilde a\equiv\eta(a)\pmod{q^K}$. The section then states
  [[diophantine_problems/openai_2026_hilberts_tenth_problem_rational_numbers/theorem_2_4|Theorem 2.4]]
  (the five-point height estimate, p. 9) with Corollary 2.5 (p. 10), and
  Corollary 2.6 (ordinary contact representations, p. 10): a fixed finite
  multiplier set $\mathcal K$ such that every integer $A$ is
  $u_1/v+u_2/v+u_3/v$ with each of the thirteen contact values $v$ and
  $L_b(u_i,v)$ ($b\ne\infty$) equal to $\pm k r$, $k\in\mathcal K$, $r$ a
  large prime split in $F$ and good for both curves, with test witnesses at
  both places above $r$. Section 2.3 (pp. 11--12) writes the recursive theory
  $\mathcal T$: for every ordinary precision $K$, a representation axiom
  asking for such sums with ring-language versions of the two tests at the
  two branch ideals cut out by a square root of $2$ modulo $r$. Lemma 2.7
  (p. 12): $\mathcal T$ is recursive and has the model $\mathbb Z$ with
  $T_a=aP$; the text adds that the fixed constants are hardcoded and need no
  effective search. Proposition 2.8 (p. 12): a positive existential formula
  $\Phi(b)$ with rational coefficients and a finite prime set $S_1$ such
  that $\Phi$ holds on every integer and any $b\in\mathbb Q^\times$
  satisfying $\Phi$ has even valuation at each $q\notin S_1$ where
  $v_q(b)<0$. The finite tests Skolemize $\mathcal T$ plus $f(\mathbf a)=0$
  and impose ring values, functionality, ground instances of the universal
  axioms and $\Phi$ on every ground-term value; each finite initial part
  reduces to finitely many rational-solvability queries. Lemma 2.9 (p. 13)
  is the compactness step; Lemma 2.10 (p. 14) coarsens the valuation at a
  contact prime by the convex subgroup generated by the poles of ring
  elements, so that pole parity selects a tested branch; Proposition 2.11
  (p. 15) gives the index congruence at every prime counted by a contact
  radical; Proposition 2.12 (p. 16) says that for nonconstant $f$, if every
  finite test is solvable then $f$ has an integer zero. Figure 1 (p. 16)
  diagrams that proof, and the proof of Theorem 1.1 closes the section
  (p. 17).
- Section 3, An existential condition excluding odd poles (pp. 18--26;
  `03-parity.tex`). Proves Proposition 2.8, comparing it with the existential
  divisibility predicates of Demeyer and Van Geel (2006). The formula uses
  the curves $E_l:y^2=x(x-l)(x+3l)$: for $b\ne0$, $\Phi(b)$ asks, for
  listed multipliers $m,m_d$ and rational $t,e$, that two twists $E_e$ and
  $E_{eH'}$, with $H'$ a rational function of $b$ and $t$, both have a
  rational point whose $x$-coordinate lies in the square class of $mb$.
  Lemma 3.1 (p. 18) proves the pole restriction by a valuation count.
  Lemma 3.2 (p. 20) prepares square classes for an integer input. Lemma 3.3
  (p. 21): for squarefree $l>0$ prime to $6$ with $l\equiv3\pmod4$,
  $l\equiv2\pmod3$, a condition on its prime support and a kernel and
  image condition on a Monsky-type matrix of Legendre symbols over that
  support, $\dim_{\mathbb F_2}\mathrm{Sel}_2(E_l/\mathbb Q)=3$ with a
  prescribed Selmer class outside the two-torsion classes. Lemma 3.4
  (p. 23): such an $E_l$ has a rational point with $x$-coordinate in the
  prescribed square class; the proof shows rank one and
  $\mathrm{Sha}(E_l/\mathbb Q)[2]=0$, applying the finiteness of the
  Tate--Shafarevich group from the pointwise 2-converse and the alternating
  Cassels--Tate pairing (Cassels 1962; Poonen and Stoll 1999). Remark 3.5
  (p. 24) names the unrestricted 2-converse as an alternative. Lemma 3.6
  (p. 24) builds one parameter serving both twists by prescribing Legendre
  symbols and applying Dirichlet's theorem. Monsky's appendix to
  Heath-Brown (1994), Mokrani (2020) and Wei and Guo (2022) are cited for
  the matrix viewpoint on these $\pi/3$-congruent number curves.
- Section 4, A height bound from odd contact with five points (pp. 26--44;
  `04-height.tex`). Proves Theorem 2.4 through Lemmas 4.1--4.8, with Remark
  4.3 giving a second route to Lemma 4.2; the result page outlines the
  argument: the discriminant-$210$ Shimura curve and its Atkin--Lehner
  quotient $\mathbf P^1$ with five rational branch values (Section 4.1,
  citing Long, Maclachlan and Reid and Nualart Riera), an abelian surface
  family with quaternionic multiplication, ramification of fiber fields
  only at odd-contact primes (Lemma 4.1, p. 31), a base-height comparison
  through theta heights (Lemma 4.2, p. 32), the split of the sign
  obstruction (Lemma 4.5, p. 37), modularity and the level bound
  $N\le CM^a$ (Lemma 4.7, p. 40, where the proof allows $a=2$), the modular
  factor (Lemma 4.8, p. 42) and the final isogeny estimate (p. 43), with the
  proof closing on p. 44. Remark 4.9 (p. 44) compares related
  Faltings-height bounds of von Känel and of von Känel and Kret.
- Section 5, The rank-one elliptic group and its local parameters
  (pp. 44--46; `05-elliptic.tex`). Proves Proposition 2.1 by a two-isogeny
  descent over $\mathbb Z[\sqrt2]$ (class number one, $d$ of norm $7$, the
  point $(-dw,2\sqrt2\,d^2)$ with $w=-5+4\sqrt2$), and Proposition 2.2 from
  the valuation properties of the formal logarithm, with a recursion for its
  coefficients; it compares Lemmas 9 and 11 of Poonen's rank-one paper.
- Section 6, Prime patterns for the two conjugate local tests (pp. 46--56;
  `06-primes.tex`). Lemma 6.1 (prime patterns, p. 47): a finite set
  $\mathcal K\subset\mathbb Z_{>0}$ such that for every $A\in\mathbb Z$ and
  $B>0$ the thirteen values above can all be made $\pm k r$ with
  $k\in\mathcal K$ and $r>B$ prime, split in $F$, good for $E$ and
  $E^\sigma$, and with the two reduction orders $d_1,d_2$ satisfying
  $\gcd(d_1,d_2)\mid4$ and $r\nmid d_1d_2$. Corollary 6.2 (p. 47) builds the
  test witnesses $h,j_0$ by the Chinese remainder theorem, and Corollary 2.6
  follows (p. 48). The proof of Lemma 6.1 restricts to primes
  $r\equiv1\pmod8$, $r\equiv3\pmod7$, where $E$ and $E^\sigma$ reduce to
  opposite twists of $y^2=x^3-x$ with orders $r+1\pm2a$ ($r=a^2+b^2$); fixes
  a finite multiplier catalog; obtains $\gg X^3/(\log X)^{13}$ patterns
  from the Green--Tao--Ziegler theorem on linear equations in primes (Green
  and Tao 2010 and 2012, Green, Tao and Ziegler 2012 with its 2024 erratum);
  and removes patterns with a large common odd factor of the orders by a
  Selberg upper sieve (Lemma 6.3, p. 52) and a fiber sieve, closing on p. 56.
- Section 7, Turing degree and a quartic normal form (pp. 56--57;
  `07-consequences.tex`). States and proves
  [[diophantine_problems/openai_2026_hilberts_tenth_problem_rational_numbers/corollary_7_1|Corollary 7.1]]
  (p. 56).
- References (pp. 57--62), 74 entries, three of them release manuscripts:
  the pointwise 2-converse [48], Fontaine--Mazur modularity at $2$ [49] and
  the Goldfeld and 2-converse manuscript [50].

The manuscript flags nothing as numerical, computer-assisted or conditional.
Two load-bearing inputs are other release manuscripts that are themselves
unreviewed: the pointwise 2-converse (Lemma 3.4, hence Proposition 2.8) and
Fontaine--Mazur modularity at $2$ (Section 4.7, hence Theorem 2.4). The fixed
data the theory and the tests use (the five points and their contact forms,
the multiplier sets and $m,P$) are asserted to exist and are hardcoded rather
than computed, and the text says their existence suffices for its argument
(p. 12); the exceptional set and constants $S,H,c$ of Theorem 2.4 enter only
the proof, which gives no values for them, and its bound for the fibers with
complex multiplication in Section 4 rests on a finiteness that "need not be
effective" (p. 36). The release folder for this manuscript holds only the
README, `main.pdf` and the TeX build directory; there is no `verification/`
folder.

## Bears on

The manuscript names no Erdős problem, and no problem page is identified as
using it. Problem pages were searched for decision problems, rational points
on curves, height bounds in terms of squarefree parts or radicals, and the
elliptic-curve families of Sections 3 and 5; none records an argument, a
conditional route or an open question about the objects these results
control.
