import aoc
from aoc import pr
from collections import defaultdict, Counter

ls = aoc.getlines()
p1, p2 = 0, 0
n = len(ls)
assert n == len(ls[0])
G = {(i,j) : ls[i][j] == "#" for i in range(n) for j in range(n)}

start = (-1,-1)
for i in range(n):
    for j in range(n):
        if ls[i][j] == "^":
            start = (i,j)
            break
assert start != (-1,-1)
DIRS = [(-1,0),(0,1),(1,0),(0,-1)]

def exit_path(ox=-1,oy=-1):
    px,py = start
    d = 0
    visited = {(px,py,d)}

    while True:
        dx, dy = DIRS[d]
        nx, ny = px + dx, py + dy
        if G.get((nx,ny)) is None:
            return visited
        if G[(nx,ny)] or (nx,ny) == (ox,oy):
            d = (d+1) % 4
        else:
            px,py = (nx,ny)
            if (px,py,d) in visited:
                return []
            visited.add((px,py,d))

visited = exit_path()
vis = {(x,y) for (x,y,_) in visited}
p1 = len(vis)
assert p1 == 5095

for i, (ox,oy) in enumerate(vis):
    if exit_path(ox,oy) == []:
        p2 += 1
assert p2 == 1933