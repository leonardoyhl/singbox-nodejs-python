#!/usr/bin/env python
import subprocess
import sys

try:
    subprocess.run(["bash", "start.sh"], check=True, text=True)
except subprocess.CalledProcessError as exc:
    print(f"\033[31mError: Failed with exit code {exc.returncode}\033[0m", file=sys.stderr)
    raise
