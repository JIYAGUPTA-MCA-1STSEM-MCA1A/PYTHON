Write a Python program to create a binary search tree using recursive function and display that. 

class Node:
  
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None

class BST:
    def __init__(self):
        self.root = None
    
    def insert(self, root, key):
        if root is None:
            return Node(key)
        if key < root.key:
            root.left = self.insert(root.left, key)
        else:
            root.right = self.insert(root.right, key)
        return root
    
    def inorder_traversal(self, root):
        if root:
            self.inorder_traversal(root.left)
            print(root.key, end=' ')
            self.inorder_traversal(root.right)
    
    def insert_key(self, key):
        self.root = self.insert(self.root, key)
    
    def display(self):
        print("Inorder Traversal of BST:")
        self.inorder_traversal(self.root)
        print()

# Main function to test BST
if __name__ == "__main__":
    bst = BST()
    keys = [50, 30, 70, 20, 40, 60, 80]
    
    for key in keys:
        bst.insert_key(key)
    
    bst.display()
