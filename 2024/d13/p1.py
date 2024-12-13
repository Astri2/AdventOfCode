# 7h45 -> 8h06
# 8h06 -> 

TEST = False
import os
with open(f"2024/{os.path.split(os.path.split(__file__)[0])[1]}/input{"_test" if TEST else ""}.txt") as f:
    lines = f.read().splitlines()

res = 0
for i in range(0, len(lines), 4):
    lineA = lines[i].split()
    lineB = lines[i+1].split()
    lineRes = lines[i+2].split()

    xA = int(lineA[2][1:-1])
    yA = int(lineA[3][1:])
    xB = int(lineB[2][1:-1])
    yB = int(lineB[3][1:])
    xRes = int(lineRes[1][2:-1])
    yRes = int(lineRes[2][2:])

    solutions = []
    for a in range(100):
        for b in range(100):
            if xA * a + xB * b == xRes and yA * a + yB * b == yRes:
                solutions.append(3*a+b)
    
    # solutions.sort(key= lambda x: 3*x[0] + x[1])
    solutions.sort()

    if(solutions):
        # print(solutions[0])
        res += solutions[0]
    # else: print("no sol")
print(res)