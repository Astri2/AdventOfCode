TEST = True
import os
with open(f"2024/{os.path.split(os.path.split(__file__)[0])[1]}/input{"_test" if TEST else ""}.txt") as f:
    lines = f.read().splitlines()

locks = []
keys = []
for i in range(0, len(lines), 8):
    combin = [0]*5
    for i_ in range(i+1, i+6):
        for d in range(5):
            combin[d] += lines[i_][d] == "#"
    if lines[i][0] == "#":
        locks.append(combin)
    else: keys.append(combin)
    
def fits(lock, key):
    for i in range(5):
        if lock[i] + key[i] > 5: return False
    return True
    
res = 0
for lock in locks:
    for key in keys:
        res += fits(lock, key)
        
print(res)