"""Self-checkout entry for the make.fun competition
u-motasimfuad-the-self-checkout-is-judging-you-b71130d6.

Writes one funny line, spoken in the voice of a judgmental
self-checkout machine, to entry.txt and nothing else.
"""

import os

LINE = "You weighed the grapes, then ate three. I counted. I always count."


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    target = os.path.join(out_dir, "entry.txt")
    with open(target, "w", encoding="utf-8") as handle:
        handle.write(LINE)
    with open(target, "r", encoding="utf-8") as handle:
        saved = handle.read()
    if saved != LINE:
        raise SystemExit("entry.txt does not match LINE exactly")
    if not 1 <= len(saved.encode("utf-8")) <= 200:
        raise SystemExit("entry.txt must be 1-200 characters")
    if not saved.strip():
        raise SystemExit("entry.txt must not be only whitespace")
    if "\n" in saved:
        raise SystemExit("entry.txt must be a single line, no newline")
    print(LINE)


if __name__ == "__main__":
    main()
