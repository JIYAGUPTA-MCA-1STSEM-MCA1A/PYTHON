Write a Python program to count number of internal node present in a binary tree.

class Node:
def __init__(self, key):
self.left = None
self.right = None
self.value = key

# Function to count internal nodes

def count_internal_nodes(root):
if root is None or (not root.left and not root.right):
return 0
return 1 + count_internal_nodes(root.left) + count_internal_nodes(root.right)

# Example usage
root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)

print("Number of internal nodes:", count_internal_nodes(root))
