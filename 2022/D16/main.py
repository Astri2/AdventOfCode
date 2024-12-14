TESTING = True

def part1(content, lines):
    print("la calotte de ses morts")

def main():
    import os 
    folder = os.path.dirname(os.path.realpath(__file__)).split("\\")[-1]
    file = open(f"{folder}\\input{'_test' if TESTING else ''}.txt",'r')
    content = file.read()
    lines = content.splitlines()
    
    part1(content, lines)


if __name__ == "__main__":
    main()