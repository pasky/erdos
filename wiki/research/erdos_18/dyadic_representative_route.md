---
name: research/erdos_18/dyadic_representative_route
title: Dyadic representatives for the polylogarithmic factorial question
desc: |
  An editable route to Problem 18(c): a proved criterion with factorial
  index, length and height costs, counting obstructions to extracting it
  from the accepted proof of (b), and a stopped test of the full-divisor
  law at the collision estimate it needs.
created: 2026-10-14T08:41:00Z
updated: 2026-10-23T18:22:29Z
---

***

## Target and standing

Part (c) of [[problems/divisors/E0018/_index|Problem 18]] asks whether
$h(n!)<(\log n)^{O(1)}$. Each represented integer may use its own set of
distinct divisors. Part (a) has a pending claim graded sound by Plasma AI's
internal review; part (b), $h(n!)<n^{o(1)}$, has an accepted Lean proof.
Neither settles (c). The deductions on this page are Plasma AI's and
author-recorded. Their precise statements and proofs are
[[theory/number_theory/L63_polylogarithmic_dyadic_representatives/_index|L63]]
and [[theory/number_theory/L64_factorial_digit_entropy/_index|L64]], with
the full-divisor alternative in
[[theory/number_theory/L66_divisor_residue_spread/_index|L66]] and its
collision form in
[[theory/number_theory/L53_divisor_product_collision_criterion/_index|L53]],
all at tier 0. No solution of (c) is asserted.

## The local interface

Put $L(t)=1+\log_2(t+1)$. The sufficient construction is the following:
for every sufficiently large bit length $k$, every residue modulo $2^k$
has a nonnegative representative $S\le2^{kD}$ that is a sum of at most
$u$ divisors of $F!$, repetitions allowed, where fixed constants satisfy

$$
F\ll kL(k)^a,\qquad u\ll L(k)^b,\qquad D\ll L(k)^d.
                                                               \tag{1}
$$

L63 proves that (1) gives
$h(n!)\ll(\log n)^{a+b+d+3}$. The exponent is an upper bound from the
construction, not a claim of optimality. The local representatives remain
unconstructed.

The proof makes the composition explicit. Repeated subtraction of a
representative modulo $2^k$, followed by division by $2^k$, expresses an
integer with $t$ bits by polylogarithmically many divisors of a factorial
with index $O(tL(t)^a)$. Choose $k$ small enough relative to $t/D$ so
that the representative is smaller than the integer: the quotient stays
nonnegative. Adding factorial indices pays for powers of two used in
lifting, and merging equal summands costs only a further polylogarithmic
index. Finally, for $Q=n!/m!$, exact representatives of all $r<Q$ by
distinct divisors of $n!$ give

$$
h(n!)\le h(m!)+\max_{r<Q}\{\text{length of the representative of }r\}.
                                                               \tag{2}
$$

The quotient representation has summands at least $Q$; the remainder's
summands are smaller than $Q$. This enforces distinctness across the two
parts. Taking $n-m$ of order $n/L(n)^{a+1}$ yields the claimed bound after
polylogarithmically many steps.

This route uses only dyadic residue problems. It avoids a separate covering
of the 3-part or a Chinese-remainder composition. The alternative using
[[research/erdos_18/doorn_lemma_3_1_reconstruction|van Doorn's Lemma 3.1]]
still has a different interface: every residue modulo $n!/m!$ must be a
short sum of **distinct divisors of $m!$**, of total at most $m!$, none
divisible by the modulus. Separate modular coverings do not establish those
conditions or a simultaneous covering. The odd-modulus criterion in
[[research/erdos_18/doorn_lemma_3_2_reconstruction|Lemma 3.2]] also requires
its weighted collision sum to be less than one; its hypotheses have not been
verified for this factorial quotient.

## What the accepted proof supplies

The [[../library/divisors/jenw1n_2026_lean_proof_erdos_problem_18b/target|accepted target record]]
identifies the Conjectures.io source, the Problem 18 solution file that
Conjectures.io serves, from which the declarations below are read. Static
inspection of `WeightedDyadicMixing`,
`dyadic_modular_bounds_of_block_product_decay`, and
`dyadic_modular_bounds_of_weighted_dyadic_mixing` gives the following
parameters, for each **fixed** $a>1$ and all sufficiently large $k$:

$$
F=r(\lceil k^a\rceil+2k),\qquad
u=s\bigl((\operatorname{binaryLength}(k)+1)^r+1\bigr),
\qquad D=r+1.                                          \tag{3}
$$

Here $r,s$ are fixed after the nonconcentration and mixing parameters are
chosen. The output is a bounded nonnegative representative by a multiset of
divisors, the convention used in (1). The source's final presentation bounds
$u$ by an arbitrarily small power of $k$, but the displayed construction
already has polylogarithmic $u$. The obstruction to substituting (3) in (1)
is the factorial index $k^a$.

The mixing declaration fixes a nonconcentration exponent $g>0$ first, then
produces a product count $r$, a decay exponent $t>0$, and a starting scale.
It gives no quantitative bound on these outputs as $g\downarrow0$. Choosing
$a=1+o(1)$ with $k$ therefore requires new estimates; the fixed-$a$
theorem does not justify it. No Lean build or new formal verification is
part of this deduction.

## A proved limitation of the separated digits

The source builds `binaryBlockSet` from an initial odd integer below
$2^{b_0}\le F$, followed by separated blocks. A block of width $w$ is
zero or a divisor of $F!$ smaller than $2^w$, and the total width is $k$.
For $F\le kL(k)^C$ and at most $L(k)^B$ such blocks, L64 proves

$$
\log_2|\operatorname{binaryBlockSet}|=o(k).             \tag{4}
$$

It counts large prime factors across **all** blocks against the same bit
budget. Thus every probability law on this support has an atom of mass
at least $2^{-o(k)}$. At level $k$, the hypothesis of
`WeightedDyadicMixing` would require each residue mass to be at most
$2^{-gk}$. This fails for every fixed $g>0$.

Consequently this construction cannot retain fixed positive
nonconcentration while its factorial index is linear up to logarithms and
its block count is polylogarithmic. L66 supplies the missing restriction on
varying parameters: every universal mixing witness satisfies $rg\ge1$.
Thus $g=g(k)\to0$ forces $r=r(k)\to\infty$, and the displayed bound
$s((\operatorname{binaryLength}(k)+1)^r+1)$ exceeds every fixed power of
$\log k$. Even granting uniform starting thresholds, parameter changes
alone cannot make this bound satisfy (1). Reopening this construction
requires a different representation argument or a different law, not merely
a quantitative choice of its existing parameters.

## Quantitative mixing for the full divisor law

L66 supplies an unconditional input for a different law. Uniformly choose
an odd divisor of $K!$. There is an absolute $c>0$ such that its mass in
each residue modulo $2^j$ is at most

$$
2^{-g_Kj},\qquad g_K=\frac{c}{\log_2(K+1)},\qquad 2\le j\le K.
                                                               \tag{5}
$$

The proof pairs the exponents of a set of primes whose product is smaller
than $2^j$. In each cell the remaining squarefree products are distinct
modulo $2^j$, so one residue receives at most one divisor per cell. A
Chebyshev estimate supplies enough such primes. This controls the full
divisor law, whose height is not restricted to one separated block.

If the witnesses in `WeightedDyadicMixing` can be chosen with
$r,J_0,1/t\ll g^{-A}$ for one fixed $A$, L66 proves part (c). A product
of $r$ divisors of $K!$ is one divisor of $(rK)!$; it incurs no
$(\log K)^r$ expansion. A further polylogarithmic number of additive
copies covers the high conductors. A uniform binary reserve with
$\max(1,J_0)$ digits kills the low conductors and costs a polylogarithmic
factorial index, length and height. L63 then gives exponent at most
$3A+4$. These polynomial parameter bounds remain unproved.

The source identifies a concrete loss to test. In
`exists_dyadic_unit_product_fourier_decay`, after $R$ flattening steps,
it sets $N=2^{R+2}$ and $t=(g-\delta)/N$, with
$\delta=\min(g/2,1/2)$. The final weighted theorem takes $r=R+2$.
For $0<g\le1/2$, the supplied decay is therefore

$$
t=\frac{g}{2^{R+3}}.                                  \tag{6}
$$

L66 proves that any universal weighted mixing assertion requires $rg\ge1$:
test it on the odd integers below $2^{\lceil gJ\rceil+1}$. Their product
law cannot decay at the primitive frequency if $rg<1$. Since the source
takes $r=R+2$, (6) therefore forces

$$
\frac1t\ge\frac2g\,2^{1/g}.
$$

For $g=g_K$ this is a positive power of $K$, even before any further
quantitative losses. Thus the **displayed source witnesses** cannot give
the polynomial parameters required here. Merely improving the flattening
step count to $O(\log(1/g))$ is incompatible with $rg\ge1$ in this
universal argument. The next construction test must replace the
Fourier conversion losing $2^R$, prove a stronger property of the
particular divisor law, or obtain coverage by another route. This is not
a refutation of those alternatives. Their starting scale, including any
cutoff involving $\varepsilon$, must also fit the local index and length
bounds.

The generic comparison itself is sharp under its bare hypotheses. Modulo
$4$, take $f=(3\delta_1+\delta_3)/4$, and let every dilation law be the
point mass at $1$. At frequency $1$, $|\widehat f|=1/2$. The product
iteration leaves $f$ unchanged. The symmetrized initial law has Fourier
coefficient $1/4$, and $R$ averaging steps square it $R$ times, giving
$2^{-2^{R+1}}$. Thus a comparison
$|\widehat f|^P\le2^{-2^{R+1}}$ requires $P\ge2^{R+1}$, exactly the
power in `norm_dft_unit_product_final_power_le`. Normalization and
nonnegativity alone cannot lower that power. The point-mass dilation laws
fail nonconcentration, so this example does **not** refute an improved
comparison using the mixing theorem's additional hypotheses.

## An additive Fourier estimate to test

One possible replacement is a law on odd divisors of $F!$ themselves,
instead of the separated-digit set. The last section of
[the proof of L63](../../theory/number_theory/L63_polylogarithmic_dyadic_representatives/_proof.md)
gives an exact sufficient Fourier estimate. For a nonempty set $X$ of odd
divisors, seek

$$
\left|\frac1{|X|}\sum_{z\in X}e^{2\pi i az/2^j}\right|
\le2^{-\eta\min(j,E)}
\quad(2\le j\le k,\ a\text{ odd}),                    \tag{7}
$$

with $F\ll kL(k)^C$ and both $\eta^{-1}$ and $k/E$ polylogarithmic.
Convolving polylogarithmically many copies of this law and one uniform law
on $\{0,1\}$ covers every residue; the last factor handles parity exactly.
The representatives have height at most $qF!+1$ for a polylogarithmic
number $q$ of copies, which already has an admissible polylogarithmic
height exponent. Thus no additional height truncation is necessary for
this version of (1).

Estimate (7) is unproved. A collision count for a single law does not by
itself supply its pointwise additive Fourier bounds; for a product of two
independent factors it does once the collision decay exponent exceeds one
half, as the next section explains. Small finite profiles cannot establish
cancellation for all conductors up to $k$. A useful test must either
prove (7) on the needed scales, produce another construction satisfying
(1), or identify the exact estimate that prevents doing so. An estimate
confined to $j=O(\log F)$ does not alone meet this interface when
$F=k(\log k)^{O(1)}$.

## The product-collision test

The replacement test sought a conversion without the loss in (6), or a
stronger property of the full divisor law.
[[theory/number_theory/L53_divisor_product_collision_criterion/_index|L53]]
supplies the conversion. For independent $x\sim\alpha$ and $y\sim\beta$
modulo $2^j$ and odd $a$, the classical bilinear bound is

$$
\bigl|\mathbb E\,e^{2\pi iaxy/2^j}\bigr|\le2^{j/2}\|\alpha\|_2\|\beta\|_2.
                                                               \tag{8}
$$

It turns a collision decay exponent above one half into additive decay for a
product, and nothing is raised to a power that grows with the number of
steps. The Conjectures.io source applies the same bound in its last step, to a
sum-product average; its loss comes from comparing the product law with
that average. Write $\mathrm{Coll}(K,s,j)$ for the collision probability
modulo $2^j$ of a product of $s$ independent uniform odd divisors of
$K!$. L53 proves that if, for every $J_0\le j\le k$,

$$
\mathrm{Coll}(K,s,j)\le2^{-(1/2+\eta)j},                      \tag{9}
$$

with $K\le CkL(k)^A$ and $s,J_0,\eta^{-1}\le CL(k)^A$, then (1) holds with
$a=2A$, $b=A$ and $d=2A+1$, and $h(n!)=O((\log n)^{5A+4})$. The
construction uses products of $2s$ divisors, $\lceil2/\eta\rceil$
additive copies and a binary reserve of $J_0$ digits. It needs one
explicit law and no universal mixing statement. It supplies the coverage
that (7) would give, for a product law in place of a uniform set law.

Estimate (9) is the missing step. Three findings bound the test.

**Nonconcentration does not give (9).** L53 also exhibits the powers
$3^i$, $0\le i<2^{\lceil gJ\rceil}$. For $g\le1/3$ they satisfy the
hypothesis of `WeightedDyadicMixing` at every level up to $J$, yet every
product of $s$ of them lies on at most $s2^{\lceil gJ\rceil}$ residues.
Bound (8) then needs exponentially many factors. The polynomial universal
statement that L66 assumes cannot be obtained by first flattening every
multiplicative product law past the one-half collision threshold. An
argument exploiting additive structure, as the source does,
remains possible; no polynomial version is proved here.

**The pairing bound of L66 cannot reach (9).** Its cells consist of
products of a set $P$ of primes with $\prod_{p\in P}p<2^j$, so it never
certifies a residue mass below $2^{-|P|}$, and $|P|=O(j/\log j)$. The
argument uses only that distinct integers below $2^j$ stay distinct
modulo $2^j$. The collision bound it yields is thus never better than
$2^{-O(j/\log j)}$, while (9) needs $2^{-(1/2+\eta)j}$. These are limits
on the certified upper bound, not lower bounds on the actual collision
probability of the divisor law.

Allowing larger exponent cells does not remove the size restriction. At
the top conductor $j=k$, suppose every cell normalizes its output by a
fixed odd factor to a set of divisors of $H!$ smaller than $2^k$, with
$H\le kL(k)^C$. L64 with one digit gives at most $M_k=2^{o(k)}$ such
normalized values. The usual cell certificate bounds a residue mass by
the sum, over cells, of the cell probability times its conditional largest
atom. Each conditional largest atom is at least $1/M_k$, so this
certificate is at least $1/M_k=2^{-o(k)}$. Even this enlarged version
cannot certify (9) by first bounding the largest atom. Products of $s$
factorial divisors allow $H=sK\le kL(k)^{O(1)}$, so the same argument applies
to size-restricted cells in their law. A stronger estimate must use
information beyond separate injectivity of small positive integers, such
as the positions of different cells modulo $2^k$. No lower bound on the
true collision probability follows from this certificate limitation.

**The direct estimate is a short-range character bound.** By the identity
in the proof of L53,

$$
\mathrm{Coll}(K,s,j)=\frac1{2^{j-1}}\sum_{\chi\bmod2^j}\,
\prod_{3\le p\le K}\bigl|\phi_{e_p}(\chi(p))\bigr|^{2s},\qquad
\phi_e(\omega)=\frac1{e+1}\sum_{i=0}^{e}\omega^i,               \tag{10}
$$

with $e_p=v_p(K!)$. Thus the exact missing estimate is

$$
\sum_{\chi\bmod2^j}\prod_{3\le p\le K}
 |\phi_{e_p}(\chi(p))|^{2s}\le2^{(1/2-\eta)j-1}
 \quad(J_0\le j\le k).                                    \tag{11}
$$

It limits the weighted contribution of characters whose values on the
small primes make the factors large. At the largest conductor $q=2^k$,
the primes reach only $(\log q)(\log\log q)^{O(1)}$. Neither the
nonconcentration theorem nor the integer-injectivity estimates above
establish (11). In particular, multiplicative generation of the unit
group by small primes is not this quantitative moment bound. The bounded
test supplies no estimate for the required range; it does not assert
that every method for this arithmetic question is excluded.

For scale calibration only, replace each nonprincipal character's values
$\chi(p)$ by independent uniform points on the circle. Each factor then has
$\mathbb E|\phi_e(\chi(p))|^2=1/(e+1)$, and the expected right side of
(10) with $s=1$ would be at most $2^{1-j}+1/\tau(N_K)$, where $N_K$ is
the odd part of $K!$. For fixed $0<\eta<1/2$ and sufficiently large $j$,
this expectation is below the bound in (9) once
$\tau(N_K)>2^{(1/2+\eta)j+1}$. The model places that scale within a factor
$2$ of the support-counting requirement for $s=1$; it gives no estimate
for actual characters and no uniform control over the conductors. It is
not evidence for (9), or for (7) for the original single-divisor law.

## Stop and reopening conditions

The bounded replacement test stops without constructing (1). The block
extraction is stopped by (4) together with L66's factor-count lower
bound. The full-divisor law cannot be completed through the displayed
source decay witnesses, by (6). L53 removes the exponential conversion,
but only in exchange for estimate (9). That estimate is open. It does not
follow from nonconcentration, and the cell certificates above cannot
supply it. The generic comparison also cannot be improved under only
normalization and nonnegativity. These obstructions stop the tested
arguments; they refute neither (7), (9), nor the polynomial mixing
hypothesis. The local construction remains open.

The line reopens with any one of the following inputs.

- A proof of (9), equivalently the character moment bound (11), for products
  of polylogarithmically many odd divisors of $K!$ with
  $K=k(\log k)^{O(1)}$, at every level
  $J_0\le j\le k$. A pointwise bound suffices: if every nonprincipal
  character of conductor $2^{j'}$ has product in (10), before the power
  $2s$, at most $2^{-j'/(2s)}$, then the sum in (10) is at most
  $(j+3)/4$, and (9) holds with $\eta=1/4$ for $j\ge12$. The proof of L53
  supplies the conductor count. This pointwise condition is stronger than
  the moment bound, not equivalent to it.
- A universal mixing theorem with the polynomial parameters of L66,
  including its starting scale. L53 excludes proving it by universally
  flattening the multiplicative product law below collision $2^{-j/2}$.
- A covering of the residues modulo $2^k$ that does not pass through
  Fourier decay of factorial-divisor laws, still with factorial index
  $k(\log k)^{O(1)}$, polylogarithmic length and polylogarithmic height
  exponent.

Renaming an unproved estimate as a distribution hypothesis is not
progress on the construction. A proof meeting (1) would complete an
argument for part (c) and require scrutiny of the whole conclusion and the
distinct-divisor convention before any solution claim.
