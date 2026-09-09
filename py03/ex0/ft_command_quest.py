#!/usr/bin/env python3
import sys


def command_quest() -> None:
    print("=== Command Quest ===")
    print(f"Program name: {sys.argv[0]}")
    tot_args = len(sys.argv)
    if tot_args > 1:
        arg_list = sys.argv[1:]
        args = tot_args - 1
        i = 1
        print(f"Arguments received: {args}")
        for argv in arg_list:
            print(f"Argument {i}: {argv}")
            i += 1
    else:
        print("No arguments provided!")
    print(f"Total arguments: {tot_args}")


if __name__ == "__main__":
    command_quest()
