from functools import wraps

def memoize(func):
    cache = {}

    @wraps(func)
    def wrapper(*args, **kwargs):
        key = str(args) + str(kwargs)

        if key not in cache:
            cache[key] = func(*args, **kwargs)

        return cache[key]
    return wrapper

with open("dayy12/input.txt") as f:
    lines = f.read().splitlines()
lines = [[a, list(map(int,b.split(',')))] for line in lines for a,b in [line.split()]]

@memoize
def explore(record, nbs):
    l_record = len(record)
    l_nb = len(nbs)
    
    # conditions de sortie
    if(l_record == 0):
        return l_nb == 0

    # on skip les points
    if(record[0] == '.'):
        return explore(record[1:], nbs)
    # on skip ou traite commme une diese les iconnus
    if(record[0] == '?'):
        # le premier revient a mettre un point, mais on évite de faire une récursion inutile
        return explore(record[1:], nbs) + explore("#" + record[1:], nbs)
    
    # on a une diese:

    # s'il n'y a plus de groupe ou qu'on a plus de place pour le groupe suivant
    if l_nb == 0 or nbs[0] > l_record:
        return 0
    # si il y a un point au milieu du groupe suivant
    if '.' in record[:nbs[0]]:
        return 0
    
    # # s'il y a une diese juste apres le groupe
    if(l_record > nbs[0] and record[nbs[0]] == '#'):
        return 0
    return explore(record[nbs[0]+1:], nbs[1:])
    
    

        
res = 0
for line in lines:
    record = "?".join(5*[line[0]])
    nbs = 5*line[1]
    n = explore(record, nbs)
    res+=n
print(res)