def is_legit(path,neighboor):
    if(neighboor == "start"): return False
    if(neighboor == "end"): return True
    lowers=[]
    allowedCaveUsed=False
    for step in path+[neighboor]:
        if step.islower():
            if step in lowers:
                if(allowedCaveUsed): return False
                allowedCaveUsed=True
            else:
                lowers.append(step)
    return True 

def get_path(map,pos,current_path):
    paths_from_here=[]
    for neighboor in map[pos]:
        if(is_legit(current_path,neighboor)):
            if neighboor == "end":
                paths_from_here.append(current_path+[neighboor])
            else:
                paths_from_here.extend(get_path(map,neighboor,current_path+[neighboor]))
        else:
            continue
    return paths_from_here

def get_caves_connections(input)->dict:
    dic={}
    for side1,side2 in input:
        if(side1 in dic.keys()):
            dic[side1].append(side2)
        else : dic[side1] = [side2]

        if(side2 in dic.keys()):
            dic[side2].append(side1)
        else : dic[side2] = [side1]
    return(dic)

def part2(map):
    paths = [path for path in get_path(map,"start",["start"]) if path[-1]=="end"]
    print(len(paths))

if __name__=="__main__":
    f = open("AdventOfCode2021\\D12\\input.txt","r")
    input = [line.split("-") for line in f.read().splitlines()]
    part2(get_caves_connections(input))

#40min+20min=1h