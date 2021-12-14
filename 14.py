#!/usr/bin/env python3

"""
--- Day 14: Extended Polymerization ---
"""
from datetime import datetime as dt


def parse(fname):
    with open(fname) as fp:
        templ = fp.readline().strip()
        fp.readline()
        rules = {k: v for k, v in [l.strip().split(" -> ") for l in fp.readlines()]}
    return templ, rules


def process(templ, rules):
    pairs = [templ[i : i + 2] for i in range(len(templ) - 1)]
    return "".join([p[0] + rules[p] for p in pairs]) + templ[-1]


def doit(fname, steps):
    templ, rules = parse(fname)
    for i in range(steps):
        templ = process(templ, rules)
    x = max(templ.count(c) for c in set(templ))
    n = min(templ.count(c) for c in set(templ))
    print("solution:", x, n, x - n)


doit("14-sample.txt", 10)  # 1588
doit("14.txt", 10)  # 2899
