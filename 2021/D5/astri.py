from math import pow

def print_matrix(matrix):
    str_matrix=""
    for line in matrix:
        for value in line:
            str_matrix+= (str(value) if value != 0 else ".")
        str_matrix+="\n"
    print(str_matrix+"====")
    return str_matrix

def get_matrix(input,size):
    matrix = [list([0]*size) for __ in range(size)]
    for line in input:
        x1 = int(line[0][0])
        y1 = int(line[0][1])
        x2 = int(line[1][0])
        y2 = int(line[1][1])
        matrix[y1][x1] += 1
        while(not(x1 == x2 and y1 == y2)):
            x1+=int(pow(-1,x1>x2))*(x1!=x2) #x1 ++ or -- towards x2 IF x1!=x2
            y1+=int(pow(-1,y1>y2))*(y1!=y2)
            matrix[y1][x1] += 1
    print_matrix(matrix)
    counter=0
    for line in matrix:
        for value in line:
            if value >= 2:
                counter+=1
    print(counter)


def main():
    file = open("AdventOfCode2021\\D5\\input.txt",'r')
    lines = [k.replace("\n","") for k in file.readlines()]
    inputs=[]
    for line in lines:
        inputs.append([])
        subs = line.split(" -> ")
        for sub in subs:
            inputs[-1].append(sub.split(","))
    get_matrix(inputs,991)
    
if __name__ == "__main__":
    main()