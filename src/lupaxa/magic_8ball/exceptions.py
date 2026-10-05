"""Custom exceptions for the magic_8ball package."""

from __future__ import annotations


class Magic8BallError(Exception):
    """Base error for the magic_8ball package."""


class InvalidQuestionError(Magic8BallError):
    """Raised when the question is empty or not a string."""
