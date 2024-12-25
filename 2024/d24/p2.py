TEST = False
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

units=  set()
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
    units.add(len(id_to_name))
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

# for var in topo_order:
#     if states[var] != None: continue
    
#     op, a, b = operations[var]
#     assert states[a] != None and states[b] != None
#     states[var] = op(states[a],states[b])

# res = dict()
# for var in topo_order:
#     res[id_to_name[var]] = states[var]
    
# #filter only Z 
# res2 = {k:v for k,v in res.items() if k.startswith("z")}
# # order by lexico order
# res2 = sorted(res2.items(), key=lambda k: k[0], reverse=True)
# # turn values to a single
# res2 = "".join([str(v) for k,v in res2])
# print(res2)
# # convert to base 2
# print(int(res2, 2))

# # P2

# print("x")
# #filter only X
# res2 = {k:v for k,v in res.items() if k.startswith("x")}
# # order by lexico order
# res2 = sorted(res2.items(), key=lambda k: k[0], reverse=True)
# # turn values to a single
# res2 = "".join([str(v) for k,v in res2])
# print(res2)
# # convert to base 2
# print(int(res2, 2))
# print("y")
# #filter only Y
# res2 = {k:v for k,v in res.items() if k.startswith("y")}
# # order by lexico order
# res2 = sorted(res2.items(), key=lambda k: k[0], reverse=True)
# # turn values to a single
# res2 = "".join([str(v) for k,v in res2])
# print(res2)
# # convert to base 2
# print(int(res2, 2))

"""
x:         110110010101001111001100111101010010110100011
y:         110000110101111100101111001011011111011001101

got :     1101000001011001011111011001000100001001110000
expeted : 1100111001011001011111100001000110010001110000
          ---####---------------###----------##---------
"""

involved =set()
def op_to_str(id_c):
    involved.add(id_to_name[id_c])
    op, id_a, id_b = operations[id_c]
    # involved.add(id_to_name[id_a])
    # involved.add(id_to_name[id_b])
    
    if id_a not in units:
        a = op_to_str(id_a)
    else: a = id_to_name[id_a] 
    if id_b not in units:
        b = op_to_str(id_b)
    else: b = id_to_name[id_b]
        
    return "(" + a + " " + op.__name__ + " " + b + ")"
involved.clear()
print(op_to_str(name_to_id["z00"]))
print(sorted(involved))
involved.clear()
print(op_to_str(name_to_id["z01"]))
print(sorted(involved))
involved.clear()
print(op_to_str(name_to_id["z02"]))
print(sorted(involved))
involved.clear()
print(op_to_str(name_to_id["z03"]))
print(sorted(involved))
involved.clear()
print(op_to_str(name_to_id["z04"]))
print(sorted(involved))
involved.clear()
print(op_to_str(name_to_id["z05"]))
print(sorted(involved))
involved.clear()
print(op_to_str(name_to_id["z06"]))
print(sorted(involved))
involved.clear()
print(op_to_str(name_to_id["z07"]))
print(sorted(involved))

# for i in range(0, 63):
#     for i2 in range(0,63):
#         b = bin(i)[2:]
#         b = "0"*(6-len(b)) + b
#         b2 = bin(i2)[2:]
#         b2 = "0"*(6-len(b2)) + b2
        
#         states = [None]*len(states)
#         states[name_to_id["x00"]] = int(b[-1])
#         states[name_to_id["x01"]] = int(b[-2])
#         states[name_to_id["x02"]] = int(b[-3])
#         states[name_to_id["x03"]] = int(b[-4])
#         states[name_to_id["x04"]] = int(b[-5])
#         states[name_to_id["x05"]] = int(b[0])
#         # states[name_to_id["x06"]] = int(b[0])
#         # states[name_to_id["x07"]] = int(b[0])
#         states[name_to_id["y00"]] = int(b2[-1])
#         states[name_to_id["y01"]] = int(b2[-2])
#         states[name_to_id["y02"]] = int(b2[-3])
#         states[name_to_id["y03"]] = int(b2[-4])
#         states[name_to_id["y04"]] = int(b2[-5])
#         states[name_to_id["y05"]] = int(b2[0])
#         # states[name_to_id["y06"]] = int(b2[0])
#         # states[name_to_id["y07"]] = int(b2[0])
        
#         for var in topo_order:
#             if states[var] != None: continue
#             if id_to_name[var][0] in "xy" and states[var] == None: continue

#             op, a, b = operations[var]
#             if states[a] == None or states[b] == None: continue # skip unused bits
#             states[var] = op(states[a],states[b])

#         res = dict()
#         for var in topo_order:
#             res[id_to_name[var]] = states[var]
            
#         #filter only Z 
#         res2 = {k:v for k,v in res.items() if k.startswith("z")}
#         # order by lexico order
#         res2 = sorted(res2.items(), key=lambda k: k[0], reverse=True)
#         # turn values to a single
#         res2 = "".join([str(v) for k,v in res2][-6:])
#         # print(res2)
#         # convert to base 2
#         b10 = int(res2, 2)
#         print(f"x: {i}, y: {i2}, x+y= {i+i2}, got: {b10}, {'#####' if b10 != i+i2 else ''}")
        
