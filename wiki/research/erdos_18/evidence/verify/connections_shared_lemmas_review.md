---
name: research/erdos_18/evidence/verify/connections_shared_lemmas_review
title: "Independent review of the connections section: Shared lemmas"
desc: |
  Refutation-failed for Lemmas A, B, C and C′ and for the counting
  inequality of Lemma D; the asymptotic floor of Lemma D is
  refuted-as-stated when its seed is unrestricted, and its "hence" sentence
  is then unresolved, both repaired by a fixed-seed clause. Two required
  corrections.
created: 2026-09-28T17:59:34Z
updated: 2026-09-28T17:59:34Z
---

***

## Subject and independence

Role: independent reviewer in a fresh context, given only the commission.
The reviewer took no part in writing the subject page, the reconstruction
pages of the folder, or any earlier review of them. Charge: refutation of
the author-recorded mathematics of one section.

Subject: page `wiki/research/erdos_18/connections.md` as it stood at
2026-09-28T13:50:48Z, section `## Shared lemmas`, lines 47–243 (from the H2
heading to the line before `## Problem 304`). The subject page is the lead page;
no other lead was named.

Read in full as of the same time: the section; the page's preamble (lines 1–46,
the standing sentence and the Conventions paragraph) as an input; the
reconstruction pages `hughes_lemma_4_reconstruction.md`,
`hughes_theorem_1_reconstruction.md`,
`hughes_corollary_3_reconstruction.md`, `doorn_lemma_3_1_reconstruction.md`,
`doorn_lemma_3_3_reconstruction.md`,
`doorn_corollary_3_4_reconstruction.md`,
`doorn_proposition_4_1_reconstruction.md` and
`doorn_theorem_1_1_reconstruction.md` of the folder, taken as premises at
their reviewed standing; the Statement paragraphs of
`wiki/problems/divisors/E0018/_index.md`,
`wiki/problems/unit_fractions/E0304/_index.md` and
`wiki/problems/unit_fractions/E0293/_index.md`; the provenance paragraphs of the
two library cards; the held PDFs, namely Hughes (2026) p. 2 on the page
image (Theorem 2 as quoted, Corollary 3, Lemma 4) with the extracted text
of pp. 1–3, and van Doorn (2026) pp. 2, 3 and 6 on the page images (Lemma
3.1 with its proof, Lemma 5.1 with its proof) with the extracted text of
pp. 1, 4 and 5 (the definitions of $Q(k)$ and $t(k)$, Lemma 3.3, Corollary
3.4, Proposition 4.1); `docs/verification.md` sections "Grading and claim
standing", "Audit checklist", "Whole-claim report" and the shared audit
checklist; `docs/approach_vetting.md`; `docs/evidence.md` section "Source
fidelity"; `docs/math_authoring.md`.

Exposures. (1) The three problem pages carry, between their Statement and
their first H2, a bold Status paragraph with known bounds and proof-claim
summaries, and their frontmatter `desc` and `status` fields; these were
printed together with the Statement and were read. No Current assessment
or Known results section was read. (2) The two library cards' generated
link rows, their Read status and Bears on paragraphs, and the opening of
the Hughes card's Overview were printed with the provenance paragraph and
were read. (3) The reconstruction pages carry Standing paragraphs that
describe their sources' standing; they were read as parts of those pages.
Nothing under any `evidence/` folder, no `_index.md`, no other section's
review and no web search was consulted.

## Restatement

Throughout, $h(N)$ is the page's fresh-set count over $1\le m\le N$,
practical means every $1\le m\le N$ is a sum of distinct divisors of $N$,
$\tau$ is the divisor count and logarithms are natural unless subscripted.

S1 (Lemma A). Let $N\ge1$ be an integer such that
$v_2(N)\ge\lfloor\log_2p\rfloor$ for every odd prime $p$ dividing $N$.
Then (a) any two consecutive divisors $d<b$ of $N$ satisfy $b\le2d$; (b)
by the consequence clause of the Lemma 4 page, the greedy expansion of
every $1\le m\le N$ terminates and writes $m$ as a sum of distinct
divisors of $N$, so $N$ is practical; (c) $h(N)\le\log_2N+1$; (d) the
hypothesis holds for $N=n!$ for every $n\ge1$, for $N=\mathrm{lcm}(1,\dots,x)$
for every $x\ge1$, and for $N=p^jM$ whenever it holds for $M$, $p$ is an
odd prime, $j\ge1$ and $\lfloor\log_2p\rfloor\le v_2(M)$.

S2 (Lemma B). Let $N$ have property (a) of S1, let $T\ge2$ be real with
$2T\le\sqrt N$, let $\delta\colon[T,\sqrt N]\to(0,1/8]$ be nonincreasing,
and suppose every pair of consecutive divisors $d<b$ of $N$ with
$T\le\sqrt{db}\le\sqrt N$ has $\log(b/d)\le\frac12\delta(\sqrt{db})$. Put
$\sigma(\ell)=\log(1/\delta(e^\ell/2))$ for
$\log(2T)\le\ell\le\frac12\log N$. Then $\sigma$ is nondecreasing,
$\sigma\ge\log8$, and

$$
h(N)\le3\int_{\log(2T)}^{\frac12\log N}\frac{d\ell}{\sigma(\ell)}
+\log_2\sigma\bigl(\tfrac12\log N\bigr)+2\log_2(2T)+5 ,
$$

with the constants $3$, $2$ and $5$ absolute.

S3 (Lemma C). Let $n\ge b\ge2$ be integers with $n$ practical and
$1\le a<b$. Then there are $s+t\le2h(n)$ distinct integers greater than
$1$ whose reciprocals sum to $a/b$, of which $s$ are divisors of $n$ (in
$(1,n]$) and $t$ are of the form $bn/e$ with $e\mid n$, each greater than
$n$. If $b\nmid n$, none of them equals $b$.

S4 (Lemma C′). Let $b$ be a sufficiently large integer, $n$ the least
integer with $n!\ge b$, $p$ the least prime not dividing $n$, and
$N=n!$ if $b\nmid n!$, else $N=p^j(n-1)!$ with
$j=\lceil\log n/\log p\rceil$. Then $N$ is practical, $N\ge b$,
$b\nmid N$, and $h(N)\le\max(h(n!),h((n-1)!)+\lceil\log_2n\rceil)$. The
parenthetical asserts $p\le n-1$ and $p\ll\log n$.

S5 (Lemma D, first inequality). For every practical $n_0$ and every chain
$n_{j+1}=A_jn_j$, $0\le j<J$, with $A_j\ge2$, in which every residue
modulo $A_j$ is a sum of at most $L_j$ distinct divisors of $n_j$,
$L_j\ge\log A_j/\log(\tau(n_j)+1)$ for each $j$, hence for the sums over
$j<J$.

S6 (Lemma D, second inequality). Under the hypotheses of S5,

$$
\sum_{j<J}\frac{\log A_j}{\log(\tau(n_j)+1)}
\ge\Bigl(\frac1{2\log2}-\epsilon(n_J)\Bigr)(\log\log n_J)^2
$$

with $\epsilon(x)\to0$ as $x\to\infty$, where, as written ("uniformly
over all such chains"), $\epsilon$ depends on neither the chain nor its
seed $n_0$.

S7 (Lemma D, "Hence" sentence). For every such chain,
$h(n_0)+\sum_{j<J}L_j\ge(1/(2\log2)-\epsilon(n_J))(\log\log n_J)^2$ with
the same $\epsilon$; this includes $J=0$, where the chain is the seed
alone.

S8 (closing paragraph). (a) No certificate built from Lemma 3.1 extensions
alone from a fixed seed can prove $h(N)\le(\log\log N)^{2-\eta}$ for any
fixed $\eta>0$, or $h(N)\le c(\log\log N)^2$ with $c<1/(2\log2)$, for all
large $N$ along the chain. (b) In the van Doorn chain each step costs $4$
while $\log A_j/\log\tau(n_j)\to6/7$. (c) Its primes of size $k^6\log k$
make $\log\tau(n_j)$ about one sixth of the maximal order
$(\log2)\log n_j/\log\log n_j$. (d) $c_0=14/\log2\approx20.2$ is $28$
times $1/(2\log2)\approx0.72$.

## Checklist

- Quantifiers and scope: defect in S6 and S7. "Let $n_0$ be practical"
  quantifies the seed universally and "uniformly over all such chains"
  removes the seed from the error term; under that reading S6 is false
  (F1) and S7 is unproved (F2). S1–S5 and S8 state their quantifiers
  exactly; S8 carries the "fixed seed" clause that S6 and S7 lack.
- Circularity: pass. No statement is assumed in its own proof; Lemma A
  reproves the ratio property rather than citing the Lemma 4 page's
  factorial case, and Lemma D's floor uses only counting and an external
  maximal-order bound.
- Model and convention changes: pass. The page's $h$ (over $m\le N$) is
  the convention of the Lemma 4, Theorem 1 and Lemma 3.1 pages, and Lemma
  C uses it only for $q<n$ and $r<n$, so the site's $h$ also serves. Lemma
  B transports the Theorem 1 count to an arbitrary profile; the bridge
  (facts (i) and (ii) and Lemma 4 hold for every $N$) was checked, not
  assumed from the shape of the formulas.
- Finite and statistical overreach: pass. No finite check is used as a
  proof on the page. Lemma C′'s "sufficiently large" is honest: $b=2$
  gives $n=2$, $p=3>n-1$ and $N=3$, which is not practical. The exact
  checks reported below are attacks, not warrants.
- Uniformity: defect in S6 (F1). The proof's $O_\eta(1)$ silently contains
  $(\log\log n_0)^2$ when the seed already exceeds the Wigert threshold.
  Lemma B's constants are explicit and absolute; Lemma A's bound is
  explicit; Lemma C′'s bound is explicit in $n$.
- Extremal conclusions: pass with F2. The floor of Lemma D is stated in
  its own units, $(\log\log n_J)^2$ with the constant $1/(2\log2)$, and
  the "never below" of S7 is exactly the sentence that overreaches for
  unrestricted seeds. The arithmetic of S8(d), $28=(4/(6/7))\cdot6$, was
  recomputed.
- Consequences and composition: pass except F2. Lemma A's "Consequently"
  was checked against the Lemma 4 page's consequence clause; Lemma C′
  composes Lemma A with Lemma 3.1 and supplies every hypothesis of the
  latter ($A=p\ge2$, seed practical, residues by one divisor each, total
  at most the seed, no summand divisible by $p$); Lemma D's "Hence" is
  F2.
- Computation: pass. The page computes only $28$, $6/7$, $0.72$ and
  $20.2$; all were recomputed. The reviewer's own exact checks are
  described under Strongest attack with their coverage.
- Reproduction: inapplicable. The section states no rerun command and no
  coverage claim.
- Source and verdict fidelity: pass with a note (F5). Lemma C matches
  Lemma 5.1 on the p. 6 image clause for clause; Lemma 3.1's interface
  matches p. 2; "pays $4$ per step" matches Corollary 3.4 on p. 5;
  $Q(k)=k^6\log k$ and $t(k)$ match p. 4; Lemma 4 and Corollary 3 match
  Hughes p. 2. The attribution "as the Problem 304 page records" lies
  outside the read set.

## Weakest steps

W1 (Lemma D, the asymptotic floor). Write $\ell_j=\log n_j$ and
$f(\ell)=\log\ell/\ell$, decreasing for $\ell>e$. The maximal order of
$\tau$ gives $\log(\tau(n)+1)\le(\log2+\eta'(n))\log n/\log\log n$ with
$\eta'(n)\to0$; fix $\eta>0$ and a threshold $n(\eta)$ beyond which
$\eta'\le\eta$ and $\log n>e$. For $n_j\ge n(\eta)$, S5 gives
$L_j\ge(\ell_{j+1}-\ell_j)f(\ell_j)/(\log2+\eta)$, and because $f$
decreases, the left Riemann sum over $j\ge j(\eta)$ dominates
$\int_{\ell_{j(\eta)}}^{\ell_J}f=\frac12\bigl((\log\ell_J)^2-(\log\ell_{j(\eta)})^2\bigr)$.
If $j(\eta)\ge1$, the step $j(\eta)-1$ has $n_{j(\eta)-1}<n(\eta)$, so by
S5 and $\tau(n)\le n$ its cost is at least
$(\ell_{j(\eta)}-\log n(\eta))/\log(2n(\eta))$, linear in
$\ell_{j(\eta)}$; this exceeds $(\log\ell_{j(\eta)})^2$ once
$\ell_{j(\eta)}\ge C(\eta)$, and otherwise
$(\log\ell_{j(\eta)})^2\le(\log C(\eta))^2$. Either way
$\sum_jL_j\ge(\log\ell_J)^2/(2(\log2+\eta))-O_\eta(1)$, and letting
$\eta\to0$ gives S6 with $\epsilon$ depending only on $n_J$. If
$j(\eta)=0$, that is $n_0\ge n(\eta)$, nothing compensates the subtracted
$(\log\ell_0)^2=(\log\log n_0)^2$: the argument yields only
$\sum_jL_j\ge\bigl((\log\log n_J)^2-(\log\log n_0)^2\bigr)/(2(\log2+\eta))$,
which is empty when $n_J$ is a bounded multiple of $n_0$. The witness in
F1 shows this is not a weakness of the proof but of the statement.

W2 (Lemma B, the upper range). For a nonterminal remainder
$\sqrt N<R\le N/(2T)$ with bracketing divisors $d<R<b$, put $U=N/R$, so
$2T\le U<\sqrt N$. The map $x\mapsto N/x$ reverses the divisor order, so
$N/b<U<N/d$ are consecutive divisors with ratio $b/d$. From $d>R/2$ and
$b<2R$ (property (a) of S1) one has $R/\sqrt2<\sqrt{db}<\sqrt2R$, hence
$U/\sqrt2<N/\sqrt{db}<\sqrt2U$; fact (ii) of the Theorem 1 page ($R>\sqrt N$
forces $db\ge N$) gives $N/\sqrt{db}\le\sqrt N$, and $U\ge2T$ gives
$N/\sqrt{db}>\sqrt2T\ge T$. So the hypothesis applies to the mirror pair:
$\log(b/d)\le\frac12\delta(N/\sqrt{db})\le\frac12\delta(U/2)$, the last by
monotonicity since $N/\sqrt{db}>U/2\ge T$. Lemma 4 at the actual remainder
gives $R'=R-d\le2R\log(b/d)\le R\,\delta(U/2)$, so
$\log U'-\log U\ge\sigma(\log U)$. The starts $\log U_i$ of the
upper-range steps increase and lie in $[\log(2T),\frac12\log N)$. With
$J_k=\{\ell:2^k\log8\le\sigma(\ell)<2^{k+1}\log8\}$, an interval because
$\sigma$ is monotone, the starts in $J_k$ form a run, consecutive members
of which differ by at least $\sigma(\log U_i)\ge2^k\log8$; so $M_k$ starts
in $J_k$ force $|J_k|\ge(M_k-1)2^k\log8$, while
$\int_{J_k}d\ell/\sigma\ge|J_k|/(2^{k+1}\log8)$, giving
$M_k\le1+2\int_{J_k}d\ell/\sigma$. There are at most
$K=\lfloor\log_2(\sigma(\frac12\log N)/\log8)\rfloor+1$ classes. Adding
the lower range ($1+\int$), the two endgames (each at most
$\log_2(2T)+1$ halving steps) and the terminal divisor gives
$3\int+K+2\log_2(2T)+4\le3\int+\log_2\sigma(\tfrac12\log N)+2\log_2(2T)+5-\log_2\log8$,
which is below the stated bound. The lower-range charging needs $\sigma$
at the upper end of each step's interval to dominate the integrand, which
nondecreasing $\sigma$ supplies; the last lower-range step may leave
$[\log(2T),\frac12\log N]$ and is counted by the $1$.

W3 (Lemma C′, the second case). If $b\mid n!$, then $b\nmid(n-1)!$
because $(n-1)!<b$ by the minimality of $n$ (for $n\ge2$). For
$N=p^j(n-1)!$ with $p\nmid n$,
$\gcd(n!,N)=(n-1)!\gcd(n,p^j)=(n-1)!$, so $b\mid N$ together with
$b\mid n!$ would give $b\mid(n-1)!$, a contradiction; and $p^j\ge n$ gives
$N\ge n!\ge b$. For the practicality and the cost, the residues
$1\le c\le p-1$ modulo $p$ are each a single divisor of $(n-1)!$, hence
of $p^i(n-1)!$, not divisible by $p$ and of total $c\le p^i(n-1)!$, and
the residue $0$ is the empty sum; this is the hypothesis of Lemma 3.1 with
$A=p$ and $L=1$, valid exactly when $p-1\le n-1$, that is $p\le n$, which
with $p\nmid n$ is $p\le n-1$. Applying Lemma 3.1 $j$ times from the
practical number $(n-1)!$ (Lemma A) gives $h(N)\le h((n-1)!)+j$ and
$j\le\lceil\log_2n\rceil$ because $p\ge2$. The condition $p\le n-1$ holds
for every $n\ge3$: if every prime below $n$ divided $n$, their product
would be at most $n$, which fails for $n\ge4$, and $n=3$ has $p=2$. For
$n=2$ it fails ($p=3$), which is the $b=2$ case above.

## Strongest attack

S1. The attack looked for an $N$ meeting the hypothesis with a divisor
gap above $2$, concentrating on odd primes just below a power of two,
where $p/2^c$ is close to $2$ (for example $N=4\cdot7$ and $N=16\cdot31$),
and on the proof's step $v_2(d)=v_2(N)$, which needs $q=N/d$ odd and is
supplied by the case split. An exhaustive exact check of every $N\le3000$
satisfying the hypothesis confirmed the ratio property, that the greedy
divisors are distinct and sum to $m$ for every $1\le m\le N$, and that
their number is at most $\lfloor\log_2N\rfloor+1$; the hypothesis is not
vacuous ($N=10$ fails it and has the consecutive divisors $2<5$). The
factorial, lcm and $p^jM$ cases were rederived, including
$\lfloor n/2\rfloor\ge\lfloor\log_2n\rfloor$ for $n\ge4$ and the three
values $N=1,2,6$ for $n\le3$. The attack failed.

S2. The attack targeted the direction of monotonicity in each range (the
lower range bounds a descent by $\sigma$ at the upper end of the step's
interval, the upper range an ascent by $\sigma$ at the lower end, which is
why the dyadic classes are needed), the domain of $\delta$ at each
evaluation ($R/2$, $U/2$, $\sqrt{db}$ and $N/\sqrt{db}$ all lie in
$[T,\sqrt N]$ when $R\ge2T$ or $U\ge2T$), the possibility of many starts in
one class (excluded by the forced separation $2^k\log8$), the boundary
steps (the last lower-range step, counted by $1$; runs whose last ascent
leaves the interval, which the count of starts ignores) and the constant
bookkeeping, which has slack $\log_2\log8$. The bookkeeping was also
exercised on $N=10!,11!,12!$ with $\delta$ read off the actual gaps and
$T$ the least power of two admissible under the hypothesis: the greedy
steps of sampled $m$ in each of the four ranges stayed within that
range's bound. The attack failed.

S3. The attack targeted distinctness across the two groups (settled by
$n/d_i\le n<bn/e_j$), the degenerate cases $r=0$ (empty second group)
and $q\ge1$ (forced by $an\ge n\ge b$), and the last clause, which fails
without $b\nmid n$: for $n=b$ and $a=1$ the representation is $1/b$
itself. An exhaustive exact-rational check over every practical $n\le48$,
every $2\le b\le n$ and every $1\le a<b$ confirmed the sum, the
distinctness, the bound $2h(n)$ and the avoidance of $b$ when $b\nmid n$.
The attack failed.

S4. The attack targeted the choice of $p$ (it must avoid $n$, not $b$;
the gcd computation shows why), the case $p=2$ for odd $n$ (the single
residue $1$), the inequality $p\le n-1$ (W3), and small $b$: $b=2$ breaks
the lemma ($N=3$), so "sufficiently large" cannot be removed, while an
exact computation of $h$ for the factorials and prime-power multiples
involved confirmed every clause for $3\le b\le2000$. The attack failed.

S5. Each residue class needs its own representing subset, since a subset
has one sum. The number of subsets of a $\tau$-set with at most $L$
elements is
$\sum_{i\le L}\binom\tau i\le\sum_{i\le L}\binom Li\tau^i=(\tau+1)^L$.
The attack failed.

S6. Witness: $n_0=2^k$ (practical by binary expansion), $J=1$, $A_0=3$,
$L_0=1$, since the residues $0,1,2$ modulo $3$ are the empty sum, the
divisor $1$ and the divisor $2$, with totals at most $n_0$ and no summand
divisible by $3$; $n_1=3\cdot2^k$. The middle term of the display is
$\log3/\log(k+2)<1$, the left is $1$, and the right is
$(1/(2\log2)-\epsilon(3\cdot2^k))(\log(k\log2+\log3))^2\to\infty$ for any
$\epsilon\to0$ (about $30.9$ at $k=1000$). The statement as written is
refuted; W1 locates the gap. Restricted to seeds $n_0\le C$ for a fixed
$C$, the proof of the page closes with the one-line addition that the
subtracted $(\log\log n_0)^2$ is then $O_C(1)$, and no attack against that
version succeeded.

S7. The witness of S6 does not refute S7, because $h(2^k)=k$. But for
$J=0$ and unrestricted seed, S7 reads
$h(n_0)\ge(1/(2\log2)-o(1))(\log\log n_0)^2$ for every practical $n_0$, a
lower bound for $h$ that the page itself disclaims ("not a lower bound for
$h$") and that no argument on the page supports; the counting bound gives
only $h(n)\ge\log n/\log(\tau(n)+1)\gg\log\log n$. No disproof is known to
the reviewer. For seeds bounded by a fixed $C$, S7 follows from the
repaired S6 since $h(n_0)\ge0$.

S8. (a) follows from the repaired S6 with $h(n_0)$ a constant. For (b),
(c) and (d) the Lemma 3.3 and Proposition 4.1 pages give
$\tau(n_j)=(E+1)2^{k_j}$, $A_j$ a product of $t(k_j)$ primes in
$(Q(k_j),2Q(k_j)]$ with $Q(k)=k^6\log k$ and
$t(k)=\lfloor k\log2/(7\log k+3\log\log k)\rfloor$, so
$\log A_j=t(k_j)(6\log k_j+O(\log\log k_j))=(6/7+o(1))k_j\log2$ and
$\log A_j/\log(\tau(n_j)+1)\to6/7$; $\log V_j=\sum_{i<j}t(k_i)\log Q(k_i)+O(1)$
compares with $6\int^{k_j}\log k\,dk$, so $\log n_j\sim6k_j\log k_j$ and
the maximal order $(\log2)\log n_j/\log\log n_j\sim6k_j\log2$ is six times
$\log\tau(n_j)\sim k_j\log2$; and $(14/\log2)/(1/(2\log2))=28=(4/(6/7))\cdot6$.
The van Doorn chain's certified cost $4j$ with $j\sim(c_0/4)u_j^2$ exceeds
its own Lemma D sum $\sim(6/7)j$ by the factor $14/3$ and the universal
floor by $28$, consistently. The attack failed.

## Premises

- [[research/erdos_18/hughes_lemma_4_reconstruction|Lemma 4 page]]: for
  $N$ whose consecutive divisors have ratio at most $2$ and a nonterminal
  remainder $1\le R\le N$ with bracketing divisors $d<R<b$,
  $R-d<d$ and $R-d\le2R\log(b/d)$; the compilation-supplied consequence
  that the greedy expansion of every $1\le m\le N$ terminates and writes
  $m$ as a sum of distinct divisors. Independently reviewed as of
  2026-09-28T05:03:27Z per the commission; read in full; the source lemma
  checked on Hughes p. 2.
- [[research/erdos_18/hughes_theorem_1_reconstruction|Theorem 1 page]]:
  facts (i) ($R\le\sqrt N$ forces $db\le N$) and (ii) ($R>\sqrt N$ forces
  $db\ge N$), whose proofs use only that $N/x$ permutes the divisors, and
  the lower-range charging argument. Same standing; read in full.
- [[research/erdos_18/hughes_corollary_3_reconstruction|Corollary 3 page]]:
  the conventions $\varepsilon_j$ and the windows named in the page's
  Conventions; not otherwise consumed by the section. Read in full.
- [[research/erdos_18/doorn_lemma_3_1_reconstruction|Lemma 3.1 page]]:
  for $A\ge2$ and practical $n$, if every residue modulo $A$ is a sum of at
  most $L$ distinct divisors of $n$ with total at most $n$ and no summand
  divisible by $A$, then $An$ is practical and $h(An)\le h(n)+L$. Same
  standing; read in full; statement and proof checked on van Doorn pp.
  2–3.
- [[research/erdos_18/doorn_lemma_3_3_reconstruction|Lemma 3.3 page]],
  [[research/erdos_18/doorn_corollary_3_4_reconstruction|Corollary 3.4 page]],
  [[research/erdos_18/doorn_proposition_4_1_reconstruction|Proposition 4.1 page]]
  and
  [[research/erdos_18/doorn_theorem_1_1_reconstruction|Theorem 1.1 page]]:
  the definitions of $Q(k)$, $t(k)$, $c_0$, the cost $4$ per step, the
  construction $n_j=2^EV_j$ and its size estimates, used only for S8(b)–(d).
  Same standing (claimed results, reconstructed); read in full; checked
  against van Doorn pp. 4–6.
- [[../library/divisors/hughes_2026_sums_distinct_divisors_factorials/_index|Hughes (2026)]],
  held: p. 2 read on the page image, pp. 1–3 in extracted text.
- [[../library/divisors/doorn_2026_practical_numbers_egyptian_fractions/_index|van Doorn (2026)]],
  held: pp. 2, 3, 6 read on the page images, pp. 1, 4, 5 in extracted
  text. Lemma 5.1 (p. 6) states exactly S3 and is called well known there.
- Wigert's maximal order of $\tau$, used by Lemma D in the form
  $\log\tau(n)\le(\log2+\eta(n))\log n/\log\log n$ with $\eta(n)\to0$: a
  classical theorem, not held in the library, imported by the page without
  a citation; the form is the standard one and was accepted.
- An elementary lower bound for the product of the primes below $p$
  (Chebyshev type), silently behind the aside $p\ll\log n$ in Lemma C′;
  not held, not used by the proof (F4).
- The Statement paragraphs of Problems 18, 304 and 293 for the
  conventions $h$, $N(a,b)$, $N(b)$, $D_k$ and $v(k)$; read as stated.
- Explicit assumptions of this review: the reconstruction pages are taken
  as established at their reviewed standing, and the Lemma 3.1 page's
  result is consumed as a *claimed* result whose proof was nevertheless
  rechecked on the source pages because Lemma C′ and Lemma D rest on its
  interface.

## Findings

F1 (required). Location: Lemma D, Statement, "where the $o(1)$ tends to
$0$ as $n_J\to\infty$ uniformly over all such chains", together with "Let
$n_0$ be practical". Defect: the second inequality is false when the seed
is unrestricted; the proof handles the first index $j(\eta)$ only when a
step precedes it ("The step $j(\eta)-1$, if it exists"), and when it does
not exist the subtracted $(\log\ell_{j(\eta)})^2=(\log\log n_0)^2$ is
absorbed into $O_\eta(1)$ without justification. Witness: $n_0=2^k$,
$J=1$, $A_0=3$, $L_0=1$, for which the middle term is
$\log3/\log(k+2)<1$ while the right side tends to infinity with $k$.
Replacement: "where, for each fixed $C$, the $o(1)$ tends to $0$ as
$n_J\to\infty$ uniformly over all such chains with $n_0\le C$", and in
the proof, after "the other steps contribute nonnegatively": "if
$j(\eta)=0$, then $\ell_{j(\eta)}=\log n_0\le\log C$ and the subtracted
term is $O_C(1)$", with $O_\eta(1)$ read as $O_{\eta,C}(1)$.

F2 (required). Location: Lemma D, Statement, "Hence the bound
$h(n_0)+\sum_jL_j$ that such a chain certifies for $h(n_J)$ is never below
$(1/(2\log2)-o(1))(\log\log n_J)^2$." Defect: for unrestricted seeds this
sentence, at $J=0$, asserts the lower bound
$h(n_0)\ge(1/(2\log2)-o(1))(\log\log n_0)^2$ for every practical $n_0$,
which the page does not prove and elsewhere disclaims; the sentence is
proved only for seeds bounded by a fixed $C$, which is what the following
paragraph's "from a fixed seed" means. Witness: none for a disproof; the
defect is an unsupported inference. Replacement: "Hence, for chains from
seeds $n_0\le C$, the bound $h(n_0)+\sum_jL_j$ that such a chain certifies
for $h(n_J)$ is never below $(1/(2\log2)-o(1))(\log\log n_J)^2$."

F3 (suggested). Location: Lemma D, Proof, "let $j(\eta)$ be the least
index with $n_{j(\eta)}\ge n(\eta)$". Defect: $n(\eta)$ is not defined;
the proof needs it to satisfy both $\eta'(n)\le\eta$ for $n\ge n(\eta)$
and $\log n(\eta)>e$, the latter so that $f$ decreases on the range of
the Riemann sum. Replacement: define $n(\eta)$ by these two properties
before introducing $j(\eta)$.

F4 (note). Location: Lemma C′, Statement, "(so $p\le n-1$: the primes
dividing $n$ have product at most $n$, whence $p\ll\log n$)". Defect: the
"whence" imports a lower bound for the product of the primes below $p$
without saying so, and the proof uses only $p\le n-1$, which holds for
every $n\ge3$ (W3); the lemma's "large" is still needed, as $b=2$ shows.
Replacement: "(so $p\le n-1$ for $n\ge3$, since the primes below $n$
cannot all divide $n$ once $n\ge4$)"; drop $p\ll\log n$ or mark it as an
unused aside.

F5 (note). Location: Lemma C, preamble, "it is the transfer behind Erdős's
1950 bound and behind Vose's, as the Problem 304 page records". The
attribution to the Problem 304 page lies outside this review's read set
and was not checked; the note's own introduction (pp. 1–2) supports the
mathematical attribution. No replacement proposed.

## Verdict

- S1 (Lemma A): refutation-failed.
- S2 (Lemma B): refutation-failed.
- S3 (Lemma C): refutation-failed.
- S4 (Lemma C′): refutation-failed.
- S5 (Lemma D, first inequality): refutation-failed.
- S6 (Lemma D, second inequality with the $o(1)$ uniform over all chains):
  refuted-as-stated, by the witness of F1; the same inequality with the
  seed bounded by a fixed constant survived every attack once the proof
  receives the one-line addition of F1.
- S7 (Lemma D, "Hence" sentence): proof defective; statement unresolved,
  for unrestricted seeds (F2); it follows from the repaired S6 for seeds
  bounded by a fixed constant.
- S8 (closing paragraph, fixed-seed obstruction and the van Doorn
  accounting): refutation-failed, its "from a fixed seed" being exactly
  the hypothesis the repaired S6 needs.

Limitations. Wigert's maximal order and the Berend–Harmse conventions were
accepted as imported; the reconstruction pages were consumed at their
reviewed standing and the note's results remain claimed; the exact checks
cover only the stated finite ranges and warrant nothing beyond the
derivations they accompany. This focused review assigns no tier and
changes no status.
