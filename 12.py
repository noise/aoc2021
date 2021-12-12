#!/usr/bin/env python3

"""
--- Day 11: Passage Pathing ---
"""

from collections import defaultdict


class Graph:
    def __init__(self, nv):
        self.nv = nv
        self.graph = defaultdict(list)

    def addEdge(self, a, b):
        self.graph[a].append(b)
        if a != "start" and b != "end":  # omit these
            self.graph[b].append(a)

    def walk(self, a, dest, visited, path):
        path.append(a)
        if a.islower():
            visited[a] = True

        if a == dest:
            # end, backout
            self.cnt += 1
        else:
            # explore all edges from here
            for c in self.graph[a]:
                if not c in visited or not visited[c]:
                    self.walk(c, dest, visited, path)

        path.pop()
        visited[a] = False

    def lowerdoubles(self, path):
        return len(
            {n: path.count(n) for n in set(path) if n.islower() and path.count(n) > 1}
        )

    def walk2(self, a, dest, visited, path):
        path.append(a)
        if a.islower():
            visited[a] = True

        if a == dest:
            # end, backout
            self.cnt += 1
        else:
            for c in self.graph[a]:
                if c.isupper():
                    self.walk2(c, dest, visited, path)
                elif c.islower() and c != "start":
                    if (c in visited and visited[c]) and self.lowerdoubles(path) == 0:
                        self.walk2(c, dest, visited, path)
                    elif c not in visited or visited[c] == False:
                        self.walk2(c, dest, visited, path)

        path.pop()
        if a not in path:
            visited[a] = False

    def paths(self, a, b, small):
        visited = {"small": None}
        paths = []
        self.cnt = 0
        if small:
            self.walk2(a, b, visited, paths)
        else:
            self.walk(a, b, visited, paths)
        return self.cnt

    def printg(self):
        print(self.graph)


def parse(fname):
    with open(fname) as fp:
        edges = [(a, b) for a, b in [l.strip().split("-") for l in fp.readlines()]]
        print(edges)
    return edges


def doit(fname, small=False):
    edges = parse(fname)
    graph = Graph(len(edges))
    for a, b in edges:
        graph.addEdge(a, b)

    graph.printg()
    cnt = graph.paths("start", "end", small)
    print("solution: ", cnt)


# doit("12-sample1.txt")  # 10
# doit("12-sample2.txt")  # 19
# doit("12-sample3.txt")  # 226
doit("12.txt")  # 5874

# doit("12-sample1.txt", True)  # 36
# doit("12-sample2.txt", True)  # 103
# doit("12-sample3.txt", True)  # 3509
doit("12.txt", True)  # 153592
