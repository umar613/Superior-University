# taske 1

class Graph:
    def __init__(self, vertices, representation="list"):
        self.vertices = vertices
        self.representation = representation
        
        if self.representation == "list":
            # Adjacency list representation: Dictionary of lists
            self.graph = {i: [] for i in range(vertices)}
        elif self.representation == "matrix":
            # Adjacency matrix representation: 2D List (matrix)
            self.graph = [[0] * vertices for _ in range(vertices)]
    
    def add_edge(self, v1, v2):
        if self.representation == "list":
            # Add edge in adjacency list (undirected graph example)
            self.graph[v1].append(v2)
            self.graph[v2].append(v1)  # Since it's undirected
        elif self.representation == "matrix":
            # Add edge in adjacency matrix (undirected graph example)
            self.graph[v1][v2] = 1
            self.graph[v2][v1] = 1  # Since it's undirected
    
    def remove_edge(self, v1, v2):
        if self.representation == "list":
            # Remove edge in adjacency list (undirected graph example)
            if v2 in self.graph[v1]:
                self.graph[v1].remove(v2)
            if v1 in self.graph[v2]:
                self.graph[v2].remove(v1)
        elif self.representation == "matrix":
            # Remove edge in adjacency matrix (undirected graph example)
            self.graph[v1][v2] = 0
            self.graph[v2][v1] = 0
    
    def display(self):
        if self.representation == "list":
            # Display adjacency list
            for vertex in self.graph:
                print(f"{vertex}: {self.graph[vertex]}")
        elif self.representation == "matrix":
            # Display adjacency matrix
            for row in self.graph:
                print(row)

# Test cases
print("Adjacency List Representation:")
g1 = Graph(5, "list")
g1.add_edge(0, 1)
g1.add_edge(0, 2)
g1.add_edge(1, 3)
g1.add_edge(2, 4)
g1.display()

print("\nAdjacency Matrix Representation:")
g2 = Graph(5, "matrix")
g2.add_edge(0, 1)
g2.add_edge(0, 2)
g2.add_edge(1, 3)
g2.add_edge(2, 4)
g2.display()
  

# taske 2

from collections import deque

class Graph:
    def __init__(self, vertices, representation="list"):
        self.vertices = vertices
        self.representation = representation
        if self.representation == "list":
            # Adjacency list representation
            self.graph = {i: [] for i in range(vertices)}
        elif self.representation == "matrix":
            # Adjacency matrix representation
            self.graph = [[0] * vertices for _ in range(vertices)]

    def add_edge(self, v1, v2):
        if self.representation == "list":
            self.graph[v1].append(v2)
            self.graph[v2].append(v1)  # For undirected graph
        elif self.representation == "matrix":
            self.graph[v1][v2] = 1
            self.graph[v2][v1] = 1  # For undirected graph
    
    def remove_edge(self, v1, v2):
        if self.representation == "list":
            if v2 in self.graph[v1]:
                self.graph[v1].remove(v2)
            if v1 in self.graph[v2]:
                self.graph[v2].remove(v1)
        elif self.representation == "matrix":
            self.graph[v1][v2] = 0
            self.graph[v2][v1] = 0
    
    def display(self):
        if self.representation == "list":
            for vertex in self.graph:
                print(f"{vertex}: {self.graph[vertex]}")
        elif self.representation == "matrix":
            for row in self.graph:
                print(row)
    
    def bfs(self, start):
        visited = [False] * self.vertices
        queue = deque([start])
        visited[start] = True
        traversal = []
        
        while queue:
            node = queue.popleft()
            traversal.append(node)
            
            for neighbor in self.graph[node]:
                if not visited[neighbor]:
                    queue.append(neighbor)
                    visited[neighbor] = True
        
        return traversal
    
    def dfs(self, start):
        visited = [False] * self.vertices
        traversal = []
        
        def dfs_helper(v):
            visited[v] = True
            traversal.append(v)
            
            for neighbor in self.graph[v]:
                if not visited[neighbor]:
                    dfs_helper(neighbor)
        
        dfs_helper(start)
        return traversal

# Test the implementation
g = Graph(6, "list")
g.add_edge(0, 1)
g.add_edge(0, 2)
g.add_edge(1, 3)
g.add_edge(1, 4)
g.add_edge(2, 5)

print("BFS traversal starting from node 0:")
print(g.bfs(0))  # Expected output: [0, 1, 2, 3, 4, 5]

print("DFS traversal starting from node 0:")
print(g.dfs(0))  # Expected output: [0, 1, 3, 4, 2, 5] (or similar order)


# task 3

import heapq

def dijkstra(graph, start):
    # Initialize the distances dictionary
    distances = {node: float('inf') for node in graph}
    distances[start] = 0
    
    # Priority queue to store the nodes with the shortest distance so far
    priority_queue = [(0, start)]  # (distance, node)
    
    while priority_queue:
        # Get the node with the smallest distance
        current_distance, current_node = heapq.heappop(priority_queue)
        
        # If the current distance is greater than the recorded one, skip it
        if current_distance > distances[current_node]:
            continue
        
        # Explore the neighbors of the current node
        for neighbor, weight in graph[current_node].items():
            distance = current_distance + weight
            
            # Only consider this new path if it's better
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(priority_queue, (distance, neighbor))
    
    return distances

# Example graph
graph = {
    'A': {'B': 4, 'C': 1},
    'B': {'A': 4, 'C': 2, 'D': 5},
    'C': {'A': 1, 'B': 2, 'D': 8},
    'D': {'B': 5, 'C': 8}
}

# Call Dijkstra's algorithm
print(dijkstra(graph, 'A'))
