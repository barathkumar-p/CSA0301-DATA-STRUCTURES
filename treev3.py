class Node:
    def __init__(self,value):
        self.value=value
        self.left=None
        self.right=None

class Binarytree:
    def __init__(self,root):
        self.root=Node(root)

    def inordertraversal(self,start,Traversal):
        if start:
            Traversal=self.inordertraversal(start.left,Traversal)
            Traversal = Traversal + (str(start.value) + "->")
            Traversal=self.inordertraversal(start.right,Traversal)
        return Traversal

    def preordertraversal(self,start,Traversal):
        if start:
            Traversal = Traversal + (str(start.value) + "->")
            Traversal=self.preordertraversal(start.left,Traversal)
            Traversal=self.preordertraversal(start.right,Traversal)      

    def postordertraversal(self,start,Traversal):
        if start:
            Traversal=self.postordertraversal(start.left,Traversal)
            Traversal=self.postordertraversal(start.right,Traversal)
            Traversal= Traversal +(str(start.value) + "->") 

    def PrintTree(self,TraversalType):
        if TraversalType=="Inorder":
            return self.inordertraversal(tree.root,"")
        elif TraversalType=="Preorder":
            return self.preordertraversal(tree.root,"")
        elif TraversalType=="Postorder":
            return self.postordertraversal(tree.root,"")
        else:
            return "Invalid!"

tree = Binarytree(1)
tree.root.left = Node(2)
tree.root.right = Node(3)
tree.root.left.left = Node(4)
tree.root.left.right = Node(5)
tree.root.right.left = Node(6)
tree.root.right.right = Node(7)

print("inorder:",tree.PrintTree("inorder"))
print("preorder:",tree.PrintTree("Preorder"))
print("postorder:",tree.PrintTree("postorder"))