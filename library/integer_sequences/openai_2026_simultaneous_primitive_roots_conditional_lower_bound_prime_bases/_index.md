---
name: integer_sequences/openai_2026_simultaneous_primitive_roots_conditional_lower_bound_prime_bases
desc: |
  A 21-page release manuscript claiming, conditionally on four analytic and
  sieve inputs it states and attributes to the companion Artin manuscript,
  that for every fixed finite set of distinct primes at least c x/(log x)^2
  primes in (x,2x), for all large x, have every member as a primitive root;
  it names no Erdős problem and touches Problem 985 as background.
license: Apache-2.0
created: 2026-10-12T23:13:55Z
updated: 2026-10-12T23:13:55Z
---

# integer_sequences/openai_2026_simultaneous_primitive_roots_conditional_lower_bound_prime_bases

[[integer_sequences/_index|..]]

[[integer_sequences/openai_2026_simultaneous_primitive_roots_conditional_lower_bound_prime_bases/proposition_2_1|proposition_2_1]]: The manuscript's prime reservoir, conditional on three inputs it takes
from the companion Artin manuscript: many primes p in (x,2x) in a
fixed progression with p-1 = 4rQ, Q > x^0.9 prime and r composed of
primes in a controlled range. Claims checked only.

[[integer_sequences/openai_2026_simultaneous_primitive_roots_conditional_lower_bound_prime_bases/theorem_1_1|theorem_1_1]]: The manuscript's main claim, conditional on four inputs it states and takes
from the companion Artin manuscript: for distinct primes q_1,...,q_k, at
least c x/(log x)^2 primes p in (x,2x) have every q_i as a primitive root.
Claims checked only.

***

OpenAI, *Simultaneous primitive roots: a conditional lower bound for prime
bases*, OpenAI Math Release preprint, October 4, 2026. Released under the Apache
License 2.0 at <https://github.com/openai/math> (revision fd4aeeb2e), folder
`preprints/Simultaneous-primitive-roots-a-conditional-lower-bound-for-prime-bases-October-4-2026`;
the held PDF,
`simultaneous-primitive-roots-conditional-lower-bound-prime-bases.pdf` in the
release, is retained as
[openai_2026_simultaneous_primitive_roots_conditional_lower_bound_prime_bases.pdf](openai_2026_simultaneous_primitive_roots_conditional_lower_bound_prime_bases.pdf),
and the release's TeX bundle in that folder (`build/`) is the TeX source cited
on this card. The license term was read in the release's root `LICENSE` file at
that revision on 2026-10-12.

```bibtex
@misc{OAI:Simultaneous-primitive-roots-a-conditional-lower-bound-for-prime-bases-October-4-2026,
  author = {{OpenAI}},
  title = {{Simultaneous primitive roots: a conditional lower bound for prime bases}},
  howpublished = {OpenAI Math Release preprint
                  \href{https://github.com/openai/math/blob/main/preprints/Simultaneous-primitive-roots-a-conditional-lower-bound-for-prime-bases-October-4-2026/simultaneous-primitive-roots-conditional-lower-bound-prime-bases.pdf}{OAI:Simultaneous-primitive-roots-a-conditional-lower-bound-for-prime-bases-October-4-2026}},
  year = {2026}
}
```

The held PDF has 21 pages with a text layer; its title page is dated October
4, 2026, and its metadata records a creation date of 6 October 2026. The TeX
source is `build/paper.tex` (49 lines), which inputs six section files under
`build/sections/` and `build/references.tex`: eight files and 1,640 lines in
all, the text read here.

**Attestation.** The release README states that the collection holds
manuscripts "produced by an internal OpenAI model", that it "includes results
at different stages of verification", that "Not all have accompanying Lean
formalizations" and that "Some of the unformalized results could have
issues". Its account of the method says that "The vast majority of results
were obtained with the same procedure" and names as exceptions work on a
zero-free region for the Riemann zeta function and on the Hodge conjecture
for CM abelian varieties, neither of which is this family's subject. The
manuscript's own README carries only the title, the author line "OpenAI",
the date October 4, 2026 and the citation block above, with no sentence on
authorship, assistance or verification; the title page and the PDF metadata
name OpenAI as the sole author. The abstract and introduction say that the
result assumes four inputs whose proofs lie outside the paper. These are the
source's own statements, recorded as attestations and not as this corpus's
review. No refereed publication, arXiv version or independent review of the
manuscript is recorded here, and nothing on this card is independently
reviewed.

**Formalization.** The release lists no formalization of this manuscript:
its Lean catalog `lean/formalization.yaml` at revision fd4aeeb2e has no entry
for it, and its family has no Lean page.

**Companions.** The release's family for it holds one other manuscript, the
October 4, 2026 *Primitive roots for every admissible integer base*, filed at
[[integer_sequences/openai_2026_primitive_roots_admissible_integer_base/_index|the Artin card]];
it claims without hypotheses that every integer other than $-1$ and the squares
is a primitive root modulo at least $c_ax/(\log x)^2$ primes in $(x,2x)$ for all
large $x$, which for a prime base is the conclusion of Theorem 1.1 here with
$k=1$. The release states the relation: this manuscript's abstract and
introduction take all four of its Inputs from that manuscript, and Sections 3--5
name the sources, Input 3.1 as its Theorem 1.2, Input 4.1 as the coefficient
criterion of its Lemma 10.2 with mark parameter $1/2$ together with the
cancellation verified inside the proof of its Proposition 10.3, Input 5.1 as its
Lemma 11.1 and Input 5.2 as its Lemma 11.2. The companion's statements of
Theorem 1.2, Lemma 10.2, Proposition 10.3, Lemmas 11.1--11.2 and Propositions
2.1--2.2 were read at the same revision for comparison only. Input 3.1 and
Inputs 5.1--5.2 agree in substance with Theorem 1.2 and Lemmas 11.1--11.2, with
small differences of phrasing (for instance $z>1$ where the companion has
$z\ge2$). The companion's Proposition 10.3 states the resulting Type II bound,
not the cancellation that Input 4.1(ii) assumes, and the Artin card records that
the companion imports its Theorem 10.1 from another release manuscript and
extracts Lemma 10.2 from that theorem's proof. On this card's reading, the
companion's Propositions 2.1 and 2.2 as stated appear to contain this
manuscript's Propositions 2.1 (take the modulus $8M$, $c=4$ and a class
$u\equiv5\pmod8$, $u\equiv a\pmod M$) and 2.2 (take the base $a=q$ and the
companion's splitting test, Lemma 2.3), so that the companion's claims, if
correct, would give Theorem 1.1 here by the argument of Section 2 alone. The
manuscript does not make this remark: its introduction presents Sections 4--5 as
extending the companion's Section 12 construction to a fixed progression. The
comparison was made on the statements only and is unverified. The release lists
no other dated version of this manuscript. The companion's arguments were not
read for this card.

Read status: claims checked for Theorem 1.1 and Proposition 2.1, together
with the statements of Proposition 2.2, the four Inputs and the definitions
they use, read clause by clause in the release's TeX source on 2026-10-12
(under `build/sections/`: `01-introduction.tex` label `thm:main` at lines
32--47; `02-reduction.tex` labels `prop:reservoir` at lines 11--28 and
`prop:splitting` at lines 33--46; `03-splitting.tex` label `input:hecke` at
lines 8--15; `04-marked-family.tex` lines 10--71 and 88--89 for the marked
setup and label `input:marked` at lines 99--151; `05-prime-reservoir.tex` labels
`input:block` at lines 11--63 and `input:density` at lines 65--78). The
proofs (Section 2 for Theorem 1.1, Section 3 for Proposition 2.2, Sections
4--5 for Proposition 2.1) were read for their structure only and no step was
checked; nothing here is independently reviewed.

## Contents

The PDF's page numbers are its printed ones; theorems, propositions, lemmas
and Inputs share one counter numbered within sections. The four Inputs,
which Theorem 1.1 and Propositions 2.1 and 2.2 assume, are summarized after
this list and stated in full on the page of Theorem 1.1.

- Abstract and Section 1, Introduction (pp. 1--2; `00-abstract.tex`,
  `01-introduction.tex`). Defines $\operatorname{ord}_p(q)$ and primitive
  roots. Places the one-base problem in Artin's conjecture (recorded by
  Hasse in 1927, cited to Hasse's diaries) and recalls Hooley's asymptotic
  under generalized Riemann hypotheses, Matthews's densities for
  simultaneous primitive roots under the same hypotheses, Anwar and
  Pappalardi's infinitude criterion under Schinzel's Hypothesis H, and the
  unconditional results of Gupta and Murty and of Heath-Brown, the latter
  read as making one member of any three distinct positive primes a
  primitive root modulo infinitely many primes. Calls the result an
  implication from four statements of the companion, Inputs 3.1, 4.1, 5.1
  and 5.2, reproduced "in the precise forms used here", and states
  [[integer_sequences/openai_2026_simultaneous_primitive_roots_conditional_lower_bound_prime_bases/theorem_1_1|Theorem 1.1]]
  (p. 1): under the four Inputs, for distinct positive primes
  $q_1,\dots,q_k$ there are $c_{\mathbf q}>0$ and $x_{\mathbf q}>1$ such
  that for all real $x\ge x_{\mathbf q}$ at least
  $c_{\mathbf q}x/(\log x)^2$ primes $p\in(x,2x)$ have $p\nmid q_1\cdots q_k$
  and $\operatorname{ord}_p(q_i)=p-1$ for every $i$. Outlines the proof: the
  companion's construction of primes with controlled predecessors, carried
  into a fixed progression; the marked Type II estimate twisted by a fixed
  character; Bombieri--Vinogradov in the progression; a direct sieve for
  balanced semiprimes; a progression making every base a nonresidue; and
  uniform splitting bounds in the Kummer fields.
- Section 2, Reduction to two estimates (pp. 2--3; `02-reduction.tex`).
  Sets $L=\log x$, $\eta=10^{-6}$ and the order index
  $\iota_p(q)=(p-1)/\operatorname{ord}_p(q)$. States
  [[integer_sequences/openai_2026_simultaneous_primitive_roots_conditional_lower_bound_prime_bases/proposition_2_1|Proposition 2.1]]
  (a prime reservoir in a fixed progression, assuming Inputs 4.1, 5.1 and
  5.2): for odd squarefree $M\ge1$ and a class $a$ with
  $\gcd(a(a-1),M)=1$ there are $c_{M,a}>0$ and $x_{M,a}>1$ such that for
  all real $x\ge x_{M,a}$ at least $c_{M,a}x/L^2$ primes $p\in(x,2x)$ have
  $p\equiv a\pmod M$ and $p=4rQ+1$, with $Q>x^{0.9}$ prime and every prime
  factor of the positive integer $r$ in $(\exp(L^{0.1}),\exp(L^{0.3}))$.
  States Proposition 2.2 (a uniform bound for order obstructions, assuming
  Input 3.1): for each fixed positive prime $q$, all sufficiently large $x$
  and uniformly in primes $\ell$ with $\exp(L^{0.1})<\ell<\exp(L^{0.3})$,
  the primes $p\in(x,2x)$ with $p\nmid q\ell$, $p\equiv1\pmod\ell$ and
  $q^{(p-1)/\ell}\equiv1\pmod p$ number
  $\ll_q x/(\ell(\ell-1)L)+x^{1-\eta}$. Proves Theorem 1.1 from the two
  propositions (pp. 2--3), as summarized on the result page.
- Section 3, A uniform splitting estimate (pp. 3--6; `03-splitting.tex`).
  States Input 3.1, citing the companion's Theorem 1.2, and proves
  Proposition 2.2: degree $\ell(\ell-1)$ and a discriminant bound for
  $K=\mathbb Q(\mu_\ell,q^{1/\ell})$ (3.1)--(3.2); the two congruences as
  complete splitting, by Frobenius; zero-freeness of $\zeta_K$ in
  $\operatorname{Re}s>1-\eta$ (3.4), by what the text calls the companion's
  Section 9 tower argument specialized to the base $q$: place $K$ under
  $K\mathbb Q(\mu_{12\ell})$, factor with abelian Artin formalism
  (Neukirch), and use that nonprincipal Hecke $L$-functions are entire
  (Tate); a smoothed explicit formula (3.5) whose error is uniform in the
  field, with the zero count of Hasanalizade, Shen and Wong (3.6); the
  upper bound $\Psi_{K'}(x)\ll x+x^{1-\eta}(\log D'+n')$ for the smoothed
  prime-ideal sum of any number field $K'$ of degree $n'$ and discriminant
  $D'$ that is zero-free in that half-plane (3.8); and the count (3.9).
- Section 4, A marked family in a fixed progression (pp. 6--12;
  `04-marked-family.tex`). The marked setup and Input 4.1 (see below). Lemma
  4.2 (p. 8): the Type II bound of Input 4.1 for the rough-factor
  coefficient twisted by any character modulo $M$, uniformly in that
  character. The character expansion of the progression (4.14); the family
  $w(d)=\mathbf 1_{d\equiv a\,(M)}\Psi(d/x)F(d-1)\mathcal W(d-1)$ (4.15),
  where $F$ selects $h/h_{\mathcal P}=4Q$ with $Q>x^{0.9}$ prime, and its
  unique representation $d=4rQ+1$ (4.16). Lemma 4.3 (p. 9): the harmonic
  mass $J_0=\sum_r\mathcal W(r)/r$ satisfies $1\le J_0\ll_K1$ with a
  Rankin tail, the prime number theorem in the progression for each small
  $r$, and $X_0\asymp xJ_0/L$ for the total weight, with constants
  independent of $K$ and the $a_i$. Lemma 4.4 (p. 11): the sieve remainders
  are small on average over $r\le x^\epsilon$ and moduli up to
  $D_0=x^{1/2-\kappa/2}$, by Bombieri--Vinogradov. The sieve products
  $V_M$ and the constant $\mathfrak S_M>0$ (4.24)--(4.25), and the
  negligible effect of the group primes dividing $r$ (4.27).
- Section 5, Extracting primes from the marked family (pp. 12--20;
  `05-prime-reservoir.tex`). Inputs 5.1 and 5.2 (see below), with a remark
  that the density identity removes the least factor. Section 5.1 (p. 14):
  the initial lower-bound sieve at level $x^b$ (5.5) and a sieve
  conditioned on a prime divisor $n$ (5.6). Section 5.2 (p. 15): removal of
  composites by their least prime factor in bins, replacing the rough count
  by the density through Lemma 4.2 (5.8), and summing the bins with Input
  5.2 (5.12)--(5.13). Section 5.3 (p. 17): an upper-bound sieve for
  balanced semiprimes with a constant independent of $\kappa$, $b$ and $K$
  (5.20); the order of the parameter choices; the conclusion (5.21) that
  primes carry at least $\mathfrak S_MX_0/(2L)$ of the weight, which proves
  Proposition 2.1 (p. 20).
- References (pp. 20--21; `references.tex`): 12 entries, one of them the
  companion release manuscript.

**The Inputs.** The manuscript assumes four statements of the companion
without proof;
[[integer_sequences/openai_2026_simultaneous_primitive_roots_conditional_lower_bound_prime_bases/theorem_1_1|the page of Theorem 1.1]]
restates them in full, with the marked setup two of them use. Input 3.1
(p. 3) says that no finite-order Hecke $L$-function of a cyclotomic field
containing $\mu_{12}$ vanishes in $\operatorname{Re}s>1-10^{-6}$. Input 4.1
(pp. 7--8) bounds the marked bilinear sum
$\sum_{m,n}\alpha_m\beta_nF(mn-1)\mathcal W(mn-1)$ by $XL^{-D_*}$, for $K$
large, whenever the coefficients $\alpha_m$ cancel against Dirichlet
characters of modulus up to a power of $L$ and frequencies up to $2XL^B$,
and it grants that cancellation to the difference between the indicator of
$P^-(m)>x^\gamma$ and its density-weighted model on $W$-rough $m$. Input 5.1
(pp. 12--13) is a block sieve that gives the weight surviving the sifting as
its expected main term times $1+O(e^{-H})$, with remainders summed up to
level $z^{4H+2}$ and an upper-bound form at $H=2$, all constants depending
only on the two bounds assumed for the sieve density $g$. Input 5.2 (p. 13)
is the identity $\int_b^{1/2}D_t(1-t)\,dt/t=D_b(1)-1$ for the rough-factor
density, which removes the least factor, with the bound
$D_b(1)\le e^{-\gamma_E}b^{-1}(1+C_de^{-c_d/b})$ for small fixed $b$.

Flags. The manuscript is conditional by design: Theorem 1.1 and
Propositions 2.1 and 2.2 assume the Inputs, which are stated and not proved
in it, and by its own account Input 4.1(ii) is a cancellation verified
inside a proof in the companion rather than a result stated there. Nothing
is marked numerical or computer-assisted; the constants are explicit
($\eta=10^{-6}$ and the exponents $0.1$, $0.24$, $0.3$ and $0.9$) or are
fixed in a stated order. The release folder holds only the README, the PDF
and the TeX build directory; there is no `verification/` folder.

## Bears on

The manuscript names no Erdős problem. The row below is a background lead
inferred on this card; it is not stated in the manuscript, it is not
verified here, and the page's status rests on its own acceptance evidence.
Problem 429, whose recorded disproof uses a positive integer that is a
primitive root modulo infinitely many primes, is not listed: that problem is
solved, and the classical theorems its page cites already supply that input
without hypotheses. Problem 1065, which asks for infinitely many primes
$p=2^kq+1$ with $q$ prime, or $p=2^k3^lq+1$, is not listed either.
Proposition 2.1 gives primes $p=4rQ+1$ in which every prime factor of $r$
exceeds $\exp((\log x)^{0.1})$, so such a $p$ has one of the asked forms
only when $r=1$. The proposition does not promise that case, and its
construction gives it weight zero. The proposition therefore controls none
of the primes the question asks about; the two share only a theme, the
factorization of $p-1$.

- [[../wiki/problems/integer_sequences/E0985/_index|Problem 985]]: background.
  The corrected question asks whether every prime $p>2$ has a prime
  primitive root $q<p$. Under Inputs 3.1, 4.1, 5.1 and 5.2, Theorem 1.1
  gives, for any fixed finite set of primes, infinitely many $p$ at which
  all of them are primitive roots, so each such $p$ has a prime primitive
  root below it; for a single prime base, $2$ for instance, the companion
  claims this without hypotheses, and the manuscript's introduction reads
  Heath-Brown's theorem, cited on the page, as giving it for one of any
  three distinct primes. The theorem says nothing about the "every $p$"
  quantifier and bounds the least prime primitive root of no given $p$; no
  deduction toward the question is known. Unverified.
