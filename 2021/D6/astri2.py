import matplotlib.pyplot as plt

def make_tab(tab):
    return [len([fish for fish in tab if fish == i]) for i in range(9)]

def calculate_population(tab,days):
    population=[sum(tab)]
    for __ in range(1,days+1):
        fish_reproduce=tab[0]
        tab = [tab[i+1] for i in range(8)]
        tab[6]+=fish_reproduce
        tab.append(fish_reproduce)
        population.append(sum(tab))
    print("fishes after",days,"days:",population[-1])
    plt.plot(list(range(days+1)),population)
    plt.show()

def main():
    file = open("AdventOfCode2021\\D6\\input.txt",'r')
    tab = [int(k) for k in file.read().split(",")]
    calculate_population(make_tab(tab),256)
    
if __name__ == "__main__":
    main()