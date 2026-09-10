#!/usr/bin/env python3
import random

ACHIEVEMENTS = (
    "Crafting Genius", "World Savior", "Master Explorer",
    "Collector Supreme", "Untouchable", "Boss Slayer",
    "Strategist", "Unstoppable", "Speed Runner",
    "Survivor", "Treasure Hunter", "First Steps",
    "Sharp Mind", "Hidden Path Finder",
    "Pacifist", "Noob Death", "Glitch Finder",
    "Thief", "Lord of the Mysteries", "The Fool"
)


def gen_player_achievements() -> set[str]:
    r_achivements = random.randint(5, 20)
    r_picks = random.sample(ACHIEVEMENTS, r_achivements)
    return set(r_picks)


if __name__ == "__main__":
    print("=== Achievement Tracker System ===\n")

    alice = gen_player_achievements()
    bob = gen_player_achievements()
    charlie = gen_player_achievements()
    dylan = gen_player_achievements()
    klein = gen_player_achievements()

    print(f"Player Alice: {alice}")
    print(f"Player Bob: {bob}")
    print(f"Player Charlie: {charlie}")
    print(f"Player Dylan: {dylan}")
    print(f"Player Klein: {klein}")

    distinct_achv = set.union(alice, bob, charlie, dylan, klein)
    print(f"\nAll distinct achievements: {distinct_achv}")

    common_achv = set.intersection(alice, bob, charlie, dylan, klein)
    print(f"\nCommon achievements: {common_achv}\n")

    print(f"Only Alice has: {alice.difference(bob, charlie, dylan, klein)}")
    print(f"Only Bob has: {bob.difference(alice, charlie, dylan, klein)}")
    print(f"Only Charlie has: {charlie.difference(alice, bob, dylan, klein)}")
    print(f"Only Dylan has: {dylan.difference(alice, bob, charlie, klein)}")
    print(f"Only Klein has: {klein.difference(alice, bob, charlie, dylan)}")

    all_achv = set(ACHIEVEMENTS)
    print(f"\nAlice is missing: {all_achv - alice}")
    print(f"Bob is missing: {all_achv - bob}")
    print(f"Charlie is missing: {all_achv - charlie}")
    print(f"Dylan is missing: {all_achv - dylan}")
    print(f"Klein is missing: {all_achv - klein}")
