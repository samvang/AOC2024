import aoc
from aoc import pr
from collections import defaultdict, Counter

ls = aoc.getlines()
p1, p2 = 0, 0
n = len(ls)
G = {(i, j): ls[i][j] for i in range(n) for j in range(n)}
locs = defaultdict(list)
for i, j in G:
    if G[(i, j)] != ".":
        locs[G[(i, j)]].append((i, j))


def antilocs(x1, y1, x2, y2):
    dx, dy = x2 - x1, y2 - y1
    return {
        (x, y)
        for (x, y) in {(x1 - dx, y1 - dy), (x2 + dx, y2 + dy)}
        if 0 <= x < n and 0 <= y < n
    }


def antilocs2(x1, y1, x2, y2):
    new = {(x1, y1), (x2, y2)}
    dx, dy = x2 - x1, y2 - y1
    x, y = x1 - dx, y1 - dy
    while 0 <= x < n and 0 <= y < n:
        new.add((x, y))
        x, y = x - dx, y - dy
    x, y = x2 + dx, y2 + dy
    while 0 <= x < n and 0 <= y < n:
        new.add((x, y))
        x, y = x + dx, y + dy
    return new


antinodes = set()
antinodes2 = set()
for freq, xys in locs.items():
    for i, (x1, y1) in enumerate(xys):
        for x2, y2 in xys[i + 1 :]:
            antis = antilocs(x1, y1, x2, y2)
            antis2 = antilocs2(x1, y1, x2, y2)
            antinodes = antinodes.union(antis)
            antinodes2 = antinodes2.union(antis2)
p1 = len(antinodes)
p2 = len(antinodes2)
assert p1 == 303
assert p2 == 1045
