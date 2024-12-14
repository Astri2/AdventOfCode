TESTING = False

import numpy
import sys
from PIL import Image
sys.setrecursionlimit(10000)

def generate_img(m, path: list[tuple]):
    data = numpy.zeros((*numpy.shape(m), 3), dtype=numpy.uint8) #init the object data

    for i in range(len(m)):
        for j in range(len(m[i])):
            data[i, j] = 3*[(m[i, j]-1) * 10]
    for tile in path:
        data[tile][0] = 255
    img = Image.fromarray(data, 'RGB') #convert into image
    img.save("D12\\heightmap.png") #save the image

def get_path(m, w, i, j, s, obj, path):
    
    if(not(w[i,j] is None) and s >= w[i,j]):
        return (False, [])
    
    w[i, j] = s

    if((i,j) == obj):
        # print("found end at distance", w[i, j])
        return (True, path)

    mini = 1e10
    p_returned = []
    possible = False
    for ip,jp in [(i+1,j),(i-1,j),(i,j+1),(i,j-1)]:
        if(1 >= abs(m[ip, jp]) - abs(m[i, j])):
            po, p = get_path(m,w,ip,jp, s+1, obj, path+[(ip,jp)])
            if po: p_returned = p
            possible = possible or po
    return (possible,p_returned)

def part1(content, lines):
    start = None
    finish = None
    for i in range(len(lines)):
        for j in range(len(lines[i])):
            index_s = lines[i].find("S")
            if index_s != -1:
                start = (i+1, index_s+1)
            index_e = lines[i].find("E")
            if index_e != -1:
                finish = (i+1, index_e+1)
    
    m = [[ord(c)-96 for c in line] for line in content.replace('S','a').replace('E','z').splitlines()]

    m = numpy.pad(numpy.array(m),1,mode="constant",constant_values=99)
    weigths = numpy.full(numpy.shape(m), None)

    possible, path = get_path(m, weigths, *(start), 0, finish, [start])
    if possible:

        print("dist:",weigths[finish])
        print(path)
    else: 
        print("couldn't find path")
    generate_img(m, path)

def part2(content, lines):
    a_counter=  0
    finish = None
    for i in range(len(lines)):
        for j in range(len(lines[i])):
            index_e = lines[i].find("E")
            if index_e != -1:
                finish = (i+1, index_e+1)
    
    m = [[ord(c)-96 for c in line] for line in content.replace('S','a').replace('E','z').splitlines()]

    m = numpy.pad(numpy.array(m),1,mode="constant",constant_values=99)
    weigths = numpy.full(numpy.shape(m), None)


    mini = 1e100
    for i in range(1,len(m)-1):
        for j in range(1,len(m[i])-1):
            if(m[i,j] == 1):
                a_counter+=1
                print(a_counter)
                weigths = numpy.full(numpy.shape(m), None)
                possible, _ = get_path(m, weigths, i, j, 0, finish, [(i,j)])
                if possible:
                    mini = min(mini,weigths[finish])
    print(mini)

def main():
    import os 
    folder = os.path.dirname(os.path.realpath(__file__)).split("\\")[-1]
    file = open(f"{folder}\\input{'_test' if TESTING else ''}.txt",'r')
    content = file.read()
    lines = content.splitlines()
    
    part1(content, lines)
    # part2(content, lines)


if __name__ == "__main__":
    main()