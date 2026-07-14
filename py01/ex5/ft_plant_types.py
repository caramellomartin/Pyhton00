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

    def age(self) -> None:
        self._curr_age += 1

    def grow(self, value: float) -> None:
        self._height = round(self._height + value, 1)

class Flower(Plant):
    def __init__(self, name: str, height: float, curr_age: int, color: str) -> None:
        super().__init__(name, height, curr_age)
        self._color: str = color
        self._bloom_plant: bool = False

    def bloom(self) -> None:
        print(f"[asking the {self._name} to bloom]")
        self._bloom_plant = True

    def show(self) -> str:
        base_text = super().show()
        if self._bloom_plant:
            bloom_state = f"{self._name} is blooming beautifully!"
        else:
            bloom_state = f"{self._name} has not bloomed yet"
        return f"{base_text}\n Color: {self._color}\n {bloom_state}"

class Tree(Plant):
    def __init__(self, name: str, height: float, curr_age: int, trunk_diameter: float) -> None:
        super().__init__(name, height, curr_age)
        self._trunk_diameter: float = trunk_diameter

    def produce_shade(self) -> None:
        print(f"[asking the {self._name} to produce shade]")
        print(f"Tree {self._name} now produces a shade of {self._height}cm long and {self._trunk_diameter}cm wide.")

    def show(self) -> str:
        base_text = super().show()
        return f"{base_text}\n Trunk diameter: {self._trunk_diameter}cm"

if __name__ == "__main__":
    rose: Plant = Plant("Rose", 15.0, 10)

    print("=== Garden Security System ===")
    print(f"Plant created: {rose.show()}\n")

    rose.set_height(25.0)
    print(f"Height update: {rose.get_height()}cm")
    rose.set_age(30)
    print(f"Age update: {rose.get_age()} days")
    rose.set_height(-25)
    rose.set_age(-30)

    print(f"\nCurrent state: {rose.show()}")
