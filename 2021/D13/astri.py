import numpy as np
from PIL import Image

def init_matrice_and_instructions(lines):
    i=0
    matrice = [[0]*1311 for __ in range(895)] #hardcoded
    while lines[i] != '':
        val1,val2=lines[i].split(",")
        matrice[int(val2)][int(val1)]=1
        i+=1
    i+=1 #skip empty line
    instructions=[]
    while i < len(lines):
        instructions.append(lines[i].split(" ")[2].split("="))
        i+=1
    return matrice,instructions



def fold(matrice,instructions):
    for instruction in instructions:
        slice = int(instruction[1])
        if instruction[0] == "x":
            matrice = matrice[:,:slice]+np.flip(matrice[:,slice+1:],1)
        else:
            matrice = matrice[:slice,:]+np.flip(matrice[slice+1:,:],0) # il faut flip celui du bas quand on le replie
   
    dots=0
    w,h=len(matrice), len(matrice[0])
    data = np.zeros((w, h, 3), dtype=np.uint8)
    for x in range(w):
        for y in range(h):
            print("\033[0;37;41m" if matrice[x][y] else "\033[1;30;40m"," ",end="")
            if matrice[x][y] : data[x][y] = [(255//w)*x,(255//h)*y,255-(255//w)*x]
        print()
    img = Image.fromarray(data, 'RGB') #convert into image
    img.save("AdventOfCode2021\\D13\\code.png")

if __name__ == "__main__":
    lines = open("AdventOfCode2021\\D13\\input.txt").read().splitlines()
    matrice, instructions = init_matrice_and_instructions(lines)
    fold(np.asarray(matrice),instructions)