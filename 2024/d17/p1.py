TEST = False
import os
with open(f"2024/{os.path.split(os.path.split(__file__)[0])[1]}/input{"_test" if TEST else ""}.txt") as f:
    lines = f.read().splitlines()


registers = []

registers.append(int(lines[0].split()[2]))
registers.append(int(lines[1].split()[2]))
registers.append(int(lines[2].split()[2]))

prog = list(map(int, lines[4].split()[1].split(",")))

"""
Combo operands 0 through 3 represent literal values 0 through 3.
Combo operand 4 represents the value of register A.
Combo operand 5 represents the value of register B.
Combo operand 6 represents the value of register C.
Combo operand 7 is reserved and will not appear in valid programs.
"""
def combo(v):
    if v < 0: raise Exception
    if v < 4: return v
    return registers[v-4]
    
i = 0
res = []
while i < len(prog):
    match prog[i]:
        case 0:
            registers[0] = registers[0] // (2**(combo(prog[i+1])))
            i+=2
        case 1:
            registers[1] = registers[1] ^ prog[i+1]
            i+=2
        case 2:
            registers[1] = combo(prog[i+1]) % 8
            i+=2
        case 3:
            if registers[0] == 0:
                i+=2
                continue
            i = prog[i+1]
        case 4:
            registers[1] = registers[1] ^ registers[2]
            i+=2
        case 5:
            res.append(combo(prog[i+1]) % 8)
            i+=2
        case 6:
            registers[1] = registers[0] // (2**(combo(prog[i+1])))
            i+=2
        case 7:
            registers[2] = registers[0] // (2**(combo(prog[i+1])))
            i+=2
        case _: raise Exception
    print(end="")

print(*res, sep=",")