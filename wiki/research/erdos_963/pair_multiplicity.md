---
name: research/erdos_963/pair_multiplicity
title: 'Repeated pair sums forced by low dissociation dimension'
desc: The target holds at restricted pair-sum multiplicity at most two; a counterexample must have exponentially many pairs with a common sum.
tags: []
sources: []
created: 2026-09-19T00:40:00Z
updated: 2026-10-13T05:28:09Z
---


# Repeated pair sums forced by low dissociation dimension

***

These are proved restrictions, not a solution of the unrestricted problem.
For a finite positive real set $P$, write $n=|P|$, $d=d(P)$, and


$$
\mu(P)=\max_t\#\{\{a,b\}\subseteq P:a\ne b,\ a+b=t\}.
$$


The pairs counted for a fixed $t$ are pairwise disjoint. We prove that the
target $n\le2^d-1$ holds whenever $\mu(P)\le2$, and that in general


$$
\boxed{\displaystyle
\mu(P)\ge\frac{(n-d)(n-d+1)}{3^{d+1}-1}}
\qquad(d<n).                                      \tag{1}
$$


Thus a counterexample with $n\ge2^d$ must have at least three pairs with
a common sum and, as $d\to\infty$, at least
$(1-o(1))(4/3)^d/3$ such pairs.

## A random-extraction estimate

Sample distinct $X_1,\ldots,X_k$ uniformly in ordered positions from
$P$, where $k\le n$. A nonzero ternary relation must have both signs
because the elements are positive. Support one is impossible, and support
two would require equality of distinct sampled elements. For a fixed
mixed sign pattern with support $s\ge3$, select two coordinates with
the same sign. Once the other $s-2$ coordinates in the support are fixed,
their required sum is fixed. At most $2\mu(P)$ ordered pairs can supply
it. Consequently the probability of this relation is at most


$$
\frac{2\mu(P)}{(n-s+2)(n-s+1)}.                    \tag{2}
$$


There are fewer than $(3^k-1)/2$ mixed sign patterns up to reversing all
signs. A union bound therefore gives


$$
\Pr(\{X_1,\ldots,X_k\}\text{ is dependent})
\le\frac{\mu(P)(3^k-1)}{(n-k+2)(n-k+1)}.           \tag{3}
$$


For $k=d+1$, the probability on the left is one, proving (1).

Two refinements will handle the small dimensions in the next argument.

* For a singleton-versus-$(s-1)$ relation, leave two coordinates of the
  larger side unexposed. The singleton must be the largest of the $s-2$
  exposed entries. This has probability $1/(s-2)$. Conditional on the
  exposed entries, the same pair count applies. Hence the probability is
  at most

  $$
  \frac{2\mu(P)}{(s-2)(n-s+2)(n-s+1)}.             \tag{4}
  $$

* For a balanced four-term relation, expose one of its pairs. That pair
  already occupies one representation of its sum and cannot be reused.
  The probability is at most

  $$
  \frac{2(\mu(P)-1)}{(n-2)(n-3)}.                 \tag{5}
  $$


The use of (4) is legitimate without independence assumptions: conditional
on any exposed tuple the completion probability is bounded by (2), and
only tuples having the stated largest-entry property can contribute.

## The target when $\mu(P)\le2$

It suffices to find a dissociated $k$-set whenever $n\ge2^{k-1}$.
For $k\le5$ this is supplied by the established positive small cases in
[[research/erdos_963/proof_sketch|the proof sketch]].

For $k=6$, evaluate the union bound at $n=32$, using (4) for singleton
patterns, (5) for balanced support four, and (2) otherwise. The contributions
of supports three, four, five, and six are respectively


$$
\frac8{31},\qquad \frac7{29},\qquad
\frac{10}{29},\qquad \frac{53}{378}.
$$


For example the support-six contribution is
$(6\cdot4/4+15\cdot4+10\cdot4)/(28\cdot27)$: the three terms
come from the $1+5$, $2+4$, and $3+3$ sign partitions. Their total is


$$
\frac{334549}{339822}<1.
$$


For $k=7,n=64$, (2) and (5) alone give the upper bound


$$
\frac{420}{63\cdot62}+
\frac{770}{62\cdot61}+
\frac{1260}{61\cdot60}+
\frac{868}{60\cdot59}+
\frac{252}{59\cdot58}<1.                           \tag{6}
$$


To verify the strict inequality without decimal approximations, its terms
are respectively smaller than (108/1000,204/1000,345/1000,246/1000,
74/1000), whose sum is $977/1000$. Again the terms are indexed by the
five possible support sizes.

For $k\ge8$, the crude estimate (3) suffices. At $k=8,n=128$,

$$
2(3^8-1)=13120<121\cdot122=14762.
$$

Writing $N=2^{k-1}$, both factors in the next threshold denominator
$(2N-k)(2N-k+1)$ exceed twice the respective factors of
$(N-k+1)(N-k+2)$ when $k\ge8$. Thus the denominator grows by a
factor greater than four. The numerator $3^k-1$ grows by a factor less
than four. This proves the strict inequality for all larger $k$.
All these probability bounds decrease as $n$ increases. In each case the
dependent-sample probability is less than one, establishing the assertion.

## A stronger odd-set case

If $O$ is positive odd and $\mu(O)=1$, then


$$
\boxed{|O|\le2^{d(O)-1}.}                         \tag{7}
$$


Put $k=d(O)+1$. At the hypothetical threshold
$n=2^{k-2}+1$, only even-support relations need be counted. Balanced
support-four relations are absent. For $k=5,6,7$, respectively, (2)
therefore gives the bounds


$$
\frac{40}{42}<1,\qquad
\frac{120}{210}+\frac{62}{156}=\frac{529}{546}<1,
\qquad
\frac{280}{930}+\frac{434}{812}<1.
$$


For $k\ge8$, the number of all even-support sign patterns up to reversal
is at most $(3^k+1)/4$. The analog of (3) is at most


$$
\frac{3^k+1}{2(n-k+1)(n-k+2)}.
$$


At $k=8,n=65$ this is $3281/3422<1$. The denominator grows by a
factor greater than four at successive thresholds, and the numerator by
a factor less than three. The cases $k\le4$ follow from the established
small cases. This proves (7).

By the valuation-layer argument in [[research/erdos_963/proof_sketch|the proof
sketch]], the target consequently holds for every positive integer set whose
individual (2)-adic valuation layers each have restricted pair-sum multiplicity
one. A counterexample must therefore have a four-point pair-sum equality
entirely within some valuation layer.

## What remains

Estimate (1) forces a large reflected-pair family in a potential
counterexample. It does not supply an augmentation from that family.
In particular, symmetry alone is insufficient for the naive step
$d(\{c-x,c+x:x\in X\})\ge d(X)+1$: take
$c=7$, $X=\{1,3,5\}$. The set $X$ is dissociated but its
reflection union is $2\{1,2,3,4,5,6\}$, of dimension three. Every
four-subset of $\{1,\ldots,6\}$ contains one of

$$
1+2=3,\quad1+3=4,\quad1+4=5,\quad1+5=6,\quad
2+3=5,\quad2+4=6,\quad3+6=4+5.
$$

Thus the repeated-pair restriction does not close the recorded rank-one,
binary-connected gap.
