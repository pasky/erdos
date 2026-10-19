---
name: theory/number_theory/L24_powerful_sum_bound/_proof
title: Quadratic norms and a dyadic count
desc: A field-uniform count for each pair of cube factors, followed by three complementary bounds on every dyadic box.
created: 2026-10-14T12:38:34Z
updated: 2026-10-14T12:38:34Z
---

***

Every positive powerful integer has a unique expression $a^2b^3$, with
$a\ge1$ and $b\ge1$ squarefree. At a prime with even exponent put the
whole exponent in $a^2$; at a prime with odd exponent, which is at least
three, put three in $b^3$ and the remaining even exponent in $a^2$.

Fix squarefree $b,d$ in a representation
$a^2b^3+c^2d^3=N$. Multiplying by $b^3$ gives

$$
(b^3a)^2+(bd)^3c^2=b^3N=M.
$$

Write $(bd)^3=Dq^2$ with $D$ positive squarefree. Then
$\alpha=b^3a+qc\sqrt{-D}$ is an algebraic integer of norm $M$ in
$K=\mathbb Q(\sqrt{-D})$. The map $(a,c)\mapsto\alpha$ is injective.
In the ring of integers of $K$, unique factorization of nonzero ideals
and $(\alpha)(\bar\alpha)=(M)$ show that $(\alpha)$ divides $(M)$.
If $p^e\parallel M$, the numbers of ideal divisors of the $p$-part of
$(M)$ in the split, inert and ramified cases are respectively
$(e+1)^2$, $e+1$ and $2e+1$. Each is at most $(e+1)^2$.
Thus $(M)$ has at most $\tau(M)^2$ ideal divisors, uniformly in $K$.
Generators of the same principal ideal differ by a unit; an imaginary
quadratic field has at most six units. There are therefore at most
$6\tau(M)^2$ possible pairs $(a,c)$.

For clarity, the standard divisor estimate used here is uniform in its
integer argument: for every $\eta>0$, $\tau(m)\ll_\eta m^\eta$.
Indeed, for primes $p$ with $p^\eta\ge2$, one has
$e+1\le2^e\le p^{\eta e}$. For each of the finitely many other
primes, $(e+1)p^{-\eta e}$ is bounded over $e\ge0$; multiplying those
bounds proves the assertion. Since $b^3\le N$ in any representation,
$M\le N^2$. The fixed-$(b,d)$ count is consequently $N^{o(1)}$, with
an implied bound independent of $b,d$ and $D$.

Put $a,b,c,d$ into half-open dyadic intervals with lower endpoints
$A,B,C,E$, respectively. Any box containing a solution satisfies
$A^2B^3\le N$ and $C^2E^3\le N$. Its number of solutions has each of
the bounds

$$
O(AB),\qquad O(CE),\qquad BE N^{o(1)}.
$$

The first holds because $(a,b)$ determines the other summand and its
canonical representation; the second is symmetric. The third sums the
uniform norm bound over at most $O(BE)$ core pairs. Taking the geometric
mean with weights $2/5,2/5,1/5$ bounds the minimum by

$$
(AB)^{2/5}(CE)^{2/5}(BE)^{1/5}N^{o(1)}
=(A^2B^3C^2E^3)^{1/5}N^{o(1)}
\le N^{2/5+o(1)}.
$$

There are $O((\log N)^4)$ nonempty dyadic parameter boxes. The subpower
factor absorbs this count and is uniform across the boxes, proving the
claim for every $N\ge2$ after enlarging the constant for small $N$.

This is a plus-sign argument. The real-quadratic difference equation in
Section 2.5 of
[[../library/diophantine_problems/tao_2026_products_consecutive_integers_unusual_anatomy/_index|Tao's held version 2]]
is methodological context, not an application with a coefficient's sign
silently changed. Its proof uses the same three-way dyadic interpolation;
the norm argument above supplies the needed imaginary-quadratic interface.
