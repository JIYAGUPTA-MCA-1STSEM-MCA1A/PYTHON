Write a Python program to count number of node present in a given binary tree using
linked list.

class Node:
def __init__(self, key):
self.left = None
self.right = None
self.value = key

# Function to count nodes in the tree
def count_nodes(root):
if root is None:
return 0
return 1 + count_nodes(root.left) + count_nodes(root.right)

# Example usage
root = Node(1)

root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)

print("Number of nodes in the tree:", count_nodes(root))
