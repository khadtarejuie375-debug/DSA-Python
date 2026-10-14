# Singly Circular linkedlist  (append code is changed from here onwards) 
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
            new_node.next = self.head
        else:
            temp = self.head  #for traversing the list
            while(temp.next != self.head):
                temp = temp.next  
            temp.next = new_node #appending new_node
            new_node.next = self.head #last node next is copied back into head (bcoz of Circular linkedlist)

    def del_node(self,value):
      	temp = self.head
		if temp is None:
			print("List is empty ")
			return
      	prev = None      
      	if temp.data == value: #first node to delete  
			while(temp.next != self.head): #find last node
				temp = temp.next
			self.head = self.head.next
			temp.next = self.head			 
     	else:
			while(temp != self.head and temp.data != value):
          		prev = temp
          		temp = temp.next        
      			if temp == self.head:
        			print("Value is not there in the list")
        			return
      			temp.next = temp.next.next        

    def display(self):
        print()
        print("List elements :")
        temp = self.head
        while (True):
            print(temp.data ,end =" ")
            temp = temp.next
            if temp == self.head:
              break

list = LinkedList()
n1 = Node(10)
n2 = Node(20)
list.append(n1)
list.append(n2)
list.append(Node(40))
list.append(Node(50))
list.append(Node(60))
list.append(Node(70))
list.display()
list.del_node(30)
list.display()