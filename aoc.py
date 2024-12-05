import sys
sys.setrecursionlimit(10**6)
import pyperclip as pc

def pr(s):
    print(s)
    pc.copy(s)

if len(sys.argv) > 1:
    filename = sys.argv[1]
else:
    n = sys.argv[0].split(".")[0]
    filename = f"{n}.in"


def getlines():
    with open(filename) as f:
        ls = [l.rstrip() for l in f.readlines()]
    return ls
