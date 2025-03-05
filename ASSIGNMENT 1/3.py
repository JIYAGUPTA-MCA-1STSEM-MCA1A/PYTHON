Write a Python program to create a binary tree using array only and display the tree level
wise.

class BinaryTree:
def __init__(self, arr):
self.tree = arr

def level_order_traversal(self):
for value in self.tree:
print(value, end=" ")

# Example usage
arr = [20, 10, 30, 5, 15, 25, 35]
bt = BinaryTree(arr)

print("Level-wise display of the tree:")
bt.level_order_traversal()
