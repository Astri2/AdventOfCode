def my_pgcd(a,b ):
    if a%b == 0: return b
    if a < b: a,b=b,a
    while(b > 0):
        a%=b
        a,b=b,a
    return a

def my_lcm(*l):
    res = l[0]
    for i in range(1,len(l)):
        res = res*l[i]//my_pgcd(res,l[i])
    return res

f = open("day8/input.txt", "r")
lines = f.read().splitlines()

seq = lines[0]

nodes  = dict()
paths = list()

for line in lines[2:]:
    name, dest = line.split(" = ")
    l,r = dest[1:-1].split(", ")
    nodes[name] = (l,r)
    if(name[2] == 'A'): paths.append(name)

min_steps = set()
steps = 0

while True:
    for dir in seq:
        steps+=1
        i = 0
        while i < len(paths):
            paths[i] = nodes[paths[i]][0 if dir == 'L' else 1]
            if paths[i][2] == 'Z':
                min_steps.add(steps)
                paths.remove(paths[i])
                i-=1
            i+=1
        if(len(paths) == 0):
            print(min_steps)
            print(my_lcm(*min_steps))
            exit()