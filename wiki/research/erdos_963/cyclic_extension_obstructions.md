---
name: research/erdos_963/cyclic_extension_obstructions
title: 'Further obstructions to cyclic lifting arguments'
desc: An odd-only quotient drop of two and an inconsistent prescribed doubled lift; neither contradicts the target.
tags: []
sources: []
created: 2026-09-19T00:40:00Z
updated: 2026-09-19T00:40:00Z
---


# Further obstructions to cyclic lifting arguments

***

The sufficient cyclic assertions in [[research/erdos_963/proof_sketch|the proof
sketch]] remain unproved. These exact examples show why two possible repairs of
the lifting step do not work. They are not counterexamples to the real-number
bound.

## A quotient drop of two with all entries odd

Let

$$
D=\{9,25,37,61,65,85\}\subset\mathbb Z/128\mathbb Z.
$$

Then $d_{128}(D)=6$, but its image modulo $64$ has dimension four.

All six entries are $1\pmod4$. A possible ternary zero relation has
support four or six. It must be balanced, an all-plus four-relation,
or a five-versus-one six-relation. (Two-term relations are excluded by
the entries being distinct and all (1\pmod4\).)

The twenty triple sums modulo $128$ are distinct:

$$
3,7,19,23,27,31,35,43,47,55,
59,71,83,95,99,107,111,119,123,127.
$$

This excludes balanced relations. In particular, any equality of two
disjoint pair sums could be extended by a common unused element to an
equality of two triple sums.

The total is $282\equiv26\pmod{128}$. The pair sums are

$$
18,22,34,46,62,70,74,86,90,94,98,102,110,122,126,
$$

none congruent to $26$. Hence no four elements sum to zero. A
five-versus-one relation would require $2a\equiv26\pmod{128}$, or
$a\equiv13,77$, neither present. This proves dissociation modulo $128$.

Modulo $64$, the four relations

$$
\begin{aligned}
25-65+37-61&=-64,\\
25-65+61-85&=-64,\\
25-37-9+85&=64,\\
37+9+61+85&=192
\end{aligned}
$$

exclude every five-subset. Their omitted pairs are, respectively,
$\{9,85\},\{9,37\},\{61,65\},\{25,65\}$, covering all six possible
omitted points. The quadruple $\{9,25,37,65\}$ is dissociated modulo
$64$: its pair-sum residues are $10,26,34,38,46,62$, all distinct,
and its total is $136\equiv8\ne0$. Since its entries are $1\pmod4$,
these checks exclude every possible relation.

Thus the earlier quotient-drop obstruction cannot be repaired just by
requiring the original set to be odd.

## A prescribed doubled lift need not be consistent

The set

$$
T=\{5,15,25,27,41\}\subset\mathbb Z/64\mathbb Z
$$

is dissociated. Nevertheless no choices of lifts of $5,25,27,41$
to $\mathbb Z/128\mathbb Z$ give a dissociated set together with both
$15$ and $79$.

For the dissociation certificate, change signs individually to obtain
$\{5,25,37,41,49\}$. Its entries are $1\pmod4$. Its ten pair sums
modulo $64$ are the distinct residues

$$
2,10,14,22,26,30,42,46,54,62,
$$

and its five four-element sums are $4,24,44,52,56$, all nonzero.
These exclude the balanced and all-plus four-relations, the only
possible relations.

The two identities

$$
2(15)+25+41-5-27=64,\qquad
2(15)+25+41+5+27=128
$$

make the lifting contradiction direct. Write the chosen lift of each
other element $a$ as $a+64s_a$. Using both $15$ and $79$
with positive coefficients adds $64$ to the displayed left sides.
To avoid a zero relation modulo $128$, the first identity requires

$$
s_{25}+s_{41}+s_5+s_{27}=1\pmod2,
$$

whereas the second requires the same sum to be zero. They are
inconsistent.

This refutes consistency for a **prescribed** doubled element. It does
not rule out doubling another element or changing the projected
dissociated subset, and it does not give the joint fiber bound needed
by the cardinality induction.

## A different sufficient cyclic assertion

For a finite cyclic group call $A$ skew if $0\notin A$ and
$A\cap(-A)=\varnothing$. The assertion

$$
|A|\le2^{d(A)}-1\quad\text{for every skew subset of an odd cyclic group}
                                                               \tag{1}
$$

would imply the stronger positive odd bound. Indeed, if $M=\max O$
for a positive odd integer set $O$, its other elements give distinct
nonzero skew residues modulo $M$. Two of them cannot sum to $M$,
since that sum is even and $M$ is odd. Any modularly dissociated
subset of these residues can be adjoined to $M$ over the reals.
Thus its modular dimension is at most $d(O)-1$, and (1) would yield


$$
|O|-1\le2^{d(O)-1}-1.
$$


Assertion (1) remains unproved here. It cannot be generalized to all
finite abelian odd-order groups: the nonzero sign-classes of
$\mathbb F_3^r$ have cardinality $(3^r-1)/2$ and dissociation
dimension $r$, violating (1) for $r\ge3$. No cyclic counterexample
or real-number counterexample was obtained.
