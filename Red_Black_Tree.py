class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None
        self.parent = None
        self.color = 1

class RedBlackTree:
    def __init__(self):
        self.nil = Node(None)
        self.root = self.nil

    def insert(self, key):
        node = Node(key)
        node.left = self.nil
        node.right = self.nil
        node.parent = self.nil

        current = self.root
        parent = None

        while current != self.nil:
            parent = current
            if node.key < current.key:
                current = current.left
            else:
                current = current.right

        node.parent = parent

        if parent == None:
            self.root = node
        elif node.key < parent.key:
            parent.left = node
        else:
            parent.right = node

        node.color = 0
        self.insert_fixup(node)

    def insert_fixup(self, node):
        while node.parent.color == 0:
            if node.parent == node.parent.parent.left:
                uncle = node.parent.parent.right

                if uncle.color == 0:
                    node.parent.color = 1
                    uncle.color = 1
                    node.parent.parent.color = 0
                    node = node.parent.parent
                else:
                    if node == node.parent.right:
                        node = node.parent
                        self.left_rotate(node)
                    node.parent.color = 1
                    node.parent.parent.color = 0
                    self.right_rotate(node.parent.parent)
            else:
                uncle = node.parent.parent.left

                if uncle.color == 0:
                    node.parent.color = 1
                    uncle.color = 1
                    node.parent.parent.color = 0
                    node = node.parent.parent
                else:
                    if node == node.parent.left:
                        node = node.parent
                        self.right_rotate(node)
                    node.parent.color = 1
                    node.parent.parent.color = 0
                    self.left_rotate(node.parent.parent)

        self.root.color = 1

    def left_rotate(self, node):
        y = node.right
        node.right = y.left

        if y.left != self.nil:
            y.left.parent = node

        y.parent = node.parent

        if node.parent == None:
            self.root = y
        elif node == node.parent.left:
            node.parent.left = y
        else:
            node.parent.right = y

        y.left = node
        node.parent = y

    def right_rotate(self, node):
        y = node.left
        node.left = y.right

        if y.right != self.nil:
            y.right.parent = node

        y.parent = node.parent

        if node.parent == None:
            self.root = y
        elif node == node.parent.right:
            node.parent.right = y
        else:
            node.parent.left = y

        y.right = node
        node.parent = y

    def inorder_traversal(self, node):
        if node != self.nil:
            self.inorder_traversal(node.left)
            print(node.key, end=" ")
            self.inorder_traversal(node.right)

# Example usage
tree = RedBlackTree()
tree.insert(10)
tree.insert(20)
tree.insert(30)
tree.insert(40)
tree.insert(50)

tree.inorder_traversal(tree.root)