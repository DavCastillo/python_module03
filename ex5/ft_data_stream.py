#!/usr/bin/env python3

from typing import Generator
import random


players = ['alice', 'bob', 'charlie', 'dylan']
actions = ['run', 'eat', 'sleep', 'grab', 'move', 'climb', 'swim', 'release']


def gen_event() -> Generator[tuple[str, str], None, None]:
    player = players[random.randint(0, len(players) - 1)]
    action = actions[random.randint(0, len(actions) - 1)]
    yield (player, action)


def consume_event(lst_gen: list[tuple[str, str]]) -> Generator[
        list[tuple[str, str]], None, None]:
    while (lst_gen):
        element = random.randint(0, len(lst_gen) - 1)
        print("\nGot event from list:", lst_gen[element])
        lst_gen.remove(lst_gen[element])
        yield lst_gen


if __name__ == "__main__":
    print("=== Game Data Stream Processor ===")
    for event in range(1000):
        pl_ev = next(gen_event())
        print(f"Event {event}: Player {pl_ev[0]} did action {pl_ev[1]}")
    lst_gen = []
    for _ in range(10):
        pl_ev = next(gen_event())
        lst_gen.append(pl_ev)
    print("\nBuilt list of 10 events:", lst_gen)
    for events in consume_event(lst_gen):
        print("Remains in list:", events)
