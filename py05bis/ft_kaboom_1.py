#!/usr/bin/env python3
from alchemy.grimoire.dark_spellbook import dark_spell_record


def main() -> None:
    print("=== Kaboom 1 ===")
    print("Access to alchemy/grimoire/dark_spellbook.py directly\n")
    print(
        f"Testing record DARK spell: "
        f"{dark_spell_record('Nightmare', 'Bats and frogs')}"
    )


if __name__ == "__main__":
    main()
