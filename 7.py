import aoc
from aoc import pr
from collections import defaultdict, Counter
from itertools import product

ls = aoc.getlines()
p1, p2 = 0, 0
probs = []
for l in ls:
    goal, ns = l.split(":")
    goal = int(goal)
    ns = list(map(int, ns.split()))
    probs.append((goal, ns))


def is_possible(goal, ns):
    N = len(ns) - 1

    for choices in product((True, False), repeat=N):
        tot = ns[0]
        for i, n in enumerate(ns[1:]):
            if choices[i]:
                tot += n
            else:
                tot *= n
            if tot > goal:
                break
        if tot == goal:
            return True
    return False


def is_possible2(goal, ns):
    for choices in product((0, 1, 2), repeat=len(ns) - 1):
        tot = ns[0]
        for i, n in enumerate(ns[1:]):
            if choices[i] == 0:
                tot = int(str(tot) + str(n))
            if choices[i] == 1:
                tot += n
            if choices[i] == 2:
                tot *= n
            if tot > goal:
                break
        if goal == tot:
            return True
    return False


p1 = sum(goal for (goal, ns) in probs if is_possible(goal, ns))
pr(p1)
assert p1 == 5837374519342
p2 = sum(goal for (goal, ns) in probs if is_possible2(goal, ns))
pr(p2)
assert p2 == 492383931650959
