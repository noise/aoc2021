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


print(count_inc())
