TEST = False
import os
import networkx as nx
with open(f"2024/{os.path.split(os.path.split(__file__)[0])[1]}/input{"_test" if TEST else ""}.txt") as f:
    lines = f.read().splitlines()

G = nx.Graph()
for line in lines:
    a,b = line.split("-")
    G.add_node(a)
    G.add_node(b)
    
    G.add_edge(a,b)


max_clq = None
max_size = 0
for clq in nx.clique.find_cliques(G):
    if len(clq) > max_size:
        max_clq = clq
        max_size = len(max_clq)

print(*sorted(max_clq), sep=",")


# for clq in nx.clique.find_cliques(G):
#     print(clq)