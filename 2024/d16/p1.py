TEST = False
from heapq import heappop, heappush
def dijkstra(graph, weight, source=0, target=None):
    """single source shortest paths by Dijkstra

       :param graph: directed graph in listlist or listdict format
       :param weight: in matrix format or same listdict graph
       :assumes: weights are non-negative
       :param source: source vertex
       :type source: int
       :param target: if given, stops once distance to target found
       :type target: int

       :returns: distance table, precedence table
       :complexity: `O(|V| + |E|log|V|)`
    """
    n = len(graph)
    assert all(weight[u][i] >= 0 for u in range(n) for i,v in enumerate(graph[u]))
    prec = [None] * n
    black = [False] * n
    dist = [float('inf')] * n
    dist[source] = 0
    heap = [(0, source)]
    while heap:
        dist_node, node = heappop(heap)       # Closest node from source
        if not black[node]:
            black[node] = True
            if node == target:
                break
            for i, neighbor in enumerate(graph[node]):
                dist_neighbor = dist_node + weight[node][i]
                if dist_neighbor < dist[neighbor]:
                    dist[neighbor] = dist_neighbor
                    prec[neighbor] = node
                    heappush(heap, (dist_neighbor, neighbor))
    return dist, prec

import os
with open(f"2024/{os.path.split(os.path.split(__file__)[0])[1]}/input{"_test" if TEST else ""}.txt") as f:
    lines = f.read().splitlines()

map = [[c for c in line] for line in lines]

def get_start():
    for i in range(len(map)):
        for j in range(len(map[0])):
            if map[i][j] == "S":
                map[i][j] = '.'
                return i,j

def get_end():
    for i in range(len(map)):
        for j in range(len(map[0])):
            if map[i][j] == "E":
                map[i][j] = '.'
                return i,j
            
s_i,s_j = get_start()
e_i,e_j = get_end()


N = len(map)

def pos_to_idx(i,j):
    return i*N+j

s_idx = pos_to_idx(s_i, s_j)
e_idx = pos_to_idx(e_i, e_j)

G = [[] for _ in range(N*N)]
W = [[] for _ in range(N*N)]

def add_node(i1, i2, w):
    G[i1].append(i2)
    W[i1].append(w)
    # G[i2].append(i1)
    # W[i2].append(w)

corners = set()
for i in range(1, N-1):
    for j in range(1, N-1):
        if (i,j) in corners and (i,j) != (s_i,s_j): continue

        if map[i][j] == '#': continue
        idx = pos_to_idx(i,j)

        # looking down
        if map[i+1][j] == '.':
            corner = False
            if map[i+1][j+1] == '.':
                add_node(idx, pos_to_idx(i+1,j+1), 1002)
                corner = True
            if map[i+1][j-1] == '.':
                add_node(idx, pos_to_idx(i+1,j-1), 1002)
                corner = True
            if corner:
                corners.add((i+1,j))
                if map[i+2][j] == '.':
                    add_node(idx, pos_to_idx(i+2,j), 2)
            if not corner or (i-1,j) == (e_i, e_j):
                add_node(idx, pos_to_idx(i+1,j), 1)

        # looking up
        if map[i-1][j] == '.':
            corner = False
            if map[i-1][j+1] == '.':
                if idx == s_idx:
                    add_node(idx, pos_to_idx(i-1,j+1), 2002)
                else:
                    add_node(idx, pos_to_idx(i-1,j+1), 1002)
                corner = True
            if map[i-1][j-1] == '.':
                if idx == s_idx:
                    add_node(idx, pos_to_idx(i-1,j-1), 2002)
                else: add_node(idx, pos_to_idx(i-1,j-1), 1002)
                corner = True
            if corner:
                corners.add((i-1,j))
                if map[i-2][j] == '.':
                    if idx == s_idx:
                        add_node(idx, pos_to_idx(i-2,j), 1002)
                    else: add_node(idx, pos_to_idx(i-2,j), 2)
            if not corner or (i-1,j) == (e_i, e_j):
                if idx == s_idx: add_node(idx, pos_to_idx(i-1,j), 1001)
                else: add_node(idx, pos_to_idx(i-1,j), 1)

        # looking right
        if map[i][j+1] == '.':
            corner = False
            if map[i+1][j+1] == '.':
                add_node(idx, pos_to_idx(i+1,j+1), 1002)
                corner = True
            if map[i-1][j+1] == '.':
                add_node(idx, pos_to_idx(i-1,j+1), 1002)
                corner = True
            if corner:
                corners.add((i,j+1))
                if map[i][j+2] == '.':
                    add_node(idx, pos_to_idx(i,j+2), 2)
            if not corner or (i,j+1) == (e_i, e_j):
                add_node(idx, pos_to_idx(i,j+1), 1)

        # looking left
        if map[i][j-1] == '.':
            corner = False
            if map[i+1][j-1] == '.':
                add_node(idx, pos_to_idx(i+1,j-1), 1002)
                corner = True
            if map[i-1][j-1] == '.':
                add_node(idx, pos_to_idx(i-1,j-1), 1002)
                corner = True
            if corner:
                corners.add((i,j-1))
                if map[i][j-2] == '.':
                    add_node(idx, pos_to_idx(i,j-2), 2)
            if not corner or (i,j-1) == (e_i, e_j):
                add_node(idx, pos_to_idx(i,j-1), 1)

# print(G)
# print(W)

dist, path = dijkstra(G, W, pos_to_idx(s_i, s_j), pos_to_idx(e_i, e_j))
print(dist[pos_to_idx(e_i, e_j)])