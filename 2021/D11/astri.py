from copy import deepcopy

def flash(matrice,x,y) -> int: #returns nb of new flashes
    if matrice[x][y][0] >= 10:
        matrice[x][y] = [0,True]
        xmax = len(matrice)-1
        ymax = len(matrice[x])-1
        flashes=0
        for j in range(-1+(x==0),2-(x==xmax),1):
            for k in range(-1+(y==0),2-(y==ymax),1):
                if(j!=0 or k!=0):
                    if(matrice[x+j][y+k][1] == False):
                        matrice[x+j][y+k][0]+=1
                        flashes+=flash(matrice,x+j,y+k)
        return 1+flashes
    else: return 0

def printmatrice(matrice):
    disp=[]
    for line in matrice:
        disp.append("")
        for value in line:
            disp[-1]+=str(value[0]) + " " + (" " if value[0] < 10 else "")
    return disp

from copy import deepcopy
import numpy as np
from PIL import Image

gradient = {
    0:[0,0,0],
    1:[45,31,0],
    2:[51,53,0],
    3:[65,75,0],
    4:[85,99,0],
    5:[110,123,0],
    6:[137,148,0],
    7:[166,174,0],
    8:[195,200,0],
    9:[225,227,0],
    10:[255,255,0]
}

def day11(lines):
    matrice = deepcopy(lines)
    w,h = len(matrice),len(matrice[0]) 
    nb_fish = w*h
    flashes=0 ; i = 0 ; simultaneously = False
    images = []
    while(not(simultaneously)):
        i+=1
        old_flashes=flashes
        matrice = [[[k[0]+1,False] for k in line] for line in matrice] #gain +1 energy for each
        for x in range(w):
            for y in range(h):
                flashes+=flash(matrice,x,y)

        if(old_flashes+nb_fish==flashes): #part2, flash simultaneously
            simultaneously=True
        
        data = np.zeros((h, w, 3), dtype=np.uint8) #init the object data
        for x in range(w):
            for y in range(h):
                pixel = matrice[x][y]
                data[x][y]=gradient[pixel[0]] if not(pixel[1]) else gradient[10]
        img = Image.fromarray(data, 'RGB') #convert into image
        img.save("AdventOfCode2021\\D11\\export\\frame_"+str(i)+".png")
        images.append(img)
    images[0].save("AdventOfCode2021\\D11\\flashes_animation.gif",append_images=images,save_all=True,duration=100,loop=1)
    print("day",str(i))
    print(flashes)

if __name__ == "__main__":
    f = open("AdventOfCode2021\\D11\\input.txt")
    matrice = [[[int(k),False] for k in line] for line in f.read().splitlines()]
    day11(matrice)