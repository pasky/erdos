---
name: integer_sequences/openai_2026_quadratic_bound_jacobsthal_function/evidence/verify/covering_bound_review
title: Review of Y(x) = o(x^2) from the quadratic Jacobsthal bound
desc: |
  Retains Plasma AI's review of 2026-10-12: the accepted Lean bound
  h(k) <= Ck^2, with Y(x) = j(P(x)) - 1 and Chebyshev's bound, gives
  Y(x) << x^2/(log x)^2, a yes to Problem 687's first displayed question.
created: 2026-10-13T05:29:01Z
updated: 2026-10-13T05:29:01Z
---

***

## Record and attribution

Reviewer: Plasma AI. Date of the review: 2026-10-12. The review ran three
independent checks, of the definitions, of the bound and of the asymptotics,
against the sources named below; all three hold. It is the review on which
[[../wiki/problems/integer_sequences/E0687/claims/2026_09_25_openai|Problem 687's claim page for the OpenAI release]]
accepts the answer $Y(x)=o(x^2)$.

This record was filed on 2026-10-13 from the reviewer's report, which is
retained below. Filed records may be edited to remove private paths, and the
filing replaced the report's private working paths with plain descriptions:
the corpus's cached copies of the site's pages, a copy of the arXiv v3 PDF of
[FGKMT18] that the repository does not hold, the corpus's build and
axiom-audit records of 2026-10-07 for the release's Lean tree, the corpus's
statement-audit records for that tree, and the working copies of the release
used to read and to build it. The filing also adds the source identities
below and links. It changes no repository path, scope, date or verdict.

[FGKMT18] is K. Ford, B. Green, S. Konyagin, J. Maynard and T. Tao, *Long gaps
between primes*, arXiv:1412.5029v3, J. Amer. Math. Soc. 31 (2018), filed as
[[integer_sequences/ford_2018_long_gaps_between_primes/_index|ford_2018_long_gaps_between_primes]].
The manuscript is OpenAI, *A quadratic bound for Jacobsthal's function*, of
the OpenAI mathematics release of 25 September 2026, filed as
[[integer_sequences/openai_2026_quadratic_bound_jacobsthal_function/_index|openai_2026_quadratic_bound_jacobsthal_function]];
the release revision read is `adc7f1241b42e322a6451854ab7e4b4c146bf78a`, the
revision the claim pages pin.

## Retained report

**Verdict.** The deduction holds. The accepted Lean declaration
`OAI.Erdos970.Erdos970Final.erdos_970_quadratic` ($h(k)\le Ck^2$ for every
$k\ge1$, one absolute $C>0$) gives $Y(x)\le C\,\pi(x)^2-1$ for every real
$x\ge2$, hence $Y(x)\ll x^2/(\log x)^2=o(x^2)$: a yes to the first displayed
question of Problem 687. The second question, $Y(x)\ll x^{1+o(1)}$, and the
request for good estimates stay open.

### The deduction

1. **Definition of $Y(x)$.** The site's wording, read from the corpus's
   cached copies of the site's page for Problem 687 (the first taken when this
   corpus opened the problem page, the second on 2026-09-18; identical in
   both), is the largest $y$ such that some choice of one class $a_p$ at each
   prime $p\le x$ covers every integer in $[1,y]$. The problem page
   `wiki/problems/integer_sequences/E0687/_index.md` (Statement, lines 25-31)
   reproduces it word for word. [FGKMT18] Definition 1 (a copy of the arXiv
   v3 PDF, p. 3) is the same condition with $y$ an integer; the only coherent
   reading of the site's "maximal $y$" is also integer $y$.

2. **$Y(x)=j(P(x))-1$.** [FGKMT18] display (1.3), p. 4, with $j(n)$ the
   maximal gap between integers coprime to $n$, glossed there as $1$ plus the
   longest run of consecutive integers each divisible by a prime $p\le x$.
   The library page
   `library/integer_sequences/ford_2018_long_gaps_between_primes/lemma_1_1.md`
   records both directions from the definitions: a covering of $[1,y]$ gives,
   through the Chinese remainder theorem ($m\equiv-a_p\pmod p$ for all
   $p\le x$), the run $m+1,\dots,m+y$ of integers not coprime to $P(x)$, and a
   run $m+1,\dots,m+L$ of such integers gives the covering $a_p\equiv-m\pmod p$
   of $[1,L]$. So $Y(x)$ is the longest run of integers not coprime to $P(x)$,
   and $j(P(x))=Y(x)+1$. Re-verified here; brute force to $x=11$ gives
   $Y=1,3,5,9,13$ and $j(P(x))=2,4,6,10,14$, matching OEIS A048670 as quoted
   on the problem page.

3. **Jacobsthal conventions agree.** [FGKMT18]'s "maximal gap between coprime
   integers" and Problem 970's "least $m$ such that every $m$ consecutive
   integers contain one coprime to $n$" (the site's wording, from the
   corpus's first cached copy of the site's page for Problem 970; the problem
   page `wiki/problems/integer_sequences/E0970/_index.md`, Formulation; the
   manuscript's introduction, p. 2) both equal $1$ plus the longest run of
   non-coprime integers, since integers $\equiv1\pmod n$ are coprime to $n$
   and bound every run on both sides.

4. **$j(P(x))\le h(\pi(x))$.** $P(x)$ is squarefree with exactly $\pi(x)$
   prime factors, distinct or with multiplicity, so it lies in the set
   $h(\pi(x))$ maximizes over under either reading of "at most $k$ prime
   factors". Already recorded on the 970 problem page (Formulation:
   $h(\pi(x))\ge Y(x)+1$) and in the manuscript (its transcription on the
   card,
   `library/integer_sequences/openai_2026_quadratic_bound_jacobsthal_function/openai_2026_quadratic_bound_jacobsthal_function.md`,
   line 34: "Since $j(P_k)\le h(k)$").

5. **$h(k)\le Ck^2$ for every $k\ge1$.** The Lean declaration
   `erdos_970_quadratic` (in the release's tree,
   `lean/OAI/NumberTheory/Jacobsthal/Conclusions/QuadraticBound.lean`, line
   13; its type `JacobsthalQuadratic` from `Model.lean`, lines 12-18): there
   is a real $C>0$ such that for every natural $k>0$ some natural $m\le Ck^2$
   satisfies `IsJacobsthalBound k m`, which says that for every $n>0$ with
   `n.primeFactors.card ≤ k` (distinct primes) and every integer $a$ some
   $a+i$, $0\le i<m$, has $\gcd(|a+i|,n)=1$. For $n$ with $\omega(n)\le k$
   this is $j(n)\le m$, so $h(k)\le m\le Ck^2$. Acceptance is taken from the
   970 claim page `wiki/problems/integer_sequences/E0970/claims/2026_09_25_openai.md`
   (status accepted, evidence formalized): built on 2026-10-07 at the pinned
   release revision, axioms exactly `propext`, `Classical.choice`,
   `Quot.sound`, comparator fingerprint identical (the corpus's build and
   axiom-audit records of 2026-10-07 for the release's family 021). The copy
   of the release read here is at that revision with the Lean files
   unchanged; a text search over the 819 Jacobsthal files finds no `sorry`,
   `axiom`, `native_decide` or similar escape. Not rebuilt here.

6. **The chain.** For real $x\ge2$, $k=\pi(x)\ge1$ (so the Lean hypothesis
   $0<k$ holds) and $n=P(x)$ has `primeFactors.card` $=\pi(x)$. Applying the
   predicate to $n=P(x)$ and $a=m'+1$, the start of the run from step 2,
   gives $Y(x)<m\le C\pi(x)^2$. Equivalently
   $Y(x)=j(P(x))-1\le h(\pi(x))-1<C\,\pi(x)^2$. (The deduction as proposed,
   $Y(x)\le h(\pi(x))$, drops a harmless $-1$.) $Y(x)$ depends on $x$ only
   through the primes $\le x$, so real $x$ costs nothing. For $x<2$ there are
   no primes and $Y(x)=0$.

7. **Asymptotics.** Chebyshev's $\pi(x)\le c\,x/\log x$ for $x\ge2$ (the
   problem page already invokes it) gives
   $Y(x)\le Cc^2\,x^2/(\log x)^2$ for all $x\ge2$, so $Y(x)/x^2\to0$:
   $Y(x)=o(x^2)$. Sieve to $10^7$: $\pi(x)^2(\log x)^2/x^2$ runs
   $1.35,1.28,1.22,1.18,1.15$ at $x=10^3,\dots,10^7$, consistent.

### What it answers

The first displayed question of Problem 687, $Y(x)=o(x^2)$: yes, with the
saving $(\log x)^2$ over Iwaniec's $Y(x)\ll x^2$. Through the page's own
inverse-form remark ($B(n)$ the least $x$ with $Y(x)\ge n$) it also gives
$B(n)/\sqrt n\to\infty$, Erdős's [Er80] p. 106 question.

### What it does not answer

The second displayed question, $Y(x)\ll x^{1+o(1)}$, and the request for good
estimates of $Y(x)$: the exponent stays $2$. The site's OPEN label attaches
to the estimate, so the problem's standing stays open, with a partial
accepted claim, as on Problem 970. No contradiction with any statement on the
687 or 970 pages was found.

### Caveats

- **The bridge is authored, not formalized.** Nothing in the release's Lean
  tree names $Y(x)$, $P(x)$, $\pi(x)$ or a covering by one class per prime
  (confirmed by a text search of the tree; the corpus's own statement-audit
  records for the release's family 021 say the same). The deduction rests on
  the accepted formal statement plus three elementary unformalized steps:
  [FGKMT18] (1.3) or directly the Chinese remainder construction,
  $\omega(P(x))=\pi(x)$, and Chebyshev. A claim page for 687 should list
  `formalized` only for the $h(k)$ half and say the bridge is authored. The
  corpus already accepts one-line authored identity steps on 970's Iwaniec
  and FGKMT claim pages, so this follows precedent.
- **No explicit constant.** $C$ is existential and, by the manuscript's
  conventions (p. 4), need not be effective. The result is
  $Y(x)\ll x^2/(\log x)^2$ with an unspecified constant, not the constant-1
  form $Y(z)<\lfloor z^2/(\log z)^2\rfloor$ read from the manuscript's
  Theorem 1.2 on the 687 claim page as it then stood. Same order, weaker
  constant; the record should attribute $o(x^2)$ to the accepted Lean route
  and the constant-1 form to the unreviewed manuscript.
- **Theorem 1.2 and the Lean bound are one argument, not two sources.** The
  manuscript's Section 11.2 derives Theorem 1.1 from Theorem 1.2; the
  declaration `erdos_970_quadratic` is proved from the survivor lower bound
  `source_root_survivor_lower`. The stronger `erdos_970_iterated_log` (its
  axioms are listed in the same axiom-audit records of 2026-10-07, but the
  corpus has not accepted it) would give
  $Y(x)\ll x^2/((\log x)^2(\log\log x)^2)$; a record should not call
  $x^2/(\log x)^2$ the manuscript's best for $Y$.
- **Two wording ambiguities, both immaterial here.** The site's 687 wording
  does not say $y$ is an integer (the real reading has no maximum); the
  site's 970 wording does not say "distinct" prime factors (the Lean uses
  distinct, the stronger statement, and $P(x)$ is squarefree). Worth one line
  each in the record.
- **[FGKMT18] Definition 1 misstatement.** Its second sentence reads
  "$m$ consecutive integers coprime to $P(x)$" where "none coprime" is meant
  (confirmed on the PDF page image, arXiv v3 p. 3); the first sentence and
  the p. 4 gloss are the operative ones. The lemma_1_1 and _index library
  pages quote only the first sentence; the journal text was not compared.
- **Pages to update if adopted.** 687's Status (lines 54-57, "No source
  proving $Y(x)=o(x^2)$ ... was found"), Bounds map, Remaining gaps item (6),
  and its claim page's Formalization and Acceptance paragraphs say the
  audited declaration reaches $h(k)$ alone; 970's Formulation already records
  $h(\pi(x))\ge Y(x)+1$. 687's Depends on should point to the 970 claim page,
  the lemma_1_1 page and Chebyshev.
- **Not re-done here.** The 2026-10-07 build and axiom audit were not re-run
  (the working copy used for that build is no longer available); the site was
  not fetched, and only the corpus's cached copies of the site's pages were
  read.
