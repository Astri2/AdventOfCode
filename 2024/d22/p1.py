TEST = False
import os
with open(f"2024/{os.path.split(os.path.split(__file__)[0])[1]}/input{"_test" if TEST else ""}.txt") as f:
    lines = f.read().splitlines()

def mix(secret, val):
    return secret ^ val
def prune(secret):
    return secret % 16777216

t = [0]

def next_secret(secret):
    t[0]+=1
    secret = prune(mix(secret, secret * 64))
    secret = prune(mix(secret, secret // 32))
    secret = prune(mix(secret, secret * 2048))
    return secret
    
res = 0
for line in lines:
    secret = int(line)
    for _ in range(2000):
        secret = next_secret(secret)
    res += secret
print(res)