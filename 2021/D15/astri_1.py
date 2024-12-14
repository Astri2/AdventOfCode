def upgrade_map(matrice_p):
    map=[]
    for line in matrice_p:
        map.append(line)
        prev_line=line
        for i in range(4):
            new_line = [k+1 if k<9 else 1 for k in prev_line]
            map[-1].extend(new_line)
            prev_line=new_line
    prev_map=map
    for i in range(4):
        new_map = [[k+1 if k<9 else 1 for k in line] for line in prev_map]
        map.extend(new_map)
        prev_map = new_map

    f=open("AdventOfCode2021\\D15\\bigger_map.txt",'w')
    output = ""
    for line in map:
        for c in line:
            output+=str(c)
        output+="\n"
    f.write(output[:-1])
    f.close

    return map

def maj_distance(s1,s2,d,poids,pred,cherche):
    if d[s2] > d[s1]+poids[s2[0]][s2[1]]:
        d[s2] = d[s1]+poids[s2[0]][s2[1]]
        cherche.append(s2)
        pred[s2]=s1

def trouver_min(cherche,d):
    mini = 1e1000
    som=(-1,-1)
    for s in cherche:
        if d[s]<mini:
            som=s
            mini=d[s]
    return som

def init_r(xmax,ymax):
    d={}
    for x in range(xmax+1):
        for y in range(ymax+1):
            d[(x,y)]=1e1000
    d[(0,0)]=0
    return d

def main(part2):
    f = open("AdventOfCode2021\\D15\\input.txt","r")
    matrice_p = [[int(c) for c in line] for line in f.read().splitlines()] #matrice qui donne le poids des connexions
    f.close()
    if(part2):
        matrice_p = upgrade_map(matrice_p)
    G = {} #connexions entre les nodes
    xmax = len(matrice_p)-1 ; ymax = len(matrice_p[0])-1
    for x in range(xmax+1):
        for y in range(ymax+1):
            neighboor = []
            G[(x,y)] = neighboor
            if x!=0: neighboor.append((x-1,y))
            if x!=xmax: neighboor.append((x+1,y))
            if y!=0: neighboor.append((x,y-1))
            if y!=ymax: neighboor.append((x,y+1))
    d = init_r(xmax,ymax)#matrice qui donne le risque minimum en chaque point

    Q=list(G.keys())
    pred={}
    cherche=[(0,0)]
    while(len(Q)!=0):
        s1 = trouver_min(cherche,d)
        Q.remove(s1)
        cherche.remove(s1)
        for s2 in G[s1]:
            maj_distance(s1,s2,d,matrice_p,pred,cherche)
    print(d[(xmax,ymax)])

    f=open("AdventOfCode2021\\D15\\best_path.txt",'w')
    map = [["." for k in line] for line in matrice_p]
    prede = (xmax,ymax)
    while prede !=(0,0):
        map[prede[0]][prede[1]]=str(matrice_p[prede[0]][prede[1]])
        prede = pred[prede]
    map[0][0]=str(matrice_p[0][0])

    output = ""
    for line in map:
        for c in line:
            output+=c
        output+="\n"
    f.write(output)
    f.close

if __name__ == "__main__":
    is_part2=True
    main(is_part2)