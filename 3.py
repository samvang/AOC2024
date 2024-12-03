import aoc
import re

ls = aoc.getlines()
mem = "".join(ls)

pattern = re.compile(r"mul\((\d{1,3}),(\d{1,3})\)")
matches = pattern.findall(mem)
tot = 0
for match in matches:
    n, m = map(int, match)
    tot += n * m

print(tot)
assert tot == 165225049

# tot = 0
# i = 0
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
    
# while i < len(mem):
#     i = mem.find("mul(",i)
#     if i == -1:
#         break
#     i += 4
#     i, k1 = read_num(i)
#     if k1 is None or mem[i] != ",":
#         i += 1
#         continue
#     i += 1
#     i, k2 = read_num(i)
#     if k2 is None or mem[i] != ")":
#         continue
#     tot += k1 * k2
