---
name: research/erdos_699/proofs/details/index_9_nonvanishing
title: "Erdős 699: arithmetic nonvanishing for the two largest index-nine kernels"
desc: "Local certificates modulo 251 remove the common-zero thresholds for round3_000 and round3_001 without increasing their polynomial degrees."
created: 2026-09-22T16:48:00Z
updated: 2026-09-22T19:12:28Z
---

# Erdős 699: arithmetic nonvanishing for the two largest index-nine kernels

[[research/erdos_699/_index|P699 research]] ·
[[research/erdos_699/proofs/details/index_9_effective|The index-nine argument]] ·
[[research/erdos_699/proofs/details/index_7_nonvanishing|The local arithmetic nonvanishing proof]]

***

The common-zero thresholds for the polynomial certificates `round3_000`
and `round3_001` can both be removed. Their degrees and prescribed
multiplicities remain unchanged. The coefficient estimates, source
thresholds, and other common-zero thresholds are separate parts of the
index-nine argument.

The proof uses the elementary $251$-adic argument in the linked
index-seven note: check all common residue points of two modular
sections, use another section where necessary, and examine the tangent
forms at each prescribed grid point. At an odd-multiplicity diagonal
point symmetry forces the tangent $U+V=0$; an invertible matrix of the
next linear terms excludes that direction as well.

## Exact data

The [retained certificate](../../computations/erdos_699_index_9_nonvanishing.json)
contains the kernel vectors and local matrices. The
[checker](../../computations/erdos_699_index_9_nonvanishing.py)
checks their jets, their independence, all residue points over
$\mathbf F_{251}$, and the tangent calculations. It does not repeat
either large jet rank computation or enumerate binomial rows.

| Certificate | Residual degree | Jet matrix | Kernel dimension | Sections used |
|---|---:|---:|---:|---:|
| `round3_000` | 243 | $15003\times15006$ | 3 | 3 |
| `round3_001` | 270 | $18494\times18496$ | 2 | 2 |

Both prescribed supports contain 43 points. For `round3_000`, the first
two sections have only two additional common residue points,
$(29,112)$ and $(112,29)$. The newly retained third section has value 84
at both. For `round3_001`, the two existing sections already have no
common residue point outside their support.

The tangent forms are coprime except at the following diagonal points.
The matrices give the next linear terms in
$t=U$, $w=(U+V)/U$ after dividing by $t^R$.

| Certificate | Point | Multiplicity $R$ | Matrix modulo 251 | Determinant |
|---|---|---:|---|---:|
| `round3_000` | $(0,0)$ | 29 | $\left(\begin{smallmatrix}72&248\\108&188\end{smallmatrix}\right)$ | 55 |
| `round3_000` | $(1,1)$ | 25 | $\left(\begin{smallmatrix}155&148\\66&176\end{smallmatrix}\right)$ | 193 |
| `round3_000` | $(3,3)$ | 37 | $\left(\begin{smallmatrix}213&197\\58&224\end{smallmatrix}\right)$ | 142 |
| `round3_000` | $(4,4)$ | 59 | $\left(\begin{smallmatrix}179&161\\155&38\end{smallmatrix}\right)$ | 170 |
| `round3_001` | $(1,1)$ | 29 | $\left(\begin{smallmatrix}111&124\\180&56\end{smallmatrix}\right)$ | 211 |
| `round3_001` | $(4,4)$ | 65 | $\left(\begin{smallmatrix}74&248\\79&230\end{smallmatrix}\right)$ | 189 |

All determinants are nonzero. The constant terms of these strict
transforms vanish exactly for symmetric lifts, since every displayed
$R$ is odd. Therefore the same minimum-valuation argument as for
index seven excludes every nonzero displacement in
$251\mathbf Z_{251}^2$.

## Consequence and lifting

The retained full row ranks provide maximal jet minors invertible over
$\mathbf Z_{(251)}$. Every selected modular section consequently lifts
to a symmetric rational section, with denominators prime to 251 and
with the prescribed jets exactly. For either certificate, the common
zeros of the selected lifts in $\mathbf Z_{251}^2$ are precisely the
43 support points. In particular, at least one section is nonzero at
every physical integer point $(j,n-j)$ for index nine.

Integral monic Newton basis changes are unimodular and preserve this
lifting argument, so the certificate is compatible with coefficient
bounds in those bases. The assertion here concerns arithmetic zeros;
it does not assert that the geometric base locus is empty over an
algebraic closure.

The two common-zero contributions may thus be set to zero when combining
the numerical thresholds. No additional polynomial degree is needed.
