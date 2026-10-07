# 06 October 2026
# Singly Linked List

class Node:
    def __init__(self,val):
        self.data = val
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, new_node):
        if (self.head == None):
            self.head = new_node
        else:
            temp = self.head
            while(temp.next):
                temp = temp.next  
            temp.next = new_node #appending new_node

    def display(self):
        temp = self.head
        while temp:
            print(temp.data)
            temp = temp.next    
                            
    # WAP to count number of nodes in the Linked List:
    def count_nodes(self):
        count = 0
        temp = self.head
        while temp:
            count = count + 1
            temp = temp.next
        print(count)

    # WAP to count sum of all node values in the Linked List:
    def sum_nodes(self):
        total = 0
        temp = self.head

        while temp:
            total = total + temp.data
            temp = temp.next
        print(total)

    # WAP TO display sum of only positive node values in the Linked List
    def positive_sum(self):
        total = 0
        temp = self.head
        while temp:
            if temp.data > 0:
                total = total + temp.data
            temp = temp.next
        print(total)

    # WAP to display sum of only negative node values in the Linked list
    def negative_sum(self):
        total = 0
        temp = self.head

        while temp:
            if temp.data < 0:
                total = total + temp.data
            temp = temp.next
        print(total)

    # WAP to display alternate values in the Linked List
    def display_alternate(self):
        temp = self.head
        while temp:
            print(temp.data)
            if temp.next:
                temp = temp.next.next
            else:
                temp = None


list = LinkedList()
n1 = Node(10)
n2 = Node(20)
n3 = Node(30)
n4 = Node(-35)
list.append(n1)
list.append(n2)
list.append(n3)
list.append(n4)
list.append(Node(40))

print("Linked List: ")
list.display()

print("number of nodes: ")
list.count_nodes()

print("Sum of all nodes: ")
list.sum_nodes()

print("Sum of positive nodes: ")
list.positive_sum()

print("Sum of negative nodes: ")
list.negative_sum()

print("alternate nodes: ")
list.display_alternate()