# 3 minutes
# + 7h11 -> 7h33

TEST = False
import os
import numpy as np
with open(f"2024/{os.path.split(os.path.split(__file__)[0])[1]}/input{"_test" if TEST else ""}.txt") as f:
    lines = f.read().splitlines()

line = list(map(int, lines[0]))

arr = np.array([-1]*sum(line))

file = True
idx = 0
file_counter = 0
for c in line:
    if file:
        arr[idx:idx+c] = file_counter
        file = False
        file_counter+=1
    else:
        file = True
    idx +=c 

i = 0
j = len(arr)-1
while i < j:
    while arr[i] != -1: i+=1
    while arr[j] == -1: j-=1 
    arr[i], arr[j] = arr[j], arr[i]
arr[i], arr[j] = arr[j], arr[i]

res = 0
for idx, id in enumerate(arr.astype(int)):
    if id == -1: break
    res += (int)(idx*id)
print(res)
