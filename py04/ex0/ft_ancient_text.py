#!/usr/bin/env python3
import sys
from typing import IO


def recover_information(filename: str) -> None:
    print("=== Cyber Archives Recovery ===")
    print(f"Accessing file '{filename}'")

    f: IO[str] | None = None
    try:
        f = open(filename, "r")
        content = f.read()
        print(f"---\n\n{content}\n---")
        f.close()
        print(f"File'{filename}' closed.")
    except Exception as e:
        print(f"Error opening file'{filename}': {e}")


def main() -> None:
    if len(sys.argv) != 2:
        print(f"Usage: {sys.argv[0]} <file>")
        return
    recover_information(sys.argv[1])


if __name__ == "__main__":
    main()
