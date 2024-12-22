TEST = False
import os
from itertools import product
from functools import lru_cache
from joblib import Parallel, delayed
import time

with open(f"2024/{os.path.split(os.path.split(__file__)[0])[1]}/input{"_test" if TEST else ""}.txt") as f:
    lines = f.read().splitlines()

def mix(secret, val):
    return secret ^ val
def prune(secret):
    return secret % 16777216

t = [0]

@lru_cache
def next_secret(secret):
    t[0]+=1
    secret = prune(mix(secret, secret * 64))
    secret = prune(mix(secret, secret // 32))
    secret = prune(mix(secret, secret * 2048))
    return secret

deltas = []
bananas = []

# gen all deltas
for line in lines:
    secret = int(line)
    deltas.append([None]*2001)
    bananas.append([None]*2001)
    bananas[-1][0] = secret%10
    for i in range(2000):
        s = next_secret(secret)
        bananas[-1][i+1] = s%10
        deltas[-1][i+1] = bananas[-1][i+1] - bananas[-1][i]
        secret = s

def fct(i,seq):
    r = 0
    if(i % 1000 == 0): print("multiple of 1000!")
    for b, d in zip(bananas, deltas):
        for i in range(len(b)):
            if d[i] == seq[0] and i < len(b)-3:
                if d[i+1] == seq[1] and d[i+2] == seq[2] and d[i+3] == seq[3]:
                    r += b[i+3]
                    break
    return r

t = time.time()
gen = product(range(-9,10), repeat=4)
results = Parallel(n_jobs=8)(delayed(fct)(i,seq) for i,seq in enumerate(gen))
res = max(results)
print()
print(res)
print(time.time()-t)