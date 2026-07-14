#!/usr/bin/env python3

class Plant:
    def __init__(self, name: str, height: float, curr_age: int) -> None:
        self.name: str = name
        self.height: float = height
        self.curr_age: int = curr_age
    def show(self) -> str:
        return f"{self.name}: {self.height}cm, {self.curr_age} days old"

if __name__ == "__main__":
    rose: Plant = Plant("Rose", 25.0, 30)
    oak: Plant = Plant("Oak", 200.0, 365)
    cactus: Plant = Plant("Cactus", 5.0, 90)
    sunflower: Plant = Plant("Sunflower", 80.0, 45)
    fern: Plant = Plant("Fern", 15.0, 120)

    print("=== Plant Factory Output ===")
    print(f"Created: {rose.show()}")
    print(f"Created: {oak.show()}")
    print(f"Created: {cactus.show()}")
    print(f"Created: {sunflower.show()}")
    print(f"Created: {fern.show()}")
