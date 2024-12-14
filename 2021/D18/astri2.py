from FishNumber import *

def get_magnitude(fish_nb):
    left,right = get_pair_from_here(fish_nb,0)
    if right == '[4,0]' and left == '9':
        print()
    
    if(left.nb.isdigit()): left_nb = int(left.nb)
    else: left_nb = int(get_magnitude(left))
    if(right.nb.isdigit()): right_nb = int(right.nb)
    else: right_nb = int(get_magnitude(right))

    return 3*left_nb+2*right_nb

def get_pair_from_here(fish_nb,index):
    nb = fish_nb.nb
    i = index
    depth=1
    str_nb,str_left,str_right="","",""
    while depth > 0:
        i+=1
        str_nb+=nb[i]
        if nb[i] == "[": depth+=1
        elif nb[i] == "]": depth-=1
        elif nb[i]=="," and depth==1:
            str_left=FishNumber(str_nb[:-1]) #no comas
            str_nb=""
    str_right = FishNumber(str_nb[:-1]) #no closing square bracket
    return str_left,str_right

def add_to_other_number(fish_nb,fish_nb_to_add,i,mode):
    nb = fish_nb.nb
    iteration=0
    exit_val=0
    if mode == "r":
        iteration = 1 ; exit_val = len(nb)
    elif mode == "l":
        iteration = -1 ; exit_val = -1
    else: print("UNKNOWN MODE!!!!") ; return -1
    
    i+=iteration ; k=0
    while(i != exit_val):
        #skip the 0
        if(nb[i].isdigit()):
            k=i
            while nb[k+iteration].isdigit(): 
                k+=iteration
            (i1,i2)=(i,k) if mode=="r" else (k,i)
            nb = nb[:i1]+str(int(fish_nb_to_add.nb)+int(nb[i1:i2+1]))+nb[i2+1:]
            break
        i+=iteration 
    fish_nb.nb = nb

def explode(fish_nb):
    nb = fish_nb.nb
    depth=0
    for i in range(len(nb)):
        if nb[i] == "[": depth+=1
        elif nb[i] == "]": depth-=1
        if depth == 5:
            left,right = get_pair_from_here(fish_nb,i)
            fish_nb.nb = nb[:i]+"0"+nb[i+len(left.nb+right.nb)+3:] #replace the pair by a 0
            add_to_other_number(fish_nb,right,i,mode="r")
            add_to_other_number(fish_nb,left,i,"l")
            return True
    return False

from math import floor,ceil
def split(fish_nb):
    nb = fish_nb.nb
    for i in range(len(nb)-1):
        if nb[i].isdigit() and nb[i+1].isdigit():
            val = int(nb[i]+nb[i+1])
            fish_nb.nb = nb[:i]+"["+str(floor(val/2)//1)+","+str(ceil(val/2)//1)+"]"+nb[i+2:]
            return True
    return False

def get_max_magnitude(numbers):
    magnitudes=[]
    for nb1 in numbers:
        for nb2 in numbers:
            nb = nb1+nb2
            while(explode(nb) or split(nb)): continue
            magnitudes.append(get_magnitude(nb))
    return max(magnitudes)

if __name__ == "__main__":
    f = open("AdventOfCode2021\\D18\\input.txt",'r')
    numbers = [FishNumber(nb) for nb in f.read().splitlines()]
    magn_max = get_max_magnitude(numbers)
    print(magn_max)
