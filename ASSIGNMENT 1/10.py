Write a Python program to count number of siblings present in a binary tree.

class Node:
def __init__(self, key):
self.left = None
self.right = None
self.value = key

# Function to count siblings of a given node
def count_siblings(root, key):
if root is None:
return 0
if root.left and root.left.value == key:
return 1 if root.right else 0

if root.right and root.right.value == key:
return 1 if root.left else 0
return count_siblings(root.left, key) + count_siblings(root.right, key)

# Example usage
root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)

key = 4
print(f"Number of siblings of node {key}:", count_siblings(root,key))
