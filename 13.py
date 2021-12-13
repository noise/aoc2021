#!/usr/bin/env python3

"""
--- Day 13: Transparent Origami ---
"""


def parse(fname):
    with open(fname) as fp:
        ptl, foldl = fp.read().split("\n\n")
        pts = [[int(n) for n in l.strip().split(",")] for l in ptl.split("\n")]
        folds = [l.strip().split(" ")[2].split("=") for l in foldl.split("\n")]
    return pts, folds


def foldpt(x, y, f):
    v = int(f[1])
    if f[0] == "y":
        return [x, v - (y - v)] if y > v else [x, y]
    else:
        return [v - (x - v), y] if x > v else [x, y]


def fold(pts, f):
    return [foldpt(x, y, f) for x, y in pts]


def show(pts):
    xr = max(p[0] for p in pts)
    yr = max(p[1] for p in pts)
    for y in range(yr + 1):
        for x in range(xr + 1):
            if [x, y] in pts:
                print("#", end="")
            else:
                print(".", end="")
        print()


def doit(fname):
    pts, folds = parse(fname)
    for f in folds:
        pts = fold(pts, f)
        print("# pts: ", len(set([tuple(p) for p in pts])))
    show(pts)


doit("13-sample.txt")  # 17 (first fold)
doit("13.txt")  # CPJBERUL
