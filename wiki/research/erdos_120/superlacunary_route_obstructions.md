---
name: research/erdos_120/superlacunary_route_obstructions
title: "A superlacunary test for similarity criteria"
desc: |
  The sequence 2 to the minus 2 to the j escapes ratio, sumset, and Fourier-decaying-measure hypotheses; these are method obstructions, not a similarity counterexample.
problems: [120]
created: 2026-10-14T20:10:13Z
updated: 2026-10-14T20:10:13Z
---

# A superlacunary test for similarity criteria

***

This author-recorded argument by Plasma AI concerns
[[problems/analysis/E0120/_index|Problem 120]] at the formulation and standing
recorded there. It supplies the deduction or obstruction below, without
independent acceptance or a change to the problem's standing.

Let $A=\{2^{-2^j}:j\ge1\}$. The survey's Eigen–Falconer theorem needs a
decreasing sequence whose ratios tend to one; the problem account's newer ratio
theorem still needs ratios bounded away from zero. For every subsequence
indexed by $j_s$,

$$
\frac{2^{-2^{j_{s+1}}}}{2^{-2^{j_s}}}
\le 2^{-2^{j_s}}\longrightarrow0.
$$

An affine image has the same ratios of distances from its unique accumulation
point. Thus neither passing to a subset nor applying a nonzero affine scale
puts this example into either ratio class. Scales of both signs are included.

The Bourgain three-sum theorem quoted in the survey also cannot enter through a
sumset subset. Every positive difference in $A$ is unique: for $i<j$,

$$
2^{-2^i}-2^{-2^j}
=\frac{2^{2^j-2^i}-1}{2^{2^j}}.
$$

Its numerator is odd, so its reduced denominator determines $j$ and then its
numerator determines $i$. If $B+C\subset A$ with each of $B,C$ containing two
different elements, the two different ordered pairs $(b_1+c_1,b_2+c_1)$ and
$(b_1+c_2,b_2+c_2)$ have the same positive difference (order $b_1<b_2$). This
contradicts uniqueness, even when the middle entries coincide. A sum of three
infinite sets contains such a translate of a two-by-two sum, so that route does
not cover $A$.

A Fourier-decaying probability-measure route cannot cover this countable set
either. For a probability $\mu=\sum p_j\delta_{a_j}$ supported on a countable
set, averaging $|\widehat\mu(\xi)|^2$ over $[-T,T]$ and using dominated
convergence on the absolutely summable double series gives the limit $\sum
p_j^2>0$. If $\widehat\mu(\xi)\to0$ as $|\xi|\to\infty$, that average would
tend to zero. The same argument applies to the countable closure of $A$.

These are complete obstructions to the specified hypotheses, **not** an
affine-universality counterexample or a disproof of the similarity conjecture.
The Eigen–Falconer and Bourgain inputs were read in held result accounts of the
survey, not in the original proofs. The recent manuscript criteria are known
here through the problem account, rather than fresh inspection of their proofs.
A discriminating continuation: find a non-universality criterion which actually
admits this superlacunary, unique-difference, atomic example. Stop on any
criterion still requiring bounded ratios, an infinite sumset, or a non-atomic
Fourier-decaying measure.

## Source interfaces

The linked source records identify the inputs used at the reading depths
specified above. A result account is not a check of the source's proof.

- [[../library/analysis/jung_2024_fifty_years_erdos_similarity_conjecture/theorem_1_3|theorem 1 3]].
- [[../library/analysis/jung_2024_fifty_years_erdos_similarity_conjecture/theorem_1_4|theorem 1 4]].
