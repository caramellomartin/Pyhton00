#!/usr/bin/env python3

class GardenError(Exception):
    def __init__(self, message: str = "Unknown garden error") -> None:
        super().__init__(message)


class PlantError(GardenError):
    def __init__(self, message: str = "The tomato plant is wilting!") -> None:
        super().__init__(message)


class WaterError(GardenError):
    def __init__(self, message: str = "Not enough water in the tank!") -> None:
        super().__init__(message)


def test_custom_errors() -> None:
    print("=== Custom Garden Errors Demo ===")
    print("\nTesting PlantError...")
    try:
        raise PlantError()
    except PlantError as e:
        print(f"Caught PlantError: {e}")
    print("\nTesting WaterError...")
    try:
        raise WaterError()
    except WaterError as e:
        print(f"Caught WaterError: {e}")
    print("\nTesting catching all garden errors...")
    try:
        raise PlantError()
    except GardenError as e:
        print(f"Caught GardenError: {e}")
    try:
        raise WaterError()
    except GardenError as e:
        print(f"Caught GardenError: {e}")
    print("\nAll custom error types work correctly")


if __name__ == "__main__":
    test_custom_errors()
