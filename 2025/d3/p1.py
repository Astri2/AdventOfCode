with open("d3/input.txt") as f:
    lines = f.read().splitlines()

res = 0
for line in lines:

    max_idx = -1
    max = -1
    for i, c in enumerate(line[:-1]):
        if(int(c) > max):
            max = int(c)
            max_idx = i
    best = 10*max

    max = -1
    for c in line[max_idx+1:]:
        if(int(c) > max):
            max = int(c)
    best += max
    res += best
print(res)
    