---
name: research/leads/equilateral_two_scale/circle_exclusion
title: Circle structure excludes two equilateral scales for measurable colorings
desc: |
  At a boundary point of a measurable coloring that weakly misses equilateral
  sides 1 and x, the density points on a suitable circle must be invariant
  under a dense group of rotations while a sixty-degree turn swaps the
  colors, unless that circle meets the boundary in positive length, which a
  null boundary cannot sustain. With the Bessel bound this excludes every
  ratio x != 1 for measurable colorings.
created: 2026-10-17T01:48:10Z
updated: 2026-10-17T01:48:10Z
---

***

Theorem 4, Corollary 5 and their finite-forcing interface are covered by
the [[research/leads/equilateral_two_scale/evidence/verify/whole_conclusion/grade|graded whole-conclusion review]].
The project argument is credited to Plasma AI. The source inputs are
Lemma 1.3 of
[[../library/discrete_geometry/jelinek_2009_monochromatic_triangles_two_colored_plane/corollary_1_4|Jelínek, Kynčl, Stolař and Valla]]
(statement and proof read in the transcription), Theorem 2 of
[[research/leads/equilateral_two_scale/spectral_exclusion|the spectral
account]] (covered in the same review) for ratios outside the window, and
the standard Lebesgue density theorem and Federer criterion for finite perimeter
(H. Federer, *Geometric Measure Theory*, 1969, 4.5.11). The criterion,
the definition of measure-theoretic boundary and the perimeter formula
were checked at statement level in P. Lahti,
[*Federer's characterization of sets of finite perimeter in metric
spaces*](https://arxiv.org/abs/1804.11216v1), Introduction and Section 2,
pp. 1--2 and 5--6; their original proofs were not read.
No premise of the release's rigidity theorem is used on this page.

## Setting

Notation follows the spectral account. A measurable coloring is a Lebesgue
measurable $c:\mathbb C\to\{\pm1\}$, with red and blue classes
$\{c=1\}$ and $\{c=-1\}$. For a triangle $(0,a,b)$ its copies are
$(p,p+ua,p+ub)$ with $p\in\mathbb C$ and $|u|=1$, and $c$ *weakly avoids* the
triangle when its monochromatic copies form a null set for area times arc
length in $(p,u)$.

Let $A^*$ and $B^*$ be the points at which the red class has density $1$,
respectively density $0$, and let $S=\mathbb C\setminus(A^*\cup B^*)$. The
upper and lower densities are limits superior and inferior, over rational
radii, of functions continuous in $p$, so $A^*$, $B^*$ and $S$ are Borel.
Lebesgue's density theorem gives $|S|=0$. At every point of $S$ both
classes have positive upper density, since the red density is neither $0$
nor $1$ there. In the notation of geometric measure
theory, $S$ is the measure-theoretic boundary of the red class.

For $r>0$ and $p\in\mathbb C$ put, with $\mathbb T=\mathbb R/2\pi\mathbb Z$,

$$
\Theta_r^+(p)=\{\theta:p+re^{i\theta}\in A^*\},\quad
\Theta_r^-(p)=\{\theta:p+re^{i\theta}\in B^*\},\quad
\Theta_r^0(p)=\{\theta:p+re^{i\theta}\in S\}.
$$

These Borel sets partition $\mathbb T$. For $0<\gamma\le\pi$ write
$I_{r,\gamma}=(0,\,r,\,re^{i\gamma})$ for the isosceles triangle with legs
$r$ and apex angle $\gamma$ at the origin; $I_{r,\pi/3}$ is the equilateral
triangle of side $r$.

## Theorem

**Theorem 4.** Let $x>0$ and $x\ne1$. No Lebesgue measurable two-coloring of
the plane weakly avoids both the equilateral triangle of side $1$ and the
equilateral triangle of side $x$. Equivalently, every measurable two-coloring
of the plane has a set of monochromatic equilateral triangles of side $1$ or
of side $x$ of positive measure in $(p,u)$.

**Corollary 5.** For every non-equilateral triangle $T$, every measurable
two-coloring of the plane has a set of monochromatic copies of $T$ of
positive measure. In particular a measurable two-coloring misses the
monochromatic congruent copies of at most one triangle, which is then
equilateral; this is the statement of Problem 173 restricted to measurable
colorings.

*Proof of Corollary 5 from Theorem 4.* Lemma 1.3 of Jelínek et al. is proved
from one finite configuration, fixed once a triangle is placed. In every
coloring of it in which the placed equilateral triangle of side $a$ is
monochromatic, one of its copies of the triangle with sides $a,b,c$ is
monochromatic (part (i)); in every coloring in which the placed triangle
with sides $a,b,c$ is monochromatic, one of its equilateral triangles is
(part (ii)). If a set of placements of positive Haar measure makes the
hypothesis triangle monochromatic, then one of the finitely many triangles
named in the conclusion is monochromatic on a subset of positive measure.
Composing with the fixed motion that carries the standard copy of that
triangle into the configuration preserves Haar measure on the group of
orientation-preserving motions. So the lemma holds with "contains" read as
"has a positive-measure set of monochromatic copies". Let $T$ have side
lengths $a\ne b$; a cyclic relabeling of its sides makes $T$ an
$(a,\cdot,\cdot)$ and a $(b,\cdot,\cdot)$-triangle in the anticlockwise
convention of the lemma. If the monochromatic copies of $T$ were null, part
(i) in this form would make the monochromatic equilateral triangles of
sides $a$ and $b$ null, and scaling by $1/a$ would contradict Theorem 4 at
$x=b/a$. Reflected copies are not needed, as copies by rotation are
congruent. $\square$

## Coordinates for the finite forcing input

The finite configuration used in Lemma 1.3 can be specified without its
figure. This also fixes the orientation and measure interfaces in the
preceding deduction. Put $\omega=e^{i\pi/3}$, let $a>0$, and choose
$z\ne0,a$. The triangle $(B,A,D)=(a,0,z)$ has side lengths
$a,b=|z|,c=|z-a|$. Use the eight points

$$
\begin{aligned}
A&=0,& B&=a,& C&=a\omega,& D&=z,\\
B'&=\omega z,& A'&=a+\omega z,&
C'&=a\bar\omega+\omega z,& D'&=a-\bar\omega z.
\end{aligned}
$$

The triples $ABC,A'B'C'$ are equilateral of side $a$;
$ADB',A'D'B$ are equilateral of side $b$; and $BDC',B'D'C$ are
equilateral of side $c$. The six triples
$BAD,CAB',CBD',B'A'D',C'A'B,C'B'D$ are orientation-preserving copies
of $(a,0,z)$. Their multipliers and translations, in that order, are

$$
(1,0),\ (\omega,0),\ (-\bar\omega,a),\
(-1,a+\omega z),\ (-\omega,a+\omega z),\
(\bar\omega,\omega z).
$$

If $A,B,C$ have one color and all six copies of the target triangle are
assumed nonmonochromatic, the first three force $D,B',D'$ to have the
other color. The fourth forces $A'$ back to the first color; the fifth
then forces $C'$ to the second, contradicting the sixth. This proves
part (i) of the source lemma.
For part (ii), start with $B,A,D$ of one color and assume the six
equilateral triples are nonmonochromatic. The triples $ADB',ABC,BDC'$
force $B',C,C'$ to the other color. Then $A'B'C'$ forces $A'$ to the
first color, and $A'D'B$ forces $D'$ to the other, contradicting
$B'D'C$. Coincidences between different listed points can only give
an earlier color contradiction; each named triangle itself still has
three distinct vertices. The argument therefore includes collinear
target triples.

Only finitely many fixed translations and rotations are involved. Their
composition with a variable placement preserves Haar measure on the
orientation-preserving motion group, giving exactly the positive-measure
version used above and in the proof of Theorem 4.

## Four lemmas

**Lemma 1 (apex lemma).** Let $c$ be measurable and weakly avoid
$I_{r,\gamma}$. If a color class has positive upper density at $p$, then
there is no $\theta$ for which $p+re^{i\theta}$ and $p+re^{i(\theta+\gamma)}$
are both density-one points of that class.

*Proof.* Say the class is red, with
$|B(p,h)\cap\{c=1\}|\ge\delta|B(p,h)|$ for a sequence $h\to0$, and let
$q=p+re^{i\theta}$ and $q'=p+re^{i(\theta+\gamma)}$ be red density points.
Choose $p'$ uniformly in $B(p,h)$ and, independently, $\varphi$ uniformly in
$[-h/r,h/r]$. The copy $(p',\,p'+e^{i\varphi}(q-p),\,p'+e^{i\varphi}(q'-p))$
of $I_{r,\gamma}$ has its second vertex, for fixed $\varphi$, uniform in a
disk of radius $h$ whose center is within $h$ of $q$. Its law therefore has
density at most $1/(\pi h^2)$ on $B(q,2h)$, and the probability that it is
blue is at most $4|B(q,2h)\setminus\{c=1\}|/|B(q,2h)|\to0$. The same holds
at $q'$. Hence all three vertices are red with probability at least
$\delta-o(1)$ along the sequence. The law of $(p',\varphi)$ has a bounded
density, so the monochromatic copies have positive measure, contrary to
weak avoidance. $\square$

This is the three-point density-point argument of the
[[research/leads/equilateral_two_scale/binary_transfer|binary transfer]],
with only positive upper density required at the apex.

**Lemma 2 (alternation on a circle).** Let $R\subset\mathbb T$ be
measurable and put $R'=\mathbb T\setminus R$. Suppose that
$R\cap(R+\pi/3)$, $R'\cap(R'+\pi/3)$ and $R\cap(R+\gamma)$ are null. Then
$\pi/3$ does not belong to the closed subgroup $H_\gamma$ of $\mathbb T$
generated by $2\pi/3$ and $\gamma-\pi/3$. In particular $\gamma/\pi$ is
rational.

*Proof.* From the first condition $R+\pi/3\subset R'$ up to a null set, so
$|R|\le|R'|$; the second gives $|R'|\le|R|$. Thus $|R|=|R'|=\pi$, and an
inclusion of sets of equal finite measure is an equality up to null sets:
$R+\pi/3=R'$. The first condition also says $R-\pi/3\subset R'$, so
$R-\pi/3=R'$ and $R+2\pi/3=R$. The third gives $R+\gamma=R'=R+\pi/3$, so
$R+(\gamma-\pi/3)=R$. All equalities hold up to null sets. The set of $t$
with $|(R+t)\triangle R|=0$ is a closed subgroup, since this measure is
continuous in $t$; it contains $H_\gamma$. If it contained $\pi/3$, then
$R'=R+\pi/3=R$ up to a null set, impossible as $R\cap R'=\emptyset$ and
$|R|=\pi$. When $\gamma/\pi$ is irrational, $H_\gamma=\mathbb T$. $\square$

The finer condition is arithmetic. If $\gamma/2\pi=P/Q$ in lowest terms,
then $\pi/3\in H_\gamma$ exactly when some integer $k$ makes
$k(6P-Q)/Q$ an odd integer, which happens if and only if
$Q\not\equiv2\pmod4$: take $k=Q$ when $Q$ is odd and $k=Q/2$ when $4\mid Q$;
when $Q=2Q_1$ with $Q_1$ odd, integrality forces $k=tQ_1/g$ with
$g=\gcd(Q_1,3)$, and the value $t(3P-Q_1)/g$ is even because $P$ and
$Q_1$ are odd.
For $\gamma=\pi/3$, the case $x=1$, one has $Q=6$, consistent with the
zebra-like colorings, whose boundary points see six alternating arcs of
sixty degrees, the hexagon of Claim 3.11 of Jelínek et al.

**Lemma 3 (no self-supporting null set).** Let $S\subset\mathbb C$ be Borel
and $r>0$, and suppose that $\Theta_r^0(p)=\{\theta:p+re^{i\theta}\in S\}$
has positive measure for every $p\in S$. Then $S$ is empty or has positive
area.

*Proof.* Let $p\in S$ and let $E$ be the Borel set of
$(\theta,\varphi)\in\mathbb T^2$ with $p+re^{i\theta}\in S$ and
$p+re^{i\theta}+re^{i\varphi}\in S$. Fubini gives
$|E|=\int_{\Theta_r^0(p)}|\Theta_r^0(p+re^{i\theta})|\,d\theta>0$, since
every point $p+re^{i\theta}$ with $\theta\in\Theta_r^0(p)$ lies in $S$. The
map $F(\theta,\varphi)=p+re^{i\theta}+re^{i\varphi}$ has Jacobian
determinant $r^2\sin(\varphi-\theta)$, nonzero off a null set, and is at
most two-to-one away from the single point $p$. The area formula gives
$\int_E r^2|\sin(\varphi-\theta)|\,d\theta\,d\varphi
=\int_{\mathbb C}\#(F^{-1}(z)\cap E)\,dz$, so $F(E)$, which lies in $S$,
has positive area. $\square$

**Lemma 4 (two rational chord angles).** Let $1/2<x<2$, and suppose that
$A=\arcsin(x/2)$ and $B=\arcsin(1/(2x))$ are both rational multiples of
$\pi$. Then $x$ is one of $1$, $(1+\sqrt5)/2$, $(\sqrt5-1)/2$,
$2\sin(5\pi/12)$ and $2\sin(\pi/12)$. None of these except $1$ lies in
$(2/3,3/2)$.

*Proof.* Here $A,B\in(0,\pi/2)$ and $\sin A\sin B=1/4$, so with $u=A-B$ and
$v=A+B$,

$$
\alpha-\beta=1,\qquad \alpha=2\cos u,\quad \beta=2\cos v,
\qquad |u|<\pi/2,\quad 0<v<\pi .
$$

Let $e^{iu}$ and $e^{iv}$ have orders $m_1$ and $m_2$. For $m\ge3$ the
number $2\cos(2\pi k/m)$ with $\gcd(k,m)=1$ has the $\varphi(m)/2$
conjugates $2\cos(2\pi j/m)$, $\gcd(j,m)=1$, whose sum is the Ramanujan sum
$\mu(m)$; for $m=1,2$ the number is $\pm2$. So the average of the
conjugates of $\alpha$ is $\tau(m_1)$, where $\tau(1)=2$, $\tau(2)=-2$ and
$\tau(m)=2\mu(m)/\varphi(m)$ for $m\ge3$; in particular $\tau(3)=-1$,
$\tau(4)=0$, $\tau(6)=1$, and otherwise $|\tau(m)|\le1/2$, with
$\tau(m)=\pm1/2$ only for $m=10$ and $m=5$ respectively, and $\tau(m)$ of
the form $\pm1/j$ or $0$. Applying every automorphism of the real
cyclotomic field containing $\alpha$ and $\beta$ to $\alpha-\beta=1$ and
averaging gives $\tau(m_1)-\tau(m_2)=1$. The only solutions are
$(\tau(m_1),\tau(m_2))=(2,1),(1,0),(0,-1),(-1,-2),(1/2,-1/2)$. The third
and fourth force $\alpha=0$ or $\beta=-2$, excluded by $|u|<\pi/2$ and
$v<\pi$. The first gives $u=0$, $v=\pi/3$, so $A=B=\pi/6$ and $x=1$. The
second gives $\alpha=1$, $\beta=0$, so $|u|=\pi/3$, $v=\pi/2$ and
$\{A,B\}=\{5\pi/12,\pi/12\}$. The last gives $m_1=10$, $m_2=5$; among
$\alpha\in\{2\cos(\pi/5),2\cos(3\pi/5)\}$ and
$\beta\in\{2\cos(2\pi/5),2\cos(4\pi/5)\}$ with $\alpha-\beta=1$, only
$|u|=\pi/5$, $v=2\pi/5$ has $|u|<\pi/2$, so
$\{A,B\}=\{3\pi/10,\pi/10\}$. Then $x=2\sin A$ is as listed. $\square$

## Proof of Theorem 4

For $x\ge3/2$ or $x\le2/3$ this is Theorem 2 of the spectral account. Let
$2/3<x<3/2$ and $x\ne1$, and suppose $c$ weakly avoids both sides. Put
$\gamma_1=2\arcsin(x/2)$ and $\gamma_x=2\arcsin(1/(2x))$, the apex angles
of the isosceles triangles with sides $1,1,x$ and $x,x,1$, both in
$(0,\pi)$. By Lemma 4 one of $\gamma_1/\pi$ and $\gamma_x/\pi$ is
irrational; let $r\in\{1,x\}$ be the corresponding leg and $\gamma=\gamma_r$.
The triangle $I_{r,\gamma}$ has sides in $\{1,x\}$, so part (ii) of Lemma
1.3 of Jelínek et al., in the measure form used for Corollary 5, shows that
$c$ weakly avoids it. It also weakly avoids $I_{r,\pi/3}$, the equilateral
triangle of side $r$.

Let $p\in S$. Both classes have positive upper density at $p$. If
$\Theta_r^0(p)$ were null, put $R=\Theta_r^+(p)$, whose complement differs
from $\Theta_r^-(p)$ by a null set. Lemma 1 for red with $I_{r,\pi/3}$ and
$I_{r,\gamma}$, and for blue with $I_{r,\pi/3}$, makes $R\cap(R+\pi/3)$,
$\Theta_r^-(p)\cap(\Theta_r^-(p)+\pi/3)$ and $R\cap(R+\gamma)$ empty.
Lemma 2 then contradicts the irrationality of $\gamma/\pi$. Hence
$\Theta_r^0(p)$ has positive measure for every $p\in S$, and Lemma 3 with
$|S|=0$ gives $S=\emptyset$.

So the red class has empty measure-theoretic boundary. By Federer's
criterion, in the [[../library/analysis/lahti_2018_federer_characterization_finite_perimeter/theorem_1_1|local form recorded by Lahti]],
it has locally finite perimeter, and its perimeter measure is
one-dimensional Hausdorff measure on its reduced boundary, which lies in
the measure-theoretic boundary and is empty. The distributional gradient of
its indicator vanishes, so the red class is null or conull. Then almost
every copy of the unit equilateral triangle is monochromatic, contradicting
weak avoidance. $\square$

**Remark (range of the circle argument alone).** By the arithmetic after
Lemma 2 and the list in Lemma 4, the same proof works for every
$x\in(1/2,2)$ except $1$, $(1+\sqrt5)/2$ and $(\sqrt5-1)/2$: at
$x=2\sin(5\pi/12)$ and $x=2\sin(\pi/12)$ one has $\gamma_1/2\pi=5/12$ and
$1/12$, with denominators divisible by $4$, while at the golden ratio both
$\gamma_1/2\pi=3/10$ and $\gamma_x/2\pi=1/10$ have denominator $10$. For
$x\ge2$ only the circle of radius $x$ is available, and for $x\le1/2$ only
the unit circle; there the argument excludes every $x$ outside a countable
set. Theorem 2 covers all of these exceptions.

## Place in the route

Theorem 4 supplies step 6 of the
[[research/leads/equilateral_two_scale/_index|proof sketch]] for measurable
colorings without the zebra-like classification. The
[[research/leads/equilateral_two_scale/binary_transfer|binary transfer]]
composes with it at algebraic ratios granting the separate premise (R0).
The reviewed
[[research/leads/equilateral_two_scale/rigidity_extension|rigidity extension]]
supplies the transfer for every real ratio. The graded whole-conclusion
review covers the resulting full argument on the canonical sketch.
The argument on this page itself needs measurability throughout
(density points, arc length, area); its application to arbitrary colorings
uses that transfer.

A web search on 2026-10-17 for the two-scale or all-non-equilateral form of
this statement for measurable colorings found Shkredov's Bessel criterion
and the polygonal and closed-open results of Jelínek et al., but no
statement covering every non-equilateral triangle for measurable
colorings. The search was brief and does not certify novelty.
