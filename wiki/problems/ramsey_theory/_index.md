---
name: problems/ramsey_theory
title: Ramsey Theory
desc: |
  Ramsey numbers for graphs and hypergraphs, off-diagonal and induced
  variants, and monochromatic structures forced by colorings of the integers
  of Schur and Rado type; Euclidean Ramsey problems and colorings of the
  plane are filed with discrete geometry.
created: 2026-09-04T09:17:27Z
updated: 2026-10-14T01:26:14Z
---

# Ramsey Theory

[[problems/_index|..]]

[[problems/ramsey_theory/E0054/_index|E0054/]]: Asks to improve the Burr–Erdős
bounds on how sparse a Ramsey $2$-complete sequence can be. Conlon, Fox and Pham
determined the order as $(\log N)^2$, closing the gap to a constant factor.

[[problems/ramsey_theory/E0055/_index|E0055/]]: Asks for non-trivial bounds on
how sparse a set $A$ of integers can be if, for a given $r>2$, all large
integers are monochromatic sums of elements of $A$ under every $r$-coloring of
$A$.

[[problems/ramsey_theory/E0076/_index|E0076/]]: Asks whether every $2$-coloring
of the edges of $K_n$ has at least $(1+o(1))n^2/12$ edge-disjoint monochromatic
triangles; yes, by a 2020 theorem of Gruslys and Letzter that erdosproblems.com
accepted.

[[problems/ramsey_theory/E0077/_index|E0077/]]: Asks for the value of
$\lim_{k\to\infty}R(k)^{1/k}$, where $R(k)$ is the Ramsey number of $K_k$; the
limit is not known to exist.

[[problems/ramsey_theory/E0078/_index|E0078/]]: Asks for a constructive proof
that $R(k)>C^k$ for some constant $C>1$, or equivalently for an explicit graph
on $n$ vertices with clique and independence numbers $O(\log n)$.

[[problems/ramsey_theory/E0079/_index|E0079/]]: Asks whether infinitely many
graphs fail to be Ramsey size linear while all their proper subgraphs are Ramsey
size linear. Wigderson proved this in 2024 by a non-constructive argument, and
no explicit example beyond $K_4$ is known.

[[problems/ramsey_theory/E0080/_index|E0080/]]: Asks to estimate $f_c(n)$, the
largest book (an edge in many triangles) forced in an $n$-vertex graph with at
least $cn^2$ edges, each in a triangle. It is open: the question whether
$f_c(n)>n^{\epsilon}$ for some $\epsilon>0$ was answered no, and the question
whether $f_c(n)\gg\log n$ is open.

[[problems/ramsey_theory/E0085/_index|E0085/]]: Asks whether the least minimum
degree $f(n)$ forcing a $C_4$ in an $n$-vertex graph satisfies $f(n+1)\ge f(n)$
for all large $n$. It is open, and the equivalent star Ramsey numbers
$R(C_4,K_{1,n})$ are known exactly only for small $n$ and near prime-power
squares.

[[problems/ramsey_theory/E0087/_index|E0087/]]: Asks whether, for each
$0<\epsilon<1$ and all large $k$, every graph $G$ with $\chi(G)=k$ has
$R(G)>(1-\epsilon)^kR(k)$, or even $R(G)>cR(k)$ for a fixed $c>0$. Erdős's
original conjecture, $R(G)\ge R(k)$, fails at $k=4$.

[[problems/ramsey_theory/E0088/_index|E0088/]]: Asks whether, for some
$\delta=\delta(\epsilon)>0$, every $n$-vertex graph with no clique or
independent set of size $\epsilon\log n$ has an induced subgraph with $m$ edges
for every $m\le\delta n^2$.

[[problems/ramsey_theory/E0112/_index|E0112/]]: Asks to determine $k(n,m)$, the
fewest vertices forcing every directed graph to contain an independent set of
size $n$ or a transitive tournament of size $m$. It is open, with exact values
known when $n=1$ or $m\le2$, when $n=2$ and $m\le6$, and when $m=3$ and $n\le5$.

[[problems/ramsey_theory/E0129/_index|E0129/]]: Asks for a constant $C=C(r)>1$
with $R(n;3,r)<C^{\sqrt n}$, where $R(n;3,r)$ is the least $N$ such that every
$r$-coloring of $K_N$ has $n$ vertices with no triangle in some color. A random
coloring refutes the erdosproblems.com wording, and no source gives another
intended form.

[[problems/ramsey_theory/E0159/_index|E0159/]]: Asks whether $R(C_4,K_n)\ll
n^{2-c}$ for some constant $c>0$.

[[problems/ramsey_theory/E0163/_index|E0163/]]: Asks whether every graph $H$ on
$n$ vertices in which each subgraph has a vertex of degree at most $d$ satisfies
$R(H)\ll_d n$. Lee proved it (2015 preprint, Ann. of Math. 2017), and the
constant is still open.

[[problems/ramsey_theory/E0165/_index|E0165/]]: Asks for an asymptotic formula
for $R(3,k)$. The order $k^2/\log k$ is known, and the constant lies between
$1/2$ and $1$.

[[problems/ramsey_theory/E0166/_index|E0166/]]: Asks to prove that $R(4,k)\gg
k^3/(\log k)^{O(1)}$; proved by Mattheus and Verstraete, with the fourth power
of the logarithm.

[[problems/ramsey_theory/E0172/_index|E0172/]]: Asks whether every finite
coloring of $\mathbb{N}$ has arbitrarily large finite sets $A$ whose sums and
products of distinct elements all have one color.

[[problems/ramsey_theory/E0181/_index|E0181/]]: Asks whether $R(Q_n)\ll 2^n$ for
the $n$-dimensional hypercube graph $Q_n$, which has $2^n$ vertices. It was open
on erdosproblems.com, and a 2026 OpenAI release preprint claims the linear bound
in full.

[[problems/ramsey_theory/E0183/_index|E0183/]]: Asks for
$\lim_{k\to\infty}R(3;k)^{1/k}$, where $R(3;k)$ is the least $n$ such that every
$k$-coloring of the edges of $K_n$ has a monochromatic triangle.

[[problems/ramsey_theory/E0187/_index|E0187/]]: Asks for the best $f(d)$ such
that every $2$-coloring of the integers has, for infinitely many $d$, a
monochromatic arithmetic progression of difference $d$ and length $f(d)$. Beck
(1980) gives $f(d)\le(1+o(1))\log_2 d$, and no usable lower bound is known.

[[problems/ramsey_theory/E0191/_index|E0191/]]: Asks whether, for every $C>0$
and large $n$, every $2$-coloring of the pairs from $\{2,\ldots,n\}$ has a set
$X$ with all its pairs one color and $\sum_{x\in X}1/\log x\ge C$; proved by
Rödl, with the order of growth determined by Conlon, Fox and Sudakov.

[[problems/ramsey_theory/E0439/_index|E0439/]]: Asks whether every finite
coloring of the integers has two distinct integers of one color whose sum is a
square, or a $k$th power. Khalfalah and Szemerédi proved it for the values of
every non-constant polynomial that takes an even value.

[[problems/ramsey_theory/E0483/_index|E0483/]]: Asks for an estimate of the
least $N=f(k)$ such that every $k$-coloring of $\{1,\ldots,N\}$ has a
monochromatic solution of $a+b=c$, and whether $f(k)$ is at most exponential in
$k$. It is open, with $f(k)$ between a constant times $3.28^k$ and
$(e-\frac16)k!$.

[[problems/ramsey_theory/E0484/_index|E0484/]]: Asks whether there is an
absolute constant $c>0$ such that, for $N$ large in terms of $k$, every
$k$-coloring of $\{1,\ldots,N\}$ leaves at least $cN$ of these integers
expressible as a sum of two distinct integers of one color.

[[problems/ramsey_theory/E0518/_index|E0518/]]: Asks whether every two-coloring
of the edges of $K_n$ has $\sqrt{n}$ monochromatic paths, all of one color, that
cover all vertices. It is proved for $n>20^{40}$, and the remaining $n$ are
claimed in an unrefereed 2026 preprint.

[[problems/ramsey_theory/E0531/_index|E0531/]]: Asks for an estimate of the
least $N=F(k)$ such that every two-coloring of $\{1,\ldots,N\}$ has a
$k$-element set whose non-empty subset sums all have the same color.

[[problems/ramsey_theory/E0532/_index|E0532/]]: Asks whether every two-coloring
of $\mathbb{N}$ has an infinite set whose finite non-empty subset sums all have
one color. The answer is yes, by Hindman's theorem, proved in Hindman's 1974
paper and in Baumgartner's 1974 note.

[[problems/ramsey_theory/E0544/_index|E0544/]]: Asks whether the gap
$R(3,k+1)-R(3,k)$ between consecutive Ramsey numbers of a triangle against a
complete graph tends to infinity, and whether it is $o(k)$. Both are open, and
the gap is known only to lie between $3$ and $k+1$.

[[problems/ramsey_theory/E0545/_index|E0545/]]: Asks whether, for all large $m$,
the graph with $m$ edges that is as complete as possible has the largest Ramsey
number among graphs with $m$ edges and no isolated vertices; open. The
erdosproblems.com wording, for every $m$, fails at two edges.

[[problems/ramsey_theory/E0546/_index|E0546/]]: Asks whether
$R(G)\le2^{O(\sqrt{m})}$ for every graph $G$ with $m$ edges and no isolated
vertices.

[[problems/ramsey_theory/E0547/_index|E0547/]]: Asks whether every tree $T$ on
$n\ge2$ vertices has $R(T)\le2n-2$; proved in 2026, on the evidence of a third
party's Lean proof that was built here. The erdosproblems.com wording also
covers the one-vertex tree, where it fails.

[[problems/ramsey_theory/E0549/_index|E0549/]]: Asks whether every tree $T$ with
$k$ vertices in one class and $2k$ in the other has $R(T)=4k-1$.

[[problems/ramsey_theory/E0550/_index|E0550/]]: Asks for a proof that, for large
$n$, every tree $T$ on $n$ vertices and the complete multipartite graph $G$ with
class sizes $m_1\le\cdots\le m_k$ satisfy
$R(T,G)\le(\chi(G)-1)(R(T,K_{m_1,m_2})-1)+m_1$.

[[problems/ramsey_theory/E0551/_index|E0551/]]: Asks for a proof that
$R(C_k,K_n)=(k-1)(n-1)+1$ for $k\ge n\ge3$, except when $n=k=3$.

[[problems/ramsey_theory/E0552/_index|E0552/]]: Asks for the Ramsey number
$R(C_4,S_n)$ of a four-cycle against the star with $n$ edges, and whether, for
every $c>0$, infinitely many $n$ have $R(C_4,S_n)\le n+\sqrt{n}-c$.

[[problems/ramsey_theory/E0553/_index|E0553/]]: Asks for a proof that
$R(3,3,n)/R(3,n)\to\infty$, where $R(3,3,n)$ is the three-color Ramsey number
for two triangles and $K_n$ and $R(3,n)$ is the two-color one.

[[problems/ramsey_theory/E0554/_index|E0554/]]: Asks for a proof that
$R_k(C_{2n+1})/R_k(K_3)\to0$ as $k\to\infty$ for every $n\ge2$, where $R_k$ is
the $k$-color Ramsey number.

[[problems/ramsey_theory/E0555/_index|E0555/]]: Asks for the $k$-color Ramsey
number $R_k(C_{2n})$ of the even cycle on $2n$ vertices.

[[problems/ramsey_theory/E0556/_index|E0556/]]: Asks whether, for every $n>3$,
every 3-coloring of the edges of $K_{4n-3}$ has a monochromatic cycle of length
$n$; the bound is known for all large $n$. The erdosproblems.com wording also
includes the triangle, where it fails.

[[problems/ramsey_theory/E0557/_index|E0557/]]: Asks whether $R_k(T)\le kn+O(1)$
for every tree $T$ on $n$ vertices, where $R_k$ is the $k$-color Ramsey number.

[[problems/ramsey_theory/E0558/_index|E0558/]]: Asks for the $k$-color Ramsey
number $R_k(K_{s,t})$ of the complete bipartite graph with $s$ vertices in one
class and $t$ in the other.

[[problems/ramsey_theory/E0559/_index|E0559/]]: Asks whether every graph $G$ on
$n$ vertices with maximum degree $d$ has size Ramsey number $\hat{R}(G)\ll_d n$.
It is false already for maximum degree $3$.

[[problems/ramsey_theory/E0560/_index|E0560/]]: Asks for the size Ramsey number
of $K_{n,n}$, the complete bipartite graph with $n$ vertices on each side; its
order is known to lie between $n^22^n$ and $n^32^n$.

[[problems/ramsey_theory/E0561/_index|E0561/]]: Asks for a proof of the 1978
formula $\hat{R}(F_1,F_2)=\sum_{2\le k\le s+t}l_k$, with
$l_k=\max\{n_i+m_j-1:i+j=k\}$, for the star forests $F_1=\bigcup_{i\le
s}K_{1,n_i}$ and $F_2=\bigcup_{j\le t}K_{1,m_j}$ with stars in decreasing order
of size; proved in special cases only.

[[problems/ramsey_theory/E0562/_index|E0562/]]: Asks for a proof that
$\log_{r-1}R_r(n)\asymp_r n$ for $r\ge3$, where $R_r(n)$ is the two-color Ramsey
number of the complete $r$-uniform hypergraph on $n$ vertices and $\log_{r-1}$
is the $(r-1)$-fold iterated logarithm.

[[problems/ramsey_theory/E0563/_index|E0563/]]: Asks for a proof that
$F(n,\alpha)\sim c_\alpha\log n$ for each $0\le\alpha<1/2$, where $F(n,\alpha)$
is the least $m$ such that some two-coloring of $K_n$ gives every set $X$ of at
least $m$ vertices more than $\alpha\binom{|X|}{2}$ edges of each color.

[[problems/ramsey_theory/E0564/_index|E0564/]]: Asks whether
$R_3(n)\ge2^{2^{cn}}$ for some $c>0$, where $R_3(n)$ is the two-color Ramsey
number of the complete $3$-uniform hypergraph on $n$ vertices.

[[problems/ramsey_theory/E0565/_index|E0565/]]: Asks whether $R^*(G)\le2^{O(n)}$
for every graph $G$ on $n$ vertices, where the induced Ramsey number $R^*(G)$ is
the fewest vertices of a graph in which every two-coloring of the edges gives an
induced monochromatic copy of $G$.

[[problems/ramsey_theory/E0566/_index|E0566/]]: Asks whether every graph whose
subgraphs on $k\ge2$ vertices have at most $2k-3$ edges is Ramsey size linear;
open. This corrects the erdosproblems.com wording, which no graph meets, since a
one-vertex subgraph exceeds the bound.

[[problems/ramsey_theory/E0567/_index|E0567/]]: Asks whether each of the cube
$Q_3$, the graph $K_{3,3}$ and the graph $H_5$ ($K_4$ with one edge subdivided)
is Ramsey size linear; open, with partial results.

[[problems/ramsey_theory/E0568/_index|E0568/]]: Asks whether every graph $G$
with $R(G,T_n)\ll n$ for all trees $T_n$ on $n$ vertices and $R(G,K_n)\ll n^2$
satisfies $R(G,H)\ll m$ for every graph $H$ with $m$ edges and no isolated
vertices.

[[problems/ramsey_theory/E0569/_index|E0569/]]: Asks for the least constant
$c_k$ such that $R(C_{2k+1},H)\le c_km$ for every graph $H$ with $m$ edges and
no isolated vertices.

[[problems/ramsey_theory/E0570/_index|E0570/]]: Asks whether, for each $k\ge3$
and all sufficiently large $m$, every graph $H$ with $m$ edges and no isolated
vertices has $R(C_k,H)\le 2m+\lfloor(k-1)/2\rfloor$.

[[problems/ramsey_theory/E0582/_index|E0582/]]: Asks whether some $K_4$-free
graph has a monochromatic triangle in every 2-coloring of its edges.

[[problems/ramsey_theory/E0609/_index|E0609/]]: Asks for estimates of the least
$m$ such that every $n$-coloring of the edges of $K_{2^n+1}$ has a monochromatic
odd cycle of length at most $m$.

[[problems/ramsey_theory/E0613/_index|E0613/]]: Asks whether every graph with
one edge fewer than a conjectured size Ramsey number is the union of a bipartite
graph and a graph of maximum degree below $n$. Disproved for every $n\ge5$ by
Pikhurko's constructions.

[[problems/ramsey_theory/E0615/_index|E0615/]]: Asks whether, for some constant
$c>0$, every graph on $n$ vertices with at least $(1/8-c)n^2$ edges contains a
$K_4$ or an independent set of $n/\log n$ vertices. Disproved by Fox, Loh and
Zhao.

[[problems/ramsey_theory/E0636/_index|E0636/]]: Asks whether a graph on $n$
vertices with no large clique or independent set has many induced subgraphs that
pairwise differ in vertex count or edge count.

[[problems/ramsey_theory/E0637/_index|E0637/]]: Asks whether a graph on $n$
vertices with no large clique or independent set has an induced subgraph on many
vertices with many distinct degrees.

[[problems/ramsey_theory/E0638/_index|E0638/]]: Asks whether a family of finite
graphs closed under subgraphs, with members forcing a monochromatic triangle
under each finite number of colors, must contain all finite subgraphs of some
graph forcing one under $\aleph$ colors, for every infinite cardinal $\aleph$. A
disproof is claimed.

[[problems/ramsey_theory/E0639/_index|E0639/]]: Asks whether, for large $n$,
every 2-coloring of the edges of $K_n$ leaves at most $n^2/4$ edges in no
monochromatic triangle, as Erdős stated it. Proved by Keevash and Sudakov's
exact theorem, though the erdosproblems.com wording fails for $3\le n\le6$.

[[problems/ramsey_theory/E0645/_index|E0645/]]: Asks whether every 2-coloring of
the positive integers has a monochromatic progression $x,x+d,x+2d$ with $d>x$.
Proved by Brown and Landman in 1999, and erdosproblems.com also records an
elementary argument.

[[problems/ramsey_theory/E0667/_index|E0667/]]: Asks whether $c(p,q)$, the
growth exponent of the largest clique forced when every $p$ vertices span at
least $q$ edges, is strictly increasing in $q$. Open; the 1997 source gives
bounds at the endpoints and a disputed upper bound near the top.

[[problems/ramsey_theory/E0720/_index|E0720/]]: Asks whether the size Ramsey
number of the path $P_n$ grows faster than $n$ but slower than $n^2$, and
whether that of the cycle $C_n$ is $o(n^2)$. Both are linear, so the first
answer is no and the other two are yes.

[[problems/ramsey_theory/E0721/_index|E0721/]]: Asks for bounds on $W(3,k)$, the
least $n$ such that every red/blue coloring of $\{1,\ldots,n\}$ has a red 3-term
progression or a blue $k$-term one. Green, Hunter and Schoen meet the two
explicit challenges, but the order of magnitude remains open.

[[problems/ramsey_theory/E0800/_index|E0800/]]: Asks whether every graph $G$ on
$n$ vertices with no two adjacent vertices both of degree at least 3 has $R(G)$
at most an absolute constant times $n$.

[[problems/ramsey_theory/E0801/_index|E0801/]]: Asks whether every graph on $n$
vertices with no independent set of more than $\sqrt n$ vertices has a set of at
most $\sqrt n$ vertices spanning $\gg\sqrt n\log n$ edges.

[[problems/ramsey_theory/E0809/_index|E0809/]]: Asks whether, for every $k\ge3$,
the fewest colors that make every $C_{2k+1}$ rainbow in some $n$-vertex graph
with $\lfloor n^2/4\rfloor+1$ edges is asymptotically $n^2/8$. Proved by two
Lean developments built and audited here: Asad Shahab's, filed first, and the
project's claim L17.

[[problems/ramsey_theory/E0810/_index|E0810/]]: Asks whether there is an
$\epsilon>0$ such that, for all large $n$, some graph on $n$ vertices with at
least $\epsilon n^2$ edges can be edge-colored with $n$ colors so that every
$C_4$ gets four distinct colors.

[[problems/ramsey_theory/E0811/_index|E0811/]]: Asks for which graphs $G$ every
balanced coloring of a large $K_n$ with $e(G)$ colors, in which each vertex sees
equally many edges of every color, contains a rainbow copy of $G$.

[[problems/ramsey_theory/E0812/_index|E0812/]]: Asks whether consecutive
diagonal Ramsey numbers satisfy $R(n+1)/R(n)\ge1+c$ for a constant $c>0$, and
whether $R(n+1)-R(n)\gg n^2$.

[[problems/ramsey_theory/E0894/_index|E0894/]]: Asks whether, for a lacunary
sequence $A$, the integers can be finitely colored so that no two numbers of the
same color differ by an element of $A$. Proved, and Peres and Schlag's bound of
order $\epsilon^{-1}\log(1/\epsilon)$ colors is the best known.

[[problems/ramsey_theory/E0911/_index|E0911/]]: Asks whether the size Ramsey
number of every graph with $n$ vertices and $e\ge Cn$ edges exceeds $f(C)e$ for
some $f$ growing faster than linearly. Open, with no result found beyond Erdős's
1982 statement.

[[problems/ramsey_theory/E0924/_index|E0924/]]: Asks whether, for $k\ge2$ and
$l\ge3$, some $K_{l+1}$-free graph has a monochromatic $K_l$ in every
$k$-coloring of its edges. True, by Folkman for two colors and by Nešetřil and
Rödl for every $k$.

[[problems/ramsey_theory/E0925/_index|E0925/]]: Asks whether every $n$-vertex
graph whose edges can be 2-colored with no monochromatic triangle has an
independent set of size $\gg n^{1/3+\delta}$ for some fixed $\delta>0$.
Disproved through the Alon–Rödl bound on $R(3,3,m)$.

[[problems/ramsey_theory/E0948/_index|E0948/]]: Asks whether there are $f$ and
$k$ such that every $k$-coloring of the integers has a sequence $a_1<a_2<\cdots$
with $a_n<f(n)$ for infinitely many $n$ whose finite subset sums miss a color.
No, by a 2026 AI-generated coloring that erdosproblems.com accepted after
review.

[[problems/ramsey_theory/E0949/_index|E0949/]]: Asks whether the complement of
every sum-free set $S\subseteq\mathbb R$ contains a set $A$ of size continuum
with $A+A$ also outside $S$. Open, with AlphaProof's Lean proof of the Sidon
case pending as a claim and a thread comment arguing the Baire case.

[[problems/ramsey_theory/E0965/_index|E0965/]]: Asks whether every 2-coloring of
$\mathbb R$ admits a set of size $\aleph_1$ whose sums of two distinct elements
all have one color. False in ZFC, by Komjáth and by Soukup and Weiss, after
Hindman, Leader and Strauss showed it false under CH.

[[problems/ramsey_theory/E0966/_index|E0966/]]: Asks whether, for $k,r\ge2$,
some set $A\subseteq\mathbb N$ with no $(k+1)$-term arithmetic progression has a
monochromatic $k$-term one in every $r$-coloring. True, by Spencer's 1975
restricted van der Waerden theorem.

[[problems/ramsey_theory/E0986/_index|E0986/]]: Asks whether, for each fixed
$s\ge3$, $R(s,k)\gg k^{s-1}/(\log k)^c$ for some constant $c=c(s)>0$.

[[problems/ramsey_theory/E1014/_index|E1014/]]: Asks whether, for each fixed
$k$, the ratio $R(k,l+1)/R(k,l)$ of consecutive off-diagonal Ramsey numbers
tends to $1$. Answered yes by a 2026 manuscript hosted by OpenAI, attributed to
an internal model and accepted by erdosproblems.com.

[[problems/ramsey_theory/E1015/_index|E1015/]]: Asks for the largest number of
vertices that a two-colored complete graph can force to be left over when it is
covered by disjoint monochromatic copies of $K_t$. Burr, Erdős and Spencer
determined it for fixed $t$ and large $n$ in terms of $R(t,t-1)$, so it grows
exponentially.

[[problems/ramsey_theory/E1029/_index|E1029/]]: Asks whether
$R(k)/(k2^{k/2})\to\infty$, where $R(k)$ is the Ramsey number of the complete
graph $K_k$.

[[problems/ramsey_theory/E1030/_index|E1030/]]: Asks whether the off-diagonal
Ramsey number $R(k+1,k)$ exceeds the diagonal number $R(k,k)$ by a constant
factor in the limit.

[[problems/ramsey_theory/E1105/_index|E1105/]]: Asks for the anti-Ramsey numbers
of cycles and paths, the most colors on the edges of $K_n$ without a rainbow
copy. It proposes an asymptotic formula for cycles and an exact formula for
paths.

[[problems/ramsey_theory/E1182/_index|E1182/]]: Asks to estimate the largest
edge counts of connected graphs $G$ on $n$ vertices with $R(K_3,G)=2n-1$. A 1996
preprint claims a linear threshold for all such graphs, a negative answer to the
closing question.

[[problems/ramsey_theory/E1183/_index|E1183/]]: Asks to estimate the size of the
largest monochromatic family closed under unions and intersections that every
two-coloring of the subsets of $\{1,\ldots,n\}$ must contain. It is open, and
nothing beyond the trivial chain bound is proved.

[[problems/ramsey_theory/E1198/_index|E1198/]]: Asks whether every two-coloring
of $\mathbb{N}$ admits an infinite set all of whose sums of products of distinct
members share one color. The answer is no, by a 1995 theorem of Smith, as the
erdosproblems.com thread deduced in 2026.

[[problems/ramsey_theory/E1199/_index|E1199/]]: Asks whether every two-coloring
of $\mathbb{N}$ admits an infinite set whose pairwise sums, doubles included,
share one color (Owings's question). erdosproblems.com listed it as open, the
analogue for three colors is false, and a proof for two colors is claimed.

[[problems/ramsey_theory/E1211/_index|E1211/]]: Asks how large the larger upper
logarithmic density of the two subset-sum sets must be when $\mathbb{N}$ is
split into two classes. Conlon, Fox and Pham showed that the minimum is
$(2+\sqrt3)/4$.

[[problems/ramsey_theory/E1216/_index|E1216/]]: Asks whether the largest
transitive subtournament that every tournament on $n$ vertices must contain has
$\lfloor\log_2 n\rfloor+1$ vertices. This first fails at $n=14$ and fails for
infinitely many $n$, and the exact value is known for $n\le33$ and $47\le
n\le56$.

***

Ramsey numbers for graphs and hypergraphs, off-diagonal and induced variants,
and monochromatic structures forced by colorings of the integers of Schur and
Rado type; Euclidean Ramsey problems and colorings of the plane are filed with
discrete geometry.

erdosproblems.com tags routed here: additive combinatorics, arithmetic
progressions, combinatorics, graph theory, hypergraphs, number theory, ramsey,
ramsey theory.
