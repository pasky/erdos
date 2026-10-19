"""Operating wrapper: report the execution environment, then run unchanged input."""

import importlib.metadata
import json
from pathlib import Path
import runpy
import sys
import typing

import tools


target = Path(sys.argv[1]).resolve()
runtime = target.parent.parent / "runtime"
expected_tools = runtime / "tools" / "__init__.py"
environment = {
    "sys_prefix": sys.prefix,
    "tools_file": tools.__file__,
    "typing_file": typing.__file__,
    "python_flint_version": importlib.metadata.version("python-flint"),
    "python_version": sys.version,
    "safe_path": sys.flags.safe_path,
}
print("EXECUTION_ENVIRONMENT " + json.dumps(environment, sort_keys=True), flush=True)
if Path(tools.__file__).resolve() != expected_tools.resolve():
    raise RuntimeError("tools import is not the commissioned frozen runtime")
if Path(sys.prefix).resolve() != (Path.cwd() / ".venv").resolve():
    raise RuntimeError("execution environment is not the child-local .venv")
sys.argv = [str(target)]
runpy.run_path(str(target), run_name="__main__")
