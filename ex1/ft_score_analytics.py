#!/usr/bin/env python3

import sys


def get_scores(argv: list[str]) -> list[int]:
    idx = 0
    scores = []
    while (idx < len(argv)):
        try:
            scores.append(int(argv[idx]))
        except ValueError:
            print("Invalid parameter: '" + argv[idx] + "'")
        idx += 1
    return (scores)


if __name__ == "__main__":
    print("=== Player Score Analytics ===")
    scores = get_scores(sys.argv[1:])
    if (len(scores) == 0):
        print("No scores provided. ", end='')
        print("Usage: python3", sys.argv[0], "<score1> <score2> ...")
    else:
        print("Score processed:", scores)
        print("Total players:", len(scores))
        print("Total score:", sum(scores))
        print("Average score:", (sum(scores) / len(scores)))
        print("High score:", max(scores))
        print("Low score:", min(scores))
        print("Score range:", (max(scores) - min(scores)))
    print("")
