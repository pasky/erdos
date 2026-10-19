# Frozen mathematical extraction

[cut]

## Target and conventions

The target is
Problem955:
for $s(n)=\sigma(n)-n$, does every set $A\subseteq\mathbb N$ of natural
density zero have a preimage $s^{-1}(A)$ of natural density zero? [cut]
Here inputs are positive integers, and $s(1)=0$.

For $x\ge1$ and $m\ge0$ write $r_x(m)=\#\{n\le x:s(n)=m\}$. For a set $S$ of
admitted inputs, which may depend on $x$, write $r_{S,x}(m)$ for the number
of $n\in S\cap[1,x]$ with $s(n)=m$, $R_S(x)=\#(S\cap[1,x])$, and

$$
C_S(x)=\sum_m r_{S,x}(m)^2
=\#\{(n,n')\in(S\cap[1,x])^2:\ s(n)=s(n')\}.
$$

Pairs are ordered and the diagonal $n=n'$ is included. So $C_S(x)-R_S(x)$
counts the ordered pairs of distinct inputs with equal values, and
$(C_S(x)-R_S(x))/2$ the unordered ones.

The route recorded here is the second-moment route: if few pairs collide,
Cauchy–Schwarz bounds the number of inputs that any sparse target can
capture. The sections below show which form of that route is false, which
form is exactly as strong as the problem, and what an exact computation
shows about each.

## The density-zero form is false

The proposed form removes a density-zero set of degenerate inputs, such as
the semiprimes with $s(pq)=p+q+1$ for distinct primes $p,q$, and asks for
$C_S(x)=O(x)$ for the rest.
No density-zero exclusion can give this.

**Theorem A.** Let $E_x\subseteq[1,x]$ satisfy $|E_x|=o(x)$ and put
$S_x=[1,x]\setminus E_x$. Then $C_{S_x}(x)/x\to\infty$.

*Proof.* Fix $\delta\in(0,1/10]$ and put $z=1/\delta$ and $Z=100z$. Let
$\mathcal R_Z$ be the set of positive integers with no prime factor at most
$Z$ (so $1\in\mathcal R_Z$), let $m_Z=\prod_{q\le Z}(1-1/q)$, and let
$f(k)=\sum_{q\mid k}1/(q-1)$, summed over the primes $q$ dividing $k$.

*A class with small $s(n)/n$.* Let $V_\delta$ be the set of $n=pk$ with $p$
prime, $z/1.8<p\le z/1.1$, $k\in\mathcal R_Z$ and $f(k)\le\delta/10$. Since
$p<Z$, $p\nmid k$, so $\sigma(n)/n=(1+1/p)\,\sigma(k)/k$ and

$$
1\le\frac{\sigma(k)}{k}\le\prod_{q\mid k}\Bigl(1-\frac1q\Bigr)^{-1}
\le e^{f(k)}\le1+0.11\,\delta,
$$

so $\delta\le1/p\le s(n)/n\le(1+1.8\delta)(1+0.11\delta)-1\le2\delta$. The
pair $(p,k)$ is determined by $n$, since $p$ is the only prime factor of $n$
at most $Z$.

*Its size.* $\mathcal R_Z$ is a union of residue classes modulo
$\prod_{q\le Z}q$, so $\#(\mathcal R_Z\cap[1,y])=m_Zy+O_Z(1)$. For a prime
$q>Z$, the members of $\mathcal R_Z$ divisible by $q$ are exactly the $qk'$
with $k'\in\mathcal R_Z$. Hence

$$
\sum_{\substack{k\le y\\ k\in\mathcal R_Z}}f(k)
=\sum_{Z<q\le y}\frac{\#(\mathcal R_Z\cap[1,y/q])}{q-1}
\le m_Zy\sum_{m>Z}\frac1{m(m-1)}+O_Z(\log\log y)
\le\frac{1.01\,m_Zy}{Z}+O_Z(\log\log y),
$$

using $\sum_{m>Z}1/(m(m-1))=1/\lfloor Z\rfloor$ and $Z\ge1000$. By Markov's
inequality at most $(10/\delta)\,1.01\,m_Zy/Z+o(y)\le0.11\,m_Zy+o(y)$
members of $\mathcal R_Z\cap[1,y]$ have $f(k)>\delta/10$. Summing over the
finitely many $p$,

$$
\#(V_\delta\cap[1,x])\ge(d_\delta-o(1))\,x,\qquad
d_\delta=0.89\,m_Z\sum_{z/1.8<p\le z/1.1}\frac1p.
$$

As $\delta\to0$, Mertens' product theorem gives
$m_Z\sim e^{-\gamma}/\log(1/\delta)$ and the prime number theorem gives
$\sum_{z/1.8<p\le z/1.1}1/p\sim\log(18/11)/\log(1/\delta)$. Since
$0.89\,e^{-\gamma}\log(18/11)>0.24$, every sufficiently small $\delta$ has
$d_\delta\ge0.2/\log^2(1/\delta)$. The convergence is slow, because
$\log Z=\log(1/\delta)+\log100$; the bound is asymptotic and is not claimed
for every $\delta\le1/10$.

*Pigeonhole.* The set $N_x=(V_\delta\cap[1,x])\setminus E_x$ has at least
$(d_\delta-o(1))x$ members, and their values $s(n)$ lie in $[1,2\delta x]$.
By Cauchy–Schwarz over those values,

$$
C_{S_x}(x)\ge\sum_{m\le2\delta x}r_{N_x,x}(m)^2\ge\frac{|N_x|^2}{2\delta x}
\ge\frac{(d_\delta-o(1))^2}{2\delta}\,x .
$$

So $\liminf_x C_{S_x}(x)/x\ge d_\delta^2/(2\delta)\ge
0.02/(\delta\log^4(1/\delta))$ for every small $\delta$, which is unbounded
as $\delta\to0$. $\square$

The mechanism is general: the inputs of $V_\delta$, whose least prime factor
is near $1/\delta$ and whose other prime factors are large, have their values
in $[1,2\delta x]$ although they range over $[1,x]$, and they form a
proportion of order $1/\log^2(1/\delta)$ of all inputs. The degenerate
families that an exclusion is meant to remove, such as the semiprimes, are
only the extreme case. The same argument with $|E_x|\le\varepsilon x$ gives

$$
\liminf_{x\to\infty}\frac{C_{S_x}(x)}{x}
\ge\sup_{\delta:\ d_\delta>\varepsilon}\frac{(d_\delta-\varepsilon)^2}{2\delta},
$$

and taking $\delta=\exp(-\sqrt{0.1/\varepsilon})$, where
$d_\delta\ge2\varepsilon$ for small $\varepsilon$, shows that the right side
is at least $(\varepsilon^2/2)\exp(\sqrt{0.1/\varepsilon})$. Any constant $K$ in
the corrected form below must therefore grow faster than every power of
$1/\varepsilon$.

[cut] It uses
only the prime number theorem and Mertens' product theorem.

## An equivalent form of the problem

The second-moment route loses nothing in principle once the exceptional set
may have small positive density and the constant may depend on it.

**Theorem B.** The following are equivalent.

1. Every $A\subseteq\mathbb N$ of natural density zero has $s^{-1}(A)$ of
   natural density zero.
2. The fiber sizes are tight:
   $\lim_{T\to\infty}\limsup_{x\to\infty}x^{-1}\#\{n\le x:r_x(s(n))>T\}=0$.
3. For every $\varepsilon>0$ there are $K$ and $x_0$ such that every
   $x\ge x_0$ has a set $E_x\subseteq[1,x]$ with $|E_x|\le\varepsilon x$ and
   $C_{[1,x]\setminus E_x}(x)\le Kx$.
4. For every $\varepsilon>0$ there are $\eta>0$ and $x_0$ such that
   $\#\{n\le x:s(n)\in B\}\le\varepsilon x$ for every $x\ge x_0$ and every
   set $B\subseteq\mathbb N\cup\{0\}$ of at most $\eta x$ integers.

*Proof.* (2 ⇒ 3) Given $\varepsilon$, choose $T$ and $x_0$ with
$\#\{n\le x:r_x(s(n))>T\}\le\varepsilon x$ for $x\ge x_0$, and let $E_x$ be
that set. Every value taken on $[1,x]\setminus E_x$ is taken at most $T$
times there, so
$C_{[1,x]\setminus E_x}(x)\le T\,R_{[1,x]\setminus E_x}(x)\le Tx$.

(3 ⇒ 1) Let $A$ have density zero, and fix $\varepsilon>0$ and $L\ge1$. For
$x\ge x_0$ the inputs $n\le x$ with $s(n)\in A$ are of three kinds. At most
$\varepsilon x$ lie in $E_x$. Those with $s(n)>Lx$ have
$\sigma(n)/n>L+1$, and

$$
\sum_{n\le x}\frac{\sigma(n)}n=\sum_{d\le x}\frac1d\Bigl\lfloor\frac xd
\Bigr\rfloor\le\zeta(2)\,x
$$

bounds their number by $2x/L$. The rest have values in $A\cap[0,Lx]$, and
Cauchy–Schwarz bounds them by $(|A\cap[0,Lx]|\cdot Kx)^{1/2}=o(x)$. So the
upper density of $s^{-1}(A)$ is at most $\varepsilon+2/L$ for all
$\varepsilon$ and $L$.

(1 ⇒ 2) Suppose (2) fails. The quantity in (2) is nonincreasing in $T$, so
there is $\eta>0$ such that for every $T$ arbitrarily large $x$ have
$\#\{n\le x:r_x(s(n))>T\}>\eta x$. Write $m_w=\prod_{p\le w}(1-1/p)$ and fix
$L\ge4$ with $L^{-1/2}+m_{\sqrt L}\le\eta/4$. An input $n\in(x/\sqrt L,x]$
with $s(n)<x/L$ has $\sigma(n)/n<1+L^{-1/2}$, hence no prime factor at most
$\sqrt L$; so $\#\{n\le x:s(n)<x/L\}\le(\eta/4)x+O_L(1)$. Put $x_0=1$ and
choose inductively $x_k$ with $\#\{n\le x_k:r_{x_k}(s(n))>k\}>\eta x_k$,
$x_k\ge k^2L\,x_{k-1}$ and $O_L(1)\le\eta x_k/4$, and let

$$
A_k=\{m\ge x_k/L:\ r_{x_k}(m)>k\},\qquad A=\bigcup_kA_k .
$$

Then $\#\{n\le x_k:s(n)\in A\}\ge\eta x_k-(\eta/2)x_k$, so $s^{-1}(A)$ has
upper density at least $\eta/2$. On the other hand
$|A_k|<x_k/k$, because $\sum_mr_{x_k}(m)\le x_k$, so
$\sum_{j<k}|A_j|<\sum_{j<k}x_j\le k\,x_{k-1}$. If $k$ is the largest index
with $x_k/L\le y$, then $A\cap[1,y]\subseteq A_1\cup\dots\cup A_k$ and

$$
\frac{|A\cap[1,y]|}{y}\le\frac{L}{x_k}\Bigl(\frac{x_k}{k}+k\,x_{k-1}\Bigr)
\le\frac{L}{k}+\frac1k ,
$$

so $A$ has density zero and (1) fails.

(2 ⇔ 4) If (2) holds, choose $T$ with $\#\{n\le x:r_x(s(n))>T\}\le\varepsilon
x/2$ for large $x$ and put $\eta=\varepsilon/(2T)$: a set $B$ of at most
$\eta x$ values captures at most $\varepsilon x/2$ inputs in fibers larger
than $T$ and at most $T\eta x$ others. If (4) holds, take $T=1/\eta$; the set
$B=\{m:r_x(m)>T\}$ has fewer than $x/T=\eta x$ members, so it captures at
most $\varepsilon x$ inputs. The quantity in (2) is therefore at most
$\varepsilon$ for every $T\ge1/\eta$, and $\varepsilon$ is arbitrary.
$\square$

[cut] Statement 4
places the problem beside
[[../library/arithmetic_functions/pollack_2018_divisor_sum_fibers/theorem_1_2|Pollack, Pomerance and Thompson's Theorem 1.2, which proves the same uniform control for targets of total size at most $x^{1/2+\epsilon(x)}$]]:
the problem asks for it at size $\eta x$, with $\varepsilon\to0$ as
$\eta\to0$. The problem page's countermodel shows that control at the smaller
size cannot be extended by an abstract argument; Theorem B says that control
at linear size is exactly what is needed.

Statement 3 is the corrected form of the route. Its natural explicit version
uses the sets

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
$E_x=[1,x]\setminus D(\delta)$, and hence the problem. It is not known to be
equivalent. The class $V_\delta$ of Theorem A, apart from its finitely many
primes, lies in $D(\delta)$, so the pigeonhole step gives
$K_\delta\ge0.02/(\delta\log^4(1/\delta))$ for small $\delta$, and
$K_\delta\to\infty$. The semiprimes in $D(\delta)$ are harmless. For
distinct primes $p<q$, $s(pq)=p+q+1\ge\delta pq$ forces $p\le3/\delta$, and
$s(p^2)=p+1$ comes from one prime square at most; so each value is taken by
at most $\pi(3/\delta)+1$ semiprimes in $D(\delta)$, and they contribute at
most $(\pi(3/\delta)+1)x$ to the sum of squares, which
$(r_1+r_2)^2\le2r_1^2+2r_2^2$ separates from the rest.


[cut]
