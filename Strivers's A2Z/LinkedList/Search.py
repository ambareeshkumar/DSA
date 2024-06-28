class Node:
    def __init__(self, data):
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

        new_node = Node(data)
        last = self.head

        while last.next:
            last = last.next

        last.next = new_node

    def searchElement(self,target):

        temp = self.head
        while temp:

            if temp.data == target:
                return f'Element {target} Present in Linked List'
            temp = temp.next

        return f'Element {target} Not present in Linked list'

    def indexOf(self,element):

        current = self.head
        index = 0

        while current:

            if current.data == element:
                return f'Element {element} found at Linked list index {index}'

            current = current.next
            index += 1
    def display(self):

        temp = self.head

        while temp:
            print(temp.data, end = " ")
            temp = temp.next


llist = Linkedlist()

# Inserting to LinkedList
llist.insertAtStart(1)
llist.insertAtStart(2)
llist.insertAtEnd(1)
llist.insertAtEnd(2)

# Displaying the Linked List
llist.display()

# Search in Linked List
print()
print(llist.searchElement(5))

# Return Index of Element At Linked List
print()
print(llist.indexOf(2))