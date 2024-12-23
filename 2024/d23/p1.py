TEST = False
import os
from collections import defaultdict
with open(f"2024/{os.path.split(os.path.split(__file__)[0])[1]}/input{"_test" if TEST else ""}.txt") as f:
    lines = f.read().splitlines()

g: defaultdict[str, set[str]] = defaultdict(set)
trouples = []


for line in lines:
    a,b = line.split("-")
    
    # if not g[a].isdisjoint(g[b]): print("Trouple !", a,b , g[a].intersection(g[b]))
    for c in g[a].intersection(g[b]):
        trouples.append((a,b,c))
    
    g[a].add(b)
    g[b].add(a)
    
print(*trouples, sep="\n")

res = 0
for a,b,c in trouples:
    if a[0] == 't' or b[0] == 't' or c[0] == 't':
       res+=1
print(res) 