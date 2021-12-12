#!/usr/bin/env python3

"""
--- Day 11: Dumbo Octopus
"""


def parse(fname):
    with open(fname) as fp:
        grid = [[int(n) for n in l.strip()] for l in fp.readlines()]
    return grid


def adjacent(grid, i, j):
    adj = []
    for y in range(max(j - 1, 0), min(j + 2, 10)):
        for x in range(max(i - 1, 0), min(i + 2, 10)):
            if i == x and j == y:
                continue
            adj.append((y, x))
    # print(adj)
    return adj


def inc1(grid):
    return [list(map(lambda n: n + 1, l)) for l in grid]


def flash9s(grid, flashed):
    flashed_cnt = 0
    for y in range(10):
        for x in range(10):
            if grid[y][x] > 9 and not flashed[y][x]:
                # print("flashing at ", x, y)
                adj = adjacent(grid, x, y)
                for i, j in adj:
                    grid[i][j] += 1
                flashed[y][x] = True
                # show(grid)
                flashed_cnt += 1
    return grid, flashed, flashed_cnt


def reset9s(grid, flashed):
    # print("reseting nines", flashed)
    # return [list(map(lambda n: 0 if n>9 else n, l)) for l in grid]
    for y in range(10):
        for x in range(10):
            if flashed[y][x]:
                grid[y][x] = 0
    return grid


def sim(grid, f_cnt):
    """
    - First, the energy level of each octopus increases by 1.
    - Then, any octopus with an energy level greater than 9 flashes.
      This increases the energy level of all adjacent octopuses by 1,
      including octopuses that are diagonally adjacent. If this causes
      an octopus to have an energy level greater than 9, it also flashes.
      This process continues as long as new octopuses keep having their
      energy level increased beyond 9. (An octopus can only flash at most
      once per step.)
    - Finally, any octopus that flashed during this step has its energy
      level set to 0, as it used all of its energy to flash.
    """
    grid = inc1(grid)
    round = 1
    flashed = [[False for _ in range(10)] for _ in range(10)]
    f_cnt2 = 0
    sync = False
    while True:
        grid, flashed, flashed_cnt = flash9s(grid, flashed)
        f_cnt += flashed_cnt
        f_cnt2 += flashed_cnt
        if flashed_cnt == 0:
            break
        round += 1

    if f_cnt2 == 100:
        # print("got flash count 100 at step")
        sync = True
    grid = reset9s(grid, flashed)
    # show(grid, flashed)
    # print(f_cnt, flashed_cnt)
    return grid, f_cnt, sync


def show(grid, flashed=None):
    for l in grid:
        # if flashed:
        #    print(' '.join([str(n) for n in l]))
        # else:
        print(" ".join([str(n) for n in l]))


def doit(fname):
    grid = parse(fname)
    f_cnt = 0
    for i in range(100):
        print("================== STEP {} =============".format(i + 1))
        grid, f_cnt, _ = sim(grid, f_cnt)
        show(grid)
    print("solution: ", f_cnt)


def doit2(fname):
    grid = parse(fname)
    f_cnt = 0
    for i in range(500):
        print("=============== STEP {} =============".format(i + 1))
        grid, f_cnt, sync = sim(grid, f_cnt)
        show(grid)
        if sync:
            print("got sync at round ", i + 1)
            break
    print("solution: ", f_cnt)


doit("11-sample.txt")  # 1656
doit("11.txt")  # 1723

doit2("11-sample.txt")  # step 195
doit2("11.txt")  # step 327
