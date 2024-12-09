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
fileaddress = {}
gapaddress = {}
# for every location in the state, if it is in a gap, keep track of where this gap starts and ends
interval = {p : None for p in range(L)}

for i in range(0,n):
    fstart = p
    fend = p+size[i]
    gstart = p+size[i]
    gend = p+size[i]+gap[i]
    for j in range(p,fend):
        state[j] = i
    for j in range(gstart,gend):
        interval[j] = (gstart,gend) #type: ignore
    fileaddress[i] = p
    gapaddress[i] = p + size[i]
    p += size[i] + gap[i]


def findpos(state,n,x):
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

def move(state,f,orig,dest):
    for p in range(dest,dest+size[f]):
        state[p] = f
    
    for p in range(orig,orig+size[f]):
        state[p] = -1

for f in range(n-1,-1,-1):
    print(f)
    a = findpos(state,size[f],fileaddress[f])
    if a is None:
        # print("nothing found")
        continue
    move(state,f,fileaddress[f],a)
    # print(shows(state))

pr(sum(i * s for (i,s) in enumerate(state) if s > 0))



# gapbook = dict((gapaddress[i], gap[i]) for i in range(0,n))


# for f in range(n-1,-1,-1):
#     dest = None
#     for a in gapbook:
#         if gapbook[a] >= size[f]:
#             dest = gapbook.pop(a)
#             break
#     if dest is None:
#         continue
#     for p in range(dest,dest+size[f]):
#         assert state[p] == -1 # do not overwrite
#         state[p] = f
#         interval[p] = None
    
#     newgapstart = dest + size[f]
#     newgapsize = dest - size[f]
#     newgapend = newgapstart + newgapsize
#     for p in range(newgapstart,newgapend):
#         assert state[p] == -1
#         interval[p] = (newgapstart,newgapend) #type:ignore
    
#     if newgapsize > 0:
#         gapbook[newgapstart] = newgapsize

#     # merge gaps
#     if f == 0:
#         continue
#     pregap = gapaddress[f-1]

