---
name: research/leads/restricted_difference_basis_limit
title: Endpoint patches for restricted difference bases
desc: A corrected Singer-lift covering argument proves convergence while leaving the exact sparse-ruler constant undetermined.
problems: [170]
research_state: blocked
review_status: unreviewed
created: 2026-10-14T20:10:13Z
updated: 2026-10-14T20:10:13Z
---

# Endpoint patches for restricted difference bases

[[research/leads/_index|..]]

***

[[problems/additive_combinatorics/E0170/_index|Problem 170]] asks for the
value of the limit of $F(N)/\sqrt N$, where the marks of the difference
basis must all lie in $[0,N]$. The
[[../library/additive_combinatorics/erdos_1948_representation_1/theorem_p1155|Erdős–Gál covering argument]]
lifts a small ruler by a Singer difference set modulo $q=p^2+p+1$.
Its modular carry proves coverage through $nq$. The remainder written as
$M=N-(n+1)q$ does not measure the entire interval still requiring coverage.
This is a defect in the printed argument, not in its transcription.

[[theory/additive_combinatorics/L38_restricted_difference_basis_convergence/_index|L38]]
supplies the missing coverage using $\Delta=N-nq$ and at most
$2\sqrt\Delta+4$ extra marks. It proves, at author-recorded tier 0,

$$
\lim_{N\to\infty}\frac{F(N)}{\sqrt N}
=\inf_{n\ge1}\frac{F(n)+2}{\sqrt{n+1}}.
$$

Singer's theorem and the prime number theorem are exact external inputs,
used at statement level. The proof keeps the mark restriction, handles the
carry at $nq$, and takes the large-$N$ limit before varying $n$.

The exact value remains open in this account. In particular, this deduction
does not prove the printed infimum $\inf_nF(n)/\sqrt n$, the numerical
upper bound derived from that different formula, or the conjectural value
$\sqrt3$. A route to the exact constant needs a matching asymptotic lower
bound or a construction below the conjectured value. Repeating the
convergence argument or extending a finite ruler table does not supply either.

The useful bounded check is examination of L38's carry, endpoint placement
and limiting order. Reopening the constant problem requires a new estimate
that addresses that value, rather than a further convergence calculation.
