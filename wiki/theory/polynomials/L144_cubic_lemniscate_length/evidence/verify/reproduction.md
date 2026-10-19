---
name: theory/polynomials/L144_cubic_lemniscate_length/evidence/verify/reproduction
desc: Exact retained inputs, portable path substitutions, and both observed outcomes of the cubic grading reruns.
created: 2026-10-15T23:40:25Z
updated: 2026-10-15T23:40:25Z
---

# theory/polynomials/L144_cubic_lemniscate_length/evidence/verify/reproduction

***

These instructions accompany the [grade](grade.md). The mathematical files
under [review/](review/report.md) preserve the settled mathematical delivery;
the source-excerpt locator and editorial filing changes are disclosed in the index. The
[original reproduction account](review/reproduction.md) describes the
reviewer's executions; this account records the grader's two reruns on
2026-10-15 UTC. Neither stored output nor a previous successful exit replaces
a fresh execution.

## Inputs and relocation

The 34-file public bundle under `review/` preserves the computational inputs
and the examination, with a bibliographic locator replacing its source excerpt: the report,
three derivations in one file, reproduction account, independent diagnostic,
exact diagnostic JSON, statement, eight-section proof, evidence description,
full checker, source locator, runtime modules, project specification,
lockfile text, API capture, and identity wrapper. The runtime's `uv.lock.txt`
is preserved in its delivered safe name. Neither it nor the copied project
specification was used to install an environment.

The grader first reconstructed those files in private scratch with their
original relative hierarchy, then preserved identical bytes in the settled grading bundle. The public
filing replaces only the copyrighted source excerpt by its locator and makes
the disclosed path and citation edits.
Every path is mapped in the private reconstruction receipt. The only execution
substitutions were the enclosing directory, explicit interpreter selection,
and the frozen runtime import path. No mathematical source, constant, input,
or assertion was edited. The public reproduction paths include `/review` in `review_dir`; use the
value below when reproducing this package.

The full checker has no separate data file or quick-mode option. It begins
with thirteen small-parameter boxes and 300 larger-parameter seed intervals,
then adaptively encloses the latter. The diagnostic reads twelve exact
Gaussian-rational root cases from
[diagnostic_inputs.json](review/assets/diagnostic_inputs.json), with five
prescribed points per local input box, and the retained boundary/rejection
instances. It imports helper functions from the full checker without calling
its `main()`.

## Environment and bounded execution

Use an already installed repository-local environment. The observed grader
runs used CPython 3.14.6, python-flint 0.9.0, typer 0.27.2, and PyYAML 6.0.3.
The checker sets 64-bit arb precision and one flint thread; the diagnostic
compares 64-bit tested boxes with 128-bit reference calculations, also with
one thread. It is a different root construction, not a different ball library.

Before execution the grader verified `sys.prefix`, `tools.__file__`,
`typing.__file__`, the installed package versions, safe-path mode, and every
loaded `tools` module location. The prefix was the local environment, `tools`
came from the reconstructed permitted runtime, and `typing` came from the
interpreter's standard library. Both mathematical programs also print their
commissioned runtime identities. Inspect those identities on a rerun.

The commands below are the inner mathematical commands used by the recorded
supervisor, with portable path substitutions. The supervisor imposed a
**900-second wall limit** on the full checker and a **60-second wall limit** on
the diagnostic, stopped only its own process group if necessary, and retained
stdout, stderr, return code, and elapsed time. These are enforced execution
limits, not claims that the algorithms have a proven runtime below those
limits on every machine. Both observed runs finished within their limits.
A timeout or missing required enclosure is not a pass. Apply the corresponding
wall limit when using another execution supervisor.

The extra `--no-project`, `--no-config`, `--offline`, and
`--no-python-downloads` flags prevent project discovery, configuration reads,
network resolution, and interpreter acquisition. The already installed
interpreter is explicit. `uv` reported that `--no-sync` is redundant alongside
`--no-project`; no synchronization or installation occurred.

## Full checker

From the repository root after filing the package at its commissioned home:

```sh
review_dir=wiki/theory/polynomials/L144_cubic_lemniscate_length/evidence/verify/review
env -u VIRTUAL_ENV -u UV_PROJECT -u UV_PROJECT_ENVIRONMENT \
  -u UV_WORKING_DIR -u UV_NO_PROJECT \
  PYTHONPATH="$PWD/$review_dir/assets/subject/runtime" \
  PYTHONDONTWRITEBYTECODE=1 OMP_NUM_THREADS=1 OPENBLAS_NUM_THREADS=1 \
  MKL_NUM_THREADS=1 VECLIB_MAXIMUM_THREADS=1 NUMEXPR_NUM_THREADS=1 \
  uv run --no-sync --no-project --no-config --offline --no-python-downloads \
  "$PWD/.venv/bin/python" -P -u \
  "$review_dir/assets/operating/run_frozen_evidence.py" \
  "$review_dir/assets/subject/evidence/main.py"
```

The grader's run exited **0** after **251.65 seconds**, with all **22**
obligations passing. It reproduced 13 small-parameter boxes, 591 accepted
larger-parameter boxes, and respectively 1,930,449 and 2,581,149 regular
integration pieces. Printed enclosures included

$$
L_0=[9.17972422234316\pm2.77\cdot10^{-15}],
$$

largest small-regime integral upper bound
$[-0.216023\pm1.23\cdot10^{-7}]$, and reported smallest large-regime
margin $[0.0114301\pm4.80\cdot10^{-8}]$. The control at $\beta=1/2$
implies the conservative scalar bracket $[8.1746135,8.1829017]$.
The checker must establish its individual accepted-box inequalities and
complete covers; these printed summaries alone do not certify them.

The [original reproduction account](review/reproduction.md) lists concrete
failing inputs for the tiling, graph, far-branch, gamma-consistency, negativity,
regime-join, unresolved-cover, margin, and control predicates. Those interfaces
were inspected; their hypothetical modifications were not executed or applied
to the frozen code.

## Independent finite diagnostic

Using the same `review_dir` and repository root:

```sh
env -u VIRTUAL_ENV -u UV_PROJECT -u UV_PROJECT_ENVIRONMENT \
  -u UV_WORKING_DIR -u UV_NO_PROJECT \
  PYTHONPATH="$PWD/$review_dir/assets/subject/runtime" \
  PYTHONDONTWRITEBYTECODE=1 OMP_NUM_THREADS=1 OPENBLAS_NUM_THREADS=1 \
  MKL_NUM_THREADS=1 VECLIB_MAXIMUM_THREADS=1 NUMEXPR_NUM_THREADS=1 \
  uv run --no-sync --no-project --no-config --offline --no-python-downloads \
  "$PWD/.venv/bin/python" -P -u "$review_dir/independent_check.py"
```

The grader's run exited **1** after **0.324 seconds**. Exactly **44 of 48**
reported predicates passed. All sixty prescribed-root comparisons and the
specified exact/rejection instances behaved as recorded. The same four
predicates failed as in the original review:

- `finite depth cap retains rectangle bounds [2,4]`;
- `negative rectangle bound uses correct width endpoints`;
- `positive rectangle bound uses correct width endpoints`;
- `sign-changing rectangle bound contains both extremes`.

These failures remain part of the retained result. The exact discrepant
endpoints were not printed, so their magnitudes and individual causes were
not measured. The assertions demand exact ideal endpoints, whereas the
required mathematical argument uses enclosing inequalities. The grade gives
these four predicates no successful-calibration weight and explains why the
written signed-rectangle argument supplies the mandatory warrant independently.
Do not repair the code merely to reproduce a successful exit, or report this
leg as a pass.

The exact retained negative cases include a wrong origin-density factor,
indeterminate integrand at depth zero, invalid critical window at $\beta=0$,
unresolved cover $[0,2^{-41}]$, and the singular point $2i$. They test the
specified error paths. The finite root route can expose a Cardano
branch/normalization error on its cases; it cannot certify the whole parameter
family or the ball arithmetic implementation.

## Scope of the record

Exactly two mathematical checks were run in this grading. Administrative
byte comparisons, static code/history parsing, and identity probes are
separate and introduce no further mathematical execution. The unchanged
programs, JSON, source, runtime support, and wrapper above are the inputs
needed for mathematical reproduction. The exact administrative scripts,
bounded supervisor, commands, stdout/stderr, timings, identity receipts, and
primary isolation records are retained privately beside the grade for intake.
They are not needed as cached mathematical data.

The uniform integral certificate relies on the mathematical argument in the
[report](review/report.md) and [derivations](review/derivations.md). The
existence reduction, gamma identity, source interfaces, and equality proof
remain written mathematical obligations and are assessed in the grade.
Reproducing either program alone supplies no grade of those obligations.
