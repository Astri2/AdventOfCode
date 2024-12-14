TESTING = False


def get_elves(content) -> list[list[str]]:
    return [[int(food) for food in k.split("\n")] for k in content.split("\n\n")]

def run(content, lines):
    elves = get_elves(content)
    calories = [sum(elf) for elf in elves]

    print(max(calories))
    print(sum(sorted(calories,reverse=True)[0:3]))

if __name__ == "__main__":
    import os 
    folder = os.path.dirname(os.path.realpath(__file__)).split("\\")[-1]
    file = open(f"{folder}\\input{'_test' if TESTING else ''}.txt",'r')
    content = file.read()
    lines = file.readlines()
    
    run(content, lines)

print(sum(sorted([sum([int(n) for n in elf]) for elf in [k.split("\n") for k in open("D1\\input.txt","r").read().split("\n\n")]], reverse=True)[:3]))
