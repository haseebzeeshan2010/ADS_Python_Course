class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def pre_order_traversal(node):
    if node is not None:
        print(node.data, end=" ")
        pre_order_traversal(node.left)
        pre_order_traversal(node.right)

# Create a binary tree
root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)

# Perform pre-order traversal
print("Pre-order traversal:")
pre_order_traversal(root)
print()