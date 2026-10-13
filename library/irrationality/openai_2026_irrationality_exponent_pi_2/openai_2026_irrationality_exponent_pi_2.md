# The irrationality exponent of $\pi$ is $2$

OpenAI

## Abstract

We prove the conjecture that the irrationality exponent of $\pi$ is $2$. As a consequence, the classical Flint–Hills series $\sum_{n\ge1}1/(n^3\sin^2 n)$ converges, with angles in radians.

## Introduction

For an irrational real number $x$, its *irrationality exponent* (also called its irrationality measure) is $$\mu(x)=\sup\left\{\nu>0:
0<\left|x-\frac pq\right|<q^{-\nu}
\text{ for infinitely many coprime }p,q\in\mathbb Z,\ q\ge2\right\}.$$ The pigeonhole principle gives $\mu(x)\ge2$. An upper bound limits how frequently rational numbers can approximate $x$ exceptionally closely; irrationality alone supplies no finite upper bound. The expected value for the usual positive circle constant is $2$. Waldschmidt records the corresponding epsilon-dependent approximation conjecture in (Waldschmidt 2004, 265). Our main result proves it.

**Theorem 1.1**. *The irrationality exponent of $\pi$ is $2$. More precisely, for every real $\nu>2$, there is an integer $Q(\nu)$ such that $$\left|\pi-\frac pq\right|\ge q^{-\nu}
\qquad(p\in\mathbb Z,\ q\in\mathbb Z,\ q\ge Q(\nu)).$$*

The inequality applies to all integer numerators and denominators, whether or not the fraction is reduced. The threshold may depend on $\nu$, and the argument does not give it effectively. In particular, an exponent of $2$ is different from a uniform positive lower bound of the form $c/q^2$, or equivalently from bounded continued-fraction partial quotients.

The related Flint–Hills problem, popularized by Pickover and discussed by Alekseyev (Alekseyev 2011), asks whether $$\sum_{n\ge1}\frac{1}{n^3\sin^2 n}$$ converges, with angles in radians. Integers very close to multiples of $\pi$ make individual denominators small. A rational-approximation bound controls how often such small values can occur, not just their individual size.

**Corollary 1.2**. *The classical Flint–Hills series converges.*

Alekseyev showed that convergence requires $\mu(\pi)\le5/2$ (Alekseyev 2011, Corollary 4); Meiburg proved the sufficient strict condition $\mu(\pi)<5/2$ (Meiburg 2022, Theorem 2.5). Theorem 1.1 supplies this condition. Section 5 includes a short dyadic proof of the implication needed here. Neither cited criterion settles its equality boundary at $5/2$.

More generally, for fixed real numbers $a,b>0$, consider the family $$\sum_{n=1}^{\infty}\frac{1}{n^a|\sin n|^b}.$$ Theorem 1.1 and the spacing argument in Section 5 show that, with angles in radians, this series converges if and only if $a>\max\{1,b\}$; see Corollary 5.2.

### Quantitative approximation and related work

Mahler’s 1953 paper (Mahler 1953) established a finite irrationality exponent for $\pi$ by constructing polynomial-coefficient combinations of powers of logarithms and proving determinant nonvanishing. It gave the explicit exponent $42$ for all denominators at least two and also stated an eventual improvement to $30$. Mignotte refined that construction, obtaining exponent $21$ for all such denominators and $20$ eventually (Mignotte 1974, Theorem 1). Chudnovsky developed Hermite–Padé approximation to exponential functions with precise asymptotic estimates (Chudnovsky 1982).

Hata’s integral constructions led to the bound $\mu(\pi)\le8.01604539\ldots$ (Hata 1993); Zudilin gives an account of the simultaneous logarithmic approximation and denominator arithmetic behind this value (Zudilin 2004, Theorem 2). Salikhov’s symmetric-integral method improved it to $7.606308\ldots$ (Salikhov 2008, 2010). Zeilberger and Zudilin combined parameter experiments with a rigorous arithmetic and asymptotic analysis to obtain $7.103205334137\ldots$ (Zeilberger and Zudilin 2020). Bai’s September 2026 preprint claims the further bound $\mu(\pi)<7.101862832357$ by a two-exponent variation of the latter integral (Bai 2026). These quantitative bounds are context, not inputs to our proof.

The connection with trigonometric series also has a longer history: Mahler applied approximation estimates to sine-denominator Dirichlet series in (Mahler 1953, sec. 16). For the classical Flint–Hills question, recent work of Dan on generalized series (Dan 2026) and López Zapata’s continued-fraction criterion (López Zapata 2026) leaves convergence undecided. The earlier convergence claim of Mantzakouras and López Zapata was withdrawn in September 2026 because its proof did not establish convergence or the asserted irrationality bound (Mantzakouras and López Zapata 2025). Carella claims both exponent two and the stronger bounded-partial-quotient property (Carella 2022). Neither claim is used here. The displayed proof of the stronger assertion contains a sign obstruction.[^1]

### The proof in outline

The proof uses a multivariable interpolation theorem to construct a nonzero determinant, then compares two incompatible estimates for its absolute value. This organization is related to the interpolation-determinant method discussed by Laurent (Laurent 1991, sec. 6). Successively separated approximation denominators already play a central role in Roth’s many-variable method (Roth 1960, secs. 2–3). Our application requires a different interpolation statement, adapted to logarithmic curves and with thresholds independent of their centers.

##### Prescribing coefficients.

A jet here means a finite packet of Taylor coefficients. Give the coordinates $Y,X_1,\ldots,X_m$ positive weights and retain polynomial monomials satisfying one weighted degree inequality. Their exponent vectors fill a simplex. At each point $(1,c_{j1},\ldots,c_{jm})$, expand after the substitution $$Y=1+t,\qquad X_i=c_{ji}+u_i+\log(1+t).$$ The variable $t$ follows the logarithmic curve; the variables $u_i$ are transverse displacements. Theorem 2.1 states that every packet below the prescribed weighted cutoff can be realized, at finitely many centers whose $X_i$-coordinates are pairwise distinct for each $i$, simultaneously. The weights of $X_1,\ldots,X_m$ are chosen successively before the center locations are known. The weights leave more polynomial coefficients than prescribed Taylor coefficients, but that dimension count alone does not prove full rank at these special centers.

The proof in Section 2 starts from a local multiplicity comparison between coordinate directions and commuting differential directions. Derivative persistence and separated scales restrict any algebraic obstruction; logarithmic residues then force coordinate constancy. This stage is related to the zero-estimate methods of Philippon (Philippon 1986) and the separated multidegrees in Farhi’s Roth lemma (Farhi 2006, sec. 5.2). The resulting curve inequality bounds total weighted contact at the centers by the weighted degree of the curve. It gives positivity on an ordinary blowup, and vanishing yields all the requested coefficients. The relation between curvewise positivity and asymptotic jet generation is familiar from Demailly’s work (Demailly 1992, sec. 6); the weighted, multiple-center statement on the possibly singular schemes used here is proved explicitly.

##### Two ways to make the determinant small.

Suppose that a fixed exponent $\nu>2$ permits exceptionally close approximations with unbounded denominators. Choose finitely many of these successively and set $c_{ji}=2\mathrm ij p_i/q_i$. They approximate the common logarithmic periods $2\pi\mathrm ij$. After truncating the logarithms by a filtration-preserving change, interpolation gives a matrix over $\mathbb Q(\mathrm i)$ with independent rows. A square minor using all rows is nonzero. Clearing its denominators gives an arithmetic lower bound.

For the analytic bound, translate each row to the exact periods and expand in the transverse variables. The index $a$ denotes the chosen transverse coefficient. For a polynomial column $P$, $$[u^a]P(e^z,z+u_1,\ldots,z+u_m)$$ is an entire function of $z$. Rows test its Taylor coefficients after $z=2\pi\mathrm ij+\log(1+t)$. Rows with the same $a$ therefore test the same entire functions. On expanding those functions in $z$, repeated Taylor degrees within that group annihilate a determinant term. Distinct degrees then force a quadratic saving in the group size. This uses the Taylor-expansion mechanism also appearing in (Laurent 2000, Theorem 1). If many rows have small weighted transverse index, there are too few groups to avoid this saving. If few do, the many large indices instead supply powers of the small rational-approximation errors. Section 3 proves uniform bounds for both alternatives before summing the expansion.

##### Why full simplices and separated choices matter.

The polynomial degree of $Y$ and those of the $X_i$ share one budget. Both the interpolation volume and the arithmetic column cost therefore come from full simplices. Comparing the row count in dimension $m+1$ with the transverse-index count in dimension $m$ produces a collision saving that can grow with $m$, while the other errors decrease. Section 4 arranges this for each fixed $\nu>2$, then chooses approximation denominators meeting all the interpolation thresholds. Their independence from centers prevents a circular choice. Only after dimension, weights, and centers have been fixed does the polynomial degree tend to infinity. The final section proves Corollary 1.2 using a fixed exponent between $2$ and $5/2$, and establishes the exact convergence criterion in Corollary 5.2.

##### Conventions and inputs.

All logarithms are natural; $\log(1+t)$ denotes its power series at zero. Write $\mathrm i^2=-1$, and let multi-indices have nonnegative integer entries. For them, $\alpha!=\prod_i\alpha_i!$ and $\binom\alpha\beta=\prod_i\binom{\alpha_i}{\beta_i}$, with the latter zero unless $\beta\le\alpha$ coordinatewise. Geometry is over $\mathbb C$, and a curve means an integral algebraic curve. We use polynomial Bézout with isolated local multiplicities, ordinary blowups, nef-plus-ample, eventual Proj recovery, Serre vanishing, and smooth projective models of curves. Their exact hypotheses are checked at use; no prior irrationality bound for $\pi$ is assumed.

## Interpolation with separated weights

We prove the interpolation statement used in the determinant argument. Its essential uniformity is that the weights can be chosen before the interpolation points: each coordinate weight has a lower threshold depending on the earlier weights, but not on the locations of the points. The degree at which interpolation becomes surjective is allowed to depend on all the fixed data.

All multi-indices below have nonnegative integer entries. For a positive rational vector $W=(w_0,\ldots,w_m)$, the $W$-degree of the monomial $Y^hX_1^{\alpha_1}\cdots X_m^{\alpha_m}$ is $w_0h+\sum_iw_i\alpha_i$. Write $\mathcal P_W(H)$ for the complex vector space of polynomials of $W$-degree at most $H$. For a positive rational vector $V=(v_0,\ldots,v_m)$, let $\mathcal J_V(H)$ be the quotient of $\mathbb C[[t,u_1,\ldots,u_m]]$ by the ideal of series whose monomials all have $V$-weight at least $H$. Thus a vector in $\mathcal J_V(H)$ is a packet of coefficients indexed by $$v_0s+\sum_{i=1}^m v_i\beta_i<H.$$ The strict inequality in this definition will be used throughout.

**Theorem 2.1** (Separated-weight interpolation). *Fix integers $m,K\ge1$ and positive rational numbers $w_0,v_0,\theta$ such that $0<\theta<1$ and $$\begin{equation}
\tag{2.1}
 K\theta^m<1,
 \qquad K\frac{w_0}{v_0}\theta^m<1.
\end{equation}$$ There are successive lower thresholds for positive rational numbers $w_1,\ldots,w_m$, depending only on these fixed data and the previously chosen weights, with the following property. Put $$W=(w_0,w_1,\ldots,w_m),\qquad
 V=(v_0,w_1/\theta,\ldots,w_m/\theta).$$ For any points $$a_j=(1,c_{j1},\ldots,c_{jm})\in\mathbb C^{m+1},\qquad 0\le j<K,$$ whose coordinates $c_{0i},\ldots,c_{K-1,i}$ are pairwise distinct for each $i$, the map $$\begin{equation}
\tag{2.2}
 \begin{aligned}
 \mathcal P_W(H)&\longrightarrow\bigoplus_{j=0}^{K-1}\mathcal J_V(H),\\
 P&\longmapsto
 \left(P\bigl(1+t,(c_{ji}+u_i+\log(1+t))_{i=1}^m\bigr)\right)_{j=0}^{K-1}.
 \end{aligned}
\end{equation}$$ is surjective for all sufficiently large, sufficiently divisible integers $H$. The divisibility requirement can be chosen using only the weights. The remaining lower threshold for $H$ may depend on the points.*

We first establish a numerical inequality on algebraic curves, and then use it to obtain all the jets in (2.2). The local estimate driving the curve argument is recorded separately.

### A local multiplicity comparison

A collection of vector fields is called a *normal basis* to a smooth subvariety at a point if its images form a basis of the ambient tangent space modulo the tangent space of the subvariety. For an irreducible subvariety, this terminology will refer to a general smooth point. There are only finitely many possible index sets in the applications below, so all their generic rank conditions can be checked on one common open subset.

**Lemma 2.2** (Weighted transverse multiplicity). *Give the coordinates $x_1,\ldots,x_d$ positive rational degree weights $\rho_1,\ldots,\rho_d$. On an open subset of $\mathbb C^d$, let $D_1,\ldots,D_d$ be commuting analytic vector fields forming a frame, and assign them positive rational costs $\kappa_1,\ldots,\kappa_d$. Fix $\varepsilon>0$.*

*Let $N>0$. Suppose that polynomials $f_1,\ldots,f_r$ have weighted degree at most $N$, that $Z$ is an irreducible component of their common zero set of codimension $k\ge1$, and that $$\begin{equation}
\tag{2.3}
 D^\gamma f_\ell\big|_Z=0
 \quad\text{whenever}\quad
 \sum_b\kappa_b\gamma_b<\varepsilon N.
\end{equation}$$ For any coordinate normal basis $A$ and any $D$-field normal basis $B$, each of cardinality $k$, one has $$\begin{equation}
\tag{2.4}
 \prod_{a\in A}\rho_a
 \le 2k!\,\varepsilon^{-k}\prod_{b\in B}\kappa_b
\end{equation}$$ The bound is uniform in the equations, the component $Z$, and the analytic frame; no lower threshold for $N$ is required.*

*Proof.* Choose a smooth point $x$ of $Z$ where both normal-basis conditions hold and which lies on no other irreducible component of the common zero set. Flowing from $Z$ along the fields indexed by $B$ gives local analytic coordinates $(z,b)$, where $z$ parametrizes $Z$ and $b=(b_1,\ldots,b_k)$ consists of transverse flow parameters. Commutativity implies that the chosen fields are the derivatives in the $b$-directions. Thus (2.3) says that in the expansion $$f_\ell(z,b)=\sum_{\alpha\in\mathbb Z_{\ge 0}^k} f_{\ell,\alpha}(z)b^\alpha,$$ every coefficient function of $B$-weight less than $\varepsilon N$ vanishes identically on the chosen neighborhood in $Z$.

Let $S$ be the affine coordinate slice through $x$ obtained by fixing the coordinates outside $A$. It is transverse to $Z$, and the zero set of the restricted equations is isolated at $x$. The flow parameters $b$ give regular analytic coordinates on $S$; the coordinates $z$ become analytic functions $z(b)$. Substitution cannot generate a missing term of smaller $B$-weight. Indeed, each surviving summand already contains a monomial $b^\alpha$ of weight at least $\varepsilon N$, and its analytic coefficient has only nonnegative powers of $b$. Consequently the ideal of the restricted equations is contained in the monomial ideal of weight at least $\varepsilon N$. Its quotient therefore has length at least $$\begin{equation}
\tag{2.5}
 \#\left\{\alpha\in\mathbb Z_{\ge 0}^k:
       \sum_{b\in B}\kappa_b\alpha_b<\varepsilon N\right\}
 \ge \frac{(\varepsilon N)^k}{2k!\prod_{b\in B}\kappa_b}
\end{equation}$$ In fact the factor $1/2$ can be omitted: the simplex $\{x\in\mathbb R_{\ge0}^k:\sum_{b\in B}\kappa_bx_b<\varepsilon N\}$ is covered by the disjoint half-open unit cubes $\alpha+[0,1)^k$ indexed by the admissible multi-indices $\alpha=\lfloor x\rfloor$. Its volume is $(\varepsilon N)^k/(k!\prod_{b\in B}\kappa_b)$. Thus the displayed bound holds for every $N>0$. Analytic local coordinates preserve finite length, so no radius or coefficient bound for the flow map is needed.

In the regular local ring of the $k$-dimensional slice, the ideal generated by the restricted equations is primary to the maximal ideal. Over the infinite field $\mathbb C$, $k$ sufficiently general constant linear combinations of these equations still have an isolated common zero at $x$: successive generic combinations avoid the finitely many positive-dimensional components that remain. Their ideal is contained in the original ideal. Their quotient length is therefore an upper bound for the length in (2.5).

Each of the $k$ combinations has weighted degree at most $N$ in the variables indexed by $A$. We claim that their local intersection length is at most $$\begin{equation}
\tag{2.6}
 \frac{N^k}{\prod_{a\in A}\rho_a}.
\end{equation}$$ Choose an integer $M_0$ clearing the denominators of the $\rho_a$, and make the substitutions $$x_a=\lambda_a+z_a^{M_0\rho_a}\qquad(a\in A).$$ Choose the constants $\lambda_a$ so that no preimage of the given point is ramified. There are $\prod_{a\in A}(M_0\rho_a)$ such preimages, each with the same local intersection length. The substituted polynomials have ordinary total degree at most $M_0N$. The ordinary Bézout bound for isolated complete-intersection zeros, with their local multiplicities, bounds the sum of these lengths by $(M_0N)^k$; see (Mondal 2021, Corollary VIII.3, p. 144). The multiplicities there are local quotient lengths, unchanged by completion (Mondal 2021, sec. IV.4.2). Dividing gives (2.6). This application concerns isolated zeros only and permits other components elsewhere.

Combining (2.5) and (2.6) proves the result. Neither the polynomials nor the possibly varying component enters the constant in (2.4). ◻

### The curve inequality

Choose a positive rational number $\sigma$ sufficiently small that $$\begin{equation}
\tag{2.7}
 \begin{split}
 (1+3\sigma)^{m+1}K(w_0/v_0)\theta^m&<1,\\
 (1+3\sigma)^mK\theta^m&<1,\\
 (1+\sigma)\theta&<1.
 \end{split}
\end{equation}$$ This choice is possible by (2.1). Set $v_i=w_i/\theta$ for $i>0$. Fix $L_0=m+2$ and put $$\begin{equation}
\tag{2.8}
 C_* =\max_{1\le k\le m}2k!(L_0/\sigma)^k.
\end{equation}$$ We choose the positive weights successively so that for every pair of subsets $A,B\subseteq\{0,\ldots,m\}$ of the same cardinality between $1$ and $m$, $$\begin{equation}
\tag{2.9}
 \prod_{a\in A}w_a>C_*\prod_{b\in B}v_b
\end{equation}$$ whenever the largest positive index in their symmetric difference belongs to $A$.

Here and below a condition involving that largest index is imposed only when a positive index does differ. The successive choice is possible: if this largest index is $i$, the ratio in (2.9) is $w_i$ times a positive expression in the already chosen lower weights and the fixed zeroth weights. Every higher index occurs in both sets or in neither; in the former case its ratio is $w_j/v_j=\theta$. Hence the expression is independent of all higher weights. There are finitely many pairs of sets. A sufficiently large choice of $w_i$ enforces all conditions whose largest differing index is $i$, and subsequent choices do not disturb them. This construction involves no interpolation point.

Let $C$ be an irreducible algebraic curve whose generic point lies in the affine coordinate chart. Such a curve has a smooth projective model over $\mathbb C$; see (The Stacks Project Authors 2026, Theorem 53.2.6 and Lemma 53.2.8, Tag 0BXX). On that model define $$\begin{equation}
\tag{2.10}
 \deg_W C=
 \sum_P\max\left\{0,-\frac{\operatorname{ord}_P Y}{w_0},
                  -\frac{\operatorname{ord}_P X_1}{w_1},\ldots,
                  -\frac{\operatorname{ord}_P X_m}{w_m}\right\}.
\end{equation}$$ The order of an identically zero coordinate is understood as $+\infty$; it contributes no pole. At a branch $P$ through $a_j$, set $$\begin{equation}
\tag{2.11}
 h_P=\min\left\{
 \frac{\operatorname{ord}_P(Y-1)}{v_0},
 \frac{\operatorname{ord}_P(X_1-c_{j1}-\log Y)}{v_1},\ldots,
 \frac{\operatorname{ord}_P(X_m-c_{jm}-\log Y)}{v_m}
 \right\}.
\end{equation}$$ The logarithm here is its formal expansion at $Y=1$. All entries have positive order, possibly infinite, and their minimum is finite on a nonconstant curve.

**Proposition 2.3** (Curve inequality). *With the weights chosen above, every such curve satisfies $$\begin{equation}
\tag{2.12}
 \deg_W C\ge(1+\sigma)\sum_{P\mapsto a_j}h_P,
\end{equation}$$ where the sum includes all branches through the prescribed points.*

*Proof.* There is nothing to prove if the curve misses all the points. Suppose instead that (2.12) fails. For every sufficiently large auxiliary integer $N$, linear algebra gives a nonzero polynomial $F_N$ of $W$-degree at most $N$ whose expansions at all the points have $V$-order at least $(1+3\sigma)N$. Indeed, the number of its coefficients has leading term $$\frac{N^{m+1}}{(m+1)!\prod_{a=0}^m w_a},$$ whereas the number of conditions has leading term $$\frac{K(1+3\sigma)^{m+1}N^{m+1}}
      {(m+1)!\prod_{a=0}^m v_a}.$$ Their comparison is the first inequality in (2.7). This argument requires no independence among the conditions.

On the open set $Y\ne0$ consider the commuting frame $$\begin{equation}
\tag{2.13}
 D_0=Y\partial_Y+\sum_{i=1}^m\partial_{X_i},\qquad
 D_i=\partial_{X_i}\quad(1\le i\le m).
\end{equation}$$ It preserves polynomial degree at most $N$. In the formal coordinates of (2.2), $$D_0=(1+t)\partial_t,\qquad D_i=\partial_{u_i}.$$ Thus differentiation by $D_a$ decreases weighted order by at most $v_a$. Every $D^\gamma F_N$ with $\sum_av_a\gamma_a\le\sigma N$ retains order at least $(1+2\sigma)N$ at each point. On a branch $P$, its order is consequently at least $(1+2\sigma)N h_P$.

A polynomial of $W$-degree at most $N$ restricts to a rational function on the complete model of $C$ with total pole degree at most $N\deg_W C$. Since we assumed that (2.12) fails, the just obtained total zero order exceeds this pole bound. The ordinary divisor equality for a nonzero rational function therefore forces $$\begin{equation}
\tag{2.14}
 D^\gamma F_N\big|_C=0
 \qquad\left(\sum_av_a\gamma_a\le\sigma N\right).
\end{equation}$$ All the assertions about branch orders hold for formal power series: each monomial has order at least its weight times $h_P$, and cancellation can only increase the order.

We have converted excess contact into vanishing of many derivatives on $C$. We next find a component on which that vanishing persists, as in the derivative-ideal method of zero estimates (Philippon 1986, sec. 5), and compare all its normal bases. Put $\delta=\sigma N/L_0$. For $0\le r\le L_0$, let $V_r$ be the common zero set in $Y\ne0$ of the derivatives of cost at most $r\delta$. Let $C^\circ$ be the part of $C$ in this affine open set. The $V_r$ form a decreasing chain, and (2.14) puts $C^\circ$ in $V_{L_0}$. Choose an irreducible component of $V_{L_0}$ containing $C^\circ$, and extend it backwards to nested irreducible components of the earlier $V_r$. Every selected component has dimension between $1$ and $m$: it contains a curve, and it lies in the proper zero set of $F_N$. Since there are $L_0+1=m+3$ levels, two adjacent selected components coincide. Denote this persistent component by $Z$, and write $k=\operatorname{codim}Z$.

Take the derivatives of cost at most $r\delta$ as the equations of the earlier of these two levels. Any further derivative of cost less than $\delta$ vanishes along $Z$, because the fields commute and $Z$ is also a component at the next level. Lemma 2.2, with $\varepsilon=\sigma/L_0$, gives $$\begin{equation}
\tag{2.15}
 \prod_{a\in A}w_a\le C_*\prod_{b\in B}v_b
\end{equation}$$ for every coordinate normal basis $A$ and every frame normal basis $B$. The equations and $Z$ may vary with $N$; the uniformity proved in Lemma 2.2 is exactly what permits this use.

We show that $Y$ is constant on $Z$, working on the common smooth open subset where all the normal-basis conditions hold. Suppose first that some positive coordinate direction is nontangent to $Z$, and choose the largest such index $i$. Every larger positive index occurs in neither kind of normal basis, since $D_j=\partial_{X_j}$ for $j>0$. Some coordinate normal basis $A$ contains $i$. If a frame normal basis $B$ omitted $i$, the largest positive index where these sets differ would be $i$. Then (2.9) would contradict (2.15). Thus every frame normal basis contains $D_i$.

The other frame vectors consequently fail to span the normal quotient. Their ambient span is the hyperplane $$\ker(dX_i-dY/Y).$$ For an ambient hyperplane $Q$ and a tangent space $T$, the image of $Q$ in the quotient by $T$ fails to be surjective precisely when $T\subseteq Q$. We obtain $$\begin{equation}
\tag{2.16}
 dX_i=dY/Y\quad\text{on }Z.
\end{equation}$$ This identity forces $Y$ to be constant on the algebraic variety $Z$. Indeed, if $Y$ were nonconstant, choose a smooth point where $dY\ne0$ and intersect with general algebraic hyperplanes through that point until a curve remains on which $Y$ is nonconstant. On the smooth complete model of this curve, (2.16) is an identity of meromorphic differentials. A nonconstant meromorphic function $Y$ has a zero or pole, where $dY/Y$ has nonzero residue $\operatorname{ord}_P Y$. An exact differential $dX_i$ has zero residue at every point. This is a contradiction. It follows also that $X_i$ is constant, since $dX_i=0$ in characteristic zero.

If instead every positive coordinate direction is tangent, the $m$ independent vectors $\partial_{X_i}$ all lie in the tangent space of $Z$. Properness forces that tangent space to be their span, and $dY=0$ on $Z$ again. We conclude in all cases that $Y$ is constant on $Z$. Since $C^\circ\subseteq Z$ meets a prescribed point with $Y=1$, we have $Y=1$ on $C^\circ$, and hence on $C$ by density.

It remains to rule out a violating curve in that fiber. We work with $C^\circ$ in the affine fiber $Y=1$, while computing orders and degrees on the complete model of $C$ as before. In this fiber, the degree weights are $w_i$, the order weights are $v_i=w_i/\theta$, and $h_P=\min_i\operatorname{ord}_P(X_i-c_{ji})/v_i$. Choose a new auxiliary polynomial in these $m$ variables. The ratio of the number of vanishing conditions to the number of coefficients now tends to $K(1+3\sigma)^m\theta^m<1$, by the second inequality in (2.7). Thus, for sufficiently large $N$, there is a nonzero polynomial $G_N(X_1,\ldots,X_m)$ of weighted degree at most $N$ and order at least $(1+3\sigma)N$ at every center.

An ordinary partial derivative of cost at most $\sigma N$ still has order at least $(1+2\sigma)N$ at every center and degree at most $N$. The same zero–pole comparison on $C$ therefore gives $$\partial_X^\gamma G_N\big|_C=0
 \qquad\left(\sum_{i=1}^m v_i\gamma_i\le\sigma N\right).$$ If $m=1$, this is already impossible: a nonzero polynomial on the affine line cannot vanish on a curve. Suppose henceforth that $m\ge2$. For $0\le r\le L_0$, let $U_r$ be the common zero set in this fiber of the partial derivatives of $G_N$ of cost at most $r\delta$, with $\delta=\sigma N/L_0$ as before. The curve $C^\circ$ lies in $U_{L_0}$. Choose nested irreducible components containing $C^\circ$ backwards through this chain. Their dimensions lie between $1$ and $m-1$, since $G_N$ is nonzero, so two adjacent components coincide in a component $Z'$. Its codimension in the fiber satisfies $1\le k\le m-1$.

For the equations at the earlier of these two levels, every further partial derivative of cost less than $\delta$ vanishes on $Z'$. Lemma 2.2, again with $\varepsilon=\sigma/L_0$, therefore gives (2.15) for $Z'$, with the same $C_*$ and with normal-basis index sets contained in $\{1,\ldots,m\}$.

Here the coordinate and frame bases are the same. They must have a unique index set: two different basis sets could be ordered so that the largest differing index belongs to $A$, contradicting (2.9). The codimension is positive, so this unique normal basis has some index $i$. The other coordinate directions fail to span the normal quotient; hence the tangent space is contained in $\ker dX_i$, and $X_i$ is constant on $Z'$. Coordinatewise distinctness shows that $Z'$ meets at most one prescribed point. Every prescribed point of $C$ belongs to $C^\circ\subseteq Z'$, so the same holds for $C$.

Let that point be $a_j$. Choose a coordinate $X_l$ nonconstant on $C$. The nonzero rational function $X_l-c_{jl}$ has total pole degree at most $w_l\deg_W C$, and at each branch through $a_j$ it has order at least $(w_l/\theta)h_P$. Therefore $$\deg_W C\ge\theta^{-1}\sum_{P\mapsto a_j}h_P
             >(1+\sigma)\sum_{P\mapsto a_j}h_P,$$ by the last inequality in (2.7). This final contradiction proves (2.12). ◻

### From the curve inequality to all coefficient packets

We complete the proof of Theorem 2.1. The argument uses ordinary projective schemes and the ordinary blow-up; smoothness or normality of the compactification will not be needed. Curve positivity and asymptotic jet generation are closely related in the Seshadri-constant approach of (Demailly 1992, sec. 6). Here we supply the passage for our weighted ideals at several points, including the eventual ordinary-power comparison required on a possibly singular scheme.

Choose an integer $R$ sufficiently large that $R/w_a$ and $R/v_a$ are positive integers for every index. Embed affine space by all monomials of $W$-degree at most $R$, including the constant monomial, and let $X$ be the projective closure of the image. Since these monomials include each coordinate, the chart of the constant monomial is precisely the original affine space. Let $L=\mathcal O_X(1)$, a very ample line bundle.

For any curve meeting this chart, $$\begin{equation}
\tag{2.17}
 \deg(L|_C)=R\deg_W C.
\end{equation}$$ To see this on its smooth complete model, at each point clear the largest pole of the homogeneous monomial coordinates. Every monomial has pole order at most $R$ times the maximum in (2.10). A pure power of one coordinate attains that bound whenever the maximum is positive, and the constant monomial attains it when the maximum is zero. The resulting sections have no common zero, proving (2.17).

To make the local data algebraic, replace $\log(1+t)$ in each coordinate by a fixed Taylor polynomial $G_i(t)$ whose omitted terms have $t$-weight strictly greater than $v_i$. Then $$t=Y-1,\qquad u_i'=X_i-c_{ji}-G_i(t)$$ are regular local coordinates at $a_j$. This replacement preserves $h_P$. Indeed, if $t$ is not identically zero on a branch, each omitted term has order divided by $v_i$ strictly larger than $\operatorname{ord}_P(t)/v_0$; if $t$ is identically zero, its tail vanishes. It also preserves interpolation surjectivity for every threshold: the formal coordinate change fixes $t$ and changes $u_i$ only by terms of weight greater than $v_i$. It and its inverse preserve the weighted filtration and induce inverse triangular maps on each finite coefficient packet.

At $a_j$ form the finite-colength ideal $$I_j=\left(t^{R/v_0},(u_1')^{R/v_1},\ldots,(u_m')^{R/v_m}\right).$$ The points are distinct. These local ideals, together with the unit ideal away from the points, define a coherent ideal sheaf $I$ on $X$. For a branch through a center, $$\begin{equation}
\tag{2.18}
 \operatorname{ord}_P I
 =\min_a\left\{(R/v_a)\operatorname{ord}_P z_a\right\}
 =Rh_P,
 \qquad z_0=t,\quad z_i=u_i'.
\end{equation}$$ Let $p:X'\to X$ be the ordinary blow-up of $I$, namely the relative Proj of its Rees algebra, and write $$I\mathcal O_{X'}=\mathcal O_{X'}(-E).$$ The scheme $X$ is integral and Noetherian, $I$ is a coherent nonzero ideal, and $E$ is an effective Cartier divisor. The tautological bundle $\mathcal O_{X'}(-E)$ is relatively ample; these are the standard blow-up properties in (The Stacks Project Authors 2026, Tags 02OS, 02ND, and 02NS).

Write $A=p^*L$ in additive divisor notation. We claim that $$\begin{equation}
\tag{2.19}
 A-(1+\sigma)E\quad\text{is nef}.
\end{equation}$$ For a noncontracted integral curve $\Gamma$ upstairs whose image meets the affine chart, the map to its image is birational, since $p$ is an isomorphism away from the finite center. On the complete normalizations, (2.17) and (2.18) give $$A\cdot\Gamma=R\deg_W p(\Gamma),\qquad
 E\cdot\Gamma=R\sum_{P\mapsto a_j}h_P.$$ Proposition 2.3 gives the desired nonnegative degree. A curve whose image misses the affine chart avoids the exceptional divisor. A contracted curve has $A$-degree zero and positive degree for $-E$ by relative ampleness. These cases account for every integral curve, proving (2.19).

For sufficiently large $a>1$, the divisor $aA-E$ is ample. One can see this directly: choose $b$ so that $I\otimes L^b$ is globally generated. The Rees construction embeds $X'$ in a product $X\times\mathbb P^r$, with the second hyperplane bundle restricting to $bA-E$. Tensoring with the first very ample bundle makes $(b+1)A-E$ ample. Now the identity $$\begin{equation}
\tag{2.20}
 A-E=
 \frac{a-1}{a(1+\sigma)-1}\bigl(A-(1+\sigma)E\bigr)
 +\frac{\sigma}{a(1+\sigma)-1}(aA-E)
\end{equation}$$ expresses $A-E$ as a positive multiple of a nef class plus a positive multiple of an ample class. It is therefore ample; see (Lazarsfeld 2004, Corollary 1.4.10). This theorem applies to projective schemes and does not require a smooth blow-up.

For all sufficiently large $n$, the graded-piece and relative vanishing theorems for the ordinary Rees algebra give $$\begin{equation}
\tag{2.21}
 p_*\mathcal O_{X'}(-nE)=I^n,\qquad
 R^q p_*\mathcal O_{X'}(-nE)=0\quad(q>0).
\end{equation}$$ Indeed, on any affine open of the Noetherian base the Rees algebra is a Noetherian graded algebra generated in degree one. Its sufficiently high graded pieces recover the sections of its associated sheaf on Proj, and the higher cohomology of those twists vanishes. A finite affine cover gives one common threshold; see (The Stacks Project Authors 2026, Tags 0AG6 and 0AG7). In particular, (2.21) uses ordinary powers $I^n$, not their integral closures, and makes no assertion about small $n$.

By the projection formula, Leray, and Serre vanishing for the ample line bundle $A-E$, $$\begin{equation}
\tag{2.22}
 H^1(X,I^n\otimes L^n)
 =H^1(X',\mathcal O_{X'}(n(A-E)))=0
\end{equation}$$ for all sufficiently large $n$; see (The Stacks Project Authors 2026, Tag 0B5U). The exact sequence for $I^n$ consequently gives a surjection from $H^0(X,L^n)$ onto all its local coefficient data modulo $I^n$. The constant projective coordinate trivializes $L$ on the affine chart. Finite-colength local quotients are unchanged by completion, so these algebraic classes are also the formal coefficient data used in the theorem. In these trivializations, every element of $I^n$ has weighted order at least $nR$, because every displayed generator of $I$ has weight $R$. Thus $$\begin{equation}
\tag{2.23}
 I^n\subseteq\{\text{local series of weight at least }nR\}.
\end{equation}$$ Surjectivity modulo $I^n$ therefore implies surjectivity onto the smaller quotient consisting of the desired packets of weight less than $nR$. Equality in (2.23) is not needed.

Finally, every section of $L^n$ for sufficiently large $n$ is supplied by a homogeneous degree-$n$ polynomial in the projective embedding coordinates. This follows from Serre vanishing applied to the homogeneous ideal sheaf of $X$ in its projective space. Such a polynomial restricts on the affine chart to one of $W$-degree at most $nR$. Taking $H=nR$ and undoing the filtered Taylor-polynomial coordinate change proves the surjectivity in (2.2), and completes the proof of Theorem 2.1.

## The arithmetic and analytic determinant estimates

Interpolation now supplies the algebraic rank needed for an interpolation determinant, in the sense of (Laurent 1991, sec. 6). We estimate one full-row minor from below arithmetically, and then translate its rows to exact logarithmic periods to obtain an analytic upper bound.

Throughout this section all parameters except $H$ are fixed. Write $$w\alpha=\sum_{i=1}^m w_i\alpha_i,
 \qquad w_* =\min_{1\le i\le m}w_i,
 \qquad \omega=2\pi\mathrm i.$$ Let $\nu>2$, and suppose that integers $p_i$ and $q_i\ge2$ satisfy $$\begin{equation}
 \left|\pi-\frac{p_i}{q_i}\right|\le q_i^{-\nu},
 \qquad w_i=\lceil\log q_i\rceil,
 \qquad r_i=\frac{2\mathrm ip_i}{q_i}
 \quad(1\le i\le m).
 \tag{3.1}
\end{equation}$$ Assume that $p_i\ne0$ and that $m,K,w_0,v_0,\theta,w_1,\ldots,w_m$ satisfy the hypotheses of Theorem 2.1, with centers $c_{ji}=jr_i$, $0\le j<K$. In particular $w_i$ is a positive integer for $i>0$, while $w_0$ and $v_0$ are positive rational numbers. Fix $F_0>2/\theta$, and put $$\begin{equation}
 T_i=\left\lceil\frac{F_0w_i}{v_0}\right\rceil,
 \qquad
 G_i(t)=\sum_{1\le k<T_i}\frac{(-1)^{k+1}t^k}{k}.
 \tag{3.2}
\end{equation}$$ Empty sums are zero. The first omitted term has weight $v_0T_i\ge F_0w_i>w_i/\theta$. Consequently the substitution $u_i\mapsto u_i+G_i(t)-\log(1+t)$ is an invertible substitution preserving the weighted filtration. It induces an invertible map on every finite space of coefficients of weight less than $H$. Thus replacing the logarithms in Theorem 2.1 by these $G_i$ preserves surjectivity.

### A full-row-rank minor and its arithmetic size

Use the monomials $$P(Y,X)=Y^hX^\alpha,
 \qquad h\in\mathbb Z_{\ge0},\quad \alpha\in\mathbb Z_{\ge0}^m,
 \qquad w_0h+w\alpha\le H$$ as columns, and the triples $$\rho=(j,s,\beta),\qquad
 0\le j<K,\quad s\in\mathbb Z_{\ge0},\quad\beta\in\mathbb Z_{\ge0}^m,
 \qquad v_0s+\frac{w\beta}{\theta}<H$$ as rows. The matrix entry is the coefficient of $t^su^\beta$ in $$\begin{equation}
 P\bigl(1+t,jr_1+G_1(t)+u_1,\ldots,jr_m+G_m(t)+u_m\bigr).
 \tag{3.3}
\end{equation}$$ For all sufficiently large, sufficiently divisible $H$, choose a square minor $\Delta_H\ne0$ using every row, as permitted by Theorem 2.1. Denote its size by $M=M_H$, and set $$\begin{equation}
 \bar b=\bar b_H=\frac{1}{MH}\sum_{\rho=(j,s,\beta)}w\beta.
 \tag{3.4}
\end{equation}$$ The elementary lattice count for a simplex gives $$\begin{equation}
 M\sim
 \frac{K\theta^mH^{m+1}}{(m+1)!\,v_0\prod_{i=1}^m w_i},
 \qquad 0\le\bar b\le\theta.
 \tag{3.5}
\end{equation}$$ Indeed, after scaling by $H$, the lattice boxes of side lengths $H^{-1}$ are Riemann sums for the fixed simplex. Its volume is $\theta^m/((m+1)!v_0\prod_iw_i)$; its boundary has volume zero, so the strict inequality in the row definition does not affect the leading term. We always let $H$ tend to infinity only after all the weights and centers have been fixed.

**Lemma 3.1** (Arithmetic lower bound). *Let $\Lambda=4\log2$, and define $$\begin{equation}
 E_{\rm ar}
 =\frac{\Lambda F_0m}{v_0}
  +\Lambda\sum_{i=1}^m\frac1{w_i}+\frac{\theta}{w_*}.
 \tag{3.6}
\end{equation}$$ Then every minor just chosen satisfies $$\begin{equation}
 \frac{\log|\Delta_H|}{MH}
 \ge -(1-\bar b)-E_{\rm ar}.
 \tag{3.7}
\end{equation}$$*

*Proof.* Let $L_i=\operatorname{lcm}(1,\ldots,T_i-1)$, interpreted as $1$ if $T_i=1$, and put $$D_H=\prod_{i=1}^m L_i^{\lfloor H/w_i\rfloor}.$$ Scale a column $Y^hX^\alpha$ by $\prod_iq_i^{\alpha_i}$ and a row $(j,s,\beta)$ by $\prod_iq_i^{-\beta_i}$. The scaled entry is zero unless $\alpha\ge\beta$ componentwise; otherwise it is $$\prod_i\binom{\alpha_i}{\beta_i}
 [t^s](1+t)^h
 \prod_i\bigl(q_i(jr_i+G_i(t))\bigr)^{\alpha_i-\beta_i}.$$ Here $q_ijr_i=2\mathrm ijp_i\in\mathbb Z[\mathrm i]$. Since $G_i$ has coefficients in $L_i^{-1}\mathbb Z$, the denominator of this entry divides $\prod_iL_i^{\alpha_i-\beta_i}$, which divides $D_H$. Thus multiplying every entry of the scaled matrix by $D_H$ gives a matrix over $\mathbb Z[\mathrm i]$ with nonzero determinant. A nonzero Gaussian integer has modulus at least one, so $$\begin{equation}
 \begin{aligned}
 \log|\Delta_H|
 &\ge -M\log D_H
      -\sum_{\text{columns }\alpha}\sum_i\alpha_i\log q_i\\
 &\quad+\sum_{\text{rows }\beta}\sum_i\beta_i\log q_i.
 \end{aligned}
 \tag{3.8}
\end{equation}$$ For each selected column, $\sum_i\alpha_i\log q_i\le w\alpha\le H$. Also $0\le w_i-\log q_i<1$, and hence $$\sum_{\text{rows }\beta}\sum_i\beta_i\log q_i
 \ge MH\bar b-\sum_{\text{rows }\beta}\sum_i\beta_i
 \ge MH\bar b-\frac{MH\theta}{w_*}.$$

For completeness, $\log\operatorname{lcm}(1,\ldots,n)\le\Lambda n$. To see this, the factorial valuation formula shows that each prime power in $(\ell,2\ell]$ contributes its logarithmic prime weight to $\log\binom{2\ell}{\ell}$; all the other contributions to the latter are nonnegative. Thus the increase of the log least common multiple across this interval is at most $2\ell\log2$. Summing over dyadic intervals up to the smallest power of two above $n$ gives at most $4n\log2$. Therefore $$\frac{\log D_H}{H}
 \le\Lambda\sum_i\frac{T_i}{w_i}
 \le\frac{\Lambda F_0m}{v_0}+\Lambda\sum_i\frac1{w_i}.$$ Substitution in (3.8) proves (3.7). ◻

### Translation to entire functions

For every multi-index $a\in\mathbb Z_{\ge0}^m$ and every selected column $P$, define the entire function $$\begin{equation}
 f_{a,P}(z)=[u^a]P(e^z,z+u_1,\ldots,z+u_m).
 \tag{3.9}
\end{equation}$$ We regard $(f_{a,P})_P$ as a row vector of entire functions, indexed by the selected columns. For $P=Y^hX^\alpha$ it has the explicit entry $$\begin{equation}
 f_{a,P}(z)=
 \begin{cases}
 \displaystyle\binom{\alpha}{a}e^{hz}z^{|\alpha|-|a|},&a\le\alpha,\\
 0,&\text{otherwise}.
 \end{cases}
 \tag{3.10}
\end{equation}$$ In particular only indices $a$ with $wa\le H$ can contribute.

**Lemma 3.2** (Exact row translation). *Every row $\rho=(j,s,\beta)$ of (3.3) is a sum of at most $$\begin{equation}
 Q_H=(\lfloor H\rfloor+1)^{2m}
          (\lfloor H/v_0\rfloor+1)
 \tag{3.11}
\end{equation}$$ scalar multiples of row vectors of the form $$\bigl([t^\ell]f_{a,P}(j\omega+\log(1+t))\bigr)_P,
 \qquad a\ge\beta,\quad wa\le H,\quad0\le\ell\le s.$$ Each scalar $\xi$ occurring with index $a$ satisfies $$\begin{equation}
 \begin{aligned}
 |\xi|&\le\exp\{-\nu w(a-\beta)+H E_{\rm tr}\},\\
 E_{\rm tr}
 &=\frac{\nu}{F_0}+\frac{\log2}{v_0}
   +\frac{\log4+\log(2K)+\nu}{w_*}.
 \end{aligned}
 \tag{3.12}
\end{equation}$$*

*Proof.* Put $$\epsilon_i=j(r_i-\omega),\qquad
 \tau_i(t)=G_i(t)-\log(1+t).$$ Since $e^{j\omega}=1$, the substitutions in (3.3) can be written as $Y=e^z$, $X_i=z+u_i+\epsilon_i+\tau_i(t)$, where $z=j\omega+\log(1+t)$. Expanding first in the variables $u_i$, then in the constants $\epsilon_i$ and tails $\tau_i$, gives the exact row vector identity $$\begin{align}
 \text{row}_{j,s,\beta}
 ={}&\sum_{\substack{a\ge\beta\\wa\le H}}
       \binom a\beta
       \sum_{0\le d\le a-\beta}\binom{a-\beta}{d}
       \epsilon^{a-\beta-d}
       \sum_{k=0}^s
       \left([t^k]\prod_i\tau_i(t)^{d_i}\right)
 \nonumber\\[-2pt]
 &\hspace{35mm}\cdot
 \bigl([t^{s-k}]f_{a,P}(j\omega+\log(1+t))\bigr)_P.
 \tag{3.13}
\end{align}$$ All scalar factors in this identity are independent of the column $P$. This is therefore an identity to which determinant multilinearity applies directly.

The product of tails vanishes to order at least $\sum_i d_iT_i$. Consequently a nonzero coefficient in (3.13) satisfies $$\begin{equation}
 \sum_i d_iw_i\le\frac{v_0}{F_0}\sum_i d_iT_i
 \le\frac{v_0s}{F_0}<\frac{H}{F_0}.
 \tag{3.14}
\end{equation}$$ On $|t|=1/2$, $$|\tau_i(t)|
 \le\sum_{k\ge T_i}\frac{2^{-k}}k\le1.$$ Cauchy’s coefficient estimate thus bounds the tail coefficient in (3.13) by $2^k\le2^s$. From (3.1), $$|\epsilon_i|\le2Kq_i^{-\nu}
 \le2K e^\nu e^{-\nu w_i}.$$ Moreover $\binom a\beta\binom{a-\beta}{d}\le4^{|a|}$ and $|a|\le H/w_*$. Combining these inequalities and using (3.14) gives $$\log|\xi|
 \le-\nu w(a-\beta)+\frac{\nu H}{F_0}
       +\frac{H\log2}{v_0}
       +\frac{H(\log4+\log(2K)+\nu)}{w_*}$$ for each nonzero scalar. A zero scalar obeys the required bound as well. Finally, each coordinate of $a$ and $d$ is at most $H$ because $w_i\ge1$, while $0\le k\le H/v_0$. This proves the term count and the Lemma. ◻

### Repeated Taylor degrees force a quadratic saving

The Taylor expansion of interpolation determinants eliminates repeated degrees (Laurent 2000, Theorem 1). Our rows fall into different transverse-index groups, so this cancellation is used only inside a fixed group. The next bound is uniform over all row choices.

**Lemma 3.3** (Collision estimate). *Choose one translated test row from each row expansion in Lemma 3.2, and remove its scalar factor. Let $T$ be the resulting square matrix, and let $n_a$ be the number of its rows with index $a$. With $$\begin{equation}
 c=\frac{\log2}{4},\qquad
 E_{\rm hol}=\frac{100K}{w_0}+\frac{\log2}{v_0}
             +\frac{\log(200K)}{w_*},
 \tag{3.15}
\end{equation}$$ there is a quantity $\rho_H\to0$, independent of all these row choices and of the selected columns, such that $$\begin{equation}
 |\det T|
 \le\exp\left\{-c\sum_a n_a^2+MH(E_{\rm hol}+\rho_H)\right\}.
 \tag{3.16}
\end{equation}$$*

*Proof.* Put $R=100K$. Equation (3.10) gives, on $|z|\le R$, $$|f_{a,P}(z)|\le
 \exp\left\{H\left(\frac R{w_0}
                      +\frac{\log(2R)}{w_*}\right)\right\}
 =:\mathcal D_H.$$ Expand $$f_{a,P}(z)=\sum_{d\ge0}c_{a,d,P}(z/R)^d.$$ Cauchy’s estimate gives $|c_{a,d,P}|\le\mathcal D_H$. A row of $T$ is a test of order $\ell\le s$ at some center $j$. Since $$|j\omega+\log(1+t)|
 \le2\pi(K-1)+\log2<50K=R/2
 \qquad(|t|=1/2),$$ its value on $(z/R)^d$ has modulus at most $2^\ell2^{-d}$.

Expand the determinant in these power-series rows. The expansion is absolutely convergent: a coefficient determinant has modulus at most $M!\mathcal D_H^M$, and the sum of the product bounds $2^{-d}$ over all degrees is finite. If two rows have the same pair $(a,d)$, their coefficient vectors $(c_{a,d,P})_P$ agree, and that summand vanishes. Thus every nonzero summand has distinct degrees within each group $a$, and so $$\sum_{\text{rows}}d\ge\sum_a\binom{n_a}{2}.$$ Use half of the geometric decay for this lower bound and sum the other half freely over all nonnegative degrees. Since $\sum\ell\le MH/v_0$, this gives $$|\det T|
 \le M!\mathcal D_H^M2^{MH/v_0}
       2^{-\frac12\sum_a\binom{n_a}{2}}
       (1-2^{-1/2})^{-M}.$$ Because $\sum_a n_a=M$, the asserted inequality follows with, for example, $$\rho_H=\frac{\log M+\frac14\log2
                    -\log(1-2^{-1/2})}{H}.$$ Equation (3.5) shows that $\rho_H\to0$ with the fixed parameters stipulated above. ◻

### A comparison with two alternatives

Put $$\begin{equation}
 E_{\rm an}=E_{\rm tr}+E_{\rm hol}.
 \tag{3.17}
\end{equation}$$

Let $0<A<1$ set a cutoff $AH$ for transverse weights, and let $0<\eta<1$ be a fraction of rows. The main arithmetic cost is $1-\bar b$. In each term of the determinant expansion, if at least $\eta M$ rows have $wa\le AH$, they give a collision saving; otherwise the rows with $wa>AH$ supply approximation-error factors. We seek a saving larger than $1-\bar b+E_{\rm ar}+E_{\rm an}$, and choose $A$ and $\eta$ in Section 4.

**Proposition 3.4** (Determinant comparison). *Let $0<A<1$ and $0<\eta<1$, and define $$\begin{equation}
 g=\nu\bigl(A(1-\eta)-\theta\bigr)-(1-\theta),
 \qquad
 L=\frac{\eta^2K\theta^m}{(m+1)v_0A^m}.
 \tag{3.18}
\end{equation}$$ The approximations (3.1) and the interpolation hypotheses cannot hold simultaneously if $$\begin{equation}
 g>0,\qquad
 E_{\rm ar}+E_{\rm an}<g,
 \qquad
 cL>1+E_{\rm ar}+E_{\rm an}.
 \tag{3.19}
\end{equation}$$*

*Proof.* Let $$D_A(H)=\#\{a\in\mathbb Z_{\ge0}^m:wa\le AH\},
 \qquad L_H=\frac{\eta^2M}{H D_A(H)}.$$ The simplex count, now in dimension $m$, and (3.5) show that $$D_A(H)\sim\frac{(AH)^m}{m!\prod_iw_i},
 \qquad L_H\longrightarrow L.$$ Expand $\Delta_H$ by the row identities in Lemma 3.2. For a choice of terms with indices $a_\rho$, the product of their scalar factors has modulus at most $$\exp\left\{-\nu\sum_\rho wa_\rho
             +\nu MH\bar b+MH E_{\rm tr}\right\}.$$ There are at most $Q_H^M$ term choices. Apply Lemma 3.3 to each one.

Suppose first that at least $\eta M$ of its indices obey $wa\le AH$. There are at most $D_A(H)$ such indices, so Cauchy–Schwarz gives $$\sum_a n_a^2\ge\frac{(\eta M)^2}{D_A(H)}=MH L_H.$$ The scalar main exponent $-\nu\sum_\rho w(a_\rho-\beta_\rho)$ is nonpositive, because $a_\rho\ge\beta_\rho$. Discarding it leaves an upper bound $-cL_H+E_{\rm an}+\rho_H$ after division by $MH$.

In the other case, more than $(1-\eta)M$ indices have $wa>AH$. Hence $\sum_\rho wa_\rho\ge MH A(1-\eta)$. Discarding the nonpositive collision term leaves the upper bound $-\nu(A(1-\eta)-\bar b)+E_{\rm an}+\rho_H$. Taking absolute values before summing the determinant expansion gives $$\begin{equation}
 \begin{aligned}
 \frac{\log|\Delta_H|}{MH}
 &\le E_{\rm an}+\varepsilon_H+
       \max\{-cL_H,-\nu(A(1-\eta)-\bar b)\},\\
 \varepsilon_H&=\rho_H+\frac{\log Q_H}{H}\longrightarrow0.
 \end{aligned}
 \tag{3.20}
\end{equation}$$ All bounds here are uniform over the row-term choices.

For the second alternative, the gap between the two main exponents is at least $g$, since $\bar b\le\theta$ gives $$\nu(A(1-\eta)-\bar b)-(1-\bar b)
 =\nu A(1-\eta)-1-(\nu-1)\bar b\ge g.$$ Under (3.19), both quantities inside the maximum in (3.20), after adding $E_{\rm an}+\varepsilon_H$, are strictly less than $-(1-\bar b)-E_{\rm ar}$ for all sufficiently large $H$. For the first quantity, use $L_H\to L$ and $1-\bar b\le1$; for the second, use the displayed uniform gap. This contradicts Lemma 3.1. ◻

## Choice of parameters and proof of Theorem 1.1

We now combine the interpolation theorem and the determinant estimates. The order of choices is essential: the dimension is fixed before the approximation scales, and all these data are fixed before the polynomial degree tends to infinity.

**Lemma 4.1**. *For every real $\nu>2$, there are positive rational numbers $\theta,A,B,C$ such that $$\begin{equation}
\tag{4.1}
0<\theta<A<B<1,\qquad
\nu(A-\theta)>1-\theta,\qquad
C>1,\quad B<1/C,\quad B<C\theta<1.
\end{equation}$$ One can then choose $0<\eta<1$ such that $$\begin{equation}
\tag{4.2}
g:=\nu\bigl(A(1-\eta)-\theta\bigr)-(1-\theta)>0.
\end{equation}$$*

*Proof.* Choose a rational $b$ with $1/2<b<1-1/\nu$. For a sufficiently small positive rational $\delta$, put $\theta=1-\delta$ and $A=1-b\delta$. Then $0<\theta<A<1$, and $$\nu(A-\theta)-(1-\theta)
=\bigl(\nu(1-b)-1\bigr)\delta>0,$$ whereas $$\theta-A^2=(2b-1)\delta-b^2\delta^2>0.$$ It follows that the interval $(A/\theta,1/A)$ is nonempty. Choose a rational $C$ in this interval. Since $A>\theta$, we have $C>1$; since $\theta<A$, we also have $C\theta<\theta/A<1$. Now choose a rational $B$ between $A$ and $\min(1/C,C\theta)$. This proves (4.1). Finally, the strict inequality at $\eta=0$ allows a sufficiently small $\eta>0$ in (4.2). ◻

The two inequalities used in this construction have different roles. The inequality $\nu(A-\theta)>1-\theta$ supplies the approximation-error gap. The inequality $A^2<\theta$ permits $A/\theta<C<1/A$, and hence a choice of $B$ for which $CB<1$, $C\theta/B>1$, and $B/A>1$. With the full-simplex counts of Section 3, these three ratios make the dimension-dependent errors tend to zero while the collision saving tends to infinity. We now choose one finite dimension realizing both requirements; it will remain fixed throughout the degree limit.

*Proof of Theorem 1.1.* Fix $\nu>2$. Suppose for a contradiction that there are arbitrarily large positive integers $q$ for which some $p\in\mathbb Z$ satisfies $$\begin{equation}
\tag{4.3}
\left|\pi-\frac pq\right|\le q^{-\nu}.
\end{equation}$$ Fix $\theta,A,B,C,\eta,g$ from Lemma 4.1, and put $\varepsilon_0=\min(g/2,1/2)$. First choose $F_0>2/\theta$ so large that $\nu/F_0<\varepsilon_0/3$.

For an integer $m$, set $$\begin{equation}
\tag{4.4}
K=\lfloor C^m\rfloor,\qquad
w_0=B^{-m},\qquad
v_0=2K\theta^m w_0.
\end{equation}$$ These are admissible rational interpolation data: $$\begin{equation}
\tag{4.5}
K\theta^m\le(C\theta)^m<1,\qquad
K\frac{w_0}{v_0}\theta^m=\frac12.
\end{equation}$$ The relevant limits as $m\to\infty$ are $$\begin{equation}
\tag{4.6}
\frac{K}{w_0}\le(CB)^m\longrightarrow0,\qquad
v_0\sim2\left(\frac{C\theta}{B}\right)^m\longrightarrow\infty,
\qquad
\frac{m}{v_0}\longrightarrow0.
\end{equation}$$ With the notation of Proposition 3.4, these choices give $$\begin{equation}
\tag{4.7}
L=\frac{\eta^2K\theta^m}{(m+1)v_0A^m}
 =\frac{\eta^2(B/A)^m}{2(m+1)}\longrightarrow\infty.
\end{equation}$$ Thus, with $\Lambda=4\log2$ and $c=(\log2)/4$, choose $m$ large enough that $$\begin{equation}
\tag{4.8}
\frac{\Lambda F_0m+2\log2}{v_0}+\frac{100K}{w_0}
 <\frac{\varepsilon_0}{3},
\qquad cL>2.
\end{equation}$$ Fix this $m$, and hence $K,w_0,v_0$.

The remaining constants are now fixed. Choose approximations $p_i/q_i$ satisfying (4.3), with $w_i=\lceil\log q_i\rceil$, successively sufficiently large for Theorem 2.1 and, in addition, for $$\begin{equation}
\tag{4.9}
\Lambda\sum_{i=1}^m\frac1{w_i}
+\frac{\theta+\log4+\log(2K)+\nu+\log(200K)}{w_*}
 <\frac{\varepsilon_0}{3},
\qquad w_*=\min_{i>0}w_i.
\end{equation}$$ This is possible: first impose a sufficiently large lower bound on every $w_i$, using $\sum_i1/w_i\le m/w_*$, and then impose the successive geometric thresholds. The assumed denominators are unbounded, so every finite sequence of such requirements can be met. The thresholds for weight separation are independent of the centers. For sufficiently large $q_i$, $p_i\ne0$, and hence $c_{ji}=jr_i$, $r_i=2\mathrm ip_i/q_i$, are distinct across $j$ in each coordinate. No independence between different coordinates is required.

Using (3.6), (3.12), (3.15), and (3.17), the sum of errors is exactly $$\begin{aligned}
E_{\rm ar}+E_{\rm an}
&=\frac{\nu}{F_0}
 +\frac{\Lambda F_0m+2\log2}{v_0}+\frac{100K}{w_0}\\
&\quad +\Lambda\sum_i\frac1{w_i}
 +\frac{\theta+\log4+\log(2K)+\nu+\log(200K)}{w_*}.
\end{aligned}$$ Our three choices make this less than $\varepsilon_0$. In particular it is less than $g$, while $cL>2>1+E_{\rm ar}+E_{\rm an}$. All hypotheses of Proposition 3.4 now hold, a contradiction. The degree $H$ in that Proposition tends to infinity only after the dimension, weights, and centers just chosen are fixed.

We have excluded (4.3) for arbitrarily large $q$, for each fixed $\nu>2$. This gives the required eventual lower bound, in fact with a strict inequality. The contradiction allowed unreduced fractions and zero error. If $\pi$ were rational, exact representations with arbitrarily large denominators would contradict it; hence $\pi$ is irrational.

Finally divide the unit interval into $N$ equal parts and apply pigeonhole to $0,\pi,\ldots,N\pi$ modulo one. There exist $p\in\mathbb Z$ and $1\le q\le N$ such that $$0<\left|\pi-\frac pq\right|\le\frac1{qN}\le\frac1{q^2}.$$ After reduction, the same error is at most the inverse square of the reduced denominator. These errors tend to zero as $N\to\infty$; irrationality forces the reduced denominators to be unbounded. Every exponent less than two therefore occurs infinitely often in the defining inequality. Hence $\mu(\pi)\ge2$, and the upper bound already proved gives $\mu(\pi)=2$. ◻

## Flint–Hills series and its generalization

We first prove Corollary 1.2. Alekseyev showed that convergence of the classical Flint–Hills series requires $\mu(\pi)\le5/2$ (Alekseyev 2011, Corollary 4); Meiburg proved that $\mu(\pi)<5/2$ is sufficient (Meiburg 2022, Theorem 2.5). We include the short spacing argument needed for the consequence of Theorem 1.1. Write $\|x\|=\min_{p\in\mathbb Z}|x-p|$ for distance to the nearest integer.

**Lemma 5.1** (Dyadic spacing estimate). *Let $\alpha>0$ be irrational. Suppose that, for some $c>0$ and $1<\nu<5/2$, $$\|q\alpha\|\ge c q^{1-\nu}\qquad(q\in\mathbb Z,\ q\ge1).$$ Then $$\sum_{q=1}^{\infty}\frac{1}{q^3\|q\alpha\|^2}<\infty.$$*

*Proof.* Fix a positive integer $K$, and put $d=c(2K)^{1-\nu}$. For $K\le q<2K$, the points $q\alpha$ on the circle $\mathbb R/\mathbb Z$ have distance at least $d$ from zero. Two distinct such points also have circle distance at least $d$: apply the hypothesis to their nonzero integer difference, whose absolute value is less than $2K$, and use $1-\nu<0$.

On either half-circle starting at zero, arrange the distances in increasing order. Their first distance is at least $d$, and each successive distance increases by at least $d$. Thus these distances are at least $d,2d,3d,\ldots$. No positive integer multiple of $\alpha$ lies at either endpoint of a half-circle. Consequently $$\sum_{K\le q<2K}\frac{1}{q^3\|q\alpha\|^2}
 \le \frac{2}{K^3d^2}\sum_{j=1}^{\infty}\frac{1}{j^2}
 =O\bigl(K^{2\nu-5}\bigr).$$ The implied constant depends only on $c$ and $\nu$. Since $2\nu-5<0$, summing over $K=1,2,4,\ldots$ proves the assertion. ◻

*Proof of Corollary 1.2.* Fix a real number $\nu$ with $2<\nu<5/2$, and choose a positive integer $Q$ as in Theorem 1.1. Taking a nearest integer numerator in that theorem gives $$\|q\pi\|\ge q^{1-\nu}\qquad(q\ge Q).$$ The same theorem has established irrationality of $\pi$. Hence $$c=\min\left(\{1\}\cup
       \left\{q^{\nu-1}\|q\pi\|:q\in\mathbb Z,\ 1\le q<Q\right\}\right)>0.$$ It follows that $\|q\pi\|\ge c q^{1-\nu}$ for every positive integer $q$, including the finitely many exceptions below $Q$. Lemma 5.1 therefore gives $$\begin{equation}
\tag{5.1}
 \sum_{q=1}^{\infty}\frac{1}{q^3\|q\pi\|^2}<\infty.
\end{equation}$$

For each positive integer $n$, choose a nearest nonnegative integer $q$ to $n/\pi$, and group the integers $n$ by $q$. Then $|n-q\pi|\le\pi/2$. The group with $q=0$ is finite, and its terms in the Flint–Hills series are finite because irrationality of $\pi$ excludes $\sin n=0$ for a positive integer $n$. For each $q\ge1$, its group lies in an interval of length $\pi<4$, so contains at most four integers. Every integer in that group satisfies $$n\ge\pi(q-1/2)\ge\frac{\pi q}{2}.$$ Concavity of sine on $[0,\pi/2]$ also gives $$|\sin n|=|\sin(n-q\pi)|
 \ge\frac{2}{\pi}|n-q\pi|
 \ge\frac{2}{\pi}\|q\pi\|.$$ The contribution of the group indexed by $q\ge1$ is consequently at most $$\frac{8}{\pi}\frac{1}{q^3\|q\pi\|^2}.$$ Summing this bound and using (5.1) proves convergence of $\sum_{n\ge1}n^{-3}\sin^{-2}n$, with angles in radians. ◻

The same spacing argument gives the convergence criterion for the two-parameter family.

**Corollary 5.2** (Generalized Flint–Hills series). *For fixed real numbers $a,b>0$, the series $$\sum_{n=1}^{\infty}\frac{1}{n^a|\sin n|^b}$$ with angles in radians converges if and only if $a>\max\{1,b\}$.*

*Proof.* Suppose first that $a>\max\{1,b\}$, and choose $\varepsilon>0$ so that $a>\max\{1,b\}+b\varepsilon$. Theorem 1.1, with the finitely many exceptional denominators absorbed into a positive constant as above, gives $\|q\pi\|\ge c_\varepsilon q^{-1-\varepsilon}$ for all $q\ge1$. For an integer $K\ge1$, put $d=c_\varepsilon(2K)^{-1-\varepsilon}$. As in the proof of Lemma 5.1, the points $q\pi$ on $\mathbb R/\mathbb Z$ with $K\le q<2K$ are mutually $d$-separated and at least $d$ from zero. There are at most $K$ points, so the half-circle ordering gives $$\sum_{K\le q<2K}\frac{1}{q^a\|q\pi\|^b}
 \le 2K^{-a}d^{-b}\sum_{j=1}^{K}j^{-b}
 \ll_{a,b,\varepsilon}
 \begin{cases}
 K^{1-a+b\varepsilon},&0<b<1,\\
 K^{1-a+\varepsilon}\log(2K),&b=1,\\
 K^{b-a+b\varepsilon},&b>1.
 \end{cases}$$ Each power of $K$ is negative by the choice of $\varepsilon$; summing over $K=1,2,4,\ldots$, including the logarithmic factor when $b=1$, proves convergence of $\sum_{q\ge1}q^{-a}\|q\pi\|^{-b}$. Use the same nearest-multiple groups as in the preceding proof. The $q=0$ group is finite, while the group indexed by $q\ge1$ contributes at most $$4(2/\pi)^a(\pi/2)^b q^{-a}\|q\pi\|^{-b}.$$ This proves the required convergence.

If $a\le1$, including the boundary $a=1$, then $|\sin n|\le1$ compares the series from below with the divergent series $\sum n^{-a}$. It remains to consider $1<a\le b$. Let $p_j/q_j$ be the continued-fraction convergents to $\pi$, whose positive integer numerators tend to infinity. They satisfy $$|\sin p_j|=|\sin(p_j-\pi q_j)|
 \le|p_j-\pi q_j|<q_j^{-1}.$$ Since $p_j/q_j\to\pi$, eventually $p_j\le(\pi+1)q_j$, and hence $$\frac{1}{p_j^a|\sin p_j|^b}
 >p_j^{-a}q_j^b\ge(\pi+1)^{-b}p_j^{b-a}.$$ These summands are bounded away from zero when $a=b$, and tend to infinity when $a<b$. Thus the series also diverges throughout $1<a\le b$, including its boundary $a=b>1$. ◻

## References

Alekseyev, Max A. 2011. *On Convergence of the Flint Hills Series*. arXiv:1104.5100v1 $$math.CA$$. <https://arxiv.org/abs/1104.5100v1>.

Bai, Yufei. 2026. *The Irrationality Measure of $\pi$ Is at Most $7.101862832357$*. arXiv:2609.11276v2 $$math.NT$$. <https://doi.org/10.48550/arXiv.2609.11276>.

Carella, N. A. 2022. *Irrationality Measure of Pi*. arXiv:1902.08817v10 $$math.GM$$. <https://doi.org/10.48550/arXiv.1902.08817>.

Chudnovsky, G. V. 1982. “Hermite–Padé Approximations to Exponential Functions and Elementary Estimates of the Measure of Irrationality of $\pi$.” In *The Riemann Problem, Complete Integrability and Arithmetic Applications*, edited by D. V. Chudnovsky and G. V. Chudnovsky, vol. 925. Lecture Notes in Mathematics. Springer. <https://doi.org/10.1007/BFb0093516>.

Dan, Yuya. 2026. *Critical Convergence and Hausdorff Measures for Generalized Flint Hills Series*. arXiv:2609.12338v1 $$math.NT$$. <https://doi.org/10.48550/arXiv.2609.12338>.

Demailly, Jean-Pierre. 1992. “Singular Hermitian Metrics on Positive Line Bundles.” In *Complex Algebraic Varieties*, edited by Klaus Hulek, Thomas Peternell, Michael Schneider, and Frank-Olaf Schreyer, vol. 1507. Lecture Notes in Mathematics. Springer. <https://doi.org/10.1007/BFb0094512>.

Farhi, Bakir. 2006. *Un Lemme de Roth Sur Les Groupes Algébriques Commutatifs*. arXiv:math/0603257v1 $$math.NT$$. <https://arxiv.org/abs/math/0603257v1>.

Hata, Masayoshi. 1993. “Rational Approximations to $\pi$ and Some Other Numbers.” *Acta Arithmetica* 63 (4): 335–49. <https://doi.org/10.4064/aa-63-4-335-349>.

Laurent, Michel. 1991. “Sur Quelques résultats récents de Transcendance.” *Astérisque* 198-199-200: 209–30. <https://www.numdam.org/item/AST_1991__198-199-200__209_0/>.

Laurent, Michel. 2000. “Interpolation Determinants of Exponential Polynomials.” *Publicationes Mathematicae Debrecen* 56 (3-4): 457–73. <https://doi.org/10.5486/PMD.2000.2310>.

Lazarsfeld, Robert. 2004. *Positivity in Algebraic Geometry I: Classical Setting: Line Bundles and Linear Series*. Vol. 48. Ergebnisse Der Mathematik Und Ihrer Grenzgebiete, 3. Folge. Springer-Verlag. <https://doi.org/10.1007/978-3-642-18808-4>.

López Zapata, Carlos H. 2026. *A Continued-Fraction Criterion for the Flint Hills Series, and the Integer Sequences It Generates*. arXiv:2603.09719v5 $$math.GM$$. <https://doi.org/10.48550/arXiv.2603.09719>.

Mahler, Kurt. 1953. “On the Approximation of $\pi$.” *Proceedings of the Koninklijke Nederlandse Akademie van Wetenschappen, Series A* 56: 30–42. <https://ems.press/books/dms/252/4986>.

Mantzakouras, Nikos, and Carlos López Zapata. 2025. *Diophantine FLINT-HILLS Series*. arXiv:2502.03474v2 $$math.GM$$. <https://doi.org/10.48550/arXiv.2502.03474>.

Meiburg, Alex. 2022. *Bounds on Irrationality Measures and the Flint-Hills Series*. arXiv:2208.13356v1 $$math.NT$$. <https://arxiv.org/abs/2208.13356v1>.

Mignotte, Maurice. 1974. “Approximations Rationnelles de $\pi$ Et Quelques Autres Nombres.” In *Journées Arithmétiques (Grenoble, 1973)*. Bulletin de La Société Mathématique de France. Mémoire 37. Société mathématique de France. <https://doi.org/10.24033/msmf.139>.

Mondal, Pinaki. 2021. *How Many Zeroes? Counting the Number of Solutions of Systems of Polynomials via Geometry at Infinity (Draft III)*. arXiv:1806.05346v5 $$math.AG$$. <https://arxiv.org/abs/1806.05346v5>.

Philippon, Patrice. 1986. “Lemmes de zéros Dans Les Groupes Algébriques Commutatifs.” *Bulletin de La Société Mathématique de France* 114: 355–83. <https://doi.org/10.24033/bsmf.2060>.

Roth, K. F. 1960. “Rational Approximations to Algebraic Numbers.” In *Proceedings of the International Congress of Mathematicians 1958*, edited by J. A. Todd. Cambridge University Press. <https://www.mathunion.org/fileadmin/ICM/Proceedings/ICM1958/ICM1958.ocr.pdf>.

Salikhov, V. Kh. 2008. “On the Irrationality Measure of $\pi$.” *Russian Mathematical Surveys* 63 (3): 570–72. <https://doi.org/10.1070/RM2008v063n03ABEH004543>.

Salikhov, V. Kh. 2010. “On the Measure of Irrationality of the Number $\pi$.” *Mathematical Notes* 88 (4): 563–73. <https://doi.org/10.1134/S0001434610090294>.

The Stacks Project Authors. 2026. *The Stacks Project*. <https://stacks.math.columbia.edu>.

Waldschmidt, Michel. 2004. “Open Diophantine Problems.” *Moscow Mathematical Journal* 4 (1): 245–305. <https://webusers.imj-prg.fr/~michel.waldschmidt/articles/pdf/odp.pdf>.

Zeilberger, Doron, and Wadim Zudilin. 2020. “The Irrationality Measure of $\pi$ Is at Most 7.103205334137….” *Moscow Journal of Combinatorics and Number Theory* 9 (4): 407–19. <https://doi.org/10.2140/moscow.2020.9.407>.

Zudilin, Wadim. 2004. *An Essay on Irrationality Measures of $\pi$ and Other Logarithms*. arXiv:math/0404523 $$math.NT$$. <https://arxiv.org/abs/math/0404523>.

[^1]: In the notation of (Carella 2022, Theorem 8.1, Equations (52) and (55)), let $C=p_{n+1}-\pi q_{n+1}-1/q_n$. The convergent estimate $\lvert p_{n+1}-\pi q_{n+1}\rvert<1/q_{n+2}<1/q_n$ gives $-2/q_n<C<0$. Thus $\sin C<0$ for large $n$, contrary to the positive lower bound in that argument. This objection concerns the displayed proof of the stronger assertion; it does not decide the exponent-two claim or the truth of the stronger conclusion.
