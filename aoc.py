import sys

if len(sys.argv) > 1:
    filename = sys.argv[1]
else:
    n = sys.argv[0].split(".")[0]
    filename = f"{n}.in"


def getlines():
    with open(filename) as f:
        ls = [l.rstrip() for l in f.readlines()]
    return ls
