Supporting convention from wiki/problems/irrationality/E0251/_index.md, Statement:

“Here $p_n$ is the $n$th prime.” The index begins at $p_1=2$.

[cut]

***

[cut]

It gives
an alternative precise missing input for
[[problems/irrationality/E0251/_index|Problem 251]], not an estimate for primes.

Use the same indexing:

$$
S=\sum_{n\ge1}\frac{p_n}{2^n},\qquad
g_n=p_{n+1}-p_n,\qquad
G_n=\sum_{j\ge0}\frac{g_{n+j}}{2^{j+1}}.
$$

The convergent sums satisfy $S=2+G_1$ and $G_{n+1}=2G_n-g_n$.
Suppose $S=a/(2^sd)$ in lowest terms, where $s\ge0$ and $d\ge1$ is odd.
Then $dG_n$ is an integer for $n\ge s+1$. Since $g_n$ is even for $n\ge2$,
the recurrence also gives

$$
G_n\in\frac2d\mathbb Z
\qquad\bigl(n\ge\max(s+2,3)\bigr).
\tag{1}
$$

Indeed $dG_{n+1}=2dG_n-dg_n$ is even once $dG_n$ is integral and $n\ge2$.

## A repeated-window constraint

Let $m>n\ge\max(s+2,3)$ and $K\ge1$. Suppose

$$
g_{n+j}=g_{m+j}\qquad(0\le j<K).
\tag{2}
$$

If

$$
|G_{n+K}-G_{m+K}|<\frac{2^{K+1}}d,
\tag{3}
$$

then $G_n=G_m$ and $G_{n+K}=G_{m+K}$. When $d>1$, this also implies

$$
\operatorname{ord}_d(2)\mid(m-n).
\tag{4}
$$

To prove this, iterate the tail identity and cancel the equal windows:

$$
G_n-G_m=2^{-K}(G_{n+K}-G_{m+K}).
$$

By (1) the left side lies in $(2/d)\mathbb Z$, while (3) makes its absolute
value less than $2/d$. It is zero, and the displayed identity also makes the
two later tails equal. Iterating $G_{n+1}=2G_n-g_n$ from $G_1=S-2$ gives

$$
\{G_n\}=\{2^{n-1}S\}
        =\left\{\frac{2^{n-1-s}a}{d}\right\}.
$$

Equality of $G_n,G_m$, together with $\gcd(a,d)=1$ and the oddness of $d$,
therefore gives $2^{m-n}\equiv1\pmod d$, proving (4).

All tails are positive, so a sufficient condition for (3) is that both
$G_{n+K}$ and $G_{m+K}$ are less than $2^{K+1}/d$. Equivalently, if (2)
holds but (4) fails, rationality forces a separation

$$
|G_{n+K}-G_{m+K}|\ge\frac{2^{K+1}}d.
$$

## What would finish this route

For a fixed odd $d>1$, it would suffice to produce such pairs at arbitrarily
large indices with equal gap windows, small later tails, and
$\operatorname{ord}_d(2)\nmid(m-n)$. Arbitrarily large indices are needed
because the binary preperiod $s$ is unknown. This would exclude every rational
value whose reduced denominator has odd part $d$. A separate argument is
needed for $d=1$, where the congruence gives no obstruction.

No theorem supplying these pairs is proved here. Repetition of short gap
patterns alone does not bound the later tails at the needed scale, and a
count of repeated windows alone does not put them in different index classes
modulo $\operatorname{ord}_d(2)$. The
[[research/prime_binary_new_attack/critical_length_obstructions|critical-length obstructions]]
still apply: exact cancellation of the window leaves a difference of two
infinite tails, and an upper bound for it must be justified. Congruences of
the gaps are weaker than (2); replacing equality by congruence introduces a
nonzero finite-window contribution that this argument does not control.
