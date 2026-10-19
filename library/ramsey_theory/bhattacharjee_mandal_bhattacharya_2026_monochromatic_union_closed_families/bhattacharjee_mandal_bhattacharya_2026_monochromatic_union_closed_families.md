# Resolving Erdős–Ulam Monochromatic Union-Closed Family Conjectures

Deep Bhattacharjee<sup>†</sup>, Priyabrata Mandal and Ushashi Bhattacharya

## Abstract.

We prove both Erdős–Ulam conjectures on monochromatic union-closed families. Every two-colouring of the subsets of a finite set contains a monochromatic union-closed family whose size grows faster than any fixed power of the size of the set, while suitable colourings admit no monochromatic union-closed family of exponential size. Both results hold for any number of colours and are verified in Lean.

*Key words and phrases:* union-closed families, Ramsey theory, Hilbert cubes, box norm, van der Waerden’s theorem, Sauer–Shelah lemma, Lean

*2020 Mathematics Subject Classification* Primary 11B75, 05D10; Secondary 05D05, 11B25, 68V20

## 1. Introduction

Write $[n]=\{1,\dots,n\}$ and $2^{[n]}$ for the family of all subsets of $[n]$. For an integer $k\geq 2$, a *$k$-colouring* of $2^{[n]}$ is a map $\chi:2^{[n]}\to[k]$, and a family $\mathcal{F}\subseteq 2^{[n]}$ is *monochromatic* if $\chi$ is constant on $\mathcal{F}$. The family $\mathcal{F}$ is *union-closed* if $A\cup B\in\mathcal{F}$ whenever $A,B\in\mathcal{F}$, and it is a *sublattice* if it is closed under both union and intersection. Erdős and Ulam asked how large a monochromatic family of either kind a colouring is forced to contain. Accordingly let

$$\begin{aligned}f(n)&=\min_{\chi}\,\max\bigl\{|\mathcal{L}|:\ \mathcal{L}\subseteq 2^{[n]}\text{ is a monochromatic sublattice}\bigr\},\\ F_{k}(n)&=\min_{\chi}\,\max\bigl\{|\mathcal{F}|:\ \mathcal{F}\subseteq 2^{[n]}\text{ is a monochromatic union-closed family}\bigr\},\end{aligned}$$

where the first minimum is over all $2$-colourings and the second over all $k$-colourings of $2^{[n]}$, and write $F=F_{2}$. A single set is a sublattice and every sublattice is union-closed, so $1\leq f(n)\leq F(n)$. A maximal chain $\emptyset\subset\{1\}\subset\{1,2\}\subset\dots\subset[n]$ has $n+1$ members, at least $\lceil(n+1)/2\rceil$ of them receive the same colour under a $2$-colouring, and every subchain is a sublattice. Hence

$$F(n)\ \geq\ f(n)\ \geq\ \Bigl\lceil\frac{n+1}{2}\Bigr\rceil. \tag{1.1}$$

A $2$-colouring is also a $k$-colouring, so $F_{k}(n)\leq F(n)$ for every $k\geq 2$. Figure 1 shows the smallest interesting case.

**Figure 1.** A $2$-colouring of the subsets of $\{1,2,3\}$, drawn on the cube $2^{[3]}$. The five red sets (discs) form a union-closed family which is not a sublattice, since $\{1\}\cap\{2\}=\emptyset$ is blue. The three blue sets (squares) form a chain.

The question is Problem 1183 in Bloom’s collection of Erdős problems [Bl26], where it is listed as open. As recorded there, Erdős had no plausible conjecture for the true order of magnitude of $F(n)$, but asked whether

$$F(n)\ \geq\ n^{\omega(n)}\ \text{ for some }\omega(n)\to\infty,\qquad\text{and}\qquad F(n)\ <\ (1+o(1))^{n}. \tag{1.2}$$

Erdős also noted that Howorka had proved the first statement for colourings in which the colour of a set depends only on its size.[^1] We prove both statements in (1.2) for arbitrary colourings, and for any number of colours.

### 1.1. Results

The main result is a polynomial lower bound of every degree, with an explicit constant.

**Theorem 1.1.** Let $k\geq 2$ and $t\geq 1$ be integers, put $M=t^{2}k^{2^{t}}$ and

$$c_{k,t}=\Bigl(k^{2^{t}+1}\,t^{t}\,(4M^{2})^{t+1}\Bigr)^{-1}.$$

Every $k$-colouring of $2^{[n]}$ contains a monochromatic union-closed family with at least $c_{k,t}\,n^{t+1}$ members; that is, $F_{k}(n)\geq c_{k,t}\,n^{t+1}$ for all $n\geq 1$. For two colours, $F(n)\geq n^{t}$ whenever $\log_{2}n\geq(t+2)^{2}\,2^{t}$.

The upper bound comes from a random colouring and the Sauer–Shelah lemma.

**Theorem 1.2.** Let $d\geq 1$ be an integer with $2^{d}>nd+2$. Then

$$F(n)\ \leq\ \sum_{j=0}^{d-1}\binom{n}{j}.$$

In particular, for $n\geq 2$ and $d=\lfloor\log_{2}n\rfloor+\lfloor\log_{2}\lfloor\log_{2}n\rfloor\rfloor+3$,

$$F(n)\ \leq\ d\,n^{d-1}\ \leq\ \bigl(\log_{2}n+\log_{2}\log_{2}n+3\bigr)\,n^{\log_{2}n+\log_{2}\log_{2}n+2}.$$

Together the two theorems settle both parts of (1.2), and they locate the exponent: the largest $\omega(n)$ with $F(n)\geq n^{\omega(n)}$ lies between $(1-o(1))\log_{2}\log_{2}n$ and $(1+o(1))\log_{2}n$.

**Corollary 1.3 (The Erdős–Ulam conjectures).** Both statements in (1.2) hold, in the following form.

1.  For every $n\geq 2$ we have $F(n)\geq n^{\omega(n)}$, where

    $$\omega(n)=\ell-2\log_{2}(\ell+2)-1,\qquad\ell=\log_{2}\log_{2}n,$$

    and $\omega(n)\to\infty$.

2.  There is a function $\varepsilon:\mathbb{N}\to\mathbb{R}$ with $\varepsilon(n)\to 0$ such that $F(n)<(1+\varepsilon(n))^{n}$ for every $n\geq 1$.

3.  If $\omega:\mathbb{N}\to\mathbb{R}$ satisfies $F(n)\geq n^{\omega(n)}$ for every $n$, then for every $\varepsilon>0$ we have $\omega(n)\leq(1+\varepsilon)\log_{2}n$ for all large $n$.

4.  For every $k\geq 2$ there are functions $\omega_{k}(n)\to\infty$ and $\varepsilon_{k}(n)\to 0$ such that $n^{\omega_{k}(n)}\leq F_{k}(n)<(1+\varepsilon_{k}(n))^{n}$ for every $n\geq 1$.

Parts (i) and (ii) are the two statements of (1.2), with the term $o(1)$ written out as a function $\varepsilon(n)\to 0$, so Corollary 1.3 answers both questions of Problem 1183 in the affirmative. Since $\log_{2}(\ell+2)=o(\ell)$, the exponent in (i) is $(1-o(1))\log_{2}\log_{2}n$. This is also, to first order, the size of the monochromatic union-closed families that we can exhibit in a uniformly random colouring (Proposition 5.2), so a better lower bound for $F(n)$ would have to say something new about random colourings as well. In the other direction, Proposition 5.4 reduces an upper bound for the random colouring to counting union-closed families.

The two functions of Erdős and Ulam turn out to be of quite different sizes. For sublattices the trivial bound (1.1) is correct up to a factor of order $(\log n)^{2}$.

**Theorem 1.4.** For every $n\geq 1$, with $L=\lfloor\log_{2}n\rfloor+1$,

$$\Bigl\lceil\frac{n+1}{2}\Bigr\rceil\ \leq\ f(n)\ \leq\ \min\bigl\{\,n^{2}+n+1,\ \ nL(3L+2)+2n+3L+3\,\bigr\}.$$

Thus $f(n)\leq(3+o(1))\,n(\log_{2}n)^{2}$, whereas $F(n)/n^{C}\to\infty$ for every constant $C$.

### 1.2. Colourings by cardinality, Hilbert cubes and progressions

Howorka’s case of the problem is arithmetic in nature. Call $\chi$ a *cardinality colouring* if $\chi(S)=g(|S|)$ for some $g:\{0,1,\dots,n\}\to[k]$. The building blocks of our families are the *$t$-cubes* $\{U\cup X_{I}:\ I\subseteq[t]\}$, where $U,X_{1},\dots,X_{t}$ are pairwise disjoint, the $X_{i}$ are nonempty and $X_{I}=\bigcup_{i\in I}X_{i}$. The sizes of the members of such a cube form the *Hilbert cube*

$$H(u;a_{1},\dots,a_{t})=\Bigl\{u+\sum_{i\in I}a_{i}:\ I\subseteq[t]\Bigr\},\qquad u=|U|,\ a_{i}=|X_{i}|,$$

so a cube is monochromatic under a cardinality colouring exactly when $g$ is constant on the corresponding Hilbert cube. Hilbert’s lemma [Hi1892], proved in the course of Hilbert’s work on the irreducibility of polynomials with integer coefficients and usually regarded as the first theorem of Ramsey theory, says that every finite colouring of the positive integers has monochromatic Hilbert cubes of every dimension. Our argument gives it with an explicit window (Corollary 6.1): every $k$-colouring of $\{r,r+1,\dots,r+t^{2}k^{2^{t}}\}$ is constant on a $t$-dimensional Hilbert cube inside this interval. Read through the dictionary between cubes of sets and cubes of integers, the proof of Theorem 1.1 produces many monochromatic Hilbert cubes spread along a single sequence of bounded steps.

**Theorem 1.5.** Let $k\geq 2$ and $t\geq 1$, put $M=t^{2}k^{2^{t}}$, let $n\geq 4M(t+1)$, and put $m=\lfloor(n-1)/M\rfloor$ and $s=\lfloor m/2\rfloor$. For every $g:\{0,1,\dots,n\}\to[k]$ there are integers $\beta_{1},\dots,\beta_{m}\in[M]$ with $\beta_{1}+\dots+\beta_{m}<n$ and a colour $c$ with the following property. For at least

$$\frac{n^{t+1}}{k\,t^{t}\,(4M^{2})^{t+1}}$$

of the pairs $(j,A)$ with $s<j\leq m$, $A\subseteq[s]$ and $|A|=t$, the function $g$ takes the value $c$ at every point of the Hilbert cube

$$H_{\beta}(j,A)=\Bigl\{\beta_{1}+\beta_{2}+\dots+\beta_{j}-\sum_{b\in B}\beta_{b}:\ B\subseteq A\Bigr\}.$$

Different pairs $(j,A)$ may give the same set of integers, and there are at most $(n+1)M^{t}$ Hilbert cubes $H(u;a_{1},\dots,a_{t})$ in $\{0,\dots,n\}$ with all $a_{i}\leq M$. What Theorem 1.5 provides is one sequence $\beta$ for which a fixed proportion of the cubes indexed by the pairs $(j,A)$ have a common colour, all of them hanging from the partial sums $\beta_{1}+\dots+\beta_{j}$. This is the structure that lets the corresponding families of sets be glued into one union-closed family. Section 6 also shows that a monochromatic arithmetic progression of sizes yields a large monochromatic union-closed family and a monochromatic sublattice, and derives Howorka’s theorem from van der Waerden’s theorem with an explicit bound (Theorem 6.4).

### 1.3. The idea of the proof of Theorem 1.1

Chains and cubes are monochromatic union-closed families that are easy to find, but a chain has at most $n+1$ members and a single cube is too rigid to be forced to be large. The families we build are unions of many cubes that fit together. Take pairwise disjoint nonempty blocks $Y_{1},\dots,Y_{m}$, put $C_{j}=Y_{1}\cup\dots\cup Y_{j}$, and for $j>s$ and $A\subseteq[s]$ consider the cube $Q(j,A)=\{C_{j}\setminus Y_{B}:\ B\subseteq A\}$. The union of a member of $Q(j,A)$ and a member of $Q(j^{\prime},A^{\prime})$ with $j\leq j^{\prime}$ is again a member of $Q(j^{\prime},A^{\prime})$, so the union of any collection of cubes $Q(j,A)$ that are monochromatic in a common colour is union-closed. There are about $m^{t+1}$ pairs $(j,A)$ with $|A|=t$, and it is therefore enough to make a fixed proportion of these cubes monochromatic.

For a fixed chain of blocks this cannot be arranged, since the colouring may have been chosen against it. We therefore randomise twice: the ground set is permuted by a uniformly random $\sigma$, and each block size is chosen at random from $\{1,\dots,M\}$. After a random permutation, the probability that a cube is monochromatic depends only on the sizes of its parts (Lemma 2.2). The central step is a supersaturation statement: for every $r$, some shape whose base size lies between $r$ and $r+M$ is monochromatic with probability at least $k^{-2^{t}}$ (Proposition 3.2). It follows from an inequality of Cauchy–Schwarz type for products over the vertices of a box (Lemma 3.1), applied to the sets obtained by running along $t$ disjoint chains of elements (Figure 6). The shape of $Q(j,A)$ is governed by $t+1$ block sizes, those of $Y_{j}$ and of $Y_{a}$ for $a\in A$, and these can be tuned independently of all the others (Lemma 4.1). Averaging over $\sigma$ and the block sizes then produces one chain of blocks in which a proportion $k^{-2^{t}}M^{-t-1}$ of all the cubes is monochromatic (Lemma 4.2). Figure 2 shows how the pieces are assembled.

**Figure 2.** The structure of the proof of Theorem 1.1. Here $\mathcal{P}$ is the set of pairs $(j,A)$ with $s<j\leq m$, $A\subseteq[s]$ and $|A|=t$, and $\rho_{\chi}$ is defined after Lemma 2.2.

### 1.4. Related work

The union-closed families in this paper should not be confused with those of Frankl’s union-closed sets conjecture, which asks whether every union-closed family other than $\{\emptyset\}$ has an element lying in at least half of its members. That problem concerns the internal structure of one family and involves no colouring. Gilmer [Gi22] proved that some element lies in a constant proportion of the members, and Alweiss, Huang and Sellke [AHS24] improved the constant. The entropy method behind these results compares the union of two independent random members of a family with a single random member, and we see no analogue of it here, where the family is not given in advance.

Families of $2^{d}$ sets of the form $\{U\cup X_{I}\}$ are called $d$-dimensional Boolean algebras by Gunderson, Rödl and Sidorenko [GRS99], who studied their extremal theory alongside that of $d$-dimensional affine cubes of integers and complete $d$-partite $d$-uniform hypergraphs. The passage between cubes of sets and Hilbert cubes of integers used in Section 6 is of the same kind. Proposition 3.2 contains the two-letter case of the multidimensional Hales–Jewett theorem [HJ63] with an explicit bound (Remark 3.3); see [GRS90] for this theorem and for the background in Ramsey theory, including van der Waerden’s theorem [vdW27]. The box inequality behind it is the simplest instance of the repeated use of the Cauchy–Schwarz inequality introduced by Gowers [Go01]. The upper bound rests on the Sauer–Shelah lemma [Sa72, Sh72], which is also at the root of the theory of Vapnik–Chervonenkis dimension [VC71].

### 1.5. Formal verification

All theorems, propositions, corollaries and lemmas of Sections 2–7 have been formalised and checked in the Lean proof assistant [MU21] with the Mathlib library [Mat20]. The functions $f$, $F$ and $F_{k}$ are defined in the formal development literally as above, the two conjectures are stated in the form (1.2) with the term $o(1)$ written out as a function tending to zero, and Lean reports that the proof of each formal statement uses only the three standard axioms of the system. Section 8 describes the formalisation.

### 1.6. Organisation

Section 2 introduces cubes and block chains and proves that monochromatic cubes of one chain can be glued. Section 3 proves the box inequality and the supersaturation statement, and Section 4 completes the proof of Theorem 1.1. Section 5 proves Theorem 1.2 and Corollary 1.3 and studies the random colouring. Section 6 treats cardinality colourings, Hilbert cubes and arithmetic progressions, and Section 7 the lattice function $f$. Section 8 describes the formalisation, and Section 9 collects open questions.

## 2. Cubes and block chains

Throughout, $k\geq 2$ and $\chi$ is a $k$-colouring of $2^{[n]}$, and $S_{n}$ is the group of permutations of $[n]$. A permutation acts on sets and on families of sets in the obvious way: $\sigma(S)=\{\sigma(x):x\in S\}$ and $\sigma(\mathcal{F})=\{\sigma(S):S\in\mathcal{F}\}$. For sets $X_{1},X_{2},\dots$ and a finite set $I$ of indices we write $X_{I}=\bigcup_{i\in I}X_{i}$, so that $X_{\emptyset}=\emptyset$.

**Definition 2.1.** Let $t\geq 0$. A *$t$-cube* in $2^{[n]}$ is a family

$$Q(U;X_{1},\dots,X_{t})=\{U\cup X_{I}:\ I\subseteq[t]\},$$

where $U,X_{1},\dots,X_{t}\subseteq[n]$ are pairwise disjoint and $X_{1},\dots,X_{t}$ are nonempty. We call $U$ the *base*, $T=U\cup X_{[t]}$ the *top* and $X_{1},\dots,X_{t}$ the *generators*. The *shape* of the cube is the tuple $(|U|;|X_{1}|,\dots,|X_{t}|)$.

The $2^{t}$ sets $U\cup X_{I}$ are distinct, and

$$(U\cup X_{I})\cup(U\cup X_{J})=U\cup X_{I\cup J},\qquad(U\cup X_{I})\cap(U\cup X_{J})=U\cup X_{I\cap J},$$

so a $t$-cube is a sublattice of $2^{[n]}$ isomorphic to $2^{[t]}$. Writing $U\cup X_{I}=T\setminus X_{[t]\setminus I}$ describes the same cube from the top downwards, as the family $\{T\setminus X_{I}:\ I\subseteq[t]\}$; this is the form in which cubes appear in block chains. Figure 3 shows a $3$-cube in this form.

**Figure 3.** A $3$-cube with top $T$ and generators $X_{1},X_{2},X_{3}$, where $X_{12}=X_{1}\cup X_{2}$ and so on. Moving along an edge in direction $i$ adds or removes $X_{i}$. The vertex $U=T\setminus X_{123}$ is the base.

**Lemma 2.2.** If $Q$ and $Q^{\prime}$ are $t$-cubes in $2^{[n]}$ of the same shape, then

$$\bigl|\{\sigma\in S_{n}:\ \sigma(Q)\text{ is monochromatic}\}\bigr|\\
=\bigl|\{\sigma\in S_{n}:\ \sigma(Q^{\prime})\text{ is monochromatic}\}\bigr|.$$

*Proof.* Let $Q=Q(U;X_{1},\dots,X_{t})$ and $Q^{\prime}=Q(U^{\prime};X^{\prime}_{1},\dots,X^{\prime}_{t})$ with tops $T$ and $T^{\prime}$. The sets $U,X_{1},\dots,X_{t},[n]\setminus T$ partition $[n]$, as do $U^{\prime},X^{\prime}_{1},\dots,X^{\prime}_{t},[n]\setminus T^{\prime}$, and corresponding parts have the same size. So there is $\tau\in S_{n}$ with $\tau(U)=U^{\prime}$ and $\tau(X_{i})=X^{\prime}_{i}$ for every $i$, and then $\tau(Q)=Q^{\prime}$. Now $\sigma(Q^{\prime})=(\sigma\tau)(Q)$, and $\sigma\mapsto\sigma\tau$ is a bijection of $S_{n}$. ∎

For integers $u\geq 0$ and $a_{1},\dots,a_{t}\geq 1$ with $u+a_{1}+\dots+a_{t}\leq n$ we may therefore define

$$\rho_{\chi}(u;a_{1},\dots,a_{t})=\frac{1}{n!}\,\bigl|\{\sigma\in S_{n}:\ \sigma(Q)\text{ is monochromatic}\}\bigr|,$$

where $Q$ is any $t$-cube of shape $(u;a_{1},\dots,a_{t})$. Since $\sigma(Q)$ is a uniformly random cube of that shape when $\sigma$ is uniform, $\rho_{\chi}(u;a)$ is the probability that a random cube of shape $(u;a)$ is monochromatic.

**Definition 2.3.** Let $Y_{1},\dots,Y_{m}\subseteq[n]$ be pairwise disjoint nonempty sets, the *blocks*, and put $C_{j}=Y_{1}\cup\dots\cup Y_{j}$ for $0\leq j\leq m$. For $1\leq j\leq m$ and $A\subseteq[j-1]$ let

$$Q(j,A)=\{C_{j}\setminus Y_{B}:\ B\subseteq A\}.$$

This is the $|A|$-cube with top $C_{j}$, generators $Y_{a}$ $(a\in A)$ and base $C_{j}\setminus Y_{A}$; its shape is $\bigl(\sum_{i\leq j,\,i\notin A}|Y_{i}|;\ (|Y_{a}|)_{a\in A}\bigr)$, the generators being listed in increasing order of $a$.

Figure 4 shows a member of such a cube. The chain structure enters through the following rule, illustrated in Figure 5.

**Figure 4.** A block chain with $m=10$ blocks placed in slots $G_{1},\dots,G_{10}$ of size $M=6$, with $|Y_{k}|=\beta_{k}$ and $\beta=(4,2,5,3,6,2,4,5,3,4)$. Here $s=5$, and the teal blocks form the member $C_{8}\setminus Y_{\{4\}}$ of the cube $Q(8,\{2,4\})$; the hatched block $Y_{4}$ is removed and the grey blocks lie beyond $C_{8}$.

**Lemma 2.4 (Union rule).** Let $1\leq j\leq j^{\prime}\leq m$ and $B,B^{\prime}\subseteq[j]$. Then

$$(C_{j}\setminus Y_{B})\cup(C_{j^{\prime}}\setminus Y_{B^{\prime}})=C_{j^{\prime}}\setminus Y_{B\cap B^{\prime}}.$$

*Proof.* Both sides are contained in $C_{j^{\prime}}$. Let $x\in C_{j^{\prime}}$. If $x\notin Y_{B^{\prime}}$, then $x$ lies in $C_{j^{\prime}}\setminus Y_{B^{\prime}}$ and also outside $Y_{B\cap B^{\prime}}$. Otherwise $x\in Y_{b}$ for some $b\in B^{\prime}$; then $b\leq j$, so $x\in C_{j}$, and $x$ lies in the left side if and only if $b\notin B$, that is, if and only if $x\notin Y_{B\cap B^{\prime}}$. ∎

**Figure 5.** The union rule with $s=5$: $C_{6}\setminus Y_{\{2,4\}}$ and $C_{8}\setminus Y_{\{3,4\}}$ have union $C_{8}\setminus Y_{\{4\}}$. Filled squares are blocks present in the set.

**Proposition 2.5 (Gluing).** Let $1\leq s<m$, and let $\mathcal{S}$ be a set of pairs $(j,A)$ with $s<j\leq m$ and $A\subseteq[s]$ such that the cube $Q(j,A)$ is monochromatic for every $(j,A)\in\mathcal{S}$. Then there is a monochromatic union-closed family with at least $|\mathcal{S}|/k$ members.

*Proof.* Choose a colour $c$ such that the set $\mathcal{S}_{c}$ of pairs in $\mathcal{S}$ whose cube has colour $c$ satisfies $|\mathcal{S}_{c}|\geq|\mathcal{S}|/k$, and let $\mathcal{F}$ be the union of the cubes $Q(j,A)$ over $(j,A)\in\mathcal{S}_{c}$. Every member of $\mathcal{F}$ has colour $c$.

Let $C_{j}\setminus Y_{B}\in Q(j,A)$ and $C_{j^{\prime}}\setminus Y_{B^{\prime}}\in Q(j^{\prime},A^{\prime})$ be members of $\mathcal{F}$, where $(j,A),(j^{\prime},A^{\prime})\in\mathcal{S}_{c}$ and, say, $j\leq j^{\prime}$. As $B,B^{\prime}\subseteq[s]\subseteq[j]$, Lemma 2.4 shows that their union is $C_{j^{\prime}}\setminus Y_{B\cap B^{\prime}}$, and since $B\cap B^{\prime}\subseteq A^{\prime}$ this set belongs to $Q(j^{\prime},A^{\prime})\subseteq\mathcal{F}$. So $\mathcal{F}$ is union-closed.

Finally, the map $(j,A)\mapsto C_{j}\setminus Y_{A}$ from $\mathcal{S}_{c}$ to $\mathcal{F}$ is injective. Indeed, $j>s$ means $j\notin A$, so $C_{j}\setminus Y_{A}$ meets $Y_{j}$ and no block of larger index, which determines $j$; and then $A$ is the set of indices $i\leq s$ for which $Y_{i}$ is disjoint from $C_{j}\setminus Y_{A}$. Hence $|\mathcal{F}|\geq|\mathcal{S}_{c}|\geq|\mathcal{S}|/k$. ∎

The family $\mathcal{F}$ is not closed under intersection in general: the intersection of the two sets above is $C_{j}\setminus Y_{B\cup B^{\prime}}$, and $B\cup B^{\prime}$ need not be contained in $A$. This is as it must be, in view of Theorem 1.4.

## 3. A box inequality and supersaturation

The proof of Theorem 1.1 needs, for every $r$, a shape whose base size lies a little above $r$ and which is monochromatic with probability bounded below by a quantity depending on $k$ and $t$ alone. This section obtains such a shape from an inequality of Cauchy–Schwarz type for products taken over the vertices of a box.

Let $G$ be a finite set and $t\geq 0$. For $x,x^{\prime}\in G^{t}$ and $\omega\in\{0,1\}^{t}$ let $x^{(\omega)}\in G^{t}$ be the point whose $i$-th coordinate is $x^{\prime}_{i}$ if $\omega_{i}=1$ and $x_{i}$ if $\omega_{i}=0$. The $2^{t}$ points $x^{(\omega)}$ are the vertices of the *box* spanned by $x$ and $x^{\prime}$; they are distinct precisely when $x_{i}\neq x^{\prime}_{i}$ for every $i$. Expectations are taken with respect to the uniform distribution on the finite set indicated by the variables.

**Lemma 3.1 (Box inequality).** Let $f:G^{t}\to[0,\infty)$. If $x$ and $x^{\prime}$ are independent and uniformly distributed in $G^{t}$, then

$$\mathbb{E}\prod_{\omega\in\{0,1\}^{t}}f\bigl(x^{(\omega)}\bigr)\ \geq\ \bigl(\mathbb{E}f(x)\bigr)^{2^{t}}.$$

*Proof.* We use induction on $t$. For $t=0$ both sides equal the value of $f$ at the only point of $G^{0}$. Let $t\geq 1$ and write the points of $G^{t}$ as $(a,y)$ with $a\in G$ and $y\in G^{t-1}$. For $y,y^{\prime}\in G^{t-1}$ and $a\in G$ put

$$h_{y,y^{\prime}}(a)=\prod_{\omega\in\{0,1\}^{t-1}}f\bigl(a,y^{(\omega)}\bigr).$$

Splitting $\omega\in\{0,1\}^{t}$ according to its first coordinate shows that the product over the box spanned by $x=(a,y)$ and $x^{\prime}=(a^{\prime},y^{\prime})$ equals $h_{y,y^{\prime}}(a)\,h_{y,y^{\prime}}(a^{\prime})$. The variables $a,a^{\prime},y,y^{\prime}$ are independent, so the Cauchy–Schwarz inequality gives

$$\mathbb{E}\prod_{\omega}f\bigl(x^{(\omega)}\bigr)=\mathbb{E}_{y,y^{\prime}}\bigl(\mathbb{E}_{a}h_{y,y^{\prime}}(a)\bigr)^{2}\ \geq\ \bigl(\mathbb{E}_{a}\mathbb{E}_{y,y^{\prime}}h_{y,y^{\prime}}(a)\bigr)^{2}.$$

For fixed $a$, the induction hypothesis applied to $f(a,\cdot)$ gives $\mathbb{E}_{y,y^{\prime}}h_{y,y^{\prime}}(a)\geq(\mathbb{E}_{y}f(a,y))^{2^{t-1}}$, and since $z\mapsto z^{2^{t-1}}$ is convex on $[0,\infty)$, Jensen’s inequality gives

$$\mathbb{E}_{a}\bigl(\mathbb{E}_{y}f(a,y)\bigr)^{2^{t-1}}\ \geq\ \bigl(\mathbb{E}_{a}\mathbb{E}_{y}f(a,y)\bigr)^{2^{t-1}}=\bigl(\mathbb{E}f\bigr)^{2^{t-1}}.$$

Squaring, the left-hand side of the lemma is at least $(\mathbb{E}f)^{2^{t}}$. ∎

The quantity on the left of Lemma 3.1 is the $2^{t}$-th power of the box norm of $f$, and the argument is the one Gowers used for the uniformity norms in a proof of Szemerédi’s theorem [Go01].[^2] Applied to the indicator of each colour class it says that a random box is monochromatic with probability at least $k^{1-2^{t}}$, whatever the colouring. What remains is to turn boxes in a grid into cubes of sets, and this is where the order of the ground set is randomised.

For the rest of the paper put

$$L_{k}(t)=t\,k^{2^{t}}\qquad\text{and}\qquad M_{k}(t)=t\,L_{k}(t)=t^{2}\,k^{2^{t}}\qquad(t\geq 1), \tag{3.1}$$

so that $M_{2}(1)=4$, $M_{2}(2)=64$ and $M_{2}(3)=2304$. Note that $M_{k}(t)\geq t+1$.

**Proposition 3.2 (Supersaturation).** Let $t\geq 1$ and $L\geq 1$ be integers, put $M=tL$, and let $r\geq 0$ be an integer with $r+M\leq n$. There are integers $u$ and $a_{1},\dots,a_{t}\geq 1$ with

$$r\leq u,\qquad(u-r)+a_{1}+\dots+a_{t}\leq M,\qquad\rho_{\chi}(u;a_{1},\dots,a_{t})\ \geq\ k^{1-2^{t}}-\frac{t}{L+1}.$$

In particular, with $L=L_{k}(t)$ and $M=M_{k}(t)$ as in (3.1), one can achieve $\rho_{\chi}(u;a_{1},\dots,a_{t})\geq k^{-2^{t}}$, and then $u\leq r+M-t$ and $a_{i}\leq M$ for every $i$.

*Proof.* Choose pairwise disjoint sets $R,Z_{1},\dots,Z_{t}\subseteq[n]$ with $|R|=r$ and $|Z_{i}|=L$, which is possible because $r+tL\leq n$, and list $Z_{i}=\{z_{i,1},\dots,z_{i,L}\}$. Put $G=\{0,1,\dots,L\}$ and, for $x\in G^{t}$,

$$S(x)=R\cup\bigcup_{i=1}^{t}\{z_{i,q}:\ 1\leq q\leq x_{i}\},$$

so that $x$ records how far along each of the $t$ chains $z_{i,1},z_{i,2},\dots$ the set $S(x)$ reaches. Let $\sigma\in S_{n}$ and $x,x^{\prime}\in G^{t}$ be independent and uniform, and let $E$ be the event that $\chi(\sigma(S(\cdot)))$ is constant on the box spanned by $x$ and $x^{\prime}$.

Fix $\sigma$, and for each colour $c$ let $p_{c}$ be the probability that $\chi(\sigma(S(x)))=c$ for uniform $x$. Lemma 3.1 applied to the indicator function of the colour class of $c$ shows that, conditionally on $\sigma$, all vertices of the box have colour $c$ with probability at least $p_{c}^{2^{t}}$. Since $p_{1}+\dots+p_{k}=1$, convexity gives $\sum_{c}p_{c}^{2^{t}}\geq k\cdot k^{-2^{t}}$, and averaging over $\sigma$ gives $\Pr(E)\geq k^{1-2^{t}}$. The event $D$ that $x_{i}=x^{\prime}_{i}$ for some $i$ has probability at most $t/(L+1)$, so

$$\Pr(E\setminus D)\ \geq\ k^{1-2^{t}}-\frac{t}{L+1}.$$

Suppose now that $x_{i}\neq x^{\prime}_{i}$ for every $i$, and put $\ell_{i}=\min(x_{i},x^{\prime}_{i})$ and $h_{i}=\max(x_{i},x^{\prime}_{i})$. The vertices of the box are the points whose $i$-th coordinate is $\ell_{i}$ or $h_{i}$ for every $i$, so the sets $S(x^{(\omega)})$ form the $t$-cube $Q_{x,x^{\prime}}=Q(U;X_{1},\dots,X_{t})$ with

$$U=S(\ell),\qquad X_{i}=\{z_{i,q}:\ \ell_{i}<q\leq h_{i}\}$$

(Figure 6). Its shape is $(r+\sum_{i}\ell_{i};\ h_{1}-\ell_{1},\dots,h_{t}-\ell_{t})$, and $u=r+\sum_{i}\ell_{i}$ and $a_{i}=h_{i}-\ell_{i}$ satisfy $u\geq r$, $a_{i}\geq 1$ and $(u-r)+\sum_{i}a_{i}=\sum_{i}h_{i}\leq tL=M$. The event $E\setminus D$ says that $\sigma(Q_{x,x^{\prime}})$ is monochromatic. For a fixed pair $(x,x^{\prime})$ outside $D$, the probability of this over $\sigma$ is $\rho_{\chi}$ at the shape of $Q_{x,x^{\prime}}$, because $\sigma(Q_{x,x^{\prime}})$ is then a uniformly random cube of that shape. Hence $\Pr(E\setminus D)$ is an average, over all pairs $(x,x^{\prime})$, of numbers that vanish on $D$ and are values of $\rho_{\chi}$ at admissible shapes elsewhere, and one of these values is at least $\Pr(E\setminus D)$.

For $L=L_{k}(t)$ we have $t/(L+1)<t/L=k^{-2^{t}}$, so the value found is at least $(k-1)k^{-2^{t}}\geq k^{-2^{t}}$. The bounds on $u$ and $a_{i}$ follow from $a_{i}\geq 1$. ∎

**Figure 6.** The grid $G^{3}$ with $G=\{0,1,\dots,4\}$, as in the proof of Proposition 3.2 with $t=3$ and $L=4$, and the box spanned by $x=(1,1,2)$ and $x^{\prime}=(3,3,0)$. Its eight vertices are the points of $\{1,3\}\times\{1,3\}\times\{0,2\}$, between the corners $\ell=(1,1,0)$ and $h=(3,3,2)$. The sets $S(y)$ at these vertices form the $3$-cube with base $S(\ell)$ and generators $X_{i}=\{z_{i,q}:\ell_{i}<q\leq h_{i}\}$, whose shape is $(r+2;2,2,2)$.

The proof is short enough that its two sources of loss are easy to see.[^3] The factor $k^{1-2^{t}}$ is already the probability that a fixed $t$-cube is monochromatic in a uniformly random $k$-colouring, so for such colourings the expected value of $\rho_{\chi}$ at every shape equals $k^{1-2^{t}}$ and nothing better can be obtained on average. The subtraction of $t/(L+1)$ only accounts for degenerate boxes, and it is what forces the window $M$ to be as large as $t^{2}k^{2^{t}}$.

**Remark 3.3.** Identify a subset $S$ of a finite set $Z$ with the word in $\{0,1\}^{Z}$ that has the letter $1$ exactly at the positions in $S$. A $t$-cube then becomes a $t$-dimensional combinatorial subspace: the positions in $U$ carry the fixed letter $1$, those outside $T$ the fixed letter $0$, and those in $X_{i}$ the $i$-th variable. Since $\rho_{\chi}>0$ in Proposition 3.2, every $k$-colouring of the subsets of a set of size $M_{k}(t)$ is constant on some $t$-cube, which is the two-letter case of the multidimensional Hales–Jewett theorem [HJ63, GRS90] with the bound $t^{2}k^{2^{t}}$. The proposition says more: a proportion at least $k^{-2^{t}}$ of the cubes of one shape are monochromatic, and this density is what makes the rate in Theorem 1.1 explicit.

## 4. Proof of Theorem 1.1

Fix $k\geq 2$ and $t\geq 1$, put $M=M_{k}(t)$ as in (3.1), and let $n$ be large enough that

$$m=\Bigl\lfloor\frac{n-1}{M}\Bigr\rfloor\qquad\text{and}\qquad s=\Bigl\lfloor\frac{m}{2}\Bigr\rfloor$$

satisfy $s\geq t$. Note that $mM\leq n-1$. Fix pairwise disjoint sets $G_{1},\dots,G_{m}\subseteq[n]$ of size $M$, the *slots*, and list each slot as $G_{i}=\{g_{i,1},\dots,g_{i,M}\}$; for instance $g_{i,q}=(i-1)M+q$. For a vector $\beta\in[M]^{m}$ of block sizes let

$$Y_{i}^{\beta}=\{g_{i,1},\dots,g_{i,\beta_{i}}\}\qquad(1\leq i\leq m),$$

and for $\sigma\in S_{n}$ let $Q_{\sigma,\beta}(j,A)$ denote the cube $Q(j,A)$ of Definition 2.3 built from the blocks $\sigma(Y_{1}^{\beta}),\dots,\sigma(Y_{m}^{\beta})$. Thus $Q_{\sigma,\beta}(j,A)=\sigma\bigl(Q_{\mathrm{id},\beta}(j,A)\bigr)$, and $Q_{\sigma,\beta}(j,A)$ has shape

$$\Bigl(\sum_{i\leq j,\ i\notin A}\beta_{i};\ (\beta_{a})_{a\in A}\Bigr). \tag{4.1}$$

Let $\mathcal{P}$ be the set of pairs $(j,A)$ with $s<j\leq m$, $A\subseteq[s]$ and $|A|=t$. Call $\beta$ *good for* $(j,A)$ if the shape (4.1) satisfies $\rho_{\chi}\geq k^{-2^{t}}$.

**Lemma 4.1 (Slices).** Let $1\leq j\leq m$ and $A\subseteq[j-1]$ with $|A|=t$. At least $M^{m-t-1}$ vectors $\beta\in[M]^{m}$ are good for $(j,A)$.

*Proof.* Write $A=\{a_{(1)}<\dots<a_{(t)}\}$ and let $K=[m]\setminus(A\cup\{j\})$, a set of $m-t-1$ indices. We show that every choice of $(\beta_{i})_{i\in K}\in[M]^{K}$ extends to a vector $\beta$ that is good for $(j,A)$. Different choices give different vectors, which proves the lemma.

Fix $(\beta_{i})_{i\in K}$, let $R=\sum_{i<j,\,i\notin A}\beta_{i}$, which involves only indices in $K$, and put $r=R+1$. Since $R\leq(j-1-t)M\leq(m-2)M$, we have $r+M\leq(m-1)M+1\leq n$. Proposition 3.2 gives $u$ and $a_{1},\dots,a_{t}$ with $\rho_{\chi}(u;a)\geq k^{-2^{t}}$, where $z=u-r$ satisfies $0\leq z\leq M-t\leq M-1$ and $1\leq a_{i}\leq M$. Set

$$\beta_{j}=z+1,\qquad\beta_{a_{(i)}}=a_{i}\quad(1\leq i\leq t).$$

These values lie in $[M]$, and the shape (4.1) becomes $(R+z+1;a_{1},\dots,a_{t})=(u;a_{1},\dots,a_{t})$. So $\beta$ is good for $(j,A)$. ∎

**Lemma 4.2 (Averaging).** There are $\sigma\in S_{n}$ and $\beta\in[M]^{m}$ such that at least

$$\frac{|\mathcal{P}|}{k^{2^{t}}M^{t+1}}$$

of the cubes $Q_{\sigma,\beta}(j,A)$, $(j,A)\in\mathcal{P}$, are monochromatic.

*Proof.* Count the triples $(\sigma,\beta,(j,A))\in S_{n}\times[M]^{m}\times\mathcal{P}$ for which $Q_{\sigma,\beta}(j,A)$ is monochromatic. For fixed $(j,A)\in\mathcal{P}$ and $\beta$ good for $(j,A)$, the number of suitable $\sigma$ is $n!$ times the value of $\rho_{\chi}$ at the shape (4.1), which is at least $n!\,k^{-2^{t}}$. By Lemma 4.1 the number of triples is at least $|\mathcal{P}|\,M^{m-t-1}\,n!\,k^{-2^{t}}$. There are $n!\,M^{m}$ pairs $(\sigma,\beta)$, so one of them occurs in at least $|\mathcal{P}|\,k^{-2^{t}}M^{-t-1}$ triples. ∎

*Proof of Theorem 1.1.* Let $c_{k,t}$ be as in the statement. Since $M\geq t+1$ we have $(4M^{2})^{t+1}\geq(4M(t+1))^{t+1}$, so for $1\leq n<4M(t+1)$ the bound $F_{k}(n)\geq 1>c_{k,t}n^{t+1}$ is trivial. Let $n\geq 4M(t+1)$.

Take $\sigma,\beta$ as in Lemma 4.2 and apply Proposition 2.5 to the blocks $\sigma(Y_{1}^{\beta}),\dots,\sigma(Y_{m}^{\beta})$, which are pairwise disjoint and nonempty, and to the set $\mathcal{S}\subseteq\mathcal{P}$ of pairs whose cube is monochromatic. Every $k$-colouring therefore has a monochromatic union-closed family with at least

$$\frac{|\mathcal{P}|}{k^{2^{t}+1}M^{t+1}} \tag{4.2}$$

members. It remains to bound $|\mathcal{P}|=(m-s)\binom{s}{t}$ from below. Since $n-1<M(m+1)$ and $m\leq 2s+1$, we have $n\leq 2M(s+1)$. Together with $n\geq 4M(t+1)$ this gives $s\geq 2t+1$, so $s\geq 1$ and therefore $n\leq 4Ms$. Also $m-s\geq s$, and $\binom{s}{t}\geq(s/t)^{t}$ because $s\geq t$. Hence

$$|\mathcal{P}|\ \geq\ \frac{s^{t+1}}{t^{t}}\ \geq\ \frac{n^{t+1}}{t^{t}(4M)^{t+1}},$$

and (4.2) is at least $c_{k,t}\,n^{t+1}$.

For the last assertion let $k=2$, so that $\log_{2}M=2\log_{2}t+2^{t}$ and

$$\begin{aligned}\log_{2}\frac{1}{c_{2,t}}&=2^{t}+1+t\log_{2}t+(t+1)(2+2\log_{2}M)\\ &=(2t+3)\,2^{t}+(5t+4)\log_{2}t+2t+3.\end{aligned}$$

Since $\log_{2}t\leq t-1$ and $2^{t}\geq 2t$, the last two terms are at most $5t^{2}+t-1\leq 2t(t+1)^{2}\leq(t+1)^{2}2^{t}$, so $\log_{2}(1/c_{2,t})\leq(t+2)^{2}2^{t}$. If $\log_{2}n\geq(t+2)^{2}2^{t}$, then $c_{2,t}n\geq 1$ and $F(n)\geq c_{2,t}n^{t+1}\geq n^{t}$. ∎

## 5. The upper bound and the random colouring

A family $A_{1},\dots,A_{d}$ of subsets of $[n]$ is an *independent system* if each $A_{i}$ has a *private element*, that is, some $x_{i}\in A_{i}$ lying in no $A_{i^{\prime}}$ with $i^{\prime}\neq i$. A set $X\subseteq[n]$ is *shattered* by a family $\mathcal{F}$ if $\{A\cap X:\ A\in\mathcal{F}\}=2^{X}$, and the *Vapnik–Chervonenkis dimension* $\vc(\mathcal{F})$ is the largest size of a shattered set.

**Lemma 5.1.** Let $d\geq 0$ and $\mathcal{F}\subseteq 2^{[n]}$.

1.  If $A_{1},\dots,A_{d}$ is an independent system, the $2^{d}-1$ unions $\bigcup_{i\in I}A_{i}$, $\emptyset\neq I\subseteq[d]$, are pairwise distinct.

2.  If $\mathcal{F}$ shatters a set of size $d$, then $\mathcal{F}$ contains an independent system of $d$ sets.

3.  (Sauer [Sa72], Shelah [Sh72]) If $\vc(\mathcal{F})\leq d$, then $|\mathcal{F}|\leq\sum_{j=0}^{d}\binom{n}{j}$.

*Proof.* (a) The private element $x_{i}$ lies in $\bigcup_{i^{\prime}\in I}A_{i^{\prime}}$ exactly when $i\in I$, so the union determines $I$. (b) If $X=\{x_{1},\dots,x_{d}\}$ is shattered, choose $A_{i}\in\mathcal{F}$ with $A_{i}\cap X=\{x_{i}\}$; then $x_{i}$ is a private element of $A_{i}$. (c) This is the Sauer–Shelah lemma. ∎

*Proof of Theorem 1.2.* Let $\chi$ be a uniformly random $2$-colouring of $2^{[n]}$, the colours of the $2^{n}$ sets being independent and uniform. Call an ordered $d$-tuple $(A_{1},\dots,A_{d})$ of subsets of $[n]$ *bad* if it is an independent system and the $2^{d}-1$ sets $\bigcup_{i\in I}A_{i}$, $\emptyset\neq I\subseteq[d]$, all have the same colour. By Lemma 5.1(a) these sets are distinct, so a fixed independent tuple is bad with probability $2^{1-(2^{d}-1)}=2^{2-2^{d}}$. There are at most $2^{nd}$ tuples, and $2^{nd}\cdot 2^{2-2^{d}}<1$ by hypothesis, so some colouring has no bad tuple. Fix it.

Let $\mathcal{F}$ be a monochromatic union-closed family. If $\mathcal{F}$ contained an independent system of $d$ sets, all unions of its members would lie in $\mathcal{F}$ and have the same colour, and the system would be bad. So $\mathcal{F}$ contains no independent system of $d$ sets, $\vc(\mathcal{F})\leq d-1$ by Lemma 5.1(b), and $|\mathcal{F}|\leq\sum_{j<d}\binom{n}{j}$ by Lemma 5.1(c).

For the second assertion let $n\geq 2$, and put $a=\lfloor\log_{2}n\rfloor$ and $b=\lfloor\log_{2}a\rfloor$, so that $a\geq 1$, $n<2^{a+1}$, $a<2^{b+1}$ and $b+1\leq a$. For $d=a+b+3$ we get

$$2^{d}=2^{a+1}\cdot 2\cdot 2^{b+1}\ \geq\ 2(n+1)(a+1),$$

whereas $nd+2=n(a+1)+n(b+2)+2\leq 2n(a+1)+2<2(n+1)(a+1)$, because $b+2\leq a+1$ and $a\geq 1$. So $2^{d}>nd+2$, and the first assertion gives $F(n)\leq\sum_{j<d}\binom{n}{j}\leq\sum_{j<d}n^{j}\leq d\,n^{d-1}$. Finally $a\leq\log_{2}n$ and $b\leq\log_{2}a\leq\log_{2}\log_{2}n$, so $d\leq\log_{2}n+\log_{2}\log_{2}n+3$. ∎

Figure 7 shows the size of the bound of Theorem 1.2 as a function of $n$ and $d$. Taking for $d$ the least admissible value $d(n)$ gives a bound valid for every $n$, and $d(n)=\log_{2}n+\log_{2}\log_{2}n+O(1)$ as $n\to\infty$.

**Figure 7.** The surface $\log_{2}\sum_{j<d}\binom{n}{j}$ over $8\leq n\leq 256$ and $1\leq d\leq 14$, with the plane $z=n$ of the trivial bound $2^{n}$. The red curve follows the least admissible $d=d(n)$ of Theorem 1.2, along which the bound stays far below the plane.

*Proof of Corollary 1.3.* (i) Let $n\geq 2$, so that $\ell=\log_{2}\log_{2}n\geq 0$. If $\omega(n)\leq 0$ there is nothing to prove, since $F(n)\geq 1$. Otherwise $x=\ell-2\log_{2}(\ell+2)>1$, and the integer $t=\lfloor x\rfloor$ satisfies $t\geq 1$ and $\omega(n)=x-1<t\leq x$. As $t\leq\ell$ we have $\log_{2}(t+2)\leq\log_{2}(\ell+2)$, and so

$$\log_{2}\bigl((t+2)^{2}2^{t}\bigr)=t+2\log_{2}(t+2)\ \leq\ x+2\log_{2}(\ell+2)=\ell,$$

that is, $(t+2)^{2}2^{t}\leq\log_{2}n$. Theorem 1.1 gives $F(n)\geq n^{t}\geq n^{\omega(n)}$. As $\ell\to\infty$ and $\log_{2}(\ell+2)=o(\ell)$, we have $\omega(n)\to\infty$.

\(ii\) Put $\varepsilon(n)=F(n)^{1/n}-1+1/n$ for $n\geq 1$. Then $(1+\varepsilon(n))^{n}=(F(n)^{1/n}+1/n)^{n}>F(n)$. By Theorem 1.2, $\log F(n)=O((\log n)^{2})$, so $F(n)^{1/n}\to 1$ and $\varepsilon(n)\to 0$.

\(iii\) Let $n\geq 2$ and write $\lambda=\log_{2}n$ and $D=\lambda+\log_{2}\lambda+3$. Theorem 1.2 gives $n^{\omega(n)}\leq F(n)\leq D\,n^{D-1}$, hence

$$\omega(n)\ \leq\ D-1+\frac{\log_{2}D}{\log_{2}n}\ =\ \lambda+O(\log\lambda),$$

which is at most $(1+\varepsilon)\lambda$ for all large $n$.

\(iv\) For every $t\geq 1$, Theorem 1.1 gives $F_{k}(n)\geq c_{k,t}n^{t+1}\geq n^{t}$ as soon as $n\geq 1/c_{k,t}$. Let $\omega_{k}(n)$ be the largest integer $t\leq n$ with $n^{t}\leq F_{k}(n)$; the value $t=0$ qualifies because $F_{k}(n)\geq 1$. Then $\omega_{k}(n)\geq t$ whenever $n\geq\max(t,1/c_{k,t})$, so $\omega_{k}(n)\to\infty$. For the second statement take $\varepsilon_{k}=\varepsilon$ from (ii) and use $F_{k}(n)\leq F(n)$. ∎

The random colouring does contain large monochromatic union-closed families. How large they are indicates how much room is left between Theorems 1.1 and 1.2.

**Proposition 5.2.** Let $n\geq 1$. The average, over all $2$-colourings $\chi$ of $2^{[n]}$, of the largest size of a monochromatic union-closed family is at least

$$\sum_{j=0}^{n}\binom{n}{j}\,2^{1-2^{j}}.$$

If $1\leq j\leq n$ and $2^{2^{j}}\leq n$, this average is at least $(2/n)(n/j)^{j}$.

*Proof.* Let $c=\chi([n])$ and let $\mathcal{Y}$ be the set of $Y\subseteq[n]$ such that $\chi([n]\setminus Y^{\prime})=c$ for every $Y^{\prime}\subseteq Y$. Then $\mathcal{Y}$ is closed under taking subsets and under intersection, so $\mathcal{F}=\{[n]\setminus Y:\ Y\in\mathcal{Y}\}$ is monochromatic and union-closed, because $([n]\setminus Y)\cup([n]\setminus Y^{\prime})=[n]\setminus(Y\cap Y^{\prime})$. A set $Y$ of size $j$ lies in $\mathcal{Y}$ exactly when the $2^{j}-1$ distinct sets $[n]\setminus Y^{\prime}$ with $\emptyset\neq Y^{\prime}\subseteq Y$ all have colour $c$, which happens for a proportion $2^{1-2^{j}}$ of all colourings. Summing over $Y$ gives the average of $|\mathcal{F}|$, which is the first bound. For the second, the term of index $j$ is at least $\binom{n}{j}2^{1-2^{j}}\geq(n/j)^{j}\cdot 2/n$, since $\binom{n}{j}\geq(n/j)^{j}$ and $2^{2^{j}}\leq n$. ∎

For $n\geq 4$ and $j=\lfloor\log_{2}\log_{2}n\rfloor$ the conditions of Proposition 5.2 hold, and $(2/n)(n/j)^{j}\geq n^{\log_{2}\log_{2}n-2-o(1)}$ because $j>\log_{2}\log_{2}n-1$ and $j^{j}=n^{o(1)}$. So for the random colouring the exponent $\omega$ is at least about $\log_{2}\log_{2}n$, while Theorem 1.2, which is also proved with the random colouring, allows it to be as large as $\log_{2}n$. The next two statements turn the upper bound for the random colouring into a counting problem.

**Lemma 5.3.** If $\mathcal{F}\subseteq 2^{[n]}$ is union-closed and $N\leq|\mathcal{F}|$, then $\mathcal{F}$ contains a union-closed subfamily with exactly $N$ members.

*Proof.* It suffices to remove one member when $|\mathcal{F}|>N$. Let $A$ be a member of least size. If $B,C\in\mathcal{F}\setminus\{A\}$ satisfied $B\cup C=A$, then $B\subseteq A$ and $|B|\geq|A|$ would give $B=A$. So $\mathcal{F}\setminus\{A\}$ is union-closed. ∎

**Proposition 5.4.** Let $U(n,N)$ be the number of union-closed families $\mathcal{F}\subseteq 2^{[n]}$ with $|\mathcal{F}|=N$. If $U(n,N)<2^{N-1}$, then $F(n)<N$.

*Proof.* A fixed family of $N$ distinct sets is monochromatic under exactly $2\cdot 2^{2^{n}-N}$ of the $2^{2^{n}}$ colourings. The colourings under which some union-closed family of $N$ sets is monochromatic are therefore at most $U(n,N)\,2^{2^{n}+1-N}<2^{2^{n}}$ in number, and some colouring has no monochromatic union-closed family of exactly $N$ members. By Lemma 5.3 it has none with $N$ or more members, since a subfamily of a monochromatic family is monochromatic. Hence $F(n)\leq N-1$. ∎

Proposition 5.4 is the first-moment method for a uniformly random colouring, and Corollary 1.3(i) shows where it must fail: if $N\leq n^{\omega(n)}\leq F(n)$, then $U(n,N)\geq 2^{N-1}$. We return to this in Question 9.2.

## 6. Cardinality colourings, Hilbert cubes and arithmetic progressions

In this section $k\geq 2$ and $\chi(S)=g(|S|)$ for a function $g:\{0,1,\dots,n\}\to[k]$. A $t$-cube of shape $(u;a_{1},\dots,a_{t})$ consists of sets whose sizes are the elements of $H(u;a_{1},\dots,a_{t})$, and every permutation preserves sizes, so

$$\rho_{\chi}(u;a_{1},\dots,a_{t})=\begin{cases}1&\text{if $g$ is constant on }H(u;a_{1},\dots,a_{t}),\\
0&\text{otherwise.}\end{cases} \tag{6.1}$$

Figure 8 shows a monochromatic Hilbert cube of dimension two.

**Figure 8.** A colouring $g$ of $\{0,1,\dots,20\}$, red discs and blue squares, and a red Hilbert cube $H(5;3,7)=\{5,8,12,15\}$. For the cardinality colouring $\chi(S)=g(|S|)$, every $2$-cube of shape $(5;3,7)$ is red.

Since $\rho_{\chi}$ takes only the values $0$ and $1$ here, Proposition 3.2 turns into Hilbert’s lemma with an explicit window.

**Corollary 6.1.** Let $k\geq 2$, $t\geq 1$, $M=t^{2}k^{2^{t}}$ and $r\geq 0$. Every $g:\{r,r+1,\dots,r+M\}\to[k]$ is constant on some Hilbert cube $H(u;a_{1},\dots,a_{t})$ with $a_{i}\geq 1$, $u\geq r$ and $u+a_{1}+\dots+a_{t}\leq r+M$.

*Proof.* Extend $g$ arbitrarily to $\{0,\dots,r-1\}$ and apply Proposition 3.2, with $n=r+M$, $L=L_{k}(t)$ and $M=M_{k}(t)$, to the cardinality colouring $S\mapsto g(|S|)$ of $2^{[r+M]}$. It gives a shape with $r\leq u$, $(u-r)+\sum_{i}a_{i}\leq M$ and $\rho_{\chi}(u;a)\geq k^{-2^{t}}>0$, so $\rho_{\chi}(u;a)=1$ and $g$ is constant on $H(u;a)$ by (6.1). The elements of $H(u;a)$ lie between $u\geq r$ and $u+\sum_{i}a_{i}\leq r+M$. ∎

*Proof of Theorem 1.5.* Consider the cardinality colouring $\chi(S)=g(|S|)$ and the construction of Section 4, whose hypotheses hold since $n\geq 4M(t+1)$ gives $s\geq n/(4M)\geq t+1$. By (6.1), a vector $\beta$ is good for $(j,A)$ precisely when $g$ is constant on the Hilbert cube formed by the sizes of the members of $Q_{\mathrm{id},\beta}(j,A)$, and these sizes are

$$|C_{j}\setminus Y_{B}|=\beta_{1}+\dots+\beta_{j}-\sum_{b\in B}\beta_{b}\qquad(B\subseteq A),$$

that is, the elements of $H_{\beta}(j,A)$. By Lemma 4.1, for every $(j,A)\in\mathcal{P}$ at least $M^{m-t-1}$ vectors $\beta$ make $H_{\beta}(j,A)$ monochromatic. Averaging over the $M^{m}$ vectors, as in Lemma 4.2 but without the permutations, some $\beta$ makes at least $|\mathcal{P}|/M^{t+1}$ of the cubes $H_{\beta}(j,A)$ monochromatic, and at least a proportion $1/k$ of these share a colour $c$. The estimate $|\mathcal{P}|\geq n^{t+1}/(t^{t}(4M)^{t+1})$ from the proof of Theorem 1.1 completes the proof. All elements of the cubes lie in $\{0,\dots,n\}$, since $\beta_{1}+\dots+\beta_{m}\leq mM\leq n-1$. ∎

Given $\beta$ and $c$ as in Theorem 1.5, the cubes $Q_{\mathrm{id},\beta}(j,A)$ attached to the pairs of colour $c$ are monochromatic under $\chi$, and Proposition 2.5 glues them into a single union-closed family of colour $c$. For cardinality colourings the proof of Theorem 1.1 is therefore entirely a statement about sums of a bounded sequence of integers.

There is also a direct route through arithmetic progressions, which gives Howorka’s theorem.

**Proposition 6.2.** Suppose that $g$ is constant on the arithmetic progression $a,a+e,\dots,a+(p-1)e$, where $e\geq 1$, $p\geq 1$ and $a+(p-1)e\leq n$. Put $q=\lfloor a/e\rfloor$ and $b=q+p-1$. Then $\chi$ has a monochromatic union-closed family with $\sum_{i=0}^{p-1}\binom{b}{i}$ members and a monochromatic sublattice with $2^{p-1}$ members.

*Proof.* Let $a_{0}=a-qe$, so $0\leq a_{0}<e$, and let $D=\{1,\dots,a_{0}\}$ and $X_{i}=\{a_{0}+(i-1)e+1,\dots,a_{0}+ie\}$ for $1\leq i\leq b$. These sets are pairwise disjoint subsets of $[n]$, because $a_{0}+be=a+(p-1)e\leq n$, and $|D|=a_{0}$ and $|X_{i}|=e$. The family

$$\mathcal{F}=\bigl\{D\cup X_{I}:\ I\subseteq[b],\ |I|\geq q\bigr\}$$

is union-closed, since $D\cup X_{I}\cup D\cup X_{I^{\prime}}=D\cup X_{I\cup I^{\prime}}$ and $|I\cup I^{\prime}|\geq q$ whenever $|I|\geq q$. A member with index set $I$ has size $a_{0}+|I|e=a+(|I|-q)e$, where $0\leq|I|-q\leq p-1$, so all members have the colour of the progression, and

$$|\mathcal{F}|=\sum_{i=q}^{b}\binom{b}{i}=\sum_{i=0}^{p-1}\binom{b}{i}$$

by the symmetry $\binom{b}{i}=\binom{b}{b-i}$. For the sublattice take $D^{\prime}=\{1,\dots,a\}$ and $X^{\prime}_{i}=\{a+(i-1)e+1,\dots,a+ie\}$ for $1\leq i\leq p-1$. The $(p-1)$-cube $Q(D^{\prime};X^{\prime}_{1},\dots,X^{\prime}_{p-1})$ is a sublattice with $2^{p-1}$ members, whose sizes $a+|I|e$ lie in the progression. ∎

For $k\geq 1$ and $p\geq 1$ let $W_{k}(p)$ be the least $W$ such that every $g:\{0,1,\dots,W-1\}\to[k]$ is constant on some progression $a,a+e,\dots,a+(p-1)e$ with $e\geq 1$. This number exists by van der Waerden’s theorem.

**Theorem 6.3 (van der Waerden [vdW27]).** For all $k\geq 1$ and $p\geq 1$ there is $W$ such that every $g:\{0,1,\dots,W-1\}\to[k]$ is constant on an arithmetic progression of length $p$ with a positive common difference.

The formal proof derives Theorem 6.3 from the Hales--Jewett theorem.[^4]

**Theorem 6.4 (Howorka).** Let $p\geq 2$, let $W=W_{k}(p)$, and let $n\geq 2W$. Every cardinality $k$-colouring of $2^{[n]}$ has a monochromatic union-closed family with at least

$$\binom{\lfloor n/(2W)\rfloor+p-1}{p-1}\ \geq\ \frac{\bigl(\lfloor n/(2W)\rfloor+1\bigr)^{p-1}}{(p-1)!}$$

members.

*Proof.* The integers $n-W,n-W+1,\dots,n-1$ lie in $\{0,\dots,n\}$, and by the definition of $W$ the function $g$ is constant on a progression $a,a+e,\dots,a+(p-1)e$ among them, with $e\geq 1$. Here $a\geq n-W$ and $a+(p-1)e\leq n-1$, and $e\leq(p-1)e\leq W-1$ because $p\geq 2$. Since $n\geq 2W$ we have $n-W\geq\lfloor n/2\rfloor$, and so

$$\Bigl\lfloor\frac{a}{e}\Bigr\rfloor\ \geq\ \Bigl\lfloor\frac{n-W}{W}\Bigr\rfloor\ \geq\ \Bigl\lfloor\frac{\lfloor n/2\rfloor}{W}\Bigr\rfloor=\Bigl\lfloor\frac{n}{2W}\Bigr\rfloor.$$

Proposition 6.2 gives a monochromatic union-closed family with at least $\binom{b}{p-1}$ members, where $b=\lfloor a/e\rfloor+p-1\geq\lfloor n/(2W)\rfloor+p-1$, and $\binom{b}{p-1}$ increases with $b$. Finally, with $N=\lfloor n/(2W)\rfloor$,

$$\binom{N+p-1}{p-1}=\frac{(N+1)(N+2)\cdots(N+p-1)}{(p-1)!}\ \geq\ \frac{(N+1)^{p-1}}{(p-1)!}.\qed$$

For fixed $p$ the bound of Theorem 6.4 is at least a constant multiple of $n^{p-1}$, and $p$ is arbitrary. So for cardinality colourings the largest monochromatic union-closed family grows faster than every fixed power of $n$, which is Howorka’s theorem as recorded in [Bl26]; for all colourings this is contained in Corollary 1.3. Proposition 6.2 also restricts the cardinality colourings that are good for $f$: if no monochromatic sublattice has more than $m$ members, then $g$ is constant on no progression of length $p$ in $\{0,\dots,n\}$ with $2^{p-1}>m$.

## 7. The lattice function

The lower bound in Theorem 1.4 is (1.1). The upper bounds come from a random colouring and a count of sublattices, which in turn rests on a description of a sublattice by a small amount of data.

Let $\mathcal{L}\subseteq 2^{[n]}$ be a nonempty sublattice, and put $B=\bigcap_{A\in\mathcal{L}}A$ and $T=\bigcup_{A\in\mathcal{L}}A$, the least and the greatest member of $\mathcal{L}$. For $x\in T\setminus B$ let

$$A_{x}=\bigcap\{A\in\mathcal{L}:\ x\in A\},$$

the least member of $\mathcal{L}$ containing $x$, and for $X\subseteq T\setminus B$ put $A_{X}=\bigcup_{x\in X}A_{x}$. For $x\in T\setminus B$ let $[x]=\{y\in T\setminus B:\ A_{y}=A_{x}\}$ be the *class* of $x$, and let $D_{x}=\{y\in T\setminus B:\ A_{y}\subsetneq A_{x}\}$.

**Lemma 7.1.** Let $\mathcal{L}$ be a nonempty sublattice of $2^{[n]}$.

1.  Every $A\in\mathcal{L}$ equals $B\cup A_{A\setminus B}$, and $B\cup A_{X}\in\mathcal{L}$ for every $X\subseteq T\setminus B$. Hence $\mathcal{L}=\{B\cup A_{X}:\ X\subseteq T\setminus B\}$.

2.  For $x,y\in T\setminus B$ we have $y\in A_{x}$ if and only if $A_{y}\subseteq A_{x}$.

3.  For $x\in T\setminus B$ we have $A_{x}=B\cup[x]\cup A_{D_{x}}$.

*Proof.* (a) Let $A\in\mathcal{L}$. Then $B\subseteq A\subseteq T$, and $A_{x}\subseteq A$ for every $x\in A\setminus B$, so $B\cup A_{A\setminus B}\subseteq A$; conversely every $x\in A$ lies in $B$ or in $A_{x}$. The set $B\cup A_{X}$ is a union of members of $\mathcal{L}$, or equals $B$ when $X=\emptyset$.

\(b\) If $y\in A_{x}$, then $A_{x}$ is a member containing $y$, so $A_{y}\subseteq A_{x}$. Conversely $y\in A_{y}$.

\(c\) The right-hand side is contained in $A_{x}$: we have $B\subseteq A_{x}$, every $y\in[x]$ lies in $A_{y}=A_{x}$, and $A_{y}\subseteq A_{x}$ for $y\in D_{x}$. Let $z\in A_{x}\setminus B$. Then $z\in T\setminus B$ and $A_{z}\subseteq A_{x}$ by (b), so either $A_{z}=A_{x}$ and $z\in[x]$, or $z\in D_{x}$ and $z\in A_{z}\subseteq A_{D_{x}}$. ∎

Part (a) is the form that Birkhoff’s representation theorem for finite distributive lattices [Bi37] takes for sublattices of $2^{[n]}$.[^5] Part (a) already shows that $\mathcal{L}$ is determined by $B$ and the map $x\mapsto A_{x}$. To count large sublattices more efficiently we describe each $A_{x}$ through a small set of points below it.

**Lemma 7.2.** Let $\mathcal{L}$ be a nonempty sublattice and $x\in T\setminus B$, and let $R_{x}\subseteq D_{x}$ be a set of least size with $A_{R_{x}}=A_{D_{x}}$. Then $A_{x}=B\cup[x]\cup A_{R_{x}}$, no set $A_{y}$ with $y\in R_{x}$ is contained in $A_{y^{\prime}}$ for another $y^{\prime}\in R_{x}$, and the $2^{|R_{x}|}$ sets $B\cup A_{Y}$, $Y\subseteq R_{x}$, are distinct members of $\mathcal{L}$. In particular $|R_{x}|\leq\log_{2}|\mathcal{L}|$.

*Proof.* The first statement is Lemma 7.1(c). If $A_{y}\subseteq A_{y^{\prime}}$ for distinct $y,y^{\prime}\in R_{x}$, then $R_{x}\setminus\{y\}$ would be a smaller set with the same union $A_{R_{x}}$. The sets $B\cup A_{Y}$ lie in $\mathcal{L}$ by Lemma 7.1(a). Let $Y\neq Y^{\prime}$ be subsets of $R_{x}$, say $y\in Y\setminus Y^{\prime}$. Then $y\in A_{y}\subseteq B\cup A_{Y}$. If $y$ lay in $B\cup A_{Y^{\prime}}$, then, as $y\notin B$, we would have $y\in A_{y^{\prime}}$ for some $y^{\prime}\in Y^{\prime}$, so $A_{y}\subseteq A_{y^{\prime}}$ by Lemma 7.1(b) with $y^{\prime}\neq y$, which is impossible. So $B\cup A_{Y}\neq B\cup A_{Y^{\prime}}$. ∎

For each nonempty sublattice fix sets $R_{x}$ as in Lemma 7.2, and for $x\in T\setminus B$ let $r(x)$ be the least element of $[x]$.

**Lemma 7.3.** Let $\mathcal{L}$ and $\mathcal{L}^{\prime}$ be nonempty sublattices of $2^{[n]}$ with the same least member $B$, the same greatest member $T$, the same map $r$ on $T\setminus B$ and the same sets $R_{x}$ for $x\in T\setminus B$. Then $\mathcal{L}=\mathcal{L}^{\prime}$.

*Proof.* Write $A_{x}$ and $A^{\prime}_{x}$ for the least members containing $x$ in $\mathcal{L}$ and $\mathcal{L}^{\prime}$. The class of $x$ is $\{y\in T\setminus B:\ r(y)=r(x)\}$ in both lattices. We show $A_{x}=A^{\prime}_{x}$ for $x\in T\setminus B$ by induction on $|A_{x}|$. By Lemma 7.2,

$$A_{x}=B\cup[x]\cup A_{R_{x}}\qquad\text{and}\qquad A^{\prime}_{x}=B\cup[x]\cup A^{\prime}_{R_{x}}.$$

Every $y\in R_{x}$ satisfies $A_{y}\subsetneq A_{x}$, so $|A_{y}|<|A_{x}|$ and $A_{y}=A^{\prime}_{y}$ by induction. Hence $A_{x}=A^{\prime}_{x}$, and Lemma 7.1(a) gives $\mathcal{L}=\mathcal{L}^{\prime}$. ∎

**Lemma 7.4.**

1.  The number of nonempty sublattices of $2^{[n]}$ is at most $2^{n(n+1)}$.

2.  For $w\geq 0$, the number of nonempty sublattices $\mathcal{L}$ of $2^{[n]}$ with $\lfloor\log_{2}|\mathcal{L}|\rfloor=w$ is at most $2^{2n}\,n^{n}\,(n+1)^{wn}$.

*Proof.* (a) By Lemma 7.1(a), $\mathcal{L}$ is determined by $B$ and the map $x\mapsto A_{x}$, extended by $A_{x}=B$ for $x\notin T\setminus B$. There are $2^{n}$ choices for $B$ and $(2^{n})^{n}$ for the map.

\(b\) By Lemma 7.3, $\mathcal{L}$ is determined by $B$, $T$, the map $r$ and the sets $R_{x}$, extended in any fixed way to all $x\in[n]$. By Lemma 7.2 each $R_{x}$ has at most $w$ elements. There are at most $2^{n}$ choices for each of $B$ and $T$, at most $n^{n}$ for $r$, and, since the number of subsets of $[n]$ with at most $w$ elements is $\sum_{i\leq w}\binom{n}{i}\leq\sum_{i\leq w}n^{i}\leq(n+1)^{w}$, at most $(n+1)^{wn}$ for the family $(R_{x})_{x\in[n]}$. ∎

*Proof of Theorem 1.4.* The number of $2$-colourings under which a fixed family of $N$ distinct sets is monochromatic is $2\cdot 2^{2^{n}-N}$.

For the first bound put $m_{1}=n^{2}+n+2$. By Lemma 7.4(a), the colourings under which some sublattice with at least $m_{1}$ members is monochromatic number at most $2^{n(n+1)}\cdot 2\cdot 2^{2^{n}-m_{1}}=2^{2^{n}-1}$. So some colouring has no such sublattice, and $f(n)\leq m_{1}-1=n^{2}+n+1$.

For the second bound let $L=\lfloor\log_{2}n\rfloor+1$, so that $n+1\leq 2^{L}$, and for $w\geq 0$ put

$$E(w)=n\bigl(L(w+1)+2\bigr)+w+3.$$

The function $E$ is increasing, and $E(w)\leq 2^{w}$ for $w\geq 3L+2$. Indeed, with $P=2^{L}$ we have $n\leq P-1$ and $L+1\leq P$, so

$$E(3L+2)=n(3L^{2}+3L+2)+3L+5\leq P(3L^{2}+3L+5)\leq 4P^{3}=2^{3L+2},$$

and $E(w+1)=E(w)+nL+1\leq 2E(w)$. Put $m_{2}=E(3L+1)=nL(3L+2)+2n+3L+4$. Every sublattice $\mathcal{L}$ with $|\mathcal{L}|\geq m_{2}$ and $\lfloor\log_{2}|\mathcal{L}|\rfloor=w$ satisfies $|\mathcal{L}|\geq E(w)$: for $w\leq 3L+1$ because $E(w)\leq m_{2}$, and for $w\geq 3L+2$ because $E(w)\leq 2^{w}\leq|\mathcal{L}|$. By Lemma 7.4(b), and using $n\leq 2^{L}$ and $n+1\leq 2^{L}$, there are at most $2^{2n}n^{n}(n+1)^{wn}\leq 2^{n(L(w+1)+2)}$ such sublattices for each $w$, and each is monochromatic under at most $2^{2^{n}+1-E(w)}$ colourings. The colourings under which some sublattice with at least $m_{2}$ members is monochromatic therefore number at most

$$\sum_{w=0}^{n}2^{n(L(w+1)+2)}\,2^{2^{n}+1-E(w)}=2^{2^{n}}\sum_{w=0}^{n}2^{-(w+2)}\ <\ 2^{2^{n}-1},$$

the sum running up to $w=n$ because a sublattice has at most $2^{n}$ members. So some colouring has no such sublattice, and $f(n)\leq m_{2}-1=nL(3L+2)+2n+3L+3$.

As $L\leq\log_{2}n+1$, the second bound is $(3+o(1))\,n(\log_{2}n)^{2}$. The last assertion of the theorem follows from Theorem 1.1 with $t>C$. ∎

The first bound is the smaller one for $n<210$ and the second for $n\geq 263$. Both bounds come from the random colouring, and the gap between them and the lower bound $\lceil(n+1)/2\rceil$ is the subject of Question 9.3.

## 8. Formal verification

The results of Sections 2–7 have been formalised in Lean 4 [MU21], version 4.34.1, with the Mathlib library [Mat20] at the release of the same version number. The development contains no unproved steps, and for each statement listed below Lean reports that the proof uses only the three standard axioms of its logic, namely propositional extensionality, the axiom of choice and the soundness of quotient types.[^6]

In the formalisation the ground set is the type of $n$ elements, a $k$-colouring is a function from its subsets to a finite type with $k$ elements, and $F_{k}(n)$, $F(n)$ and $f(n)$ are defined literally as the minimum over all colourings of the largest size of a monochromatic family that is closed under union, respectively under union and intersection. It is also proved that $F_{k}(n)$ is the largest $m$ such that every $k$-colouring has a monochromatic union-closed family of at least $m$ sets. The following statements are checked.

1.  The bound (1.1), and $F_{k}(n)\leq F(n)$ for $k\geq 2$.

2.  Theorem 1.1 in the stated form $n^{t+1}\leq k^{2^{t}+1}t^{t}(4M^{2})^{t+1}F_{k}(n)$ for $n\geq 1$, and the bound $F(n)\geq n^{t}$ for $n\geq 2^{(t+2)^{2}2^{t}}$, together with Lemmas 2.2–4.2 and Propositions 2.5 and 3.2 in the form in which the proof uses them.

3.  Lemma 5.1 and Theorem 1.2, both the bound $F(n)\leq\sum_{j<d}\binom{n}{j}$ and the two explicit forms, with the Sauer–Shelah lemma taken from Mathlib.

4.  Corollary 1.3: part (i) with the stated $\omega(n)$ and $\omega(n)\to\infty$, parts (ii)–(iv), and the conjunction of the two conjectures in the form (1.2) as a single theorem.

5.  Proposition 5.2, Lemma 5.3 and Proposition 5.4.

6.  Corollary 6.1, Theorem 1.5, Proposition 6.2, Theorem 6.3, derived from Mathlib’s Hales–Jewett theorem as described above, and Theorem 6.4, proved for every number $W$ with the property that defines $W_{k}(p)$.

7.  Lemmas 7.1–7.4 and Theorem 1.4.

The formal proofs follow the arguments given here, with one change of language: probabilities are replaced by counts. Permutations and size vectors are counted rather than sampled, so that Lemma 4.2 becomes a double counting over the product of the two sets, and the random colourings of Sections 5 and 7 are replaced by counts of colourings. The box inequality is proved for sums over all pairs of points, which is Lemma 3.1 multiplied by $|G|^{2t}$. Outside the formal development remain only the figures and the elementary asymptotic rewritings of the proved bounds, such as $\omega(n)=(1-o(1))\log_{2}\log_{2}n$ in Corollary 1.3 and $n^{\log_{2}\log_{2}n-2-o(1)}$ after Proposition 5.2.

## 9. Questions

With both conjectures settled, what remains open is the precise size of the two functions, above all of $F$.

**Question 9.1.** What is the order of magnitude of $\log F(n)/\log n$? By Corollary 1.3 it lies between $(1-o(1))\log_{2}\log_{2}n$ and $(1+o(1))\log_{2}n$. Is $F(n)=n^{\Theta(\log\log n)}$, or is $F(n)=n^{\Theta(\log n)}$?

The random colouring is the natural candidate for an upper bound, and by Proposition 5.2 it cannot give anything below $n^{(1-o(1))\log_{2}\log_{2}n}$. Proposition 5.4 reduces the matching upper bound to a count.

**Question 9.2.** Is there a constant $C$ such that $U(n,N)<2^{N-1}$ for all large $n$ and all $N\geq n^{C\log_{2}\log_{2}n}$?

A positive answer would give $F(n)<n^{C\log_{2}\log_{2}n}$ by Proposition 5.4, and together with Corollary 1.3(i) it would determine $\log F(n)/\log n$ up to a constant factor, answering Question 9.1 in favour of $n^{\Theta(\log\log n)}$. By Corollary 1.3(i) the inequality fails for $N\leq n^{\omega(n)}$, so the threshold in Question 9.2 cannot be lowered below $n^{(1-o(1))\log_{2}\log_{2}n}$.

**Question 9.3.** Is $f(n)=O(n)$? Is $f(n)=\lceil(n+1)/2\rceil$ for every $n$?

The lower bound $\lceil(n+1)/2\rceil$ comes from a single chain, and the upper bounds of Theorem 1.4 from counting sublattices in a random colouring, which leaves a factor of order $(\log n)^{2}$ between them.

## Data availability

The Lean formalisation of the results of this paper and the sources of the paper are available at https://doi.org/10.5281/zenodo.23094057. Claude (Anthropic) assisted with the coding.

## References

- [AHS24] R. Alweiss, B. Huang and M. Sellke, *Improved lower bound for Frankl’s union-closed sets conjecture*, Electron. J. Combin. 31 (2024), no. 3, Paper No. P3.35. doi:10.37236/12232
- [Bi37] G. Birkhoff, *Rings of sets*, Duke Math. J. 3 (1937), no. 3, 443–454. doi:10.1215/S0012-7094-37-00334-X
- [Bl26] T. F. Bloom, *Erdős Problem \#1183*, https://www.erdosproblems.com/1183, accessed 30 September 2026.
- [Gi22] J. Gilmer, *A constant lower bound for the union-closed sets conjecture*, preprint (2022), arXiv:2211.09055.
- [Go01] W. T. Gowers, *A new proof of Szemerédi’s theorem*, Geom. Funct. Anal. 11 (2001), no. 3, 465–588. doi:10.1007/s00039-001-0332-9
- [GRS90] R. L. Graham, B. L. Rothschild and J. H. Spencer, *Ramsey Theory*, second edition, John Wiley & Sons, New York, 1990.
- [GRS99] D. S. Gunderson, V. Rödl and A. Sidorenko, *Extremal problems for sets forming Boolean algebras and complete partite hypergraphs*, J. Combin. Theory Ser. A 88 (1999), no. 2, 342–367. doi:10.1006/jcta.1999.2973
- [HJ63] A. W. Hales and R. I. Jewett, *Regularity and positional games*, Trans. Amer. Math. Soc. 106 (1963), no. 2, 222–229. doi:10.1090/S0002-9947-1963-0143712-1
- [Hi1892] D. Hilbert, *Ueber die Irreducibilität ganzer rationaler Functionen mit ganzzahligen Coefficienten*, J. Reine Angew. Math. 110 (1892), 104–129. doi:10.1515/crll.1892.110.104
- [Mat20] The mathlib Community, *The Lean mathematical library*, in: Proceedings of the 9th ACM SIGPLAN International Conference on Certified Programs and Proofs, CPP 2020, ACM, New York, 2020, 367–381. doi:10.1145/3372885.3373824
- [MU21] L. de Moura and S. Ullrich, *The Lean 4 theorem prover and programming language*, in: Automated Deduction, CADE 28, Lecture Notes in Comput. Sci. 12699, Springer, Cham, 2021, 625–635. doi:10.1007/978-3-030-79876-5_37
- [Sa72] N. Sauer, *On the density of families of sets*, J. Combin. Theory Ser. A 13 (1972), no. 1, 145–147. doi:10.1016/0097-3165(72)90019-2
- [Sh72] S. Shelah, *A combinatorial problem; stability and order for models and theories in infinitary languages*, Pacific J. Math. 41 (1972), no. 1, 247–261. doi:10.2140/pjm.1972.41.247
- [VC71] V. N. Vapnik and A. Ya. Chervonenkis, *On the uniform convergence of relative frequencies of events to their probabilities*, Theory Probab. Appl. 16 (1971), no. 2, 264–280. doi:10.1137/1116025
- [vdW27] B. L. van der Waerden, *Beweis einer Baudetschen Vermutung*, Nieuw Arch. Wisk. 15 (1927), 212–216.

[^1]: The problem page states Howorka’s result without a reference, and we have not found Howorka’s argument in print. Section 6 gives a complete proof, with an explicit bound in terms of van der Waerden numbers.

[^2]: In that setting one works with a function on an abelian group and the vertices of a parallelepiped $x+\omega\cdot h$, and repeated use of the Cauchy–Schwarz inequality compares the average over parallelepipeds with the average of the function. Here the underlying set is a product and the box is a combinatorial one, which is the simplest case of the method.

[^3]: The random ordering $\sigma$ is what turns a single good shape into a positive proportion of all cubes of that shape. Without it the box inequality would still produce a monochromatic cube in every window, but it would say nothing about how many cubes of the same shape are monochromatic, and it is this density that the averaging of Section 4 consumes.

[^4]: Let $N$ be such that every $k$-colouring of the words of length $N$ over the alphabet $\{0,1,\dots,p-1\}$ has a monochromatic combinatorial line, and put $W=N(p-1)+1$. Colour a word by the value of $g$ at the sum of its letters. A combinatorial line has a nonempty set $E$ of active coordinates, which carry the letter $i$ at its $i$-th point, and fixed letters elsewhere, with sum $a$ say. The sums of its points are $a+i|E|$ for $0\leq i\leq p-1$, all less than $W$, so a monochromatic line gives a monochromatic progression with common difference $|E|$.

[^5]: The sets $A_{x}$ are exactly the members of $\mathcal{L}$ other than $B$ that are not the union of two smaller members: $A_{x}$ is not such a union because each of the two parts would have to contain $x$, and by (a) any other member is the union of the sets $A_{x}$ it contains, all of them smaller. Birkhoff’s theorem identifies a finite distributive lattice with the down-sets of the poset of these elements.

[^6]: These axioms are part of the foundations on which Mathlib is built. In particular, no statement relies on an additional axiom or on evaluating code in place of a proof.
