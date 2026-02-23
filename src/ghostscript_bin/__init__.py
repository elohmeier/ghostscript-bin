"""Ghostscript (gs) binary distribution."""

from __future__ import annotations

import os
import subprocess
import sys
from pathlib import Path


def gs_path() -> Path:
    """Return the absolute path to the bundled gs binary."""
    return Path(__file__).parent / "bin" / "gs"


def version() -> str:
    """Return the Ghostscript version string."""
    return subprocess.check_output(
        [str(gs_path()), "--version"], text=True
    ).strip()


def run(
    args: list[str], **kwargs: object
) -> subprocess.CompletedProcess[str]:
    """Run gs with the given arguments.

    Accepts the same keyword arguments as subprocess.run.
    """
    return subprocess.run([str(gs_path()), *args], **kwargs)  # noqa: S603


def _main() -> None:
    """Console script entry point — replaces the process with gs."""
    os.execv(str(gs_path()), [str(gs_path()), *sys.argv[1:]])
