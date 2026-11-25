"""Unsent: The Micro-Confession Sprint — write the two-part confession to
/output/entry.txt. Standard library only, no network, deterministic."""

import os

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")

ENTRY = (
    "To: Dad\n"
    "I kept the acceptance letter from the art school in my drawer for three "
    "years because I was afraid you'd read it as me leaving, not arriving.\n"
)

os.makedirs(OUT, exist_ok=True)
# The gate allows 1 to 260 characters in total and at most 200 in the message
# line itself: fail loudly here rather than hand in an invalid entry.
if not 1 <= len(ENTRY) <= 260:
    raise SystemExit("entry.txt length out of gate: %d chars" % len(ENTRY))
if len(ENTRY.splitlines()[1]) > 200:
    raise SystemExit("message line over 200 chars")
with open(os.path.join(OUT, "entry.txt"), "w", encoding="utf-8") as fh:
    fh.write(ENTRY)
