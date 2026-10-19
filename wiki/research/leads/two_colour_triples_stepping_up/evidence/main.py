"""Finite checks of explicit obstructions and a prefix-selected routing table.

The obstructions on the owning research pages are proved there for every
dimension M and every rule; this driver checks their explicit constructions on
deterministic instances, recomputing the colour of every triple from the rule
and the actual binary words:

1. Bounded-query rules on {0,1}^M: 24 rules reading random query sets of
   w=0,1,2 positions (M=14,16) and 16 rules reading windows of radius 1 or 2
   around the two deltas (M=20,26). For each: a spread label set, the
   canonical values F(p,q,side,eta), and the red and blue trees of the
   product inequality (labels repeated where the proof allows), checking that
   their sizes multiply to more than |Lambda|, that no two demands on an
   outsider bit disagree, and that every triple of the realized words has the
   tree's colour. Also the two extreme cases: the subcube on a clique of pairs
   whose four values are all red (RR4), the blue greedy tree on an
   RR4-independent set, the mirror pair for blue, and |Lambda| <
   (alpha+1)^omega for RR4. Two controls per rule: it takes both colours, and
   a square on a pair with mixed values is not monochromatic.
2. Prefix rules: 12 rules that also read the common prefix above the upper
   delta (in the mode as well as the colour). The product sets are built with
   contexts (fixed bits pushed down the recursion) and every triple is
   recoloured; a control checks that the construction without contexts fails
   for some of these rules, so the prefix dependence is exercised.
3. All 256 outsider-bit tables over two seed graphs on 16 labels: an explicit
   monochromatic set of at least ceil(sqrt(16))=4 words, and of 17 words
   whenever some colour is achievable on every label pair.
4. Copy-squaring of a seed colouring of the triples of a 14-point set with a
   planted red 7-set: explicit monochromatic sets of 2(k-1) points for the
   bottoms rule (fat-thin) and the outsider-top rule (fat-fat), where k is the
   seed's largest monochromatic size, found by exhaustive search.
5. The retained prefix_selector_16.json table: its exact domain, all 560
   triple colours, all 4,368 five-sets, both monochromatic four-set witnesses,
   and a triple where the prefix changes the queried position and colour.
   A prefix-independent one-query control also has largest sets of size four;
   the positive instance does not establish an advantage from the prefix.
   This checks the witness only, not the finite synthesis procedure.
6. The prefix-selected XOR obstruction: deterministic sparse label sets for
   four routing families in dimensions 64, 512, 4096 and 32768, in each
   colour. Check the no-bad-pair property, the prefix computed using only
   higher labels, and every triple of the resulting distinct-label tree.

Exact integer arithmetic; pseudo-randomness comes from BLAKE2b of fixed
strings, so every run is identical. Runtime: about a second. The universal
statements (every M, every rule, every seed) are not checked here; they rest
on the proofs on the pages.
"""

from __future__ import annotations

import hashlib
import json
import sys
from collections.abc import Callable
from itertools import combinations
from math import comb, isqrt
from pathlib import Path

from tools import Checker, evidence_parser

RED, BLUE = 0, 1
SIDES = ('L', 'R')
Colour = Callable[[int, int, int], int]
Node = tuple[int, 'Node | None', 'Node | None']


def hbit(*parts: object) -> int:
    """Return a deterministic pseudo-random bit keyed by the given parts."""
    digest = hashlib.blake2b(repr(parts).encode(), digest_size=8).digest()
    return digest[0] & 1


def hval(modulus: int, *parts: object) -> int:
    """Return a deterministic pseudo-random residue modulo ``modulus``."""
    digest = hashlib.blake2b(repr(parts).encode(), digest_size=8).digest()
    return int.from_bytes(digest, 'big') % modulus


def delta(x: int, y: int) -> int:
    """Return the most significant position where two distinct words differ."""
    return (x ^ y).bit_length() - 1


def is_monochromatic(words: list[int], colour: Colour, target: int) -> bool:
    """Recompute every triple's colour and compare it with ``target``."""
    ordered = sorted(words)
    return all(colour(x, y, z) == target for x, y, z in combinations(ordered, 3))


def max_clique(vertices: list[int], adjacent: Callable[[int, int], bool]) -> list[int]:
    """Return a largest clique of a small graph by exhaustive branching."""
    best: list[int] = []

    def extend(current: list[int], candidates: list[int]) -> None:
        nonlocal best
        if len(current) > len(best):
            best = list(current)
        for index, vertex in enumerate(candidates):
            if len(current) + len(candidates) - index <= len(best):
                return
            rest = [u for u in candidates[index + 1 :] if adjacent(vertex, u)]
            extend([*current, vertex], rest)

    extend([], list(vertices))
    return best


class QueryRule:
    """A bounded-query colouring: (a, b) and the bits at W(a,b) | {a,b}."""

    def __init__(
        self, seed: str, size: int, width: int, window: bool, prefix: bool = False
    ) -> None:
        """Fix the query sets: windows of the given radius, or random sets."""
        self.seed, self.size, self.width, self.prefix = seed, size, width, prefix
        self.queries: dict[tuple[int, int], tuple[int, ...]] = {}
        for a in range(size):
            for b in range(size):
                if a != b and window:
                    near = {a + d for d in range(-width, width + 1)}
                    near |= {b + d for d in range(-width, width + 1)}
                    self.queries[(a, b)] = tuple(sorted(near & set(range(size))))
                elif a != b:
                    chosen: set[int] = set()
                    salt = 0
                    while len(chosen) < width:
                        chosen.add(hval(size, seed, 'W', a, b, salt))
                        salt += 1
                    self.queries[(a, b)] = tuple(sorted(chosen))

    def mode(self, a: int, b: int, common: int = 0) -> int:
        """Return 0 (constant red), 1 (constant blue) or 2 (pattern-dependent)."""
        return hval(10, self.seed, 'mode', min(a, b), max(a, b), common) % 3

    def __call__(self, x: int, y: int, z: int) -> int:
        """Colour the triple x<y<z from its deltas and its queried bits."""
        a, b = delta(x, y), delta(y, z)
        common = x >> (max(a, b) + 1) if self.prefix else 0
        mode = self.mode(a, b, common)
        if mode < 2:
            return mode
        positions = sorted(set(self.queries[(a, b)]) | {a, b})
        pattern = tuple(((x >> i) & 1, (y >> i) & 1, (z >> i) & 1) for i in positions)
        return hbit(self.seed, 'G', a, b, pattern, common)


def canonical_triple(p: int, q: int, side: str, eta: int) -> tuple[int, int, int]:
    """Words with deltas {q,p} in the given orientation, outsider bit eta at q."""
    if side == 'L':
        return 0, 1 << q, (1 << p) | (eta << q)
    return eta << q, 1 << p, (1 << p) | (1 << q)


def spread_labels(rule: QueryRule) -> list[int]:
    """Choose labels whose query sets meet the chosen set only in the pair.

    Greedy passes over the positions taken in steps of 1 to 6 from each
    offset; the largest valid set is kept.
    """
    best: list[int] = []
    for step in range(1, 7):
        for offset in range(step):
            chosen: list[int] = []
            for p in range(rule.size - 1 - offset, -1, -step):
                trial = [*chosen, p]
                good = True
                for u, v in combinations(trial, 2):
                    for a, b in ((u, v), (v, u)):
                        queried = rule.queries[(a, b)]
                        if any(i in trial and i not in (u, v) for i in queried):
                            good = False
                if good:
                    chosen = trial
            if len(chosen) > len(best):
                best = chosen
    return sorted(best)


def table(colour: Colour, labels: list[int]) -> dict[tuple[int, int], dict]:
    """Return F(p,q,side,eta) for every pair p>q of labels."""
    values = {}
    for p, q in combinations(sorted(labels, reverse=True), 2):
        values[(p, q)] = {
            (side, eta): colour(*canonical_triple(p, q, side, eta))
            for side in SIDES
            for eta in (0, 1)
        }
    return values


def subcube(labels: list[int]) -> list[int]:
    """Return every word supported on the given labels."""
    words = [0]
    for label in labels:
        words += [w | (1 << label) for w in words]
    return words


def greedy_tree_words(labels: list[int], values: dict, target: int) -> list[int]:
    """Build the greedy target-coloured tree on distinct labels as actual words.

    The root is the largest label; a label goes left when the target is
    achievable in orientation L, else right when achievable in orientation R.
    Leaves on one side of a node receive, at each label of the other side, the
    outsider bit that achieves the target for that pair.
    """

    def witness(p: int, q: int, side: str) -> int | None:
        for eta in (0, 1):
            if values[(p, q)][(side, eta)] == target:
                return eta
        return None

    def build(pool: list[int]) -> Node | None:
        if not pool:
            return None
        root, rest = max(pool), [q for q in pool if q != max(pool)]
        left = [q for q in rest if witness(root, q, 'L') is not None]
        right = [q for q in rest if q not in left and witness(root, q, 'R') is not None]
        return root, build(left), build(right)

    def labels_of(node: Node | None) -> list[int]:
        if node is None:
            return []
        return [node[0], *labels_of(node[1]), *labels_of(node[2])]

    def words_of(node: Node | None) -> list[int]:
        if node is None:
            return [0]
        root, left, right = node
        mask_right = sum((witness(root, q, 'L') or 0) << q for q in labels_of(left))
        mask_left = sum((witness(root, q, 'R') or 0) << q for q in labels_of(right))
        return [w | mask_left for w in words_of(left)] + [
            w | (1 << root) | mask_right for w in words_of(right)
        ]

    return words_of(build(labels))


def side_type(values: dict, p: int, q: int, side: str) -> str:
    """Return 'R' or 'B' if both outsider bits give that colour, else 'M'."""
    first, second = values[(p, q)][(side, 0)], values[(p, q)][(side, 1)]
    if first != second:
        return 'M'
    return 'R' if first == RED else 'B'


def product_split(values: dict, r: int, rest: frozenset) -> dict[str, set[int]]:
    """Split the labels below r into the four sets of the product inequality.

    Each label lies in exactly two sets: (R,R) in both red sets, (B,B) in both
    blue sets, otherwise red-left with blue-right when red is possible on the
    left and blue on the right, and red-right with blue-left in the rest.
    """
    sets: dict[str, set[int]] = {'1R': set(), '2R': set(), '1B': set(), '2B': set()}
    for q in rest:
        left, right = side_type(values, r, q, 'L'), side_type(values, r, q, 'R')
        if left == right == 'R':
            sets['1R'].add(q)
            sets['2R'].add(q)
        elif left == right == 'B':
            sets['1B'].add(q)
            sets['2B'].add(q)
        elif left in 'RM' and right in 'BM':
            sets['1R'].add(q)
            sets['2B'].add(q)
        else:
            sets['2R'].add(q)
            sets['1B'].add(q)
    return sets


def product_tree(
    labels: list[int], values: dict, target: int
) -> tuple[int, Node | None]:
    """Return the recursion value and a tree for one colour (labels may repeat)."""
    memo: dict[frozenset, tuple[int, Node | None]] = {}
    key_left, key_right = ('1R', '2R') if target == RED else ('1B', '2B')

    def best(pool: frozenset) -> tuple[int, Node | None]:
        if pool in memo:
            return memo[pool]
        if not pool:
            return 1, None
        r = max(pool)
        rest = pool - {r}
        sets = product_split(values, r, rest)
        left_value, left_tree = best(frozenset(sets[key_left]))
        right_value, right_tree = best(frozenset(sets[key_right]))
        skip_value, skip_tree = best(rest)
        if left_value + right_value >= skip_value:
            result = (left_value + right_value, (r, left_tree, right_tree))
        else:
            result = (skip_value, skip_tree)
        memo[pool] = result
        return result

    return best(frozenset(labels))


def realize(tree: Node | None, values: dict, target: int) -> tuple[list[int], bool]:
    """Realize a tree with repeated labels as words; report demand consistency.

    A leaf's bit at a label q off its path answers every node v labelled q off
    the path: with u the lowest common ancestor of v and the leaf, the bit must
    make F(label(u), q, side of v, bit) the target unless both bits do. The
    second value is False if two such demands on one bit disagree or a demand
    has no answer.
    """
    nodes: list[tuple[int, list[tuple[int, int, int]]]] = []
    leaves: list[list[tuple[int, int, int]]] = []

    def walk(node: Node | None, path: list[tuple[int, int, int]]) -> None:
        if node is None:
            leaves.append(path)
            return
        identity = len(nodes)
        nodes.append((node[0], path))
        walk(node[1], [*path, (identity, node[0], 0)])
        walk(node[2], [*path, (identity, node[0], 1)])

    walk(tree, [])
    used = {label for label, _ in nodes}
    words, consistent = [], True
    for path in leaves:
        turns = {label: turn for _, label, turn in path}
        word = sum(turn << label for label, turn in turns.items())
        for q in used - set(turns):
            demands = set()
            for label, node_path in nodes:
                if label != q:
                    continue
                k = 0
                while node_path[k] == path[k]:
                    k += 1
                upper, side = node_path[k][1], 'L' if node_path[k][2] == 0 else 'R'
                answers = {e for e in (0, 1) if values[(upper, q)][(side, e)] == target}
                if answers != {0, 1}:
                    demands.add(min(answers) if answers else -1)
            if len(demands) > 1 or -1 in demands:
                consistent = False
            word |= (max(demands) if demands else 0) << q
        words.append(word)
    return words, consistent


def context_product_words(
    rule: QueryRule, labels: list[int], target: int
) -> tuple[int, list[int]]:
    """Build the product-inequality set for one colour with contexts.

    A context fixes bits at label positions outside the current label set.
    At the root r of a label set, every label position above r not yet fixed
    is fixed to 0, the canonical table is computed with that prefix, the
    labels are split as in product_split, and the children receive the root
    bit and the outsider-bit demands as context. Words are supported on the
    labels, so the rule's prefix is fully determined at each root.
    """
    memo: dict[tuple, tuple[int, list[int]]] = {}
    key_left, key_right = ('1R', '2R') if target == RED else ('1B', '2B')

    def best(pool: frozenset, context: tuple) -> tuple[int, list[int]]:
        key = (pool, context)
        if key in memo:
            return memo[key]
        fixed = dict(context)
        if not pool:
            word = sum(bit << pos for pos, bit in fixed.items())
            return 1, [word]
        r = max(pool)
        for pos in labels:
            if pos > r and pos not in fixed:
                fixed[pos] = 0
        above = sum(bit << pos for pos, bit in fixed.items() if pos > r)
        values = {}
        for q in pool - {r}:
            values[(r, q)] = {
                (side, eta): rule(
                    *(above | w for w in canonical_triple(r, q, side, eta))
                )
                for side in SIDES
                for eta in (0, 1)
            }
        sets = product_split(values, r, pool - {r})
        left_set, right_set = sets[key_left], sets[key_right]

        def demand(q: int, side: str) -> int:
            answers = [e for e in (0, 1) if values[(r, q)][(side, e)] == target]
            return answers[0] if len(answers) == 1 else 0

        left_context = dict(fixed)
        left_context[r] = 0
        for q in right_set - left_set:
            left_context[q] = demand(q, 'R')
        right_context = dict(fixed)
        right_context[r] = 1
        for q in left_set - right_set:
            right_context[q] = demand(q, 'L')
        left_value, left_words = best(
            frozenset(left_set), tuple(sorted(left_context.items()))
        )
        right_value, right_words = best(
            frozenset(right_set), tuple(sorted(right_context.items()))
        )
        skip_value, skip_words = best(pool - {r}, tuple(sorted(fixed.items())))
        if left_value + right_value >= skip_value:
            result = (left_value + right_value, left_words + right_words)
        else:
            result = (skip_value, skip_words)
        memo[key] = result
        return result

    return best(frozenset(labels), ())


def bounded_query_checks(checker: Checker) -> None:
    """Check the two constructions for 40 bounded-query rules."""
    cases = [(size, width, False) for size in (14, 16) for width in (0, 1, 2)]
    cases += [(size, width, True) for size in (20, 26) for width in (1, 2)]
    for size, width, window in cases:
        for index in range(4):
            kind = 'window radius' if window else 'random w'
            name = f'bq-{size}-{width}-{window}-{index}'
            rule = QueryRule(name, size, width, window)
            labels = spread_labels(rule)
            values = table(rule, labels)
            tag = f'M={size} {kind}={width} rule {index} |Lambda|={len(labels)}'
            everywhere = table(rule, list(range(size)))
            seen = {v for pair in everywhere.values() for v in pair.values()}
            checker.check(f'{tag}: rule takes both colours (control)', seen == {0, 1})
            mixed = [k for k, pair in everywhere.items() if len(set(pair.values())) > 1]
            square = subcube(list(mixed[0])) if mixed else []
            checker.check(
                f'{tag}: a mixed pair gives a non-monochromatic square (control)',
                bool(mixed)
                and not is_monochromatic(square, rule, RED)
                and not is_monochromatic(square, rule, BLUE),
            )
            for colour_all, other in ((RED, BLUE), (BLUE, RED)):

                def all_four(
                    p: int, q: int, colour_all: int = colour_all, values: dict = values
                ) -> bool:
                    key = (max(p, q), min(p, q))
                    return all(v == colour_all for v in values[key].values())

                clique = max_clique(labels, all_four)[:6]
                independent = max_clique(labels, lambda p, q: not all_four(p, q))
                cube = subcube(clique)
                tree = greedy_tree_words(independent, values, other)
                checker.check(
                    f'{tag}: subcube on all-{colour_all} clique, {len(cube)} words',
                    len(set(cube)) == 2 ** len(clique)
                    and is_monochromatic(cube, rule, colour_all),
                )
                checker.check(
                    f'{tag}: colour-{other} greedy tree, {len(tree)} words',
                    len(set(tree)) == len(independent) + 1
                    and is_monochromatic(tree, rule, other),
                )
                full = max_clique(labels, all_four)
                checker.check(
                    f'{tag}: |Lambda| < (alpha+1)^omega',
                    len(labels) < (len(independent) + 1) ** max(1, len(full)),
                )
            red_value, red_tree = product_tree(labels, values, RED)
            blue_value, blue_tree = product_tree(labels, values, BLUE)
            checker.check(
                f'{tag}: product {red_value}*{blue_value} >= |Lambda|+1',
                red_value * blue_value >= len(labels) + 1,
            )
            for value, tree, target in (
                (red_value, red_tree, RED),
                (blue_value, blue_tree, BLUE),
            ):
                words, consistent = realize(tree, values, target)
                checker.check(
                    f'{tag}: colour-{target} product tree, {len(words)} words',
                    consistent
                    and len(set(words)) == value == len(words)
                    and is_monochromatic(words, rule, target),
                )


def prefix_rule_checks(checker: Checker) -> None:
    """The product inequality for rules that also read the common prefix."""
    context_free_failures = 0
    for size, width, window in ((12, 0, False), (14, 1, False), (18, 1, True)):
        for index in range(4):
            name = f'px-{size}-{width}-{window}-{index}'
            rule = QueryRule(name, size, width, window, prefix=True)
            labels = spread_labels(rule)[:11]
            tag = f'prefix rule M={size} w={width} {index} |Lambda|={len(labels)}'
            red_value, red_words = context_product_words(rule, labels, RED)
            blue_value, blue_words = context_product_words(rule, labels, BLUE)
            checker.check(
                f'{tag}: product {red_value}*{blue_value} >= |Lambda|+1',
                red_value * blue_value >= len(labels) + 1,
            )
            for value, words, target in (
                (red_value, red_words, RED),
                (blue_value, blue_words, BLUE),
            ):
                checker.check(
                    f'{tag}: colour-{target} context tree, {len(words)} words',
                    len(set(words)) == value == len(words)
                    and is_monochromatic(words, rule, target),
                )
            zero_prefix = table(rule, labels)
            for target in (RED, BLUE):
                _, tree = product_tree(labels, zero_prefix, target)
                words, _ = realize(tree, zero_prefix, target)
                if not is_monochromatic(words, rule, target):
                    context_free_failures += 1
    checker.check(
        f'prefix dependence is exercised: {context_free_failures} of 24 '
        'context-free product trees are not monochromatic (control)',
        context_free_failures > 0,
    )


def seed_graph(name: str, size: int) -> dict[tuple[int, int], int]:
    """Return a deterministic two-colouring of the pairs of range(size)."""
    return {(p, q): hbit(name, p, q) for p in range(size) for q in range(size) if p > q}


def outsider_table_checks(checker: Checker) -> None:
    """Every outsider-bit table has a large explicit monochromatic set."""
    size = 16
    for name in ('phi-A', 'phi-B'):
        phi = seed_graph(name, size)
        failures = []
        full_sets = 0
        for code in range(256):

            def colour(
                x: int, y: int, z: int, code: int = code, phi: dict = phi
            ) -> int:
                a, b = delta(x, y), delta(y, z)
                low, high = min(a, b), max(a, b)
                outsider = z if a < b else x
                eta = (outsider >> low) & 1
                index = 4 * phi[(high, low)] + 2 * int(a < b) + eta
                return (code >> index) & 1

            labels = list(range(size))
            values = table(colour, labels)
            best = 0
            for target in (RED, BLUE):

                def bad(
                    p: int, q: int, target: int = target, values: dict = values
                ) -> bool:
                    key = (max(p, q), min(p, q))
                    return all(v != target for v in values[key].values())

                pool = max_clique(labels, lambda p, q: not bad(p, q))
                tree = greedy_tree_words(pool, values, target)
                if (
                    is_monochromatic(tree, colour, target)
                    and len(set(tree)) == len(pool) + 1
                ):
                    best = max(best, len(tree))
                if len(pool) == size:
                    full_sets += 1
                clique = max_clique(labels, lambda p, q: bad(p, q))[:3]
                cube = subcube(clique)
                if is_monochromatic(cube, colour, 1 - target):
                    best = max(best, len(cube))
            achievable_everywhere = any(
                all(any(v == target for v in values[key].values()) for key in values)
                for target in (RED, BLUE)
            )
            if best < isqrt(size - 1) + 1 or (
                achievable_everywhere and best < size + 1
            ):
                failures.append((code, best))
        checker.check(
            f'{name}: all 256 outsider tables have a verified monochromatic set '
            f'of >= {isqrt(size - 1) + 1} words ({full_sets} full greedy trees)',
            not failures,
            repr(failures[:5]),
        )


def seed_colouring(points: int, planted: int) -> dict[tuple[int, int, int], int]:
    """Return a deterministic colouring of triples with a planted red set.

    Triples inside range(planted) are red; the others are pseudo-random.
    """
    return {
        t: RED if t[2] < planted else hbit('chi0', t)
        for t in combinations(range(points), 3)
    }


def largest_monochromatic(points: int, chi: dict) -> tuple[list[int], int]:
    """Return a largest monochromatic set of the seed colouring and its colour."""
    for size in range(points, 2, -1):
        for subset in combinations(range(points), size):
            colours = {chi[t] for t in combinations(subset, 3)}
            if len(colours) == 1:
                return list(subset), colours.pop()
    return [0, 1], RED


def squaring_checks(checker: Checker) -> None:
    """The two natural copy-squaring rules lose a factor of two."""
    points = 14
    chi = seed_colouring(points, 7)
    mono, colour = largest_monochromatic(points, chi)
    k = len(mono)

    def seed(a: int, b: int, c: int) -> int:
        x, y, z = sorted((a, b, c))
        return chi[(x, y, z)]

    Point = tuple[int, int]

    def product(rule: str) -> Callable[[Point, Point, Point], int]:
        def colour_of(u: Point, v: Point, w: Point) -> int:
            tops = [u[0], v[0], w[0]]
            if len(set(tops)) == 3:
                return seed(*tops)
            if len(set(tops)) == 1:
                return seed(u[1], v[1], w[1])
            pair = [p for p in (u, v, w) if tops.count(p[0]) == 2]
            (outsider,) = [p for p in (u, v, w) if tops.count(p[0]) == 1]
            if rule == 'bottoms':
                third = outsider[1]
            elif pair[0][0] < outsider[0]:
                third = outsider[0]
            else:
                return seed(outsider[0], pair[0][1], pair[1][1])
            return seed(pair[0][1], pair[1][1], third)

        return colour_of

    def mono_in_product(points_set: list[Point], rule: str) -> bool:
        colour_of = product(rule)
        ordered = sorted(points_set)
        return all(colour_of(u, v, w) == colour for u, v, w in combinations(ordered, 3))

    beta, t0 = mono[-1], mono[0]
    fat_thin = [(t0, a) for a in mono if a != beta] + [
        (r, beta) for r in mono if r != t0
    ]
    checker.check(
        f'bottoms rule: fat-thin set of {len(set(fat_thin))} = 2(k-1) points, k={k}',
        len(set(fat_thin)) == 2 * (k - 1) and mono_in_product(fat_thin, 'bottoms'),
    )
    t1, t0 = mono[-1], mono[0]
    fat_fat = [(t0, a) for a in mono if a != t1] + [(t1, b) for b in mono if b != t0]
    checker.check(
        f'outsider-top rule: fat-fat set of {len(set(fat_fat))} = 2(k-1) points',
        len(set(fat_fat)) == 2 * (k - 1) and mono_in_product(fat_fat, 'top'),
    )
    checker.check(f'seed has a monochromatic set of size k={k} >= 7', k >= 7)
    print(f'    seed on {points} points: k={k}, colour {colour}, set {mono}')
    print(f'    comb check: {comb(points, 3)} seed triples coloured')


def prefix_selector_witness_checks(checker: Checker) -> None:
    """Recheck the retained 16-point witness without a solver."""
    path = Path(__file__).resolve().parent / 'assets' / 'prefix_selector_16.json'
    data = json.loads(path.read_text())
    size, forbidden = data['dimension'], data['forbidden_size']
    checker.check(
        'prefix selector: dimension 4 and forbidden size 5', (size, forbidden) == (4, 5)
    )
    if (size, forbidden) != (4, 5):
        return
    phi = {(p, q): value for p, q, value in data['phi']}
    selectors = {(p, prefix, q): h for p, prefix, q, h in data['selectors']}
    expected_phi = {(p, q) for p in range(size) for q in range(p)}
    expected_selectors = {
        (p, prefix, q)
        for p in range(1, size)
        for prefix in range(1 << (size - p - 1))
        for q in range(p)
    }
    valid = (
        set(phi) == expected_phi
        and len(phi) == len(data['phi'])
        and all(value in (0, 1) for value in phi.values())
        and set(selectors) == expected_selectors
        and len(selectors) == len(data['selectors'])
        and all(isinstance(h, int) and 0 <= h < p for (p, _, _), h in selectors.items())
    )
    checker.check(
        'prefix selector: exact seed and query domains, no duplicate entries', valid
    )
    if not valid:
        return

    def colour(x: int, y: int, z: int, *, freeze_prefix: bool = False) -> int:
        a, b = delta(x, y), delta(y, z)
        p, q = max(a, b), min(a, b)
        prefix = 0 if freeze_prefix else x >> (p + 1)
        outsider = z if a < b else x
        position = selectors[(p, prefix, q)]
        return phi[(p, q)] ^ int(a < b) ^ ((outsider >> position) & 1)

    colours = {xyz: colour(*xyz) for xyz in combinations(range(1 << size), 3)}
    checker.check(
        'prefix selector: all 560 triples take one of two colours',
        len(colours) == 560 and set(colours.values()) == {0, 1},
    )
    failures = []
    covered = 0
    for vertices in combinations(range(1 << size), forbidden):
        covered += 1
        if len({colours[xyz] for xyz in combinations(vertices, 3)}) == 1:
            failures.append(vertices)
    checker.check(
        'prefix selector: all 4368 five-sets are nonmonochromatic',
        covered == 4368 and not failures,
        repr(failures[:3]),
    )
    witnesses = data['monochromatic_witnesses']
    checker.check(
        'prefix selector: one four-set witness for each colour', len(witnesses) == 2
    )
    for target, words in enumerate(witnesses):
        checker.check(
            f'prefix selector: colour-{target} four-set {words}',
            len(set(words)) == len(words) == 4
            and all(isinstance(w, int) and 0 <= w < (1 << size) for w in words)
            and is_monochromatic(words, colour, target),
        )
    checker.check(
        'prefix selector: the prefix changes the colour of (9,12,14)',
        colour(9, 12, 14) == 1 and colour(9, 12, 14, freeze_prefix=True) == 0,
    )

    def fixed_colour(x: int, y: int, z: int) -> int:
        a, b = delta(x, y), delta(y, z)
        p, q = max(a, b), min(a, b)
        position = q if p <= 2 else (2 if q == 0 else 0)
        outsider = z if a < b else x
        return phi[(p, q)] ^ int(a < b) ^ ((outsider >> position) & 1)

    fixed_colours = {
        xyz: fixed_colour(*xyz) for xyz in combinations(range(1 << size), 3)
    }
    checker.check(
        'prefix-independent one-query control also has largest sets of size four',
        all(
            len({fixed_colours[xyz] for xyz in combinations(vertices, 3)}) == 2
            for vertices in combinations(range(1 << size), forbidden)
        )
        and all(
            is_monochromatic(words, fixed_colour, target)
            for target, words in enumerate(witnesses)
        ),
    )


def prefix_routing_obstruction_checks(checker: Checker) -> None:
    """Recolour sparse canonical trees for arbitrary-prefix query examples."""
    for cube_root in (4, 8, 16, 32):
        size = cube_root**3
        denominator = 2 * cube_root**2
        for family in range(4):

            def phi(p: int, q: int, family: int = family) -> int:
                return hbit('routing-obstruction', family, p, q)

            def query(prefix: int, p: int, q: int, family: int = family) -> int:
                if family == 0:
                    return q
                if family == 1:
                    return (q + 1 + prefix % 3) % p
                if family == 2:
                    return prefix % p
                return hval(p, 'routing-obstruction', hex(prefix), p, q)

            def colour(x: int, y: int, z: int) -> int:
                a, b = delta(x, y), delta(y, z)
                p, q = max(a, b), min(a, b)
                outsider = z if a < b else x
                position = query(x >> (p + 1), p, q)
                return phi(p, q) ^ int(a < b) ^ ((outsider >> position) & 1)

            for target in (RED, BLUE):

                def build(
                    pool: list[int],
                    base: int,
                    prefixes: dict[int, int],
                    target: int = target,
                ) -> list[int]:
                    if not pool:
                        return [base]
                    root, rest = max(pool), [q for q in pool if q != max(pool)]
                    prefixes[root] = base >> (root + 1)
                    left = [q for q in rest if phi(root, q) ^ 1 == target]
                    right = [q for q in rest if q not in left]
                    return build(left, base, prefixes) + build(
                        right, base | (1 << root), prefixes
                    )

                minimum = max(3, (cube_root + 3) // 4)
                accepted = False
                for trial in range(64):
                    labels = [
                        p
                        for p in range(size)
                        if hval(denominator, 'labels', size, family, target, trial, p)
                        == 0
                    ]
                    if len(labels) < minimum:
                        continue
                    prefixes: dict[int, int] = {}
                    words = build(labels, 0, prefixes)
                    chosen = set(labels)
                    if any(
                        query(prefixes[p], p, q) in chosen - {q}
                        for p, q in combinations(sorted(labels, reverse=True), 2)
                    ):
                        continue
                    accepted = True
                    break
                tag = f'prefix XOR: M={size}, family={family}, colour={target}'
                if not accepted:
                    checker.check(f'{tag}: sparse witness found within cap', False)
                    continue

                # Compute the insertion prefix a second way, from higher labels
                # only. A higher label is on p's path exactly when it follows
                # all the same branches at ancestors already on that path.
                prefix_ok = True
                for p in labels:
                    ancestors: list[int] = []
                    base = 0
                    for r in sorted((q for q in labels if q > p), reverse=True):
                        if all(phi(a, r) == phi(a, p) for a in ancestors):
                            ancestors.append(r)
                            if phi(r, p) ^ 1 != target:
                                base |= 1 << r
                    prefix_ok &= base >> (p + 1) == prefixes[p]
                checker.check(
                    f'{tag}: {len(words)} words, valid prefixes and every triple',
                    prefix_ok
                    and len(set(words)) == len(words) == len(labels) + 1
                    and len(labels) >= minimum
                    and all(0 <= w < (1 << size) for w in words)
                    and is_monochromatic(words, colour, target),
                )


def main() -> int:
    """Run the finite checks and return a failing status on disagreement."""
    evidence_parser(__doc__ or 'Stepping-up obstructions', quick=False).parse_args()
    checker = Checker()
    bounded_query_checks(checker)
    prefix_rule_checks(checker)
    outsider_table_checks(checker)
    squaring_checks(checker)
    prefix_selector_witness_checks(checker)
    prefix_routing_obstruction_checks(checker)
    return checker.finish()


if __name__ == '__main__':
    sys.exit(main())
