#concatenate two lists
class Node:
    def __init__(self,val):
        self.data=val
        self.next=None
class LinkedList:
    def __init__(self):
        self.head=None
    def append(self, new_node):
        if (self.head==None):
            self.head=new_node
        else:
            temp=self.head
            while(temp.next):
                temp=temp.next
            temp.next=new_node   #appending new node

    def concatenate(self):
        temp=self.head
        while(temp.next):
            temp=temp.next
        temp.next=list2.head


    def print(self):
        temp=self.head
        while temp :
            print(temp.data)
            temp=temp.next

list=LinkedList()
list2=LinkedList()
n1=Node(10)
n2=Node(20)
n3=Node(30)
list.append(n1)
list.append(n2)
list.append(n3)
list.append(Node(40))
list.print()
list2.append(Node(11))
list2.append(Node(22))
list2.append(Node(33))
list2.append(Node(44))
list2.append(Node(55))
list.concatenate()
list2.print()