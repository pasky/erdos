---
name: research/erdos_699/methods/details/small_index_discriminant
title: "Erdős 699: an effective discriminant bound for selected maximal positions"
desc: "The exact orbit discriminant gives a weighted S-part inequality, and an effective cutoff for additional patterns of small-prime maximal positions. It does not give a cutoff for every remaining index."
created: 2026-09-22T02:16:24Z
updated: 2026-09-22T19:12:28Z
---

# Erdős 699: an effective discriminant bound for selected maximal positions

[[research/erdos_699/_index|P699 research]] ·
[[research/erdos_699/archive/previous_bounds/effectivity|The effectivity question]] ·
[[research/erdos_699/proofs/details/cutoff_and_cubic|The symmetric discriminant]]

***

The discriminant supplies an effective bound for some patterns of
small-prime maximal positions, including patterns not excluded by counting
the positions alone. This is a refinement of the existing inequalities;
it does not make every remaining index effective.

Fix an admissible bad triple $(n,i,j)$, put $c=n-j$, and write

$$\binom ni=UV,\qquad S=\{p:p<i\},\qquad
b=\frac{i(i-1)}2,\qquad w_t=2i-2-t.$$

For each $p\in S$, choose $r_p\in\{0,\ldots,i-1\}$ maximizing
$a_p=v_p(n-r_p)$, and set

$$T=\{r_p:p\in S\},\qquad
M_t=\prod_{p:r_p=t}p^{a_p},\qquad
W(T)=\sum_{t\in T}(2i-2-t).\tag{1}$$

Thus $M_t\mid n-t$ and $M_t\le n$. Define

$$\kappa_i=\begin{cases}1,&i\text{ composite},\\i^i,&i\text{ prime},\end{cases}
\qquad
C_i=\frac{\kappa_i\bigl(2(i-1)!\bigr)^{2i-2}}{4^b}.\tag{2}$$

**Proposition.** If $n\ge i(i-1)$, then

$$
n^b\le C_i\prod_{t\in T}M_t^{w_t}.\tag{3}
$$

In particular, if $W(T)<b$, then the explicit bound

$$
n\le C_i^{1/(b-W(T))}\tag{4}
$$

holds. If $|T|\ge2$ and $W(T)=b$, an effective row bound still exists,
by the effective $S$-part theorem. Its constants have not been evaluated
here.

## Proof of the weighted inequality

The orbit polynomial

$$
R(z)=\sum_{r=0}^i\binom j{i-r}\binom cr z^r
$$

has every coefficient divisible by $V$, so $P=R/V$ is an integer
polynomial with nonzero discriminant. The retained symmetric formula is

$$|\operatorname{Disc}R|=
\frac{K_i}{(i!)^{2i-2}}
\prod_{t=0}^{i-1}\bigl((j-t)(c-t)\bigr)^{i-1-t}
\prod_{t=0}^{i-1}(n-t)^t,\qquad
K_i=\prod_{r=1}^i r^r.\tag{5}$$

Let $[x]_S$ denote the $S$-part of a positive integer. Since $V$ is
coprime to every prime in $S$, formula (5) gives

$$|\operatorname{Disc}P|\ge
\frac{[K_i]_S}{[i!]_S^{2i-2}}
\prod_{t=0}^{i-1}[n-t]_S^t.\tag{6}$$

This remains valid when the displayed lower bound is not an integer:
the valuation inequality holds at every $p\in S$, while the nonzero
integer discriminant has nonnegative valuations at all other primes.

Put $\gamma=1-i(i-1)/(2n)$. The bounds

$$\binom ni\ge\frac{\gamma n^i}{i!},\qquad
|\operatorname{Disc}R|\le
\frac{K_i n^{3b}}{(i!)^{2i-2}4^b}$$

give

$$|\operatorname{Disc}P|\le
\frac{K_iU^{2i-2}}{4^b\gamma^{2i-2}n^b}.\tag{7}$$

Combining (6) and (7), and using
$U=[\prod_{t=0}^{i-1}(n-t)]_S/[i!]_S$, yields the direct weighted
$S$-part inequality

$$4^b\gamma^{2i-2}n^b
\le\kappa_i
\left[\prod_{t=0}^{i-1}(n-t)^{2i-2-t}\right]_S.\tag{8}$$

Here $K_i/[K_i]_S=\kappa_i$, since every prime factor of $K_i$ is at
most $i$.

For $r\ne r_p$, maximality and the ultrametric inequality give
$v_p(n-r)\le v_p(r-r_p)$. Consequently

$$\begin{aligned}
v_p\!\left(\prod_{r=0}^{i-1}(n-r)^{w_r}\right)
&\le w_{r_p}a_p+
\sum_{r\ne r_p}w_rv_p(|r-r_p|)\\
&\le w_{r_p}a_p+(2i-2)v_p((i-1)!).
\end{aligned}$$

It follows that the $S$-part in (8) is at most

$$
((i-1)!)^{2i-2}\prod_{t\in T}M_t^{w_t}.
$$

Finally $n\ge i(i-1)$ gives $\gamma\ge1/2$, proving (3).

For the equality case, use

$$\prod_{t\in T}M_t^{w_t}
\le[g_T(n)]_S,\qquad
g_T(X)=\prod_{t\in T}(X-t)^{w_t}.$$

The polynomial $g_T$ has at least two distinct roots and degree $W(T)$.
Bugeaud--Evertse--Győry's effective Theorem 2.2, in the form already used
in the effectivity note, gives effectively computable $A_T,\epsilon_T>0$
with $[g_T(n)]_S\le A_Tn^{W(T)-\epsilon_T}$. This proves an effective
cutoff when $W(T)=b$ as well.

## What the criterion adds

The positions nearer $i-1$ have smaller weights. For example, at $i=27$
the earlier count bound only handles at most eight distinct maximal
positions. This discriminant criterion also handles every nine-position
set satisfying

$$
\sum_{t\in T}t\ge117,
$$

because $9\cdot52-27\cdot26/2=117$. Equality uses the effective
$S$-part theorem; a strict inequality gives (4).

For the other two nearby indices whose old exponent deficit is about
$1/3$, the analogous sufficient conditions are

$$\begin{array}{c|c|c}
i&|T|&\text{sufficient condition}\\\hline
30&10&\sum_{t\in T}t\ge145\\
33&11&\sum_{t\in T}t\ge176.
\end{array}$$

These thresholds are restrictions on finite sets of positions, not a
search over rows. Patterns with smaller sums remain to be handled by
other arguments. Replacing the integer-discriminant bound by a fixed
lower bound for totally real field discriminants can change constants,
but by itself does not improve the exponent in (8).
