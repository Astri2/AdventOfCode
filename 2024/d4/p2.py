TEST = False
import os
with open(f"2024/{os.path.split(os.path.split(__file__)[0])[1]}/input{"_test" if TEST else ""}.txt") as f:
    lines = f.read().splitlines()
    
r = 0

for i in range(1, len(lines)-1):
    for j in range(1, len(lines[0])-1):
        if lines[i][j] == 'A':
            if lines[i-1][j-1] == "M" and lines[i-1][j+1] == "M" and\
               lines[i+1][j-1] == "S" and lines[i+1][j+1] == "S":
                r+=1
            if lines[i-1][j-1] == "S" and lines[i-1][j+1] == "M" and\
               lines[i+1][j-1] == "S" and lines[i+1][j+1] == "M":
                r+=1
            if lines[i-1][j-1] == "M" and lines[i-1][j+1] == "S" and\
               lines[i+1][j-1] == "M" and lines[i+1][j+1] == "S":
                r+=1
            if lines[i-1][j-1] == "S" and lines[i-1][j+1] == "S" and\
               lines[i+1][j-1] == "M" and lines[i+1][j+1] == "M":
                r+=1
print(r)