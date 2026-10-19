---
name: research/erdos_939/evidence/verify/connections_shared_results_review
title: "Independent review of the connections section: Shared results"
desc: |
  Focused refutation review of the Shared results section of the Problem 939
  connections page: all nine mathematical statements survive with the verdict
  refutation-failed, with zero required corrections, four suggested
  clarifications and three notes.
created: 2026-09-28T18:54:54Z
updated: 2026-09-28T18:54:54Z
---

***

## Subject and independence

**Role.** Independent reviewer in a fresh context, commissioned for
refutation of one section. The reviewer took no part in writing the
connections page, the reconstruction page, or any other page of the folder,
had no contact with the compilation that wrote them, and received only the
assignment text.

**Frozen subject.** The source as it stood on 2026-09-28T13:50:48Z (called
"the commit" below), path
`wiki/research/erdos_939/connections.md`, section `## Shared results`, lines
58 to 302 (from the H2 heading to the line before
`## Problem 939 at r = 4: the two-summand case`). The section holds Lemma 1
with its application paragraph and Corollary 1.1 (lines 60 to 146), Lemma 2
(lines 148 to 184), Theorem 3 and Corollary 3.1 with a coverage paragraph
(lines 186 to 238), and Proposition 4 with Corollary 4.1 (lines 240 to 301).
The paths named are what was read. The page's Conventions
paragraph (lines 35 to 56) was read as the section's notation input.

**Lead pages.** The assignment names none, and the section names none. The
page's $r=5$ section names a lead folder; it was not read.

**Read set and depth.**

- The connections page at the commit, whole, to locate the section
  boundaries; the section and the Conventions paragraph line by line.
- `wiki/research/erdos_939/theorem_1_reconstruction.md` at the commit,
  whole, as a premise (the identity, the data $J$, $t$, $v_\ell$, $P$, $B$,
  and the distinctness argument).
- The page `recalled_abc_abcd_bounds.md` of the source folder
  `corvaja_zannier_2011_abcd_function_fields` under
  `library/diophantine_problems/`, whole; the card `_index.md` of that
  source (provenance and reading coverage); and printed p. 438 (PDF p. 3) of
  the held journal PDF by text extraction, to confirm the two recalled
  bounds at claims level.
- `wiki/research/erdos_940/finite_core_reduction.md`, the section
  "Independent polynomial summands still reduce to fixed forms" only
  (statement and proof of the polynomial-factor proposition), read as the
  input consumed by Corollary 3.1; the proof was read because the section
  adapts that proof rather than the statement, so the bridge could only be
  checked against the proof's actual structure. The rest of that page was
  not read beyond its heading list.
- The Statement paragraph of `wiki/problems/diophantine_problems/E0939/_index.md`.
- `docs/verification.md` sections "Report contract", "Grading and claim
  standing" and "Audit checklist"; `docs/approach_vetting.md`;
  `docs/evidence.md` section "Source fidelity"; `docs/math_authoring.md`.

**Exposure.** Two incidental exposures, neither used: while locating the
Statement paragraph of the Problem 939 page, its frontmatter (a `desc` line
summarizing the problem's status and a `status` field) scrolled past; and
the connections page's other sections, read only to fix the section
boundaries, summarize in their own words what the target pages' assessments
record. No `_index.md`, no `evidence/` content, no review, grade, Current
assessment or Known results text was opened, and no web search was made.

## Restatement

- **S1 (Lemma 1).** Fix integers $r\ge2$ and $n\ge3$ and nonzero
  $A_1,\dots,A_n\in\mathbb Z[U,V]$ with $A_1+\cdots+A_{n-1}=A_n$, together
  with one presentation $A_i=c_i\prod_jH_{ij}^{e_{ij}}$ ($c_i$ a nonzero
  integer, $H_{ij}\in\mathbb Z[U,V]$, every $e_{ij}\ge r$, empty products
  allowed) such that $V^r$ divides $A_i$ whenever $|c_i|>1$; $A_1=K^r$ with
  $K\in\mathbb Z[U,V]$, $K(U,0)=\pm U^d$ and $K(0,V)=\pm V^{d'}$; and
  $A_2=c_2U^aV^b$ with $a+b\ge1$, the symbol $c_2$ being that of the
  presentation. For every integer $B\ge1$ divisible by every prime dividing
  some $c_i$ ($1\le i\le n$) and every integer $m\ge1$ with $\gcd(m,B)=1$
  and $A_i(m,B)>0$ for all $i$: each of $A_1(m,B),\dots,A_{n-1}(m,B)$ is
  $r$-powerful, their greatest common divisor is $1$, and $A_n(m,B)$ is
  $r$-powerful. For such a $B$: if every $A_i(U,B)\in\mathbb Z[U]$ has
  positive leading coefficient then the positivity holds for all large $m$;
  if $A_n(U,B)$ is nonconstant then the sums $A_n(m,B)$ over $m$ coprime to
  $B$ take infinitely many values; if $A_i(U,B)\ne A_j(U,B)$ for all
  $i\ne j\le n-1$ then the $n-1$ values are pairwise distinct for all but
  finitely many $m$.
- **S2 (application paragraph).** For each $r\ge6$ the Theorem 1 identity
  of the reconstruction page, written in $U,V$ with $X=U^r$ and $Y=V^r$,
  satisfies (i) to (iv) with $A_1=(U^r-V^r)^r$, $K=U^r-V^r$,
  $A_2=2rU^{r(r-1)}V^r$, the other binomial and split terms as monomials,
  $A_n=(U^r+V^r)^r$ and $n=r-1$; and with $B=B_0=\prod_{p\in P}p$ and
  $m=q$ a prime above $B_0$, Lemma 1 returns the reconstruction's
  conclusions except distinctness.
- **S3 (Corollary 1.1).** $r\ge6$. (a) For every positive multiple $B$ of
  $B_0$ and every integer $m>B$ with $\gcd(m,B)=1$, the $r-2$ right-hand
  terms of the identity at $(m,B)$ are pairwise distinct positive
  $r$-powerful integers with greatest common divisor $1$, and their sum
  $N=(m^r+B^r)^r$ is $r$-powerful. (b) Distinct pairs $(m,B)$ give distinct
  tuples. (c) There are constants $c_r,C_r>0$ depending only on $r$ such
  that for all large $X$ the number of these tuples with $N\le X$ is at
  least $c_rX^{2/r^2}/\log\log X$ and at most $C_rX^{2/r^2}$.
- **S4 (Lemma 2 and its normalization remark).** For nonzero pairwise
  coprime $a,b,c\in\mathbb C[t]$, not all constant, with $a+b=c$,
  $\max(\deg a,\deg b,\deg c)\le n_0(abc)-1$, where $n_0$ counts distinct
  complex roots. This is the library's recalled Mason–Stothers bound in
  genus zero: the height of a polynomial tuple without common factor is its
  maximal degree, the support is the root set of $abc$ together with
  $\infty$, and $|S|-2=n_0(abc)-1$.
- **S5 (Theorem 3 and sharpness).** $r\ge2$. If $a,b,c\in\mathbb C[t]$ are
  nonzero, pairwise coprime, $r$-powerful as polynomials (every root of
  multiplicity at least $r$; constants included), not all constant, and
  $a+b=c$, then $r=2$ and none of $a,b,c$ is constant. Weighted form: if
  $a,b,c$ are $r_a$-, $r_b$-, $r_c$-powerful with $r_a,r_b,r_c\ge2$ under
  the same other hypotheses, then the sum of $1/r_f$ over the nonconstant
  $f$ exceeds $1$. The theorem is sharp: $(t^2-1)^2+(2t)^2=(t^2+1)^2$.
- **S6 (Corollary 3.1).** $r\ge2$; $a,b\in\mathbb Z[t]$, $c=a+b$, not all
  constant; there is an arithmetic progression such that for every
  sufficiently large integer $t$ in it the values $a(t),b(t),c(t)$ are
  positive $r$-powerful integers, and $\gcd(a(t),b(t))=1$ for infinitely
  many such $t$. Then $r=2$ and $a,b,c$ are all nonconstant. Hence for
  $r\ge3$ no one-parameter polynomial family of coprime $r$-powerful
  solutions of $a+b=c$ exists, and for $r=2$ none with a constant term. The
  proof consumes the author-recorded polynomial-factor proposition of the
  Problem 940 folder, with its proof adapted to inputs restricted to a
  progression.
- **S7 (coverage paragraph).** Corollary 3.1 covers a fixed polynomial
  identity evaluated on integer parameters; in the two-parameter device it
  applies along every line $B$ fixed and along every polynomially
  parametrized curve on which its hypotheses hold; it does not cover an
  identity whose terms share a nonconstant factor $D$ and whose members are
  taken only at the integer points where $D=\pm1$.
- **S8 (Proposition 4).** For $\omega$ a primitive cube root of unity and
  $Q=aU^2+bUV+cV^2\in\mathbb C[U,V]$ with $ac=-2b^2$,
  $\sum_{k=0}^{2}Q(\omega^kU,\omega^{-k}V)^5=(3bUV)^5$.
- **S9 (Corollary 4.1).** With $(a,b,c)=(1,1,-2)$: the three forms
  $Q_k=\omega^{2k}U^2+UV-2\omega^kV^2$ factor as
  $\omega^{2k}(U-\omega^kV)(U+2\omega^kV)$ and satisfy
  $Q_0^5+Q_1^5+Q_2^5=(3UV)^5$ in $\mathbb Q(\omega)[U,V]$; no proper subsum
  of the four-term relation vanishes; the four forms have no common factor;
  the Fermat quintic surface $x^5+y^5+z^5=w^5$ contains the conic
  parametrized by $(Q_0:Q_1:Q_2:3UV)$, defined over $\mathbb Q(\omega)$; no
  element of $\mathrm{PGL}_2(\mathbb C)$ acting on $(U,V)$ together with
  scalars on the four forms makes all four real; consequently the identity
  has no four-term version (in that sense) in $\mathbb Q[U,V]$, and Lemma 1
  does not apply to it over $\mathbb Z$.
- **S10 (provenance sentence).** The identity was found by a numerical
  search at $r=5$ and then recognized and proved; the literature on conics
  on the Fermat quintic was not searched. This describes process and
  asserts no mathematics.

## Checklist

- **Quantifiers and scope.** Pass. Every statement carries its own
  quantifiers: Lemma 1 is universal over the admissible $(B,m)$; Corollary
  1.1 says "for all large $X$" with constants depending only on $r$;
  Theorem 3 needs "not all constant"; Corollary 3.1 needs "some
  progression" and "infinitely many"; the non-reality claim of Corollary
  4.1 quantifies over $\mathrm{PGL}_2(\mathbb C)$ and scalars, and finding
  F3 asks that its consequence sentence say so. No "almost all" is upgraded
  to "all".
- **Circularity.** Pass. Lemma 2 is proved from first principles; Theorem 3
  uses only Lemma 2; Corollary 3.1 uses Theorem 3 and the imported
  proposition, whose proof (read) uses neither. Corollary 1.1 uses Lemma 1
  and the reconstruction page. Nothing consumes its own conclusion.
- **Model and convention changes.** Pass. Integer $r$-powerfulness
  (positive, every prime to exponent at least $r$, $1$ included) and
  polynomial $r$-powerfulness (root multiplicities, constants included) are
  both defined in Conventions and used consistently; joint coprimality
  (Lemma 1, Corollary 1.1) and pairwise coprimality (Lemma 2, Theorem 3,
  Corollary 3.1) are kept apart, and coincide for two summands; the
  substitution $X=U^r$, $Y=V^r$ is declared. The normalization from
  $S$-unit heights to degrees in S4 was re-derived (Premises).
- **Finite and statistical overreach.** Pass. The only finite computation
  mentioned, the numerical search behind Proposition 4, is labeled
  exploratory and supports no statement; the identity is proved
  symbolically. Corollary 1.1's count is analytic.
- **Uniformity.** Pass. Corollary 1.1 states that its constants depend only
  on $r$; the coprime-count error term $2^{\omega(B)}$ is bounded uniformly
  for $B\le M$ by $M^{o(1)}$; the "sufficiently large" thresholds in
  Corollary 3.1 are per polynomial and never asserted uniform.
- **Extremal conclusions.** Pass. Theorem 3's sharpness sentence was checked
  in its own units: the inequality $k/r>1$ with $k\le3$ admits exactly
  $(k,r)=(3,2)$, and the Pythagorean identity attains it. Corollary 1.1
  claims no sharpness of the exponent $2/r^2$.
- **Consequences and composition.** Pass with findings F2 and F3.
  Corollary 3.1 inherits the author-recorded standing of the Problem 940
  proposition and discloses it in place. The heading of Theorem 3 (F2)
  omits the qualifier $r\ge3$ that its statement carries; the
  "consequently" sentence of Corollary 4.1 (F3) leaves "version" undefined.
- **Computation.** Pass. The reviewer recomputed, in exact arithmetic over
  $\mathbb Q(\omega)$ with own code that expands the fifth powers directly
  (a different route from the page's multinomial-coefficient argument): the
  three coefficients $[U^8V^2]$, $[U^5V^5]$, $[U^2V^8]$ of $Q^5$ for three
  unrelated triples; Proposition 4 for eight rational triples with
  $ac=-2b^2$; the factorization of $Q_k$; $Q_0+Q_1+Q_2=3UV$; the linear
  independence of $Q_0,Q_1,Q_2$ (determinant $6+12\omega$); the
  non-vanishing of all fourteen proper subsums; and the two involution
  cases. Lemma 1 and Corollary 1.1(a) were checked exactly for
  $r=6,7,8,9$ on sixteen pairs $(m,B)$ each, with
  $B\in\{B_0,2B_0,3B_0,7B_0\}$ and composite $m$ included. All agree with
  the section.
- **Reproduction.** Not applicable. The section retains no evidence program
  and makes no rerun claim; the search scripts it mentions are filed under
  a lead outside this review.
- **Source and verdict fidelity.** Pass with finding F4. The recalled
  Mason–Stothers and Brownawell–Masser bounds were read on the held PDF
  (printed p. 438) and match the library page and the section's use; the
  reconstruction page's identity, data and distinctness argument are cited
  exactly; the Problem 940 proposition is quoted with its hypotheses and
  standing. Every statement is called author-recorded, and no tier is
  assigned. The preamble sentence discussed in F4 lies outside the section
  and is ambiguous about which input Lemma 2 reproves.

## Weakest steps

**W1: joint coprimality in Lemma 1.** Let $p$ divide $A_i(m,B)$ for every
$i\le n-1$. Since $n\ge3$, both $A_1(m,B)$ and $A_2(m,B)$ are among these.
From $A_2(m,B)=c_2m^aB^b$, $p$ divides $c_2$, $m$ or $B$; a prime of $c_2$
divides $B$ by the choice of $B$; so $p\mid mB$, and as $\gcd(m,B)=1$
exactly one of $p\mid m$, $p\mid B$ holds. From $A_1(m,B)=K(m,B)^r$,
$p\mid K(m,B)$. Write $K=\sum k_{ij}U^iV^j$. If $p\mid m$, every term with
$i\ge1$ vanishes modulo $p$, so $K(m,B)\equiv K(0,B)=\pm B^{d'}\pmod p$, a
unit modulo $p$ since $p\nmid B$; if $p\mid B$, likewise
$K(m,B)\equiv K(m,0)=\pm m^d\pmod p$, a unit since $p\nmid m$. Both
contradict $p\mid K(m,B)$. The step needs $c_2$ to be the full integer
coefficient of the monomial (Finding F1): the argument is exactly what F1's
witness breaks when a prime of that coefficient is hidden in an $H_{2j}$
and left out of $B$.

**W2: the lower bound in Corollary 1.1.** Put $M=\lfloor X^{1/r^2}/2\rfloor$
and count pairs $(B,m)$ with $B$ a multiple of $B_0$, $B\le M/2$,
$M/2<m\le M$, $\gcd(m,B)=1$. Then $m>B$, and $m^r+B^r\le M^r+(M/2)^r<2M^r$,
so $N<2^rM^{r^2}\le2^{r-r^2}X\le X$. By Möbius inversion the number of $m$
in $(M/2,M]$ coprime to $B$ is
$\sum_{d\mid B}\mu(d)(\lfloor M/d\rfloor-\lfloor M/(2d)\rfloor)$, which
differs from $(M/2)\phi(B)/B$ by at most the number of squarefree divisors,
$2^{\omega(B)}$. For $B\ge3$, $\phi(B)/B\gg1/\log\log B\ge1/\log\log M$,
while $2^{\omega(B)}\le C_\varepsilon B^\varepsilon$ for every
$\varepsilon>0$ and $B^\varepsilon\le M^\varepsilon$, so each admissible $B$
contributes
$\gg M/\log\log M$ values of $m$ once $M$ is large, uniformly in $B$. There
are $\asymp M/B_0$ admissible $B$, giving
$\gg M^2/\log\log M\asymp X^{2/r^2}/\log\log X$ pairs, and distinct pairs
give distinct tuples because $N$ and the first term recover $m^r+B^r$ and
$m^r-B^r$, hence $m$ and $B$. The reviewer also checked the coprime-count
estimate numerically for $B\in\{30,60,90,210,420,2310,30030\}$ and
$M\in\{10^3,10^4,10^5\}$: the error never exceeded $2^{\omega(B)}/6$. The
upper bound is immediate: $N\le X$ forces $m,B\le X^{1/r^2}$.

**W3: Corollary 3.1's adaptation of the imported proof to a progression.**
The imported proof factors $f=c\prod_jg_j^{m_j}$ over $\mathbb Z$ with
distinct primitive irreducible $g_j$, fixes $j$, and picks a prime $p$ that
divides some value of $g_j$ and avoids the finite set of primes dividing
$c$, the leading coefficients, the discriminants and the pairwise
resultants of the $g_i$; a root $n_0$ of $g_j$ modulo $p$ is then simple
and is not a root of any other $g_i$, and among the $p$ lifts of $n_0$
modulo $p^2$ exactly one is a root of $g_j$ modulo $p^2$, so on a different
lift's class modulo $p^2$ one has $v_p(g_j(n))=1$ and $v_p(g_i(n))=0$ for
$i\ne j$, hence $v_p(f(n))=m_j$. When inputs are confined to a progression
$t\equiv t_0\pmod M$, add $p\nmid M$ to the finite avoidance set;
$\gcd(p^2,M)=1$ lets the Chinese remainder theorem combine the class modulo
$p^2$ with the progression into a class modulo $p^2M$, all of whose members
$n$ satisfy $n\equiv n_0\pmod p$ and avoid the root lift modulo $p^2$, so
$v_p(f(n))=m_j$ still, and the class contains arbitrarily large $n$ at
which $f(n)$ is a positive $r$-powerful integer by hypothesis; thus
$m_j\ge r$. Positivity on the whole line is never used, only positivity at
the chosen inputs. The rest of Corollary 3.1 (separability of irreducible
factors over $\mathbb Q$, Gauss's lemma for the common factor, then
Theorem 3) was re-derived without difficulty.

## Strongest attack

- **S1.** The reviewer tried to break joint coprimality by hiding a prime
  of the monomial's coefficient inside an $H_{2j}$ so that $B$ need not
  carry it: with $r=2$ and $(V^2-U^2)^2+(2UV)^2=(U^2+V^2)^2$, presenting
  $A_2=1\cdot(2UV)^2$ satisfies (i) with $c_2=1$ and (ii) vacuously, and
  $B=1$, $m=3$ gives the values $64,36,100$ with $\gcd(64,36)=4$. The
  attack fails against the statement as written because (iv) reuses the
  symbol $c_2$, so a single presentation must have
  $\prod_jH_{2j}^{e_{2j}}=U^aV^b$ and $c_2=4$, after which (ii) forces
  $V^2\mid A_2$ and $B$ must be even; with $B=2$, $m=3$ the values are
  $25,144,169$ with greatest common divisor $1$. The attack survives only
  as the clarification F1. A second attack, $B=1$ with all $|c_i|=1$,
  leaves the argument intact ($p\mid m$ and $K(m,1)\equiv\pm1$). Hiding
  constants in $H_{ij}$ for $i\ne2$ does not hurt powerfulness, since
  $p\nmid c_i$ then puts $p$ in some $H_{ij}(m,B)$ with exponent at least
  $r$.
- **S2.** Checked (i) to (iv) against the reconstruction's display (1):
  $K(U,0)=U^r$ and $K(0,V)=-V^r$; every coefficient other than $1$ is
  $2\binom rj$ with odd $j\ge1$ or a $v_\ell$, and sits on $V^{rj}$ or
  $V^{3r}$; $P$ is exactly the set of primes of these coefficients, so
  $B_0$ qualifies, and a prime $q>B_0$ is coprime to $B_0$ with
  $q^r>B_0^r$. No gap found.
- **S3.** Attacked distinctness at odd $r$, where the $j=r$ term $2B^{r^2}$
  and $(m^r-B^r)^r$ both have $p$-adic valuation $0$ for $p\mid m$:
  equality would make $2$ a rational $r$-th power. Attacked injectivity
  through the tuple order: the first term is $(m^r-B^r)^r$ by the
  identity's order, and sets instead of tuples change the count by at most
  $(r-2)!$, absorbed in the constants. Attacked the count's uniformity in
  $B$ (W2). Nothing broke.
- **S4.** Attacked the case $W=0$ and the case of a constant summand: if
  $a/b$ is constant then coprimality makes $b$ a unit, so all three are
  constant, excluded; if $a$ is constant then $W=ab'$ still has degree
  $\deg a+\deg b-1$. The third expression $-W=bc'-b'c$, not displayed,
  gives the bound for $\deg a$ (note F5). The normalization remark was
  checked against the library interface: "$f_2/f_1$, $f_3/f_1$ not both
  constant" is equivalent to "not all constant" under pairwise coprimality,
  and $S$ must contain $\infty$ as the pole of the nonconstant members.
- **S5.** Attacked the weighted form at the boundary
  $(r_a,r_b,r_c)=(2,3,6)$, where the sum equals $1$: the proof gives
  $D\le D-1$, so no coprime polynomial solution of $x^2+y^3=z^6$ exists,
  consistent with the statement's strict inequality. Attacked $k=2$ with a
  constant term: the identity forces $k\ge2$ and $k/r>1$ forces $r<k$. No
  gap.
- **S6.** Attacked with a progression whose modulus shares primes with the
  bad set, with positivity holding only on the progression, and with a
  constant summand: the adapted proof (W3) avoids finitely many primes, uses
  positivity only at the chosen inputs, and constants are $r$-powerful
  polynomials by convention, so Theorem 3 applies and excludes them. The
  Gauss-lemma step needs only that a primitive nonconstant $D_0$ has
  $|D_0(t)|\ge2$ for large $t$. No gap.
- **S7.** Attacked the claim that the device runs "along the lines $B$
  fixed": Corollary 3.1 wants one progression, while Lemma 1 ranges over
  all $m$ coprime to $B$; one residue class modulo $B$ coprime to $B$ is a
  progression on which the hypotheses hold, so the reduction stands.
- **S8.** Exact recomputation for eight rational triples with $ac=-2b^2$,
  including non-integral ones, and the degenerate $b=0$ case (both sides
  vanish). No gap.
- **S9.** The reviewer re-derived the classification of anti-holomorphic
  involutions preserving $\{0,\infty\}$: $\tau(z)=\lambda\bar z$ needs
  $|\lambda|=1$ and $\tau(z)=\lambda/\bar z$ needs $\lambda$ real for
  $\tau^2=\mathrm{id}$; the first fixes $\{1,-2\}$ only with $\lambda=1$
  and then sends $\omega$ to $\omega^2\notin\{\omega,-2\omega\}$; the
  second needs $\lambda=-2$ and is then fixed-point free, while
  $g\circ\overline{\phantom{z}}\circ g^{-1}$ fixes the circle
  $g(\mathbb{RP}^1)$. An independent route confirms the conclusion for the
  identity as it stands: the parametrized curve lies in the plane
  $w=x+y+z$ (since $Q_0+Q_1+Q_2=3UV$) on the conic
  $x^2+y^2+z^2+xy+yz+zx=0$, a form that is positive definite over
  $\mathbb R$, so the conic has no real point and admits no real
  parametrization (note F6). The only residue is the wording "version"
  (F3).
- **S10.** Not attacked; not a claim.

## Premises

- **Theorem 1 reconstruction page**
  ([[research/erdos_939/theorem_1_reconstruction|the reconstruction page]]),
  read whole. Interface used: for $r\ge6$, the identity
  $(X+Y)^r=(X-Y)^r+\sum_{j\in J\setminus\{3\}}2\binom rjX^{r-j}Y^j+\sum_{\ell}v_\ell X^{r-3}Y^3$
  with $J$ the odd integers in $[1,r]$, $t=\lfloor r/2\rfloor-2\ge1$,
  $v_1,\dots,v_t$ distinct positive integers summing to $2\binom r3$, $P$
  the primes of the $v_\ell$ and of the $2\binom rj$ ($j\in J\setminus\{3\}$),
  $B=\prod_{p\in P}p\ge2$, and the $q$-adic distinctness argument. Standing
  taken as the assignment states (independently reviewed at an earlier
  commit, corrections applied); the section uses it within these
  hypotheses.
- **Recalled abc and abcd bounds**
  ([[../library/diophantine_problems/corvaja_zannier_2011_abcd_function_fields/recalled_abc_abcd_bounds|library result page]]),
  read whole, with the card's provenance paragraph and the held PDF at
  printed p. 438 by text extraction. Interface: for $S$-units $u,v$ on a
  curve of genus $g$ with support $S$, not both constant, $1+u+v=0$ gives
  $H(1:u:v)\le2g-2+|S|$; for $S$-units with $z=1+u+v$ and no vanishing
  subsum, $H(1:u:v:z)\le3(2g-2+|S|)$. Claims-checked on the page and
  confirmed on the PDF; used by the section only for the normalization
  remark of Lemma 2, which the section proves itself.
- **Polynomial-factor proposition**
  ([[research/erdos_940/finite_core_reduction|the Problem 940 finite-core page]],
  section "Independent polynomial summands still reduce to fixed forms"),
  statement and proof read. Interface: a nonconstant $f\in\mathbb Z[T]$,
  eventually positive and $r$-powerful at every sufficiently large integer
  input, has every nonconstant irreducible factor over $\mathbb Q$ with
  multiplicity at least $r$. Author-recorded on its page, as the section
  states; Corollary 3.1 adapts its proof (W3), so Corollary 3.1 stands at
  author-recorded standing and says so.
- **Problem 939 statement**
  ([[problems/diophantine_problems/E0939/_index|Problem 939]]), Statement
  paragraph only: the $r\ge4$ questions on sums of $r-2$ coprime
  $r$-powerful numbers and the $r=3$ triple question. The section's
  Corollary 1.1 concerns the second question at $r\ge6$.
- **Conventions paragraph** of the connections page (lines 35 to 56):
  definitions of integer and polynomial $r$-powerfulness, joint
  coprimality, $n_0$, and the substitution $X=U^r$, $Y=V^r$.

## Findings

- **F1 (suggested).** Location: Lemma 1, hypothesis (iv), line 82,
  "$A_2=c_2U^aV^b$ is a monomial with $a+b\ge1$". Defect: (i) lets a
  presentation hide integer constants inside the $H_{ij}$, and (iv) does
  not say in words that its $c_2$ is the constant of that presentation; a
  reader who takes (iv) as a shape condition can choose $B$ without the
  primes of the monomial's coefficient, and the joint-coprimality step then
  fails. Witness: $r=2$, $(V^2-U^2)^2+(2UV)^2=(U^2+V^2)^2$,
  $A_2=1\cdot(2UV)^2$, $B=1$, $m=3$: values $64,36,100$ with
  $\gcd(64,36)=4$. Proposed replacement: "(iv) $A_2=c_2U^aV^b$ is a
  monomial with $a+b\ge1$, $c_2$ being the constant of (i), so that every
  prime of the monomial's integer coefficient divides $B$".
- **F2 (suggested).** Location: heading line 186, "Theorem 3: no polynomial
  family with two summands", and the page's `desc` (lines 7 to 8, outside
  the section), "a proved Mason-Stothers obstruction to every polynomial
  family with two summands". Defect: at $r=2$ such families exist, as the
  page itself records at line 202; the statement carries the qualifier and
  the heading and desc do not. Proposed replacement: "Theorem 3: no
  polynomial family with two summands for $r\ge3$", and in the desc "to
  every polynomial family with two summands for r at least 3".
- **F3 (suggested).** Location: Corollary 4.1, lines 279 to 281,
  "Consequently the identity has no version with four terms in
  $\mathbb Q[U,V]$". Defect: "version" is undefined; the proof covers
  images under a projective change of variables over $\mathbb C$ and
  rescaling of the four forms, and a hostile reading takes the sentence as
  the universal statement that the page's $r=5$ section leaves open.
  Proposed replacement: "Consequently no projective change of variables
  over $\mathbb C$ and rescaling of the four forms turns the identity into
  one with four terms in $\mathbb Q[U,V]$".
- **F4 (suggested; outside the section's lines).** Location: preamble,
  lines 28 to 33, "the former is reproved below as Lemma 2, and the latter
  is used only to say what it does not exclude". Defect: read with "the
  former" as the polynomial-factor proposition and "the latter" as the two
  bounds, the sentence says the Problem 940 proposition is reproved as
  Lemma 2, which is false: Lemma 2 reproves the Mason–Stothers bound, the
  Brownawell–Masser bound is used only negatively, and the proposition is
  consumed author-recorded in Corollary 3.1 with its proof adapted.
  Proposed replacement: "the Mason–Stothers bound is reproved below as
  Lemma 2, the Brownawell–Masser bound is used only to say what it does not
  exclude, and the proposition is used in Corollary 3.1 with its proof
  adapted to a progression".
- **F5 (note).** Location: Lemma 2, proof, line 183, "the other two
  expressions of $W$". Only two expressions are displayed; the third is
  $bc'-b'c=-W$, which gives the bound for $\deg a$. Proposed replacement:
  add "and $-W=bc'-b'c$" after the second expression.
- **F6 (note).** Location: Corollary 4.1, lines 276 to 277, "the conic
  $(Q_0:Q_1:Q_2:3UV)$ defined over $\mathbb Q(\omega)$". The conic is
  defined over $\mathbb Q$: $Q_0+Q_1+Q_2=3UV$ places it in the plane
  $w=x+y+z$, and $Q_0^2+Q_1^2+Q_2^2+Q_0Q_1+Q_1Q_2+Q_2Q_0=0$ identically
  (checked in exact arithmetic), matching the factorization
  $(x+y+z)^5-x^5-y^5-z^5=5(x+y)(y+z)(z+x)(x^2+y^2+z^2+xy+yz+zx)$. The
  quadratic form is positive definite, so the conic has no real point,
  which explains and independently confirms the non-reality of every
  reparametrization. The page's wording is correct but weaker than what
  holds; recording the $\mathbb Q$-model would strengthen the page.
- **F7 (note).** Location: lines 162 to 163, "The same statement is used on
  the cubic-curves page of the Problem 699 folder". This cross-reference
  lies outside the commissioned read set and was not verified.

## Verdict

- **S1 (Lemma 1): refutation-failed.** The proof is complete under the
  statement's shared symbol $c_2$; F1 asks that the sharing be said in
  words.
- **S2 (application to the Theorem 1 identity): refutation-failed.**
- **S3 (Corollary 1.1): refutation-failed.** Structure, injectivity and
  both count bounds re-derived; constants depend only on $r$ as stated.
- **S4 (Lemma 2 with its normalization remark): refutation-failed.**
- **S5 (Theorem 3, weighted form and sharpness): refutation-failed.**
- **S6 (Corollary 3.1): refutation-failed.** It stands at the
  author-recorded standing of the Problem 940 proposition it adapts, which
  the section discloses.
- **S7 (coverage paragraph): refutation-failed.**
- **S8 (Proposition 4): refutation-failed.**
- **S9 (Corollary 4.1): refutation-failed.** The consequence sentence needs
  the definition of "version" in F3; with it, every clause is proved.
- **S10 (provenance sentence): not a claim.**

Required corrections: none. Suggested: F1, F2, F3, F4. Notes: F5, F6, F7.

Limitations: the reviewer checked the imported proposition's proof only as
far as needed to validate the progression bridge (W3) and did not review
that proposition itself; the standing of Corollary 3.1 is therefore bounded
by that page's author-recorded standing. The library bounds were confirmed
at claims level on the held PDF and not proved. The computational checks
are the reviewer's scratch arithmetic, retained here only as described, not
as evidence. The other sections of the connections page, the lead folder
and every review or grade in the folder were outside this review.

This focused review assigns no tier and changes no status.
