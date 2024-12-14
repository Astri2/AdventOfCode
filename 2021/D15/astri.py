from copy import deepcopy


def get_all_paths(m,p,x,y,depth):
    xmax = len(m)-1 ; ymax = len(m[0])-1
    matrice = deepcopy(m)
    path = deepcopy(p)
    path[0]+=matrice[x][y][0]
    path[1].append((x,y))
    
    if x==xmax and y==ymax: 
        return path #end reached

    paths=[]
     
    if(x!=xmax and matrice[x+1][y][1] == False):
        matrice[x+1][y][1] = True
        t = get_all_paths(matrice,path,x+1,y,depth+1)
        paths.extend(t)
    if(y!=ymax and matrice[x][y+1][1] == False):
        matrice[x][y+1][1] = True
        t = get_all_paths(matrice,path,x,y+1,depth+1)
        paths.extend(t)

    if len(paths) == 0:
        return [path]
    else: return paths


def get_optimal_path(matrice):
    matrice[0][0][1] = True
    paths = get_all_paths(matrice,[0,[]],0,0,0)
    dic = {}
    for i in range(0,len(paths)-1,2):
        dic[paths[i]]=paths[i+1]
    mini = min(dic.keys())
    print("min",mini-matrice[0][0][0],"\n",dic[mini])


def parse_input():
    f = open("AdventOfCode2021\\D15\\input.txt","r")
    lines = f.read().splitlines()
    f.close()
    matrice=[]
    for line in lines:
        matrice.append([])
        for val in line:
            matrice[-1].append([int(val),False])
    return matrice

if __name__ == "__main__":
    matrice = parse_input()
    get_optimal_path(matrice)