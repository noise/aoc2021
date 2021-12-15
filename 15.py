#!/usr/bin/env python3

"""
--- Day 15: Chiton ---
"""
from queue import PriorityQueue
import time


def parse(fname):
    with open(fname) as fp:
        risks = [list(map(lambda s: int(s), list(l.strip()))) for l in fp.readlines()]
    return risks


def show(risks):
    for y in range(len(risks)):
        for x in range(len(risks[0])):
            print(risks[y][x], end="")
        print()


def grow(grid, n):
    w = len(grid[0])
    h = len(grid)
    newg = [[0 for _ in range(w * n)] for _ in range(h * n)]
    for j in range(h * n):
        for i in range(w * n):
            newg[j][i] = ((grid[j % h][i % w] + int(j / h) + int(i / w) - 1) % 9) + 1
    return newg


def adjacent(grid, i, j):
    adj = []
    if j > 0:
        adj.append((i, j - 1))
    if j < len(grid) - 1:
        adj.append((i, j + 1))
    if i > 0:
        adj.append((i - 1, j))
    if i < len(grid[0]) - 1:
        adj.append((i + 1, j))
    return adj


def ucs(risks, start, goal):
    """thanks wikipedia"""
    frontier = PriorityQueue()

    # source has no cost
    frontier.put((0, start))
    explored = {start: 0}

    while not frontier.empty():
        (c, node) = frontier.get()
        if node == goal:
            return explored

        for a in adjacent(risks, node[0], node[1]):
            cost = explored[node] + risks[a[1]][a[0]]

            if a not in explored or cost < explored[a]:
                explored[a] = cost
                frontier.put((cost, a))
    return explored


def doit(fname):
    risks = parse(fname)
    h = len(risks)
    w = len(risks[0])
    costs = ucs(risks, (0, 0), (w - 1, h - 1))
    print("solution:", costs[(w - 1, h - 1)])


def doit2(fname):
    risks = parse(fname)
    risks = grow(risks, 5)
    h = len(risks)
    w = len(risks[0])
    costs = ucs(risks, (0, 0), (w - 1, h - 1))
    print("solution:", costs[(w - 1, h - 1)])


doit("15-sample.txt")  # 40
doit("15.txt")  # 415

doit2("15-sample.txt")  # 315
doit2("15.txt")  # 2864
