---
name: research/prime_binary_new_attack/critical_length_obstructions
title: Critical-length obstructions for the prime binary series
desc: |
  Limits of specified phase-counting mechanisms for Problem 251, a
  rational interpolation theorem preserving residues below the critical
  length, and a comparison with known consecutive-prime theorems.
created: 2026-10-15T18:43:21Z
updated: 2026-10-17T22:11:11Z
---

***

The notation, Lemma B, the rule (P), Theorem C, Corollary D and the critical
phase statement CPS($d$) are those of
[[research/prime_binary_new_attack/proof_sketch|the parity-prediction sketch]];
$r(n)\in R_K$ is the residue pattern $(h_{n+j}\bmod2^{j+1})_{0\le j<K}$ and
$E_d\subseteq R_K$ the set of patterns on which the rule fails. Each item
below concerns a specified mechanism, either for proving CPS($d$) or for
excluding a denominator in some other way, and states where that mechanism
stops. None is an impossibility theorem for all proofs. Items O1, O3, O5 and
O7--O10 are proved here; O2 is proved from the sieve premise stated with it; O4
and O6 compare a requirement with what is proved, and say where a model
computation is used. All are Plasma AI's author-recorded deductions, not
independently reviewed.

## O1. Fixed block lengths

The left side of $(C_d)$ is at most $N_X=(1+o(1))X/\log X$, so $(C_d)$ is
false whenever $2^K\le2dX/N_X=2d\log X\,(1+o(1))$. For large $X$ this
excludes every fixed $K$ and every $K\le c\log_2\log X$ with $c<1$.
Equivalently, part 2 of Theorem C is automatically true below that length,
whatever the gaps are, so it carries no information there. No statement about
a bounded number of consecutive gaps, proved or conjectured, can feed
Corollary D, and the same holds for Proposition 4 of
[[research/prime_binary_series/truncation_certificates|the truncation sketch]],
whose "Length" paragraph makes the same computation. This is the averaged form
of the critical length. It is consistent with the sparse rational
perturbations of the prime gaps discussed on the truncation sketch ("Growth
and short-block statistics"), which are reported to preserve block statistics
at lengths $o(\log\log M)$, with $M$ an index scale. That range lies below the
critical length $\log_2\log X\approx1.44\log\log X$, so the two do not
conflict. O8 supplies a broader comparison for residue information:
pointwise residue patterns at subcritical lengths can be preserved by a
sequence with a rational sum and the same cumulative growth. This does not
cover arguments using primality or rare-event counts not preserved by the
comparison.

## O2. Certificates built from residue patterns

Call a **pattern certificate** for $(C_d)$ a set $\mathcal C\subseteq E_d$ of
residue patterns together with a proved lower bound, exceeding $2dX/2^K$, for
$\#\{n\in I_X:r(n)\in\mathcal C\}$. Since $E_d$ is a union of patterns, every
certificate that counts starts by congruence conditions on the next $K$ gaps
has this form, and the question is how many patterns it must involve.
Congruence blocks (all $r_j=0$), exact gap templates and the strings of
congruent primes in the theorems compared below are single patterns or
subsets of single patterns.

**Premise (U), unproved here.** There is a function
$U(k)=\exp(O(k\log(k+1)))$ such that for large $X$, every integer
$\tfrac12\log_2\log X\le k\le2\log_2\log X$ and all positive even integers
$\sigma_1<\dots<\sigma_k\le(\log X)^2$,

$$
\#\{p\in(X,2X]\ \text{prime}:p+\sigma_i\ \text{prime for}\ 1\le i\le k\}
\le U(k)\,\frac{X}{(\log X)^{k+1}} .
$$

This is a hypothesis in a growing dimension and a short offset range. A
fixed-dimension prime-tuple sieve normally retains an offset-dependent
singular series; it does not supply a constant uniform over arbitrary
offsets just by fixing $k$. For example, the singular series of a pair can
grow with the small prime divisors of its difference. No such uniform
fixed-$k$ bound is asserted, and (U) has not been verified from a source.

**Proposition O2.** Assume (U), fix $C\ge0$ and an odd $d$, and let
$K=\lceil\log_2(d\log X)\rceil+C$. For large $X$ every pattern certificate for
$(C_d)$ has

$$
|\mathcal C|\ge\frac{2^{K^2/2-(C+3/2)K-C-1}}{K^K\,U(K)}
=2^{K^2/2-O_C(K\log K)} ,
$$

a proportion $2^{-O_C(K\log K)}$ of the $2^{K(K+1)/2}$ patterns in $R_K$, and
more than $(\log X)^D$ patterns for every fixed $D$.

*Proof.* Lower bounds cannot exceed the true counts, so it suffices to bound
$\#\{n\in I_X:r(n)\in\mathcal C\}$ from above. Put $B=K2^K/d$. Since
$\sum h_m$ over $\pi(X)<m\le\pi(2X)+K$ is $X/2+o(X)$, at most
$KX/(2B)\,(1+o(1))=dX2^{-K-1}(1+o(1))$ starts have some $h_{n+j}>B$ with
$j<K$. A pattern $c$ fixes $h_{n+j}\bmod2^{j+1}$, so it contains at most
$\prod_{j<K}(B2^{-j-1}+1)\le2^K\prod_{j<K}B2^{-j-1}=2^K(K/d)^K2^{K(K-1)/2}$
gap vectors with all entries at most $B$ (each factor $B2^{-j-1}$ is at least
$K/d\ge1$ for large $X$). Their offsets are at most
$2KB=2K^2 2^K/d=O_C(K^2\log X)<(\log X)^2$, and $K$ lies in the range
of (U), for large $X$. For each vector, the starts carrying it have
$p_n+2(h_n+\dots+h_{n+i-1})$ prime for $1\le i\le K$, so (U) bounds their
number by $U(K)X/(\log X)^{K+1}$. A certificate therefore needs

$$
\frac{2dX}{2^K}<\frac{dX}{2^{K+1}}(1+o(1))
+|\mathcal C|\,2^K\Bigl(\frac Kd\Bigr)^K2^{K(K-1)/2}U(K)
\frac{X}{(\log X)^{K+1}} ,
$$

so $|\mathcal C|\ge d(\log X)^{K+1}/\bigl(4^K(K/d)^K2^{K(K-1)/2}U(K)\bigr)$ for
large $X$. Since $d\log X\ge2^{K-C-1}$, one has
$(\log X)^{K+1}\ge2^{(K-C-1)(K+1)}d^{-K-1}$, and the displayed bound follows by
collecting powers of $2$. $\square$

The count concerns exact residue patterns. Certificates that group patterns
by the leading binary digits of each residue, and so fix the phase only
approximately, are not covered: for them the sieve loss $U(K)$ is as large as
the number of groups, and the same counting argument gives nothing.

## O3. Pointwise brackets need about $0.525\log_2p_m$ gaps

Proposition G of the sketch decides the parity rule at a single large index
$m$ from the residues of $J_m=\lceil0.525\log_2p_m+\log_2d\rceil+3$ gaps,
using the gap bound $g_k\le2p_k^{0.525}$ that the
[[../library/primes/baker_2001_difference_between_consecutive_primes/theorem_1|Baker–Harman–Pintz theorem]]
gives for large $k$. Fewer gaps cannot do the same with that bound alone.

**Proposition O3.** Let $d$ be odd, let $m\ge2$ and $J\ge1$ with
$2^J\le p_{m+J}^{0.525}$, and let $c$ be the least positive integer with
$c\equiv-2^JQ_{m,J}\pmod{2^J}$. The sequence that agrees with $(h_k)$ for
$k<m+J$ and equals $c$ for $k\ge m+J$ satisfies the same bound,
$h'_k\le(p'_k)^{0.525}$ for $k\ge m+J$, where $p'_k$ are its partial sums,
and its tails satisfy $dH'_k\in\mathbb Z$ for every $k\ge m$.

*Proof.* $2^JQ_{m,J}$ is an integer, and $c\le2^J\le p_{m+J}^{0.525}\le
(p'_k)^{0.525}$ for $k\ge m+J$, since $p'_k\ge p'_{m+J}=p_{m+J}$. The tail of
the new sequence at $m$ is $H'_m=Q_{m,J}+2^{-J}c$, and
$2^JH'_m=2^JQ_{m,J}+c\equiv0\pmod{2^J}$, so $H'_m\in\mathbb Z$. By
$H'_{k+1}=2H'_k-h'_k$ every later tail is an integer too. $\square$

So no argument that uses only the first $J$ gaps after $m$ and the bound
$g_k\le2p_k^{0.525}$ can show $dH_m\notin\mathbb Z$ when
$J\le0.525\log_2p_{m+J}$: a sequence obeying the same bound, with the same
first gaps, has every later tail on the lattice. This is the completion
argument of the truncation sketch with the gap bound kept. Under Cramér's
conjecture $g_k\ll(\log p_k)^2$ both thresholds become
$2\log_2\log p_m+O_d(1)$, still of critical order. Theorems producing large
gaps enlarge tails and give no upper bracket. The completing sequence is not a
sequence of primes; the proposition says that a pointwise gap bound is not
enough, not that primes cannot be handled pointwise.

## O4. Weighted means

Summing Lemma B with weights $w_n\ge0$ on $I_X$ gives

$$
\sum_{n\in I_X}w_n(1-\varphi_{n,K})\le d2^{-K}\sum_{n\in I_X}w_nH_{n+K}
\le(\max_nw_n)\frac{(1+\varepsilon)dX}{2^{K+1}} .
$$

After normalising $\max w_n=1$ the left side is at most the unweighted sum,
so a weighted refutation implies the unweighted one: bounded weights never
ask for less. Sieve weights, whose maximum far exceeds their mean, do worse.
Replacing (T) by Cauchy–Schwarz and the convexity bound
$H_m^2\le\sum_ih_{m+i}^22^{-i-1}$ gives
$\sum_{n\in T}H_{n+K}\le\bigl(|T|\sum_{X<p_k\le3X}h_k^2\bigr)^{1/2}$ up to a
negligible term. Under rationality, the mispredicted starts have
$H_{n+K}\ge2^{K-1}/d$ (part 3 of Theorem C), so their number is at most
$4d^2\,4^{-K}\sum_{X<p_k\le3X}h_k^2$. With a second moment of the size
$\asymp X\log X$ that the Cramér model predicts, this bound is about
$4^{1-C}N_X$ at $K=\lceil\log_2(d\log X)\rceil+C$. That would lower the
proportion CPS($d$) needs from about $2^{-C}$ to about $4^{-C}$, at the same
critical length. The known bounds are weaker:
[[../library/primes/stadlmann_2022_mean_square_gap_between_primes/theorem_1|Stadlmann's unconditional $x^{1.23+\varepsilon}$, and the bound $x(\log x)^3$ of Selberg under the Riemann hypothesis recorded on the same page]].
With Selberg's bound the route needs $4^K\gg(\log X)^4$, which is longer
than the critical length; with Stadlmann's it needs a power of $X$.

## O5. Integer combinations of tails

**Proposition O5.** Let $c_n$ be integers, finitely many nonzero, and
$q=\sum_nc_n2^{n-1}$. Then

$$
\sum_nc_nG_n\equiv qS\pmod 1 ,
$$

and for every $M$ at least as large as each $n$ with $c_n\ne0$,

$$
\sum_nc_nG_n=\sum_nc_nP_{n,M-n}+q\,2^{1-M}G_M ,
$$

where $P_{n,K}=2Q_{n,K}$ is the truncation of the truncation sketch.

*Proof.* $G_n=2^{n-1}G_1-\sum_{k<n}2^{n-1-k}g_k$ and $G_1=S-2$ give
$G_n\equiv2^{n-1}S\pmod1$. The identity is identity 4 of the truncation sketch
applied at each $n$ with $K=M-n$. $\square$

So an integer combination of tails has the fractional part of an integer
multiple of $S$. Showing that $b\sum_nc_nG_n$ is not an integer is the same
as showing $bqS\notin\mathbb Z$, and by the identity it requires a bracket for
the single tail $G_M$ with the multiplier $bq2^{1-M}$: the certificate
lemma of the truncation sketch at one index. The uncontrolled remainder can be
rescaled but not cancelled, and when $q=0$ the combination is an integer and
says nothing. Comparing two starts $n\ne m$ whose truncations satisfy
$d(P_{n,K}-P_{m,K})\in\mathbb Z$ is the combination $G_n-G_m$ truncated at
$n+K$ and at $m+K$. Under rationality it forces
$d2^{-K}(G_{n+K}-G_{m+K})\in\mathbb Z$, so a refutation needs
$0<|G_{n+K}-G_{m+K}|<2^K/d$: two tails known to the critical precision instead
of one.

## O6. Upper bounds for the correctly predicted starts

A rational $S$ makes at least $N_X-(1+\varepsilon)dX/2^K$ starts in $I_X$
correctly predicted (Theorem C). To refute this from above one would show
that fewer starts are correctly predicted. The direct upper bound examined
here drops consecutiveness. For a bound $B$ on the halved gaps,

$$
\#\{n\in I_X:h_n\equiv\beta_{n,K}\pmod2\}
\le\#\{n\in I_X:\max_{j<K}h_{n+j}>B\}+\sum_{v\in V_B^+}T_X(v),
$$

where $V_B^+$ is the set of vectors $v\in\{1,\dots,B\}^K$ whose residue
pattern lies outside $E_d$, and $T_X(v)$ counts primes $p\in(X,2X]$ with
$p+2(v_0+\dots+v_{i-1})$ prime for $1\le i\le K$.

**Proposition O6.** (a) If the first term is bounded through
$\sum h_m=X/2+o(X)$, the bound obtained is $KN_X\log X/(2B)\,(1+o(1))$, which
is at least $N_X$ unless $B>K\log X/2$, up to its asymptotic error.
(b) Suppose $K\to\infty$ and $K=O(\log\log X)$. For $B\ge K\log X$,

$$
\sum_{v\in\{1,\dots,B\}^K}T_X(v)\ge(1+o(1))\frac{4^K}{16K^{3/2}}N_X .
$$

*Proof.* (a) is Markov's inequality applied to the $K$ shifted ranges. For
(b), the sum is nondecreasing in $B$, so take $B=\lceil K\log X\rceil$ and cut
$(X,2X]$ into $\lfloor X/(2B)\rfloor=(1+o(1))N_X/(2K)$ full intervals of
length $2B$, discarding the final interval of length less than $2B$.
The discarded interval holds at most $2B+1$ integers. Any $K+1$ primes
$q_0<\dots<q_K$ in one full interval have consecutive halved
differences at most $B$, so they are counted by $T_X(v)$ for the vector $v$
of those differences, and distinct sets give distinct pairs $(q_0,v)$. By the
convexity of $m\mapsto\binom m{K+1}$, the number of such sets is at least the
number of intervals times $\binom{\lfloor\bar m\rfloor}{K+1}$, where
$\bar m$ is the mean number of primes per full interval. The quantitative
prime number theorem gives
$N_X=(X/\log X)(1+O(1/\log X))$. With the stated range of $K$, the rounding
and discarded-interval errors therefore give $\bar m=2K+o(1)$, so
$\lfloor\bar m\rfloor\ge2K-1$ for large $X$. Finally
$\binom{2K-1}{K+1}\ge4^K/(8\sqrt K)$ for large $K$. $\square$

With $B\ge K\log X$, success of this bound would require the vectors outside
$E_d$ to carry only $O(K^{3/2}4^{-K})$ of all the sub-configurations counted
by the $T_X$. The total-count lower bound alone says nothing about that
restricted share. A model assigning comparable mass to the two phase halves
would not have the required concentration; no estimate for the actual share
is proved here. Thus this is a diagnostic of the loss from dropping
consecutiveness, not an impossibility theorem for upper-bound methods.
Ringer's positive comparison, recorded
on the truncation sketch, is an upper bound of the required kind that keeps
consecutiveness, since its tests are sets of first consecutive offsets; that
is why it enters as a hypothesis and not as a sieve estimate.

## O7. Information content and balance

- The phase $\varphi_{n,K}$, and with it the rule, is a function of
  $r(n)\in R_K$, a set of $2^{K(K+1)/2}$ patterns. The first gap enters only
  through its parity, the gap of index $j$ through its residue modulo
  $2^{j+1}$; at $K=\lceil\log_2(d\log X)\rceil+C$ the gaps with $2^{j+1}$
  comparable to $d\log X$ enter through their actual size, at the scale of the
  mean gap.
- Up to circular distance $\delta$ in the phase, only the leading
  $t=\lceil\log_2(dK/\delta)\rceil$ binary digits of each residue matter:
  replacing the lower digits of every $r_j$ by zeros moves the phase by less
  than $dK2^{-t}\le\delta$. Deciding the rule away from the two boundary
  phases therefore uses about $K\log_2(dK/\delta)$ bits of the next $K$ gaps.
- By Lemma E each translation $\tau_j$ exchanges $E_d$ and its complement.
  The rule is balanced in every coordinate, so the demand of a rational $S$,
  $\mu_{X,K}(E_d)\to0$, is a failure of anti-concentration in every one of
  these coordinates at once (part 1 of Theorem F), not a small bias.

## O8. Residue laws below the critical length

O1 shows that the averaged mechanism of Corollary D cannot work below the
critical length, and part 2 of Theorem F turns a non-degenerate residue law at
lengths with $2^K/\log X\to\infty$ into irrationality. The construction below
shows that these residues and cumulative growth alone do not force
irrationality: every sequence of gaps of the stated growth has a
dyadic-rational comparison sequence preserving the pointwise residues. It
extends the theorem on bounded perturbations preserving congruences in
Section 8.1 of W. Cook's manuscript *Prime-Gap Dyadic Series: Perturbations,
Exact Criteria and Certificates*, dated September 2026
([source](https://raw.githubusercontent.com/wcook04/plectis-erdos/01d2dddbd81440d8fd37a6178835baca097e1a3a/paper/251/erdos251-prime-gap-reasoning-surface.tex);
unrefereed). That theorem adds $0$ or a fixed modulus $M$ to every
coefficient after a prefix, so that the sum becomes rational while every
coefficient keeps its residue modulo $M$. Here the modulus is a power of $2$
that grows with the index as fast as the growth of the positions allows, and
the changes are sparse.

The construction applies to every sequence of gaps of the size of the prime
gaps. Let $h_n$ ($n\ge2$) be positive integers, put $g_1=1$, $g_n=2h_n$ for
$n\ge2$, $p_1=2$ and $p_{n+1}=p_n+g_n$, and suppose that $p_n\sim n\log n$.
Define $S=\sum_{n\ge1}p_n2^{-n}$, $H_n$, $I_X$, $N_X$, $r(n)$ and
$\mu_{X,K}$ from this sequence as on the sketch; the prime gaps are one such
sequence. The proofs of Lemmas A and B, of (T) on the truncation sketch, and
of Theorems C and F use only that the gaps from the second on are positive
and even and that $p_n\sim n\log n$ (through $p_{m+J}-p_m=o(p_m)$ for
$J=o(m)$, $p_{2m}\le3p_m$, $p_m\le m^2$ and $N_X\sim X/\log X$), so those
results hold for every such sequence.

**Proposition O8.** Let $(h_n)$ be as above, and let $(K_n)_{n\ge2}$ be a
nondecreasing sequence of nonnegative integers with $2^{K_n}/\log n\to0$.
There are integers $c_n\ge0$ such that the sequence $h'_n=h_n+c_n$, with
$g'_1=1$, $g'_n=2h'_n$, $p'_1=2$, $p'_{n+1}=p'_n+g'_n$ and
$S'=\sum_{n\ge1}p'_n2^{-n}$, has the following properties.

1. $S'$ is a dyadic rational: $S'\in\mathbb Z[1/2]$.
2. $2^{K_n}$ divides $c_n$ for every $n$. Hence, for every $n\ge2$ and every
   $K\le K_n$, the residue patterns $(h'_{n+j}\bmod2^{j+1})_{0\le j<K}$ and
   $(h_{n+j}\bmod2^{j+1})_{0\le j<K}$ are equal.
3. $c_n/\log n\to0$, and $c_n=0$ outside a set of indices of density zero.
4. $p'_n/p_n\to1$.

*Proof.* For $n\ge3$ put $\omega_n=\log_2\log n-K_n$, so that
$\omega_n\to\infty$, and let
$L_n=\max\bigl(1,\lfloor\frac12\inf_{m\ge n}\omega_m\rfloor\bigr)$, a
nondecreasing sequence of positive integers tending to infinity. Fix
$n_0\ge3$, let $i_0=n_0$ and $i_t=i_{t-1}+L_{i_{t-1}}$ for $t\ge1$, and put
$m_t=i_t-n_0+1-K_{i_t}$. Since $K_i\le\log_2\log i$ for large $i$,
$m_t\to\infty$.

Let $a=\lceil H_{n_0}\rceil-H_{n_0}\in[0,1)$. Define $r_0=a$, $\bar m_0=0$
and, for $t\ge1$,

$$
u_t=\lfloor2^{m_t}r_{t-1}\rfloor,\qquad
r_t=r_{t-1}-u_t2^{-m_t},\qquad
\bar m_t=\max(\bar m_{t-1},m_t).
$$

By induction $0\le r_t<2^{-\bar m_t}$: the choice of $u_t$ gives
$0\le r_t<2^{-m_t}$, and $r_t\le r_{t-1}<2^{-\bar m_{t-1}}$. Hence
$r_t\to0$ and $u_t\le2^{m_t}r_{t-1}<2^{m_t-\bar m_{t-1}}$. For $t\ge2$,
$m_t-\bar m_{t-1}\le m_t-m_{t-1}\le i_t-i_{t-1}=L_{i_{t-1}}$, because $K$ is
nondecreasing, and $m_1\le L_{n_0}+1$. As $L$ is nondecreasing,
$u_t<2^{L_{i_t}+1}$ for every $t\ge1$.

Put $c_{i_t}=2^{K_{i_t}}u_t$ for $t\ge1$ and $c_n=0$ at every other index.
Every $i_t$ exceeds $n_0$ and $c_{i_t}2^{-(i_t-n_0)-1}=u_t2^{-m_t}$, so

$$
H'_{n_0}-H_{n_0}=\sum_{t\ge1}u_t2^{-m_t}=\lim_{t\to\infty}(a-r_t)=a ,
$$

and $H'_{n_0}=\lceil H_{n_0}\rceil$ is an integer. Identity 2 of the
truncation sketch, $G'_{k+1}=2G'_k-g'_k$, gives
$2^{n_0-1}G'_1=G'_{n_0}+\sum_{k<n_0}2^{n_0-1-k}g'_k\in\mathbb Z$, since
$G'_{n_0}=2H'_{n_0}$; and $S'=2+G'_1$ by identity 1 there, which holds for
every such sequence because $p'_n2^{-n}\to0$. This proves part 1. Part 2
holds by construction: the pattern of length $K$ at $n$ uses the moduli
$2^{j+1}\le2^K\le2^{K_n}\le2^{K_{n+j}}$. For part 3,
$c_{i_t}<2^{K_{i_t}+L_{i_t}+1}$, and once $\omega_i\ge2$ one has
$L_i\le\omega_i/2$, so $c_i<2^{1-\omega_i/2}\log i$; thus $c_n/\log n\to0$.
The changed indices lie among the $i_t$, whose spacing tends to infinity, so
they have density zero. For part 4, $0\le p'_n-p_n=2\sum_{i<n}c_i$. Given
$\varepsilon>0$, $c_i\le\varepsilon\log i$ for $i\ge i_\varepsilon$, so
$p'_n-p_n\le C_\varepsilon+2\varepsilon n\log n$, and $p'_n/p_n\to1$.
$\square$

The changes write the binary digits of $a$ into high bits of sparse gaps,
above the modulus $2^{K_n}$, where no residue pattern of length at most $K_n$
looks. A changed gap grows by less than $2^{K+L+1}$ and the changes are $L$
apart, so the cost is about $2^{K+L}/L$ per index; the condition
$2^{K_n}=o(\log n)$ is what keeps this cost $o(\log n)$, so that the positions
keep their growth.

**Corollary O8 (comparison below and concentration above the critical length).** Let
$(h_n)$ be as above, and let $K_X$ be block lengths, nondecreasing in $X$,
with $K_X\le X/(\log X)^2$.

1. If $2^{K_X}/\log X\to0$, there is a sequence $(h'_n)$ with
   $S'\in\mathbb Z[1/2]$ and $p'_n/p_n\to1$ such that
   $\sup_{K\le K_X}d_{\mathrm{TV}}(\mu'_{X,K},\mu_{X,K})\to0$, where
   $\mu'_{X,K}$ is formed from $(h'_n)$. In particular
   $\sup_{j<K\le K_X}|\delta_j(\mu'_{X,K})-\delta_j(\mu_{X,K})|\to0$.
2. If $2^{K_X}/\log X\to\infty$, then every such sequence whose sum is
   rational has $\min_{j<K_X}\delta_j(\mu_{X,K_X})\to1$.

*Proof.* Part 2 is part 1 of Theorem F for that sequence. For part 1, extend
$X\mapsto K_X$ to a nondecreasing function on $[1,\infty)$, put
$K_n=K_{2p_n}$, which is nondecreasing with $2^{K_n}/\log n\to0$ because
$\log p_n\sim\log n$, and apply Proposition O8. Let
$I'_X=\{n:X<p'_n\le2X\}$. Since $p_n\le p'_n\le(1+o(1))p_n$, every
$n\in I'_X\setminus I_X$ has $p_n\in(X/(1+o(1)),X]$ and every
$n\in I_X\setminus I'_X$ has $p_n\in(2X/(1+o(1)),2X]$. The counting function
of the $p_n$ is asymptotic to $X/\log X$, so $|I_X\triangle I'_X|=o(N_X)$.
For large $X$ every $n\in I_X\cup I'_X$ has $p_n>X/2$, hence $K_n\ge K_X$,
and by part 2 of Proposition O8 the patterns of length $K\le K_X$ at $n$ are
the same for the two sequences. Two uniform probability measures on finite
sets $A$ and $B$ are at total variation distance at most
$|A\triangle B|/\max(|A|,|B|)$, and pushing both forward by one map does not
increase that distance; this gives the first claim. Finally
$\delta_j(\mu)=d_{\mathrm{TV}}(\mu,\mu\circ\tau_j)$, so
$|\delta_j(\mu)-\delta_j(\nu)|\le2d_{\mathrm{TV}}(\mu,\nu)$. $\square$

Every law that a sequence of gaps of this size has at lengths with
$2^K=o(\log X)$ is, up to $o(1)$ in total variation, the law of a
sequence with a dyadic rational sum; above the critical length, rationality
forces every law to be nearly singular to each of its translates. A
criterion relying on the preserved pointwise residues and growth cannot
exclude these comparison sequences. A criterion formulated only through
limiting laws must also be stable under the $o(1)$ total-variation error
before this observation applies to it. Relative counts of rare events are
not preserved by that error bound.
Part 2 of Theorem F works at $K=\log_2\log X+\omega_X$ with
$\omega_X\to\infty$, and Corollary D, through CPS($d$), already at
$K=\log_2\log X+O(1)$ when the mispredicted proportion beats its constants;
Proposition O8 does not reach lengths with $2^K\asymp\log X$. A criterion
using only bounded-length residue patterns and the preserved growth cannot
exclude the comparison sequences. This includes a positive proportion of
$n$ with $p_n\not\equiv p_{n+1}\pmod4$. The
two conditional constructions recorded on the truncation sketch also work
above the threshold, although their hypotheses concern exact offsets rather
than residues: Land's block length is
$\log_2\log X+4\log_2\log\log X$, and Ringer's comparison length is about
$\log_2\log X+\sqrt{\log_2\log X}$.

The positions $p'_n$ are not primes. Arguments that use primality, or the
exact sizes of gaps at lengths below the critical length, are not covered.
For exact block laws, Cook's sparse theorem reaches lengths $o(\log\log X)$,
as the truncation sketch records ("Growth and short-block statistics");
whether exact laws at lengths between that range and $\log_2\log X$ can
decide rationality is not settled here.

For the actual prime gaps there is a stronger comparison:
[[theory/irrationality/L228_sparse_prime_position_interpolation/_index|L228 preserves the nth prime itself outside a density-zero set]].
For every nested sequence of integer moduli $q_n=o(\log n)$, it interpolates
an interval of values of the binary series while preserving
$a_n\equiv p_n\pmod{2q_n}$ and changing each gap by $o(\log n)$. Choosing
$q_n=2^{K_n}$ retains the residue patterns in Proposition O8 at every start.
The signed gap changes have density-zero support, and their cumulative
position changes vanish on a set of density one. The proof uses the
classical prime-pair upper bound to find later gaps that absorb the negative
changes. The modified terms are not all primes. This strengthens the
comparison-sequence obstruction without supplying an estimate for CPS($d$).

At the logarithmic modulus the same interpolation problem has a different
answer.
[[theory/irrationality/L229_critical_modulus_interpolation/_index|L229 proves a dimension-zero bound]]
when the nested moduli satisfy $q_n\ge c\log n$ eventually. All binary-series
values from increasing integer sequences agreeing with $p_n$ at density
one and preserving these congruences form a set of Hausdorff dimension zero.
No smallness assumption on the individual gap changes is needed. The proof
counts their sparse integer quotients, whose total variation up to $N$ is
$O(N)$ after the first $\sqrt N$ indices. Thus L228's interval conclusion
cannot extend to this regime. A dimension-zero set may contain rationals;
L229 supplies no exclusion of a particular value and no prime-phase count.

Another attempted extension would reduce the number of changed positions
to $o(N/\log\log N)$, enough to keep exact blocks of $O(\log\log N)$ gaps
unchanged at almost every index start. That cannot support an interval
of values:
[[theory/irrationality/L230_sparse_interpolation_support/_index|L230 proves dimension zero under this support bound]],
without any congruence restriction. This leaves open a construction for
one specified rational target, and constructions preserving block laws
by overlap or cancellation rather than by this support estimate.
For moduli $q_n=O((\log n)^\alpha)$ with fixed $\alpha<1$, L228 does
achieve $|D\cap[1,N]|=O(N/\log\log N)$: its prime-pair estimate is
uniform for the shrinking small-gap cutoff in the proof. Thus the
big-oh support bound is attainable and the little-oh bound is not for
interval interpolation.

## O9. Filters and the number of original gaps

The step lemma of the sketch replaces an odd denominator by an integer
lattice for a sum of shifted tails. Its truncation length counts filtered
gaps. The following calculation keeps track of the original consecutive
primes that a theorem would have to control.

**Proposition O9.** Let $a_0,\ldots,a_r$ be nonnegative integers, with
$a_0a_r>0$, and put

$$
A(z)=\sum_{j=0}^r a_jz^j,\qquad W=A(1),\qquad q=A(2),\qquad
\widehat h_n=\sum_{j=0}^r a_jh_{n+j},\qquad
\widehat H_n=\sum_{j=0}^r a_jH_{n+j}.
$$

Suppose $S=a/(2^sd)$ with $d$ odd and $d\mid q$. Then
$\widehat H_n\in\mathbb Z$ for $n\ge\max(s+2,3)$. The parity-prediction
criterion applied to $\widehat h$ has mean factor $W$: a sufficient
contradictory count is more than $2WX/2^K$ mispredicted starts at filtered
length $K$, provided $K+r\le X/(\log X)^2$ and $X$ is sufficiently large.
The original window spans $K+r$ consecutive gaps. Whenever its count is
even cardinally possible, it satisfies the exact inequality

$$
2^{K+r}>\frac{2dX}{N_X}.
\tag{O9}
$$

Thus, with the same ordinary mean-tail estimate, filtering does not reduce
the necessary number of original gaps below
$\log_2(d\log X)+1-o(1)$.

*Proof.* Iterating $H_{n+1}=2H_n-h_n$ gives

$$
\widehat H_n=qH_n-
\sum_{j=0}^r a_j\sum_{i=0}^{j-1}2^{j-1-i}h_{n+i}.
$$

The second term is an integer, and $qH_n$ is an integer because $dH_n$ is
an integer. Absolute convergence also gives
$\widehat H_n=\sum_{i\ge0}\widehat h_{n+i}2^{-i-1}$, with positive integer
coefficients $\widehat h_{n+i}$. Applying (T) separately to the shifts gives

$$
\sum_{n\in I_X}\widehat H_{n+K}
\le W(1+\varepsilon)X/2 .
$$

The proofs of Lemma B and Theorem C apply with multiplier $1$ and this
mean bound; their parity rule uses the first $K$ filtered gaps. These depend
on the original gaps $h_n,\ldots,h_{n+K+r-1}$. Since there are only $N_X$
starts, the contradictory count requires $2^K>2WX/N_X$. Finally,
$q=\sum_j a_j2^j\le2^rW$ and $q\ge d$, so multiplying this last inequality
by $2^r$ proves (O9). The prime number theorem gives its asymptotic form.
$\square$

For the $t$-step gaps one has $A(z)=1+\cdots+z^{t-1}$, $W=t$ and
$q=2^t-1$. Their filtered critical length is
$K=\log_2(t\log X)+O(1)$, but the required original window has
$K+t-1$ gaps. In particular $d=2^t-1$ gains no reduction in the original
window length. Another possible choice takes the coefficients of $A$ to be
the binary digits of $d$, so $q=d$ and $W$ is the number of those digits
equal to one. It obeys the same tradeoff.

Leading zero coefficients can be removed by shifting the start; this
divides $A(2)$ by a power of $2$ and preserves its divisibility by the odd
number $d$. The span in (O9) is measured after this normalization. Some
gaps inside that span may be unused when $K<r$; the statement concerns the
length of the consecutive-prime window, not a lower bound on the number
of independent data entries.

The conclusion concerns this mean-based counting test. A filter could still
be useful if its prime statistic admits an estimate unavailable for the
unfiltered statistic. Such an estimate is an additional arithmetic
obligation. For signed coefficients the algebraic bound
$|A(2)|\le2^r\sum_j|a_j|$ still holds, but positivity and the one-sided phase
test need separate justification. A filter with $A(2)=0$ gives an integer
finite combination of gaps independently of rationality, as O5 shows.

## O10. Requiring the lattice at every cut

Another attempted strengthening is to impose the rational carry recurrence
at every cut of a block, then count those conditions as independent
restrictions on its primes. The exact finite calculation is as follows.

**Lemma O10.** Fix positive integers $h_0,\ldots,h_{K-1}$, an odd positive
integer $d$, and put

$$
U=\sum_{j=0}^{K-1}2^{K-1-j}h_j .
$$

Given a positive integer endpoint $c_K=u$, there is an integer path
$c_0,\ldots,c_K$ satisfying $c_{j+1}=2c_j-dh_j$ exactly when

$$
u+dU\equiv0\pmod{2^K}.
\tag{O10a}
$$

If in addition the initial residue $c_0\equiv v\pmod d$ is prescribed,
where $0\le v<d$, the exact condition is the single congruence

$$
u+dU\equiv2^Kv\pmod{d2^K}.
\tag{O10b}
$$

In either case the path is unique and every $c_j$ is positive.

*Proof.* Iteration gives $u=2^Kc_0-dU$. Condition (O10a) is exactly the
integrality of $c_0=(u+dU)/2^K$; forward iteration then makes every $c_j$
an integer. Requiring that integer to be $v$ modulo $d$ gives (O10b).
Backward iteration $c_j=(c_{j+1}+dh_j)/2$ proves positivity and uniqueness.
$\square$

For a block of actual primes the putative path is $c_j=dH_{n+j}$. In a
reduced rational representation $S=a/(2^sd)$ its initial residue is
$v\equiv2^{n-s-2}a\pmod d$ at every $n\ge\max(s+2,3)$: here
$H_n-2^{n-2}S$ is an integer, since $H_3=2S-6$ and
$H_{n+1}=2H_n-h_n$. This keeps the information about the
numerator and the prime-index class that the bare lattice condition omits.

Every finite positive gap block admits positive endpoints in each allowed
class (O10b). A bound $H_{n+K}<R$ additionally restricts $u<dR$; that is real
information about the continuation. For example, (O10a) admits at most one
such endpoint when $dR<2^K$. At zero phase $U\equiv0\pmod{2^K}$, it forces
$u\ge2^K$, recovering Lemma Z2. Without a bound or an arithmetic exclusion
for the actual endpoint, the finite path supplies no contradiction.

Thus multiplying putative independent savings for its overlapping cuts is
invalid: all their integrality conditions propagate from the one initial
integer and are summarized by (O10a), or by (O10b) when its index phase is
kept. This does not exclude an upper-bound argument using primality,
consecutiveness, or quantitative restrictions on the intermediate sizes.
It identifies the input such an argument must add; no estimate excluding
these paths for the actual primes is proved here.

## Three further routes and where they stop

- **A global constraint from consecutive primality, used at single indices.**
  Proposition G is the exact pointwise form; O3 shows that its length
  $0.525\log_2p_m$ cannot be shortened with the gap bound alone.
- **Bounding all rationality-compatible configurations from above.** O6.
- **Cancelling the uncontrolled tails by combining several of them.** O5.

O9 and O10 also apply to proposed enhancements of these routes: count
original gaps after filtering, and retain the dependence among the carry
conditions before applying a counting or probabilistic estimate.

## Comparison with known theorems on consecutive primes

- **Strings of congruent primes.**
  [[../library/primes/maynard_2014_dense_clusters_primes_subsets/_index|Maynard's Theorem 3.3 on constant residue runs]]
  (arXiv:1405.2593v2; statement read, proof not checked):
  for fixed $\varepsilon>0$ and $x>x_0(\varepsilon,q)$, uniformly for
  $m\le c_\varepsilon\log\log x$, $q\le(\log x)^{1-\varepsilon}$ and
  $(a,q)=1$, the number of $p_n\le x$ with
  $p_n\equiv\dots\equiv p_{n+m}\equiv a\pmod q$ and
  $p_{n+m}-p_n\le\varepsilon\log x$ is
  $\gg_\varepsilon\pi(x)/(2q)^{\exp(Cm)}$. For fixed $m$ and $q$ this is a
  positive proportion; with $m=1$, $q=4$ it gives a positive proportion of $n$
  with $p_n\equiv p_{n+1}\pmod4$. A string of $K+1$ primes congruent modulo
  $2^{K+1}$ has the pattern $r=0$, which lies in $E_d$, so for fixed $K$ the
  theorem gives a positive proportion of mispredicted starts. Corollary D
  needs $K\ge\log_2(d\log X)+1$, where $q=2^{K+1}\ge4d\log X$ is outside the
  stated range, and inside the range the bound decays faster than every power
  of $\log x$ once $m$ is a fixed multiple of $\log\log x$. O2 shows that no
  single pattern, and no family of polylogarithmic size, can reach the
  required count under its explicitly unproved premise (U).
  [[research/prime_binary_new_attack/zero_phase_certificates|Proposition Z7 of the zero-phase analysis]]
  shows, without that premise, that the counts these cluster theorems prove
  fall short of the count needed by certificates built from a congruence and
  size bounds.
- **Mixed residue patterns.**
  [[../library/integer_sequences/kimmel_kuperberg_2024_consecutive_runs_sums_two_squares/_index|Kimmel and Kuperberg's introductory comparison with prime runs]]
  records that positive density of consecutive-prime residue patterns is
  known only for constant patterns, and that for other patterns only
  infinitude is known, for length two and $\varphi(q)=2$ (Knapowski and
  Turán).
  [[../library/primes/lau_2024_prime_residue_patterns/_index|Lau's comparison of attainable prime-residue patterns]]
  (arXiv:2409.12819v2) states in the abstract that showing that a
  single non-constant pattern of length $m$ occurs infinitely often is in
  general beyond existing methods, and proves that many block patterns occur
  infinitely often when $q$ is squarefree; those results concern occurrence,
  not density, and do not cover the moduli $4,8,16,\dots$ that the residues
  here involve. A search on
  2026-10-15 found no proof that a positive proportion of $n$ have
  $p_n\not\equiv p_{n+1}\pmod4$. The
  [[research/prime_binary_new_attack/residue_switch_moments|moment analysis]]
  distinguishes an aggregate switch count from a specified nonconstant
  pattern: the inspected unconditional inputs give a positive proportion
  of switches for fixed $q$ with $\varphi(q)>8$. A uniform pair constant
  $4$ would lower this sufficient threshold to $\varphi(q)>4$, but
  requires a separate source interface. Neither bound supplies the
  modulo-$4$ switches needed by the $j=0$ overlap condition in part 2
  of Theorem F; that theorem also requires growing block length.
- **Small gaps.**
  [[../library/primes/goldston_pintz_yildirim_2011_small_prime_gaps/_index|Goldston, Pintz and Yıldırım's positive-proportion theorem]]
  (arXiv:1103.3986v1; statement comparison, proof not checked): a positive
  proportion of gaps are
  below any fixed fraction of the mean. It concerns the size of one gap, with
  no residue information.
- **Growing denominators.** For a series $\sum p_n/(a_1\cdots a_n)$,
  [[../library/irrationality/hancl_2004_irrationality_cantor_series/theorem_6_1|Hančl and Tijdeman's Theorem 6.1]]
  assumes monotonicity and $a_n/\log n\to\infty$. Its proof uses blocks of
  $O(\log n)$ terms and differences of tails. Relative domination by a first
  term would not itself give the absolute precision needed for a lattice
  certificate. The hypothesis excludes $a_n=2$; no one-term substitute for
  the present missing estimate follows from this theorem.
