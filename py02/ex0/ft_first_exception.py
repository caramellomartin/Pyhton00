#!/usr/bin/env python3

def input_temperature(temp_str: str) -> int:
    return int(temp_str)


def test_temperature() -> None:
    print("=== Garden Temperature ===")
    temp_ok = "25"
    print(f"\nInput data is '{temp_ok}'")
    try:
        temp = input_temperature(temp_ok)
        print(f"Temperature is now {temp}°C")
    except ValueError as e:
        print(f"Caught input_temperature error: {e}")
    temp_ko = "abc"
    print(f"\nInput data is '{temp_ko}'")
    try:
        temp = input_temperature(temp_ko)
        print(f"Temperature is now {temp}°C")
    except ValueError as e:
        print(f"Caught input_temperature error: {e}")
    print("\nAll tests completed - program didn't crash!")


if __name__ == "__main__":
    test_temperature()
