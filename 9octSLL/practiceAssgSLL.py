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
            new_node.next = self.head
            self.head = new_node
            return
        else:
            p = 1
            temp = self.head
            while(p != pos-1):
                temp = temp.next
                p+=1
            new_node.next = temp.next
            temp.next = new_node
            return

    # finding middle node 
    def middle(self):
      temp1 = self.head
      temp2 = self.head

      while temp2 and temp2.next:
        temp1 = temp1.next
        temp2 = temp2.next.next

      if temp1:
        print("Middle node :",temp1.data)
      else:
        print("Linked list is empty")

    # deleting node
    def del_node(self,value):
      temp = self.head
      prev = None
      #deleting first node
      if temp.data == value:   #searching
        self.head = self.head.next
        return
      while(temp):
        if temp.data == value:
          break
        else:     #traverse 
          prev = temp
          temp = temp.next        
      if temp == None:
        print("Value is not there in the list")
        return
      prev.next = temp.next
      temp = None

    #reversing a SSL:
    def reverse(self):
      curr = self.head
      prev = None
      while(curr):
        nextnode = curr.next
        curr.next = prev
        prev = curr
        curr = nextnode
      self.head = prev
    
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
list.append(Node(40))
list.append(Node(50))
list.display()
print("inserting node at 1st position")
list.insert(Node(05),1)
list.display()
list.insert(Node(15),6)
list.display()
list.middle()
list.del_node(30)
list.display()
list.reverse()
print("Sum of consecutive nodes :")
list.sum_Of_Consecutive()
