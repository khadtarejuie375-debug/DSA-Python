#BST using Linked List
class Node:
    def __init__(self, value):
        self.left=None
        self.data=value
        self.right=None
class BST:
    def __init__(self):
        self.root=None
       
    def insert(self, new_node):
        if self.root is None: ##BST is empty
            self.root=new_node
        else:
            temp=self.root
            while True:
                if new_node.data<temp.data: #left subtree
                    if temp.left is None:
                        temp.left=new_node
                        return
                    else:
                        temp=temp.left
                else: #right subree
                    if temp.right is None:
                        temp.right=new_node
                        return
                    else:
                        temp=temp.right
    def del_node(self, rt ,val):
        if rt is None:
            return rt
        if val<rt.data:
            rt.left=self.del_node(rt.left, val)
        elif val>rt.data:
            rt.right = self.del_node(rt.right ,val)
        else:
            if rt.left is None: #node with right child only
                return rt.right
            if rt.right is None: #node with left child only
                return rt.left
            # node has both left & right children
            succ =self.get_successor(rt)
            rt.data = succ.data
            rt.right = self.del_node(rt.right , succ.data)
        return rt

    def get_successor(self , temp):
        temp = temp.right
        while temp.left is not None:
            temp = temp.left
        return temp 

    def inorder(self, rt):
        if rt is None:
            return
        else:
            self.inorder(rt.left)
            print(rt.data, end=" ")
            self.inorder(rt.right)
    
b1=BST()
b1.insert(Node(100))
b1.insert(Node(10))
b1.insert(Node(450))
b1.insert(Node(0))
b1.insert(Node(65))
b1.insert(Node(300))
print("\nInorder: ")
b1.inorder(b1.root)
b1.del_node(b1.root,65)
print("\n After deletion :" ,end = "")
b1.inorder(b1.root)