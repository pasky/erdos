# A $4$-choosable Graph that is Not $(8:2)$-choosable

Zdeněk Dvořák$^*$  Xiaolan Hu$^\dagger$  Jean-Sébastien Sereni$^\ddagger$

*Received 11 June 2018; Published 30 October 2019*

**Abstract:** In 1980, Erdős, Rubin and Taylor asked whether for all positive integers $a$, $b$, and $m$, every $(a:b)$-choosable graph is also $(am:bm)$-choosable. We provide a negative answer by exhibiting a $4$-choosable graph that is not $(8:2)$-choosable.

**Key words and phrases:** $(am:bm)$-conjecture, $(a:b)$-choosable graph, list coloring.

Coloring the vertices of a graph with sets of colors (that is, each vertex is assigned a fixed-size subset of the colors such that adjacent vertices are assigned disjoint sets) is a fundamental notion, which in particular captures fractional colorings. The fractional chromatic number of a graph $G$ can indeed be defined to be the infimum (which actually is a minimum) of the ratios $a/b$ such that, if every vertex of $G$ is replaced by a clique of order $b$ and every edge of $G$ is replaced by a complete bipartite graph between the relevant cliques, then the chromatic number of the obtained graph is at most $a$.

In their seminal work on list coloring, Erdős, Rubin and Taylor [2] raised several intriguing questions about the list version of set coloring. Before stating them, let us review the relevant definitions.

**Set coloring.** A function that assigns a set to each vertex of a graph is a *set coloring* if the sets assigned to adjacent vertices are disjoint. For positive integers $a$ and $b\leq a$, an $(a:b)$-coloring of a graph $G$ is a set coloring with range $\binom{\{1,\ldots,a\}}{b}$, *i.e.*, a set coloring that to each vertex of $G$ assigns a $b$-element subset of $\{1,\ldots,a\}$. The concept of $(a:b)$-coloring is a generalization of the conventional vertex coloring. In fact, an $(a:1)$-coloring is exactly an ordinary proper $a$-coloring.

This project falls within the scope of L.I.A. STRUCO.

$^*$Supported by the Center of Excellence – Inst. for Theor. Comp. Sci., Prague (project P202/12/G061 of Czech Science Foundation).

$^\dagger$Partially supported by NSFC under grant number 11601176.

$^\ddagger$Partially supported by P.H.C. Barrande 40625WH.

*A list assignment* for a graph $G$ is a function $L$ that to each vertex $v$ of $G$ assigns a set $L(v)$ of colors. A set coloring $\varphi$ of $G$ is an *$L$-set coloring* if $\varphi(v)\subseteq L(v)$ for every $v\in V(G)$. For a positive integer $b$, we say that $\varphi$ is an *$(L:b)$-coloring* of $G$ if $\varphi$ is an $L$-set coloring and $|\varphi(v)|=b$ for every $v\in V(G)$. If such an $(L:b)$-coloring exists, then $G$ is *$(L:b)$-colorable*. For an integer $a\geq b$, we say that $G$ is *$(a:b)$-choosable* if $G$ is $(L:b)$-colorable for every list assignment $L$ such that $|L(v)|=a$ for each $v\in V(G)$. We abbreviate $(L:1)$-coloring, $(L:1)$-colorable, and $(a:1)$-choosable to $L$-coloring, $L$-colorable, and $a$-choosable, respectively.

**Questions and results.** It is straightforward to see that if a graph is $(a:b)$-colorable, it is also $(am:bm)$-colorable for every positive integer $m$: we can simply replace every color in an $(a:b)$-coloring by $m$ new colors. However, this argument fails in the list coloring setting, leading Erdős, Rubin and Taylor [2] to ask whether every $(a:b)$-choosable graph is also $(am:bm)$-choosable whenever $m\geq 1$. A positive answer to this question is sometimes referred to as “the $(am:bm)$-conjecture”. Using the characterization of $2$-choosable graphs [2], Tuza and Voigt [4] provided a positive answer when $a=2$ and $b=1$. In the other direction, Gutner and Tarsi [3] demonstrated that if $k$ and $m$ are positive integers and $k$ is odd, then every $(2mk:mk)$-choosable graph is also $2m$-choosable.

Formulated differently, the question is to know whether every $(a:b)$-choosable graph is also $(c:d)$-choosable whenever $c/d=a/b$ and $c\geq a$. This formulation raises the same question when $c/d>a/b$, which was also asked by Erdős, Rubin and Taylor [2]. About ten years ago, Gutner and Tarsi [3] answered this last question negatively, by studying the *$k$th choice number* of a graph for large values of $k$. More precisely, the *$k$th choice number* of a graph $G$ is $\operatorname{ch}_{:k}(G)$, the least integer $a$ for which $G$ is $(a:k)$-choosable. Their result reads as follows.

**Theorem 1** (Gutner & Tarsi, 2009). *Let $G$ be a graph. For every positive real $\epsilon$, there exists an integer $k_0$ such that $\operatorname{ch}_{:k}(G)\leq k(\chi(G)+\epsilon)$ for every $k\geq k_0$.*

As a direct corollary, one deduces that for all integers $m\geq 3$ and $\ell>m$, there exists a graph that is $(a:b)$-choosable and not $(\ell:1)$-choosable with $\frac{a}{b}=m$. (To see this, one can for example apply Theorem 1 with $\varepsilon=1$ to the disjoint union of a clique of order $m-1$ and a complete balanced bipartite graph with choice number $\ell+1$.)

Another related result that should be mentioned here was obtained by Alon, Tuza and Voigt [1]. They proved that for every graph $G$,

$$
\inf\left\{\frac{a}{b}\,\middle|\,G\text{ is }(a:b)\text{-choosable}\right\}
=
\inf\left\{\frac{a}{b}\,\middle|\,G\text{ is }(a:b)\text{-colorable}\right\}.
$$

In other words, the fractional choice number of a graph equals its fractional chromatic number.

The purpose of our work is to provide a negative answer to Erdős, Rubin and Taylor’s question when $a=4$ and $b=1$.

**Theorem 2.** *There exists a graph $G$ that is $4$-choosable, but not $(8:2)$-choosable.*

We build such a graph by incrementally combining pieces with certain properties. Each piece is defined, and its relevant properties established, in the forthcoming lemmas.

Figure 1: The gadget $(C,L_0)$ of Lemma 3 is depicted on the left; the gadget $(G_1,L_1)$ of Corollary 4 is depicted on the right.

[[figure: The title “A 4-CHOOSABLE GRAPH THAT IS NOT (8 : 2)-CHOOSABLE” appears above two annotated graph diagrams: the 5-cycle gadget $(C,L_0)$ is on the left, and the gadget $(G_1,L_1)$, a 5-cycle with the path $v_1xyv_3$, is on the right.]]

**Gadgets and lemmas.** A *gadget* is a pair $(G,L_0)$, where $G$ is a graph and $L_0$ is an assignment of lists of even size. Given a gadget $(G,L_0)$, a *half-list assignment* for $G$ is a list assignment $L$ for $G$ such that $|L(v)|=|L_0(v)|/2$ for every $v\in V(G)$. Let us start the construction by a key observation on list colorings of $5$-cycles.

**Lemma 3.** *Consider the gadget $(C,L_0)$, presented in Figure 1, where $C=v_1v_2v_3v_4v_5$ is a $5$-cycle, $L_0(v_1)=\{1,2,5,6\}$, $L_0(v_2)=\{1,4,5,6\}$, $L_0(v_3)=L_0(v_4)=\{3,4,5,6\}$ and $L_0(v_5)=\{2,4,5,6\}$. Then $C$ is $L$-colorable for every half-list assignment $L$ such that $|L(v_1)\cap L(v_3)|\leq 1$, but $C$ is not $(L_0:2)$-colorable.*

*Proof.* The first statement is well known, but let us give the easy proof for completeness: since $|L(v_1)\cap L(v_3)|\leq 1$, we have $|L(v_1)\cup L(v_3)|\geq 3$, and thus $L(v_1)$ or $L(v_3)$ contains a color $c_6$ not belonging to $L(v_2)$. By symmetry, we can assume that $c_6\in L(v_1)$. We color $v_1$ by $c_6$ and then for $i=5,4,3,2$ in order, we color $v_i$ by a color $c_i\in L(v_i)\setminus\{c_{i+1}\}$. The resulting coloring is proper—we have $c_2\neq c_6$, since $c_6\notin L(v_2)$.

Suppose now that $C$ has an $(L_0:2)$-coloring, and for $c\in\{1,\ldots,6\}$ let $V_c$ be the set of vertices of $C$ on which the color $c$ is used. Since two colors are used on each vertex of $C$, we have $\sum_{c=1}^{6}|V_c|=10$. On the other hand, $V_c$ is an independent set of a $5$-cycle, and thus $|V_c|\leq 2$ for every color $c$. Furthermore, color 1 only appears in the lists of $v_1$ and $v_2$, which are adjacent in $C$. It follows that $|V_1|\leq 1$. The situation is similar for color 2, which appears only in the lists of $v_1$ and $v_5$, and also for color 3, which only appears in the lists of $v_3$ and $v_4$. Consequently, $\sum_{c=1}^{6}|V_c|\leq 3\cdot 2+3\cdot 1=9$, which is a contradiction. $\square$

**Corollary 4.** *Consider the gadget $(G_1,L_1)$, presented in Figure 1, where $G_1$ consists of a $5$-cycle $C=v_1v_2v_3v_4v_5$ and a path $v_1xyv_3$, with $L_1(v_1)=L_1(v_3)=\{1,\ldots,6\}$, $L_1(v_2)=\{1,4,5,6\}$, $L_1(v_4)=\{3,4,5,6\}$, $L_1(v_5)=\{2,4,5,6\}$, $L_1(x)=\{1,2,3,4\}$ and $L_1(y)=\{1,2\}$. Then $G_1$ is $L$-colorable for every half-list assignment $L$ such that $L(v_1)=L(v_3)$, but $G_1$ is not $(L_1:2)$-colorable.*

*Proof.* Let $L$ be a half-list assignment for $G_1$. First $L$-color $y$ and $x$ by colors $c_y\in L(y)$ and $c_x\in L(x)\setminus\{c_y\}$, respectively. Since $c_x\neq c_y$ and $L(v_1)=L(v_3)$, there exist sets $L'(v_1)\subseteq L(v_1)\setminus\{c_x\}$ and $L'(v_3)\subseteq L(v_3)\setminus\{c_y\}$ of size two such that $L'(v_1)\ne L'(v_3)$. Let $L'(v_i)=L(v_i)$ for $i\in\{2,4,5\}$. Lemma 3 implies that $C$ is $L'$-colorable, which yields an $L$-coloring of $G$.

In an $(L_1:2)$-coloring, the vertex $y$ would have to be assigned $\{1,2\}$ and $x$ would have to be assigned $\{3,4\}$, and thus the sets of available colors for $v_1$ and for $v_3$ would have to be $\{1,2,5,6\}$ and $\{3,4,5,6\}$, respectively. However, no such $(L_1:2)$ coloring of $C$ exists according to Lemma 3. $\square$

Next we construct auxiliary gadgets, which will be combined with the gadget from Corollary 4 to deal with the case where $L(v_1)\ne L(v_3)$. Let $G$ be a graph, let $S$ be a subset of vertices of $G$ and $L$ a list assignment for $G$. An $L$-coloring of $S$ is a coloring of the subgraph of $G$ induced by $S$. Moreover, if $S'$ is a subset of vertices of $G$ that contains $S$ and $\varphi'$ is an $L$-coloring of $S'$, then $\varphi'$ extends $\varphi$ if $\varphi'|_S=\varphi$. Let $(G,L_0)$ be a gadget, let $v_1$ and $v_3$ be distinct vertices of $G$, and let $S$ be a set of vertices of $G$ not containing $v_1$ and $v_3$. The gadget is $(v_1,v_3,S)$-relaxed if every half-list assignment $L$ satisfies at least one of the following conditions.

(i) There exists an $L$-coloring $\psi_0$ of $\{v_1,v_3\}$ such that every $L$-coloring of $S\cup\{v_1,v_3\}$ extending $\psi_0$ extends to an $L$-coloring of $G$.

(ii) $L(v_1)=L(v_3)$ and there exists an $L$-coloring $\psi_0$ of $S$ such that every $L$-coloring of $S\cup\{v_1,v_3\}$ extending $\psi_0$ extends to an $L$-coloring of $G$.

Figure 2: The gadget $(G_2,L_2)$ of Lemma 5

[[figure: Diagram of the gadget $(G_2,L_2)$ showing the 5-cycle $v_1u_2v_3u_4u_5$, vertex $y_1$ joined to the cycle, triangle $y_2y_3y_4$ below, and list labels at the vertices.]]

**Lemma 5.** Consider the gadget $(G_2,L_2)$ presented in Figure 2, where $G_2$ consists of a 5-cycle $C_2=v_1u_2v_3u_4u_5$, a vertex $y_1$ adjacent to all vertices of $C_2$, a triangle $y_2y_3y_4$, and an edge $y_1y_2$, with $L_2(v)=\{1,\ldots,6\}$ for every $v\in V(C_2)$, $L_2(y_1)=\{1,\ldots,8\}$, $L_2(y_2)=L_2(y_4)=\{1,2,3,4,7,8\}$, and $L_2(y_3)=\{1,2,3,4\}$. The gadget is $(v_1,v_3,\{y_4\})$-relaxed, and $\varphi(y_4)\cap\{7,8\}\ne\varnothing$ for every $(L_2:2)$-coloring $\varphi$ of $G_2$.

*Proof.* Let $L$ be a half-list assignment for $G_2$. If not all vertices of $C_2$ have the same list, then choose a color $c\in L(y_1)\setminus L(y_2)$, and observe there exists an $L$-coloring of $G_2[V(C_2)\cup\{y_1\}]$ such that $y_1$ has color $c$. Let $\psi_0$ be the restriction of this coloring to $\{v_1,v_3\}$. Clearly, every $L$-coloring of $\{v_1,v_3,y_4\}$ extending $\psi_0$ extends to an $L$-coloring of $G_2$, and thus (i) holds.

If all the vertices of $C_2$ have the same list (and hence in particular $L(v_1)=L(v_3)$), then let $c$ be a color in $L(y_1)\setminus L(v_1)$. Observe that there exists an $L$-coloring of $G_2[\{y_1,y_2,y_3,y_4\}]$ such that $y_1$ has color $c$. Let $\psi_0$ be the restriction of this coloring to $y_4$. Again, every $L$-coloring of $\{v_1,v_3,y_4\}$ extending $\psi_0$ extends to an $L$-coloring of $G_2$, and thus (ii) holds.

It remains to show that if $\varphi$ is an $(L_2:2)$-coloring of $G_2$ then $\varphi(y_4)\cap\{7,8\}\ne\varnothing$. Suppose, on the contrary, that $\varphi(y_4)\cap\{7,8\}=\varnothing$. It follows that $\varphi(y_4)\cup\varphi(y_3)=\{1,2,3,4\}$, and hence $\varphi(y_2)=\{7,8\}$. As a result, $\varphi(y_1)\subseteq\{1,\ldots,6\}$ and, by symmetry, we can assume that $\varphi(y_1)=\{5,6\}$. This implies that $\varphi(v)\subseteq\{1,2,3,4\}$ for each $v\in V(C_2)$. In particular, $\varphi|V(C_2)$ is a $(4:2)$-coloring of $C_2$, which is a contradiction since the $5$-cycle $C_2$ has fractional chromatic number $5/2$.

**Figure 3:** The graph $G_3$ from Lemma 6 is depicted on the left; the gadget $(G_3,L_3)$ is obtained from $(G_2,L_2)$ by adding to $G_3$ a disjoint copy of the graph depicted on the right (with the corresponding lists) for each $i\in\{1,2\}$, and joining $y_4$ to each of $z_{1,1},z_{1,2},z_{2,1}$ and $z_{2,2}$.

[[figure: diagram of the graph $G_3$ on the left and the corresponding list gadget on the right]]

**Lemma 6.** *Consider the gadget $(G_3,L_3)$, obtained from the gadget $(G_2,L_2)$ of Lemma 5 as follows (see Figure 3 for an illustration of $G_3$). The graph $G_3$ consists of $G_2$ and for $i\in\{1,2\}$, the vertices $z_{i,1},\ldots,z_{i,7}$; the edges $y_4z_{i,1}$ and $y_4z_{i,2}$; the edge $z_{i,j}z_{i,k}$ for every $j$ and every $k$ such that $1\leq j<k\leq 4$ and $(j,k)\ne(1,2)$; the edges of the triangle $z_{i,5}z_{i,6}z_{i,7}$ and the edge $z_{i,4}z_{i,5}$. Let $L_3(v)=L_2(v)$ for $v\in V(G_2)$, and for $i\in\{1,2\}$ let $L_3(z_{i,1})=\{1,2,3,6+i\}$, $L_3(z_{i,2})=\{4,5,6,6+i\}$, $L_3(z_{i,3})=\{1,\ldots,6\}$, $L_3(z_{i,4})=\{1,\ldots,8\}$, $L_3(z_{i,5})=L_3(z_{i,7})=\{1,2,3,4,7,8\}$ and $L_3(z_{i,6})=\{1,2,3,4\}$. The gadget $(G_3,L_3)$ is $(v_1,v_3,\{z_{1,7},z_{2,7}\})$-relaxed, and $\varphi(z_{1,7})=\{7,8\}$ or $\varphi(z_{2,7})=\{7,8\}$ for every $(L_3:2)$-coloring $\varphi$ of $G_3$.*

*Proof.* Let $L$ be a half-list assignment for $G_3$. The gadget $(G_2,L_3|V(G_2))$ is $(v_1,v_3,\{y_4\})$-relaxed by Lemma 5. Suppose first that (i) holds for the restriction of $L$ to $G_2$ (with $S=\{y_4\}$), and let $\psi_0$ be the corresponding $L$-coloring of $\{v_1,v_3\}$. For $i\in\{1,2\}$, if $L(z_{i,1})\cap L(z_{i,2})\ne\varnothing$, then let $c_i$ be a color in $L(z_{i,1})\cap L(z_{i,2})$. Otherwise, $|L(z_{i,1})\cup L(z_{i,2})|=4>|L(z_{i,3})|$, and thus we can choose a color $c_i\in(L(z_{i,1})\cup L(z_{i,2}))\setminus L(z_{i,3})$. Let $c$ be a color in $L(y_4)\setminus\{c_1,c_2\}$. By (i) for $G_2$, we know that $\psi_0$ extends to an $L$-coloring $\psi$ of $G_2$ such that $\psi(y_4)=c$. If $L(z_{i,1})\cap L(z_{i,2})\ne\varnothing$, then color both $z_{i,1}$ and $z_{i,2}$ by $c_i$, otherwise color one of them by $c_i$ and the other one by an arbitrary color from its list that is different from $c$. There are at least two colors in $L(z_{i,4})$ distinct from the colors of $z_{i,1}$ and $z_{i,2}$, choose such a color $c'_i$ so that $L(z_{i,5}) \setminus \{c'_i\} \ne L(z_{i,6})$. Color $z_{i,4}$ by $c'_i$ and extend the coloring to $z_{i,3}$, which is possible by the choice of $c_i$. Observe that any $L$-coloring of $z_{i,7}$ extends to an $L$-coloring of the triangle $z_{i,5}z_{i,6}z_{i,7}$ where the color of $z_{i,5}$ is not $c'_i$. We conclude that $(G_3,L_3)$ with the half-list assignment $L$ satisfies (i). $\square$

Suppose next that (ii) holds for the restriction of $L$ to $G_2$ (with $S=\{y_4\}$), and let $\psi'_0$ be the corresponding $L$-coloring of $y_4$. For $i\in\{1,2\}$, greedily extend $\psi'_0$ to an $L$-coloring of $z_{i,1},\ldots,z_{i,7}$ in order, and let $\psi_0$ be the restriction of the resulting coloring to $\{z_{1,7},z_{2,7}\}$. Observe that $(G_3,L_3)$ with the half-list assignment $L$ satisfies (ii).

Finally, let $\varphi$ be an $(L_3 : 2)$-coloring of $G_3$. Lemma 5 implies that $\varphi(y_4)\cap\{7,8\}\ne\varnothing$. By symmetry, we can assume that $7\in\varphi(y_4)$. It follows that $\varphi(z_{1,1})\subset\{1,2,3\}$ and $\varphi(z_{1,2})\subset\{4,5,6\}$, and thus $\varphi(z_{1,1})\cup\varphi(z_{1,2})\cup\varphi(z_{1,3})=\{1,\ldots,6\}$. Consequently, $\varphi(z_{1,4})=\{7,8\}$, and $\varphi(z_{1,5})$ is a subset of $\{1,2,3,4\}$. This yields that $\varphi(z_{1,5})\cup\varphi(z_{1,6})=\{1,2,3,4\}$, and therefore $\varphi(z_{1,7})=\{7,8\}$. $\square$

**Figure 4:** The graph $G_4$ from Lemma 7: the filled vertices are those added to $G_3$ to form $G_4$; the red ones have list $\{1,2,3,4,7,8\}$ while the black ones have list $\{1,2,3,4\}$.

[[figure: Diagram of the graph $G_4$ with labeled vertices and edges; added vertices are filled red or black, with their lists indicated.]]

**Lemma 7.** *Consider the gadget $(G_4,L_4)$ obtained from the gadget $(G_3,L_3)$ of Lemma 6 as follows (see Figure 4 for an illustration of $G_4$). The graph $G_4$ consists of $G_3$; the three triangles $w_1w_2w_3$ and $w_{i,1}w_{i,2}w_{i,3}$ for $i\in\{1,2\}$; and the edges $z_{1,7}w_1$, $z_{2,7}w_1$, $w_3w_{1,1}$ and $w_3w_{2,1}$. Let $L_4(v)=L_3(v)$ for $v\in V(G_3)$, and for $i\in\{1,2\}$, let $L_4(w_1)=L_4(w_3)=L_4(w_{i,1})=L_4(w_{i,3})=\{1,2,3,4,7,8\}$ and $L_4(w_2)=L_4(w_{i,2})=\{1,2,3,4\}$. The gadget is $(v_1,v_3,\{w_{1,3},w_{2,3}\})$-relaxed, and $\varphi(w_{1,3})=\varphi(w_{2,3})=\{7,8\}$ for every $(L_4 : 2)$-coloring $\varphi$ of $G_4$.*

*Proof.* Let $L$ be a half-list assignment for $G_4$. The gadget $(G_3,L_4|V(G_3))$ is $(v_1,v_3,\{z_{1,7},z_{2,7}\})$-relaxed by Lemma 6. Suppose first that (i) holds for the restriction of $L$ to $G_3$ (with $S=\{z_{1,7},z_{2,7}\}$), and let $\psi_0$ be the corresponding $L$-coloring of $\{v_1,v_3\}$. Choose a color $c_1\in L(z_{1,7})$ so that $L(w_1)\setminus\{c_1\}\ne L(w_2)$. If $c_1\in L(w_1)$, then choose $c_2\in L(z_{2,7})\setminus(L(w_1)\setminus\{c_1\})$, otherwise choose $c_2\in L(z_{2,7})$ so that $L(w_1)\setminus\{c_2\}\ne L(w_2)$. Choose a color $c_3\in L(w_3)$ so that $L(w_{i,1})\setminus\{c_3\}\ne L(w_{i,2})$ for $i\in\{1,2\}$. By (i) for $G_3$, there exists an $L$-coloring of $G_3$ extending $\psi_0$ and assigning $c_i$ to $z_{i,7}$ for each $i\in\{1,2\}$. Color $w_3$ by $c_3$ and observe that the $L$-coloring can be extended to $w_1$ and $w_2$ thanks to the choice of $c_1$ and $c_2$. Moreover, the choice of $c_3$ ensures that for each $i\in\{1,2\}$, we can color $w_{i,3}$ with any color in $L(w_{i,3})$ and further extend the coloring to $w_{i,1}$ and $w_{i,2}$. We conclude that $(G_4,L_4)$ with the half-list assignment $L$ satisfies (i).

Suppose next that (ii) holds for the restriction of $L$ to $G_4$ (with $S=\{z_{1,7},z_{2,7}\}$), and let $\psi'_0$ be the corresponding $L$-coloring of $\{z_{1,7},z_{2,7}\}$. Greedily extend $\psi'_0$ to an $L$-coloring of $w_1$, $w_2$, $w_3$, and $w_{i,1}$, $w_{i,2}$, $w_{i,3}$ for $i\in\{1,2\}$ in order, and let $\psi_0$ be the restriction of the resulting coloring to $\{w_{1,3},w_{2,3}\}$. Observe that $(G_4,L_4)$ with the half-list assignment $L$ satisfies (ii).

Finally, let $\varphi$ be an $(L_4:2)$-coloring of $G_4$. By Lemma 6 and by symmetry, we can assume that $\varphi(z_{1,7})=\{7,8\}$. Consequently, $\varphi(w_1)\subset\{1,2,3,4\}$, and thus $\varphi(w_1)\cup\varphi(w_2)=\{1,2,3,4\}$, which yields that $\varphi(w_3)=\{7,8\}$. We conclude analogously that $\varphi(w_{1,3})=\{7,8\}=\varphi(w_{2,3})$. $\square$

Figure 5: The graph $G_5$ from Lemma 8.

[[figure: labeled graph $G_5$ with several triangular subgraphs connected by long curved edges]]

We can now combine $(G_1,L_1)$ with $(G_4,L_4)$ to obtain a gadget $(G_5,L_5)$ that is $L$-colorable from each half-list assignment $L$, but not $(L_5:2)$-colorable.

**Lemma 8.** *Consider the gadget $(G_5,L_5)$ obtained from the gadgets $(G_1,L_1)$ of Corollary 4 and $(G_4,L_4)$ of Lemma 7 as follows (see Figure 5 for an illustration of $G_5$). The graph $G_5$ is obtained from the union of the graphs $G_1$ and $G_4$ (intersecting in $\{v_1,v_3\}$) by adding the edges $w_{1,3}v_2$, $w_{1,3}v_4$, $w_{2,3}x$ and $w_{2,3}y$. Let $L_5(v)=L_4(v)$ for $v\in V(G_4)$, $L_5(v)=L_1(v)$ for $v\in V(G_1)\setminus\{v_2,v_4,x,y\}$, and $L_5(v)=L_1(v)\cup\{7,8\}$ for $v\in\{v_2,v_4,x,y\}$. Then $G_5$ is $L$-colorable for every half-list assignment $L$, but not $(L_5:2)$-colorable.*

*Proof.* Let $L$ be a half-list assignment for $G_5$. The gadget $(G_4,L_5|V(G_4))$ is $(v_1,v_3,\{w_{1,3},w_{2,3}\})$-relaxed by Lemma 7. Suppose first that (i) holds for the restriction of $L$ to $G_4$ (with $S=\{w_{1,3},w_{2,3}\}$), and let $\psi_0$ be the corresponding $L$-coloring of $\{v_1,v_3\}$. Greedily extend $\psi_0$ to an $L$-coloring $\psi$ of $G_1$. Choose $c_1\in L(w_{1,3})\setminus\{\psi(v_2),\psi(v_4)\}$ and $c_2\in L(w_{2,3})\setminus\{\psi(x),\psi(y)\}$. By (i) for $G_4$, there exists an $L$-coloring of $G_4$ that extends $\psi_0$ and assigns to $w_{i,3}$ the color $c_i$ for each $i\in\{1,2\}$. This yields, together with $\psi$, an $L$-coloring of $G_5$.

Suppose next that (ii) holds for the restriction of $L$ to $G_4$ (with $S=\{w_{1,3},w_{2,3}\}$), and let $\psi_0$ be the corresponding $L$-coloring of $\{w_{1,3},w_{2,3}\}$. Note that $L(v_1)=L(v_3)$ in this case. Corollary 4 implies that $G_1$ has an $L$-coloring $\psi$ such that $\psi(v_2)\in L(v_2)\setminus\{\psi_0(w_{1,3})\}$, $\psi(v_4)\in L(v_4)\setminus\{\psi_0(w_{1,3})\}$, $\psi(x)\in L(x)\setminus\{\psi_0(w_{2,3})\}$, and $\psi(y)\in L(y)\setminus\{\psi_0(w_{2,3})\}$. By (ii), the restriction of $\psi\cup\psi_0$ to $\{v_1,v_3,w_{1,3},w_{2,3}\}$ extends to an $L$-coloring of $G_4$, which together with $\psi$ gives an $L$-coloring of $G_5$.

It remains to show that $G_5$ is not $(L_5:2)$-colorable. If $\varphi$ were an $(L_5:2)$-coloring of $G_5$, then by Lemma 7 we would have $\varphi(w_{1,3})=\varphi(w_{2,3})=\{7,8\}$, and thus the restriction of $\varphi$ to $G_1$ would be an $(L_1:2)$-coloring, thereby contradicting Corollary 4. $\square$

**The final graph.** We are now in a position to prove Theorem 2 by simply using a standard construction to ensure uniform lengths of lists.

*Proof of Theorem 2.* Let $G$ be a graph and $L^{\prime}$ an assignment of lists of size $8$ obtained as follows. Let $K$ be a clique with vertices $r_1,\ldots,r_4$, and let $L^{\prime}(r_1)=\cdots=L^{\prime}(r_4)=\{9,\ldots,16\}$. For every $(L^{\prime}:2)$-coloring $\psi$ of $K$, let $G_\psi$ be a copy of the graph $G_5$ from the gadget $(G_5,L_5)$ of Lemma 8, and for each vertex $v\in V(G_\psi)$ such that $|L_5(v)|=2k$ with $k\in\{2,3\}$, we add the edges $vr_1,\ldots,vr_{4-k}$ and let $L^{\prime}(v)=L_5(v)\cup\bigcup_{i=1}^{4-k}\psi(r_i)$. If $G$ had an $(L^{\prime}:2)$-coloring $\varphi$, then letting $\psi$ be the restriction of $\varphi$ to $K$, the restriction of $\varphi$ to $G_\psi$ would be an $(L_5:2)$-coloring of $G_5$, thereby contradicting Lemma 8.

Consider now a list assignment $L$ for $G$ such that $|L(v)|=4$ for every $v\in V(G)$. Let $\varphi$ be any $L$-coloring of $K$. For each $(L^{\prime}:2)$-coloring $\psi$ of $K$, let $L_\psi$ be the list assignment for $G_\psi$ obtained by, for each $v\in V(G_\psi)$, removing the colors of neighbors in $K$ according to $\varphi$, and possibly removing further colors to ensure that $|L_\psi(v)|=|L_5(v)|/2$. By Lemma 8, the graph $G_\psi$ has an $L_\psi$-coloring. The union of these colorings and $\varphi$ yields an $L$-coloring of $G$. $\square$

**Concluding remarks.** It follows from Theorem 2 that for each integer $a\geq 4$, there exists a graph $G_a$ that is $a$-choosable but not $(2a:2)$-choosable—if we have such a graph $G_a$, taking the disjoint union of $\binom{2(a+1)}{2}$ copies of $G_a$ and adding a vertex adjacent to all other vertices yields $G_{a+1}$, by an argument analogous to the list uniformization procedure used for the proof of Theorem 2. It is natural to ask whether there exists a graph that is 3-choosable but not $(6:2)$-choosable. We believe this to be the case; in particular, Corollary 4 only requires lists of size at most 6. However, it does not seem easy to construct a gadget that satisfies the properties stated in Lemma 5 without using a vertex with a list of size 8.

## References

[1] N. Alon, Z. Tuza and M. Voigt. Choosability and fractional chromatic numbers. *Discrete Mathematics*, 165/166:31–38, 1997. Graphs and Combinatorics (Marseille, 1995). 2

[2] P. Erdős, A. L. Rubin and H. Taylor. Choosability in graphs. *Congressus Numerantium*, XXVI:125–157, 1980. West Coast Conference on Combinatorics, Graph Theory and Computing (Humboldt State Univ., Arcata, Calif., 1979). 1, 2

[3] S. Gutner and M. Tarsi. Some results on $(a\colon b)$-choosability. *Discrete Mathematics*, 309:2260–2270, 2009. 2

[4] Z. Tuza and M. Voigt. Every 2-choosable graph is $(2m,m)$-choosable. *Journal of Graph Theory*, 22:245–252, 1996. 2

AUTHORS

Zdeněk Dvořák\
Associate Professor\
Computer Science Institute (CSI) of Charles University\
Prague, Czech Republic\
rakdver@iuuk.mff.cuni.cz\
https://iuuk.mff.cuni.cz/~rakdver/

Xiaolan Hu\
Assistant Professor\
School of Mathematics and Statistics $\&$ Hubei Key Laboratory of Mathematical Sciences\
Central China Normal University, Wuhan, PR China.\
xlhu@mail.ccnu.edu.cn\
http://maths.ccnu.edu.cn/info/1042/15221.htm

Jean-Sébastien Sereni\
Directeur de recherche\
Centre National de la Recherche Scientifique\
CSTB (ICube), Strasbourg, France.\
sereni@kam.mff.cuni.cz\
http://lbgi.fr/~sereni/index.html
