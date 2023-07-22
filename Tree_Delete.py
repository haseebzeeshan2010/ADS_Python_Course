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

def delete_node(root, key):
    if root is None:
        return root
    
    if key < root.value:
        root.left = delete_node(root.left, key)
    elif key > root.value:
        root.right = delete_node(root.right, key)
    else:
        # Case 1: Node to be deleted is a leaf node
        if root.left is None and root.right is None:
            root = None
        # Case 2: Node to be deleted has only one child
        elif root.left is None:
            root = root.right
        elif root.right is None:
            root = root.left
        # Case 3: Node to be deleted has two children
        else:
            successor = find_min(root.right)
            root.value = successor.value
            root.right = delete_node(root.right, successor.value)
    
    return root

def find_min(node):
    current = node
    while current.left is not None:
        current = current.left
    return current

# Example usage
root = Node(50)
root.left = Node(30)
root.right = Node(70)
root.left.left = Node(20)
root.left.right = Node(40)
root.right.left = Node(60)
root.right.right = Node(80)

print("Inorder Traversal:")
inorder_traversal(root)
print("\n")

key = 30
root = delete_node(root, key)

print(f"After deleting node with value {key}:")
print("Inorder Traversal:")
inorder_traversal(root)
print("\n")