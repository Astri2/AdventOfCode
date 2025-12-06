with open("d5/input.txt") as f:
    lines = f.read().splitlines()

ranges = []

i = 0
while True:
    line = lines[i] 
    i += 1
    if(line == ""): break

    ranges.append(tuple(map(int, line.split("-"))))

res = 0
for line in lines[i:]:
    id = int(line)

    for (begin, end) in ranges:
        if begin <= id and id <= end:
            res +=1
            break

print(res)