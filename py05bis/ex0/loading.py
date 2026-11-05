#!/usr/bin/env python3
import sys


def main() -> None:
    print("REAGENT STATUS: Loading reagents...")
    print("Checking dependencies:")

    missing_deps: bool = False

    try:
        import pandas as pd  # type: ignore
        pandas_version: str = pd.__version__
        print(f"[OK] pandas ({pandas_version}) - Data manipulation ready")
    except ImportError:
        print("[MISSING] pandas - Data manipulation reagent not found")
        missing_deps = True

    try:
        import numpy as np  # type: ignore
        numpy_version: str = np.__version__
        print(f"[OK] numpy ({numpy_version}) - Numerical computation ready")
    except ImportError:
        print("[MISSING] numpy - Numerical computation reagent not found")
        missing_deps = True

    if missing_deps:
        print("\nWARNING: Missing reagents detected!")
        print("\nTo install reagents with pip, run:")
        print("  pip install -r ex0/requirements.txt")
        print("\nTo install reagents with Poetry, run:")
        print("  poetry install")
        print("  poetry run python ex0/loading.py")
        sys.exit(1)

    print("\npip vs Poetry:")
    print(
        "requirements.txt declares what to install; "
        "pip resolves it at install time."
    )
    print(
        "pyproject.toml declares the same constraints, "
        "and Poetry pins the resolved"
    )
    print("versions in poetry.lock so every install is identical.")
    print("\nAll reagents present and accounted for.")


if __name__ == "__main__":
    main()
