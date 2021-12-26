#!/usr/bin/env python3

"""
--- Day 25: Sea Cucumber ---
"""

from copy import deepcopy


def parse(fname):
    with open(fname) as fp:
        return [list(l.strip()) for l in fp.readlines()]


def empty_target(herd, w, h, x, y):
    if herd[y][x] == ">":
        x2 = (x + 1) % w
        y2 = y
    elif herd[y][x] == "v":
        x2 = x
        y2 = (y + 1) % h
    ok = herd[y2][x2] == "."
    return x2, y2, ok


def step(herd, east):
    w = len(herd[0])
    h = len(herd)
    oks = 0
    nherd = deepcopy(herd)
    for y in range(len(herd)):
        for x in range(len(herd[0])):
            if herd[y][x] == ".":
                continue
            if herd[y][x] == "v" and east:
                continue
            if herd[y][x] == ">" and not east:
                continue

            x2, y2, ok = empty_target(herd, w, h, x, y)
            if ok:
                nherd[y2][x2] = herd[y][x]
                nherd[y][x] = "."
                oks += 1
    return nherd, oks


def show(grid):
    print("\n".join(["".join([n for n in l]) for l in grid]))


def doit(fname):
    herd = parse(fname)
    show(herd)
    steps = 0
    while True:
        herd, ok = step(herd, True)
        herd, ok2 = step(herd, False)
        steps += 1
        # show(herd)
        if not ok and not ok2:  # no moves
            break
    print("solution", steps)


doit("25-sample.txt")  # 58
doit("25.txt")  # 520
