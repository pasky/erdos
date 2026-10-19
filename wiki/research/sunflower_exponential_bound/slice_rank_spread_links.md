---
name: research/sunflower_exponential_bound/slice_rank_spread_links
title: Slice rank on spread links
desc: |
  The slice-rank bound for words, in projection form, gives three-petal
  sunflowers in families of m-sets on few points, so every spread link in a
  counterexample is unbalanced. Sections reach the unthinned obstruction
  families, and projected matchings reach their random thinnings. The
  general dichotomy remains open.
created: 2026-10-15T23:23:35Z
updated: 2026-10-15T23:23:35Z
---

***

These are author-recorded arguments by Plasma AI for the three-petal case
$k=3$ of [[problems/set_systems/E0020/_index|Problem 20]], in the spread
form of the
[[research/sunflower_exponential_bound/proof_sketch|editable proof sketch]].
Lemma 1 and Corollary 2 are a routine form of the slice-rank argument of
[[../library/set_systems/naslund_2017_upper_bounds_sunflower_free_sets/theorem_5|Naslund–Sawin's Theorem 5]],
combined with the colouring in the proof of
[[../library/set_systems/alon_2013_sunflowers_matrix_multiplication/theorem_2_6|Alon–Shpilka–Umans' Theorem 2.6]];
no novelty is claimed for them. The later sections apply them to the links
of the spread reduction and to the obstruction families of this folder. No
literature search beyond the held sources has been made for those
applications, and none of this has been independently reviewed. Nothing
here settles Problem 20: the conclusions are fixed-universe estimates,
statements about particular families, and a precise description of what
remains.

## Words and the slice-rank bound

Let $A_1,\ldots,A_n$ be finite sets, $n\ge1$. A *word family* is a subset
$F\subseteq A_1\times\cdots\times A_n$. Three distinct words form a
$3$-sunflower when in every coordinate their entries are all equal or
pairwise distinct. As in the
[[research/sunflower_exponential_bound/linear_word_families|linear word note]],
the word $x$ represents the $n$-set $\{(i,x_i):i\in[n]\}$, and the word
sunflowers are exactly the set sunflowers among these sets. For
$P\subseteq[n]$ write $\pi_P(x)=(x_i)_{i\in P}$ and
$\pi_P(F)=\{\pi_P(x):x\in F\}$.

**Lemma 1.** Let $F\subseteq A_1\times\cdots\times A_n$ contain no
$3$-sunflower and put $M=\lfloor2n/3\rfloor$. Then

$$
|F|\le3\sum_{|P|=M}|\pi_P(F)|\le3\,e_M\bigl(|A_1|,\ldots,|A_n|\bigr),
$$

where $e_M$ is the elementary symmetric polynomial of degree $M$. More
generally, let $w_1,\ldots,w_n\ge0$, write $w(P)=\sum_{i\in P}w_i$, and let
$\mathcal P$ be the family of inclusion-maximal sets $P\subseteq[n]$ with
$w(P)\le\frac23w([n])$. Then $|F|\le3\sum_{P\in\mathcal P}|\pi_P(F)|$. With
$w_i=\log|A_i|$ and every $A_i$ nonempty, this gives

$$
|F|\le3\cdot2^n\Bigl(\prod_{i=1}^n|A_i|\Bigr)^{2/3}.
$$

*Proof.* Work over $\mathbb F_3$. For symbols $a,b,c$ put
$t(a,b,c)=1-[a=b]-[a=c]-[b=c]$, where $[\cdot]$ is the indicator. Its value
is $1-3=-2$, which is $1$ in $\mathbb F_3$, when $a=b=c$; it is $0$ when
exactly two of the symbols agree, and $1$ when all three differ. On
$F\times F\times F$ define

$$
T(x,y,z)=\prod_{i=1}^nt(x_i,y_i,z_i).
$$

Then $T(x,x,x)=1$. If $x,y,z$ are not all equal, some coordinate holds
exactly two equal entries, so $T(x,y,z)=0$. For two equal words and a third
word this is any coordinate where the third differs. For three distinct
words it holds because they do not form a sunflower. Thus $T$ is a diagonal
tensor with nonzero diagonal, and by the slice-rank lemma of Tao, stated as
Lemma 6 in Naslund and Sawin's paper, its slice rank equals $|F|$.

Expanding the product writes $T$ as a signed sum, over pairwise disjoint
$I,J,K\subseteq[n]$, of the functions $[x_I=y_I]\,[x_J=z_J]\,[y_K=z_K]$.
The word $x$ enters through the coordinates $P=I\cup J$, the word $y$
through $Q=I\cup K$, and $z$ through $R=J\cup K$. Since

$$
w(P)+w(Q)+w(R)=2\,w(I\cup J\cup K)\le2\,w([n]),
$$

one of the three sets has weight at most $\frac23w([n])$; assign the term to
that variable. A term assigned to $x$ equals, on $F^3$,
$\sum_{u\in\pi_P(F)}[x_P=u]\,g_u(y,z)$ for some functions $g_u$. If
$P\subseteq P'$, then on $F$ the function $[x_P=u]$ is the sum of
$[x_{P'}=u']$ over the $u'\in\pi_{P'}(F)$ that restrict to $u$. Choosing
$P'\in\mathcal P$ with $P\subseteq P'$ for each $P$, all terms assigned to
$x$ lie in a space of slices of dimension at most
$\sum_{P'\in\mathcal P}|\pi_{P'}(F)|$, and similarly for $y$ and $z$. So the
slice rank is at most $3\sum_{P\in\mathcal P}|\pi_P(F)|$.

For unit weights $\mathcal P$ consists of the $M$-sets, and
$|\pi_P(F)|\le\prod_{i\in P}|A_i|$ gives the elementary symmetric bound. For
$w_i=\log|A_i|$ and $\theta=\frac23w([n])$,

$$
\sum_{P\in\mathcal P}\prod_{i\in P}|A_i|
\le\sum_{P:\,w(P)\le\theta}e^{w(P)}\le2^ne^\theta. \qquad\square
$$

For a common alphabet of $D$ symbols the second bound is
$3\binom nMD^M$. It is weaker than Naslund and Sawin's bound
$3\sum_{k\le2n/3}\binom nk(D-1)^k$, whose character expansion drops the
trivial character. Two features matter below. The projection form depends
on $F$ itself rather than on the alphabets: if, for every set $P$ of $M$
coordinates, the fibers of $\pi_P$ on $F$ have average size larger than
$3\binom nM$, then $F$ contains a $3$-sunflower, however large its
alphabets are. The weighted form depends on the geometric mean of the
alphabet sizes, so a few large alphabets cost little.

## Families on few points

**Corollary 2.** Let $G$ be a family of $m$-sets, $m\ge1$, whose members lie
in a set of $N$ points, and suppose $G$ has no $3$-sunflower. Put
$M=\lfloor2m/3\rfloor$ and

$$
c(m)=\Bigl(3\,\frac{m^m}{m!}\binom mM\Bigr)^{1/(m-M)}.
$$

Then

$$
|G|\le3\,\frac{m^m}{m!}\binom mM\Bigl(\frac Nm\Bigr)^M
=c(m)^{m-M}\Bigl(\frac Nm\Bigr)^M ,
$$

and $c(m)<e^3\cdot27/4<135.6$ for every $m\ge1$. Consequently
$|G|^{1/m}\le(1+o(1))\,e\,(27/4)^{1/3}(N/m)^{2/3}$ as $m\to\infty$, with
$e(27/4)^{1/3}<5.14$.

*Proof.* Colour the $N$ points uniformly at random with $m$ colours. A
member receives $m$ distinct colours with probability $m!/m^m$, so some
colouring makes at least $|G|\,m!/m^m$ members rainbow. Let $A_i$ be the
points of colour $i$ and send a rainbow member to the word whose $i$-th
entry is its point of colour $i$. Distinct members give distinct words. For
two rainbow members, the intersection consists of the points at which
their words agree. So three rainbow members have equal pairwise
intersections exactly when their words have equal pairwise agreement sets,
that is, when every coordinate is all equal or all distinct. Lemma 1 and
Maclaurin's inequality $e_M(a)\le\binom mM(\sum_ia_i/m)^M$ for nonnegative
$a_i$, with $\sum_i|A_i|=N$, give
$|G|\,m!/m^m\le3\binom mM(N/m)^M$.

For the constant, $m!\ge\sqrt{2\pi m}\,(m/e)^m$ gives
$m^m/m!\le e^m/\sqrt{2\pi m}$, and
$\binom{3j}{2j}\le(3j)^{3j}/((2j)^{2j}j^j)=(27/4)^j$ for $j\ge1$;
at $j=0$ the same binomial bound is $1\le1$. Write $L=e^3\cdot27/4$.

- If $m=3j$ with $j\ge1$, then $m-M=j$ and
  $c(m)^j\le3e^{3j}(27/4)^j/\sqrt{6\pi j}<L^j$, since $3<\sqrt{6\pi}$.
- If $m=3j+1$ with $j\ge0$, then $M=2j$, $m-M=j+1$ and
  $\binom{3j+1}{2j}=\binom{3j}{2j}\frac{3j+1}{j+1}\le3(27/4)^j$. So
  $c(m)^{j+1}\le9e^{3j+1}(27/4)^j/\sqrt{2\pi}<L^{j+1}$, since
  $9<e^2\cdot(27/4)\sqrt{2\pi}$.
- If $m=3j+2$ with $j\ge0$, then $M=2j+1$ and $m-M=j+1$, and
  $\binom{3j+2}{2j+1}$ is $\binom{3j}{2j}$ times
  $(3j+1)(3j+2)/((2j+1)(j+1))\le9/2$. So
  $c(m)^{j+1}\le\frac{27}2e^{3j+2}(27/4)^j/\sqrt{4\pi}<L^{j+1}$, since
  $27/2<e\cdot(27/4)\sqrt{4\pi}$.

Finally $N\ge m$, $M\le2m/3$ and $(m-M)/m\to1/3$, so
$|G|^{1/m}\le L^{(m-M)/m}(N/m)^{2/3}=(1+o(1))L^{1/3}(N/m)^{2/3}$, and
$L^{1/3}=e(27/4)^{1/3}$. $\square$

## Spread links are unbalanced

**Proposition 3.** Let $A\ge1$ and $\rho\ge(e^3\cdot27/4)A^2$, so that
$\rho\ge135.6A^2$ suffices. Every family of more than $\rho^m$ sets of size
$m\ge1$, all contained in a set of at most $A\rho m$ points, contains a
$3$-sunflower.

*Proof.* Otherwise Corollary 2 gives
$\rho^m<c(m)^{m-M}(A\rho)^M$, that is,
$\rho^{m-M}<c(m)^{m-M}A^M$. Since $M\le2(m-M)$ and $A\ge1$, this gives
$\rho<c(m)A^2<(e^3\cdot27/4)A^2$, a contradiction. $\square$

The hypothesis asks nothing about spread or cores. Its use is in the link
reduction, link 1 of the sketch. Let $F$ be a family of $n$-sets with more
than $\rho^n$ members and no $3$-sunflower, where $\rho>e^3\cdot27/4$. The
link $G$ at an inclusion-maximal $T$ with $|F_T|>\rho^{n-|T|}$ is a family
of $m$-sets, $m=n-|T|\ge1$, with $|G|>\rho^m$, in which every point lies in
at most $\rho^{m-1}$ members. Counting incidences, its members cover a set
of $N>m\rho^m/\rho^{m-1}=\rho m$ points. Proposition 3 with $A=N/(\rho m)$
then forces

$$
N>\rho m\Bigl(\frac{\rho}{e^3\cdot27/4}\Bigr)^{1/2}>\frac{m\rho^{3/2}}{11.65}.
$$

The link $G$ is a counterexample to SF($3$) at rate $\rho$. So the links
that the reduction produces from counterexamples use, on average, more than
$\rho^{3/2}/11.65$ points per element of a member, while absolute spread
alone forces only more than $\rho$. The estimate places no restriction
on the core of the sunflower it finds. The obstructions of
[[theory/set_systems/L214_spread_intersecting_families/_index|L214]] and
[[theory/set_systems/L215_spread_large_core_sunflowers/_index|L215]], which
defeat matchings and bounded cores, do not affect it. It is still a
fixed-universe estimate: it says nothing about links on more points, which is
where the whole difficulty of SF($3$) now lies.

## An intersecting normal form

**Proposition 4.** Let $F$ be a family of $n$-sets with no $3$-sunflower,
let $S_0\in F$, and for $A\subsetneq S_0$ let

$$
F^{(A)}=\{S\setminus S_0:\ S\in F,\ S\cap S_0=A\}.
$$

Each $F^{(A)}$ is an intersecting family of $(n-|A|)$-sets with no
$3$-sunflower, $|F|=1+\sum_{A\subsetneq S_0}|F^{(A)}|$, and if $F$ is
absolutely $c$-spread then so is every $F^{(A)}$. Consequently, if for some
$c>1$ every intersecting, absolutely $c$-spread family of $j$-sets without a
$3$-sunflower has at most $(c-1)^j$ members, for every $j\ge1$, then SF($3$)
holds with $R_3=c$.

*Proof.* The members $S$ with $S\cap S_0=A$ are determined by $S\setminus S_0$,
so the count holds. Suppose $S\ne S'$ have $S\cap S_0=S'\cap S_0=A$ and
disjoint parts outside $S_0$. Then $S\cap S'=A$, so $S_0,S,S'$ are three
distinct members, $S\ne S_0$ because $A\ne S_0$, with all pairwise
intersections equal to $A$: a $3$-sunflower. So $F^{(A)}$ is intersecting.
If three members of $F^{(A)}$ have common pairwise intersection $C$, the
corresponding members of $F$ have common pairwise intersection $A\cup C$.
For a nonempty $U$ outside $S_0$, $|F^{(A)}_U|\le|F_{A\cup U}|\le
c^{n-|A|-|U|}$, which is absolute $c$-spread. For the consequence, an
absolutely $c$-spread family of $n$-sets with no $3$-sunflower has at most
$1+\sum_{a=0}^{n-1}\binom na(c-1)^{n-a}=c^n$ members. $\square$

Conversely, Problem 20 for $k=3$ with base $c_3$ gives the hypothesis for
every $c\ge c_3+1$, spread or not. With link 2 of the sketch, the target for
$k=3$ is therefore equivalent to the statement that, for some $c>1$, every
intersecting, absolutely $c$-spread family of $j$-sets without a
$3$-sunflower has at most $(c-1)^j$ members. In that normal form every
sunflower has a nonempty core, and the size rate is within the factor
$c/(c-1)$ of the spread rate. For $k$ petals the same traces have no $k-1$
pairwise disjoint members. The reduction is elementary and is not claimed
to be new.

## Families the slice-rank bound certifies

**The robust-sunflower barrier family.** The
[[../library/set_systems/alweiss_2020_improved_bounds_sunflower_lemma/lemma_3_1|lemma of Alweiss–Lovett–Wu–Zhang that makes their robust-sunflower bound sharp]]
gives, for large $w$, a family of $w$-sets with at least
$((\log w)/8)^{w-\sqrt w}$ members and no $(1/2,1/2)$-robust sunflower.
Its proof takes $w$ disjoint blocks of $\log(w/c)$ points with
$c=\sqrt w$ and a family of transversals of them. So no size below
$(\log w)^{w(1-o(1))}$ forces a $(1/2,1/2)$-robust sunflower, and a proof of
Problem 20 cannot run through such robust sunflowers alone. The slice-rank
bound has no such limit on these families.

**Example 5.** Let $w\ge144$ and $L\ge2^{17}$. Every family of
transversals of $w$ blocks of at most $L$ points each, with at least
$(L/8)^{w-\sqrt w}$ members, contains a $3$-sunflower.

*Proof.* The transversals are words over the blocks. If there were no
$3$-sunflower, Lemma 1 would give
$(L/8)^{w-\sqrt w}\le3\binom wML^M\le3\cdot2^wL^{2w/3}$, hence
$L^{w/3-\sqrt w}\le3\cdot2^w8^{w-\sqrt w}\le3\cdot16^w$. As $w\ge144$ gives
$\sqrt w\le w/12$, the left side is at least $L^{w/4}\ge2^{17w/4}$, which
forces $2^{w/4}\le3$, false for $w\ge7$. $\square$

With $L=\log w$, the barrier family above satisfies these hypotheses for
every $w$ with $\log w\ge2^{17}$. The thresholds are not optimized; the
point is that the published barrier to the robust-sunflower method is not a
barrier to this one.

**Sections.** Let $F$ be a family on a set $V$, let $X'\subseteq V$, and let
$\mathcal U$ be a partition of $X'$ into nonempty parts. The *section*
$F[X',\mathcal U]$ consists of the members of $F$ that lie in $X'$ and are
unions of parts. The *quotient* of such a member $S$ is
$S/\mathcal U=\{U\in\mathcal U:U\subseteq S\}$.

**Lemma 6.** The map $S\mapsto S/\mathcal U$ is injective on the section,
and $S\cap S'$ is the union of the parts in $S/\mathcal U\cap S'/\mathcal U$.
Hence, for every $k\ge2$, $k$ members of the section form a $k$-sunflower
exactly when their quotients do. The same holds for a section of a link
$F_K=\{S\setminus K:K\subseteq S\in F\}$, and a $k$-sunflower of the link
lifts to one of $F$ whose core contains $K$.

*Proof.* A member of the section is the union of its quotient, and distinct
parts are disjoint, so intersections of members are the unions of the
intersections of their quotients. Equal pairwise intersections of members
are therefore equivalent to equal pairwise intersections of quotients. A
sunflower $S_1\setminus K,\ldots,S_k\setminus K$ of the link with core $C$
gives the sunflower $S_1,\ldots,S_k$ with core $K\cup C$. $\square$

Call a *section certificate* of $F$ a link $F_K$, $K$ possibly empty, a
section of $F_K$, and a set of quotients with a common number $m'$ of parts
that is larger than the bound of Corollary 2 for $m'$ and $N'=|\mathcal U|$.
By Corollary 2 and Lemma 6, a certificate yields a $3$-sunflower of $F$.

**Example 7.** In the family $B(\rho,m)^h$ of L214, $h\ge2$, fix for every
point $v$ of the outer ground set an inner member $S^*_v$ of
$B(\rho,m)^{h-1}$, and take the parts $\{v\}\times S^*_v$. A member
$\bigcup_{v\in A}\{v\}\times S_v$ is a union of parts exactly when $S_v=S^*_v$
for every $v\in A$, so the section is a copy of $B(\rho,m)$ whose quotient is
$B(\rho,m)$ itself. Its link at the center $x$ is the full product of the
blocks $Y_1,\ldots,Y_m$, a word family with $\rho^m$ words over alphabets of
$\rho$ symbols. For $\rho\ge3$ it has three pairwise disjoint words, a
sunflower with core $\{x\}$. Lemma 1 also detects a sunflower there from
the number of words and the alphabet sizes alone once
$\rho^{m-M}>3\binom mM$, which holds for every $\rho\ge7$ when $m$ is large,
because $7^{1/3}>3/2^{2/3}$. For $\rho\ge136$, this center link also exceeds
the bound of Corollary 2, since $N=\rho m$ and $\rho>c(m)$, and hence gives
a section certificate in the narrower sense defined above. In the
families of L215, sections whose parts are inner triangle-power members
reduce to these. The sunflowers were already known
([[research/sunflower_exponential_bound/spread_matching_obstruction|obstruction note]]);
the point is that sections reach them although the families are
intersecting and their point counts lie far beyond the range of
Proposition 3.

## Thinned families and unit-core links

The absolute families of L214 come from a random thinning, under which the
sections of Example 7 retain almost nothing. The sunflowers survive in
links at single parts.

**Proposition 8.** Let $G$ be an $a$-uniform family on $V$, let
$A_1,A_2,A_3\in G$ form a $3$-sunflower with core $C$, and let $H$ be a
nonempty $b$-uniform family with $b\ge1$. Let $F'$ keep every member of
$G[H]$ independently with probability $q$. Then, with probability at least
$1-3\exp(-q|H|^{a-|C|})$, $F'$ contains a $3$-sunflower whose core is
$\bigcup_{v\in C}\{v\}\times S_v$ for some members $S_v\in H$; when $C$ is a
single point this core is a single part.

*Proof.* Fix $S_v\in H$ for $v\in C$. For each $i$, the members of $G[H]$
with outer set $A_i$ and fiber $S_v$ over every $v\in C$ number
$|H|^{a-|C|}$, since the fibers over $A_i\setminus C$ are free, and these
three classes are disjoint. One retained member from each class gives a
$3$-sunflower with the stated core: the outer sets meet pairwise exactly in
$C$, where all three fibers agree. Each class is missed with probability
$(1-q)^{|H|^{a-|C|}}\le\exp(-q|H|^{a-|C|})$. $\square$

Every block family $B(\rho,m)$ with $m\ge3$ has such sunflowers. For
$\rho\ge3$, three pairwise disjoint transversals $T_1,T_2,T_3$ of
$Y_1,\ldots,Y_m$ give the members $\{x\}\cup T_i$, with core $\{x\}$. For
every $\rho\ge2$, three members $\{z\}\cup Y_i\cup W$ of the second kind
with a common $W$ have core $\{z\}\cup W$. So Proposition 8 applies to
random thinnings of every substitution power in this folder whose outer
family is a block family, including those of L214, L215 and the
varying-scale construction of the
[[research/sunflower_exponential_bound/refined_spread_obstructions|refined obstruction note]],
with a bound that depends on the retention probability.

**Corollary 9.** Let $r\ge16$, $\rho=\lceil16r\rceil$, $m=\rho^\rho$,
$h=\lceil\log_2\rho\rceil$, $F=B(\rho,m)^h$ and $n=(m+1)^h$. Let $F'$ keep
every member of $F$ independently with probability $q=2r^n/|F|$, the
thinning in
[[theory/set_systems/L214_spread_intersecting_families/_proof|Lemma 4 of the proof of L214]].

- Every section of Example 7 contains fewer than one member of $F'$ in
  expectation.
- Put $t=\lceil4\rho\log(2\rho)\rceil+2<m$. With probability at least
  $1-e^{-n}$, every section of Example 7 contains fewer than $t$ members
  of $F'$ simultaneously.
- With probability at least $1-3\exp(-e^{m^2})$, $F'$ contains a
  $3$-sunflower whose core is a single part $\{x\}\times S$, with $x$ the
  first center of the outer block family and $S$ an inner member.
- Hence, with positive probability, $F'$ has more than $r^n$ members, is
  absolutely $r$-spread and intersecting, contains such a sunflower, and
  has fewer than $t$ members in each of those sections.

*Proof.* As $\rho\ge256$, $h\ge8$. Here $\kappa=1$, so
$|B(\rho,m)|=2\rho^m$, and by L214's Lemma 1
$|F|=2\rho^m|B(\rho,m)^{h-1}|^{m+1}$ and
$|B(\rho,m)^{h-1}|=(2\rho^m)^{(n'-1)/m}\le(2\rho)^{n'}$ with
$n'=(m+1)^{h-1}$. A section of Example 7 holds $2\rho^m$ members of $F$, so
it retains $2q\rho^m=4r^n\rho^m/|F|\le4r^n\rho^{m+1-n}$ in expectation,
using $|F|\ge\rho^{n-1}$. As $r\le\rho/16$ and $n\ge(m+1)^2$, this is at most
$4(\rho\,16^{-(m+1)})^{m+1}<1$.

For the simultaneous assertion, let $N_0$ be the number of outer points.
There are at most $|H|^{N_0}$ choices of the section, where
$H=B(\rho,m)^{h-1}$ and $N_0=2+(2m-\rho)\rho<2\rho(m+1)$.
Using $|H|\le(2\rho)^{n'}$ and $n=(m+1)n'$ gives

$$
\log\bigl(|H|^{N_0}\bigr)<2\rho n\log(2\rho).
$$

The mean $\mu$ for each fixed section obeys the bound above, so
$\log\mu\le\log4+(m+1)\log\rho-n\log16\le-n$.
Indeed $n\ge(m+1)^2$, $\log\rho\le m+1$, $\log4\le n/2$, and
$\log16>5/2$. The binomial tail bound then gives
$\Pr[X\ge t]\le(e\mu/t)^t\le\exp(-t(n-1))$. A union bound over all
sections, followed by $n-1\ge n/2$, yields

$$
\Pr[\text{some such section has at least }t\text{ members}]
\le\exp\bigl(2\rho n\log(2\rho)-t(n-1)\bigr)\le e^{-n}.
$$

Finally $\log(2\rho)\le\rho$ gives
$t\le4\rho^2+3<\rho^\rho=m$ for $\rho\ge256$.

Apply Proposition 8 with $G=B(\rho,m)$, the sunflower with core
$C=\{x\}$, $a=m+1$ and $H=B(\rho,m)^{h-1}$. Then

$$
q\,|H|^m=\frac{r^n}{\rho^m|H|}
\ge\exp\bigl(n'((m+1)\log r-\log(2\rho))-m\log\rho\bigr).
$$

Since $2\rho\le34r$ and $r\ge16$, $(m+1)\log r-\log(2\rho)\ge m\log16-\log34
\ge2m$, and with $n'\ge m+1$ and $\log\rho\le m$ the exponent is at least
$m^2$. The proof of L214's Lemma 4 bounds the probability that $|F'|\le r^n$
by $e^{-r^n/4}$ and the probability that spread fails by $e^{-n}$, and
$e^{-r^n/4}+2e^{-n}+3\exp(-e^{m^2})<1$. Every subfamily of $F$ is
intersecting. $\square$

The same count works far below the rate of L214. Keep every member of $F$
independently with probability $q''=R^n/|F|$, for any $R$ with
$(2\rho)^{2/(m+1)}\le R\le|F|^{1/n}$. Then
$q''|H|^m=R^n/(2\rho^m|H|)\ge2^m$, because

$$
n\log R\ge2n'\log(2\rho)\ge n'\log(2\rho)+m\log\rho+(m+1)\log2,
$$

so by Proposition 8 the result contains a $3$-sunflower with probability
at least $1-3\exp(-2^m)$. Random subfamilies of these powers therefore keep a
sunflower at rates barely above $1$; a family that hides its sunflowers
must be thinned in a correlated way.

The sunflower of Proposition 8 is a matching in the link at the parts over
$C$, found through the projection of that link onto the outer family: three
members whose outer sets meet only in $C$ are disjoint outside the core,
whatever their other inner fibers. On the simultaneous event of
Corollary 9, even choosing a section of Example 7 after seeing $F'$ leaves
fewer than $m$ members. Neither its whole quotient, of rank $m+1$, nor its
link at the first-center part, of rank $m$, can then exceed the count
bounds used in Example 7. For either rank $u\ge2$, the bound of Corollary
2 is at least $3\binom u{\lfloor2u/3\rfloor}\ge3u$; the unweighted bound
of Lemma 1 has the same lower bound for a nonempty family. Some such
sections can nevertheless contain a few sunflower members. In particular,
the three members selected in Proposition 8 fit into one adaptively chosen
section, since their outer petals are disjoint and their core fibers agree.

Disjointness lifts from such projections, while sunflowers with
nonempty cores do not in general, since a common outer point can carry
different inner fibers. So exact sections certify the unthinned families,
while for the thinned ones the sunflower comes from a projected matching;
whether another link inside those sections, or a different section,
certifies the thinned families is not decided here. Projected matchings
after taking links at unions of parts supply an additional certificate
for these thinned families.

## Where the engine stops

**The single-scale window.** For a word family of $m$ coordinates with
$\rho^m$ words over alphabets of $B$ symbols, the alphabet bound of Lemma 1
decides nothing once $\rho^m\le3\binom mMB^M$, that is, roughly once
$B>(2^{2/3}\rho/3)^{3/2}$; the projection form still applies when the
projections to $M$ coordinates are far from injective. The hitting lemma
behind
[[../library/set_systems/bell_2021_note_sunflowers/lemma_2|Bell–Chueluecha–Warnke's Lemma 2]]
needs spread $C\log m$. Take a uniformly random subfamily of $[B]^m$ with
$\rho^m$ words, $\rho^m$ an integer and $B>\rho$. A cylinder fixing $t$
coordinates holds $\rho^mB^{-t}<\rho^{m-t}$ of its words in expectation,
and for constant $\rho$, large $m$ and $B$ beyond the window, neither the
alphabet bound nor the hitting lemma applies. Such families are not
plausible counterexamples: the expected number of ordered triples of
pairwise disjoint words among them is
$(B(B-1)(B-2))^m(\rho^m)_3/(B^m)_3$, about
$\rho^{3m}\bigl((B-1)(B-2)/B^2\bigr)^m$, far more than $\rho^m$ when
$\rho\ge3$. The
[[research/sunflower_exponential_bound/agreement_statistics|complete second-moment calculation]]
shows that the matching probability tends to one at every fixed rate
$\rho>(9/2)^{1/3}$, uniformly over alphabets $B\ge3$ when the requested
sample size is available. Thus the random-family side is proved, while
its extension to adversarially correlated families remains open.

**The residual.** Let $\rho\ge137$. A counterexample to SF($3$) at rate
$\rho$ is an absolutely $\rho$-spread family of $n$-sets with more than
$\rho^n$ members and no $3$-sunflower. By Proposition 4 one of its traces is
an intersecting, absolutely $\rho$-spread family of $m$-sets, $m\ge1$, with
more than $(\rho-1)^m$ members and no $3$-sunflower. Let $N$ be the number
of points its members cover. Proposition 3 at rate $\rho-1>e^3\cdot27/4$,
with $A=\max(1,N/((\rho-1)m))$, rules out $A=1$ and then gives
$N>m(\rho-1)^{3/2}/11.65$. By Corollary 2 and Lemma 6 it has no section
certificate in any link. The thinned substitution powers of Corollary 9
are intersecting, absolutely spread and large, like the families of this
class. In those powers, the sections of Example 7 can fail to give the
displayed counting certificates even though a matching in a projected
unit-core link finds a sunflower.
Since a $3$-sunflower is a matching in the link at its core, SF($3$) is
equivalent to the statement that every family in this class has three
pairwise disjoint members in some link. That is a reformulation, not a
reduction; its use is to name the families that no known certificate
reaches.

**What would advance.** A dichotomy of the following kind would prove
SF($3$):

- *(R)* an alphabet-independent pseudorandomness condition on a link,
  under which counting gives three pairwise disjoint members, or a
  condition that counts sunflowers with arbitrary cores;
- *(S)* when the condition fails, a passage to a link, section or
  projection whose matchings or sunflowers lift, with a controlled increment
  in an explicit invariant, so that the process ends in case (R) or in a
  certificate after boundedly many steps per scale.

Any such statement must handle four test cases at once: random families
(by (R)); the unthinned substitution powers (by sections); the thinned
powers of Corollary 9 (by projected matchings); and the
[[research/sunflower_exponential_bound/maximal_rate_chain_obstruction|maximal-rate chain obstruction]],
whose union of two intersecting parts requires keeping both parts.
Counting inside a single link is not enough by itself: the families of L214
have no disjoint pair at all in the empty link, at every rate, and their
sunflowers lie in other links. The
[[research/sunflower_exponential_bound/agreement_statistics|agreement-statistics note]]
supplies concrete Fourier criteria for (R), including a criterion on a
binary affine span that permits nonempty cores. It also proves that the
aggregate pair-agreement profile does not determine sunflower behavior.
The structural implication (S), and therefore the dichotomy, remains open.

The bound of Lemma 1 is for three petals. For $k\ge4$ the analogous
coordinate function contains terms such as $[a=b][c=d]$ that involve every
variable, and no saving of this kind is established here.
