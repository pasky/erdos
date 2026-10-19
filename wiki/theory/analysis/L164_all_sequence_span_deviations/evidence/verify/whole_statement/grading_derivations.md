---
name: theory/analysis/L164_all_sequence_span_deviations/evidence/verify/whole_statement/grading_derivations
title: "Mathematical assessment of the retained derivations"
desc: Mathematical checks used to grade the unchanged one-sided report, including the transport, planar bound, localization and separate extrema.
created: 2026-10-15T20:39:29Z
updated: 2026-10-15T20:39:29Z
---

# Mathematical assessment of the retained derivations

***

Examination date: 2026-10-15. Reading: the complete
[unchanged report](report.md), its complete
[retained derivations](review_derivations.md), and all twelve
mathematical payloads named by its
[subject manifest](../../assets/whole_statement/returned/assets/review/subject/manifest.json), including every
supplied proof. These are grading checks of the existing evidence. They
neither repair the subject nor replace a missing part of its review.

The three groups below follow the report's three identified weakest steps.
The final operations for the two consequences are checked separately.
All calculations are analytic. There is no finite numerical experiment,
computational certificate or second independent review cycle.

## 1. One-sided error, label transport and all scales

The relevant inputs are the [circle model](../../assets/whole_statement/returned/assets/review/subject/model_and_theorem.md.txt),
[Lemma 2.1](../../assets/whole_statement/returned/assets/review/subject/lemma_2_1.md.txt),
[Lemma 6.1](../../assets/whole_statement/returned/assets/review/subject/lemma_6_1.md.txt),
[Lemma 6.2](../../assets/whole_statement/returned/assets/review/subject/lemma_6_2.md.txt),
[Lemma 6.3](../../assets/whole_statement/returned/assets/review/subject/lemma_6_3.md.txt), their
[all-sequence transfers](../../assets/whole_statement/returned/assets/review/subject/all_sequence_transfer.md.txt),
and [Proposition 6.4](../../assets/whole_statement/returned/assets/review/subject/proposition_6_4.md.txt).

Let the ordered prefix have nonnegative cyclic gaps \(g_i\) summing to one.
Then \(S_i=\sum_{j=0}^{r-1}g_{i+j}\) and
\(\sum_iS_i=r\). For \(d_i=S_i-r/n\), \(\sum_i d_i=0\).
The upper alternative bounds each \(d_i\) by \(A/n\); the lower
alternative bounds each \(-d_i\) by \(A/n\). Each separately gives

$$
\sum_i|d_i|=2\sum_i(d_i)_+=2\sum_i(-d_i)_+\le 2A.
$$

This is the exact bridge that the proof needs. It does not give the
pointwise two-sided hypothesis of Lemma 2.1 with the same budget.

The report's two proposed refutations of that stronger bridge are valid.
At \(n=r^2+r\), for \(r\ge2\), \(r\) consecutive zero gaps followed by
\(r^2\) gaps of size \(r^{-2}\) give \((nM-r,r-nm)=(1,r)\).
For the other witness, use one gap
\((r+n-1)/(nr)\) and \(n-1\) gaps \((r-1)/(nr)\).
They sum to one. An \(r\)-span without the exceptional gap has length
\((r-1)/n\); one with it has length \(r/n+(n-r)/(nr)\).
Thus the deviation pair is \((r,1)\). Partial sums realize both gap lists
as circle points. These witnesses disprove the hypothetical shortcut,
not an eventual assertion about an infinite sequence. The report makes
that distinction, and the frozen proof never uses the shortcut.

At real time \(t\), writing \(n=\lfloor t\rfloor\), changing the center
adds \(r(t-n)/t\). Summing the \(k\) shifted \(r\)-spans therefore gives

$$
\sum_p|L_{t,k}(p)-kr/t|
\le 2kA+kr(t-n)/t\le 2kA+kr/t.
$$

Each cyclic shift is a permutation even if \(r\) and \(n\) share a
divisor. Repetitions are separate labels, so nested prefixes and the
forward/backward moves remain injections. With
\(s=t/(1-ut/(kr))\), the displacement of the forward-then-backward
injection is

$$
L_{t,k}(p)-L_{s,k}(B_sF_t(p))
=u+\eta_u(p),\qquad
\sum_p|\eta_u(p)|\le4kA+2kr/t.
$$

The second error is summed over an injective subset of the later prefix.
No lower bound on individual gaps is necessary. A real displacement
\(\eta\), reduced modulo one only for membership, changes the interval
indicator in \(L^1\) by at most \(2|\eta|\). Integrating the counting
error gives \(8kA+4kr/t\).

The two full comparisons in Lemma 2.1 also survive at their own stronger
hypothesis. For \(t_+=(1+q)t\), enlarge the interval by
\(k(a_t+A)/t\) on the left and \(k(b_t+A)/t\) on the right.
Its length is at most \((D+3kA)/t\). For
\(t_-=(1-q)t\), the reverse injection displaces by \(-u+\eta\);
shrink by \(ka_t/t+kA/t_-\) and \(kb_t/t+kA/t_-\).
The remaining length, multiplied by \(t_-/D\), is at least
\((1-q-(kA/D)(3-q))_+\). The strict left endpoint and inclusive right
endpoint give the stated containment in each direction. For the empty
shrunk arc the assertion reduces to nonnegativity.

For either comparison, integrating one atom at a time proves

$$
\int_0^\ell N(J+u)\,du
=\int_JN((v,v+\ell])\,dv.
$$

This is a circle identity, including intervals crossing the origin.
Finite endpoint sets affect none of these integrals. Dividing by
\(D\ell\) gives precisely (2.2) and (2.3). The comparison times are
independent of \(D\), and bounded \(D\) bounds all enlarged arc lengths.
Thus their asserted uniform onset is justified.

For Lemma 6.2 the same integral identity yields a constant
\((1+q)D\), rather than \(D\). Subtracting \(D\) leaves the essential
\(qD\) term. Positivity and integration give

$$
Z_t(D)\le\frac{(1+q)D}{E}Z_{(1+q)t}(E)
          +qD+8kA+\frac{4kr}{t}.
$$

The maps are measurable in the averaging variable: only finitely many
integer prefixes occur in each fixed comparison interval. Hence no
unstated convergence or probabilistic premise enters the integration.

The terminal estimate needs its own check at coincident points. Off the
finite set of positions, choose the last lifted label \(j\) below \(x\).
Exactly the ending indices \(j+1,\ldots,j+r\) satisfy
\(y_{i-r}<x\le y_i\). Consequently the ending span arcs cover \(r\)
times even when some are empty and others have full length one. Pair
each with the arc of length \(r/t\) sharing its right endpoint; the
symmetric-difference measure is the absolute difference of their lengths.
It follows that

$$
\|\Delta_t(\cdot,r)\|_1\le2A+r(t-n)/t,\qquad
\int\Delta_t(\cdot,r)=-r(t-n)/t.
$$

The identity \(2f_+=|f|+f\) proves \(Z_t(r)\le A\).
The report correctly retains this negative real-time mean. For example,
if all labels coincide, precisely \(r\) of the ending arcs are full
turns and the others are empty; the covering multiplicity is still \(r\).
At late times full turns can also be excluded under either hypothesis
as stated in the transfer extract, but the cover itself needs no such
exclusion.

The periodic lift for \(r=qn+s>n\), \(0\le s<n\), gives
\(y_{i+r}-y_i=q+y_{i+s}-y_i\). It must not be replaced by a shorter
circular distance. All actual span estimates and walks are used only
after \(\lfloor t\rfloor>kr\). The early prefixes in localization use
counts, including \(N_0=0\), and do not invoke an undefined small-prefix
span theorem.

The explicit constants in the report check out. Set
\(\Lambda=\log(r/A)\ge20\), \(\theta=e^{-\Lambda/2}\), \(K=\sqrt{Ar}\),
and \(C_2=e^{20}\). There are at most \(2\Lambda\) scale comparisons.
With \(k=\lceil D/K\rceil\), \(q\le2\theta\),
\(kA/D\le2\theta\), and \(4kr/(tD)\le8r/(Kt)\).
The recurrence coefficient \(1+18\theta\) is a valid enlargement of
\(1+q\), since \(z\ge0\). Its product is less than three:
\(18h\theta\le36\Lambda e^{-\Lambda/2}\le720e^{-10}<1\).
Iteration from \(z(r)\le\theta^2\) gives

$$
z_t(K)\le111\theta\Lambda+\frac{24hr}{Kt}
\le112\theta\Lambda
$$

at one sufficiently late time threshold depending on \(r,A\) and the
sequence. In the final descent \(E=K,k=1\), so all maps and time
requirements except the arc-length condition are independent of \(D\).
For \(0<D\le S=K/\Lambda^2\),

$$
Z_t(D)\le8A+225D\theta\Lambda+4r/t\le233A+4r/t.
$$

At integer \(n>S\) with \(4r/n\le A\), mean zero gives
\(\|\Delta_n(\cdot,D)\|_1=2Z_n(D)\le468A\).
The case \(D=0\) is identically zero. Thus \(C_3=468\) and the
single threshold for the entire continuum \(0\le D\le S\) are supported,
not inferred from pointwise eventual bounds.

Assessment: the report's first weakest-step derivation is complete and
supports both sequence alternatives separately, with the exact interfaces
needed by their respective consequences.

## 2. The planar proof and its endpoint convention

The [full local planar proof](../../assets/whole_statement/returned/assets/review/subject/halasz_bound.md.txt)
is assessed, rather than an appeal to an unprovided publication.
For \(I=[a,a+\ell)\) and the signed Haar function used there,

$$
\int xh_I(x)\,dx=\ell^2/4,\qquad
\psi_I(q)=\int{\bf1}_{q<x}h_I(x)\,dx
=\begin{cases}
\min(q-a,a+\ell-q),&a<q<a+\ell,\\
0,&\text{otherwise}.
\end{cases}
$$

In particular both dyadic endpoints contribute zero. Tensor multiplication
gives (H0) with area term \(-M|R|^2/16\).
At total level \(n\) with \(2^{n-2}\le M<2^{n-1}\), at least
\(2^{n-1}\) rectangles of each shape have empty interior. Choosing the
coefficient signs gives
\(\langle D,f_k\rangle\ge1/128\). Repetitions cannot increase the
number of occupied interiors beyond \(M\). At any total level \(s\),
the point terms sum in absolute value to at most \(M2^{-s}/4\);
the area terms add at most \(M2^{-s}/16\). This proves (H2)'s
\(5M2^{-s}/16\).

For indices \(k_1<\cdots<k_j\), restrict the product to a rectangle
of shape \((k_j,n-k_1)\). Every sign and every binary digit in the
factors is fixed except the next digit in each coordinate. The remaining
product is the Haar function on that rectangle, with a sign. Thus the
product is an \(r\)-function of total level \(n+k_j-k_1\), as required
by (H3). There is no assumption of statistical independence.

For the Riesz product, group a subset of indices by its diameter \(d\).
For a fixed minimum and maximum, the intermediate-index sum is
\(\alpha^2(1+\alpha)^{d-1}\); there are \(n-d+1\) positions for the
extremes. Hence every subset size is accounted for, and

$$
|\langle D,\Gamma_2\rangle|
\le\frac5{16}M2^{-n}\alpha^2
\sum_{d=1}^n(n-d+1)2^{-d}(1+\alpha)^{d-1}
\le\frac5{16}(n+1)\alpha^2.
$$

The last inequality uses \(M2^{-n}<1/2\) and the geometric sum
\(1/(1-\alpha)\le2\). Even terms need not cancel; the estimate
bounds them too. With \(\alpha=1/(80\sqrt{n+1})\) the linear pairing
has modulus at least \(\sqrt{n+1}/10240\), the entire remainder at
most \(1/20480\), and
\(\|\Gamma\|_\infty<20001/10000\).
Since \(2s-1\ge s\) for \(s=\sqrt{n+1}\ge1\), the exact comparison

$$
20480\cdot20001=409620480<410000000=41000\cdot10000
$$

proves \(\|D\|_1\ge\sqrt{n+1}/41000\).
Finally \(\log M<(n-1)\log2<n+1\); \(M=1\) has target zero.
The claimed constant is valid on the whole stated list domain.

The strongest convention attack is substantive: the singleton \((0,0)\)
has norms \(3/4\) and \(1/4\) for the two anchored conventions, so
equality almost everywhere would be false. The frozen proof and report
instead compare tensor Haar coefficients. A zero-coordinate contribution
is constant in at least one variable in the first convention and absent
in the second, so its tensor pairing is zero either way. The area term
keeps the full \(M\). The subtraction of one from the product removes
its constant term, and all remaining factors are the \(r\)-functions
already checked. Therefore the same pairing argument proves the second
convention directly. This is a supplied transfer, not a repair by the
grader.

Assessment: all of (H0)--(H4), the constant calculation and both anchored
conventions survive. The report's second weakest-step derivation supplies
the entire planar input consumed downstream.

## 3. Localization, absolute constants and separate consequences

Use the [localization proof](../../assets/whole_statement/returned/assets/review/subject/lemma_7_2.md.txt)
and [both closing comparisons](../../assets/whole_statement/returned/assets/review/subject/one_sided_comparison.md.txt).
For fixed \(S,B\) let \(L=\lfloor S\rfloor\), \(w=L/N<1\), and
\(M_a=N_N((a,a+w])\). The small-interval hypothesis gives
\(\int|M_a-L|\le B\). The localized points
\(((x_i-a)/w,i/N)\) belong to \((0,1]^2\); their second coordinates
are distinct even for repeated circle positions.

The condition on the time coordinate is exactly \(i\le\lfloor Nv\rfloor\).
Thus their planar discrepancy differs from
\(G_a(u,v)=N_{\lfloor Nv\rfloor}((a,a+uw])-Luv\)
by \((L-M_a)uv\), whose norm is \(|L-M_a|/4\).
If \(B<L/4\), the set \(|M_a-L|\le L/2\) has measure at least one
half. Applying the planar result there gives

$$
\int\|G_a\|_1\,da
\ge \frac{c_H}{2}\sqrt{\log(L/2)}-\frac B4.
$$

For the opposite estimate set \(n=\lfloor Nv\rfloor\) and
\(D=nuw\le L\le S\) whenever \(n\) exceeds the hypothesis's onset
\(n_0\). The center error is at most \(L/N\). On the remaining strip
of width \(n_0/N\), use the elementary bound \(n_0+L\).
Consequently

$$
\int\|G_a\|_1\,da
\le B+\frac LN+\frac{n_0(n_0+L)}N.
$$

Both bounds hold for each \(N\). No localization point or good set is
passed to the limit. Keeping \(L,n_0\) fixed and taking the scalar
error to zero yields
\(B\ge(2c_H/5)\sqrt{\log(L/2)}\).
For \(S\ge64\), \(L/2\ge S/4\ge\sqrt S\), giving the report's
\(c_4=c_H/5=1/205000\). The other case \(B\ge L/4\) satisfies
\(B\ge S/8\ge\sqrt S\ge\sqrt{\log S}\), so the same constants work.

Now set \(c=c_4/(4C_3)>0\),
\(R=\max(64,c^{-2})\), \(r_0=\lceil e^R\rceil\).
For \(r\ge r_0\), \(H=\log r\), \(A=c\sqrt H\ge1\), one has
\(H/2\le\Lambda=H-\log A\le H\), so \(\Lambda\ge32>20\) and
\(r\ge C_2A\). Also

$$
\log S=\tfrac12(H+\log A)-2\log\Lambda
\ge H/2-2\log H\ge H/3,\qquad H\ge64.
$$

The last inequality follows because \(H-12\log H\) is positive at
64 and increasing thereafter. These bounds ensure every size condition
of Proposition 6.4 and Lemma 7.2, with \(B=C_3A\).

For the upper theorem, a contrary limsup strictly below \(A\) gives
eventual upper control. The positive centered-span mass argument in
section 1, the scale estimate and localization would force
\(c_4/4\ge c_4/\sqrt3\), a contradiction. For the lower theorem, a
contrary limsup gives eventual lower control; the negative mass argument
gives exactly the same chain and contradiction. These are independent
applications to the two fixed alternatives. Their exceptional starting
times may depend on the sequence and \(r\); \(c,r_0\) do not.

For the infimum consequence, every sequence satisfies
\(\limsup_n nM_n^{(r)}\ge r+c\sqrt{\log r}\).
The infimum of these numbers satisfies the same lower bound, without
attainment or exchanging operations. For the supremum consequence use
\(0\le nm_n^{(r)}\le r\) and

$$
\limsup_n(r-nm_n^{(r)})=r-\liminf_n nm_n^{(r)}.
$$

Every inner liminf is therefore at most \(r-c\sqrt{\log r}\);
taking their supremum proves its own deficit bound. Each deficit then
diverges because the same positive constant multiplies
\(\sqrt{\log r}\).

The report's dyadic witness distinguishes the limit conventions exactly.
Start at zero and insert each level's grid midpoints clockwise from zero.
For \(m=2^j\le n<2m\) the gap lengths lie between \(1/(2m)\) and
\(1/m\). At \(n=m\), both scaled span extrema are \(r\).
For \(m>r\), at \(n=2m-r\) there remain \(r\) consecutive unsplit
gaps, giving \(nM=(2m-r)r/m\to2r\). At \(n=m+r\), the first \(r\)
original gaps have split into \(2r\) consecutive short gaps, giving
\(nm=(m+r)r/(2m)\to r/2\). The global bounds imply

$$
(\liminf nM,\limsup nM)=(r,2r),\qquad
(\liminf nm,\limsup nm)=(r/2,r).
$$

In particular the incorrect subtraction from \(\limsup nm\) gives zero,
while the correct deviation limsup is \(r/2\). The example also proves
\(r\le\Lambda_r\le2r\); all inner minima lie in \([0,r]\), so
\(0\le\lambda_r\le r\). It does not purport to compute either optimum.
Allowing a different sequence for each \(r\) cannot change the universal
inequalities proved before either extremum.

Assessment: the report's third weakest-step derivation, both sequence
contradictions, the separate infimum and supremum deductions, and both
divergences are supported in their exact stated units and quantifiers.

The local source attributions remain those in the
[preserved provenance](../../assets/whole_statement/returned/assets/review/subject/provenance_and_scope.md.txt):
Korsky's cited work is unrefereed; Halász's theorem is credited through
Bilyk; Larcher's finite-list attribution is contextual here; and the
original local proof with constants and composition is credited to Plasma
AI. The publications were not read. This assessment establishes no
original-paper fidelity, ratio result, literal original growth expression,
optimal constant or acceptance of the whole catalog problem.
