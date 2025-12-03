with open("d1/input.txt") as f:
    lines = f.read().splitlines()

v = 50
res = 0
for l in lines:
    w = l[0]
    r = int(l[1:])

    shift = 1 if w == 'L' else -1

    for i in range(r):
        v = (v+shift) % 100
        if(v == 0): res +=1


print(res)