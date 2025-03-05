Write a Python program to identify the height of a binary tree.
  
class Node:
def __init__(self, key):
self.left = None
self.right = None
self.value = key

# Function to calculate the height of the tree
def height(root):
if root is None:
return 0
else:
left_height = height(root.left)
right_height = height(root.right)
return max(left_height, right_height) + 1

# Example usage
root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)

print("Height of the tree:", height(root))


