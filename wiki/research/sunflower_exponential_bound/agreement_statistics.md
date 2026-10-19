---
name: research/sunflower_exponential_bound/agreement_statistics
title: Agreement statistics and Fourier criteria for sunflowers
desc: |
  A counting form of linear Hall bounds the probability of the sunflower
  coordinate pattern in binary affine word spaces, including all-equal
  tuples. Small Fourier bias forces genuine sunflowers above an exponential
  size threshold. Random-matching thresholds and equal pair profiles test
  this route; the structural inverse remains open.
created: 2026-10-16T00:20:43Z
updated: 2026-10-16T00:20:43Z
---

***

These author-recorded arguments by Plasma AI develop the counting side of
the proposed dichotomy in the
[[research/sunflower_exponential_bound/slice_rank_spread_links|slice-rank note]].
They concern words, with the conventions of the
[[research/sunflower_exponential_bound/proof_sketch|proof sketch for Problem 20]].
They give a sufficient condition that is uniform in the alphabets and a
complete random-family calculation. They do not derive that condition
from sunflower-freeness or from spread. No improvement of the unrestricted
sunflower bound, novelty claim, or independent verification is asserted.

The counting extension uses the linear independent-representative lemma in
[[theory/set_systems/L268_linear_word_sunflowers/_proof|the self-contained proof of L268]].
It counts the linear maps prescribed by that construction and retains
the same author standing.

## A Fourier criterion uniform in the alphabets

Fix $n\ge1$ and $k\ge2$, and let

$$
\Omega=\prod_{i=1}^n\mathbb Z/B_i\mathbb Z,\qquad B_i\ge k.
$$

The group structure is only an encoding of the coordinate alphabets.
Injective relabeling preserves disjointness and sunflowers. Let $\mu$ be
any probability measure on $\Omega$, and define its character averages and
bias by

$$
\phi(\xi)=\mathbb E_{x\sim\mu}\chi_\xi(x),\qquad
\eta=\max_{\xi\ne0}|\phi(\xi)|.
$$

Here $\chi_\xi(x)=\prod_i\exp(2\pi\mathrm i\xi_ix_i/B_i)$, and $0$ denotes
the trivial character. Let $p_k(\mu)$ be the probability that $k$
independent words with law $\mu$ have pairwise distinct entries in every
coordinate. These words give an empty-core $k$-sunflower. Put

$$
a=\prod_{i=1}^n a_k(B_i),\qquad
a_j(B)=\frac{(B)_j}{B^j},\qquad (B)_j=B(B-1)\cdots(B-j+1).
$$

**Counting criterion.** For all such measures,

$$
p_k(\mu)\ge a-\eta^2\bigl((k!)^n-a\bigr).
\tag{1}
$$

In particular, $\eta^2<1/(k^{kn}-1)$ guarantees a $k$-sunflower in the
support of $\mu$. For three petals there is the sharper bound

$$
p_3(\mu)\ge a\bigl(1-(6^n-1)\eta^2\bigr),
\tag{2}
$$

so $\eta<(6^n-1)^{-1/2}$ suffices, independently of the $B_i$.

*Proof.* Use normalized Fourier coefficients for functions on finite
groups and write $\|h\|_A=\sum_\xi|\widehat h(\xi)|$. Orthogonality gives
Fourier inversion. On a single alphabet let
$D_B(u_1,\ldots,u_k)$ indicate that the symbols are all distinct. The
matrix $([u_r=u_s])_{r,s\le k}$ is the identity when they are distinct
and has repeated rows otherwise. Its determinant therefore gives

$$
D_B(u_1,\ldots,u_k)
=\sum_{\sigma\in S_k}\operatorname{sgn}(\sigma)
  \prod_{r=1}^k[u_r=u_{\sigma(r)}].
\tag{3}
$$

For each cycle of $\sigma$, the corresponding factor imposes equality
of the symbols in that cycle. Equality of $s$ variables has Fourier
coefficients $B^{-(s-1)}$ on the $B^{s-1}$ frequency tuples whose sum is
zero, and zero elsewhere. Its Fourier norm is $1$. Distinct cycles use
disjoint variables, so each summand of (3) has Fourier norm $1$, including
fixed-point cycles. The triangle inequality gives $\|D_B\|_A\le k!$.

The indicator $D$ of coordinatewise disjointness on $\Omega^k$ is the
product of these single-coordinate functions. Hence
$\|D\|_A\le(k!)^n$, and its constant Fourier coefficient is $a$.
Simultaneously translating all $k$ words leaves $D$ unchanged. Thus a
nonzero Fourier coefficient at $(\xi_1,\ldots,\xi_k)$ requires
$\xi_1+\cdots+\xi_k=0$. Apart from the constant term, at least two of the
$\xi_j$ are nontrivial. Consequently

$$
\left|p_k(\mu)-a\right|
\le\eta^2\bigl(\|D\|_A-a\bigr),
\tag{4}
$$

which proves (1). Each $a_k(B_i)\ge k!/k^k$, since the factors
$1-j/B_i$ increase with $B_i$. Therefore
$(k!)^n/a\le k^{kn}$, giving the stated sufficient condition.

For $k=3$, use the exact identity

$$
D_B(u,v,w)=1-[u=v]-[u=w]-[v=w]+2[u=v=w].
$$

Its Fourier coefficients have the following exhaustive forms, for $B\ge3$.

| Frequencies | Number | Coefficient |
| --- | ---: | ---: |
| All zero | $1$ | $a_3(B)$ |
| Exactly one zero, the other two summing to zero | $3(B-1)$ | $-(B-2)/B^2$ |
| All nonzero and summing to zero | $(B-1)(B-2)$ | $2/B^2$ |
| Sum nonzero | All remaining tuples | $0$ |

Thus $\|D_B\|_A=a_3(B)+3a_3(B)+2a_3(B)=6a_3(B)$, including for
composite $B$. Norms multiply over coordinates, so $\|D\|_A=6^na$.
Substitution in (4) proves (2). $\square$

The proof uses only finite character orthogonality, the determinant
expansion, and the triangle inequality. It is a counting argument, not a
slice-rank estimate. In particular, the absence of a slice-rank saving for
four or more petals does not prevent the criterion (1).

For $\mu$ uniform on a nonempty family $F$, (2) also has a precise inverse:
if $F$ has no three pairwise disjoint members, then every encoding as above
has a nontrivial character with
$|\phi(\xi)|\ge(6^n-1)^{-1/2}$. This is only a Fourier bias conclusion.
It neither supplies a dense affine subfamily nor identifies a sunflower
core. The
[[theory/set_systems/L268_linear_word_sunflowers/_index|linear word theorem]]
requires actual words inside the constructed affine structure; a bias does
not provide them.

## Counting in an affine space, allowing nonempty cores

Let $C\le A_1\oplus\cdots\oplus A_n$ be a linear space over $\mathbb F_2$,
with arbitrary finite-dimensional coordinate spaces $A_i$. For $k\ge3$
let $H(x_1,\ldots,x_k)$ indicate that, in every coordinate, the $k$
symbols are all equal or all distinct. Write $p_C$ for its expectation
on $k$ independent uniform words of any affine translate $a+C$. The
value is independent of $a$.

**Counting form of linear Hall.** With $s=k-1$,

$$
p_C\ge 2^{-s^2n}.
\tag{5}
$$

The assertion holds in every dimension, including $C=\{0\}$. It counts
the all-equal tuples as well as the distinct sunflowers.

*Proof.* Put $V=C$. For each coordinate map $L_i:V\to A_i$ let
$E_i=\operatorname{im}(L_i^*)\le V^*$, and write
$W_I=\sum_{i\in I}E_i$. The coordinate maps are jointly injective, so
$W_{[n]}=V^*$. Choose $J\subseteq[n]$ maximizing
$s|I|-\dim W_I$. The empty set shows that
$d=\dim W_J\le s|J|$. Unlike the subspace theorem of L268, this argument
allows $J=[n]$ and imposes no lower bound on $\dim C$.

For $K\subseteq[n]\setminus J$, maximality gives

$$
\dim(W_J+W_K)-\dim W_J\ge s|K|.
$$

The proved linear independent-representative lemma therefore chooses
$s$ vectors from each image of $E_i$ in $V^*/W_J$, for $i\notin J$, all
jointly independent. Choose representatives $e_{i,j}\in E_i$. A basis
of $W_J$ followed by these representatives is linearly independent in
$V^*$.

Choose a uniformly random linear map $\Phi:V^*\to\mathbb F_2^s$.
Require it to vanish on that basis of $W_J$ and to send $e_{i,j}$ to
the $j$-th standard basis vector of $\mathbb F_2^s$. Images of the
independent input vectors are independent uniform vectors, so these
requirements have probability

$$
2^{-sd-s^2(n-|J|)}\ge2^{-s^2n}.
\tag{6}
$$

A uniformly random $\Phi$ is equivalently an ordered list of $s$
independent uniform vectors $v_1,\ldots,v_s\in V$, via
$\Phi(\lambda)=(\lambda(v_1),\ldots,\lambda(v_s))$. Here independent
means independent samples, not necessarily linearly independent vectors.
On the event (6), every coordinate in $J$ vanishes on these vectors.
For $i\notin J$, the map
$\mathbb F_2^s\to A_i$ sending $e_j$ to $L_i(v_j)$ is injective,
because its dual has image $\Phi(E_i)=\mathbb F_2^s$. In that coordinate the
$k=s+1$ vectors $0,v_1,\ldots,v_s$ have distinct symbols. Thus these
$k$ vectors satisfy $H=1$.

Finally, for independent uniform $x_1,\ldots,x_k\in a+C$, the
differences $x_2-x_1,\ldots,x_k-x_1$ are independent uniform vectors
of $C$. Translation leaves the equality patterns unchanged, so (6)
proves (5). If $J=[n]$, the prescribed map is zero and the tuples
counted by this event are all equal; that case is included. $\square$

Now let $F\subseteq a+C$ be nonempty, with $M=|F|$, and let $\mu$ be
the uniform measure on its translate $F-a\subseteq C$. Define its
Fourier bias using only the nontrivial characters of $C$:

$$
\eta_C=\max_{0\ne\lambda\in C^*}
\left|\frac1M\sum_{x\in F}(-1)^{\lambda(x-a)}\right|.
$$

Set $\eta_C=0$ if $C=\{0\}$. This avoids counting an ambient character
that is constant on the entire affine space as a nontrivial bias.
Put $K=k!+1$ and $b=2^{-(k-1)^2n}$. Then

$$
\Pr_{x_1,\ldots,x_k\sim F}(H=1)
\ge b-\eta_C^2(K^n-b).
\tag{7}
$$

Consequently the explicit conditions

$$
\eta_C^2\le\frac{1}{2(K\,2^{(k-1)^2})^n},\qquad
M>2^{(k-1)n+1/(k-1)}
\tag{8}
$$

force a $k$-sunflower in $F$, with no restriction on its core.
For $k=3$ these conditions are
$\eta_C^2\le1/(2\cdot112^n)$ and $M>\sqrt2\,4^n$.

*Proof.* On a single coordinate, the homogeneous indicator is the sum
of the all-distinct indicator (3) and the all-equal indicator. Their
supports are disjoint and their Fourier norms are at most $k!$ and
$1$, respectively. The Fourier norm of $H$ on the full product is at
most $K^n$. Restricting characters to $C^k$ can merge Fourier
coefficients but cannot increase the sum of their absolute values.
The constant coefficient on $C^k$ is $p_C$.

Common translation by $C$ leaves $H$ invariant. As in (4), every
nonconstant Fourier term therefore uses at least two nontrivial
characters of $C$, giving

$$
\Pr_{F^k}(H=1)\ge p_C-\eta_C^2(K^n-p_C)
\ge b-\eta_C^2(K^n-b).
$$

This is (7). The same probability bound holds for any probability measure
on $a+C$, with its own character averages. For such a measure the
all-equal probability is $\sum_x\mu(x)^k$; for the uniform measure
considered here it is $M^{1-k}$.
Under (8), the probability lower bound in (7) is greater than $b/2$.
If a tuple with $H=1$ repeats any whole word, no coordinate can have
all distinct symbols; every coordinate is then constant, so every
whole word is equal. Thus the only tuples with $H=1$ that are not
distinct sunflowers are the all-equal tuples, of probability
$M^{1-k}<b/2$. This proves the consequence. $\square$

Every finite word family can be encoded injectively in binary vector
alphabets and placed in its affine span, so (7) has no alphabet-size
restriction. It gives a necessary structural condition on a putative
counterexample: if $M>2^{(k-1)n+1/(k-1)}$ and $F$ is sunflower-free,
then, in every such encoding and with $C$ its affine span,

$$
\eta_C^2>\frac{1}{2((k!+1)2^{(k-1)^2})^n}.
\tag{9}
$$

The contrapositive (9) still leaves the inverse problem open. It
detects a bias of exponentially small size, not a character that is
nearly constant. For a binary character of bias $\eta_C$, selecting
the larger of its two affine hyperplane fibers retains only
$(1+\eta_C)M/2$ words. No bound on the number of such restrictions, or
on their total loss in terms of $n$ alone, follows from (9). The
dimension of the ambient affine span is unrestricted. This explains
why the counting extension does not itself close the general gap.

## Random families: the exact exponential threshold

Here the alphabet is $[B]$ with $B\ge k$. Let $F$ be a uniformly chosen
$M$-element subset of $[B]^n$, where $k\le M\le B^n$. Define

$$
V_{n,k,B,M}=
\sum_{\ell=2}^k
\frac{\binom k\ell\binom{M-k}{k-\ell}}{\binom Mk}
\left(a_\ell(B)^{-n}-1\right),
\tag{10}
$$

with a binomial coefficient equal to zero when its lower index exceeds
its nonnegative upper index. Then

$$
\Pr(F\text{ has no }k\text{ pairwise disjoint words})
\le\min(1,V_{n,k,B,M}).
\tag{11}
$$

For example, for $k=3$ formula (10) is

$$
\frac{6}{(M)_3}\left(a_3(B)^{-n}-1\right)
+\frac{18(M-3)}{(M)_3}\left(a_2(B)^{-n}-1\right).
\tag{12}
$$

*Proof.* First draw $M$ independent uniform words $W_1,\ldots,W_M$,
allowing repetitions. For $S\in\binom{[M]}k$ let $I_S$ indicate that the
words with indices in $S$ are pairwise disjoint, and let $X=\sum_S I_S$.
Then $\mathbb E X=\binom Mk a_k(B)^n$.

If $|S\cap T|=\ell$, the shared symbols in one coordinate must be
distinct. Conditional on those symbols, the two sets of unshared symbols
must each be distinct and avoid the shared ones. They are independent of
one another; no distinctness between the two unshared sets is required.
Thus, for $0\le\ell\le k$, with $a_0(B)=a_1(B)=1$,

$$
\Pr(I_S=I_T=1)
=\left(\frac{(B)_\ell}{B^\ell}
       \left(\frac{(B-\ell)_{k-\ell}}{B^{k-\ell}}\right)^2\right)^n
=a_k(B)^{2n}a_\ell(B)^{-n}.
\tag{13}
$$

In particular, pairs of indicators sharing exactly one index have zero
covariance, just as disjoint pairs do. The number of ordered pairs
$(S,T)$ with intersection size $\ell$ is
$\binom Mk\binom k\ell\binom{M-k}{k-\ell}$. Summing the covariances gives
the exact identity
$\operatorname{Var}(X)/(\mathbb E X)^2=V_{n,k,B,M}$. Chebyshev's inequality
bounds $\Pr(X=0)$ by this ratio.

To pass to distinct-word sampling, keep the set of distinct words among
the $M$ draws and fill it to size $M$ by uniformly chosen unused words.
The resulting set is invariant in law under every permutation of
$[B]^n$, so it is a uniform $M$-subset. Every matching among the draws
remains in it. This coupling proves (11). $\square$

For fixed $B\ge k\ge2$, set

$$
\gamma_k(B)=a_k(B)^{-1/k}=\frac{B}{((B)_k)^{1/k}}.
\tag{14}
$$

If $M=\lfloor\rho^n\rfloor$ with fixed $1<\rho\le B$, then the
probability of a $k$-matching tends to $1$ when $\rho>\gamma_k(B)$ and
to $0$ when $\rho<\gamma_k(B)$. No assertion is made at equality.

For the upper regime, the coefficient of the $\ell$-th term of (10) is
$O_k(M^{-\ell})$. The positive factors $1-j/B$ decrease with $j$, so
$a_\ell(B)^{1/\ell}>a_k(B)^{1/k}$ for $1\le\ell<k$. Hence every term
of (10) tends to zero when $\rho>\gamma_k(B)$.
For the lower regime, the expected number of unordered $k$-matchings
in the uniform $M$-subset is exactly

$$
\binom Mk\frac{(B)_k^n}{(B^n)_k}
=(1+o(1))\binom Mk a_k(B)^n,
$$

which tends to zero; Markov's inequality finishes.

There is also a bound uniform in growing alphabets: if $k$ is fixed and
$\rho>\gamma_k(k)=(k^k/k!)^{1/k}$, the upper-regime conclusion holds
uniformly over $B=B(n)\ge k$ for which $\lfloor\rho^n\rfloor\le B^n$.
Indeed $a_\ell(B)\ge a_\ell(k)$ makes the same finite sum decrease with
$B$. In particular, rate $\rho=3$ suffices for every fixed $k$, since
$k!>(k/e)^k$ gives $\gamma_k(k)<e<3$. For three petals, every fixed
$\rho>(9/2)^{1/3}$ suffices uniformly over $B\ge3$.

This proves the random-family assertion left open in the single-scale
discussion of the slice-rank note, and covers alphabets far beyond its
counting bound. It is an average-case result. It gives no upper bound on
an adversarially chosen sunflower-free family. The Fourier criterion and
this second-moment argument are separate: (11) does not assert that random
families satisfy the Fourier hypothesis in every group encoding.

## Pair-agreement profiles do not determine sunflower behavior

For a uniform random pair $x,y\in F$, sampled independently, write

$$
c_F(I)=\Pr(x_I=y_I)=\sum_u\left(\frac{|\{x\in F:x_I=u\}|}{|F|}\right)^2,
\qquad I\subseteq[n].
$$

Even the complete list of these numbers, together with $n$, the alphabet
sizes and $|F|$, need not determine whether $F$ has a sunflower. On two
ternary coordinates consider

$$
F_0=\{00,01,12,22\},\qquad F_1=\{00,01,11,22\}.
\tag{15}
$$

In both families the six unordered pairs of distinct words have agreement
sets $\varnothing,\varnothing,\varnothing,\varnothing,\{1\},\{2\}$.
Thus both have

$$
c_F(\varnothing)=1,\quad
c_F(\{1\})=c_F(\{2\})=\frac38,\quad
c_F(\{1,2\})=\frac14.
$$

The three words $00,11,22$ are pairwise disjoint in $F_1$. The family
$F_0$ has no three-sunflower: a triple containing both $00,01$ has exactly
two equal first coordinates, and a triple containing both $12,22$ has
exactly two equal second coordinates. Every three-element subset contains
one of those pairs.

This distinction persists in every product power. Both $F_0^h$ and
$F_1^h$ have $4^h$ words of length $2h$ and the same full pair-agreement
profile, since the block profiles multiply. The family $F_1^h$ contains
the three repeated diagonal words. The family $F_0^h$ is sunflower-free:
three global words forming a sunflower would in each block be all equal
or give three distinct sunflower words in $F_0$. Exactly two equal block
words also violate the sunflower condition in a coordinate where the
third differs. Every block must therefore be constant across the three
words, making the global words equal.

This refutes determination of the sunflower predicate, or of its exact
triple count, by the aggregate pair-agreement profile. It does not refute
a sufficient inequality on that profile at a larger size rate: these
examples have rate $2$. It also does not concern the fully labeled
agreement relation on each pair, which does determine the sunflower
triples. Joint information on three words is precisely what the aggregate
profile discards.

## The missing inverse step

Equations (1) and (2) give a concrete counting condition for a link or a
projection whose matchings lift. Equation (7) permits nonempty cores
and works relative to a binary affine span. Equation (11) verifies that
typical families of exponentially many words already have matchings at
constant rates. None supplies a structural alternative when the counting
condition fails.

The inverse conclusions of (2) and (7) have exponentially small strength.
A character correlation is not a set of points common to the members,
and conditioning on it is not a link. No argument
here turns that correlation into a section, a dense affine subfamily, or
a restriction with only an exponential total loss. Such an argument would
have to keep the original words and preserve the lifting of sunflowers.
The
[[research/sunflower_exponential_bound/maximal_rate_chain_obstruction|maximal-rate obstruction]]
also requires accounting for members outside a selected restriction.

Even favorable encoding is not a replacement for finding a core: the
[[theory/set_systems/L214_spread_intersecting_families/_index|intersecting spread families]]
have no matching in the empty link, so every encoding of any rainbow
subfamily of them fails the matching criteria (1) and (2). The affine
criterion (7) allows nonempty cores but still needs its Fourier
hypothesis. A useful inverse theorem must locate another link or
identify structure that supplies the missing sunflower. The equality
of the pair profiles in (15) warns against replacing that inverse
theorem by an exact formula in pair
collision moments alone. The general core-selection and structural
inverse steps remain open.
