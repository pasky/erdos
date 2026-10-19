"""Check the finite stack-process computations of the height-three attack.

The owning note proves a fixed-shape compression and expansion rule. This
program checks finite statements about the resulting stack process, and a
separate artificial adversary model. It does not remove numerical histories
from arbitrary Architect strategies.

0. At height one, for 1 <= m <= 8, the all-doubles rotation (outside) and the
   one-summand mark pattern (inside) complete without deadlock. The empty
   outside shape m=0 is also checked.

1. Fixed-shape strategies. For every pair of selection shapes (X, Y) of height
   h with every node degree at most d and at most L leaves, where Y has the
   same number of leaves as X (outside) or one fewer (inside), some choice of
   tree words completes the stack process without deadlock. Ranges: h=1, d=6,
   L=6; h=2, d=4, L=6; h=3, d=3, L=6 (--quick: h=3, d=2, L=4). Each found
   schedule is re-verified by an independent replay of the three games.
2. A retained witness for the inside shapes X = 1-1-2 and Y = 1-1-1 at height
   three, and the exhaustive check that every schedule against that pair
   gives the first tree a leaf selected in both of its games.
   Two height-two pairs are scheduled although no schedule gives the first
   tree (respectively the last tree) only doubles. The height-three shapes
   X=1-1-3 and Y=1-2-(1,1) have a retained merged-tree certificate and event
   schedule. Both tree projections and the actual pairwise cell endpoints
   are checked separately. No schedule for this pair makes A all doubles.
   The next pair 1-1-4 / 1-3-(1,1,1) is schedulable, but not with C all
   doubles.
3. A finite global-state adversary model with nonempty root selections and a
   coarse total filter. Counts from 1 to K are chosen with knowledge of all
   three games. The filter keeps lower bounds and whether a pending internal
   node exists; it does not check bounded completability or existence of a
   game-local winning strategy. In this artificial process Builder survives
   at h=1 (K=3), h=2 (K=2), h=2 outside (K=3) and h=3 outside (K=2); the
   no Builder policy survives at h=2 inside (K=3) and at h=3 inside (K=2).

Run from the repository root:
    uv run --no-sync python wiki/research/erdos_592/height_three_evidence/main.py

Dependencies are the standard library and the installed root tools package.
There are no file inputs, random choices or output files. The full run takes
about nine minutes and up to about four gigabytes of memory; --quick takes
under a minute. Failure exits nonzero, including with python -O. These
finite checks establish no partition relation and say nothing about counts
outside the stated ranges or about strategies that use the numerical
   histories. The owning note's proof, not this finite run, gives arbitrarily
   large realizations of the retained merged trees and the symbolic
   obstruction to synchronizing A.
"""

from __future__ import annotations

import itertools
import sys
from functools import cache

import tools

__all__ = [
    'merge_words',
    'solve',
    'replay',
    'run_words',
    'delannoy',
    'relaxation',
    'main',
]

# selection shapes are nested tuples (None is the empty shape); a pending
# node of the relaxation is a pair (depth, type)
Shape = tuple | None
Agenda = tuple[tuple[int, str], ...]

# the three trees in start order and, for each, the other two in a fixed order
_OTHERS = {'A': ('B', 'C'), 'B': ('A', 'C'), 'C': ('A', 'B')}
_INDEX = {'A': 0, 'B': 1, 'C': 2}
_GAMES = (('A', 'B'), ('A', 'C'), ('B', 'C'))


def leaves(shape: Shape, height: int) -> int:
    """Return the number of leaves of a selection shape (None is empty)."""
    if shape is None:
        return 0
    if height == 0:
        return 1
    return sum(leaves(child, height - 1) for child in shape)


@cache
def merge_words(first: Shape, second: Shape, height: int) -> frozenset[str]:
    """Return the mark words of one tree carrying two selection shapes.

    Letter x marks a leaf selected only for the first shape, y only for the
    second, and D for both; the two shapes share the root.
    """
    if first is None and second is None:
        return frozenset([''])
    if first is None:
        return frozenset(['y' * leaves(second, height)])
    if second is None:
        return frozenset(['x' * leaves(first, height)])
    if height == 0:
        return frozenset(['D'])
    out: set[str] = set()

    # every interleaving of the two child lists, with order-preserving pairing
    def walk(i: int, j: int, parts: list[frozenset[str]]) -> None:
        if i == len(first) and j == len(second):
            out.update(''.join(choice) for choice in itertools.product(*parts))
            return
        if i < len(first):
            walk(i + 1, j, [*parts, frozenset(['x' * leaves(first[i], height - 1)])])
        if j < len(second):
            walk(i, j + 1, [*parts, frozenset(['y' * leaves(second[j], height - 1)])])
        if i < len(first) and j < len(second):
            walk(i + 1, j + 1, [*parts, merge_words(first[i], second[j], height - 1)])

    walk(0, 0, [])
    return frozenset(out)


def tree_words(
    x_shape: Shape, y_shape: Shape, height: int
) -> dict[str, frozenset[str]]:
    """Return the realizable words of A, B and C for first shape X, second Y."""
    return {
        'A': merge_words(x_shape, x_shape, height),
        'B': merge_words(y_shape, x_shape, height),
        'C': merge_words(y_shape, y_shape, height),
    }


def _trie(words: frozenset[str]) -> dict:
    root: dict = {}
    for word in sorted(words):
        node = root
        for letter in word:
            node = node.setdefault(letter, {})
        node['$'] = True
    return root


def solve(words: dict[str, frozenset[str]]) -> list[tuple[str, str]] | None:
    """Search for a deadlock-free stack process; return its event list."""
    tries = {tree: _trie(words[tree]) for tree in 'ABC'}
    memo: dict = {}

    def go(stack: tuple[str, ...], nodes: dict) -> list[tuple[str, str]] | None:
        if not stack:
            return []
        key = (stack, tuple(id(nodes[tree]) for tree in 'ABC'))
        if key in memo:
            return memo[key]
        memo[key] = None
        top = stack[0]
        node = nodes[top]
        result = None
        # a completed word lets the top tree build its last cell and finish
        if node.get('$'):
            rest = go(stack[1:], nodes)
            if rest is not None:
                result = [(top, 'end'), *rest]
        for letter, child in node.items():
            if result is not None or letter == '$':
                continue
            first, second = _OTHERS[top]
            if letter == 'D':
                if len(stack) != 3:
                    continue
                new = (*stack[1:], top)
                named = 'D'
            else:
                named = first if letter == 'x' else second
                if len(stack) < 2 or stack[1] != named:
                    continue
                new = (stack[1], top, *stack[2:])
            rest = go(new, {**nodes, top: child})
            if rest is not None:
                result = [(top, named), *rest]
        memo[key] = result
        return result

    return go(('A', 'B', 'C'), tries)


def replay(
    events: list[tuple[str, str]], words: dict[str, frozenset[str]], inside: bool
) -> bool:
    """Replay the three games independently of the search.

    Each tree must emit a realizable word; within each game the selection
    marks must alternate starting with the first tree and finish with the
    counts the type requires; and every event must occur while its tree holds
    the turn in both of its games.
    """
    emitted = dict.fromkeys('ABC', '')
    marks = {(k, i): 0 for k in 'ABC' for i in _OTHERS[k]}
    finished: set[str] = set()
    letters = {tree: {_OTHERS[tree][0]: 'x', _OTHERS[tree][1]: 'y'} for tree in 'ABC'}

    def holds(tree: str, other: str) -> bool:
        # the turn of game (first, second) is decided by the two mark counts
        if other in finished:
            return True
        first, second = sorted((tree, other))
        lead = marks[(first, second)] - marks[(second, first)]
        return lead == 0 if tree == first else lead == 1

    for tree, event in events:
        if tree in finished:
            return False
        if not all(holds(tree, other) for other in _OTHERS[tree]):
            return False
        if event == 'end':
            finished.add(tree)
            continue
        named = _OTHERS[tree] if event == 'D' else (event,)
        if any(other in finished for other in named):
            return False
        for other in named:
            marks[(tree, other)] += 1
        emitted[tree] += 'D' if event == 'D' else letters[tree][event]
    if finished != {'A', 'B', 'C'}:
        return False
    if any(emitted[tree] not in words[tree] for tree in 'ABC'):
        return False
    # the type fixes each game's final counts
    return all(marks[(f, s)] - marks[(s, f)] == (1 if inside else 0) for f, s in _GAMES)


def run_words(words: dict[str, str]) -> list[tuple[str, str]] | None:
    """Run the stack process on fixed mark words; return None at a deadlock."""
    position = dict.fromkeys('ABC', 0)
    stack = ['A', 'B', 'C']
    events: list[tuple[str, str]] = []
    while stack:
        top = stack[0]
        if position[top] == len(words[top]):
            events.append((top, 'end'))
            stack.pop(0)
            continue
        letter = words[top][position[top]]
        position[top] += 1
        if letter == 'D':
            if len(stack) != 3:
                return None
            events.append((top, 'D'))
            stack = [*stack[1:], top]
            continue
        named = _OTHERS[top][0] if letter == 'x' else _OTHERS[top][1]
        if len(stack) < 2 or stack[1] != named:
            return None
        events.append((top, named))
        stack = [stack[1], top, *stack[2:]]
    return events


def cell_replay(events: list[tuple[str, str]], inside: bool) -> bool:
    """Recover actual pairwise leaf cells, without using turn counters.

    Each event represents one leaf, with ``end`` the final unmarked leaf.
    Inserting additional unmarked leaves in its preceding construction run
    does not change the cell endpoints. A mark for a partner must occur
    exactly at the last event of a nonfinal cell for that tree.
    """
    for tree in 'ABC':
        own = [event for emitter, event in events if emitter == tree]
        if not own or own[-1] != 'end' or own.count('end') != 1:
            return False
    if any(
        tree not in _OTHERS or event not in (*_OTHERS[tree], 'D', 'end')
        for tree, event in events
    ):
        return False
    for first, second in _GAMES:
        selected = [
            (i, tree, mark)
            for i, (tree, mark) in enumerate(events)
            if tree in (first, second)
        ]
        cells: list[list[tuple[int, str, str]]] = []
        for entry in selected:
            if not cells or cells[-1][-1][1] != entry[1]:
                cells.append([])
            cells[-1].append(entry)
        if cells[0][0][1] != first:
            return False
        if cells[-1][-1][1] != (first if inside else second):
            return False
        for tree, partner in ((first, second), (second, first)):
            own_cells = [cell for cell in cells if cell[0][1] == tree]
            expected = {cell[-1][0] for cell in own_cells[:-1]}
            actual = {
                i
                for i, emitter, mark in selected
                if emitter == tree and mark in (partner, 'D')
            }
            if expected != actual:
                return False
    return True


# A selected union node is (mask, children): 1 selects the first projection,
# 2 the second, and 3 both. Leaves have no children. No filler node is stored.
UnionNode = tuple[int, tuple]


def union_valid(node: UnionNode, height: int) -> bool:
    """Check height and upward closure of both selections."""
    mask, children = node
    if mask not in (1, 2, 3):
        return False
    if height == 0:
        return children == ()
    if not children or any(not union_valid(child, height - 1) for child in children):
        return False
    combined = 0
    for child in children:
        combined |= child[0]
    return combined == mask


def union_projection(node: UnionNode, height: int, side: int) -> Shape:
    """Recover one ordered selection shape from the retained union tree."""
    mask, children = node
    if not mask & side:
        return None
    if height == 0:
        return ()
    return tuple(
        union_projection(child, height - 1, side)
        for child in children
        if child[0] & side
    )


def union_word(node: UnionNode) -> str:
    """Read the leaf marks directly from a selected union tree."""
    mask, children = node
    if not children:
        return {1: 'x', 2: 'y', 3: 'D'}[mask]
    return ''.join(union_word(child) for child in children)


def synchronization_witness() -> tuple[dict[str, UnionNode], list[tuple[str, str]]]:
    """The explicit 1-1-3 / 1-2-(1,1) selected unions and schedule."""
    x, y, double = (1, ()), (2, ()), (3, ())
    unions = {
        'A': (3, ((3, ((3, (x, double, y, double)),)),)),
        'B': (3, ((3, ((1, (x,)), (3, (y, double, y)))),)),
        'C': (3, ((3, ((3, (double,)), (3, (double,)))),)),
    }
    events = [
        ('A', 'B'),
        ('B', 'A'),
        ('A', 'D'),
        ('B', 'C'),
        ('C', 'D'),
        ('B', 'D'),
        ('A', 'C'),
        ('C', 'D'),
        ('A', 'D'),
        ('B', 'C'),
        ('C', 'end'),
        ('B', 'end'),
        ('A', 'end'),
    ]
    return unions, events


def height_one_words(m: int, inside: bool) -> dict[str, str]:
    """Return the page's height-one words: rotation, or the printed pattern."""
    if not inside:
        return {'A': 'D' * m, 'B': 'D' * m, 'C': 'D' * m}
    if m == 1:
        return {'A': 'D', 'B': 'y', 'C': ''}
    # letters as in merge_words: in A x=B, y=C; in B x=A, y=C; in C x=A, y=B
    return {
        'A': 'D' + 'y' * (m - 1) + 'x' * (m - 1),
        'B': 'y' * (m - 1) + 'D' + 'x' * (m - 2),
        'C': 'y' * (m - 2) + 'D' + 'x' * (m - 2),
    }


def shapes(height: int, degree: int, most: int) -> list:
    """Return every selection shape within the stated degree and leaf bounds."""
    if height == 0:
        return [()]
    lower = shapes(height - 1, degree, most)
    out = []
    for width in range(1, degree + 1):
        for combo in itertools.product(lower, repeat=width):
            if sum(leaves(child, height - 1) for child in combo) <= most:
                out.append(tuple(combo))
    return out


def fixed_shape_range(height: int, degree: int, most: int) -> tuple[int, list]:
    """Search every fixed-shape pair in range; return the count and failures."""
    failures = []
    tested = 0
    family = shapes(height, degree, most)
    for x_shape in family:
        count = leaves(x_shape, height)
        for y_shape in [*family, None]:
            gap = count - leaves(y_shape, height)
            if gap not in (0, 1):
                continue
            tested += 1
            words = tree_words(x_shape, y_shape, height)
            events = solve(words)
            if (
                events is None
                or not replay(events, words, gap == 1)
                or not cell_replay(events, gap == 1)
            ):
                failures.append((x_shape, y_shape))
    return tested, failures


def delannoy(a: int, b: int) -> list[tuple[str, ...]]:
    """Return the child-type sequences of a node with a and b selections."""
    paths: list[tuple[str, ...]] = []

    def path(i: int, j: int, acc: tuple[str, ...]) -> None:
        if i == a and j == b:
            paths.append(acc)
            return
        if i < a:
            path(i + 1, j, (*acc, 'x'))
        if j < b:
            path(i, j + 1, (*acc, 'y'))
        if i < a and j < b:
            path(i + 1, j + 1, (*acc, 'D'))

    path(0, 0, ())
    return paths


def relaxation(height: int, bound: int, inside: bool) -> bool:
    """Decide the coarse global-state model; True when the Builder survives.

    A pending node is (depth, type) with type x, y or D as in merge_words.
    Counts 1..bound are chosen when a selected node is built, including roots.
    They must pass the coarse total filter below. It is not a bounded
    completability or game-locality check. The first tree's root counts are
    equal, as is the second tree's root count in its own first game, and the
    first tree's counts stay equal while all its selections are common.
    """
    gap = 1 if inside else 0
    arrangements = {
        (a, b): delannoy(a, b) for a in range(1, bound + 1) for b in range(1, bound + 1)
    }

    def names(tree: str, kind: str) -> tuple[str, ...]:
        first, second = _OTHERS[tree]
        return {'x': (first,), 'y': (second,), 'D': (first, second)}[kind]

    def passes_total_filter(
        agendas: list[Agenda], counts: dict[tuple[str, str], int]
    ) -> bool:
        """Keep minimum totals and an unbounded-growth flag, not upper bounds."""
        span = {}
        for tree in 'ABC':
            for other in _OTHERS[tree]:
                low, open_ = counts[(tree, other)], False
                for depth, kind in agendas[_INDEX[tree]]:
                    if other in names(tree, kind):
                        low += 1
                        open_ = open_ or depth < height
                span[(tree, other)] = (low, open_)
        for first, second in _GAMES:
            (lf, of), (ls, os_) = span[(first, second)], span[(second, first)]
            if not of and not os_ and lf - ls != gap:
                return False
            if not of and os_ and lf - gap < ls:
                return False
            if of and not os_ and ls + gap < lf:
                return False
        return True

    keys = [(tree, other) for tree in 'ABC' for other in _OTHERS[tree]]

    @cache
    def survive(
        stack: tuple[str, ...],
        ag_a: Agenda,
        ag_b: Agenda,
        ag_c: Agenda,
        sym: bool,
        root_count: int | None,
        packed: tuple[int, ...],
    ) -> bool:
        agendas = [ag_a, ag_b, ag_c]
        counts = dict(zip(keys, packed))
        if not stack:
            return True
        top = stack[0]
        agenda = agendas[_INDEX[top]]
        if not agenda:
            return survive(stack[1:], *agendas, sym, root_count, packed)
        (depth, kind), rest = agenda[0], agenda[1:]
        if depth == height:
            named = names(top, kind)
            # a mark naming a finished tree is an incorrect play
            if any(other not in stack for other in named):
                return True
            if kind == 'D':
                new = (*stack[1:], top)
            elif stack[1] != named[0]:
                return False
            else:
                new = (stack[1], top, *stack[2:])
            for other in named:
                counts[(top, other)] += 1
            agendas[_INDEX[top]] = rest
            symmetric = sym and top != 'A'
            return survive(
                new, *agendas, symmetric, root_count, tuple(counts[k] for k in keys)
            )
        if kind in 'xy':
            for count in range(1, bound + 1):
                trial = list(agendas)
                trial[_INDEX[top]] = ((depth + 1, kind),) * count + rest
                if passes_total_filter(trial, counts) and not survive(
                    stack, *trial, sym and top != 'A', root_count, packed
                ):
                    return False
            return True
        for a in range(1, bound + 1):
            for b in range(1, bound + 1):
                if top == 'A' and sym and a != b:
                    continue
                if top == 'B' and depth == 0 and b != root_count:
                    continue
                new_root = a if (top == 'A' and depth == 0) else root_count
                valid = False
                answered = False
                for arrangement in arrangements[(a, b)]:
                    trial = list(agendas)
                    trial[_INDEX[top]] = (
                        tuple((depth + 1, k) for k in arrangement) + rest
                    )
                    if not passes_total_filter(trial, counts):
                        continue
                    valid = True
                    symmetric = sym
                    if top == 'A':
                        symmetric = sym and all(k == 'D' for k in arrangement)
                    if survive(stack, *trial, symmetric, new_root, packed):
                        answered = True
                        break
                if valid and not answered:
                    return False
        return True

    root = ((0, 'D'),)
    return survive(('A', 'B', 'C'), root, root, root, True, None, (0,) * 6)


def main() -> int:
    """Run the fixed-shape ranges, the retained witness and the relaxation."""
    parser = tools.evidence_parser('Check the height-three stack-process computations.')
    args = parser.parse_args()
    checker = tools.Checker()

    # fixed-shape strategies: every pair in range has a deadlock-free schedule
    ranges = [
        (1, 6, 6, 12),
        (2, 4, 6, 1287),
        (3, 2, 4, 203) if args.quick else (3, 3, 6, 33278),
    ]
    for height, degree, most, expected_pairs in ranges:
        tested, failures = fixed_shape_range(height, degree, most)
        checker.check(
            f'fixed shapes h={height} d<={degree} leaves<={most}: {tested} pairs all scheduled',
            tested == expected_pairs and not failures,
            f'expected {expected_pairs} pairs; first failures: {failures[:3]}',
        )

    empty_events = run_words(height_one_words(0, False))
    checker.check(
        'height one m=0 outside: all three selections are empty',
        empty_events is not None
        and replay(empty_events, tree_words(None, None, 1), False)
        and cell_replay(empty_events, False),
    )

    # the height-one rotation and the printed one-summand pattern
    for m in range(1, 9):
        for inside in (False, True):
            x_shape = ((),) * m
            y_shape = (
                ((),) * (m - 1) if inside and m > 1 else (None if inside else x_shape)
            )
            words = tree_words(x_shape, y_shape, 1)
            events = run_words(height_one_words(m, inside))
            kind = 'inside' if inside else 'outside'
            checker.check(
                f'height one m={m} {kind}: stated words complete',
                events is not None
                and replay(events, words, inside)
                and cell_replay(events, inside),
            )

    # The symbolic synchronization obstruction and its alternative schedule.
    x_shape = ((((), (), ()),),)
    y_shape = ((((),), ((),)),)
    unions, events = synchronization_witness()
    projected = {
        'A': (x_shape, x_shape),
        'B': (y_shape, x_shape),
        'C': (y_shape, y_shape),
    }
    checker.check(
        '1-1-3 / 1-2-(1,1): retained union trees have both prescribed projections',
        all(
            union_valid(node, 3)
            and tuple(union_projection(node, 3, side) for side in (1, 2))
            == projected[tree]
            for tree, node in unions.items()
        ),
    )
    words = {tree: frozenset([union_word(node)]) for tree, node in unions.items()}
    checker.check(
        '1-1-3 / 1-2-(1,1): event schedule replays on the retained union trees',
        replay(events, words, True),
    )
    checker.check(
        '1-1-3 / 1-2-(1,1): marks are exactly the actual nonfinal cell maxima',
        cell_replay(events, True),
    )
    mutated = [('A', 'D'), *events[1:]]
    checker.check(
        'cell replay rejects replacing the first single by a double',
        not cell_replay(mutated, True),
    )
    words = tree_words(x_shape, y_shape, 3)
    checker.check(
        '1-1-3 / 1-2-(1,1): no schedule makes A all doubles',
        'DDD' in words['A'] and solve({**words, 'A': frozenset(['DDD'])}) is None,
    )

    x_shape = ((((), (), (), ()),),)
    y_shape = ((((),), ((),), ((),)),)
    words = tree_words(x_shape, y_shape, 3)
    events = solve(words)
    checker.check(
        '1-1-4 / 1-3-(1,1,1): an unrestricted schedule exists',
        events is not None
        and replay(events, words, True)
        and cell_replay(events, True),
    )
    checker.check(
        '1-1-4 / 1-3-(1,1,1): no schedule makes C all doubles',
        'DDD' in words['C'] and solve({**words, 'C': frozenset(['DDD'])}) is None,
    )

    # retained witness for the inside pair 1-1-2 / 1-1-1
    x_shape = ((((), ()),),)
    y_shape = ((((),),),)
    words = tree_words(x_shape, y_shape, 3)
    witness = [
        ('A', 'D'),
        ('B', 'C'),
        ('C', 'D'),
        ('B', 'D'),
        ('A', 'D'),
        ('C', 'end'),
        ('B', 'end'),
        ('A', 'end'),
    ]
    checker.check(
        'retained 1-1-2 / 1-1-1 witness replays', replay(witness, words, True)
    )
    no_common = {'A': frozenset(w for w in words['A'] if 'D' not in w)}
    checker.check(
        'every schedule against 1-1-2 / 1-1-1 selects a leaf of A in both games',
        len(no_common['A']) == 6 and solve({**words, **no_common}) is None,
    )

    # identical selections in the first or the last tree do not always suffice
    for tree, x_shape, y_shape in (
        ('A', (((), (), ()),), (((),), ((),))),
        ('C', (((), ()), ((),)), (((), (), ()),)),
    ):
        words = tree_words(x_shape, y_shape, 2)
        inside = leaves(x_shape, 2) > leaves(y_shape, 2)
        doubles = frozenset(w for w in words[tree] if set(w) <= {'D'})
        events = solve(words)
        checker.check(
            f'h=2 {x_shape} / {y_shape}: scheduled, but not with {tree} all doubles',
            events is not None
            and replay(events, words, inside)
            and len(doubles) == 1
            and solve({**words, tree: doubles}) is None,
        )

    # The coarse global-state adversary model, not an actual Architect strategy.
    expected = [
        (1, 3, False, True),
        (1, 3, True, True),
        (2, 2, False, True),
        (2, 2, True, True),
        (2, 3, False, True),
        (2, 3, True, False),
        (3, 2, False, True),
        (3, 2, True, False),
    ]
    for height, bound, inside, builder in expected:
        outcome = relaxation(height, bound, inside)
        kind = 'inside' if inside else 'outside'
        checker.check(
            f'coarse model h={height} K={bound} {kind}: Builder survives = {builder}',
            outcome == builder,
            f'observed {outcome}',
        )
    return checker.finish()


if __name__ == '__main__':
    sys.exit(main())
