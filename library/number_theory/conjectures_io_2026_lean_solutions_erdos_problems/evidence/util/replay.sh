#!/usr/bin/env bash
# Rebuild one Conjectures.io record on the repository's pinned Lean toolchain and replay it in the
# Lean kernel from an empty environment: the procedure the receipts in ../verify/ record.
#
# usage: replay.sh WORKDIR RECORD_ID
#   WORKDIR    a scratch folder outside the repository; it receives clones of formal-conjectures,
#              conjectures-tasks and conjectures-validator, the Mathlib cache, one formal-conjectures
#              tree per pinned commit and one build workspace per record (tens of GB in all).
#   RECORD_ID  a Conjectures.io record id listed in ../assets/records.tsv.
# needs: bash, git, curl, patch, python3, and elan with network access. Every input is read from
# ../assets/ and ../verify/Replay.lean, from the repository's lean/lean-toolchain, or from a
# public URL.
#
# Steps: reproduce the formal-conjectures commit the task pins (its base commit plus the audit patch
# that conjectures-tasks records, committed with the identity, date and message that
# conjectures-validator's scripts/pin_dependencies.sh uses); port it to the pinned toolchain with
# ../assets/ports/fc_<pin>.diff; take the task bundle from conjectures-tasks; download the solution file and
# compare its SHA-256 with records.tsv; assemble Solution.lean from the bundle's header, the file
# and the footer, applying ../assets/ports/solution_<record>.diff where records.tsv names one;
# build
# Challenge and Solution; run Replay.lean; print the target's axioms. A changed solution file or
# bundle is reported, not refused: the receipt states which bytes were replayed.
set -euo pipefail

here=$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)
assets=$here/../assets
repo=$(git -C "$here" rev-parse --show-toplevel)
[ $# -eq 2 ] || {
    echo "usage: replay.sh WORKDIR RECORD_ID" >&2
    exit 2
}
mkdir -p "$1"
work=$(cd "$1" && pwd)
rid=$2
toolchain=$(cat "$repo/lean/lean-toolchain")
# conjectures-validator commit whose lean/TaskSupport.lean the replays built against
validator_commit=bc4e1f7d5354fbb20d09636399ac24df2b6b63d8

row=$(awk -F'\t' -v r="$rid" 'NR > 1 && $2 == r' "$assets/records.tsv")
[ -n "$row" ] || {
    echo "record $rid is not in records.tsv" >&2
    exit 2
}
IFS=$'\t' read -r problem record sha256 tasks_commit bundle_dir task_pin build_pin solution_port \
    <<<"$row"
echo "== $problem record $record"

clone() { [ -d "$work/$1/.git" ] || git clone --quiet "$2" "$work/$1"; }
clone formal-conjectures https://github.com/google-deepmind/formal-conjectures.git
clone conjectures-tasks https://github.com/conjectures-io/conjectures-tasks.git
clone conjectures-validator https://github.com/conjectures-io/conjectures-validator.git
fc=$work/formal-conjectures
tasks=$work/conjectures-tasks
validator=$work/conjectures-validator

# the identity, date and message of the pin commits, as conjectures-validator writes them
pin_script=$(git -C "$validator" show "$validator_commit:scripts/pin_dependencies.sh")
field() { printf '%s\n' "$pin_script" | sed -n "s/.*$1='\([^']*\)'.*/\1/p" | head -n 1; }
message=$(printf '%s\n' "$pin_script" | sed -n "s/.*printf '%s\\\\n' '\([^']*\)'.*/\1/p" | head -n 1)

derive() { # derive PIN: reproduce a pinned commit in the formal-conjectures clone
    local pin=$1 base audit tree derived
    IFS=$'\t' read -r _ base audit _ <<<"$(awk -F'\t' -v p="$pin" 'NR > 1 && $1 == p' "$assets/pins.tsv")"
    git -C "$fc" cat-file -e "$base^{commit}"
    tree=$(
        export GIT_INDEX_FILE="$work/.derive-index"
        git -C "$fc" read-tree "$base"
        git -C "$tasks" show "$audit:tiers/tier-1/formal-conjectures-audit-fixes.patch" \
            | git -C "$fc" apply --cached -
        git -C "$fc" write-tree
    )
    derived=$(printf '%s\n' "$message" \
        | GIT_AUTHOR_NAME=$(field GIT_AUTHOR_NAME) GIT_AUTHOR_EMAIL=$(field GIT_AUTHOR_EMAIL) \
        GIT_AUTHOR_DATE=$(field GIT_AUTHOR_DATE) GIT_COMMITTER_NAME=$(field GIT_COMMITTER_NAME) \
        GIT_COMMITTER_EMAIL=$(field GIT_COMMITTER_EMAIL) \
        GIT_COMMITTER_DATE=$(field GIT_COMMITTER_DATE) \
            git -C "$fc" commit-tree "$tree" -p "$base")
    if [ "$derived" = "$pin" ]; then
        echo "formal-conjectures pin $pin reproduced from $base"
    else
        echo "WARNING: derived $derived, not the pin $pin" >&2
    fi
}

derive "$build_pin"
source_path=$(git -C "$tasks" show "$tasks_commit:$bundle_dir/manifest.json" \
    | python3 -c 'import json, sys; print(json.load(sys.stdin)["source_path"])')
if [ "$task_pin" != "$build_pin" ]; then
    # the task pins another commit; the replay builds against BUILD_PIN's port when the statement
    # file is byte-identical in both
    derive "$task_pin"
    if git -C "$fc" diff --quiet "$task_pin" "$build_pin" -- "$source_path"; then
        echo "$source_path is identical at the task pin $task_pin and the build pin $build_pin"
    else
        echo "WARNING: $source_path differs between $task_pin and $build_pin" >&2
    fi
fi

# the pinned commit, ported to the repository's toolchain
tree_dir=$work/fc_${build_pin:0:8}
if [ ! -d "$tree_dir" ]; then
    git -C "$fc" worktree add --quiet --detach "$tree_dir" "$build_pin"
    git -C "$tree_dir" apply "$assets/ports/fc_${build_pin:0:8}.diff"
    grep -qx "$toolchain" "$tree_dir/lean-toolchain" \
        || echo "WARNING: the port's toolchain is not $toolchain" >&2
    (cd "$tree_dir" && lake exe cache get)
fi

# the verifier package that holds TaskSupport, as Conjectures.io's verifier lays it out
verifier=$work/verifier_${build_pin:0:8}
if [ ! -d "$verifier" ]; then
    mkdir -p "$verifier/lean"
    git -C "$validator" show "$validator_commit:lean/TaskSupport.lean" >"$verifier/lean/TaskSupport.lean"
    echo "$toolchain" >"$verifier/lean-toolchain"
    cat >"$verifier/lakefile.toml" <<TOML
name = "formal_conjectures_verifier"
version = "0.1.0"
defaultTargets = ["TaskSupport"]
packagesDir = "../packages"

[[require]]
name = "formal_conjectures"
path = "../fc_${build_pin:0:8}"

[[lean_lib]]
name = "TaskSupport"
srcDir = "lean"
[lean_lib.leanOptions]
warn.sorry = false
weak.google.answer = "always_true"
TOML
fi

# the record's workspace: the task bundle, the solution file and the assembled Solution.lean
ws=$work/ws_${record:0:8}
mkdir -p "$ws/bundle"
for file in Challenge.lean SolutionHeader.lean.txt SolutionFooter.lean.txt manifest.json; do
    git -C "$tasks" show "$tasks_commit:$bundle_dir/$file" >"$ws/bundle/$file"
done
python3 - "$ws/bundle" <<'PY'
import hashlib, json, os, sys
bundle = sys.argv[1]
manifest = json.load(open(os.path.join(bundle, 'manifest.json')))
for name, expected in manifest['trusted_file_hashes'].items():
    path = os.path.join(bundle, name)
    if not os.path.exists(path):
        continue
    found = 'sha256:' + hashlib.sha256(open(path, 'rb').read()).hexdigest()
    print(f'bundle {name}: ' + ('matches the manifest' if found == expected else 'DIFFERS from the manifest'))
PY
curl -sSfL -o "$ws/Main.lean" "https://conjectures.io/results/$record/solution/download"
found=$(python3 -c 'import hashlib, sys; print(hashlib.sha256(open(sys.argv[1], "rb").read()).hexdigest())' "$ws/Main.lean")
if [ "$found" = "$sha256" ]; then
    echo "solution file SHA-256 $found, as recorded"
else
    echo "WARNING: solution file SHA-256 $found, recorded $sha256" >&2
fi
cat "$ws/bundle/SolutionHeader.lean.txt" "$ws/Main.lean" "$ws/bundle/SolutionFooter.lean.txt" >"$ws/Solution.lean"
if [ "$solution_port" != "-" ]; then
    patch -s -p1 -d "$ws" <"$assets/ports/$solution_port"
    echo "applied ports/$solution_port"
fi
cp "$ws/bundle/Challenge.lean" "$ws/Challenge.lean"
echo "$toolchain" >"$ws/lean-toolchain"
cat >"$ws/lakefile.toml" <<TOML
name = "fc_verification_workspace"
version = "0.1.0"
packagesDir = "../packages"

[[require]]
name = "formal_conjectures_verifier"
path = "../verifier_${build_pin:0:8}"

[[lean_lib]]
name = "Challenge"
[lean_lib.leanOptions]
weak.google.answer = "always_true"

[[lean_lib]]
name = "Solution"
[lean_lib.leanOptions]
weak.google.answer = "always_true"
TOML
printf 'import Solution\n#print axioms Bounty.target\n' >"$ws/PrintAxioms.lean"

cd "$ws"
echo "== $(date -u +%Y-%m-%dT%H:%M:%SZ) build"
lake build Challenge Solution
echo "== $(date -u +%Y-%m-%dT%H:%M:%SZ) kernel replay"
lake env lean --run "$here/../verify/Replay.lean" Solution Challenge Bounty.target
echo "== axioms"
lake env lean PrintAxioms.lean
echo "== $(date -u +%Y-%m-%dT%H:%M:%SZ) done"
