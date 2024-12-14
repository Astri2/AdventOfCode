TESTING = False

def line_based(content, lines):
    X = [1]
    i = 1
    s = ""
    for line in lines:
        X.append(X[-1])
        s+= "█" if X[-1]-1 <= (i-1)%40 <= X[-1]+1 else " "
        i+=1
        if line != "noop":
            s+= "█" if X[-1]-1 <= (i-1)%40 <= X[-1]+1 else " "
            X.append((X[-1]+int(line.split()[1])))
            i+=1
    
    print(sum([i*X[i-1] for i in [20, 60, 100, 140, 180, 220]]))
    print(*[s[i*40:(i+1)*40] for i in range(len(s)//40)],sep="\n")

def main():
    import os 
    folder = os.path.dirname(os.path.realpath(__file__)).split("\\")[-1]
    file = open(f"{folder}\\input{'_test' if TESTING else ''}.txt",'r')
    content = file.read()
    lines = content.splitlines()
    
    line_based(content, lines)

if __name__ == "__main__":
    main()