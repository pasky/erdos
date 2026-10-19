---
name: research/erdos_1221/connections
title: "Connections of the Problem 1221 reconstructions: Problems 255 and 480, the erdosproblems.com family, and the span-to-count mechanism"
desc: |
  Assesses the connections from the reconstructed consecutive-gap proofs to the
  rest of the corpus: the 1949 implication toward the proved Problem 255 (proved
  here; nothing new for that problem), the background transfer of the 1/log 4
  bound behind the proved Problem 480 (proved here; no bearing on that
  question), the 2026 arguments without the distinctness hypothesis (a route on
  Problem 1221 itself, with its lead), and the absence of a second consumer for
  the span-to-count transfer.
created: 2026-09-28T05:40:00Z
updated: 2026-10-19T04:19:07Z
---

[[research/erdos_1221/_index|..]]

***

**Purpose and standing.** This page draws the connections from the
author-recorded reconstructions in
[[research/erdos_1221/_index|the Problem 1221 folder]] to the rest of the
corpus. Each section names its exact target with the target's current
assessment, states what the reconstructed mechanism gives when transported,
with a proof where one is given here, states what it does not give and why,
and names the next investigation with what each outcome would establish.
Every new statement below is author-recorded, and no status or tier changes.
The statements were independently reviewed as they stood on
2026-09-28T13:50:48Z by four focused reviews, one per section, graded in
[[research/erdos_1221/evidence/verify/connections_grade|the connections grade]],
which passes all four and accepts eight corrections, since applied; it assigns
no tier. The Target sentences on the standings of Problems 255 and 1221
differ from that reviewed subject. In the Problem 1221 section, the current
explanation specifies lifted span arcs, including full turns, the empty-list
convention in Proposition 1221.1, and the vacuous separation restriction when a
list has only one distinct value. Its standing and outcome distinguish the
reviewed conditional extension from the separate whole composition, which has no
independent review. The statements of Propositions 1221.1--1221.2 and the
conditional deduction 1221.3 retain their mathematical conclusions. The
notation is the folder's: a sequence $a=(a_1,a_2,\ldots)$ on the circle
$\mathbb T$ of circumference $1$, the $n$ gaps cut by its first $n$ terms (of
length $0$ between coincident terms), the $r$-spans, that is, the sums of $r$
cyclically consecutive gaps, with largest and smallest values $M_n^r(a)$ and
$m_n^r(a)$, and the 1949 constants

$$
\Lambda_r=\inf_a\limsup_{n\to\infty}nM_n^r(a),\qquad
\lambda_r=\sup_a\liminf_{n\to\infty}nm_n^r(a),\qquad
\mu_r=\inf_a\limsup_{n\to\infty}\frac{M_n^r(a)}{m_n^r(a)} .
$$

For an arc $I$ and a stage $n$ the counting error is
$D_n(I)=\#\{i\le n:\ a_i\in I\}-n|I|$, and $N_n(I)=\#\{i\le n:\ a_i\in I\}$
counts indices, so coincident terms count with multiplicity.

## Problem 255: the 1949 implication toward the discrepancy theorem

**Target.** [[problems/discrepancy/E0255/_index|Problem 255]] asks whether every
sequence $z_1,z_2,\ldots\in[0,1]$ has an interval $I$ with
$\limsup_N|D_N(I)|=\infty$. Its page records the problem as solved, with
the question proved, on three accepted claim pages for Schmidt's papers of
1968 and 1972 and Tijdeman--Wagner 1980, and its Progress section records
the implication proved below; the held source
[[../library/discrepancy/schmidt_1972_irregularities_distribution/_index|Schmidt 1972, part VI]]
shows that the anchors $\alpha$ for which $D_n([0,\alpha))$ stays bounded
form a countable set, so all but countably many anchored intervals answer
the question. The connection named in the folder index is the remark on
p. 14 of the 1949 note, recorded on the
[[../library/analysis/debruijn_erdos_1949_sequences_points_circle/conjecture_p17|conjecture page]]:
the third part of the conjecture would imply van Aardenne-Ehrenfest's
"just distributions" theorem of 1945, that no sequence has
$\sup_\alpha|D_n([0,\alpha))|$ bounded in $n$.

**What transports.** The remark is a theorem, each of the three parts of
the mean-normalized reading suffices, and the proof is four lines of the
folder's span bookkeeping.

*Proposition 255.1 (author-recorded).* Let $a$ be a sequence on the circle,
coincident terms allowed, and let $K$ be a number with $|D_n(I)|\le K$ for
every $n\ge1$ and every half-open arc $I$. Then for every $r\ge1$ and every
$n>r$,

$$
nM_n^r(a)\ \le\ r+K-1,\qquad nm_n^r(a)\ \ge\ r-K+1 .
$$

Consequently $\Lambda_r-r\le\Lambda_r(a)-r\le K-1$ and
$r-\lambda_r\le r-\lambda_r(a)\le K-1$ for every $r$, and for $r\ge K$

$$
r(\mu_r-1)\ \le\ r\bigl(\mu_r(a)-1\bigr)\ \le\ \frac{2(K-1)\,r}{r-K+1}
\ \xrightarrow[r\to\infty]{}\ 2(K-1),
$$

so all three expressions of the mean-normalized conjecture stay bounded.
Hence each part of the conjecture implies that no sequence has uniformly
bounded counting error on arcs; a bound $K$ on the anchored intervals
$[0,\alpha)$ gives the bound $2K$ on every arc and conversely, so this is
the 1945 theorem in its original form.

*Proof.* The hypothesis passes from half-open arcs to open and closed
arcs: for an open arc $(p,q)$ of positive length the half-open arcs
$(p,q-\varepsilon]$ contain the same terms of stage $n$ once $\varepsilon$
is small, and their lengths tend to $|(p,q)|$; for a closed arc $[p,q]$
the arcs $(p-\varepsilon,q]$ contain the same terms once $\varepsilon$ is
small. So $|D_n(I)|\le K$ for arcs of every endpoint type, and the
complement of an arc, which has counting error $-D_n(I)$, covers the
wrapping arcs. (At $n=1$ a short arc containing $a_1$ shows $K\ge1$.)

Fix $r\ge1$ and $n>r$, list the first $n$ terms in cyclic order, coincident
terms in order of index, and let $J$ be an $r$-span: the clockwise distance
$|J|$ from a term $p$ to the term $q$ that is $r$ places after $p$. The
open arc $(p,q)$ contains only terms strictly between $p$ and $q$ in the
cyclic order, since a term at the position of $p$ or of $q$ is excluded, so
$N_n((p,q))\le r-1$; from $D_n((p,q))\ge-K$,

$$
n|J|\ \le\ N_n((p,q))+K\ \le\ r-1+K ,
$$

trivially so when $|J|=0$. The closed arc $[p,q]$ contains the $r+1$ terms
$p,\ldots,q$, which are distinct terms because $n>r$; from
$D_n([p,q])\le K$, $r+1-n|J|\le K$, that is, $n|J|\ge r+1-K$. The largest
and the smallest span give the two displayed bounds. Letting $n\to\infty$
gives $\Lambda_r(a)\le r+K-1$ and $\lambda_r(a)\ge r-K+1$. For $r\ge K$ the
lower bound makes every late span positive and

$$
\frac{M_n^r(a)}{m_n^r(a)}\ \le\ \frac{r+K-1}{r-K+1}=1+\frac{2(K-1)}{r-K+1},
$$

which gives the bound on $r(\mu_r(a)-1)$; the universal constants obey
$\Lambda_r\le\Lambda_r(a)$, $\lambda_r\ge\lambda_r(a)$, $\mu_r\le\mu_r(a)$.
The last display tends to $2(K-1)$, so each expression is bounded in $r$.
Finally $D_n((\alpha,\beta])=D_n([0,\beta])-D_n([0,\alpha])$ up to the
endpoint adjustments above, so anchored bounds give arc bounds with the
factor $2$, and anchored intervals are arcs. $\square$

**What it does not give.**

- Not the fixed interval of Problem 255. The arcs whose counting error the
  proof exploits are the spans of stage $n$ and move with $n$; the
  conclusion is $\limsup_n\sup_I|D_n(I)|=\infty$, the 1945 form. Problem
  255 asks for one interval $I$ with $\limsup_n|D_n(I)|=\infty$, which is
  the content of Schmidt's 1968 paper (the bounded anchors form a null set)
  and of part VI (they are countable); no page of the folder bears on the
  passage from a moving arc to a fixed one.
- No rate, in either direction. With a nondecreasing $K(n)\to\infty$ in
  place of $K$ the proof gives $nM_n^r(a)\le r+K(n)-1$ and
  $nm_n^r(a)\ge r-K(n)+1$, which bound nothing in the limit because
  $K(n)\to\infty$: the constants $\Lambda_r,\lambda_r,\mu_r$ are limits in
  $n$ at fixed $r$, so through Proposition 255.1 a growth rate of the
  discrepancy in $n$ neither follows from the conjecture nor feeds it.
  Coupling $r$ to a point count is exactly what
  [[research/erdos_1221/ko26b_lemma_4_2_reconstruction|Lemma 4.2 of the 2026 preprint]]
  adds; see the reverse edge.
- Circular through the only claimed proof of the premise. The fixed-$r$
  bounds, (5.7) of 1949 and
  [[research/erdos_1221/ko26a_theorem_1_1_reconstruction|Theorem 1.1 of the 2026 note]],
  are bounded in $r$ and do not reach the premise; the growth is claimed
  only by
  [[research/erdos_1221/ko26b_theorem_1_1_reconstruction|Theorem 1.1 of the 2026 preprint]],
  whose ratio part consumes a finite-list form of Schmidt's theorem, itself
  a quantitative strengthening of the 1945 theorem, and whose one-sided
  parts consume Halász's planar theorem. Deriving the 1945 theorem from
  that claim through Proposition 255.1 proves nothing new. A proof of any
  one part that avoids discrepancy lower bounds would give a new proof of
  the 1945 theorem; none is in the sources read.
- Scope. The 2026 claim is stated over sequences of distinct points, so
  through Proposition 255.1 it would exclude only just-distributed
  sequences of distinct points; the extension to all sequences is the
  subject of the section on Problem 1221's own family below.

**The reverse edge.** A quantitative form of the 1945 theorem, the uniform
statement that the conclusion of Problem 255 strengthens, is an input of
the claimed resolution, not a consequence of it.
[[research/erdos_1221/ko26b_lemma_4_2_reconstruction|Lemma 4.2]] turns the
short-interval counting bound of
[[research/erdos_1221/ko26b_proposition_3_1_reconstruction|Proposition 3.1]]
into a list of $\lfloor S\rfloor$ points all of whose prefixes have
counting error at most $B$, and the imported Theorem 4.1, the finite-prefix
form $H_L\ge\frac1{16}\log L$ that the source derives from Larcher's 2015
proof, supplies the contradiction;
[[research/erdos_1221/ko26b_lemma_7_2_reconstruction|Lemma 7.2]] does the
same with Halász's planar $L^1$ theorem. The Problem 255 source held here,
part VI of Schmidt's series, is a different theorem (countability of the
bounded anchors) from the planar theorem of part VII (Acta Arith. 21
(1972), 45--50) that the Lemma 4.2 page names as the source of the
qualitative finite-list bound. Neither part VII, nor Larcher 2015, nor
Halász 1981 is held, so the corpus holds neither of the two inputs the
reconstruction imports.

**Next investigation.** Acquire and file Larcher 2015 (J. Complexity 31,
474--485; arXiv:1407.2094) and Halász 1981, and check the two imported
statements as used: the finite-list bound with the constant $1/16$ for
every list of length $\lfloor a^h\rfloor$, and the unnormalized planar
$L^1$ bound $c_H\sqrt{\log M}$. A positive outcome closes the two import
gaps of the reconstruction of the 2026 preprint and gives the Problem 255
library a hook to the theorem actually consumed; a negative one (for
instance, Larcher's Section 3 bounding only infinitely many prefixes of an
infinite sequence) leaves the growth statement of the ratio part standing
through part VII with an unspecified constant and removes the warrant for
the coefficient $1/100$. Neither outcome changes Problem 255.

**Outcome.** Transfers as an implication (Proposition 255.1); it yields
nothing new for Problem 255, which is proved and stronger, and the
mathematical dependency runs the other way.

## Problem 480: the clustering constant and the Section 4 count

**Target.** [[problems/number_theory/E0480/_index|Problem 480]] asks whether every
sequence $x_1,x_2,\ldots\in[0,1]$ satisfies

$$
C(\bar x)=\inf_n\liminf_{m\to\infty}n\,|x_{m+n}-x_m|\ \le\ 5^{-1/2} .
$$

Its Current assessment records the status proved: Theorem 1 of Chung and
Graham (1984) gives $C(\bar x)\le\alpha=0.39441967\ldots$ for every
sequence, their Theorem 2 shows that $\alpha$ is best possible, and
erdosproblems.com showed PROVED (LEAN). The folder index names two links. First,
the chapter's introduction attributes to the 1949 note the bound $1/\log4$ for
its measure

$$
\omega(\bar x)=\liminf_{n\to\infty}\ n\min_{1\le i<j\le n}|x_i-x_j| ,
$$

which is the interval analog of $\lambda_1(a)=\liminf_nnm_n^1(a)$ on the
circle; the
[[../library/analysis/debruijn_erdos_1949_sequences_points_circle/_index|card of the note]]
points at Proposition 480.1 below for the passage from the circle to the
interval. Second, the index says the
Chung--Graham proof descends from the Section 4 count.

**What transports.** The Section 4 count, rerun on the interval, gives the
chapter's display (1).

*Proposition 480.1 (author-recorded).* For every sequence
$x_1,x_2,\ldots\in[0,1]$ and every $n\ge1$ there is an integer $k$ with
$n<k\le2n$ such that

$$
k\,g_k\ \le\ \tau'_n:=\Bigl(2\sum_{k=n+1}^{2n}\frac1k-\frac1{n+1}\Bigr)^{-1},
\qquad g_k=\min_{1\le i<j\le k}|x_i-x_j| .
$$

Since $\tau'_n\to1/\log4$, every sequence in $[0,1]$ has
$\omega(\bar x)\le1/\log4$, and the sequence $x_k=\{\log_2(2k-1)\}$ attains
the bound.

*Proof.* Fix $n$, put $N=2n$, and list $x_1,\ldots,x_N$ in increasing
order as $y_1\le y_2\le\cdots\le y_N$ with $y_i=x_{k_i}$, $(k_1,\ldots,k_N)$
a permutation of $(1,\ldots,N)$ (equal values in either order). For
$1\le i\le N-1$ put $k_i^*=\max(k_i,k_{i+1},n+1)$, so $n<k_i^*\le2n$. The
terms $x_{k_i}$ and $x_{k_{i+1}}$ are two of the first $k_i^*$ terms, so
$y_{i+1}-y_i\ge g_{k_i^*}$. Suppose that $\varrho>0$ satisfies $kg_k>\varrho$
for every $k$ with $n<k\le2n$. Then $y_{i+1}-y_i>\varrho/k_i^*$ for every
$i$, and summing the $N-1$ consecutive differences,

$$
1\ \ge\ y_N-y_1\ >\ \varrho\sum_{i=1}^{N-1}\frac1{k_i^*} .
$$

For $n+1<k\le N$ the equality $k_i^*=k$ forces $k\in\{k_i,k_{i+1}\}$, and
$k=k_j$ for exactly one $j$, which occurs in the windows $i=j-1$ and
$i=j$ only; so $k$ occurs $\varepsilon_k\le2$ times among the $k_i^*$, and
$\varepsilon_{n+1}=(N-1)-\sum_{k\ge n+2}\varepsilon_k$. Expanding the
coefficients as on the
[[research/erdos_1221/dber49_inequality_4_3_reconstruction|(4.3) page]],

$$
\sum_{i=1}^{N-1}\frac1{k_i^*}=\sum_{k=n+1}^{2n}\frac{\varepsilon_k}k
=2\sum_{k=n+1}^{2n}\frac1k-\frac1{n+1}+\sum_{k=n+2}^{2n}(2-\varepsilon_k)
\Bigl(\frac1{n+1}-\frac1k\Bigr)\ \ge\ \frac1{\tau'_n},
$$

the coefficient of $1/(n+1)$ on the right being
$1+\sum_{k\ge n+2}(2-\varepsilon_k)=2n-1-\sum_{k\ge n+2}\varepsilon_k=\varepsilon_{n+1}$.
Hence $\varrho<\tau'_n$, and with $\varrho=\tau'_n$ the hypothesis fails: some
$k\in(n,2n]$ has $kg_k\le\tau'_n$. Since $2\sum_{k=n+1}^{2n}1/k\to2\log2=\log4$,
$\tau'_n\to1/\log4$, and choosing such a $k_n$ for each $n$ gives
$\omega(\bar x)\le\lim\tau'_n=1/\log4$.

For the sharpness, the first $n$ terms of $x_k=\{\log_2(2k-1)\}$ are,
modulo $1$, the numbers $\log_2k$ for $n\le k\le2n-1$ (the
[[../library/analysis/debruijn_erdos_1949_sequences_points_circle/section_2_r_equals_1|Section 2 page]]),
so on the circle their $n$ gaps are $\log_2\frac{k+1}k$ for
$n\le k\le2n-1$, and the $n-1$ interior gaps of the interval are these $n$
circle gaps with the wrap gap, from the largest term back to $x_1=0$,
removed. The smallest interior gap is therefore at least the smallest
circle gap and at most the second smallest:
$\log_2\frac{2n}{2n-1}\le g_n\le\log_2\frac{2n-1}{2n-2}$ for $n\ge2$, and
both bounds times $n$ tend to $1/(2\log2)=1/\log4$, so
$ng_n\to1/\log4$. $\square$

The circle statement does not transfer by itself: reading $[0,1]$ as the
circle adds the wrap gap $y_1+1-y_N$, which can be the smallest gap, so
$m_n^1(a)\le g_n$ and (4.3) bounds the wrong side. The interval argument
replaces the $N$ cyclic windows by the $N-1$ adjacent pairs and the total
length $1$ by $y_N-y_1\le1$; its finite-$n$ bound $\tau'_n$ is weaker than
the circle's $\tau_n^{(1)}=(2\sum_{k=n+1}^{2n}1/k)^{-1}$ by the term
$1/(n+1)$ and has the same limit.

**What it does not give.**

- Nothing for the question of Problem 480, which is proved with the sharp
  constant $\alpha$ and concerns a measure of a different quantifier
  structure: $C$ reads pairs at a fixed lag $n$ in order of insertion, with
  $m\to\infty$, while $\omega$ and $\lambda_1$ read the closest pair among
  all the first $n$ terms. The two measures are not comparable. A sequence
  whose first two terms coincide has $\omega(\bar x)=0$, while $C$ ignores
  any finite set of indices, so prepending a repeated term to the extremal
  sequence of the chapter's Theorem 2 gives $\omega=0$ and $C=\alpha$; in
  the other direction the chapter's introduction, as the card of the
  chapter records, remarks that $C$ can be small while $\omega$ stays
  large, when the close pairs occur far out (for instance
  $|x_{m+1}-x_m|=m^{-1/2}$ at infinitely many $m$ gives $C=0$ without
  disturbing $\omega$). So neither bound transfers to the other measure.
- The "descent" is a resemblance of shape, not a dependency. Both
  arguments bound a sum of consecutive sorted gaps by $1$ and bound each
  gap below from the hypothesis, but the 1949 count uses all $N$ adjacent
  pairs, the bound $\varrho/k_i^*$ from the largest index in the window,
  and the multiplicity bound $2$, while the proof of Theorem 1 on p. 211 of
  the chapter uses only the pairs of an increasing subsequence of the order
  permutation of $N$ consecutive terms, the bound
  $(1+\epsilon)\alpha/|\pi(i_{k+1})-\pi(i_k)|$ from the lag hypothesis, and
  the exact extremal value $u_m$ of its Theorem 3, proved on pp. 188--210
  and reconstructed nowhere in the corpus. No step of Section 4 enters
  Theorem 3.
- No reverse transfer is available either. Whether a permutation extremal
  problem in the style of Theorem 3 could sharpen (4.3) for $r\ge2$, where
  the 1949 windows read $r+1$ consecutive sorted terms, is addressed by no
  held source; for $r=1$ the bound is sharp, and the growth of
  $r-\lambda_r$ claimed by the 2026 preprint comes from the discrepancy
  route, not from a sharper count.

**Next investigation.** The Problem 480 page lists as an unread lead a
later Chung--Graham paper on a sequence of points on a circle of
circumference $1$. Reading it would settle whether its circle measure is
the 1949 $\lambda_1$, a lag measure on the circle, or something else: a
positive identification with the de Bruijn--Erdős constants or a variant
would add a library hook for Problem 1221 and possibly small-$r$
information; a negative one leaves this connection at the background level
of Proposition 480.1.

**Outcome.** Fails as a route to Problem 480 (proved, sharp constant,
incomparable measure); the background transfer of the $1/\log4$ bound to
the interval, which the card of the note left unreconciled, is proved
above.

## Problem 1221 itself: the site's family against sequences of distinct points

**Target.** [[problems/analysis/E1221/_index|Problem 1221]], status `claimed`,
claim `proved`, under its mean-normalized reading: whether $\Lambda_r-r$,
$r-\lambda_r$ and $r(\mu_r-1)$ tend to infinity. The erdosproblems.com family,
like Section 1 of the 1949 note, admits coincident terms, while the two 2026
sources state their lower bounds over sequences of distinct points; the sources
do not establish equality of the constants over the two families.
This section records what the reconstructed arguments give for the larger
family.

**The two families.** Distinct sequences form a subfamily, so the infima
over all sequences are at most those over distinct sequences and the
supremum is at least:
$\mu_r^{\mathrm{all}}\le\mu_r^{\mathrm{dist}}$,
$\Lambda_r^{\mathrm{all}}\le\Lambda_r^{\mathrm{dist}}$,
$\lambda_r^{\mathrm{all}}\ge\lambda_r^{\mathrm{dist}}$. An upper bound on
$\mu_r$ proved by exhibiting a sequence of distinct points,
[[research/erdos_1221/clst25_theorem_2_reconstruction|Theorem 2 of the balanced-stick preprint]],
passes to the erdosproblems.com family at once; the 1949 bounds are stated over
all sequences; the lower bounds of the 2026 note and preprint do not pass by
inclusion, and they are the subject here. The note's zero-length intervals are
the multiset model used below: the first $n$ terms are listed in cyclic order by
position, coincident terms in order of index; the $n$ gaps, some possibly $0$,
do not depend on the tie-break; an $r$-span is the sum of $r$ consecutive gaps.
With cyclic coordinates lifted by $y_{i+n}=y_i+1$, its length is
$y_{i+r}-y_i$, which can equal $1$ even when its two positions coincide on
the circle. $N_n(I)$ counts indices.

**Where distinctness enters the reconstructed arguments** (author-recorded
reading of the folder's pages).

- Positivity of the spans, used only to make ratios finite. Under the
  contradiction hypotheses, $R_n\le\rho$ for late $n$ in the note and the
  ratio hypothesis of Section 5 in the preprint, every late $r$-span is
  positive by the mean identity $m_n\ge M_n/\rho\ge r/(\rho n)$; where a
  span vanishes, the ratio conclusion holds trivially with $M/0=+\infty$.
  The one-sided hypotheses (6.1) do not need positive spans.
- The least distance $\delta$ between distinct points of $P_{n_0}$ in
  [[research/erdos_1221/ko26b_lemma_4_2_reconstruction|Lemma 4.2]], used
  to keep early terms out of the short interval and to produce an interval
  with exactly $L$ terms. Proposition 1221.1 replaces it.
- Nowhere else. Checked page by page:
  [[research/erdos_1221/ko26b_lemma_2_1_reconstruction|Lemma 2.1]] (the
  moves $F_s$, $B_s$ are bijections of index sets, the displacement bounds
  are positional, and the averaging counts with multiplicity);
  [[research/erdos_1221/ko26b_proposition_3_1_reconstruction|Proposition 3.1]]
  (for the terminal bounds (3.2), among $r+1$ terms in an arc, ordered by
  cyclic rank from the arc's start, the first and the last are $r$ places
  apart and the terms between them lie in the arc);
  [[research/erdos_1221/ko26b_lemma_6_1_reconstruction|Lemma 6.1]] (the
  zero-sum identity);
  [[research/erdos_1221/ko26b_lemma_6_2_reconstruction|Lemma 6.2]];
  [[research/erdos_1221/ko26b_lemma_6_3_reconstruction|Lemma 6.3]] (for $x$
  at no term's position, $y_i$ is among the $r$ terms after $x$ exactly
  when $x$ lies in the lifted arc from $y_{i-r}$ to $y_i$, projected to
  the circle; zero spans give empty arcs and length-one spans give full
  turns, as the
  [[research/erdos_1221/all_sequence_composition|composition page's covering identity]]
  writes out);
  [[research/erdos_1221/ko26b_proposition_6_4_reconstruction|Proposition 6.4]];
  [[research/erdos_1221/ko26b_lemma_7_2_reconstruction|Lemma 7.2]] (the
  planar points carry the distinct second coordinates $i/N$, so the
  imported planar theorem meets a set of distinct points); and in the
  2026 note [[research/erdos_1221/ko26a_lemma_3_1_reconstruction|Lemma 3.1 with Lemma 2.1]],
  [[research/erdos_1221/ko26a_proposition_4_1_reconstruction|Proposition 4.1]]
  and [[research/erdos_1221/ko26a_theorem_1_1_reconstruction|Theorem 1.1]],
  where a term inserted at an occupied position comes last among the terms
  at that position and splits the gap that starts at the previous last term
  into a zero piece and the old gap, so "one insertion splits one gap"
  stays true, and every inequality on those pages uses only gaps $\ge0$.

*Proposition 1221.1 (Lemma 4.2 without distinctness; author-recorded).*
Let $(x_n)$ be any sequence on $\mathbb T$, coincident terms allowed, let
$B\ge1$ and $S\ge2$, and suppose that (4.1) holds for all integers
$n\ge n_0$: $|N_n((x,x+D/n])-D|\le B$ for all $x\in\mathbb T$ and
$0\le D\le S$. Put $L=\lfloor S\rfloor$. Then there are an integer $L'$
with $L-B\le L'\le L+B$ and a list $z_1,\ldots,z_{L'}\in(0,1)$, possibly
with repeated entries, whose maximum prefix counting error satisfies
$H_{L'}(z_1,\ldots,z_{L'})\le B$, with $H_0=0$ for the empty list. If the
imported Theorem 4.1 holds for
lists of distinct entries, it holds for all lists, and then
$B\ge\frac1{16}\log(L-B)$ whenever $L-B\ge L_0$.

*Proof.* Choose an integer $N>n_0$ with $n_0L/N<1$ and put $w=L/N$. The
positions of the first $n_0$ terms form a set $Q$ of at most $n_0$ points,
and the set of $a\in\mathbb T$ for which $(a,a+w]$ meets $Q$ has measure at
most $n_0w<1$; the finitely many $a$ for which $a$ or $a+w$ is the position
of one of the first $N$ terms are excluded too. Fix such an $a$ and put
$J=(a,a+w]$. By (4.1) at time $N$ with $D=L\le S$, the number $L'=N_N(J)$
satisfies $|L'-L|\le B$, and every term in $J$ has index greater than
$n_0$. List the terms in $J$ by index, $m_1<\cdots<m_{L'}\le N$, and put
$z_i=(x_{m_i}-a)/w\in(0,1)$. Fix $j$ and let $n=m_j\ge n_0+1$; the terms of
$P_n$ in $J$ are exactly the first $j$ listed, so
$\#\{i\le j:\ z_i\le u\}=N_n((a,a+uw])$ for $0\le u\le1$. Put
$f(u)=N_n((a,a+uw])-nuw$. The arc $(a,a+uw]$ has length $D/n$ with
$D=nuw\le Nw=L\le S$, so $|f(u)|\le B$ by (4.1); the complementary arc
$(a+uw,a+w]$ has length $D'/n$ with $D'=n(1-u)w\le S$ and count
$j-N_n((a,a+uw])$, so $|f(1)-f(u)|\le B$. Since $f(1)=j-nw$,

$$
\#\{i\le j:\ z_i\le u\}-ju=f(u)-uf(1)=(1-u)f(u)-u\bigl(f(1)-f(u)\bigr),
$$

of absolute value at most $B$; for the convention $z_i<u$ the count is the
left limit, with the same supremum. So $H_{L'}(z_1,\ldots,z_{L'})\le B$.

For the last sentence let $z_1,\ldots,z_M$ be any list with $M\ge1$ and
$\eta>0$, and
let $\delta>0$ be smaller than $\eta/M^2$, than $(1-\max_iz_i)/M$, and
than the least distance between distinct values of the list divided by
$M$; omit the last restriction if the list takes only one value. For each
value $v$ taken by $m\ge2$ entries, move those entries, in list order, to
$v,v+\delta,\ldots,v+(m-1)\delta$; the new list $z'$ has distinct entries
in $[0,1)$. For a prefix $j$ the function $F(u)=\#\{i\le j:\ z_i<u\}-ju$ is
unchanged outside the intervals $(v,v+(m-1)\delta]$, and on such an
interval the new function lies between $F(v)-j(m-1)\delta$ and $F(v+)$,
where $F(v)$ and $F(v+)$ are the values of $F$ just before and just after
its jump at $v$; so the new prefix error is at most
$H_M(z)+M^2\delta<H_M(z)+\eta$, and $H_M(z')\le H_M(z)+\eta$. If Theorem 4.1
holds for distinct lists, $H_M(z)\ge H_M(z')-\eta\ge\frac1{16}\log M-\eta$ for
every $\eta>0$, hence $H_M(z)\ge\frac1{16}\log M$. Applied to the list above
with $M=L'\ge L-B$, this gives $B\ge\frac1{16}\log(L-B)$. $\square$

*Proposition 1221.2 (the fixed-$r$ bound over all sequences;
author-recorded).* For every integer $r\ge2$ and every sequence on
$\mathbb T$, coincident terms allowed, with $M/0=+\infty$,

$$
\limsup_{n\to\infty}\frac{M_n^{(r)}}{m_n^{(r)}}\ \ge\ 1+\frac r{r^2-1}.
$$

*Proof.* Suppose the upper limit is smaller and choose $\rho$, $\eta$,
$N_1$ as on the
[[research/erdos_1221/ko26a_theorem_1_1_reconstruction|Theorem 1.1 page]];
then $R_n\le\rho$ for $n\ge N_1$, so every $r$-block at those times is
positive, while single gaps may vanish. The three pages are now read with
gaps $\ge0$: Lemma 2.1 (a block containing a zero piece is compared with a
block of the previous time as before), Lemma 3.1 (the blocks $W_i$, $U_i$
and the protected block of part 2 need only nonnegative gaps),
Proposition 4.1 (the counting is on gaps as combinatorial objects; an
insertion at an occupied position is a split with a zero piece, and a zero
gap may later be split into two zero pieces, which the descendant
accounting treats like any split), and Theorem 1.1 (the mean identity and
the epoch recursion). The contradiction is reached as on those pages.
$\square$

*Conditional deduction 1221.3 (author-recorded).* Let (P) be the premise
that the chain reconstructed on the preprint's pages proves
[[research/erdos_1221/ko26b_theorem_1_1_reconstruction|Theorem 1.1]] for
sequences of distinct points, with its two imported inputs as stated there
(Theorem 4.1, stated there for every list in $[0,1)$, of which only the
case of distinct entries is needed, and Halász's Theorem 7.1). Then the
same chain, with Proposition 1221.1 in place of Lemma 4.2, proves the
three bounds of Theorem 1.1, with the same $c$ and the same coefficient
$1/100$, and an absolute threshold in place of $r_0$, for every sequence
on $\mathbb T$, coincident terms allowed; in particular, under (P), all
three parts of the mean-normalized conjecture hold for the erdosproblems.com
family. Argument: Sections 2--3 and 6--8 use distinctness nowhere (the checklist
above); Section 5 derives (2.1) from the ratio hypothesis through the mean
identity alone; Proposition 1221.1 gives
$B\ge\frac1{16}\log(\lfloor S\rfloor-B)$, and since $B=\frac3{100}\log r+O(1)$
while $\log\lfloor S\rfloor=\frac12\log r-O(\log\log r)$, subtracting $B$ inside
the logarithm changes it by $o(1)$ and the comparison of Section 5 is unchanged;
Lemma 7.2's planar sets are sets of distinct points, so Theorem 7.1 applies as
before. Premise (P) is an explicit assumption: the source claim is
unrefereed, and the focused review of this deduction did not check its two
imports or independently verify the full chain. The separate composition
below supplies written proofs for a variant with coefficient $1/200$; it
does not establish (P) with the coefficient $1/100$. No status changes.

**What it does not give.** Equality of the constants over the two families
is not proved: under (P) the extended lower bounds and the shared upper
bound give $\mu_r-1$ the same order $\log r/r$ over both families, but
$\mu_r^{\mathrm{all}}<\mu_r^{\mathrm{dist}}$ is not excluded, and nothing
here needs it. The sources state their theorems for distinct points; the
extension is the corpus's reading of the reconstructed arguments, not a
statement of any source. The
[[research/erdos_1221/evidence/verify/connections_grade|connections grade]]
accepts the focused check of the extraction and the conditional extension,
with (P) still an explicit premise. Its review took the reconstruction
pages at their existing standing and did not certify their entire source
chain. The filed reconstruction reviews cover their distinct-point
subjects, relative to the imported inputs; neither review set covers the
complete all-sequence composition.

**Further scrutiny.** The route recorded as the lead
[[research/leads/consecutive_gap_bounds_coincident_points/_index|consecutive_gap_bounds_coincident_points]]
has a focused conditional warrant as described above. The
[[research/erdos_1221/all_sequence_composition|complete composition]]
requires independent whole-conclusion scrutiny of its discrepancy inputs,
the span-to-count chain, the lifted-arc convention and the closing
quantifiers. A positive verdict would support that full argument at the
scope its grade accepts; a defect must identify the affected branch and
its first unsupported estimate.

**Outcome.** Transfers for the fixed-$r$ bound (Proposition 1221.2);
transfers conditionally for the claimed growth bounds (deduction 1221.3,
under the standing of the claim). The
[[research/erdos_1221/all_sequence_composition|composition page]] instead
proves the finite-list and planar estimates it uses and composes the
all-sequence argument without assuming (P), with ratio coefficient $1/200$
in place of $1/100$. That whole argument remains author-recorded.

## The span-to-count transfer has no second consumer

**The mechanism at its actual scope.** The reusable content of the 2026
preprint is the passage from span control to counting control for a
nested family of point sets: the sets $P_t=\{x_1,\ldots,x_{\lfloor t\rfloor}\}$
grow by one term per step, and the hypothesis is an eventual bound on the
$r$-spans at scale $1/t$, two-sided in
[[research/erdos_1221/ko26b_lemma_2_1_reconstruction|Lemma 2.1]]
(every span in $[(r-a_t)/t,(r+b_t)/t]$ with $a_t+b_t\le A$) or one-sided in
[[research/erdos_1221/ko26b_lemma_6_1_reconstruction|Lemma 6.1]]
(only $nM_n^{(r)}-r\le A$, or only $r-nm_n^{(r)}\le A$), with $A\ge1$ and
$r\ge C_0A$ for an absolute $C_0$, that is, a span error small compared
with $r$. The conclusion is a counting error $O(A)$, pointwise
([[research/erdos_1221/ko26b_proposition_3_1_reconstruction|Proposition 3.1]])
or in spatial $L^1$
([[research/erdos_1221/ko26b_proposition_6_4_reconstruction|Proposition 6.4]]),
on arcs holding at most $\sqrt{Ar}/\log^2(r/A)$ terms, with a threshold in
$t$ depending on $r$, $A$ and the sequence. The nesting is essential: the
cyclic walks compare $P_t$ with $P_s\supseteq P_t$ at nearby times, and the
localization of
[[research/erdos_1221/ko26b_lemma_4_2_reconstruction|Lemma 4.2]] and
[[research/erdos_1221/ko26b_lemma_7_2_reconstruction|Lemma 7.2]] reads the
insertion time as a coordinate. The converse passage, from counting
control to span control, is the elementary direction and is what
[[research/erdos_1221/clst25_theorem_2_reconstruction|Theorem 2 of the balanced-stick preprint]]
takes from its Theorem 3.

**The search.** The problems, research and theory trees were searched for
sequences on the circle or in the unit interval, consecutive gaps and
spacings, discrepancy, and the named imported theorems. No open problem
consumes the mechanism:

- [[problems/discrepancy/E0255/_index|Problem 255]] is an input, not a consumer
  (the section above).
- [[problems/discrepancy/E0997/_index|Problem 997]] (well-distribution of
  $\{\alpha p_n\}$; proved) counts terms with indices in a block
  $n<m\le n+k$ of fixed length for every shift $n$, a statement about all
  blocks of one sequence rather than about the prefixes $P_t$ of a growing
  family; the mechanism's conclusion concerns prefixes on arcs of length
  $D/n$, and the problem is proved.
- [[problems/discrepancy/E0987/_index|Problem 987]] (exponential sums of a
  sequence in $(0,1)$; proved) and
  [[problems/irrationality/E0998/_index|Problem 998]] (bounded remainder
  intervals of $\{\alpha m\}$; disproved as worded, with Kesten's length
  criterion the correct theorem) are resolved, and the Kronecker sequence
  that appears in the balanced-stick preprint enters the folder only
  through the imported Theorem 3, which is not reconstructed.
- [[problems/discrepancy/E0992/_index|Problem 992]],
  [[problems/discrepancy/E0994/_index|Problem 994]],
  [[problems/discrepancy/E0995/_index|Problem 995]] and
  [[problems/analysis/E0996/_index|Problem 996]] are metric statements for
  almost every $\alpha$; the mechanism is deterministic for one sequence
  and carries no metric information.
- [[problems/discrepancy/E0988/_index|Problem 988]],
  [[problems/discrepancy/E0989/_index|Problem 989]] and
  [[problems/discrepancy/E0991/_index|Problem 991]] concern finite point sets on
  the sphere or a sequence in the plane without the one-insertion-per-step
  structure, and are resolved.
- The integer-sequence gap problems (for instance
  [[problems/integer_sequences/E0208/_index|Problem 208]] and
  [[problems/additive_bases/E0153/_index|Problem 153]]) concern the gaps of one
  fixed set, not of a growing family, and the theory tree holds no claim
  about sequences in the unit interval.

**Outcome.** Open: no second consumer in the corpus, so no method page is
made. A future consumer would be recognized by a hypothesis that controls
the $r$-th neighbor distances of a nested growing family uniformly in the
position to within an error small compared with $r$, and a conclusion that
counts terms in short arcs; the (4.3) count of 1949, rerun on the interval
in Proposition 480.1, is the only transfer of the folder's mechanisms to
another setting proved here.
