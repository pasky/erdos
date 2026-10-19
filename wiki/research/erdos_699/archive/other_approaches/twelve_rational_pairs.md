---
name: research/erdos_699/archive/other_approaches/twelve_rational_pairs
title: "Erdős 699: two additional prime-power seeds for index 12"
desc: "The seeds 49−3·16=1 and 13·512−5·1331=1 give effective rational-block restrictions excluding three remaining exploratory cofactor boxes."
created: 2026-09-22T06:08:34Z
updated: 2026-09-22T19:12:28Z
---

# Erdős 699: two additional prime-power seeds for index 12

***

This is a retained earlier research note. The [[research/erdos_699/_index|current reading guide]] gives the latest status and distinguishes completed proofs from remaining cases.

The [rational-block inequality](../../methods/details/bft_rational_blocks.md)
can use coefficients other than one in a Padé seed. Two useful choices are

$$
7^2-3\cdot2^4=1,\qquad13\cdot2^9-5\cdot11^3=1.
$$

Theorem 2.4 of BFT permits arbitrary positive integer coefficients $a,b$.
They need not be powers of either prime. Their contribution is already
included in the definitions of $\Omega_3$ and $\Omega_4$.

Fix a gap bound $D\ge1$, and write

$$
|p^ku-q^lv|\le D,\qquad x=\min(p^ku,q^lv),
$$

$$
e_p=\frac{\log u}{\log x},\qquad e_q=\frac{\log v}{\log x}.
$$

For a seed $P=p^{k_0},Q=q^{l_0}$ in either order, put

$$C=\frac{\log\Omega_3}{s},\qquad
K=\log\max(P,Q)+\frac{\log\Omega_4}{s},\qquad J=K-C.$$

Above an effective threshold, the rational-block inequality requires

$$(k_0\log p-J(1-e_p))_+
 +(l_0\log q-J(1-e_q))_+>C-\epsilon.$$

The following three choices give strict contradictions throughout the
indicated closed boxes. Here $\ell=\log L_1$ is an exact rational number,
and the displayed margin is $C$ minus the sum of the two positive parts
at the upper corner of the box. Monotonicity then handles every smaller
cofactor exponent.

| Seed | $s$ | $\ell$ | Upper bounds | Certified margin greater than |
|---|---:|---:|---|---:|
| $49-3\cdot16=1$ | $61/33$ | $577/1000$ | $e_2\le.2773$, $e_7\le.0295$ | $.24528449$ |
| $49-3\cdot16=1$ | $70/37$ | $609/1000$ | $e_2\le.2773$, $e_7\le0$ | $.32021006$ |
| $13\cdot512-5\cdot1331=1$ | $37/16$ | $121/200$ | $e_2\le.14$, $e_{11}\le0$ | $.48191326$ |

One may take $\epsilon=.24,.32,.48$, respectively. The directed interval
calculation verifies $\Omega_3,\Omega_4>1$, $J>0$, $1<s<1/z_0$, and
$\ell<\log L(s)$ in each case. The strict final inequality supplies an
effective coefficient-gcd starting point by BFT Theorem 2.2. Thus these
are effective restrictions, even though their numerical height thresholds
have not been evaluated here.

## Ordinary cofactor alternatives

The same two seeds also give the simpler alternatives from the
[asymmetric matched-block argument](../../methods/details/asymmetric_cofactors.md).
For each prime power $p^{k_0}$ in a seed, its limiting endpoint is

$$
\alpha_p=1-\frac{k_0\log p}{K}.
$$

A stronger ordinary alternative comes from the first seed with
$s=53/31$ and $\ell=255299/500000=.510598$. Its endpoints are

$$\alpha_2=.37560690082818396\ldots,\qquad
\alpha_7=.12355347987060026\ldots.$$

Thus, above an effective height threshold,

$$
\boxed{u_2>x^{.375}\quad\text{or}\quad u_7>x^{.123}.}
$$

The directed interval calculation gives
$\log\Omega_3>.0007025768$ and
$\log L(53/31)>.5105995243>\ell$, so all required inequalities
remain strict despite the small gap in $\Omega_3>1$.

For comparison, the first seed with $s=61/33$ and $\ell=.577$ gives

$$\alpha_2=.3485929600297605\ldots,\qquad
\alpha_7=.08563462003828685\ldots.$$

Consequently, above an effective height threshold,

$$
\boxed{u_2>x^{.348}\quad\text{or}\quad u_7>x^{.085}.}
$$

For the second seed, taking $s=80/39$ and
$\ell=347257/500000=.694514$ gives the stronger endpoints

$$\alpha_2=.24848491362569955\ldots,\qquad
\alpha_{11}=.13339498277126851\ldots.$$

Thus one also has the effective alternative

$$
\boxed{u_2>x^{.248}\quad\text{or}\quad u_{11}>x^{.133}.}
$$

The checker certifies $\log\Omega_3>0$ and
$\ell<\log L(80/39)$; the strict rational-block margin at this box
exceeds $.00000922$.

The earlier parameters $s=37/16$ and $\ell=.605$ give

$$\alpha_2=.1935369055356310\ldots,\qquad
\alpha_{11}=.07003202391529480\ldots.$$

It therefore gives the effective alternative

$$
\boxed{u_2>x^{.193}\quad\text{or}\quad u_{11}>x^{.069}.}
$$

Here $u_p$ denotes the positive integer cofactor of the relevant prime
power in two positive integers whose difference is bounded by $D$; $x$
is their minimum. The retained checker certifies all exact rational
endpoint targets. These ordinary alternatives suffice wherever only an
OR condition on individual cofactor exponents is needed.

These boxes arose from the remaining index-12 interpolation profiles, in
prime order $2,3,5,7,11$:

$$(.2773,.3454,.3941,.0295,0),\qquad
(.2773,.3641,.3941,0,.0212),\qquad
(.14,.3454,.2715,.3255,0).$$

The calculation in this note excludes those boxes. A proof for a whole
index additionally needs complete coverage of all cofactor and position
cases and the corresponding interpolation certificates.

The retained [checker](../../computations/erdos_699_twelve_rational_pairs.py)
and [interval output](../../computations/erdos_699_twelve_rational_pairs.json)
contain the exact seeds and parameters. They can be reproduced with

```sh
.venv/bin/python wiki/research/erdos_699/computations/erdos_699_twelve_rational_pairs.py
```
