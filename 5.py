import aoc
from aoc import pr
from collections import defaultdict, Counter
from functools import cmp_to_key

ls = aoc.getlines()
p1, p2 = 0, 0

i = ls.index("")
rules, updates = ls[:i], ls[i + 1 :]
rules = [list(map(int, l.split("|"))) for l in rules]

before = defaultdict(set)
after = defaultdict(set)
for r in rules:
    after[r[0]].add(r[1])
    before[r[1]].add(r[0])
U = [list(map(int, l.split(","))) for l in updates]

def compare(a, b):
    if b in after[a]:
        return -1
    if b in before[a]:
        return 1
    if b == a:
        return 0
    assert False

def correct(u):
    return sorted(u, key=cmp_to_key(compare))

for u in U:
    v = correct(u)
    m = v[len(v) // 2]
    if u == v:
        p1 += m
    else:
        p2 += m
# p1 = sum(middle(u) for u in U if is_valid(u))
# p2 = sum(middle(correct(u)) for u in U if not is_valid(u))
assert p1 == 4281
assert p2 == 5466

# def is_valid(u):
#     for i, k in enumerate(u):
#         b, a = set(u[:i]), set(u[i + 1 :])
#         if not (b <= before[k] and a <= after[k]):
#             return False
#     return True
