# # task 1 BFS without Queue & without Node
# def bfs_without_queue(graph, start):
#     visited=set()
#     to_visit=[start]

#     while to_visit:
#         current=to_visit.pop(0)
#         if current not in visited:
#             print(current)
#             visited.add(current)
#             for neighbor in graph[current]:
#                 if neighbor not in visited:
#                     to_visit.append(neighbor)

#     graph={
#         "A": ["B", "C"],
#         "B": ["D", "E"],
#         "C": ["F"],
#         "D": [],
#         "E": ["F"],
#         "F": []
#     }

#     print("BFS Traversal without Queue & Node:")
#     bfs_without_queue(graph, "A")



# taske 2  BFS with Queue & Node
from collections import deque

class Node:
    def __init__(self, value):
        self.value=value
        self.children=[]

    def add_child(self, child_node):
        self.children.append(child_node)

def bfs_with_queue(start_node):
    visited=set()
    queue=deque([start_node])

    while queue:
        current_node=queue.popleft()
        if current_node not in visited:
            print(current_node.value)
            visited.add(current_node)
            for child in current_node.children:
                if child not in visited:
                    queue.append(child)

root=Node("A")
b=Node("B")
c=Node("C")
d=Node("D")
e=Node("E")
f=Node("F")

root.add_child(b)
root.add_child(c)
b.add_child(d)
b.add_child(e)
c.add_child(f)

print("\nBFS Traversal with Queue & Node:")
bfs_with_queue(root)