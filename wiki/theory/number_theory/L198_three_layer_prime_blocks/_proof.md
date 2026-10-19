---
name: theory/number_theory/L198_three_layer_prime_blocks/_proof
title: Placing a block between the outer layers
desc: The multiples of every cell prime fall in layers near multiples of q, and a block of floor(alpha P) integers fits strictly between the layers t=-1 and t=3.
created: 2026-10-15T15:58:15Z
updated: 2026-10-15T15:58:15Z
---

***

Write $d(c)=y-x$, $p_c=q+d(c)$ and $w(c)=2y-x$ for a cell $c=(x,y)$
of $S$. Since $d$ is injective on $S$, the $|S|$ primes $p_c$ are
distinct. Put $K=\lfloor\alpha P\rfloor$.

**Size of the primes.** From $|x|,|y|\le\omega$ we get $|d(c)|\le2\omega$,
so every $p_c$ and $P$ lie in $[q-2\omega,q+2\omega]$. The hypothesis
$(4-\alpha)q\ge16\omega+1$ with $4-\alpha\le1$ gives $q\ge16\omega+1$.
Since $3P$ is an integer and $3P\le\alpha P$, we have $K\ge3P$.
Hence

$$
K\ \ge\ 3q-6\omega\ \ge\ 2q+4\omega+1,
\qquad
K\ \le\ \alpha(q+2\omega)\ \le\ 4q-8\omega-1 .
$$

The first inequality uses $q\ge10\omega+1$. The second is
$(4-\alpha)q\ge(2\alpha+8)\omega+1$, which follows from the hypothesis
because $2\alpha+8<16$.

**The layers.** By the Chinese remainder theorem choose $z$ with
$z\equiv-x\pmod{p_c}$ for every $c=(x,y)$ in $S$. The multiples of
$p_c$ are then exactly the integers

$$
z+x+tp_c\;=\;z+tq+(1-t)x+ty\qquad(t\in\mathbb Z),
$$

since $x+t(y-x)=(1-t)x+ty$. Call this the layer-$t$ multiple of $c$.
With $|x|,|y|\le\omega$ its offset from $z+tq$ is at most
$(|1-t|+|t|)\omega$ in absolute value. In particular:

- layer $0$ is $z+x\in[z-\omega,z+\omega]$;
- layer $1$ is $z+q+y\in[z+q-\omega,z+q+\omega]$;
- layer $2$ is $z+2q+w(c)\in[z+2q-3\omega,z+2q+3\omega]$;
- every layer $t\le-1$ is at most $z-q+3\omega$;
- every layer $t\ge3$ is at least $z+3q-5\omega$.

For the last two, the bound at $t=-1$ is $z-q+3\omega$ and at $t=3$
it is $z+3q-5\omega$. Moving from $t$ to $t-1$ or $t+1$ changes the
position by $q$ and the offset bound by $2\omega<q$, so the bounds hold
for all $t\le-1$ and all $t\ge3$.

**The block.** Let

$$
L=\max\bigl(z-q+3\omega+1,\ z+2q+3\omega+1-K\bigr),
\qquad J=[L,\,L+K-1].
$$

We check $z-q+3\omega+1\le L\le z-\omega$ and
$z+2q+3\omega\le L+K-1\le z+3q-5\omega-1$. The two lower bounds hold by
the definition of $L$. For the two upper bounds, compare each term of the
maximum with each upper limit:
$z-q+3\omega+1\le z-\omega$ since $q\ge4\omega+1$;
$z-q+3\omega+1\le z+3q-5\omega-K$ since $K\le4q-8\omega-1$;
$z+2q+3\omega+1-K\le z-\omega$ since $K\ge2q+4\omega+1$; and
$z+2q+3\omega+1-K\le z+3q-5\omega-K$ since $q\ge8\omega+1$.

Therefore $J$ contains every layer $0$, $1$ and $2$ multiple: they lie in
$[z-\omega,z+2q+3\omega]\subseteq J$. It contains no multiple in a layer
$t\le-1$ or $t\ge3$, since those lie below $L$ or above $L+K-1$. So the
integers of $J$ divisible by some $p_c$ are exactly the three sets
$z+X$, $z+q+Y$ and $z+2q+W$.

**Counting once.** The three sets lie in the disjoint intervals
$[z-\omega,z+\omega]$, $[z+q-\omega,z+q+\omega]$ and
$[z+2q-3\omega,z+2q+3\omega]$, because $q>4\omega$. Hence $J$
contains exactly $|X|+|Y|+|W|$ integers divisible by at least one
$p_c$, each counted once; an integer of $J$ divisible by several of the
primes is a single element of one of these sets.

**Positivity.** Replacing $z$ by $z+n\prod_{c\in S}p_c$ preserves every
congruence and translates $J$ and all layers by the same amount. For $n$
large, $L\ge1$, so $J$ is a block of $K$ consecutive positive integers.
This completes the proof.
