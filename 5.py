#!/usr/bin/env python3

"""
--- Day 5: hydrothermal vent lines ---
"""


def parse(fname):
    with open(fname) as fp:
        return [
            [int(n) for n in l.strip().replace(" -> ", ",").split(",")]
            for l in fp.readlines()
        ]


def show(plot):
    for l in plot:
        print(l)


def horz(l):
    return l[1] == l[3]


def vert(l):
    return l[0] == l[2]


def horz_vert(l):
    return horz(l) or vert(l)


def render(lines, plot, size, diag=False):
    for l in lines:
        if horz(l):
            # print("horz ", l)
            y = l[1]
            for x in range(size):
                plot[y][x] += (
                    1 if (x >= l[0] and x <= l[2]) or (x <= l[0] and x >= l[2]) else 0
                )
        elif vert(l):
            # print("vert ", l)
            x = l[0]
            for y in range(size):
                plot[y][x] += (
                    1 if (y >= l[1] and y <= l[3]) or (y <= l[1] and y >= l[3]) else 0
                )
        elif diag:  # meh
            print("diag", l)
            steps = abs(l[0] - l[2])  # since only 45deg
            dx = 1 if l[2] - l[0] > 0 else -1
            dy = 1 if l[3] - l[1] > 0 else -1
            x = l[0]
            y = l[1]
            for _ in range(steps + 1):
                plot[y][x] += 1
                x += dx
                y += dy
    return plot


def count_intersects(plot):
    # brain hurts, do a loop
    cnt = 0
    for l in plot:
        cnt += sum(1 for n in l if n > 1)

    return cnt


def doit(fname, size, diag=False):
    lines = parse(fname)
    plot = [[0 for _ in range(size)] for _ in range(size)]
    plot = render(lines, plot, size, diag)
    # show(plot)
    print("solution:", count_intersects(plot))


doit("5-sample.txt", 10)  # 5
# doit("5.txt", 1000)  # 5698

doit("5-sample.txt", 10, True)  # 12
doit("5.txt", 1000, True)  # 15463
