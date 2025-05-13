# taske 1

class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, value):
        def _insert(root, value):
            if not root:
                return Node(value)
            if value < root.value:
                root.left = _insert(root.left, value)
            else:
                root.right = _insert(root.right, value)
            return root
        self.root = _insert(self.root, value)

    def search(self, value):
        def _search(root, value):
            if not root or root.value == value:
                return root is not None
            if value < root.value:
                return _search(root.left, value)
            return _search(root.right, value)
        return _search(self.root, value)

    def delete(self, value):
        def _min_value_node(node):
            current = node
            while current.left:
                current = current.left
            return current

        def _delete(root, value):
            if not root:
                return root
            if value < root.value:
                root.left = _delete(root.left, value)
            elif value > root.value:
                root.right = _delete(root.right, value)
            else:
                if not root.left:
                    return root.right
                elif not root.right:
                    return root.left
                temp = _min_value_node(root.right)
                root.value = temp.value
                root.right = _delete(root.right, temp.value)
            return root
        self.root = _delete(self.root, value)

    def inorder_traversal(self):
        def _inorder(root):
            return _inorder(root.left) + [root.value] + _inorder(root.right) if root else []
        return _inorder(self.root)

# Test
bst = BinarySearchTree()
for num in [50, 30, 70, 20, 40, 60, 80]:
    bst.insert(num)
print("Inorder:", bst.inorder_traversal())
print("Search 60:", bst.search(60))
print("Search 100:", bst.search(100))
bst.delete(20)
bst.delete(30)
bst.delete(50)
print("Inorder after deletion:", bst.inorder_traversal())


# task 2

class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, value):
        def _insert(root, value):
            if not root:
                return Node(value)
            if value < root.value:
                root.left = _insert(root.left, value)
            else:
                root.right = _insert(root.right, value)
            return root
        self.root = _insert(self.root, value)

    def find_lca(self, root, n1, n2):
        if not root:
            return None
        if n1 < root.value and n2 < root.value:
            return self.find_lca(root.left, n1, n2)
        if n1 > root.value and n2 > root.value:
            return self.find_lca(root.right, n1, n2)
        return root

# Test
bst = BinarySearchTree()
for val in [20, 10, 30, 5, 15, 25, 35]:
    bst.insert(val)

print("LCA(5, 15):", bst.find_lca(bst.root, 5, 15).value)   # 10
print("LCA(5, 25):", bst.find_lca(bst.root, 5, 25).value)   # 20
print("LCA(25, 35):", bst.find_lca(bst.root, 25, 35).value) # 30


# task 3

class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def is_balanced(root):
    def check_height(node):
        if not node:
            return 0, True
        left_height, left_balanced = check_height(node.left)
        right_height, right_balanced = check_height(node.right)

        current_height = 1 + max(left_height, right_height)
        balanced = (
            left_balanced and right_balanced and
            abs(left_height - right_height) <= 1
        )
        return current_height, balanced

    _, balanced = check_height(root)
    return balanced
# test cases

# Balanced Tree
root1 = Node(10)
root1.left = Node(5)
root1.right = Node(15)
root1.left.left = Node(2)
root1.left.right = Node(7)
root1.right.left = Node(12)
root1.right.right = Node(20)

print("Tree 1 is balanced:", is_balanced(root1))  # True

# Unbalanced Tree
root2 = Node(10)
root2.left = Node(5)
root2.left.left = Node(2)

print("Tree 2 is balanced:", is_balanced(root2))  # False

