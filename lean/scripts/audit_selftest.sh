#!/usr/bin/env bash
set -euo pipefail

# Prove the audit still rejects what it must and admits only what it re-evaluates
# -------------------------------------------------------------------------------
# Usage: scripts/audit_selftest.sh
# Environment: LEAN_NUM_THREADS caps Lake's parallel compiles (default 4).
#
# The audit's value is its refusals: sorried proofs, custom axioms,
# compiler-shaped axioms that do not compile, compiler-shaped axioms
# that evaluate to false, unsafe constants, opaque constants, partial
# defs, @[implemented_by], @[extern], @[csimp], metaprogramming, a
# corpus module importing the audit library, malformed claim triples and
# a stale manifest must all fail it; a native_decide proof and a
# kernel-inert notation must each pass it with its NOTE line, and the
# manifest must record a native_decide claim's compiler axiom where each
# row should. This harness re-proves each verdict against the live
# toolchain: for every fixture in scripts/selftest/ (one class per
# file), it copies the fixture to Erdos/AuditSelfTestProbe.lean, builds,
# runs the audit, and requires a nonzero exit whose output contains
# every `-- EXPECT:` fragment of the fixture (one per line). A fixture
# with `-- MODE: check` runs `audit --check` instead of the bare audit.
# A fixture with `-- MODE: admit` must instead pass: exit zero with the
# fragments (the audit's NOTE line) in its output. A fixture with
# `-- MODE: print` must pass the same way under `audit --print`, and the
# manifest it prints must hold exactly the compiler records that its
# `-- RECORD: <claim id or top> <declaration>` lines place in each named
# claim row and in the top-level array (`top`): each record from the
# probe module, and each record of a row naming an axiom the row lists
# and appearing in the top-level array. No row or array that the lines
# leave unnamed may hold a record from the probe module, and a print
# fixture without RECORD lines fails. python3 reads that manifest. A
# final control run on the unmodified corpus must pass. Each failure
# prints the last 40 lines of the failing command's output. The probe is
# removed on every exit path. The stamp digest is taken before the first
# fixture and taken again after the control; only a complete pass whose
# two digests match rewrites the stamp, so an input edited during the
# run is never certified. Ignored build state may change on any run.
#
# Run on demand after editing Audit/ or bumping the toolchain -- it
# rebuilds and re-imports the corpus once per fixture, so it takes
# minutes, not seconds. The clean gate (scripts/gate.sh --clean) runs
# the archived revision's copy of it.

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd -P)"
LEAN_DIR="$(dirname "$SCRIPT_DIR")"
PROBE="$LEAN_DIR/Erdos/AuditSelfTestProbe.lean"
PROBE_MODULE="Erdos.AuditSelfTestProbe"

# Lake compiles one module per worker thread of its Lean runtime, sized by
# this variable; at one thread per CPU a full build can take most of a
# machine's memory.
export LEAN_NUM_THREADS="${LEAN_NUM_THREADS:-4}"

# Refuse a thread cap that is not a positive whole number before any
# Lake command.
if ! [[ "$LEAN_NUM_THREADS" =~ ^[1-9][0-9]*$ ]]; then
    echo "Error: LEAN_NUM_THREADS must be a positive whole number, not '$LEAN_NUM_THREADS'." >&2
    exit 2
fi

# Print the first expected fragment (one per line) that the output lacks.
first_missing() {
    local fragment
    while IFS= read -r fragment; do
        if ! grep -qF -- "$fragment" <<<"$2"; then
            printf '%s\n' "$fragment"
            return
        fi
    done <<<"$1"
}

# Read the manifest from a print fixture's audit output (stdin) and check
# the compiler records its `-- RECORD:` lines (the first argument) place,
# and that no unnamed row or array holds one of the probe's; exit nonzero
# with the first misplacement.
RECORD_CHECK="$(
    cat <<'PY'
import json
import sys

records, module = sys.argv[1], sys.argv[2]
text = sys.stdin.read()
try:
    manifest = json.JSONDecoder().raw_decode(text, text.find("\n{") + 1)[0]
    rows = {row["id"]: row for row in manifest["claims"]}
except (ValueError, KeyError, TypeError) as error:
    sys.exit(f"no manifest in the audit output ({error})")
placed = {}
for line in records.splitlines():
    location, declaration = line.split()
    placed.setdefault(location, []).append(declaration)
for location, declarations in placed.items():
    row = rows.get(location)
    if row is None and location != "top":
        sys.exit(f"no claim row {location}")
    found = (manifest if row is None else row)["compiler"]
    names = sorted(record["declaration"] for record in found)
    if names != sorted(declarations):
        sys.exit(f"{location} records {names}, not {sorted(declarations)}")
    for record in found:
        if record["module"] != module:
            sys.exit(f"{location} records a declaration of {record['module']}")
        if row is not None and record["axiom"] not in row["axioms"]:
            sys.exit(f"{location} records {record['axiom']} outside its axioms")
        if row is not None and record not in manifest["compiler"]:
            sys.exit(f"{location} records a record the top-level array lacks")
for location, row in [("top", manifest), *rows.items()]:
    if location not in placed and any(
        record["module"] == module for record in row["compiler"]
    ):
        sys.exit(f"{location} records a probe declaration that no RECORD line places")
PY
)"
check_records() {
    python3 -I -c "$RECORD_CHECK" "$1" "$PROBE_MODULE" <<<"$2"
}

# The digest of the inputs this run tests, compared again after the control.
BEFORE_DIGEST="$("$SCRIPT_DIR/selftest_digest.sh")"

# Never overwrite or unlink a source path that the caller already owns.
if [[ -e "$PROBE" || -L "$PROBE" ]]; then
    echo "Error: refusing to replace existing probe path: $PROBE" >&2
    exit 1
fi

# Refuse a cold cache before creating any temporary source module.
if [[ ! -f "$LEAN_DIR/.lake/packages/mathlib/.lake/build/lib/lean/Mathlib.olean" &&
    ! -f "$LEAN_DIR/.lake/packages/mathlib/.lake/build/lib/Mathlib.olean" ]]; then
    echo "Error: Mathlib binary cache is missing; run 'lake exe cache get' from lean/." >&2
    echo "Refusing to run 'lake build' because it may build Mathlib from source." >&2
    exit 1
fi
trap 'rm -f "$PROBE"' EXIT

# Lake and the audit resolve this project from lean/.
cd "$LEAN_DIR"
failed=0
for fixture in "$SCRIPT_DIR"/selftest/*.lean; do
    name="$(basename "$fixture" .lean)"
    expect="$(sed -n 's/^-- EXPECT: //p' "$fixture")"
    mode="$(sed -n 's/^-- MODE: //p' "$fixture" | head -1)"
    records="$(sed -n 's/^-- RECORD: //p' "$fixture")"
    if [[ -z "$expect" ]] || grep -qx -- '-- EXPECT: *' "$fixture"; then
        echo "selftest FAIL $name: missing EXPECT"
        failed=1
        continue
    fi
    if [[ "$mode" == "print" && -z "$records" ]]; then
        echo "selftest FAIL $name: missing RECORD"
        failed=1
        continue
    fi
    cp "$fixture" "$PROBE"

    if ! output="$(nice -n 15 lake build 2>&1)"; then
        echo "selftest FAIL $name: fixture does not build"
        tail -n 40 <<<"$output"
        failed=1
        continue
    fi

    status=0
    if [[ "$mode" == "check" ]]; then
        output="$(nice -n 15 lake exe audit --check 2>&1)" || status=$?
    elif [[ "$mode" == "print" ]]; then
        output="$(nice -n 15 lake exe audit --print 2>&1)" || status=$?
    else
        output="$(nice -n 15 lake exe audit 2>&1)" || status=$?
    fi
    missing="$(first_missing "$expect" "$output")"

    if [[ "$mode" == "admit" || "$mode" == "print" ]]; then
        if [[ "$status" -ne 0 ]]; then
            echo "selftest FAIL $name: audit refused an admitted corpus"
            tail -n 40 <<<"$output"
            failed=1
        elif [[ -n "$missing" ]]; then
            echo "selftest FAIL $name: audit passed without expected report '$missing'"
            tail -n 40 <<<"$output"
            failed=1
        elif [[ "$mode" == "print" ]] \
            && ! verdict="$(check_records "$records" "$output" 2>&1)"; then
            echo "selftest FAIL $name: record check failed: $verdict"
            failed=1
        else
            echo "selftest ok   $name"
        fi
    elif [[ "$status" -eq 0 ]]; then
        echo "selftest FAIL $name: audit passed on a violating corpus"
        tail -n 40 <<<"$output"
        failed=1
    elif [[ -n "$missing" ]]; then
        echo "selftest FAIL $name: audit failed without expected message '$missing'"
        tail -n 40 <<<"$output"
        failed=1
    else
        echo "selftest ok   $name"
    fi
done
rm -f "$PROBE"

# The unmodified corpus must pass the full build and audit checks.
if output="$(nice -n 15 lake build 2>&1)" \
    && output="$(nice -n 15 lake exe audit --check 2>&1)"; then
    echo "selftest ok   control (clean corpus passes)"
else
    echo "selftest FAIL control: clean corpus does not pass"
    tail -n 40 <<<"$output"
    failed=1
fi

# An input that changed during the run is not the input the run tested.
AFTER_DIGEST="$("$SCRIPT_DIR/selftest_digest.sh")"
if [[ "$AFTER_DIGEST" != "$BEFORE_DIGEST" ]]; then
    echo "selftest FAIL inputs: the stamp's inputs changed during the run"
    failed=1
fi

if [[ "$failed" -eq 0 ]]; then
    # stamp the pass: the gate checks this digest against the audited
    # surface (Audit/ source, toolchain + mathlib pins, harness,
    # fixtures), so a bump that skips the self-test fails the gate
    # instead of silently disarming a refusal
    printf '%s\n' "$BEFORE_DIGEST" >"$SCRIPT_DIR/selftest.stamp"
    echo "SELFTEST PASS (stamp written)"
else
    echo "SELFTEST FAIL"
fi
exit "$failed"
