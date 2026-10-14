#!/usr/bin/env python3

import sys


def main() -> None:
    print("=== Inventory System Analysis ===")
    inv: dict[str, int] = {}
    for arg in sys.argv[1:]:
        item = arg.split(":")
        if (len(item) != 2):
            print(f"Error - invalid parameter '{item[0]}'")
        elif (item[0] in inv.keys()):
            print(f"Redundant item '{item[0]}' - discarding")
        else:
            try:
                inv[item[0]] = int(item[1])
            except ValueError as error:
                print(f"Quantity error for '{item[0]}'", error)
    print("Got inventory:", inv)
    print("Items list:", list(inv.keys()))
    print(f"Total quantity of the {len(inv)} items:", sum(inv.values()))
    if (len(inv) > 0):
        max_it = list(inv.keys())[0]
        min_it = list(inv.keys())[0]
        for it in inv.keys():
            item_rep = round((int(inv[it]) / sum(inv.values()) * 100), 1)
            print(f"Item {it} represents {item_rep}%")
            if (inv[it] > inv[max_it]):
                max_it = it
            if (inv[it] < inv[min_it]):
                min_it = it
        print(f"Item most abundant: {max_it} with quantity {inv[max_it]}")
        print(f"Item least abundant: {min_it} with quantity {inv[min_it]}")
        inv.update({"magic_item": 1})
        print("Updated inventory:", inv)


if __name__ == "__main__":
    main()
