---
name: number_theory/bloom_2026_erdos_problems_openai_proofs
title: "Bloom: Erdős problems in the OpenAI proofs"
desc: |
  The catalog curator's blog post of 8 October 2026 listing the OpenAI
  mathematics release's claims on 25 Erdős problems, with a short remark on
  each and whether its proof was formalized; a summary of claims, expressly
  not an endorsement.
license: unstated
created: 2026-10-14T00:20:00Z
updated: 2026-10-14T00:21:45Z
---

# Bloom: Erdős problems in the OpenAI proofs

[[number_theory/_index|..]]

***

T. F. Bloom, "Erdős problems in the OpenAI proofs", blog post on
erdosproblems.com, 8 October 2026,
<https://www.erdosproblems.com/forum/thread/blog:10>. The curator added
Problems 174 and 986 to the post on 9 October 2026, as his comment of that day
in the thread
([post 9337](https://www.erdosproblems.com/forum/thread/blog:10#post-9337))
says.

**Edition read.** The thread as it read on 13 October 2026, with Problems 174
and 986 already in the post and eleven comments below it. A web page has no
pinned version, and the post says it will be updated if anything changes,
such as new formalizations or retracted proofs, so a later reading may differ.
The captured page carries no copyright, license or terms line; the term is
unstated.

**Read status.** Claims checked: the whole post was read, and each problem's
remark is recorded below as the post states it. The post is the curator's
summary of claims, not a review: it says that he had not yet examined the
proofs seriously, had not checked that the Lean files compile or that their
challenge statements capture the problems, and that the post "should not be
read as any kind of endorsement". It confers no acceptance on any claim.

## Contents

- The release (6 October 2026) and its scope: claims bearing on 25 Erdős
  problems, 21 of them with proofs formalized in Lean, in PDFs of 1347 pages
  in all. The post counts among them solutions to 12 problems of the
  FrontierMath Erdős list, Problem 508 as partial.
- Two disclaimers: the post is a list of claims, not an endorsement; and
  there have been accusations of plagiarism, some of the proofs having
  appeared online before the release, a question of attribution the post
  leaves open.
- The curator's view of how to treat the proofs: as raw material to be read,
  verified, simplified and understood, poorly written but, he expects, mostly
  correct; none of them closes its problem for further work.
- One entry per problem, stating the claimed theorem, the best earlier result
  the curator cites, whether the proof is formalized and the PDF's length,
  sometimes with a first impression of the method. The remarks that bear on
  the record of a problem:
  - [3]: the comparator challenge file states only the divergent-reciprocals
    conjecture, and the Lean code appears to prove only the weaker bound
    $\exp(-(\log\log N)^{1+c_k})N$, not the PDF's quasipolynomial bound.
  - [90]: the upper bound $n^{4/3-c}$ for some $c>0$, with no value of $c$;
    formalized.
  - [120]: the case $A=\{q,q^2,q^3,\ldots\}$; formalized only for $q=1/2$.
  - [138]: $W_r(k)\ge k^{ck\log r}$, by methods similar to Fox and Hunter's;
    formalized.
  - [148], [293], [304]: one PDF, whose main theorem is the $O(\log\log b)$
    bound for [304], with the bounds for [148] and [293] as corollaries;
    formalized.
  - [172], [181], [821], [1083]: not formalized.
  - [174]: a classification of Ramsey sets by a tensor matrix condition; the
    post mentions Pálvölgyi's work in preparation proving that all finite
    transitive sets are Ramsey; formalized.
  - [184], [371], [416], [431], [508], [551], [604], [802], [952], [968],
    [970], [1150]: formalized. For [416] the post notes that Erdős asked the
    case $c=2$; for [1150] that the PDF relies heavily on two companion PDFs of
    the release.
  - [986]: the sharp logarithmic power for fixed $s\ge5$; the post notes that
    Bradač's earlier determination of the power of $t$ already answered
    Erdős's question, which did not ask for the logarithmic exponent;
    formalized.

## Compiled scope

The post's statements about each problem, recorded as the curator's remarks;
no mathematical result is extracted. Its descriptions of the claimed theorems
are not checked against the release's manuscripts, which have their own cards
where the corpus records them.

**Bears on.**
[[../wiki/problems/additive_combinatorics/E0003/_index|#3]],
[[../wiki/problems/distance_problems/E0090/_index|#90]],
[[../wiki/problems/analysis/E0120/_index|#120]],
[[../wiki/problems/additive_combinatorics/E0138/_index|#138]],
[[../wiki/problems/unit_fractions/E0148/_index|#148]],
[[../wiki/problems/ramsey_theory/E0172/_index|#172]],
[[../wiki/problems/discrete_geometry/E0174/_index|#174]],
[[../wiki/problems/ramsey_theory/E0181/_index|#181]],
[[../wiki/problems/extremal_graph_theory/E0184/_index|#184]],
[[../wiki/problems/unit_fractions/E0293/_index|#293]],
[[../wiki/problems/unit_fractions/E0304/_index|#304]],
[[../wiki/problems/arithmetic_functions/E0371/_index|#371]],
[[../wiki/problems/arithmetic_functions/E0416/_index|#416]],
[[../wiki/problems/primes/E0431/_index|#431]],
[[../wiki/problems/discrete_geometry/E0508/_index|#508]],
[[../wiki/problems/ramsey_theory/E0551/_index|#551]],
[[../wiki/problems/distance_problems/E0604/_index|#604]],
[[../wiki/problems/extremal_graph_theory/E0802/_index|#802]],
[[../wiki/problems/arithmetic_functions/E0821/_index|#821]],
[[../wiki/problems/number_theory/E0952/_index|#952]],
[[../wiki/problems/integer_sequences/E0968/_index|#968]],
[[../wiki/problems/integer_sequences/E0970/_index|#970]],
[[../wiki/problems/ramsey_theory/E0986/_index|#986]],
[[../wiki/problems/distance_problems/E1083/_index|#1083]],
[[../wiki/problems/polynomials/E1150/_index|#1150]]: the post lists the
release's claim on each as a claim, with the remarks above.

No file of this source is held: no license on record permits its redistribution,
and the card cites the edition it names above.
