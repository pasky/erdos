---
name: research/erdos_1221/larcher_finite_prefix_interface
title: "Larcher's finite-prefix interface and qualitative ratio growth"
desc: |
  Larcher's Section 3 explicitly treats a finite list before deriving its
  infinite-sequence theorem; his optimized constant is unchecked. Any positive
  logarithmic constant gives the ratio limit, and an elementary finite-list
  bound supplies one, while compactness with Schmidt's countability theorem
  gives an independent qualitative route.
problems: [1221]
created: 2026-10-14T20:10:13Z
updated: 2026-10-16T06:44:50Z
---

# Larcher's finite-prefix interface and qualitative ratio growth

***

The mean-normalized target of [[problems/analysis/E1221/_index|Problem 1221]]
permits repeated points. The [[research/erdos_1221/connections|existing
multiset extension]] and
[[research/erdos_1221/ko26b_theorem_1_1_reconstruction|closing reconstruction]]
rest on the span-to-count argument and, as the preprint argues, on two imported
discrepancy theorems. This page records what Larcher's paper supplies for the
first import and two ways to do without its optimized constant. The
[[research/erdos_1221/all_sequence_composition|composed argument]] now carries
the whole chain for all sequences, with the
[[research/erdos_1221/finite_list_prefix_bound|elementary finite-list bound]]
in place of the first import. This source-interface analysis and the constant
calculation below are author-recorded by Plasma AI; they supply no independent
acceptance of the full chain.

## What the source actually states

Section 3 of Gerhard Larcher's
[[../library/analysis/larcher_2014_star_discrepancy_sequences_unit_interval/_index|On
the star discrepancy of sequences in the unit interval]], arXiv:1407.2094v1,
starts with an arbitrary finite list $x_1,\ldots,x_N\in[0,1)$, $N=\lfloor
a^t\rfloor$, $3<a<4$. Writing $D_j(u)=\#\{i\le j:x_i<u\}-ju$, it applies the
auxiliary lemmas to the integral of $\max_{j\le N}D_j-\min_{j\le N}D_j$ and
concludes, before passing to an infinite sequence, that some $j\le N$ has

$$
\sup_u|D_j(u)|\ge c_a\log N,
\qquad c_a=\frac{(a-2)(8a+3)}{16(1-2a)^2\log a}.
$$

Thus the required finite-list quantifier is present in the proof itself; it is
not inferred merely from the abstract's infinitely-many-prefixes theorem.
Section 3 and the definitions at the start of Section 2 have been inspected in
the source TeX. The complete optimization proof of the auxiliary lemmas has not
been checked. The text writes block endpoints such as $a^{t-1}$ and the
equality $t=\log N/\log a$ while suppressing integer-rounding adjustments, and
counts distinct jump locations. These points need explicit handling in a fully
checked derivation. No discrepancy constant is newly certified here.

Under the finite-list bound as stated, any list of length $L$ has $H_L\ge
c_a\log L-O_a(1)$: keep the prefix of the largest $\lfloor a^t\rfloor\le L$.
Its logarithm differs from $\log L$ by $O_a(1)$, and the maximum over prefixes
cannot increase when prefixes are removed. At $a=7/2$, the source's expression
is $31/(384\log(7/2))>1/16$, so an absolute large-$L$ threshold gives the
constant used in the existing reconstruction, provided the source's finite-list
estimate is established with an additive error bounded uniformly in the list.
Repeated coordinates are covered by the ordered-perturbation argument in
Proposition 1221.1 of the connections page: for every $\eta>0$ a distinct list
has prefix error at most $H_L+\eta$, and then $\eta\downarrow0$ transfers a
universal lower bound.

## The qualitative ratio needs only a positive constant

Suppose, more weakly, that every finite list satisfies $H_L\ge c_0\log L-C_0$,
with absolute $c_0>0$ and $C_0$. Proposition FP of the
[[research/erdos_1221/finite_list_prefix_bound|finite-list page]] proves this
with $c_0=1/(16\log4)$ and $C_0=1/16$, by Larcher's range splitting and a
quadratic potential, without his optimized lemmas. The span-to-count estimate
and its reading for multisets are checked on the
[[research/erdos_1221/all_sequence_composition|composition page]]. Set
$A=\alpha\log r$ with $0<\alpha<c_0/6$. The ratio contradiction then gives

$$
B=3A+O\left(\frac A{\log(r/A)}\right)
 =3\alpha\log r+O(1),
\qquad S=\frac{\sqrt{Ar}}{\log^2(r/A)}.
$$

The multiset extraction gives a list of length $L'\in[\lfloor
S\rfloor-B,\lfloor S\rfloor+B]$ with $H_{L'}\le B$. Since $B/S\to0$,

$$
\log(\lfloor S\rfloor-B)
 =\tfrac12\log r-\tfrac32\log\log r+O(1).
$$

Consequently $3\alpha\log r+O(1)\ge(c_0/2)\log r-O(\log\log r)$, a
contradiction. All constants are independent of the original sequence. This
yields $\mu_r-1\ge\alpha\log r/r$ for large $r$, hence $r(\mu_r-1)\to\infty$;
with Proposition FP, $\alpha=1/200$ is admissible, and the composition page
writes the comparison out. The two one-sided divergences need the separate
planar $L^1$ input, which the composition page takes from the
[[research/erdos_1221/halasz_planar_l1_bound|written-out Halász bound]].

## A qualitative finite-prefix bound from a held source

For the limit $r(\mu_r-1)\to\infty$, even a logarithmic discrepancy rate is
unnecessary. The following compactness argument uses the
[[../library/discrepancy/schmidt_1972_irregularities_distribution/corollary_p64|countability
corollary of Schmidt's 1972 part VI]], rather than the different planar theorem
of part VII. For every infinite sequence in $(0,1]$, that corollary says the
set of $u$ at which the anchored counting error stays bounded is countable.
The definitions and corollary were checked against Section 1 of the held
transcription, printed pp. 63--64. Its published proof is an external premise,
not independently reverified here.

**Uniform qualitative bound.** For every finite $K\ge0$ there is an integer
$L_K$ such that every list $z_1,\ldots,z_L\in[0,1]$ with $L\ge L_K$ has
$H_L>K$, allowing repeated entries. Here $H_L$ has the strict counting
convention of the
[[research/erdos_1221/ko26b_lemma_4_2_reconstruction|finite-prefix interface]].

*Proof.* For a prefix of length $j$, let
$z_{(1)}\le\cdots\le z_{(j)}$ be its order statistics, retaining
multiplicity. Its star discrepancy in counting units is

$$
\sup_{0\le u\le1}
\left|\#\{i\le j:z_i<u\}-ju\right|
=\max_{1\le i\le j}
\max\{i-jz_{(i)},\ jz_{(i)}-(i-1)\}.
$$

The left and right limits at each distinct coordinate give the two extrema;
within a repeated block the last and first indices, respectively, give the
extremal values. At $0$ and $1$ the same formula holds, with the unused
one-sided value contributing only zero. Order statistics are continuous in
the coordinates. Thus $H_j$, the maximum of this expression over its first
$j$ prefixes, is continuous on $[0,1]^j$.

Suppose arbitrarily long finite lists had $H_L\le K$. In the compact product
$[0,1]^{\mathbb N}$, put

$$
\mathcal C_L=\{z:H_L(z_1,\ldots,z_L)\le K\}.
$$

These sets are closed, nested and nonempty: any sufficiently long list supplies
the needed prefix and can be extended arbitrarily. Compactness gives an
infinite sequence in their intersection, with every prefix discrepancy at most
$K$. In any prefix, letting $u\downarrow0$ shows that its number of zero
entries is at most $K$. Hence the whole sequence contains at most
$\lfloor K\rfloor$ zero entries. Replace them by $1$. This produces a sequence
in $(0,1]$ and changes every prefix counting error by at most
$\lfloor K\rfloor$. For this sequence every $u\in(0,1]$ therefore has error
bounded by $2K$ at every prefix, contradicting Schmidt's countability
corollary. This proves the uniform bound. $\square$

This is an author-recorded deduction by Plasma AI, with no effective estimate
for $L_K$. It does not certify Larcher's constant or rounding argument. The
composed argument uses Proposition FP instead, so this bound is an independent
alternative resting on Schmidt's published theorem.

## Closing the qualitative ratio with a fixed parameter

This uses the all-sequence span-to-count implication of
[[research/erdos_1221/ko26b_proposition_3_1_reconstruction|Proposition 3.1]]
and the multiset extraction in Proposition 1221.1 of the
[[research/erdos_1221/connections|connections page]], read for coincident
terms on the composition page. The latter supplies a list of length $L'$ with
$H_{L'}\le B$ and $|L'-\lfloor S\rfloor|\le B$. These inputs keep the standing
the composition page records.

Fix any real $A\ge1$. If for some sequence
$\limsup_n M_n^{(r)}/m_n^{(r)}<1+A/r$, choose $0<C<A$ so that the ratio
is at most $1+C/r$ for all sufficiently large $n$. The mean-span identity
$nm_n^{(r)}\le r\le nM_n^{(r)}$ then gives

$$
n(M_n^{(r)}-m_n^{(r)})\le C,\qquad
nM_n^{(r)}\le r+C.
$$

With $n=\lfloor t\rfloor$, the nonnegative choices
$a_t=r-nm_n^{(r)}$ and $b_t=tM_n^{(r)}-r$ satisfy
$a_t+b_t\le C+(r+C)/n<A$ eventually. Thus the same real-time span
hypothesis used in the
[[research/erdos_1221/ko26b_theorem_1_1_reconstruction|closing reconstruction]]
holds, including for coincident terms as read on the composition page.
Proposition 3.1 gives

$$
B=3A+\frac{C_1A}{\log(r/A)},\qquad
S=\frac{\sqrt{Ar}}{\log^2(r/A)}.
$$

As $r\to\infty$ with $A$ fixed, $B\le4A$ eventually and $S\to\infty$.
The extracted list consequently has $L'\ge\lfloor S\rfloor-B\to\infty$
and $H_{L'}\le4A$. This contradicts the uniform qualitative bound with
$K=4A$. Its length threshold depends on $A$ but not on the sequence, so for
every fixed $A$ and all sufficiently large $r$, no sequence has the strict
ratio bound above. Taking the infimum over sequences yields
$r(\mu_r-1)\ge A$. Since $A$ was arbitrary, the ratio expression tends to
infinity, with the standing of these inputs.

The eventual time at which a sequence obeys the count bound may depend on that
sequence; the contradiction only needs its existence. The threshold in $r$
does not depend on the sequence. This separates the two quantifiers and avoids
a uniformity claim about convergence times.

This qualitative route is independent of both Larcher's optimized
minimization and Proposition FP, but rests on Schmidt's published theorem. It
gives no logarithmic rate, no coefficient $1/100$, and neither one-sided
divergence. The rate $\mu_r-1\ge\log r/(200r)$ follows instead from
Proposition FP, and the one-sided conclusions from the planar $L^1$ bound,
whose statement in counting normalization is Bilyk's
[[../library/discrepancy/bilyk_2011_roth_orthogonal_function_method/equation_1_14|exposition
of Halász's bound]] and whose proof is written out on the planar page; both
are composed on the composition page. Larcher's optimized lemmas would raise
the ratio coefficient to Korsky's $1/100$, and they remain unchecked.
