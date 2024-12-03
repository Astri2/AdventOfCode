with open("d1/in.txt") as f:
    lines = f.read().splitlines()

from collections import defaultdict
l1, d2 = [], defaultdict(int)
for line in lines:
    a, b = line.split()
    l1.append(int(a))
    d2[int(b)]+=1

res = 0
for a in l1:
    res += a*d2[a]

print(res)
