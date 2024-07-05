"""
Given the head of a singly linked list, return the middle node of the linked list.

If there are two middle nodes, return the second middle node.

Example 1
Input: head = [1,2,3,4,5]
Output: [3,4,5]
Explanation: The middle node of the list is node 3.

Example 2
Input: head = [1,2,3,4,5,6]
Output: [4,5,6]
Explanation: Since the list has two middle nodes with values 3 and 4, we return the second one.


Constraints:

The number of nodes in the list is in the range [1, 100].
1 <= Node.val <= 100
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

    def returnMiddle(self,middle):

        start = self.head
        cnt = 0

        while start:
            cnt += 1
            if cnt > middle:
                return start.data

            start = start.next

    def length(self):
        temp = self.head
        total = 0
        while temp:
            total += 1
            temp = temp.next

        return total


    def display(self):
        temp = self.head
        length = 0
        while temp:
            length += 1
            print(temp.data, end = ' ')
            temp = temp.next

        return length


linked_list = Linkedlist()

# Inserting at start
linked_list.insertAtStart(3)
linked_list.insertAtStart(2)
linked_list.insertAtStart(1)

# Inserting at End
linked_list.insertAtEnd(4)
linked_list.insertAtEnd(5)
linked_list.insertAtEnd(6)

# Displaying the Linked List
# linked_list.display()

length = linked_list.length()
print(linked_list.returnMiddle(length // 2))