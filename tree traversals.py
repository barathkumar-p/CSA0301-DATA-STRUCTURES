class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BinaryTree:
    def __init__(self, root):
        self.root = Node(root)

    def inorder_traversal(self, start, traversal):
        
        if start:
            traversal = self.inorder_traversal(start.left, traversal)
            traversal += (str(start.value) + "->")
            traversal = self.inorder_traversal(start.right, traversal)
        return traversal

    def preorder_traversal(self, start, traversal):
       
        if start:
            traversal += (str(start.value) + "->")
            traversal = self.preorder_traversal(start.left, traversal)
            traversal = self.preorder_traversal(start.right, traversal)
        return traversal

    def postorder_traversal(self, start, traversal):
       
        if start:
            traversal = self.postorder_traversal(start.left, traversal)
            traversal = self.postorder_traversal(start.right, traversal)
            traversal += (str(start.value) + "->")
        return traversal

    def print_tree(self, traversal_type):
        if traversal_type == "preorder":
            return self.preorder_traversal(tree.root, "")
        elif traversal_type == "inorder":
            return self.inorder_traversal(tree.root, "")
        elif traversal_type == "postorder":
            return self.postorder_traversal(tree.root, "")
        else:
            print("Traversal type " + str(traversal_type) + " is not supported.")
            return False

# Create a binary tree
tree = BinaryTree(1)
tree.root.left = Node(2)
tree.root.right = Node(3)
tree.root.left.left = Node(4)
tree.root.left.right = Node(5)
tree.root.right.left = Node(6)
tree.root.right.right = Node(7)

print("In-Order Traversal:", tree.print_tree("inorder"))
print("Pre-Order Traversal:", tree.print_tree("preorder"))
print("Post-Order Traversal:", tree.print_tree("postorder"))
