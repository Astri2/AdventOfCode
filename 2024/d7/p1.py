TEST = False
import os
import itertools
with open(f"2024/{os.path.split(os.path.split(__file__)[0])[1]}/input{"_test" if TEST else ""}.txt") as f:
    lines = f.read().splitlines()

res = 0
for line in lines:
    nb, args = line.split(": ")
    nb = int(nb)
    args = list(map(int, args.split()))

    if nb== 0 and not 0 in args:
        continue

    for b in itertools.product([0,1], repeat=len(args)-1):
        r = args[0]
        for i,c in enumerate(b):
            if c == 0:
                r += args[i+1]
            else: r*= args[i+1]
    
        if r == nb:
            res+=r
            break
print(res)