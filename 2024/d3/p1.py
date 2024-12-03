with open("d3/in.txt") as f:
    lines = f.read().splitlines()


import re

p = re.compile(r"mul\(([0-9]+),([0-9]+)\)")

res = 0
for line in lines:
    for match in p.finditer(line):
        res += int(match.group(1))*int(match.group(2))
print(res)
# 7 minutes