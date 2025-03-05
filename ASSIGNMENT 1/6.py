Write a Python program to count number of leaf node present in a binary tree.

class Node:
def __init__(self, key):

self.left = None
self.right = None
self.value = key

# Function to count leaf nodes
def count_leaf_nodes(root):
if root is None:
return 0
if not root.left and not root.right:
return 1
return count_leaf_nodes(root.left) + count_leaf_nodes(root.right)

# Example usage
root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)

print("Number of leaf nodes:", count_leaf_nodes(root))
