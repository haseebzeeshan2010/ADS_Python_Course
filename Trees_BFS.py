from collections import deque

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

# Perform Breadth-First Search (BFS)
def bfs(node):
    if node is None:
        return

    queue = deque()
    queue.append(node)

    while queue:
        current_node = queue.popleft()
        print(current_node.data, end=" ")

        if current_node.left:
            queue.append(current_node.left)

        if current_node.right:
            queue.append(current_node.right)

print("BFS traversal:")
bfs(root)