TESTING = True

def part2(content, lines):
    pass

def part1(content, lines):
    pass

def one_line():
    pass

def main():
    import os 
    folder = os.path.dirname(os.path.realpath(__file__)).split("\\")[-1]
    file = open(f"{folder}\\input{'_test' if TESTING else ''}.txt",'r')
    content = file.read()
    lines = content.splitlines()
    
    part1(content, lines)
    part2(content, lines)
    one_line()

if __name__ == "__main__":
    main()