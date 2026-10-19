"""Replay the exact finite symmetric polygon census and verify its retained data.

From the repository root:
  uv run --no-sync python wiki/research/leads/concentric_polygon_census/evidence/main.py

Default: m=3..32 concentric half-step polygons, n=8..24 affine regular
polygons; every positive critical parameter, plus the generic-case proof in
sketch.md. --quick checks only m=3..6 and n=8..10. Expected full runtime is
about half a minute, single-threaded, using SymPy and python-flint.

Equality: exact rational polynomials modulo cyclotomic polynomials. Strict
order: certified Arb enclosures with a finite precision cap that raises on
failure. All retained event labels, positions and vertex counts are rebuilt.
This author check awards no independent standing or unbounded-order result.
"""

import json
from pathlib import Path

from flint import ctx
from tools import Checker, evidence_parser

from util.census import affine, concentric, controls


def main():
    parser = evidence_parser(__doc__)
    parser.add_argument("--assets", type=Path, default=Path(__file__).parent / "assets",
                        help="exact census inputs; override also permits corruption controls")
    args = parser.parse_args()
    ctx.threads = 1
    checker = Checker()
    controls()
    checker.check("exact arithmetic, branches, zero roots and strict boundary controls", True)
    domains = [("concentric", concentric, range(3, 7 if args.quick else 33)),
               ("affine", affine, range(8, 11 if args.quick else 25))]
    expected_names = {
        *(f"concentric_{m:02}.json" for m in range(3, 33)),
        *(f"affine_{n:02}.json" for n in range(8, 25)),
    }
    checker.check("retained input covers exactly the two full order ranges",
                  {p.name for p in args.assets.glob("*.json")} == expected_names)
    totals = {"concentric": 0, "affine": 0}
    for name, compute, orders in domains:
        for order in orders:
            computed = compute(order)
            path = args.assets / f"{name}_{order:02}.json"
            expected = json.loads(path.read_text())
            checker.check(f"{name} {order}: exact event census and every recorded count",
                          computed == expected)
            admissible = [
                row for row in computed["critical"]
                if row.get("position", "inside") == "inside"
            ]
            checker.check(f"{name} {order}: no every-vertex counterexample",
                          all(max(row["counts"]) >= computed["threshold"] for row in admissible)
                          and max(computed["generic_counts"]) >= computed["threshold"])
            if name == "concentric":
                expected_events = sorted([
                    ["P", order // 2, (order - 1) // 2],
                    ["Q", order // 2, (order - 1) // 2],
                ])
                # Branches are checked in the complete retained census above.
                actual_events = sorted([e[:3] for row in admissible for e in row["events"]])
                checker.check(f"concentric {order}: only the two farthest-distance events",
                              actual_events == expected_events
                              and sorted(row["counts"] for row in admissible)
                              == [[order - 1, order], [order, order - 1]])
            totals[name] += len(computed["critical"])
    print(f"Coverage ({'quick subset' if args.quick else 'full'}): {totals}")
    return checker.finish()


if __name__ == "__main__":
    raise SystemExit(main())
