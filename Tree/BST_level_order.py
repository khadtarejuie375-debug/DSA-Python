# 26 nov 2026
# - level order traversal  : printing level wise

class Node:
    def __init__(self, value):
        self.left=None
        self.data=value
        self.right=None
class BST:
    def __init__(self):
        self.root=None
        # self.cnt = 0


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

    # level order traversal : BFS(Breadth First Search)
    def level_order(self, rt):
        if rt is None:
            print("BST is empty")
            return
        arr = []
        count = 0    #for counting visited node
        level = 0
        arr.append(rt)
        while count < len(arr):
            
            node_count = len(arr) - count    #no of nodes to be visited
            print("\n Level",level, "nodes:", end=" ")
            for i in range(node_count):

                temp = arr[count]
                count += 1
                print(temp.data, end=" ")
                if temp.left:
                    arr.append(temp.left)
                if temp.right:
                    arr.append(temp.right)
            level += 1
        print("\nHeight of the tree: ", level-1)


    # delete node
    def deleteNode(self, rt, val):
        if rt is None:
            return 
        if val < rt.data:
            rt.left = self.deleteNode(rt.left, val)
        elif val > rt.data:
            rt.right = self.deleteNode(rt.right, val)
        else:
            if rt.left is None:    #node with right child only
                return rt.right
            if rt.right is None:    #node with left child only
                return rt.left
            # node has both left and right children
            successor = self.get_successor(rt)
            rt.data = successor.data
            rt.right = self.deleteNode(rt.right, successor.data)
        return rt


    def get_successor(self, temp):
        temp = temp.right
        while temp.left is not None: 
            temp = temp.left
        return temp
    

    # search for a node
    def serachNode(self, key):
        temp = self.root
        while temp:
            if temp.data == key:
                return True
            elif key < temp.data:
                temp = temp.left
            else:
                temp = temp.right
        return False
    

    def inorder(self, rt):
        if rt is None:
            return
        else:
            self.inorder(rt.left)
            print(rt.data, end=" ")
            if rt.left is not None or rt.right is not None:
                # self.cnt+=1
                self.inorder(rt.right)


    def preorder(self, rt):
        if rt is None:
            return
        else:
            print(rt.data, end=" ")
            self.preorder(rt.left)
            self.preorder(rt.right)


    def postorder(self, rt):
        if rt is None:
            return
        else:
            self.postorder(rt.left)
            self.postorder(rt.right)
            print(rt.data, end=" ")


    def findminmax(self):
        temp=self.root
        while temp.left:
            temp=temp.left
        print("\nMin: ", temp.data)
        temp=self.root
        while temp.right:
            temp=temp.right
        print("\nMax: ", temp.data)
   
b1=BST()
b1.insert(Node(100))
b1.insert(Node(10))
b1.insert(Node(450))
b1.insert(Node(4))
b1.insert(Node(65))
b1.insert(Node(300))
b1.insert(Node(500))
b1.insert(Node(50))
b1.insert(Node(70))
print("\nInorder: ")
b1.inorder(b1.root)

if b1.serachNode(450):
    print("\n Found!")
else:
    print("\n Not found!")

print("Level order traversal")
b1.level_order(b1.root)