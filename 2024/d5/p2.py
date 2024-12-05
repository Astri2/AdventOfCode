TEST = False
import os
with open(f"{os.path.split(os.path.split(__file__)[0])[1]}/input{"_test" if TEST else ""}.txt") as f:
    lines = f.read().splitlines()

# snip{ topological_order_dfs
def topological_order_dfs(graph):
    """Topological sorting by depth first search

    :param graph: directed graph in listlist format, cannot be listdict
    :returns: list of vertices in order
    :complexity: `O(|V|+|E|)`
    """
    n = len(graph)
    order = []
    times_seen = [-1] * n
    for start in range(n):
        if times_seen[start] == -1:
            times_seen[start] = 0
            to_visit = [start]
            while to_visit:
                node = to_visit[-1]
                children = graph[node]
                if times_seen[node] == len(children):
                    to_visit.pop()
                    order.append(node)
                else:
                    child = children[times_seen[node]]
                    times_seen[node] += 1
                    if times_seen[child] == -1:
                        times_seen[child] = 0
                        to_visit.append(child)
    return order[::-1]
# snip}

ref_dic = dict()
ref_dic_inv = []
g = []
i = 0
while lines[i]:
    # ensure numbers are from 0 to n
    a, b = lines[i].split("|")
    if a not in ref_dic:
        ref_dic[a] = len(ref_dic)
        ref_dic_inv.append(a)
        g.append([])
    if b not in ref_dic:
        ref_dic[b] = len(ref_dic)
        ref_dic_inv.append(b)
        g.append([])

    g[ref_dic[a]].append(ref_dic[b])
    i+=1
# empty line 

res = 0
for line in lines[i+1:]:
    nodes = line.split(",")
    ref_nodes = [ref_dic[n] for n in nodes]
    ref_nodes_set = set(ref_nodes)
    g2 = [[child for child in node if child in ref_nodes_set] if i in ref_nodes_set else [] for i,node in enumerate(g)]

    removed = set()
    for node in ref_nodes:
        childs = g2[node]
        filtered_childs = [c for c in childs if c in removed]
        if(filtered_childs):
            fixed_order = topological_order_dfs(g2)
            fixed_order = [n for n in fixed_order if n in ref_nodes_set]
            res += int(ref_dic_inv[fixed_order[len(fixed_order)//2]])
            break
        removed.add(node)
   
print(res)
