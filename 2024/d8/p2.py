TEST = False
import os
with open(f"2024/{os.path.split(os.path.split(__file__)[0])[1]}/input{"_test" if TEST else ""}.txt") as f:
    lines = f.read().splitlines()

from collections import defaultdict
from dataclasses import dataclass
@dataclass(frozen=True, eq=True, repr=True)
class Point:
    i: int
    j: int

    @property 
    def x(self): return self.j
    
    @property
    def y(self): return self.i

    def in_bound(self, h, w):
        return self.i >= 0 and self.j >= 0 and self.i < h and self.j < w

    def __repr__(self):
        return (self.i,self.j)

    def __str__(self):
        return str(self.__repr__())

antennas = defaultdict(list)
antinodes = set()

for i in range(len(lines)):
    for j in range(len(lines[i])):
        if lines[i][j] != '.':
            antennas[lines[i][j]].append(Point(i,j))
            antinodes.add(Point(i,j))

for k,v in antennas.items():
    for i,a1 in enumerate(v):
        for a2 in v[i+1:]:
            vect = Point(a2.i - a1.i, a2.j-a1.j)
            antinode = Point(a1.i - vect.i, a1.j - vect.j)
            while antinode.in_bound(len(lines), len(lines[0])):
                antinodes.add(antinode)
                antinode = Point(antinode.i - vect.i, antinode.j - vect.j)

            antinode = Point(a2.i + vect.i, a2.j + vect.j)
            while antinode.in_bound(len(lines), len(lines[0])):
                antinodes.add(antinode)
                antinode = Point(antinode.i + vect.i, antinode.j + vect.j)
    
print(len(antinodes))

# map = [["." for j in range(len(lines[0]))] for i in range(len(lines))]
# for a in antinodes: map[a.i][a.j] = "#"
# [print("".join(l)) for l in map]


    
