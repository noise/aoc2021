#!/usr/bin/env python3

"""
--- Day 22: Reactor Reboot ---
"""

import re


def parse(fname):
    reg = ".*=([0-9-]+)\.\.([0-9-]+),y=([0-9-]+)\.\.([0-9-]+),z=([0-9-]+)\.\.([0-9-]+)"
    toggles = []
    bounds = []
    with open(fname) as fp:
        for l in fp.readlines():
            t, c = l.split(" ")
            toggles.append(True if t == "on" else False)
            bounds.append([int(n) + 50 for n in re.match(reg, c).groups()])
    return toggles, bounds


def count_on(reactor):
    cnt = 0
    for z in range(101):
        for y in range(101):
            for x in range(101):
                cnt += 1 if reactor[z][y][x] == True else 0
    print(cnt)
    return cnt


def doit(fname, rounds=2, exp=50):
    toggles, bounds = parse(fname)
    reactor = [[[False for _ in range(101)] for _ in range(101)] for _ in range(101)]

    for i in range(len(toggles)):
        t = toggles[i]
        b = bounds[i]
        print(t, b)
        if any([n > 100 or n < 0 for n in b]):
            print("skipping", b)
            continue
        for z in range(b[4], b[5] + 1):
            for y in range(b[2], b[3] + 1):
                for x in range(b[0], b[1] + 1):
                    reactor[z][y][x] = t

    cnt = count_on(reactor)
    print("solution", cnt)


doit("22-sample.txt")  # 590784
doit("22.txt")  # 623748
