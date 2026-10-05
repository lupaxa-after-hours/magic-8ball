"""Command-line interface for lupaxa.magic_8ball."""

from __future__ import annotations

import argparse
import sys

from lupaxa.magic_8ball import __version__, ask
from lupaxa.magic_8ball.exceptions import InvalidQuestionError


def build_parser() -> argparse.ArgumentParser:
    """Return the Magic 8-Ball argument parser."""
    parser = argparse.ArgumentParser(description="Ask the Magic 8-Ball a yes-or-no question.")
    parser.add_argument(
        "--version",
        action="store_true",
        help="Show version information and exit.",
    )
    parser.add_argument("question", nargs="?", help="Yes-or-no question.")
    return parser


def main(argv: list[str] | None = None) -> int:
    """Run the CLI and return a process exit code."""
    parser = build_parser()
    args = parser.parse_args(argv)

    if args.version:
        print(f"magic-8ball {__version__}")
        return 0

    if not args.question:
        parser.error("question is required unless --version is used")

    try:
        print(ask(args.question))
    except InvalidQuestionError as exc:
        print(f"error: {exc}", file=sys.stderr)
        return 2
    return 0
