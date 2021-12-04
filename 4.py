#!/usr/bin/env python3

"""
--- Day 4: Bingo ---
"""


def parse(fname):
    with open(fname) as fp:
        calls = [int(n) for n in fp.readline().split(",")]
        boards = [
            [[(int(n), False) for n in r.split()] for r in b.split("\n")]
            for b in fp.read().strip().split("\n\n")
        ]
    return boards, calls


def transpose(board):
    return list(map(list, zip(*board)))


def mark(board, call):
    return [[(n, True if n == call else m) for n, m in r] for r in board]


def check(board):
    rows = any(all([m for (n, m) in r]) for r in board)
    cols = any(all([m for (n, m) in r]) for r in transpose(board))
    return rows or cols


def play(boards, calls):
    for c in calls:
        for i in range(len(boards)):
            boards[i] = mark(boards[i], c)
            if check(boards[i]):
                #print("got winner:", boards[i])
                return boards[i], c


def score(b, c):
    return sum(n for r in b for n, m in r if not m) * c


def doit(fname):
    boards, calls = parse(fname)
    (win_b, call) = play(boards, calls)
    s = score(win_b, call)
    print(win_b, call)
    print("solution: ", s)


doit("4-sample.txt")  # 4512
doit("4.txt")  # 51034

# part 2 - let the squid win
def doit2(fname):
    boards, calls = parse(fname)
    while len(boards) > 0:
        (win_b, call) = play(boards, calls)
        boards.remove(win_b)
    s = score(win_b, call)
    print(win_b, call)
    print("solution: ", s)

doit2("4-sample.txt")  # 1924
doit2("4.txt")  # 5434
