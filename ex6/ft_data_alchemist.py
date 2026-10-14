#!/usr/bin/env python3

import random


names = ['Alice', 'bob', 'Charlie', 'dylan', 'Emma',
         'Gregory', 'jhon', 'kevin', 'Liam']


if __name__ == "__main__":
    print("=== Game Data Alchemist ===\n")
    print("Initial list of players:", names)
    new_all_capitalized = [x.capitalize() for x in names]
    print("New list with all names capitalized:", new_all_capitalized)
    capitalized_only = [x for x in names if x[0].isupper()]
    print("New list of capitalized names only:", capitalized_only)
    print()
    scores = {x: random.randint(0, 1000) for x in new_all_capitalized}
    print("Score dict:", scores)
    avrg_score = round(sum(scores.values()) / len(scores), 2)
    print(f"Score average is: {avrg_score}")
    above_avrg = {k: scores[k] for k in scores if scores[k] > avrg_score}
    print("High scores:", above_avrg)
