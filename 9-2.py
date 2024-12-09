import aoc
from aoc import pr
from collections import defaultdict, Counter

ls = aoc.getlines()
p1, p2 = 0, 0

mem = ls[0] + "0"
assert len(mem) % 2 == 0
n = len(mem) // 2
size = [0] * n
gap = [0] * n
for i in range(0, n):
    size[i] = int(mem[2 * i])
    gap[i] = int(mem[2 * i + 1])
assert all(s != 0 for s in size)

L = sum(size) + sum(gap)
state = [-1] * L
address = {}

p = 0
for i in range(0, n):
    for j in range(p, p + size[i]):
        state[j] = i
    address[i] = p
    p += size[i] + gap[i]


def findpos(state, n, x):
    """Find leftmost start position before x where we have a continuous gap of size n"""
    buf = 0
    start = None
    p = 0
    while p <= x:
        if state[p] == -1:
            if start is None:
                start = p
            buf += 1
            if buf >= n:
                return start
        else:
            buf = 0
            start = None
        p += 1
    return None


def move(state, f, orig, dest):
    for p in range(dest, dest + size[f]):
        state[p] = f

    for p in range(orig, orig + size[f]):
        state[p] = -1


for f in range(n - 1, -1, -1):
    a = findpos(state, size[f], address[f])
    if a is None:
        continue
    move(state, f, address[f], a)

pr(sum(i * s for (i, s) in enumerate(state) if s > 0))
