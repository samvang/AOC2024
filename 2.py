import aoc

ls = aoc.getlines()

ls = [[int(x) for x in l.rstrip().split()] for l in ls]

def is_safe(l):
    inc = l[1] - l[0] > 0
    if not all((l[i+1]-l[i] > 0) == inc for i in range(0,len(l)-1)):
        return False
    d = [abs(l[i+1]-l[i]) for i in range(0,len(l)-1)]
    return all(1 <= n <= 3 for n in d)

def contains_safe(l):
    for i in range(len(l)):
        l2 = l[:i] + l[i+1:]
        if is_safe(l2):
            return True
    return False

print(sum(is_safe(l) for l in ls))
print(sum(contains_safe(l) for l in ls))