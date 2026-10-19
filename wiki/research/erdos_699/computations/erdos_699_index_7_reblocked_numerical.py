"""Numerical index-seven joint sources using shorter witness blocks.

The original intercepts, relaxed thresholds, and exact forest are unchanged.
This file writes only new artifacts; the retained numerical fallback stays
available independently. --target-only computes the useful direct-source
classification before the optional uniform fallback search.
"""

import argparse
import json
import time
from fractions import Fraction as F
from pathlib import Path

from erdos_699_off_diagonal_gcd_sharp import gcd_exponent_lower
from erdos_699_off_diagonal_pade import rational
from erdos_699_off_diagonal_reblocking import joint_clause_threshold, prepare
from mpmath import iv

HERE = Path(__file__).parent
OUTPUT = Path(__file__).with_suffix(".json")
TARGET = 10**8


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--target-only", action="store_true")
    parser.add_argument("--check", action="store_true")
    args = parser.parse_args()
    if args.check:
        return check()
    original_path = HERE / "erdos_699_index_7_effective.json"
    relaxed_path = HERE / "erdos_699_index_7_relaxed_sources.json"
    old_path = HERE / "erdos_699_index_7_joint_numerical.json"
    original = json.loads(original_path.read_text())
    relaxed = json.loads(relaxed_path.read_text())
    old = {r["source_id"]: r for r in json.loads(old_path.read_text())}
    records = []
    start = time.monotonic()
    direct = 0
    result = {
        "scope": "Unchanged index-seven joint clauses with shorter integer Pade witnesses.",
        "original_file": original_path.name,
        "relaxed_file": relaxed_path.name,
        "old_numerical_file": old_path.name,
        "target_height_power_of_ten": TARGET,
        "records": records,
    }
    for index, source in enumerate(original["sources"]):
        sid = source["id"]
        certificate = source["certificate"]
        eta = relaxed["source_eta"][sid]
        prepared = prepare(certificate, threshold_weakening=eta)
        block = F(prepared["witness_block_parameter"])
        product = rational(block) * TARGET * iv.log(10)
        m0 = int(product.a) - 1
        assert product >= m0 + 1 and m0 >= 2
        analytic = gcd_exponent_lower(*prepared["directions"], terms=4000, m0=m0)
        ell = F(analytic["ell_lower"])
        row = {
            "source_id": sid,
            "prepared": prepared,
            "target_gcd_certificate": analytic,
            "old_threshold_power_of_ten": old[sid]["threshold_power_of_ten"],
        }
        gap = 6 if source["hypothesis"]["kind"] == "pair" else 36
        try:
            bound = joint_clause_threshold(
                certificate,
                m0,
                gap=gap,
                maximum_shift=6,
                gcd_log_rate=ell,
                threshold_weakening=eta,
                prepared=prepared,
            )
        except AssertionError:
            bound = None
        success = bound is not None and bound["threshold_power_of_ten"] <= TARGET
        row["directly_valid_at_target"] = success
        if bound is not None:
            row["target_numerical_certificate"] = bound
        direct += success
        records.append(row)
        if (index + 1) % 20 == 0:
            OUTPUT.write_text(json.dumps(result, indent=2) + "\n")
            print(
                json.dumps(
                    {
                        "sources": index + 1,
                        "direct": direct,
                        "elapsed": round(time.monotonic() - start, 1),
                    }
                ),
                flush=True,
            )
    result["target_summary"] = {
        "sources": len(records),
        "directly_valid": direct,
        "remaining_source_ids": [
            r["source_id"] for r in records if not r["directly_valid_at_target"]
        ],
        "improved_source_margin_count": sum(
            F(r["prepared"]["new_uniform_margin_lower"])
            > F(r["prepared"]["old_uniform_margin_lower"])
            for r in records
        ),
        "maximum_margin_factor": max(
            float(
                F(r["prepared"]["new_uniform_margin_lower"])
                / F(r["prepared"]["old_uniform_margin_lower"])
            )
            for r in records
        ),
    }
    OUTPUT.write_text(json.dumps(result, indent=2) + "\n")
    print(json.dumps(result["target_summary"], indent=2), flush=True)
    if args.target_only:
        return
    # One uniform gcd bound is shared across each direction.
    grouped = {}
    for row in records:
        key = tuple(row["prepared"]["directions"])
        grouped.setdefault(key, []).append(row)
    by_id = {r["id"]: r for r in original["sources"]}
    gcd_records = []
    for number, (directions, rows) in enumerate(sorted(grouped.items())):
        target = max(F(r["prepared"]["requested_gcd_log_rate"]) for r in rows)
        for exponent in range(5, 16):
            analytic = gcd_exponent_lower(*directions, terms=4000, m0=10**exponent)
            if F(analytic["ell_lower"]) > target:
                break
        else:
            raise AssertionError(("No uniform rate", directions, str(target)))
        upper = analytic["m0"]
        for trial in (2 * (upper // 10), 5 * (upper // 10)):
            if trial < 10**5:
                continue
            proposal = gcd_exponent_lower(*directions, terms=4000, m0=trial)
            if F(proposal["ell_lower"]) > target:
                analytic = proposal
                break
        gcd_records.append(
            {
                "directions": list(directions),
                "required_log_rate": str(target),
                "analytic_certificate": analytic,
                "source_ids": [r["source_id"] for r in rows],
            }
        )
        for row in rows:
            source = by_id[row["source_id"]]
            eta = relaxed["source_eta"][source["id"]]
            bound = joint_clause_threshold(
                source["certificate"],
                analytic["m0"],
                gap=6 if source["hypothesis"]["kind"] == "pair" else 36,
                maximum_shift=6,
                gcd_log_rate=analytic["ell_lower"],
                threshold_weakening=eta,
                prepared=row["prepared"],
            )
            row["uniform_numerical_certificate"] = bound
        if (number + 1) % 20 == 0:
            result["uniform_gcd_records"] = gcd_records
            OUTPUT.write_text(json.dumps(result, indent=2) + "\n")
            print(
                json.dumps(
                    {
                        "uniform_directions": number + 1,
                        "elapsed": round(time.monotonic() - start, 1),
                    }
                ),
                flush=True,
            )
    result["uniform_gcd_records"] = gcd_records
    result["uniform_summary"] = {
        "directions": len(gcd_records),
        "maximum_threshold_power_of_ten": max(
            r["uniform_numerical_certificate"]["threshold_power_of_ten"]
            for r in records
        ),
        "maximum_m0": max(r["analytic_certificate"]["m0"] for r in gcd_records),
        "improved_threshold_count": sum(
            r["uniform_numerical_certificate"]["threshold_power_of_ten"]
            < r["old_threshold_power_of_ten"]
            for r in records
        ),
    }
    result["helper_files"] = [
        "erdos_699_off_diagonal_reblocking.py",
        "erdos_699_off_diagonal_gcd_sharp.py",
        "erdos_699_off_diagonal_explicit_clauses.py",
    ]
    OUTPUT.write_text(json.dumps(result, indent=2) + "\n")
    print(json.dumps(result["uniform_summary"], indent=2))


def check():
    result = json.loads(OUTPUT.read_text())
    for field in ("original", "relaxed", "old_numerical"):
        path = HERE / result[field + "_file"]
        assert path.is_file(), path.name
    for name in result["helper_files"]:
        assert (HERE / name).is_file(), name
    original = json.loads((HERE / result["original_file"]).read_text())
    relaxed = json.loads((HERE / result["relaxed_file"]).read_text())
    sources = {r["id"]: r for r in original["sources"]}
    groups = {tuple(r["directions"]): r for r in result["uniform_gcd_records"]}
    assert len(groups) == 210
    for group in groups.values():
        analytic = group["analytic_certificate"]
        replay = gcd_exponent_lower(
            *analytic["directions"],
            terms=analytic["terms"],
            m0=analytic["m0"],
            scale=analytic["rounding_denominator"],
            root_scale=analytic["root_scale"],
        )
        assert replay == analytic
        assert F(analytic["ell_lower"]) > F(group["required_log_rate"])
    assert {r["source_id"] for r in result["records"]} == set(sources)
    for row in result["records"]:
        source = sources[row["source_id"]]
        eta = relaxed["source_eta"][source["id"]]
        prepared = prepare(source["certificate"], threshold_weakening=eta)
        assert prepared == row["prepared"]
        group = groups[tuple(prepared["directions"])]
        assert row["source_id"] in group["source_ids"]
        analytic = group["analytic_certificate"]
        replay = joint_clause_threshold(
            source["certificate"],
            analytic["m0"],
            gap=6 if source["hypothesis"]["kind"] == "pair" else 36,
            maximum_shift=6,
            gcd_log_rate=analytic["ell_lower"],
            threshold_weakening=eta,
            prepared=prepared,
        )
        assert replay == row["uniform_numerical_certificate"]
    maximum = max(
        r["uniform_numerical_certificate"]["threshold_power_of_ten"]
        for r in result["records"]
    )
    assert maximum == result["uniform_summary"]["maximum_threshold_power_of_ten"]
    print(
        json.dumps(
            {
                "uniform_gcd_directions_checked": len(groups),
                "joint_clauses_checked": len(result["records"]),
                "maximum_threshold_power_of_ten": maximum,
            },
            indent=2,
        )
    )


if __name__ == "__main__":
    main()
