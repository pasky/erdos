---
name: analysis/pendyala_2026_radial_access_lemniscates/theorem_6_2
title: "Theorem 6.2 (p. 9): an explicit degree-six polynomial with zeros inside the disk blocks every radius"
desc: |
  Pendyala's degree-six obstruction, as claimed in an unrefereed preprint
  with a rational certificate: the monic polynomial with double zeros at
  -rho e^{2 pi i 927/960} and -rho e^{2 pi i 317/960} and simple zeros at
  -rho e^{2 pi i 697/960} and -rho e^{2 pi i 547/960}, rho = 1999999/2000000,
  has modulus greater than 1 somewhere on every radius, so the worst-case
  shortest escape length S(6) exceeds 1.
created: 2026-10-14T22:51:14Z
updated: 2026-10-14T22:51:14Z
---

***

**Source.** Section 6, pp. 8--10, with Lemma 6.1 and Theorem 6.2 on p. 9 and
Remark 6.4 on p. 10, and Appendix A, pp. 10--14, of Venkata Siddharth
Pendyala, *Radial access for polynomial lemniscates: the cubic theorem and a
degree-six obstruction*, SSRN preprint (2026), doi:10.2139/ssrn.6850818, the
edition named on the
[[analysis/pendyala_2026_radial_access_lemniscates/_index|source card]].

## Statement

Admissible polynomials, safe radii, $\Delta$, $\mathcal B$ and $N^*$ are as
on the
[[analysis/pendyala_2026_radial_access_lemniscates/theorem_1_1|Theorem 1.1 page]].

**The polynomial** (pp. 8--9). Let

$$
\rho=\frac{1999999}{2000000},\qquad S=(927,927,317,317,697,547),\qquad
q_\rho(z)=\prod_{s\in S}\bigl(\rho+e^{-2\pi is/960}z\bigr),
$$

the product running over $S$ with its repetitions, so that

$$
q_\rho(z)=\bigl(\rho+e^{-2\pi i\,927/960}z\bigr)^2\bigl(\rho+e^{-2\pi i\,317/960}z\bigr)^2
\bigl(\rho+e^{-2\pi i\,697/960}z\bigr)\bigl(\rho+e^{-2\pi i\,547/960}z\bigr).
$$

Its leading coefficient is
$\prod_{s\in S}e^{-2\pi is/960}=e^{-2\pi i\,3732/960}=e^{-2\pi i\,71/80}$, so

$$
P_\rho(z)=e^{2\pi i\,71/80}\,q_\rho(z)
$$

is monic of degree six, and $|P_\rho|=|q_\rho|$. Its zeros are
$-\rho e^{2\pi is/960}$ for $s\in S$: double at $s=927$ and $s=317$, simple
at $s=697$ and $s=547$, all of modulus $\rho<1$; and $|P_\rho(0)|=\rho^6<1$.
As fractions of a turn, their directions are $447/960$ and $797/960$ for the
double zeros and $217/960$ and $67/960$ for the simple ones, the four
directions Remark 6.4 names (p. 10). For $z=re^{2\pi iu}$ the paper's (6.1)
is

$$
|q_\rho(re^{2\pi iu})|^2=\prod_{s\in S}\Bigl(\rho^2+r^2+2\rho r\cos2\pi\bigl(u-\tfrac{s}{960}\bigr)\Bigr).
$$

**Lemma 6.1** (Three-radius certificate, p. 9). Let $R=\{1,1/300,439/1000\}$.
For every $u\in[0,1]$,

$$
\max_{r\in R}\lvert q_\rho(re^{2\pi iu})\rvert>1,
$$

and, more quantitatively,

$$
\min_{0\le u\le1}\ \max_{r\in R}\lvert q_\rho(re^{2\pi iu})\rvert^2>1+2.327036066010500056098356\cdot10^{-6}.
$$

**Theorem 6.2** (Strict degree-six radial obstruction, p. 9). There is a
monic polynomial $P_\rho$ of degree six, with all its zeros in the open disk
$\mathbb D$, such that

$$
\min_{\theta\in\mathbb R}\ \max_{0\le r\le1}\lvert P_\rho(re^{i\theta})\rvert>1 .
$$

Consequently $N^*\le6$. The polynomial is the $P_\rho$ above: every radius
carries a point at distance $1$, $1/300$ or $439/1000$ from $0$ where
$|P_\rho|>1$, so no radius is safe, $\mathcal B(P_\rho)>1$, and Proposition
2.2 gives $\Delta(P_\rho)>0$ (p. 10).

## The certificate

Appendix A (pp. 10--12) states the certificate for Lemma 6.1 as a finite
datum and checks it by rational inequalities.

- Intervals. $[0,1]$ is cut into $I_j=[j/8192,(j+1)/8192]$ for
  $0\le j<8192$, and each $I_j$ gets a radius $r_j\in R$ from Table 1
  (p. 11), which the paper calls the certificate; no search or numerical
  optimization enters the check.
- Table 1, the blocks of $j$ with their radius: $0$ to $363$, radius $1$;
  $364$ to $795$, $439/1000$; $796$ to $1627$, $1$; $1628$ to $2058$,
  $439/1000$; $2059$ to $3317$, $1$; $3318$ to $4260$, $1/300$; $4261$ to
  $6353$, $1$; $6354$ to $7296$, $1/300$; $7297$ to $8191$, $1$. The outer
  radius $1$ blocks every direction except four short corridors centered at
  the zero directions; the middle radius $439/1000$ closes the corridors at
  $67/960$ and $217/960$ of the simple zeros, and the inner radius $1/300$
  those at $447/960$ and $797/960$ of the double zeros (Remark 6.4, p. 10).
- Cosine bound. For a phase $s$ let $J_{j,s}=I_j-s/960$ and let
  $\delta_{j,s}$ be the distance from $J_{j,s}$ to $\mathbb Z+1/2$. If
  $\delta_{j,s}=0$ then $c_{j,s}=-1$; otherwise
  $c_{j,s}=\max\{-1,-U(2\pi_0\delta_{j,s})\}$, with
  $\pi_0=103993/33102<\pi$ and
  $U(x)=\sum_{k=0}^{10}(-1)^kx^{2k}/(2k)!+x^{21}/21!$. Each $c_{j,s}$ is
  rational, and $\cos2\pi(u-s/960)\ge c_{j,s}$ for $u\in I_j$, the paper's
  (A.1).
- Inequalities. With multiplicities
  $(m_{927},m_{317},m_{697},m_{547})=(2,2,1,1)$, let
  $M_j=\prod_{s\in\{927,317,697,547\}}\max\{0,\rho^2+r_j^2+2\rho r_jc_{j,s}\}^{m_s}-1$.
  By (6.1) and (A.1), $M_j>0$ gives $|q_\rho(r_je^{2\pi iu})|^2>1$ for all
  $u\in I_j$, so Lemma 6.1 reduces to the 8192 rational inequalities
  $M_j>0$.
- Margins. Table 2 (p. 12) lists the least $M_j$ in each block. The least of
  all is at $(j,r)=(3318,1/300)$, in block 6, an exact rational with a
  numerator of 1289 digits and a denominator of 1295 digits; the paper states
  that the smallest $M_j$ is at least $2.327036066010500056098356\cdot10^{-6}$.
  The other block minima run from about $2.6\cdot10^{-6}$ (block 8) to about
  $1.5\cdot10^{-2}$ (blocks 2 and 4). The paper calls its displayed decimals
  renderings of exact positive rationals.
- Checker. Pages 12--14 print a Wolfram Language program that checks that
  the blocks cover $j=0,\dots,8191$, computes every $M_j$ in exact rational
  arithmetic, stops if some $M_j\le0$, and prints the block minima with
  SHA-256 hashes of their exact values; floating point enters only the
  displayed decimals (p. 12). It was not run for this page.

**Read depth.** Claims checked: the construction, (6.1), Lemma 6.1, Theorem
6.2, Remark 6.4 and the definitions and Tables 1 and 2 of Appendix A were
read clause by clause on the page images. Only the certificate's bookkeeping
was recomputed here, in exact arithmetic and without the printed checker: the
leading coefficient, the zero directions, which match Remark 6.4, and that
the blocks of Table 1 cover $j=0,\dots,8191$ and give the radius $439/1000$
to the intervals containing $67/960$ and $217/960$ and the radius $1/300$ to
those containing $447/960$ and $797/960$. The derivation of (A.1) was read
and not checked, none of the 8192 inequalities was checked, and the printed
checker was not run. The paper is an unrefereed preprint, and nothing here is
independently reviewed.

## Proof pointer

Theorem 6.2, pp. 9--10. $P_\rho$ is monic and admissible by construction.
Since $|P_\rho|=|q_\rho|$, Lemma 6.1 gives
$\max_{0\le r\le1}|P_\rho(re^{2\pi iu})|>1$ for every $u$, so no radius lies
in $\{|P_\rho|\le1\}$; then $\mathcal B(P_\rho)>1$, and Proposition 2.2 gives
$\Delta(P_\rho)>0$. Lemma 6.1 (p. 9) follows from the certificate above,
since the intervals $I_j$ cover $[0,1]$. For (A.1) the paper uses that the
cosine is symmetric about half-integers and decreasing on $[0,\pi]$, that
$\pi_0<\pi$, and Taylor's theorem for the cosine with remainder at most
$x^{21}/21!$ (pp. 10--11).

## Dependencies

Lemma 6.1 (p. 9) with Appendix A (pp. 10--14), and the harder half of
Proposition 2.2 (p. 2), stated on the
[[analysis/pendyala_2026_radial_access_lemniscates/theorem_1_1|Theorem 1.1 page]]:
zero detour forces a safe radius.

## Bears on

- [[../wiki/problems/analysis/E1120/_index|Problem 1120]]: in the problem
  page's worst-case reading $S(n)$, the theorem gives $S(6)\ge L(P_\rho)>1$,
  so in degree six the trivial bound $1$ is not attained. It gives no lower
  bound for $L(P_\rho)-1$, does not say whether $L(P_\rho)$ is finite, and
  says nothing about other degrees.
