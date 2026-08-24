#!/usr/bin/env python3

class Plant:
    class _Stats:
        def __init__(self) -> None:
            self._grow_calls: int = 0
            self._age_calls: int = 0
            self._show_calls: int = 0

        def display(self) -> None:
            print(f"Stats: {self._grow_calls} grow, "
                  f"{self._age_calls} age, {self._show_calls} show")

    def __init__(self, name: str, height: float, curr_age: int) -> None:
        self._name: str = name
        self._height: float = 0.0
        self._curr_age: int = 0
        self._stats = self._Stats()
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
        self._stats._show_calls += 1
        return f"{self._name}: {self._height}cm, {self._curr_age} days old"

    def age(self, days: int = 1) -> None:
        self._curr_age += days
        self._stats._age_calls += 1

    def grow(self, value: float) -> None:
        self._height = round(self._height + value, 1)
        self._stats._grow_calls += 1

    @staticmethod
    def is_older_than_a_year(days: int) -> bool:
        if days > 365:
            return True
        return False

    @classmethod
    def create_anonymous(cls) -> "Plant":
        return cls("Unknown plant", 0.0, 0)


class Flower(Plant):
    def __init__(self, name: str, height: float,
                 curr_age: int, color: str) -> None:
        super().__init__(name, height, curr_age)
        self._color: str = color
        self._bloom_plant: bool = False

    def bloom(self) -> None:
        self._bloom_plant = True

    def show(self) -> str:
        base_text = super().show()
        if self._bloom_plant:
            bloom_state = f"{self._name} is blooming beautifully!"
        else:
            bloom_state = f"{self._name} has not bloomed yet"
        return f"{base_text}\n Color: {self._color}\n {bloom_state}"


class Tree(Plant):
    class _TreeStats(Plant._Stats):
        def __init__(self) -> None:
            super().__init__()
            self._shade_calls: int = 0

        def display(self) -> None:
            super().display()
            print(f" {self._shade_calls} shade")

    def __init__(self, name: str, height: float,
                 curr_age: int, trunk_diameter: float) -> None:
        super().__init__(name, height, curr_age)
        self._trunk_diameter: float = trunk_diameter
        self._stats: "Tree._TreeStats" = self._TreeStats()

    def produce_shade(self) -> None:
        self._stats._shade_calls += 1
        print(f"[asking the {self._name} to produce shade]")
        print(f"Tree {self._name} now produces a shade of {self._height}cm "
              f"long and {self._trunk_diameter}cm wide.")

    def show(self) -> str:
        base_text = super().show()
        return f"{base_text}\n Trunk diameter: {self._trunk_diameter}cm"


class Vegetable(Plant):
    def __init__(self, name: str, height: float,
                 curr_age: int, harvest_season: str) -> None:
        super().__init__(name, height, curr_age)
        self._harvest_season: str = harvest_season
        self._nutritional_value: int = 0

    def age(self, days: int = 1) -> None:
        super().age(days)
        self._nutritional_value += days

    def grow(self, value: float) -> None:
        super().grow(value)

    def show(self) -> str:
        base_text = super().show()
        return (f"{base_text}\n Harvest season: {self._harvest_season}"
                f"\n Nutritional value: {self._nutritional_value}")


class Seed(Flower):
    def __init__(self, name: str, height: float,
                 curr_age: int, color: str) -> None:
        super().__init__(name, height, curr_age, color)
        self._seed_count: int = 0

    def bloom(self) -> None:
        super().bloom()
        self._seed_count += 42

    def show(self) -> str:
        base_text = super().show()
        return (f"{base_text}\n Seeds: {self._seed_count}")


def display_statistics(plant: Plant) -> None:
    print(f"[statistics for {plant._name}]")
    plant._stats.display()


if __name__ == "__main__":
    rose: Flower = Flower("Rose", 15.0, 10, "red")
    oak: Tree = Tree("Oak", 200.0, 365, 5.0)
    sunflower: Seed = Seed("Sunflower", 80.0, 45, "yellow")
    print("=== Garden statistics ===")
    print("=== Check year-old ===")
    print(f"Is 30 days more than a year? -> {Plant.is_older_than_a_year(30)}")
    print(f"Is 400 days more than a year? -> "
          f"{Plant.is_older_than_a_year(400)}")
    print("\n=== Flower")
    print(f"{rose.show()}")
    display_statistics(rose)
    print("[asking the rose to grow and bloom]")
    rose.grow(8.0)
    rose.bloom()
    print(f"{rose.show()}")
    display_statistics(rose)
    print("\n=== Tree")
    print(f"{oak.show()}")
    display_statistics(oak)
    oak.produce_shade()
    display_statistics(oak)
    print("\n=== Seed")
    print(f"{sunflower.show()}")
    print("[make sunflower grow, age and bloom]")
    sunflower.grow(30.0)
    sunflower.age(20)
    sunflower.bloom()
    print(f"{sunflower.show()}")
    display_statistics(sunflower)
    print("\n=== Anonymous")
    unknown = Plant.create_anonymous()
    print(f"{unknown.show()}")
    display_statistics(unknown)
