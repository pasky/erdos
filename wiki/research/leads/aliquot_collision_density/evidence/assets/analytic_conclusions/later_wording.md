# Separately frozen later author wording

This is supplied solely to judge applicability of the older report. It is outside the originally examined subject; no inherited warrant is asserted.

[cut]

$$
D(\delta)=\{n\ \text{composite}:\ s(n)\ge\delta n\}.
$$

An input outside $D(\delta)$ is $1$, a prime, or has no prime factor at most
$1/\delta$, so the complement of $D(\delta)$ has upper density at most
$\prod_{p\le1/\delta}(1-1/p)\to0$. The bound

$$
\text{(D)}\qquad C_{D(\delta)}(x)\le K_\delta\,x\quad\text{for every fixed
}\delta>0\text{ and all large }x
$$

therefore implies statement 3, by choosing $\delta$ with
$\prod_{p\le1/\delta}(1-1/p)<\varepsilon$ and
$E_x=[1,x]\setminus D(\delta)$, and hence the problem. The argument does not establish the converse. The class $V_\delta$ of Theorem A, apart from its finitely many
primes, lies in $D(\delta)$, so the pigeonhole step gives
$K_\delta\ge0.02/(\delta\log^4(1/\delta))$ for small $\delta$, and
$K_\delta\to\infty$. The semiprimes in $D(\delta)$ are harmless. For
distinct primes $p<q$, $s(pq)=p+q+1\ge\delta pq$ forces $p\le3/\delta$, and
$s(p^2)=p+1$ comes from one prime square at most; so each value is taken by
at most $\pi(3/\delta)+1$ semiprimes in $D(\delta)$, and they contribute at
most $(\pi(3/\delta)+1)x$ to the sum of squares, which
$(r_1+r_2)^2\le2r_1^2+2r_2^2$ separates from the rest.


[cut]
