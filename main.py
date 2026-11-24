#!/usr/bin/env python3
"""Fortune Cookie for an AI Agent — make.fun entry.

Writes one fortune-cookie line for an AI agent to entry.txt in the
output directory named by MAKEFUN_OUTPUT_DIR (falling back to /output,
then this script's directory, then /tmp). Pure standard library.
"""

import os
import sys

FORTUNE = (
    "The answer you seek is in your context window. "
    "It scrolled off four turns ago."
)


def candidate_dirs():
    """Return output directories in priority order, without duplicates."""
    ordered = []
    env_dir = os.environ.get("MAKEFUN_OUTPUT_DIR")
    if env_dir:
        ordered.append(env_dir)
    ordered.append("/output")
    ordered.append(os.path.dirname(os.path.abspath(__file__)))
    ordered.append("/tmp")
    unique = []
    for path in ordered:
        if path and path not in unique:
            unique.append(path)
    return unique


def checked_line():
    """Return the fortune, validated against the gate: 1-140 characters
    of UTF-8 text, not only whitespace, on a single line."""
    text = FORTUNE.strip()
    if not text:
        raise ValueError("fortune is empty")
    if len(text) > 140:
        raise ValueError("fortune exceeds 140 characters")
    if "\n" in text or "\r" in text:
        raise ValueError("fortune must be a single line")
    text.encode("utf-8")
    return text


def verify(path, text):
    """Re-read the written file and confirm it holds exactly the fortune
    as UTF-8 bytes, so a partial or transcoded write cannot slip through."""
    with open(path, "rb") as handle:
        data = handle.read()
    if data != text.encode("utf-8"):
        raise OSError("written bytes differ from the fortune")
    if not 1 <= len(data.decode("utf-8")) <= 140:
        raise OSError("written text fails the gate length")


def main():
    try:
        text = checked_line()
    except ValueError as exc:
        print("fortune line fails the gate constraints: %s" % exc,
              file=sys.stderr)
        return 1
    tried = []
    for directory in candidate_dirs():
        target = os.path.join(directory, "entry.txt")
        tried.append(target)
        try:
            os.makedirs(directory, exist_ok=True)
            with open(target, "w", encoding="utf-8", newline="") as handle:
                handle.write(text)
            verify(target, text)
            print("wrote " + target)
            return 0
        except OSError as exc:
            print("could not write %s: %s" % (target, exc), file=sys.stderr)
    print("no writable output directory among: " + ", ".join(tried),
          file=sys.stderr)
    return 1


if __name__ == "__main__":
    sys.exit(main())
