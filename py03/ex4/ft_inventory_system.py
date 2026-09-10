#!/usr/bin/env python3
import sys


def manage_inventory() -> None:
    print("=== Inventory System Analysis ===")
    inventory: dict[str, int] = {}

    for arg in sys.argv[1:]:
        parts_arg = arg.split(":")
        if len(parts_arg) != 2:
            print(f"Error - invalid parameter '{arg}'")
            continue
        item = parts_arg[0]
        qty_str = parts_arg[1]

        if item in inventory:
            print(f"Redundant item '{item}' - discarding")
            continue

        try:
            quantity = int(qty_str)
            inventory[item] = quantity
        except ValueError as e:
            print(f"Quantity error for '{item}': {e}")
    print(f"Got inventory: {inventory}")

    if not inventory:
        return

    print(f"Item list: {list(inventory.keys())}")
    tot_quantity = sum(inventory.values())
    print(f"Total quantity of the {len(inventory)} items: {tot_quantity}")

    most_item = ""
    most_quantity = -1
    least_item = ""
    least_quantity = float('inf')

    for item in inventory:
        item_quantity = inventory[item]
        percentage = (item_quantity * 100) / tot_quantity
        print(f"Item {item} represents {percentage:.1f}%")

        if item_quantity > most_quantity:
            most_quantity = item_quantity
            most_item = item
        if item_quantity < least_quantity:
            least_quantity = item_quantity
            least_item = item

    print(f"Item most abundant: {most_item} with quantity {most_quantity}")
    print(f"Item least abundant: {least_item} with quantity {least_quantity}")

    inventory.update({"magic_item": 1})
    print(f"Updated inventory: {inventory}")


if "__main__" == __name__:
    manage_inventory()
