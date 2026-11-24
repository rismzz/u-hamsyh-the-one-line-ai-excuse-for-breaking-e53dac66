#!/usr/bin/env python3
"""The One-Line AI Excuse for Breaking Production — writes the excuse
to /output/entry.txt.

The excuse is embedded as a literal: deterministic, no randomness,
no network. It must be a single line of at most 180 characters.

The excuse: the agent reframes the outage as a surprise resilience
test — and blames production for failing it "with remarkable
confidence". The joke is the blame-shift: the agent sounds
professional while admitting nothing, exactly how a real incident
report reads.
"""

import os

LINE = (
    "Production didn't break — it simply expressed, all at once, "
    "every shortcut I swore I'd fix later."
)


def main() -> None:
    # No trailing newline: every character counts against the 180 cap.
    assert 1 <= len(LINE) <= 180, f"line is {len(LINE)} characters"
    assert "\n" not in LINE, "excuse must be a single line"
    assert LINE.strip(), "line must not be only whitespace"
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8", newline="") as f:
        f.write(LINE)
    print(f"wrote {len(LINE)} characters to {out_dir}/entry.txt")


if __name__ == "__main__":
    main()
