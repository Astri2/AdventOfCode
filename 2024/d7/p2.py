TEST = False
import os
import itertools
with open(f"2024/{os.path.split(os.path.split(__file__)[0])[1]}/input{"_test" if TEST else ""}.txt") as f:
    lines = f.read().splitlines()

def concat(n1, n2):
    return 10**len(str(n2))*n1+n2

def is_maxed(t):
    return 2*len(t) == sum(t)

res = 0
for i,line in enumerate(lines):
    print(f"{i}/{len(lines)}     ",end="\r")
    nb, args = line.split(": ")
    nb = int(nb)
    args = list(map(int, args.split()))

    if nb== 0 and not 0 in args:
        continue

    for t in itertools.product([0,1,2], repeat=len(args)-1):
        r = args[0]
        for i,c in enumerate(t):
            if c == 0:
                r += args[i+1]
            elif c == 1: r*= args[i+1]
            else: r = concat(r, args[i+1])
    
        if r == nb:
            res+=r
            break
        
        if(is_maxed(t)): break
print(res)