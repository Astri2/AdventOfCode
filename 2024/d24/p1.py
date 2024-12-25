TEST = True
import os
with open(f"2024/{os.path.split(os.path.split(__file__)[0])[1]}/input{"_test" if TEST else ""}.txt") as f:
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

def AND(a, b): return a and b
def OR (a, b): return a or  b
def XOR(a, b): return a ^   b

name_to_id = dict()
id_to_name = list()
states = list()
operations = dict()
graph = list() # g[0] = [1,2] => 0 débloque 1 et 2

i = 0 
while lines[i] != "":
    line = lines[i]
    i+=1
    
    var, state = line.split(": ")
    name_to_id[var] = len(id_to_name)
    id_to_name.append(var)
    states.append(int(state))
    graph.append([])

i+=1 # skip empty line

while i < len(lines):
    line = lines[i]
    i+=1
    
    a, op, b, _, c = line.split()
    op = XOR if op == "XOR" else AND if op == "AND" else OR
    
    
    for var in [a,b,c]:
        if var in name_to_id: continue
        
        name_to_id[var] = len(id_to_name)
        id_to_name.append(var)
        states.append(None)
        graph.append([])
    
    id_a, id_b, id_c = name_to_id[a], name_to_id[b], name_to_id[c]
    
    graph[id_a].append(id_c)
    graph[id_b].append(id_c)
    operations[id_c] = (op, id_a, id_b)
    
topo_order = topological_order_dfs(graph)
# print(topo_order)

for var in topo_order:
    if states[var] != None: continue
    
    op, a, b = operations[var]
    assert states[a] != None and states[b] != None
    states[var] = op(states[a],states[b])

res = dict()
for var in topo_order:
    res[id_to_name[var]] = states[var]
    
#filter only Z 
res = {k:v for k,v in res.items() if k.startswith("z")}
# order by lexico order
res = sorted(res.items(), key=lambda k: k[0], reverse=True)
# turn values to a single
res = "".join([str(v) for k,v in res])
print(res)
# convert to base 2
print(int(res, 2))