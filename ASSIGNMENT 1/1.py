class Node:
def __init__(self, key):
self.left = None
self.right = None
self.value = key

# Recursive function to insert a new node
def insert(root, key):
if root is None:
return Node(key)
else:
if key < root.value:
root.left = insert(root.left, key)
else:
root.right = insert(root.right, key)
return root

# Level-order traversal (breadth-first)
def level_order_traversal(root):
if root is None:
return

queue = [root]

while queue:
node = queue.pop(0)
print(node.value, end=" ")

if node.left:

queue.append(node.left)
if node.right:
queue.append(node.right)

# Example usage
root = None
values = [20, 10, 30, 5, 15, 25, 35]
for val in values:
root = insert(root, val)

print("Level-wise display of the tree:")
level_order_traversal(root)
