TESTING = False

def run(content, lines):
    print(sum([[scores[line.replace(" ","")] for line in lines] for scores in [{"AX":4,"AY":8,"AZ":3,"BX":1,"BY":5,"BZ":9,"CX":7,"CY":2,"CZ":6}]][0]))
    
    print(sum([[scores[line.replace(" ","")] for line in lines] for scores in [{"AX":3,"AY":4,"AZ":8,"BX":1,"BY":5,"BZ":9,"CX":2,"CY":6,"CZ":7}]][0]))

if __name__ == "__main__":
    import os 
    folder = os.path.dirname(os.path.realpath(__file__)).split("\\")[-1]
    file = open(f"{folder}\\input{'_test' if TESTING else ''}.txt",'r')
    content = file.read()
    lines = content.splitlines()
    
    # run(content, lines)

print(sum([[scores[line.replace(" ","")] for line in open("D2\input.txt").read().splitlines()] for scores in [{"AX":3,"AY":4,"AZ":8,"BX":1,"BY":5,"BZ":9,"CX":2,"CY":6,"CZ":7}]][0]))