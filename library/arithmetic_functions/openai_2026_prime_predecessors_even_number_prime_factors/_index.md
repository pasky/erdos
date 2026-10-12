---
name: arithmetic_functions/openai_2026_prime_predecessors_even_number_prime_factors
desc: |
  A 45-page release manuscript claiming infinitely many primes p for which
  p-1 is squarefree with an even number of prime factors, so that
  mu(p-1)=1, by sieving weights that force an odd number of prime factors
  in (p-1)/2 with a parity-twisted Type II estimate; it names no Erdős
  problem, and the release's Artin-conjecture manuscript cites its Lemmas 3.1
  and 3.3.
license: Apache-2.0
created: 2026-10-12T23:13:55Z
updated: 2026-10-12T23:13:55Z
---

# arithmetic_functions/openai_2026_prime_predecessors_even_number_prime_factors

[[arithmetic_functions/_index|..]]

[[arithmetic_functions/openai_2026_prime_predecessors_even_number_prime_factors/lemma_3_1|lemma_3_1]]: Any fixed log-power saving in the sum of chi(p)p^(-1+it) over primes in an
interval inside [N,2N], x^tau/2 <= N <= x^eta, for characters of modulus at
most a power of log x and (log x)^B0 <= |t| <= x^2; the release's
Artin-conjecture manuscript cites it. Claims checked only.

[[arithmetic_functions/openai_2026_prime_predecessors_even_number_prime_factors/lemma_3_3|lemma_3_3]]: Sums of n^(iv) over an arithmetic progression of modulus at most a power of
log x in an interval inside [N',2N'], exp(log x/(log log x)^2) <= N' <=
2x^5, save exp(-log x/(log log x)^C3) for heights
exp(log x/(2(log log x)^2)) <= |v| <= 4x^3; it feeds Lemma 3.1, and the
release's Artin-conjecture manuscript cites it. Claims checked only.

[[arithmetic_functions/openai_2026_prime_predecessors_even_number_prime_factors/theorem_1_1|theorem_1_1]]: The manuscript's main claim: infinitely many primes p for which p-1 is
squarefree with an even number of prime factors, that is with mu(p-1)=1.
Claims checked only.

***

OpenAI, *Prime Predecessors with an Even Number of Prime Factors*, OpenAI Math
Release preprint, September 17, 2026. Released under the Apache License 2.0 at
<https://github.com/openai/math> (revision fd4aeeb2e), folder
`preprints/Prime-Predecessors-with-an-Even-Number-of-Prime-Factors-September-17-2026`;
the held PDF, `paper.pdf` in the release, is retained as
[openai_2026_prime_predecessors_even_number_prime_factors.pdf](openai_2026_prime_predecessors_even_number_prime_factors.pdf),
and the release's TeX bundle in that folder (`build/`) is the TeX source cited
on this card. The license term was read in the release's root `LICENSE` file at
that revision on 2026-10-12.

```bibtex
@misc{OAI:Prime-Predecessors-with-an-Even-Number-of-Prime-Factors-September-17-2026,
  author = {{OpenAI}},
  title = {{Prime Predecessors with an Even Number of Prime Factors}},
  howpublished = {OpenAI Math Release preprint
                  \href{https://github.com/openai/math/blob/main/preprints/Prime-Predecessors-with-an-Even-Number-of-Prime-Factors-September-17-2026/paper.pdf}{OAI:Prime-Predecessors-with-an-Even-Number-of-Prime-Factors-September-17-2026}},
  year = {2026}
}
```

The held PDF has 45 pages with a text layer; its title page is dated September
17, 2026 and its metadata records a creation date of 17 September 2026. The
TeX source is `build/main.tex` (141 lines: preamble, abstract, Theorem 1.1 and
the introduction), which inputs seven section files
`build/sections/01-preliminaries.tex` to `07-extraction.tex` (3,263 lines
together; they print as Sections 2--8) and `build/references.tex` (39 lines),
3,443 lines in all.

**Attestation.** The release README says that the collection's manuscripts and
supporting proof artifacts were "produced by an internal OpenAI model", that
"Some outputs build upon earlier results produced by the models", that the
collection "includes results at different stages of verification", that "Not
all have accompanying Lean formalizations" and that "Some of the unformalized
results could have issues". Its account of the method says that "The vast
majority of results were obtained with the same procedure" using an unreleased
model, and names as exceptions work on a zero-free region for the Riemann zeta
function and on the Hodge conjecture for CM abelian varieties, neither of
which is this family's subject. The manuscript's own README carries only the
title, the author line "OpenAI", the date September 17, 2026 and the citation
block, and adds no sentence about authorship or assistance; the title page
names OpenAI as the sole author, and the text says nothing about how it was
produced. These are the source's own statements, recorded as attestations and
not as this corpus's review. No refereed publication, arXiv version or
independent review of the manuscript is recorded here, and nothing on this
card is independently reviewed.

**Formalization.** The release lists no formalization of this manuscript: its
Lean catalog `lean/formalization.yaml` has no entry for it at this revision,
and the release has no Lean page for its family.

**Companions.** The release files this manuscript in a family titled
"Prime-factor statistics of $p-1$" in its manuscript map and "The
Ford--Konyagin--Luca conjecture on prime predecessors" in its overview, whose
summary describes only the other two members. *Weighted dilation graphs, smooth
shifted primes and totient fibers* (September 24, 2026), filed at
[[arithmetic_functions/openai_2026_weighted_dilation_graphs_smooth_shifted_primes_totient_fibers/_index|the weighted-dilation card]],
is the paper this manuscript calls S: it imports from S, without proof, the
stated forms of its classical estimates (Section 2), its transference and
residual ideal operator theorems and integer bilinear estimate (Section 4), and
its block sieve and proxy estimates (Section 8), and says its own new work is to
put a prime in the long factor slot where S's shifted-correlation argument has a
rough integer, and to keep the same parity sign at both ends of the correlation.
The bibliography's link to S names S's release folder, dated a week after this
manuscript; S does not cite this manuscript, as its card records. *The
Poisson--Dirichlet law for prime predecessors*, dated September 24, 2026 and
filed at
[[arithmetic_functions/openai_2026_poisson_dirichlet_law_prime_predecessors/_index|the Poisson--Dirichlet card]],
is the third member; neither manuscript cites the other. That manuscript states
the long prime polynomial and logarithmic-phase estimates, in the same ranges as
Lemmas 3.1 and 3.3 here, as its Lemmas 2.3 and 2.4, and proves them in its own
Appendix A. The release holds no other dated version of this manuscript, and its
history file records no change to it. Outside the family, the release's
Artin-conjecture manuscript, *Primitive roots for every admissible integer
base* (October 4, 2026), filed at
[[integer_sequences/openai_2026_primitive_roots_admissible_integer_base/_index|the Artin card]],
lists this manuscript as its reference [22] with the note "Section 3,
especially Lemmas 3.1 and 3.3". Its three citations all sit in the proof of
its Proposition 10.3, a rough-factor Type II estimate on which its Theorem 1.1
rests. They take Lemma 3.1, Lemma 3.3 (for the range of a bound quoted from
the Poisson--Dirichlet manuscript) and the classical Siegel--Walfisz estimate
that Proposition 2.1 here records without proof, and nothing from Sections
4--8 or from Theorem 1.1; the lemma pages give the citing passages. The
companions' arguments were not read for this card; only the statements of the
Poisson--Dirichlet Lemmas 2.3 and 2.4 were compared with Lemmas 3.1 and 3.3,
and the opening paragraph of its Appendix A was read. Of the Artin manuscript
only the citing passages were read.

Read status: claims checked for Theorem 1.1, Lemma 3.1, Lemma 3.3 and
Proposition 2.1, read clause by clause in the release's TeX source on
2026-10-12 (`build/main.tex`, abstract lines 40--44 and label `thm:main` at
lines 53--57; `build/sections/01-preliminaries.tex`, conventions lines 3--17
and label `pre:primes` at lines 24--40; `build/sections/02-long-prime.tex`,
labels `lp:prime-polynomial` at lines 8--21 and `lp:log-phase` at lines
185--197); the statements of Theorems 4.1, 6.1 and 7.1 and of the lemmas
numbered 3.2, 3.4--3.6, 5.1--5.3 and 8.1--8.9 were read as statements; all
proofs were read for their structure only and no step was checked; nothing
here is independently reviewed. The citing passages of the Artin manuscript
were read in its TeX source at the same revision (`sections/08-type-ii.tex`
lines 321--536, `sections/12-construction.tex` lines 83--127, where Lemma 12.1
invokes the proof of Proposition 10.3, and `references.tex` lines 148--153).
No search was made for earlier results on the parity of $\Omega(p-1)$.

## Contents

The PDF has 45 pages: eight sections and five references. Results share one
counter numbered within sections, and the printed page numbers are the PDF's.

- Section 1, Introduction (pp. 1--2). Defines $\Omega$ and $\omega$, states
  [[arithmetic_functions/openai_2026_prime_predecessors_even_number_prime_factors/theorem_1_1|Theorem 1.1]]
  (p. 1), and says that squarefreeness makes the two counting conventions
  agree. The plan: write $p=2u+1$ and build nonnegative weights on odd $u$
  with $\Omega(u)$ odd, with enough bilinear distribution to detect primes
  $2u+1$ and a negligible nonsquarefree part. It names the parity
  obstruction of sieve theory, cites the asymptotic sieve of Friedlander and
  Iwaniec (their Section 1) for the role of bilinear information and the
  smooth-shifted-prime work of Baker--Harman and Lichtman as context, and
  says the parity condition is not deduced from smoothness. Two analytic
  extensions are announced: cancellation in prime polynomials up to height
  $x^2$ through a logarithmic-phase estimate and a weak zero-free strip, and
  the cancellation of a shared dilation's sign, which occurs twice in a lifted
  correlation, by complete multiplicativity.
- Section 2, Conventions and classical estimates (pp. 2--4). Sets
  $L=\log x$, $T=\log L$, $W=\exp(\sqrt L)$; constants may depend on all
  previously fixed parameters and no effective threshold for $x$ is
  asserted. Proposition 2.1 (prime number theorem with any fixed
  log-power error, Mertens, Siegel--Walfisz for moduli up to $(\log y)^C$,
  constants not necessarily effective), Proposition 2.2 (the
  primitive-character large sieve, divisor moments, and mean values of
  Dirichlet polynomials on intervals and at spaced points), Proposition 2.3
  (first and second derivative tests), all recorded without proof in the
  forms of S's Section 2 (Proposition 2.2 is its Theorem 2.3 and Lemmas
  2.5--2.6, Proposition 2.3 its Lemma 2.7), and Lemma 2.4 (smooth separation
  of variables by Fourier inversion), an elementary version of S's Lemma 2.8
  proved here.
- Section 3, A long prime polynomial (pp. 4--11). States
  [[arithmetic_functions/openai_2026_prime_predecessors_even_number_prime_factors/lemma_3_1|Lemma 3.1]]
  (p. 4). Lemma 3.2 (p. 5): a Vinogradov mean-value bound uniform in the
  degree, $J_{s,k}(M)\le\exp(C_1k^{C_2})M^{2s-k(k+1)/2+1/100}$ for some
  $s\le C_1k^4$, by Linnik's $p$-adic iteration (exposition cited to
  Wooley 2012, Section 2; efficient congruencing not used).
  [[arithmetic_functions/openai_2026_prime_predecessors_even_number_prime_factors/lemma_3_3|Lemma 3.3]]
  (p. 7). Lemmas 3.4--3.6 (pp. 8--10), for Dirichlet $L$-functions
  $D(s,\chi)$ of modulus at most $L^C$: $\log|D|\ll T^2$ within $10T^4/L$ of
  the line $\operatorname{Re}s=1$ at heights $1/2$ to $3x^3$, a local formula
  for $D'/D$ through $O(T^2)$ nearby zeros, and no zero in
  $\operatorname{Re}s\ge1-cT^2/L$, $1\le|\operatorname{Im}s|\le x^3$. The
  proof of Lemma 3.1 closes the section (pp. 10--11).
- Section 4, A prime-slot shifted correlation with a common parity twist
  (pp. 12--22). Fixes disjoint groups of primes (small ones in
  $[\exp(L^a),\exp(L^b)]$, big ones in $[\exp(L^c),\exp(L^d)]$,
  $0<a<b<c<d<0.47$, of order $T$ groups of each kind), marked weights
  $W_{\mathbf t}$ that count marked group-prime divisors with a damping
  factor $q_0$ per unmarked one, a sign $\varepsilon$ equal to $1$ or to $-1$
  raised to the number of group-prime factors counted with multiplicity, and
  endpoint cores $F(n)$: sums over the factorizations $n_*=mpr$, where $n_*$
  is the part of $n$ prime to the groups, of a $W$-rough coefficient
  $\alpha_m$ twisted by a character and a phase, a prime $p$ in a slot
  $I_p\subset[x^\tau,x^\eta]$, $\eta<1/4$, with a phase, and a coefficient
  $c_r$, with $|\alpha_m|,|c_r|\le L^C$. Theorem 4.1
  (p. 13): if the coefficients $\alpha$ of one core have discrepancy at most
  $L^{-B}$ against characters of modulus up to $L^B$ and phases $m^{it}$,
  $|t|\le L^B$, then the harmonic shifted correlation of $\overline{F(z)}$
  with $G(z+k)$, weighted by $W_\ell$ and the same sign at both ends, is
  $\ll L^{-D_0}$ at scales $Z$ within a power of $L$ of $x$ and for shifts
  $0<|k|\le L^C$. Propositions 4.2 and 4.3 restate the imported graph inputs
  (S's Theorem 3.5, Corollary 3.11 and Lemma 3.4; S's Theorem 4.1 and
  Lemma 4.3), and S's integer bilinear estimate (its Lemma 4.2) is quoted.
  The proof removes the shared dilation by $\varepsilon(D_R)^2=1$ ((4.18),
  p. 16), then treats the comparison terms by minor and major arcs, the local
  Mellin energy of Lemma 4.4 (p. 19, from S with proof), a factorial bound on
  the exceptional times of a small-prime polynomial, Lemma 3.1 on the prime
  slot, and the discrepancy hypothesis at low heights. Remark 4.5 (p. 22)
  fixes the order of choices.
- Section 5, Candidate weights and their mass (pp. 22--26). Ordinary bands
  $Q_j$ ($\log p\in[s_j,\tfrac65s_j]$, $s_j=s'2^{-j}L$) each contribute
  exactly $r_0$ primes, $r_0$ a fixed even integer; groups $\mathcal P_g$ in
  $[L^{1/10},L^{1/5}]$ and $[L^{3/10},L^{2/5}]$ (in $\log p$) carry the marks
  with $q_0=1/2$, $\ell=1$. The weight $A(u)$ keeps an odd number of
  group-prime factors, so $A(u)>0$ forces $\Omega(u)$ odd and $\Omega(2u)$
  even ((5.5), p. 23). Lemma 5.1 bounds the group part's tail; Lemma 5.2
  (p. 24) gives the total mass $X_A\asymp(x/L)H_QH_P\gg xL^{-C_A}$; Lemma 5.3
  (p. 25) shows that $u$ with $2u$ not squarefree carry $o(X_A/L)$.
- Section 6, Bilinear distribution (pp. 26--33). Theorem 6.1 (p. 26), the
  Type II estimate: for $mn=2u+1$ with $m,n$ in dyadic ranges inside
  $[x^{b_*},x^{1-b_*}]$, bounded-by-$L^C$ coefficients, and the $m$
  coefficient $W$-rough and of small discrepancy, the sum against
  $A(u)\Psi(u/x)$ is $\ll xL^{-D_*}$, with no condition on the $n$
  coefficient. Proof by a designated prime slot, a smooth allocation of the
  band primes, Fourier separation, Cauchy--Schwarz and a change of variables
  that turns the off-diagonal terms into correlations covered by Theorem 4.1,
  once for $\varepsilon=1$ and once for the parity sign. Remark 6.2 (p. 33)
  orders the later proxy precision after the discrepancy exponent.
- Section 7, Distribution in congruence classes (pp. 33--36). Theorem 7.1
  (p. 33): the remainders $r(d)$ of the weight on $d\mid 2u+1$ against
  $X_A/\varphi(d)$, summed over odd squarefree $d\le x^\vartheta$,
  $\vartheta<1/2$, are $\ll xL^{-D}+X_AL^{-18}$, from one prime of the band
  $Q_0$, the large sieve for large conductors and Siegel--Walfisz for small
  ones.
- Section 8, Prime extraction (pp. 36--45). Imports Lemma 8.1 (block sieve,
  S's Lemma 2.9) and Lemma 8.2 (local-density proxies for the prime and
  $x^\gamma$-rough indicators on logarithmic cells of width $L^{-S_1}$, with
  their discrepancy and density bounds, S's Lemmas 7.3--7.4). Lemmas 8.3--8.4
  (p. 39) give a positive pair bound by a masked sieve. Lemma 8.5 (p. 42)
  replaces tests by proxies through Theorem 6.1. Lemma 8.6 (p. 42) is the
  presieve to $P^-(2u+1)>x^{b_1}$, with the singular series
  $\mathfrak S=2\prod_{p\ge3}(1-(p-1)^{-2})$. Lemmas 8.7--8.8 (p. 43) remove
  the composites whose least prime factor lies in $(x^{b_1},x^{1/2-\kappa}]$
  by Buchstab's identity, leaving at least $\mathfrak SX_A/(2L)$. Lemma 8.9
  (p. 44) bounds the products of two primes near $\sqrt x$ by
  $C_{\rm bal}(\kappa+1/L)X_A/L$ up to $o(X_A/L)$. The proof of Theorem 1.1
  (pp. 44--45) combines them.
- References (p. 45): Baker--Harman (1998), Friedlander--Iwaniec (1998),
  Lichtman (arXiv:2211.09641v1), S, and Wooley (2012).

The manuscript flags nothing as numerical, computer-assisted or conditional;
it asserts no effective threshold for $x$, and its Siegel--Walfisz inputs may
have ineffective constants. The release folder holds only the README, the PDF
and the TeX build directory; there is no `verification/` folder.

## Bears on

The manuscript names no Erdős problem, and no problem page is identified as
using it. A search of the problem pages' statements and assessments for the
squarefreeness or the parity of the number of prime factors of $p-1$, for
$\mu(p-1)$, $\Omega(p-1)$ and $\omega(p-1)$, and for shifted primes found no
page whose question or recorded argument turns on these objects: the pages
that use smooth shifted primes (Problems 821 and 1057) rest on the
smoothness of $p-1$, which this manuscript does not address, and the mention
of the parity problem on the page of Problem 385 concerns semiprimes in short
intervals. Lemmas 3.1 and 3.3 reach problem pages only at second hand,
through the Artin manuscript's Theorem 1.1, whose card records its own rows
(Problems 985 and 429); this card adds none.
