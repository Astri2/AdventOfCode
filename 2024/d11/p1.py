# 9h01->9h50

TEST = False
import os
from linkedlist import *
from math import log10, pow
with open(f"2024/{os.path.split(os.path.split(__file__)[0])[1]}/input{"_test" if TEST else ""}.txt") as f:
    lines = f.read().splitlines()


stones: LinkedList = LinkedList()
for s in lines[0].split()[::-1]:
    stones.insertAtBegin(int(s))

n=75
m=0
for i in range(n):
    print(f"{i+1}/{n}",end="")
    # stones.printLL()
    
    node: Node = stones.head
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
            stones.size+=1
            
            # i+=1
            node = node.next
        else:
            node.data = node.data*2024
        # i+=1
        node = node.next
    print("->" + str(stones.size), "max:", m, end="\r")
print()
print(stones.size)