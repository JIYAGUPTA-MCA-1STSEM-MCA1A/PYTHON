Write a Python program to display a BST using In-order, Pre-order, Post-order. 

class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None

class BST:
    def __init__(self):
        self.root = None
    
    def insert(self, key):
        new_node = Node(key)
        if self.root is None:
            self.root = new_node
            return
        
        current = self.root
        while True:
            if key < current.key:
                if current.left is None:
                    current.left = new_node
                    return
                current = current.left
            else:
                if current.right is None:
                    current.right = new_node
                    return
                current = current.right
    
    def inorder_traversal(self, node):
        if node:
            self.inorder_traversal(node.left)
            print(node.key, end=' ')
            self.inorder_traversal(node.right)
    
    def preorder_traversal(self, node):
        if node:
            print(node.key, end=' ')
            self.preorder_traversal(node.left)
            self.preorder_traversal(node.right)
    
    def postorder_traversal(self, node):
        if node:
            self.postorder_traversal(node.left)
            self.postorder_traversal(node.right)
            print(node.key, end=' ')
    
    def display(self):
        print("In-order Traversal:")
        self.inorder_traversal(self.root)
        print("\nPre-order Traversal:")
        self.preorder_traversal(self.root)
        print("\nPost-order Traversal:")
        self.postorder_traversal(self.root)
        print()

# Main function to process user input
if __name__ == "__main__":
    bst = BST()
    numbers = list(map(int, input("Enter a set of integers separated by spaces: ").split()))
    
    for num in numbers:
        bst.insert(num)
    
    bst.display()

                    
