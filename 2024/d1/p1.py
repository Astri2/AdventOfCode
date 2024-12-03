with open("d1/in.txt") as f:
    lines = f.read().splitlines()

l1, l2 = [], []
for line in lines:
    a, b = line.split()
    l1.append(int(a))
    l2.append(int(b))

l1.sort()
l2.sort()

res = 0
for a,b in zip(l1, l2):
    res += abs(a-b)

print(res)
