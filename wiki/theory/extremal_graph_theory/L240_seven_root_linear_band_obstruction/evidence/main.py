"""Check L240 through its shared, exact profile-envelope evidence.

The full run regenerates the Higman–Sims graph and all seven-root tables,
checks every exact branch lower bound, and checks the interior-band mixture.
It also runs the related research controls and separately labeled numerical
optimality probes. Runtime: several minutes. --quick checks the small controls
only and does not verify the Higman–Sims clause of L240.
"""

from pathlib import Path
import runpy

if __name__ == '__main__':
    research = Path(__file__).resolve().parents[4] / 'research/triangle_free_bipartization'
    runpy.run_path(str(research / 'evidence/main.py'), run_name='__main__')
