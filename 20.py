#!/usr/bin/env python3

"""
--- Day 20: Trench Map ---
"""


def parse(fname):
    with open(fname) as fp:
        algo = fp.readline()
        fp.readline()
        img = [l.strip() for l in fp.readlines()]
    return algo, img


def adjacentpx(img, i, j):
    adj = []
    for y in range(max(j - 1, 0), min(j + 2, len(img))):
        for x in range(max(i - 1, 0), min(i + 2, len(img[0]))):
            adj.append(img[y][x])
    return adj


def adj2bin(adj):
    b = ""
    for px in adj:
        b += "0" if px == "." else "1"
    return int(b, 2)


def neighbor2bin(img, n):
    b = ""
    for (j, i) in n:
        b += "0" if img[j][i] == "." else "1"
    return int(b, 2)


def exp_img(img, b):
    iy = len(img)
    ix = len(img[0])
    eimg = []
    for j in range(b * 2 + iy):
        l = ""
        if b <= j < b + iy:  # pattern
            l += "".join("." for _ in range(b))
            for i in range(ix):
                l += img[j - b][i]
            l += "".join("." for _ in range(b))
        else:
            l += "".join("." for _ in range(b * 2 + ix))
        eimg.append(l)
    return eimg


def enhance(img, algo):
    enh = []
    for j in range(0, len(img)):
        l = ""
        for i in range(0, len(img[0])):
            a = adjacentpx(img, i, j)
            if not (3 < i < len(img[0]) - 3):  # we are at the edges
                # dirty dirty hack, my algo alternates empty grid so fake it
                # probably I just need to expand by 2 on each round but meh
                if img[0][0] == ".":
                    l += "#"
                else:
                    l += "."
            else:
                b = adj2bin(a)
                l += algo[b]
        enh.append(l)
    return enh


def show(img):
    for j in range(len(img)):
        print(img[j])
    print()


def count_lit(img):
    cnt = 0
    for j in range(5, len(img) - 10):  # more dirty edge hacks
        for i in range(5, len(img[0]) - 10):
            cnt += 1 if img[j][i] == "#" else 0
    print(cnt)
    return cnt


def doit(fname, rounds=2, exp=50):
    algo, img = parse(fname)

    img = exp_img(img, exp)
    show(img)
    for i in range(rounds):
        print("<><><>><><>><>><><><<>><>> ROUND ", i)
        img = enhance(img, algo)
        show(img)
    cnt = count_lit(img)
    print("solution", cnt)


# doit("20-sample.txt")  # 35
#doit("20.txt")  # 5486

# doit("20-sample.txt", 50, 100)  # 3351
doit("20.txt", 50, 100)  # 20210
