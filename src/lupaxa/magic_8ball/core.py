"""Ask the Magic 8-Ball a yes-or-no question."""

from __future__ import annotations

import secrets

from lupaxa.magic_8ball.exceptions import InvalidQuestionError
from lupaxa.magic_8ball.responses import RESPONSES


def ask(question: str) -> str:
    """Return one classic Magic 8-Ball response for a non-empty question.

    The question text is checked, then discarded. The reply is chosen from
    :data:`RESPONSES`.
    """
    if not isinstance(question, str) or not question.strip():
        raise InvalidQuestionError("Question must be a non-empty string.")
    return secrets.choice(RESPONSES)


class Magic8Ball:
    """Classic Magic 8-Ball emulator."""

    def ask(self, question: str) -> str:
        """Return one classic response for ``question``."""
        return ask(question)

    def __str__(self) -> str:
        """Return a short description of this emulator."""
        return "Magic 8-Ball Emulator"
