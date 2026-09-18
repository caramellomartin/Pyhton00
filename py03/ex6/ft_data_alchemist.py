#!/usr/bin/env python3
import random


def main() -> None:
    print("=== Game Data Alchemist ===\n")

    players = ["Alice", "bob", "Charlie", "dylan",
               "Emma", "Gregory", "john", "kevin", "Liam"
               ]
    print(f"Initial list of players: {players}")

    capitalized = [name.capitalize() for name in players]
    print(f"New list with all names capitalized: {capitalized}")

    orig_capitalized = [name for name in players if name[0].isupper()]
    print(f"New list of capitalized names only: {orig_capitalized}")

    scores = {name: random.randint(1, 1000) for name in capitalized}
    print(f"\nScore dict: {scores}")

    avg_score = sum(scores.values()) / len(scores)
    print(f"Score average is {avg_score:.2f}")

    high_scores = {
        name: score for name, score in scores.items() if score > avg_score
    }
    print(f"High scores: {high_scores}")


if __name__ == "__main__":
    main()
