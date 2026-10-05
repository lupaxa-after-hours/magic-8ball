"""Tests for the Magic 8-Ball library."""

from __future__ import annotations

import pytest

from lupaxa.magic_8ball import (
    RESPONSES,
    InvalidQuestionError,
    Magic8Ball,
    Magic8BallError,
    ask,
)


def test_responses_are_the_classic_twenty() -> None:
    """The answer set is the twenty traditional phrases, each once."""
    assert len(RESPONSES) == 20
    assert len(set(RESPONSES)) == 20
    assert RESPONSES[0] == "It is certain."
    assert RESPONSES[-1] == "Very doubtful."


def test_ask_returns_a_classic_response(monkeypatch: pytest.MonkeyPatch) -> None:
    """``ask`` returns the phrase chosen from the classic set."""
    monkeypatch.setattr(
        "lupaxa.magic_8ball.core.secrets.choice",
        lambda choices: choices[7],
    )
    assert ask("Will it rain tomorrow?") == "Outlook good."


def test_ask_rejects_blank_questions() -> None:
    """Empty and whitespace-only questions are rejected."""
    with pytest.raises(InvalidQuestionError, match="non-empty string"):
        ask("")
    with pytest.raises(InvalidQuestionError):
        ask("   ")


def test_ask_rejects_non_strings() -> None:
    """Non-strings are rejected."""
    with pytest.raises(InvalidQuestionError):
        ask(None)  # type: ignore[arg-type]


def test_invalid_question_error_is_a_package_error() -> None:
    """Callers can catch the package base error."""
    with pytest.raises(Magic8BallError):
        ask("")


def test_instance_ask_matches_function(monkeypatch: pytest.MonkeyPatch) -> None:
    """``Magic8Ball.ask`` uses the same selection as ``ask``."""
    monkeypatch.setattr(
        "lupaxa.magic_8ball.core.secrets.choice",
        lambda choices: choices[3],
    )
    ball = Magic8Ball()
    assert ball.ask("Will I get a promotion?") == "Yes - definitely."
    assert str(ball) == "Magic 8-Ball Emulator"
