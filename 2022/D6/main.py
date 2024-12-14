TESTING = False

def get_header(content,N):
    for i in range(N-1,len(content)):
        if(len(set(content[i-N+1:i+1]))) == N:
            return i+1
            
def one_line():
    [[print([n+N for n,s in enumerate([set(content[i-N+1:i+1]) for i in range(N-1,len(content))]) if len(s)==N][0]) for content in [open(f"D6\\input{'_test' if TESTING else ''}.txt",'r').read()]] for N in [14]]

def part2(content, lines):
    print(get_header(content,14))

def part1(content, lines):
    print(get_header(content,4))


def main():
    import os 
    folder = os.path.dirname(os.path.realpath(__file__)).split("\\")[-1]
    file = open(f"{folder}\\input{'_test' if TESTING else ''}.txt",'r')
    content = file.read()
    lines = content.splitlines()
    
    # part1(content, lines)
    # part2(content, lines)
    one_line()

if __name__ == "__main__":
    main()