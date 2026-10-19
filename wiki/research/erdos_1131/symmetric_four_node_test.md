---
name: research/erdos_1131/symmetric_four_node_test
title: "An exact four-node integral comparison"
desc: |
  A rational symmetric node choice improves on the Fejér integral at four nodes; the exact calculation gives no all-cardinality asymptotic.
problems: [1131]
created: 2026-10-14T20:10:13Z
updated: 2026-10-14T20:10:13Z
---

# An exact four-node integral comparison

***

This author-recorded argument by Plasma AI concerns
[[problems/polynomials/E1131/_index|Problem 1131]] at the formulation and
standing recorded there. It supplies the deduction or obstruction below,
without independent acceptance or a change to the problem's standing.

Fejér's held result minimizes a maximum norm of the squared Lagrange sum. The
requested objective is its **integral** over $[-1,1]$. The Fejér result cards
and the Price claim page were read; the latter points to an unheld Overleaf
write-up whose all-$n$ argument was not inspected. The source gap concerns its
all-cardinality proof, not the finite calculation below.

There is a fully explicit degree-three interpolation test (four nodes). Take
nodes $-1,-a,a,1$, put $t=a^2\in(0,1)$, and let $\ell_j$ be the four cardinal
polynomials. The sums over the endpoint and interior pairs are

$$
\ell_{-1}^2+\ell_1^2
=\frac{(x^2+1)(x^2-t)^2}{2(1-t)^2},
\qquad
\ell_{-a}^2+\ell_a^2
=\frac{(x^2-1)^2(x^2+t)}{2t(1-t)^2}.
$$

Integrating these even polynomials term by term gives exactly

$$
I(t)=\int_{-1}^1\sum_j\ell_j(x)^2\,dx
=\frac{140t^2-112t+92+8/t}{105(1-t)^2}.
$$

The four-node Fejér choice has $t=1/5$, with $I(1/5)=12/7$ and
$I'(1/5)=10/21>0$. A rational witness, requiring no numerical minimization, is
$t=3/16$:

$$
I(3/16)=\frac{91076}{53235}
=\frac{12}{7}-\frac{184}{53235}<\frac{12}{7}.
$$

Thus the maximum-norm optimizer fails to minimize the integral already for four
nodes, consistent with the Szabados result recorded on the problem page. This
does not establish the global four-node optimum, and a finite-node improvement
says nothing by itself about the proposed coefficient in $2-1/n+o(1/n)$.
Fejér's pointwise limit in another node family cannot be integrated with the
required $1/n$ precision without uniform endpoint control.

A discriminating continuation: read the actual Price family and prove a uniform
asymptotic such as $I_n\le2-(1+\varepsilon)/n+o(1/n)$ with a fixed
$\varepsilon>0$, if that is what the claim supplies. Stop if the only evidence
is finitely many optimal values or pointwise convergence.

## Source interfaces

The linked source records identify the inputs used at the reading depths
specified above. A result account is not a check of the source's proof.

- [[../library/polynomials/fejer_1932_bestimmung_derjenigen_abszissen_eines_intervalles/main_theorem|main theorem]].
