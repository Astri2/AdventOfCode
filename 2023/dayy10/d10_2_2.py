import re

f = open("dayy10/cleared.txt",'r')
r = f.read()
if("S" in r):
    print("Please replace S with correct symbol first!")
    exit()
lines = r.splitlines()
f.close()

def setCharAt(s, i, c):
    return s[:i] + c + s[i+1:]

def expand_vert():
    for i in range(len(lines)-1, 0, -1):
        lines.insert(i, ','*len(lines[i]))
        for j in range(len(lines[i])):
            if lines[i+1][j] in "|LJ":
                lines[i] = setCharAt(lines[i],j,'|')

def expand_hor():
    for i in range(len(lines)):
        line = lines[i]
        line = re.sub(r"([\-7J])",r"-\1", line)
        line = re.sub(r"([,\.\|LF])", r",\1", line)
        lines[i] = line

def expand():
    expand_vert()
    expand_hor()

expand()

with open("dayy10/expanded.txt",'w') as f:
    print(*lines,sep="\n", file=f)