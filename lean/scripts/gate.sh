#!/usr/bin/env bash
set -euo pipefail

# Validate the Lean corpus and audit stamp
# ----------------------------------------
# Usage: scripts/gate.sh [--clean [rev]]
# Environment: LEAN_NUM_THREADS caps Lake's parallel compiles (default 4).
#
# No arguments validate the working tree. Clean mode archives a committed
# revision (HEAD by default), fetches its binary cache, and hands that
# independent checkout to the revision's own launcher and then to its own
# self-test harness, which reruns the refusal suite there.

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd -P)"
LEAN_DIR="$(dirname "$SCRIPT_DIR")"

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

if [[ "$#" -gt 0 ]]; then
    if [[ "$1" != "--clean" || "$#" -gt 2 || "${2:-HEAD}" == -* ]]; then
        echo "Usage: scripts/gate.sh [--clean [rev]]" >&2
        exit 2
    fi
    REV="$(git -C "$LEAN_DIR" rev-parse --verify --end-of-options "${2:-HEAD}^{commit}")"
    GATE_TEMP_DIR="$(mktemp -d)"
    trap 'rm -rf -- "$GATE_TEMP_DIR"' EXIT
    # Archive from lean/ so the extracted project has no extra path prefix.
    # Write the archive first: tar may stop at its end marker before Git has
    # written the padding, giving Git SIGPIPE under pipefail on macOS.
    git -C "$LEAN_DIR" archive --format=tar --output="$GATE_TEMP_DIR/project.tar" "$REV"
    mkdir "$GATE_TEMP_DIR/project"
    tar -xf "$GATE_TEMP_DIR/project.tar" -C "$GATE_TEMP_DIR/project"
    LEAN_DIR="$GATE_TEMP_DIR/project"
    # A clean archive has no compiled dependencies: fetch them before building.
    (cd "$LEAN_DIR" && lake exe cache get)
fi

# Lake resolves this project and its generated manifest from lean/.
cd "$LEAN_DIR"
if [[ ! -f .lake/packages/mathlib/.lake/build/lib/lean/Mathlib.olean &&
    ! -f .lake/packages/mathlib/.lake/build/lib/Mathlib.olean ]]; then
    echo "Error: Mathlib binary cache is missing; run 'lake exe cache get' from lean/." >&2
    echo "Refusing to run 'lake build' because it may build Mathlib from source." >&2
    exit 1
fi

# Clean mode keeps the cache check above, which older launchers lack, and
# then lets the archived revision decide: its own launcher validates the
# tree in place and its own harness reruns the refusal suite.
if [[ "$#" -gt 0 ]]; then
    bash scripts/gate.sh
    bash scripts/audit_selftest.sh
    echo "Lean clean gate passed."
    exit 0
fi

# The audit walks declarations, and an `example` (a fidelity example
# included) leaves none, so two rules read the sources before the build.
# The first refuses what could hide the sorry warning checked below,
# matching anywhere in a line, comments included: in a corpus module, a
# `set_option` line that mentions sorry, any spelling of the `warn.sorry`
# option, or `#guard_msgs`, which swallows a command's messages; in the
# lakefile, any `sorry`, a word it has no other use for.
if grep -rnE --include='*.lean' \
    'set_option.*sorry|warn(»)?[[:space:]]*\.[[:space:]]*(«)?sorry|#guard_msgs' \
    Erdos >&2 || grep -Hn 'sorry' lakefile.toml >&2; then
    echo "Error: a corpus source could silence the build's sorry warning." >&2
    exit 1
fi
# The second refuses a compiler-evaluated decision (`native_decide`,
# `decide +native`, a `native :=` option) inside an `example`, whose
# compiler axiom no declaration would carry. A command starts on a line
# that begins in the first column with a command keyword or modifier, a
# `#` command, an attribute (`@[`) or a doc comment; it is an example when
# `example` follows the line's start, a space or an attribute's `]`,
# outside a doc comment. Line comments are ignored.
if ! find Erdos -name '*.lean' -exec awk '
    BEGIN {
        k = "theorem|lemma|def|abbrev|instance|example|structure|class"
        k = k "|inductive|axiom|opaque|alias|noncomputable|private|protected"
        k = k "|partial|unsafe|nonrec|public|meta|scoped|local|namespace|end"
        k = k "|section|open|export|variable|universe|set_option|attribute"
        k = k "|mutual|import|module|deriving|initialize|macro|macro_rules"
        k = k "|syntax|notation|infix|infixl|infixr|prefix|postfix|elab|omit"
        k = k "|include"
        start = "^(@\\[|/--|/-!|#[a-z]|(" k ")([^[:alnum:]_.]|$))"
    }
    $0 ~ start {
        line = $0
        sub(/\/--.*-\//, "", line)
        sub(/\/--.*/, "", line)
        inside = line ~ /(^|[[:space:]]|\])example([[:space:]:({[]|$)/
    }
    { code = $0; sub(/--.*/, "", code) }
    inside && code ~ /native_decide|[+]native|(^|[^[:alnum:]_.])native[[:space:]]*:=/ {
        print FILENAME ":" FNR ": " $0; found = 1
    }
    END { exit found }' {} + >&2; then
    echo "Error: an example uses a compiler-evaluated decision, which the audit never sees." >&2
    exit 1
fi

# The build's warning is the one place a `sorry` in an example shows. Lake
# replays the saved warnings of up-to-date modules, so every build reports
# each one.
BUILD_LOG="$(mktemp)"
trap 'rm -f -- "$BUILD_LOG"' EXIT
lake build 2>&1 | tee "$BUILD_LOG"
if grep -F 'declaration uses ' "$BUILD_LOG" >&2; then
    echo "Error: the build reports a declaration that uses sorry." >&2
    exit 1
fi
lake exe audit --check

STAMP="$LEAN_DIR/scripts/selftest.stamp"
if [[ ! -f "$STAMP" ]]; then
    echo "Error: no audit self-test stamp; run scripts/audit_selftest.sh." >&2
    exit 1
fi

EXPECTED_DIGEST="$(<"$STAMP")"
ACTUAL_DIGEST="$("$LEAN_DIR/scripts/selftest_digest.sh")"
if [[ "$ACTUAL_DIGEST" != "$EXPECTED_DIGEST" ]]; then
    echo "Error: audit self-test stamp is stale; run scripts/audit_selftest.sh." >&2
    exit 1
fi

echo "Lean gate passed."
