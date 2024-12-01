import sys

if len(sys.argv) > 1:
    filename = sys.argv[1]
else:
    n = sys.argv[0].split(".")[0]
    filename = f"{n}.in"
    
with open(filename) as f:
    ls = [l.rstrip() for l in f.readlines()]

ns1, ns2 = [], []
for l in ls:
    n1, n2 = map(int, l.split())
    ns1.append(n1)
    ns2.append(n2)

ns1.sort()
ns2.sort()
print(sum(abs(n2-n1) for n1,n2 in zip(ns1,ns2)))

from collections import Counter
cts2 = Counter(ns2)
print(sum(n * cts2[n] for n in ns1))