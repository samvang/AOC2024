import aoc
from aoc import pr

ls = aoc.getlines()
p1, p2 = 0, 0
n = len(ls)
G = {(i, j): ls[i][j] for i in range(n) for j in range(n)}
word = "XMAS"
for x, y in G:
    for dx in (-1, 0, 1):
        for dy in (-1, 0, 1):
            for t in range(4):
                if G.get((x + t * dx, y + t * dy)) != word[t]:
                    break
            else:
                p1 += 1
pr(p1)

cs = ([(-1, -1), (1, 1)], [(-1, 1), (1, -1)])
for x in range(1, n - 1):
    for y in range(1, n - 1):
        if G.get((x, y)) == "A":
            for c in cs:
                if set(G.get((x + dx, y + dy)) for (dx, dy) in c) != {"M", "S"}:
                    break
            else:
                p2 += 1
pr(p2)
