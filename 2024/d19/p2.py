TEST = False
import os
from functools import lru_cache
with open(f"2024/{os.path.split(os.path.split(__file__)[0])[1]}/input{"_test" if TEST else ""}.txt") as f:
    lines = f.read().splitlines()

available = lines[0].split(", ")

@lru_cache
def is_possible(towel):  
    if towel == "":
        return 1
    
    res = 0
    for i in range(1,len(towel)+1):
        if towel[:i] in available:
            r = is_possible(towel[i:])
            res+= r
            
    return res    

final_res = 0
for i, towel in enumerate(lines[2:]):
    print(f"\r{i}/{len(lines)-2}")
    final_res += is_possible(towel)
print(final_res)
