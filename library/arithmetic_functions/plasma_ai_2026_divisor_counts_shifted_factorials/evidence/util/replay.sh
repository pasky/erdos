#!/usr/bin/env bash
# Rebuild Plasma AI's Problem 420 formalization at its own pinned toolchain, check its two
# theorems with Comparator, and replay them in the Lean kernel from an empty environment: the
# procedure the receipt in ../verify/ records.
#
# usage: replay.sh WORKDIR [fetch|check]
#   WORKDIR  a scratch folder outside the repository. It receives the extracted tree and its build,
#            Comparator and lean4export:
#            several GB beside the Mathlib cache, which lake keeps in its own cache folder.
#   fetch    the steps that need the network. Extract ../assets/erdos_420_formalization.tar.gz
#            into a fresh folder. This held archive is the exact external source input.
#            Fetch the toolchain, Mathlib and its cache; fetch
#            Comparator and lean4export at the toolchain's tag, with their
#            dependencies.
#   check    the offline steps, under sandbox-exec with ./build.sb on macOS: no network, and writes
#            only to WORKDIR, the temporary folders and lake's and elan's caches. Build Comparator
#            and lean4export; run Comparator with the tree's comparator.json before anything else
#            builds Solution, as Comparator requires; build all default targets, including vendored
#            libraries; run the Conjectures.io card's Replay.lean on
#            each theorem; print their axioms. Comparator's sandbox, landrun, runs only on Linux;
#            elsewhere its own scripts/fake-landrun.sh stands in, and the run relies on build.sb.
#   With neither, fetch and then check.
#   Optional ERDOS420_PACKAGE_CACHE seeds clean, pinned Mathlib dependency checkouts.
#   Optional ERDOS420_VENDOR_CACHE names a built copy with byte-identical vendor sources
#   and build configuration. Only vendor namespace artifacts are reused; the project
#   modules and both targets are always rebuilt in the fresh extraction. Without this
#   option all vendored sources are rebuilt. Full kernel replay is required either way.
# needs: bash, tar, gzip, git, python3 and elan, and network access for fetch.
set -euo pipefail
export LEAN_NUM_THREADS=${LEAN_NUM_THREADS:-4}

here=$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)
assets=$here/../assets
repo=$(git -C "$here" rev-parse --show-toplevel)
replay=$repo/library/number_theory/conjectures_io_2026_lean_solutions_erdos_problems/evidence/verify/Replay.lean
# Source: https://github.com/plasma-ai/erdos-420
# The archive contains git archive of external commit
# daa3bba1d72b41c80beaa8bb2114590ac2f76c6a, excluding paper/.
targets=(Erdos420.erdos_420.parts.iii Erdos420.erdos_420.parts.ii)
[ $# -ge 1 ] && [ $# -le 2 ] || {
    echo "usage: replay.sh WORKDIR [fetch|check]" >&2
    exit 2
}
mkdir -p "$1"
work=$(cd "$1" && pwd)
phase=${2:-all}
src=$work/erdos-420
tools=$work/tools
stamp() { date -u +%Y-%m-%dT%H:%M:%SZ; }

fetch() {
    echo "== $(stamp) extract"
    [ ! -e "$src" ] || {
        echo "refusing to replace existing source folder $src" >&2
        exit 2
    }
    mkdir -p "$src"
    tar -xzf "$assets/erdos_420_formalization.tar.gz" -C "$src"

    echo "== $(stamp) toolchain $(cat "$src/lean-toolchain"), Mathlib and its cache"
    # An optional, already downloaded dependency cache avoids copying project build products.
    # Its entries must be clean Git checkouts at the manifest revisions; only Mathlib and
    # its dependencies are eligible. The project and its vendored sources always start fresh.
    if [ -n "${ERDOS420_PACKAGE_CACHE:-}" ]; then
        python3 "$here/seed_packages.py" "$src" "$ERDOS420_PACKAGE_CACHE"
    fi
    (cd "$src" && lake exe cache get)
    if [ -n "${ERDOS420_VENDOR_CACHE:-}" ]; then
        python3 "$here/seed_vendors.py" "$src" "$ERDOS420_VENDOR_CACHE"
    fi

    # Comparator and lean4export at the tag that matches the toolchain
    toolchain=$(cat "$src/lean-toolchain")
    tag=${toolchain#*:}
    echo "== $(stamp) Comparator and lean4export at $tag"
    [ ! -e "$tools" ] || {
        echo "refusing to replace existing tools folder $tools" >&2
        exit 2
    }
    mkdir -p "$tools"
    for name in comparator lean4export; do
        git clone --quiet --depth 1 --branch "$tag" "https://github.com/leanprover/$name.git" "$tools/$name"
        echo "$name $(git -C "$tools/$name" rev-parse HEAD)"
        # loading the workspace fetches its dependencies at their manifest revisions
        (cd "$tools/$name" && lake env true)
    done
}

run() { # run the command, under the build sandbox on macOS
    if [ "$(uname -s)" = Darwin ]; then
        sandbox-exec -f "$here/build.sb" -D WORK="$work" -D HOME="$HOME" "$@"
    else
        "$@"
    fi
}

check() {
    echo "== $(stamp) build Comparator and lean4export"
    for name in comparator lean4export; do
        (cd "$tools/$name" && run lake build)
    done
    landrun=$(command -v landrun || echo "$tools/comparator/scripts/fake-landrun.sh")
    echo "== $(stamp) Comparator, with $landrun"
    (cd "$src" && run env COMPARATOR_LANDRUN="$landrun" \
        COMPARATOR_LEAN4EXPORT="$tools/lean4export/.lake/build/bin/lean4export" \
        lake env "$tools/comparator/.lake/build/bin/comparator" comparator.json)
    echo "== $(stamp) full project and vendored-library build"
    (cd "$src" && run lake build)
    for target in "${targets[@]}"; do
        echo "== $(stamp) kernel replay of $target"
        (cd "$src" && run lake env lean --run "$replay" Solution Challenge "$target")
    done
    {
        echo 'import Solution'
        for target in "${targets[@]}"; do echo "#print axioms $target"; done
    } >"$work/PrintAxioms.lean"
    echo "== axioms"
    (cd "$src" && run lake env lean "$work/PrintAxioms.lean")
    echo "== $(stamp) done"
}

case $phase in
    fetch) fetch ;;
    check) check ;;
    all) fetch && check ;;
    *)
        echo "usage: replay.sh WORKDIR [fetch|check]" >&2
        exit 2
        ;;
esac
