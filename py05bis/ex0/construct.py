#!/usr/bin/env python3
import sys
import os
import site


def main() -> None:
    r_act = sys.prefix
    r_glob = sys.base_prefix
    r_py = sys.executable
    n_venv = os.path.basename(r_act)
    r_pckg = site.getsitepackages()

    if (r_act == r_glob):
        print("LABORATORY STATUS: You are working in the open")
        print(f"\nCurrent Python: {r_py}")
        print("Virtual Environment: None detected")
        print("\nWARNING: You are in the global environment!")
        print("Every reagent you install here leaks into the whole system.")
        print("\nTo seal the laboratory, run:")
        print("python3 -m venv lab_env")
        print("source lab_env/bin/activate # On Unix")
        print("lab_env\\Scripts\\activate # On Windows")
        print("\nThen run this program again.")
    else:
        print("LABORATORY STATUS: The laboratory is sealed")
        print(f"\nCurrent Python: {r_py}")
        print(f"Virtual Environment: {n_venv}")
        print(f"Environment Path: {r_act}")
        print("\nSUCCESS: You are working in an isolated environment!")
        print("Safe to install reagents without affecting the global system.")
        print("\nReagent installation path:")
        print(f"{r_pckg[0]}")


if __name__ == "__main__":
    main()
