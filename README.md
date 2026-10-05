<p align="center">
  <a href="https://github.com/lupaxa-after-hours">
    <img src="https://raw.githubusercontent.com/the-lupaxa-project/brand-assets/master/logos/organisations/after-hours/readme-logo.png" alt="After Hours" />
  </a>
</p>

<h1 align="center">Magic 8 Ball</h1>

Ask a yes-or-no question and get one of the twenty classic Magic 8-Ball
replies. The question is checked, then discarded. The reply is chosen at
random from the traditional set.

The PyPI name is `lupaxa-magic-8ball`. The import path is
`lupaxa.magic_8ball`. The console script is `magic-8ball`. `lupaxa` is a
namespace package — there is no `lupaxa/__init__.py`.

Public names: `ask`, `Magic8Ball`, `RESPONSES`, `Magic8BallError`,
`InvalidQuestionError`, `__version__`, `get_version()`.

## Install

```bash
pip install lupaxa-magic-8ball
```

Requires Python 3.10+. The standard library is enough.

## CLI

```bash
magic-8ball "Will it rain tomorrow?"
magic-8ball --version
```

The question is one positional argument. Quote it so the shell keeps it
together.

| Flag        | Meaning                                          |
| ----------- | ------------------------------------------------ |
| `question`  | Yes-or-no question (required unless `--version`) |
| `--version` | Print `magic-8ball x.y.z` and exit `0`           |
| `--help`    | Show argparse help                               |

| Result                    | Stdout              | Exit |
| ------------------------- | ------------------- | ---- |
| Success                   | One response        | `0`  |
| `--version`               | `magic-8ball x.y.z` | `0`  |
| Missing or blank question | error on stderr     | `2`  |

```bash
python -m lupaxa.magic_8ball "Will it rain tomorrow?"
```

## Library

```python
from lupaxa.magic_8ball import Magic8Ball, ask

ask("Will it rain tomorrow?")

ball = Magic8Ball()
ball.ask("Will it rain tomorrow?")
```

| Call                         | Return                      |
| ---------------------------- | --------------------------- |
| `ask(question)`              | one of the twenty responses |
| `Magic8Ball().ask(question)` | the same                    |
| `str(Magic8Ball())`          | `Magic 8-Ball Emulator`     |

`RESPONSES` is the fixed tuple of twenty phrases, affirmative first,
non-committal in the middle, and negative last.

| Situation                       | Result                 |
| ------------------------------- | ---------------------- |
| Non-empty string                | One classic response   |
| Empty string or only whitespace | `InvalidQuestionError` |
| Value that is not a string      | `InvalidQuestionError` |

```python
from lupaxa.magic_8ball import InvalidQuestionError, ask

try:
    ask("Will I get a promotion?")
except InvalidQuestionError as exc:
    print(f"Error: {exc}")
```

## Development

```bash
make init
make python-install-dev
make python-check
```

<a href="https://github.com/the-lupaxa-project">
    <img src="https://raw.githubusercontent.com/the-lupaxa-project/brand-assets/master/logos/components/footer-for-child-orgs.svg" alt="The Lupaxa Project Footer" width="100%" />
</a>
