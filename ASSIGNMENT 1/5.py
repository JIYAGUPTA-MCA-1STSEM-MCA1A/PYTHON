Write a Python program to identify degree of a given node.

class Node:
def __init__(self, key):
self.left = None
self.right = None
self.value = key

# Function to calculate the degree of a node
def degree(node):
degree = 0
if node.left:
degree += 1
if node.right:
degree += 1
return degree

# Example usage
root = Node(1)
root.left = Node(2)
root.right = Node(3)

print("Degree of root node:", degree(root))
print("Degree of left child:", degree(root.left))
