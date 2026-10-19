"""Independent finite attacks on the frozen cubic lemniscate checker.

The root route starts with an exact Gaussian-rational root r, forms
s=r^3+3*a2*r, and factors the remaining quadratic. It does not use Cardano,
a cube root, or selection of a quadratic resolvent root. At 128 bits it
checks five prescribed roots inside each of twelve 64-bit input boxes.
It also tests exact analytic instances and explicit failure cases.

This finite diagnostic does not certify the full parameter range. The
uniform bounds require the report's analytic audit and the full subject run.
One thread, no random inputs, normally seconds, no stored outputs read.
From the repository root, set PYTHONPATH to assets/subject/runtime beside
this file and run with the installed environment using uv run --no-sync
python -P <path-to-this-file>. No packages are installed by this script.
"""

from __future__ import annotations

import contextlib
import importlib.metadata
import importlib.util
import io
import json
from pathlib import Path
import sys
import typing

from flint import acb, arb, ctx
import tools
from tools import Checker, evidence_parser


HERE = Path(__file__).resolve().parent


def quadratic_density(root: acb, a2: arb) -> arb:
    """Inverse-derivative sum using (z-r)(z^2+r*z+r^2+3*a2)."""
    discriminant = (-3 * root * root - 12 * a2).sqrt()
    roots = (root, (-root + discriminant) / 2, (-root - discriminant) / 2)
    return sum((1 / (3 * abs(z * z + a2)) for z in roots), arb(0))


def main() -> int:
    parser = evidence_parser(__doc__, quick=False)
    parser.add_argument("--subject", type=Path, default=HERE / "assets/subject/evidence/main.py")
    parser.add_argument("--cases", type=Path, default=HERE / "assets/diagnostic_inputs.json")
    args = parser.parse_args()
    print("EXECUTION_ENVIRONMENT " + json.dumps({
        "sys_prefix": sys.prefix,
        "tools_file": tools.__file__,
        "typing_file": typing.__file__,
        "python_flint_version": importlib.metadata.version("python-flint"),
        "safe_path": sys.flags.safe_path,
    }, sort_keys=True), flush=True)
    expected_runtime = args.subject.resolve().parent.parent / "runtime/tools/__init__.py"
    if Path(tools.__file__).resolve() != expected_runtime.resolve():
        raise RuntimeError("tools import is not the retained subject runtime")
    spec = importlib.util.spec_from_file_location("frozen_cubic_subject", args.subject)
    if spec is None or spec.loader is None:
        raise RuntimeError("cannot load the retained subject")
    subject = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(subject)
    # Importing the subject defines functions and constants; it does not run main.
    ctx.threads = 1
    checker = Checker()
    inputs = json.loads(args.cases.read_text())
    for case in inputs["cases"]:
        ctx.prec = 64
        a2 = arb(case["a2"])
        center_root = acb(arb(case["root"][0]), arb(case["root"][1]))
        center_s = center_root**3 + 3 * a2 * center_root
        radius = arb(inputs["box_radius"])
        s_box = acb(arb(center_s.real, radius), arb(center_s.imag, radius))
        numerator, denominator = subject.root_sum(s_box, a2, a2**3)
        enclosure = numerator / (3 * denominator)
        checker.check(case["name"] + ": finite Cardano density box", enclosure.is_finite())
        ctx.prec = 128
        a2 = arb(case["a2"])
        center_root = acb(arb(case["root"][0]), arb(case["root"][1]))
        perturbation = arb(inputs["root_perturbation"])
        offsets = (acb(0), acb(perturbation), acb(-perturbation), acb(0, perturbation), acb(0, -perturbation))
        contained_inputs = True
        contained_densities = True
        for offset in offsets:
            root = center_root + offset
            s = root**3 + 3 * a2 * root
            reference = quadratic_density(root, a2)
            contained_inputs = contained_inputs and s_box.real.contains(s.real) and s_box.imag.contains(s.imag)
            contained_densities = contained_densities and reference.is_finite() and enclosure.contains(reference)
        checker.check(case["name"] + ": all five generated inputs lie in the box", contained_inputs)
        checker.check(case["name"] + ": quadratic-division densities lie in the Cardano box", contained_densities)

    # Hand-derived value: roots of z^3+3z=0 are 0,+i*sqrt(3),-i*sqrt(3).
    ctx.prec = 64
    origin = subject.g1(acb(0))
    ctx.prec = 128
    checker.check("analytic G1(0)=2/3 is contained", origin.contains(arb(2) / 3))
    checker.check("deliberately wrong G1(0)=4/3 is rejected", not origin.contains(arb(4) / 3))

    # At s=2i the polynomial has roots i,i,-2i. The numerator is 2*sqrt(3).
    ctx.prec = 64
    numerator, denominator = subject.root_sum(acb(0, 2), arb(1), arb(1))
    singular = subject.g1(acb(0, 2))
    ctx.prec = 128
    checker.check("critical numerator encloses 2*sqrt(3)", numerator.contains(2 * arb(3).sqrt()))
    checker.check("critical denominator is zero", denominator == 0)
    checker.check("unwindowed critical density is nonfinite", not singular.is_finite())

    ctx.prec = 64
    upper, upper_count = subject.bound_integral(lambda _: arb(3, 1), arb(0), arb(1), arb(0), max_depth=0)
    lower, lower_count = subject.bound_integral(lambda _: arb(3, 1), arb(0), arb(1), arb(0), upper=False, max_depth=0)
    checker.check("finite depth cap retains rectangle bounds [2,4]", lower == 2 and upper == 4 and lower_count == 1 and upper_count == 1)
    width = arb(1, arb(1) / 4)
    checker.check("negative rectangle bound uses correct width endpoints", subject.piece_bound(arb(-2, 1), width, True) == -arb(3) / 4 and subject.piece_bound(arb(-2, 1), width, False) == -arb(15) / 4)
    checker.check("positive rectangle bound uses correct width endpoints", subject.piece_bound(arb(2, 1), width, True) == arb(15) / 4 and subject.piece_bound(arb(2, 1), width, False) == arb(3) / 4)
    checker.check("sign-changing rectangle bound contains both extremes", subject.piece_bound(arb(0, 1), width, True) == arb(5) / 4 and subject.piece_bound(arb(0, 1), width, False) == -arb(5) / 4)

    nonfinite_rejected = False
    try:
        subject.bound_integral(lambda _: arb("nan"), arb(0), arb(1), arb(0), max_depth=0)
    except ArithmeticError:
        nonfinite_rejected = True
    checker.check("nonfinite depth-cap input raises ArithmeticError", nonfinite_rejected)

    bad_window_rejected = False
    try:
        subject.regime_b_box(arb(0), arb(0))
    except ArithmeticError:
        bad_window_rejected = True
    checker.check("beta=0 invalid window raises ArithmeticError", bad_window_rejected)

    rejected_cover = Checker(quiet=True)
    capture = io.StringIO()
    with contextlib.redirect_stdout(capture):
        subject.cover_b(arb(0), arb(2) ** -41, rejected_cover)
        rejection_exit = rejected_cover.finish()
    checker.check("unresolved tiny cover records failure and exits nonzero", not rejected_cover.passed and rejection_exit == 1)
    print("finite diagnostic: 12 input boxes, 60 prescribed-root instances; failure cases tested")
    return checker.finish()


if __name__ == "__main__":
    sys.exit(main())
