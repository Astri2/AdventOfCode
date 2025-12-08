import heapq
import timeit

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

def run():
    with open("d8/input.txt") as f: lines = f.read().splitlines()

    # parse points
    points = [None]*len(lines)
    for i, line in enumerate(lines): points[i] = tuple(map(int, line.split(",")))
        
    # compute all connection distances
    distances = []
    _append = distances.append
    for i, p1 in enumerate(points):
        for j in range(i+1, len(points)):
            p2 = points[j]
            dx = p1[0] - p2[0]
            dy = p1[1] - p2[1]
            dz = p1[2] - p2[2]
            _append((dx*dx+dy*dy+dz*dz, i, j))
    heapq.heapify(distances)

    # make connections until there is a single component left
    components = len(points)
    uf = UnionFind(len(points))
    while components > 1:
        (_, i, j) = heapq.heappop(distances)
        if uf.union(i, j): 
            components -=1
            
    # print(points[i][0] * points[j][0])
