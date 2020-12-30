import random

"""
Creating Linked List with classes and methods. 
"""


class Node:
    def __init__(self, data=None, next=None):  # Node class, holds piece of data and next element
        self.data = data
        self.next = next

    def print_node(self):  # Function to help print node information
        print(self.data)


class LinkedList:
    def __init__(self):  # Keep track of list's head
        self.head = None

    def append_node(self, data):  # Method to append objects to the list.
        if not self.head:  # First node is added as the head
            self.head = Node(data)
            return
        else:
            current = self.head  # Elements afterwards are appended to head using next
            while current.next:
                current = current.next
            current.next = Node(data)

    def print_list(self):
        node = self.head  # Print list, use node.next to encounter next object
        while node is not None:
            print(node.data, end="<-->")
            node = node.next

    def search(self, target):
        current = self.head
        while current is not None:  # While we have not reached end of list
            if current.data == target:  # If data we look at is our target, we found it
                print("Found")
                return True
            else:
                current = current.next  # Data we looked at is not target, assign current node to next node, loop
        print("Not found")
        return False


a_list = LinkedList()
for i in range(10):
    j = random.randint(1, 20)
    a_list.append_node(j)
a_list.print_list()

# Searching is done via linear search. We reach end when current.next = None.
