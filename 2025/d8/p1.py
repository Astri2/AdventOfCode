import heapq
from math import dist
from collections import defaultdict

class UnionFind:
    """Maintains a partition of {0, ..., n-1}
    """
    def __init__(self, n):
        self.up_bound = list(range(n))
        self.rank = [0] * n

    def find(self, x_index):
        """
        :returns: identifier of part containing x_index
        :complex_indexity: O(inverse_ackerman(n))
        """
        if self.up_bound[x_index] == x_index:
            return x_index
        self.up_bound[x_index] = self.find(self.up_bound[x_index])

        return self.up_bound[x_index]

    def union(self, x_index, y_index):
        """
        Merges part that contain x and part containing y
        :returns: False if x_index, y_index are already in same part
        :complexity: O(inverse_ackerman(n))
        """
        repr_x = self.find(x_index)
        repr_y = self.find(y_index)
        if repr_x == repr_y:       # already in the same component
            return False
        if self.rank[repr_x] == self.rank[repr_y]:
            self.rank[repr_x] += 1
            self.up_bound[repr_y] = repr_x
        elif self.rank[repr_x] > self.rank[repr_y]:
            self.up_bound[repr_y] = repr_x
        else:
            self.up_bound[repr_x] = repr_y
        return True

with open("d8/input.txt") as f: lines = f.read().splitlines()
    
n_connection: int = 1000

# parse points
points = [None]*len(lines)
for i, line in enumerate(lines): points[i] = tuple(map(int, line.split(",")))
    
# compute all connection distances
distances = []
for i, p1 in enumerate(points):
    for j, p2 in enumerate(points[i+1:]):
        distances.append((dist(p1, p2), i, j+i+1))

# retrieve n smallests connections (sorted)
min_distances = heapq.nsmallest(n_connection, distances)
# print(*min_distances, sep="\n")

# make connections
uf = UnionFind(len(points))
for (min_dist, i, j) in min_distances:
    uf.union(i, j)

# compute group sizes
group_sizes = defaultdict(int)
for i in range(len(points)):
    group_sizes[uf.find(i)] += 1

max3 = heapq.nlargest(3, group_sizes.values())

print(max3[0] * max3[1] * max3[2])