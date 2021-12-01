#!/usr/bin/env python3

"""
Count the number of times a depth measurement
increases from the previous measurement
"""

import fileinput


def count_inc():
    c = 0
    last = None
    for line in fileinput.input():
        n = int(line.strip())
        if last and n > last:
            c += 1
        last = n
    return c


def count_inc_slide():
    c = 0
    i = 0

    l = [int(line.strip()) for line in fileinput.input()]
    last = l[0]
    for i in range(1, len(l)):
        if i == 1:
            s = l[0] + l[1]
        elif i == len(l) - 2:
            s = l[len(l) - 3] + l[len(l) - 2]
        elif i == len(l) - 1:
            s = l[len(l) - 1]
        else:
            s = l[i - 1] + l[i - 2] + l[i]

        if s > last:
            c += 1
        last = s

    return c


print("simple", count_inc())
print("sliding window", count_inc_slide())
