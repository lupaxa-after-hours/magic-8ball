"""lupaxa.magic_8ball — classic Magic 8-Ball answers for yes-or-no questions.

``ask(question)`` returns one of the twenty traditional responses.
``Magic8Ball`` is the same call on an instance. A missing or blank
question raises ``InvalidQuestionError``.
"""

from __future__ import annotations

from .core import Magic8Ball, ask
from .exceptions import InvalidQuestionError, Magic8BallError
from .responses import RESPONSES
from .version import __version__, get_version

__all__ = [
    "RESPONSES",
    "InvalidQuestionError",
    "Magic8Ball",
    "Magic8BallError",
    "__version__",
    "ask",
    "get_version",
]
