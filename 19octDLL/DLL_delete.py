# 19 Oct 2026
# Doubly Linked List Delete Operation
# Count occurrence of a number in DLL

class Node:
    def __init__(self, val):
        self.data = val
        self.next = None
        self.prev = None


class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, new_node):
        if self.head == None:
            self.head = new_node
        else:
            temp = self.head

            while temp.next:
                temp = temp.next

            temp.next = new_node
            new_node.prev = temp

    def delete(self, value):
        temp = self.head

        while temp and temp.data != value:
            temp = temp.next

        if temp == None:
            print("Node value is not present in the list")
            return

        # deleting first node
        if temp.prev == None:
            self.head = temp.next

            if self.head:
                self.head.prev = None

        # deleting middle or last node
        else:
            temp.prev.next = temp.next

            if temp.next:
                temp.next.prev = temp.prev

    # count occurrence of a number
    def count_occurrence(self, num):
        count = 0
        current = self.head

        while current:
            if current.data == num:
                count += 1

            current = current.next

        return count

    # Write a function to SWAP first and last nodes in DLL with all pointer values also:
    def swap(self):
        node1 = self.head
        temp = self.head
        if node1 == None or node1.next == None:
            return
        while temp.next:
            temp = temp.next
        # Save important nodes
        node2 = node1.next
        prev_last = temp.prev
        # Last node becomes first
        self.head = temp
        temp.prev = None
        temp.next = node2
        node2.prev = temp
        # First node becomes last
        prev_last.next = node1
        node1.prev = prev_last
        node1.next = None


    def display(self):
        temp = self.head

        while temp:
            print(temp.data)
            temp = temp.next




list = LinkedList()

list.append(Node(10))
list.append(Node(20))
list.append(Node(30))
list.append(Node(-35))
list.append(Node(40))
list.append(Node(10))

print("Linked List:")
list.display()

list.delete(40)

print("After deleting 40:")
list.display()

print("Occurrence of 10:")
print(list.count_occurrence(10))