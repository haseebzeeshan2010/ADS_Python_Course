class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def in_order_traversal(node):
    if node is not None:
        in_order_traversal(node.left)
        print(node.data, end=" ")
        in_order_traversal(node.right)

# Create a binary tree
root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)

# Perform in-order traversal
print("In-order traversal:")
in_order_traversal(root)
print()