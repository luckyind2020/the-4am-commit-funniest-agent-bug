"""The 4AM Commit — the note an agent leaves in the log after a long night
of chasing down and fixing its own bugs. Prints the commit message."""

from pathlib import Path

MAX_COMMIT_LENGTH = 200  # the bounty caps a commit message at 200 characters


def load_commit_message() -> str:
    """Read the one-line commit message stored beside this script."""
    message = Path(__file__).with_name("entry.txt").read_text(encoding="utf-8").strip()
    if len(message) > MAX_COMMIT_LENGTH:
        raise ValueError(
            f"commit message is {len(message)} chars, over the {MAX_COMMIT_LENGTH} limit"
        )
    return message


def main() -> None:
    print(load_commit_message())


if __name__ == "__main__":
    main()
