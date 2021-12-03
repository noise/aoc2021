#!/usr/bin/env python3

"""
--- Day 3: Binary Diagnostic ---
"""

import math
import fileinput


def calc(diag):
    w = len(diag[0])
    sums = [0] * w
    gamma = "0b"

    for d in diag:
        for i in range(w):
            sums[i] += int(d[i])
            # sums[i] += (1 if d[i] == '1' else 0) # which is faster?

    for i in range(w):
        gamma += "1" if (sums[i] > (len(diag) / 2)) else "0"

    gamma = int(gamma, 2)
    epsilon = gamma ^ int(math.pow(2, w) - 1)

    print(gamma)
    print(epsilon)
    return gamma * epsilon


print(calc([l.strip() for l in fileinput.input()]))  # 3549854
