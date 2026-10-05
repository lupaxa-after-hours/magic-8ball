"""Tests for the magic-8ball CLI."""

from __future__ import annotations

import os
import subprocess
import sys
from pathlib import Path

import pytest

from lupaxa.magic_8ball import __version__
from lupaxa.magic_8ball.cli import main

_SRC = Path(__file__).resolve().parents[1] / "src"


def test_version(capsys: pytest.CaptureFixture[str]) -> None:
    """``--version`` prints the package version and exits 0."""
    assert main(["--version"]) == 0
    assert f"magic-8ball {__version__}" in capsys.readouterr().out


def test_prints_chosen_response(
    monkeypatch: pytest.MonkeyPatch, capsys: pytest.CaptureFixture[str]
) -> None:
    """A question prints one classic response."""
    monkeypatch.setattr(
        "lupaxa.magic_8ball.core.secrets.choice",
        lambda choices: choices[8],
    )
    assert main(["Will it rain tomorrow?"]) == 0
    assert capsys.readouterr().out.strip() == "Yes."


def test_blank_question_exits_2(capsys: pytest.CaptureFixture[str]) -> None:
    """A blank question is an error on stderr and exit 2."""
    assert main(["   "]) == 2
    assert "error:" in capsys.readouterr().err


def test_missing_question() -> None:
    """Omitting the question exits 2."""
    with pytest.raises(SystemExit) as exc:
        main([])
    assert exc.value.code == 2


def test_module_entry_version() -> None:
    """``python -m lupaxa.magic_8ball --version`` prints the version."""
    env = os.environ.copy()
    src = str(_SRC)
    current = env.get("PYTHONPATH")
    env["PYTHONPATH"] = src if not current else src + os.pathsep + current
    proc = subprocess.run(
        [sys.executable, "-m", "lupaxa.magic_8ball", "--version"],
        capture_output=True,
        text=True,
        check=False,
        env=env,
    )
    assert proc.returncode == 0, proc.stderr
    assert __version__ in proc.stdout
