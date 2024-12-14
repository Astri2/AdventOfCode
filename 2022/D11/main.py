TESTING = False
PART = 2
class Monkey:

    MODULO = 1

    def __init__(self, lines):
        self.id = int(lines[0][-2])

        self.items = [int(n.replace(",","")) for n in lines[1].split()[2:]][::-1]

        self.factor = lines[2].split()[-1]
        self.factor = int(self.factor) if self.factor.isnumeric() else None
        if "+" in lines[2]:
            self.operation = lambda old: old + int(old if self.factor is None else self.factor)
        else:
            self.operation = lambda old: old * int(old if self.factor is None else self.factor)
       
        self.mod = int(lines[3].split()[-1])
        self.test = (lambda x: x % self.mod == 0)
        self.results = (int(lines[5].split()[-1]), int(lines[4].split()[-1]))

        Monkey.MODULO*=self.mod

        self.traded_items = 0

def part2(content, lines):
    pass

def part1(content, lines):
    roundNumber = (20 if PART == 1 else 10000)
    monkeys: list[Monkey] = []
    for i in range((len(lines)+1)//7):
        monkeys.append(Monkey(lines[i*7:i*7+7]))
    
    for r in range(roundNumber):
        print(r)
        for monkey in monkeys:
            while len(monkey.items) != 0:
                item = monkey.items.pop()
                item = monkey.operation(item)
                if PART == 1:
                    item//=3
                elif PART == 2:
                    item %= Monkey.MODULO
                monkey.traded_items+=1
                if monkey.test(item):
                    monkeys[monkey.results[1]].items.insert(0,item)
                else:
                    monkeys[monkey.results[0]].items.insert(0,item)  
                
    res = sorted([monkey.traded_items for monkey in monkeys])
    print(res[-1]*res[-2])

def main():
    import os 
    folder = os.path.dirname(os.path.realpath(__file__)).split("\\")[-1]
    file = open(f"{folder}\\input{'_test' if TESTING else ''}.txt",'r')
    content = file.read()
    lines = content.splitlines()
    
    part1(content, lines)
    part2(content, lines)

if __name__ == "__main__":
    main()        

