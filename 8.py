#!/usr/bin/env python3

"""
--- Day 4: Seven segment fun ---
"""


segs = [
    "a",
    "b",
    "c",
    "e",
    "f",
    "g",  # 0
    "c",
    "f",  # 1
    "a",
    "c",
    "d,",
    "e",
    "g",  # 2
    "a",
    "c",
    "d",
    "f",
    "g",  # 3
    "b",
    "c",
    "d",
    "f",  # 4
    "a",
    "b",
    "d",
    "f",
    "g",  # 5
    "a",
    "b",
    "d",
    "e",
    "f",
    "g",  # 6
    "a",
    "c",
    "f",  # 7
    "a",
    "b",
    "c",
    "d",
    "e",
    "f",
    "g",  # 8
    "a",
    "b",
    "c",
    "d",
    "f",
    "g",  # 9
]


def parse(fname):
    with open(fname) as fp:
        outs = [
            [o for o in l.strip().split(" | ")[1].split(" ")] for l in fp.readlines()
        ]
    print(outs)
    return outs


def count_easy(outs):
    return sum([len([d for d in o if len(d) in [2, 3, 4, 7]]) for o in outs])


def doit(fname):
    outs = parse(fname)
    s = count_easy(outs)
    print("solution: ", s)


doit("8-sample.txt")  # 26
doit("8.txt")  # 421
