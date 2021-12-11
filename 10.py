#!/usr/bin/env python3

"""
--- Day 10: Syntax Scoring ---
"""

from os import pathsep


def parse(fname):
    with open(fname) as fp:
        return [l.strip() for l in fp.readlines()]


def check(line):
    openers = "([{<"
    closers = ")]}>"
    points = [3, 57, 1197, 25137]

    s = []
    for c in line:
        if c in openers:
            s.append(c)
            # print("push", c)
        elif c in closers:
            last = s.pop()
            # print("pop", last, openers[closers.index(c)])
            if last != openers[closers.index(c)]:
                return points[closers.index(c)]
    return 0


def doit(fname):
    lines = parse(fname)
    pts = 0
    for l in lines:
        pts += check(l)
    print("solution: ", pts)


doit("10-sample.txt")  # 26397
doit("10.txt")  # 339477
