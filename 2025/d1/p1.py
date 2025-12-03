with open("d1/input.txt") as f:
    lines = f.read().splitlines()

v = 50
res = 0
for l in lines:
    w = l[0]
    r = int(l[1:])
    if(w == 'L'): v = (v-r)%100
    else: v = (v+r)%100

    if(v == 0): res += 1
print(res)