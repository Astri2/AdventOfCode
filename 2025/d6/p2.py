with open("d6/input.txt") as f:
    lines = f.read().splitlines()

operands = lines[-1].split()

# parse expression without removing whitespaces
expressions = [[""]*(len(lines)-1) for _ in range(len(operands))]
operatorBegin = None
operatorEnd = None
operatorIdx = 0
for i, c in enumerate(lines[-1]):
    if c in "*+": 
        if operatorBegin == None:
            print("Begin: ", i)
            operatorBegin = i
        else:
            print("End: ", i)
            operatorEnd = i-1
            for j, line in enumerate(lines[:-1]):
                expressions[operatorIdx][j] = lines[j][operatorBegin:operatorEnd]
            operatorIdx += 1
            operatorBegin = i
            operatorEnd = None
for j, line in enumerate(lines[:-1]):
    expressions[operatorIdx][j] = lines[j][operatorBegin:]
# print(expressions)

# convert expression
for i, expression in enumerate(expressions):
    new_expr = [0] * len(expression[0])
    for char_id in range(len(expression[0])):
        for number in expression:
            if(number[char_id] == ' '): continue
            new_expr[char_id] = 10 * new_expr[char_id] + int(number[char_id])
    expressions[i] = new_expr
# print(expressions)


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
    
