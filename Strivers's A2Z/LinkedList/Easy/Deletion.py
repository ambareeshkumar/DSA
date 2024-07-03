class Node:

    def __init__(self,data):
        self.data = data
        self.next = None

class LinkedList:

    def __init__(self):
        self.head = None

    def insertAtStart(self,data):

        if self.head == None:
            self.head = Node(data)
            return
        else:
            new_node = Node(data)
            new_node.next = self.head
            self.head = new_node

    def insertAtEnd(self,data):

        new_node = Node(data)
        last = self.head

        if self.head == None:
            self.head = new_node
            return

        while last.next:
            last = last.next
        last.next = new_node

    def deleteAtStart(self):

        if self.head == None:
            return 'Linked List is empty'
        else:
            self.head = self.head.next

    def deleteAtEnd(self):

        last = self.head
        if self.head == None:
            return "Linked List is Empty"
        if self.head.next == None:
            self.head = None
            return
        while last.next.next != None:
            last = last.next
        last.next = None

    def deleteAtSpecificElement(self,data):
        current = self.head
        prev = None
        if current.data != None and current.data == data:
            self.head = self.head.next
            return f'Deleted the Element {data} from Linked List'

        while current:
            if current.data == data:
                break
            prev = current
            current = current.next

        if not current:
            return f'Element {data} not found in Linked List'

        prev.next = current.next
        return f'Deleted the Element {data} from Linked List'

    def display(self):

        temp = self.head
        while temp:
            print(temp.data, end = ' ')

            temp = temp.next


llist = LinkedList()

# Inserting at Start
llist.insertAtStart(1)
llist.insertAtStart(2)
llist.insertAtStart(3)

# Inserting at End
llist.insertAtEnd(1)
llist.insertAtEnd(2)
llist.insertAtEnd(3)

#Displaying the Linked List
print('Displaying before deletion At Start')
llist.display()

print()
print('Displaying After Deletion At Start')
llist.deleteAtStart()
llist.display()


# Deletion At end
llist.deleteAtEnd()
print()
print("Displaying After Deletion At End")
llist.display()

# Deletion At Specific position
print()
print("Deletion at specific position")
llist.display()
print()
print("Display After Deletion At Specific position")
print(llist.deleteAtSpecificPosition(2))
llist.display()

