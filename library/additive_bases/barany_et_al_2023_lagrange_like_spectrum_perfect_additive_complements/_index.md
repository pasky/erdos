---
name: additive_bases/barany_et_al_2023_lagrange_like_spectrum_perfect_additive_complements
title: "Bárány et al.: Lagrange-like spectrum of perfect additive complements"
desc: |
  Proves that the set of limsup values of A(x)B(x)/x over perfect additive
  complements is closed, describes its discrete part below the first
  accumulation point, and locates an interval it contains and one it misses.
license: CC-BY-4.0
created: 2026-09-21T00:00:00Z
updated: 2026-10-13T04:56:43Z
---

# Bárány et al.: Lagrange-like spectrum of perfect additive complements

[[additive_bases/_index|..]]

***

[Full paper in Markdown](barany_et_al_2023_lagrange_like_spectrum_perfect_additive_complements.md).
The arXiv record (https://arxiv.org/abs/2301.04365, read 2026-10-02) names the
Creative Commons Attribution 4.0 license.

Balázs Bárány, Jin-Hui Fang, Csaba Sándor, "Lagrange-like spectrum of perfect
additive complements," arXiv:2301.04365 (2023); published in Acta Arith. 212
(2024), 269--287, DOI 10.4064/aa230224-10-10. The copy read for this card is
the arXiv version dated October 11, 2023.

## Overview

The paper studies the possible normalized counting-function growth of *perfect
additive complements*: infinite sets $A,B\subseteq\mathbb Z_{\ge 0}$ satisfying
$r_{A,B}(n)=1$ for every $n\ge0$. Its object is

$$
\mathfrak L=\left\{\limsup_{x\to\infty}\frac{A(x)B(x)}x:(A,B)\text{ are perfect additive complements}\right\},
$$

expressed parametrically in the paper as $\limsup_k 2/(1+D_k)$. The mixed-radix
classification (1.1) is quoted as **Theorem A** from [5, Theorem 1.1], rather
than proved here. Likewise, **Theorem B**, quoted from [12, Lemma 2.1], gives

$$
\limsup_{x\to\infty}\frac{A(x)B(x)}x=\limsup_{k\to\infty}\frac{2}{1+D_k},\qquad D_k=\frac1{m_k}-\frac1{m_km_{k-1}}+\cdots+\frac{(-1)^{k-1}}{m_k\cdots m_1};
$$

see equations (1.1)–(1.2). Thus the paper’s new problem is the structure of the
set of these limsup values, not the classification of perfect complements
itself.

The principal result is **Theorem 1.1**. It proves that $\mathfrak L$ is closed;
identifies its smallest accumulation point $\gamma_0\approx1.62688284$; and
describes the spectrum below it as a strictly increasing explicit sequence

$$
\frac32=\gamma_1<\frac85=\gamma_2<\frac{13}8=\gamma_3<\frac{109}{67}=\gamma_4<\cdots\to\gamma_0.
$$

It also proves $[7/4,2]\subseteq\mathfrak L$, while
$[12/7-\delta,2]\not\subseteq\mathfrak L$ for every $\delta>0$, and establishes
that $[3/2,17/10]\cap\mathfrak L$ has Lebesgue measure zero. The exact lower
endpoint $c_0=\inf\{c:[c,2]\subseteq\mathfrak L\}$ remains open between $12/7$
and $7/4$; see **Problem 1.2**. Dimension and continuity questions are posed in
**Problem 1.3**.

The main reduction appears in Section 2. With $T_m(x)=(1-x)/m$, one has
$D_k=T_{m_k}\circ\cdots\circ T_{m_1}(0)$. Defining

$$
\mathcal L=\left\{\liminf_kT_{m_k}\circ\cdots\circ T_{m_1}(0):(m_i)\in\mathbb Z_{\ge2}^{\mathbb Z^+}\right\},
$$

equation (2.3) gives $\mathfrak L=g(\mathcal L)$ for $g(x)=2/(1+x)$. The
conjugate maps $\widehat G_m=g\circ T_m\circ g^{-1}$ yield the IFS
representation (1.3). Theorems 2.1–2.5 are the corresponding statements for
$\mathcal L$: closedness (**Theorem 2.1**), the interval
$[0,1/7]\subseteq\mathcal L$ (**Theorem 2.2**), explicit gaps accumulating at
$1/6$ (**Theorem 2.3**), measure zero on $[3/17,1/3]$ (**Theorem 2.4**), and the
discrete portion above the first accumulation point (**Theorem 2.5**).

Section 3 proves **Theorem 2.1** by concatenating increasingly long blocks from
sequences realizing convergent spectral values; estimates (3.2)–(3.3) ensure
that the resulting sequence has the desired liminf, as asserted in (3.1).
Section 4 treats the interval and gap results. The attractor of
$\{T_2,T_3,T_4\}$ is $[1/7,3/7]$ by (4.1); Lemmas 4.1–4.2 and the block
construction following (4.2) prove **Theorem 2.2**. Lemma 4.3 restricts possible
liminf values according to the symbols occurring infinitely often, while Lemma
4.4 and estimates (4.4)–(4.8) produce the gaps of **Theorem 2.3**.

Section 5 constructs words $M^{(1)}=2$, $M^{(2)}=3$, and
$M^{(n)}=M^{(n-1)}M^{(n-2)}M^{(n-2)}$ in (5.5). If
$\lambda_n=\operatorname{Fix}(T_{M^{(n)}})$, then $\lambda_n$ decreases to
$\lambda_0=\Pi(M)=0.2293\ldots$. Proposition 5.3 proves
$\lambda_n,\lambda_0\in\mathcal L$, using the cyclic-word ordering in Lemma 5.5;
Proposition 5.6 excludes every interval $(\lambda_{n+1},\lambda_n)$ and all
values above $\lambda_1$. Together these prove **Theorem 2.5**, and applying the
decreasing map $g$ gives the sequence $\gamma_n=g(\lambda_n)$ in **Theorem
1.1(2)**. Finally, Section 6 excludes the recurring block $(4,2)$ above $3/17$,
embeds the remaining possibilities in a 55-map finite IFS, and applies the
contraction-sum criterion of Lemma 2.1 to prove **Theorem 2.4**.

## Relation to E1145

This source bears on [[../wiki/problems/additive_bases/E1145/_index|Problem 1145]].

For E1145, $1_A*1_B(n)$ is exactly the paper’s representation function
$r_{A,B}(n)$. Consequently, every perfect complement in the paper would become a
counterexample to E1145 if it also satisfied the balance condition on
corresponding ordered elements.

More precisely, let $A_0,B_0\subseteq\mathbb Z_{\ge0}$ be a pair of the form
(1.1), and put

$$
A=A_0+1,\qquad B=B_0+1.
$$

Then $A,B\subseteq\mathbb Z^+$ and

$$
1_A*1_B(n)=r_{A_0,B_0}(n-2)=1\qquad(n\ge2).
$$

Thus $A+B$ contains every integer at least $2$, while $\limsup_n1_A*1_B(n)=1$.
If $A_0=\{\alpha_1<\alpha_2<\cdots\}$ and $B_0=\{\beta_1<\beta_2<\cdots\}$, the
remaining E1145 hypothesis is precisely

$$
\frac{\alpha_n+1}{\beta_n+1}\longrightarrow1,
$$

or equivalently $\alpha_n/\beta_n\to1$. The paper neither constructs a radix
sequence $(m_i)$ with this property nor proves that none exists. This is the
decisive missing step, so its perfect-complement constructions do not resolve
E1145.

The most directly usable reduction is the cited mixed-radix classification,
**Theorem A / equation (1.1)**: any attempt to refute E1145 using unique
representations may be reduced to asking whether the two digit sets in (1.1),
possibly interchanged, can have asymptotically equal $n$th elements. Conversely,
ruling out $\alpha_n/\beta_n\to1$ for every such radix sequence would eliminate
all perfect-complement counterexamples, though not counterexamples with another
fixed representation bound.

**Theorem B** and equation (2.3) provide only a coarser invariant. For the
shifted pair above, the shift does not alter

$$
\limsup_{x\to\infty}\frac{A(x)B(x)}x\in\mathfrak L.
$$

Hence this limsup lies in $[3/2,2]$, with the finer interval, gap, closedness,
and measure restrictions of **Theorem 1.1**. These results constrain the product
of the two counting functions, but E1145’s condition compares their inverse
counting functions at the same index. No theorem in the paper controls the
quotient $\alpha_n/\beta_n$, derives balance from $A(x)B(x)$, or converts
balance into repeated sums.

The IFS formalism $D_k=T_{m_k}\circ\cdots\circ T_{m_1}(0)$ could be adapted
hypothetically if the ratio of the two ordered digit sets were encoded by an
additional dynamical observable. In the present paper, however, the IFS tracks
only the normalized product $A(x)B(x)/x$. The paper therefore supplies a sharp
model class and useful necessary spectral tests for a perfect-representation
counterexample, but proves neither the assertion of E1145 nor a counterexample
satisfying its balance hypothesis.
