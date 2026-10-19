---
desc: Independent adversarial examination of the complete union-closed-family bounds in Theorems 1.1 and 1.2 and Corollary 1.3 of the specified arXiv version.
---

# Adversarial examination of the union-closed-family bounds

## Subject and independence

**Examination date:** 2026-10-15 UTC. **Subject frozen:** 2026-10-15 at
13:17:10.128162 UTC, as recorded in the supplied neutral manifest.
**Reviewer:** independent mathematical examiner, disclosed model gpt-6-astra.
The reviewer neither authored nor collaborated on the subject and received no
earlier review or author working context. The examination was charged to find
a counterexample, an unsupported essential inference, or a convention failure.

The subject is the complete $F/F_k$ content of Theorems 1.1 and 1.2 and
Corollary 1.3(i)--(iv) of Deep Bhattacharjee, Priyabrata Mandal and Ushashi
Bhattacharya, *Resolving Erdos-Ulam Monochromatic Union-Closed Family
Conjectures*, arXiv:2610.02833v1, original Erdos.tex. The source's theorem
labels and mathematical credits remain theirs. The neutral model and packet
assembly are Plasma AI work; the independent derivations in this report are
also Plasma AI work. The Gowers method credit and the Sauer and Shelah
citations are retained below.

Only the supplied frozen extraction was examined. Its input root, relative to
the repository, is
subject/ in this retained mathematical record.
An exact retained copy accompanies this report at the repository-relative root
subject/ beside this report.
The table below names every mathematical input relative to either root.
The manifest retains mathematical selections; private revision and operating
identity records are separate from this mathematical report.

The two assigned pins resolved, the charter and recorded subject pin agreed,
and the supplied files matched their frozen manifests. The subject remained
unchanged throughout the examination. The reviewer did not extract a source
from Git or inspect the full manuscript archive. The manifest's repository
source revision identifies the material used to assemble the packet; its
separate packet-pinning rule identifies the review subject. No inference about
an unexamined version is made.

The permitted mathematical reading consisted exactly of the following files.
All were read in full, including every supplied proof and static figure source.
Source-line locators are those supplied by the manifest; they were not checked
against an unlisted archive or PDF.

| Retained input | Actual reading and source locator |
| --- | --- |
| [manifest.json](subject/manifest.json) | Whole neutral scope, selection and identity record. |
| [model.md.txt](subject/model.md.txt) | Whole model, 21 lines; neutral restatement of Erdos.tex 120--145. |
| [notation.tex.txt](subject/notation.tex.txt) | Whole notation, 20 lines; Erdos.tex 46--65. |
| [statements.tex.txt](subject/statements.tex.txt) | Whole retained statements, 52 lines; selections from Erdos.tex 180--191, 195--207 and 213--234. |
| [cubes_and_gluing.tex.txt](subject/cubes_and_gluing.tex.txt) | Whole, 155 lines; Erdos.tex 414--568, including every definition and proof. |
| [box_and_supersaturation.tex.txt](subject/box_and_supersaturation.tex.txt) | Whole, 155 lines; Erdos.tex 576--730, including both proofs and the Gowers credit. |
| [lower_proof.tex.txt](subject/lower_proof.tex.txt) | Whole, 109 lines; Erdos.tex 763--871, including slices, averaging, constants and threshold. |
| [upper_proof.tex.txt](subject/upper_proof.tex.txt) | Whole retained text, 63 lines; selection from Erdos.tex 874--936, including Lemma 5.1 and the entire retained theorem proof. |
| [corollary_proof.tex.txt](subject/corollary_proof.tex.txt) | Whole, 33 lines; Erdos.tex 951--983, all four clauses. |
| [source_references.tex.txt](subject/source_references.tex.txt) | Whole, 20 lines; Erdos.tex 1552--1556 and 1597--1608. |
| [fig-holecube.tex.txt](subject/figures/fig-holecube.tex.txt) | Whole, 37 lines; static original figure source. |
| [fig-chain.tex.txt](subject/figures/fig-chain.tex.txt) | Whole, 60 lines; static original figure source. |
| [fig-union.tex.txt](subject/figures/fig-union.tex.txt) | Whole, 24 lines; static original figure source. |
| [fig-box.tex.txt](subject/figures/fig-box.tex.txt) | Whole, 55 lines; static original figure source. |
| [provenance_and_scope.md.txt](subject/provenance_and_scope.md.txt) | Whole, 46 lines; source identity, exact scope and external-premise boundary. |

The operating reading was separate: README, campaign/AGENTS and both
verification contracts in full; anatomy at Claims, Evidence, Tiers and
Project claims; the research guide at Reading only; the permitted charter,
configuration, steps, effective-settings record, command help and relevant
operating skills. For report preparation, math_authoring was read in full,
weaving at its relationship/authoring and fence sections, and evidence at
Statements and proof scope, Source fidelity, Mathematical review and its
subsections, and Erdos-specific. These instructions supplied no mathematical
premise. Their links were not followed.

Isolation was supported by the accepted blind, sealed, local, no-sync
configuration and empty subscription inspections. More directly, the reviewer
read no inbox, feed, sibling report, author inspection account, canonical
mathematical page, ledger, live agent configuration, unlisted source, or
internet material. No excluded exposure occurred. Outbound communication was
limited to an operational notice and the authorized delivery of this report.
No reply or mathematical steering was consumed.

This is a text-based whole-proof mathematical examination, with the explicit
Sauer--Shelah premise stated below. It is not original-PDF fidelity, TeX
rendering, kernel validation, source installation, source acceptance, or an
examination of the excluded sublattice quantity $f$. The other source versions
named in the provenance file were not read or substituted.

## Model and quantified restatements

For every positive integer $n$, write $[n]=\{1,\ldots,n\}$. For an integer
$k\ge2$, a coloring is any map $\chi:2^{[n]}\to[k]$, with unused colors
allowed. A family $\mathcal A\subseteq2^{[n]}$ is union-closed if
$A\cup B\in\mathcal A$ for every $A,B\in\mathcal A$. There is no
intersection requirement and no requirement that $\varnothing\in\mathcal A$.
Put

$$
F_k(n)=\min_\chi\max\{|\mathcal A|:
 \mathcal A\text{ is monochromatic and union-closed}\},
\qquad F(n)=F_2(n).
$$

Both extrema are attained over finite collections. A singleton family is
always available, so $1\le F_k(n)\le2^n$. Embedding the two colors in $[k]$
shows $F_k(n)\le F(n)$: the maximum for each embedded coloring is unchanged,
and the minimum is then taken over a larger set of colorings. These statements
concern cardinalities of actual families, not the number of their generators.

### Theorem 1.1: polynomial bound

For every pair of integers $k\ge2$, $t\ge1$, define

$$
M=t^2k^{2^t},
\qquad
c_{k,t}=\bigl(k^{2^t+1}t^t(4M^2)^{t+1}\bigr)^{-1}.
$$

For every integer $n\ge1$ and every $k$-coloring of all subsets of $[n]$,
there is a monochromatic union-closed family of at least
$c_{k,t}n^{t+1}$ members. Equivalently,
$F_k(n)\ge c_{k,t}n^{t+1}$. The constant depends on both $k$ and $t$,
not on $n$ or the coloring.

### Theorem 1.1: two-color threshold

For every integer $t\ge1$ and positive integer $n$ with
$\log_2 n\ge(t+2)^2 2^t$, one has $F(n)\ge n^t$.
The non-strict threshold includes equality.

### Theorem 1.2: binomial bound

For every positive integer $n$ and integer $d\ge1$ satisfying the strict
hypothesis $2^d>nd+2$,

$$
F(n)\le\sum_{j=0}^{d-1}\binom nj.
$$

Here $\binom nj=0$ for $j>n$. There is no hypothesis $d\le n$.

### Theorem 1.2: explicit choice

For every integer $n\ge2$, the integer

$$
d=\lfloor\log_2 n\rfloor
  +\lfloor\log_2\lfloor\log_2 n\rfloor\rfloor+3
$$

satisfies the strict hypothesis above and gives

$$
F(n)\le d\,n^{d-1}
\le(\log_2 n+\log_2\log_2 n+3)
       n^{\log_2 n+\log_2\log_2 n+2}.
$$

### Corollary 1.3(i)

For every integer $n\ge2$, with $\ell=\log_2\log_2 n$ and
$\omega(n)=\ell-2\log_2(\ell+2)-1$,
$F(n)\ge n^{\omega(n)}$, and $\omega(n)\to\infty$ as $n\to\infty$.
Negative values of the displayed exponent are permitted.

### Corollary 1.3(ii)

There exists a real-valued function $\varepsilon$ on the positive integers
such that $\varepsilon(n)\to0$ and
$F(n)<(1+\varepsilon(n))^n$ for every positive integer $n$.
The asserted inequality is strict at every $n$, including $n=1$.

### Corollary 1.3(iii)

For every real-valued function $\omega$ on the positive integers such that
$F(n)\ge n^{\omega(n)}$ for every positive integer $n$, and every real
$\varepsilon>0$, there exists $N$ such that
$\omega(n)\le(1+\varepsilon)\log_2 n$ for every integer $n\ge N$.
No monotonicity or divergence assumption on this $\omega$ is made.

### Corollary 1.3(iv)

For each fixed integer $k\ge2$, there exist real-valued functions
$\omega_k,\varepsilon_k$ on the positive integers with
$\omega_k(n)\to\infty$ and $\varepsilon_k(n)\to0$, such that

$$
n^{\omega_k(n)}\le F_k(n)<(1+\varepsilon_k(n))^n
\quad\text{for every integer }n\ge1.
$$

The lower-growth assertion is for each fixed $k$; it does not assert
uniform divergence when $k$ is allowed to grow with $n$.

## Three weakest steps, independently rederived

The three derivations below cover the delicate internal interfaces rather
than treating same-paper lemmas as accepted premises. The consequence checks
following them give the remaining deductions and the strongest attacks for
each assigned conclusion.

### 1. From the box inequality to one usable cube shape

The consumed text is box_and_supersaturation.tex.txt, lines 10--141, together
with the cube and shape definitions in cubes_and_gluing.tex.txt, lines 4--72.

A cube with disjoint base $U$ and nonempty disjoint generators
$X_1,\ldots,X_t$ has $2^t$ different vertices: membership of any point of
$X_i$ recovers whether generator $i$ was selected. Union of two vertices
corresponds to union of their index sets; intersection corresponds to
intersection of those index sets. The top-down description follows by
complementing the index set inside $[t]$. This also handles $t=0$, when the
cube is the singleton $\{U\}$. The intersection identity is used only to
understand this cube, not to strengthen the assigned family model.

Two cubes of the same ordered shape are carried to one another by a
permutation: biject corresponding base, generator and unused parts. Right
composition by that permutation bijects the permutations producing a
monochromatic image. Thus $\rho_\chi(u;a_1,\ldots,a_t)$ is independent of
the chosen representative. Uniform permutations give uniform images on
their orbit, since fibers have equal size. Equal generator sizes or
different representations of the same cube do not affect this argument.
The proof never assumes that different shapes are equally likely.

Here is an independent induction for the box inequality, using products of
two slices rather than the source's first application of Cauchy--Schwarz.
Write $\mathcal B_t(f)$ for the box average of a nonnegative function.
For $t=0$ it is the value at the sole point of $G^0$. For $t\ge1$, take
$a,a'\in G$, $y\in G^{t-1}$ and put $q=2^{t-1}$. Applying the induction
hypothesis to the nonnegative function
$y\mapsto f(a,y)f(a',y)$ gives

$$
\begin{aligned}
\mathcal B_t(f)
&=\mathbb E_{a,a'}\mathcal B_{t-1}
          \bigl(y\mapsto f(a,y)f(a',y)\bigr)\\
&\ge\mathbb E_{a,a'}
          \bigl(\mathbb E_y f(a,y)f(a',y)\bigr)^q\\
&\ge\bigl(\mathbb E_y(\mathbb E_a f(a,y))^2\bigr)^q\\
&\ge(\mathbb E f)^{2q}.
\end{aligned}
$$

The second inequality is Jensen for the exponent $q\ge1$, after exchanging
finite sums and using independence of $a,a'$. The last is
Cauchy--Schwarz applied to the mean over $y$. All quantities are
nonnegative, so raising them to $q$ preserves inequalities. This proves
the exponent $2^t$ without an assumption about the desired conclusion.
The source's induction also works: its first squared mean is bounded by
Cauchy--Schwarz, and its subsequent slice bound and Jensen inequality have
the same nonnegative domains. For $t=1$, $q=1$ makes the relevant Jensen
step an equality.

A uniform distribution on $G$ presupposes $G\ne\varnothing$ when $t>0$.
The application uses $G=\{0,\ldots,L\}$ with $L\ge1$, so it satisfies this
domain condition. No assertion about a uniform random point of an empty
set is needed.

For fixed $\sigma$, let $p_c$ be the density of color $c$ on this grid.
The box inequality applied to each color indicator and Jensen give

$$
\Pr(E\mid\sigma)\ge\sum_{c=1}^k p_c^{2^t}
\ge k^{1-2^t}.
$$

The monochromatic events for different colors are disjoint even for
degenerate boxes. The event $D$ that some coordinate pair coincides has
probability at most $t/(L+1)$, by a union bound. Therefore

$$
\Pr(E\setminus D)\ge k^{1-2^t}-\frac{t}{L+1}.
$$

For a pair outside $D$, put $\ell_i=\min(x_i,x'_i)$ and
$h_i=\max(x_i,x'_i)$. The sets at its vertices have base
$U=S(\ell)$ and generators consisting of positions
$\ell_i+1,\ldots,h_i$ in chain $Z_i$. Disjoint chains make these
generators disjoint from each other and from the base. Their shape satisfies

$$
u=r+\sum_i\ell_i,\qquad
a_i=h_i-\ell_i\ge1,\qquad
(u-r)+\sum_i a_i=\sum_i h_i\le tL=M.
$$

There is no conditioning error when a single shape is chosen. For each
nondegenerate pair its conditional probability over $\sigma$ is exactly
the corresponding $\rho_\chi$. Writing its nonnegative sampling weight
as $w_\eta$,

$$
\Pr(E\setminus D)=\sum_{\eta\notin D}w_\eta\rho_\chi(\eta)
\le \max_{\eta\notin D}\rho_\chi(\eta).
$$

The nondegenerate collection is nonempty because $L\ge1$; for instance,
the all-zero and all-one grid points form such a pair. The weights sum to
at most one. Thus the maximum is a value for an admissible shape, including
when the displayed general lower bound is zero or negative. No shape
uniformity, and no shape independent of the given coloring, is asserted.

For $L=t k^{2^t}$ and $M=tL$, the degeneracy loss satisfies
$t/(L+1)<k^{-2^t}$. The surviving lower bound is strictly larger than
$(k-1)k^{-2^t}$, hence at least $k^{-2^t}$ for every $k\ge2$.
Also $u-r\le M-t$ and every $a_i\le M$. These are exactly the interfaces
used by the slices argument. The numerical examples
$M_2(1)=4$, $M_2(2)=64$, $M_2(3)=2304$ follow directly, and
$M\ge4t^2\ge t+1$ for all allowed $k,t$.

This derivation discharges the internal box and supersaturation obligations.
The source's description of a box norm and its Gowers attribution supply
method context; no norm theorem or result from Gowers's paper is imported.

### 2. From separately good slices to one large union-closed family

The consumed text is lower_proof.tex.txt, lines 4--109, and the block-chain,
union-rule and gluing arguments in cubes_and_gluing.tex.txt, lines 74--155.
The main attack is that existence of a good shape for each slice need not
give one block vector good for many pairs. The exact incidence count below
supplies that missing implication; it does not assume simultaneous choices.

Let $m=\lfloor(n-1)/M\rfloor$ and $s=\lfloor m/2\rfloor$, initially in the
regime $s\ge t$. Then $m\ge2$, and $m$ disjoint slots of size $M$ fit
inside $[n]$. Every vector $\beta\in[M]^m$ specifies nonempty disjoint
blocks. For $A\subseteq[j-1]$ with $|A|=t$, freeze the coordinates
outside $A\cup\{j\}$ and put

$$
R=\sum_{\substack{i<j\\i\notin A}}\beta_i,\qquad r=R+1.
$$

There are exactly $m-t-1$ frozen coordinates. Since $j\ge t+1$,

$$
0\le R\le(j-1-t)M\le(m-2)M,
\qquad
r+M\le(m-1)M+1\le n.
$$

Supersaturation therefore supplies a shape $(u;a_1,\ldots,a_t)$ with
$u-r=z\in[0,M-t]$ and $\rho_\chi\ge k^{-2^t}$.
Taking $\beta_j=z+1$ and assigning $a_1,\ldots,a_t$ in increasing order
to the indices in $A$ gives entries in $[M]$ and exactly the desired
shape: its base size is $R+\beta_j=u$. In particular, the $+1$ both makes
the level block nonempty and matches the base. This works at $j=t+1$,
where $R=0$, as well as at later levels.

Every fixed assignment extends, and different frozen assignments yield
different full vectors. Consequently there are at least $M^{m-t-1}$
good vectors for each pair. This lower bound does not say that their sets
of extensions have a large intersection.

Set
$\mathcal P=\{(j,A):s<j\le m,\ A\subseteq[s],\ |A|=t\}$.
For each good vector at one pair, at least $n!k^{-2^t}$ permutations
make its cube monochromatic. Counting incidences between pairs
$(\sigma,\beta)$ and elements of $\mathcal P$ gives at least

$$
|\mathcal P|\,M^{m-t-1}\,n!k^{-2^t}
$$

incidences among $n!M^m$ pairs $(\sigma,\beta)$. Hence at least one
common pair has at least
$|\mathcal P|k^{-2^t}M^{-(t+1)}$ monochromatic cubes.
No independence between these cube events is used. A real-valued lower
bound on an integer count is legitimate, with the integer automatically
at least its ceiling.

It remains to turn this cube count into cardinality of a union-closed
family. Write $H(j,B)=C_j\setminus Y_B$. For $j\le j'$ and
$B,B'\subseteq[j]$, a point in a block with index at most $j$ is missing
from the union precisely when both factors omit it; blocks with indices
between $j+1$ and $j'$ are all present. Thus

$$
H(j,B)\cup H(j',B')=H(j',B\cap B').
$$

For the cubes being glued, $B,B'\subseteq[s]$ and $j>s$, so this
identity applies. Choose a color possessed by at least $1/k$ of the
selected monochromatic cubes. Their union as families is monochromatic.
The union of two of its members lies in the cube at the larger level:
$B\cap B'\subseteq B'\subseteq A'$. This proves closure in the actual
union-family model without requiring intersections or an empty member.

Cube overlap cannot erase the needed cardinality. The base
$H(j,A)$ contains the whole nonempty block $Y_j$, contains no later
block, and omits exactly the blocks with indices in $A$ among $[s]$.
It therefore determines $j$ and $A$. These bases inject the chosen pairs
into the glued family, giving at least

$$
\frac{|\mathcal P|}{k^{2^t+1}M^{t+1}}
$$

distinct members. An empty selection would make the gluing conclusion
trivial; in the large-parameter application the positive incidence bound
already yields a nonempty selection.

For $n\ge4M(t+1)$, the floor estimates are valid including at equality.
Because $n$ and $M(m+1)$ are integers, $n-1<M(m+1)$ implies
$n\le M(m+1)\le2M(s+1)$. Thus $s\ge2t+1$, which establishes every
needed condition $s\ge t$ and $1\le s<m$. Also $n\le4Ms$ and $m-s\ge s$.
For $s\ge t$ each factor $(s-i)/(t-i)$, $0\le i<t$, is at least $s/t$,
because $i(s-t)\ge0$. It follows that

$$
|\mathcal P|=(m-s)\binom st
\ge \frac{s^{t+1}}{t^t}
\ge\frac{n^{t+1}}{t^t(4M)^{t+1}}.
$$

Combining the two denominators gives
$M^{t+1}(4M)^{t+1}=(4M^2)^{t+1}$, with exactly the stated
$k^{2^t+1}$ factor. This proves the polynomial bound in the large regime.
For $1\le n<4M(t+1)\le4M^2$,

$$
c_{k,t}n^{t+1}
=\frac{(n/(4M^2))^{t+1}}{k^{2^t+1}t^t}<1\le F_k(n).
$$

Thus no value of $n$ is lost when slots and slices are unavailable.
At the cutoff itself, $m=4t+3$ and $s=2t+1$, so the large-regime
argument begins without a floor ambiguity.

For the two-color threshold, expanding the constant gives exactly

$$
\log_2(c_{2,t}^{-1})
=(2t+3)2^t+(5t+4)\log_2 t+2t+3.
$$

For all integers $t\ge1$, the elementary induction
$2^{t-1}\ge t$ implies both $\log_2 t\le t-1$ and $2^t\ge2t$.
The remainder is bounded by

$$
\begin{aligned}
(5t+4)\log_2 t+2t+3
&\le5t^2+t-1\\
&\le2t(t+1)^2\\
&\le(t+1)^2 2^t.
\end{aligned}
$$

For the middle inequality, the difference is
$2t^3-t^2+t+1=t^2(2t-1)+t+1>0$.
Since $(2t+3)+(t+1)^2=(t+2)^2$, this proves
$\log_2(c_{2,t}^{-1})\le(t+2)^2 2^t$ for every allowed $t$.
In particular, $t=1$ gives $c_{2,1}=2^{-15}$ and a permitted threshold
$\log_2 n\ge18$; it is not an omitted exception. At any allowed threshold
$c_{2,t}n\ge1$, so the already established all-$n$ polynomial bound
implies $F(n)\ge n^t$.

### 3. From nonempty unions to the probabilistic upper bound

The consumed text is upper_proof.tex.txt, lines 4--60. Its sole external
step is Lemma 5.1(c), with the exact Sauer--Shelah interface recorded
separately below.

If $(A_1,\ldots,A_d)$ is an independent system and $x_i$ is private to
$A_i$, the $x_i$ are distinct. The trace of $\bigcup_{i\in I}A_i$ on
$X=\{x_1,\ldots,x_d\}$ is exactly $\{x_i:i\in I\}$. Therefore its
$2^d-1$ nonempty-index unions are distinct. The sets $A_i$ may overlap
outside $X$; pairwise disjointness is not used.

If a family shatters a $d$-element set $X$, choosing a member with trace
$\{x_i\}$ for each $i$ gives just such a private-element system.
Shattering is inherited by subsets, so absence of an independent system
of size $d$ rules out all shattered sets of size at least $d$. The
auxiliary $d=0$ statements cause no difficulty: there are no nonempty
index unions to distinguish and an empty system is available. The
random-coloring theorem itself only uses $d\ge1$.

For fixed $d\ge1$, let every subset of $[n]$ receive an independent fair
bit. A fixed independent tuple is bad exactly when its
$N=2^d-1$ distinct nonempty unions all get one bit. As $N\ge1$, the
two possible constant assignments are disjoint, and

$$
\Pr(\text{this tuple is bad})=2\cdot2^{-N}=2^{2-2^d}.
$$

This is where the missing empty union matters: using $2^d$ vertices
would give the wrong constant. There are at most $2^{nd}$ ordered
tuples. Non-independent tuples contribute no bad event. A union bound,
which needs no independence between different tuples, therefore gives

$$
\Pr(\text{some bad tuple})\le2^{nd+2-2^d}<1.
$$

The strict hypothesis yields a coloring with no bad tuple. Fix that
single coloring. In any monochromatic union-closed family, binary
closure implies closure under each nonempty finite union by induction
on the number of sets being joined. An independent $d$-tuple in that
family would consequently be bad. Hence every nonempty such family
has VC dimension at most $d-1$, and Sauer--Shelah with $q=d-1\ge0$
bounds its cardinality by $\sum_{j<d}\binom nj$.

An empty family has cardinality zero and can be disposed of directly.
The printed definition of VC dimension as a largest shattered size
does not specify a value for the empty family; this proof does not need
one. For nonempty families the empty test set is shattered, so the
definition has a finite maximum. The minimax maximum is always attained
by a nonempty family. This explicit treatment avoids turning an
unstated convention into a premise.

The resulting bound is on every actual monochromatic union-closed
family of the selected coloring, so taking its maximum and then the
minimum over colorings gives exactly the asserted bound on $F$.
If $d>n$, no independent $d$-system exists and the binomial sum is $2^n$,
so this case is also valid directly. For positive $n$, the hypotheses
cannot hold at $d=1$ or $d=2$; the theorem does not silently use either
case. At $n=1$, they first hold at $d=3$, again with the trivial full
binomial sum. The auxiliary cases therefore create no unsupported
all-positive-$n$ assertion.

For the explicit choice, let $a=\lfloor\log_2 n\rfloor\ge1$ and
$b=\lfloor\log_2 a\rfloor\ge0$. Integrality strengthens the strict
power inequalities to
$2^{a+1}\ge n+1$ and $2^{b+1}\ge a+1$.
The inequality $2^{a-1}\ge a$ gives $b+1\le a$. For $d=a+b+3$,

$$
\begin{aligned}
2^d&=2\cdot2^{a+1}\cdot2^{b+1}
       \ge2(n+1)(a+1),\\
nd+2&=n(a+1)+n(b+2)+2
       \le2n(a+1)+2.
\end{aligned}
$$

The former lower bound exceeds the latter upper bound by $2a>0$.
This checks the strict hypothesis at every floor transition, not just
asymptotically. In particular, $n=2,3$ give $d=4$; at $n=3$ the
comparison still has positive margin $16-14=2$.

For $j\ge0$, $\binom nj\le n^j$, including $j=0$ and the zero terms
$j>n$. Thus $\sum_{j<d}\binom nj\le d n^{d-1}$. If
$\lambda=\log_2 n\ge1$ and $D=\lambda+\log_2\lambda+3$, then
$d\le D$; positivity and $n\ge2$ give
$d n^{d-1}\le D n^{D-1}$. Both factors are compared in the required
direction. No estimate involving $\log_2\log_2 n$ is applied at $n=1$.

## Conclusion-specific attacks, composition and verdicts

The checklist sections below apply to each conclusion in this section.
Each conclusion has its own restatement above, its consumed interfaces and
weakest-step reference here, and its own verdict. No favorable verdict is
inferred merely from another conclusion's name or from an author's output.

### Theorem 1.1: polynomial bound

**Strongest attack.** Good shapes could depend on the frozen coordinates in
incompatible ways, and even a large number of same-colored cubes could
overlap almost completely. These are two successive ways that a count of
local witnesses might fail to give a large actual family. Derivation 2
reconstructs the incidence count over all $(\sigma,\beta,(j,A))$ and the
injective map $(j,A)\mapsto H(j,A)$. It thereby defeats both objections:
the former selects one common pair, while the latter still distinguishes
all selected bases even when many cubes share their top.

As an additional adversarial coloring, take $\chi(A)=|A|\pmod k$.
A cube is monochromatic exactly when every generator size is divisible
by $k$. Thus a lower bound that silently treated arbitrary shapes as
good would fail. The actual argument needs only one good extension per
slice. Its free generator coordinates can all be $k$, since $k\le M$,
so this coloring supplies no obstruction. The proof's averaging over
shapes makes no prohibited uniform-goodness assertion.

The universal $k,n$ quantifiers also survive the extreme case
$k\ge2^n$, where an injective coloring gives $F_k(n)=1$.
Here $M\ge k^2\ge4^n>n$, so the source's small-$n$ branch gives
$c_{k,t}n^{t+1}<1$. It does not demand an impossible large family.

**Premises and composition.** Derivations 1 and 2 verify all internal
cube, permutation, box, supersaturation, slice, averaging, gluing and
constant interfaces. Only the stated elementary finite and inequality
principles are used; Sauer--Shelah is not a premise for this conclusion.
The small-$n$ and large-$n$ branches partition all positive integers.

**Verdict: refutation-failed.** The exact polynomial bound, including its
constant and every integer $k\ge2$, $t\ge1$, $n\ge1$, survives.

### Theorem 1.1: two-color threshold

**Strongest attack.** Recomputing $c_{2,t}$ could expose a lost factor of
$M$, or a failure of the logarithmic bound at small $t$, leaving
$c_{2,t}n<1$ at the advertised threshold. Derivation 2 recomputes both
$M$ factors and the full logarithm, and proves the needed comparison
for every $t\ge1$. The displayed positive polynomial difference checks
the potentially weak estimate without relying on a finite sample.
The endpoint $t=1$ is explicitly covered, and threshold equality still
gives $c_{2,t}n\ge1$.

**Premises and composition.** This conclusion consumes the polynomial
bound already examined in this report, at $k=2$, and the final constant
calculation of Derivation 2. There is no new external theorem premise.

**Verdict: refutation-failed.** The stated non-strict threshold implies
$F(n)\ge n^t$ with the claimed quantifiers.

### Theorem 1.2: binomial bound

**Strongest attack.** A union-closed family can omit the empty set, and
sets obtained from shattering can share a large common part. These facts
could invalidate a random-coloring argument written for disjoint
generators or a full $2^d$-vertex cube. The following exact test exposes
both distinctions. On $[d]\cup\{p\}$, consider

$$
\mathcal H=\{\{p\}\cup I:I\subseteq[d]\},
\qquad A_i=\{p,i\}.
$$

This is a union-closed family omitting $\varnothing$, it shatters $[d]$,
and its chosen generators all overlap at $p$. Nonetheless $i$ is private
to $A_i$, and their nonempty unions are exactly the $2^d-1$ sets
$\{p\}\cup I$ with $I\ne\varnothing$. The source's probability
$2^{2-2^d}$ is the correct one for these sets. Its argument does not
use either the empty union or disjointness of the $A_i$.

Derivation 3 also checks the dependence between overlapping bad events.
It uses only a union bound, so that dependence cannot invalidate the
estimate. The strict exponent $nd+2-2^d<0$ gives positive probability
of no bad event. The proof does not infer this from a non-strict
probability bound of one.

**Premises and composition.** The private-element and shattering
implications, nonempty finite-union closure, tuple count, probability
and minimax transfer are verified in Derivation 3. Sauer--Shelah is
used exactly once, with $q=d-1$, as the explicit classical external
premise; its original proof is not examined. The empty-family case
and $d>n$ are handled there directly.

**Verdict: refutation-failed**, relying on the stated Sauer--Shelah
premise. Every allowed $n,d$ in the conditional binomial assertion is
covered.

### Theorem 1.2: explicit choice

**Strongest attack.** Taking $n$ just below a power of two, and $a$ just
below a power of two, can minimize the slack in the floor estimates.
At the smallest allowed $a=1$, logarithms and the inequality
$b+1\le a$ are especially vulnerable. Derivation 3 uses the integer
inequalities $2^{a+1}\ge n+1$, $2^{b+1}\ge a+1$ and retains the
strict positive margin $2a$. The case $n=3$ realizes the small
comparison $16>14$, so the margin is not manufactured by treating
a strict inequality as equality. The argument applies throughout
every interval of constant $a,b$ and through each jump.

**Premises and composition.** This consumes the examined binomial bound,
the floor estimates and the two elementary monotone comparisons at
the end of Derivation 3. The binomial convention beyond $n$ is
retained. The asserted domain begins at $n=2$, exactly where the
nested logarithm is defined.

**Verdict: refutation-failed**, with the same Sauer--Shelah premise.
Both the specified integer $d$ and the two displayed upper estimates
survive for every $n\ge2$.

### Corollary 1.3(i)

**Strongest attack and deduction.** Rounding the real exponent down can
lose nearly one, and the formula is negative for small $n$. Write
$x=\ell-2\log_2(\ell+2)$, so $\omega=x-1$.
If $\omega\le0$, then $n^\omega\le1\le F(n)$.
Otherwise $x>1$ and $t=\lfloor x\rfloor$ satisfies
$t\ge1$ and $\omega=x-1<t\le x\le\ell$. In particular,

$$
t+2\log_2(t+2)
\le x+2\log_2(\ell+2)=\ell.
$$

Exponentiation gives $(t+2)^2 2^t\le2^\ell=\log_2 n$.
The examined two-color threshold yields
$F(n)\ge n^t\ge n^\omega$. This works when $x$ is an integer and
when its fractional part is arbitrarily close to one; the supplied
$-1$ is enough in both cases. At $n=2$, $\ell=0$ and
$\omega=-3$, so the small case uses the first branch.
Finally $\log_2(\ell+2)=o(\ell)$ as $\ell\to\infty$, giving
$\omega\to\infty$.

**Premises and composition.** This consumes the examined two-color
threshold and elementary logarithmic limits, with no Sauer--Shelah
premise. To express the lower growth question on all positive integers,
one can define the exponent at $n=1$ to be zero; $1^0=1\le F(1)$.
The displayed formula itself is asserted only for $n\ge2$.

**Verdict: refutation-failed.** The explicit exponent, its complete
stated domain and its divergent limit survive.

### Corollary 1.3(ii)

**Strongest attack and deduction.** The natural choice
$F(n)^{1/n}-1$ would give equality, not the claimed strict inequality.
The source instead sets

$$
\varepsilon(n)=F(n)^{1/n}-1+\frac1n.
$$

Since $F(n)\ge1$ and $n\ge1$,
$1+\varepsilon(n)=F(n)^{1/n}+1/n>F(n)^{1/n}>0$.
Raising to the positive integer power $n$ gives the strict bound
for every positive $n$, independent of any asymptotic estimate.
In particular $F(1)=1$: color the two subsets differently for the
upper bound, and use a singleton for the lower bound.
Thus $\varepsilon(1)=1$ gives $1<2$.

For the limit, the examined explicit upper bound with
$\lambda=\log_2 n$ and $D=\lambda+\log_2\lambda+3$ gives

$$
0\le\log_2 F(n)
\le\lambda^2+\lambda\log_2\lambda+2\lambda+\log_2 D
=O(\lambda^2).
$$

Since $\lambda^2/2^\lambda\to0$ and $n=2^\lambda$, it follows that
$\log F(n)/n\to0$, whence $F(n)^{1/n}\to1$ and
$\varepsilon(n)\to0$. Only the eventual estimate is used for the
limit; it is not extended to undefined logarithms at $n=1$.

**Premises and composition.** This consumes the examined explicit upper
bound, hence Sauer--Shelah through Derivation 3, as well as the
finite extremum and positivity of $F$ and elementary exponential
continuity. The function is allowed to be defined in terms of $F$;
the assertion is existential, not an algorithm to evaluate $F$.

**Verdict: refutation-failed**, with the stated external premise for
the limiting upper estimate. The strict inequality itself is
verified at every positive integer.

### Corollary 1.3(iii)

**Strongest attack and deduction.** Merely knowing
$\log F=O((\log n)^2)$ would not establish the leading coefficient
$1$ in this exponent comparison. It could only give an unspecified
constant. The source uses the explicit bound instead. For $n\ge2$,
logarithms in base $2$ and division by $\lambda=\log_2 n>0$ give

$$
\begin{aligned}
\omega(n)
&\le D-1+\frac{\log_2 D}{\lambda}\\
&=\lambda+\log_2\lambda+2+\frac{\log_2 D}{\lambda}.
\end{aligned}
$$

After division of the excess by $\lambda$, the terms
$\log_2\lambda/\lambda$, $2/\lambda$ and
$\log_2 D/\lambda^2$ all tend to zero. Thus for each
$\varepsilon>0$ their sum is at most $\varepsilon$ eventually,
which gives the precise claimed coefficient. This is a comparison
in the exponent's own units. It holds for any qualifying real
function $\omega$, including one that is negative or irregular.
The resulting threshold can even be chosen independently of that
function; only $\varepsilon$ enters the error estimate.

**Premises and composition.** The premise $n^{\omega(n)}\le F(n)$ is
the explicit hypothesis of this conditional assertion, not a
conclusion assumed without proof. The other inputs are the
examined explicit upper bound, hence Sauer--Shelah, and elementary
logarithmic limits. The value at $n=1$ is irrelevant to the
eventual conclusion.

**Verdict: refutation-failed**, with the stated external premise.
The coefficient, quantifier over $\omega$, and quantifier over
every $\varepsilon>0$ survive.

### Corollary 1.3(iv)

**Strongest attack and deduction.** The thresholds from the lower
theorem depend very strongly on both $k$ and $t$. An interchange
of these quantifiers with $n\to\infty$ could be false. Indeed,
allowing $k(n)\ge2^n$ permits injective colorings with $F_{k(n)}(n)=1$.
That example refutes an unasserted varying-color version, not the
fixed-color conclusion under examination.

Fix $k$. For any integer $t\ge1$, the polynomial theorem gives
$F_k(n)\ge c_{k,t}n^{t+1}\ge n^t$ once $n\ge c_{k,t}^{-1}$.
For each positive integer $n$, define

$$
\omega_k(n)=\max\{t\in\{0,1,\ldots,n\}:n^t\le F_k(n)\}.
$$

This is exactly the source's largest qualifying integer $t\le n$:
$t=0$ qualifies, so no negative integer could alter that maximum.
The set is nonempty and finite. For every fixed integer $t\ge1$,
all integers $n\ge\lceil\max(t,c_{k,t}^{-1})\rceil$ have
$\omega_k(n)\ge t$. Given any real target, choose a larger such
integer $t$; this proves $\omega_k(n)\to\infty$ with the correct
order of quantifiers. The lower inequality holds by the definition
of the maximum at every positive $n$. At $n=1$ it has
$\omega_k(1)=1$ and $1^{\omega_k(1)}=1\le F_k(1)=1$.

Set $\varepsilon_k=\varepsilon$ from (ii). Since unused colors
are allowed, the already checked comparison $F_k(n)\le F(n)$
preserves the strict upper bound for every $n$, and
$\varepsilon_k(n)\to0$. No change of coloring convention is used.

**Premises and composition.** The lower half consumes the examined
fixed-$k$ polynomial bound and a finite maximum. The upper half
consumes (ii) and the model comparison, hence Sauer--Shelah.
The same upper function can serve every $k\ge2$; no analogous
uniformity is claimed for the lower growth threshold.

**Verdict: refutation-failed**, with the stated external premise
for the upper half. Both all-positive-$n$ inequalities and both
limits survive for each fixed $k\ge2$.

### Elementary limits and static examples

The logarithmic limits above require no experimental extrapolation.
For example, on $\lambda\in[m,m+1]$,
$\lambda^2/2^\lambda\le(m+1)^2/2^m$, and the latter sequence has
successive ratio tending to $1/2$, so it decays geometrically after
some point. Applying the same elementary comparison after writing
a positive variable as $2^u$ gives $\log x/x\to0$.
These limits imply all the stated $o(\ell)$ and normalized error
estimates. The only additional limit operation is continuity of
the exponential at zero.

The four supplied figures were checked as static mathematical text.
The hole-cube labels add exactly the coordinate's generator along
each indicated edge. In the block-chain example, the top at level
$8$ has size $31$, the base for $A=\{2,4\}$ has size $26$, and
the generators have sizes $2$ and $3$; the displayed member omits
block $4$ and retains block $2$. The union example has omissions
$\{2,4\}$ and $\{3,4\}$, whose common omission is $\{4\}$.
The box example has corners $(1,1,2)$ and $(3,3,0)$, lower corner
$(1,1,0)$, upper corner $(3,3,2)$, and shape $(r+2;2,2,2)$.
These checks validate the examples' stated identities; no rendering
or TeX execution is claimed or needed by the proofs.

## Checklist verdicts

Every row below is a checklist verdict for each of the eight conclusion
sections individually. The references specify the relevant argument for that
conclusion; inapplicability is stated explicitly. The conclusion-specific
sections above supply the associated strongest attack, composition and
premises. This shared presentation does not leave any conclusion exempt from
an item.

### Canonical failure modes

| Failure mode | Verdict for the assigned conclusions |
| --- | --- |
| “Almost all” quietly upgraded to “all” | No failure found. The polynomial theorem partitions every positive $n$ into two regimes; the conditional upper theorem covers every $n,d$ satisfying its strict hypothesis. Corollary (i) begins at $n=2$, (ii) and (iv) establish their inequalities for every positive $n$, and (iii) is explicitly eventual. |
| Induction that presupposes termination | No failure found. Box induction decreases the nonnegative integer dimension. Closure under nonempty finite unions is induction on their finite length. Neither requires an unproved termination assertion. |
| Probabilistic or averaging heuristics presented as proofs | No failure found. Grid probabilities and incidence counts are finite identities or inequalities. The upper coloring has positive probability because its bad-event bound is strictly below one. Independence is used for coordinate sampling and colors of distinct sets, never incorrectly for overlapping cube or tuple events. |
| Circular use of an equivalent statement | No failure found. The acyclic premise order below contains no use of a target bound to prove an internal step. Defining the existential functions in (ii) and (iv) from the already defined finite extrema is legitimate; their limiting properties are separately proved. |
| Exceptional sets dropped from density arguments | No failure found. Degenerate boxes cost at most $t/(L+1)$ and are explicitly removed. The small-$n$ lower regime, negative exponents, empty families, and logarithmic domain restrictions are handled. |
| Finite verification cited beyond base-case coverage | No failure found. No finite experiment is a premise. All parameter estimates are analytic and universal over their stated integer ranges. Numerical examples and static figure checks are illustrations only. |
| Convergence of a relaxed or averaged system standing in for actual objects | No failure found. The finite incidence average selects one actual $(\sigma,\beta)$; gluing produces an actual union-closed family with injectively counted bases. The upper union bound selects one actual coloring. No asymptotic relaxation is substituted for either object. |

### Named patterns

| Named pattern | Verdict for the assigned conclusions |
| --- | --- |
| Model-class transport instead of entailment | No failure found in model transfer: private elements do not require disjoint sets, the upper proof uses nonempty unions, and the lower construction proves closure in the specified family model. Classification of axiom-system extensions and a claim of novelty of such an extension are inapplicable: neither is asserted. |
| Uniformity over an infinite family asserted from finitely many instances | No failure found. $c_{k,t}$ is explicit and independent of $n,\chi$ but depends on $k,t$. The threshold estimates hold for every integer $t\ge1$. Corollary (iv) fixes $k$ before taking the limit. No finite sample establishes these claims. |
| Extremal claims audited in their own units | No failure found. The extrema exist over finite colorings and families. The lower count is transferred to distinct members, the upper estimate bounds every member-family's cardinality in one coloring, and (iii) divides by $\log_2 n$ to compare the actual exponent. No unproved sharpness or optimality claim is made. |
| Consequence sentences are claim surfaces | No failure found. The threshold, explicit $d$, both displayed upper estimates, all four corollary clauses, the model comparison, the constants' examples and the static figure identities are each checked above. The growth formulation at $n=1$ is explicitly extended only where needed. |
| Carry hypotheses actually used by a quantified argument | No failure found. Disjoint nonempty blocks, positive generator lengths, $A\subseteq[s]<j$, the room condition $r+tL\le n$, fixed $k$, and the strict condition $2^d>nd+2$ are all available at their uses. Nonempty probability spaces and the direct disposal of empty families are explicit. |
| A composition inherits its unproved premises | No hidden premise found. Every consumed internal lemma is examined. The exact Sauer--Shelah premise remains explicit in the binomial upper bound and its descendants; its original proof is not silently claimed as verified. The lower chain has no reliance on it. |
| Reproducibility notes are claims | No computational rerun claim is made. The retained reading route resolves to the exact supplied texts and the full derivations and witnesses are in this report. Byte-preservation checks establish identity only, not mathematical validity. |
| Verifier quotations are claims | Inapplicable to the frozen subject: prior verifier rulings and standing prose were excluded and none was read or characterized. This report makes no claim about an absent grade. |
| Verdict words spelled in full | Satisfied throughout: each mathematical verdict is written as refutation-failed. No ambiguous shortened verdict is used. This spelling check is separate from the mathematical support given above. |
| Certified-bracket functions fail loudly | Inapplicable. There is no numerical enclosure routine, iterative numerical cap, periodic-window calculation or floating-point certificate. Algebraic and logarithmic comparisons are proved directly. |
| A harness leg with no failing input is decoration | Inapplicable. No computational mathematical harness or alleged checker leg is used. The report's analytic attacks retain exact obstruction candidates, including modular coloring and the shared-core family, rather than treating mechanical file checks as mathematical evidence. |
| A gate that reads caches instead of rerunning is defective | Inapplicable. No verdict relies on a repository gate, cached success, saved numerical output or an author's checker. No such success is asserted. |

### Erdős-specific checklist

| Item | Verdict for the assigned conclusions |
| --- | --- |
| Quantifiers and scope | Checked without a failure. The restatements and individual verdicts preserve all integer domains, fixed-parameter limits, strict and non-strict inequalities, negative exponents, and eventual versus all-positive-$n$ assertions. The excluded $f$ model is not inferred from $F$. |
| Circularity | No failure found. Internal dimensions and finite-union length decrease in their inductions. The premise graph below is acyclic. Corollary (iii)'s lower bound is an explicitly assumed antecedent. |
| Model and convention changes | No failure found. The supplied all-subsets coloring model, unused colors, arbitrary base, nonempty generators, binary union closure and absence of an empty-member or intersection requirement remain intact. Probability averages are transferred by proved finite steps. |
| Finite and statistical overreach | No failure found. There is no empirical inference or correlated-sample estimate. Finite probability is exact, and the universal and limiting conclusions have direct deductions. |
| Uniformity | No failure found. Parameter dependence is retained in the constants and thresholds. Finite sum exchanges need no limiting interchange. The only asymptotics use elementary logarithmic limits with fixed $k$ where required. |
| Extremal conclusions | Checked in their own coordinates without a failure. The cardinality extrema are attained and bounded; base injection and the all-families upper estimate justify the minimax bounds. The exponent comparison retains leading coefficient one. No sharpness assertion is added. |
| Consequences and composition | No failure found. All assigned clauses and the auxiliary consequences used by them have separate deductions above. Sauer--Shelah is the only named external theorem premise and is used at its stated strength. |
| Computation | Numerical-certification requirements are inapplicable because this is an analytic examination. Exact algebra, integer floors and inequalities are displayed. No finite search, floating-point bound, executable check or cap artifact is a premise. |
| Reproduction | The exact subject texts and independent derivations are retained together. The analytic reproduction route below needs no numerical output or machine-local source. Computational reproduction requirements are inapplicable; no unrun command is presented as a mathematical check. |
| Source and verdict fidelity | The exact arXiv v1 packet and its source credits are preserved. Text-only scope, excluded versions, the original Sauer/Shelah reading limit, and ungraded reviewer verdicts are explicit. PDF fidelity, original-source acceptance and formalization are not asserted. |

The neighboring statistical-correlation discipline is inapplicable because no
statistical sample is used. The proof/evidence-coverage discipline is met by the
complete internal coverage and the explicit external-premise boundary; the
elementary examples have no claimed universal evidentiary force.

## Premises, reading depth and verification order

No native L-claim or ledger row is consumed by the frozen statement or proof.
This was checked against the actual mathematical files on 2026-10-15, including
the consequence sentences. No live ledger was read, and no native standing or
pending grade is used as a premise. Source result labels are not native claim
identities.

### Exact Sauer--Shelah interface

The external theorem used is:

> For a family $\mathcal A$ of subsets of an $n$-element set, if its VC
> dimension is at most an integer $q\ge0$, then
> $|\mathcal A|\le\sum_{j=0}^q\binom nj$, with $\binom nj=0$ for $j>n$.

Here shattering means realizing every intersection trace on the test set.
This is the finite cardinality form explicitly supplied in
provenance_and_scope.md.txt and upper_proof.tex.txt, Lemma 5.1(c).
The consuming specialization is $\mathcal A=\mathcal F$, a nonempty
monochromatic union-closed family in the selected no-bad-tuple coloring,
and $q=d-1\ge0$. Derivation 3 proves $\operatorname{vc}(\mathcal F)\le q$
from absence of an independent system. No closure hypothesis is required
by Sauer--Shelah itself; union closure is used in the preceding step.
For an empty family the cardinality bound is immediate without this
interface.

The basis for reliance is the expressly commissioned classical
Sauer--Shelah premise in this exact finite form. Actual reading depth is
**the supplied claim checked and its application verified**. The original
Sauer and Shelah papers are **unread**, and their proofs are **not
independently verified here**. Their bibliographic citations, read from the
supplied reference excerpt, are:

- N. Sauer, *On the density of families of sets*, Journal of Combinatorial
  Theory, Series A **13** (1972), no. 1, 145--147.
  [DOI supplied by the source](https://doi.org/10.1016/0097-3165(72)90019-2).
- S. Shelah, *A combinatorial problem; stability and order for models and
  theories in infinitary languages*, Pacific Journal of Mathematics **41**
  (1972), no. 1, 247--261.
  [DOI supplied by the source](https://doi.org/10.2140/pjm.1972.41.247).

No stronger variant, structural characterization, or assertion about
intersection-closed families is taken from those references. If this
external theorem is not granted, this report alone does not supply the
binomial upper bound or the consequences that consume it. The lower
polynomial bound, its threshold, Corollary (i), and the lower half of
Corollary (iv) are independent of that external theorem.

### Other inputs and credits

The internal box inequality is proved in the supplied text and independently
rederived in Derivation 1. The source credits the method to W. T. Gowers,
*A new proof of Szemerédi's theorem*, Geometric and Functional Analysis
**11** (2001), no. 3, 465--588,
[DOI supplied by the source](https://doi.org/10.1007/s00039-001-0332-9).
That paper is unread here. Its attribution is preserved, but no theorem
from it is an external premise.

The other foundational inputs are elementary finite counting and
pigeonholing, finite product probability and the union bound,
Cauchy--Schwarz and Jensen for nonnegative real quantities, and elementary
logarithmic/exponential properties. Their exact roles are displayed:
Cauchy--Schwarz and Jensen in the box and color-density bounds; counting
and averaging in slices and gluing; product probability and the union
bound in the bad-tuple construction; logarithms and limits in the
threshold and corollary deductions. No claim of a new proof of these
elementary principles is made.

The arXiv subject's supplied internal proofs have **proof verified**
coverage for the assigned $F/F_k$ scope, relative to those elementary
principles and the explicit Sauer--Shelah premise where used. This
reading-depth statement covers the retained sections and deductions
enumerated here, not the full paper, its original PDF, its other
versions, or the excluded sublattice claims.

The analytic verification order is acyclic:

1. Cube definitions and permutation invariance establish the shape
   probability; the independently checked box inequality gives the
   grid estimate.
2. The grid estimate and permutation averaging give supersaturation.
   Supersaturation gives slices, and slices give a common arrangement
   by incidence counting.
3. The union rule, color pigeonholing and injective bases give gluing.
   It composes with that arrangement and the constant estimates to
   prove the polynomial bound, then the two-color threshold.
4. The threshold gives Corollary (i). The polynomial bound gives the
   lower half of Corollary (iv).
5. Private-element unions and the random-coloring argument give a
   coloring with no independent system inside any monochromatic
   union-closed family. Shattering and the external Sauer--Shelah
   interface give the binomial upper bound, then its explicit version.
6. The explicit upper version gives (ii) and (iii); (ii) and
   $F_k\le F$ give the upper half of (iv).

These are mathematical consumption relations within this examination,
not promotions or assertions of native standing.

## Reproduction, limitations and grading

The independent reasoning is retained in this report, especially the three
derivations and the conclusion-specific attacks. All necessary finite
examples and parameters are written explicitly. The exact fourteen supplied
mathematical payloads and their neutral manifest are retained under
subject/ beside the report. They are sufficient to reconstruct what was
examined without a private archive or changing canonical page.

The reproduction route is analytic:

1. Read the retained model and statements, then the cube/gluing and
   box/supersaturation files against Derivation 1.
2. Reproduce the free-coordinate extension, incidence count, base
   injection and constant arithmetic in Derivation 2 against the
   retained lower proof.
3. Count the nonempty unions and bad events, verify the VC interface
   under the explicitly supplied Sauer--Shelah premise, and reproduce
   the strict floor estimates in Derivation 3 against the upper proof.
4. Check the eight separate attack/verdict sections, all four retained
   corollary deductions, and the explicit small cases and figure
   identities.

No mathematical computation was run or used. Accordingly there is no
numerical checker, numerical output, executable rerun command, or
computational failing-input obligation. The structurally disjoint
computational-batch rule is inapplicable. This is a first independent
examination, not a second-cycle countersign; no prior-cycle attacks were
supplied. The alternative box induction and the explicit obstruction
candidates are preserved mathematical work, not agreement with cached
author results.

All assigned conclusions have the verdict **refutation-failed**, at the
exact scopes stated individually above. No counterexample or unsupported
essential internal deduction was found. The two auxiliary domain issues
identified in the examination are fully localized: the probability
application has a nonempty grid, and empty families are bounded directly.
Neither requires a changed theorem, a changed constant, or an additional
theorem premise. No correction to the frozen source was made or treated
as part of the subject.

There is no unfinished internal proof obligation within the assigned
$F/F_k$ scope. The limits of the verdict are the explicitly assumed
Sauer--Shelah theorem, the exact frozen version and scope, and text-only
inspection. Original Sauer/Shelah proofs, original-PDF fidelity, other
source versions, the $f$ claims, formalization and public acceptance
remain outside the examination. A change to the subject would require
its own assessment.

These are the reviewer's mathematical verdicts. A distinct fresh grader
must assess this unchanged report's contract and independence. This
report gives no grade, native tier, source-acceptance determination, or
problem-status assertion.
