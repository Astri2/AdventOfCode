import numpy

TESTING = False

def get_visible_trees(n, h, pos, dir):
    next_pos = (pos[0]+dir[0],pos[1]+dir[1])
    if(n[next_pos] == -1): return 0
    elif(n[next_pos] >= h): return 1
    else: return 1+get_visible_trees(n, h, next_pos, dir)

def part2(content, lines):
    m = []
    for line in lines:
        m.append([int(n) for n in line])
    n = numpy.full((len(m)+2,len(m[0])+2),-1)
    n[1:len(n)-1,1:len(n[0])-1] = m
    maxi = 0
    for i in range(1,len(n)-2):
        for j in range(1,len(n[0])-2):
            score = get_visible_trees(n,n[i,j],(i,j),(0,1))*\
                get_visible_trees(n,n[i,j],(i,j),(0,-1))*\
                get_visible_trees(n,n[i,j],(i,j),(1,0))*\
                get_visible_trees(n,n[i,j],(i,j),(-1,0))
            maxi = max(maxi, score)
    print(maxi)

def is_visible(m, pos, dir, max):
    if(pos == (2,2)):
        pass
    if m[pos][0] != -1:
        if m[pos][0] > max:
            max = m[pos][0]
            m[pos][1] = True
        is_visible(m,(pos[0]+dir[0],pos[1]+dir[1]),dir,max)
    
    
def part1(content, lines):
    m = []
    for line in lines:
        m.append([[int(n),False] for n in line])
    n = numpy.full((len(m)+2,len(m[0])+2,2),(-1,False))
    n[1:len(n)-1,1:len(n[0])-1] = m
    
    for i in range(1,len(n)-1):
        is_visible(n,(i,1),(0,1),-1)
        is_visible(n,(i,len(n)-2),(0,-1),-1)
    for j in range(1,len(n[0])-1):
        pass
        is_visible(n,(1,j),(1,0),-1)
        is_visible(n,(len(n)-2,j),(-1,0),-1)
    score = 0
    for i in range(1,len(n)-1):
        for j in range(1,len(n[0])-1):
            score+=n[i,j][1]
            print("\033[1;91m" if n[i,j][1] else "",end=f"{n[i,j][0]}\033[0m")
        print()
    print(score)

def one_line():
    pass

def main():
    import os 
    folder = os.path.dirname(os.path.realpath(__file__)).split("\\")[-1]
    file = open(f"{folder}\\input{'_test' if TESTING else ''}.txt",'r')
    content = file.read()
    lines = content.splitlines()
    
    part1(content, lines)
    # part2(content, lines)

if __name__ == "__main__":
    main()