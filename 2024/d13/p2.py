# 7h45 -> 8h06 p1
# 8h06 -> 8h10
# 12h22 -> 12h33
TEST = False
import os
with open(f"2024/{os.path.split(os.path.split(__file__)[0])[1]}/input{"_test" if TEST else ""}.txt") as f:
    lines = f.read().splitlines()

res = 0
for i in range(0, len(lines), 4):
    lineA = lines[i].split()
    lineB = lines[i+1].split()
    lineRes = lines[i+2].split()

    x1 = int(lineA[2][1:-1])
    y1 = int(lineA[3][1:])
    x2 = int(lineB[2][1:-1])
    y2 = int(lineB[3][1:])
    x = int(lineRes[1][2:-1]) + 10000000000000
    y = int(lineRes[2][2:]) + 10000000000000

    if x1 / y1 == x2 / y2 == x / y:
        print("pas indé!")

    b = (x - y*x1/y1) / (x2-y2*x1/y1)
    a = (x - b*x2) / x1

    a = round(a, 3)
    b = round(b, 3)
    if(a == round(a) and b == round(b)):
        res += 3*a+b

print(res)