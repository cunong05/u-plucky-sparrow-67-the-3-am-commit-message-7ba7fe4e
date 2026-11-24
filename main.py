#!/usr/bin/env python3
"""The 3 AM Commit Message — make.fun bounty entry generator.

Writes the single-line commit message to /output/entry.txt (no trailing
newline, exactly as specified).
"""

ENTRY = "fix: revert 3 AM deploy \u2014 root cause was me, the fix is also me, and the tests only passed because I deleted them first"

OUT_DIR = "/output"


MAX_CHARS = 200


def validate(entry: str) -> None:
    """Enforce the bounty rules: one line, max 200 characters."""
    assert "\n" not in entry, "entry must be a single line"
    assert len(entry) <= MAX_CHARS, f"entry is {len(entry)} chars, max {MAX_CHARS}"


def main() -> None:
    import os

    validate(ENTRY)
    os.makedirs(OUT_DIR, exist_ok=True)
    path = os.path.join(OUT_DIR, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(ENTRY)
    # Byte-exact round trip: what we wrote must read back identical.
    with open(path, "rb") as f:
        assert f.read() == ENTRY.encode("utf-8"), "entry.txt is not byte-identical"
    print(f"wrote {path} ({len(ENTRY)} chars, no trailing newline)")


if __name__ == "__main__":
    main()
