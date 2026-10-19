# Bounded VC-dimension implies the Erdős–Rado sunflower conjecture

Gennian Ge  Jian Wang  Zixiang Xu  Xiaochen Zhao

## Abstract

The Erdős–Rado sunflower conjecture asserts that, for every fixed integer $r\geq 3$, there is a constant $K(r)$ such that every $\ell$-uniform family with more than $K(r)^{\ell}$ members contains an $r$-sunflower. We prove this conjecture for families of bounded VC-dimension.

## 1 Introduction

A collection of distinct sets $H_{1},\ldots,H_{r}$ is an $r$-*sunflower*, or a $\Delta$-system, if every two of its members have the same intersection. Thus there is a set $C$, called the *kernel*, such that $H_{i}\cap H_{j}=C$ whenever $i\neq j$, the sets $H_{i}\setminus C$ are the petals and are pairwise disjoint. A family is $\ell$-*bounded* if each of its members has size at most $\ell$, and is $\ell$-uniform if each of its members has size exactly $\ell$. This simple intersection pattern is one of the fundamental configurations in extremal set theory. For integers $r\geq 3$ and $\ell\geq 1$, let $f_{r}(\ell)$ be the maximum size of an $\ell$-uniform family containing no $r$-sunflower. In 1960, Erdős and Rado [11] proved the classical sunflower lemma $f_{r}(\ell)\leq(r-1)^{\ell}\ell!$, which have become standard reduction tools across combinatorics and theoretical computer science [1, 8, 9, 12, 18, 23, 24, 25, 27, 28, 29], and the remarkable persistence of the problem reflects the difficulty of forcing even this rigid local structure from a purely global hypothesis on the size of a family.

Erdős and Rado [11] also conjectured that the factorial term can be removed: there should be a constant $K(r)$, depending only on $r$, for which

$$f_{r}(\ell)\leq K(r)^{\ell}.$$

The conjecture has been one of the favorite open problems of Erdős [10], which remains open in general and also stands as one of the most important problem in the field of extremal combinatorics [6]. In a major breakthrough, Alweiss, Lovett, Wu, and Zhang [3] obtained a bound of the form $\bigl(Cr^{3}\log\ell\log\log\ell\bigr)^{\ell}$, Bell, Chueluecha, and Warnke [5] subsequently sharpened the best general estimate to $\bigl(Cr\log\ell\bigr)^{\ell}$. These advances introduced and refined the spread viewpoint that now plays a central role in extremal set theory [7, 16, 17, 19, 20, 21, 22, 34].

For a set system $\mathcal{H}$, a set $D$ is *shattered* if $\{H\cap D:H\in\mathcal{H}\}=2^{D}$, and the VC-dimension $\operatorname{VC}(\mathcal{H})$ is the largest size of such a set. This parameter measures the complexity of the traces of $\mathcal{H}$. Its basic counting consequence is the Sauer–Shelah lemma [30, 31, 33], which gives the largest size of a set systems with bounded VC-dimension.

Bounded VC-dimension has repeatedly made difficult extremal conjectures accessible. Fox, Pach, and Suk [13] initiated the study of the Erdős–Hajnal conjecture in this setting. Nguyen, Scott, and Seymour [26] subsequently resolved the bounded-VC case completely: for every fixed $d$, there is a constant $c=c(d)>0$ such that every $n$-vertex graph with VC-dimension at most $d$ contains a clique or an independent set of size at least $n^{c}$, also see a recent improvement on the exponent [32]. Fox, Pach, and Suk [14] also proved the Schur–Erdős prediction $r(k;m)=2^{\Theta_{k}(m)}$ for edge-colorings whose monochromatic neighborhood systems have bounded VC-dimension.

The sunflower problem under bounded VC-dimension was first studied by Fox, Pach, and Suk [15]. They proved that an $\ell$-uniform family $\mathcal{H}$ with $\operatorname{VC}(\mathcal{H})\leq d$ contains an $r$-sunflower whenever $\lvert\mathcal{H}\rvert\geq 2^{10\ell(dr)^{2\log^{*}\ell}}$. Balogh, Bernshteyn, Delcourt, Ferber, and Pham [4] later obtained the substantially sharper sufficient condition $\lvert\mathcal{H}\rvert>\bigl(Cr(\log d+\log^{*}\ell)\bigr)^{\ell}$ for an absolute constant $C$, and also determined the sharp bound when $d=1$. For general fixed $d$, however, the exponential base still depends on $\ell$. Our main result removes this final dependence.

**Theorem 1.1.** Let $d\geq 1$, $r\geq 2$, and $\ell\geq 1$. If $\mathcal{H}$ is an $\ell$-bounded set system with $\operatorname{VC}(\mathcal{H})\leq d$ and no $r$-sunflower, then

$$\lvert\mathcal{H}\rvert\leq\sum_{k=0}^{\ell}(50dr)^{k}<2(50dr)^{\ell}.$$

In particular, every $\ell$-uniform set system $\mathcal{H}$ with $\operatorname{VC}(\mathcal{H})\leq d$ and $\lvert\mathcal{H}\rvert>(50dr)^{\ell}$ contains an $r$-sunflower.

## 2 Proof of main result

### 2.1 Notation and Tools

For a family $\mathcal{G}$ on a ground set $X$ and $T\subseteq X$, write

$$d_{\mathcal{G}}(T)=\lvert\{G\in\mathcal{G}:T\subseteq G\}\rvert.$$

Thus $d_{\mathcal{G}}(T)$ is the number of members of $\mathcal{G}$ that contain $T$. For $E\subseteq X$, the family $\{G\cap E:G\in\mathcal{G}\}$ is called the *trace* of $\mathcal{G}$ on $E$. We write $\nu(\mathcal{G})$ for the matching number of $\mathcal{G}$, that is, the maximum number of pairwise disjoint members in $\mathcal{G}$.

Let $0<q<1$. A nonempty family $\mathcal{G}$ is *$q$-spread* if $d_{\mathcal{G}}(T)\leq q^{\lvert T\rvert}\lvert\mathcal{G}\rvert$ for every nonempty $T\subseteq X$. In other words, the proportion of members containing any prescribed set $T$ is at most $q^{\lvert T\rvert}$. If $G$ is chosen uniformly from $\mathcal{G}$, meaning that each member is chosen with probability $\frac{1}{\lvert\mathcal{G}\rvert}$, we write

$$\mu_{x}=\mathbb{P}(x\in G)=\frac{d_{\mathcal{G}}(\{x\})}{\lvert\mathcal{G}\rvert}.$$

Thus $\mu_{x}$ is simply the probability that a random member contains $x$. For a $q$-spread family, the case $T=\{x\}$ gives $\mu_{x}\leq q$.

We use the following standard form of the Sauer–Shelah lemma [30, 31, 33].

**Lemma 2.1.** Let $\mathcal{G}$ be a set system on $X$ with $\operatorname{VC}(\mathcal{G})\leq d$, and let $E\subseteq X$ have size $m\geq d\geq 1$. Then

$$\lvert\{G\cap E:G\in\mathcal{G}\}\rvert\leq\sum_{i=0}^{d}\binom{m}{i}\leq\left(\frac{em}{d}\right)^{d}.$$

We shall use some facts about entropy. If a discrete random variable $Y$ takes only finitely many values, its *support* is the set of its possible values, namely

$$\operatorname{supp}(Y)=\{y:\mathbb{P}(Y=y)>0\}.$$

Writing $p_{y}=\mathbb{P}(Y=y)$, the *entropy* of $Y$ is defined as

$$H(Y)=\sum_{y\in\operatorname{supp}(Y)}p_{y}\log\frac{1}{p_{y}}.$$

Thus entropy is the average of $\log\frac{1}{p_{y}}$, where each possible value $y$ is given its probability $p_{y}$. Unless a base is displayed explicitly, all logarithms in the proof are natural. The entropy cannot exceed the logarithm of the number of values that the random variable can take. Indeed, by the concavity of the logarithm,

$$H(Y)\leq\log\left(\sum_{y\in\operatorname{supp}(Y)}p_{y}\frac{1}{p_{y}}\right)=\log\lvert\operatorname{supp}(Y)\rvert. \tag{1}$$

We also use the following standard Caro–Wei bound for the independence number of a graph, see [2]. Here $\alpha(J)$ denotes the largest size of an independent set in $J$, and $\deg_{J}(v)$ denotes the degree of a vertex $v$.

**Lemma 2.2.** If $J$ is a graph with $N$ vertices and $e(J)$ edges, then

$$\alpha(J)\geq\sum_{v\in V(J)}\frac{1}{\deg_{J}(v)+1}\geq\frac{N^{2}}{N+2e(J)}.$$

### 2.2 Proof of Theorem 1.1

We first bound the sum of the probabilities with which the elements of a fixed set $E$ occur in a random member of $\mathcal{G}$. It perfectly combines the property of $q$-spread family and Sauer–Shelah lemma, which is the key ingredient of the proof.

**Lemma 2.3.** Let $\mathcal{G}$ be a $q$-spread family with $\operatorname{VC}(\mathcal{G})\leq d$, where $0<q<1$ and $d\geq 1$. Let $G$ be chosen uniformly at random from $\mathcal{G}$, and put $\mu_{x}=\mathbb{P}(x\in G)$. If $E\subseteq X$ has size $m\geq d$, then

$$\sum_{x\in E}\mu_{x}\leq\frac{d\log\left(\frac{em}{d}\right)}{\log\left(\frac{1}{q}\right)}.$$

*Proof of Lemma 2.3.* Set $R=G\cap E$. Thus $R$ records exactly which elements of $E$ occur in the random set $G$. If $A\subseteq E$ is a possible value of $R$, then the event $R=A$ implies $A\subseteq G$, and therefore

$$\mathbb{P}(R=A)\leq\mathbb{P}(A\subseteq G)\leq q^{\lvert A\rvert}.$$

For $A\neq\varnothing$, the second inequality is exactly the spread condition. For $A=\varnothing$, it is the trivial inequality $\mathbb{P}(R=\varnothing)\leq 1=q^{0}$. Taking logarithms gives

$$\log\frac{1}{\mathbb{P}(R=A)}\geq\lvert A\rvert\log\frac{1}{q}.$$

We multiply this inequality by $\mathbb{P}(R=A)$ and sum over all possible values $A$ of $R$. By the definition of entropy,

$$H(R)\geq\log\left(\frac{1}{q}\right)\sum_{A\in\operatorname{supp}(R)}\mathbb{P}(R=A)\lvert A\rvert=\log\left(\frac{1}{q}\right)\sum_{x\in E}\mu_{x}.$$

To see the last equality directly, the middle sum is the average size of $R$. An element $x\in E$ contributes one to this size precisely when $x\in G$, which occurs with probability $\mu_{x}$.

It remains to bound the same entropy from above. Since every member of $\mathcal{G}$ is chosen with positive probability, the possible values of $R$ are exactly the sets $G\cap E$ with $G\in\mathcal{G}$. Hence Lemma 2.1 and the general entropy bound (1) give

$$H(R)\leq\log\lvert\operatorname{supp}(R)\rvert=\log\lvert\{G\cap E:G\in\mathcal{G}\}\rvert\leq d\log\left(\frac{em}{d}\right).$$

Comparing the lower and upper bounds for $H(R)$ proves the lemma. ∎

We next bound the sum of the squared inclusion probabilities based on lemma 2.3.

**Lemma 2.4.** Let $\mathcal{G}$ be $q$-spread with $\operatorname{VC}(\mathcal{G})\leq d$, where $d\geq 1$ and $0<q\leq\frac{1}{2}$. If $G$ is chosen uniformly at random from $\mathcal{G}$ and $\mu_{x}=\mathbb{P}(x\in G)$, then

$$\sum_{x\in X}\mu_{x}^{2}<49dq.$$

*Proof of Lemma 2.4.* For every $x\in X$, the spread condition applied to $\{x\}$ gives $\mu_{x}\leq q$. We separate the elements according to the size of this probability. For each integer $j\geq 0$, let

$$E_{j}=\{x\in X:2^{-j-1}q<\mu_{x}\leq 2^{-j}q\}$$

and set $m_{j}=\lvert E_{j}\rvert$. The sets $E_{j}$ partition the elements for which $\mu_{x}>0$, elements with $\mu_{x}=0$ do not affect the desired sum. Moreover, every $x\in E_{j}$ satisfies $\mu_{x}^{2}\leq 4^{-j}q^{2}$. It therefore remains to control the number $m_{j}$ of elements in each group.

Fix $j\geq 0$ with $m_{j}\geq d$. Applying Lemma 2.3 to $E_{j}$, and using $\mu_{x}>2^{-j-1}q$ for every $x\in E_{j}$, gives

$$m_{j}2^{-j-1}q\log\left(\frac{1}{q}\right)<\sum_{x\in E_{j}}\mu_{x}\log\left(\frac{1}{q}\right)\leq d\log\left(\frac{em_{j}}{d}\right).$$

Put $L=\log\left(\frac{1}{q}\right)$ and $u_{j}=\frac{m_{j}2^{-j-1}q}{d}$. The definition of $u_{j}$ gives $\frac{m_{j}}{d}=\frac{u_{j}2^{j+1}}{q}$, and hence

$$\log\left(\frac{em_{j}}{d}\right)=1+\log u_{j}+(j+1)\log 2+L.$$

Thus the preceding inequality becomes

$$u_{j}L<L+(j+1)\log 2+1+\log u_{j}. \tag{2}$$

**Claim 2.5.** If $m_{j}\geq d$, then $u_{j}\leq 4(j+2)$.

*Proof of the claim.* Suppose that $u_{j}>4(j+2)$. Since $j\geq 0$, this implies $u_{j}>8$, and in particular $\log u_{j}>0$. Also, $q\leq\frac{1}{2}$ gives $L\geq\log 2$. After dividing (2) by $L$, we use $\frac{(j+1)\log 2}{L}\leq j+1$, $\frac{1}{L}\leq\frac{1}{\log 2}<2$, and $\frac{\log u_{j}}{L}\leq\log_{2}u_{j}$. It follows that

$$u_{j}<j+4+\log_{2}u_{j}.$$

The elementary inequality $\log_{2}u\leq\frac{u}{2}$ holds for $u\geq 8$, so $u_{j}<2j+8$. On the other hand, our assumption gives $u_{j}>4j+8\geq 2j+8$, a contradiction. ∎

Returning to the definition of $u_{j}$, Claim 2.5 gives

$$m_{j}=\frac{du_{j}2^{j+1}}{q}\leq\frac{8d(j+2)2^{j}}{q}$$

whenever $m_{j}\geq d$. Since every element of $E_{j}$ contributes at most $4^{-j}q^{2}$, such a group contributes at most

$$\sum_{x\in E_{j}}\mu_{x}^{2}\leq m_{j}4^{-j}q^{2}\leq 8dq(j+2)2^{-j}.$$

Summing over all groups with $m_{j}\geq d$, and using $\sum_{j\geq 0}(j+2)2^{-j}=6$, we obtain a total contribution of at most $48dq$.

If instead $m_{j}<d$, then the same pointwise bound gives

$$\sum_{x\in E_{j}}\mu_{x}^{2}\leq m_{j}4^{-j}q^{2}<d4^{-j}q^{2}.$$

The total contribution of these groups is therefore less than $dq^{2}\sum_{j\geq 0}4^{-j}=\frac{4}{3}dq^{2}\leq\frac{2}{3}dq$, where the last inequality uses $q\leq\frac{1}{2}$. Adding the two contributions yields

$$\sum_{x\in X}\mu_{x}^{2}<48dq+\frac{2}{3}dq=\frac{146}{3}dq<49dq,$$

as required. ∎

Lemma 2.4 controls intersections in an averaged sense. Indeed, for a fixed $x\in X$, there are exactly $d_{\mathcal{G}}(\{x\})^{2}$ ordered pairs $(A,B)\in\mathcal{G}^{2}$ for which $x\in A\cap B$. Summing this count over $x$ will allow us to find a large pairwise disjoint subfamily.

**Lemma 2.6.** Let $\mathcal{G}$ be a finite family of nonempty sets. If $\mathcal{G}$ is $q$-spread, $\operatorname{VC}(\mathcal{G})\leq d$, $d\geq 1$, and $0<q\leq\frac{1}{2}$, then $\nu(\mathcal{G})>\frac{1}{49dq}.$

*Proof of Lemma 2.6.* Define a graph $J$ whose vertices are the members of $\mathcal{G}$, with two distinct members joined by an edge exactly when they intersect. Thus an independent set in $J$ is the same as a pairwise disjoint subfamily of $\mathcal{G}$.

Write $N=\lvert\mathcal{G}\rvert$, choose a member $G$ uniformly from $\mathcal{G}$, and put $\mu_{x}=\mathbb{P}(x\in G)=\frac{d_{\mathcal{G}}(\{x\})}{N}$. Consider the sum of $\lvert A\cap B\rvert$ over all ordered pairs $(A,B)\in\mathcal{G}^{2}$. Since every member of $\mathcal{G}$ is nonempty, each of the $N$ pairs $(A,A)$ contributes at least one. Moreover, every edge $\{A,B\}$ of $J$ gives the two ordered pairs $(A,B)$ and $(B,A)$, each of which also contributes at least one. It follows that

$$N+2e(J)\leq\sum_{A,B\in\mathcal{G}}\lvert A\cap B\rvert.$$

We now count the sum on the right by first fixing $x\in X$. There are $d_{\mathcal{G}}(\{x\})$ choices of $A$ containing $x$, and the same number of choices for $B$. Thus $x$ is counted in exactly $d_{\mathcal{G}}(\{x\})^{2}$ ordered pairs, and consequently

$$\sum_{A,B\in\mathcal{G}}\lvert A\cap B\rvert=\sum_{x\in X}d_{\mathcal{G}}(\{x\})^{2}=N^{2}\sum_{x\in X}\mu_{x}^{2}<49dqN^{2},$$

where the last inequality follows from Lemma 2.4. Combining the two estimates and applying Lemma 2.2, we obtain

$$\alpha(J)\geq\frac{N^{2}}{N+2e(J)}>\frac{1}{49dq}.$$

Since independent sets in $J$ are precisely the pairwise disjoint subfamilies of $\mathcal{G}$, we have $\nu(\mathcal{G})=\alpha(J)$, which proves the lemma. ∎

We next show how to obtain a spread family from a sufficiently large uniform family. We select a set $C$ that is contained in many members of the original family, but for which no proper extension is contained in a comparably large proportion of the members. After $C$ is removed, this maximality becomes exactly the spread condition.

**Lemma 2.7.** Let $0<q<1$, and let $\mathcal{H}\subseteq\binom{X}{\ell}$ satisfy $\lvert\mathcal{H}\rvert>q^{-\ell}$. Then there is a set $C\subseteq X$ with $\lvert C\rvert<\ell$ such that

$$\mathcal{G}=\{H\setminus C:H\in\mathcal{H},\ C\subseteq H\}$$

is a nonempty $q$-spread, $(\ell-\lvert C\rvert)$-uniform family with $\operatorname{VC}(\mathcal{G})\leq\operatorname{VC}(\mathcal{H})$.

*Proof of Lemma 2.7.* Choose an inclusion-maximal set $C\subseteq X$ satisfying

$$d_{\mathcal{H}}(C)\geq\lvert\mathcal{H}\rvert q^{\lvert C\rvert}. \tag{3}$$

Such a choice is possible because $X$ is finite and $C=\varnothing$ satisfies (3).

The right-hand side of (3) is positive, so $C$ is contained in at least one member of $\mathcal{H}$. In particular, $\lvert C\rvert\leq\ell$. Suppose that $\lvert C\rvert=\ell$. Since $\mathcal{H}$ is $\ell$-uniform, the only member of $\mathcal{H}$ that can contain $C$ is $C$ itself, and hence $d_{\mathcal{H}}(C)=1$. On the other hand,

$$d_{\mathcal{H}}(C)\geq\lvert\mathcal{H}\rvert q^{\ell}>q^{-\ell}q^{\ell}=1,$$

a contradiction. Consequently, $\lvert C\rvert<\ell$.

Every member of $\mathcal{H}$ containing $C$ produces, after $C$ is removed, a set of size $\ell-\lvert C\rvert$. Moreover, the original member can be recovered by adding $C$ back, so distinct members of $\mathcal{H}$ produce distinct members of $\mathcal{G}$. Thus $\mathcal{G}$ is nonempty and $(\ell-\lvert C\rvert)$-uniform, and $\lvert\mathcal{G}\rvert=d_{\mathcal{H}}(C).$

We next verify the spread condition. Let $\varnothing\neq T\subseteq X\setminus C$. If $C\cup T$ also satisfied (3), it would be a proper extension of $C$ satisfying the same condition, contrary to the maximal choice of $C$. Hence

$$d_{\mathcal{H}}(C\cup T)<\lvert\mathcal{H}\rvert q^{\lvert C\rvert+\lvert T\rvert}.$$

A member of $\mathcal{G}$ contains $T$ exactly when the corresponding member of $\mathcal{H}$ contains $C\cup T$. Using (3), we therefore obtain

$$d_{\mathcal{G}}(T)=d_{\mathcal{H}}(C\cup T)<\lvert\mathcal{H}\rvert q^{\lvert C\rvert}q^{\lvert T\rvert}\leq\lvert\mathcal{G}\rvert q^{\lvert T\rvert}.$$

This is precisely the $q$-spread condition.

It remains to compare the VC-dimensions. Suppose that $D\subseteq X\setminus C$ is shattered by $\mathcal{G}$. For every $A\subseteq D$, there is a member $G\in\mathcal{G}$ such that $G\cap D=A$. By the definition of $\mathcal{G}$, there is an $H\in\mathcal{H}$ containing $C$ for which $G=H\setminus C$. Since $D\cap C=\varnothing$,

$$H\cap D=(H\setminus C)\cap D=G\cap D=A.$$

Thus every subset of $D$ also occurs as the intersection of $D$ with a member of $\mathcal{H}$, so $D$ is shattered by $\mathcal{H}$. We conclude that $\operatorname{VC}(\mathcal{G})\leq\operatorname{VC}(\mathcal{H})$. ∎

*Proof of Theorem 1.1.* We first prove the assertion for an $\ell$-uniform family. Set $Q=50dr$ and $q=Q^{-1}$. Since $d\geq 1$ and $r\geq 2$, we have $q\leq\frac{1}{2}$.

Suppose that $\mathcal{H}\subseteq\binom{X}{\ell}$, that $\operatorname{VC}(\mathcal{H})\leq d$, and that $\lvert\mathcal{H}\rvert>Q^{\ell}=q^{-\ell}$. By Lemma 2.7, there is a set $C$ such that

$$\mathcal{G}=\{H\setminus C:H\in\mathcal{H},\ C\subseteq H\}$$

is a nonempty $q$-spread family with VC-dimension at most $d$. Lemma 2.6 gives

$$\nu(\mathcal{G})>\frac{1}{49dq}=\frac{50r}{49}>r.$$

In particular, $\mathcal{G}$ contains $r$ pairwise disjoint members $G_{1},\ldots,G_{r}$. For each $i$, the definition of $\mathcal{G}$ gives a member $H_{i}=C\cup G_{i}\in\mathcal{H}$. Every $G_{i}$ is disjoint from $C$, and $G_{i}\cap G_{j}=\varnothing$ whenever $i\neq j$. Consequently,

$$H_{i}\cap H_{j}=(C\cup G_{i})\cap(C\cup G_{j})=C$$

for every $i\neq j$. Thus $H_{1},\ldots,H_{r}$ form an $r$-sunflower with kernel $C$. We have proved that every $\ell$-uniform family with no $r$-sunflower has at most $Q^{\ell}$ members.

Now let $\mathcal{H}$ be $\ell$-bounded, and partition it according to the sizes of its members. For $0\leq k\leq\ell$, let $\mathcal{H}_{k}=\mathcal{H}\cap\binom{X}{k}$. Each $\mathcal{H}_{k}$ is a subfamily of $\mathcal{H}$. Removing members cannot create a shattered set, so $\operatorname{VC}(\mathcal{H}_{k})\leq d$. Likewise, an $r$-sunflower in $\mathcal{H}_{k}$ would also be an $r$-sunflower in $\mathcal{H}$, and hence no $\mathcal{H}_{k}$ contains one. The uniform case therefore gives $\lvert\mathcal{H}_{k}\rvert\leq Q^{k}$ for $1\leq k\leq\ell$. The family $\mathcal{H}_{0}$ contains at most the empty set, so $\lvert\mathcal{H}_{0}\rvert\leq 1=Q^{0}$. It follows that

$$\lvert\mathcal{H}\rvert=\sum_{k=0}^{\ell}\lvert\mathcal{H}_{k}\rvert\leq\sum_{k=0}^{\ell}Q^{k}=\frac{Q^{\ell+1}-1}{Q-1}<2Q^{\ell},$$

where the final inequality uses $Q\geq 2$. Substituting $Q=50dr$ completes the proof. ∎

## References

- [1]  N. Alon and R. B. Boppana. The monotone circuit complexity of Boolean functions. Combinatorica, 7(1):1–22, 1987.
- [2]  N. Alon and J. H. Spencer. The probabilistic method. Wiley Series in Discrete Mathematics and Optimization. John Wiley & Sons, Inc., Hoboken, NJ, fourth edition, 2016.
- [3]  R. Alweiss, S. Lovett, K. Wu, and J. Zhang. Improved bounds for the sunflower lemma. Ann. of Math. (2), 194(3):795–815, 2021.
- [4]  J. Balogh, A. Bernshteyn, M. Delcourt, A. Ferber, and H. T. Pham. Sunflowers in set systems with small VC-dimension. Combinatorica, 45(6):Paper No. 58, 19, 2025.
- [5]  T. Bell, S. Chueluecha, and L. Warnke. Note on sunflowers. Discrete Math., 344(7):Paper No. 112367, 3, 2021.
- [6]  T. Bloom. Top 10 Erdős problems. https://www.erdosproblems.com/forum/thread/blog:5.
- [7]  G. C. Bruns, D. N. Desai, A. L. Gavrilyuk, J. Gomez, and N. Lindzey. Intersecting families of spanning trees of $K_{n,n}$. arXiv preprint, 2026. arXiv:2606.22697.
- [8]  B. P. Cavalar, M. Kumar, and B. Rossman. Monotone circuit lower bounds from robust sunflowers. Algorithmica, 84(12):3655–3685, 2022.
- [9]  S. F. de Rezende and M. Vinyals. Lifting with colourful sunflowers. In 40th Computational Complexity Conference, volume 339 of LIPIcs. Leibniz Int. Proc. Inform., pages Art. No. 36, 19. Schloss Dagstuhl. Leibniz-Zent. Inform., Wadern, 2025.
- [10]  P. Erdős. On the combinatorial problems which I would most like to see solved. Combinatorica, 1(1):25–42, 1981.
- [11]  P. Erdős and R. Rado. Intersection theorems for systems of sets.  J. London Math. Soc., 35:85–90, 1960.
- [12]  F. V. Fomin, D. Lokshtanov, S. Saurabh, and M. Zehavi. Kernelization. Cambridge University Press, Cambridge, 2019. Theory of parameterized preprocessing.
- [13]  J. Fox, J. Pach, and A. Suk. Erdős-Hajnal conjecture for graphs with bounded VC-dimension. Discrete Comput. Geom., 61(4):809–829, 2019.
- [14]  J. Fox, J. Pach, and A. Suk. Bounded VC-dimension implies the Schur-Erdős conjecture. Combinatorica, 41(6):803–813, 2021.
- [15]  J. Fox, J. Pach, and A. Suk. Sunflowers in set systems of bounded dimension. Combinatorica, 43(1):187–202, 2023.
- [16]  P. Frankl, G. Hurlbert, F. Ihringer, A. Kupavskii, N. Lindzey, K. Meagher, and V. R. T. Pantangi. Intersecting families of spanning trees. arXiv preprint, 2025. arXiv:2502.08128.
- [17]  P. Frankl and A. Kupavskii. The Hajnal–Rothschild problem. arXiv preprint, 2025. arXiv:2502.06699.
- [18]  P. Gopalan, R. Meka, and O. Reingold. DNF sparsification and a faster deterministic counting algorithm. Comput. Complexity, 22(2):275–310, 2013.
- [19]  E. Iarovikova, F. Noskov, G. Sokolov, and N. Terekhov. Forbidding just one intersection for short integer sequences. arXiv preprint, 2025. arXiv:2512.17544.
- [20]  N. Keller, N. Lifshitz, and O. Sheinfeld. The forbidden cross intersection problem for permutations. arXiv preprint, 2025. arXiv:2512.11372.
- [21]  A. Kupavskii and F. Noskov. Linear dependencies, polynomial factors in the Duke–Erdős forbidden sunflower problem. arXiv preprint, 2024. arXiv:2410.06156.
- [22]  A. Kupavskii and D. Zakharov. Spread approximations for forbidden intersections problems. Adv. Math., 445:Paper No. 109653, 29, 2024.
- [23]  X. Li, S. Lovett, and J. Zhang. Sunflowers and quasi-sunflowers from randomness extractors. In Approximation, randomization, and combinatorial optimization. Algorithms and techniques, volume 116 of LIPIcs. Leibniz Int. Proc. Inform., pages Art. No. 51, 13. Schloss Dagstuhl. Leibniz-Zent. Inform., Wadern, 2018.
- [24]  S. Lovett, R. Meka, I. Mertz, T. Pitassi, and J. Zhang. Lifting with sunflowers. In 13th Innovations in Theoretical Computer Science Conference, volume 215 of LIPIcs. Leibniz Int. Proc. Inform., pages Art. No. 104, 24. Schloss Dagstuhl. Leibniz-Zent. Inform., Wadern, 2022.
- [25]  S. Natarajan Ramamoorthy and A. Rao. Lower bounds on non-adaptive data structures maintaining sets of numbers, from sunflowers. In 33rd Computational Complexity Conference, volume 102 of LIPIcs. Leibniz Int. Proc. Inform., pages Art. No. 27, 16. Schloss Dagstuhl. Leibniz-Zent. Inform., Wadern, 2018.
- [26]  T. Nguyen, A. Scott, and P. Seymour. Induced subgraph density. VI. Bounded VC-dimension. Adv. Math., 482:Paper No. 110601, 20, 2025.
- [27]  A. Rao. Coding for sunflowers. Discrete Anal., pages Paper No. 2, 8, 2020.
- [28]  A. Rao. The story of sunflowers.  J. Lond. Math. Soc. (2), 113(1):Paper No. e70380, 12, 2026.
- [29]  A. A. Razborov. Lower bounds on the monotone complexity of some Boolean functions. Dokl. Akad. Nauk SSSR, 281(4):798–801, 1985.
- [30]  N. Sauer. On the density of families of sets.  J. Combinatorial Theory Ser. A, 13:145–147, 1972.
- [31]  S. Shelah. A combinatorial problem; stability and order for models and theories in infinitary languages. Pacific J. Math., 41:247–261, 1972.
- [32]  S. Sun, Y. Wang, and J. Zeng. A single-exponential Erdős–Hajnal bound for graphs of bounded VC-dimension. arXiv preprint, 2026. arXiv:2607.09049.
- [33]  V. N. Vapnik and A. Y. Chervonenkis. On the uniform convergence of relative frequencies of events to their probabilities. In Measures of complexity, pages 11–30. Springer, Cham, 2015. Reprint of Theor. Probability Appl. 16 (1971), 264–280.
- [34]  J. Wang and J. Xiao. A note on the maximum diversity of intersecting families in the symmetric group. European J. Combin., 134:Paper No. 104331, 7, 2026.
