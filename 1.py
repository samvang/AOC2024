import aoc

ls = aoc.getlines()

from collections import Counter

ns1, ns2 = [], []
for l in ls:
    n1, n2 = map(int, l.split())
    ns1.append(n1)
    ns2.append(n2)

ns1.sort()
ns2.sort()
print(sum(abs(n2 - n1) for n1, n2 in zip(ns1, ns2)))
cts2 = Counter(ns2)
print(sum(n * cts2[n] for n in ns1))
