#!/usr/bin/env python3
"""Post-process the BLOG-POST-LIST block that blog-post-workflow writes.

Two jobs:

1. Drop any post whose URL contains a slug listed in EXCLUDED_POST_SLUGS, then
   keep the first POSTS_SHOWN that survive. The upstream action has no filter
   of its own, so it over-fetches and we trim here.
2. Put the first bullet on its own line. The action glues it onto the START
   marker, which GFM then swallows as part of the HTML comment block.
"""

import os
import pathlib
import sys

START = "<!-- BLOG-POST-LIST:START -->"
END = "<!-- BLOG-POST-LIST:END -->"


def main() -> int:
    readme = pathlib.Path(
        os.environ.get("README_PATH", "README.md")
    )
    text = readme.read_text(encoding="utf-8")

    try:
        head, rest = text.split(START, 1)
        block, tail = rest.split(END, 1)
    except ValueError:
        print(f"::error::{readme} is missing the BLOG-POST-LIST markers", file=sys.stderr)
        return 1

    excluded = [
        slug.strip()
        for slug in os.environ.get("EXCLUDED_POST_SLUGS", "").split(",")
        if slug.strip()
    ]
    shown = int(os.environ.get("POSTS_SHOWN", "4"))

    items = [line.strip() for line in block.splitlines() if line.strip().startswith("- [")]
    kept = [item for item in items if not any(slug in item for slug in excluded)]
    dropped = len(items) - len(kept)
    kept = kept[:shown]

    if not kept:
        print("::warning::every fetched post was excluded; leaving the list empty")

    readme.write_text(
        f"{head}{START}\n" + "".join(f"{item}\n" for item in kept) + f"{END}{tail}",
        encoding="utf-8",
    )
    print(f"kept {len(kept)} post(s), excluded {dropped}, fetched {len(items)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
