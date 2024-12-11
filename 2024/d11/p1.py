# 9h01->9h50

TEST = True
import os
from math import log10, pow
with open(f"2024/{os.path.split(os.path.split(__file__)[0])[1]}/input{"_test" if TEST else ""}.txt") as f:
    lines = f.read().splitlines()


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

size = 0
head = None
node = None
for s in lines[0].split()[::-1]:
    size+=1
    if node == None:
        head = Node(int(s))
        node = head
    else:
        next_node = Node(int(s))
        node.next = next_node
        node = next_node
        
n=25
m=0
for i in range(n):
    print(f"{i+1}/{n}",end="")
    
    node: Node = head
    while(node != None):
        m = max(m, node.data)
        if node.data == 0:
            node.data = 1
        elif (len := (int)(log10(node.data)) + 1) % 2 == 0:
            div = pow(10,len//2)
            new_node: Node = Node(node.data%div)
            node.data = node.data//div
            new_node.next = node.next
            node.next = new_node
            size+=1
            
            node = node.next
        else:
            node.data = node.data*2024
        node = node.next
    print("->" + str(size), end="\r")
print()
print(size)