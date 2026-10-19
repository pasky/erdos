---
name: research/erdos_25/harmonic_affine_completion
desc: Harmonic random-period completion converges to Haar in total variation and gives an averaged conditioned return inequality, not the unaveraged tail bound.
tags: [harmonic-measure, couplings, conditioned-tails, partial-results]
sources: []
created: 2026-09-22T13:20:00Z
updated: 2026-09-24T22:13:01Z
---


# research/erdos_25/harmonic_affine_completion

***

The following uniform coupling theorem is proved. Its application to
Problem 25 includes a return-probability weight that has not been
removed. No singleton-distinctness assertion is implicit in the theorem.

## Total-variation convergence

Write $H_N=\sum_{n\le N}1/n$, with $H_0=0$. For integers
$1\le L\le X$, define a subprobability measure $\nu_{L,X}$
on $G=\widehat{\mathbb Z}$ as follows. Give each $n\in[L,X]$
mass $1/(nH_X)$, choose
$$
 1\le r\le\lfloor n/L\rfloor
 \quad\hbox{with probability}\quad
 \frac1{rH_{\lfloor n/L\rfloor}},
$$
and then choose a Haar-uniform point in the cylinder $[n]_{Lr}$.
This preserves $n\pmod L$. Its total mass is
$$
 b_{L,X}=\frac{H_X-H_{L-1}}{H_X}.
$$
Uniformly in $L,X$,
$$
 \sup_{E\subseteq G\ {
m measurable}}
 |\nu_{L,X}(E)-b_{L,X}\mu(E)|
 \ll\frac{1+\log\log(3X/L)}{H_X}.
 \tag{1}
$$
In particular $\nu_{1,X}$ converges to Haar in total variation,
not merely against fixed continuous test functions.

Its density is
$$
 \rho_{L,X}(z)=\frac L{H_X}
  \sum_{r\le X/L}
  \sum_{\substack{Lr\le n\le X\\n\equiv z\pmod{Lr}}}
       \frac1{nH_{\lfloor n/L\rfloor}}.
 \tag{2}
$$
At fixed $r$, write the canonical residue of $z$ modulo
$Lr$ as $a\in[0,Lr)$. Every term has
$n=kLr+a$, $k\ge1$, so $n\ge kLr$ and
$H_{\lfloor n/L\rfloor}\ge H_{kr}$. Consequently, with
$T=\lfloor X/L\rfloor$,
$$
 \rho_{L,X}(z)\le\frac{D_T}{H_X},\qquad
 D_T:=\sum_{j\le T}\frac{d(j)}{jH_j}.
 \tag{3}
$$
Here $d(j)$ is the divisor-counting function. The elementary identity
$$
 \sum_{j\le t}d(j)=\sum_{a\le t}\lfloor t/a\rfloor
                  =t\log t+O(t)
$$
and partial summation give
$$
 D_T=\log T+O(1+\log\log(3T)).
 \tag{4}
$$
For detail, for $j\ge2$ replace $1/H_j$ by
$1/\log j+O(1/\log^2j)$. Partial summation with the displayed
divisor estimate makes the main sum
$\log T+O(1+\log\log(3T))$, and the error sum
$O(1+\log\log(3T))$.

Uniformly, $H_X-H_{L-1}=\log T+O(1)$. Thus (3) bounds
$\rho_{L,X}$ above by $b_{L,X}+\eta$, where
$$
 0\le\eta=\frac{D_T-H_X+H_{L-1}}{H_X}
 \ll\frac{1+\log\log(3T)}{H_X}.
$$
Nonnegativity also follows by integrating (3). The density has mean
$b_{L,X}$, so its positive and negative deviations from this mean
each have integral at most $\eta$. This proves (1). For $L=1$,
the same bound implies the relative entropy estimate
$$
 D(\nu_{1,X}\Vert\mu)
 \le\log(D_X/H_X)=O(\log\log(3X)/H_X).
$$

## An averaged conditioned return inequality

Consider any finite or countable congruence family and put
$$
 U=\bigcup_q[a_q]_q,\qquad
 D_n=\{q\le n:n\equiv a_q\pmod q\}.
$$
For a set $D$, let $M(D)$ be its set of positive multiples.
If the random completion period is divisible by a member of $D_n$,
the completed point belongs to $U$. For $L=1$, (1) therefore gives
$$
 \frac1{H_X}\sum_{n\le X}
       \frac{H_{M(D_n)}(n)}{nH_n}
 \le\mu(U)+O\!\left(\frac{\log\log(3X)}{H_X}\right).
 \tag{5}
$$

More generally, let $S$ be $L$-periodic and put
$$
 D'_{n,L}=\{q/(q,L):q\in D_n\},\qquad N_n=\lfloor n/L\rfloor.
$$
The completion preserves $S$, and $q\mid Lr$ if and only if
$q/(q,L)\mid r$. Hence
$$
 \frac1{H_X}\sum_{\substack{L\le n\le X\\n\in S}}
    \frac{H_{M(D'_{n,L})}(N_n)}{nH_{N_n}}
 \le b_{L,X}\mu(S\cap U)
    +O\!\left(\frac{1+\log\log(3X/L)}{H_X}\right).
 \tag{6}
$$
Indeed, completion restricted to starting points in $S$ is exactly
the restriction of $\nu_{L,X}$ to $S$, so its mass in $U$
is $\nu_{L,X}(S\cap U)$. This also explains the coefficient
$b_{L,X}$. The theorem allows $S,U,L$ to depend on $X$.

One may take $S$ to be the full periodic survivor set of a finite
prefix and $U$ its tail union; then the right side has the desired
incremental Haar footprint. Starting with $n\ge L$, where $L$
is the prefix period, makes every prefix modulus active.

## The remaining loss

The weights on the left of (5)--(6) are return probabilities, not
indicators of deletion. For a sole active witness $q$, the return
probability at $L=1$ is only
$$
 \frac{H_{\lfloor n/q\rfloor}}{qH_n}.
$$
In (6), a witness with $q/(q,L)>n/L$ contributes zero.
Thus comparable-modulus first kills can be lost altogether, and the
coupling does not establish the required unweighted logarithmic-tail
estimate. Neither the coupling proof nor (5)--(6) uses singleton
distinctness. The counterexample below rules out a universal lower
bound for these return weights even after imposing distinctness and
primitivity. A solution by this route would need a different completion
law or additional footprint-sensitive information. No such adaptive
kernel or uniform first-kill relative-entropy bound was obtained.

### The averaged return can be arbitrarily small despite full deletion

There is no universal positive lower bound for the return weight in
(5), even for a primitive zero-residue system with canonical private
integer witnesses. Fix an integer $Q\ge2$, and put
$$
 P_Q=\{q\ge Q:\text{every proper divisor of }q\text{ is below }Q\}.
$$
This is primitive. Every integer $n\ge Q$ has a smallest divisor
at least $Q$, which belongs to $P_Q$. Thus the zero classes
at these distinct moduli, activated at $n\ge q$, delete exactly
$[Q,\infty)\cap\mathbb N$. Their canonical witnesses $r_q=q$
are globally private, since no other member of $P_Q$ divides $q$.
In particular all their full first-kill cells are nonempty.

Nevertheless the left side of (5) is at most $1/(Q-1)$, uniformly
in $X$. To see this, sample $n$ harmonically up to $X$,
and then $m$ harmonically up to $n$, as in the completion.
Its guaranteed-return event is exactly $(n,m)\ge Q$.
For every $d\ge1$,
$$
 \Pr(d\mid m\,\vert\,n)
 =\frac{H_{\lfloor n/d\rfloor}}{dH_n}\le\frac1d,
 \qquad
 \Pr(d\mid n)=\frac{H_{\lfloor X/d\rfloor}}{dH_X}\le\frac1d.
$$
Here the first probability is conditional on the sampled integer
$n$. Consequently
$$
 \Pr((n,m)\ge Q)
 \le\sum_{d=Q}^{\infty}\Pr(d\mid n,\ d\mid m)
 \le\sum_{d=Q}^{\infty}\frac1{d^2}\le\frac1{Q-1}.
$$
The deletion proportion tends to one, whereas its averaged return
can therefore be as small as desired. This example does not have
a small full Haar footprint, and it is not a counterexample to
Problem 25. It rules out deducing the desired tail bound merely
by placing a universal lower bound on this return probability,
even after passing to primitive moduli or requiring private witnesses.
