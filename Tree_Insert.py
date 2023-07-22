class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def inorder_traversal(root):
    if root is not None:
        inorder_traversal(root.left)
        print(root.value, end=" ")
        inorder_traversal(root.right)

def preorder_traversal(root):
    if root is not None:
        print(root.value, end=" ")
        preorder_traversal(root.left)
        preorder_traversal(root.right)

def postorder_traversal(root):
    if root is not None:
        postorder_traversal(root.left)
        postorder_traversal(root.right)
        print(root.value, end=" ")

def insert_node(root, value):
    if root is None:
        return Node(value)
    
    if value < root.value:
        root.left = insert_node(root.left, value)
    else:
        root.right = insert_node(root.right, value)
    
    return root

# Example usage
root = None
root = insert_node(root, 50)
root = insert_node(root, 30)
root = insert_node(root, 20)
root = insert_node(root, 40)
root = insert_node(root, 70)
root = insert_node(root, 60)
root = insert_node(root, 80)

print("Inorder Traversal:")
inorder_traversal(root)
print("\n")

print("Preorder Traversal:")
preorder_traversal(root)
print("\n")

print("Postorder Traversal:")
postorder_traversal(root)
print("\n")