TEST = False
import os
with open(f"2024/{os.path.split(os.path.split(__file__)[0])[1]}/input{"_test" if TEST else ""}.txt") as f:
    lines = f.read().splitlines()
from collections import defaultdict
from dataclasses import dataclass
@dataclass(frozen=True, eq=True)
class Point:
    i: int
    j: int

    @property 
    def x(self): return j
    
    @property
    def y(self): return i

    def __repr__(self):
        return (i,j)

antennas = defaultdict(list)
antinodes = set()
res = 0

for i in range(len(lines)):
    for j in range(len(lines[i])):
        if lines[i][j] != '.':
            antennas[lines[i][j]].append(Point(i,j))

for k,v in antennas.items():
    for i,a1 in enumerate(v):
        for a2 in v[i+1:]:
            vect = Point(a2.i - a1.i, a2.j-a1.j)
            antinodes.add(Point(a1.i - vect.i, a1.j - vect.j))
            antinodes.add(Point(a2.i + vect.i, a2.j + vect.j))

for antinode in antinodes:
    if antinode.i >= 0 and antinode.i < len(lines)\
      and antinode.j >= 0 and antinode.j < len(lines[0]):
        res +=1

print(res)
