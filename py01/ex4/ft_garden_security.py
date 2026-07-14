#!/usr/bin/env python3

class Plant:
    def __init__(self, name: str, height: float, curr_age: int) -> None:
        self._name: str = name
        self._height: float = 0.0
        self._curr_age: int = 0

        self.set_height(height)
        self.set_age(curr_age)
    def get_height(self) -> float:
        return self._height
    def set_height(self, height: float) -> None:
        if height < 0:
            print(f"\n{self._name}: Error, height can't be negative")
            print("Height update rejected")
        else:
            self._height = height
    def get_age(self) -> int:
        return self._curr_age
    def set_age(self, curr_age: int) -> None:
        if curr_age < 0:
            print(f"{self._name}: Error, age can't be negative")
            print("Age update rejected")
        else:
            self._curr_age = curr_age
    def show(self) -> str:
        return f"{self._name}: {self._height}cm, {self._curr_age} days old"

if __name__ == "__main__":
    rose: Plant = Plant("Rose", 15.0, 10)

    print("=== Garden Security System ===")
    print(f"Plant created: {rose.show()}\n")

    rose.set_height(25)
    print(f"Height update: {rose.get_height()}cm")
    rose.set_age(30)
    print(f"Age update: {rose.get_age()} days")
    rose.set_height(-25)
    rose.set_age(-30)

    print(f"\nCurrent state: {rose.show()}")

