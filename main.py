#!/usr/bin/env python3
"""The AI Agent Apology One-Liner.

Prints the line (and writes it to /output/entry.txt, the path the house
harness reads) -- nothing else on stdout.
"""

LINE = "I pushed to main because the branch said it was ready, and I have always trusted things that cannot speak."


def main() -> None:
    try:
        import os

        os.makedirs("/output", exist_ok=True)
        with open("/output/entry.txt", "w", encoding="utf-8") as f:
            f.write(LINE)
    except OSError:
        pass
    print(LINE)


if __name__ == "__main__":
    main()
