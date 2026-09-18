#!/usr/bin/env python3
import sys
from typing import IO


def recover_information(filename: str) -> None:
    print("=== Cyber Archives Recovery & Preservation ===")
    print(f"Accessing file '{filename}'")

    f: IO[str] | None = None
    try:
        f = open(filename, "r")
        content = f.read()
        print(f"---\n\n{content}\n---")
        f.close()
        print(f"File'{filename}' closed.")
    except Exception as e:
        print(
            f"[STDERR] Error opening file '{filename}': {e}",
            file=sys.stderr
        )
        return

    print("\nTransform data:")
    print("---\n")
    lines = content.splitlines()
    trans_lines = [line + "#" for line in lines]
    trans_content = "\n".join(trans_lines) + "\n" if lines else ""
    print(trans_content)
    print("---")

    sys.stdout.write("Enter new file name (or empty): ")
    sys.stdout.flush()
    save_name = sys.stdin.readline().rstrip("\r\n")
    if not save_name:
        print("Not saving data.")
        return

    print(f"Saving data to '{save_name}'")
    try:
        f_out: IO[str] = open(save_name, "w")
        f_out.write(trans_content)
        f_out.close()
        print(f"Data saved in file '{save_name}'")
    except Exception as e:
        print(
            f"[STDERR] Error opening file'{save_name}': {e}",
            file=sys.stderr
        )
        print("Data not saved.")


def main() -> None:
    if len(sys.argv) != 2:
        print(f"Usage: {sys.argv[0]} <file>")
        return
    recover_information(sys.argv[1])


if __name__ == "__main__":
    main()
