"""Discover exact census data; writes only to an explicitly supplied directory.

From the repository root: uv run --no-sync python <this-path> --outdir <scratch>.
Domains: m=3..32, n=8..24; --quick uses m=3..6, n=8..10.
This is discovery, not the retained-data verification entry point.
"""

import argparse
import json
from pathlib import Path
from time import monotonic

from util.census import affine, concentric


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--outdir", type=Path, required=True)
    parser.add_argument("--quick", action="store_true")
    args = parser.parse_args()
    args.outdir.mkdir(parents=True, exist_ok=True)
    ranges = [("concentric", concentric, range(3, 7 if args.quick else 33)),
              ("affine", affine, range(8, 11 if args.quick else 25))]
    for name, compute, orders in ranges:
        for order in orders:
            start = monotonic()
            data = compute(order)
            path = args.outdir / f"{name}_{order:02}.json"
            path.write_text(json.dumps(data, indent=2) + "\n")
            inside = [row for row in data["critical"] if row.get("position", "inside") == "inside"]
            candidates = [row for row in inside if max(row["counts"]) < data["threshold"]]
            print(f"{name} {order}: {len(data['critical'])} critical, "
                  f"{len(inside)} admissible, {len(candidates)} candidates, "
                  f"{monotonic()-start:.2f}s", flush=True)
            if candidates:
                raise RuntimeError(f"possible counterexample: inspect {path}")


if __name__ == "__main__":
    main()
