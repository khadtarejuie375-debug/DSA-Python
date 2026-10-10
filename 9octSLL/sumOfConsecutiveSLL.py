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

    #sum of consecutive nodes
    def sum_Of_Consecutive(self):
      temp = self.head

      while temp and temp.next:
        print(temp.data + temp.next.data)
        temp = temp.next

    def display(self):
        temp = self.head
        while temp:
            print(temp.data)
            temp = temp.next  

list = LinkedList()
n1 = Node(10)
n2 = Node(20)
n3 = Node(30)
list.append(n1)
list.append(n2)
list.append(n3)
list.append(Node(48))
list.append(Node(55))
list.display()
print("Sum of consecutive nodes :")
list.sum_Of_Consecutive()