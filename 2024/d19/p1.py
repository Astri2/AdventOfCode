TEST = False
import os
from functools import lru_cache
with open(f"2024/{os.path.split(os.path.split(__file__)[0])[1]}/input{"_test" if TEST else ""}.txt") as f:
    lines = f.read().splitlines()

available = lines[0].split(", ")

@lru_cache
def is_possible(towel):
    if towel == "": return True
    
    for i in range(1,len(towel)+1):
        if towel[:i] in available and is_possible(towel[i:]):
            return True
    
    return False    

res = 0
for towel in lines[2:]:
    res += is_possible(towel)
print(res)