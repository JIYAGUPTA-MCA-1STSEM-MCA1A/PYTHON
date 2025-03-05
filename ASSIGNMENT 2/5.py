Write a Python program to take user name as input and display the sorted sequence of characters  using BST. 
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
    
    def display(self):
        print("Sorted Sequence of Characters:")
        self.inorder_traversal()

# Main function to process user input
if __name__ == "__main__":
    bst = BST()
    user_name = input("Enter your name: ")
    
    for char in user_name:
        bst.insert(char)
    
    bst.display()
