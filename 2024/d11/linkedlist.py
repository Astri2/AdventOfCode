# Create a Node class to create a node
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

# Create a LinkedList class
class LinkedList:
    def __init__(self):
        self.head = None
        self.size = 0

    # Method to add a node at the beginning of the LL
    def insertAtBegin(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node
        self.size+=1


    # Update node at a given position
    
    # Print the size of the linked list
    def sizeOfLL(self):
        
        return self.size

    # Print the linked list
    def printLL(self):
        current_node = self.head
        while current_node:
            print(current_node.data, end= ", ")
            current_node = current_node.next
        print()
