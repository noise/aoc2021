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


def fix(line):
    openers = "([{<"
    closers = ")]}>"
    points = [1, 2, 3, 4]

    s = []
    pts = 0
    for c in line:
        if c in openers:
            s.append(c)
        elif c in closers:
            last = s.pop()
            if last != openers[closers.index(c)]:
                raise  # should be no more syntax errs
    while len(s) > 0:
        last = s.pop()
        line += closers[openers.index(last)]
        pts = pts * 5 + points[openers.index(last)]
    # print("fixed :", line, pts)
    return pts


def doit(fname):
    lines = parse(fname)
    pts = 0
    for l in lines:
        pts += check(l)
    print("solution: ", pts)


def doit2(fname):
    lines = parse(fname)
    inc = []
    for l in lines:
        pts = check(l)
        if pts == 0:
            inc.append(l)
    pts = 0
    scores = []
    for l in inc:
        scores.append(fix(l))
    scores.sort()
    print("solution: ", scores[int(len(scores) / 2)])


doit("10-sample.txt")  # 26397
doit("10.txt")  # 339477

doit2("10-sample.txt")  # 288957
doit2("10.txt")  # 3049320156
