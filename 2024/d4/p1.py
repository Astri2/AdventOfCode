TEST = False
import os
with open(f"{os.path.split(os.path.split(__file__)[0])[1]}/input{"_test" if TEST else ""}.txt") as f:
    lines = f.read().splitlines()
    
r = 0

# HOR
for i,line in enumerate(lines):
    for j in range(len(lines[0])-3):
        if line[j] == "X" and line[j+1] == "M" and line[j+2] == "A" and line[j+3] == "S":
            r +=1
            # print(i,j)
        if line[-1-j] == "X" and line[-2-j] == "M" and line[-3-j] == "A" and line[-4-j] == "S":
            r+=1
            # print(i,-j)
# print(r); print()

# VERT
for j in range(len(lines[0])):
    for i in range(len(lines)-3):
        if lines[i][j] == "X" and lines[i+1][j] == "M" and lines[i+2][j] == "A" and lines[i+3][j] == "S":
            r+=1
            # print(i,j)
        if lines[-1-i][j] == "X" and lines[-2-i][j] == "M" and lines[-3-i][j] == "A" and lines[-4-i][j] == "S":
            r+=1
            # print(-i,j)
# print(r); print()

# DIAG \
for j in range(len(lines[0])-3):
    for i in range(len(lines)-3):
        if lines[i][j] == "X" and lines[i+1][j+1] == "M" and lines[i+2][j+2] == "A" and lines[i+3][j+3] == "S":
            r+=1
            # print(i,j)
        if lines[-1-i][-1-j] == "X" and lines[-2-i][-2-j] == "M" and lines[-3-i][-3-j] == "A" and lines[-4-i][-4-j] == "S":
            r+=1
            # print(-i,-j)
# print(r); print()

# DIAG / 
for j in range(len(lines[0])-3):
    for i in range(len(lines)-3):
        if lines[i][-1-j] == "X" and lines[i+1][-2-j] == "M" and lines[i+2][-3-j] == "A" and lines[i+3][-4-j] == "S":
            r+=1
            # print(i,-j)
        if lines[-1-i][j] == "X" and lines[-2-i][j+1] == "M" and lines[-3-i][j+2] == "A" and lines[-4-i][j+3] == "S":
            r+=1
            # print(-i,j)
print(r)