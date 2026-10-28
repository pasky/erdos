---
name: theory/number_theory/L63_polylogarithmic_dyadic_representatives/_proof
title: Proof of the dyadic representative criterion
desc: |
  Positive modular lifting, removal of repeated divisors, and a factorial
  radix chain with every index, count, and height cost retained.
created: 2026-10-14T08:41:00Z
updated: 2026-10-23T18:31:25Z
---

***

We prove [[theory/number_theory/L63_polylogarithmic_dyadic_representatives/_index|L63]].
All constants below may depend on the fixed constants and starting threshold
in its hypothesis. Write $L(t)=1+\log_2(t+1)$.

## Elementary operations

If $v$ divides $F!$ and $w$ divides $G!$, then $vw$ divides $(F+G)!$,
because $F!G!$ divides $(F+G)!$. Also

$$
2^kF!\mid(F+2k)!.
$$

Indeed, $2^k\mid(2k)!$ and $F!(2k)!\mid(F+2k)!$. We may therefore enlarge
each index in the hypothesis from $F$ to $F+2k$, retaining its stated order
and ensuring $2^k\mid F!$.

A multiset of at most $U$ divisors of $H!$ can be replaced by at most $U$
distinct divisors of $(H+2U)!$ with the same sum. Repeatedly replace two equal
terms $v,v$ by $2v$. Each replacement reduces the number of terms, so fewer
than $U$ replacements occur. Every resulting term divides $2^U H!$, and that
integer divides $(H+2U)!$. Positivity and the sum are preserved.

The factorial radix step has the following exact form. Put $Q=n!/m!$, where
$m\le n$. If each integer $0\le r<Q$ is a sum of at most $u$ distinct
divisors of $n!$, then

$$
h(n!)\le h(m!)+u.                                      \tag{1}
$$

Write $R=Qz+r$ for $0\le R\le n!$. Then $z\le m!$. Multiply a
representation of $z$ by distinct divisors of $m!$ by $Q$, and add the
prescribed representation of $r$. The first group's positive terms are at
least $Q$ and the second group's are at most $r<Q$, so the groups are
disjoint. Each term divides $n!$. Factorials are practical: induct on $n$
using this same construction with $m=n-1$, $Q=n$, and the one-term
representation of $1\le r<n$, since each such $r$ divides $n!$. Including the
endpoint $n!$ in the definition of $h$ does not change it for $n\ge2$,
because that endpoint has a one-term representation.

These operations also occur as `factorial_binary_reserve`,
`factorial_multiset_to_distinct` and `factorial_radix_recurrence` in the
[Conjectures.io source for part (b)](../../../../library/divisors/jenw1n_2026_lean_proof_erdos_problem_18b/_index.md).
The arguments above supply the operations used here without a new Lean run.

## Lift one integer

For a sufficiently large integer $R$, let $t=\log_2R$ and choose

$$
k=\left\lfloor\frac{t}{2(C+1)L(t)^d}\right\rfloor.
$$

Increase the fixed starting threshold so that $k$ is in the hypothesis's
range, $k\ge1$, and $k\ge t/(4(C+1)L(t)^d)$. Since $k\le t$,

$$
k(D+1)\le (C+1)kL(t)^d\le t/2<t.
$$

Choose a representative $S$ of $R$ modulo $2^k$. The height condition gives
$0\le S\le2^{kD}<R$. Hence

$$
R=S+2^kT,\qquad 1\le T\le R/2^k,
\qquad \log_2 T\le t-k.                              \tag{2}
$$

Apply the same operation to $T$ until the integer is below the fixed
threshold. That final integer is a single divisor of a fixed factorial.
If the successive choices are $k_i$, then (2) gives
$\sum_i k_i\le t$. The sum of the enlarged factorial indices is therefore

$$
H\ll 1+\sum_i k_iL(k_i)^a\ll 1+tL(t)^a.               \tag{3}
$$

To justify addition of indices, if the current representative uses divisors
of $F!$ and the recursive representation uses divisors of $G!$, each
recursive term multiplied by $2^k$ divides $F!G!$, since $2^k\mid F!$.
Both groups thus lie in $(F+G)!$. Repetitions are allowed at this stage.

While the current logarithm lies in $[z/2,z]$, each step decreases it by at
least $c z/L(z)^d$ for a fixed $c>0$. There are $O(L(z)^d)$ such steps.
Summing over the $O(L(t))$ dyadic intervals down to the fixed threshold
gives $O(L(t)^{d+1})$ steps. Each uses at most $O(L(t)^b)$ terms, so their
total is

$$
U\ll L(t)^{b+d+1}.                                    \tag{4}
$$

Remove repetitions using the elementary operation above. The final index is
$H+2U=O(tL(t)^a)$: for fixed exponents, $L(t)^{b+d+1}=o(t)$.
Equivalently, given a bit bound $t$, every integer $0\le R<2^t$ has an exact
representation by
$O(L(t)^{b+d+1})$ distinct divisors of a factorial with index
$O(tL(t)^a)$. The bounded integers and $R=0$ are absorbed by a fixed index
and the empty sum. The constants can be chosen uniformly for all $R<2^t$.

## Chain the factorial radix steps

Choose a sufficiently large constant $K$ and, for large $n$, set

$$
\Delta=\left\lfloor\frac{n}{K L(n)^{a+1}}\right\rfloor,
\qquad m=n-\Delta,\qquad Q=n!/m!.
$$

Then $\log_2Q\le\Delta\log_2n$, and (3), including the distinctness cost,
puts every residue $0\le r<Q$ in a factorial of index at most $n$ when
$K$ is large enough. Equation (4) bounds its length by
$O(L(n)^{b+d+1})$. Equation (1) applies.

On a dyadic interval of indices $[N/2,N]$, the decrease $\Delta$ is at
least $c'N/L(N)^{a+1}$ for all sufficiently large $N$. Thus halving the
index costs $O(L(N)^{a+1})$ radix steps. Down to a fixed index there are
$O(L(n)^{a+2})$ steps in total. Charging each its uniform
$O(L(n)^{b+d+1})$ cost gives

$$
h(n!)=O\bigl(L(n)^{a+b+d+3}\bigr),
$$

as required. The representatives required by the hypothesis have not been
constructed by this argument.

## A sufficient exponential-sum input

Here is one precise way to supply the local representatives, without
separated digits. Let $X$ be a nonempty set of odd divisors of $F!$, and
let $\mu$ be its uniform law modulo $2^k$. Suppose, for some
$\eta>0$ and integer $2\le E\le k$, that

$$
\left|\frac1{|X|}\sum_{z\in X}
 e^{2\pi i az/2^j}\right|
 \le 2^{-\eta\min(j,E)}
 \quad(2\le j\le k,\ a\text{ odd}).                  \tag{5}
$$

Choose an integer $q$ with $\eta q\ge2$ and $\eta qE\ge k+2$, and
convolve $q$ copies of $\mu$ with the uniform law on $\{0,1\}$. The
last factor kills the character of order two exactly. There are $2^{j-1}$
characters of exact order $2^j$. The sum of the absolute values of all
remaining nontrivial Fourier coefficients is at most

$$
\sum_{j=2}^k 2^{j-1}2^{-\eta q\min(j,E)}
\le\sum_{j=2}^E2^{-j-1}+2^k2^{-\eta qE}
\le\tfrac12<1.
$$

Fourier inversion makes the convolution positive at every residue. Each
residue thus has a nonnegative representative that is a sum of at most
$q+1$ divisors of $F!$, with repetition allowed, and is at most $qF!+1$.
If $F\le CkL(k)^a$, $1/\eta$ and $k/E$ are bounded by fixed powers of
$L(k)$, then $q$ can be chosen polylogarithmic in $k$, and
$\log_2(qF!+1)=O(kL(k)^{a+1})$. These are precisely allowed count and
height bounds in L63.

No estimate (5) with these parameters is proved here. The calculation is a
sufficient input specification; it does not identify additive cancellation
with a multiplicative-character generation condition.
