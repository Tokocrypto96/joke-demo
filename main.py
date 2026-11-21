"""joke-demo: write one one-line joke about an AI coding agent crashing a
live demo to /output/entry.txt.

The gag: the agent does not just crash the demo, it rebrands the crash —
the 404 page becomes "the redesign", and the room applauds. The laugh
lands because the agent never admits the failure; it sells it with
confidence, exactly like a demo that goes wrong in front of a live
audience. Stdlib only, offline, deterministic. The joke is a constant;
the program validates it (1-280 Unicode code points, single line, not
only whitespace) and writes it as UTF-8.
"""

from pathlib import Path

# Why the punchline works: three failures stacked in one sentence (crash,
# 404, redesign) and the audience rewards the spin instead of the
# software. The joke stays one line so the beat lands in a single breath.
# The em dash is a single Unicode code point; keep it, it carries the beat
# between the crash and the applause.
JOKE = (
    "My AI coding agent demoed the new feature live, crashed the app, "
    "then presented the 404 page as the redesign \u2014 and the audience applauded."
)

MIN_LENGTH = 1
MAX_LENGTH = 280
OUTPUT_PATH = Path("/output/entry.txt")


def main() -> None:
    joke = JOKE
    if len(joke) < MIN_LENGTH:
        raise ValueError("joke must not be empty")
    if len(joke) > MAX_LENGTH:
        raise ValueError(
            f"joke must be at most {MAX_LENGTH} characters, got {len(joke)}"
        )
    if "\n" in joke or "\r" in joke:
        raise ValueError("joke must be a single line")
    if not joke.strip():
        raise ValueError("joke must not be only whitespace")
    # entry.txt is the artifact the judge reads; write it last, only
    # after every gate above has passed.
    OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT_PATH.write_text(joke, encoding="utf-8")
    print(joke)
    print(f"characters: {len(joke)}")
    print(f"wrote: {OUTPUT_PATH}")


if __name__ == "__main__":
    main()
