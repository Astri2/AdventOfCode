# 9h01->9h50
# 10h13 -> 10h35


# 65601038650482: too low

TEST = True
import os
from linkedlist import *
from collections import defaultdict
from math import log10, pow
with open(f"2024/{os.path.split(os.path.split(__file__)[0])[1]}/input{"_test" if TEST else ""}.txt") as f:
    lines = f.read().splitlines()

d: defaultdict[int, int] = defaultdict(int)

res = 0
for n in lines[0].split():
    d[int(n)]+=1
    res+=1

n = 75
for i in range(n):
    # print(d)
    print(f"{i+1}/{n}",end="")

    new_d = defaultdict(int)
    for k, v in d.items():
        if k == 0:
            new_d[1] += v
        elif (len := (int)(log10(k)) + 1) % 2 == 0: 
            div = int(pow(10, len//2))
            new_d[k%div] += v
            new_d[k//div] += v
            res+=v
        else:
            new_d[k*2024] += v
    d = new_d

    print("->", res, end="\r")
print()
print(res)