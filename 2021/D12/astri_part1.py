def get_path(map,pos,current):
    paths_from_here=[]
    for neighboor in map[pos]:
        if(neighboor in current and not neighboor.isupper()):
            paths_from_here.append(list(current))
        else:
            if neighboor == "end":
                paths_from_here.append(list(current)+[neighboor])
            else:
                paths_from_here.extend(get_path(map,neighboor,current+[neighboor]))
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

def part1(map):
    paths = [path for path in get_path(map,"start",["start"]) if path[-1]=="end"]
    print(len(paths))

if __name__=="__main__":
    f = open("AdventOfCode2021\\D12\\input.txt","r")
    input = [line.split("-") for line in f.read().splitlines()]
    part1(get_caves_connections(input))

#40mins