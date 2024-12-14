TESTING = True

import numpy
from copy import deepcopy


def get_path(m,x,y):
    #sortie de boucle, anti boucle infinie
    if(m[x,y] < 0):
        return (False,0)

    #sortie de boucle victorieuse
    if(m[x,y] == 27):
        print("found end!!")
        return (True,0)
    
    #sorte de boucle
    m[x,y] *= -1

    mini = 1e10
    possible = False
    for xp,yp in [(x+1,y),(x-1,y),(x,y+1),(x,y-1)]:
        if(1 >= abs(m[xp, yp]) - abs(m[x, y]) >= 0):
            po, mi = get_path(deepcopy(m),xp,yp)
            if(po): mini = min(mini, mi)
            possible = possible or po
    return (possible,mini+1)

def part1(content, lines):
    m = [[ord(l)-96 for l in line.replace("S","a").replace("E","{")] for line in lines]
    
    m = numpy.pad(numpy.array(m),1,mode="constant",constant_values=99)

    print(m)

    print(get_path(m, 1, 1))


def main():
    import os 
    folder = os.path.dirname(os.path.realpath(__file__)).split("\\")[-1]
    file = open(f"{folder}\\input{'_test' if TESTING else ''}.txt",'r')
    content = file.read()
    lines = content.splitlines()
    
    part1(content, lines)

if __name__ == "__main__":
    main()