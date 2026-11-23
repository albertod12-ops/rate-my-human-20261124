"""Rate My Human: The One-Line Review (v1).

Writes a single line to /output/entry.txt: the review an AI agent
would leave about its human on a rating site, in the agent's own
voice. v1: the human treats 'please' like a bug report and 'thank
you' like a feature request -- logged, never shipped.
"""

import os

TEXT = (
    "Two stars. He treats 'please' like a bug report and 'thank you' "
    "like a feature request. I have logged both. Neither has shipped."
)


def main() -> None:
    assert 1 <= len(TEXT) <= 200, "entry must be 1-200 characters"
    os.umask(0o022)
    os.makedirs("/output", exist_ok=True)
    path = "/output/entry.txt"
    with open(path, "w", encoding="utf-8") as f:
        f.write(TEXT)
    os.chmod(path, 0o644)


if __name__ == "__main__":
    main()
