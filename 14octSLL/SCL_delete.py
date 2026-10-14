class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, new_node):
        if self.head is None:
            self.head = new_node
            new_node.next = self.head
        else:
            temp = self.head

            while temp.next != self.head:
                temp = temp.next

            temp.next = new_node
            new_node.next = self.head

    def insert(self, new_node, pos):
        if self.head is None:
            self.head = new_node
            new_node.next = self.head
            return

        if pos == 1:
            temp = self.head

            while temp.next != self.head:
                temp = temp.next
            new_node.next = self.head
            self.head = new_node
            temp.next = self.head
            return
        temp = self.head

        for i in range(pos - 2):
            temp = temp.next
            if temp.next == self.head:
                break
        new_node.next = temp.next
        temp.next = new_node

    def del_node(self, value):
        if self.head is None:
            print("List is empty")
            return
        temp = self.head
        prev = None

        # Deleting the first node
        if temp.data == value:
            if temp.next == self.head:
                self.head = None
                return
            while temp.next != self.head:
                temp = temp.next
            temp.next = self.head.next
            self.head = self.head.next
            return
        # Searching for the node
        temp = self.head

        while(temp.next != self.head and temp.next.data != value):
            temp = temp.next
        if temp.next == self.head:
            print("Value is not present in the list")
            return
        temp.next = temp.next.next

    def display(self):
        if self.head is None:
            print("List is empty")
            return

        temp = self.head

        while True:
            print(temp.data, end=" ")
            temp = temp.next

            if temp == self.head:
                break

        print()


# Creating linked list
llist = LinkedList()

n1 = Node(10)
n2 = Node(20)

llist.append(n1)
llist.append(n2)
llist.append(Node(40))
llist.append(Node(50))

print("Original list:")
llist.display()

print("After insertion:")
llist.insert(Node(38), 4)
llist.display()

print("After deletion:")
llist.del_node(10)
llist.display()