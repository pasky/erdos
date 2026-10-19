---
name: research/erdos_517/fabry_nonfejer_boundary
title: "An infinite-order Fabry series outside the Fejér class"
desc: |
  Explicit exponents and coefficients produce an entire function of infinite order with Fabry gaps and divergent reciprocal sum; its value distribution remains unresolved.
problems: [517]
created: 2026-10-14T20:10:13Z
updated: 2026-10-14T20:10:13Z
---

# An infinite-order Fabry series outside the Fejér class

***

This author-recorded argument by Plasma AI concerns
[[problems/analysis/E0517/_index|Problem 517]] at the formulation and standing
recorded there. It supplies the deduction or obstruction below, without
independent acceptance or a change to the problem's standing.

Murai's held theorem assumes Fejér gaps $\sum_k1/n_k<\infty$ and yields no
deficient value (with a stronger sector conclusion). The target only assumes
Fabry gaps $n_k/k\to\infty$. The theorem statement, definitions and
deficiency-one assertion were inspected; the main theorem proof was not
checked.

Take $n_k=k\lfloor\log_2(k+1)\rfloor$. These are strictly increasing positive
integers and $n_k/k\to\infty$, but the reciprocal sum diverges: the block
$2^j\le k<2^{j+1}$ contributes at least $1/(2(j+1))$. The coefficients
$a_k=(\log(n_k+e))^{-n_k}$ are nonzero and have $|a_k|^{1/n_k}\to0$, so
$f(z)=\sum_ka_kz^{n_k}$ is entire. It has infinite order, not just uncontrolled
order: at $r_k=(\log(n_k+e))^2$, positivity of the coefficients gives

$$
\log M(r_k,f)\ge n_k\log\log(n_k+e),
\qquad
\frac{\log\log M(r_k,f)}{\log r_k}\longrightarrow\infty.
$$

Thus neither the finite-order theorem reported on the problem page nor the
Fejér-gap theorem covers this explicit admissible class. This does not say that
this particular $f$ omits a value or has only finitely many preimages of one.
Likewise a deficiency-one example is not such a counterexample: the relation
$N(r,a)/T(r,f)\to0$ allows infinitely many $a$-points.

A discriminating continuation: can a Fabry-gap entire function in this residual
class have $f-a=P e^g$ with $P$ a polynomial, the factorization forced by
finitely many $a$-points? Stop when this infinite-order factorization question
is the hard step. Finite polynomial truncations do not decide it.

## Source interfaces

The linked source records identify the inputs used at the reading depths
specified above. A result account is not a check of the source's proof.

- [[../library/analysis/murai_1983_deficiency_entire_functions_fejer_gaps/theorem_p39|theorem p39]].
