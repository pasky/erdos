---
name: research/sunflower_exponential_bound
title: Sunflower exponential bound
desc: |
  The attack on Problem 20 through spread families: the target is equivalent
  to a sunflower statement for spread families. Explicit constructions
  test matching, bounded-core, and maximal-rate link routes. Linear word
  families, families of bounded additive growth, and families on linearly
  many points satisfy exponential bounds. A linear counting extension
  gives Fourier criteria allowing arbitrary cores; the unrestricted
  structural inverse remains open.
created: 2026-10-15T17:54:12Z
updated: 2026-10-16T00:33:41Z
---

# Sunflower exponential bound

[[research/_index|..]]

[[research/sunflower_exponential_bound/additive_word_families|additive_word_families]]: Binary word families with bounded fourfold growth lie densely in an
affine linear family and obey an exponential sunflower bound. Standard
sumset estimates give a bounded-doubling corollary.

[[research/sunflower_exponential_bound/agreement_statistics|agreement_statistics]]: A counting form of linear Hall bounds the probability of the sunflower
coordinate pattern in binary affine word spaces, including all-equal
tuples. Small Fourier bias forces genuine sunflowers above an exponential
size threshold. Random-matching thresholds and equal pair profiles test
this route; the structural inverse remains open.

[[research/sunflower_exponential_bound/fukuyama_sequence_gap|fukuyama_sequence_gap]]: Full transversals satisfy the spread hypothesis of arXiv:2212.13609v3 but
violate Lemma 2.1 and admit no sequence satisfying (2.4). The missing
factor in Case 3 cannot be supplied by the stated hypotheses.

[[research/sunflower_exponential_bound/linear_word_families|linear_word_families]]: A linear Hall argument finds a subspace on which every coordinate map
is zero or injective. It gives an alphabet-independent exponential
sunflower bound for affine linear word families over finite fields.

[[research/sunflower_exponential_bound/maximal_rate_chain_obstruction|maximal_rate_chain_obstruction]]: For arbitrarily large exponential size, a family with matching number two
can force every maximal-rate link chain into a sunflower-free family.
An explicit sunflower can be retained outside the chosen chain.

[[research/sunflower_exponential_bound/maximal_rate_links|maximal_rate_links]]: Exact excess formulas show that the maximal-rate link procedure succeeds
at its first step on L214 and L215, although these families defeat
matching and bounded-core statements at fixed spread.

[[research/sunflower_exponential_bound/proof_sketch|proof_sketch]]: Problem 20 is equivalent to a sunflower statement for spread families; L214
refutes the constant-spread matching route and L215 any bounded-core
variant. Maximal-rate link chains can fail; a linear Hall argument bounds
affine linear word families, and slice rank handles links on few points.
A counting extension gives Fourier criteria allowing arbitrary cores.
The general structural inverse remains open.

[[research/sunflower_exponential_bound/refined_spread_obstructions|refined_spread_obstructions]]: Decreasing block scales give intersecting families with spread of order
log n/log log n. An anchored first-moment argument converts normalized
spread to absolute spread without a bound on the original family size.

[[research/sunflower_exponential_bound/slice_rank_spread_links|slice_rank_spread_links]]: The slice-rank bound for words, in projection form, gives three-petal
sunflowers in families of m-sets on few points, so every spread link in a
counterexample is unbalanced. Sections reach the unthinned obstruction
families, and projected matchings reach their random thinnings. The
general dichotomy remains open.

[[research/sunflower_exponential_bound/spread_matching_obstruction|spread_matching_obstruction]]: Substitution powers of intersecting seeds have an exactly computable spread
whose limit is a one-level seed quantity; block seeds give intersecting
families with spread log n/(log log n)^2, and inner sunflower-free seeds
force large sunflower cores.

***

This folder holds the attack on
[[problems/set_systems/E0020/_index|Problem 20, the Erdős–Rado sunflower problem]]
through spread families. The
[[research/sunflower_exponential_bound/proof_sketch|proof sketch]] states the
target, the equivalent spread form, the links held so far at their standing,
and the open gap. The
[[research/sunflower_exponential_bound/spread_matching_obstruction|obstruction note]]
explains the substitution construction behind the claims
[[theory/set_systems/L214_spread_intersecting_families/_index|L214]], which
gives intersecting families at arbitrarily large spread,
and [[theory/set_systems/L215_spread_large_core_sunflowers/_index|L215]],
which shows that spread does not force a sunflower with a bounded core, and
records what that leaves for a proof.

The existence of highly spread intersecting families is already known
from the literature cited on L214; the substitution formulas here provide
an explicit alternative. The
[[research/sunflower_exponential_bound/maximal_rate_chain_obstruction|maximal-rate chain obstruction]]
shows that always choosing a densest link can miss a sunflower even at
arbitrarily large exponential size. The
[[research/sunflower_exponential_bound/fukuyama_sequence_gap|product-family source test]]
identifies a specific failed intermediate assertion in an outside claimed
proof. These are author-recorded arguments. They do not settle the full
question or establish acceptance of the pending claim on the problem page.

On the positive side, the
[[theory/set_systems/L268_linear_word_sunflowers/_index|linear Hall argument of L268]]
proves an exponential bound for affine linear word families over arbitrary
finite fields and arbitrarily large coordinate alphabets. Its
[[research/sunflower_exponential_bound/linear_word_families|dense-subset corollary]]
also bounds families of fixed positive density in an affine linear family. The
[[research/sunflower_exponential_bound/additive_word_families|additive-growth extension]]
also handles nonlinear binary word families of bounded doubling or
fourfold growth. Their exact remaining gap is a structural argument for
general word families; passing to a linear span can introduce words that
were not in the family.

The
[[research/sunflower_exponential_bound/slice_rank_spread_links|slice-rank note]]
treats three petals whatever the core. A routine form of the slice-rank
bound gives sunflowers in families of $m$-sets on few points, so every
spread link in a counterexample uses many more points than its spread
forces. The note also reduces the three-petal case to intersecting spread
families, and records which obstruction families the bound reaches
through sections and projected links, and which remain.

The
[[research/sunflower_exponential_bound/agreement_statistics|agreement-statistics note]]
extends the linear Hall argument to a uniform lower bound on the
probability of the coordinate sunflower pattern in binary affine spaces,
including all-equal tuples. Subtracting those tuples and using an explicit
Fourier norm bound gives a criterion for genuine sunflowers with arbitrary
cores. The note also proves
the exponential threshold for matchings in random word families and gives
two families with identical aggregate pair-agreement profiles but different
sunflower behavior. A structural argument turning Fourier bias into a
restriction with controlled total loss is still missing.
