class Node:
def __init__(self, key):
self.left = None
self.right = None
self.value = key

# Non-recursive insert using a queue
def insert_non_recursive(root, key):
new_node = Node(key)
if root is None:
return new_node

queue = [root]

while queue:
node = queue.pop(0)

if not node.left:
node.left = new_node
return root
else:
queue.append(node.left)

if not node.right:
node.right = new_node
return root
else:
queue.append(node.right)

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
root = insert_non_recursive(root, val)

print("Level-wise display of the tree:")
level_order_traversal(root)
