from math import *

def calculate_fuel_needed(pos,goal):
    diff = abs(pos-goal)
    return diff*(diff+1)/2

def part1(tab):
    mini=inf
    for i in range(max(tab)):
        mini=min(mini,sum([calculate_fuel_needed(crab,i) for crab in tab]))
    print(mini)

def main():
    file = open("AdventOfCode2021\\D7\\input.txt",'r')
    tab = [int(k) for k in file.read().split(",")]
    part1(tab)
    
if __name__ == "__main__":
    main()