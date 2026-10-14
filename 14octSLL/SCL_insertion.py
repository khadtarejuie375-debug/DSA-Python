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

    # Insertion operations : 
    def insert(self, new_node, pos):
        if pos == 1:     # inserting node at first position
            temp = self.head
            while(temp.next != self.head): #find last node
              temp = temp.next
            new_node.next = self.head
            self.head = new_node
            return
        else:       #inserting from 2nd to last position
            p = 1
            temp = self.head
            while(p != pos-1):
                temp = temp.next
                p+=1
            new_node.next = temp.next
            temp.next = new_node
            return


    def display(self):
        temp = self.head
        while temp:
            print(temp.data)
            temp = temp.next

list = LinkedList()
n1 = Node(10)
n2 = Node(20)
list.append(n1)
list.append(n2)
list.append(Node(40))
list.append(Node(50))
list.display()
list.insert(Node(38),4)
list.display()