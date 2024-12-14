def get_result(dic):
    vals = dic.values()
    return max(vals)-min(vals)

def dic_add(dic,k,v):
    if k in dic.keys():
        dic[k]+=v
    else:
        dic[k]=v

def process(template,possible_pairs):
    letters={}
    pairs={}
    for c in template: dic_add(letters,c,1)
    for i in range(len(template)-1): dic_add(pairs,template[i]+template[i+1],1)

    for i in range(40):
        old_pairs = pairs.copy()
        for pair in old_pairs.keys():
            if pair in possible_pairs:
                nb_pair=old_pairs[pair]
                pairs[pair]-=nb_pair
                letter = possible_pairs[pair]
                dic_add(letters,possible_pairs[pair],nb_pair)
                pair1 = pair[0]+letter ; pair2 = letter+pair[1]
                dic_add(pairs,pair1,nb_pair)
                dic_add(pairs,pair2,nb_pair)
    print(get_result(letters))

def parse_input():
    f = open("AdventOfCode2021\\D14\\input.txt")
    lines = f.read().splitlines()
    template = lines[0]
    pairs={}
    for i in range(2,len(lines)):
        k,v = lines[i].split(" -> ")
        pairs[k]=v
    return template,pairs
    

if __name__ == "__main__":
    template,pairs = parse_input()
    process(template,pairs)