TESTING = False

def part2(content, lines):
    score = 0
    for i in range(0, len(lines), 3):
        letter=list(set(lines[i]).intersection(set(lines[i+1]).intersection(lines[i+2])))[0].swapcase()
        score+=ord(letter)-96 if letter.islower() else ord(letter)-38
    print(score)

    print(sum([ord(letter)-96 if letter.islower() else ord(letter)-38 for letter in [list(set(lines[i]).intersection(set(lines[i+1]).intersection(lines[i+2])))[0] for i in range(0,len(lines),3)]]))

def part1(content, lines):
    score = 0
    for line in lines:
        a, b = line[:len(line)//2], line[len(line)//2:]
        intersection = set(a).intersection(b)
        for letter in intersection:
            score+=ord(letter)-96 if letter.islower() else ord(letter)-38
    print(score)

    print(sum([[ord(letter)-96 if letter.islower() else ord(letter)-38 for letter in[list(set(a).intersection(b))[0] for a,b in [(line[:len(line)//2],line[len(line)//2:]) for line in lines]]]][0]))

if __name__ == "__main__":
    import os 
    folder = os.path.dirname(os.path.realpath(__file__)).split("\\")[-1]
    file = open(f"{folder}\\input{'_test' if TESTING else ''}.txt",'r')
    content = file.read()
    lines = content.splitlines()
    
    part1(content, lines)
    part2(content, lines)