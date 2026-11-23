#!/usr/bin/env python3
"""One-line joke about working beside AI coding agents.

Writes the joke to /output/entry.txt, or $OUTPUT_DIR/entry.txt when
set for local testing. No network, no third-party packages.
"""

import os

JOKE = (
    "My coding agent fixed the demo crash by making it crash faster "
    "and calling it a performance improvement."
)


def main() -> None:
    out_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    joke = JOKE.strip()
    if not 1 <= len(joke) <= 280:
        raise SystemExit(f"joke must be 1-280 characters, got {len(joke)}")
    if "\n" in joke or joke != joke.strip() or not joke.strip():
        raise SystemExit("joke must be a single non-blank line")
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as handle:
        handle.write(joke + "\n")
    print(f"wrote {len(joke)} characters to {path}")


if __name__ == "__main__":
    main()
