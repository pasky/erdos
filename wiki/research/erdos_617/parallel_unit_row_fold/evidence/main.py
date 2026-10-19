"""Check one local fold obstruction, not a normalized-core counterexample.

Input: assets/local_witness.json, one 29-vertex graph with r=12.
Exact integer arithmetic; repository tools.Checker plus Python standard library.
All 2**29 induced subsets are covered by an exact component dynamic program.
No graph search or SAT is performed. An 11-vertex restriction is also checked
by direct exhaustive enumeration before the full calculation. Expected runtime
under 5 seconds, bounded state space below one million transitions and 64 MiB.
Default is the complete check; there is no reduced quick mode.

From the repository root:
nice -n 10 uv run --no-sync python \
  wiki/research/erdos_617/parallel_unit_row_fold/evidence/main.py
"""

from __future__ import annotations

import json
import sys
from itertools import combinations, product
from pathlib import Path

from tools import Checker, evidence_parser


def pair(u: str, v: str) -> frozenset[str]:
    return frozenset((u, v))


def choose2(n: int) -> int:
    return n * (n - 1) // 2


def cap(r: int, n: int) -> int:
    q, b = divmod(n, r)
    return choose2(n) - (r - 1) * (r * choose2(q) + q * b)


def edge_count(edges: set[frozenset[str]], vertices: set[str]) -> int:
    return sum(e <= vertices for e in edges)


def build(data: dict) -> tuple[list[str], set[frozenset[str]]]:
    groups = [data[k] for k in ("deleted_row", "receiving_row", "test_set")]
    vertices = [v for group in groups for v in group] + data["exceptions"]
    if len(vertices) != len(set(vertices)) or len(vertices) != 29:
        raise ValueError("Expected 29 distinct labeled vertices")
    edges = {pair(u, v) for group in groups for u, v in combinations(group, 2)}
    for u, v in data["missing_test_edges"]:
        edges.remove(pair(u, v))
    for u, v in data["row_test_edges"]:
        edges.add(pair(u, v))
    for u, neighbors in data["exception_neighbors"].items():
        edges.update(pair(u, v) for v in neighbors)
    if any(len(e) != 2 or not e <= set(vertices) for e in edges):
        raise ValueError("Malformed edge")
    return vertices, edges


def profiles(data: dict, edges: set[frozenset[str]], allowed: set[str]):
    """Exact min/max induced-edge counts for every subset cardinality.

    Subtract the two complete-graph edge counts on P and T. The remaining
    interaction graph on P+T has components of order at most two: matching
    edges P--T, the negative missing edge in T, and isolated vertices. Fixing
    x,y turns their edges into vertex weights. Receiving-row vertices are
    interchangeable true twins with outside neighborhood exactly {x,y}.
    The DP records both extrema for each pair of occupancies in P,T.
    """
    ps = [v for v in data["deleted_row"] if v in allowed]
    ts = [v for v in data["test_set"] if v in allowed]
    js = [v for v in data["receiving_row"] if v in allowed]
    xs = [v for v in data["exceptions"] if v in allowed]
    if len(ps) > 11 or len(ts) > 12 or len(js) > 4 or len(xs) != 2:
        raise ValueError("Outside the declared bounded domain")
    pset, tset, jset, xset = map(set, (ps, ts, js, xs))
    core = ps + ts
    if set(core) | jset | xset != allowed:
        raise ValueError("Incomplete vertex partition")
    if any(pair(u, v) not in edges for u, v in combinations(ps, 2)):
        raise ValueError("P must be a clique")
    for u in js:
        expected = (jset - {u}) | xset
        actual = {v for v in allowed - {u} if pair(u, v) in edges}
        if actual != expected:
            raise ValueError("Receiving-row twin condition failed")

    weights = {}
    neighbors = {v: set() for v in core}
    for u, v in combinations(core, 2):
        baseline = int((u in pset and v in pset) or (u in tset and v in tset))
        weight = int(pair(u, v) in edges) - baseline
        if weight:
            weights[pair(u, v)] = weight
            neighbors[u].add(v)
            neighbors[v].add(u)
    pending = set(core)
    components = []
    while pending:
        stack = [min(pending)]
        component = set()
        while stack:
            v = stack.pop()
            if v not in component:
                component.add(v)
                stack.extend(neighbors[v] - component)
        pending -= component
        if len(component) > 2:
            raise ValueError("Residual interaction component is too large")
        components.append(sorted(component))

    # Values are pairs (minimum, maximum), each with a realizing subset.
    extremes = [None] * (len(allowed) + 1)
    for flags in product((0, 1), repeat=2):
        chosen_x = {x for x, flag in zip(xs, flags, strict=True) if flag}
        dp = {(0, 0): ((0, frozenset()), (0, frozenset()))}
        for component in components:
            options = []
            for mask in range(1 << len(component)):
                chosen = frozenset(
                    v for j, v in enumerate(component) if mask & (1 << j)
                )
                value = sum(
                    weights.get(pair(u, v), 0) for u, v in combinations(chosen, 2)
                ) + sum(pair(u, x) in edges for u in chosen for x in chosen_x)
                options.append((len(chosen & pset), len(chosen & tset), value, chosen))
            new_dp = {}
            for (p, t), old in dp.items():
                for add_p, add_t, value, chosen in options:
                    key = (p + add_p, t + add_t)
                    candidates = tuple((entry[0] + value, entry[1] | chosen) for entry in old)
                    if key not in new_dp:
                        new_dp[key] = candidates
                    else:
                        prior = new_dp[key]
                        new_dp[key] = (
                            min((prior[0], candidates[0]), key=lambda entry: entry[0]),
                            max((prior[1], candidates[1]), key=lambda entry: entry[0]),
                        )
            dp = new_dp
        for (p, t), extrema in dp.items():
            for h in range(len(js) + 1):
                constant = (
                    choose2(p) + choose2(t) + choose2(h)
                    + h * len(chosen_x) + edge_count(edges, chosen_x)
                )
                n = p + t + h + len(chosen_x)
                candidates = tuple(
                    (entry[0] + constant, entry[1] | frozenset(js[:h]) | chosen_x)
                    for entry in extrema
                )
                if extremes[n] is None:
                    extremes[n] = candidates
                else:
                    prior = extremes[n]
                    extremes[n] = (
                        min((prior[0], candidates[0]), key=lambda entry: entry[0]),
                        max((prior[1], candidates[1]), key=lambda entry: entry[0]),
                    )
    if any(value is None for value in extremes):
        raise ValueError("Missing cardinality in DP")
    return extremes


def brute_profiles(edges: set[frozenset[str]], selected: set[str]):
    labels = sorted(selected)
    values = [[choose2(len(labels)) + 1, -1] for _ in range(len(labels) + 1)]
    for mask in range(1 << len(labels)):
        chosen = {v for j, v in enumerate(labels) if mask & (1 << j)}
        n, count = len(chosen), edge_count(edges, chosen)
        values[n][0] = min(values[n][0], count)
        values[n][1] = max(values[n][1], count)
    return values


def main() -> int:
    evidence_parser(__doc__, quick=False).parse_args()
    data = json.loads((Path(__file__).parent / "assets/local_witness.json").read_text())
    vertices, edges = build(data)
    all_vertices = set(vertices)
    r = data["r"]
    if r != 12:
        raise ValueError("The certified scope is the single r=12 witness")
    check = Checker()
    small = {"q", "u0", "u1", "v0", "j0", "t0", "t1", "t2", "t3", "x", "y"}
    small_dp = profiles(data, edges, small)
    small_brute = brute_profiles(edges, small)
    check.check(
        "DP agrees with all 2048 subsets of the 11-vertex boundary fixture",
        [[lo[0], hi[0]] for lo, hi in small_dp] == small_brute,
    )
    full = profiles(data, edges, all_vertices)
    check.check(
        "Every DP extremizer has its claimed cardinality and actual edge count",
        all(len(vs) == n and edge_count(edges, set(vs)) == count
            for n, extrema in enumerate(full) for count, vs in extrema),
    )
    failures = [(n, hi[0], cap(r, n), sorted(hi[1]))
                for n, (_, hi) in enumerate(full) if hi[0] > cap(r, n)]
    check.check("All hereditary D_12 caps on all 2^29 subsets", not failures, repr(failures))
    omega = max(n for n, (_, hi) in enumerate(full) if hi[0] == choose2(n))
    alpha = max(n for n, (lo, _) in enumerate(full) if lo[0] == 0)
    check.check("Clique number is 11", omega == r - 1)
    check.check("Independence number is 4", alpha == 4)
    anchors = set(data["anchors"])
    check.check("Named four anchors are independent", edge_count(edges, anchors) == 0)
    support = {v: {q for q in anchors if pair(v, q) in edges}
               for v in all_vertices - anchors}
    check.check("Every nonanchor has one or two anchor neighbors",
                all(1 <= len(s) <= 2 for s in support.values()))
    check.check("There are exactly r=12 two-supported exceptions",
                sum(len(s) == 2 for s in support.values()) == r)
    p, j, t = map(set, (data["deleted_row"], data["receiving_row"], data["test_set"]))
    zblock = p | {"x", "y"}
    neighbors = {u: {v for v in all_vertices - {u} if pair(u, v) in edges}
                 for u in all_vertices}
    check.check("P is the private row of q and has exactly r-1 vertices",
                p == {"q"} | {v for v, s in support.items() if s == {"q"}}
                and len(p) == r - 1)
    check.check("x,y are the only exceptions incident with q, parallel and nonadjacent",
                {v for v, s in support.items() if len(s) == 2 and "q" in s} == {"x", "y"}
                and support["x"] == support["y"] == {"q", "j0"}
                and pair("x", "y") not in edges)
    check.check("Every deleted-row vertex has degree exactly r",
                all(len(neighbors[v]) == r for v in p))
    check.check("The receiving row has pointwise charge exactly one",
                all(len(neighbors[v] & p) + int({"x", "y"} <= neighbors[v]) == 1 for v in j))
    check.check("Z is saturated and all outsiders have at most two neighbors in Z",
                edge_count(edges, zblock) == cap(r, len(zblock))
                and all(len(neighbors[v] & zblock) <= 2 for v in all_vertices - zblock))
    union = t & (neighbors["x"] | neighbors["y"])
    common = t & neighbors["x"] & neighbors["y"]
    a_charge = sum(len(neighbors[v] & t) for v in p)
    slack = cap(r, len(zblock | t)) - edge_count(edges, zblock | t)
    fold_edges = edge_count(edges, t) + len(union)
    delta = fold_edges - cap(r, len(t) + 1)
    check.check("The folded 13-set really has 68 edges, exceeding cap 67",
                fold_edges == 68 and cap(r, len(t) + 1) == 67 and delta == 1)
    check.check("Exact original slack is one: t=12, A=10, C=0, sigma_Z=1",
                (len(t), a_charge, len(common), slack) == (12, 10, 0, 1)
                and delta == len(t) - a_charge - len(common) - slack)
    check.check("The witness is explicitly underloaded and fails receiving-row degree",
                len(vertices) == 29 < 4 * r + 1
                and all(len(neighbors[v]) == 5 < r + 1 for v in j))
    mutated = edges | {pair("t0", "t1")}
    bad = profiles(data, mutated, all_vertices)
    check.check("Negative control detects an actual original cap violation",
                bad[r + 1][1][0] > cap(r, r + 1))
    print("n, maximum original edges, D_12(n):")
    for n, (_, hi) in enumerate(full):
        print(f"{n:2d} {hi[0]:3d} {cap(r, n):3d}")
    print("Scope: one local obstruction; no normalized counterexample or fold theorem.")
    return check.finish()


if __name__ == "__main__":
    sys.exit(main())
