import aoc
from aoc import pr
from collections import defaultdict, Counter

ls = aoc.getlines()
p1, p2 = 0, 0

mem = ls[0] + "0"
n = len(mem) // 2
size = [0] * n
gap = [0] * n
for i in range(0,n):
    size[i] = int(mem[2*i])
    gap[i] = int(mem[2*i+1])
assert all(s != 0 for s in size)


def show(size,gap):
    n = len(size)
    s = ""
    for i in range(n):
        s = s + str(i) * size[i] + "." * gap[i]
    return s


def shows(state):
    return "".join("." if s == -1 else str(s) for s in state)

L = sum(size) + sum(gap)
state = [-1] * L
p = 0
fileaddress = {} # address[i] contains the ith free memory location
gapaddress = {}
for i in range(0,n):
    for j in range(p,p+size[i]):
        state[j] = i
    fileaddress[i] = p
    gapaddress[i] = p + size[i]
    p += size[i] + gap[i]

gapdict = {s: [] for s in range(10)} #gapdict[s] contains in decreasing order the list of gap ids of size s.
for i, g in enumerate(gap):
    gapdict[g] = [i] + gapdict[g]


# print(gapdict)
for i in range(n-1,1,-1):
    # print(shows(state))
    # print(gapdict)
    to_move = size[i]
    print(f"treating file {i}, size {to_move}")
    candidate_dests = [(gapdict[s][-1],s) for s in range(to_move,10) if len(gapdict[s]) > 0]
    if len(candidate_dests) == 0:
        print(f"there is no gap of size >= {to_move} anymore.")
        continue
    dest, s = min(candidate_dests, key=lambda x: x[0])
    gapdict[s].pop()
    newsize = s - to_move
    if newsize > 0:
        gapdict[newsize].append(dest)
        gapdict[newsize].sort(reverse=True)
    olda = fileaddress[i]

    for p in range(olda,olda+to_move):
        state[p] = -1
    a = gapaddress[dest] # beginning of the gap
    print(f"the leftmost gap of size >= {to_move} is at #{dest}, starting at {a}")
    print(f"moving file {i} there")
    print(shows(state))
    print(" " * a + "^")
    for p in range(a, a+to_move):
        state[p] = i
    gapaddress[dest] += to_move
    print()
    print(shows(state))
    input()
pr(sum(i * s for (i,s) in enumerate(state) if s > 0))


# print(shows(state))

    

# print(show(size,gap))
# print(shows(state))