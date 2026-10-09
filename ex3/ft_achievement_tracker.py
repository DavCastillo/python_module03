#!/usr/bin/env python3

import random

achvmnts = ['Crafting Genius', 'Strategist', 'World Savior',
            'Speed Runner', 'Survivor', 'Master Explorer',
            'Treasure Hunter', 'Unstoppable', 'First Steps',
            'Collector Supreme', 'Untouchable', 'Sharp Mind', 'Boss Slayer']


def gen_player_achvmnts() -> set[str]:
    n_achvmnts = random.randint(4, len(achvmnts))
    p_achvmts = set()
    while (n_achvmnts):
        rnd_achv = random.randint(0, (len(achvmnts) - 1))
        p_achvmts.add(achvmnts[rnd_achv])
        n_achvmnts -= 1
    return (p_achvmts)


if __name__ == "__main__":
    print("=== Achievement Tracker System ===\n")

    alice = gen_player_achvmnts()
    bob = gen_player_achvmnts()
    charlie = gen_player_achvmnts()
    dylan = gen_player_achvmnts()

    print("Player Alice:", alice)
    print("Player Bob:", bob)
    print("Player Charlie:", charlie)
    print("Player Dylan:", dylan)

    union_achvmnts = alice | bob | charlie | dylan
    intersec_achvmnts = alice & bob & charlie & dylan
    print("\nAll distinct achievements:", union_achvmnts)
    print("\nCommon achievements:", intersec_achvmnts)

    print("\nOnly Alice has:", (alice - bob - charlie - dylan))
    print("Only Bob has:", (bob - alice - charlie - dylan))
    print("Only Charlie has:", (charlie - alice - bob - dylan))
    print("Only Dylan has:", (dylan - alice - bob - charlie))

    achvmnts_set = set(achvmnts)
    print("\nAlice is missing:", achvmnts_set.difference(alice))
    print("Bob is missing:", achvmnts_set.difference(bob))
    print("Charlie is missing:", achvmnts_set.difference(charlie))
    print("Dylan is missing:", achvmnts_set.difference(dylan))
