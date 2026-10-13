# Modularity of elliptic curves over imaginary quadratic fields

OpenAI

## Abstract

We prove the modularity conjecture for elliptic curves over imaginary quadratic fields: every such curve is modular, with matching local parameters at every place.

## Introduction

Let $K$ be an imaginary quadratic number field and let $E/K$ be an elliptic curve. The automorphy conjecture for $E$ asks for an automorphic representation of $\mathop{\mathrm{GL}}_2(\mathbb A_K)$ whose local parameters realize the cohomology of $E$. At a place of good reduction this requires the Hecke polynomial to recover the point count of the reduced curve; at a bad place it requires the full local parameter, including its inertia and monodromy. At infinity the parameter is prescribed by the Hodge types $(1,0)$ and $(0,1)$.

We prove this conjecture for every $K$ and $E$. We use unitary normalization on the automorphic side and the Tate-normalized local Langlands correspondence on the cohomological side. These conventions are recalled in Section 2.

**Theorem 1.1**. *Let $K$ be an imaginary quadratic number field and $E/K$ an elliptic curve. There is an isobaric automorphic representation $\pi_E$ of $\mathop{\mathrm{GL}}_2(\mathbb A_K)$ with trivial central character and weight zero such that, for every prime $l$ and every isomorphism $\iota:\overline{\mathbb Q}_l\xrightarrow{\sim}\mathbb C$, $$r_\iota(\pi_E)\simeq
 H^1_{\mathrm{\acute et}}(E_{\overline K},\overline{\mathbb Q}_l).$$ At every finite place $v\nmid l$ one has $$\iota\mathop{\mathrm{WD}}\bigl(H^1_{\mathrm{\acute et}}(E_{\overline K},\overline{\mathbb Q}_l)
                     |_{G_{K_v}}\bigr)^{\mathrm{F\text{-}ss}}
 \simeq
 \mathop{\mathrm{rec}}_{K_v}\bigl(\pi_{E,v}\otimes|\det|_v^{-1/2}\bigr).$$ The unitary parameter at the complex place is $z\mapsto\mathop{\mathrm{diag}}(z/|z|,\overline z/|z|)$. In particular every local factor agrees, and $$L(E/K,s)=L(\pi_E,s-1/2).$$ If $E$ has no complex multiplication, $\pi_E$ is cuspidal. In the CM case it is given by automorphic induction of a Hecke character, or by an isobaric sum when the CM field is already $K$.*

Here $r_\iota$ in the CM isobaric case is the sum of the corresponding character realizations with the same Tate normalization.

### Historical context

The arithmetic groups associated with imaginary quadratic fields and their action on hyperbolic three-space originate in Bianchi’s work [5]. Their presentations and cohomology were developed further by Swan and Harder [34, 24]. The expected relationship with elliptic curves belongs to the Langlands program: in [27, Section 7], Langlands explicitly discusses the automorphy of local representations attached to elliptic curves over global fields of characteristic zero. Grunewald–Helling–Mennicke, Cremona, and Cremona–Whitley developed substantial computations relating elliptic curves and automorphic forms over imaginary quadratic fields [23, 13, 14].

Over $\mathbb Q$, Wiles and Taylor–Wiles proved modularity of semistable elliptic curves [41, 38], and Breuil–Conrad–Diamond–Taylor proved modularity of every elliptic curve [9]. A central method is to lift automorphy from a residual Galois representation. Wiles’s $3$–$5$ switch also shows how an auxiliary elliptic curve, chosen with prescribed torsion and local behavior, can replace a residual representation that does not satisfy the initial lifting hypotheses.

For imaginary quadratic fields, the relevant cohomology occurs in more than one degree. The construction of Galois representations and the lifting problem both require additional work. Harris–Soudry–Taylor and Taylor constructed representations attached to Bianchi forms in important cases [26, 36]. For conjugation-invariant central character, Berger–Harcos obtained Frobenius compatibility away from finitely many primes [4]. Harris–Lan–Taylor–Thorne constructed Galois representations for general regular algebraic cuspidal representations over CM fields [25], and Scholze treated torsion cohomology as well [30]. Calegari–Geraghty developed patching for cohomology in several degrees [10]. The potential automorphy theorem of Allen–Calegari–Caraiani–Gee–Helm–Le Hung–Newton–Scholze–Taylor–Thorne implies potential modularity of every elliptic curve over a CM field [1, Theorem 1.0.1]. Boxer–Calegari–Gee–Pilloni also proved potential modularity for genus-one curves over quadratic extensions of totally real fields [8, Theorem 1.1.4]. Potential modularity permits an extension of the ground field; automorphy over the original field is a further problem.

Allen–Khare–Thorne proved residual modularity results in small characteristics and deduced modularity for a positive proportion of elliptic curves over each CM field not containing a primitive fifth root of unity [2]. Caraiani–Newton proved a lifting theorem allowing small coefficient primes and ramified CM fields, together with the local-global compatibility needed for its applications [11]. Their results give modularity under suitable residual-image hypotheses in characteristic $3$ or $5$, modularity for $100\%$ of Weierstrass equations, ordered by height, over each Galois CM field not containing $\zeta_5$, and modularity of every elliptic curve over an imaginary quadratic field $K$ for which $X_0(15)(K)$ has rank zero [11, Theorem 6.1 and Corollaries 6.1.2 and 7.1.2]. Theorem 1.1 removes the remaining restrictions on the curve and the imaginary quadratic field. Caraiani–Newton’s lifting theorem and residual-image criterion for modularity of elliptic curves remain essential inputs.

### The geometric prime switch

The difficulty is to reach a residual representation to which the known modularity theorem applies while retaining control at the primes where automorphy will be lifted. We construct the intermediate representations as character pieces of a single family of Jacobians.

Fix a non-CM elliptic curve $E/K$. Choose a sufficiently large prime $p$ for which the image on $E[p]$ contains $\mathop{\mathrm{SL}}_2(\mathbb F_p)$, and put $n=3p$ and $F=K(\mu_n)$. For $t$ in a nonempty affine open over $K$, we construct a genus-$n$ cyclic cover $C_n(t)$ of a quadratic twist $B_t$ of $E$. It is branched at two points and admits an involution that inverts the rotations. For a character $\theta$ of the rotation group $\mu_n$, write $$V_\theta=H^1(C_n(t))_\theta.$$ Each $V_\theta$ is a rank-two compatible system with determinant $\epsilon_l^{-1}$, where $\epsilon_l$ is the $l$-adic cyclotomic character, and labeled Hodge–Tate weights $0,1$.

Choose characters $\eta$ and $\psi$ of orders $3$ and $p$, respectively, and set $\chi=\eta\psi$. The order-three system $V_\eta$ comes from an elliptic curve $A/F$, while $V_1=H^1(B_t)$. An integral description of the cohomology gives the chain $$\begin{equation}
\tag{1.1}
 \underbrace{V_\eta}_{H^1(A)}
 \ \equiv\!\!\pmod p\ \ V_\chi
 \ \equiv\!\!\pmod 3\ \ V_\psi
 \ \equiv\!\!\pmod p\ \ \underbrace{V_1}_{H^1(B_t)}.
\end{equation}$$ Each congruence means equality of the semisimplified residual Galois representations. The order-$p$ part of a character disappears modulo $p$, and the order-$3$ part disappears modulo $3$. Automorphy will pass from left to right. The prime $5$ is used only to prove the initial modularity of $A$.

There are two useful degenerations of the covers. At one, the Jacobian has compact-type limit $E^n$. This yields a free integral group-ring description of its cohomology and lets us impose the local reduction behavior of all the character pieces at once. At the other, explicit vanishing cycles give opposite unipotent elements on each nontrivial rank-two piece. The latter supply absolute irreducibility and suitable Frobenius elements in residual characteristic $3$, $5$, or $p$. The two degeneration pictures are given in Section 3, and the vanishing-cycle calculation in Section 4.

Two specialization arguments complete the construction. First, finite torsion is locally constant in a family over a local field. Once semistability is secured, the full Frobenius polynomials belong to a finite set. Sufficiently deep torsion comparison with the fiber $E^n$ therefore preserves its toric rank and, in the good-reduction case, its Newton slopes. This provides simultaneous local conditions for every character piece. Second, Hilbert irreducibility is applied to the restriction of scalars of the parameter line from $K$ to $\mathbb Q$. The two conjugate families then occur in one finite monodromy quotient. This ensures the required residual genericity at every place above a rational split prime, while retaining the prescribed local conditions on $t$.

The construction has close antecedents. Cyclic covers of elliptic curves with two branch points and dihedral symmetry occur in the real-multiplication constructions of Tautz–Top–Verberkmoes and in Ellenberg’s treatment of Jacobian endomorphism algebras [35, 19]; Mestre’s constructions form part of the same geometric tradition [29]. Darmon developed congruences that remove prime-power parts of monodromy and a conditional modularity argument based on successive lifts for rigid local systems [15, 16]. The coefficient $2-\zeta-\zeta^{-1}$ in our monodromy calculation also appears in the rank-two monodromy studied by Darmon–Mestre [17]. Taylor’s use of auxiliary abelian varieties with real multiplication is another higher-dimensional form of prime switching [37].

The feature developed here is the combination for a *prescribed* elliptic curve: the character orders $1,p,3p,3$ occur in one integral cohomology lattice, an elliptic curve occurs at each end of the chain, and the compact-type degeneration and simultaneous residual specialization make every step applicable to the CM-field lifting theorem. The local constancy argument and the two-conjugate specialization argument are formulated separately, so they can be used independently of the final automorphy application.

Sections 3 and 4 establish the cover geometry and integral monodromy. Section 5 constructs the rank-two systems and their congruences. Section 6 states the automorphy inputs at the point where their hypotheses become concrete conditions on those systems. Sections 7 and 8 find one parameter satisfying those conditions. Section 9 performs the three lifts, descends from $F$ to $K$, and completes the local comparisons and the CM case.

## Galois and automorphic conventions

We use the cohomological realization $$H^1(X)=H^1_{\mathrm{\acute et}}(X_{\overline L},\mathbb Q_l)$$ for a smooth proper variety over a number field $L$; coefficient extensions will always be indicated or understood. We write $G_L=\mathop{\mathrm{Gal}}(\overline L/L)$. The cyclotomic character $\epsilon_l$ has Hodge–Tate weight $-1$ in our convention. Thus an elliptic curve has labeled Hodge–Tate weights $0,1$, and its $H^1$ has determinant $\epsilon_l^{-1}$. The bar on a characteristic-zero representation denotes the semisimplification of the reduction of a stable lattice. This semisimplification is independent of the lattice.

For a regular algebraic cuspidal representation $\pi$ of $\mathop{\mathrm{GL}}_2(\mathbb A_L)$ over a CM field, let $r_\iota(\pi)$ denote the associated semisimple $l$-adic representation, where $\iota:\overline{\mathbb Q}_l\xrightarrow{\sim}\mathbb C$. We use the normalization of [25, 30, 11]: the local comparison is with $$\begin{equation}
\tag{2.1}
 \mathop{\mathrm{rec}}^T_{L_v}(\pi_v)
 :=\mathop{\mathrm{rec}}_{L_v}\bigl(\pi_v\otimes|\det|_v^{-1/2}\bigr).
\end{equation}$$ Here the reciprocity convention uses geometric Frobenius. The algebraic weight corresponding to trivial coefficients is called *weight zero*. At a complex place the generic weight-zero parameter, in unitary normalization, is $$\begin{equation}
\tag{2.2}
 z\longmapsto
 \begin{pmatrix}z/|z|&0\\0&\overline z/|z|\end{pmatrix},
 \qquad |z|=(z\overline z)^{1/2}.
\end{equation}$$ The corresponding Tate-normalized parameter has Hodge types $(1,0)$ and $(0,1)$. In particular, if the Tate-normalized finite parameters realize an elliptic curve $E$, then $$\begin{equation}
\tag{2.3}
 L(E/L,s)=L(\pi,s-1/2).
\end{equation}$$

All geometric cover constructions below are made in characteristic zero. For a local field, a representation is *potentially crystalline* if it becomes crystalline after a finite extension. A two-dimensional representation is *potentially ordinary of weight zero* if, after a finite extension, it admits an invariant line with unramified character and its quotient is $\epsilon_l^{-1}$ times an unramified character. This is the Hodge–Tate ordering $0,1$ in the lifting theorem. Local fields used to check these properties may be enlarged independently at different places.

## Cyclic covers and two degenerations

We construct a family of cyclic covers of quadratic twists of a fixed elliptic curve. Two boundary fibers explain the features needed later. At the first, the Jacobian becomes a product of copies of the original elliptic curve; at the second, the cover acquires nodes whose vanishing cycles will give explicit monodromy operators. All degenerations in this section take place over a parameter curve in characteristic zero.

### The family and its dihedral action

Let $k$ be a number field, let $E/k$ be an elliptic curve, and fix an odd integer $n\geq 3$. Write $$E:\quad y^2=h(x),$$ where $h\in k[x]$ is a separable cubic and the point at infinity is the origin $O$. For $t$ with $h(t)\ne 0$, put $$\begin{equation}
\tag{3.1}
 B_t:\quad h(t)y^2=h(x),\qquad R_t=(t,1),\qquad S_t=[n]R_t.
\end{equation}$$ Let $U\subset\mathbb A^1_k$ be the open set on which $O,R_t,-R_t,S_t,-S_t$ are pairwise distinct. This is a nonempty open set: after the double cover $t=x(R)$ parametrized by $R\in E$, the map $$B_{x(R)}\longrightarrow E,\qquad (x,y)\longmapsto (x,y(R)y)$$ identifies $R_t$ with the moving point $R$. Each excluded equality then imposes a torsion condition on $R$, so excludes only finitely many points. We may remove further finitely many points from $U$ when necessary.

**Lemma 3.1**. *For each divisor $m>1$ of $n$, there is a smooth proper family of geometrically connected genus-$m$ curves $\mathcal C_m\to U$. It is the normalization of the smooth proper elliptic family $B\to U$ in the function-field extension, written fiberwise as $$\begin{equation}
\tag{3.2}
 Y^m=f_t(Z),\qquad
 \operatorname{div}(f_t)=(S_t)-(-S_t)-n(R_t)+n(-R_t),\qquad f_t(O)=1.
\end{equation}$$ The family has an involution $$\begin{equation}
\tag{3.3}
 w:(Z,Y)\longmapsto(-Z,Y^{-1}).
\end{equation}$$ Over a field containing $\mu_m$, rotations $u_\zeta:(Z,Y)\mapsto(Z,\zeta Y)$ are defined and satisfy $wu_\zeta w=u_{\zeta^{-1}}$. If $d\mid m$, the map $Y\mapsto Y^{m/d}$ gives the quotient $C_{m,t}\to C_{d,t}$; for $d=1$ the quotient is $B_t$.*

*Proof.* On an elliptic curve, a degree-zero divisor is principal precisely when its sum in the elliptic-curve group is $O$. The divisor in (3.2) has sum $$S_t-(-S_t)-nR_t+n(-R_t)=2S_t-2nR_t=O.$$ It therefore determines a rational function, uniquely after imposing $f_t(O)=1$. Applying this argument over $k(U)$ and spreading out gives a rational function on the family. Its divisor changes sign under $Z\mapsto-Z$, and its normalization at $O$ consequently gives $$\begin{equation}
\tag{3.4}
 f_t(-Z)=f_t(Z)^{-1}.
\end{equation}$$ This also shows that the function has no vertical divisor: every fiber component of the smooth elliptic family is preserved by inversion, so its valuation is its own negative. Thus the prescribed disjoint sections are the entire divisor on $U$.

The valuation at $S_t$ is $1$, so the Kummer extension has degree $m$ even geometrically. It is totally ramified at $S_t$ and $-S_t$ and unramified elsewhere, since the remaining nonzero valuations are $\pm n$, divisible by $m$. Riemann–Hurwitz gives $2g(C_{m,t})-2=2(m-1)$. The same local description proves that the normalization is smooth over $U$. Indeed, a zero or pole of order divisible by $m$ can be removed from the Kummer equation; at a section of order $1$ or $-1$, after taking a root of a unit *étale* locally, the equation is the $m$th-root cover of a parameter transverse to that section. Normalization is finite here, so the resulting smooth family is proper. Equation (3.4) gives the involution, and the remaining assertions follow from the Kummer equations. ◻

We will study the pullback of this family to the open set of $E$ on which $R$ is a moving point and $O,\pm R,\pm[n]R$ are distinct. There the base elliptic curve is the constant curve $E$. We write $C_{m,R}$ for the fiber and $f_R$ for its normalized function. The normalization at $O$ ensures that the pullback identification is exact: it introduces no scalar twist into the equation $Y^m=f_R$.

### Separating colliding sections

The two boundary points we use are $$\begin{equation}
\tag{3.5}
 R=O,\qquad\text{and}\qquad
 R=R_*,\quad [n]R_*\in E[2]\setminus\{O\},
 \quad O,\pm R_*,[n]R_*\ \text{distinct}.
\end{equation}$$ The second point may be considered after extending the ground field; we will ultimately use it over $\mathbb C$.

**Lemma 3.2**. *In the constant-$E$ family, blow up the surface at the collision point over either boundary parameter in (3.5), and normalize the resulting surface in $Y^m=f_R$. This gives a regular semistable model near that parameter. Its special fiber has $m$ geometric nodes lying over the node of the blown-up elliptic surface. Each node has smoothing parameter of order one in a parameter on the base. The component above the exceptional projective line is a geometrically connected rational curve.*

*Proof.* At $R=O$, choose parameters $r$ on the parameter curve and $z$ on the constant elliptic curve, both at $O$, with the same tangent coordinate. The sections $R,-R,[n]R,-[n]R$ have first-order equations $z=r,-r,nr,-nr$. Their strict transforms meet the exceptional line at four distinct points with coordinates $1,-1,n,-n$; the node joining this line to the main component has coordinate $\infty$. At the second boundary parameter, only the sections $[n]R$ and $-[n]R$ collide. Their tangent slopes are distinct, so one blowup again separates them from each other and from the node.

The involution $Z\mapsto-Z$ preserves both components of each blown-up fiber. Equation (3.4) therefore forces the valuation of $f_R$ on each component to be zero. None of its horizontal divisor sections passes through the node. Since the surface is regular, $f_R$ is consequently a unit at that node. Taking its $m$th root is étale there. The node downstairs has local smoothing equation $xy=b$, with $b$ a parameter on the base. Over an algebraic closure, its $m$ lifts have the same local equation. In particular, the smoothing parameter is $b$, rather than a higher power of $b$.

At the separated sections the normalization has the smooth local description used in Lemma 3.1. This proves regularity of the total space and semistability of the family. On the exceptional line, only the two sections of multiplicities $1$ and $-1$ cause ramification. The cyclic cover is connected, is totally ramified at these two points, and has genus zero by Riemann–Hurwitz. ◻

**Proposition 3.3**. *Suppose that $k$ contains $\mu_m$. At $R=O$, the special fiber of the model in Lemma 3.2 is a rational curve joined at distinct points to $m$ copies of $E$, all defined over $k$. Rotations cyclically permute the elliptic components. The Jacobian family of $C_{m,R}$ therefore extends to an abelian scheme on a Zariski neighborhood of $O$ in the parameter curve, with fiber $E^m$ at $O$.*

*Proof.* Let $v=z/r$ be the coordinate on the exceptional line. Its normalized function is $$\begin{equation}
\tag{3.6}
 f_{\mathrm{exc}}(v)=
 \frac{v-n}{v+n}\left(\frac{v+1}{v-1}\right)^n.
\end{equation}$$ Indeed, the divisor gives this expression up to a scalar. The section $Z=O$ meets the exceptional line at $v=0$, where the function is a unit with value $1$. Since $n$ is odd, the displayed expression also has value $1$ at $0$, so the scalar is $1$.

The restriction of $f_R$ to the main elliptic component has no divisor, and is therefore constant. At its node with the exceptional component this constant is $f_{\mathrm{exc}}(\infty)=1$. The cover of the main component is consequently the disjoint union of the $m$ copies of $E$ given by $Y\in\mu_m$. On the exceptional line the substitution $$Y'=Y\left(\frac{v-1}{v+1}\right)^{n/m}$$ gives $Y'^m=(v-n)/(v+n)$. Its $m$ points over $v=\infty$ are defined over $k$ and attach to the $m$ elliptic components, one each.

The dual graph is a tree, as illustrated in Figure 1. Thus the fiber is of compact type: its identity-component Picard variety is the product of the Jacobians of its components, namely $E^m$. The marked point $(O,1)$ extends to a section through the smooth locus. The relative Picard theorem for a family of nodal curves of compact type then makes the Jacobian family an abelian scheme across this fiber. More precisely, the relative identity-component Picard scheme is semi-abelian, and its torus vanishes when the dual graph is a tree; see [7, Section 9.4, Theorem 1, and Section 9.2, Proposition 10]. Shrinking the parameter neighborhood removes the other singular fibers and gives the asserted extension. ◻

**Remark 3.4**. Proposition 3.3 concerns an abelian scheme over an open subset of the characteristic-zero parameter curve $E_k$. After passing to a completion of $k$, it remains a family over that local field. No assertion about extending the Kummer cover over a ring of integers, particularly in residue characteristic dividing $m$, is needed here. The arithmetic reduction types of nearby Jacobians will be established separately.

### The second fiber and its nodes

For the monodromy computation, choose an oriented period basis $a,b$ of $E(\mathbb C)$ and take $R_*=a/(2n)$. The next explicit equation records why a simple loop around $R_*$ contributes one twist at each node.

**Lemma 3.5**. *For $R_*=a/(2n)$, the special fiber in Lemma 3.2 consists of a connected unramified degree-$m$ cover $E'\to E$ and a rational component, joined at $m$ distinct nodes. In analytic coordinates near each node, the family has equation $XU=-2nt$, where $t=R-R_*$ is an additive local parameter.*

*Proof.* Write $Q=a/2=[n]R_*$ and use additive analytic coordinates $t=R-R_*$ and $z=Z-Q$. The colliding sections have equations $z=nt$ and $z=-nt$, while the other divisor sections avoid this neighborhood. Thus $$f_R=g(z,t)\frac{z-nt}{z+nt}$$ with $g$ a holomorphic unit. Choose a local $m$th root of $g$ and put $V=Y/g^{1/m}$. The Kummer equation becomes $$\begin{equation}
\tag{3.7}
 (z+nt)(V^m-1)=-2nt.
\end{equation}$$ For each $V=\zeta$, $\zeta\in\mu_m$, the function $U=V^m-1$ is a local coordinate. Taking $X=z+nt$ gives the asserted node equation. It is the local chart of the normalization of the blowup from Lemma 3.2; the exceptional component has $X=0$, and the main component has $U=0$. In particular, the nonzero constant $2n$ changes no vanishing order.

On the main component, the divisor of the limiting function is $n(-R_*)-n(R_*)$. The associated unramified Kummer cover is determined by the $m$-torsion divisor class $$\frac{n}{m}\bigl((-R_*)-(R_*)\bigr)
 \quad\longleftrightarrow\quad
 -\frac{2n}{m}R_*=-\frac{a}{m}\quad\text{in }E(\mathbb C).$$ This class has exact order $m$, so that cover is connected. It is unramified of degree $m$ over an elliptic curve and hence is itself an elliptic curve $E'$. The exceptional cover is rational by Lemma 3.2, and its $m$ attachments are the nodes just computed. ◻

**Figure 1:** The dual graphs of the two special fibers. Vertex labels indicate component genera and identify the elliptic components; edges are nodes. At $R=O$ the graph is a star with $m$ elliptic leaves, so the Jacobian is $E^m$. At $R=a/(2n)$ two components meet in $m$ nodes, giving graph Betti number $m-1$. The drawings are schematic for general odd $m$.

The first degeneration has now supplied a split product fiber and a neighborhood in which its homology can be compared with nearby smooth fibers. The second has supplied $m$ nodes, each with smoothing order one. We next identify their vanishing cycles in a single integral basis.

## Integral homology and explicit monodromy

Fix the complex elliptic curve $E$ and the constant-$E$ family from Section 3. Let $n\geq3$ be odd and let $m>1$ divide $n$. We write $$\Gamma_m=\mu_m,\qquad u:(Z,Y)\longmapsto(Z,e^{2\pi i/m}Y),$$ so that $u$ is the chosen generator of the deck group. Throughout this section $\mathbb Z[\Gamma_m]$ denotes the *group ring*, not the cyclotomic integer ring. We first construct an integral basis permuted by $u$, and then compute two monodromy operators in that same basis. Their reduction on character spaces will supply the residual irreducibility used later.

### A basis obtained by cutting the torus

Choose an oriented period basis $a,b$ and identify the underlying oriented torus with $(\mathbb R/\mathbb Z)^2$, with $a$ horizontal and $b$ vertical. Consider the path of parameters $$\begin{equation}
\tag{4.1}
 R_s=\frac{s}{n}a,\qquad 0<s<\frac12.
\end{equation}$$ Its branch points are $-sa$ and $sa$. Let $I_s$ be the horizontal arc from $-sa$ to $sa$ through $O$.

**Lemma 4.1**. *For the parameters in (4.1), the cover $C_{m,R_s}\to E$ is trivial over $E\setminus I_s$. It is obtained by cutting $m$ copies of $E$ along $I_s$ and joining adjacent banks cyclically. Crossing the slit changes the sheet index by $1$ or $-1$, according to the orientation of crossing and the initial choice of indexing.*

*Proof.* For small $s$, enclose the colliding sections in a small disk about $O$. The model at $R=O$ restricts outside that disk to $m$ disjoint copies of its complement, by Proposition 3.3. If $D$ is such a disk, the inclusion $E\setminus\operatorname{int}(D)\hookrightarrow E\setminus I_s$ is a homotopy equivalence. The unramified cover of $E\setminus I_s$ is therefore trivial. As $s$ varies in $(0,1/2)$, the arcs $I_s$ move by isotopy, and the topological isomorphism class of this unramified cover remains constant. The monodromy around either branch point is a generator of $\Gamma_m$, since its valuation in $f_R$ is $1$ or $-1$. This gives the stated gluing. ◻

On each sheet let $a_i$ be the horizontal loop at vertical coordinate $1/2$ and let $b_i$ be the vertical loop at horizontal coordinate $1/2$, for $i\in\mathbb Z/m\mathbb Z$. These loops avoid the slit, intersect at one point on their common sheet, and may be oriented so that $$\begin{equation}
\tag{4.2}
 \langle a_i,b_j\rangle=\delta_{ij},\qquad
 \langle a_i,a_j\rangle=\langle b_i,b_j\rangle=0.
\end{equation}$$ Index the sheets so that $u$ sends $a_i,b_i$ to $a_{i+1},b_{i+1}$.

**Proposition 4.2**. *The cycles $a_i,b_i$ form an integral symplectic basis of $H_1(C_{m,R_s},\mathbb Z)$. Consequently, for every smooth fiber of the family, $$\begin{equation}
\tag{4.3}
 H_1(C_m,\mathbb Z)\simeq\mathbb Z[\Gamma_m]^2,
 \qquad H^1(C_m,\mathbb Z)\simeq\mathbb Z[\Gamma_m]^2.
\end{equation}$$ In particular, after comparison, $H^1_{\mathrm{et}}(C_m,\mathbb Z_\ell)$ is free of rank two over $\mathbb Z_\ell[\Gamma_m]$ for every prime $\ell$, including $\ell\mid m$.*

*Proof.* The genus is $m$, so $H_1$ has rank $2m$. Equation (4.2) shows that the $2m$ displayed classes are linearly independent and span a sublattice with unimodular intersection pairing. If its index in $H_1$ were $d$, its intersection determinant would be $d^2$ times the determinant on $H_1$. Both determinants are $1$, so $d=1$. The deck action now gives the first isomorphism in (4.3).

The dual of the regular integral module is again regular: explicitly, the coefficient-of-identity pairing $$\mathbb Z[\Gamma_m]\times\mathbb Z[\Gamma_m]\longrightarrow\mathbb Z,
 \qquad (x,y)\longmapsto [1](xy)$$ is perfect. With the pullback action on the dual, it identifies $\operatorname{Hom}_{\mathbb Z}(\mathbb Z[\Gamma_m],\mathbb Z)$ with $\mathbb Z[\Gamma_m]$. This proves the cohomological assertion without dividing by $m$. Topological local triviality transports the result through the connected smooth parameter open, and comparison gives the étale assertion. ◻

**Remark 4.3**. The compact-type degeneration gives another explanation of the integral statement. Its Jacobian extends to an abelian scheme with special fiber $E^m$, and $\Gamma_m$ permutes the factors regularly. The integral homology of this fiber is the regular module twice. The slit construction makes this description concrete by identifying cycles that can also be followed towards the other degeneration.

### Vanishing cycles and a common monodromy basis

Let $s$ approach $1/2$ in (4.1). The branch points meet at $a/2$, while the slit fills all but a shrinking gap in the horizontal circle. Choose a small disk about $a/2$ containing both branch points, with radius larger than their distance from the collision point. Its boundary has $m$ closed lifts $\delta_i$. They are the neck circles at the $m$ nodes of Lemma 3.5; hence they are the vanishing cycles.

**Lemma 4.4**. *After a cyclic indexing of the lifts, their homology classes are $$\begin{equation}
\tag{4.4}
 [\delta_i]=\pm(a_i-a_{i+1}),\qquad i\in\mathbb Z/m\mathbb Z,
\end{equation}$$ or the same formula with $i-1$ in place of $i+1$.*

*Proof.* Arrange the boundary of the disk to cross the slit transversely twice. A lifted boundary circle has its upper arc on one sheet and its lower arc on an adjacent sheet. Index the upper sheet by $i$; the lower one is $i+1$ or $i-1$, by Lemma 4.1. The circle is disjoint from every $a_j$. It crosses the two corresponding vertical loops once each, with opposite intersection signs, and no other $b_j$. These intersections determine its class in the integral symplectic basis of Proposition 4.2, giving (4.4). See Figure 2. ◻

**Figure 2:** The horizontal slit leaves a gap about the collision point $a/2$. A small circle about that gap crosses the slit twice. Its lift has one arc on sheet $i$ and the other on sheet $i+1$; its two intersections with the lifted vertical cycles have opposite signs. This identifies the vanishing class as $\pm(a_i-a_{i+1})$. Opposite edges of the torus rectangle are identified; its coordinates range over $[0,1]\times[-1/4,3/4]$, so $-s$ is plotted at $1-s$. In the right panel, solid and dashed arcs distinguish the two sheets.

**Theorem 4.5**. *In one integral basis $a_i,b_i$ as above, the geometric monodromy of the constant-$E$ family contains operators $T_a,T_b$ satisfying $$\begin{align}
 T_a(a_j)&=a_j,&
 T_a(b_j)&=b_j+\sigma_a(2a_j-a_{j-1}-a_{j+1}),
 \tag{4.5}\\
 T_b(b_j)&=b_j,&
 T_b(a_j)&=a_j+\sigma_b(2b_j-b_{j-1}-b_{j+1}),
 \tag{4.6}
\end{align}$$ where $\sigma_a,\sigma_b\in\{1,-1\}$ are independent of $j$. Equivalently, their two off-diagonal entries, in the basis of the free $\mathbb Z[\Gamma_m]$-module, are $\sigma_a(2-u-u^{-1})$ and $\sigma_b(2-u-u^{-1})$. The geometric monodromy of the family over $U$ contains these actions as well, under the pullback identification.*

*Proof.* The Picard–Lefschetz formula for a positively oriented loop about a semistable fiber is the product of the Dehn twists at its nodes; see [18, Exposé XV]. In the present family, every node has smoothing order one by (3.7), so every twist has exponent one. The vanishing cycles are disjoint. Their intersection pairings with one another therefore vanish, and the product acts on a class $\gamma$ by $$\begin{equation}
\tag{4.7}
 \gamma\longmapsto
 \gamma+\sigma\sum_i
 \langle\gamma,\delta_i\rangle[\delta_i],
\end{equation}$$ with one sign $\sigma$ depending only on the intersection convention. Substituting (4.4) gives zero on the $a_j$ and, up to this one sign, $$(a_j-a_{j+1})-(a_{j-1}-a_j)
   =2a_j-a_{j-1}-a_{j+1}$$ on $b_j$. This proves (4.5). Replacing the horizontal path by $R_s=(s/n)b$ gives (4.6), initially in the basis obtained from the corresponding vertical slit.

It remains to compare the two bases; this matters because separate triangular matrices in unrelated bases would not give the stated conclusion. Choose the starting parameters of both paths sufficiently close to $O$. The horizontal loop at $y=1/2$ and the vertical loop at $x=1/2$ avoid one fixed small disk about $O$ and avoid both short slits. Outside this disk the covering extends across $R=O$ as $m$ disjoint sheets. Trivialize it over a small, simply connected parameter disk containing $O$, and use this trivialization to label the lifts of the two fixed loops. Parallel transport between the starting parameters now identifies both sets of $a_i,b_i$ with the same basis. There is no monodromy ambiguity from circling $O$ on these classes: the sheet trivialization extends over $O$ itself. A different initial labeling makes only a common cyclic shift, which leaves (4.5)–(4.6) unchanged.

Both loops therefore define the asserted operators in a single geometric monodromy group. Pullback along the open parameter curve in $E\to U$ maps its fundamental group into that of $U$, so these operators occur in the latter image too. Removing additional finitely many points from either smooth parameter open induces a surjection on fundamental groups and does not remove any of the operators. ◻

The operator $2-u-u^{-1}$ is the cyclic difference operator arising from the adjacent-sheet vanishing classes. The next sections use the integral module in Proposition 4.2 to specialize rotation characters, and the two matrices above to keep the resulting residual representations irreducible.

## Rank-two systems and integral congruences

The cyclic covers now supply the Galois representations through which we will transfer automorphy. The involution identifies opposite rotation characters, giving each character space the determinant and Hodge–Tate weights of an elliptic curve. The integral regular-module calculation will then give congruences even at primes dividing the covering degree.

Return to an imaginary quadratic field $K$ and a non-CM elliptic curve $E/K$. By Serre’s open image theorem [31, §4.4, Théorème 3], choose a prime $p>100$ such that the image of $G_K$ on $E[p]$ contains $\mathop{\mathrm{SL}}_2(\mathbb F_p)$. Set $$\begin{equation}
\tag{5.1}
 n=3p,\qquad F=K(\mu_n).
\end{equation}$$ Both $K/\mathbb Q$ and $\mathbb Q(\mu_n)/\mathbb Q$ are abelian, so $F/\mathbb Q$ is abelian. It is a CM field: complex conjugation is central, its fixed field is totally real, and $F$ has no real embedding because it contains $K$. Moreover, $$\begin{equation}
\tag{5.2}
 \zeta_5\notin F.
\end{equation}$$ Indeed, $\mathbb Q(\mu_n)$ is unramified at $5$, and the ramification index of $F$ at $5$ is consequently at most $[K:\mathbb Q]=2$. A field containing $\mathbb Q(\zeta_5)$ has ramification index divisible by $4$ at $5$.

Apply the construction of Lemma 3.1 with this $n$. Write $U\subset\mathbb A^1_K$ for its parameter open and $B_t$ for the quadratic twist of $E$ used there. We may shrink $U$ whenever a smooth proper model of one of the finitely many families is required. Until Section 8, the point $t\in U(K)$ is arbitrary.

### Character spaces

Fix an embedding $\overline{\mathbb Q}\hookrightarrow\mathbb C$ and put $M=\mathbb Q(\mu_n)\subset\overline{\mathbb Q}$. For each rational prime $\ell$, choose an embedding $j_\ell:\overline{\mathbb Q}\hookrightarrow\overline{\mathbb Q}_\ell$ and an isomorphism $\iota_\ell:\overline{\mathbb Q}_\ell\xrightarrow{\sim}\mathbb C$ whose composition with $j_\ell$ is the fixed complex embedding. Every rotation character in this section is a homomorphism $$\theta:\mu_n(F)\longrightarrow M^\times.$$ Write $C_m(t)=C_{m,t}$ for a fiber of the family. For the curve $C_n=C_n(t)$, define $$\begin{equation}
\tag{5.3}
 V_{\theta,\ell}
 =\bigl\{x\in H^1_{\mathrm{\acute et}}
       (C_{n,\overline F},\overline{\mathbb Q}_\ell):
       u^*x=j_\ell(\theta(u))x\text{ for all }u\in\mu_n(F)\bigr\}.
\end{equation}$$ Here $u$ denotes the deck transformation with multiplier $u$. All deck transformations are defined over $F$, so these are $G_F$-representations. We write $V_\theta$ for the collection of these realizations. In a congruence at $\ell$, all characters use the same embedding $j_\ell$; this convention is essential when comparing their reductions.

**Proposition 5.1**. *For every $t\in U(K)$ and every rotation character $\theta$, the representations $V_{\theta,\ell}$ have the following properties.*

1.  *They are semisimple of dimension two, with determinant $\epsilon_\ell^{-1}$.*

2.  *At every place of $F$ above $\ell$, they are potentially semistable with labelled Hodge–Tate weights $\{0,1\}$.*

3.  *There is a finite set of places $S$ of $F$, independent of $\ell$, such that $V_{\theta,\ell}$ is unramified at every $v\notin S$ of residue characteristic different from $\ell$. At such a place its Frobenius characteristic polynomial is the image under $j_\ell$ of a polynomial in $M[T]$ independent of $\ell$.*

*Proof.* The rank-two regular-module statement of Proposition 4.2, followed by comparison between singular and $\ell$-adic cohomology, gives $\dim V_{\theta,\ell}=2$.

Let $\langle\ ,\ \rangle$ be the cup-product pairing on $H^1(C_n)$, with values in $\overline{\mathbb Q}_\ell(-1)$. It pairs the $\theta$-space perfectly with the $\theta^{-1}$-space. The involution $w$ is defined over $F$, preserves cup product, and exchanges these two spaces. Consequently $$[x,y]_\theta=\langle x,w^*y\rangle,
 \qquad x,y\in V_{\theta,\ell},$$ is a perfect $G_F$-equivariant pairing into $\overline{\mathbb Q}_\ell(-1)$. It is alternating, because $$\langle y,w^*x\rangle
   =\langle w^*y,x\rangle
   =-\langle x,w^*y\rangle.$$ A perfect alternating pairing on a two-dimensional space identifies its determinant with the target line. This proves $\det V_{\theta,\ell}=\epsilon_\ell^{-1}$.

To compute the Hodge numbers, make any embedding of $F$ into $\mathbb C$. Let $a_\theta$ be the multiplicity of $\theta$ in the holomorphic differentials of the resulting complex curve. The holomorphic involution $w$ gives $a_\theta=a_{\theta^{-1}}$. Hodge decomposition and complex conjugation identify the dimension of the full $\theta$-space with $a_\theta+a_{\theta^{-1}}$. Since this dimension is two, $a_\theta=1$. This argument works for every embedding and every character. The comparison theorems therefore give the labelled weights $0,1$. Potential semistability follows from semistable reduction and the semistable comparison theorem for smooth proper varieties; see [39]. These properties pass to the character summands.

Outside a finite set, $C_n$ has good reduction and the rotations extend to its smooth proper model. Smooth proper base change gives unramifiedness. The projector onto the $\theta$-space is $$e_\theta=\frac1n\sum_{u\in\mu_n(F)}
              j_\ell(\theta(u))^{-1}u^*.$$ This formula is used only in characteristic zero. The Lefschetz trace formula for a rotation composed with a positive power of Frobenius shows that its trace on $H^1(C_n)$ is independent of $\ell$. Applying the displayed projector gives traces in $M$, compatible under the embeddings $j_\ell$. Together with the already determined determinant, this gives the asserted common characteristic polynomial.

Finally, $H^1(C_n)$ is the first cohomology of its Jacobian. Faltings’ semisimplicity theorem [20, §5, Satz 3] makes this a semisimple $G_F$-representation. Extension of scalars and passage to a $G_F$-stable direct summand preserve semisimplicity, proving the remaining assertion. ◻

### The two elliptic-curve realizations

The characters of orders one and three will connect the new systems to elliptic curves. For the order-three character, the involution produces a genus-one quotient rather than merely an abstract rank-two summand.

**Proposition 5.2**. *If $\theta$ has order $m>1$ dividing $n$, the system $V_\theta$ is realized by the corresponding character space in $H^1(C_m)$. For the trivial character, $$V_{1,\ell}\simeq H^1_{\mathrm{\acute et}}
                  (B_{t,\overline F},\overline{\mathbb Q}_\ell).$$ Let $D_t=C_3(t)/\langle w\rangle$ and $A_t=\mathop{\mathrm{Jac}}(D_t)$. Then $D_t$ has genus one, $A_t$ is an elliptic curve over $F$, and for either nontrivial order-three character $\eta$ there are $G_F$-equivariant isomorphisms $$V_{\eta,\ell}\simeq
 H^1_{\mathrm{\acute et}}(A_{t,\overline F},\overline{\mathbb Q}_\ell)
 \qquad\text{for every }\ell.$$*

*Proof.* The quotient map $C_n\to C_m$ sends the covering coordinate $Y$ to $Y^{n/m}$. Pullback is injective on rational cohomology, since its composition with trace is multiplication by the degree. Its image is the subspace fixed by the kernel of $\mu_n\to\mu_m$. The rank-two calculation therefore identifies its order-$m$ character summand with $V_{\theta,\ell}$. The same argument for the quotient $C_n\to B_t$ identifies the trivial character space.

On $H^1(C_3)$, the trivial rotation space is $H^1(B_t)$, and $w$ acts there by $[-1]^*=-1$. It exchanges the two nontrivial rotation spaces, each of dimension two. Their direct sum consequently has a two-dimensional $w$-invariant subspace. Rational cohomology of a finite quotient is the invariant subspace, so $$H^1(D_t)\simeq H^1(C_3)^{w=1}$$ has dimension two. Thus $D_t$ has genus one and its Jacobian is an elliptic curve, whether or not $D_t$ has an $F$-rational point. Projection of a vector $x+w^*x$ onto the $\eta$-space is $x$; therefore this projection is a $G_F$-equivariant isomorphism from the invariant subspace to $V_{\eta,\ell}$. Finally, $H^1(D_t)\simeq H^1(\mathop{\mathrm{Jac}}(D_t))$. The latter identification is independent of the geometric base point used in an Abel–Jacobi map, because translations act trivially on cohomology. ◻

### Evaluation of the integral group ring

A character projector contains the denominator $n$ and cannot by itself establish a congruence at $3$ or $p$. Instead, we use the integral freeness proved in Section 4. Evaluation of a free group-ring module gives a lattice before reduction; two characters with the same residual values then give the same residual representation.

**Lemma 5.3**. *Fix $t\in U(K)$ and a prime $\ell$. Let $L/\mathbb Q_\ell$ be a finite extension containing $j_\ell(M)$, with ring of integers $\mathcal O$, maximal ideal $\mathfrak m$, and residue field $k$. For a rotation character $\theta$, the module $$\mathcal T_\theta=
 H^1_{\mathrm{\acute et}}(C_{n,\overline F},\mathbb Z_\ell)
 \otimes_{\mathbb Z_\ell[\mu_n],\,j_\ell\theta}\mathcal O$$ is a free rank-two $G_F$-stable lattice realizing $V_{\theta,\ell}$ after extension to $\overline{\mathbb Q}_\ell$. If $j_\ell\theta$ and $j_\ell\theta'$ have the same reduction as characters $\mu_n\to k^\times$, then $$\mathcal T_\theta/\mathfrak m\mathcal T_\theta
 \simeq
 \mathcal T_{\theta'}/\mathfrak m\mathcal T_{\theta'}$$ as $k[G_F]$-modules.*

*Proof.* By Proposition 4.2 and comparison, $$H^1_{\mathrm{\acute et}}(C_{n,\overline F},\mathbb Z_\ell)
 \simeq \mathbb Z_\ell[\mu_n]^2$$ as group-ring modules. The Galois action commutes with this group ring because the rotations are defined over $F$. Tensoring by evaluation at $j_\ell\theta$ therefore gives a free rank-two $\mathcal O$-module with continuous Galois action. In characteristic zero the group algebra is semisimple; its quotient by character evaluation is precisely the corresponding character summand. This identifies its rational representation with $V_{\theta,\ell}$.

After reduction, the displayed tensor product becomes $$H^1_{\mathrm{\acute et}}(C_{n,\overline F},\mathbb Z_\ell)
 \otimes_{\mathbb Z_\ell[\mu_n],\,\overline\theta} k.$$ It depends only on the residual evaluation map $\overline\theta$. This proves the asserted isomorphism without assuming that $\ell$ is prime to $n$. ◻

Choose a primitive character $\chi$ of order $n=3p$ and write its unique primary decomposition as $$\chi=\psi\eta,\qquad \operatorname{ord}(\psi)=p,
 \qquad \operatorname{ord}(\eta)=3.$$ For a system $V_\theta$, write $\overline V_{\theta,\ell}$ for the semisimplified reduction of a stable lattice, with scalars extended to $\overline{\mathbb F}_\ell$. This representation is independent of the choice of stable lattice.

**Corollary 5.4**. *For every $t\in U(K)$ there are isomorphisms $$\begin{equation}
\tag{5.4}
 \overline V_{\eta,p}\simeq\overline V_{\chi,p},
 \qquad
 \overline V_{\chi,3}\simeq\overline V_{\psi,3},
 \qquad
 \overline V_{\psi,p}\simeq\overline V_{1,p}.
\end{equation}$$ These hold with the elliptic-curve realizations of Proposition 5.2 at the two ends.*

*Proof.* A root of unity of $\ell$-power order reduces to $1$ in residue characteristic $\ell$. Thus $\chi$ and $\eta$ have the same reduction at $p$, $\chi$ and $\psi$ have the same reduction at $3$, and $\psi$ and $1$ have the same reduction at $p$. Lemma 5.3 gives the three congruences. The rational isomorphisms with the smaller covers and elliptic curves in Proposition 5.2 preserve semisimplified reduction, even if their natural integral pullbacks have index divisible by $\ell$. ◻

The direction of propagation is now fixed: automorphy will pass from $V_\eta$ to $V_\chi$ at $p$, then to $V_\psi$ at $3$, and finally to $V_1$ at $p$. The congruences themselves impose no restriction on $t$. The subsequent local and residual arguments will choose one parameter for which all three automorphy-lifting steps apply.

## Automorphy inputs and the remaining specialization conditions

The congruences of Corollary 5.4 connect the cohomology of the auxiliary elliptic curve $A$ to that of the twist $B_t$ of $E$. To turn them into a proof of automorphy, we use two results of Caraiani–Newton. We state the precise forms needed here, and then identify the properties that the parameter $t$ must satisfy. All the results quoted from [11] use the numbering of its third arXiv version.

**Definition 6.1** (Decomposed genericity). Let $L$ be a number field and let $\overline r:G_L\to\mathop{\mathrm{GL}}_2(\overline{\mathbb F}_l)$ be continuous. The representation is *decomposed generic* if there is a rational prime $q\ne l$ splitting completely in $L$ such that, for every $v\mid q$, it is unramified at $v$ and its Frobenius eigenvalues $\alpha_v,\beta_v$ satisfy $$\alpha_v/\beta_v\ne q,\qquad \beta_v/\alpha_v\ne q
 \quad\text{in }\overline{\mathbb F}_l.$$

This is [11, Definition 2.1.27]. Our construction will give $q\equiv1\pmod l$, so it is enough to make the two eigenvalues distinct at *every* place above $q$.

We use potential ordinarity of Galois representations in the convention of Section 2. The corresponding automorphic condition, called *$\iota$-ordinarity of weight zero*, is the ordinary Hecke condition used in [11, Theorem 5.2]. It is imposed at a sufficiently deep level and therefore allows ramified finite-order characters. We will obtain it only for quadratic twists of Steinberg, using the local calculation in [11, Lemma 6.1.3(4)].

**Theorem 6.2** (Caraiani–Newton, specialized form). *Let $L$ be a CM number field and $l$ an odd prime other than $5$. Let $r:G_L\to\mathop{\mathrm{GL}}_2(\overline{\mathbb Q}_l)$ be continuous, unramified outside finitely many places, with determinant $\epsilon_l^{-1}$. Suppose that $r$ is potentially semistable with labeled Hodge–Tate weights $0,1$ at every $v\mid l$, that $\overline r$ is decomposed generic, and that $\overline r|_{G_{L(\zeta_l)}}$ is absolutely irreducible.*

*Suppose there are a cuspidal weight-zero regular algebraic representation $\pi$ of $\mathop{\mathrm{PGL}}_2(\mathbb A_L)$ and an isomorphism $\iota:\overline{\mathbb Q}_l\xrightarrow{\sim}\mathbb C$ for which $\overline{r_\iota(\pi)}\simeq\overline r$. At each $v\mid l$, assume one of the following:*

(i) *Both local Galois representations are potentially crystalline; one is potentially ordinary of weight zero if and only if the other is; and $\mathop{\mathrm{rec}}_{L_v}(\pi_v)$ has zero monodromy.*

(ii) *Neither local Galois representation is potentially crystalline, and $\pi$ is $\iota$-ordinary of weight zero at $v$.*

*Then $r\simeq r_\iota(\Pi)$ for a cuspidal weight-zero regular algebraic representation $\Pi$ of $\mathop{\mathrm{PGL}}_2(\mathbb A_L)$.*

This is a sufficient-hypothesis specialization of [11, Theorem 5.2]. Its inverse-cyclotomic determinant hypothesis permits $l=3$, including residual image $\mathop{\mathrm{SL}}_2(\mathbb F_3)$; see [11, Remark 5.2.2]. No additional residual adequacy assumption is being made. All three applications below have $l=3$ or $l=p>100$.

**Theorem 6.3** (Elliptic starting point). *Let $L$ be a CM number field not containing $\zeta_5$, and let $A/L$ be a non-CM elliptic curve. If its mod-$5$ representation is decomposed generic and is absolutely irreducible on $G_{L(\zeta_5)}$, then $H^1(A)$ is realized by a cuspidal weight-zero regular algebraic representation of $\mathop{\mathrm{PGL}}_2(\mathbb A_L)$.*

This is [11, Theorem 6.1 and Lemma 6.1.3], after dualizing the Tate-module convention there when necessary. Absolute irreducibility and decomposed genericity in dimension two are preserved by duality.

For later use we also record the compatibility available after an elliptic curve itself is known to be modular.

**Theorem 6.4** (Compatibility for modular elliptic curves). *Let $D/L$ be a non-CM elliptic curve over a CM number field. Suppose that a regular algebraic cuspidal representation $\pi$ realizes $H^1(D)$ at one coefficient prime. Then $\pi$ has weight zero and trivial central character, realizes $H^1(D)$ at every coefficient prime and every coefficient isomorphism, and satisfies $$\iota\mathop{\mathrm{WD}}\bigl(H^1(D,\overline{\mathbb Q}_l)|_{G_{L_v}}\bigr)^{\mathrm{F\text{-}ss}}
 \simeq\mathop{\mathrm{rec}}^T_{L_v}(\pi_v)\qquad(v\nmid l).$$ If $D$ has potentially multiplicative reduction at $v\mid l$, then $\pi$ is $\iota$-ordinary of weight zero there.*

This is [11, Lemma 6.1.3]. For the intermediate systems, which need not come from elliptic curves, we use instead the general existence and good-place compatibility of $r_\iota(\pi)$ from [25, 30], and Varma’s equality of the underlying semisimplified Weil representations at $v\nmid l$ [40, Theorem 1]. The local reduction analysis in Section 7 will supply the additional facts needed in Theorem 6.2.

Here is what remains to be arranged for a single parameter $t\in U(K)$. The determinant and Hodge–Tate conditions hold for every parameter by Proposition 5.1. At places above $3p$, we will make the Jacobian of $C_n(t)$ potentially good ordinary, potentially good with all Newton slopes $1/2$, or potentially totally toric, according to the reduction type of $E$. This will make all four systems potentially crystalline and potentially ordinary, potentially crystalline but not potentially ordinary, or non-potentially crystalline, respectively. Section 7 obtains these properties from nonempty local open conditions on $t$.

Section 8 then chooses a parameter in those open sets for which the residual hypotheses hold. The pairs $(m,l)=(3,5),(3,p),(p,3)$ provide respectively the elliptic starting point and the first two lifts; the last lift uses the large mod-$p$ image of $E$. The two conjugates of $K$ must be considered together to obtain decomposed genericity. Once these properties have been proved, Section 9 propagates automorphy along the three congruences and descends to $K$.

## Prescribing the local reduction type

The degeneration at the origin allows us to arrange the same local behavior for every character summand of the covering curve. We first explain why the reduction type of an abelian variety is controlled, locally in a characteristic-zero family, by a sufficiently large finite torsion module. We then apply this observation to the Jacobian family and translate its reduction into the local conditions on the two-dimensional representations.

### Finite torsion and reduction in a local family

Throughout this section, a local field is a finite extension of $\mathbb Q_\ell$. In this subsection, the auxiliary torsion prime $d$ is different from $\ell$. If $A$ is an abelian variety, write $V_d(A)=T_d(A)\otimes_{\mathbb Z_d}\mathbb Q_d$ for its rational Tate module.

**Lemma 7.1** (Local constancy of finite torsion). *Let $L$ be a local field, let $X$ be a smooth $L$-variety, and let $\mathcal A\to X$ be an abelian scheme. For $x_0\in X(L)$ and an integer $N\geq 1$, there is an analytic neighborhood $\mathcal N$ of $x_0$ in $X(L)$ such that $$\mathcal A_x[N](\overline L)\simeq
 \mathcal A_{x_0}[N](\overline L)
 \qquad (x\in\mathcal N)$$ as $G_L$-modules.*

*Proof.* The group scheme $\mathcal A[N]$ is finite étale over $X$, since the base has characteristic zero. Equivalently, the scheme of full level-$N$ structures is a finite étale torsor over $X$ under the constant group $\mathop{\mathrm{GL}}_{2g}(\mathbb Z/N\mathbb Z)$, where $g$ is the relative dimension. Choose a finite Galois extension $L'/L$ over which the fiber of this torsor at $x_0$ splits. The inverse function theorem for an étale morphism gives a local section through each point of the fiber over a neighborhood of $x_0$ in $X(L')$. Shrinking that neighborhood, these sections enumerate all points in every nearby fiber. Intersecting its finitely many Galois conjugates, and shrinking once more if necessary, makes the neighborhood Galois stable and preserves the Galois permutations of the sections. The right action of the finite level group likewise preserves the same permutations after shrinking. Restricting to $X(L)$ therefore identifies the fibers as Galois sets with their level-group action, and hence identifies the underlying torsion modules. ◻

The finite torsion module will first ensure semistability and then identify a Frobenius polynomial. For the second step we use the polynomial on the *full* Tate module: this retains both the toric and the lattice pieces of the semistable representation.

**Lemma 7.2** (Finitely many semistable Frobenius polynomials). *Fix a local field $L$ with residue field of cardinality $Q$, an integer $g\geq 1$, and a prime $d$ different from the residue characteristic. For a semistable abelian variety $A/L$ of dimension $g$, let $$P_A(T)=\det\bigl(T-\operatorname{Frob}_L\mid V_d(A)\bigr),$$ where $\operatorname{Frob}_L$ is any lift of arithmetic Frobenius. Then $P_A(T)$ belongs to $\mathbb Z[T]$, is independent of the lift and of $d$, and ranges over a finite set depending only on $g$ and $Q$. Moreover, $P_A$ determines the toric rank of $A$; if that rank is zero, it also determines the Newton polygon of its good reduction.*

*Proof.* Let $r$ be the toric rank of $A$. The semistable filtration of Grothendieck identifies the graded pieces of $V_d(A)$ with the rational Tate module of a torus of rank $r$, the rational Tate module of an abelian variety of dimension $g-r$ with good reduction, and a lattice of rank $r$ [22, Exposé IX]. The character lattice of the torus and the lattice quotient have finite unramified Galois action. Consequently the arithmetic Frobenius eigenvalues on the toric and lattice graded pieces are respectively $Q$ times roots of unity and roots of unity. The middle piece has the $2(g-r)$ Frobenius eigenvalues of an abelian variety over $\mathbb F_Q$, all of complex absolute value $Q^{1/2}$.

Each graded piece has an integral characteristic polynomial independent of $d$: for the toric and lattice pieces this follows from the finite-order integral actions just described, together with the toric Tate twist; for the abelian piece it is the usual finite-field Frobenius polynomial. Inertia acts trivially on the graded pieces, so the product of these three polynomials is also independent of the lift of Frobenius. Every root has complex absolute value at most $Q$. Thus the coefficient of $T^{2g-j}$ has absolute value at most $\binom{2g}{j}Q^j$. Integral polynomials of fixed degree with these bounds form a finite set.

Exactly $r$ roots have absolute value $1$, exactly $r$ have absolute value $Q$, and the others have absolute value $Q^{1/2}$. Since $Q>1$, these three absolute values distinguish $r$. If $r=0$, semistability is good reduction, and the normalized $\ell$-adic valuations of the roots of $P_A$ are its Newton slopes. ◻

**Proposition 7.3** (Local constancy of the semistable type). *Let $L_0$ be a local field, let $X$ be a smooth $L_0$-variety, and let $\mathcal A\to X$ be an abelian scheme of relative dimension $g$. For $x_0\in X(L_0)$, there exist a finite extension $L/L_0$ and an analytic neighborhood $\mathcal N\subset X(L_0)$ of $x_0$ with the following properties. For every $x\in\mathcal N$, the abelian variety $\mathcal A_x$ is semistable over $L$ and has the same toric rank as $\mathcal A_{x_0}$ over $L$. If $\mathcal A_{x_0}$ has good reduction over $L$, then $\mathcal A_x$ has the same Newton polygon over $L$.*

*In particular, if $\mathcal A_{x_0}\simeq E_0^g$ for an elliptic curve $E_0/L_0$, every sufficiently nearby fiber has, after the same finite extension, the same one of the following three properties as $E_0^g$:*

1.  *good ordinary reduction;*

2.  *good reduction with all Newton slopes equal to $1/2$;*

3.  *semistable reduction of toric rank $g$.*

*Proof.* Choose an odd prime $d$ different from the residue characteristic. By semistable reduction, we may choose a finite extension $L/L_0$ over which $\mathcal A_{x_0}$ is semistable and all its $d$-torsion points are rational. Lemma 7.1, applied after base change to $L$, shows that, in a neighborhood of $x_0$, all nearby fibers also have rational $d$-torsion over $L$.

These fibers are semistable over $L$. Indeed, the matrix of any inertia element on their $d$-adic Tate module has the form $1+dB$ with $B$ integral. Each eigenvalue $\lambda$ therefore satisfies $v_d(\lambda-1)\geq 1$, where $v_d(d)=1$. The local monodromy theorem makes $\lambda$ a root of unity. For odd $d$ the only root of unity satisfying this inequality is $1$: a root with nontrivial prime-to-$d$ part has $v_d(\lambda-1)=0$, and a primitive $d^a$th root has valuation $1/(d^{a-1}(d-1))<1$. Thus every inertia element acts unipotently, and Grothendieck’s criterion gives semistability [22, Exposé IX].

Let $\mathcal P$ be the finite set of polynomials in Lemma 7.2 for dimension $g$ and the residue cardinality of $L$. Choose $j$ so large that reduction modulo $d^j$ is injective on $\mathcal P$. A second application of Lemma 7.1 gives, throughout a smaller neighborhood, $$\mathcal A_x[d^j](\overline L)\simeq
 \mathcal A_{x_0}[d^j](\overline L)
 \quad\text{as }G_L\text{-modules}.$$ Their full Frobenius polynomials are congruent modulo $d^j$, hence equal. Lemma 7.2 now gives the assertions about toric rank and Newton polygon. The inverse image of this neighborhood under $X(L_0)\to X(L)$ is a neighborhood of $x_0$, as required.

For the final assertion, choose $L$ so that $E_0$ has good or split multiplicative reduction. In the good case an elliptic curve is either ordinary or supersingular; in the latter case both its Newton slopes are $1/2$. In the multiplicative case $E_0^g$ has toric rank $g$. Enlarging $L$ to rationalize its $d$-torsion preserves these properties, so the preceding argument applies. ◻

### Monodromy of a totally toric abelian variety

The third possibility in Proposition 7.3 must force nonzero monodromy on *each* character summand, including when the coefficient prime is the residue characteristic. The rank statement needed for this is a consequence of the valuation pairing in toric uniformization. We give the argument at the residue characteristic as well, in terms of Kummer extensions.

**Lemma 7.4**. *Let $L/\mathbb Q_\ell$ be finite and let $A/L$ be an abelian variety of dimension $g$. Suppose that $A$ acquires semistable reduction of toric rank $g$ after a finite extension. For every prime $d$, the monodromy operator on the Weil–Deligne representation of $H^1_{\mathrm{et}}(A_{\overline L},\mathbb Q_d)$ has rank $g$. For $d=\ell$, the Weil–Deligne representation is the one attached to the potentially semistable representation by $\ell$-adic Hodge theory.*

*Proof.* Monodromy rank does not change after finite extension. We may therefore assume that $A$ has split toric uniformization $$A^{\mathrm{an}}\simeq (\mathbb G_m^g)^{\mathrm{an}}/\Lambda,$$ where $\Lambda\simeq\mathbb Z^g$ is rational over $L$. Choosing bases of the torus and lattice writes the periods as a matrix $(q_{ij})\in(L^\times)^{g\times g}$. The valuation pairing is nondegenerate, so $$\begin{equation}
\tag{7.1}
 \bigl(v_L(q_{ij})\bigr)_{1\leq i,j\leq g}
 \quad\text{is nonsingular.}
\end{equation}$$ This is the toric case of the monodromy pairing for a semistable abelian variety [22, Exposé IX]; its realization on de Rham cohomology is described in [12].

If $d\ne\ell$, the same pairing describes the monodromy map from the lattice quotient to the toric subspace of the Tate module. Its nondegeneracy gives rank $g$. We now prove this rank assertion for $d=\ell$.

Toric uniformization supplies an exact sequence $$\begin{equation}
\tag{7.2}
 0\longrightarrow\mathbb Q_\ell(1)^g\longrightarrow V_\ell(A)
   \longrightarrow\mathbb Q_\ell^g\longrightarrow0,
\end{equation}$$ whose extension classes are the Kummer classes of the $q_{ij}$. The representation is semistable, by the semistable comparison theorem for abelian varieties [12]. Let $L_{\mathrm{ur}}$ be the maximal unramified subfield of $L$, and write $D_{\mathrm{st}}$ for Fontaine’s semistable functor over $L$. On the two outer terms of (7.2), monodromy is zero. Consequently it induces a map $$\nu:D_{\mathrm{st}}(\mathbb Q_\ell^g)
       \longrightarrow D_{\mathrm{st}}(\mathbb Q_\ell(1)^g).$$ After the standard identifications, Frobenius on these two spaces is respectively $\sigma$ and $\ell^{-1}\sigma$, with $\sigma$ the Frobenius of $L_{\mathrm{ur}}/\mathbb Q_\ell$. The identity $N\varphi=\ell\varphi N$ therefore makes $\ker\nu\subset L_{\mathrm{ur}}^g$ stable under $\sigma$.

Suppose that $\nu$ has rank less than $g$. Finite Galois descent for $L_{\mathrm{ur}}/\mathbb Q_\ell$ then gives a nonzero vector $a=(a_j)\in\mathbb Q_\ell^g\cap\ker\nu$. Pull (7.2) back along the line spanned by $a$ in its trivial quotient. The resulting extension of $\mathbb Q_\ell$ by $\mathbb Q_\ell(1)^g$ is semistable and has zero monodromy, hence is crystalline. Under Kummer theory the Bloch–Kato crystalline subspace $H_f^1(L,\mathbb Q_\ell(1))$ is the kernel of the valuation map [6, Example 3.9]. Applying this to each coordinate of the pulled-back extension gives $$\sum_{j=1}^g a_jv_L(q_{ij})=0
 \qquad(1\leq i\leq g),$$ contrary to (7.1). Thus $N$ has rank $g$ on $V_\ell(A)$. Dualizing gives the same rank on $H^1_{\mathrm{et}}(A_{\overline L},\mathbb Q_\ell)$. ◻

### Open conditions on the original parameter

Return to the elliptic curve $E/K$, the odd integer $n=3p$, and $F=K(\mu_n)$. The Jacobian of the constant-$E$ cover $C_n$ extends over a neighborhood of $O$ in the parameter curve $E$, with fiber $E^n$ at $O$, by Proposition 3.3. Proposition 7.3 therefore applies at every finite completion of $F$. The following statement expresses the resulting neighborhoods in the original parameter $t\in U\subset\mathbb A^1_K$, so they can later be combined with Hilbert irreducibility.

**Proposition 7.5**. *For every place $v_0\mid 3p$ of $K$, there is a nonempty open subset $\Omega_{v_0}\subset U(K_{v_0})$ with the following property. Suppose that $t\in U(K)$ belongs to $\Omega_{v_0}$ for all $v_0\mid3p$, and set $J_t=\mathop{\mathrm{Jac}}(C_{n,t})$. At each place $v\mid3p$ of $F$, $J_t$ has the same one of the following potential reduction types as $E^n$:*

1.  *good ordinary reduction;*

2.  *good reduction with all Newton slopes $1/2$;*

3.  *semistable reduction of toric rank $n$.*

*For each $v$, the extensions giving these properties may be chosen in advance, independently of $t$ in the indicated open subsets.*

*Proof.* Fix $v_0\mid3p$. For each $v\mid v_0$, apply Proposition 7.3 to the extended Jacobian family over $F_v$, at the point $O$ of its parameter curve. This gives a neighborhood of $O$ in $E(F_v)$ and a fixed finite extension of $F_v$ on which the asserted reduction type holds. The inverse images of these finitely many neighborhoods in $E(K_{v_0})$ have an intersection that is again a neighborhood of $O$.

Choose $R_0\ne O$ in this intersection, sufficiently close to $O$ and away from the finitely many excluded parameters of the cover family. We may also avoid the ramification points of $x:E\to\mathbf P^1$, since these form a finite set. The local inverse function theorem gives a nonempty neighborhood $\Omega_{v_0}\subset U(K_{v_0})$ of $x(R_0)$ and an analytic lift $$R(t)=(t,y(t))\in E(K_{v_0}),\qquad y(t)^2=h(t),$$ whose image remains in the chosen intersection. Shrink the neighborhood so that $y(t)\ne0$ and it avoids all excluded parameters.

The map $$B_t\longrightarrow E,\qquad (x,y)\longmapsto(x,y(t)y)$$ is an isomorphism over $K_{v_0}$ carrying the marked point $(t,1)$ to $R(t)$. It carries the defining function for the cover to the function in the constant-$E$ construction: their divisors agree, and both have value $1$ at $O$. Thus it identifies the covers and their Jacobians at every $v\mid v_0$. The reduction conclusions follow from the choice of the neighborhoods. Carrying this out independently at the finitely many $v_0\mid3p$ proves the proposition. ◻

### The local representations of the character summands

For a prime $\ell$ and a rotation character $\theta$, write $V_{\theta,\ell}$ for the $\ell$-adic realization of the rank-two system in Section 5. Recall from Section 2 that the ordinary filtration of weight zero has an unramified character on its line and $\epsilon_\ell^{-1}$ times an unramified character on its quotient, after a finite extension. In the ordinary case below the distinguished line is already preserved before this extension.

**Corollary 7.6**. *Choose $t$ satisfying the open conditions of Proposition 7.5. Let $v\mid3p$ be a place of $F$, of residue characteristic $\ell$. Then, simultaneously for every rotation character $\theta$, the following conclusions hold.*

1.  *If $E$ has potentially good ordinary reduction at $v$, then $V_{\theta,\ell}|_{G_{F_v}}$ is potentially crystalline and potentially ordinary of weight $0$.*

2.  *If $E$ has potentially good supersingular reduction at $v$, then $V_{\theta,\ell}|_{G_{F_v}}$ is potentially crystalline and is not potentially ordinary of weight $0$.*

3.  *If $E$ has potentially multiplicative reduction at $v$, then the monodromy of $V_{\theta,d}|_{G_{F_v}}$ has rank one for every coefficient prime $d$, including $d=\ell$. In particular, $V_{\theta,\ell}|_{G_{F_v}}$ is not potentially crystalline.*

*Proof.* Choose a finite extension $L/F_v$ on which $J_t$ has the reduction given by Proposition 7.5. In the two good-reduction cases, crystalline comparison makes $H^1_{\mathrm{et}}(J_{t,\overline L},\mathbb Q_\ell)$, and hence each character summand, crystalline over $L$.

Suppose first that the reduction is ordinary. The connected–étale sequence of the ordinary $\ell$-divisible group, dualized to $H^1$, gives a filtration whose subrepresentation is unramified and whose quotient is $\epsilon_\ell^{-1}$ times an unramified representation. This filtration is functorial in endomorphisms and therefore stable under the rotations. It restricts to such a filtration on each $V_{\theta,\ell}$. By Proposition 5.1, this summand has dimension two and labeled Hodge–Tate weights $0,1$. Its unramified part contributes only weight $0$, whereas the quotient contributes only weight $1$; thus both parts have dimension one. This is the required ordinary filtration. After replacing $L$ by a finite Galois extension, its weight-zero line is uniquely determined by its inertia action, since $\epsilon_\ell$ has infinite image on the inertia of every finite extension. Conjugation by $G_{F_v}$ preserves that line, so the line descends to the original decomposition group.

If the reduction has all slopes $1/2$, the crystalline module of every summand has the same slope. These normalized slopes remain $1/2$ after further finite extension. An ordinary filtration of weight $0$ would provide a crystalline rank-one subrepresentation of parallel Hodge–Tate weight zero. For that character weak admissibility forces Newton slope zero, contradicting the slopes of the summand. Thus no such potential ordinary filtration exists.

Finally, suppose that $J_t$ has potentially toric rank $n$. Lemma 7.4 gives rank $n$ for monodromy on its $2n$-dimensional first cohomology, at every coefficient prime. Monodromy commutes with the rotations, so preserves the $n$ character summands. Each summand has dimension two. On first cohomology of a semistable abelian variety one has $N^2=0$, so the rank on each summand is at most one. Their ranks sum to $n$ and there are exactly $n$ summands; every rank is therefore one. Nonzero monodromy persists after finite extension and excludes potential crystallinity. ◻

## One specialization with all residual properties

We now choose a single parameter for the congruence chain. The geometric monodromy supplies irreducibility and suitable Frobenius elements, whereas Hilbert irreducibility allows us to retain these elements after imposing the local conditions of Section 7. To obtain decomposed genericity, we must control every place above a split rational prime. We therefore specialize the two conjugate parameter families together.

Throughout this section, $K,E,p,n,F,U$ have the meanings fixed in Section 5. In particular, $p>100$, $n=3p$, and $F=K(\mu_n)$. The pairs of covering degree and residual characteristic that require geometric monodromy are $$\begin{equation}
\tag{8.1}
 (m,\ell)=(3,p),\quad(3,5),\quad(p,3).
\end{equation}$$ In each case $\ell\nmid m$, so the residual cohomology decomposes into rotation-character spaces after extending its finite coefficient field.

### Consequences of the two monodromy transformations

**Lemma 8.1**. *For each pair in (8.1), the geometric monodromy of $H^1(C_m,\overline{\mathbb F}_\ell)$ on every nontrivial rotation-character space is absolutely irreducible. Its image contains opposite nonidentity root unipotents on that space. Moreover, one element of the geometric monodromy acts regular semisimply on all these nontrivial character spaces simultaneously. These statements also hold for the conjugate family over $K$.*

*Proof.* We first work with homology; duality will give the cohomological statements. On the character space with generator eigenvalue $\lambda\in\overline{\mathbb F}_\ell^\times$, the transformations of Theorem 4.5 have the form $$T_a=\begin{pmatrix}1&\sigma c_\lambda\\0&1\end{pmatrix},
 \qquad
 T_b=\begin{pmatrix}1&0\\\tau c_\lambda&1\end{pmatrix},
 \qquad
 c_\lambda=2-\lambda-\lambda^{-1},$$ where $\sigma,\tau\in\{1,-1\}$. Since $c_\lambda=-(\lambda-1)^2/\lambda$, it is nonzero when $\lambda\ne1$. The two matrices have different unique invariant lines, even over the algebraic closure. Hence their common representation is absolutely irreducible.

The product $T_aT_b^k$ has determinant one and trace $$\begin{equation}
\tag{8.2}
 2+\sigma\tau k c_\lambda^2.
\end{equation}$$ In odd characteristic, a determinant-one matrix is regular semisimple exactly when its trace is different from $2$ and $-2$. If $m=3$, then $\lambda+\lambda^{-1}=-1$, so $c_\lambda=3$ for both nontrivial characters. Take $k=2$. The two possible traces in (8.2) are $20$ and $-16$. Modulo $5$ these are $0$ and $4$, and neither equals $2$ or $-2$; modulo $p>100$ they again avoid $2$ and $-2$.

For $m=p$ and $\ell=3$, take $k=1$. Failure of regular semisimplicity would force $c_\lambda^2=4$ or $-4$, since $c_\lambda\ne0$. Multiplying either equation by $\lambda^2$ gives a polynomial of degree four over $\mathbb F_3$ satisfied by $\lambda$. Its degree over $\mathbb F_3$ is therefore some $d\le4$, and its order divides $3^d-1\le80$. This contradicts the fact that its order is the prime $p>100$. Thus the same product works for every nontrivial character in this case as well.

The transformations come from loops in the constant-elliptic-curve parameter space. As explained in Theorem 4.5, that family is a pullback of the family over $U$. Its monodromy image is therefore contained in the geometric monodromy image over $U$. Duality preserves absolute irreducibility, nonidentity unipotents, and regular semisimplicity. This proves the assertions for cohomology. The geometric argument applies to every complex elliptic curve, so it applies equally to the conjugate of $E$. ◻

### The original elliptic curve and its conjugate

The trivial character requires a different argument, since the geometric family varies only a quadratic twist of $E$. Its large residual image was built into the choice of $p$. The following count shows that no independence assumption between $E$ and its conjugate is necessary.

**Lemma 8.2**. *For every $t\in U(K)$, the representation $\overline V_{1,p}$ is absolutely irreducible on $G_{F(\zeta_p)}$ and is decomposed generic over $F$.*

*Proof.* Let $\Gamma$ be the image of $G_K$ on $E[p]$. The abelian extension $F/K$ implies that the image of $G_F$ contains $[\Gamma,\Gamma]$. Since $\Gamma$ contains $\mathop{\mathrm{SL}}_2(\mathbb F_p)$ and this group is perfect for $p>3$, its commutator subgroup is $\mathop{\mathrm{SL}}_2(\mathbb F_p)$: one inclusion follows from perfectness, and the other from the determinant map. Moreover, the determinant is trivial on $G_F$ because $\mu_p\subset F$. We have therefore proved $$\begin{equation}
\tag{8.3}
 \rho_{E,p}(G_F)=\mathop{\mathrm{SL}}_2(\mathbb F_p).
\end{equation}$$ The same equality holds for the conjugate curve $E^c$, where $c$ is the nontrivial automorphism of $K/\mathbb Q$, because $F/\mathbb Q$ is normal.

Consider the joint image $$J\subset\mathop{\mathrm{SL}}_2(\mathbb F_p)\times\mathop{\mathrm{SL}}_2(\mathbb F_p)$$ of $G_F$ on $E[p]$ and $E^c[p]$. Both projections are surjective. In $\mathop{\mathrm{SL}}_2(\mathbb F_p)$ there are exactly $p^2$ matrices of trace $2$. Indeed, writing a matrix as $\left(\begin{smallmatrix}a&b\\c&d \end{smallmatrix}\right)$, the trace and determinant conditions give $d=2-a$ and $bc=-(a-1)^2$. The value $a=1$ gives $2p-1$ choices for $(b,c)$; the other $p-1$ values of $a$ each give $p-1$ choices. Their sum is $p^2$. Replacing a matrix by its negative gives the same count for trace $-2$.

The order of $\mathop{\mathrm{SL}}_2(\mathbb F_p)$ is $p(p^2-1)$. Since each projection of $J$ has equal-sized fibers, the proportion of elements of $J$ whose image in at least one factor has trace $2$ or $-2$ is at most $$2\frac{2p^2}{p(p^2-1)}
 =\frac{4p}{p^2-1}<1.$$ Thus some element of $G_F$ acts regular semisimply on both $E[p]$ and $E^c[p]$.

Take a finite Galois extension of $\mathbb Q$ containing $F$ and the fields needed for these two residual actions. Conjugation by $G_\mathbb Q$ either preserves the two curves or exchanges them, and conjugates their residual matrices. The selected element and all its conjugates therefore act regular semisimply on the representation of $E$. Chebotarev supplies rational primes $q$ splitting completely in $F$ with this property at every $v\mid q$ of $F$. We exclude $p$ and the finitely many primes of bad reduction. Since $\mu_p\subset F$, these primes satisfy $q\equiv1\pmod p$. Distinct Frobenius eigenvalues then give the ratio condition in the definition of decomposed genericity.

The curve $B_t$ is a quadratic twist of $E$. Twisting multiplies residual matrices by scalar signs and hence preserves absolute irreducibility and eigenvalue ratios. Excluding the finitely many ramified primes of this twist leaves the same Chebotarev argument available. Finally, $\zeta_p\in F$, and taking the dual of $E[p]$ gives the residual $H^1$ realization. Proposition 5.2 now proves both assertions for $\overline V_{1,p}$. ◻

### Simultaneous specialization

We have obtained the requisite geometric elements and dealt with the trivial character. It remains to retain the geometric elements at one parameter and arrange that their Frobenius properties hold at all places above a rational prime. Restriction of scalars makes the two conjugate parameter families visible in the same finite Galois cover.

We next record precisely the specialization theorem needed to preserve these finite monodromy images. Allowing a constant field in the cover is essential: the Frobenius primes used below must split in a prescribed field.

**Lemma 8.3**. *Let $W$ be a nonempty open subset of $\mathbb A^d_\mathbb Q$, let $D/\mathbb Q$ be a finite Galois extension, and let $H$ be a finite quotient of $\pi_1(W)$ through which the constant-field map factors as $$\pi_1(W)\twoheadrightarrow H\twoheadrightarrow\mathop{\mathrm{Gal}}(D/\mathbb Q).$$ Prescribe nonempty open subsets of $W(\mathbb Q_r)$ for finitely many rational primes $r$. There is a point $x\in W(\mathbb Q)$ in all the prescribed opens for which the specialization map $s_x:G_\mathbb Q\to H$ is surjective. For this point, $$\begin{equation}
\tag{8.4}
 s_x(G_D)=\ker\bigl(H\longrightarrow\mathop{\mathrm{Gal}}(D/\mathbb Q)\bigr).
\end{equation}$$*

*Proof.* The quotient $H$ defines a connected finite $\acute etale$ Galois cover of $W$. Hilbert irreducibility with weak approximation gives a rational point in the prescribed local opens for which its fiber is connected; see [32, Proposition 3.3.1 and Theorem 3.5.3]. Connectedness of this Galois fiber is equivalent to surjectivity of $s_x$. Geometric connectedness of the cover is not required. The composition of $s_x$ with $H\to\mathop{\mathrm{Gal}}(D/\mathbb Q)$ is the usual restriction map of absolute Galois groups. Consequently, an element of $H$ in the displayed kernel has a preimage in $G_D$, which proves (8.4). ◻

**Proposition 8.4**. *Let $S_K$ be a finite set of finite places of $K$ containing all places above $3p$. For each $v_0\in S_K$, prescribe a nonempty open subset $\Omega_{v_0}\subset U(K_{v_0})$. There exists a single $t\in U(K)$ lying in every $\Omega_{v_0}$ such that the following assertions hold over $F=K(\mu_{3p})$.*

1.  *For each $(m,\ell)$ in (8.1) and each character $\theta$ of order $m$, the representation $\overline V_{\theta,\ell}$ is absolutely irreducible on $G_{F(\zeta_\ell)}$ and is decomposed generic.*

2.  *The representation $\overline V_{1,p}$ has these same two properties at $p$.*

3.  *The elliptic curve $A_t=\mathop{\mathrm{Jac}}(C_3(t)/\langle w\rangle)$ is non-CM.*

*In particular, when the opens above $3p$ are those of Proposition 7.5, this same parameter also satisfies all the local conclusions of Corollary 7.6.*

*Proof.* Put $$W=\mathop{\mathrm{Res}}_{K/\mathbb Q}U.$$ Since $U$ is an open subset of $\mathbb A^1_K$, the scheme $W$ is an open subset of $\mathbb A^2_\mathbb Q$. Choose a finite Galois extension $D/\mathbb Q$ containing $F$ and $\zeta_\ell$ for every residual characteristic in (8.1). Let $c$ be the nontrivial automorphism of $K/\mathbb Q$, and write $U^c$ and $\mathcal C_m^c$ for the conjugate parameter open and curve family. Then $$W_D\simeq U_D\times (U^c)_D.$$ For all three pairs, pull back the finite local system $H^1(C_m,\mathbb F_\ell)$ from the first factor and $H^1(C_m^c,\mathbb F_\ell)$ from the second.

Their joint monodromy has finite image on $\pi_1(W_D)$. Take the normal core, in $\pi_1(W)$, of the common kernel of these actions. It is an open normal subgroup contained in $\pi_1(W_D)$. The resulting finite quotient $H$ of $\pi_1(W)$ records every listed action and has a quotient $\mathop{\mathrm{Gal}}(D/\mathbb Q)$.

Over $\mathbb C$, a loop in either parameter factor acts trivially on local systems pulled back from the other factor. Thus the geometric monodromy transformations of Lemma 8.1 are available independently in both factors. In particular, for each fixed pair $(m,\ell)$ we can choose an element $h_{m,\ell}$ of the image of geometric monodromy that is regular semisimple on every nontrivial character space in both factors. To obtain it, take a product of the two factor loops furnished by that lemma. Every such element maps trivially to $\mathop{\mathrm{Gal}}(D/\mathbb Q)$. The quotient also contains the individual opposite unipotents on every character space.

The prescribed local conditions are compatible with this restriction of scalars. For a rational prime $r$ one has $$W(\mathbb Q_r)=\prod_{v_0\mid r}U(K_{v_0}).$$ The sets $\Omega_{v_0}$ therefore specify nonempty open subsets of $W(\mathbb Q_r)$ for the finitely many relevant $r$; at unprescribed factors impose no additional condition. Apply Lemma 8.3. It gives a point $x\in W(\mathbb Q)$, equivalently $t\in U(K)$, satisfying all these local conditions and inducing a surjection $G_\mathbb Q\to H$. Over $D$, this point has coordinates $(t,t^c)$ in the displayed product. Smooth proper base change identifies the specialized local systems with the residual cohomology of $C_m(t)$ and $C_m^c(t^c)$.

By (8.4), every geometric monodromy element used above is the image of an element of $G_D$. The opposite unipotents therefore survive on each specialized character space already over $G_D$, and prove its absolute irreducibility. Since $G_D\subset G_{F(\zeta_\ell)}$, this also proves absolute irreducibility on the latter group. Because $\ell\nmid m$, taking rotation eigenspaces in integral cohomology of $C_m$ commutes with reduction after adjoining the character values. These specialized character spaces are thus reductions of $V_{\theta,\ell}$. The rational identifications and independence of semisimplified reduction in Section 5 show that they give precisely $\overline V_{\theta,\ell}$, including when this system is defined using $C_n$.

To establish decomposed genericity, fix a pair $(m,\ell)$ and choose a preimage $g\in G_D$ of $h_{m,\ell}$. An element $\sigma\in G_\mathbb Q$ preserves or exchanges the two specialized covers $C_m(t)$ and $C_m^c(t^c)$, according to its restriction to $K$; it also permutes the rotation characters through its action on the roots of unity. The action of $\sigma g\sigma^{-1}$ on a character space of the first cover is therefore conjugate to the action of $g$ on some character space of one of the two covers. The construction imposed regular semisimplicity on all these spaces, so the property holds for every such conjugate.

The kernel of the surjective specialization $G_\mathbb Q\to H$ defines a finite Galois extension of $\mathbb Q$. It contains $D$. Chebotarev applied to the conjugacy class of $h_{m,\ell}$ in this extension gives rational primes $q$ whose Frobenius class is that class. They split completely in $D$, since $h_{m,\ell}$ is trivial on $D$. Discard $q=\ell$ and the finitely many primes where the curves or residual representations are ramified. For every $v\mid q$ of $F$, its Frobenius is represented by a conjugate of the selected element, and acts regular semisimply on each required character space. Here the residue degree is one because $q$ splits in $F$. Moreover, $q\equiv1\pmod\ell$ because $\zeta_\ell\in D$. Thus the ratio of the two Frobenius eigenvalues is different from $q$ in characteristic $\ell$, at every $v\mid q$. This is exactly decomposed genericity. A different $q$ may be used for each pair, as the definition permits. Assertion (2) follows from Lemma 8.2.

It remains to exclude CM for $A_t$. For $(m,\ell)=(3,p)$ the preceding specialization places two opposite nonidentity unipotents in the residual image of $V_{\eta,p}$. Proposition 5.2 identifies this with the residual cohomology of $A_t$: both are irreducible, so their common semisimplification is the representation itself. If $A_t$ had CM, all its endomorphisms would be defined over an extension of $F$ of degree at most two. Over that extension, the characteristic-zero Galois image lies in the commutative centralizer of the CM algebra. Its reduction is abelian as well. Consequently the full residual image would have an abelian normal subgroup of index at most two.

Each of the two unipotents has the odd prime order $p$, so both would belong to that abelian subgroup. But $$\begin{pmatrix}1&a\\0&1\end{pmatrix}
 \begin{pmatrix}1&0\\b&1\end{pmatrix}
 \ne
 \begin{pmatrix}1&0\\b&1\end{pmatrix}
 \begin{pmatrix}1&a\\0&1\end{pmatrix}
 \qquad(a b\ne0).$$ This contradiction proves (3). Finally, the local assertions follow by choosing the prescribed opens as in Proposition 7.5; the Hilbert specialization was made inside all those opens. ◻

## Propagation of automorphy and descent

We now fix a parameter $t\in U(K)$ supplied by Proposition 8.4, taking the local open sets of Proposition 7.5. Write $B=B_t$. The four systems $V_\eta,V_\chi,V_\psi,V_1$ have the congruences of Corollary 5.4, the local properties of Corollary 7.6, and the residual properties proved in Section 8. We first explain why automorphy at one coefficient prime supplies the information needed at the next one.

### Coefficient primes and local automorphic conditions

**Lemma 9.1**. *Suppose a weight-zero regular algebraic cuspidal representation $\pi$ of $\mathop{\mathrm{GL}}_2(\mathbb A_F)$ realizes one member of the compatible system $V_\theta$. Then it realizes every member, using the compatible coefficient embeddings fixed in Section 5.*

*Proof.* At all places outside a finite set and away from the coefficient prime, the characteristic polynomial of Frobenius on $V_\theta$ is independent of that prime, as an algebraic polynomial with the fixed embeddings of the character values. The good-place characteristic polynomials of $r_\iota(\pi)$ have the same compatibility. Equality at the original prime therefore identifies the polynomials at every other prime. Both representations are semisimple: for $V_\theta$ this follows from Faltings’ theorem as in Proposition 5.1, and the automorphic Galois representations are taken semisimple. Chebotarev density and the Brauer–Nesbitt theorem give the asserted isomorphism. ◻

The next lift also requires information about the local automorphic components at the new coefficient prime. We recover it by applying Varma’s comparison at a different coefficient prime, where it applies directly to the local Weil representation.

**Lemma 9.2**. *Suppose that a weight-zero regular algebraic cuspidal representation $\pi$ of $\mathop{\mathrm{PGL}}_2(\mathbb A_F)$ realizes $V_\theta$. Let $l\in\{3,p\}$ and $v\mid l$, and write $J_t=\mathop{\mathrm{Jac}}(C_n(t))$.*

(i) *If $J_t$ has potentially good reduction at $v$, then $\mathop{\mathrm{rec}}_{F_v}(\pi_v)$ has zero monodromy.*

(ii) *If $J_t$ acquires semistable reduction of toric rank $n$ at $v$, then $\pi_v$ is a quadratic or trivial twist of the Steinberg representation, and $\pi$ is $\iota_l$-ordinary of weight zero at $v$.*

*Proof.* Choose a coefficient prime $a$ different from the residue characteristic $l$. Lemma 9.1 identifies $r_{\iota_a}(\pi)$ with $V_{\theta,a}$. Varma’s local-global compatibility theorem identifies the underlying semisimplified Weil representations of its local Weil–Deligne parameter and $\mathop{\mathrm{rec}}^T_{F_v}(\pi_v)$ [40, Theorem 1]. We use this statement about the Weil representations first; equality of the monodromy operators is not assumed.

In the potentially good case, pass to an extension where the Jacobian has good reduction. All Frobenius eigenvalues on its $H^1$, and hence on the character summand, have complex absolute value the square root of the residue cardinality. Taking a positive power of Frobenius shows that the two eigenvalues before this extension also have the same absolute value. A rank-two Weil–Deligne representation with nonzero monodromy has Frobenius eigenvalues differing by the norm character. They cannot have the same absolute value. Thus the automorphic parameter has zero monodromy. The Tate twist in (2.1) does not change this conclusion.

In the totally toric case, Corollary 7.6 gives nonzero monodromy on $V_{\theta,a}$. Its semisimplified Weil representation is therefore a sum of two characters differing by the norm. For this Weil representation, the two possibilities under the local Langlands correspondence for $\mathop{\mathrm{GL}}_2$ are the special parameter with nonzero monodromy and the zero-monodromy parameter of a one-dimensional local representation. The latter is not generic. Since every local component of a cuspidal automorphic representation of $\mathop{\mathrm{GL}}_2$ is generic, $\pi_v$ is a twist of Steinberg. Its central character is trivial, so the twisting character has square one.

The local calculation in the proof of [11, Lemma 6.1.3(4)], which invokes the proof of [21, Lemma 5.6], shows that a quadratic twist of Steinberg is $\iota_l$-ordinary of weight zero. This calculation uses only the stated local representation and trivial central character. In particular, it also applies when the quadratic character is ramified: the ordinary condition is imposed at a sufficiently deep level, and a finite-order twist multiplies the relevant normalized Hecke eigenvalues by units. ◻

### The three lifts

**Proposition 9.3**. *The elliptic curve $B/F$ is modular. More precisely, $H^1(B)$ is realized by a cuspidal weight-zero regular algebraic representation of $\mathop{\mathrm{PGL}}_2(\mathbb A_F)$.*

*Proof.* The order-three system $V_\eta$ is $H^1(A)$ for the elliptic curve $A/F$ of Proposition 5.2. It is non-CM by Proposition 8.4. Its mod-$5$ representation is decomposed generic and absolutely irreducible over $F(\zeta_5)$ by the $(m,l)=(3,5)$ part of that proposition. Since $\zeta_5\notin F$, Theorem 6.3 supplies a cuspidal weight-zero representation of $\mathop{\mathrm{PGL}}_2(\mathbb A_F)$ realizing $V_\eta$.

Apply Theorem 6.2 in the following order:

| Automorphic input | Coefficient prime | System lifted | Residual input  |
|:-----------------:|:-----------------:|:-------------:|:---------------:|
|     $V_\eta$      |        $p$        |   $V_\chi$    |  $(m,l)=(3,p)$  |
|     $V_\chi$      |        $3$        |   $V_\psi$    |  $(m,l)=(p,3)$  |
|     $V_\psi$      |        $p$        |     $V_1$     | $H^1(B)\bmod p$ |

In each row Corollary 5.4 identifies the residual representations, and Proposition 8.4 gives decomposed genericity and absolute irreducibility over the cyclotomic extension. Proposition 5.1 supplies the determinant, finite ramification, potential semistability, and labeled Hodge–Tate weights. Lemma 9.1 makes the previously obtained automorphy available at the coefficient prime of the next row.

It remains to check the local hypotheses at that prime. At a place of potentially good ordinary type, both systems in the row are potentially crystalline and potentially ordinary of weight zero. At a place of potentially good supersingular type, they are potentially crystalline and neither is potentially ordinary of weight zero. These assertions follow from Corollary 7.6. In either case Lemma 9.2(i) gives zero monodromy in the input automorphic parameter. At a place of potentially totally toric type, neither Galois representation is potentially crystalline, and Lemma 9.2(ii) gives automorphic ordinarity. Thus the relevant alternative of Theorem 6.2 holds at every place above the coefficient prime.

The theorem therefore applies in all three rows. Its conclusion preserves cuspidality, weight zero, and trivial central character, so each row provides the input required for the next. The last row gives automorphy of $V_1=H^1(B)$. ◻

### Descending to the original field

We recall why automorphy over the cyclotomic extension suffices here. The character adjustment in the following argument is important: it identifies the descended Galois representation with the prescribed one.

**Lemma 9.4**. *Let $L'/L$ be a cyclic extension of prime degree between CM fields. Let $r:G_L\to\mathop{\mathrm{GL}}_2(\overline{\mathbb Q}_l)$ be a continuous representation whose restriction to $G_{L'}$ is absolutely irreducible. Suppose that this restriction is realized by a cuspidal weight-zero regular algebraic representation $\Pi$ of $\mathop{\mathrm{GL}}_2(\mathbb A_{L'})$. Then $r$ is realized by a cuspidal weight-zero regular algebraic representation of $\mathop{\mathrm{GL}}_2(\mathbb A_L)$.*

*Proof.* For $\sigma\in\mathop{\mathrm{Gal}}(L'/L)$, the representations $\Pi^\sigma$ and $\Pi$ have the same good-place Hecke polynomials, because the associated Galois representation extends to $G_L$. Strong multiplicity one makes $\Pi$ Galois invariant. The cyclic base-change theorem therefore gives a cuspidal automorphic representation $\pi$ of $\mathop{\mathrm{GL}}_2(\mathbb A_L)$ whose base change is $\Pi$ [28, 3]. Every archimedean place is complex, so its local extension is trivial. Consequently $\pi$ is regular algebraic of weight zero.

Good-place compatibility with base change and Chebotarev imply $$\bigl(r_\iota(\pi)|_{G_{L'}}\bigr)^{\mathrm{ss}}
 \simeq r|_{G_{L'}}.$$ The right-hand side is absolutely irreducible. The restriction on the left is therefore already irreducible and isomorphic to it, without semisimplification. After choosing this isomorphism, the two representations agree on $G_{L'}$. For $g\in G_L$, their matrices at $g$ differ by a scalar, since they induce the same conjugation on the absolutely irreducible representation of $G_{L'}$. Schur’s lemma shows that these scalars form a character $\delta:\mathop{\mathrm{Gal}}(L'/L)\to\overline{\mathbb Q}_l^{\times}$ and $$r_\iota(\pi)\simeq r\otimes\delta.$$ The finite-order Hecke character corresponding to $\delta^{-1}$ removes this discrepancy. Twisting preserves cuspidality and weight zero, and the compatibility with Galois twisting follows at good places and hence everywhere by Chebotarev. ◻

Since $F/K$ is abelian, choose a tower from $K$ to $F$ with cyclic prime-degree steps. Each intermediate field is abelian over $\mathbb Q$ and contains the imaginary quadratic field $K$, hence is CM. The representation $H^1(B,\overline{\mathbb Q}_p)$ remains absolutely irreducible over $F$: its residual representation is already absolutely irreducible there. Apply Lemma 9.4 down the tower to Proposition 9.3. This gives automorphy of $B/K$. Finally, $B$ is the quadratic twist of $E$ by $h(t)$, so twisting the automorphic representation by the same quadratic Hecke character gives a cuspidal weight-zero representation $\pi_E$ realizing $H^1(E)$.

### Local parameters and the CM case

For non-CM $E$, Theorem 6.4 shows that $\pi_E$ has trivial central character, realizes $H^1(E)$ for every coefficient prime, and has the required Frobenius-semisimplified Weil–Deligne parameter at each finite place, by choosing a coefficient prime different from the residue characteristic. Thus every finite local $L$-factor matches. At infinity a cuspidal representation is generic. The archimedean classification with weight-zero infinitesimal character therefore gives exactly the parameter (2.2); the finite-dimensional alternative is not generic. Equations (2.1) and (2.3) give the stated normalization of the local and global $L$-functions.

Suppose now that $E$ has complex multiplication by an imaginary quadratic field $M$. Its endomorphisms are defined over $KM$. One way to see this is to use their faithful action on invariant differentials: the eigenvalues lie in $M$, and are fixed by $G_{KM}$. The main theorem of complex multiplication expresses the two one-dimensional constituents of $H^1(E)|_{G_{KM}}$ as the realizations of algebraic Hecke characters, with the infinity types prescribed by the CM type [33].

If $M\not\subset K$, Galois exchanges the two characters and $H^1(E)$ is induced from either one over the quadratic extension $KM/K$. Automorphic induction gives the required representation of $\mathop{\mathrm{GL}}_2(\mathbb A_K)$. If $M=K$, use the isobaric sum of the two characters. In either case normalize the resulting representation by $|\det|^{1/2}$ so that its Tate-normalized parameter realizes $H^1(E)$. Complex multiplication and local class field theory, together with local compatibility of quadratic automorphic induction in the first case, give the finite parameters and the prescribed infinity types. These are the CM alternatives allowed in Theorem 1.1. Their central character is trivial: the determinant of $H^1(E)$ is $\epsilon_l^{-1}$, so undoing the Tate normalization gives determinant one for the local automorphic parameters, and hence trivial central character.

In both the CM and non-CM cases, the finite factors also agree if one uses the Weil–Deligne representation at the residue-characteristic coefficient prime. For good reduction this follows from crystalline comparison. For bad potentially good reduction, the Weil–Deligne inertia action is finite and nontrivial, and monodromy is zero. The inertia action has determinant one. Its invariant subspace cannot have dimension one, since a semisimple two-dimensional determinant-one representation with a nonzero fixed vector would be trivial. It therefore has no invariants, giving local factor one. At the residue-characteristic coefficient prime, nontriviality of inertia follows from the crystalline good-reduction criterion [12]. Finally, in the potentially multiplicative case the Tate-curve description, allowing a quadratic twist, gives the same special Weil–Deligne parameter at all coefficient primes. This completes the proof of Theorem 1.1.

## References

**[1]** Patrick B. Allen, Frank Calegari, Ana Caraiani, Toby Gee, David Helm, Bao V. Le Hung, James Newton, Peter Scholze, Richard Taylor, and Jack A. Thorne, *Potential automorphy over CM fields*, Annals of Mathematics **197** (2023), no. 3, 897–1113.

**[2]** Patrick B. Allen, Chandrashekhar Khare, and Jack A. Thorne, *Modularity of $\operatorname{GL}_2(\mathbb{F}_p)$-representations over CM fields*, Cambridge Journal of Mathematics **11** (2023), no. 1, 1–158.

**[3]** James Arthur and Laurent Clozel, *Simple algebras, base change, and the advanced theory of the trace formula*, Annals of Mathematics Studies, vol. 120, Princeton University Press, Princeton, NJ, 1989.

**[4]** Tobias Berger and Gergely Harcos, *$l$-adic representations associated to modular forms over imaginary quadratic fields*, International Mathematics Research Notices **2007** (2007), no. 23, Art. ID rnm113, 16.

**[5]** Luigi Bianchi, *Sui gruppi di sostituzioni lineari con coefficienti appartenenti a corpi quadratici immaginarı̂*, Mathematische Annalen **40** (1892), no. 3, 332–412.

**[6]** Spencer Bloch and Kazuya Kato, *$L$-functions and Tamagawa numbers of motives*, The Grothendieck Festschrift, Vol. I, Progress in Mathematics, vol. 86, Birkhäuser Boston, Boston, MA, 1990, pp. 333–400.

**[7]** Siegfried Bosch, Werner Lütkebohmert, and Michel Raynaud, *Néron models*, Ergebnisse der Mathematik und ihrer Grenzgebiete, 3. Folge, vol. 21, Springer-Verlag, Berlin, 1990.

**[8]** George Boxer, Frank Calegari, Toby Gee, and Vincent Pilloni, *Abelian surfaces over totally real fields are potentially modular*, Publications Mathématiques de l’IHÉS **134** (2021), 153–501.

**[9]** Christophe Breuil, Brian Conrad, Fred Diamond, and Richard Taylor, *On the modularity of elliptic curves over $\mathbb{Q}$: wild 3-adic exercises*, Journal of the American Mathematical Society **14** (2001), no. 4, 843–939.

**[10]** Frank Calegari and David Geraghty, *Modularity lifting beyond the Taylor–Wiles method*, Inventiones Mathematicae **211** (2018), no. 1, 297–433.

**[11]** Ana Caraiani and James Newton, *On the modularity of elliptic curves over imaginary quadratic fields*, 2025, Preprint, arXiv:2301.10509v3, 27 March 2025.

**[12]** Robert Coleman and Adrian Iovita, *The Frobenius and monodromy operators for curves and abelian varieties*, Duke Mathematical Journal **97** (1999), no. 1, 171–215.

**[13]** John E. Cremona, *Hyperbolic tessellations, modular symbols, and elliptic curves over complex quadratic fields*, Compositio Mathematica **51** (1984), no. 3, 275–324.

**[14]** John E. Cremona and E. Whitley, *Periods of cusp forms and elliptic curves over imaginary quadratic fields*, Mathematics of Computation **62** (1994), no. 205, 407–429.

**[15]** Henri Darmon, *Modularity of fibres in rigid local systems*, Annals of Mathematics **149** (1999), no. 3, 1079–1086.

**[16]** to3em, *Rigid local systems, Hilbert modular forms, and Fermat’s last theorem*, Duke Mathematical Journal **102** (2000), no. 3, 413–449.

**[17]** Henri Darmon and Jean-François Mestre, *Courbes hyperelliptiques à multiplications réelles et une construction de Shih*, Canadian Mathematical Bulletin **43** (2000), no. 3, 304–311.

**[18]** Pierre Deligne and Nicholas Katz (eds.), *Groupes de monodromie en géométrie algébrique. II (SGA 7 II)*, Lecture Notes in Mathematics, vol. 340, Springer-Verlag, Berlin–New York, 1973.

**[19]** Jordan S. Ellenberg, *Endomorphism algebras of Jacobians*, Advances in Mathematics **162** (2001), no. 2, 243–271.

**[20]** Gerd Faltings, *Endlichkeitssätze für abelsche varietäten über zahlkörpern*, Inventiones Mathematicae **73** (1983), no. 3, 349–366.

**[21]** David Geraghty, *Modularity lifting theorems for ordinary Galois representations*, Mathematische Annalen **373** (2019), no. 3-4, 1341–1427.

**[22]** Alexandre Grothendieck, Michel Raynaud, and Dock Sang Rim, *Groupes de monodromie en géométrie algébrique. I (SGA 7 I)*, Lecture Notes in Mathematics, vol. 288, Springer-Verlag, Berlin–New York, 1972.

**[23]** Fritz Grunewald, Hermann Helling, and Jens Mennicke, *$\operatorname{SL}_2$ over complex quadratic number fields. I*, Algebra i Logika **17** (1978), no. 5, 512–580.

**[24]** Günter Harder, *Eisenstein cohomology of arithmetic groups. The case $\operatorname{GL}_2$*, Inventiones Mathematicae **89** (1987), 37–118.

**[25]** Michael Harris, Kai-Wen Lan, Richard Taylor, and Jack Thorne, *On the rigid cohomology of certain Shimura varieties*, Research in the Mathematical Sciences **3** (2016), Paper No. 37, 308.

**[26]** Michael Harris, David Soudry, and Richard Taylor, *$l$-adic representations associated to modular forms over imaginary quadratic fields. I. Lifting to $\operatorname{GSp}_4(\mathbb{Q})$*, Inventiones Mathematicae **112** (1993), 377–411.

**[27]** Robert P. Langlands, *Problems in the theory of automorphic forms*, Lectures in Modern Analysis and Applications III (C. T. Taam, ed.), Lecture Notes in Mathematics, vol. 170, Springer, Berlin, 1970, pp. 18–61.

**[28]** to3em, *Base change for $\operatorname{GL}(2)$*, Annals of Mathematics Studies, vol. 96, Princeton University Press, Princeton, NJ, 1980.

**[29]** Jean-François Mestre, *Familles de courbes hyperelliptiques à multiplications réelles*, Arithmetic Algebraic Geometry (Texel, 1989), Progress in Mathematics, vol. 89, Birkhäuser Boston, Boston, MA, 1991, pp. 193–208.

**[30]** Peter Scholze, *On torsion in the cohomology of locally symmetric varieties*, Annals of Mathematics **182** (2015), no. 3, 945–1066.

**[31]** Jean-Pierre Serre, *Propriétés galoisiennes des points d’ordre fini des courbes elliptiques*, Inventiones Mathematicae **15** (1972), 259–331.

**[32]** to3em, *Topics in Galois theory*, 2 ed., Research Notes in Mathematics, vol. 1, A K Peters, Wellesley, MA, 2008, With notes by Henri Darmon.

**[33]** Goro Shimura and Yutaka Taniyama, *Complex multiplication of abelian varieties and its applications to number theory*, Publications of the Mathematical Society of Japan, vol. 6, Mathematical Society of Japan, Tokyo, 1961.

**[34]** Richard G. Swan, *Generators and relations for certain special linear groups*, Advances in Mathematics **6** (1971), no. 1, 1–77.

**[35]** Walter Tautz, Jaap Top, and Alain Verberkmoes, *Explicit hyperelliptic curves with real multiplication and permutation polynomials*, Canadian Journal of Mathematics **43** (1991), no. 5, 1055–1064.

**[36]** Richard Taylor, *$l$-adic representations associated to modular forms over imaginary quadratic fields. II*, Inventiones Mathematicae **116** (1994), 619–643.

**[37]** to3em, *Remarks on a conjecture of Fontaine and Mazur*, Journal of the Institute of Mathematics of Jussieu **1** (2002), no. 1, 125–143.

**[38]** Richard Taylor and Andrew Wiles, *Ring-theoretic properties of certain Hecke algebras*, Annals of Mathematics **141** (1995), no. 3, 553–572.

**[39]** Takeshi Tsuji, *$p$-adic étale cohomology and crystalline cohomology in the semi-stable reduction case*, Inventiones Mathematicae **137** (1999), no. 2, 233–411.

**[40]** Ila Varma, *Local-global compatibility for regular algebraic cuspidal automorphic representations when $\ell\ne p$*, Forum of Mathematics, Sigma **12** (2024), Paper No. e21, 32.

**[41]** Andrew Wiles, *Modular elliptic curves and Fermat’s last theorem*, Annals of Mathematics **141** (1995), no. 3, 443–551.
