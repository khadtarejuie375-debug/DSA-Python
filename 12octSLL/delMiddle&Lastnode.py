#find and delete middle node, delete first and last node
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

    def findmid_del(self):
        temp=temp1=self.head
        prev=None
        while temp1 and temp1.next:
            prev=temp
            temp=temp.next
            temp1=temp1.next.next
        print("Middle Node:",temp.data)
        prev.next=temp.next
        temp=None

    def delfirst_last(self):
        temp1=self.head
        temp1=None
        prev=None
        temp=self.head=self.head.next
        while(temp.next):
            prev=temp
            temp=temp.next
        prev.next=None
        temp=None

    def del_alternate(self):
        prev=self.head
        temp=self.head.next
        while prev and temp:
            prev.next=temp.next
            temp=None
            prev=prev.next
            if prev:
                temp=prev.next


    def print(self):
        temp=self.head
        while temp :
            print(temp.data)
            temp=temp.next

list=LinkedList()
n1=Node(10)
n2=Node(20)
n3=Node(30)
list.append(n1)
list.append(n2)
list.append(n3)
list.append(Node(40))
#list.findmid_del()
#list.delfirst_last()
list.del_alternate()
list.print()
