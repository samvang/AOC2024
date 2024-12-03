import aoc
import re

ls = aoc.getlines()
mem = "".join(ls)
tot = 0
pattern = re.compile(r"mul\((\d{1,3}),(\d{1,3})\)|do\(\)|don't\(\)")

active = True
for m in pattern.finditer(mem):
    if m.group(0) == "do()":
        active = True
    elif m.group(0) == "don't()":
        active = False
    else:
        if active:
            tot += int(m.group(1)) * int(m.group(2))
print(tot)
assert tot == 108830766

# def read_num(i):
#     buf = mem[i]
#     if not buf.isdigit():
#         return i, None
#     for _ in range(2):
#         i += 1
#         if mem[i].isdigit():
#             buf += mem[i]
#         else:
#             return i, int(buf)
#     i += 1
#     return i, int(buf)

# i = 0
# active = True
# while i < len(mem):
#     imul = mem.find("mul(",i)
#     ido = mem.find("do()", i)
#     idont = mem.find("don't()", i)
#     if max(imul,ido,idont) == -1:
#         break
#     imul = len(mem) if imul == -1 else imul
#     ido = len(mem) if ido == -1 else ido
#     idont = len(mem) if idont == -1 else idont
#     i = min(imul, ido, idont)
#     if i == -1:
#         break
#     if mem[i:i+4] == "mul(":
#         i += 4
#         i, k1 = read_num(i)
#         if k1 is None or mem[i] != ",":
#             i += 1
#             continue
#         i += 1
#         i, k2 = read_num(i)
#         if k2 is None or mem[i] != ")":
#             continue
#         if active:
#             tot += k1 * k2
#     if mem[i:i+4] == "do()":
#         active = True
#         i += 4
#     if mem[i:i+7] == "don't()":
#         active = False
#         i += 7
