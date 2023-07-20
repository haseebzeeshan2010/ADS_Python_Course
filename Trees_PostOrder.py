# Define the Node class
class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

# Function to perform post-order traversal
def post_order_traversal(node):
    if node is None:
        return
    
    # Recursively traverse the left subtree
    post_order_traversal(node.left)
    
    # Recursively traverse the right subtree
    post_order_traversal(node.right)
    
    # Print the data of the current node
    print(node.data, end=" ")

# Create a binary tree
root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)

# Perform post-order traversal
print("Post-order traversal:")
post_order_traversal(root)
print()