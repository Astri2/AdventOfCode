f = open("day8/input.txt", "r")
lines = f.read().splitlines()

seq = lines[0]

nodes  = dict()
starts = set()

for line in lines[2:]:
    name, dest = line.split(" = ")
    l,r = dest[1:-1].split(", ")
    nodes[name] = (l,r)

steps = 0
current = 'AAA'
while True:
    for dir in seq:
        steps+=1
        current = nodes[current][0 if dir == 'L' else 1]
        if current == 'ZZZ':
            print(steps)
            exit()