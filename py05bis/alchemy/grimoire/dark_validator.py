#!/usr/bin/env python3
from .dark_spellbook import dark_spell_allowed_ingredients


def validate_ingredients(ingredients: str) -> str:
    allowed: list[str] = dark_spell_allowed_ingredients()
    ing_lower = ingredients.lower()

    is_valid = any(item in ing_lower for item in allowed)
    status = "VALID" if is_valid else "INVALID"

    return (
        f"{ingredients} - {status}"
    )
