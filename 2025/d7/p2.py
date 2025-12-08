from functools import lru_cache
import sys

sys.setrecursionlimit(1000)

with open("d7/input.txt") as f:
    lines = f.read().splitlines()

map = []

for i, line in enumerate(lines):
    map.append(list(line))
    idx = line.find("S")
    if(idx != -1):
        start = (i, idx)

@lru_cache
def run(i, j):
    if(i == len(lines)-1): 
        return 1

    if(map[i+1][j] == "."): return run(i+1, j)

    return run(i+1, j+1) + run(i+1, j-1)

print(run(*start))