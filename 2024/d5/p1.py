TEST = False
import os
with open(f"{os.path.split(os.path.split(__file__)[0])[1]}/input{"_test" if TEST else ""}.txt") as f:
    lines = f.read().splitlines()

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
            print("False")
            break
        removed.add(node)
    else:
        print("True")
        res += int(nodes[len(nodes)//2])
print(res)
