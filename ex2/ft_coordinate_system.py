#!/usr/bin/env python3

import math


def get_player_pos() -> tuple[float, ...]:
    while (True):
        try:
            coords: list[str] = input("Enter new coordinates as floats "
                                      "in format 'x,y,z': ").split(",")
            idx = 0
            for _ in coords:
                idx += 1
            if (idx != 3):
                raise ValueError("Invalid syntax")
            coords_tup = []
            idx = 0
            while (idx < 3):
                try:
                    coords_tup.append(float(coords[idx]))
                except ValueError as error:
                    raise ValueError(error)
                idx += 1
            return tuple(coords_tup)
        except ValueError as error:
            print(error)


def clc_dst(crds1: tuple[float, ...], crds2: tuple[float, ...]) -> float:
    (x1, y1, z1) = crds1
    (x2, y2, z2) = crds2
    rslt = math.sqrt((x2 - x1)**2 + (y2 - y1)**2 + (z2 - z1)**2)
    return (round(rslt, 4))


if __name__ == "__main__":
    print("=== Game Coordinate System ===\n")
    print("Get a first set of coordinates")
    crds1 = get_player_pos()
    print("Got a first tuple:", crds1)
    print(f"It includes: X={crds1[0]}, Y={crds1[1]}, Z={crds1[2]}")
    print("Distance to center:", clc_dst(crds1, (0, 0, 0)))

    print("\nGet a second set of coordinates")
    crds2 = get_player_pos()
    print("Distance between the 2 sets of coodinates:", clc_dst(crds1, crds2))
