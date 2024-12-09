import aoc
from aoc import pr
from collections import defaultdict, Counter

ls = aoc.getlines()
p1, p2 = 0, 0

mem = ls[0]
n = len(mem) // 2 + 1
size = [0] * n
gap = [0] * (n-1)
for i in range(0,n):
    size[i] = int(mem[2*i])
    if i + 1 < n:
        gap[i] = int(mem[2*i+1])
size[n-1] = int(mem[2*(n-1)])
assert all(s != 0 for s in size)

def show(size,gap):
    assert len(gap) == len(size) - 1
    n = len(size)
    s = ""
    for i in range(n-1):
        s = s + str(i) * size[i] + "." * gap[i]
    s = s + str(n-1) * size[n-1]
    return s

def checksum(size,gap):
    tot = 0
    pos = 0
    ptr1 = 0 # fileid of current file from left
    ptr2 = len(size) - 1 # pointer from right
    while ptr1 < ptr2:
        s = size[ptr1]
        for _ in range(s):
            tot += pos * ptr1
            print(ptr1, end="")
            pos += 1
        
        g = gap[ptr1]
        ptr1 += 1

        for _ in range(g):
            if size[ptr2] == 0:
                ptr2 -= 1
            tot += pos * ptr2
            print(ptr2, end="")
            size[ptr2] -= 1
            pos += 1
    for _ in range(size[ptr1]):
            tot += pos * ptr1
            print(ptr1, end="")
            pos += 1
    print()
    return tot

p1 = checksum(size,gap)
pr(p1)
# 22:53

# stopped working on part 2 after 30:00