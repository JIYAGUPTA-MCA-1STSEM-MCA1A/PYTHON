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
    
    def inorder_traversal(self):
        stack = []
        current = self.root
        sorted_numbers = []
        while True:
            if current is not None:
                stack.append(current)
                current = current.left
            elif stack:
                current = stack.pop()
                sorted_numbers.append(current.key)
                current = current.right
            else:
                break
        return sorted_numbers
    
    def display(self):
        print("Sorted Sequence of Numbers:")
        print(self.inorder_traversal())

# Main function to process user input
if __name__ == "__main__":
    bst = BST()
    numbers = list(map(int, input("Enter a set of integers separated by spaces: ").split()))
    
    for num in numbers:
        bst.insert(num)
    
    bst.display()
