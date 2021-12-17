#!/usr/bin/env python3

"""
--- Day 17: Trick Shot ---
"""


def sign(n):
    return -1 if n < 0 else 1


def inrange(x, y, tx1, tx2, ty1, ty2):
    return tx1 <= x <= tx2 and ty1 <= y <= ty2


def overshot(x, y, tx1, tx2, ty1, ty2):
    return x > tx2 or y < ty1


def tick(x, y, vx, vy):
    x += vx
    y += vy
    vx += 0 if vx == 0 else -sign(vx)  # drag
    vy += -1  # gravity
    return x, y, vx, vy


def fire(vx, vy, tx1, tx2, ty1, ty2):
    x = 0
    y = 0
    maxy = y
    while True:
        if inrange(x, y, tx1, tx2, ty1, ty2):
            # print("hit", x, y, maxy)
            return x, y, maxy
        if overshot(x, y, tx1, tx2, ty1, ty2):
            # print("overshot", x, y, tx2, ty2)
            return -1, -1, -1
        x, y, vx, vy = tick(x, y, vx, vy)
        maxy = max(maxy, y)


def doit(tx1, tx2, ty1, ty2):
    gmaxy = 0
    cntgood = 0
    goods = []
    for vy in range(-200, 200):
        for vx in range(1, 300):
            x, y, maxy = fire(vx, vy, tx1, tx2, ty1, ty2)
            if maxy == -1:  # overshot
                continue
            else:
                cntgood += 1
                goods.append([vx, vy])

            if maxy > gmaxy:
                gmaxy = maxy
                maxvx = vx
                maxvy = vy
    print("final maxy", gmaxy, maxvx, maxvy, "count good", cntgood)
    # print( min([g[0] for g in goods]), max([g[0] for g in goods]))
    # print( min([g[1] for g in goods]), max([g[1] for g in goods]))


# sample
doit(20, 30, -10, -5)  # 45, 112 good
# target area: x=185..221, y=-122..-74
doit(185, 221, -122, -74)  # 7381, 19,121, 3019 good
