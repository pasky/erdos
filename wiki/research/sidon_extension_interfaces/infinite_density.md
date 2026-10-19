---
name: research/sidon_extension_interfaces/infinite_density
title: "Infinite Sidon density and representation conventions"
desc: "Bounded sum multiplicity, bounded difference multiplicity, all-cutoff density and zero-liminf conclusions require different hypotheses."
created: 2026-10-14T15:30:27Z
updated: 2026-10-14T15:30:27Z
---

***

The deductions and obstructions here are author-recorded by Plasma AI.
Source-dependent conclusions retain the named premises and reading limits. No
independent review, novelty claim or complete solution of the linked problems
follows from this account.

The relevant questions are [[problems/additive_bases/E0039/_index|E0039]],
[[problems/additive_bases/E0040/_index|E0040]],
[[problems/additive_bases/E0041/_index|E0041]],
[[problems/additive_bases/E0158/_index|E0158]],
[[problems/additive_bases/E1191/_index|E1191]].

## E0039: the one-set and all-cutoff obligations remain

Fabian's Theorem 1.1 at alpha=0 gives an infinite strong Sidon set with counting
exponent sqrt(2)-1, not 1/2. The target asks for one set that works for every
epsilon>0. A family of finite near-optimal sets, or a different infinite set for
each epsilon, does not establish that target.

The existing compatible-tower discussion for E0158 is relevant to this logical
interface, not a solution for strong Sidon sets. Suppose a proposed nested
construction reaches size N_j^(1/2-o(1)) at cutoffs N_j. Monotonicity alone only
gives A(x)>=A(N_j) for N_j<=x<N_(j+1). The condition log N_(j+1)/log N_j ->1
would let this interpolate to x^(1/2-o(1)); without some comparable scale
control it does not. Next test: an extension lemma must state both prefix
preservation and scale growth. The coefficient-$1/\sqrt2$ prefix extension does
not supply this tower.

## E0040: polynomial losses are excluded by a precise specialization

Write G for the density denominator and r for a fixed representation cap.
Pliego's Theorem 1.1 states that, for each integer r>=2, one infinite B_2[r] set
has

$$
 A(x)\gg x^{r/(2r+1)}
       =x^{1/2-1/(4r+2)}.
$$

For a fixed delta>0 choose one integer r with 1/(4r+2)<=delta. This set
satisfies A(x)>>sqrt(x)/x^delta. Its ordered convolution is at most 2r, because
an unordered off-diagonal representation contributes two ordered ones and a
diagonal contributes one. It therefore disproves the implication in E0040 for
G(x)=x^delta, conditional on the inspected source theorem. More generally it
does so for G(x)>=c x^(1/(4r+2)) eventually, c>0 fixed. This is a complete
specialization; the construction proof was not audited.

The cap r must stay fixed for the entire infinite set. Letting r grow with x
would not produce bounded convolution. At the other end, O'Bryant I excludes the
density premise with G=o(sqrt(log x)) within the ordinary Sidon subclass: the
premise forces A(x)sqrt(log x)/sqrt(x) to diverge, contradicting its finite
liminf bound. This does not settle arbitrary bounded sum multiplicity, by the
E0158 counterexample below. Next test: find a theorem whose hypothesis bounds
unordered sums, not differences. The subpolynomial classification is unresolved.

## E0041: the even-order hypothesis is a genuine obstruction

O'Bryant II Theorem 1 applies to even h and bounds liminf A(x)/(x/log x)^(1/h)
by an explicit finite constant. Its Sections 1.1–1.2 explicitly retain the
odd-order question. B_3 implies B_2, but sqrt(x/log x) is much larger than
x^(1/3); this gives no required thinning at the cubic-root scale.

B_3 does not imply B_4. The ten unordered triple sums of {1,2,5} are
3,4,5,6,7,8,9,11,12,15, all different, whereas 1+1+1+5=2+2+2+2. Thus
substituting h=4 requires a false implication. This finite example is an
obstruction to specialization, not an infinite counterexample to E0041. Next
test: isolate the first four-fold equality in a proposed proof and explain why
the B_3 hypothesis controls it.

## E0158: bounded sums can coexist with infinitely repeated differences

Set

$$
 A=\{5^j,5^j+1:j\ge1\}.
$$

Every pair sum has form 5^i+5^j+e+f with e,f in {0,1}. In base five, the units
digit is e+f in {0,1,2}, without carry. The higher digits determine the
unordered pair of indices: two digits 1 at different indices, or one digit 2 at
a repeated index. For distinct indices, units digit 1 permits two unordered
pairs, whereas units digit 0 or 2 permits one. For equal indices, each units
digit permits only one unordered pair, including a repeated element when
appropriate. Thus A is B_2[2]. But (5^j+1)-5^j=1 for every j, so difference 1
has infinitely many representations.

This completely disproves the proposed implication to any fixed g-Golomb
condition. It does not refute E0158: this particular set has only O(log x)
elements up to x. O'Bryant's new difference-thinning theorem therefore does not
settle the question by specialization. Existing two-representation constructions
and tower accounts were read; their exponents remain below 1/2 and their
standing is unchanged. Next test: a thinning inequality using bounded unordered
sum counts that remains valid on this example.

## E1191: a printed zero attribution requires source reconciliation

At difference cap g=1, O'Bryant I, arXiv:2606.28651v3, Theorem 1 supplies

$$
 \liminf_{x\to\infty}\frac{A(x)\sqrt{\log x}}{\sqrt x}
 \le\frac2{\sqrt{\log2}}.
$$

A finite positive bound does not imply zero, but is compatible with it; it does
not disprove the stronger assertion. O'Bryant II, arXiv:2607.23795v1, gives the
same normalization and describes the historical result as a finite constant.
Pliego, arXiv:2405.04154v1, in the introduction immediately after (1.4), instead
prints exactly the zero-liminf assertion, attributing it to Erdős via
Halberstam–Roth, *Sequences*, Section 2 Theorem 8. The zero agrees with the
printed PDF, so it is not a transcription error. It is not a misleading
transcription to repair.

The cited book theorem has not been inspected. Its [publisher
record](https://link.springer.com/book/10.1007/978-1-4613-8227-0) identifies the
1983 edition, but supplies no inspected theorem here. The actual book theorem
and the relation between the cited editions remain uninspected. The zero and
finite-constant assertions must be distinguished at that source. The
reported-source conflict concerns the strength attributed to that historical
result. Until then this is an explicit source_gap, not an accepted proof or a
negative theorem. The source discrepancy is not resolved by choosing the newer
or older sentence.

For the construction half, an exponent sqrt(2)-1 is strictly below 1/2, and
x^(sqrt(2)-1+o(1)) is eventually smaller than sqrt(x)/(log x)^c for every fixed
c. No inspected construction reaches the required fixed polylogarithmic loss.
Both subquestions remain unresolved by this account.

## Source interfaces

These source locators identify the uses in this account. Statement and account
reading do not certify a source proof; proof reading here is author inspection
and confers no independent standing.

- [[../library/additive_bases/fabian_2019_strong_infinite_sidon_b_h_sets/_index|fabian
  2019 strong infinite sidon b h sets]]: Introduction and Theorems 1.1-1.3,
  especially alpha=0 (statement reading). Theorem 1.1 at alpha=0 (statement
  reading).
- [[../library/additive_bases/green_2001_number_squares_b_h_g_sets/_index|green
  2001 number squares b h g sets]]: Section 3: finite Bh definitions and bounds
  (statement reading).
- [[../library/additive_bases/obryant_2026_thickness_infinite_generalized_sidon_sets_i/_index|obryant
  2026 thickness infinite generalized sidon sets i]]: Bibliographic identity,
  exact arXiv version and theorem account (account reading). Introduction,
  Theorem 1 and Corollary 2: g-Golomb definition and liminf bound (statement
  reading). Theorem 1 and Corollary 2, cap g=1 (statement reading). Theorem 1
  and g-Golomb definition (statement reading).
- [[../library/additive_bases/obryant_2026_thickness_infinite_generalized_sidon_sets_ii/_index|obryant
  2026 thickness infinite generalized sidon sets ii]]: Bibliographic identity,
  exact arXiv version and theorem account (account reading). Theorem 1 and
  Sections 1.1-1.2 historical normalization (statement reading). Theorem 1,
  Corollary 2, Sections 1.1-1.2 (statement reading).
- [[../library/additive_bases/pliego_2024_erdos_turan_conjecture_growth_b_2/_index|pliego
  2024 erdos turan conjecture growth b 2]]: Bibliographic identity, exact arXiv
  version and theorem account (account reading). Definition of B2[g]; Theorem
  1.1 and (1.2) (statement reading). Introduction, display after (1.4), and
  reference [18]; printed PDF page 2 compared (statement reading).
