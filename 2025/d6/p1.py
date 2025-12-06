with open("d6/input.txt") as f:
    lines = f.read().splitlines()

operands = lines[-1].split()

expressions = [[0]*(len(lines)-1) for _ in range(len(operands))]
for i, line in enumerate(lines[:-1]):
    for j, number in enumerate(line.split()):
        expressions[j][i] = int(number)

res = 0
for expression, operand in zip(expressions, operands):
    if operand == '+':
        res += sum(expression)
    else:
        s = 1
        for nb in expression:
            s *= nb
        res +=s
print(res)
    
