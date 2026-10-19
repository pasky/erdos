---
name: research/erdos_774/evidence/voltage_parity_checks
title: Finite checks of inversion-parity certificates for voltage covers
desc: An exact witness refutes a proposed nonzero-XOR tensor certificate on K_{3,3}, and eight prescribed cofactor multipliers are recorded; neither is a theorem about arbitrary multipliers or colorings.
tags: [E0774, computational, finite, incomplete]
sources: []
created: 2026-09-24T23:30:00Z
updated: 2026-10-13T05:28:09Z
---

# Finite checks of inversion-parity certificates for voltage covers

[[research/erdos_774/evidence/_index|..]]

***

Both records concern the inversion-parity mechanism of
[generic voltage coloring](../routes/generic_voltage_coloring.md). They
are finite computational observations; no script is retained, and the
exact witness below is verified by the displayed algebra.

## A bounded tensor certificate test

Exactly $3^9=19683$ assignments of nonzero vectors $\delta_{ij}\in\mathbb F_2^2$
to the nine edges of $K_{3,3}$ were examined. The proposed certificate was
nonvanishing of

$$
\sum_{i<k,\ j>l}\delta_{ij}\otimes\delta_{kl}.
$$

The reported enumeration gave 432 zero tensors. An exact witness, with
$a=(1,0)$, $b=(0,1)$, is

$$
\begin{pmatrix}a&a&b\\a&a&a+b\\b&a+b&a\end{pmatrix}.
$$

Its nine inversion terms reduce, after canceling repeated terms, to

$$
a\otimes a+b\otimes b+b\otimes(a+b)
 +(a+b)\otimes b+(a+b)\otimes(a+b)=0.
$$

This verifies the needed counterexample without depending on the reported
count. It is realizable by $f(0)=0$, $f(1)=a$, $f(2)=b$ on $\mathbb Z/3$
with origin matrix
$\begin{pmatrix}0&0&2\\0&0&1\\2&1&0\end{pmatrix}$. The six resulting
four-bit colors are not all equal. Thus this refutes the proposed
**nonzero-XOR certificate**, not the full four-bit coloring construction.
The test stopped at its finite range and was not enlarged to classify that
different question.

## Eight prescribed multiplier checks

One bounded probe used the complete $3\times4$ symbolic matrix
$M_{xv}=X_{xv}$ in the integer group ring of $(\mathbb Z/2)^{12}$, with
incidences ordered row-major. Products add exponent masks by XOR. For
$j=0,1,2,3$, let $C_j$ be the increasing list of column indices other than
$j$, and define

$$
p_j=(-1)^j\sum_{\pi\in S_3}\operatorname{sgn}(\pi)
                 \prod_{x=0}^2X_{x,C_j[\pi(x)]}.
$$

The kernel vector was $p=(p_0,p_1,p_2,p_3)$. Exactly eight multipliers
$f$ were tested: the four $p_j$ and the four unsigned polynomials obtained
by replacing all six coefficients of $p_j$ by $+1$. Each test collected all
monomials of all four coordinates $p_if$, discarding zero coefficients.
The reported support sizes were

| Multiplier | Four support sizes |
|---|---|
| $p_0$ | 16,30,30,30 |
| unsigned $p_0$ | 6,24,24,24 |
| $p_1$ | 30,16,30,30 |
| unsigned $p_1$ | 24,6,24,24 |
| $p_2$ | 30,30,16,30 |
| unsigned $p_2$ | 24,24,6,24 |
| $p_3$ | 30,30,30,16 |
| unsigned $p_3$ | 24,24,24,6 |

In all eight cases the common coefficient gcd was one, the vector was
nonflat, and its support met both values of the inversion-parity coloring
$Q(g)=\sum_{x<y,v>w}g_{xv}g_{yw}$ modulo two. These are finite
computational observations about these eight untranslated products, not a
theorem about arbitrary multipliers. The complete-support base has
repeated columns, so the probe concerns formal cofactor algebra, not a
proposed set of distinct frequencies. No search beyond those eight
products was performed.
