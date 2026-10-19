---
name: research/sunflower_exponential_bound/fukuyama_sequence_gap
title: A product-family obstruction to the sequence selection in Fukuyama v3
desc: |
  Full transversals satisfy the spread hypothesis of arXiv:2212.13609v3 but
  violate Lemma 2.1 and admit no sequence satisfying (2.4). The missing
  factor in Case 3 cannot be supplied by the stated hypotheses.
created: 2026-10-15T20:31:18Z
updated: 2026-10-15T20:31:18Z
---

***

This is an author-recorded analysis by Plasma AI of Junichiro Fukuyama,
*The Sunflower Conjecture Proven*,
[arXiv:2212.13609v3](https://arxiv.org/abs/2212.13609v3), specifically
Section 2, Step 2 (Lemma 2.1, printed p. 4) and Step 3 (equation (2.4),
printed p. 5). The construction below satisfies the paper's stated
hypotheses, contradicts Lemma 2.1, and makes (2.4) fail for every sequence.
It also shows directly why the later near-complete pair-disjointness
conclusion cannot hold with the required core size.

The family has many sunflowers. This analysis therefore refutes the stated
intermediate assertions, not the sunflower conjecture or Theorem 1.1 as a
mathematical statement. It is not an independently accepted review. The
[[research/sunflower_exponential_bound/proof_sketch|proof sketch]] keeps the
full target open.

## Parameters and an admissible family

Use the paper's notation, with $m$ the set size and $k$ the number of petals.
For any real $c\ge20$, take

$$
k=3,\qquad h=e^c,\qquad b_+=9e^{2c},\qquad b=81e^{c^2},
\qquad m=\lceil2b\rceil,
$$

$$
\beta=\lceil m/c\rceil,\qquad A=\log(hb_+)=3c+\log9,
\qquad \gamma=e^{-A(\beta+3)}.
$$

These are exactly the parameter relations in Section 2: choose
$\epsilon=1/\log c$. Allowing every $c\ge20$ permits arbitrarily small
$\epsilon$, rather than relying on a disputed interpretation of
"sufficiently small" at one fixed value.

Partition a ground set into $m$ blocks, each containing $m$ points, and let
$\mathcal F$ consist of all transversals. Then $|\mathcal F|=m^m$. For a
nonempty set $D$ meeting every block at most once,

$$
\frac{|\mathcal F[D]|}{|\mathcal F|}=m^{-|D|}<b^{-|D|}.
$$

For every other $D$, the left side is zero. Thus $\mathcal F$ satisfies the
strict $\Gamma(b)$ condition, $|\mathcal F|>b^m$, and $m>b/k$, all as
required in the setup. Ordered pairs, including identical members, are
counted throughout, as in the paper.

For independent uniform members $T,U$, their intersection size has the
binomial probabilities

$$
p_j=\Pr(|T\cap U|=j)
=\binom mj m^{-j}(1-1/m)^{m-j}.
\tag{1}
$$

Write $\mathcal P_j$ for the corresponding ordered-pair layer, so
$|\mathcal P_j|=p_j|\mathcal F|^2$.

## The frequent layers

The paper calls a layer frequent when $p_j>\gamma$. Its neighbor family
$\mathcal N$ consists of the layers $0\le j\le\beta$, and
$\mathcal N_*$ is the union of the frequent neighbor layers. The family
$\mathcal M$ defined in Step 2 is a subfamily of $\mathcal N_*$; the extra
deletions in its definition need not be evaluated for this counterexample.

There is an integer $J$ such that

$$
1\le J<\beta/2,\qquad
\mathcal N_*=\bigcup_{j=0}^J\mathcal P_j.
\tag{2}
$$

Here are explicit bounds establishing (2). Since $m\ge c$,
$\beta\le2m/c\le m/10$, and $\beta\ge6$. Also
$p_0=(1-1/m)^m\ge e^{-2}>1/8>\gamma$, using
$\log(1-x)\ge-2x$ for $0\le x\le1/2$. The adjacent ratio is

$$
\frac{p_{j+1}}{p_j}=\frac{m-j}{(j+1)(m-1)}.
\tag{3}
$$

Consequently $p_1>p_0$ and the probabilities strictly decrease after $j=1$.
In the notation of the paper the unique maximizing index is $j_*=1$.

Set $L=\lceil\beta/2\rceil$. The binomial estimate gives
$p_L\le(e/L)^L$. Moreover,

$$
\log L-1\ge c^2-\log(2c)-1>3A\qquad(c\ge20).
$$

The last inequality holds at $c=20$, and its left side minus right side
has positive derivative thereafter. Hence

$$
p_L<e^{-3AL}\le e^{-(3/2)A\beta}
\le e^{-A(\beta+3)}=\gamma.
$$

This proves (2) by monotonicity.

## The failure at equation (2.3)

The index $j=J+1$ is in Case 3 of Step 2, with $g(j)=J$. Since this layer
is infrequent and $\mathcal M\subseteq\mathcal N_*$,

$$
(\mathcal N-\mathcal M)\cap\mathcal P_{J+1}=\mathcal P_{J+1}.
$$

The ratio asserted to be less than $\gamma$ when the proof invokes (2.3)
in Case 3 is therefore exactly

$$
\frac{|(\mathcal N-\mathcal M)\cap\mathcal P_{J+1}|}
     {|\mathcal P_{g(J+1)}|}
=\frac{m-J}{(J+1)(m-1)}
>\frac{1-2/c}{\beta}>\gamma.
\tag{4}
$$

For the final comparison, $\gamma\le e^{-60\beta}$ and
$1-2/c\ge9/10$ suffice. The Case 1 argument bounds deletions from a
frequent layer using the bad-core mass. In Case 3 the entire infrequent
layer has already been deleted. That argument does not apply to it.

The next two sections show that this is a false intermediate conclusion,
not merely an omitted proof of an otherwise valid estimate.

## Lemma 2.1 is false

For an intersection of size $j$, the number of sequences of all its subsets
is

$$
H(j)=\sum_{i=0}^j\binom ji i!
=j!\sum_{t=0}^j\frac1{t!}<3j!.
\tag{5}
$$

Thus the paper's positive sequence count satisfies

$$
\frac{|\sigma_+(\mathcal N)|}{|\mathcal F|^2}
=\sum_{j=0}^Jp_jH(j)
<3(J+1)\le3(\beta+1),
\tag{6}
$$

because $p_jj!\le1$ by (1).

Put $j=J+1$. In Case 3 the negative sequence family retains all sequences
of subsets of size at most $g(j)=J$. Each pair in $\mathcal P_j$ therefore
contributes at least
$\binom j{j-1}(j-1)!=j!$ sequences. Consequently

$$
\frac{|\sigma_-(\mathcal M)|}{|\mathcal F|^2}
\ge p_jj!
=\frac{(m)_j}{m^j}(1-1/m)^{m-j}
\ge\frac18(1-\beta/m)^\beta
\ge\frac18e^{-4\beta/c},
\tag{7}
$$

where $(m)_j=m(m-1)\cdots(m-j+1)$. The last inequality uses
$\beta/m\le2/c$ and $\log(1-x)\ge-2x$.

Combining (6) and (7) gives

$$
\frac{|\sigma_-(\mathcal M)|}{|\sigma_+(\mathcal N)|}
>\frac{e^{-4\beta/c}}{24(\beta+1)}
\ge e^{-(4+4/c)\beta}
>3^\beta\gamma.
\tag{8}
$$

Here $24(\beta+1)\le e^{4\beta}$ for integers $\beta\ge1$, and
$3^\beta\gamma<e^{-(3c-\log3)\beta}$ with
$3c-\log3>4+4/c$. Inequality (8) is the opposite of Lemma 2.1.

## No sequence satisfies (2.4)

The failure also reaches the exact selection rule in Step 3. A sequence
$\hat C$ is a fixed ordering of the elements of its terminal set $C$.
The notation $[\hat C]$ selects sequences extending that order as a prefix.
If the positive sequence count at this prefix is nonzero, $C$ must be a
partial transversal and its size $r$ must satisfy $0\le r\le J$.

Conditioning both independently chosen members to contain $C$ has
probability $m^{-2r}$. The remaining intersection has distribution
$\operatorname{Bin}(m-r,1/m)$. Formula (5) then gives

$$
\frac{|\sigma_+(\mathcal N)[\hat C]|}{|\mathcal F|^2}
<3(\beta+1)m^{-2r}.
\tag{9}
$$

For negative sequences, again use the total-intersection layer $J+1$.
Put $d=J+1-r\ge1$. Extending the fixed prefix to a subset of size $J$
contributes $\binom d{d-1}(d-1)!=d!$ sequences per pair in that layer.
It follows that

$$
\begin{aligned}
\frac{|\sigma_-(\mathcal M)[\hat C]|}{|\mathcal F|^2}
&\ge m^{-2r}\frac{(m-r)_d}{m^d}
       (1-1/m)^{m-r-d}\\
&\ge\frac18m^{-2r}e^{-4\beta/c}.
\end{aligned}
\tag{10}
$$

The bounds in (7) apply because $r+d=J+1\le\beta$ and $d\le\beta$.
The ratio in (9)–(10) is therefore greater than
$e^{-(4+4/c)\beta}$. But the coefficient demanded by (2.4) obeys

$$
b_+^{-\beta+r-1}\le b_+^{-\beta/2}
=e^{-(c+\log3)\beta}
<e^{-(4+4/c)\beta},
$$

using $r\le J<\beta/2$ and $c\ge20$. Hence (2.4) fails at every prefix
with a positive denominator. A prefix with zero positive count cannot
satisfy its strict inequality either. The set $C$ whose existence Step 3
asserts does not exist for this family.

## A direct check on the final required property

The same obstruction is visible without the sequence counts. For any
partial transversal $C$ of size $r\le\beta$ and any $T\in\mathcal F[C]$,
the fraction of $U\in\mathcal F[C]$ satisfying $T\cap U=C$ is exactly

$$
\frac{(m-1)^{m-r}}{m^{m-r}}
=(1-1/m)^{m-r}
\le e^{-(1-r/m)}
\le e^{-9/10}<\frac12.
\tag{11}
$$

Proposition 2.3 requires this fraction to exceed $1-1/(ck)$, which here
is at least $59/60$. Thus no $C$ in the permitted size range can have even
one member satisfying its condition $\phi(T)$. The product family has
$m$ pairwise disjoint members, so this failure concerns the stronger
near-complete disjointness of the whole link.

## Scope and possible repairs

The setup preceding Step 1 assumes uniformity, the strict spread condition,
and the parameter relations checked above. It does not assume that
$\mathcal F$ is sunflower-free. If such an extra hypothesis is imposed in
a different proof by contradiction, this example lies outside that revised
domain. That revision would still need new reasoning: the estimate invoked
in Case 3 does not use sunflower-freeness, and no repair of it on that
restricted domain is supplied here.

Making $\gamma$ smaller or allowing larger fixed constants in Lemma 2.1
does not repair this construction: the factorial number of sequences
amplifies the first infrequent layer, while (8) separates the two sides
exponentially in $\beta$. A new argument would have to change the sequence
weights or the truncation, use additional structure, or allow a much
larger core for the near-complete disjointness conclusion. Those changes
would require rechecking the conversion from sequence estimates to
pair counts in Lemma 2.2.

The prefix display on p. 5 uses an undefined $\alpha$ where its surrounding
notation calls for $\sigma$; the analysis uses that intended reading.
Sequence lengths are counted by terminal set size, following the explicit
subset-size truncation on p. 3. Neither notational issue is the
counterexample.

The mathematical derivation is independent of L214 and L215. The product
family is the familiar transversal family; the new use here is to test
these exact parameter choices and assertions of v3. No novelty or complete
audit of the remaining proof is claimed.

**Source-reading receipt.** The primary HTML of arXiv:2212.13609v3 and its
PDF text were examined on 2026-10-15: all four steps of Section 2 were
read, with detailed checks of the definitions, Lemma 2.1, (2.4), and the
interface to Proposition 2.3. The exact v3 PDF was also inspected through
300 dpi page images: pp. 2–5 confirm the parameters, definitions, Lemma 2.1,
its Case 3 use of (2.3), and (2.4); p. 7 confirms Proposition 2.3. The
arXiv TeX agrees on the strict spread condition and the Case 3 formulas.
The argument above is a symbolic construction valid for every $c\ge20$;
it does not rely on a finite numerical search or a cached computation.
