# # task 1  DFS with Stack & Node
# class Node:
#     def __init__(self, value):
#         self.value=value
#         self.children=[]

#     def add_child(self, child_node):
#         self.children.append(child_node)

# def dfs_with_stack(start_node):
#     stack=[start_node]
#     visited=set()

#     while stack:
#         current_node=stack.pop()
#         if current_node not in visited:
#             print(current_node.value)
#             visited.add(current_node)
    
#             for child in reversed(current_node.children):
#                 stack.append(child)

# root=Node("A")
# b=Node("B")
# c=Node("C")
# d=Node("D")
# e=Node("E")
# f=Node("F")

# root.add_child(b)
# root.add_child(c)
# b.add_child(d)
# b.add_child(e)
# c.add_child(f)

# print("DFS Traversal using Stack:")
# dfs_with_stack(root)



# task 2 Inorder, Preorder, Postorder Traversal
class TreeNode:
    def __init__(self, value):
        self.value=value
        self.left=None
        self.right=None

def preorder_traversal(node):
    if node:
        print(node.value)
        preorder_traversal(node.left)
        preorder_traversal(node.right)

def inorder_traversal(node):
    if node:
        inorder_traversal(node.left)
        print(node.value)
        inorder_traversal(node.right)

def postorder_traversal(node):
    if node:
        postorder_traversal(node.left)
        postorder_traversal(node.right)
        print(node.value)

root=TreeNode("A")
root.left=TreeNode("B")
root.right=TreeNode("C")
root.left.left=TreeNode("D")
root.left.right=TreeNode("E")
root.right.left=TreeNode("F")
root.right.right=TreeNode("G")

print("Preorder Traversal:")
preorder_traversal(root)
print("\nInorder Traversal:")
inorder_traversal(root)
print("\nPostorder Traversal:")
postorder_traversal(root)