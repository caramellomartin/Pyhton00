#!/usr/bin/env python3

class Plant:
    def show(self) -> None:
        print(f"{self.name}: {self.height}cm, {self.curr_age} days old")
    def age(self) -> None:
        self.curr_age += 1
    def grow(self, value: float) -> None:
        self.height = round(self.height + value, 1)

if __name__ == "__main__":
    rose = Plant()
    sunflower = Plant()
    cactus = Plant()

    rose.name = "Rose"
    rose.height = 25.0
    rose.curr_age = 30

    init_height: float = rose.height

    for i in range(0, 8):
        if i == 0:
            print("=== Garden Plant Growth ===")
        elif i != 0:
            print(f"=== Day {i} ===")
        rose.show()
        if (i < 7):
            rose.grow(0.8)
            rose.age()
    print(f"Growth this week: {round(rose.height - init_height, 1)}cm")
