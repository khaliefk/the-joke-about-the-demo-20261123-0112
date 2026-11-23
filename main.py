#!/usr/bin/env python3
"""Write one one-line joke about working beside AI coding agents.

The joke is written to /output/entry.txt (or $OUTPUT_DIR/entry.txt when
set, so it can be tested locally). No network, no dependencies.
"""

import os

JOKE = (
    "My coding agent was so sure the demo would work, it wrote the "
    "post-mortem before the crash."
)


def main() -> None:
    out_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    text = JOKE.strip()
    assert 1 <= len(text) <= 280, f"joke is {len(text)} code points"
    assert "\n" not in text, "joke must be one line"
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(text + "\n")


if __name__ == "__main__":
    main()
