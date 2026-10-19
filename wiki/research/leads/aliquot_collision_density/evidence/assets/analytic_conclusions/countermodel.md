[cut]

## Exact scope of the arithmetic reduction

The uniform finite-target theorem in
[[../library/arithmetic_functions/pollack_2018_divisor_sum_fibers/_index|Pollack–Pomerance–Thompson,
Theorem 1.2]] applies when the target cardinality is at most
$x^{1/2+\epsilon(x)}$, with $\epsilon(x)\to0$. Splitting an arbitrary
density-zero target into many such pieces multiplies an uncontrolled $o(x)$
error and does not prove the desired extension.

A complete abstract countermodel shows the missing implication. Let
$A=\{\lfloor j^{3/2}\rfloor:j\ge1\}$, and let $T(n)$ be its largest member at
most $n$. Consecutive members near $x$ are separated by $O(x^{1/3})$, so every
fiber restricted to $[1,x]$ has size at most $Cx^{1/3}$. Uniformly over sets
$B$ of size at most $x^{1/2+\epsilon(x)}$,

$$
\#\{n\le x:T(n)\in B\}\le Cx^{5/6+\epsilon(x)}=o(x).
$$

Nevertheless $A(x)=O(x^{2/3})$, $T(n)\sim n$, and $T^{-1}(A)=\mathbb N$. Thus
even uniform small-target control and linear output size do not imply
preservation of every density-zero set. This [cut] countermodel
concerns a general inference, not the arithmetic function $s$. [cut]
