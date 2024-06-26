"""
This File contains the implementation of insertion of linked list elements at beginning
of a list and at end of a list
"""
class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

class Linkedlist:

    def __init__(self):
        self.head = None

    def insertAtStart(self,data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def insertAtEnd(self,data):
        last = self.head

        if self.head is None:
            self.head = Node(data)
            return

        while last.next:
            last = last.next

        last.next = Node(data)
    def display(self):
        temp = self.head
        while temp:
            print(temp.data, end = ' ')
            temp = temp.next

linked_list = Linkedlist()

# Inserting at start
linked_list.insertAtStart(1)
linked_list.insertAtStart(2)
linked_list.insertAtStart(3)
linked_list.insertAtStart(4)

# Inserting at End
linked_list.insertAtEnd(1)
linked_list.insertAtEnd(2)
linked_list.insertAtEnd(3)
linked_list.insertAtEnd(4)

# Displaying the Linked List
linked_list.display()