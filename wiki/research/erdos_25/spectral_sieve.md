---
name: research/erdos_25/spectral_sieve
desc: Fourier-conductor and cumulative quotient-sieve energy budgets, with the singleton-sensitive arithmetic trace still unresolved.
tags: [fourier-analysis, partial-results, obstructions]
sources: []
created: 2026-09-22T04:28:00Z
updated: 2026-10-14T00:26:52Z
---


# research/erdos_25/spectral_sieve

***

This approach studies Fourier mass rather than the size of individual
quotient-sieve spikes. The identities below are proved. They do not yet
give the required estimate along the activated integer orbit.

Let $G=\widehat{\mathbb Z}$ with Haar probability $\mu$. A rational
character $\chi\in\mathbb Q/\mathbb Z$ has conductor $d(\chi)$, its
order. Fourier transforms use
$\widehat f(\chi)=\int f(x)\overline{\chi(x)}\,d\mu(x)$.
For a finite family put
$$
 C_i=[a_i]_{q_i},\quad U=\bigcup_i C_i,\quad
 F_i=C_i\setminus\bigcup_{j<i}C_j,\quad e_i=\mu(F_i).
$$

## Logarithmic conductor energy

For every finite family, even allowing repeated moduli,
$$
 \sum_\chi \log d(\chi)\,
             |\widehat{\mathbf1_U}(\chi)|^2
 \le\sum_i e_i\log q_i.
 \tag{1}
$$

**Proof.** Work on the finite group modulo $L=\operatorname{lcm}_i q_i$.
For $p\mid L$ and $1\le k\le v_p(L)$, let $T_{p,k-1}$ average the
$p$-adic digits at levels $k$ and above, fixing all other coordinates
and the residue modulo $p^{k-1}$. Its Fourier multiplier is
$\mathbf1_{v_p(d(\chi))<k}$.

Couple Haar $x$ with a conditionally independent resampling $y$ in that
fiber. For $f=\mathbf1_U$,
$$
 \|f-T_{p,k-1}f\|_2^2
 =\mathbb P(f(x)=1,f(y)=0).
$$
If $x\in F_i$ and $v_p(q_i)<k$, the resampling preserves membership
in $C_i$, so $f(y)=1$. Therefore
$$
 \sum_{v_p(d(\chi))\ge k}|\widehat f(\chi)|^2
 \le\sum_{p^k\mid q_i}e_i.
$$
Multiply by $\log p$ and sum over $(p,k)$ to obtain (1). $\square$

The survivor indicator has the same nonconstant Fourier coefficients
up to sign, so satisfies the same bound. For a fixed infinite family,
let $U_X$ use the moduli at most $X$. Since $\sum_i e_i\le1$,
$$
 \sum_{q_i\le X}e_i\log q_i=o(\log X).
 \tag{2}
$$
Indeed, a fixed initial part contributes $O(1)$, and the remaining
sum is at most $\log X$ times its arbitrarily small total $e_i$-mass.
Thus (1) bounds the full finite-prefix Fourier energy by $o(\log X)$.
This is not a pointwise Fourier approximation theorem.

## Exact update for a singleton class

Add $C=[a]_q$ to an old union with indicator $f$. Write
$$
 h=\mathbf1_{C\setminus U},\quad e=\mu(C\setminus U),\quad f'=f+h,
$$
and let $P_q$ be conditional expectation onto functions modulo $q$.
Then
$$
 P_qh=qe\,\mathbf1_C,
\qquad
 \|(I-P_q)f'\|_2^2-\|(I-P_q)f\|_2^2=-e+qe^2.
 \tag{3}
$$
To verify the second identity, only the fiber $C$ changes. On that
fiber $P_qf=1-qe$, and after the installation it is identically one.
Since $\|f'\|_2^2-\|f\|_2^2=e$, whereas
$$
 \|P_qf'\|_2^2-\|P_qf\|_2^2
 =q^{-1}\bigl(1-(1-qe)^2\bigr)=2e-qe^2,
$$
subtracting proves (3). Thus the total Fourier mass at conductors
**not dividing $q$** decreases by $e(1-qe)$.

There is a finer blockwise identity. Put
$H_q=\{j/q\bmod1:0\le j<q\}$, and partition the dual group into
cosets of $H_q$. On a nonzero coset $\chi+H_q$, set
$v_h=\widehat f(\chi+h)$ for $h\in H_q$. Since the Fourier transform
of $\mathbf1_C$ is $q^{-1}\exp(-2\pi i a h)$ on $H_q$,
$$
 v'_h=v_h-\frac{\exp(-2\pi i a h)}q
                 \sum_{k\in H_q}\exp(2\pi i a k)v_k.
 \tag{4}
$$
This is an orthogonal rank-one projection. The squared norm decreases
on each nonzero coset separately; only the zero coset receives the
additional term from $\mathbf1_C$. Multiple residues at one modulus
would impose several orthogonal projections at that same step.
Singleton distinctness allows only one installation per $q$.

## Why individual-increment truncation is invalid

The checked [translated digit sieve](rank_and_moment_obstructions.md#disjoint-first-kill-potentials-also-have-no-uniform-higher-moment)
has distinct old moduli at most $N=M^2$, with full survivor class
$Q\pmod{L_N}$, where
$$
 Q=N+1,\qquad L_N\ge2^M/(M+1).
$$
Appending $[0]_Q$ gives a first-kill cell which contains the active
endpoint $Q$ and is one class modulo
$R=\operatorname{lcm}(Q,L_N)$.
Its Fourier coefficients have magnitude $1/R$ at the $R$ characters
whose conductors divide $R$. The number of rational characters with
conductor at most $Q^A$ is $O(Q^{2A})$. Hence, for every fixed $A$,
its conductor-$\le Q^A$ Fourier truncation has absolute value
$$
 O(Q^{2A}/R)=o(1)
$$
at $Q$, although the cell's indicator equals one there.

Activation and distinctness therefore do not justify a polynomial-height
pointwise truncation of individual first-kill increments. Any successful
use of (3)--(4) must retain cancellation against the old spectrum.
Also, (1) alone cannot distinguish the singleton problem from the
multi-residue setting, where logarithmic density can fail. No global
summation of these spectral updates giving $o(\log X)$ harmonic
discrepancy has been proved.

## The proposed energy-charging estimate is false

A proposed use of the first-kill energy was the uniform
finite estimate
$$
 H_B(X)\le\beta H_{\lfloor X\rfloor}
       +C\left(1+\sum_{q_i\le X}e_i\log q_i\right),
 \tag{5}
$$
with an absolute $C$, for distinct singleton moduli. Here $\beta$ is
the full finite union measure. This estimate is **false**.

The checked [energy counterexample](energy_counterexample.md) gives
finite distinct-modulus singleton systems, with the original delayed
activation, for which
$$
 \sum_q e_q\log q\longrightarrow2\log2,
 \qquad
 H_B(Q)-\beta H_Q\sim(\log Q)^{1/21}\longrightarrow\infty.
$$
The energy includes every preparatory congruence. Thus this is an
amortized counterexample to (5), not merely a failure of an
individual-cell comparison. It does not contradict (1) or the exact
spectral updates (3)--(4).

Its former sufficiency argument remains correct: apply it to the
finite prefix $q_i\le X$ of a fixed infinite family. Its deletion set
agrees with the infinite deletion set below $X$, its measure is at most
$\beta_\infty$, and its first-kill densities agree with the infinite
family's corresponding densities. Equation (2) would then give
$\limsup H_B(X)/\log X\le\beta_\infty$. Fixed prefixes give the
opposite lower bound.

The counterexample's normalized excess tends to zero, so it does not
refute a uniform additive $o(\log X)$ estimate or the infinite problem.
Any further spectral proof must obtain an orbit comparison other than
the false bound (5).

## A weaker energy target: unresolved

The continuation considered, but did not prove or refute, the estimate
$$
 (H_B(X)-\beta H_X)_+
 \le C\sqrt{H_X\left(1+\sum_{q_i\le X}e_i\log q_i\right)}.
 \tag{6}
$$
Together with (2), it would prove the exact problem. It is much weaker
than the false linear-energy estimate (5). The newer
[rank-filtered bounded-energy examples](energy_counterexample.md#rank-filtered-residue-channels)
have excess at least $(\log X)^\gamma$ for every
$\gamma<(7\,2^{1/7}-3\,3^{1/3}-3)/4=0.100469\ldots$.
For their parameters the trivial survivor upper bound also gives
excess $o(\sqrt{\log X})$. Thus they do not refute (6).

One exact restriction on possible counterexamples to (6) is available.
Write $\delta=1-\beta$ and
$$
 W=\sum_{\substack{p\le X\\p\text{ is a selected prime modulus}}}
                       \frac{\log p}{p}.
$$
For a selected prime modulus $p$, every earlier modulus is smaller than
$p$, hence coprime to it. Consequently its first-kill measure is
$e_p=\delta_{p-}/p\ge\delta/p$. If
$\mathcal E=\sum e_q\log q$ and $D_+=(H_B-\beta H_X)_+$, then
$$
 \mathcal E\ge\delta W,\qquad D_+\le\delta H_X,
 \qquad
 \frac{D_+^2}{H_X\mathcal E}\le\frac{\delta H_X}{W}
 \tag{7}
$$
whenever the denominators are positive. Thus (6) holds on families
with $W\ge c\delta H_X$, with a constant depending only on $c>0$.
This is not a general estimate: arbitrary families can have $W=0$.
No unverified prime-distribution theorem is needed or used in (7).

The remaining spectral gap is specific. A bound for arbitrary disjoint
periodic functions $h_q\le\mathbf1_{C_q}$ cannot substitute for (6):
such functions could select extremely small high-period subcylinders
around the sampled integers. The actual recursion
$h_q=\mathbf1_{C_q}(1-f_{\rm old})$ must be retained. No summation of
its projection identities proving (6) was obtained.

## Isolating the negative energy term in the activated trace

There is a checked refinement of the exact projection identity, but
still no bound for its remaining trace. Put
$$
 h_q=\mathbf1_{F_q},\qquad r_q=(I-P_q)h_q,
 \qquad R_q(X)=\sum_{q\le n\le X}\frac{r_q(n)}n.
$$
Here $P_qh_q=qe_q\mathbf1_{C_q}$. With
$B_q=C_q\cap[q,\infty)$, the exact identity is
$$
 H_{E_q}(X)=qe_qH_{B_q}(X)+R_q(X).
 \tag{8}
$$
Since $qH_{B_q}(X)\le H_{\lfloor X/q\rfloor}$, summation gives
$$
 \begin{aligned}
 H_B(X)-\beta H_{\lfloor X\rfloor}
 &\le\sum_{q\le X}R_q(X)
  -\sum_{q\le X}e_q
      (H_{\lfloor X\rfloor}-H_{\lfloor X/q\rfloor})\\
 &\le\sum_{q\le X}R_q(X)-\mathcal E_X+\log2,
 \qquad \mathcal E_X=\sum_{q\le X}e_q\log q.
 \end{aligned}
 \tag{9}
$$
For the last line use
$H_N-H_{\lfloor N/q\rfloor}\ge\log(q/2)$ and $\sum e_q\le1$.
If the finite family contains inactive moduli above $X$, their
contribution to $\beta$ only improves the first inequality.

Orthogonality of conditional expectation also gives
$$
 \|r_q\|_2^2=e_q-qe_q^2,
$$
exactly the decrease of the old spectrum outside the characters whose
conductors divide $q$. Thus the low-conductor part of each increment
already supplies a negative energy charge in (9). What would suffice
is the still-unproved simultaneous bound
$$
 \sum_{q\le X}R_q(X)
 \le\mathcal E_X+C\sqrt{H_{\lfloor X\rfloor}(1+\mathcal E_X)}.
 \tag{10}
$$
It would imply (6), up to an absolute additive constant.

Separate Cauchy--Schwarz estimates do not establish (10): the
point-evaluation kernels on the common period can have arbitrarily
large high-conductor norm. Pairwise progression error estimates also
do not control the nonlinear first-kill recursion. The
[sharp nonempty-cell bound](rank_and_moment_obstructions.md#size-of-a-nonempty-first-kill-cell)
quantifies a singleton restriction on such cells, but does not
bound the sum in (10). No global trace estimate resulted from this attempt.

## A cumulative quotient-sieve energy budget

There is a stronger energy inequality than (1), retaining the energy of
every first-kill innovation rather than only the final union. Put
$$
 f_i=\mathbf1_{\bigcup_{j\le i}C_j},\quad
 h_i=f_i-f_{i-1},\quad e_i=\mu(F_i),\quad
 \mathcal E(f)=\sum_\chi\log d(\chi)|\widehat f(\chi)|^2.
$$
For every finite family,
$$
 \mathcal E(f_N)+
 \sum_{i\le N}\sum_\chi
 \log\frac{d(\chi)}{\gcd(d(\chi),q_i)}
                  |\widehat h_i(\chi)|^2
 \le\sum_{i\le N}e_i\log q_i.
 \tag{11}
$$

**Proof.** Work on a finite common period and fix the prime-digit
conditional expectation $T=T_{p,k-1}$, with $Q=I-T$. If
$k>v_p(q_i)$, the cylinder $C_i$ is $T$-measurable. Therefore
$$
 Qh_i=-\mathbf1_{C_i}Qf_{i-1},\qquad
 Qf_i=(1-\mathbf1_{C_i})Qf_{i-1},
$$
and
$$
 \|Qf_i\|_2^2-\|Qf_{i-1}\|_2^2=-\|Qh_i\|_2^2.
$$
If $k\le v_p(q_i)$, orthogonality of conditional expectation and
disjointness of $f_{i-1}$ and $h_i$ instead give
$$
 \|Qf_i\|_2^2-\|Qf_{i-1}\|_2^2
 =e_i-2\langle Tf_{i-1},Th_i\rangle-\|Th_i\|_2^2
 \le e_i.
$$
Both conditional expectations in the inner product are nonnegative.
Telescoping proves the coordinatewise inequality
$$
 \|Qf_N\|_2^2+
 \sum_{i:v_p(q_i)<k}\|Qh_i\|_2^2
 \le\sum_{i:v_p(q_i)\ge k}e_i.
$$
Multiply by $\log p$ and sum over $p,k$. A character in the
innovation term occurs at exactly the levels
$v_p(q_i)<k\le v_p(d(\chi))$, proving (11). $\square$

The quotient-survivor indicator
$$
 g_i(t)=1-f_{i-1}(a_i+q_it)
$$
has mean $q_ie_i$. Extension from the cylinder $C_i$ and Fourier
pullback under $t\mapsto a_i+q_it$ give
$$
 \sum_\chi\log\frac{d(\chi)}{\gcd(d(\chi),q_i)}
                       |\widehat h_i(\chi)|^2
 =\frac1{q_i}\mathcal E(g_i).
$$
Indeed, explicitly,
$$
 \widehat h_i(\chi)=q_i^{-1}e^{-2\pi i a_i\chi}
                                      \widehat g_i(q_i\chi).
$$
For a common period $L$ divisible by $q_i$, the function $g_i$
has period $L/q_i$. Multiplication by $q_i$ maps the characters
modulo $L$ onto those modulo $L/q_i$, with fibers of size $q_i$.
The quotient character has conductor
$d(\chi)/\gcd(d(\chi),q_i)$. Thus
$$
 \mathcal E(f_N)+\sum_{i\le N}\frac{\mathcal E(g_i)}{q_i}
 \le\sum_{i\le N}e_i\log q_i.
 \tag{12}
$$
For a fixed infinite family, (2) bounds the cumulative quotient-sieve
energy over $q_i\le X$ by $o(\log X)$.

Neither inequality uses distinctness of the moduli; repeated
single-cylinder installations satisfy the same argument. They do not
control high-conductor point evaluation on the activated integer
orbit, and cannot alone distinguish the singleton problem from its
multi-residue variant. The entropy and square-root trace estimates
remain unproved.
