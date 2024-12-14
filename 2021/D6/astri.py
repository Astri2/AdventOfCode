import matplotlib.pyplot as plt

def make_dic(tab):
    dict = {k:0 for k in range(9)}
    for fish in tab:
        dict[fish]+=1
    return dict

def get_fish_number(dict):
    return sum(dict.values())

def calculate_population(dict,days):
    population=[get_fish_number(dict)]
    print("initial state:",get_fish_number(dict),dict)
    for k in range(1,days+1):
        fish_reproduce=0
        for i in range (len(dict)):
            if(i==0):
                fish_reproduce=dict[0]
            else:
                dict[i-1]=dict[i]
        dict[8]=fish_reproduce
        dict[6]+=fish_reproduce
        print("Day",k," : ",get_fish_number(dict),dict)
        population.append(get_fish_number(dict))
    plt.plot(list(range(days+1)),population)
    plt.show()


def main():
    file = open("AdventOfCode2021\\D6\\input.txt",'r')
    tab = [int(k) for k in file.read().split(",")]
    print(tab)
    calculate_population(make_dic(tab),256)
    
if __name__ == "__main__":
    main()