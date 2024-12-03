with open("d3/in.txt") as f:
    lines = f.read().splitlines()


import re

p = re.compile(r"(?:mul\(([0-9]+),([0-9]+)\)|do\(\)|don't\(\))")


res = 0
enable = True
for line in lines:
    for match in p.finditer(line):
        s = match.group(0)
        if s == "do()":
            enable = True
        elif s == "don't()":
            enable = False
        else:
            if enable:
                res += int(match.group(1))*int(match.group(2))
print(res)
# +3 minutes