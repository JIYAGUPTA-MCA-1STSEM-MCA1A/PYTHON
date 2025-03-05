Write a Python program to insert (by using a function) a specific element into an existing binary  search tree and then display that. 
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
    
    def inorder_traversal(self):
        stack = []
        current = self.root
        while True:
            if current is not None:
                stack.append(current)
                current = current.left
            elif stack:
                current = stack.pop()
                print(current.key, end=' ')
                current = current.right
            else:
                break
        print()
    
    def insert_and_display(self, key):
        print(f"Inserting {key} into BST...")
        self.insert(key)
        self.display()
    
    def display(self):
        print("Inorder Traversal of BST:")
        self.inorder_traversal()

# Main function to test BST
if __name__ == "__main__":
    bst = BST()
    keys = [50, 30, 70, 20, 40, 60, 80]
    
    for key in keys:
        bst.insert(key)
    
    bst.display()
    
    # Insert a specific element and display BST
    new_key = 55
    bst.insert_and_display(new_key)
