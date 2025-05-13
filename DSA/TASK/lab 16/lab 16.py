# task 1

# Recursive DFS
def dfs_recursive(graph, node, visited=None):
    if visited is None:
        visited = []
    visited.append(node)
    for neighbor in graph[node]:
        if neighbor not in visited:
            dfs_recursive(graph, neighbor, visited)
    return visited

# Iterative DFS
def dfs_iterative(graph, start):
    visited, stack = [], [start]
    while stack:
        node = stack.pop()
        if node not in visited:
            visited.append(node)
            stack.extend(reversed(graph[node]))  # Reverse for consistent order
    return visited

# BFS using queue
from collections import deque
def bfs(graph, start):
    visited, queue = [], deque([start])
    while queue:
        node = queue.popleft()
        if node not in visited:
            visited.append(node)
            queue.extend(graph[node])
    return visited

# Example Graph
graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': ['F'],
    'F': []
}

print("DFS Recursive:", dfs_recursive(graph, 'A'))
print("DFS Iterative:", dfs_iterative(graph, 'A'))
print("BFS:", bfs(graph, 'A'))


# task 2

import heapq

def dijkstra(graph, start):
    distances = {node: float('inf') for node in graph}
    distances[start] = 0
    min_heap = [(0, start)]

    while min_heap:
        current_distance, current_node = heapq.heappop(min_heap)
        if current_distance > distances[current_node]:
            continue
        for neighbor, weight in graph[current_node].items():
            distance = current_distance + weight
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(min_heap, (distance, neighbor))
    return distances

# Example Weighted Graph
graph_weighted = {
    'A': {'B': 1, 'C': 4},
    'B': {'A': 1, 'C': 2, 'D': 5},
    'C': {'A': 4, 'B': 2, 'D': 1},
    'D': {'B': 5, 'C': 1}
}

print("Dijkstra:", dijkstra(graph_weighted, 'A'))




# task 3

def find(parent, x):
    if parent[x] != x:
        parent[x] = find(parent, parent[x])
    return parent[x]

def union(parent, rank, x, y):
    rootX = find(parent, x)
    rootY = find(parent, y)
    if rootX == rootY:
        return True
    if rank[rootX] < rank[rootY]:
        parent[rootX] = rootY
    else:
        parent[rootY] = rootX
        if rank[rootX] == rank[rootY]:
            rank[rootX] += 1
    return False

def detect_cycle_undirected(graph):
    parent = {}
    rank = {}
    for node in graph:
        parent[node] = node
        rank[node] = 0
    for u in graph:
        for v in graph[u]:
            if u < v:  # Avoid double-checking
                if union(parent, rank, u, v):
                    return True
    return False

# Example Undirected Graph
graph_undirected = {
    'A': ['B', 'C'],
    'B': ['A', 'D'],
    'C': ['A', 'D'],
    'D': ['B', 'C']
}
print("Cycle in Undirected:", detect_cycle_undirected(graph_undirected))
