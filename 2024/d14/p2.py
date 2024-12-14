TEST = False
import os
with open(f"2024/{os.path.split(os.path.split(__file__)[0])[1]}/input{"_test" if TEST else ""}.txt") as f:
    lines = f.read().splitlines()

if TEST:
    h,w = 7, 11
else: h,w = 103, 101
max_iteration = 10000

robots = []
for line in lines:
    p, v = line.split()
    j,i = map(int,p.split("=")[1].split(","))
    dj,di = map(int,v.split("=")[1].split(","))
    robots.append((i,j,di,dj))

import numpy as np
from PIL import Image
import os.path
def save(robots, iteration):
    if TEST: return
    if not os.path.isfile(f"2024/d14/imgs{'_test' if TEST else ''}/{iteration}.png"):
        im = np.zeros((h,w))
        for robot in robots:
            i,j,_,_ = robot
            im[i][j] = 255
        new_im = Image.fromarray(im)
        new_im = new_im.convert("L")
        new_im.save(f"2024/d14/imgs{'_test' if TEST else ''}/{iteration}.png")

def compute_res(robots):
    q1, q2, q3, q4 = 0, 0, 0, 0
    for robot in robots:
        i,j,_,_ = robot
        if i < h//2:
            if j < w//2:
                q1+=1
            elif j > w//2: q2+=1
        elif i > h//2:
            if j < w//2:
                q3+=1
            elif j > w//2: q4+=1
    
    print(q1 * q2 * q3 * q4)

for iteration in range(max_iteration):
    for idx in range(len(robots)):
        i,j,di,dj = robots[idx]

        i += di
        j += dj

        while i < 0: i+=h
        while j < 0: j+=w
        while i >= h: i-=h
        while j >= w: j-=w
        robots[idx] = (i,j,di,dj)
    if 6353 <= iteration <= 6355:
        save(robots, iteration)
compute_res(robots)