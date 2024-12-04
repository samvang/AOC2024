import aoc
from aoc import pr

ls = aoc.getlines()


def nxmas(cos):
    return sum(
        "".join(ls[x][y] for (x, y) in cos[i : i + 4]) == "XMAS"
        for i in range(len(cos))
    )
    # m = 0
    # for i in range(len(cos)):
    #     buf = [ls[i][j] for (i, j) in cos[i : i + 4]]
    #     if "".join(buf) == "XMAS":
    #         m += 1


n = len(ls)
rows = [[(i, j) for i in range(n)] for j in range(n)]
cols = [[(j, i) for i in range(n)] for j in range(n)]
diags_pos_upper = [[(i, k - i) for i in range(k + 1)] for k in range(1, n)]
diags_pos_lower = [[(i, l + n - i) for i in range(l + 1, n)] for l in range(0, n - 2)]
diags_neg_upper = [[(i, i + k) for i in range(0, n - k)] for k in range(n - 1)]
diags_neg_lower = [[(i, i - k) for i in range(k, n)] for k in range(1, n - 1)]
diags = diags_pos_upper + diags_pos_lower + diags_neg_upper + diags_neg_lower
lines = rows + cols + diags
lines += [l[::-1] for l in lines]
p1 = sum(nxmas(l) for l in lines)
assert p1 == 2521

p2 = 0
for i in range(1, n - 1):
    for j in range(1, n - 1):
        if ls[i][j] == "A":
            c1 = ls[i - 1][j - 1] + ls[i + 1][j + 1]
            c2 = ls[i - 1][j + 1] + ls[i + 1][j - 1]
            if set(c1) == {"M", "S"} and set(c2) == {"M", "S"}:
                p2 += 1

assert p2 == 1912

pr(p1)
pr(p2)