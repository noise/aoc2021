#!/usr/bin/env python3

"""
Track route
"""

import fileinput

sample = ["forward 5", "down 5", "forward 8", "up 3", "down 8", "forward 2"]


def parse(dirs):
    return [(d, int(n)) for (d, n) in [d.split(" ") for d in dirs]]


def calc1(dirs):
    pos = sum(n for (d, n) in dirs if d == "forward")
    up = sum(n for (d, n) in dirs if d == "up")
    down = sum(n for (d, n) in dirs if d == "down")
    depth = down - up
    print(pos, depth, pos * depth)


def calc2(dirs):
    aim = 0
    depth = 0
    pos = 0
    for (d, x) in dirs:
        if d == "forward":
            pos += x
            depth += aim * x
        elif d == "up":
            aim -= x
        elif d == "down":
            aim += x
    print(pos, depth, pos * depth)


dirs = parse(sample)
calc1(dirs)
calc2(dirs)
dirs = parse(fileinput.input())
calc1(dirs)  # 1911 724 1383564
calc2(dirs)  # 1911 778813 1488311643
