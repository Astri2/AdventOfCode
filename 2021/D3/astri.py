from math import *
def str_b_to_int(str):
    nb=0
    for k in range(len(str)):
        nb+=pow(2,len(str)-1-k)*int(str[k])
    return nb

def get_most_common_bit(tab,i,default):
    zero=0
    one=0
    for k in tab:
        if(k[i] == "0"): zero+=1
        else: one+=1
    if(one == zero): return default
    if(zero > one): return "0"
    else: return "1"

def part1(lines):
    gamma=""
    epsilon=""
    for i in range(len(lines[0])):
       bit = get_most_common_bit(lines,i,"0")
       gamma+=bit
       epsilon+="0" if bit == "1" else "1"
    return str_b_to_int(gamma)*str_b_to_int(epsilon)
  

def part2(lines):
    ox_tab = list(lines)
    co_tab = list(lines)
    for i in range(len(lines[0])):
        k=0
        ox_bit = get_most_common_bit(ox_tab,i,"1")
        while(k < len(ox_tab) and len(ox_tab)>1):
            if(ox_tab[k][i] != ox_bit):
                ox_tab.remove(ox_tab[k])
                k-=1
            k+=1
        k=0
        co_bit = "1" if get_most_common_bit(co_tab,i,"1") == "0" else "0"
        while(k < len(co_tab) and len(co_tab)>1):
            if(co_tab[k][i] != co_bit):
                co_tab.remove(co_tab[k])
                k-=1
            k+=1
    return str_b_to_int(co_tab[0])*str_b_to_int(ox_tab[0])
            
def main():
    file = open("AdventOfCode2021\\D2\\input.txt",'r')
    lines = [k.replace("\n","") for k in file.readlines()]
    print(part1(lines))
    print(part2(lines))
    
if __name__ == "__main__":
    main()