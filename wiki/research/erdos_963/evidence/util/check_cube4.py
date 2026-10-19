"""Verify the explicit 35-edge obstruction to deleting eight ternary vectors."""
import json
from itertools import product, combinations
from pathlib import Path

certificate = json.loads(
    (Path(__file__).resolve().parent.parent / 'assets' / 'cube4.json').read_text())
blocks, edges = certificate['blocks'], certificate['edges']
expected = {v for v in product((-1, 0, 1), repeat=4)
            if next((x for x in v if x), -1) == 1}
actual = [tuple(v) for block in blocks for v in block]
assert len(actual) == 40 and set(actual) == expected
assert len(blocks) == len(edges) == 3
for block, family in zip(blocks, edges):
    for edge in family:
        assert len(edge) == len(set(edge)) == 6
        vectors = [block[i] for i in edge]
        sums = {tuple(sum(e * v[j] for e, v in zip(eps, vectors))
                      for j in range(4))
                for eps in product((0, 1), repeat=6)}
        assert len(sums) == 64
    for pair in combinations(range(len(block)), 2):
        assert any(not set(pair).intersection(edge) for edge in family)
print('Verified: every 32-element subset of the 40-vector configuration contains a dissociated 6-set.')
