def differenciate(str1,str2):
    diff=[k for k in str1 if not(k in str2)]
    diff.extend([k for k in str2 if not(k in str1)])
    diff.sort
    return "".join(diff)

def get_key(dic,value):
    for k,v in dic.items():
        if sorted(str(v)) == sorted(str(value)):
            return k
    return -1

def get_keys(dic,vals):
    return [get_key(dic,val) for val in vals]

def contains_multiple_el(patern,els):
    for el in els:
       if not(el in patern):
           return False
    return True 

def in_common(str1,str2):
    return "".join([c for c in str1 if c in str2])

if __name__=="__main__":
    f = open("AdventOfCode2021\\D8\\input.txt")
    lines = [line.split(" | ") for line in f.read().splitlines()]

    sum = 0
    for line in lines:
        values = line[1].split(" ")
        paterns = line[0].split(" ")
        letter_pos = {"a":-1,"b":-1,"c":-1,"d":-1,"e":-1,"f":-1,"g":-1,}
        patern_nb = {i:"" for i in range(10)}

        #find 1 4 7 8 patern
        i = 0
        while(i < len(paterns)):
            if len(paterns[i]) == 2 : 
                patern_nb[1]=paterns[i]
                paterns.remove(patern_nb[1])
                i-=1
            elif len(paterns[i]) == 3 : 
                patern_nb[7]=paterns[i]
                paterns.remove(patern_nb[7])
                i-=1
            elif len(paterns[i]) == 7 : 
                patern_nb[8]=paterns[i]
                paterns.remove(patern_nb[8])
                i-=1
            elif len(paterns[i]) == 4 : 
                patern_nb[4]=paterns[i]
                paterns.remove(patern_nb[4])
                i-=1
            i+=1
        
        #find top (t) letter
        letter_pos[differenciate(patern_nb[1],patern_nb[7])] = "t"
        #find 3 patern
        patern_nb[3] = [patern for patern in paterns 
            if len(patern) == 5 and contains_multiple_el(patern,patern_nb[7])][0]
        paterns.remove(patern_nb[3])
        #find middle (m) letter
        letter_pos[differenciate(patern_nb[1],in_common(patern_nb[3],patern_nb[4]))] = "m"
        #find top left (tl) letter
        letter_pos[differenciate(patern_nb[4],patern_nb[1]+get_key(letter_pos,"m"))] = "tl"        
        #find 5 patern
        patern_nb[5] = [patern for patern in paterns
            if len(patern) == 5 
            and contains_multiple_el(patern,get_keys(letter_pos,["t","tl","m"]))][0]
        paterns.remove(patern_nb[5])
        #find 2 patern
        patern_nb[2] = [patern for patern in paterns if len(patern) == 5][0]
        paterns.remove(patern_nb[2])
        #find 0 patern
        patern_nb[0] = [patern for patern in paterns if len(patern) == 6
            and not(get_key(letter_pos,"m") in patern)][0]
        paterns.remove(patern_nb[0])
        #find top right (tr) letter
        letter_pos[in_common(patern_nb[1],patern_nb[2])] = "tr"        
        #find 9 patern
        patern_nb[9] = [patern for patern in paterns if get_key(letter_pos,"tr") in patern][0]
        paterns.remove(patern_nb[9])
        #find 6 patern
        patern_nb[6] = paterns[0]
        paterns.remove(patern_nb[6])
        
        number = 0
        for value in values:
            number = number*10 + get_key(patern_nb,value)
        sum+=number
    print(sum)


        

