import re

part2: bool = True
p = r"(?=([0-9]|zero|one|two|three|four|five|six|seven|eight|nine))" if part2 else r"[0-9]"

f = open("t.txt",'r')
s = 0
lines = f.read().splitlines()
for line in lines:
    digits = re.findall(p, line)
    c1 = digits[0]
    c2 = digits[-1]
    if( not c1.isnumeric()):
        c1 = map[c1]
    if( not c2.isnumeric()):
        c2 = map[c2]
    s += int(c1+c2)
print(s)

# print(sum([[(int("".join([c if c.isnumeric() else map[c] for c in [digits[0], digits[-1]]]))) for digits in [re.findall(p, line)]][0] for re in [__import__("re")] for part1 in [True] for test in [False] for p in [r"(?=([0-9]|zero|one|two|three|four|five|six|seven|eight|nine))" if part1 else r"[0-9]"] for f in [open(f"day1/input{('_test1' if part1 else '_test2') if test else ''}.txt")] for map in [{"one":"1","two":"2","three":"3","four":"4","five":"5","six":"6","seven":"7","eight":"8", "nine":"9"}] for line in f.read().splitlines()]))