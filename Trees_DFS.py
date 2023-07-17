class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

# Create the tree
root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)

# Perform Depth-First Search (DFS)
def dfs(node):
    if node:
        print(node.data, end=" ")
        dfs(node.left)
        dfs(node.right)

print("DFS traversal:")
dfs(root)