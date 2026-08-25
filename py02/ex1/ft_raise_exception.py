#!/usr/bin/env python3

def input_temperature(temp_str: str) -> int:
    temp = int(temp_str)
    if temp > 40:
        raise ValueError(f"{temp}°C is too hot for plants (max 40°C)")
    elif temp < 0:
        raise ValueError(f"{temp}°C is too cold for plants (min 0°C)")
    return temp


def test_temperature() -> None:
    print("=== Garden Temperature Checker===")
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
    temp_hot = "100"
    print(f"\nInput data is '{temp_hot}'")
    try:
        temp = input_temperature(temp_hot)
        print(f"Temperature is now {temp}°C")
    except ValueError as e:
        print(f"Caught input_temperature error: {e}")
    temp_cold = "-50"
    print(f"\nInput data is '{temp_cold}'")
    try:
        temp = input_temperature(temp_cold)
        print(f"Temperature is now {temp}°C")
    except ValueError as e:
        print(f"Caught input_temperature error: {e}")
    print("\nAll tests completed - program didn't crash!")


if __name__ == "__main__":
    test_temperature()
